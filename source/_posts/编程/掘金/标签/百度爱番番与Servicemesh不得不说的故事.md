
---
title: '百度爱番番与Servicemesh不得不说的故事'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1091998539cb480e908368cdffd3a027~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 31 May 2021 18:11:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1091998539cb480e908368cdffd3a027~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1091998539cb480e908368cdffd3a027~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>导读</strong>：服务网格（ Servicemesh ）于 2018 年夏天随着 Istio1.0 的正式发布席卷全球，国内各大公司也遍地开花，其所带来的理念逐步为各方所接受并风靡。爱番番基于自身的痛点和 ToB 行业的特点，携手公司基础架构，于 2020 年 8 月底正式启动了 Servicemesh 项目，仅用 3 个月就快速完成了 Java 业务应用的全切，成为百度第一个将商用生产系统完全基于原生 Kubernetes + Istio 运行的产品。</p>
<p><em>全文6492字，预计阅读时间12分钟。</em></p>
<h1 data-id="heading-0"><strong>一、缘起：沉浸式治理</strong></h1>
<p>爱番番作为一站式智能营销和销售的加速器，旨在助力企业实现业务增长。在沟通、营销、销售、洞察等领域持续发力，在 ToB SaaS 行业中面临着激烈的竞争，这就意味着在技术上对系统稳定性和研发人效有着非常高的要求。而回头来看，当下爱番番在业务上面临着诸多挑战：</p>
<p><strong>1.多语言治理难</strong>。存在着 Java、Golang、Nodejs、Python 等语言，在服务治理上主要支撑 Java 的需求，其余语言的治理或自成一套，或基本缺失。其将带来很大的治理成本和系统风险。</p>
<p><strong>2.业务耦合</strong>。当前采用 Smart Client 的服务治理框架，推动迭代升级困难。服务治理的周期平均在三个月以上，带来极大的运维升级成本。</p>
<p><strong>3.能力缺失</strong>。当前采用的服务治理框架缺乏足够的治理手段，如限流熔断、混沌、金丝雀、服务分组、流量录制回放、动态配置等能力的支持。</p>
<p><strong>4.人肉配置</strong>。当前服务治理框架将治理粒度全部降到方法级，其直接导致过于大量（ 2k+ 方法）的人肉配置要求带来的事实上的不可配置。直接导致爱番番服务治理平台处于事实上的无人使用状态。也正因此出过一些严重的线上问题。</p>
<p>因而服务治理的现状即：治理边际成本无法下降，反而呈指数上升趋势，治理由于成本过高只能基于问题驱动进行。这也是业内很多公司服务治理的现状。最终在效能、稳定性、能力三方面，都面临着很大的挑战。同时，由于居高不下的治理成本，我们业务上要进行「 多云/私有化部署 」的售卖目标看起来将会遥遥无期。</p>
<p>笔者称这种治理为：<strong>沉没式治理。看着永远在治理，其实永远在沉没。</strong></p>
<h1 data-id="heading-1"><strong>二、抉择：下一代的服务治理体系</strong></h1>
<p>为了解决以上问题，扭转沉没式治理的困境，我们展开了一次艰难而不得不进行的选择。是否能够有办法，既可解决 Smart Client 带来的多语言&业务耦合的难题，又可以具备功能丰富而治理粒度适宜的服务治理能力？而且考虑到有限的资源，能够以拿来主义的务实态度去进行问题的解决？</p>
<p>经过层层筛选和论述，摆在我们眼前的答案逐渐清晰了起来：服务网格（Servicemesh）。我们选择了目前的事实上的云原生标准服务网格设施：Istio。</p>
<h2 data-id="heading-2"><strong>2.1 什么是服务网格</strong></h2>
<p>服务网格（ Servicemesh，以下简称 Mesh ）概念于 2017 年春正式提出，并与2018年夏随着Google、IBM、Lyft 共建的 Istio1.0 的正式发布席卷全球。其出现主要在于解决 Smart Client 带来的一大难题 —— 「 如何解决服务治理与业务代码强耦合以及跨语言场景治理效率低下 」的问题。Mesh 给出的解决方案即：倡导将服务治理能力进行就近下沉，统一由 Sidecar 进行接管南北东西流量。这样最直接的好处即可以实现解耦，应用自身 “黑盒化”，整体服务治理进一步实现标准化，达到运营效率提升。在此之上，快速进行各种服务治理能力的增强，“一处开发，处处具备” ，彻底解放生产力，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15aa0f6e4cda4d83ba1339e91ca5e05d~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Istio 从逻辑上可以分为数据平面和控制平面，如下图：</p>
<ul>
<li>
<p>数据平面主要由一系列的智能代理（默认为 Envoy）组成，管理微服务之间的网络通信以及收集和报告所有 mesh 中的遥测数据。</p>
</li>
<li>
<p>控制平面负责管理和配置代理来路由流量。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f701484cfb74849a4fff58ce5add999~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3"><strong>2.2 服务网格的曲折前进</strong></h2>
<p>服务网格是一个新的概念，但本身并不是一个新奇的架构设计，早在十多年前，Airbnb 就已经在其治理框架 Smartstack 中进行了实践，携程的 OSP ，以及充斥在各种云（mesos/marathon、k8s）里面的服务治理解决方案都早已是类似的 Local Agent 架构。但此时，业内并未形成统一的标准，而其运维的复杂度也让诸多人望而却步。而随着 k8s 重新定义了基础设施，服务网格则应运而生重新定义了 Local Agent。</p>
<p>随着服务网格的大放异彩，对应的问题也随之而来。不少人对于 Mesh 理念延伸出的问题如性能、稳定性和资源开销表现出不同程度的担忧和质疑，其也直接导致了最具盛名的 Linkerd 的折戟，以及 Istio 架构上的曲折前进。Istio在经历了控制平面性能漫长的质疑期后，终于不破不立移除了 Mixer，引入了 WASM 机制在数据面上进行插件化能力增强。这是很艰难而勇敢的一步，但也同样会面临新的风险。</p>
<p>时至今日，是否要用 Mesh，什么时候使用 Mesh，如何用好 Mesh，Mesh 的定位和未来仍然为大家所津津乐道。这也正是其的魅力所在。而从整体上看，Istio 开源社区表现出了积极开放的心态，我们有理由相信，Istio 在成为服务网格的事实标准之后，能够不断释放更大能量。</p>
<p>纵观目前业内 Mesh 的落地情况：</p>
<p>1.腾讯云基于 Istio 推出了 TCM，支持进行集群托管或者自建，可对多地域流量管控；</p>
<p>2.蚂蚁 Sofa-Mosn 另辟蹊径，以 Golang 语言重写 Mesh 并进行独立演化，在国内大放异彩；</p>
<p>3.美团点评也正在大力推进 OCTO2.0 服务治理体系，进行基于 Envoy+ 自研控制面板的Mesh 转型；</p>
<p>4.百度内部有 BMesh 和天合Mesh 两款 Mesh 产品；</p>
<p>5.头条、快手正在进行对应的建设，网易轻舟进行了 Mesh化，陌陌构建了Java 版 Mesh；</p>
<p>6.Azure、AWS、Google Cloud 都推出了Mesh产品；</p>
<p>7. ......</p>
<p>整体情况如下图不完全列举所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6553c88dd14f4f89961f577fc4109e2f~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以进一步归纳看到：</p>
<p>1.Envoy（ Istio 默认使用了 Envoy ）已成为事实标准；</p>
<p>2.Istio 项目还在快速迭代演进并趋于生产稳定；</p>
<p>3.全球主流云厂商和国内大量公司都已落地 Mesh；</p>
<p>4.目前主流做法采用（二次开发）Envoy + 自研控制面板；</p>
<p>5.业内正在尝试通过中间件下沉享有 Mesh 红利。</p>
<p>我们的选择：</p>
<p>1.从 ROI 来说，我们并不希望自己从 0-1 去自建 Mesh，我们希望集中更多资源投入业务迭代中，所以我们抱定「 满足 80% 的能力，剩余的 20% 可以妥协可以增强 」的思路来进行下一步的选择。</p>
<p>2.从语言栈来说，由于 Mesh 本质是「 寄生 」在应用机器上的进程，所以资源控制本身尤其重要。因而现阶段选择 Java 语言来进行 Sidecar 的开发并不明智，也这是 Linkerd1.0 失败的主要原因。所以我们并不打算引入 Java 技术栈的 Mesh。</p>
<p>3.从开源生态来说，Istio 经历几年的锤炼，虽然还有诸多不完美的地方，但其以强大的能力、巨头的背书、以及生态的活跃等方面来说，已经成为业内事实上的 Mesh 标准。所以我们希望基于 Istio 构建爱番番的 Mesh 体系。</p>
<p>4.与百度基础架构的协作上，关于是否直接复用厂内的 Mesh 产品这一问题，我们与基础架构云原生的同学进行了多轮沟通，由于「 私有化 / 多云部署 」这一前提，爱番番本身希望尽量以不改变开源组件原有结构的方式进行轻量部署，如尽量不与厂内独有基础设施进行耦合、如按照完全原生的方式落地等。</p>
<p>于是爱番番和基础架构双方商定最终方案为：暂时不直接采用基础架构的 Mesh，而改由基础架构为我们运维 k8s 集群以及搭建 calico 网络，并采用百度天合产品进行集群的管控。爱番番在此基础上选择 Istio1.7 原生组件进行落地。</p>
<h2 data-id="heading-4"><strong>2.3 ToB和Toc场景对Mesh核心诉求的差异性</strong></h2>
<p>在 ToC 场景，性能往往会被高优考虑，Mesh 目前的性能（RT & OPS）并不出众，官方方案会带来几毫秒<del>十毫秒不等的延时。业内自研/二次开发方案做得较好的约在 0.5</del>2ms 之间不等。在 toc 高流量场景下，Mesh 的落地会有一定的阻碍。在性能问题解决之后，才可能会去考虑是不是能很好迁移之类的问题。</p>
<p>而在 ToB SaaS 场景，核心点即**【可移植】**，能够很好地支撑私有化、多云部署，产品需要具备良好的可迁移性和可维护性。相比之下，Mesh绝对的性能要求在中前期并不是需要最高优考量的点。而在中后期，随着中间件能力的下沉，更高的性能要求才会逐步提上议程。</p>
<p>即二者差异性：</p>
<ul>
<li>
<p><strong>ToC场景：【性能】早于【可移植】考虑</strong></p>
</li>
<li>
<p><strong>ToB场景：【可移植】早于【性能】考虑</strong></p>
</li>
</ul>
<p>而爱番番，则是典型的 ToB 场景。Mesh 在做开箱即用上，能够很好地起到作用。</p>
<h1 data-id="heading-5"><strong>三、实践：平滑迁移与赋能业务</strong></h1>
<h2 data-id="heading-6"><strong>3.1 爱番番现状</strong></h2>
<p>爱番番目前拥有华北、华南、华东3个 IDC，300+ 的 k8s node，300+ 的应用，3k+ 的服务点，8k+ 的pod。日均 10+ 亿pv。主业务产品大多部署在华东集群上，因而本次迁移主要针对华东集群。</p>
<h2 data-id="heading-7"><strong>3.2 平滑迁移</strong></h2>
<hr>
<h3 data-id="heading-8"><strong>3.2.1 POC验证</strong></h3>
<p>我们选择了 Istio1.7 版本，以爱番番的实际使用场景作为基准进行 POC 的性能测试后，发现单机性能暂时可以满足爱番番当前需求，在单机 100 QPS 左右，引入 Istio 的性能损耗在 1%以下。并且基于 Istio 的核心能力进行了验证。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc1bd1bb3ea47b5a25a564d5a3c28c2~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9"><strong>3.2.2 迁移方案</strong></h3>
<p>迁移的大原则有如下几个：</p>
<p>1.监控先行；</p>
<p>2.业务方低感知；</p>
<p>3.尽可能无损。</p>
<p>基于大原则，产出的迁移方案整体架构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e39c2dfe0b2b41c0b4efc528a61aa029~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总体方案简述：以 calico 为网络设施构建一套新的 Mesh 容器网络集群，以入口网关进行灰度。两个集群之间采用 Istio-Gateway 进行通信，并在多环节进行容错处理。以 Istio 作为服务治理的核心重构基础设施。整个过程中，对于灰度迁移过程，以及新集群的表现进行可视化观察。整体迁移过程通过 CICD 以及 SDK 两个层面来最大化实现对业务方的细节屏蔽。</p>
<h3 data-id="heading-10"><strong>3.2.3 迁移难点</strong></h3>
<p>我们在实施过程中，碰到的主要难点：</p>
<ul>
<li>
<p><strong>无法进行流量闭环假设</strong>。复杂的分布式拓扑中，迁移时候极难挑选出完全闭环的子拓扑进行先行迁移验证。而一旦在没有任何准备的情况下，将服务迁移上容器网络集群，这时候调用链中的某一环仍然留在主机网络集群上，则极容易引起线上事故。为了解决这个问题：</p>
<p>1.通过 Skywalking 进行链路拓扑的观察，在迁移前期验证阶段时，尽量让流量不至过于分散；</p>
</li>
</ul>
<p>2.借助老注册中心和灰度名单，实现容器网络集群中的服务在访问非灰度应用的时候，可直连调回主机。通过这种方式，即可放心地进行服务迁移而无需关注是否进行流量闭环。</p>
<ul>
<li><strong>容器网络环境初期不稳定</strong>。在最开始迁移的初期，新集群偶尔会出现 Node、API Server等基础设施的不稳定，如果不进行任何干预和快速应对，则可能会导致严重的业务问题。为了解决这一问题，我们在多个环节进行了可用性的保障，包括：</li>
</ul>
<p>1.在基础设施层面，针对于 api server、etcd 等的抖动迅速止损和优化，并制定相应稳定性保障的 SOP；</p>
<p>2.在网关入口层面，基于任意产品线、任意灰度比例进行灰度和回切操作；</p>
<p>3.对于幂等的请求，提供失败时自动 fallback 的机制；</p>
<p>4.对于失败的请求，提供自动熔断和恢复的能力；</p>
<p>5.对于常见容易遗漏的定时任务和异步 MQ 消费者进程，进行标识后，一键回切时可进行自动缩容；</p>
<p>6.Mesh 容器集群里进行调用时，在调用方会进行连接/读取超时&重试的能力支持。</p>
<ul>
<li><strong>大规模的迁移较难对业务方屏蔽影响</strong>。基本涉及所有300+的业务应用的迁移，在高速迭代的业务场景之下，如何尽量降低业务方的成本，来实现快速的切换工作。针对这一问题，我们主要有三方面的举措：</li>
</ul>
<p>1.SDK 默认尽量向前兼容。避免业务方进行大面积改造；</p>
<p>2在 CICD层面，屏蔽了新老集群的部署细节，并可以按产品线进行按批次灰度，用一套模板来管控两套集群配置，通过这些方式实现在CICD环节对业务方的完全透明；</p>
<p>3.对于大规模迁移过程中发现的紧急问题，通过凤巢商业平台团队提供的launcher热加载机制，实现自动替换注入升级包来完成新功能的零侵入替换和快速验证。</p>
<ul>
<li><strong>对于 Istio 的引入带来的治理挑战</strong>。Istio 的引入，对于以 Smart Client 理念去构筑的原服务治理框架带来了颠覆性的改变，这块也会带来对应的适应和切换的成本，我们如下进行应对：</li>
</ul>
<p><strong>1.理念转变</strong>：整体理念即服务治理理念和模型全面向Istio靠齐，逐步放弃全部基于 ServiceID（方法级）进行治理的思路；</p>
<p><strong>2.配置优化</strong>：引入Istio后，会在整个调用链路上加入两跳，针对这两跳，重新审视连接/读取超时重试、tcp backlogsize 等核心配置的关系，避免引起不必要的稳定性故障；</p>
<p><strong>3.入口收敛</strong>：Istio 引入后绝大部分的治理能力都通过 CRD 进行交互。我们将其治理入口暂时集成在 CD 系统上，禁止在kiali等其他地方进行核心配置变更，通过入口收敛来杜绝无序混乱的线上管理；</p>
<p><strong>4.妥协增强</strong>：Istio 本身功能非常强大，但部分能力还需要进一步增强，比如限流熔断、混沌工程等，于是我们也是在 tradeoff 之后进行取舍，对于部分功能做阉割妥协（如短暂放弃集群限流），对于部分功能做补齐（如引入 chaosmesh 增强混沌）。通过这种方式，达到能够快速享受 Istio 红利的目的。</p>
<h3 data-id="heading-11"><strong>3.2.4 迁移节奏</strong></h3>
<p>Mesh 项目于20年8月底正式启动，9月初完成 POC 验证，9月底完成 MVP 交付，并切换爱番番 17% 的应用，在10月之后，进行逐步扩量，并不断增强新集群稳定性，同时开始释放 Istio能力，最终在20年11月底完成华东主集群业务应用的全量切换。整体投入5人力，仅历时3个月完成从验证到切换的过程，<strong>成为百度第一个将商用生产系统完全基于原生 Kubernetes+Istio运行的产品。</strong></p>
<h2 data-id="heading-12"><strong>3.3 红利释放</strong></h2>
<p>在完成 istio 的主体切换后，我们并没有停下脚步，而是紧接着开始进行了业务上的赋能以最大化发挥出 mesh 的价值点。我们基于 mesh 这一标准化的底座，交付了近 20个 功能点，帮助我们的业务实现了效能、稳定性、功能、成本上的全面提升。</p>
<h3 data-id="heading-13"><strong>3.3.1 全链路灰度发布</strong></h3>
<p>以一个 case 为例，爱番番的「全链路灰度发布」平台，基于istio通过同构底层「分组多维路由」的架构设计，在解决业内主流 flagger/helm 方案弊端的同时，完成了一套架构对 ABTest、金丝雀、容量评估、多路复用、Set化 在内的多个核心能力的支撑（部分能力研发进行中），对分组节点的全生命周期和流量进行了集中管控。针对于服务端场景，通过 FGR Operator 协调 k8s 以及 istio vs/dr 资源，并打通监控报警与 CICD。针对于端上场景，与对应的前端资源打包和获取的流程整合，进行用户级的打标和路由分发。这在传统解决方案中，需要付出大量的研发成本才能实现，而依托于 istio ，我们的整体资源投入得到了大幅的缩减。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af529ae7634941449158e4009e5a0896~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14"><strong>3.3.2 爱番番对Istio的应用现状</strong></h3>
<p>Istio 具备丰富的治理能力，在服务连接、服务发现、服务保护、服务可观察等方面都有丰富的能力进行支撑。目前，爱番番对 Istio 的使用包括但不限于：</p>
<p><strong>服务连接</strong></p>
<p>1.通讯：基于 Http1 的原协议长连；基于 K8s service 的服务发现；</p>
<p>2.负载均衡：默认 RR，对于特殊的应用需求（如爱番番的数据库中间件 dataio ）采用一致性哈希；</p>
<p>3.路由分组：金丝雀能力、测试环境多路复用、网关入口流量路由、abtest、开发机直连、灰度链路等。</p>
<p><strong>服务保护</strong></p>
<p>1.授权：敏感接口调用权限管控（如获取用户手机号）；</p>
<p>2.限流熔断：基于连接数的单机限流，基于慢调用/异常数/率的熔断；</p>
<p>3.故障注入：东西流量的故障模拟，其余由 chaosmesh/chaosblade 支持。</p>
<p><strong>服务运营</strong></p>
<p>1.服务管控：并未使用开源 kiali 管理端，而将对应的节点信息呈现在爱番番一站式平台上，并提供基础的一站式管理能力，如限流熔断、配置管控、服务迁移等；</p>
<p>2.APM：Istio 本身的 APM 中，Logging 基于 EFK架构 进行采集、Metrics 基于Prometheus 进行采集，通过 Grafana 进行一站式管理。业务应用的 APM 暂时维持现状，仍然采用无 Mesh 的 Skywalking + EFK + Prometheus + Grafana 进行管控。</p>
<h2 data-id="heading-15"><strong>3.4 爱番番切换Servicemesh带来的收益</strong></h2>
<hr>
<p>通过切换 Mesh，标志着爱番番云原生又一核心里程碑的达成，爱番番对自身业务的服务治理进行了底层解构并初步重塑，初步改变了沉没式治理的现状。之前的多语言治理难、业务耦合、能力缺失、人肉配置困境得到较大的缓解，在功能上，快速补充了超过 10+ 个之前缺失的核心治理能力，在效能上，将服务治理的生命周期从数月直线拉低到分钟级，CI pipeline 时间节省 20%，解放了业务方和架构方的效能，测试环境多路复用能力更是可以颠覆现有开发模式，实现并行开发测试，并同时节省 30%以上 的测试联调等待时间；在稳定性上，提供了限流熔断和混沌工程的能力，为业务提供了坚实的自我保护手段。通过金丝雀发布，更是可以实现上线流量的无损的同时，让研发人员告别深夜发布的局面；依托于 istio 构建的稳定性保障体系更是让爱番番整体稳定性得到了飞跃式的提升。这仅是现在就能带来的收益，而其未来的收益远不止此。</p>
<h1 data-id="heading-16"><strong>四、结篇：星辰大海</strong></h1>
<p>当下，着眼于务实的角度，爱番番的服务治理仍然面临着不小的挑战需要去一一攻克，以最大化发挥出 Istio 的核心红利。另一边，我们其实并不满足于将 Servicemesh 定义为南北东西向流量的管控上，面对效能难题，Servicemesh 的红利其实能够更大的释放，解决更大范围的痛点，沉没式的治理不仅存在于分布式服务框架中，也会长期存在于所有的中间件里。我们也关注到业内包括 Istio 自己本身也有一些对应的探索，我们也坚信这在未来必将成为「多语言微服务架构」背景下的主流趋势，爱番番也基于自身痛点开始主导 apm mesh — Apache Skywalking Satellite 的孵化并成功 Release。我们更希望爱番番的 Servicemesh 体系，能够真正意义上成为「<strong>下一代的中间件治理核心</strong>」。相信这会在不久的未来和公司其他部门的携手合作下达成，彻底告别沉没式治理，加速交付客户价值点。</p>
<p>本期作者 | 橙子，百度爱番番业务部首席架构师，腾讯云最具价值专家，QCon出品人，ArchSummit明星讲师， Apache Commiter，历任多家公司平台&基础架构&运维负责人。</p>
<p><strong>招聘信息</strong></p>
<p>无论你是后端，前端 ，大数据还是算法，这里有若干职位在等你，欢迎投递简历，关注同名公众号百度Geek说，输入内推即可，爱番番业务部期待你的加入！</p>
<p><strong>阅读原文</strong></p>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247493554&idx=1&sn=9eaa6cb738547c38980c23798fd66e29&chksm=c03ed7cef7495ed8422338b880235d04c0ca2ccfd4abb96ca0bd9c9ef47a535729865f1f0cdb&token=1064478816&lang=zh_CN#rd" target="_blank" rel="nofollow noopener noreferrer">百度爱番番与Servicemesh不得不说的故事</a></p>
<p>---------- END ----------</p>
<p>百度Geek说</p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            