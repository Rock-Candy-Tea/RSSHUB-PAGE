
---
title: '认识 Kubernetes 核心组件原理'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/658f86ef6ba0273f08b1c83a4a00a3e7.png'
author: Dockone
comments: false
date: 2021-08-21 05:06:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/658f86ef6ba0273f08b1c83a4a00a3e7.png'
---

<div>   
<br><h3>1、核心组件原理 —— Pod 核心原理</h3><h4>1.1、Pod 是什么</h4><ul><li>Pod 也可以理解是一个容器，装的是 Docker 创建的容器，也就是用来封装容器的一个容器；</li><li>Pod 是一个虚拟化分组， 有自己的 IP 地址和主机名 hostname，利用 namespace 进行资源隔离，相当于一台独立沙箱环境；</li><li>Pod 相当于一台独立主机，内部可以封装一个或多个容器（通常是一组相关的容器），内部容器之间访问采用 localhost。</li></ul><br>
<br><h4>1.2、Pod 用来干什么</h4>通常情况下，在服务部署的时候，使用 Pod 来管理一组相关的服务（一个 Pod 中要么部署一个服务，要么部署一组有关系的服务）。如下图是部署了一组有关系的服务的结构图，其中 C 表示容器（container），下面的 Pod 里就有很多个容器。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/658f86ef6ba0273f08b1c83a4a00a3e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/658f86ef6ba0273f08b1c83a4a00a3e7.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如何理解一组相关的服务？<br>
<br>如下图：有一个请求是访问 Nginx，然后部署了 Nginx 的容器就把请求转发给部署了 Web 服务的容器，Web 再访问数据库，然后请求会依次返回来数据，最后再返回给用户。<br>
<br>因此在 链式调用的调用链路上的服务 叫做一组相关的服务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/75a2385f4ed34b06fe4cce8320af0f3c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/75a2385f4ed34b06fe4cce8320af0f3c.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>1.3、实现 Web 服务集群</h4>只需要复制多个 Pod 的副本即可，这也是 Kubernetes 管理的先进之处。Kubernetes 如果要进行扩容或缩容，只需要控制 Pod 的数量即可。比如上面那个部署模式，服务集群就是复制多个这样的 Pod。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/d8f56dc5b91369b896e73212145ea45e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/d8f56dc5b91369b896e73212145ea45e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>1.4、Pod 底层网络和数据存储是如何进行的</h4>前面说过 Pod 内部的容器也是一个独立的沙箱环境，因此也有自己的 IP 和 端口。如果内部容器还是通过 ip:port 来通信，相当于还是远程访问，这样的话性能会受到一定的影响。如何提高内部容器之间访问的性能呢？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/001ca5e7b4447dc0b0b9468945dd974c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/001ca5e7b4447dc0b0b9468945dd974c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Pod 底层：<br>
<ul><li>Pod 内部容器创建之前，必须先创建 pause 容器。pause 有两个作用：共享网络和共享存储。</li><li>每个服务容器共享 pause 存储，不需要自己存储数据，都交给 pause维护。</li><li>pause 也相当于这三个容器的网卡，因此他们之间的访问可以通过 localhost 方式访问，相当于访问本地服务一样，性能非常高（就像本地几台虚拟机之间可以 ping 通）。</li></ul><br>
<br><h3>2、ReplicaSet 副本控制器</h3><h4>2.1、副本控制器基本理解</h4>作用：管理控制 Pod 副本（服务集群）的数量，以使其永远与预期设定的数量保持一致。<br>
<br>例如：replicas = 3 （创建 3 个副本，这是提前设置好的）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/1fe8955d15be22dd75a698156e211898.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/1fe8955d15be22dd75a698156e211898.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当副本设置为 3 时，副本控制器将会永远保证副本数量为 3。因此当有 Pod 服务宕机时（如上面第 3 个 Pod），那副本控制器会立马重新创建一个新的 Pod，就能够保证副本数量一直为预先设定好的 3 个。<br>
<h4>2.2、ReplicaSet 和 ReplicationController 的区别</h4>ReplicaSet 和 ReplicationController 都是副本控制器，其中：<br>
<br>相同点：都有前面 2.1 节所描述的功能<br>
<br>不同点：标签选择器的功能不同<br>
<br>ReplicaSet 可以使用标签选择器进行 单选 和 复合选择；而 ReplicationController 只支持 单选操作。<br>
<br>什么意思呢？<br>
<br>假设下面有下面两个不同机器上的 Node 结点，如何知道它们的 Pod 其实都是相同的呢？答案是通过标签。<br>
<br>给每个 Pod 打上标签（key=value 格式，如下图中的 app=web, release=stable，这有两个选项，相同的 Pod 副本的标签是一样的），于是副本控制器可以通过标签选择器 seletor 去选择一组相关的服务。<br>
<br>一旦 selector 和 Pod 的标签匹配上了，就表明这个 Pod 是当前这个副本控制器控制的，表明了副本控制器和 Pod 的所属关系。如下图中 seletor 指定了 app = web 和 release=stable 是复合选择，要用 ReplicaSet 才能实现若用 ReplicationController 的话只能选择一个，如只选择匹配 app=web 标签。这样下面的 3 个 Pod 就归这个副本控制器管。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/bbb59f97fa10671a8c78feb3f0a29a76.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/bbb59f97fa10671a8c78feb3f0a29a76.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可见 ReplicaSet 功能更齐全，所以在新版的 Kubernetes 中，建议使用 ReplicaSet 作为副本控制器，不再使用 ReplicationController。<br>
<h3>3、Deployment 部署对象</h3><h4>3.1、滚动更新</h4>ReplicaSet 副本控制器可以永久保持 Pod 副本的数量。但是项目的需求在不断的迭代、更新，项目在不断发版。那如何做到服务更新？难道把服务停掉再把新版本部署上去吗？当然不是，答案是用滚动更新。就是重新创建一个 Pod（v2 版本）来代替之前的 Pod（v1版本）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/683f34a30504d7de06b36fd549f114e1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/683f34a30504d7de06b36fd549f114e1.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
那是如何滚动更新的呢？涉及到下面要讲到的部署模型。<br>
<h4>3.2、部署模型</h4>单独的 ReplicaSet 是不支持滚动更新的，Deployment 对象支持滚动更新，通常和 ReplicaSet 一起使用。<br>
<br>需要滚动更新时的步骤：<br>
<ol><li>Deployment 建立新的 Replicaset</li><li>Replicaset 重新建立新的 Pod</li></ol><br>
<br>所以它们之间是有层次关系的，Deployment 管 Replicaset，Replicaset 维护 Pod。在更新时删除的是旧的 Pod，老版本的 ReplicaSet 是不会删除的，所以在需要时还可以回退以前的状态。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/e858bcc9e98fe2ce7e356372c10d6577.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e858bcc9e98fe2ce7e356372c10d6577.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>4、StatefulSet 部署有状态服务</h3><h4>4.1、引入定义</h4>思考：如果 MySQL（有状态服务）使用容器化部署，会存在什么问题？<br>
<ol><li>容器都是有生命周期的，一旦宕机数据就很可能丢失</li><li>Pod 也有生命周期的，用 Pod 部署时把 Pod 集群副本重启以后也可能会出现数据丢失</li></ol><br>
<br>因此对 Kubernetes 来说，不能使用 Deployment 部署有状态的服务。通常情况下，Deployment 被用来部署无状态服务。<br>
<br>然后 StatefulSet 就是为了解决有状态服务使用容器化部署的一个问题。<br>
<h4>4.2、如何理解状态服务</h4>有状态服务：<br>
<ul><li>有实时的数据需要存储</li><li>在有状态服务集群中，如果把某一个服务抽离出来，一段时间后再加入回集群网络，此后集群网络会无法使用</li></ul><br>
<br>无状态服务：<br>
<ul><li>没有实时的数据需要存储</li><li>在无状态服务集群中，如果把某一个服务抽离出去，一段时间后再加入回集群网络，对集群服务无任何影响，因为它们不需要做交互，不需要数据同步等等。</li></ul><br>
<br><h4>4.3、部署模型</h4>StatefulSet 的部署模型和 Deployment 的很相似。<br>
<br>比如下图，借助 PVC（与存储有关）文件系统来存储的实时数据，因此下图就是一个有状态服务的部署。<br>
<br>在 Pod 宕机之后重新建立 Pod 时，StatefulSet 通过保证 hostname 不发生变化来保证数据不丢失。因此 Pod 就可以通过 hostname 来关联（找到）之前存储的数据。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/a72b36e4ce5d71b272b90bfda3dbf037.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/a72b36e4ce5d71b272b90bfda3dbf037.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://blog.csdn.net/qq_43280818/article/details/106910187" rel="nofollow" target="_blank">https://blog.csdn.net/qq_43280 ... 10187</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            