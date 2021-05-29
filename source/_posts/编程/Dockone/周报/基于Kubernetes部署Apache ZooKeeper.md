
---
title: '基于Kubernetes部署Apache ZooKeeper'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/bc0c6281346ddd1832e8b3bdcd3da048.png'
author: Dockone
comments: false
date: 2021-05-29 08:48:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/bc0c6281346ddd1832e8b3bdcd3da048.png'
---

<div>   
<br>随着云原生化流行的大趋势，我们的基础组件也需要逐渐上Kubernetes了。Apache ZooKeeper作为目前最流行的分布式协调组件，在我们的微服务架构中负责扮演注册中心的角色。在Kubernetes中运行ZooKeeper集群是很有意义的，可以利用其原生的弹性扩缩容、高可用特性。<br>
<h3>使用StatefulSet部署ZooKeeper</h3>官方提供了使用StatefulSet的方式来部署ZooKeeper<a href="https://kubernetes.io/zh/docs/tutorials/stateful-application/zookeeper/">运行ZooKeeper</a>，它会创建一个headless service，一个cluster service，一个podDisruptionBudget，一个StatefulSet。<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: zk-hs<br>
labels:<br>
app: zk<br>
spec:<br>
ports:<br>
- port: 2888<br>
name: server<br>
- port: 3888<br>
name: leader-election<br>
clusterIP: None<br>
selector:<br>
app: zk<br>
---<br>
apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: zk-cs<br>
labels:<br>
app: zk<br>
spec:<br>
ports:<br>
- port: 2181<br>
name: client<br>
selector:<br>
app: zk<br>
---<br>
apiVersion: policy/v1beta1<br>
kind: PodDisruptionBudget<br>
metadata:<br>
name: zk-pdb<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: zk<br>
maxUnavailable: 1<br>
---<br>
apiVersion: apps/v1<br>
kind: StatefulSet<br>
metadata:<br>
name: zk<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: zk<br>
serviceName: zk-hs<br>
replicas: 3<br>
updateStrategy:<br>
type: RollingUpdate<br>
podManagementPolicy: OrderedReady<br>
template:<br>
metadata:<br>
  labels:<br>
    app: zk<br>
spec:<br>
  affinity:<br>
    podAntiAffinity:<br>
      requiredDuringSchedulingIgnoredDuringExecution:<br>
        - labelSelector:<br>
            matchExpressions:<br>
              - key: "app"<br>
                operator: In<br>
                values:<br>
                - zk<br>
          topologyKey: "kubernetes.io/hostname"<br>
  containers:<br>
  - name: kubernetes-zookeeper<br>
    imagePullPolicy: Always<br>
    image: "k8s.gcr.io/kubernetes-zookeeper:1.0-3.4.10"<br>
    resources:<br>
      requests:<br>
        memory: "1Gi"<br>
        cpu: "0.5"<br>
    ports:<br>
    - containerPort: 2181<br>
      name: client<br>
    - containerPort: 2888<br>
      name: server<br>
    - containerPort: 3888<br>
      name: leader-election<br>
    command:<br>
    - sh<br>
    - -c<br>
    - "start-zookeeper \<br>
      --servers=3 \<br>
      --data_dir=/var/lib/zookeeper/data \<br>
      --data_log_dir=/var/lib/zookeeper/data/log \<br>
      --conf_dir=/opt/zookeeper/conf \<br>
      --client_port=2181 \<br>
      --election_port=3888 \<br>
      --server_port=2888 \<br>
      --tick_time=2000 \<br>
      --init_limit=10 \<br>
      --sync_limit=5 \<br>
      --heap=512M \<br>
      --max_client_cnxns=60 \<br>
      --snap_retain_count=3 \<br>
      --purge_interval=12 \<br>
      --max_session_timeout=40000 \<br>
      --min_session_timeout=4000 \<br>
      --log_level=INFO"<br>
    readinessProbe:<br>
      exec:<br>
        command:<br>
        - sh<br>
        - -c<br>
        - "zookeeper-ready 2181"<br>
      initialDelaySeconds: 10<br>
      timeoutSeconds: 5<br>
    livenessProbe:<br>
      exec:<br>
        command:<br>
        - sh<br>
        - -c<br>
        - "zookeeper-ready 2181"<br>
      initialDelaySeconds: 10<br>
      timeoutSeconds: 5<br>
    volumeMounts:<br>
    - name: datadir<br>
      mountPath: /var/lib/zookeeper<br>
  securityContext:<br>
    runAsUser: 1000<br>
    fsGroup: 1000<br>
volumeClaimTemplates:<br>
- metadata:<br>
  name: datadir<br>
spec:<br>
  accessModes: [ "ReadWriteOnce" ]<br>
  resources:<br>
    requests:<br>
      storage: 10Gi<br>
</pre><br>
使用<code class="prettyprint">kubectl apply</code>应用这个配置文件，等待一会之后，发现Pod和Service都已创建成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/bc0c6281346ddd1832e8b3bdcd3da048.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/bc0c6281346ddd1832e8b3bdcd3da048.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们检查一下ZooKeeper节点的状态：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/f50f43624769478e1f4ea4d9634bae03.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/f50f43624769478e1f4ea4d9634bae03.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
将ZooKeeper部署在Kubernetes上一大优点就是可以方便扩缩容，这边我们以扩容成4个节点为例，<code class="prettyprint">kubectl edit sts zk</code>，修改<code class="prettyprint">replica:4</code>以及<code class="prettyprint">--server=4</code>。可以看到经过一段时间的滚动更新，最终扩容成了4个节点。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/cdd12f8b1fb948ec83fda422dce71127.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/cdd12f8b1fb948ec83fda422dce71127.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>使用Kubernetes Operator部署ZooKeeper</h3>除了StatefulSet的方式外，我们还可以使用Kubernetes Operator的方式部署。目前我们可以参考使用<a href="https://github.com/pravega/zookeeper-operator">pravega</a>提供的Operator。<br>
<br>首先创建自定义的crd ZookeeperCluster：<br>
<pre class="prettyprint">kubectl create -f deploy/crds<br>
</pre><br>
接着创建权限相关的，包括serviceAccount、Role和RoleBinding（注意需要修改一下权限相关的rbac.yaml的配置，如果你当前的namespace不是default，需要把namespcae: default去掉，不然权限验证有问题）。<br>
<pre class="prettyprint">kubectl create -f deploy/default_ns/rbac.yaml<br>
</pre><br>
然后给Operator创建deployment：<br>
<pre class="prettyprint">kubectl create -f deploy/default_ns/operator.yaml<br>
</pre><br>
我们看到Operator已经创建好了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/531299ecab19bdff410c952ba38fe39a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/531299ecab19bdff410c952ba38fe39a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接下来我们自己编写一个CR即可：<br>
<pre class="prettyprint">apiVersion: zookeeper.pravega.io/v1beta1<br>
kind: ZookeeperCluster<br>
metadata:<br>
name: zookeeper<br>
spec:<br>
replicas: 3<br>
image:<br>
repository: pravega/zookeeper<br>
tag: 0.2.9<br>
storageType: persistence<br>
persistence:<br>
reclaimPolicy: Delete<br>
spec:<br>
  storageClassName: "rbd"<br>
  resources:<br>
    requests:<br>
      storage: 8Gi<br>
</pre><br>
这里的storageClassName配合自建集群选择了rbd。apply之后等一会儿可以看到zk已经创建完毕。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/94f88248961ee39bc9180ac953a5abfd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/94f88248961ee39bc9180ac953a5abfd.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
扩缩容的话也非常方便，还是以扩容4节点为例，直接patch我们创建的CR即可：<br>
<pre class="prettyprint">kubectl patch zk zookeeper --type='json' -p='[&#123;"op": "replace", "path": "/spec/replicas", "value":4&#125;]'<br>
</pre><br>
<h3>使用Kubernetes Kudo部署ZooKeeper</h3><a href="https://kudo.dev/">kudo</a>是一个适用于Kubernetes Operator的组装器，也是官方推荐的。<br>
<br>首先我们安装一下kudo，在Mac上安装：<br>
<pre class="prettyprint">brew install kudo<br>
</pre><br>
安装完之后进行初始化：<br>
<pre class="prettyprint">kubectl kudo init<br>
</pre><br>
这个时候我们会发现kudo operator已经装好了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/9769c4d2d74e2c7d01841a018280d02c.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/9769c4d2d74e2c7d01841a018280d02c.jpeg" class="img-polaroid" title="6.jpeg" alt="6.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后直接安装一下ZooKeeper即可（kudo内置了ZooKeeper Operator），注意这里同样声明一下storage class为RDB。<br>
<pre class="prettyprint">kubectl kudo install zookeeper --instance=zookeeper-instance -p STORAGE_CLASS=rbd<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210527/237b940c7c505ee4abc6c914255e0a61.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210527/237b940c7c505ee4abc6c914255e0a61.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
扩缩容的话也非常方便：<br>
<pre class="prettyprint">kubectl kudo update --instance=zookeeper-instance -p NODE_COUNT=4<br>
</pre><br>
<br>原文链接：<a href="https://fredal.xin/deploy-zk-with-k8s" rel="nofollow" target="_blank">https://fredal.xin/deploy-zk-with-k8s</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            