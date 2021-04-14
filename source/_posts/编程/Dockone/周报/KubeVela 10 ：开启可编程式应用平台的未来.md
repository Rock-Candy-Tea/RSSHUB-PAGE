
---
title: 'KubeVela 1.0 ：开启可编程式应用平台的未来'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/8adf1bc1649ecb271a4d266e5d7b967e.png'
author: Dockone
comments: false
date: 2021-04-14 04:08:16
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/8adf1bc1649ecb271a4d266e5d7b967e.png'
---

<div>   
<br>作者 | KubeVela 项目维护者<br>
来源 | <a href="https://mp.weixin.qq.com/s/MHOsy8fRm92KdtXiZ2rpMw">阿里巴巴云原生公众号</a><br>
<br>作为 OAM（Open Application Model）在 Kubernetes 上的实现，KubeVela 项目从 oam-kubernetes-runtime 演进至今不过半年多时间，但发展势头非常迅猛，不仅连续登上 GitHub Go 语言趋势榜首和 HackerNews 首页，更是迅速收获了包括 MasterCard、Springer Nature、第四范式、SILOT、Upbound 等来自世界各地、不同行业的终端用户，甚至还出现了像 Oracle Cloud、Napptive 等基于它构建的商业化产品。就在 2021年3月底，KubeVela 社区宣布包含所有稳定版 API 的 <a href="https://github.com/oam-dev/kubevela/releases/tag/v1.0.0">v1.0 版本发布</a>，正式开始向企业级生产可用迈进。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/8adf1bc1649ecb271a4d266e5d7b967e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/8adf1bc1649ecb271a4d266e5d7b967e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>不过，如果你对云原生领域不太关注，可能对 KubeVela 还没有做过太深入的了解。别着急，本文就借着 v1.0 发布之际，为你详细的梳理一次 KubeVela 项目的发展脉络，解读它的核心思想和愿景，领悟这个正冉冉升起的云原生应用管理平台之星背后的“道之所在”。<br>
<br>首先，什么是 KubeVela？<br>
<br><strong>一言以蔽之，KubeVela 是一个“可编程式”的云原生应用管理与交付平台</strong>。<br>
<br>可是，什么是“可编程”呢？它跟 Kubernetes 又是什么关系？它能帮助我们解决什么问题？<br>
<br><h1>PaaS 系统的“能力困境”</h1>PaaS 系统（比如 Cloud Foundry、Heroku 等）自诞生以来，就以其简单、高效的应用部署体验而被所有人津津乐道。然而，大家也知道，我们今天的“云原生”，却是一个 Kubernetes 大行其道的世界，曾经的 PaaS（包括 Docker）到底遇到了什么问题呢？<br>
<br>其实任何一个尝试使用过 PaaS 的人，都会对这种系统的一个本质缺陷感触颇深，那就是 PaaS 系统的“能力困境”。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/3ad0c3ec693267c3afe1c77445f3e7aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/3ad0c3ec693267c3afe1c77445f3e7aa.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 1 - PaaS系统的能力困境<br>
<br>如图 1 所示，PaaS 系统在最开始使用的时候，往往体验非常好，也总能恰如其分地解决问题。但随着使用时间的推移，一个非常讨厌的情况就会出现：应用的诉求，开始超过 PaaS 系统能够提供的能力。而更可怕的是，一旦这个问题出现，用户对 PaaS 系统的满意度就会断崖式下跌，这是因为无论是重新开发平台增加功能，还是修改应用去适配平台，都是一项投入巨大但收益很低的事情。更何况所有人这时候都会开始对平台失去信心：谁知道下一次系统或者应用大改，是不是很快又要发生了？<br>
<br>这个“命门”，可以说是 PaaS 虽然具备云原生所需的一切要素、却最终未能成为主流的主要原因。<br>
<br>而相比之下，Kubernetes 的特点就比较突出了。尽管 Kubernetes 被人诟病“复杂”，但随着应用复杂度的提升，Kubernetes 的优点就会慢慢体现出来，尤其是当用户的诉求开始需要你去通过 CRD Controller 支持的时候，你一定会庆幸：幸亏当初选了 K8s。<br>
<br>这里的原因在于，Kubernetes 的本质其实是一个强大和健壮的基础设施能力接入平台，也就是所谓的 The Platform for Platform。它的这套 API 和工作方式，天然不适合直接跟人去进行交互，但却能够以非常一致的方式接入任何基础设施能力，为平台工程师构建 PaaS 等上层系统提供“无限弹药”。这种“BUG 级”的基础设施能力供给方式，让再精密的 PaaS 系统相比之下都像是一个碍手碍脚的“玩具”，这一点对于很多正挣扎于构建内部应用平台的大型企业来说（它们才是 PaaS 厂商真正想赢取的用户）无异于是久旱逢甘霖。<br>
<br><h1>云原生 PaaS ：新瓶装旧酒</h1>前面提到的一点其实很重要：假如一个大型企业要决定采纳一个 PaaS 系统还是选择 Kubernetes，平台团队往往才是能决定拍板的那一方。但另一方面，平台团队的意见虽然重要，并不意味着最终用户的想法就可以不管了。事实上，在任何一个组织中，直接创造价值的业务团队才持有最高的话语权，只不过起作用的时间稍晚而已。<br>
<br>所以在绝大多数情况下，任何一个平台团队拿到 Kubernetes 之后，并不会直接去让业务去学习 Kubernetes，而是会基于 Kubernetes 构建一个“云原生” PaaS，用它去服务业务方。<br>
<br>咦，于是乎大家兜兜绕绕，又回到了故事的原点。唯一的变化是，咱们今天这个 PaaS 是基于 K8s 实现的，确实轻松了不少。<br>
<br>但实际情况呢？<br>
<br>这个基于 Kubernetes 构建 PaaS 的故事，看似美好，其实整个过程却难免有些“心酸”。说的好听点是开发 PaaS，其实 80% 的工作是在设计和开发 UI，剩下的工作则是安装和运维 K8s 插件。而更令人遗憾的是，我们这样构建出来的 PaaS，其实跟以前的 PaaS 没有本质不同，任何时候用户诉求改变，我们都需要花大量时间重新设计、修改前端、排期上线。结果就是，K8s 日新月异的生态和无限可扩展的特性，都被“封印”在我们亲手构建的 PaaS 之下“不见天日”。终于有一天，业务方也实在忍不住要问了：你们平台团队上了 K8s，到底有啥价值？<br>
<br>上面这个“为了解决 PaaS 的固有限制，结果又引入一个新的 PaaS 和限制”的困局，是现今很多公司在落地云原生技术的过程中遇到的一个核心问题。我们似乎再一次把用户锁定在一层固定的抽象和能力集当中。<strong>所谓云原生化的好处，仅仅体现在咱们自己开发这个平台变得简单了 —— 而对业务用户来说，这似乎没什么太大的意义</strong>。<br>
<br>更为麻烦的是，云原生和 K8s 的引入，也让运维人员这个角色变得非常微妙。本来，他们所掌握的业务运维最佳实践，是整个公司中最重要的经验和资产。然而，在企业云原生化之后，这个工作的内容都必须交给 K8s 去接管。所以，很多人都说，K8s 要让“运维”失业了，这个说法虽然有点夸张，但确实反映出了这个趋势带来的焦虑。而且我们不禁也在从另一个角度思考，<strong>云原生化的背景下，应用运维的经验和最佳实践，又该怎么落实</strong>？就拿一个简单的工作负载举例子，一个 K8s Deployment 对象，哪些字段暴露给用户、哪些不能，虽然体现在 PaaS 的 UI 上，但肯定不能是靠前端开发说了算的吧。<br>
<br><h1>KubeVela：下一代可编程式应用平台</h1>阿里巴巴是整个业界在云原生技术上的先行者之一。所以上述这个围绕着应用平台的云原生技术难题，相对也比较早的暴露了出来。在 2019 年末，阿里基础技术团队与研发效能团队合作针对这个问题进行了大量的探索与尝试，最终提出了“可编程式”应用平台的思想，并以 OAM 和 KubeVela 开源项目的方式同大家见面。这套体系，目前已经迅速成为了阿里构建应用平台的主流方式。<br>
<br>简单地说，所谓“可编程”，指的是我们在构建上层平台的过程中，不会直接在 Kubernetes 本身上叠加抽象（哪怕只是一个 UI），而是通过 CUE 模板语言这种代码化（Code）的方式来抽象和管理、并透出基础设施提供的能力。<br>
<br>举个例子，比如阿里的某个 PaaS 要对用户提供一个能力叫做 Web Service，这个能力是指任何需要从外部访问的服务，都以 K8s Deployment + Service 的方式来部署，对用户暴露镜像、端口等配置项。<br>
<br>在传统方法中，我们可能会实现一个 CRD 叫做 WebService，然后在它的 Controller 里来封装 Deployment 和 Service。但这必然会带来前面 PaaS “能力困境”的问题：<br>
<ol><li>我们应该给用户暴露几种 Service 类型？未来用户想要其他类型怎么办？</li><li>用户 A 和用户 B 需要暴露的字段不统一该怎么办？比如我们允许用户 B 修改 Label，但 用户 A  不可以，那这个 PaaS 该怎么设计？</li><li>……</li></ol><br>
<br>而在 KubeVela 中，像上面这样面向用户的功能，则可以通过一段简单的 CUE 模板来描述（<a href="https://kubevela.io/docs/cue/component#how-to">这里有完整的例子</a>）。而当你编写好这样一个 CUE 文件之后，直接通过一句 kubectl apply，用户就可以立即使用到这个能力：<br>
<br><code class="prettyprint">$ kubectl apply -f web-service.yaml</code><br>
<br>更重要的是，只要执行上面这条命令，KubeVela 就会自动根据 CUE 模板内容生成这个能力的帮助文档和前端表单结构，所以用户立刻就会在 PaaS 里面看到这个 WebService 功能如何使用（比如有哪些参数、字段类型），并且直接使用它，如下 图 2 所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/195e45499284b84615ee1b412bdccc24.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/195e45499284b84615ee1b412bdccc24.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 2 - KubeVela 自动生成表单示意图<br>
<br>在 KubeVela 中，平台的所有能力比如金丝雀发布、Ingress，Autoscaler 等等，都是通过这种方式定义、维护和透出给用户的。这种端到端打通用户体验层与 Kubernetes 能力层的设计，使得平台团队可以以极低的成本快速实现 PaaS 以及任何上层平台（比如 AI PaaS，大数据 PaaS），同时高效地响应用户的持续演进诉求。<br>
<br><h2>1. 不只是 Kubernetes 原生，是 Platform-as-Code</h2>尤为重要的是，在实现层，KubeVela 并不是简单的在客户端去渲染 CUE 模板，而是使用 Kubernetes Controller 去渲染和维护生成的 API 对象。这里的原因有三点：<br>
<ol><li>Kubernetes Controller 天然适合维护用户层抽象到底层资源之间的映射，并且通过控制循环（Reconcile）机制永远确保两者的一致性，而不会发生 IaC（Infrastructure-as-Code） 系统里常见的 Configuration Drift（配置漂移）问题（即：底层资源跟用户层的输入发生不一致）。</li><li>平台团队编写的 CUE 模板 kubectl apply 到集群之后，就变成了一个 Kubernetes 中的一个自定义资源（Custom Resource），它代表了一个抽象化、模块化的平台能力。这个能力可以被全公司的平台团队复用，也可以继续修改演进，而且它是 Namespace 化的资源，所以平台的不同租户可以分配同名但不一样的模板，互不影响。这样彻底解决了不同租户对同一个能力的使用诉求不一样的问题。</li><li>如果随着时间推移，用户对平台功能的设计提出了新的要求，那么平台维护团队只需要安装一个新的模板，新的设计就会立刻生效，平台本身不需要做任何修改，也不用重启或者重新部署。而且新模板也会立刻被渲染成表单出现在用户 UI 上。</li></ol><br>
<br>所以说，KubeVela 的上述设计，从根本上解决了传统 IaC 系统用户体验虽好，但是生产环境上“靠不住”的老大难问题，<strong>又在绝大多数情况下让整个平台响应用户需求的时间从原先的数周，降低到几小时</strong>，完全打通了云原生技术与最终用户体验之间的壁垒。而它完全基于 Kubernetes 原生方式实现，确保了整个平台严格的健壮性，并且无论任何 CI/CD 以及 GitOps 工具，只要它支持 Kubernetes，就一定支持 KubeVela，没有任何集成成本。<br>
<br><strong>这套体系，被大家形象的称为：Platform-as-Code（平台即代码）</strong>。<br>
<br><h2>2. 别急，KubeVela 当然支持 Helm</h2>提到 KubeVela 以及 CUE 模板这些概念，很多小伙伴就开始问了：KubeVela 跟 Helm 又是什么关系啊？<br>
<br>实际上，Helm 和 CUE 一样，都是一种封装和抽象 Kubernetes API 资源的工具，而且 Helm 使用的是 Go 模板语言，天然适配 KubeVela Platform-as-Code 的设计思路。<br>
<br>所以在 KubeVela v1.0 中，任何 Helm 包都可以作为应用组件被部署起来，并且更重要的是，无论是 Helm 组件还是 CUE 组件，KubeVela 里的所有能力对它们都适用。这就使得通过 KubeVela 交付 Helm 包可以给你带来一些非常重要但是现有工具很难提供的能力。<br>
<br>举个例子，Helm 包其实很多是来自第三方的，比如 Kafka Chart，可能就是 Kafka 背后的公司制作的。所以一般情况下，你只能用，但不能改它里面的模板，否则修改后的 Chart 你就得自己维护了。<br>
<br>而在 KubeVela 中，这个问题就很容易解决。具体来说，KubeVela 提供一个运维侧的能力叫做 <a href="https://kubevela.io/docs/cue/patch-trait">Patch</a>，它允许你以声明式的方式给待交付组件（比如 Helm 包）里封装的资源打 Patch，而不用去关心这个字段有没有通过 Chart 模板透出来，而且 Patch 操作的时机，是在资源对象被 Helm 渲染出来之后、提交到 Kubernetes 集群处理之前的这个时间，不会让组件实例重启。<br>
<br>再比如，通过 KubeVela 内置的灰度发布系统（即：<a href="https://kubevela.io/docs/rollout/rollout">AppRollout</a> 对象），你还可以将 Helm 包作为一个整体进行渐进式发布且无需关心工作负载类型（即：哪怕 Chart 里是 Operator，KubeVela 也可以进行灰度发布），而不是像 Flagger 等控制器那样只能针对单一的 Deployment 工作负载进行发布。此外，如果将 KubeVela 同 Argo Workflow 集成，你还可以轻松的指定 Helm 包的发布顺序和拓扑等更复杂的行为。<br>
<br>所以说，KubeVela v1.0 不仅支持 Helm，它的目标是成为交付、发布和运维 Helm Chart 最强大的平台。一些社区同学已经在本文发布之前就迫不及待的试用了这部分功能，大家可以移步到<a href="https://xie.infoq.cn/article/4c7b59a7a96ac7af67501f9db">这篇文章</a>来阅读。<br>
<br><h2>3. 全自助式用户体验和云原生时代的运维</h2>得益于 Platform-as-Code 的设计，基于 KubeVela 的应用平台天然对用户是自助式的使用方式，如图 3 所示。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/3c911036a45862d50308ef1c69ab13dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/3c911036a45862d50308ef1c69ab13dc.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 3 - KubeVela 自助式能力交付流程图<br>
<br>具体来说，平台团队只需要极小的人力成本就可以在系统中维护大量的、代码化的“能力模板”。而作为平台的终端用户，业务团队只需要根据自己的应用部署需求在 PaaS UI 上选择几个能力模板，填入参数，就可以自助式的完成一次交付，无论这个应用多么复杂，业务用户的学习成本都非常低，并且默认就会遵循模板中所定义的规范；而这个应用的部署和运维过程，则由 Kubernetes 以自动化的方式去管理，从而减轻了业务用户大量的心智负担。<br>
<br>而更为重要的是，这种机制的存在，让运维人员再次成为了平台团队中的核心角色。具体的说，他们通过 CUE 或者 Helm 设计和编写能力模板，然后把这些模版安装到 KubeVela 系统中给业务团队使用。大家试想一下，<strong>这个过程，其实就是运维人员把业务对平台的诉求，结合整个平台的最佳实践，以代码化的方式固化成可被复用和定制的能力模块的过程</strong>。而且这个过程中，运维并不需要去进行复杂的 K8s 定制和开发，只需要理解 k8s 的核心概念即可。另一方面，这些代码化的能力模块，复用性极高，变更和上线非常容易，并且大多数情况下不需要额外的研发成本，可以说是最敏捷的“云原生”运维实践，能够真正让业务感受到云原生“研发、交付、运维高效一体化”的核心价值。<br>
<br><h2>4. 多环境多集群、多版本应用交付</h2>KubeVela v1.0 的另一个重大更新，就是改进了系统的部署结构，提供了 Control Plane （控制平面）模式，从而具备了面向多环境、多集群进行版本化应用交付的能力。所以现在，一个典型的生产环境 KubeVela 部署形态如下图 4 所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210413/fd895b783688a7cb0e56f18caa65a050.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210413/fd895b783688a7cb0e56f18caa65a050.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 4 - KubeVela 控制平面部署形态示意图<br>
<br>在这个场景下，KubeVela 支持为多环境应用进行描述，支持为应用配置 Placement 策略以及应用多版本同时部署在线、并通过 Istio 进行灰度的发布模型。大家可以通过<a href="https://kubevela.io/docs/rollout/appdeploy">这个文档</a>进行深入了解。<br>
<br>在 v1.0 发布之后，KubeVela 会围绕上述架构进行持续的演进，其中的一个主要的工作项就是将 KubeVela Dashboard、CLI 和 Appfile 全部迁移和升级到同 KubeVela 控制平面通过 gRPC 进行交互，而不是像之前的版本那样需要直接跟目标集群打交道。这部分工作目前尚在进行中，欢迎对构建下一代“可编程式”开发者体验有心得的同学一起来参与。与此同时，欧洲知名科技出版商 Springer Nature 也正在一起参与这部分工作以便从 CloudFoundry 上平滑迁移到 KubeVela。<br>
<br><h1>结语</h1>如果我们总结一下 KubeVela 今天的设计与能力，其实不难发现它是今天云原生应用平台发展的一条必然路径：<br>
<ol><li>完全基于 Kubernetes 构建，天然的被集成能力和普适性，天然透出 Kubernetes 及其生态的所有能力而不是叠加抽象；</li><li>基于 X-as-Code 的平台能力模块化，配合 OAM 模型实现超低成本的能力封装、抽象和组装机制，快速敏捷的响应用户需求，提供全自助、无锁定的应用管理与交付体验；</li><li>基于 Kubernetes 控制器模式进行组件解封装和应用部署，确保最终一致性、确保应用交付与运维流程的健壮性；</li><li>内置以应用为单位的发布策略和面向多环境、多集群交付策略，极大地补充了社区目前以单一工作负载为中心的发布能力；</li><li>无论应用部署多么复杂，只需要 1-2 个 Kubernetes YAML 文件就能做完整的描述，天然适合并且大大简化 GitOps 工作流，极大程度降低了终端用户使用云原生和 Kubernetes 的上手成本，并且不带来任何能力或者抽象锁定。</li></ol><br>
<br>更重要的是，KubeVela 以 Platform-as-Code 的设计思想，给未来基于云原生的应用平台团队提出了更加合理的组织方式：<br>
<ol><li>平台 SRE 负责 Kubernetes 集群和组件的健壮性；</li><li>平台研发工程师负责开发 CRD Controller，同 Kubernetes 内置能力一起对应用层提供完整的应用管理、运维和基础设施能力；</li><li>业务运维结合业务诉求，负责将最佳实践代码化为 CUE 或者 Helm 模板，将平台的能力模块化；</li><li>业务用户以完全自助化的方式使用平台的模块化能力来进行应用管理与交付，心智负担低，部署效率高。</li></ol><br>
<br>而基于这套体系，KubeVela 应用平台还可以用来实现强大的“无差别”应用交付场景，达成完全与环境无关的云端应用交付体验：<br>
<ol><li>组件提供方将应用交付所需的能力（工作负载、运维行为、云服务）定义为 Helm 包或者 CUE 包，注册到 KubeVela 系统当中；</li><li>应用交付人员使用 KubeVela 组装上述模块化能力成为一个完全与基础设施无关的应用部署描述，同时可以借助 KubeVela 的 Patch 等能力定制和覆盖组件提供方的配置，或者定义复杂的部署拓扑；</li><li>通过多环境、多集群交付模型定义应用在不同环境中的部署形态和交付策略，配置不同版本应用实例的流量分配策略。</li></ol><br>
<br>KubeVela v1.0 的发布是我们基于 OAM 模型以及云原生应用交付使用场景最大化验证的结果，它不仅代表了稳定的API，还代表了成熟的使用范式。然而这不代表结束，而是一个全新的开始，它开启了一个“可编程式”应用平台的未来，这是一个能够充分释放云原生潜力、让最终用户和软件交付方从第一天开始就充分享受云原生技术魅力的有效路径。我们期待这个项目能达成它最朴素的愿景：Make shipping applications more enjoyable!<br>
<br><h1>了解更多</h1>您可以通过如下材料了解更多关于 KubeVela 以及 OAM 项目的细节：<br>
<ol><li>项目代码库：_<a href="https://github.com/oam-dev/kubevela/_" rel="nofollow" target="_blank">https://github.com/oam-dev/kubevela/_</a>，欢迎 Star/Watch/Fork！</li><li>项目官方主页与文档：_<a href="https://kubevela.io/_" rel="nofollow" target="_blank">https://kubevela.io/_</a>，同时欢迎参加由“云原生社区”组织的 KubeVela 文档中文本地化翻译工作！</li><li>项目钉钉群：23310022；Slack：CNCF #kubevela Channel。</li></ol>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            