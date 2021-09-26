
---
title: 'Kubernetes必备工具2021版'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/79e16e11fd3991f927a1bdfa709d9492.png'
author: Dockone
comments: false
date: 2021-09-26 01:53:11
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/79e16e11fd3991f927a1bdfa709d9492.png'
---

<div>   
<br><h3>简介</h3>本文尝试归纳一下最新和比较少见的Kubernetes生态工具，也是作者很喜欢和具备潜力的Kubernetes工具清单。由于所罗列的工具是基于个人的经验，所以为避免偏见和误导，本文为每个工具提供了替代方案，让读者可以根据自己的需求进行比选。<br>
<br>作者撰写本文的目标是描述用于不同软件开发任务的生态工具，回答如何在Kubernetes环境中完成某个任务的问题。<br>
<h3>K3D</h3><a href="https://k3d.io/">K3D</a>是作者在笔记本电脑上运行Kubernetes集群的最优选方式。它使用Docker部署<a href="https://k3s.io/">K3S</a>包，非常轻量级和快速。运行只需要Docker环境，资源消耗非常低，唯一不足就是不完全兼容Kubernetes，但对于本地开发而言，基本不是问题。如果是用于测试环境，建议使用Kind等其他的解决方案。Kind完全兼容Kubernetes , 但运行速度不及K3D。<br>
<br>替代方案：<br>
<ul><li>IoT K3S或边缘<a href="https://k3s.io/">K3S</a></li><li>全兼容Kubernetes的<a href="https://kind.sigs.k8s.io/">Kind</a></li><li><a href="https://microk8s.io/">MicroK8S</a></li><li><a href="https://minikube.sigs.k8s.io/docs/">MiniKube</a></li></ul><br>
<br><h3>Krew</h3><a href="https://krew.sigs.k8s.io/">Krew</a>是管理Kubectl插件的重要工具，可能是所有Kubernetes用户的必用工具。Krew支持管理145个以上的<a href="https://krew.sigs.k8s.io/plugins/">生态插件</a>，常见的应用是安装和管理<a href="https://github.com/ahmetb/kubectx">kubens</a>和<a href="https://github.com/ahmetb/kubectx">kubectx</a>插件。<br>
<h3>Lens</h3><a href="https://k8slens.dev/">Lens</a>是面向Kubernetes的SRE工程师，Ops工程师和软件开发人员的集成开发环境。可以适用于所有的Kubernetes发行版，包括物理部署和云端部署的环境。Lens具备快速，易用和实时可观察性的特性。能够轻易地管理多个集群，是多集群运维人员的必须工具。<br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/79e16e11fd3991f927a1bdfa709d9492.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/79e16e11fd3991f927a1bdfa709d9492.png" class="img-polaroid" title="图片_2.png" alt="图片_2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
替代方案：<br>
<br>对于偏爱轻量级终端的人来说，<a href="https://k9scli.io/">K9s</a>是很好的选择，提供Kubernetes变化的持续监视功能，并提供与观察资源对象进行交互的操作指令。<br>
<h3>Helm</h3>无须多言，<a href="https://helm.sh/">Helm</a>是Kubernetes最著名的包管理器，提供等同于使用编程语言的效果，Helm支持将应用打包到Charts中，从而实现将复杂的应用程序抽象为可重用的简单组件，易于定义、安装和更新。Helm非常成熟、易于使用，提供强大的模板引擎，内置大量的预定义Charts、以及具备有力的技术支持服务。<br>
<br>替代方案：<br>
<br><a href="https://kustomize.io/">Kustomize</a>是一个新兴和潜力的Helm替代工具，它不使用模板引擎，而是在用户基础定义之上，构建一个叠加的引擎，实现与模板引擎相同的功能。<br>
<h3>ArgoCD</h3>我认为<a href="https://www.gitops.tech/">GitOps</a>是过去十年中的最佳创意之一。在软件开发中，我们需要使用单一的可信源来跟踪构建软件所需的所有动态组件，而Git是解决这个需求的完美工具。其想法是提供一个Git库，存储内容包含了应用程序代码和所需生产环境状态的基础设施（IaC）声明性描述，以及使环境匹配到要求状态的自动化过程。<br>
<br><blockquote><br>GitOps：基于声明式基础设施的版本化CI/CD。弃用脚本，开启交付。——<a href="https://twitter.com/kelseyhightower/status/953638870888849408">Kelsey Hightower</a></blockquote>尽管可以使用<a href="https://www.terraform.io/">Terraform</a>或类似的工具实现基础设施即代码（<a href="https://en.wikipedia.org/wiki/Infrastructure_as_code">IaC</a>）。但还不能够在生产Git中，实现所期望的状态同步。需要一种方法持续监控环境，并确保不会出现配置漂移。使用Terraform工具时，用户须编写脚本来运行生产环境的状态检查，并检查是否与Terraform的配置状态相匹配，但这种方式乏味，且难以维护的。<br>
<br>Kubernetes是基于全过程控制环的思想构建，意味着Kubernetes能够全天候监视集群的状态，以确保它处于预期的状态。例如，Kubernetes实际运行的副本数就等于配置的副本数量。GitOps思路还将这种模式延伸到应用程序，实现支持用户将服务定义为代码。例如，通过定义Helm Charts，并使用某个工具利用Kubernetes的功能来监控应用程序的状态，并相应地调整集群状态。换句话说，如果更新了代码库或Helm Chart，生产集群也能够相应地自动更新，做到真正的持续部署。<br>
<br>应用部署和应用全生命周期管理的核心原则就应该是自动化、可审计和易于理解。笔者认为这是个具备变革性的想法，如果实现得当，将会使企业更多地关注业务功能，较少地考虑自动化脚本编写，这个概念还可以延伸到软件开发的其他领域，例如，你可以在代码中包含开发文档，实现文档的历史变更跟踪和文档及时更新，或者使用<a href="https://github.com/jamesmh/architecture_decision_record">ADRs</a>来跟踪架构决策。<br>
<br>在笔者看来，Kubernetes中最好的GitOps工具是ArgoCD，他是Argo生态的一部分（Argo生态还包括其他的优秀工具，稍后还将讨论提及）。ArgoCD功能支持用户在代码库中存储每一种环境，并为上述每个环境定义所有的配置，能够在特定的目标环境内，自动部署所需的应用程序状态。ArgoCD 技术架构如下图所示：<br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/3664b6a141bb7048dcc9d19f8d45636f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/3664b6a141bb7048dcc9d19f8d45636f.png" class="img-polaroid" title="图片_3.png" alt="图片_3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
ArgoCD的运行实现类似于Kubernetes控制器，它持续监控正在运行的应用程序，并执行实时状态与期望状态的对比（配置存储在Git库）。Argo CD提供状态差异的报告和可视化展示，并支持自动或手动将应用状态同步为预期状态。<br>
<br>替代方案：<br>
<br><a href="https://fluxcd.io/">Flux</a>最新发布的版本有很多的改进，提供了非常相似的功能。<br>
<h3>Argo WorkMows和Argo Events</h3>Kubernetes环境存在批处理作业或复杂工作流程的运行需要，应用场景可能是数据管道、异步进程或CI/CD的部分或全部。除此之外，可能还需要运行基于事件驱动的微服务，来响应某些事件。例如文件上传或向消息队列发送消息等。对于上述需求，可以采用<a href="https://argoproj.github.io/argo-workflows/">Argo WorkMows</a>和<a href="https://argoproj.github.io/argo-events/">Argo Events</a>工具。尽管是两个独立的项目，但实际使用中，经常成对部署应用。<br>
<br>Argo WorkMows是类似于Apache AirFlow的编排引擎，是Kubernetes的原生引擎工具。它使用自定义的CRD，采用分步配置或原生YAML的<a href="https://en.wikipedia.org/wiki/Directed_acyclic_graph">DAGs</a>来定义复杂的WorkMows。它提供了友好的用户界面、重试机制、计划性作业、输入和输出跟踪等功能，支撑用户编排数据管道、批处理作业等。<br>
<br>用户有时可能想将自有的应用管道与Kafka流引擎、消息队列、webhook或者深度存储服务等异步服务整合应用。例如对S3文件上传事件作出反应。为此可以使用Argo Events。<br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/04645d2051d6fc1d499c0dbf49fc3c39.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/04645d2051d6fc1d499c0dbf49fc3c39.png" class="img-polaroid" title="图片_4.png" alt="图片_4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上述两种工具的结合为用户CI/CD在内的所有管道需求，提供了一个简单而强大的解决方案，允许用户在Kubernetes环境中原生地运行CI/CD管道。<br>
<br>替代方案：<br>
<ul><li><a href="https://www.kubeflow.org/">KubeMow</a>，适用于ML目的的管道  </li><li><a href="https://tekton.dev/docs/pipelines/pipelines/">Tekton</a>，适用于CI/CD管道</li></ul><br>
<br><h3>Kaniko</h3>前面提到如何使用Argo WorkMows在Kubernetes环境中运行原生的CI/CD管道，其中一个常见任务是构建Docker镜像，这在Kubernetes中的构建过程实际上就是使用宿主机的Docker引擎运行容器镜像本身，过程非常乏味。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/0c97bdd28ec463f0fb9afa2a7b5921c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/0c97bdd28ec463f0fb9afa2a7b5921c7.png" class="img-polaroid" title="图片_5.png" alt="图片_5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
使用<a href="https://github.com/GoogleContainerTools/kaniko">Kaniko</a>的基本原则是用户必须使用Kaniko，而不是Docker构建镜像。Kaniko不依赖于Docker守护进程，完全是在用户空间根据Dockerfile的内容逐行执行命令来构建镜像。这就使得在一些无法安全，快速获取Docker进程环境下（例如标准的Kubernetes Cluster）也能够构建容器镜像。同时，Kaniko消除了在Kubernetes集群中构建镜像的所有问题。<br>
<h3>Istio</h3><a href="https://istio.io/">Istio</a>是市面上最著名和受欢迎的开源服务网格工具。无需细说服务网格的概念（这个话题很大）。如果用户正在准备构建或正在构建微服务，且需要一个服务网格来管理服务通讯、服务可观察性,错误处理,安全控制、以及微服务架构跨平面通信等功能。可以采用服务网格避免逻辑重复导致单个微服务的代码污染。Istio的技术架构如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/709d2d090f499f6dcb63d042fb69c78f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/709d2d090f499f6dcb63d042fb69c78f.png" class="img-polaroid" title="图片_6.png" alt="图片_6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
简而言之，服务网格是一个可以添加到应用程序中的专用基础设施层。它允许用户在无需编写代码的情况下，可以透明地添加可观察性、流量管理和安全性等功能。对于具备熟练运行Istio和使用Istio运行微服务的用户，Kubernetes已经多次被证明是最佳的运行平台。Istio还可以将Kubernetes集群扩展到VM等其他服务环境，为用户构建混合环境，有利于用户将应用迁移到Kubernetes。<br>
<br>替代方案：<br>
<ul><li><a href="https://linkerd.io/">Linkerd</a>是一种更轻或更快的服务网格。Linkerd的初衷就是为了安全而研发，提供包括默认启动mTLS、采用Rust构建数据平面、采用内存安全语言以及定期安全审计等功能。</li><li><a href="https://www.consul.io/">Consul</a>是为任何运行时和云服务商构建的服务网格，非常适合跨Kubernetes和公有云的混合部署。非常适合不是纯Kubernetes负荷运行的组织。</li></ul><br>
<br><h3>Argo Rollouts</h3>如前文所述，在Kubernetes环境中，我们可以使用Argo WorkMows或类似工具来运行CI/CD管道，使用Kaniko来构建容器镜像。下面的逻辑步骤是继续进行持续部署。接下来的步骤在现实场景下风险高而极具挑战性。这也是大多数公司止步于持续交付的主要原因，同时也意味着这些公司具有自动化，手工审批和手工校验的过程步骤，导致现状的原因主要是团队还不完全信任他们的自动化。<br>
<br>那么如何建立必要的信任，从而摆脱所有的手工脚本，实现从源代码到生产部署的完全自动化呢？答案是：可观察性。需要投入更多的资源集中在指标观测上，并收集能够准确表示应用状态的所有数据，达到通过一系列指标来建立信任的目的。假设在Prometheus中拥有所有的指标数据，那么就可以基于这些指标数据开展应用程序的逐步自动化推出，实现应用程序的自动化部署。<br>
<br>简而言之， Kubernetes提供了开箱即用的滚动更新（Rolling Updates）技术，如果需要比这个更高级的部署技术，就需要使用金丝雀部署逐步交付，即逐步将流量切换到新版本的应用，然后采集指标数据并分析，与预定义的规则进行匹配，如果一切都正常的话，就可以切换更多的流量，如果有任何问题就回滚部署。<br>
<br><blockquote><br>在Kubernetes中，Argo Rollouts提供了金丝雀部署和更多的其他功能。内置了Kubernetes控制器和一组CRD，提供Kubernetes渐进式交付的蓝绿部署、金丝雀部署、金丝雀分析、部署实验等高级部署功能。</blockquote>虽然像Istio这样的服务网格也提供金丝雀发布功能，但是Argo rollout是专门为此目的而构建的，发布过程更加简化，并以开发人员为中心。最重要的是Argo Rollouts可以与任何服务网格集成。所提供的功能包括：<br>
<ul><li>蓝绿更新策略 </li><li>金丝雀更新策略 </li><li>细粒度与加权的轨迹切换 </li><li>自动更新与回滚、或人工判断执行 </li><li>自定义指标查询和业务KPI分析</li><li>入口控制器支持集成NGINX，ALB等 </li><li>服务网格支持集成Istio，Linkerd，SMI等</li><li>量化指标来源集成包括Prometheus，Wavefront，Kayenta，Web，Kubernetes Jobs等</li></ul><br>
<br>替代方案：<br>
<ul><li>Istio是具备金丝雀发布功能的服务网格工具，而不仅仅是一个过程交付工具。Istio不支持自动部署，但可以通过与Argo rollout集成来实现。 </li><li><a href="https://flagger.app/">Flagger</a>与Argo Rollouts非常相似，与Flux集成效果非常好，所以如果使用<a href="https://fluxcd.io/">Flux</a>，建议考虑Flagger。</li><li><a href="https://spinnaker.io/">Spinnaker</a>是首个Kubernetes持续交付工具，具备丰富的功能，但使用和配置比较复杂。</li></ul><br>
<br><h3>Crossplane</h3><a href="https://crossplane.io/">Crossplane</a>是笔者最喜欢和关注的Kubernetes生态项目，它实现了将第三方服务当作Kubernetes资源来管理，为Kubernetes补全了关键的一块能力。这意味着用户可以在Kubernetes内使用YAML定义公有云数据库，如AWS RDS或GCP cloud SQL等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/fbe3a924453ae680ad7fd1d7cbb18fdd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/fbe3a924453ae680ad7fd1d7cbb18fdd.png" class="img-polaroid" title="图片_7.png" alt="图片_7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过Crossplane工具，用户就不需要使用不同的工具和方法学来隔离基础设施和代码，可以将任意外部服务定义为Kubernetes的资源，且不需要再刻意学习使用和单独部署<a href="https://www.terraform.io/">Terraform</a>等工具。<br>
<br><blockquote><br>Crossplane是一个开源的Kubernetes插件，它允许平台团队封装来自多个供应商的基础设施，并向应用团队开放更高级别的自服务API，而无需编写任何代码。</blockquote>Crossplane扩展了Kubernetes集群的功能，提供管理任意基础设施或云服务的CDR。此外，与Terraform等其他工具相反，Crossplane使用现有Kubernetes的控制环等已有功能来持续监视集群，并自动检测运行时的配置漂移，从而实现完整的持续部署。例如，如果用户定义了一个托管数据库实例，但被其他用户手动更改了配置，Crossplane将自动检测该事件并将执行配置回滚操作。这个过程也巩固了基础设施即代码和GitOps的原则。<br>
<br>Crossplane与Argo CD集成非常好，即可以监控源代码，又确保代码库的唯一可信，代码中的任何变更都将同步到集群和外部云服务。没有Crossplane，用户只能在Kubernetes中部署GitOps，而不能跨Kubernetes和公有云共享使用。<br>
<br>替代方案：<br>
<ul><li>Terraform是最著名的IaC工具，但它不是Kubernetes生态的原生工具，对用户有额外的技能要求，且不具备配置漂移的自动监控功能。</li><li><a href="https://www.pulumi.com/">Pulumi</a>是Terraform的一个替代方案，运行的编程语言可以被开发人员测试和理解。</li></ul><br>
<br><h3>Knative</h3>如果用户在公有云开发应用程序，可能使用了某些无服务器计算技术，比如事件驱动范式FaaS的<a href="https://aws.amazon.com/lambda/">AWS Lambda</a>等。以往我们已经讨论过无服务器计算，所以此处不再赘述概念。但使用无服务器计算的问题在于它与公有云是紧密耦合的，因为公有云可以因此构建一个事件驱动应用的巨大的生态。<br>
<br>对于Kubernetes而言，如果用户希望使用事件驱动架构运行函数即代码应用，那么Knative将是在最佳选择。Knative设计是在Pod之上创建一个抽象层，实现在Kubernetes中运行无服务器函数。它的主要功能包括：<br>
<ul><li>为通用应用用例提供更高层次的抽象API </li><li>提供可扩展、安全、无状态的秒级函数服务 </li><li>采用功能松耦合架构，支持按需使用</li><li>具备组件可插拔，支持用户使用外部日志和监控，网络，和服务网格工具</li><li>具备组件可移植，能够在任意Kubernetes环境中运行，无需担心厂商锁定</li><li>继承通用开发理念，支持GitOps，DockerOps，ManualOps等通用模式</li><li>兼容Django、Ruby on Rails、Spring等通用开发工具和框架</li></ul><br>
<br>替代方案：<br>
<ul><li><a href="https://argoproj.github.io/argo-events/">Argo Events</a>为Kubernetes提供了一个事件驱动的工作流引擎，支持与AWS Lambda等云引擎集成。虽然不是FaaS，但为Kubernetes提供了一个事件驱动架构</li><li><a href="https://www.openfaas.com/">OpenFaas</a></li></ul><br>
<br><h3>Kyverno</h3>Kubernetes为敏捷自治团队提供了强大的灵活性。但权力越大，责任越大，Kubernetes必须有一系列的最佳实践和规则，以确保以始终一致和高度内聚的方式部署和管理工作负载，并确保这种方式符合公司的策略和安全规范。<br>
<br>在Kyverno出现之前，虽然有一些工具可以实现上述要求，但都不是Kubernetes的原生工具。Kyverno是为Kubernetes生态而设计的策略引擎，策略被定义为Kubernetes的一种资源，不需要新的语言来编写策略。Kyverno具备对策略进行验证、演化和生成Kubernetes资源的功能。<br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/c6f18adfc0c5a6f4d0141312b968b8c2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/c6f18adfc0c5a6f4d0141312b968b8c2.png" class="img-polaroid" title="图片_8.png" alt="图片_8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kyverno策略是一组规则。每个规则由一个match子句、一个可选的exclude子句和一个validate、mutate或generate子句组成。规则定义只能包含单个validate、mutation或generate子节点。<br>
<br>用户可以使用与最佳实践、网络或安全等相关的任何类型策略。例如，强制要求所有服务都具有标签，或者所有容器都必须为非根运行。用户可以查看策略用例，并将策略应用于整个集群或指定的命名空间，还可以选择是否审计策略或强制阻止用户部署资源等。<br>
<br>替代方案：<br>
<br><a href="https://www.openpolicyagent.org/">Open Policy Agent</a>是一种著名的云原生策略控制引擎。采用自有的声明性语言，并可以应用于许多环境，而不仅仅是在Kubernetes。功能比Kyverno更强大，但管理难度也更大。<br>
<h3>Kubevela</h3>使用Kubernetes的一个问题是开发人员需要非常清楚地了解平台和集群的配置。许多用户可能会认为Kubernetes的抽象级别太低，以至于给专注于编写和发布应用的开发人员，带来了很多工作协同的摩擦。<br>
<br>开放应用程序模型（OAM）就是解决这个问题而生的，其设计思想是屏蔽底层运行时，为应用程序创建更高级的抽象。<br>
<br><blockquote><br>相对于容器或容器编排，开放应用模型（OAM）专注于应用程序，为应用部署带来了模块化、可扩展和可移植的设计，并提供更高级别的API。</blockquote><a href="https://kubevela.io/">Kubevela</a>是OAM模型的一种功能实现。核心理念是以应用为中心，对运行时没有要求，具备原生可扩展性。在Kubevela中，应用被定义为Kubernetes的一种资源，具备最高的部署优先权。应用部署对于集群操作员（平台团队）和开发人员（应用团队）存在不同的内涵，集群操作员是通过定义组件（类似于helm chart的可部署/可定义的实体）和特性来管理集群和不同的环境；开发人员是通过组装组件和特性来定义应用程序。<br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/a6f048d0f347ae8f0fa01b9f35cfa16b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/a6f048d0f347ae8f0fa01b9f35cfa16b.png" class="img-polaroid" title="图片_9.png" alt="图片_9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>平台团队：将平台能力当作组件或特性，与目标环境规范一起进行建模和管理。</li><li>应用团队：选定一个环境，根据需求组装应用的组件和特性，并将其部署到目标环境中。</li></ul><br>
<br>KubeVela是云原生计算基金会的沙盒项目，目前处于起步阶段，但在不久的将来，很可能改变我们使用Kubernetes的方式，可以让开发人员专注于应用开发，而不必是Kubernetes专家。然而，对于OAM在现实世界中的适用性，也确实存在一些隐忧，对于像系统软件、ML或大数据处理等服务，存在很大程度的底层细节依赖，而这些细节可能很难纳入到OAM模型。 <br>
<br>替代方案：<br>
<ul><li><a href="https://www.shipa.io/getting-started/">Shipa</a>采用了类似的方法，使平台和开发团队能够协同工作，实现将应用轻松地部署到Kubernetes环境。</li><li><a href="https://learn.theketch.io/docs">Ketch</a>还尝试通过使用非常简单的命令行界面来部署应用程序来简化开发人员的生活。问题是它不遵循GitOps原则，而是使用命令式方法，这虽然更容易上手，但对于更大的项目来说更复杂。笔者推荐Ketch用于简单的应用程序或小型团队，但不推荐用于大型项目。</li></ul><br>
<br><h3>Snyk</h3>安全在任何软件开发过程中，都是非常重要的方面。由于迁移应用到Kubernetes的用户单位难以在Kubernetes环境部署已有的安全原则，使得安全成为Kubernetes的一大痛点。<a href="https://snyk.io/">Snyk</a>是可以与Kubernetes轻易集成的安全框架，能够检测容器镜像、代码、开源项目等组件的漏洞。从而试图缓解Kubernetes的安全问题，<br>
<br>替代方案：<br>
<br><a href="https://falco.org/">Falco</a>是Kubernetes环境中的运行时安全线程检测工具。 <br>
<h3>Velero</h3>如果在Kubernetes中运行工作负载，并使用存储卷来存储数据，则需要创建和管理数据备份。Velero提供了简单的备份/恢复流程、容灾恢复机制和数据迁移等功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/c442d4d21e8d54fa85fbcf9b98bd200d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/c442d4d21e8d54fa85fbcf9b98bd200d.png" class="img-polaroid" title="图片_11.png" alt="图片_11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
与直接访问Kubernetes etcd库来执行备份和恢复的其他工具不同，Velero使用Kubernetes API来捕获集群资源的状态，并在必要时进行恢复。此外，Velero允许用户在执行软件配置的同时备份和恢复应用程序的持久数据。<br>
<h3>Schema Hero</h3>软件开发中的另一个常见过程是在使用关系数据库时管理Schema的演化。<a href="https://schemahero.io/">Schema Hero</a>是一个开源的数据库Schema迁移工具，它能够将Schema定义转换为可以应用于任何环境的迁移脚本。它使用Kubernetes声明性特性来管理数据库Schema迁移。用户只需指定所需的状态，余下的工作都可以交由Schema Hero管理。<br>
<br>替代方案：<br>
<br><a href="https://www.liquibase.org/">LiquidBase</a>是最著名的替代方案，功能强大，但不是Kubernetes的原生工具，且操作困难。 <br>
<h3>Bitnami Sealed Secrets</h3>我们已经介绍了包括ArgoCD在内的多款GitOps工具。这些工具的设计目标都是设计将所有内容保存在Git库中，并能够使用原生的Kubernetes声明来保持与环境的同步。如前所述，ArgoCD工具保证了Git中源代码的可靠性，并提供自动化进程来处理配置变更。<br>
<br>但是在Git中存储如数据库密码或API密钥之类的密钥，通常都非常困难。因为用户不应该在代码库中包含秘钥信息。一种常见的解决方案是使用外部保险库（如AWS Secret Manager或HashiCorp）来存储密钥，但这种解决方案会带来额外独立线程处理密钥的不便需求。理想情况下，应该有一种方式可以在Git中安全地存储密钥，就像管理其他类型的任何资源一样。<br>
Sealed Secrets就是解决这个问题的工具，它提供强加密能力，允许用户将敏感数据存储在Git中。Bitnami Sealed Secrets原生集成在Kubernetes中，允许用户只能通过Kubernetes中运行的控制器来解密密钥。控制器将解密数据并创建安全存储的原生Kubernetes密钥。这使得用户能够以代码的方式存储任意内容，并允许无需外部依赖就可以安全地执行持续部署。<br>
<br>Sealed Secrets由两部分组成：客户侧控制器和客户侧应用Kubeseal。采用非对称加密来加密密钥，并且只有控制器可以解密。而加密的密钥被封装成Kubernetes资源，可以将其存储在Git中。<br>
<br>替代方案：<br>
<ul><li><a href="https://github.com/mozilla/sops">SOPS</a>是相对简单的密钥管理工具</li><li><a href="https://aws.amazon.com/secrets-manager/">AWS Secret Manager</a></li><li><a href="https://www.vaultproject.io/">Vault</a></li></ul><br>
<br><h3>Capsule</h3>许多公司使用多租户来管理不同的客户，这在软件开发设计中很常见，但在Kubernetes中却很难实现。命名空间是利用逻辑分区创建集群内独立分片的一种好方法，但还不足以安全地隔离用户。还需要强制网络策略、配额等功能。用户可以为每个命名空间创建网络策略和规则，但过程冗长且难以扩展。此外，租户有一个关键限制即不能跨越命名空间使用。<br>
<br>创建分层继承名称空间就是为了克服上述部分问题。其设计思路是为每个租户构建一个父命名空间，提供通用的网络策略和配额，并允许在此基础上创建子命名空间。这是一个巨大的改进，但在租户安全性和治理方面没有原生的技术支持，功能还没有达到生产状态，预计1.0版本有望在下个月发布。<br>
<br>目前解决这个问题的另一种常用方法是为每个客户创建一个集群，这既保证了安全，又为租户提供了所需的一切，但带来了管理困难和高成本。<br>
<a href="https://github.com/clastix/capsule">Capsule</a>是原生支持Kubernetes单集群多个租户管理的工具。通过使用Capsule，用户可以将所有租户创建在同一个集群。Capsule为租户提供近似乎原生的体验（仅有一些较小的限制），通过隐藏集群共享的底层特征，让租户能够在单集群内创建多个命名空间并完整地使用集群资源。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/d51076fc07e09dbac56a080c8ddd560f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/d51076fc07e09dbac56a080c8ddd560f.png" class="img-polaroid" title="图片_12.png" alt="图片_12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在单个集群中，Capsule控制器在一个轻量级Kubernetes抽象（租户）中聚合了多个Namespaces，即一组Kubernetes Namespaces。在每个租户中，用户可以自由创建自己的Namespaces，并共享所分配的资源，由策略引擎保证不同租户之间的隔离。<br>
<br>类似于“分级Namespaces”的运作机制，租户级的“网络与安全策略”、“资源配额”、“限制范围”、“RBAC”等策略定义，会自动被租户内的所有命名空间继承。这样，用户可以无需集群管理员的干预，自由地管理所属的租户。由于Capsule的声明性，以及所有的配置都存储在Git中，因此Capsule原生具备GitOps特征。<br>
<h3>vCluster</h3><a href="https://www.vcluster.com/">VCluster</a>在多租户管理方面更加深入，它能够在Kubernetes集群中创建虚拟集群环境，每个虚拟集群运行在一个常规的命名空间內，具备完全隔离性。虚拟集群提供自有的API服务和独立的数据存储，因此在虚拟集群中创建的每个Kubernetes对象只存在于所运行的虚拟集群中。此外，用户可以像操作常规的Kubernetes集群一样，在虚拟集群中使用kube上下文指令。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/cc5c4098a1d9b797d1e94468bb1c4531.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/cc5c4098a1d9b797d1e94468bb1c4531.png" class="img-polaroid" title="图片_13.png" alt="图片_13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
类似于在单个名称空间中创建部署，用户可以创建虚拟集群，并成为集群管理员，而集群租户可以创建命名空间、安装CRD、配置权限等等。<br>
<br>建议vCluster使用k3s作为它的API服务器，使得虚拟集群具备超轻量级和高效费比能力，且由于k3s集群100%兼容Kubernetes，虚拟集群自然也是100%兼容。超级轻量级（1 Pod）的能力让用户只需要消耗很少的资源，便可在任何Kubernetes集群上运行，而不需要有访问底层集群的权限。与Capsule相比，vCluster消耗了更多一些的资源，但它提供了更多的灵活性，多租户只是其具备的用例之一。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210923/6a2de5fb7b47f09bf25b6fac9559fd26.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210923/6a2de5fb7b47f09bf25b6fac9559fd26.png" class="img-polaroid" title="图片_14.png" alt="图片_14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>其他工具</h3><ul><li><a href="https://kubeapps.com/">KubeApps</a>是一个基于Web的UI，用于在Kubernetes集群中部署和管理应用程序。它提供了一个很好的UI，你可以在其中浏览和安装公共或私有应用程序（Helm 图表）。</li><li><a href="https://kubesphere.io/">KubeSphere</a>是一个巨大的项目，它提供了许多功能。它有一个漂亮的UI，并允许你管理Kubernetes集群、用户和应用程序。它还有一个像KubeApps那样的App Store。它有很多集成，笔者可以就此单独写一篇文章，但在笔者看来，KubeSphere有一些缺点。第一个是它有点过时，它没有遵循最新的Kubernetes最佳实践，如GitOps。其次，它非常消耗资源。我建议你检查这个项目，特别是如果你更喜欢使用UI和/或你是使用更传统工具的组织的一部分。</li><li><a href="https://github.com/cloud-bulldozer/kube-burner">Kube-burner</a>用于压力测试。它提供指标监控和警报。</li><li><a href="https://github.com/litmuschaos/litmus">Litmus</a>用于混沌引擎。</li><li><a href="https://github.com/bitnami-labs/kubewatch">Kubewatch</a>用于监控，但主要聚焦于Kubernetes事件（如资源创建或删除）的消息通知推送。支持与Slack等许多工具集成。</li><li><a href="https://www.botkube.io/">Botkube</a>是一个用于监视和调试Kubernetes集群的消息机器人。类似于kubewatch，但更新并具有更多的功能。</li><li><a href="https://getmizu.io/">Mizu</a>是一个API流量的查看器和调试器。</li><li><a href="https://github.com/senthilrch/kube-fledged">Kube-medged</a>是Kubernetes的附加组件，用于在Kubernetes集群的工作节点上直接创建和管理容器镜像的缓存。因此，不需要从镜像库获取镜像，应用Pod可以即时启动。</li></ul><br>
<br><h3>结论</h3>本文回顾了笔者喜欢的Kubernetes生态工具。笔者关注能够合并到任何Kubernetes发行版中的开源项目。鉴于内容通用性考虑，本文没有涉及介绍OpenShift或云供应商Add-Ons等商业解决方案。但如果用户在公有云上运行了Kubernete环境或使用商业工具，那鼓励用户积极探索云的潜能。<br>
笔者本文的目标是向用户展示，用户在私有化部署Kubernetes环境中可以做到的事情。同时，笔者也关注了一些不太知名，具备潜力的工具，比如Crossplane、Argo Rollouts或Kubevela。尤其对vCluster、Crossplane和ArgoCD/WorkMows等工具充满兴趣。 <br>
<br><strong>原文链接：<a href="https://itnext.io/kubernetes-essential-tools-2021-def12e84c572"># Kubernetes Essential Tools: 2021</a>（翻译：易理林）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            