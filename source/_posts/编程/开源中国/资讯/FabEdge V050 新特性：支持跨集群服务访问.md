
---
title: 'FabEdge V0.5.0 新特性：支持跨集群服务访问'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static001.geekbang.org/infoq/1e/1ec837757321a9401845c27dcde512e6.png'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 03:56:00 GMT
thumbnail: 'https://static001.geekbang.org/infoq/1e/1ec837757321a9401845c27dcde512e6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0">3 月 21 日，FabEdge 正式发布了 V0.5 版本，该版本在 V0.4 的基础上，针对集群间访问的需求，新增了 FabDNS 组件，实现了对跨集群服务访问功能的支持。</p> 
<p style="margin-left:0; margin-right:0">FabEdge 一款基于 Kubernetes 构建的专注于边缘计算场景的容器网络方案，支持 KubeEdge / SuperEdge / OpenYurt 等主流边缘计算框架。旨在解决边缘计算场景下容器网络配置管理复杂，网络割裂互不通信，缺少拓扑感知能力，无法提供就近访问等问题。2022 年 3 月 8 日，FabEdge 被接纳为 CNCF 沙箱级项目，成为 CNCF 沙箱中首个边缘容器网络项目。</p> 
<h1 style="margin-left:0px; margin-right:0px"><span><strong>1. 跨集群需求产生的背景</strong></span></h1> 
<p style="margin-left:0; margin-right:0">FabEdge 在 V0.4.0 时已经支持多边缘集群通信，但集群间的相互访问只能通过 IP 来访问，即便访问目标是一个服务也会如此，这与日常中使用 Kubernetes 的习惯极不相符。事实上，自多集群通信的需求存在以来，跨集群的服务发现和访问的需求就一直存在，开源社区也一直在努力解决这个问题：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Multi-cluster Service APIs (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes-sigs%2Fmcs-api%29" target="_blank">https://github.com/kubernetes-sigs/mcs-api)</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Lighthouse (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsubmariner.io%2Fgetting-started%2Farchitecture%2Fservice-discovery%2F%29" target="_blank">https://submariner.io/getting-started/architecture/service-discovery/)</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Cilium Load-balancing & Service Discovery (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.cilium.io%2Fen%2Fstable%2Fgettingstarted%2Fclustermesh%2Fservices%2F%29" target="_blank">https://docs.cilium.io/en/stable/gettingstarted/clustermesh/services/)</a></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>既然已经存在这些解决方案，为什么 FabEdge 要提出自己的解决方案呢？有如下原因：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">mcs-api 只是一套 API，需要其他实现者解决各个集群间服务信息的导出导入。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Lighthouse 依赖于 submariner，而 submariner 并不是面向边缘场景的。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Cilium 是一套整体解决方案，不能跟其他 CNI 共存，此外它也不是面向边缘场景。</p> </li> 
</ul> 
<h1 style="margin-left:0px; margin-right:0px"><span><strong>2. FabDNS - FabEdge 的专属方案</strong></span></h1> 
<p style="margin-left:0; margin-right:0">为 FabEdge 提供跨集群服务访问的组件叫 <strong>FabDNS</strong>  (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFabEdge%2Ffab-dns%29" target="_blank">https://github.com/FabEdge/fab-dns)</a>，它尝试达成以下目标：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">它允许一个集群访问其他集群提供的服务，服务类型仅限于 ClusterIP，Headless 两种。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">一个服务可以部署于一个集群内部，也可以分散在多个集群里。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供一定的具备拓扑感知的 DNS 解析，访问者可以就近访问最近的服务节点。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">FabDNS 有两个组件: service-hub 与 fab-dns。还提供了一个 CRD: GlobalService。一个集群若想将一个服务提供给其他集群，首先要将该服务标注为全局服务。service-hub 负责各个集群间全局服务的导出与导入，fab-dns 负责在集群内部提供全局服务的地址解析。每个集群部署时 FabDNS 时要标注拓扑信息，即 region 和 zone 信息，FabDNS 的拓扑感知就是基于这些拓扑信息来进行的。</p> 
<h1 style="margin-left:0px; margin-right:0px"><span><strong>3. 新特性实例讲解</strong></span></h1> 
<div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/1e/1ec837757321a9401845c27dcde512e6.png" referrerpolicy="no-referrer">
 </div> 
</div> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">以上图为例，共有三个集群，北京集群是主集群，上海集群和苏州集群的 service-hub 都要通过北京集群的 service-hub 交换全局服务信息。北京和上海集群同时暴露了一个 nginx 服务和一个 mysql 服务，假设这些服务都是在 default 命名空间下。如果苏州集群的 pod 去访问 nginx.default.global，那么它会被上海集群的 nginx 背后的 pod 响应，为什么呢？因为苏州和上海的 region 都是 south，而它自己本身并没有提供 nginx 服务或者没有暴露这个服务; 如果上海或北京的一个 pod 去访问 nginx.default.global，那么响应的 pod 只会是各自集群的 pod，因为 zone 是匹配的。</p> 
<p style="margin-left:0; margin-right:0">以上即是 FabEdge V0.5.0 的新特性，欢迎大家体验和提出宝贵的意见。</p> 
<hr> 
<p style="margin-left:0; margin-right:0"><strong>Github：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFabEdge%2Ffabedge" target="_blank"><u>https://github.com/FabEdge/fabedge</u></a></p> 
<p style="margin-left:0; margin-right:0"><strong>官方网站：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.fabedge.io%2F" target="_blank"><u>http://www.fabedge.io</u></a></p> 
<p style="margin-left:0; margin-right:0"><strong>例会视频汇总：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspace.bilibili.com%2F524926244" target="_blank"><u>https://space.bilibili.com/524926244</u></a></p>
                                        </div>
                                      
</div>
            