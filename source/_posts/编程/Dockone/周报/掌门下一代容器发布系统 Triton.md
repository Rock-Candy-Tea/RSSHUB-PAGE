
---
title: '掌门下一代容器发布系统 Triton'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/95ec8078afa0f0dd8c22ea4dbe1ba1ea.jpg'
author: Dockone
comments: false
date: 2021-07-20 03:07:48
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/95ec8078afa0f0dd8c22ea4dbe1ba1ea.jpg'
---

<div>   
<br>CD 平台是掌门的持续交付系统，<a href="https://zh.wikipedia.org/wiki/%E7%89%B9%E9%87%8C%E5%90%8C">Triton</a> 作为 CD 平台的核心容器发布组件，自 2020 年 4 月在 CD 平台上正式上线，支撑了掌门近 1000 个应用从虚机迁移至容器的过程，保障了虚机迁容器过程的稳定性。目前，Triton 除了提供日常的应用容器发布、网络策略配置、Ingress 域名配置等能力之外，也成为其他组件、平台的资源交付基座，比如，<a href="https://mp.weixin.qq.com/s/DFy_E6qN3hLyStaSand_Dg">大规模的流水线交付</a>，压测平台等。Triton 解决了应用生命周期管理的问题，包括开发、部署、运维等，同时打通了微服务治理，极大地帮助研发提升了持续交付的效率。<br>
<h3>背景</h3>云原生架构的快速普及带来了企业基础设施和应用架构等技术层面的革新。在 CNCF 2020 年度中国区云原生调查报告里面有一个亮眼的数字，72% 的受访者已经在生产环境当中使用 Kubernetes，同期全球调查报告的数字是 83%。可以看到，在 Kubernetes 的使用率上，中国和全球是持平的。如果看纯容器使用率，则更加惊人，超过 92%。从这些数据来看，我们可以得出结论：Kubernetes 和容器已经完全进入主流市场，成为所有人都在使用的技术。<br>
<br>在此之前，掌门的应用一直跑在虚机里，但是随着应用规模的不断扩大，虚机数量也随之快速增加，我们开始在运维成本、交付效率、应用管理上面临一些痛点：<br>
<ol><li>应用数量不断增加，基础设施的成本随之上升，降本迫在眉睫；</li><li>业务飞速发展，内部对资源、环境、应用的交付效率的要求不断提高；</li><li>应用数量增长很快，大量应用的管理给运维带来很大压力。</li></ol><br>
<br>所以，为了能够充分发挥云原生的优势，灵活地应对变化和弹性扩展以提升开发效率，加速迭代并降低成本，掌门于 2020 年 4 月份正式启动容器化项目。<br>
<br>为了最大程度降低迁移容器过程中对开发和业务的影响，我们决定在应用发布中完成从虚机到容器的迁移，以保障迁移过程中服务的稳定性，实现不停服迁移。要实现这个目标，一个全新的、支持容器发布的平台呼之欲出，Triton 就是在这种背景下诞生的。下面将介绍容器发布平台 Triton 的设计原理、实现方案。<br>
<h3>Triton 设计原理及实现方案</h3>在介绍 Triton 之前我们先看一下 CNCF 对持续交付的定义，涵盖了一个云原生应用的全生命周期流程，图中的一些技术术语在本文中也会用到，比如 <code class="prettyprint">workload</code>，<code class="prettyprint">rollout</code>，<code class="prettyprint">canary</code> 等，<a href="https://docs.google.com/document/d/1gMhRz4vEwiHa3uD8DqFKHGTSxrVJNgkLG2WZWvi9lXo/edit#">这篇文档</a> 中有详细的介绍，需要的话可以查阅。<br>
<br>同时通过这张图，也可以清晰地了解 Triton 在整个持续发布系统中的定位。Topic 1，Topic 1.5 的主要内容是应用模型描述，打包、参数配置；Topic 4 是资源管理，网络，日志/监控等平台侧的功能；而 Triton 聚焦的工作是在 Topic 2 和 Topic 3 ，主要内容是应用生命周期管理，流量管理，workload 管理，提供发布策略，比如蓝绿部署、金丝雀部署等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/95ec8078afa0f0dd8c22ea4dbe1ba1ea.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/95ec8078afa0f0dd8c22ea4dbe1ba1ea.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>CNCF SIG App Delivery</em><br>
<br>了解了 Triton 的定位后，下面将从方案选型，架构设计，UI 交互 3 个维度来详细介绍 Triton 的设计原理和实现方案。<br>
<h4>方案选型</h4><strong>workload 选型</strong><br>
<br>众所周知，不管是无状态的 Deployment 还是有状态的 StatefulSet，Kubernetes 都是支持服务的滚动更新的。我们也经常在一些文章中看到有基于原生 Deployment 实现应用的滚动发布和灰度发布，这种方式开发简单容易上手，但是随之带来了很多缺陷，使得我们无法细粒度控制发布的过程，比如不支持发布过程中暂停、继续，以及流量的优雅拉入拉出等能力。<br>
<br>为了实现更丰富的发布策略以及更加细粒度的发布控制，以保障容器发布过程的安全、稳定，Triton 选择 <a href="https://openkruise.io/zh-cn/docs/what_is_openkruise.html">OpenKruise</a> 作为应用的 workload。OpenKruise 是 Kubernetes 的一个标准扩展，它可以配合原生 Kubernetes 使用，并为管理应用容器、sidecar、镜像分发等方面提供更加强大和高效的能力。OpenKruise 提供了很多原生 kubernetes 的增强型资源，CloneSet、Advanced StatefulSet、SidecarSet 等。其中，CloneSet 提供了更加高效、确定可控的应用管理和部署能力，支持优雅原地升级、指定删除、发布顺序可配置、并行/灰度发布等丰富的策略，可以满足更多样化的应用场景，所以 Triton 选择基于 CloneSet 来实现无状态应用的发布流程。<br>
<br><strong>发布流程技术选型</strong><br>
<br>如何定义一种发布流程，并按照流程的定义去实现本次发布？为了寻找一些灵感，在设计 Triton 之前我们调研了目前在云原生领域做得比较好的的一些 CI/CD 组件，像云原生 CI 工具 Tekton，交付工具 Argo 都是设计了一套 CRD（自定义资源），然后在 Operator 中实现相应的逻辑以达到最终的目标状态（Operator 是由 CoreOS 开发的，用来扩展 Kubernetes API，特定的应用程序控制器，其基于 Kubernetes 的资源和控制器概念之上构建，但同时又包含了应用程序特定的领域知识。创建 Operator 的关键是 CRD 的设计）。<br>
<br>于是我们采用云原生的方式设计容器发布，<strong>原生为云而设计，在云上运行，充分利用和发挥云平台的弹性 + 分布式优势</strong>。我们设计了一种 CRD 来描述一次容器发布的完整流程，这样每次发布只需要创建 CRD 资源，就能定义好本次的发布流程，后续只需要在此资源基础上修改即可。经过内部讨论，最终该 CRD 被命名为 DeployFlow，即发布流的意思，关于 DeployFlow 的详细介绍请继续阅读下面的架构设计。<br>
<h4>架构设计</h4>在解决了 workload 和发布流程的技术选型后，DeployFlow 这个 CRD 的设计就成为了我们要去聚焦的核心工作。下图展示了 Triton 的主要设计架构，可以看到在 Kubernetes 和 OpenKruise 的基础之上，完成一次发布需要的配置由 CRD 定义，发布流程相关的逻辑控制通过 Operator 实现，同时 Triton 提供 REST、GRPC API 和前端 UI 实现交互。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/aa4d4196b00c5f3d45459ceeab22cf31.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/aa4d4196b00c5f3d45459ceeab22cf31.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Triton 架构图</em><br>
<br><strong>DeployFlow 和 Operator 实现</strong><br>
<br>首先介绍下 DeployFlow 这个 CRD，通过 DeployFlow 我们定义了一次发布中需要的配置以及发布过程中需要的状态展示。<br>
<pre class="prettyprint">// DeployFlow is the Schema for the deploys APItype DeployFlow struct &#123; metav1.TypeMeta   `json:",inline"` metav1.ObjectMeta `json:"metadata,omitempty"` Spec   DeployFlowSpec   `json:"spec,omitempty"` Status DeployFlowStatus `json:"status,omitempty"`&#125; <br>
</pre><br>
<code class="prettyprint">Spec</code> 字段的内容分为两部分，一部分是与应用相关的信息，比如 <code class="prettyprint">AppID</code>、<code class="prettyprint">GroupId</code>、<code class="prettyprint">副本数量</code>、<code class="prettyprint">AppName</code> 等，另一部分是指定发布策略，比如是 <code class="prettyprint">create</code> 还是 <code class="prettyprint">update</code> 操作，是 <code class="prettyprint">scale in</code> 还是 <code class="prettyprint">scale out</code>，不同的操作对应不同的发布策略，详细的字段解释可以通过下面代码来理解。<br>
<pre class="prettyprint">type DeployFlowSpec struct &#123; // Important: Run "make" to regenerate code after modifying this file AppID        int    `json:"appID"` GroupID      int    `json:"groupID"` AppName      string `json:"appName"` ...... Action       string `json:"action"` // +nullable UpdateStrategy *DeployUpdateStrategy `json:"updateStrategy,omitempty"` // +nullable NonUpdateStrategy *DeployNonUpdateStrategy `json:"nonUpdateStrategy,omitempty"`&#125; <br>
</pre><br>
<code class="prettyprint">DeployUpdateStrategy</code> 代表了本次发布是一次更新操作，也就是会使 CloneSet 中的 <code class="prettyprint">UpdateRevision</code> 字段发生变化，一般 <code class="prettyprint">create</code>、<code class="prettyprint">update</code>  <code class="prettyprint">rollback</code> 就是采用 <code class="prettyprint">DeployUpdateStrategy</code> 的字段定义。<br>
<br>DeployNonUpdateStrategy 代表本次发布不会触发资源更新，也就是 <code class="prettyprint">UpdateRevision</code> 不会发生变化，一般 <code class="prettyprint">scale in</code>、<code class="prettyprint">scale out</code>、<code class="prettyprint">restart</code> 等操作要采用 <code class="prettyprint">DeployNonUpdateStrategy</code>。<br>
<br>不同的发布策略肯定有不同的字段，但大部分的策略都是可以共用的，所以在此之上我们抽象出一个基础发布策略 <code class="prettyprint">BaseStrategy</code>，由于 <code class="prettyprint">BaseStrategy</code> 中的字段太多，我们这里放一张 CRD 的 <code class="prettyprint">schema</code> 资源视图，然后再选择其中重要的字段进行解释。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/750c5cc7e383953707af5bbd2f5fb3f2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/750c5cc7e383953707af5bbd2f5fb3f2.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DeployFlow</em><br>
<br>先介绍 <code class="prettyprint">DeployPhase</code> 字段，<code class="prettyprint">DeployPhase</code> 表示一次发布过程中，DeployFlow 所经历的阶段。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/f8b732971404d4988e263266b6290c84.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/f8b732971404d4988e263266b6290c84.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DeployPhase</em><br>
<br>字段的意思都比较好理解，这里就不展开讲了。<br>
<br>在 <code class="prettyprint">BaseStrategy</code> 中有个比较重要的字段 -  <code class="prettyprint">BatchSize</code>，表示批次大小。这意味着 <code class="prettyprint">DeployFlow</code> 支持分批次发布，用户可以自定义每个批次最大发布的副本数量，DeployFlow 会计算出本次发布的总批次是多少从而提前给出发布概览。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/2cb03b22f25cc2d21c2ae5ba0a72cfac.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/2cb03b22f25cc2d21c2ae5ba0a72cfac.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>deploy overview</em><br>
<br>从 <code class="prettyprint">BaseStrategy</code> 的 <code class="prettyprint">paused</code>、<code class="prettyprint">canceled</code> 字段就可以知道，在发布过程中可以随时暂停、继续或者取消本次发布。<code class="prettyprint">Mode</code> 表示 <code class="prettyprint">DeployFlow</code> 不同批次之间的触发方式，分为 <code class="prettyprint">auto</code> 和 <code class="prettyprint">manual</code> 两种，当选择 <code class="prettyprint">auto</code> 模式的时候，通过字段 <code class="prettyprint">BatchIntervalSeconds</code> 可以设置不同批次之间的时间间隔，如果选择手动模式则每个批次之间需要手工触发。<br>
<br>由于 <code class="prettyprint">DeployFlow</code> 是分批次发布，所以每个批次需要有阶段显示 -  <code class="prettyprint">BatchPhase</code>，以表示当前的批次所处的阶段，我们来详细解释每种阶段的含义。<br>
<br><code class="prettyprint">BatchPending</code>：表示当前批次的 <code class="prettyprint">Pod</code> 正在准备资源，比如此时 Pod 正在被调度中，image 在下载中，对应 Kubernetes 中的 Pod 处于 <code class="prettyprint">Pending</code>，<code class="prettyprint">ContainerCreating</code> 状态。<br>
<br><code class="prettyprint">BatchSmoking</code>：表示当前批次的 Pod 正在启动过程中，Pod 处于 <code class="prettyprint">Running</code> 状态，但是 <code class="prettyprint">ContainerReady</code> 字段还没有置为 true。<br>
<br><code class="prettyprint">BatchSmoked</code>：表示当前批次的所有 Pod 都已经启动成功，也就是 Pod 中的 <code class="prettyprint">ContainerReady</code> 字段已经被置为 true，但是 <code class="prettyprint">Ready</code> 字段还处于 false。此时如果通过 service 来处理服务流量的话，启动的 Pod 并不会被加入到对应 service 的 endpoint，如果是微服务架构，则该 Pod 并不会被拉入到微服务的注册中心，从而保证了业务流量的安全。正是拥有了这种机制以及批次间可暂停的能力，我们可以轻松实现应用的金丝雀发布，这个在后面还会详细讲到。<br>
<br><code class="prettyprint">BatchBaking</code>：表示当前批次的所有 Pod 都已经启动成功，正在执行流量拉入操作，也就是将 Pod 的 <code class="prettyprint">Ready</code> 字段置为 true。<br>
<br><code class="prettyprint">BatchBaked</code>：表示当前批次的所有 Pod 的 <code class="prettyprint">Ready</code> 字段都已被置为 true，Pod 开始接收生产流量，至此也意味着本批次的结束，可以开始下一批次的操作。<br>
<br>在批次进行过程中，会有 smoke 失败或者 bake 失败的情况，对应的状态就是 <code class="prettyprint">SmokeFailed</code> 和 <code class="prettyprint">BakeFailed</code>。<br>
<br>在 <code class="prettyprint">UpdateStrategy</code> 中有一个 <code class="prettyprint">canary</code> 字段，意味着 <code class="prettyprint">DeployFlow</code> 支持金丝雀发布。其实在讲解了上述 DeployFlow 分批次处理的能力后，在此基础之上实现金丝雀发布是比较简单的。也就是在金丝雀批次处于 <code class="prettyprint">BatchSmoked</code> 状态的时候，让发布暂停，在流量拉入之前也可以进行一些 API 验证的操作，开发者在验证没问题之后手工将该批次拉入，拉入金丝雀批次后，<code class="prettyprint">DeployFlow</code> 也处于暂停的状态，此时开发者可以观察线上流量的监控，确认没有问题后再执行后面批次的发布。后面的 UI 交互会更加直观地展示该功能，这里我们先通过一张 DeployFlow 的状态流转示意图完整地展示一次发布的过程，我们以本次发布分为两个批次为例，金丝雀批次和普通批次。结合本图与上文的 CRD 解释，相信读者会对 DeployFlow 有一个更加清晰的认知。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/4f095f0a2706e10e14f4da0a6a48b16d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/4f095f0a2706e10e14f4da0a6a48b16d.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DeployFlow 状态流转</em><br>
<br>至此，在 <code class="prettyprint">DeployUpdateStrategy</code>、<code class="prettyprint">BaseStrategy</code> 中的核心字段都已经介绍完了，在 <code class="prettyprint">DeployNonUpdateStrategy</code> 中还有一个 <code class="prettyprint">PodsToDelete</code> 字段，这个字段是在应用缩容、重启操作时起作用的，原生 Kubernetes 对于资源的缩容操作有自己的规则，不能随意选择想要缩容的 Pod。但是在 DeployFlow 中，你可以指定 Pod 缩容，指定 Pod 重启。<br>
<br>通过上面的介绍，读者对 DeployFlow 这个 CRD 的 spec 字段有了一定了解，下面来看下发布过程中我们需要展示的 status 字段。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/8bc5711e31fe29564e6841fa97f21bde.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/8bc5711e31fe29564e6841fa97f21bde.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DeployStatus</em><br>
<br>熟悉 Kubernetes 的同学应该能够从字段的字面意思了解这些字段的含义，这里就不详细展开了。<br>
<br>CRD 设计完成后，Operator 的实现也就是水到渠成的事情了，除了 DeployFlow 的 Operator，Triton 中还重新实现了一些 controller 来满足个性化的需求，比如 Event controller 用来将发布过程中 Pod、CloneSet、DeployFlow 等组件的日志发送到 ES 以方便开发者查看发布的情况，ReadinessGates controller 用来控制自定义 ReadinessGate 的拉入拉出操作等。<br>
<br>同时 Triton 提供 REST & GRPC API 来操作 DeployFlow，调用方即使不了解容器和 Kubernetes 的知识，也可以很容易对接到 Triton 上实现发布的功能。<br>
<h4>UI 交互</h4>底层架构以及核心组件 DeployFlow 的设计逻辑虽然稍显复杂，但得益于 Triton 暴露的 REST & GRPC API 以及丰富的 status 字段，使得前端在发布的 UI 交互逻辑上能够做到简洁直观。下面让我们从 UI 入手，看下 Triton 如何进行应用的交付以及对应用的副本实例的规划。<br>
<br><strong>发布入口及发布清单</strong><br>
<br>进入生产发布页面，在容器发布页签，选择需要发布的 group，点击“发布”。<br>
<br>点击后弹出一个发布清单的页面，在这里需要配置本次发布需要的策略以及相关参数。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/7403731319ca7e8532eb80f709f47d32.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/7403731319ca7e8532eb80f709f47d32.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>发布单页</em><br>
<br>其中有些参数在上面的 CRD 设计篇章中已经有所描述，比如应用描述，批次大小，批次间处理方式，批次间隔等，这里不再赘述。<strong>启动超时时间</strong>  是开放给开发者自定义应用需要用来启动的时间，比如有些应用尤其是 java 应用，在真正启动之前需要执行一些 warm up 的操作，开发者就可以根据自己应用的实际情况填写该值，避免这类应用启动失败。<strong>微服务拉出等待时间</strong>  是用来支持微服务 Pod 优雅退出的。<br>
<br>那何谓优雅退出，为什么要优雅退出呢？在 Kubernetes 中当删掉一个 Pod 的时候，理想状况当然是 Kubernetes 从对应的 Service（假如有的话）把这个 Pod 摘掉，同时给 Pod 发 SIGTERM 信号让 Pod 中的各个容器优雅退出就行了。但实际上 Pod 有可能犯各种幺蛾子：<br>
<ul><li>已经卡死了，处理不了优雅退出的代码逻辑或需要很久才能处理完成；</li><li>优雅退出的逻辑有 BUG，自己死循环了；</li><li>代码写得野，根本不理会 SIGTERM。</li></ul><br>
<br>因此，Kubernetes 的 Pod 终止流程中还有一个“最多可以容忍的时间”，即 grace period（在 Pod 的 <code class="prettyprint">.spec.terminationGracePeriodSeconds</code> 字段中定义），这个值默认是 30 秒，我们在执行 <code class="prettyprint">kubectl delete</code> 的时候也可通过 <code class="prettyprint">--grace-period</code> 参数显式指定一个优雅退出时间来覆盖 Pod 中的配置。而当 grace period 超出之后，Kubernetes 就只能选择 SIGKILL 强制干掉 Pod 了。<br>
<br>但是在微服务的场景下，除了把 Pod 从 Kubernetes 的 Service 上摘下来以及进程内部的优雅退出之外，我们还必须做一些额外的事情，比如说从 Kubernetes 外部的服务注册中心上反注册，不然可能会出现 Pod 已经被删掉，但是注册中心上还留着已删掉 Pod 的服务信息，此时有流量进入的话就会出现服务不可用的情况。所以我们在 prestop hook 中定义了一个名为 <code class="prettyprint">gracefully_shutdown</code> 的文件来处理 Pod 删除后的微服务优雅退出。<br>
<pre class="prettyprint">spec:  contaienrs:  - name: demo-container    lifecycle:      preStop:        exec:          command: ["/bin/sh"，"-c"，"/gracefully_shutdown"] <br>
</pre><br>
右侧的发布策略以及本次发布概览在之前的架构设计中已经讲过，这里不在赘述。<br>
<br><strong>开始发布</strong><br>
<br>完成发布配置后，即可开始发布。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/c2305946e7c8f11dd3e36bcbdda5814e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/c2305946e7c8f11dd3e36bcbdda5814e.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>deploy-layout</em><br>
<ul><li><strong>发布进度</strong>：展示发布的批次，及各个批次所启动的实例数量和状态。在发布过程中，人工操作的入口也在此区域；</li><li><strong>实例列表</strong>：展示发布的实例，可以切换实例版本查看各版本的实例；</li><li><strong>副本状态</strong>：形如 <code class="prettyprint">0/1/0/0</code> 对应 <code class="prettyprint">Pending/Running/Ready/Failed</code> 四个状态的数量（1个 Pod 在发布中），其中 <code class="prettyprint">Running</code> 对应发布中实例数，<code class="prettyprint">Ready</code> 发布成功实例数，<code class="prettyprint">Failed</code> 发布失败实例数。</li></ul><br>
<br><strong>发布过程</strong><br>
<br>一个典型的发布包括“金丝雀批次启动（Smoking）”—“金丝雀批次点火（Baking）”—“滚动发布（Rollout）” 三个阶段。<br>
<ol><li><br>金丝雀批次启动中（Smoking）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/b9b8ff5d3e0ebcd715a337c5bdd15a7d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/b9b8ff5d3e0ebcd715a337c5bdd15a7d.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>canary smoking</em></li><li><br>金丝雀批次启动成功，可以验证接口，确认没问题，可将其拉入点火（Baking）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/d74cb021d704f250533a48a16b8d0eac.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/d74cb021d704f250533a48a16b8d0eac.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>canary smoked</em></li><li><br>金丝雀批次点火中，实例已接流量，由于此时 DeployFlow 处于暂停状态，开发者可以有充足的时间可观察日志、监控等是否有异常，确认没问题后再触发滚动发布（Rollout）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/8db9cab16a3560fbaa3e9b1b1e8dc090.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/8db9cab16a3560fbaa3e9b1b1e8dc090.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>canary baked</em></li><li><br>滚动发布中，如选择“手动” 模式，每个滚动批次都需要人为触发<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/b706f689603fe7e42d41a07b06a7f6a9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/b706f689603fe7e42d41a07b06a7f6a9.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>rollout</em></li></ol><br>
<br>滚动发布过程中，可以看到新旧实例的版本数量在交替变化。<br>
<ol><li>发布成功<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/2b8f8360ac6dd84b81c34bab0a263983.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/2b8f8360ac6dd84b81c34bab0a263983.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>deploy success</em></li></ol><br>
<br>至此，一次完整的 DeployFlow 流程就走完了，发布到达成功的状态。可以看到每个批次所负责的 Pod 数量以及 Pod 状态、日志等信息。<br>
<br><strong>指定实例的操作</strong><br>
<br>在实例运行过程中，如果发现实例负载异常或需要重新加载 Apollo 配置，就会有重启实例的需求。Kubernetes 本身没有提供重启的操作逻辑，一般通过杀掉一个 Pod 来达到重启的效果，但这种方式比较粗暴而且存在安全隐患。Triton 提供了安全的重启策略，会先新增一个 Pod 如果该 Pod 启动成功成功，再删掉你所指定要重启的 Pod，以此来达到安全重启的效果，这就是 Triton 的指定实例重启的功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/2bdd12ac68cd437b2ced1d78a23b13f5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/2bdd12ac68cd437b2ced1d78a23b13f5.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>specify-pod-restart</em><br>
<br>同样的原理，缩容的操作也可以指定想要缩掉的 Pod 。<br>
<br>该功能的实现得益于 OpenKruise 中增强型无状态 workload CloneSet 提供的能力，具体的功能描述可以参考 OpenKruise 文档。<br>
<br>上面的内容就是有关 Triton 核心能力的 UI 交互，整个过程力求简洁、清晰，避免给开发者造成额外的理解负担，这为我们容器的接入、推进提供了很大的便捷。<br>
<h3>总结与展望</h3>每个公司的容器发布平台都不尽相同，可能会有读者看完说 Triton 封装了太多的 Kubernetes 细节，没有向开发者真正展示原生 Kubenetes 的状态、含义或者理念。其实从一开始，我们的目标就是设计适用于掌门自身研发体系的容器发布系统，减少开发对发布操作的学习成本，从而快速上手以更快地赋能研发流程的迭代，加速业务应用的上线。而简洁清晰的 API 也有利于我们设计出更加简单的用户界面，简单的用户界面又让我们在推广时受益。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/9e474be26ef7f779b59ef874f920635c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/9e474be26ef7f779b59ef874f920635c.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
上图是 Triton 的一些关键指标，可见 Triton 已经成为 CD 平台的核心能力，在用户需求的迭代中不断进化，不过，现在的 Triton 依然有很大的优化空间，主要有：<br>
<ol><li>掌门有大量的 socket 长连接应用，对于这类应用的容器化，以及容器化后如何发布，还没有清晰的设计方案；</li><li>Triton 按应用粒度进行发布，不支持跨应用的发布流程编排；</li><li>对开发者快速拉起本地测试环境的支持较弱。</li></ol><br>
<br>我们目前也在进行针对这些优化项的工作。<br>
<br>我们团队负责掌门研发效能平台的建设，服务于掌门所有研发人员。作为掌门研发体系的核心组成部分，致力于保障高质量的交付和研发效率的提升。当前 CD 平台已经在 CI/CD 和监控告警形成闭环，今后我们会沿着需求、设计、开发、构建、验证、发布这个路径进行更广的探索，打造真正的研发效能平台。目前掌门正在进行生产环境容器化的升级，如果你对 Triton 或者 Kunernetes 感兴趣，欢迎加入我们一起打磨生产应用容器化的设计与落地方案。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/9UtXnc-Z_F1FUBFznXQiaw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/9UtXnc-Z_F1FUBFznXQiaw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            