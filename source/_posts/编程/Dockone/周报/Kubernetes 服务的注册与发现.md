
---
title: 'Kubernetes 服务的注册与发现'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/4a17d5fc8eb12ec11d6d6363ed563be7.png'
author: Dockone
comments: false
date: 2021-08-21 10:07:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/4a17d5fc8eb12ec11d6d6363ed563be7.png'
---

<div>   
<br>本文是 Kubernetes 比较核心且抽象的部分，但会采用通俗易懂的方式来讲<br>
<h3>1、Pod 相关核心结构</h3><h4>1.1、Pod 结构</h4><ul><li>Pod 相当于一个容器，Pod 有独立的 IP 地址，也有自己的 hostname，利用 namespace 进行资源隔离，相当于一个独立沙箱环境。</li><li>Pod 内部封装的是容器，可以封装一个，或者多个容器（通常是一组相关的容器）</li></ul><br>
<br><h4>1.2、Pod 网络</h4><ul><li>Pod 有自己独立的 IP 地址</li><li>Pod 内部的容器之间是通过 localhost 进行访问</li></ul><br>
<br><h3>2、Pod 如何对外提供访问</h3>首先 Pod 有自己的 IP 和 hostname，但 Pod 是虚拟的资源对象（在计算机中表现为进程），没有对应实体（物理机，物理网卡）与之对应，所以是无法直接对外提供服务访问的。<br>
<br>因此如果 Pod 想对外提供服务，必须绑定物理机端口（即在物理机上开启端口，让这个端口和 Pod 的端口进行映射），这样就可以通过物理机进行数据包的转发。<br>
<br>下面以一台 Linux 系统的机器为例子（Logstash 是做日志收集用的）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/4a17d5fc8eb12ec11d6d6363ed563be7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/4a17d5fc8eb12ec11d6d6363ed563be7.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>3、Pod 的负载均衡</h3>很关键的一个问题：一组相关的 Pod 副本，如何实现访问负载均衡？就如当请求达到，请求转发给哪个 Pod 比较好？<br>
<br>一个想法就是用 Pod 再部署一个 Nginx。<br>
<br>举例：如下图，注意下图右边的 Node 里面有两个是 支付 服务，与订单服务的是不同类型的 pod。如果一个请求订单的服务发来上面那个 Nginx，那这个 Pod 可以有 4 条转发路线，可以想到用 hash 呀什么的把不同请求映射到不同的 Pod 去转发。但能不能这么做呢？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/620b5803da4cce71d288a966bdeb042c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/620b5803da4cce71d288a966bdeb042c.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
思考：Pod 是一个进程，是有生命周期的，一旦宕机、版本更新都会创建新的 Pod（IP 地址会变化，hostname 会变化），此时再使用 Nginx 做负载均衡不太合适，因为它不知道 Pod 发生了改变，那请求就不能被接受了。所以服务发生了变化它根本不知道，Nginx 无法发现服务，不能用 Nginx 做负载均衡。那该如何实现呢？使用 Service 资源对象。<br>
<h4>3.1、什么是 Service 资源对象</h4><ul><li>Pod IP：Pod 的 IP 地址</li><li>Node IP：物理机的 IP 地址</li><li>Cluster IP：虚拟 IP，是由 Kubernetes 抽象出的 Service 对象，这个 Service 对象就是一个 VIP（virtual IP，VIP）的资源对象</li></ul><br>
<br><h4>3.2、Service 如何实现负载均衡</h4>例如现在要负载均衡地访问一组相同的服务副本——订单，这时就要去做一个 Service，对外表现出是一个进程或资源对象，有虚拟的 IP（VIP）和端口。请求会访问 Service，然后 Service 自己会负载均衡地发送给相应服务的 Pod，也就是下图中 4 个相同的 Pod。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/bdfcbee178ce67886b3f2929ddc77630.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/bdfcbee178ce67886b3f2929ddc77630.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>3.3、深入 Service VIP</h4><ul><li>Service 和 Pod 都是一个进程，都是虚拟的，因此实际上 Service 也不能对外网提供服务</li><li>Service 和 Pod 之间可以直接进行通信，它们的通信属于局域网通信</li><li>负载策略：把请求交给 Service 后，Service 使用 iptables，ipvs 来实现数据包的分发</li></ul><br>
<br>而要对外网提供服务，首先需要和之前一样 在物理机上也绑定一个端口 来接受访问请求，然后把请求转发给 Service，Service 再把数据包分发给相应的 Pod。访问流程如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/a47e429f6dc129aa3bc3e2e6aa711022.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/a47e429f6dc129aa3bc3e2e6aa711022.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
思考1：那 Service 对象是如何和 Pod 进行关联的呢？<br>
<br>它们之间的关联利用的 还是标签选择器 selector。且 service 只能对 一组相同的副本 提供服务，不能跨组提供服务。如果有另一组，需要再创建一个 service。因此不同的业务会有不同的 service。<br>
<br>举例：service 和一组 Pod 副本是通过标签选择器进行关联的，相同的副本的标签是一样的。<br>
<br>selector：app = x 选择一组订单的服务的 Pod，创建一个 service；app = y 选择了一组支付的服务的 Pod。通过一个 endpoints 属性存储这组 Pod 的 IP 地址，这样就有了映射关系了（关联起来）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/a096c0e75408a59a8a90e3c1862856fc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/a096c0e75408a59a8a90e3c1862856fc.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
思考2：Pod 宕机或发布新版本了，Service 是如何发现 Pod 已经发生变化的？<br>
<br>通过 Kubernetes 中的一个组件 —— kube-proxy，每个 Node 里都运行着这个服务。它需要做的工作如下图右侧：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/61af762ffdc49b74d3f66378a12fde58.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/61af762ffdc49b74d3f66378a12fde58.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Service 实现服务的发现：kube-proxy 监控 Pod，一旦发现 Pod 服务变化，将会把新的 IP 地址更新到 service。<br>
<br>注意：endpoints 那些都是存储在 etcd 里的，所以 kube-proxy 更新的存储在 etcd 里的映射关系。<br>
<br>原文链接：<a href="https://blog.csdn.net/qq_43280818/article/details/107164860" rel="nofollow" target="_blank">https://blog.csdn.net/qq_43280 ... 64860</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            