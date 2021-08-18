
---
title: 'Kubernetes Service 502，IPVS 的坑'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7073'
author: Dockone
comments: false
date: 2021-08-18 12:11:15
thumbnail: 'https://picsum.photos/400/300?random=7073'
---

<div>   
<br>目前部署在 Kubernetes 中的服务，通过 Calico BGP 将 Service 与集群外网络打通，并在外部的 nginx 中配置 Service 地址对外进行服务暴露。经过一段时间的观察，发现在 Deployment 滚动更新中及之后一段时间，偶现服务访问 502 的问题。<br>
<h3>问题背景和现象</h3>当前 Kuberntes 集群使用 Calico 作为 CNI 组件，并使用 BGP 模式将 Pod IP 和 Service IP 与集群外网络打通，通过集群外的 Nginx 作反向代理对外提供服务，应用都是以 Deployment 形式部署。通过一段时间的观察，部分应用反馈，在应用发布后一段时间内，服务有一定几率出现 502 报错。<br>
<h3>问题排查</h3>最直接的猜测，是否问题只发生在滚动更新过程中，即应用没有做好检查检测的配置，导致服务没有真正可用，Pod 却已经处于 ready 状态。<br><br>
简单的测试后很快排除这个可能，对配置了有效健康检查探针的 Deployment 进行滚动更新，并使用 <code class="prettyprint">ab</code> 通过 Nginx 配置的域名进行持续请求（此时无并发），发现在应用滚动更新结束后，并通过 pod IP 人工确认了服务没有问题，仍有概率出现 502 错误，且出现错误的现象会持续几分钟甚至十几分钟的时间，显然远远超过了滚动更新所需时间。<br>
<br>上面的初步测试的现象，排除了应用本身的问题。下一个怀疑的目标指向了 Nginx。既然现象是通过 Nginx 代理访问产生的，那么直接请求 Service 有没有问题呢，由于当前集群 Service 地址和外部网络做了打通，测试起来很方便，我准备了如下的测试：<br><br>
<ol><li>ab 持续请求域名通过 Nginx 访问服务，并触发滚动更新（<code class="prettyprint">ab -r -v 2 -n 50000  http://service.domain.com/test</code>）  </li><li>ab 持续请求 serviceIP:port 访问服务，并触发滚动更新（<code class="prettyprint">ab -r -v 2 -n 50000  http://10.255.10.101/test</code>）</li></ol><br>
<br>经过测试，案例 1 出现了 502 错误，案例 2 未出现。所以，问题是在 Nginx 嘛？<br>
<br>找到负责 Nginx 的同事进行分析，结论是 Nginx 似乎不会造成类似的问题。那为什么上面测试中只有案例1 复现了问题呢？于是我决定重新进行测试，这次在 ab 请求的时候加上了并发（<code class="prettyprint">-c 10</code>），结果，两个案例都出现了 502 的错误。这样，问题似乎又回到了 Kubernetes 集群本身，而且似乎在请求量较大的情况下才会出现。<br>
<br>这时，我开始怀疑是否可能是因为某种原因，滚动发布后的一段时间里，一些请求会错误的被分发到已经被杀掉的老得 podIP 上。为了验证这一猜测，我进行了如下实验：<br><br>
<ol><li>创建一个测试的 Deployment，副本数为 1，提供简单的 http 服务，并在接收到请求时输出日志，并创建对应 Service。  </li><li>使用 ab 并发请求该服务 Service 地址。  </li><li>使用 kubectl patch 修改 Pod 的 label，使其和 Deployment 不一致，触发 Deployment 自动拉起一个新的 Pod。  </li><li>追踪新的 Pod 和老的 Pod 的日志，观察请求进来的情况。</li></ol><br>
<br>第三步 patch pod 的 label，是为了保留原来的 pod 实例，以便观察请求是否会分发到老的 Pod。（patch Pod 的 label 不会使 Pod 重启或退出，但是改变了 label，会使 Pod 脱离原 Deployment 的控制，因此触发 Deployment 新建一个 Pod）。  <br>
<br>结果和预期一致，当新的 Pod 已经 ready，Endpoint 已经出现了新的 Pod 的 IP，请求仍然会进到原来的 Pod 中。  <br>
<br>基于以上的结果，又通过多次实验，观察 Kubernetes 节点上的 IPVS 规则，发现在滚动更新及之后一段时间，老的 podIP 还会出现在 IPVS 规则中，不过 weight 为 0，手动删除后 weight 为 0 的 rs 后，问题就不再出现。到此，找到问题所在是 IPVS，但是为什么会这样呢，在搜索了相关的文章后，大概找到了原因。  <br>
<br><a href="https://k8s.imroc.io/avoid/cases/no-route-to-host/">诡异的 No route to host</a>，讲到了 IPVS 的一个特性：<br>
<br><blockquote><br>也就是 IPVS 模块处理报文的主要入口，发现它会先在本地连接转发表看这个包是否已经有对应的连接了（匹配五元组），如果有就说明它不是新连接也就不会调度，直接发给这个连接对应的之前已经调度过的 rs（也不会判断权重）；如果没匹配到说明这个包是新的连接，就会走到调度这里 （rr，wrr 等调度策略）。</blockquote>即：五元组（源IP地址、目的IP地址、协议号、源端口、目的端口）一致的情况下，IPVS 有可能不经过权重判断，直接将新的连接当成存量连接，转发到原来的 real server（即 PodIP）上。理论上这种情况在单一客户端大量请求的场景下，才有可能触发，这也是<a href="https://k8s.imroc.io/avoid/cases/no-route-to-host/">诡异的 No route to host</a>一文中模拟出的场景，即：<br>
<br><blockquote><br>不同请求的源 IP 始终是相同的，关键点在于源端口是否可能相同。由于 ServiceA 向 ServiceB 发起大量短连接，ServiceA 所在节点就会有大量 TIME_WAIT 状态的连接，需要等 2 分钟（2*MSL）才会清理，而由于连接量太大，每次发起的连接都会占用一个源端口，当源端口不够用了，就会重用 TIME_WAIT 状态连接的源端口，这个时候当报文进入 IPVS 模块，检测到它的五元组跟本地连接转发表中的某个连接一致（TIME_WAIT 状态），就以为它是一个存量连接，然后直接将报文转发给这个连接之前对应的 rs 上，然而这个 rs 对应的 Pod 早已销毁，所以抓包看到的现象是将 SYN 发给了旧 Pod，并且无法收到 ACK，伴随着返回 ICMP 告知这个 IP 不可达，也被应用解释为 “No route to host”。</blockquote><h3>原因分析</h3>这里分析一下之前的测试中为何会出现两种不同的结果。我一共进行了两次对比实验。  <br>
<br>第一次，未加并发，通过 Nginx 和 通过 Service IP 进行访问并对比。这组实验中，通过 Nginx 访问复现了问题，而通过 Service IP 没有，这个结果也险些将排查引入歧途。而现在分析一下，原因是因为目前的 Kubernetes 服务访问入口的设计，是集群外 Nginx 为整个 Kubernetes 集群共用，所以 Nginx 的访问量很高，这也导致 Nginx 向后端的 upstream（即 Service IP）发起连接时，理论上源端口重用的概率较高（事实上经过抓包观察，确实几分钟内就会观察到多次端口重用的现象），因而更容易出现五元组重复的情况。  <br>
<br>第二次，同样的对比，这次加了并发，两边的案例都复现了问题。这样，和上面文章中的场景类似，由于加了并发，发布 ab 请求的机器，也出现了源端口不足而重用的情况，因此也复现了问题。  <br>
<br>而正式环境出现的问题反馈，和我第一次实验通过 Nginx 访问得到复现，是同一个原因，虽然单个应用的请求量远没有达到能够触发五元组重复的量级，但是集群中的所有应用请求量加起来，就会触发此问题。<br>
<h3>解决方案</h3>几种解决方案，上面引用的文章中也都提到，另外可参考<a href="https://github.com/kubernetes/kubernetes/issues/81775">isuue 81775</a>，对这一问题及相关的解决方式有很多的讨论。  <br>
<br>鉴于目前我们的技术能力和集群规模，暂时无法也无需进行 linux 内核级别的功能修改和验证，并且调研了业务应用，绝大部分以短连接为主，我们采用了一种简单直接的方式，在一定程度上避免该问题。开发一个自定义的进程，并以 Daemonset 的方式部署在每个 Kubernetes 的每个节点上。该进程通过 informer 机制监听集群 Endpoint 的变化，一旦监听到事件，便获取 Endpoint 及其对应 Service 的信息，并由此找到其在本节点上对应产生的 IPVS 规则，如果发现在 Virtual Service 下有 weight 为 0 的 Real Service，则立即删除此 Real Service。但是这一解决方式，不可避免的牺牲了部分优雅退出的特性。但是在综合了业务应用的特点权衡之后，这确实是目前可接受的一种解决方式（虽然极其不优雅）。<br>
<h3>思考</h3>是否应该如此使用 Service?  <br>
<br>总结问题的原因，在我们单一业务的请求量远未达到会触发五元组重复这种小概率事件的瓶颈时，过早的遭遇这一问题，和我们对 Kubernetes 服务的入口网关的设计有很大关系，打通 Service 和虚拟机的网络，使用外部 Nginx 作为入口网关，这种用法，在 Kubernetes 的实践中应该算是非常特殊（甚至可称为奇葩），但是这一设计，也是由于目前业务的实例，存在大量虚拟机和容器混布的场景。教训是，在推广和建设 Kubernetes 这种复杂系统时，尽量紧靠社区及大厂公开的生产最佳实践，减少仅凭经验的或机械延用的方式进行架构设计，否则很容易踩坑，事倍功半。<br>
<br>原文链接：<a href="https://maoqide.live/post/problems/kubernetes-service-502/" rel="nofollow" target="_blank">https://maoqide.live/post/prob ... -502/</a>
                                
                                                              
</div>
            