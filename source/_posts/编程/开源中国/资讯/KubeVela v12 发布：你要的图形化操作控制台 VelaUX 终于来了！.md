
---
title: 'KubeVela v1.2 发布：你要的图形化操作控制台 VelaUX 终于来了！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23925f99a10b4a1094915cfdbd834500~tplv-k3u1fbpfcp-zoom-1.image'
author: 开源中国
comments: false
date: Mon, 07 Feb 2022 10:10:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23925f99a10b4a1094915cfdbd834500~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#7f8c8d"><em>作者：KubeVela 社区</em></span></p> 
<p>随着云原生的不断发展和成熟，越来越多的基础设施能力逐渐标准化成为 PaaS 平台或者 SaaS 化产品。一个产品的诞生不再像过去那样需要建立一个团队，从开发、测试一直到运维、基础设施全部分多种角色系统完成。如今，敏捷组织文化和云原生技术驱动，使得这些职责更多的是“左移”到了开发者身上，测试左移、监控左移、安全左移，以及 DevOps 等一系列理念都是在强调，通过开源项目或者云的产品和服务将测试、监控、安全、运维等一系列事务提前到开发阶段完成。这看似美好的愿景却给开发者带来了巨大的挑战，开发者对底层五花八门的产品和复杂 API 缺乏掌控力，他们不仅仅是在做选择，更多的需要去理解和协调底层复杂异构的基础设施能力，以便满足上层业务的快速发展和迭代需求。</p> 
<p>这种复杂性和不确定性无疑大大降低了开发者的体验，降低了业务系统的交付效率，增加了运维风险。开发者体验的核心是“简单”和“高效率”，不管是开发者还是企业都需要更好用的开发者工具或者平台来达成。在现代云原生技术之上打造一款帮助开发者从开发、交付以及后续持续运维的一体化平台，一直是 KubeVela 演进的核心目标。如图 1 所示，在 v1.2 版本中，我们围绕开发者体验新增了 UI 控制台组件（VelaUX），简化了编排 YAML 的复杂性，完善了插件体系建设，丰富了云资源的扩展能力，增加了大量 CI/CD 等生态对接的能力，进一步完善了开发者端到端的使用体验。</p> 
<p><img alt src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23925f99a10b4a1094915cfdbd834500~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">图 1：KubeVela 架构设计</span></p> 
<h2>发展历程回顾</h2> 
<p>让我们再来简单回顾一下 OAM 和 KubeVela 的发展阶段和历程：</p> 
<ul> 
 <li><strong>OAM（Open Application Model）诞生和成长</strong></li> 
</ul> 
<p>在复杂的世界中要创造简单，首先我们需要解决的问题就是抽象和标准化。阿里云和微软联合推出 <strong>OAM</strong> 模型，创新性地提出“关注点分离”的理念，开发者关注业务本身、运维关注模块化能力。OAM 模型围绕“一切皆服务，全面模块化”的思想，为各大厂商和云原生的平台构建者们实现自己的应用管理平台提供了简单易用与高度可扩展相结合的标准实践方式。该模型提出后的短短一年内便得到了包括 AWS、Oracle、腾讯、华为在内的国内外各大厂商响应，被国家信通院立项作为行业标准。因为大家有共同的目标，降低云原生的使用门槛，让应用交付和管理更简单。</p> 
<ul> 
 <li><strong>KubeVela 开源项目 v1.0 发布，为社区带来了 OAM 的标准实现</strong></li> 
</ul> 
<p>有了 OAM 模型作为实践指导，社区高级玩家也开始创造自己的工具来实践，包括阿里、微软、Oracle、Upbond、腾讯在内的一系列公司都基于 OAM 的指导构建了自己的业务平台。但对于更广大的开发者和中小型企业群体来说，他们却无法直接享受模型带来的红利，于是，KubeVela 作为 OAM 社区的官方实现引擎诞生了。它从一开始就由 7 家来自不同组织的 OAM 社区成员从零到一构建。KubeVela 的实现吸收了多家公司针对 OAM 的实践经验，同时结合 Kubernetes 社区生态优势，实现了自动化、可收敛、幂等且稳定的应用发布控制器，围绕 IaC（基础设施即配置）构造了用户友好的抽象层，帮助开发者实现了开箱基于的 OAM 实现引擎。</p> 
<ul> 
 <li><strong>KubeVela v1.1 发布，实现应用交付工作流，原生支持混合环境多集群应用交付</strong></li> 
</ul> 
<p>随着企业上云进程的推进，混合云、分布式云等多元化基础设施逐渐成为常态。KubeVela 作为现代应用管理系统也顺应潮流，整体架构升级为面向混合环境做应用交付和管理的控制平面，将所有的功能天然构筑在多集群技术之上。我们相信，出于高可用、成本性能、数据安全等多方面因素，未来大多数企业应用的形态都将是异构多元的。KubeVela v1.1 版本的发布，同时也实现了高度可扩展的应用发布工作流，它天然以混合环境架构呈现，创新性的实现了交付工作流与应用抽象相结合的工作模式，实现了面向终态的应用交付工作流，大大简化了流程编排的复杂性。</p> 
<p>时间来到 2022 年，KubeVela 也正式进入了第四个阶段，在原先核心控制器 API 基本稳定的基础上，我们以插件的形式增加了一系列开箱即用的功能。让开发者可以通过 UI 控制台的方式，连接 CI/CD 完整流程，端到端发布多集群应用，进一步提升开发者体验。</p> 
<h2>v1.2 版本的核心能力</h2> 
<h3>图形化操作控制台（VelaUX）</h3> 
<p>提供好用的图形化操作界面是降低开发者使用门槛的首选途径，从 KubeVela 诞生以来，社区对 UI 控制台的呼声一直很高。从 v1.2 版本开始，它正式到来了。打造 UI 控制台的目的是帮助开发者以更标准化的方式组装和管理异构业务应用，帮助他们分析和更快的发现业务故障和阻碍。</p> 
<p>VelaUX <strong>[1]</strong> 是 KubeVela 的前端项目，设计实现时它充分考虑了 KubeVela 的可扩展性这一核心要点。引入了低代码平台的理念来打造前端，我们的目标是打造一个可以通过拖拉拽方式就能做到自定义应用交付输入参数，并且实现运行数据可观测的平台。为此我们设计了前端描述规范（UISchema <strong>[2]</strong> ），配合 KubeVela 的模块化定义（X-Definition <strong>[3]</strong> ），通过配置就可以渲染出丰富的前端交互元素。同时为了让前端的数据查询也配置化，我们设计了多维数据自定义查询语言（VelaQL <strong>[4]</strong> ），这样的设计形成了 KubeVela 交付和管理异构应用的基础。</p> 
<p>目前通过 VelaUX ，用户可以管理扩展，连接 Kubernetes 集群，分配交付目标，规划环境和交付各类型应用，并观测应用运行状态，实现应用交付的完整闭环。</p> 
<p><img alt src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a1c7eea9bda4c42affd39d71e66cba3~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">图 2：VelaUX 预览</span></p> 
<p>如图 2 所示，VelaUX 中出现了一些新名词，请参考核心概念 <strong>[5]</strong> 文档进行学习和了解。</p> 
<h3>多环境统一化管理</h3> 
<p>KubeVela 将 N 个Kubernetes 集群，N 个云厂商服务或其他私有云服务统一为大的基础设施资源池。在此基础上，我们的开发者可以按照业务需求、流程需求、团队需求等多种业务维度划分环境。在大资源池的基础上形成环境空间。同一个应用可发布到不同的环境，环境之间从管理到运行态完全隔离。</p> 
<p><img alt src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb60c7c4971d420f9ca8954a4c9b5b45~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">图 3：多环境/多集群应用管理页面</span></p> 
<p>如图 3 所示，应用可被发布到生产、测试、默认三个环境中，每一个环境可以包括多个交付目标，每一个交付目标背后可以是独立的 Kubernetes 集群。</p> 
<h3>异构应用标准化交付</h3> 
<p>在云原生体系中，我们交付应用的形式选择非常多。基于 Kubernetes 基础设施，我们既可以通过成熟的 Helm Chart 包交付中间件和第三方开源应用，也可以通过镜像交付企业业务应用，还可以通过 OpenYurt 交付管理边缘应用。基于云服务商的开放能力，我们可以交付数据库、消息、缓存等中间件，也有日志、应用监控等运维能力。</p> 
<p>对于这么多的可选项，KubeVela 采用标准的 OAM 规范实现对异构应用的统一交付和管理。KubeVela 实现了高度可扩展的交付系统，通过内置、社区共享等形态帮助用户扩展平台，以一致化的交付和管理体验处理异构的应用。在 KubeVela 之上，开发者看到的都是模块化、一切皆服务的管理形态。</p> 
<p><img alt src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33f4b070002c499fb7818e47091b2716~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">图 4：云服务应用管理页面</span></p> 
<p>如图 4 所示，我们可以看到，相同的应用管理页面，用户可以非常便捷得获取到云服务应用。开发者可以通过阅读下面几篇文档查看异构应用的交付过程：</p> 
<ol> 
 <li>交付 Docker 镜像 <strong>[6]</strong></li> 
 <li>交付 Helm Chart 包 <strong>[7]</strong></li> 
 <li>交付 Kubernetes 资源 <strong>[8]</strong></li> 
 <li>交付 云服务 <strong>[9]</strong></li> 
</ol> 
<h3>扩展体系（Addon）</h3> 
<p>KubeVela 从一开始就是设计为一款微内核高可扩展的系统，上文我们说到异构应用，KubeVela 可以通过扩展体系，以标准化的形态，扩充无限的应用交付能力。既匹配企业差异性诉求，也不带来过多的认知负担。KubeVela 中可扩展的点包括了组件类型、运维能力、工作流类型、应用交付策略等。在当前版本中，我们发布了 Addon 扩展体系。Addon 是组织各种扩展能力的承载体，它便于分发和管理。</p> 
<p><img alt src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a38773f1ddd4ac09e0e2172928aa3ea~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">图 5：KubeVela 插件管理页面</span></p> 
<p>目前在官方仓库中已经存在如图 5 所示的可用 Addon。同时在实验性仓库中我们正在联合社区用户积极创造更多的扩展能力。当然，这里需要每一个社区开发者的积极参与。</p> 
<p>截止到现在，KubeVela 已经成长为一款可直接服务于广大开发者的应用交付平台，那么企业哪些场景可以直接利用 KubeVela 呢？我们整理了以下几个常见场景：</p> 
<h2>企业开发场景解决方案</h2> 
<h3>多集群应用 DevOps</h3> 
<p>在过往社区的交流中，我们发现企业主流的研发体系都类似如图 6 所示的结构，他们使用云服务厂商提供的计算资源作为生产、演示环境。使用自己购买或历史遗留的服务器搭建开发、测试环境。如果业务有多区域或灾备需求，生产环境可能需要部署到多个区域或多云。</p> 
<p><img alt src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cfa0b86c2814de3bf19f59003eb3e70~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">图 6：多集群应用实践架构</span></p> 
<p>对于基础的 DevOps 流程，包括了代码托管和 CI/CD 的环节。KubeVela 目前为你提供 CD 环节的支持。对于企业实践的步骤如下：</p> 
<ol> 
 <li>根据实际情况准备本地或云服务资源。至少单项打通本地和云资源的网络，便于资源集中管理。</li> 
 <li>将 KubeVela 系统搭建在生产环境中，保障持续的可用性。</li> 
 <li>通过 KubeVela 部署 Gitlab、Jenkins、Sonar 等 DevOps 工具，并打通工具链。通常情况下，代码托管和开发工具的可用性至关重要，我们需要将其部署在生产环境中（如果你本地机房具备生产可用性，且希望代码数据在本地环境流转，可部署在本地机房）。</li> 
 <li>通过 KubeVela 规划本地开发环境，部署本地测试用中间件，规划生产环境和部署云服务中间件。</li> 
 <li>通过 Jenkins 搭建业务代码 CI 流水线，产出 Docker 镜像交由 KubeVela 进行多环境部署，形成完整应用交付工作流。</li> 
</ol> 
<p>结合 KubeVela 的多集群应用 DevOps 方案有如下优势：</p> 
<p>（1）开发者无需掌握过多的 Kubernetes 生态知识，可实现异构应用云原生部署。</p> 
<p>（2）多集群，多环境统一管理，原生可部署跨集群应用。</p> 
<p>（3）统一的应用管理模式，无论是业务应用还是开发工具链。</p> 
<p>（4）灵活的工作流，帮助企业打通各种开发规范流程。</p> 
<h3>混合环境一体化管理</h3> 
<p>不同的企业往往都存在不一样的基础设施和业务诉求。在基础设施侧：企业可能搭建了私有云，可能购买了公有云，可能还有边缘计算资源。在业务侧：不同的业务规模不同，资源需求不同，可能有多云多活应用，也有企业遗留系统。在研发侧：业务研发往往需要开发、测试、预发和生产环境。在管理侧：不同的业务团队需要相互隔离，又可能需要业务互通。</p> 
<p>随着时间的累积，企业由于职责边界和不同分工的影响，会逐渐形成不同业务团队相互独立甚至割裂的状态，这种割裂包括了：开发工具割裂，技术架构割裂，业务管理形态割裂。KubeVela 秉持着“尊重现实，积极创新”的原则，带来的方案是追求统一的过程中用高扩展的能力去兼容差异性。</p> 
<ul> 
 <li> <p>面对基础设施差异，我们支持以 Kubernetes API、云服务 API 或其他自定义 API 的形态，去对基础设施进行充分的模型化。最终通过统一的 OAM 模型向上暴露一致的概念。</p> </li> 
 <li> <p>面对业务架构差异，应用模型是开放的，对架构无要求的。KubeVela 做的是连接和赋能，连接已有系统，通过扩展机制加持新的生态技术。</p> </li> 
 <li> <p>面对开发工具链的差异，企业中可能已经存在不同的开发工具链，产出不同的业务制品。KubeVela 通过扩展和标准模型去支持各类制品，实现其标准化交付。当然，它的标准逐步衍生到前置环节，帮助企业逐步实现工具链一致化。因此，你不用担心你是用的 Gitlab 还是 Jenkins，它都能对接。</p> </li> 
 <li> <p>面对运维能力差异，企业中不同团队的运维能力、工具方案可以在 KubeVela 的规范下逐步积累，能力互通。更多运维能力也同样在社区的维度进行共享和复用。</p> </li> 
</ul> 
<p>因此，使用 KubeVela 来作为企业打通业务，进行统一能力建设的基础平台，它是可落地、有未来的方案。</p> 
<h3>自定义企业发布平台</h3> 
<p>从 Heroku 、Cloud Foundry 时代开始，市场上一直在产生不同的 PaaS 平台，我们都知道固定模式的发布平台往往不适合所有的企业。举个例子，某些规范化程度较高的企业，他们基于业务的特性，发布应用时仅需更新镜像名称，然而使用通用 PaaS 就不得不去理解大量的概念和参数。再比如某个企业生产的是 AI 应用，对于 AI 应用的发布与普通应用有比较大的区别，这时就需要定制 AI 场景的 PaaS，企业不得不付更多的费用和学习更多的概念。</p> 
<p>通用产品不符合企业需求时，自研是真实存在的诉求。但是对于从零开始自研平台，必然又需要投入大量的人力物力，甚至超过了企业核心业务的投入，这显得得不偿失。KubeVela 也考虑到了具备自研能力企业的独特诉求，他们可以基于 KubeVela 微内核、高可扩展的设计，针对自己的业务场景和领域知识，打造属于自己的、更为简单易用的业务平台。</p> 
<p>对于需要自研发布平台的企业来说，KubeVela 的微内核是一个 PaaS 平台研发框架。一方面，企业可以根据自己的需求自研或者安装社区的各种功能插件；另一方面，企业也可以基于 OAM 模型修改模块化配置，新增或裁剪用户使用的参数。这种模块化的设计可以大大降低企业的投入成本，同时可以跟上社区的发展潮流，随时将社区更多的先进技术转化为自身的生产力。</p> 
<h2>参与社区</h2> 
<p>做了这么多的介绍，你是否对 KubeVela 的发展有了一些新的认识，没有哪个产品是绝对的银弹，也没有一个方案可以解决所有的问题。但是我们的理想是可以创造一个标准化模式，让更多的企业和开发者用户参与到这场为了“简单”和“高效”的开发者体验战役中来。KubeVela 还很年轻，我们希望你可以参与进来共同打造。这里非常感谢在过去参与 KubeVela 贡献的 100 多位开发者 <strong>[10]</strong> ，正是因为你们的携手努力，才让我们的社区生态变得更加繁荣。</p> 
<h3>共建 OAM 应用规范</h3> 
<p>对于 OAM 应用规范，模型的更新和升级基于 KubeVela 实践驱动，但是它并不绑定 KubeVela 实现。它是 KubeVela 在云原生应用交付和管理层面实践经验的总结和抽象，是创造规范化应用管理体系的最佳实践和核心理念。我们非常欢迎云厂商、平台厂商、最终用户可以参与进来，同时我们也欣喜的看到国内包括腾讯在内的多家厂商对 OAM 应用规范的关注和支持。任何人、组织都可以发表你的想法、建议和思考。</p> 
<p>参与 OAM 模型讨论：</p> 
<p>​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foam-dev%2Fspec" target="_blank">​https://github.com/oam-dev/spec​</a>​</p> 
<h3>共建 Addon 扩展生态</h3> 
<p>如上文介绍的一样，我们已经开启了 Addon 的扩展体系，非常欢迎社区的创造者、开发者可以来贡献更多的扩展能力。</p> 
<p>如何扩展和贡献 Addon 参考文档：</p> 
<p>​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Fplatform-engineers%2Faddon%2Fintro" target="_blank">​https://kubevela.net/zh/docs/platform-engineers/addon/intro​</a>​</p> 
<h3>贡献云服务能力</h3> 
<p>KubeVela 通过集成 Terraform Module 来扩展云服务集成能力，我们已经支持了常用的云资源 <strong>[11]</strong> ，欢迎社区朋友参考并贡献更多的云服务厂商和产品。</p> 
<p>如何扩展和贡献云资源 参考文档：</p> 
<p>​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Fplatform-engineers%2Fcomponents%2Fcomponent-terraform" target="_blank">​https://kubevela.net/zh/docs/platform-engineers/components/component-terraform​</a>​​​</p> 
<h3>反馈你的需求或痛点</h3> 
<p>或许你是普通开发者，也或许你是云原生领域的从业者，如果你认可我们的方向，认可我们正在做的事情，我们非常欢迎你可以参与到 KubeVela 社区讨论中来。</p> 
<p>社区讨论：</p> 
<p>​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foam-dev%2Fkubevela" target="_blank">​​https://github.com/oam-dev/kubevela​​</a>​</p> 
<h3>KubeVela 网站加速访问</h3> 
<p>KubeVela 的官方文档托管在GitHub （​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foam-dev%2Fkubevela.io" target="_blank">​https://github.com/oam-dev/kubevela.io​</a>​ ）上，如果你发现有任何错漏或者想要参与翻译，欢迎直接到项目中贡献。同时为了国内用户可以加速访问，我们增加了 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubevela.net" target="_blank">kubevela.net</a> 这个域名，可以方便国内用户更快的访问，内容与 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubevela.io" target="_blank">kubevela.io</a> 的域名完全一致、实时同步。</p> 
<p>​KubeVela 是 CNCF 沙箱项目，了解更多信息，请点击​​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fdocs%2F" target="_blank">​​<strong>此处</strong>​​</a>​​查阅官方文档。</p> 
<h2>相关链接</h2> 
<p>[1] VelaUX：</p> 
<p>​<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foam-dev%2Fvelaux" target="_blank">​https://github.com/oam-dev/velaux​</a>​</p> 
<p>[2] UISchema：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.io%2Fzh%2Fdocs%2Freference%2Fui-schema" target="_blank">https://kubevela.io/zh/docs/reference/ui-schema</a></p> 
<p>[3] X-Definition：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Fplatform-engineers%2Foam%2Fx-definition" target="_blank">https://kubevela.net/zh/docs/platform-engineers/oam/x-definition</a></p> 
<p>[4] VelaQL：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.io%2Fzh%2Fdocs%2Fplatform-engineers%2Fsystem-operation%2Fvelaql" target="_blank">https://kubevela.io/zh/docs/platform-engineers/system-operation/velaql</a></p> 
<p>[5] 核心概念：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Fgetting-started%2Fcore-concept" target="_blank">https://kubevela.net/zh/docs/getting-started/core-concept</a></p> 
<p>[6] 交付 Docker 镜像：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Ftutorials%2Fwebservice" target="_blank">https://kubevela.net/zh/docs/tutorials/webservice</a></p> 
<p>[7] 交付 Helm Chart 包：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Ftutorials%2Fhelm" target="_blank">https://kubevela.net/zh/docs/tutorials/helm</a></p> 
<p>[8] 交付 Kubernetes 资源：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Ftutorials%2Fk8s-object" target="_blank">https://kubevela.net/zh/docs/tutorials/k8s-object</a></p> 
<p>[9] 交付云服务：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.net%2Fzh%2Fdocs%2Ftutorials%2Fconsume-cloud-services" target="_blank">https://kubevela.net/zh/docs/tutorials/consume-cloud-services</a></p> 
<p>[10] 100 多位开发者：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foam-dev%2Fkubevela%2Fgraphs%2Fcontributors" target="_blank">https://github.com/oam-dev/kubevela/graphs/contributors</a></p> 
<p>[11] 常用的云资源：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubevela.io%2Fzh%2Fdocs%2Fend-user%2Fcomponents%2Fcloud-services%2Fprovider-and-consume-cloud-services%23%25E6%2594%25AF%25E6%258C%2581%25E7%259A%2584%25E4%25BA%2591%25E8%25B5%2584%25E6%25BA%2590%25E5%2588%2597%25E8%25A1%25A8" target="_blank">https://kubevela.io/zh/docs/end-user/components/cloud-services/provider-and-consume-cloud-services#支持的云资源列表​</a></p> 
<p>您可以通过如下材料了解更多关于 KubeVela 以及 OAM 项目的细节：</p> 
<p>• 项目代码库：​<a href="https://www.oschina.net/news/181454/github.com/oam-dev/kubevela">​github.com/oam-dev/kubevela​</a>​ 欢迎 Star/Watch/Fork！</p> 
<p>• 项目官方主页与文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubevela.io" target="_blank">kubevela.io</a> ，从 1.1 版本开始，已提供中文、英文文档，更多语言文档欢迎开发者进行翻译。</p>
                                        </div>
                                      
</div>
            