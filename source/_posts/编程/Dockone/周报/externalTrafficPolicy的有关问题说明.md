
---
title: 'externalTrafficPolicy的有关问题说明'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/2342f55261dfb850bd154d60a45ae2da.png'
author: Dockone
comments: false
date: 2021-09-12 14:06:25
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/2342f55261dfb850bd154d60a45ae2da.png'
---

<div>   
<br><h3>环境描述</h3>生产环境通过gitlab-running实现自动化发布业务，现需要收集客户端的真实IP，需要将externalTrafficPolicy改为Local模式（原来是Cluster模式），前天开发反映无法发布业务（镜像拉取不成功）。想到就改动过externalTrafficPolicy所以考虑到了Local模式和Cluster模式的区别。<br>
<h3>externalTrafficPolicy作用阐述</h3>把集群外部的服务引入到集群内部来，在集群内部直接使用。没有任何类型代理被创建，这只有Kubernetes 1.7或更高版本的kube-dns才支持【当我们的集群服务需要访问Kubernetes之外的集群时，可以选择这种类型，然后把外部服务的IP及端口写入到Kubernetes服务中来，Kubernetes的代理将会帮助我们访问到外部的集群服务】<br>
<h3>什么是externalTrafficPolicy</h3>在Kubernetes的Service对象（申明一条访问通道）中，有一个“externalTrafficPolicy”字段可以设置。有2个值可以设置：Cluster或者Local。<br>
<ul><li>Cluster表示：流量可以转发到其他节点上的Pod。</li><li>Local表示：流量只发给本机的Pod。</li></ul><br>
<br>图示一下：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210910/2342f55261dfb850bd154d60a45ae2da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/2342f55261dfb850bd154d60a45ae2da.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>这2种模式有什么区别</h3>存在这2种模式的原因就是，当前节点的Kube-proxy在转发报文的时候，会不会保留原始访问者的IP。<br>
<h4>选择Cluster</h4>注：这个是默认模式，Kube-proxy不管容器实例在哪，公平转发。<br>
<br>Kube-proxy转发时会替换掉报文的源IP。即：容器收的报文，源IP地址，已经被替换为上一个转发节点的了。<br><br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210910/60b4cfa59a93e8bd68a4ba2a19d08013.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/60b4cfa59a93e8bd68a4ba2a19d08013.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原因是Kube-proxy在做转发的时候，会做一次SNAT（source network address translation），所以源IP变成了节点1的IP地址。<br>
<br>PS：SNAT确保回去的报文可以原路返回，不然回去的路径不一样，客户会认为非法报文的。（我发给张三的，怎么李四给我回应？丢弃！）<br>
<br>这种模式好处是负载均衡会比较好，因为无论容器实例怎么分布在多个节点上，它都会转发过去。当然，由于多了一次转发，性能会损失一丢丢。<br>
<h4>选择Local</h4>这种情况下，只转发给本机的容器，绝不跨节点转发。<br>
<br>Kube-proxy转发时会保留源IP。即：容器收到的报文，看到源IP地址还是用户的。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210910/b282ea4e033b92f840fa4e67457a4e0e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/b282ea4e033b92f840fa4e67457a4e0e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
缺点是负载均衡可能不是很好，因为一旦容器实例分布在多个节点上，它只转发给本机，不跨节点转发流量。当然，少了一次转发，性能会相对好一丢丢。<br>
<br>注：这种模式下的Service类型只能为外部流量，即：LoadBalancer 或者 NodePort 两种，否则会报错。<br>
<br>同时，由于本机不会跨节点转发报文，所以要想所有节点上的容器有负载均衡，就需要上一级的LoadBalancer来做了。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210910/25470f583337f4336c3dc8b04beb9e4a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/25470f583337f4336c3dc8b04beb9e4a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
不过流量还是会不太均衡，如上图，LoadBalancer看到的是2个后端（把节点的IP），每个Node上面几个Pod对LoadBalancer来说是不知道的。<br>
<br>想要解决负载不均衡的问题：可以给Pod容器设置反亲和，让这些容器平均的分布在各个节点上（不要聚在一起）。<br>
<pre class="prettyprint">affinity:<br>
podAntiAffinity:<br>
preferredDuringSchedulingIgnoredDuringExecution:<br>
- weight: 100<br>
  podAffinityTerm:<br>
    labelSelector:<br>
      matchExpressions:<br>
       - key: k8s-app<br>
         operator: In<br>
         values:<br>
         - my-app<br>
    topologyKey: kubernetes.io/hostname<br>
</pre><br>
像下面这样，负载均衡情况就会好很多~<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210910/7de748cac61b7f1b397428ebf9bcab31.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210910/7de748cac61b7f1b397428ebf9bcab31.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>两种模式该怎么选</h3>要想性能（时延）好，当然应该选Local模式喽，毕竟流量转发少一次SNAT嘛。<br>
<br>不过注意，选了这个就得考虑好怎么处理好负载均衡问题（PS：通常我们使用Pod间反亲和来达成）。<br>
<br>如果你是从外部LB接收流量的，那么使用：Local模式 + Pod反亲和，一般是足够的<br>
<h3>总结</h3>同上上述的理论学习，问题可以明确的得出答案：externalTrafficPolicy的Local模式，只转发给本机的容器，绝不跨节点转发，而我司的GitLab是部署在Kubernetes环境的，分散于多节点。<br>
<br>参考文献：<br>
<ol><li><a href="https://www.asykim.com/blog/deep-dive-into-kubernetes-external-traffic-policies" rel="nofollow" target="_blank">https://www.asykim.com/blog/de ... icies</a></li><li><a href="https://bbs.huaweicloud.com/blogs/158642" rel="nofollow" target="_blank">https://bbs.huaweicloud.com/blogs/158642</a></li></ol><br>
<br>原文链接：<a href="https://www.cnblogs.com/zisefeizhu/p/13262239.html" rel="nofollow" target="_blank">https://www.cnblogs.com/zisefeizhu/p/13262239.html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            