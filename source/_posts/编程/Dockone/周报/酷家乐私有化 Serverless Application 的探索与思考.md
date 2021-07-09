
---
title: '酷家乐私有化 Serverless Application 的探索与思考'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/bb01244ef89520941e21bffc236c6036.png'
author: Dockone
comments: false
date: 2021-07-09 03:07:41
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/bb01244ef89520941e21bffc236c6036.png'
---

<div>   
<br>目前，很多公有云厂商都推出了面向应用的 Serverless Application 产品，有 Google Cloud Run、阿里云 Serverless Application Engine、腾讯云 CloudBase Run 、Trigger Mesh 等。<br>
<br>它们都提供了构建 → 部署→实例管理等全面服务托管能力，支持托管用任意语言和框架编写的容器化应用，简化并加快应用开发和部署工作。<br>
<br>酷家乐 Serverless 团队也在 2020 年中开始探索基于 Knative 开发私有化 Serverless Application，做为现有 Serverless FaaS 能力之外的补充产品，满足内部对于无语言限制的容器化应用开发部署的用户诉求。<br>
<br>截止到 2021年6月，Serverless Application 在酷家乐内部已实现了规模化落地，有近 100 个应用服务使用 Serverless Application 做托管，尤其是在非 Java 领域非常受欢迎，是目前其他语言技术栈落地最多的平台选择。<br>
<h3>为何要做私有化 Serverless Application</h3><h4>Serverless FaaS 现状和局限</h4>起初，我们简单地认为 Serverless 的产品形态就只会是 FaaS + BaaS 的组合模式，其“专注业务逻辑”开发模式可以赋能给争分夺秒上线和服务运维繁琐/困难的开发者，能带给我们的业务价值是更高的开发效率、更合理的角色分工、更多创新项目的快速落地。所以自 2019 年底起，酷家乐就开始在 <a href="https://tech.kujiale.com/kujiale-serverless-faas-experience/">Serverless FaaS 方向探索并内部落地</a>主要基于 Node.js 语言的云函数产品，截止到 2021 年初，公司已有超过 60% 内部业务线都有接入并使用 FaaS 产品，FaaS 也真实地给业务方带去了开发上的便利并且提高了整体迭代效率。<br>
<br>我们对过去一年多里 FaaS 落地场景和用户习惯做了数据统计：<br>
<ol><li>创新业务、内部系统的函数占比依旧高达 70%+，真·核心业务接入较少且场景相对简单</li><li>FaaS 在整体网站架构里的中间层作用明显，但是以整块业务形态落地的 SFF 场景并不多</li><li>FaaS 用户大多都是前端开发工程师，对于多函数（聚合部署）使用频率非常高，单逻辑函数使用越来越少</li></ol><br>
<br>简单总结就是：FaaS 主要应用于前端领域，落地场景多为可独立业务逻辑，核心业务增长较为疲软。<br>
<br>对此我们也反思了几个 FaaS 的现状问题：<br>
<ol><li>从落地场景上，逻辑单一的函数业务场景很少，多做为数据聚合或简单后台的场景</li><li>从业务维护上，颗粒化的函数开发方式会带来额外的隐性逻辑串联成本，业务不易结块，导致整体项目使用或改造的倾向度低</li><li>从基建成本上，提供的 FaaS 开发语言 runtime 种类基本就圈定未来的用户群体，这也间隔限制了可能接入的业务场景</li><li>从架构现状上，中型公司的技术架构往往倾向于稳定，业务开发分配范围广但责任明确，FaaS 价值发挥相对有限，会很依靠于架构调整的机遇; 而小公司的高速上线模式、大公司的私有化 Bu FaaS 可能会更适合 FaaS 生长</li></ol><br>
<br>那么 Serverless 的价值就只能体现在这了吗？不是的，让我们回归到做 Serverless 初衷上来。<br>
<br>无论是哪种技术/架构的演变，本质上都是为了解决资源成本或者研发效率的问题，Serverless 也是如此。<br>
<br>如果说 FaaS 做到了消除服务端技术的壁垒，赋能了开发者散装应用/模块的开发能力，那么整装应用的资源成本或效率又该如何改变呢？历史应用又该何去何从？<br>
<h4>业务诉求</h4><strong>技术栈限制</strong><br>
<br>每个公司在服务应用开发上，一般都会选有一门主体开发语言，比如常见的 Java，所以内部的基建架构、链路交互等都会围绕这个主体去实现，当然技术栈的统一的确也是项目维护的重要方式。<br>
<br>但是在不同的业务场景、不同的人员配置的情况下，由于存在开发门槛、缺乏可观察性等基建而导致地技术栈约束，同样也是种资源浪费，更直接影响交付效率。<br>
<br>开发者们也希望自己的精力能都聚焦在业务上，以前听过一句很调侃的话：“某个领域的开发专家为了落地产品，经过几个月的时间，努力把自己变成了另一个领域的中级开发者……”<br>
<br><strong>应用资源成本</strong><br>
<br>酷家乐在很早期时就开始把应用架构往云原生的方向发展，服务部署也都以容器技术为主，但在现有内部产品里，我们无法规范化地满足实现“资源弹性为 0”的业务场景。<br>
<br>假设某个服务的资源配置比较大，工作时间又都是在凌晨，如何解决资源长期占用且利用率低的问题？<br>
<br>再比如，按照常规的软件迭代发布流程，功能发布必须经过多类环境，测试环境、稳定环境、预发环境、线上环境等，如果有些环境不适用或使用频率很低的话，如何做到资源不浪费？<br>
<br>毕竟每个 team 的资源配比都是有限的。<br>
<br><strong>应用全托管</strong><br>
<br>有些应用为了快速上线在开发过程中比较粗糙，比如自写 GitLab CI 来做发布控制，又或者是缺乏相应的监控、告警、hook 等基础设施。<br>
<br>开发者们都期望能有一个全托管的服务平台，既帮助他们屏蔽繁琐的服务搭建及运维，又能够提供满足公司要求的服务稳定性等要求，不用关心代码发布、部署方式、机器宕机、实例扩缩容、机房容灾等问题，而且只需要花费较低的迁移成本就能立刻拥有这些能力。<br>
<br><strong>覆盖更多场景</strong><br>
<br>公司内部有很多周期性任务需求，需要定时处理一些事项，常见的有数据同步、日志清理等；这些虽然实现上简单，但大多都需要用户自行处理，例如自建 CronJob，随着任务的不断增多，整体维护性变差。<br>
<br>还有一些离线计算任务，这类任务对返回时间要求较低，但占用的计算资源较大，采用事件驱动可以在更宏观层面做资源调度管理。<br>
<h4>公有云约束</h4>我们也考虑过直接购买公有云的 Serverless 产品，但是调研结果显示，私有服务上到公有云的 Serverless 会有很大的难度，难以满足我们对于服务的一些基本要求，<br>
<br>公有云的在线开发工具和云资源联动特性，确实是很诱人，但也同时存在着“无法复用私有集群基建”、“日志告警依赖平台”、“灰度发布仅支持版本分流”、“单一弹性策略”、“多环境难以满足”等致命问题。<br>
<br>综合考虑后，我们决定基于 Knative 开发私有化 Serverless Application 产品来满足我们的内部需求。<br>
<h3>我们如何设计和搭建 Serverless Application</h3>我们整个 Serverless 系统都是基于 Knative 打造的，从服务 Serving 上看，其本质是更为简单的容器管理框架，所以只对平台层而言，无论是 FaaS 还是 Application，实现流程上相差并不大，主要是服务模板和运行规范上的差异。<br>
<br>得益于 Serverless FaaS 可复用基建和内部产品的提前打通，使得 Serverless Application 孵化过程变得更为简单和高效。<br>
<h4>整体架构</h4><strong>酷家乐 Serverless 产品大图</strong><br>
<br>笔者认为 Serverless 是一种云原生的系统设计思想，是从底层开始变革计算资源的形态。我们除了依赖 Knative 做为容器托管架构方案外，还融入了更多地例如 API Gateway、Service Mesh、服务发现、监控告警等内部云原生能力，把更多原本需要用户参与的事情下沉到基础设施中，提供全链路的资源整合，让整个 Serverless 体系变得强大健壮，更为简单的发挥其快速、灵活、弹性、扩展性强、迁移能力强等多种优势。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/bb01244ef89520941e21bffc236c6036.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/bb01244ef89520941e21bffc236c6036.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
除了自研 Serverless FaaS 和 Serverless Application 服务级产品外，我们也正在探索基于 Knative Eventing 做标准化的事件总线，现已支持任意 Serverless 服务去配置并使用 PingSource 做定时任务。<br>
<br><strong>Serverless Application 请求链路</strong><br>
<br>Serverless Application 同样依赖 istio gw ingress 做流量管理，通过 gateway-service 做协议转换和服务转发，使得任意语言的应用服务都可以正常访问到 SOA 体系服务，打通了 Knative 服务与内部服务架构的请求交互。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/51cc250898c4a8b6620fd2d8af3f840f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/51cc250898c4a8b6620fd2d8af3f840f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
出于内部域名的规范性，我们对不同类型的 Knative Service 会自动生成指定的域名尾缀，这也引发了 Knative Route 在服务生成时会自动添加 VirtualService，导致我们想通过 vs 直接基于 custom host 做请求转发方案失败；所以我们先通过把服务转为内部域名来阻止 Knative Route 自定义域名生成，再设定 VirtualService（添加匹配规则）的方式来做请求转发，实现流量灰度，过程参见下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/d0d7d23e65f67183cecda89414505a13.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/d0d7d23e65f67183cecda89414505a13.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Serverless CI/CD</strong><br>
<br>架构初期，我们强依赖于 GitLab CI，通过编写相对通用的 gitlab-ci.yaml 去完成服务构建&部署的方式，虽然可以做到流程上的约束，但也有较多的缺点：<br>
<ol><li>每个服务都需要添加 ci yaml，用户操作多余</li><li>无法约束用户不去修改 ci yaml 行为，虽然是对内操作，但长期对用户暴露也是件危险的事情</li><li>流程上无法自定义执行阶段，如有 stage 或 脚本内容 需要变更，是需要用户自行修改或更新，无法做到统一更新，也不利于引入例如质量卡点等检测机制</li><li>无法把用户操作都收聚在 Serverless 管理平台，使用 GitLab CI 会使得部署和版本操作是分离的，而且用户需要在 GitLab 额外维护查看及部署权限，不利于整体维护</li><li>GitLab CI 机器资源为内部共用，高峰期经常会出现排队现象，无法实现 Serverless 资源池私有化</li></ol><br>
<br>并且由于 Serverless 服务部署逻辑存在较多定制化的需求，经过一段时间的调研及讨论，我们决定放弃使用内部成熟的 DevOps 工具来做服务部署，选择使用开源的 <a href="https://argoproj.github.io/">Argo WorkFlow</a> 来满足 Serverless 服务的变更需求。<br>
<br>内置的 CI/CD 默认自动会为用户选择标准流水线模板来实现完整的服务迭代，用户也可以自定义模板（环节）来满足各种特殊的变更要求，除了页面触发外，用户还可以配置 Hook API 的方式来达到本地触发部署及 repo 持续部署的目的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/a2913fbba1f465819527fbbe67838a85.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/a2913fbba1f465819527fbbe67838a85.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Serverless 云平台</strong><br>
<br>整个云平台通过“云产品 & 服务环境 & 服务版本”三个维度来定位流量来源，用户可以在平台上轻松实现灰度、上线、回滚等流量版本操作：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/e128367f10953793d6cb2282db6215e3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/e128367f10953793d6cb2282db6215e3.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上述版本指的是 <a href="https://knative.dev/docs/serving/">Knative Revision</a>，每个 revision 记录了某一时刻的代码和 Configuration 的快照，对应着一组 deployment 管理的 Pod，通过控制 revision 就可以规范地控制服务迭代，满足灰度、分流等使用场景。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/1630029725711a0a6d30c105d3f02568.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/1630029725711a0a6d30c105d3f02568.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Knative 特性使用</h4><strong>VirtualService 使用场景</strong><br>
<br>目前酷家乐部署的 Knative Serving 在流量管理层依赖 Istio VirtualService（简称 vs） 实现。原生的 vs 在流量管理方面非常强大和灵活，但是 Knative 屏蔽了 vs 的多数能力，比如根据请求路径、header匹配等，只支持流量按比例在不同 revision 之间进行分配。原生的 Knative 流量管理策略无法满足业务方的需求，因此需要实现使用自定义 vs 替代（兼容）Knative vs。<br>
<br>knative-serving 下有两个 Istio 网关，分别是 knative-ingress-gateway 和 cluster-local-gateway，Knative 原生的 vs 作用在这两个网关上而生效。当用户使用集群外域名访问 Knative 服务时，knative-ingress-gateway 会根据生效的 vs 将请求按比例转发到对应的 revision 上。<br>
<br>在同一个 Istio Gateway 上，一个域名只能有一个 vs 转发规则，无法在 Knative 原生对外域名 vs 已存在的情况下，再发布一份自定义的 vs 策略实现覆盖。Knative 支持通过为服务增加一个特定标签，关闭对外域名（及相关的 vs 的生成）。因此对于有特定流量管理需求的服务，关闭对外域名的生成，再使用自定义的 vs 文件来实现对外域名的请求转发。符合自定义匹配规则的请求，可以将请求转发到指定服务版本，其他不符合匹配规则的请求，重写请求 authority 为该服务的内部域名，再将请求转发到 cluster-local-gateway 上，利用 Knative 的内部域名转发规则将请求转发到 revision 对应的服务上。自定义 vs 文件如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/b9a6bb682c693eeb2389c9e74a84c91b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/b9a6bb682c693eeb2389c9e74a84c91b.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Custom domain 域名配置</strong><br>
<br>我们对于 Serverless Application 域名格式要求是：&#123;custom_name&#125;.sls-&#123;cluster&#125;.qunhe.com（其中 custom_name 即为 ksvc_name），并且希望通过配置 Knative Custom domain 来统一生成标准域名。<br>
<br>但是由于 Knative 域名格式受 config-network ConfigMap 中 domainTemplate 控制，默认情况下的域名格式为：name.namespace.domain。其中 domain 字段又收到 config-domain ConfigMap 的控制，用户可以通过不同的 label 为 ksvc 生成特定的 domain。并且域名中的 name 在 revision 中时会加上 tag 信息，因此默认的 revision 的域名格式形如：tag-name.namespace.domain。<br>
<br>所以我们需要解决的问题是：如何删除默认域名中 namespace 字段，并且添加上体现集群信息的 sls-** 字段。<br>
<br>我们可以通过在 config-domain 中增加一个标签选择器，给这些服务加上特定标签，来为这些服务生成一个名为 sls-* <em>.</em>qunhe.com 的 domain。同时，为了兼容已经以前通过默认域名格式生成域名的服务，不能简单地将 config-network 中的 name.namespace.domain 改为 name.domain。因此我们的解决方法是在服务中增加一个 annotation 表示，并修改 domainTemplate；当判断当服务有该标识时，使用 name.domain 的格式，domainTemplate 的相关片段如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/2e3eb304bf40c4f2d45c675ff971ade7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/2e3eb304bf40c4f2d45c675ff971ade7.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Eventing 落地探索</strong><br>
<br>Knative Eventing 架构按流程方向简单地分成 3 块内容：事件源 → 事件处理（转发、存储、过滤等）→ 事件消费，通过 Broker/Trigger 事件处理模型对事件进行过滤分发，并且采用 CNCF 定义的标准数据格式 CloudEvents 进行事件传输，确保跨平台和互操作性。<br>
<br>我们实验性地拓展了基于 PingSource 的定时事件触发功能，由于 broker 使用的是默认的 InMemoryChannel，缺乏对事件的高可用、高可靠保障，所以现在仅对测试环境的所有 Serverless 服务开放使用，满足用户 定时推送、数据清理、备份检测等常见需求。<br>
<br>后续我们将继续调研并引入“分布式消息队列”channel，开发自定义容器源，围绕整个事件链路添加监控和输出查看，使得事件驱动模式可以在生产环境中开始试用。<br>
<h3>Serverless Application 在公司内部落地情况</h3><h4>落地场景</h4>具体的落地场景有：对外建站、异步渲染、BFF、后台管理平台、在线搜索引擎、离线数据处理、对内效能工具等。<br>
<br>这里我们挑几个落地较多的场景介绍下：<br>
<br><strong>对外建站</strong><br>
<br>通过同构上传一些静态资源就完成部署，非常适合做展示类型的需求，例如模型展示、虚拟展厅等。<br>
<br>为此，我们还提供了通用的代码模板，解决了资源获取、转发代理、部署配置 等通用问题，而且模板并不限制您使用何种前端框架。<br>
<br>既能让开发者更关注于自己的业务逻辑，也可以非常便捷地满足老项目实现建站场景，用户还可以按需增加 server 端代码逻辑，不需要关心服务器运维相关的复杂性。<br>
<br><strong>BFF、后台管理平台</strong><br>
<br>Backend For Frontend，主要用于向前端提供数据，常用作后端服务接口的聚合裁剪。<br>
<br>与 FaaS 不同的是，这里的 BFF 不受限于语言和框架，用户可以自由选择喜欢的技术栈，而且可以平滑迁移存量业务至 Serverless 模式。<br>
<br>公司内有很多的内部系统，前端部分现已基本都交由前端管理平台（PUB），其提供前端应用从构建到发布的整个生命周期管理和维护，使得前后端分离更为简单，<br>
<br>Serverless Application 正好帮助那些内部系统来托管后台服务，帮助用户实现服务快速落地，推进低运维优势的价值转化。<br>
<br><strong>离线数据处理</strong><br>
<br>离线数据都是基于服务处理的，每个新场景的上线都需要新增 service，新场景落地成本和管理运维成本非常高，<br>
<br>现在内部业务方通过利用 Serverless 的特性高效管理，实现新业务快速接入，离线计算场景也做到了“按需起服务，计算完后即回收”，不再需要占用固定资源。<br>
<br>模块之间使用云原生标准事件规范 CloudEvent 传输交互，解除平台绑定，加速云原生生态集成。<br>
<h4>落地收益</h4>截止到 2021年6月，酷家乐内部已有近 100 个应用服务使用 Serverless Application 做托管，部分核心服务也已接入到 Serverless 体系中，通过 Serverless 的弹性伸缩能力，帮助业务方降低 Kubernetes 资源成本达到近 50%，同时根据“云平台新场景接入便捷，轻运维”的特性，部分新服务上线时间也从原来的 2-3 天缩短至 0.5 天之内，整体研发效率提升约 40% 以上。<br>
<h3>遇到的困难和阻碍</h3><h4>基建融合问题</h4>Knative 帮助我们屏蔽了很多 Kubernetes 底层相关的操作，让我们轻松地就能完成服务部署和弹性控制等等。但是，对于生产级产品而言，这是远远不够的。<br>
<br>最近看到陈皓老师在 Serverless Days 里分享关于“Serverless 需要的基本配套设施”，大致分成四块：资源伸缩编排、全栈可观察性、服务治理、流量管理。<br>
<br>对比以上内容，Knative 主要帮我们解决了“资源伸缩编排”，那么剩下的三块呢？我们的做法是通过融合公司内部基建来完成。<br>
<br>这时候就会面临一个新的问题：内部基建能否兼容、满足 Serverless 架构的技术栈要求？<br>
<ul><li>服务治理：微服务架构是否统一？Service Mesh or 传统 RPC 框架 ？cmdb 规范？</li><li>可观察性：调用链接入？日志是否落盘？监控数据采集方式？告警规则设定？</li><li>流量管理：增设多级流量网关？熔断限流黑名单等基础功能满足？定制化需求？</li><li>……</li></ul><br>
<br>开始时我们也曾陷入过误区，倾向于以快速实现为主，选择更有利于我们自己的技术方向，导致部分功能难以扩展或缺失维护。<br>
<br>后来我们及时做了调整，也得益于酷家乐云原生基建较为完整，通过部门间的不断沟通和讨论，规范化注册接入服务元数据，慢慢地让 Knative Istio 这套方案与内部基建相结合，合理地分配系统功能模块，找专业的人做专业的事，让整个 Serverless 体系变得更加丰富和健壮。<br>
<h4>业务落地顾虑</h4>Serverless 虽然非常有希望成为下一代云计算主流技术，并且 Serverless 系统在酷家乐内部稳定地运行已有 2 年，但是部分业务方对新技术和架构还是持观望态度，毕竟对于业务方来说，服务稳定大如天。<br>
<br>我们的“轻运维”特性同时也是一把双刃剑。由于封装了很多的底层调度的细节，使得整个系统对于用户来说变得更为黑盒，这也导致问题定位变得更加困难。<br>
<br>所以我们一直持续地在提高系统的可观察性和稳定性 ，除了满足三板斧、故障预警、及时止血等基本要求外，也在努力达到“让用户不参与过程，但过程对用户透明”的目标，让用户平滑地放心地将业务迁到 Serverless 上来。<br>
<h4>Knative 使用问题</h4><strong>日志收集</strong><br>
<br>酷家乐内部标准的实时日志方案是基于 FileBeat（收集）+ Kafka（消息队列）+ Flink（流处理）+ ElasticSearch（查询）实现的，但有以下接入限制：<br>
<ol><li>通过对 Pod 添加 Volume 信息实现日志挂载（from deployment）</li><li>所有被采集的服务都必须要有 cmdbtag（按服务按天分索引，优化查询速度）</li></ol><br>
<br>根据上述限制并结合 Serverless 产品实际情况，我们对不同的产品采取了不同的日志收集策略：<br>
<ol><li>Serverless Application：服务部署位置在各个服务组分配的 namespace 下，cmdbtag 操作也有明确的审批流程，所以我们采用内部标准方案，通过“挂载 Volume”方案实现日志收集，期间需要用户主动声明容器内日志文件路径。</li><li>Serverless FaaS：服务部署位置及服务命名都有一定的约束，注册函数时也会同步注册 cmdbtag；出于简化整体流程，我们额外采用“非挂载式日志收集”方式来达到“不需要关心日志如何被收集，直接就能在云平台上查看日志”的用户期望。</li></ol><br>
<br>挂载 Volume：<br>
<br>由于 Knative 自身的限制，无法在 Knative 的 Service 资源中为 user-container 挂载除了 ConfigMap 和 Secret 之外的任何 Volume。为了适配现有的日志收集方式，需要使 Knative 创建的 Pod 最终能挂载其他类型（目前指 HostPath）的 Volume。<br>
<br>Knative 从 KSVC 到 Pod 的控制链路为 KSVC → Revision → Deployment → Pods，其中 KSVC，Revision，Deployment 资源都受到 Knative Controller 的约束，因此解决思路即是增加一个自定义的拦截器，在带有特定 label 的 Pod 创建时，进行拦截，并通过加 Volume 的相关配置保存在 annotation 中，拦截器解析出配置后再为 Pod 添加相关 Volume 信息。通过此种解决方案，可以以较少的代价将 Knative 服务的日志接入到公司原有的日志平台中。<br>
<br>非挂载式收集：<br>
<br>当 Docker 作为 Kubernetes 容器运行时，容器日志的落盘由 Docker 完成，保存在 /var/lib/docker/containers/$&#123;container_id&#125; 目录下。同时 kubelet 会在 /var/log/pods 和 /var/log/containers 下建立软链接，指向 /var/lib/docker/containers/$&#123;container_id&#125; 下的容器日志文件。/var/log/containers 目录中日志名称格式为：$&#123;pod_name&#125;_$&#123;namespace&#125;_$&#123;container_name&#125;_$&#123;container_id&#125;。<br>
<br>目前 Severless FaaS 服务所部署的 namespace 都符合 faas-* 的命名格则，因此通过对 Filebeat 配置新增日志收集路径，收集 /var/log/containers 目录下所有满足正则表达式："<em>_faas-</em>.log" 的文件，并发送到新的 topic。同时开发新的日志处理流来处理这个 topic，实现 Serverless FaaS 业务日志接入日志平台。<br>
<br><strong>冷启动时长</strong><br>
<br>分环境预热配置：<br>
<br>Serverless 冷启动优化是一个复杂的系统工程。目前主要是在生产环境中通过控制服务实例最小数为1来避免冷启动问题，保证服务的响应时间。<br>
<br><strong>服务灾备迁移</strong><br>
<br>服务灾备迁移主要分为两个方面，其一是 Knative 自身的相关组件和其依赖的组件（比如Istio）灾备迁移；其二就是运行在 Serverless 平台之上的服务的灾备迁移。<br>
<br>针对 Knative 自身和依赖组件，采用 Kubernetes 备份恢复工具 velero，每日定时对相关的组件、配置进行备份。同时搭建一个运行在公有云上仅有少数节点的 Knative 集群作为迁移之用的备份集群。当需要启动灾备迁移时，首先通过 velero 根据将备份集群的 Knative 相关配置更新到最近一次的备份，然后通过公有云快速扩容节点的能力，将该集群节点数扩容，以承接随之而来的业务迁移的资源需求。<br>
<br>针对 Severless 平台上的服务，由于服务的所有变更都通过平台操作，因此平台能容易的保留每个服务的 manifest 。需要迁移服务时，只需将服务最新的 manifest 文件在备份集群上重新 apply 一次即可。<br>
<h3>规划和展望</h3>本节我们会从面向用户的 Serverless 产品角度，粗浅地谈谈提出些笔者自己的看法及方向规划，只期能抛砖引玉，与大家共勉。<br>
<br>Serverless FaaS 和 Serverless Application 从开发者角度是两个不同服务形态的产品，前者是函数态，后者是应用态。<br>
<br>理论上，所有服务都可以改造成函数态，所有服务也都可以快速地迁移到应用态，那么我们该怎么去看待两者区别？<br>
<br>笔者认为函数态开发难度低，业务嵌套少，适用于无状态、低耦合、逻辑变化快的业务，是快速解决场景落地问题的“锋利匕首”，短小精悍；<br>
<br>应用态优势是没有技术栈和接入场景限制，可发展潜力巨大，前期可以做到“量贩式”产品模式， 同时“app + mesh”的链路架构又可以让 Serverless 去承载更多生产级的核心应用。<br>
<br><strong>就目前看来应用态可以极大的发挥 Serverless 带来的价值，毕竟存量项目都是应用服务，流量为王；所以应用态依旧会是我们下一年要持续稳步发展的重点内容。</strong><br>
<br>另外还有一种衍生出来的产品形式也值得去关注：基于 Serverless 服务的工作流。<br>
<br>这两年国内的主流云商们也都把工作流商业化为云产品，用来协调多个分布式任务执行，可以用顺序、分支、并行等方式来编排分布式任务，工作流会按照设定好的步骤可靠地协调任务执行，跟踪每个任务的状态转换，并在必要时执行定义的重试逻辑，以确保工作流顺利完成，很适合处理 事务型业务流程编排 和 数据流水线处理 等流式计算任务。<br>
<br>在未来，我们也将继续深入使用 Knative Eventing，结合 RocketMQ channel，建立标准且高可用的 EventBridge 架构。在功能上，先做到 Serverless 产品间可以通过事件驱动做服务交互及工作流编排，再针对不同场景创建对应的自定义容器源，打通 Serverless 服务和内部服务的事件交互，实现“低成本、松耦合”的资源联动，满足更多地内部场景需求，带来符合期望的业务价值。<br>
<h3>思考和反思</h3>最后分享几点在实践私有化 Serverless 产品时的想法：<br>
<ol><li>私有化 Serverless 可能不适用于研发体量小或云原生基建缺失较多的公司，前面也有提到，Serverless是个系统产品，需要融入很多内部基建能力。为了 Serverless 反而需要投入更多甚至几倍的研发资源到缺失的基建开发上，一定程度上来说是背道而驰的做法。企业内私有化 Serverless 的形成是一个自然而然的演进过程，得先有底子，才有可能落地开花。</li><li>在做私有化 Serverless 之前，第一步需要先分析 Serverless 能带来的业务价值并且明确受众、调研公有云是否无法达成、预估整体投入产出比，第二步是确定合作目标，推进方需要根据专业的领域寻找专业的团队，不可盲目自研，第三步就是确定 Serverless 产品边界，底层技术革新难免会出现所谓的“功能重复”，这时候我们需要守住初衷和产品定位，拉开与“看似重叠”产品的差异性，体现出价值；这样 Serverless 落地之路会好走很多。</li><li>国内外对于 Serverless 产品定义和价值还没有完全统一，各个平台间也有着自己的标准，在当前百家争鸣的阶段，我们可以多关注主流云商的产品走向以及开源社区动态，结合内部业务诉求，适式调整发展路线。</li></ol><br>
<br>原文链接：<a href="https://tech.kujiale.com/kjl-sls-app-explore/" rel="nofollow" target="_blank">https://tech.kujiale.com/kjl-sls-app-explore/</a><br>
<br>作者：<br>
<ul><li>冰蛙、三土，来自酷家乐前端基础架构团队。</li><li>东悦、吕仙，来自酷家乐运维团队。</li></ul>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            