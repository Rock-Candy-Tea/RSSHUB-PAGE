
---
title: '为什么从第一天起就应该在 Kubernetes 上构建应用'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/2077bad11511830fa30d4f2fc96bf499.png'
author: Dockone
comments: false
date: 2021-08-29 01:50:44
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/2077bad11511830fa30d4f2fc96bf499.png'
---

<div>   
<br>如果你正在从头开发一个新的项目，诸如一个新的 APP，服务或者网站，你主要的关注点通常不是如何在高可用的网络中大规模的运行它。相反，你可能会专注于为你的目标客户打造合适的产品或寻找适合市场的产品。如果你正在为一家初创公司创建一个 MVP，你需要在大规模扩展（scaling）之前完成这个最小可用产品，否则，你在为谁扩展？如果你是企业的开发人员，你希望确保的是当前做的业务满足期望和需求。规模化运营充其量只是明天的事情。<br>
<br>因此，在选择正确的技术集时，<a href="https://stackoverflow.blog/2020/05/29/why-kubernetes-getting-so-popular/">Kubernetes</a>（通常与大型分布式系统相关）现在可能不在你的关注范围内。毕竟，它带来了很大一部分工作量：设置和操作集群、容器化你的应用程序、定义服务、部署、负载平衡器等等。这在早期看起来可能有点矫枉过正，你可能认为你的时间最好花在其他任务上，例如编写实际应用程序的前几次迭代。<br>
<br>当我们在 2008 年开始构建 Stack Overflow 时，我们没得选择。没有 Docker（2013 年），也没有 Kubernetes（2014 年）。云计算还处于起步阶段：Azure 刚刚推出（2008 年），而 Amazon Web Services 大约成立两年。我们构建的东西是为特定硬件设计的，并对其做了很多假设。现在我们正在对我们的代码库进行现代化改造并迁移到云端，我们必须投入大量工作才能使 Kubernetes 和容器正常工作。<br>
<br>经历了这个过程，我们获得一个全新的视角。如果你今天正在构建一个新应用程序，那么仔细研究一下使其成为云原生并从一开始就使用 Kubernetes 可能是值得的。设置 Kubernetes 的工作量比你想象的要少。同时，它也比以后重构你的应用程序来支持容器化所需的工作量少。<br>
<br>以下有三个原因说明为什么从一开始就在 Kubernetes 上构建你的应用程序不一定是一个坏主意。<br>
<h3>托管的 Kubernetes 完成了繁重的工作</h3>几年前，当我们在 Stack Overflow 建立我们的第一个内部 Kubernetes 集群时，我们花了将近一周的时间才能启动并运行所有内容：配置虚拟机、安装、配置、配置、配置。 一旦集群启动，后面就是持续的维护工作。这个过程对我们最大的触动是 Kubernetes 对我们来说太棒了——但我们希望其他人也能来使用它。<br>
<br>如今，Amazon 的 Elastic Kubernetes Service（EKS）、Microsoft 的 Azure Kubernetes Service（AKS）或 Google 的 Google Kubernetes Engine（GKE）等托管 Kubernetes 服务允许你在几分钟内设置自己的集群。例如，在 AKS 中，你只需单击门户中的几个按钮并填写几个表单：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/2077bad11511830fa30d4f2fc96bf499.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/2077bad11511830fa30d4f2fc96bf499.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这很方便，但你可能不想在工作流结束时创建集群这种快捷方式。先完成这个向导（wizard），但不要点击最后那个蓝色的“创建”按钮！相反，将你刚刚创建的配置下载为 <a href="https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/">ARM 模板</a>并将其纳入到你的源代码控制系统。现在你拥有两全其美的优势——易用性和基础设施即代码（IaC）！<br>
<br>一旦你在此处完成设置，那么对于规模化你的应用程序，剩下的就没有什么可做的了，除了向你的云提供商提供更多的写检查（write bigger checks）。任何额外的资源分配都很容易。规模化带来的问题——容错、负载平衡、流量整形（traffic shaping）——已经得到处理。 在任何时候，都不会出现你被成功淹没的那一刻；你无需付出太多额外工作就可以使你的应用程序面向未来。<br>
<h3>你可以保持云无关（cloud agnostic）</h3>如果你的项目成功了，那么在早期阶段做出的技术决策很可能在未来数月或数年仍会产生影响。例如，Stack Overflow 最初是用 C# 编写的。13 年后，它仍然是用 C# 编写的，但它曾经也是。偶尔有人建议我们用 Node.js 重写它。但直到现在也没有发生。<br>
<br>对云服务的依赖也是如此。你可以在基础设施即服务（IaaS）产品（如 Amazon 的 EC2）之上构建你的新应用程序。或者，你可能开始依赖平台即服务（PaaS）产品，例如 Microsoft 的 Azure SQL。但是，你是否愿意在现阶段对其背后的云提供商做出长期承诺？如果你还不知道你的旅程会带你去哪里，也许你更愿意保持云无关状态一段时间。<br>
<br>让我们回到基础设施即代码：将诸如 <a href="https://www.terraform.io/">Terraform</a> 之类的工具投入其中将帮助你在某种程度上保持与云无关。它提供了统一的工具包和配置语言（<a href="https://github.com/hashicorp/hcl">HCL</a>）来跨不同的云和基础架构提供商管理你的资源。你的应用程序不太可能真正与云无关，但是在这种情况下，你可以像切换家中的互联网或电力供应商一样轻松地切换云提供商。<br>
<br>HashiCorp 论坛中有一个关于这个主题的很好的讨论：<a href="https://discuss.hashicorp.com/t/is-terraform-really-cloud-agnostic/5980">Terraform 真的与云无关吗</a>？正如其中一位评论者指出的那样：<br>
<br><blockquote><br>“Kubernetes 集群是对计算资源进行抽象的一个很好的例子：它在不同平台上有许多托管和自我管理的实现，所有这些实现都提供了一个通用的 API 和一组通用的功能。”</blockquote>这总结得很好！它仍然不是一个完美的抽象。例如，每个云提供商可能都有自己的自定义方式来实现公共负载均衡器和 Kubernetes 中的持久卷等内容。公平地说，如果你在 Kubernetes 上构建应用，你将在一定程度上保持云无关。<br>
<h3>你可以轻松地启动新环境 - 随心所欲！</h3>Kubernetes 通常被视为管理生产基础设施的一种方式。但是在 Stack Overflow，我们一直在使用它来动态管理我们的测试环境。我们使用 Kubernetes 来托管我们所谓的 PR 环境。只需按一下按钮，每个拉取请求都可以在隔离的测试环境中运行：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/7af9f2e5248dbab55ddf78697256f16a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/7af9f2e5248dbab55ddf78697256f16a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当我们说“隔离环境”时，我们指的是一切：应用程序本身（包含 PR 分支中更改的代码）及其自己的 SQL Server、Redis、Elasticsearch 和额外的服务实例。所有这些都会在几分钟内从头开始启动，并在专用命名空间中的少数容器中运行，同时只为你和任何对你的 PR 感兴趣的人服务。<br>
<br>这不是我们发明的；其他组织一直在使用这个概念。这个想法是每个代码更改都会通过拉取请求进入像 Git 这样的版本控制系统。其他开发人员会审查代码，但代码不能说明一切。你希望看到代码的运行情况。通常，你必须在本地下载所有代码，编译并运行它。这可能很简单，但是如果你正在运行一个需要从多个仓库中提取代码的大型应用程序，或者微服务架构，那么你可能会需要几个小时的调试。<br>
<br>让我们更理想一点说，假设你已将一项新功能的所有提交（commits）压缩为一个，并将其作为单个 PR 提交。将这个 PR 环境作为一个链接发送到销售或营销部门那里，以便他们可以预览实际运行的功能。如果你的销售团队想要演示具有特定功能或自定义构建的应用程序，那么直接给他们发送 PR 环境链接。你不必花时间指导技术水平较低的同事完成构建过程。<br>
<br>达到这一点需要大量的基础工作。首先，在 Windows Containers 中运行经典的 .NET Framework 并不是我们真正想要追求的途径。理论上这是可能的——从 v1.19 开始，Kubernetes 就已经提供了 Windows 支持——但 Docker/Kubernetes 生态系统实际上更以 Linux 为中心。幸运的是，我们向 .NET Core 的迁移已经在进行中，所以我们决定押注 Linux 容器。<br>
<br>当然，这也带来了一系列挑战。当处理一个已有 10 多年历史的代码库时，你可能会发现关于它运行的基础架构的假设：硬编码文件路径（包括我们最喜欢的：正斜杠与反斜杠）、服务 URL、配置等。但我们最终完成了这个工作，现在我们可以在自动扩展的 Kubernetes 集群上启动任意数量的 Stack Overflow、Stack Exchange 网络和 Teams 产品的测试实例。<br>
<br>回顾 Stack Overflow 的早期，拥有这种工具可能就会是另一种局面。在构建产品的早期阶段，你通常希望尽可能快的构建、衡量和学习相关知识。使用容器和 Kubernetes 将允许你为此构建这样的工具，并在你需要扩展时为你提供面向未来的支持。<br>
<br>那么，你应该从一开始就使用 Kubernetes 吗？可能是！当然，这仍然取决于你的特定项目、需求和优先事项。<br>
<br>但是你是否一直在说“我们不需要 Kubernetes，因为我们还没有产品市场契合度”？仔细想想，也许你会发现自己在说“我们需要 Kubernetes，因为我们还没有适合市场的产品。”<br>
<br><strong>原文链接：<a href="https://stackoverflow.blog/2021/07/21/why-you-should-build-on-kubernetes-from-day-one/">Why you should build on Kubernetes from day one</a>（翻译：王欢）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            