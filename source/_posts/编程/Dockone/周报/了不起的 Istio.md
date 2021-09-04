
---
title: '了不起的 Istio'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/cc8a999c49ef80ea8fd04c400b2b9169.png'
author: Dockone
comments: false
date: 2021-09-04 13:13:22
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/cc8a999c49ef80ea8fd04c400b2b9169.png'
---

<div>   
<br>很多企业都会面临从单体应用向微服务架构的转型，也会衍生出更多的分布式场景需求。随着规模和复杂度的不断增长，如何才能更好的理解、高效的管理<strong>服务网格</strong>呢？<br>
<br>本节篇幅较长，我们主要围绕以下几点来展开：<br>
<ol><li>什么是服务网格？</li><li>初识  <code class="prettyprint">Istio</code></li><li>核心特性</li><li>流程架构</li><li>核心模块</li><li><code class="prettyprint">Envoy</code> 进阶</li><li>方案畅想</li></ol><br>
<br>对许多公司来说，<code class="prettyprint">Docker</code> 和 <code class="prettyprint">Kubernetes</code> 这样的工具已经解决了部署问题，或者说几乎解决了。但他们还没有解决<strong>运行时</strong>的问题，这就是服务网格（<code class="prettyprint">Service Mesh</code>）的由来。<br>
<h3>什么是服务网格？</h3>服务网格（<code class="prettyprint">Service Mesh</code>）用来描述组成这些应用程序的微服务网络以及它们之间的交互。它是一个用于保证服务间安全、快速、可靠通信的网络代理组件，是随着<strong>微服务和云原生应用</strong>兴起而诞生的基础设施层。<br>
<br>它通常以轻量级网络代理的方式同应用部署在一起。比如 <code class="prettyprint">Sidecar</code> 方式，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/cc8a999c49ef80ea8fd04c400b2b9169.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/cc8a999c49ef80ea8fd04c400b2b9169.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们对上图做个解释：<br>
<br><code class="prettyprint">Service Mesh</code> 设计一般划分为两个模块，<strong>控制面</strong>和<strong>数据面</strong>。对于应用来说，所有流量都会经过数据面进行转发。顺利转发的前提：<strong>数据面需要知道转发的目标地址</strong>，目标地址本身是由一些业务逻辑来决定的（例如服务发现）。<br>
<br>所以自然而然地，我们可以推断<strong>控制面</strong>需要负责管理数据面能正常运行所需要的一些配置：<br>
<ul><li>需要知道某次请求转发去哪里：服务发现配置；</li><li>外部流量进入需要判断是否已经达到服务流量上限：限流配置；</li><li>依赖服务返回错误时，需要能够执行相应的熔断逻辑：熔断配置。</li></ul><br>
<br><code class="prettyprint">Serivce Mesh</code> 可以看作是一个位于 <code class="prettyprint">TCP/IP</code> 之上的网络模型，抽象了服务间可靠通信的机制。但与 <code class="prettyprint">TCP</code> 不同，它是面向应用的，为应用提供了统一的可视化和控制。<br>
<br><code class="prettyprint">Service Mesh</code> 具有如下优点：<br>
<ul><li>屏蔽分布式系统通信的复杂性（负载均衡、服务发现、认证授权、监控追踪、流量控制等等），服务只用关注业务逻辑；</li><li>真正的语言无关，服务可以用任何语言编写，只需和 <code class="prettyprint">Service Mesh</code> 通信即可；</li><li>对应用透明，<code class="prettyprint">Service Mesh</code> 组件可以单独升级。</li></ul><br>
<br><code class="prettyprint">Service Mesh</code> 目前也面临一些挑战：<br>
<ul><li><code class="prettyprint">Service Mesh</code> 组件以代理模式计算并转发请求，一定程度上会降低通信系统性能，并增加系统资源开销；</li><li><code class="prettyprint">Service Mesh</code> 组件接管了网络流量，因此服务的整体稳定性依赖于 <code class="prettyprint">Service Mesh</code>，同时额外引入的大量 <code class="prettyprint">Service Mesh</code> 服务实例的运维和管理也是一个挑战。</li></ul><br>
<br>随着服务网格的规模和复杂性不断的增长，它将会变得越来越难以理解和管理。<br>
<br><code class="prettyprint">Service Mesh</code> 的需求包括服务发现、负载均衡、故障恢复、度量和监控等。<code class="prettyprint">Service Mesh</code> 通常还有更复杂的运维需求，比如 <code class="prettyprint">A/B</code> 测试、金丝雀发布、速率限制、访问控制和端到端认证。<br>
<br><code class="prettyprint">Service Mesh</code> 的出现，弥补了 <code class="prettyprint">Kubernetes</code> 在微服务的连接、管理和监控方面的短板，为 <code class="prettyprint">Kubernetes</code> 提供更好的应用和服务管理。因此，<code class="prettyprint">Service Mesh</code> 的代表 <code class="prettyprint">Istio</code>  一经推出，就被认为是可以和 <code class="prettyprint">Kubernetes</code> 形成双剑合璧效果的微服务管理的利器，受到了业界的推崇。<br>
<br><code class="prettyprint">Istio</code> 提供了对整个服务网格的行为洞察和操作控制的能力，以及一个完整的满足微服务应用各种需求的解决方案。<code class="prettyprint">Istio</code> 主要采用一种一致的方式来保护、连接和监控微服务，降低了管理微服务部署的复杂性。<br>
<h3>初识 Istio</h3><code class="prettyprint">Istio</code> 发音「意丝帝欧」，重音在<strong>意</strong>上。官方给出的 <code class="prettyprint">Istio</code> 的总结，简单明了：  <br>
<br><blockquote><br>Istio lets you connect, secure, control, and observe services.</blockquote>连接、安全、控制和观测服务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/498e3e060918939977c2ca3f1256a566.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/498e3e060918939977c2ca3f1256a566.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
简单来说，<code class="prettyprint">Istio</code> 针对现有的服务网格，提供一种简单的方式将连接、安全、控制和观测的模块，与应用程序或服务隔离开来，从而开发人员可以将更多的精力放在核心的业务逻辑上，以下是 <code class="prettyprint">Istio</code> 的核心功能：<br>
<ol><li><code class="prettyprint">HTTP</code>、<code class="prettyprint">gRPC</code>、<code class="prettyprint">WebSocket</code> 和 <code class="prettyprint">TCP</code> 流量的自动负载均衡；  </li><li>通过丰富的路由规则、重试、故障转移和故障注入，可以对流量行为进行细粒度控制；  </li><li>可插入的策略层和配置 <code class="prettyprint">API</code>，支持访问控制、速率限制和配额；  </li><li>对出入集群入口和出口中所有流量的自动度量指标、日志记录和追踪；  </li><li>通过强大的基于身份的验证和授权，在集群中实现安全的服务间通信。</li></ol><br>
<br>从较高的层面来说，<code class="prettyprint">Istio</code> 有助于降低这些部署的复杂性，并减轻开发团队的压力。它是一个完全开源的服务网格，作为透明的一层接入到现有的分布式应用程序里。它也是一个平台，拥有可以集成任何日志、遥测和策略系统的 <code class="prettyprint">API</code> 接口。<br>
<br><code class="prettyprint">Istio</code> 多样化的特性使我们能够成功且高效地运行分布式微服务架构，并提供保护、连接和监控微服务的统一方法。<br>
<h3>核心特性</h3><code class="prettyprint">Istio</code> 以统一的方式提供了许多<strong>跨服务网格</strong>的关键功能：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/ff56f3d39cb05b44e9edede4f9500f5c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/ff56f3d39cb05b44e9edede4f9500f5c.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>流量管理</h4><code class="prettyprint">Istio</code> 简单的规则配置和流量路由允许我们控制服务之间的流量和 <code class="prettyprint">API</code> 调用过程。<code class="prettyprint">Istio</code> 简化了服务级属性（如熔断器、超时和重试）的配置，并且让它轻而易举的执行重要的任务（如 <code class="prettyprint">A/B</code> 测试、金丝雀发布和按流量百分比划分的分阶段发布）。<br>
<br>有了更好的对流量的可视性和开箱即用的故障恢复特性，我们就可以在问题产生之前捕获它们，无论面对什么情况都可以使调用更可靠，网络更健壮。<br>
<h4>安全</h4><code class="prettyprint">Istio</code> 的安全特性解放了开发人员，使其只需要专注于应用程序级别的安全。<br>
<br><code class="prettyprint">Istio</code> 提供了<strong>底层的安全通信通道</strong>，并为大规模的<strong>服务通信管理认证、授权和加密</strong>。有了 <code class="prettyprint">Istio</code>，服务通信在默认情况下就是受保护的，可以在跨不同协议和运行时的情况下实施一致的策略，而所有这些都只需要很少甚至不需要修改应用程序。<br>
<br><code class="prettyprint">Istio</code> 是独立于平台的，可以与 <code class="prettyprint">Kubernetes</code>（或基础设施）的网络策略一起使用。但它更强大，能够在网络和应用层面保护 <code class="prettyprint">Pod</code> 到 <code class="prettyprint">Pod</code> 或者服务到服务之间的通信。<br>
<h4>可观察性</h4><code class="prettyprint">Istio</code> 健壮的<strong>追踪、监控和日志特性</strong>让我们能够深入的<strong>了解服务网格部署</strong>。通过 <code class="prettyprint">Istio</code> 的监控能力，可以真正的了解到服务的性能是如何影响上游和下游的。而它的定制 <code class="prettyprint">Dashboard</code> 提供了对所有服务性能的可视化能力，并让我们看到它如何影响其他进程。<br>
<br><code class="prettyprint">Istio</code> 的 <code class="prettyprint">Mixer</code> 组件负责<strong>策略控制</strong>和<strong>遥测数据收集</strong>。它提供了后端抽象和中介，将一部分 <code class="prettyprint">Istio</code> 与后端的基础设施实现细节隔离开来，并为运维人员提供了对网格与后端基础实施之间交互的细粒度控制。<br>
<br>所有这些特性都使我们能够更有效地设置、监控和加强服务的 <code class="prettyprint">SLO</code>。当然，底线是我们可以快速有效地检测到并修复出现的问题。<br>
<h4>平台支持</h4><code class="prettyprint">Istio</code> 独立于平台，被设计为可以在各种环境中运行，包括跨云、内部环境、<code class="prettyprint">Kubernetes</code>、<code class="prettyprint">Mesos</code> 等等。我们可以在 <code class="prettyprint">Kubernetes</code> 或是装有 <code class="prettyprint">Consul</code> 的 <code class="prettyprint">Nomad</code> 环境上部署 <code class="prettyprint">Istio</code>。<br>
<br><code class="prettyprint">Istio</code> 目前支持：<br>
<ul><li><code class="prettyprint">Kubernetes</code> 上的服务部署</li><li>基于 <code class="prettyprint">Consul</code> 的服务注册</li><li>服务运行在独立的虚拟机上</li></ul><br>
<br><h4>整合和定制</h4><code class="prettyprint">Istio</code> 的策略实施组件可以扩展和定制，与现有的 <code class="prettyprint">ACL</code>、日志、监控、配额、审查等解决方案集成。<br>
<h3>流程架构</h3><code class="prettyprint">Istio</code> 服务网格逻辑上分为<strong>数据平面</strong>（<code class="prettyprint">Control Plane</code>）和<strong>控制平面</strong>（<code class="prettyprint">Data Plane</code>），架构图如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/6079b0b89f6f5057109b0aa42a8344b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/6079b0b89f6f5057109b0aa42a8344b4.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
1、**数据平面 <code class="prettyprint">Data Plane</code> **由一组以 <code class="prettyprint">Sidecar</code> 方式部署的智能代理 <code class="prettyprint">Envoy</code> 组成。<br>
<br><code class="prettyprint">Envoy</code> 被部署为 <code class="prettyprint">Sidecar</code>，和对应服务在同一个 <code class="prettyprint">Kubernetes Pod</code> 中。这允许 <code class="prettyprint">Istio</code> 将大量关于流量行为的信号作为属性提取出来，而这些属性又可以在 <code class="prettyprint">Mixer</code> 中用于执行策略决策，并发送给监控系统，以提供整个网格行为的信息。<br>
<br>这些代理可以调节和控制微服务及 <code class="prettyprint">Mixer</code> 之间所有的网络通信。<br>
<br>2、**控制平面 <code class="prettyprint">Control Plane</code> **负责管理和配置代理来路由流量，此外配置 <code class="prettyprint">Mixer</code> 以实施策略和收集遥测数据。主要包含如下几部分内容：<br>
<ul><li><code class="prettyprint">Mixer</code>：策略和请求追踪；</li><li><code class="prettyprint">Pilot</code>：提供服务发现功能，为智能路由（例如 <code class="prettyprint">A/B</code> 测试、金丝雀部署等）和弹性（超时、重试、熔断器等）提供流量管理功能；</li><li><code class="prettyprint">Citadel</code>：分发 <code class="prettyprint">TLS</code> 证书到智能代理；</li><li><code class="prettyprint">Sidecar injector</code>：可以允许向应用中无侵入的添加功能，避免为了满足第三方需求而添加额外的代码。</li></ul><br>
<br><h3>核心模块</h3>上文提到了很多技术名词，我们需要重点解释一下：<br>
<h4>什么是 <code class="prettyprint">Sidecar</code> 模式？</h4><code class="prettyprint">Sidecar</code> 是一种将应用功能从应用本身剥离出来作为单独进程的设计模式，可以允许向应用中无侵入的添加功能，避免为了满足第三方需求而添加额外的代码。<br>
<br>在软件架构中，<code class="prettyprint">Sidecar</code> 附加到主应用，或者叫父应用上，以扩展、增强功能特性，同时 <code class="prettyprint">Sidecar</code> 与主应用是<strong>松耦合</strong>的。<br>
<br><code class="prettyprint">Sidecar</code> 是一种单节点多容器的应用设计形式，主张以额外的容器来扩展或增强主容器。<br>
<h4><code class="prettyprint">Envoy</code> 的作用是什么？</h4><code class="prettyprint">Envoy</code> 是一个独立的进程，旨在与每个应用程序服务器一起运行。所有 <code class="prettyprint">Envoy</code> 组成了一个透明的通信网格，其中每个应用程序发送和接收来自本地主机的消息，并且不需要知道网络拓扑。<br>
<br>与传统的服务通信服务的库方法相比，<strong>进程外架构</strong>有两个实质性好处：<br>
<ul><li><code class="prettyprint">Envoy</code> 支持任何编程语言写的服务。只用部署一个  <code class="prettyprint">Envoy</code>  就可以在 <code class="prettyprint">Java</code>、<code class="prettyprint">C++</code>、<code class="prettyprint">Go</code>、<code class="prettyprint">PHP</code>、<code class="prettyprint">Python</code> 等服务间形成网格。</li><li>任何使用过大型面向服务的体系结构的人都知道，部署库升级可能会非常痛苦。<code class="prettyprint">Envoy</code> 可以在整个基础设施中迅速部署和升级。</li></ul><br>
<br><code class="prettyprint">Envoy</code> 以透明的方式弥合了面向服务的体系结构使用多个应用程序框架和语言的情况。<br>
<h4><code class="prettyprint">Mixer</code></h4><code class="prettyprint">Mixer</code> 是一个独立于平台的组件，负责在服务网格上执行<strong>访问控制</strong>和<strong>使用策略</strong>，并从 <code class="prettyprint">Envoy</code> 代理和其他服务收集遥测数据，代理提取请求级属性，发送到 <code class="prettyprint">Mixer</code> 进行评估。有关属性提取和策略评估的更多信息，请参见 <code class="prettyprint">Mixer</code> 配置。<br>
<br><code class="prettyprint">Mixer</code> 中包括一个灵活的插件模型，使其能够接入到各种主机环境和基础设施后端，从这些细节中抽象出 <code class="prettyprint">Envoy</code> 代理和 <code class="prettyprint">Istio</code> 管理的服务。<br>
<h4><code class="prettyprint">Pilot</code></h4>控制面中负责流量管理的组件为 <code class="prettyprint">Pilot</code>，它为 <code class="prettyprint">Envoy Sidecar</code> 提供服务发现功能，为智能路由（例如 <code class="prettyprint">A/B</code> 测试、金丝雀部署等）和弹性（超时、重试、熔断器等）提供流量管理功能。它将控制流量行为的高级路由规则转换为特定于 <code class="prettyprint">Envoy</code> 的配置，并在运行时将它们传播到 <code class="prettyprint">Sidecar</code>。<br>
<h4><code class="prettyprint">Istio</code> 如何保证服务通信的安全？</h4><ul><li><code class="prettyprint">Istio</code> 以可扩缩的方式管理微服务间通信的<strong>身份验证、授权和加密</strong>。<code class="prettyprint">Istio</code> 提供基础的安全通信渠道，使开发者可以专注于<strong>应用层级</strong>的安全。</li><li><br><code class="prettyprint">Istio</code> 可以<strong>增强微服务及其通信</strong>（包括服务到服务和最终用户到服务的通信）的安全性，且不需要更改服务代码。<br>
<br>它为每个服务提供基于角色的强大身份机制，以实现跨集群、跨云端的互操作性。</li><li><br>如果我们结合使用 <code class="prettyprint">Istio</code> 与 <code class="prettyprint">Kubernetes</code>（或基础架构）网络政策 <code class="prettyprint">Pod</code> 到 <code class="prettyprint">Pod</code> 或服务到服务的通信在网络层和应用层都将安全无虞。<code class="prettyprint">Istio</code> 以 <code class="prettyprint">Google</code> 的<strong>深度防御策略为基础</strong>构建而成，以确保微服务通信的安全。<br>
<br>当我们在  <code class="prettyprint">Google Cloud</code>  中使用  <code class="prettyprint">Istio</code>  时，<code class="prettyprint">Google</code>  的基础架构可让我们构建真正安全的应用部署。</li><li><br><code class="prettyprint">Istio</code> 可确保服务通信在默认情况下是安全的，并且我们可以<strong>跨不同协议和运行时一致地实施安全政策</strong>，而只需对应用稍作调整，甚至无需调整。</li></ul><br>
<br><h3>Envoy 进阶</h3><code class="prettyprint">Istio</code> 使用 <code class="prettyprint">Envoy</code>  代理的扩展版本，<code class="prettyprint">Envoy</code> 是以 <code class="prettyprint">C++</code> 开发的高性能代理，用于<strong>调解服务网格中所有服务的所有入站和出站流量</strong>。<br>
<br><code class="prettyprint">Envoy</code> 的许多内置功能被  <code class="prettyprint">Istio</code>  发扬光大，例如：<br>
<ul><li>动态服务发现</li><li>负载均衡</li><li><code class="prettyprint">TLS</code> 终止</li><li><code class="prettyprint">HTTP2 &amp; gRPC</code> 代理</li><li>熔断器</li><li>健康检查、基于百分比流量拆分的灰度发布</li><li>故障注入</li><li>丰富的度量指标</li></ul><br>
<br><code class="prettyprint">Envoy</code> 分为主线程、工作线程、文件刷新线程，其中主线程就是负责工作线程和文件刷新线程的管理和调度。而工作线程主要负责监听、过滤和转发，工作线程里面会包含一个监听器，如果收到一个请求之后会通过过滤链来进行数据过滤。前面两个都是非阻塞的，唯一一个阻塞的是这种 <code class="prettyprint">IO</code> 操作的，会不断地把内存里面一些缓存进行落盘。<br>
<br>总结来说，我们可以围绕如下 5 方面：<br>
<h4>服务的动态注册和发现</h4><code class="prettyprint">Envoy</code> 可以选择使用一组分层的动态配置 <code class="prettyprint">API</code> 来进行集中管理。<br>
<br>这些层为 <code class="prettyprint">Envoy</code> 提供了动态更新，后端群集的主机、后端群集本身、<code class="prettyprint">HTTP</code> 路由、侦听套接字和通信加密。为了实现更简单的部署，后端主机发现可以通过 <code class="prettyprint">DNS</code> 解析（甚至完全跳过）完成，层也可以替换为静态配置文件。<br>
<h4>健康检查</h4>构建 <code class="prettyprint">Envoy</code> 网格的建议方法是将<strong>服务发现</strong>视为最终一致的过程。  <code class="prettyprint">Envoy</code> 包括一个运行状况检查子系统，该子系统可以选择对上游服务集群执行主动运行状况检查。<br>
<br>然后，<code class="prettyprint">Envoy</code> 使用服务发现和运行状况检查信息的联合来确定健康的负载均衡服务器。<code class="prettyprint">Envoy</code> 还支持通过<strong>异常检测子系统</strong>进行被动运行状况检查。<br>
<h4>高级负载均衡</h4>分布式系统中不同组件之间的负载平衡是一个复杂的问题。<br>
<br>由于 <code class="prettyprint">Envoy</code> 是一个独立的代理而不是库，因此它能够在一个位置实现<strong>高级负载平衡</strong>技术，并使任何应用程序都可以访问。<br>
<br>目前 <code class="prettyprint">Envoy</code> 包括支持自动重试、断路、通过外部速率限制服务限制全局速率、请求隐藏和异常值检测。未来计划为 <code class="prettyprint">Request Racing</code> 提供支持。<br>
<h4>前端/边缘系统代理支持</h4>虽然 <code class="prettyprint">Envoy</code> 主要是为<strong>服务通信系统而设计</strong>的，但对前端/边缘系统也是很有用的，如：可观测性、管理、相同的服务发现和负载平衡算法等。<br>
<br><code class="prettyprint">Envoy</code> 包含足够的功能，使其可用作大多数  <code class="prettyprint">Web</code>  应用服务用例的边缘代理。这包括作为 <code class="prettyprint">TLS</code> 的终点、<code class="prettyprint">HTTP/1.1</code> 和 <code class="prettyprint">HTTP/2</code> 支持，以及 <code class="prettyprint">HTTP L7</code> 路由。<br>
<h4>最好的观察统计能力</h4><code class="prettyprint">Envoy</code> 的首要目标是使<strong>网络透明</strong>。但是在网络级别和应用程序级都无法避免的容易出现问题。<code class="prettyprint">Envoy</code> 包含了对所有子系统的强有力的统计支持。  <code class="prettyprint">statsd</code> 和其他兼容的数据提供程序是当前支持的统计接收器，插入不同的统计接收器也并不困难。<br>
<br><code class="prettyprint">Envoy</code> 可以通过管理端口查看统计信息，还支持通过第三方供应商进行分布式追踪。<br>
<br>更多详情请参考：<a href="https://www.jianshu.com/p/a6f7f46683e1" rel="nofollow" target="_blank">https://www.jianshu.com/p/a6f7f46683e1</a><br>
<h3>方案畅想</h3>应用上面的原理，我们可以有很多具体的方案应用于日常开发。<br>
<h4>方案一：应用 <code class="prettyprint">Istio</code> 改造微服务</h4>模仿在线书店的一个分类，显示一本书的信息。 页面上会显示一本书的描述，书籍的细节（<code class="prettyprint">ISBN</code>、页数等），以及关于这本书的一些评论。<br>
<br><strong>应用的端到端架构：</strong><code class="prettyprint">Bookinfo</code> 应用中的几个微服务是由不同的语言编写的。 这些服务对 <code class="prettyprint">Istio</code> 并无依赖，但是构成了一个有代表性的服务网格的例子：它由多个服务、多个语言构成，并且 <code class="prettyprint">reviews</code> 服务具有多个版本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/055e269a6df9fbf749eedb5759396da7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/055e269a6df9fbf749eedb5759396da7.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>用 <code class="prettyprint">Istio</code> 改造后架构如下</strong>：要在 <code class="prettyprint">Istio</code> 中运行这一应用，无需对应用自身做出任何改变。我们只需要把 <code class="prettyprint">Envoy Sidecar</code> 注入到每个服务之中。最终的部署结果将如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/f7897f069d24b36b66291aafc90b5fab.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/f7897f069d24b36b66291aafc90b5fab.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
所有的微服务都和 <code class="prettyprint">Envoy Sidecar</code>  集成在一起，被集成服务所有的<strong>出入流量</strong>都被 <code class="prettyprint">Sidecar</code> 所劫持，这样就为外部控制准备了所需的 <code class="prettyprint">Hook</code>，然后就可以利用 <code class="prettyprint">Istio</code> 控制平面为应用提供服务路由、遥测数据收集以及策略实施等功能。<br>
<br>更多细节，请移步官网示例：<a href="https://istio.io/latest/zh/docs/examples/bookinfo/" rel="nofollow" target="_blank">https://istio.io/latest/zh/docs/examples/bookinfo/</a><br>
<h4>方案二：用 <code class="prettyprint">Istio</code> 改造 <code class="prettyprint">CI/CD</code> 流程</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/b4111c51769ba9ccd98dd620bb61f4cf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/b4111c51769ba9ccd98dd620bb61f4cf.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对上述流程图简单解释一下：<br>
<ul><li>通过 <code class="prettyprint">Docker</code> 对代码进行容器化处理；</li><li>通过 <code class="prettyprint">Gitlab</code> 托管代码；</li><li><code class="prettyprint">Jenkins</code> 监听 <code class="prettyprint">Gitlab</code> 下的代码，触发自动构建，并执行 <code class="prettyprint">Kustomize</code> 文件；</li><li><code class="prettyprint">Kustomize</code> 通过配置文件，设置了 <code class="prettyprint">Istio</code> 的配置（染色识别、流量分发），并启动 <code class="prettyprint">Kubernetes</code> 部署应用；</li><li>最终我们通过 <code class="prettyprint">Rancher</code> 来对多容器进行界面化管理；</li><li>打开浏览器进行访问。</li></ul><br>
<br>看到这里，相信你也了解了，我们实现了一个<strong>前端多容器化部署</strong>的案例。它有什么意义呢？<br>
<ul><li>首先，当然是环境隔离了，研发每人一个容器开发，互不干扰；</li><li>其次，我们可以做很多小流量、灰度发布等事情；</li><li>自动化部署，一站式的流程体验。</li></ul><br>
<br>如果你对容器化还不太了解，请先看看前面两篇文章：<br>
<ul><li>《<a href="http://dockone.io/article/10551"><code class="prettyprint">Docker</code> 边学边用</a>》</li><li>《<a href="http://dockone.io/article/10564">一文了解 <code class="prettyprint">Kubernetes</code></a>》</li></ul><br>
<br><code class="prettyprint">Istio</code> 还是有很多可圈可点的地方，相信看到这里你也有了更全面的认识。如果你想深入了解，不妨仔细研究官方示例，并且在实际项目中不断打磨。<br>
<br>原文链接：<a href="http://jartto.wang/2020/07/29/istio-1/" rel="nofollow" target="_blank">http://jartto.wang/2020/07/29/istio-1/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            