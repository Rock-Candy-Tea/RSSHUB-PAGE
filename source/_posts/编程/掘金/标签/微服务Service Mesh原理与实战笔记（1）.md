
---
title: '微服务Service Mesh原理与实战笔记（1）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa1baa81bb24e3797ac2d058d135d7a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 22:38:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa1baa81bb24e3797ac2d058d135d7a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">开篇词 | Service Mesh，传统微服务架构新的里程碑</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa1baa81bb24e3797ac2d058d135d7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34e9fa221a774ce9af81063b265e83f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Service Mesh （服务网格）是一个用于处理服务和服务之间通信的基础设施层，它最重要的变革，就是引入了数据面和控制面的概念：通过 sidecar 模式将原本在 SDK 中的代码独立出来，用控制面代替配置中心的部分功能，以透明代理的形式提供安全、快速、可靠的服务间通信，同时也能实现微服务所需的基本组件功能。</p>
<p>实际上，Service Mesh 需要的基础组件和传统的微服务并没有太大的差别，很多公司选择自研控制面的原因，很多就是出于兼容老的微服务的基础组件的考虑，你可以把 Service Mesh 看作是分布式的微服务代理。</p>
<p>后来由于容器技术的火爆，作为 Service Mesh 的代表 Istio 也顺理成章成为业界明星</p>
<h2 data-id="heading-1">导读 | Service Mesh：从单体服务出发，独立于业务演进的微服务架构</h2>
<ul>
<li>没有银弹</li>
</ul>
<p>与其他现存的架构和解决方案一样，微服务架构也不是银弹。
当然它解决了单体服务很多问题，但同时也带来了单体服务中一些没有的问题，
比如负载均衡、服务治理、服务注册发现、如何拆分服务等，当然其中的大部分问题，都可以通过技术手段解决，但也增加了系统的复杂性。</p>
<ul>
<li>Service Mesh 的基础组件及常见名词</li>
</ul>
<p>Service Mesh 一个最重要的变革，就是引入了数据面和控制面的概念，这个概念也并非 Service Mesh 新创的概念，实际上在 SDN (软件定义网络)中就有了控制面和数据面的概念。</p>
<p>在课程正式开始前，我们先简单了解一下控制面和数据面。</p>
<ul>
<li>数据面(Data Plane)</li>
</ul>
<p>负责数据的转发，一般我们常见的通用网关、Web Server，
比如 Nginx、Traefik 都可以认为是数据面的一种。
在 Service Mesh 的开源世界中，Envoy 可以说是最知名的数据面了。</p>
<p>另外数据面并非局限于网关类产品，实际上某些 RPC 框架也可以充当数据面，比如 gRPC 就已经支持完整的 xDS(数据面和控制面的交互协议)，也可以当作数据面使用。一般我们把负责数据转发的数据面称为 sidecar（边车）。</p>
<ul>
<li>控制面(Control Plane)</li>
</ul>
<p>通过 xDS 协议对数据面进行配置下发，以控制数据面的行为，比如路由转发、负载均衡、服务治理等配置下发。
控制面的出现解决了无论是框架还是数据面、sidecar 都缺乏控制能力的弊端，而且之前只能通过运维批量修改 CONF 来控制数据面、导致规模上升时纯人工维护成本以及大幅度上升的错误概率等问题也得到了很好的解决。</p>
<p>实际上 Service Mesh 需要的基础组件和传统的微服务没有太大的差别，很多公司选择自研控制面就是为了兼容老版本微服务的基础组件。</p>
<p>下面我们一起看一下 Service Mesh 的基础组件。</p>
<p>服务注册中心：服务间通信的基础组件。
服务通过注册自身节点，让调用方服务发现被调方服务节点，以达到服务间点对点通信的目的。</p>
<p>配置中心：用于服务的基础配置更新，以达到代码和配置分离的目的。减少服务的发布次数，配置发布可以更快更及时地变更服务。</p>
<p>API 网关：通过统一的网关层，收敛服务的统一鉴权层、链路 ID 生成等基础服务，并聚合后端服务为客户端提供 RESTful 接口。
另外 API 网关也负责南北向流量(外网入口流量)的流量治理。</p>
<p>服务治理：通过限流、熔断等基础组件，杜绝微服务架构出现雪崩的隐患。</p>
<p>链路追踪：通过 trace 将整个微服务链路清晰地绘制出来，并进行精准的故障排查，极大地降低了故障排查的难度。</p>
<p>监控告警：通过 Prometheus 和 Grafana 这样的基础组件，绘制服务状态监控大盘，针对资源、服务、业务各项指标，做精准的监控报警。</p>
<p>说完了基础组件，再说一下一些常见的名词解释，便于你理解 Service Mesh。</p>
<p>Upstream: 上游服务，如果 A 服务调用 B 服务，在 A 服务的视角来看，B 服务就是上游服务，但是在中文的语境中，经常被叫作“下游服务”。所以在整个课程中，为了避免语言上的歧义，我会直接使用upstream，而不是中文翻译。在中文的语境中，我更喜欢称它为服务端或者被调用方。</p>
<p>Downstream: 下游服务，如果 A 服务调用 B 服务，在 B 服务的视角中，A 服务就是下游服务。在中文的语境中，我更喜欢叫客户端或者调用方。</p>
<p>Endpoint：指的是服务节点，比如 A 服务有 192.168.2.11 和 192.168.2.12 两个服务节点。</p>
<p>Cluster：指的是服务集群，比如 A 服务有 192.168.2.11 和 92.168.2.12 两个服务节点，那么A服务就是 Cluster，也可以直接理解为 Service。</p>
<p>Node：在 Kubernetes 语境中，指的是承载 pod 的服务器，但在微服务的语境中，更多的等同于Endpoint。</p>
<p>Route：指的是 Service Mesh 中的路由配置，比如 A 服务访问 B 服务，要匹配到一定的规则，比如 header 中要带有服务名(-H servicename:B)，才能够拿到 B 服务的访问方式，通过服务发现或者静态列表访问到 B 服务的节点。</p>
<p>Listener：指的是 Service Mesh 的监听端口，通常我们访问 Service Mesh 的数据面，需要知道数据面的监听端口</p>
<h2 data-id="heading-2">组件：01 | 注册中心：微服务的重中之重</h2>
<ul>
<li>
<p>服务注册与发现就是保证当服务上下线发生变更时，
服务消费者和服务提供者能够保持正常通信。</p>
<p>注册中心是微服务中最重要的内容，也是和 SOA 架构中的集中总线通信最大的区别点。今天，我就跟你聊一聊注册中心</p>
</li>
<li>
<p>服务注册发现</p>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4867e102164e4eb299c7097302b157b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>服务注册发现最大的用处就是解决需要在网关或者 LB 中，手动配置服务地址的问题。你可以无须手动配置，自动地让调用端服务发现被调用端服务的机器节点</p>
<blockquote>
<p>所以在选型的时候，优先选择 AP 的系统。</p>
</blockquote>
<p>如果技术栈是 Go ，但又担心 Java 的组件不好维护，你也可以考虑自研注册中心，当然 CP 的注册中心并非不可用，在服务集群规模比较小的情况下，也是可以选择的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/276a00dd4a6b489dab9bd774df02dfd6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">组件02 | 注册中心：如何搭建一个高可用、健壮的注册中心？</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a990ab8ca7d4776829f9de3f343d1ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a25423c7a2349109ff43d2c9cee8c83~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/276656b832204425b1c9dcd38f3adb7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了用传统的注册中心组件外，Kubernetes 内部的发现机制在 Service Mesh 中也得到了广泛应用，例如 Istio通过监听 Kubernetes Pod 的变化，实现服务发现的功能，这样就不需要服务自身来做服务注册了。</p>
<p>那么 Service Mesh 中实现的注册发现功能，相比传统微服务有哪些优势呢？</p>
<ol>
<li>无须服务自身注册，由 sidecar 代理注册</li>
</ol>
<p>sidecar 通过接受控制面下发的配置信息，进行服务注册。相对于服务自身注册，这样可以减少服务自身开发的工作量，同时也很容易做到注册的配置信息一致化。比如如果服务自己注册，其实很难控制服务注册的 metadata 信息，在 SDK 中很难约束和升级，比如运行环境、地域、健康检查方式等。</p>
<p>sidecar 代理还带来了可以随时更新 meta 信息的好处。在传统的 SDK 模式中，你想要动态调整服务的权重、metadata 等信息的时候，需要重新发布版本，或者依靠配置中心的能力，但这些控制信息往往散落在各个服务中，不方便管理，在 Service Mesh 中你只需要依靠控制面的能力，就可以轻松做到了。</p>
<ol start="2">
<li>通过控制面聚合多种、多个注册中心数据</li>
</ol>
<p>像 Istio 的 pilot 模块，在 1.1 版本就支持了单控制面多集群的功能，通过 pilot 将多个注册中心的数据聚合，可以有效降低单一注册中心的读写压力，使注册中心更容易水平扩展。</p>
<p>比如在实践中，我就将多个 Consul 数据中心的数据通过 pilot 模块聚合，然后提供 xDS 协议，供服务发现使用，实现了虚拟机到 Kubernetes 环境的无缝迁移。</p>
<ol start="3">
<li>通过 sidecar 提供服务正确性 check 功能</li>
</ol>
<p>上一讲我们提到过，在注册中心中，有一种健康检查方式是注册中心主动 ping 服务的模式。实际上如果服务 IP 发生变化，又用了同样的 ping 接口时，健康检查会出现错误。
而通过 sidecar 模式，当发现服务 ping 接口过来的流量时，进行服务名称的检测，通过 header 中增加服务名称与本地服务名称做校验的方式进行检测，可以有效避免这样的错误。</p>
<h3 data-id="heading-4">FQA</h3>
<p>老师你好，我想问问servicemesh架构对比传统微服务
架构最大的优势是什么？网上文章也看了很多，但面试回答还是有点困惑</p>
<p>讲师回复： 大多数人只能回答上来多语言的兼容性、不用开发多套语言的 SDK，却忽略了基础设施可以单独演进的核心点。
比如对于传统的微服务架构来说，
当服务数量变多时，升级 SDK 将变成一件不可能的事情。</p>
<p>1
推荐使用 AP，为啥 k8s 使用 etcd 呢？</p>
<p>讲师回复： 在大规模的k8s集群场景下，etcd也是已知的性能瓶颈点，很多公司已经魔改etcd，或者采用其他的存储方式了。由于etcd的瓶颈问题，k8s的集群规模也受到限制，现在比较常见的是搭建多套k8s集群</p>
<p>现在大家不都用的zk,etcd,为这里推荐AP类型的呢？</p>
<p>讲师回复： 注意看文章的内容，“CP 的注册中心并非不可用，
在服务集群规模比较小的情况下，也是可以选择的”。</p>
<p>Eureka 典型的 AP,作为分布式场景下的服务发现的产品较为合适，服务发现场景的可用性优先级较高，一致性并不是特别致命。</p>
<p>其次 CP 类型的场景 Consul,也能提供较高的可用性，并能 k-v store 服务保证一致性。而Zookeeper、Etcd则是CP类型牺牲可用性，在服务发现场景并没太大优势。</p></div>  
</div>
            