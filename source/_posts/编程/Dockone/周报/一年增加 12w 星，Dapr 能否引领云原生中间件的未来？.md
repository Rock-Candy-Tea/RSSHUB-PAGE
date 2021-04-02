
---
title: '一年增加 1.2w 星，Dapr 能否引领云原生中间件的未来？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/c5db967dfb1d5a0e65692bb39bede85e.png'
author: Dockone
comments: false
date: 2021-04-02 12:10:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/c5db967dfb1d5a0e65692bb39bede85e.png'
---

<div>   
<br>作者 | 敖小剑  阿里云高级技术专家、Dapr Maintainer<br>
<br>Dapr 是 2019 年 10 月微软开源的分布式运行时，在今年 2 月份刚刚发布了 v1.0 正式版本。虽然推出至今不过一年半时间，但 Dapr 发展势头十分迅猛，目前已经在 GitHub 上收获了 1.2w 星。阿里是 Dapr 开源项目的深度参与者和早期采用者，率先进行了生产落地，集团内部有十几个应用在使用 Dapr；目前已有 2 位 Dapr成员，是Dapr 项目中除微软之外代码贡献最多的公司。<br>
<br>虽然 Dapr 在国外有很高的关注度，但在国内知名度非常低，而且现有的少量 Dapr 资料也偏新闻资讯和简单介绍，缺乏对 Dapr 的深度解读。在 Dapr v1.0 发布之际，我希望可以通过这篇文章帮助大家对 Dapr 形成一个准确的认知：掌握 Dapr 项目的发展脉络，了解其核心价值和愿景，领悟 Dapr 项目背后的“道之所在”—— 云原生。<br>
<br><h1>回顾：Service Mesh 原理和方向</h1><h2>1. Service Mesh 的定义</h2>首先，让我们先快速回顾一下“Service Mesh”的定义，这是 Dapr 故事的开始。<br>
<br>以下内容摘录自我在 2017 年 10 月 QCon 上海做的演讲 "Service Mesh：下一代微服务"：<br>
<br><blockquote><br>Service Mesh 是一个基础设施层，用于处理服务间通讯。现代云原生应用有着复杂的服务拓扑，服务网格负责在这些拓扑中实现请求的可靠传递。 <br>
  在实践中，服务网格通常实现为一组轻量级网络代理，它们与应用程序部署在一起，而对应用程序透明。</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/c5db967dfb1d5a0e65692bb39bede85e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/c5db967dfb1d5a0e65692bb39bede85e.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>在 Service Mesh 的定义中，简短地描述了 Service Mesh 的关键特征：<br>
<ul><li><br>定位基础设施层；</li><li><br>功能是服务间通讯；</li><li><br>采用 Sidecar 部署；</li><li><br>特别强调无侵入、对应用透明。</li></ul><br>
<br>熟悉 Service Mesh 的同学，想必对下面这张图片不会陌生：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/a42c7c0d3fbd43e9870c37696eb56f92.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/a42c7c0d3fbd43e9870c37696eb56f92.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>2. Sidecar 模式</h2>和传统 RPC 框架相比，Service Mesh 的创新之处在于引入了 Sidecar 模式：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/0dce7e92ca007053b760964df3580989.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/0dce7e92ca007053b760964df3580989.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>引入 Sidecar 之后，服务间通讯由 Sidecar 接管，而 Sidecar 由控制平面统一控制，从而实现了服务间通讯能力的下沉，使得应用得以大幅简化。<br>
<br>我们再来快速回顾一下 Service Mesh 的基本思路：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/f94244f31107bc0d27263b4072f95c07.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/f94244f31107bc0d27263b4072f95c07.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>引入 Sidecar 之前：业务逻辑和非业务逻辑混合在一个进程内，应用既有业务逻辑，也有各种非业务的功能（体现为各种客户端 SDK）。</li><li><br>引入 Sidecar 之后：客户端 SDK 的功能剥离，业务进程专注于业务逻辑，而 SDK 中的大部分功能被拆解为独立进程，以 Sidecar 的模式运行。</li></ul><br>
<br>通过引入 Sidecar 模式，Service Mesh 成功实现了 <strong>关注点分离</strong> 和 <strong>独立维护</strong> 两大目标。<br>
<br><h2>3. Service Mesh 的发展趋势</h2>以 Istio 项目为例，我总结了最近一两年来 Service Mesh 的发展趋势（注意这些内容不是本文的重点，请快速阅读，简单了解即可）：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/09f071926ed3901a9c3f414232e37f50.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/09f071926ed3901a9c3f414232e37f50.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h3><strong>1）协议支持</strong></h3>Istio 中通讯协议的支持主要在 HTTP 和 gRPC，各家厂商在提供更多协议支持，包括 Dubbo、Thrift、Redis。也有一些社区力量在做补充，如赵化冰同学的 Aeraki 项目。<br>
<br><h3><strong>2）虚拟机支持</strong></h3>虚拟机的支持最近成为 Istio 的重要关注点：<br>
<ul><li>Istio 0.2：Mesh Expansion</li><li>Istio 1.1：ServiceEntry</li><li>Istio 1.6：WorkloadEntry</li><li>Istio 1.8：WorkloadGroup 和智能 DNS 代理</li><li>Istio 1.9：虚拟机集成</li></ul><br>
<br><h3><strong>3）易用性</strong></h3><ul><li><br>Istio 1.5：控制平面单体化，合并多个组件为 istiod（这是 Istio 开源以来最大的一次架构调整之一）。</li><li><br>Istio 1.7：主推 Operator 安装方式，增强 istioctl 工具，支持在 Sidecar 启动之后再启动应用容器。</li><li><br>Istio 1.8：改善升级和安装, 引入 istioctl bug-report</li></ul><br>
<br><h3><strong>4）可观测性</strong></h3>Istio 1.8：正式移除 Mixer，在 Envoy 基于 wasm 重新实现 Mixer 功能 （Istio 最大的架构调整之一）Istio 1.9：远程获取和加载 wasm 模块。<br>
<br><h3><strong>5）外部集成</strong></h3>和非 service mesh 体系的相互访问，实现应用在两个体系之间的平滑迁移。<br>
<ul><li><br>Istio 曾计划通过 MCP 协议提供统一的解决方案。</li><li><br>Istio 1.7：MCP 协议被废弃，改为 mcp over xds。</li><li><br>Istio 1.9：Kubernetes Service API 支持 (alpha)，对外暴露服务。</li></ul><br>
<br>从上面列出的内容，可以看到 Istio 在最近一两年间还是在非常努力地完善自身，虽然过程有些曲折和往复（比如顽固不化的坚持 Mixer 到最后听从全社区的呼唤彻底废弃了 Mixer，开始支持虚拟机后来实质性放弃再到最近重新重视，引入 Galley 再废弃 Galley，引入 MCP 再变相放弃 MCP），但整体上说 Istio 还是在朝 Product Ready 的大方向在努力。<br>
<br>备注：当然，社区对 Istio 的演进速度以及 Product Ready 的实际状态还是很不满意的，以至于出现了这个梗：Make Istio Product Ready (Again, and Again…)。<br>
<br><h2>4. Service Mesh 回顾总结</h2>我们前面快速回顾了 Service Mesh 的定义、Sidecar 模式的原理，以及粗略罗列了一下最近一两年间 Service Mesh 的发展趋势，主要是为了告知大家这样一个信息：<br>
<br><blockquote><br>虽然 Service Mesh 蓬勃发展，但核心元素始终未变。</blockquote>从 2016 年 Linkerd 的 CEO William Morgon 给出 Service Mesh 的定义，到 2021 年 Istio 都发布到了 1.9 版本，整整六年期间，Service Mesh 有了很多的变化，但以下三个核心元素始终未变：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/ea5b89da4ac5134a8b18d07d2fc5ebfd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/ea5b89da4ac5134a8b18d07d2fc5ebfd.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>定位：Service Mesh 的定位始终是提供 服务间通讯 的基础设施层，范围包括 HTTP 和 RPC——支持 HTTP1.1/REST，支持 HTTP2/gRPC，支持 TCP 协议。也有一些小的尝试如对 Redis 、 Kafka 的支持。</li><li><br>部署：Service Mesh 支持 Kubernetes 和虚拟机，但都是采用 Sidecar 模式部署，没有采用其他方式如 Node 部署、中心化部署。</li><li><br>原理：Service Mesh 的工作原理是 原协议转发，原则上不改变协议内容（通常只是 header 有些小改动）。为了达到零侵入的目标，还引入了 iptables 等流量劫持技术。</li></ul><br>
<br><h1>演进：云原生分布式应用运行时</h1>在快速完成 Service Mesh 的回顾之后，我们开始本文第二部分的内容：当 Sidecar 模式进一步推广，上述三个核心元素发生变化时，Sidecar 模式将会如何演进？<br>
<br><h2>1. 实践：更多 Mesh 形态</h2>我之前在蚂蚁金服的中间件团队做 Service Mesh 相关的内容，可能很多朋友是从那个时候开始认识我。当时蚂蚁不仅仅做了 Service Mesh，还将 Service Mesh 的 Sidecar 模式推广到其他的中间件领域，陆陆续续探索了更多的 mesh 形态：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/bd6350cf91fdfbae91b6ab8b6697b4aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/bd6350cf91fdfbae91b6ab8b6697b4aa.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>这个图片摘录自我在 2019 年 10 月的上海 QCon 上做的主题演讲 "诗和远方：蚂蚁金服 Service Mesh 深度实践"，当时我们分享了包括消息 Mesh、数据库 Mesh 等在内的多种 mesh 形态。<br>
<br><h2>2. 理论升华：Multi-Runtime 理念的提出</h2>最近有越来越多的项目开始引入 Sidecar 模式， Sidecar 模式也逐渐被大家认可和接受。就在 2020 年，Bilgin Ibryam 提出了 Multi-Runtime 的理念，对基于 Sidecar 模式的各种产品形态进行了实践总结和理论升华。<br>
<br>首先我们介绍一下 Bilgin Ibryam 同学，他是《Kubernetes Patterns》一书的作者，Apache Camel 项目的 committer，目前工作于 Red Hat 。<br>
<br>2020 年初，Bilgin Ibryam 发表文章 "Multi-Runtime Microservices Architecture" ，正式提出了多运行时微服务架构（别名 Mecha/ 机甲，非常帅气的名字）。在这篇文章中，Bilgin Ibryam 首先总结了分布式应用存在的四大类需求，作为 Multi-Runtime 的理论出发点：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/00646e7d353223ba81c8311edd12d341.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/00646e7d353223ba81c8311edd12d341.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>这四大类需求中，生命周期管理类的需求主要是通过 PaaS 平台如 kubernetes 来满足，而 Service Mesh 提供的主要是网络中的点对点通讯，对于其他通讯模式典型如 pub-sub 的消息通讯模式并没有覆盖到，此外状态类和绑定类的需求大多都和 Service Mesh 关系不大。<br>
<br>Multi-Runtime 的理论推导大体是这样的——基于上述四大类需求，如果效仿 Service Mesh，从传统中间件模式开始，那么大体会有下面两个步骤：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/ded9c49f673006f8d48975efea62b490.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/ded9c49f673006f8d48975efea62b490.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>步骤一：将应用需要的分布式能力外移到各种 runtime，此时会出现数量众多的各种 Sidecar 或者 proxy，如上面中列出来的 Istio、Knative、Cloudstate、Camel、Dapr 等。</li><li><br>步骤二：这些 runtime 会逐渐整合，只保留少量甚至只有一两个 runtime。这种提供多种分布式能力的 runtime 也被称为 Mecha。</li></ul><br>
<br>步骤二完成后，每个微服务就会由至少一个 Mecha Runtime 和应用 Runtime 共同组成，也就是每个微服务都会有多个（至少两个）runtime，这也就是 Multi-Runtime / Mecha 名字的由来。<br>
<br><h2>3. Multi-Runtime 和云原生分布式应用</h2>将 Multi-Runtime / Mecha 的理念引入到云原生分布式应用的方式：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/48b601baffb5c0c2dbe54b68e4d73fe6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/48b601baffb5c0c2dbe54b68e4d73fe6.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>能力：Mecha 是通用的，高度可配置的，可重用的组件，提供分布式原语作为现成的能力。</li><li><br>部署：Mecha 可以与单个 Micrologic 组件一起部署（Sidecar 模式），也可以部署为多个共享（如 Node 模式）。</li><li><br>协议：Mecha 不对 Micrologic 运行时做任何假设。它与使用开放协议和格式（如 HTTP/gRPC，JSON，Protobuf，CloudEvents）的多语言微服务甚至单体一起使用。</li><li><br>配置：Mecha 以简单的文本格式（例如 YAML，JSON）声明式地配置，指示要启用的功能以及如何将其绑定到 Micrologic 端点。</li><li><br>整合：与其依靠多个代理来实现不同的目的（例如网络代理，缓存代理，绑定代理），不如使用一个 Mecha 提供所有这些能力。</li></ul><br>
<br><h2>4. Multi-Runtime 的特点和差异</h2>虽然同为 Sidecar 模式，但是和 Service Mesh 相比，Multi-Runtime 有自身的特点：<br>
<ul><li><br>提供能力的方式和范围：Multi-Runtime 提供的是分布式能力，体现为应用需要的各种分布式原语，并不局限于单纯的服务间点对点通讯的网络代理.</li><li><br>Runtime 部署的方式：Multi-Runtime 的部署模型，不局限于 Sidecar 模式，Node 模式在某些场景下（如 Edge/IoT，Serverless FaaS）可能会是更好的选择。</li><li><br>和 App 的交互方式：Multi-Runtime 和应用之间的交互是开放而有 API 标准的，Runtime 和 Micrologic 之间的“协议”体现在 API 上，而不是原生的 TCP 通讯协议。另外 Multi-Runtime 不要求无侵入，还会提供各种语言的 SDK 以简化开发。</li></ul><br>
<br>Multi-Runtime 和 Service Mesh 的差异总结如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/855dd036b79ba89fb6f2d411a53fd240.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/855dd036b79ba89fb6f2d411a53fd240.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>5. Multi-Runtime 的本质</h2>至此我介绍了 Multi-Runtime 架构的由来，相信读者对 Multi-Runtime 的特点以及和 Service Mesh 的差异已经有所了解。为了加深大家的理解，我来进一步分享一下我个人对 Multi-Runtime 的感悟：<br>
<br><strong>Multi-Runtime 的本质是面向云原生应用的分布式能力抽象层。</strong><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/2a4b3f19cbd5107ab642575eaa208a9f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/2a4b3f19cbd5107ab642575eaa208a9f.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>何为 “分布式能力抽象层”?<br>
<br>如上图所示，左侧是分布式应用存在的四大类需求：生命周期、网络、状态、绑定。从需求上说 Multi-Runtime 要为分布式应用提供这四大类需求下所列出的各种具体的分布式能力。以 Sidecar 模式为应用提供这些能力容易理解，但关键在于 Multi-Runtime 提供这些能力的方式。和 Service Mesh 采用原协议转发不同，Multi-Runtime 的方式是：<br>
<ul><li><br>将能力抽象为 API：很多分布式能力没有类似 HTTP 这种业界通用的协议，因此 Multi-Runtime 的实现方式是将这些能力抽象为和通讯协议无关的 API，只用于描述应用对分布式能力的需求和意图，尽量避免和某个实现绑定。</li><li><br>为每种能力提供多种实现：Multi-Runtime 中的能力一般都提供有多种实现，包括开源产品和公有云商业产品。</li><li><br>开发时：这里我们引入一个“面对能力编程”的概念，类似于编程语言中的“不要面对实现编程，要面向接口编程”。Multi-Runtime 中提倡面向“能力（Capability）”编程，即应用开发者面向的应该是已经抽象好的分布式能力原语，而不是底层提供这些能力的具体实现。</li><li><br>运行时：通过配置在运行时选择具体实现，不影响抽象层 API 的定义，也不影响遵循“面对能力编程”原则而开发完成的应用。</li></ul><br>
<br>备注：分布式能力的通用标准 API，将会是 Multi-Runtime 成败的关键，Dapr 的 API 在设计和实践中也遇到很大的挑战。关于这个话题，我稍后将单独写文章来阐述和分析。<br>
<br><h1>介绍：分布式应用运行时 Dapr</h1>在快速回顾 Service Mesh 和详细介绍 multi-runtime 架构之后，我们已经为了解 Dapr 奠定了良好的基础。现在终于可以开始本文的正式聂荣，让我们一起来了解 Dapr 项目。<br>
<br><h2>1. 什么是 Dapr？</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/2d4fe04a85c30bd76d70098116cfc82c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/2d4fe04a85c30bd76d70098116cfc82c.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Dapr 是一个开源项目，由微软发起，下面是来自 Dapr 官方网站的权威介绍：<br>
<br>Dapr is a portable, event-> driven runtime that makes it easy for any developer to build resilient, stateless and stateful applications that run on the cloud and edge and embraces the diversity of languages and developer frameworks. Dapr 是一个可移植的、事件驱动的运行时，它使任何开发者都能轻松地构建运行在云和边缘的弹性、无状态和有状态的应用程序，并拥抱语言和开发者框架的多样性。<br>
<br>参考并对照 Service Mesh 的定义，我们对上述 Dapr 定义的分析如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/db9080420794c6e788c077fac9e849ce.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/db9080420794c6e788c077fac9e849ce.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>定位：Dapr 将自身定义为运行时（runtime），而不是 Service Mesh 中的 proxy。</li><li><br>功能：Dapr 为应用提供各种分布式能力，以简化应用的开发。上面定义中提及的关键点有弹性、支持有状态和无状态、事件驱动。</li><li><br>多语言：对多语言的支持是 Sidecar 模型的天然优势，Dapr 也不例外，考虑到 Dapr 为应用提交的分布式能力的数量，这可能比 Service Mesh 只提供服务间通讯能力对应用的价值更高。而且由于 Dapr 语言 SDK 的存在，Dapr 可以非常方便的和各编程语言的主流开发框架集成，如 Java 下和 Spring 框架集成。</li><li><br>可移植性：Dapr 适用的场景包括各种云（公有云，私有云，混合云）和边缘网络，Multi-Runtime 架构的几个关键特性如"面向能力编程"、标准 API、可运行时配置实现等为 Dapr 带来了绝佳的跨云跨平台的可移植性。</li></ul><br>
<br>我们将在后面的介绍中详细展开 Dapr 的这些特性。在开始之前，这里有一个小小的花絮—— “Dapr” 项目名字的由来：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/d729bea185bf793b7b643d5e857b704a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/d729bea185bf793b7b643d5e857b704a.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>2. Dapr Sidecar 的功能和架构</h2>和 Service Mesh 类似，Dapr 同样基于 Sidecar 模式，但提供的功能和使用场景要比 Service Mesh 的复杂多，如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/82ca83033309b2adabda9f49fef66eda.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/82ca83033309b2adabda9f49fef66eda.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Dapr 的 Sidecar，除了可以和 Service Mesh 一样支持服务间通讯（目前支持 HTTP1.1/REST 协议和 gRPC 协议外，还可以支持到更多的功能，如 state（状态管理）、pub-sub（消息通讯），resource binding（资源绑定，包括输入和输出）。<br>
<br>每个功能都有多种实现，在上图中我简单摘录了这几个能力的常见实现，可以看到实现中既有开源产品，也有公有云的商业产品。注意这只是目前 Dapr 实现中的一小部分，目前各种实现（在 Dapr 中被称为组件，我们下面会介绍）已经有超过 70 个，而且还在不断的增加中。<br>
<br>在 Dapr 的架构中，有三个主要组成部分：API、Building Blocks 和 Components，如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/18f5b2c9cf5e9695024199ef9a9e4af2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/18f5b2c9cf5e9695024199ef9a9e4af2.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>Dapr API：Dapr 提供两种 API，HTTP1.1/REST 和 HTTP2/gRPC，两者在功能上是对等的。</li><li><br>Dapr Building Blocks：翻译为构建块，这是 Dapr 对外提供能力的基本单元，每个构建块对外提供一种分布式能力。</li><li><br>Dapr components：组件层，这是 Dapr 的能力实现层，每个组件都会实现特定构建块的能力。</li></ul><br>
<br>为了帮助大家理解 Dapr 的架构，我们回顾一下前面重点阐述的 Multi-Runtime 的本质：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/c9a622de1db2be823b94cf30f4d7cfd4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/c9a622de1db2be823b94cf30f4d7cfd4.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Multi-Runtime 的本质是面向云原生应用的分布式能力抽象层。<br>
<br>结合 Multi-Runtime 理念，我们再来理解 Dapr Runtime 的架构：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/26a7061ca7146de48c18d887dea564c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/26a7061ca7146de48c18d887dea564c7.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>Dapr Building Blocks 提供“能力”。</li><li><br>Dapr API 提供对分布式能力的“抽象”，对外暴露 Building Block 的能力。</li><li><br>Dapr Components 是 Building Block 能力的具体“实现”。</li></ul><br>
<br><h2>3. Dapr 的愿景和现有能力</h2>下图来自 Dapr 官方，比较完善地概括了 Dapr 的能力和层次架构：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/41e60b21a8009164b57d52a89f8247b9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/41e60b21a8009164b57d52a89f8247b9.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>居中蓝色的是 Dapr Runtime：这里列出了 Dapr 目前已经提供的构建块。</li><li><br>Dapr Runtime 对外通过远程调用提供能力，目前有 HTTP API 和 gRPC API。</li><li><br>由于 Sidecar 模式的天然优势，Dapr 支持各种编程语言，而且 Dapr 官方为主流语言（典型如 Java、golang、c++、nodejs、.net、python）提供了 SDK。这些 SDK 封装了通过 HTTP API 或者 gRPC API 和 Dapr Runtime 进行交互的能力。</li><li><br>最下方是可以支持 Dapr 的云平台或者边缘网络，由于每个能力都可以由不同的组件来完成，因此理论上只要 Dapr 的支持做的足够完善，就可以实现在任何平台上，总是能找到基于开源产品或者基于云厂商商业化产品的可用组件。</li></ul><br>
<br>结合以上几点，Dapr 提出了这样一个愿景：<br>
<br><strong>Any language, any framework, anywhere</strong><br>
<br>即：可以使用任意编程语言开发，可以和任意框架集成，可以部署在任意平台。下图是 Dapr 目前已有的构建块和他们提供的能力的简单描述：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/f64468691cc47846bee0b6d90cd0c8fe.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/f64468691cc47846bee0b6d90cd0c8fe.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>4. Dapr 的控制平面</h2>和 Service Mesh 的架构类似，Dapr 也有控制平面的概念：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/d17fd65098ff0ca7b04190946b12abdb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/d17fd65098ff0ca7b04190946b12abdb.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Dapr 的控制平面组件有：<br>
<ul><li>Dapr Actor Placement</li><li>Dapr Sidecar Injector</li><li>Dapr Sentry</li><li>Dapr Operator</li></ul><br>
<br>比较有意思的是：Istio 为了简化运维，已经将微服务架构的控制平面进行了合并，控制平面回归到传统的单体模式。而 Dapr 的控制平面目前还是微服务架构，不知道未来会不会效仿 Istio。<br>
<br>备注：出于控制篇幅的考虑，本文不对 Dapr 的构建块和控制平面进行详细展开，稍后预计会另有单独文章做详细介绍，对 Dapr 有兴趣的同学可以关注。<br>
<br><h2>5. Dapr 的发展历程和阿里巴巴的参与</h2>Dapr 是一个非常新的开源项目，发展至今也才大约一年半的时间，不过社区关注度还不错（主要是国外），在 GitHub 上目前有接近 12000 颗星（类比：Envoy 16000，Istio 26000，Linkerd 7000）。Dapr 项目的主要里程碑是：<br>
<ul><li><br>2019 年 10 月：微软在 GitHub 上开源了 Dapr，发布 0.1.0 版本。</li><li><br>2021 年 2 月：Dapr v1.0 版本发布。</li></ul><br>
<br>阿里巴巴深度参与 Dapr 项目，不仅仅以终端用户的身份成为 Dapr 的早起采用者，也通过全面参与 Dapr 的开源开发和代码贡献成为目前 Dapr 项目中的主要贡献公司之一，仅次于微软：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/c8b7d0ae89609b0a73dfbee31ac5ae1d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/c8b7d0ae89609b0a73dfbee31ac5ae1d.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>2020 年中：阿里巴巴开始参与 Dapr 项目，在内部试用功能并进行代码开发。</li><li><br>2020 年底：阿里巴巴内部小规模试点 Dapr，目前已经十几个应用在使用 Dapr 。</li></ul><br>
<br>备注：关于 Dapr 在阿里巴巴的实践，请参阅我们刚刚发表在 Dapr 官方博客上的文章 "How Alibaba is using Dapr"。<br>
<br>目前我们已经有两位 Dapr Committer 和一位 Dapr Maintainer，在 2021 年预计我们会在 Dapr 项目上有更多的投入，包括更多的开源代码贡献和落地实践，身体力行的推动 Dapr 项目的发展。欢迎更多的国内贡献者和国内公司一起加入到 Dapr 社区。<br>
<br><h2>6. Dapr 快速体验</h2>在 Dapr 的官方文档中提供了 Dapr 安装和 quickstudy 的内容，可以帮助大家快速的安装和体验 Dapr 的能力和使用方式。<br>
<br>为了更加快捷和方便的体验 Dapr，我们通过 阿里云知行动手实验室 提供了一个超级简单的 Dapr 入门教程，只要大约十分钟就可以快速体验 Dapr 的开发、部署过程：_<a href="https://start.aliyun.com/course?id=gImrX5Aj"></a><a href="https://start.aliyun.com/course?id=gImrX5Aj" rel="nofollow" target="_blank">https://start.aliyun.com/course?id=gImrX5Aj</a>_。<br>
<br>有兴趣的同学可以实际体验一下。<br>
<br><h1>展望：应用和中间件的未来形态</h1>在本文的最后部分，我们展望一下应用和中间的未来形态。<br>
<br><h2>1. 云原生的时代背景</h2>首先要申明的是，我们阐述的所有这些内容，都是基于一个大的前提：云原生。<br>
<br>下面这张图片，摘录自我在 2019 年 10 月 QCon 大会上的演讲 "诗和远方：蚂蚁金服 Service Mesh 深度实践" :<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/bfed37aeafc8535890e69d910a2d3348.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/bfed37aeafc8535890e69d910a2d3348.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>当时（2019 年）我们刚完成了 Kubernetes 和 Service Mesh 的探索和大规模落地，并开始 Serverless 的新探索，我在文中做了一个云原生落地总结和是否采纳 Service Mesh 的建议，大体可以概括为（直接援引原文）：<br>
<ul><li><br>有一点我们是非常明确的：Mesh 化是云原生落地的关键步骤。</li><li><br>如果云原生是你的诗和远方，那么 Service Mesh 就是必由之路。</li><li><br>Kubernetes / Service Mesh / Serverless 是当下云原生落地实践的三驾马车，相辅相成，相得益彰。</li></ul><br>
<br>两年之后的今天，回顾当时对云原生发展战略大方向的判断，感触良多。上面这张图片我稍加调整，增加了 Multi-Runtime/ 容器 / 多云 / 混合云的内容，修改如下图：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/64003eff57d8b53a7989d2e426496ed0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/64003eff57d8b53a7989d2e426496ed0.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>和 2019 年相比，云原生的理念得到了更广泛的认可和采纳：多云、混合云成为未来云平台的主流方向；Service Mesh 有了更多的落地实践，有更多的公司使用 Service Mesh；Serverless 同样在过去两年间快速发展。<br>
<br>云原生的历史大潮还在进行中，而在云原生背景下，应用和中间件将何去何从？<br>
<br><h2>2. 应用的期望就是中间件的方向</h2>让我们畅想云原生背景下处于最理想状态的业务应用，就当是个甜美的梦吧：<br>
<ul><li><br>应用可以使用任意喜爱而适合的语言编写，可以快速开发和快速迭代。</li><li><br>应用需要的能力都可以通过标准的 API 提供，无需关心底层具体实现。</li><li><br>应用可以部署到任意的云端，不管是公有云、私有云还是混合云，没有平台和厂商限制，无需代码改造。</li><li><br>应用可以根据流量弹性伸缩，顶住波峰的压力，也能在空闲时释放资源。</li><li><br>……</li></ul><br>
<br>我个人的对云原生应用未来形态的看法是：Serverless 会是云上应用的理想形态和主流发展方向；而多语言支持、跨云的可移植性和应用轻量化将会是云原生应用的三个核心诉求。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/c08eb3601c810e3a71a0ec24237408b1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/c08eb3601c810e3a71a0ec24237408b1.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>应用对云原生的期望，就是中间件前进的方向！</strong><br>
<br>过去几年间，中间件在云原生的美好目标推动下摸索着前进，未来几年也必将还是如此。Service Mesh 探索了 Sidecar 模式，Dapr 将 Sidecar 模式推广到更大的领域：<br>
<ul><li><br>完善的多语言支持和应用轻量化的需求推动中间件将更多的能力从应用中分离出来。</li><li><br>Sidecar 模式会推广到更大的领域，越来越多的中间件产品会 开始 Mesh 化，整合到 Runtime。</li><li><br>对厂商锁定的天然厌恶和规避，会加剧对可移植性的追求，从而进一步促使为下沉到 Runtime 的中分布式能力提供标准而业界通用的 API。</li><li><br>API 的标准化和社区认可，将成为 Runtime 普及的最大挑战，但同时也将推动各种中间件产品改进自身实现，实现中间件产品和社区标准 API 之间的磨合与完善。</li></ul><br>
<br>在云原生需求推动下，多语言支持、跨云的可移植性和应用轻量化，预计将成为未来几年间中间件产品的突破点和重点发展方向，如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210329/46096a51b0625723bfd103278063aa4d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210329/46096a51b0625723bfd103278063aa4d.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>在目前的云原生领域，Dapr 项目是一个非常引人注目的新生力量。Dapr 是探路者，开启 Multi-Runtime 理念的全新探索，而这必然是一个艰难的过程。非常期待有更多的个人和公司，和我们一起加入 Dapr 社区，一起探索，共同成长！<br>
<br>备注：关于 Dapr API 标准化的话题，以及 Dapr 在定义 API 和实现 API 遇到的挑战，在现场曾有一段热烈的讨论，我将稍后整理出单独的文章，结合 state API 的深度实践和新的 configuration API 的设计过程，深入展开，敬请关注。<br>
<br><h1>尾声</h1>在这篇文章的最后，让我们用这么一段话来总结全文：<br>
<br>Dapr 在 Service Mesh 的基础上进一步扩展 Sidecar 模式的使用场景，一方面提供天然的多语言解决方案，满足云原生下应用对分布式能力的需求，帮助应用轻量化和 Serverless 化，另一方面提供面向应用的分布式能力抽象层和标准 API，为多云、混合云部署提供绝佳的可移植性，避免厂商锁定。<br>
<br><strong>Dapr 将引领云原生时代应用和中间件的未来</strong>。<br>
<br><h3>附录：参考资料</h3>本文相关的参考资料如下：<br>
<ul><li><br>Dapr 官网 和 Dapr 官方文档：部分 Dapr 介绍内容和图片摘录自 dapr 官方网站。</li><li><br>Multi-Runtime Microservices Architecture: multi-runtime 介绍的内容和图片部分援引自 Bilgin Ibryam 的这篇文章</li></ul><br>
<br><h3><strong>作者简介</strong></h3>敖小剑，资深码农，微服务专家，Service Mesh 布道师，Dapr maintainer。专注于基础架构，Cloud Native 拥护者，敏捷实践者，坚守开发一线打磨匠艺的架构师。目前就职阿里云，在云原生应用平台负责 Dapr 开发。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            