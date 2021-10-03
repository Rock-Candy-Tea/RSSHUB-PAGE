
---
title: '为什么我们说云原生时代，企业数字化转型更需要做好 API 全生命周期管理？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/6a02cd94df8746169cd4d088914d7487.png'
author: Dockone
comments: false
date: 2021-10-03 10:07:56
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/6a02cd94df8746169cd4d088914d7487.png'
---

<div>   
<br><h3>云原生下的机遇和挑战</h3>时至今日，Kubernetes 已至成熟期，云原生时代则刚刚开始。虽说云原生不只是围绕着 Kubernetes 生态，但无可质疑，Kubernetes 已是云原生生态的基石。通过规范 API 和 CRD 标准，Kubernetes 已经建立起了一个云原生 PaaS 生态帝国，成为了 PaaS 领域的事实标准。<br>
<br>这一层事实标准，对企业交付有着巨大的意义。在 Kubernetes 生态出现之前，类比于土木工程，连螺丝、螺帽这样的东西都缺少统一的标准，而甲方企业如果只关注上层业务功能，很容易把万丈高台架构于浮沙之上，导致业务的倾覆。不夸张的说，在企业交付领域，真是“天不生 Kubernetes，万古如长夜”。<br>
<br>以 API 管理中的 API 路由功能为例，如果不使用 Kubernetes，企业可能会选择 F5/Nginx/HAProxy/Zuul 等各式网关软件，做对应的路由配置。有的软件提供了控制台 UI，有的可能是人肉脚本运维，缺乏标准，运维技能也无法沉淀，关键人员离职可能会带来灾难。Kubernetes 把 API 路由的能力抽象为了 Ingress 资源，定义了标准，屏蔽了底层软件细节，通过 CNCF CKA 认证的人员都会具备 API 路由运维的能力。在 API 管理的领域，除了 API 路由，还有 API 流量治理策略，API 开放鉴权，以及调用量观测审计等环节，Kubernetes 以及 Istio 等生态都给出了一些标准定义，虽然其中很多尚未成熟，但标准和生态的未来已经愈发清晰。<br>
<h3>API 全生命周期管理是什么</h3>API 全生命周期管理（Full Life Cycle API Management）是指对 API 从规划、设计到实施、测试、发布、运行、调用直至版本变更与退出的整个周期的管理。<br>
<br>一般来说，API 全生命周期可以分为三个层面和六个阶段。<br>
<br><strong>三个方面是指</strong>：设计，实施，管理，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/6a02cd94df8746169cd4d088914d7487.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/6a02cd94df8746169cd4d088914d7487.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Mulesoft 对 API 管理三个层面的图示</em><br>
<br><strong>六个阶段是指</strong>：规划与设计阶段、开发阶段、测试阶段、部署与运行时阶段、运维监控阶段、版本管理与弃用阶段。<br>
<br>用以支持 API 全生命周期管理的工具应当具备以下能力：<br>
<ul><li>API 集市，用于 API 提供者发布文档展示应用程序的服务能力，API 的使用者查阅服务接口进而开发客户端。</li><li>API 网关和访问管理工具，用于 runtime 管理、访问管理、安全管理、数据收集等。</li><li>监控管理工具，用于监控 API 相关指标。</li><li>接口测试工具，用于测试接口。</li><li>API 设计工具，用于设计和编写 API 文档。</li></ul><br>
<br>近年来谷歌收购 Apigee、Red Hat 收购 3scale 等事件无一不在证明 API 生命周期管理越来越被业界所重视。<br>
<br>从2020 Ganter API 全生命周期管理“魔力象限”可以看到Google、Mulesoft、Microsoft、IBM、Kong 等众多熟悉的身影出现在了领导者第一象限；Amazon Web Services、TIBCO Software、Broadcom 等也紧随其后。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/5de43e1dac92eceb6e9df8f444057af6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/5de43e1dac92eceb6e9df8f444057af6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Magic Quadrant for Full Life Cycle API Management by gartner.com</em><br>
<h3>API 生命周期不同阶段解读</h3>API 管理的核心是需要服务 API 的整个生命周期并启用关联的生态系统。 API-First 方法将 API 视为产品并对其进行管理，强调整个生命周期的重要性。通过精心设计、管理和维护的 API 可为开发人员提供良好体验，为组织带来价值。<br>
<br>API 全生命周期管理设计的产物是 API 文档，实施的产物是 API 的服务实例，它们都是被管理对象。下面我们将针对 API 生命周期管理的不同阶段进行详细解读。<br>
<h4>规划与设计阶段</h4>规划与设计阶段要规划应用程序功能，设计 API，编写、评审以及发布 API 文档。<br>
<br>当开始规划应用程序新的功能点时，就要着手构思应用程序要呈现怎样的 API。API 涉及哪些资源、哪些操作、什么样的权限、什么样的场景等等，都是这个阶段的思考重点。设计 API 时需要充分考虑，如接口易用性、实现难度、价值等。如果不在此阶段思虑充分，就会设计出不可靠的 API，以至于开发出“腐烂”的代码和不可靠的功能，为组织带来风险。<br>
<br>设计阶段共有四个主要任务：<br>
<ul><li>设计：确定业务流程和需求，对资源合行为进行抽象。</li><li>建模：API 资源建模，API 操作与方法建模，请求/响应有效负载/代码建模等。</li><li>反馈：开发人员间互相反馈，完善设计稿。</li><li>验证：根据开发人员的反馈适当修改 API 设计，继续验证。</li></ul><br>
<br>API 设计的目标是产生一份 API 协议，一般是一份具有可读性的 API 文档。这种先行设计 API 的方法被称为“API-First”。<br>
<br>API-First 是 DevOps 实践中发展出来的，在项目开发中致力于开发出一致可重用的 API 方法论。顾名思义，API-First 就是 API 先行，在计划开发应用程序时，先设计应用程序接口，然后实现接口功能。与之相对的是 Code-First，即先实现应用程序功能，然后在此基础上根据外部需求抽象出接口。<br>
<br>相较于 Code-First，API-First 更加敏捷。API-First 的思路使得功能易于解耦，更加适合微服务拆分；API-First 通过接口发布功能，小巧轻快，能提高迭代速率；通过文档协调开发者间协作，可以提升开发效率；通过版本化的 API 持续集成，符合 DevOps 的精神内核。<br>
<h4>开发阶段</h4>开发阶段要实现规划与设计的全部接口，实现应用程序全部新功能。<br>
<br>开发阶段是产品功能从无到有的核心阶段，应用程序开发人员根据完善的 API 设计文档进行并行开发，以节约开发时间，提高开发效率。设计合理、表述清晰、风格统一、高一致性的 API 能令开发人员如沐春风，缩短学习时间，降低学习成本。<br>
<br>利用 API 管理工具，可以根据 API 文档生成服务端和客户端代码，多语言甚至框架级别的代码生成能力，能节约开发人员的编码成本；还可以生成接口测试代码和脚本，使得开发人员不必专门编写接口测试代码或者只需花少量的时间修改即可完成接口测试编写工作。<br>
<br>基于 API 文档的 mocking service 能很好地协调服务端和客户端开发人员的协作，当服务端 API 功能还未实现时，客户端开发人员可以利用 mocking service 调试开发，待服务端开发人员将阶段性成果部署到开发环境时，只需修改下客户端软件服务域名就可以联调。API 文档支持可编程 mocking，只需在文档中配置不同参数，就可以模拟不同场景下的接口响应，比如通过配置响应码模拟是否登录，通过配置 User-Agent 模拟不同来源的客户端等。<br>
<h4>测试阶段</h4>测试阶段要对已实现的接口进行充分测试，验证接口功能是否按预期实现，它要求接口可用、准确、稳定、可靠（也有人将开发和测试作为一个阶段，因为开发测试总是交织在一起的）。<br>
<br>API 开发完成之后，要经过几轮 API 测试以确保其正常运行。如果测试顺利完成，则可以继续进行下一个生命周期阶段，但大多数情况下，API 会经历几轮测试和调整，然后再进行部署。API 全生命周期管理要求 API 测试自动化，因此不能仅仅依赖接口测试脚本、桌面接口测试工具来做接口测试，集成到持续交付和部署的 DevOps 流程中的自动化测试工具在这里至关重要。<br>
<br>以往的许多 API 管理工具，将 API 生命周期各个阶段割裂开来。就开发阶段与测试阶段而言，接口测试往往面临许多痛点，比如：<br>
<ul><li>重复定义的问题：在 API 设计阶段，就已经设计过 API 接口，在测试阶段，又将接口要素重新编写一遍，从 URI 到各种参数，全要重新填写一遍。</li><li>编排接口能力不足的问题，一些传统的接口测试工具虽然能测试单个接口，但却将接口孤立的看待，没有将接口有机编排起来，难以串联成一个个完整的场景。</li></ul><br>
<br>所以，必须将 API 生命周期的各个阶段有机地联系起来。用户在编写测试用例时，直接引用文档里的接口，就避免了重复定义的问题；在设计 API 时充分周全地建模，会让编排就变得十分自然。<br>
<h4>部署与运行时阶段</h4>运行时阶段要将实现了特定 API 的应用部署到相应的环境，使 API 作为服务实例正式向外提供服务。<br>
<br>运行时阶段，可以从 API 角度对实例进行访问管理，授权客户端对实例进行访问，并限制它们的访问流量。还可以决定哪些接口可以被访问、哪些接口不可以被访问。每一个 API 的价值都值得单独考量，从商业运营角度看：<br>
<ul><li>流量：可以给初级用户开放少量流量，给重要用户开放大量流量。</li><li>接口：给初级开放初级接口，给重要用户开放高级接口。</li></ul><br>
<br><h4>运维监控阶段</h4>运维监控阶段要维护和监控实例的运行状态，对 API 的调用量、错误分布、响应时间、流量大小等维度进行监控。通过对接口的运维监控，可以调整实例的服务质量，如流量大小、访问限制等，还可以分析接口压力，调整服务资源。<br>
<h4>版本管理与弃用阶段</h4>版本管理是指添加新版 API、删除旧的 API、为版本标记语义化版本号等工作。弃用是指将某版本的 API 标记为弃用。由于服务的迭代更新，原来的 API 不再适应需求时，须需要进行版本管理或弃用。API 的订阅者收到版本变化的消息后，可以重新决定如何使用该系列接口。<br>
<h3>API 全生命周期管理最佳实践</h3>Erda 作为新一代企业级云原生 PaaS 平台，一直坚定地走在这条道路上，为企业提供符合标准并且值得信赖的 API 管理产品。Erda API 管理产品形态如图所示，是一个以 API 集市为中心的，包含 API 设计、API 访问管理等贯穿 API 全生命周期的产品矩阵。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/d85d2a97373e37d79a1d2adb505c7ebe.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/d85d2a97373e37d79a1d2adb505c7ebe.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>API 管理产品构成</em><br>
<h4>API 设计中心</h4>Erda Cloud API 设计中心基于可视化的编辑方式，通过直观而友好的交互界面，用户无需了解任何 REST API 规范标准，也无需具备任何关于 API 描述语言的知识，就可以轻松编写出一份具有专业水平的 API 文档。同时采用 OpenAPI 3.0 协议标准，任何时候都可以交付、迁出文档，一次设计，随处使用；在其他平台托管的 API 文档、代码中生成的 Swagger 文件等，也都能轻松迁移上来。<br>
<br>Erda API 设计中心将 API 文档托管到代码仓库中，这一设计使得接口描述和接口实现代码关联在一起。开发人员进入代码仓库，选择对应的代码分支，维护接口文档，可以很好地保持文档和新开发功能的同步。这样的理念遵循了 GitOps 配置即代码的思想。<br>
<br>文档托管到仓库中，还意味着可以基于分支进行文档协作。不同用户编写同一篇文档时，只要从源分支切出新的分支，在新的分支上编辑文档，然后再进行分支的合并。同一服务不同接口的负责人，随时可以设计自己负责的接口，又随时合并回去，不会相互影响和阻塞。<br>
<h4>API 集市</h4>API 集市使用了语义化版本机制来实现 API 文档的版本管理。版本号格式形如 major.minor.patch ，其中：<br>
<ul><li>major 为主版本号，主版本号的变化通常表示发生了重大变更或不向下兼容的变更。</li><li>minor 是次版本号，次版本号的变化通常表示增加了新特性，仍向下兼容。</li><li>patch 是修订号，修订号的变化通常表示对现有版本作较小的、局部的修正。</li></ul><br>
<br>除了语义化版本号外，还有一个称为“版本名称”的版本标记，它一般是有自解释性的单词或短语，表示当前文档版本的命名。版本名称与语义化版本号中的 major 是唯一对应的，版本名称可以视作是主版本号 major 的别名。这样版本化管理的好处是，将 API 文档的增长与应用程序的增长一视同仁，可以从 API 的角度审视应用程序的功能。版本号解释了服务更迭间的兼容性和依赖关系，不管是所有者还是使用者，都能根据版本号语义清晰地了解服务的变更情况。<br>
<br>API 资源可以关联到 Erda Cloud 上具体的服务实例地址。通过这样的关联，API 提供方可以进一步实现 API 的访问管理，调用方也就可以在 API 集市中申请调用并测试接口。<br>
<h4>访问管理</h4>API 提供者在集市中将 API 资源与 Erda Cloud 上具体的服务实例地址关联之后，再为 API 资源创建访问管理，调用者就可以在 API 集市中申请调用该 API；提供者收到调用申请后进行审批，为客户端设置 SLA 配额；获批的客户端获得访问资质，就可以从外部访问接口了。此后，调用方还可以在访问管理中切换 API 版本，将请求转发到不同版本对应的服务实例上，从而在客户不感知的情况下进行 API 版本的升级或回滚。<br>
<br>API 访问管理的功能都是基于 Erda 云原生网关产品的能力实现的，相比直接使用网关的配置能力，使用 API 访问管理简化了很多 —— 用户仅仅跟 API 打交道。<br>
<br>基于 Erda Cloud 的 API 管理产品，企业可以实现 API 全生命周期管理的最佳实践。如下图所示，可以分别从 API 的提供者和调用方两个视角来看待API 管理这件事：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/a874fdf57430a5035f1852696fdb74bc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/a874fdf57430a5035f1852696fdb74bc.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>API 所有者（左）和使用者（右）的视角看 API 管理</em><br>
<br><strong>从 API 提供者的视角来看</strong>：首先需要跟随服务功能变更，及时更新 API 设计中心的文档，因为文档也基于代码仓库管理，可以通过 Code Review 的方式确保 API 文档的及时同步。在开发联调阶段，API 提供者可以将 API 文档发布到集市，依赖此接口的其他模块功能就可以并行开发。如果有 API 对外开放的需求，API 提供者就为对应的 API 资源设置访问管理功能，在访问管理控制台可以实时观测外部的调用流量。<br>
<br><strong>从 API 调用方的视角来看</strong>：如果是测试工程师，应该基于开发人员提供的 API 文档，进行自动化接口测试用例的设计，而不是维护一份测试专用的接口文档。如果是外部集成方，通过 API 集市去发现所需的功能接口，申请调用成功后，应该在 API 集市进行简单的接口访问测试，确认功能符合预期；然后根据 API 文档进行集成模块的代码编写、部署；最后可以在 “我的访问” 中查看调用流量。<br>
<br>软件在自己的生命周期里不断迭代变化，API 也是一样。无论 API 提供者还是调用方，都要重视 API 迭代的影响。提供方要严格遵循 API 集市的语义化版本机制，当出现 Breaking Change 时，应该为新的 Major 版本创建独立的访问管理入口，并将旧版本标记弃用，引导调用方使用新的版本；调用方应该及时关注订阅通知，了解所使用 API 文档的最新版本情况。<br>
<br>Erda Cloud 的 DevOps 功能提供了云原生场景下 CI/CD 能力，应该把 API 管理也视作 CI/CD 的一部分。可以使用 Erda Cloud 的自动化测试平台，对接 API 集市，在 CI 流程中加入自动化接口测试；可以使用 Erda 的流水线扩展，在 CD 流程后自动发布 API 版本，并自动关联上服务的 Kubernetes Service 地址。<br>
<br>Erda Cloud 基于云原生为企业系统架构提供了一站式 PaaS 服务，Erda Cloud 的 API 管理亦是在云原生的土壤上自然生长出的产品。API 全生命周期管理作为企业数字化的关键一环，企业如果采用云原生的架构，一定要选择与之契合的 API 管理产品，否则可能导致适配成本的增加和管理效率的低下。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            