
---
title: 'Redis Cluster Operator容器化方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/58f908c4a8dda2679cc86d14485bd312.png'
author: Dockone
comments: false
date: 2021-04-13 00:28:27
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/58f908c4a8dda2679cc86d14485bd312.png'
---

<div>   
<br>对于Redis Cluster的容器化，我行已在Redis Paas中做了先期的探索和使用。在Redis Paas中实现了Redis哨兵模式、集群模式的容器化部署，结合IPAAS使得项目可依据自身需要自助申请并实时交付。但是，在Redis Paas使用过程中，出现了Redis Cluster主从Pod被调度在同一节点，Redis Master节点所在的容器发生重启导致数据丢失的问题，而且在功能上难以支持Redis集群扩缩容、主从节点差异化配置、定时持久化等需求。本文针对Redis Cluster容器化遇到的问题进行分析，并讨论使用Operator的解决方案。<br>
<h3>Redis Cluster容器化问题</h3><h4>Redis Cluster主从分布</h4>Redis Cluster从节点除了分担主节点的读压力，也是Redis高可用性重要的一部分。Redis作为一个内存数据库，为了保证高性能不会实时将数据刷盘进行持久化存储，所以Redis节点宕机可能会造成数据丢失。在集群模式中，分片中的从节点不仅可以分担主节点的读压力，而且也具有保证数据完整性的重要作用。所以在容器化部署时，同一分片的主从节点Pod不能调度在同一Kubernetes节点，防止由于Kubernetes节点宕机分片整体下线导致数据丢失。<br>
<br>Kubernets中可以使用Pod反亲和性配置，将同一类型的Pod分散在不同的节点。下面yaml配置定义所有符合Redis标签的Pod以软反亲和性的方式分布部署在不同的节点上。<br>
<pre class="prettyprint">spec:    <br>
affinity:  <br>
podAntiAffinity:  <br>
  preferredDuringSchedulingIgnoredDuringExecution:  <br>
  - podAffinityTerm:  <br>
      labelSelector:  <br>
        matchLabels:  <br>
          REDIS_POD_LABEL: REDIS_POD_VALUE  <br>
      topologyKey: kubernetes.io/hostname  <br>
</pre><br>
先期Redis Paas中，同一项目的所有Redis Pod由一个Statefulset管理，对同一Statefulset中所有Pod配置反亲和性。在实际使用中发现，这种配置方法在项目Redis Pod比较多或者容器平台节点比较少的情景下，会出现同一分片的主从Pod被调度在同一主机节点的情况。在Redis Cluster Operator的设计中，将每一个Redis Cluster每个分片部署成一个Statefulset并在Statefulset内配置Pod反亲和性，这种部署方法能很好的保证Redis Cluster分片主从Pod处于不同节点。<br>
<h4>Redis Master容器快重启</h4>在容器环境中部署的Redis Cluster，数据丢失除了可能发生在主从节点同时下线的情况外，还存在另外一种情景。<br>
<br>Redis Cluster中，Master节点下线必须经过cluster-node-timeout时间才会启动failover机制。在容器环境中，如果主节点所在的容器由于某种原因被杀死，再被Kubernetes自动拉起，这个时间非常短暂以至于集群不会启动failover流程。但在这种情况下，Redis进程下线又上线原先内存中的数据会被全部清空，Slave节点不执行failover流程继续同步Master会导致整个分片数据丢失。该种情况某种意义上可以看作是Kubernetes的高可用机制和Redis Cluster的发生了冲突。在设计Operator方案时，为避免类似情况的发生，我们需要明确Kubernetes、Operator和Redis在整个方案中的作用，划定Kuberentes、Operator和Redis Cluster的功能边界：<br>
<ol><li>Kubernetes和Operator不去介入Redis Cluster的高可用机制，若有冲突以Redis Cluster的为准</li><li>Redis 容器启动和Redis进程启动相分离，Kubernetes只负责为Redis分配资源，Operator监听Redis容器启动情况并在合适的时机启动Redis进程，将Redis加入集群</li></ol><br>
<br>在先前Redis Paas中，Redis进程随容器启动而启动，Redis进程自动读取本地nodes.conf文件重新回到集群。在Operator中，需要监听Redis容器启动，对节点加入集群的时机做把控：<br>
<ul><li>Case 1：分片中有Master节点，则启动容器Redis进程加入集群</li><li>Case 2：分片中无Master节点，但有Slave节点，则等待Redis高可用机制提升Slave为Master，然后依Case 1操作</li><li>Case 3：分片中没有节点。该种情况下，为保持集群的完整性，可以待所有分片包含的容器启动后，根据各容器持久化的nodes.conf文件，选出cluster epoch最大的首先启动其Redis进程，然后其余Redis进程依照前两种情况启动</li></ul><br>
<br>前两种情况可以保证Redis的数据安全，第三种情况由于分片全部下线，若没有在退出时对数据进行持久化保存则无法保证数据完整。除此之外，还有一种极坏的情况——Redis Cluster中存活的Master不足一半，此时Redis Cluster 的failover机制已无法正常运行。此种情况可参照上述第三种情况处理，在该种情况下可能需要执行cluster failover takeover命令才能使集群恢复正常，Operator不做高危险操作，此时由运维人员手工介入处理。<br>
<h4>Redis 服务对外暴露</h4>容器化环境不同于物理环境或者虚拟机环境，容器环境的容器IP不固定，而且容器平台使用overlay网络，网络IP对集群外不可见。在这种情景下，若应用与Redis同集群部署，可以使用为Redis Cluster建立的Service来访问，但是如果有集群外访问的需求，该种方式则不能满足。对此，需要为每个单独的Redis Pod建立NodePort型的Service，并且在Redis中增加如下配置：<br>
<pre class="prettyprint">cluster-announce-port REDIS_SERVICE-NODEPORT  <br>
cluster-announce-bus-port GOSSIP-NODEPORT  <br>
cluster-announce-ip HOSTIP<br>
</pre><br>
<h3>Redis Cluster Operator</h3>Operator的核心是CRD（CustomResourceDefinition）和自定义Controller。在项目中，我们使用Kubebuilder进行Redis Cluster Operator开发，项目整体结构如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/58f908c4a8dda2679cc86d14485bd312.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/58f908c4a8dda2679cc86d14485bd312.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>底层使用Kubebuilder生成的Operator框架，根据资源定义生成CRD模板、并且完成与容器集群交互、监听资源变动等功能。</li><li>左边RedisCluster资源定义部分根据需求定义资源实体</li><li>右边为Controller部分，对资源实例进行解析和操作</li></ul><br>
<br><h4>RedisCluster CRD</h4>建立RedisCluster CRD资源，首先将Redis Cluster的需求进行抽象，如下所示：<br>
<pre class="prettyprint">spec:  <br>
masterSize: 3  <br>
clusterReplicas: 2  <br>
exposeService: true  <br>
image: redis:6.0.4  <br>
dbSize: 4Gi<br>
</pre><br>
该spec描述了部署一个Redis Cluster的基本需求，包含分片数、每个分片从副本数量、是否需要集群外访问、使用的Redis镜像版本和每个Redis节点的最大内存大小。<br>
<br>然后，我们使用CRD将该需求定义扩展到Kubernetes，成为Kubernetes支持的资源：<br>
<pre class="prettyprint">apiVersion: apiextensions.k8s.io/v1beta1  <br>
kind: CustomResourceDefinition  <br>
metadata:  <br>
name: redisclusters.redis.cmbc.com.cn  <br>
spec:  <br>
group: redis.cmbc.com.cn  <br>
version: v1alpha1  <br>
names:  <br>
kind: RedisCluster  <br>
listKind: RedisClusterList  <br>
plural: redisclusters  <br>
singular: rediscluster  <br>
scope: Namespaced<br>
</pre><br>
该yaml文件定义了Kubernetes支持的一个资源，资源的Group是redis.cmbc.com.cn，Version是v1alpha1，Kind是RedisCluster。<br>
<br>接下来就可以使用如下yaml在Kubernetes中创建RedisCluster资源的实例：<br>
<pre class="prettyprint">apiVersion: redis.cmbc.com.cn/v1alpha1  <br>
kind: RedisCluster  <br>
metadata:  <br>
name: demorediscluster  <br>
namespace: redispaas  <br>
spec:  <br>
... <br>
</pre><br>
<h4>RedisCluster Controller</h4>在Kubernetes中注册了种类为RedisCluster的资源后，可以使用kubectl apply/create命令在容器集群中创建RedisCluster的实例。此时，容器集群仅仅做到了“认识”该资源，而对该资源的spec内容的解析和实际的管理需要开发Controller。<br>
<br>Operator的理念是将专业领域知识注入Kubernetes。在Redis Cluster Operator中，Controller通过协调操作Redis和Kubernetes完成Redis集群的创建和维持。如上图所示，Controller部分包含两层：<br>
<ol><li>组件管理层。该部分使用Redis和Kubernetes客户端，分别完成对Redis 集群的管理和对Kubernetes原生资源的操纵，并形成调用接口</li><li>在组件管理层上，根据不同的需求和资源状态，组合调用Redis和Kubernetes管理接口，实现功能需求</li></ol><br>
<br>Controller操作本质上是一个状态机操作，整体操作流程如下所示:<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/6dd3b3d97d951d1fee6b6c52bb0848ad.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/6dd3b3d97d951d1fee6b6c52bb0848ad.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对于一个三分片、每个分片一个Slave的Redis Cluster需求，Controller按照下图部署集群并保持集群状态：<br><br>
<ol><li>每个分片部署一个Statefulset，并配置Pod反亲和性，保证分片主从节点不被调度在同一主机上</li><li>使用Configmap为所有Redis Pod注入配置文件</li><li>使用Secret保存Redis密码</li><li>为某个Redis Cluster建立一个ClusterIP型的Service，集群内通过Service访问</li><li>若有集群外访问需求，则为每个Pod建立NodePort型的Service，集群外通过NodePort进行访问</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210412/fbdcfbaade2a6910095b1d77d64672f6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210412/fbdcfbaade2a6910095b1d77d64672f6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
作者简介：孟玉立，中国民生银行信息科技部开源软件支持组工程师,目前主要负责Kubernetes、Redis的源码研究和工具开发等相关工作。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/UzrLSrjDJV1qpqgAVItoHg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/UzrLSrjDJV1qpqgAVItoHg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            