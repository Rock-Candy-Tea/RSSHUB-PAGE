
---
title: 'GitOps：运用DevOps之力实现基础设施自动化'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210415213209234.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center'
author: Dockone
comments: false
date: 2021-04-17 08:08:06
thumbnail: 'https://img-blog.csdnimg.cn/20210415213209234.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center'
---

<div>   
<br>GitOps提供一种自动化基础设施管理方法，已经在众多团队中得到应用的DevOps最佳实践——包括版本控制、代码审查以及CI/CD流水线——都将被囊括于其中。目前，许多公司都在采用DevOps，看中的正是它在提高生产率和软件质量方面拥有的巨大潜力。在这一过程中，我们已经找到了自动化软件开发生命周期的方法。但是，当涉及到基础设施的设置和部署时，手动操作的比重仍然相当可观。有了GitOps，团队就可以自动化基础设施配置过程。这是由于在GitOps方法中，我们能够使用声明将基础设施编写为代码（IaC），而后像存储应用程序开发代码一样将基础设施即代码存储在Git repo当中。<br>
<br><h2>GitOps如何发挥作用？</h2>GitOps的概念最初是由Kubernetes管理公司Weaveworks所提出，因此关于GitOps的讨论主要是在Kubernetes的背景下进行的。随着整体设施转向运行在容器内的微服务架构，我们自然需要更多可行的编排平台作为支撑。事实上，基于容器的应用程序也往往拥有极为复杂且难以管理的配置体系。GitOps则通过应用在DevOps领域已经得到实际验证的技术，帮助我们简化了这一过程。如今，这一思路已经在DevOps支持者中得到广泛认可，也代表着IaC概念的升级模型。其中包含三大主要组成部分：<br>
<ul><li>基础设施即代码</li><li>Pull请求</li><li>CI/CD</li></ul><br>
<br>下面具体来看。<br>
<br><strong>基础设施即代码</strong><br>
<br>IaC是一种将基础设施以声明文件的形式进行配置和管理，并将其存储为代码的实践。通过利用IaC和版本控制，团队即可轻松优化所有的运营过程。<strong>GitOps以IaC的声明性模型为核心，同时也为Kubernetes提供了良好的施展平台。</strong>声明性意味着配置更多关注指向预期状态的声明，而不是一组具体命令。例如，在Kubernetes中，你可以在manifest中定义服务所需的Pod数量。以此为基础，系统将根据服务的运行状态自动为其提供Pod，而不再由工程师编写固定的Pod配置数量。任何符合声明式模型的云原生软件都可以被视为代码。我们使用AWS CloudFormation（一种声明性工具）来编写AWS基础设施，借此实现基础设施即代码原则。所需的状态将被声明为代码形式，系统则应用更改以自动达到这一目标状态。当然，声明式模型并不是实现GitOps的唯一途径。大家也可以使用命令式定义环境实现相同的运营效果。<br>
<br><strong>Pull请求</strong><br>
<br>GitOps概念背后的核心思路，是将版本控制系统视为单一的客观来源。我们使用Git作为应用程序代码的变更管理系统，也可以将其用于基础架构代码。所以所有的声明文件都托管在统一位置以供协作使用。在此基础之上，我们得以使用Git的关键概念——<strong>操作更改的pull请求</strong>。在应用程序开发工作流中，我们使用一个主分支作为发布分支。开发人员在主分支内创建功能分支。在开发一项特定的功能或故事之后，我们创建一个pull请求以将其合并回主分支。同样的方法也能在基础设施代码中便捷起效。通过创建pull请求，我们可以保证代码在被集成至代码库的另一个分支之前，首先经过完整的代码审查流程。代码审查可以阻止低质量代码进入测试或生产环境，这一点对于基础架构代码来说尤为重要。通过代码审查获得正式的批准，也将有助于后续的审核和故障排查工作。<br>
<br><strong>Git组织</strong><br>
<br>GitOps的部署过程至少需要两个repo：应用程序repo与环境配置repo。前者包含应用程序的源代码及其部署manifest；后者则包含了整个系统所需的状态，该状态使用声明性规范来对环境中的各项要素加以描述。你可以在代码repo中将环境描述为开发、测试和生产环境，同时包含可以在该环境的特定版本中运行的应用程序和基础设施服务。在基础设施的情况下，主分支可以表示一个环境。我们可以在功能分支中实现这些更改，而后创建一个pull请求来合并主分支中的变更。通过这种方式，我们可以在实现协作的同时，以更加透明的方式了解谁执行了哪些更改。因为所有的更改都是在Git中提交完成，因此这也有利于跟踪引发问题的根本原因。GitOps适用于任何基于Git的系统，包括GitHub、BitBucket或GitLab。其不依赖于任何特定工具或技术。<br>
<br><strong>CI/CD</strong><br>
<br>为了建立完整的GitOps实现，你还需要一条CI/CD流水线。通过使用自动化的交付流水线，每当Git存储库中发生更改时，你都可以将基础设施更改交付到指定环境当中。这条流水线将你的Git pull请求连接到业务流程系统。当你使用pull请求触发流水线时，业务流程系统将相应执行该任务。GitOps的部署策略有两种方式：push与pull流水线。二者的区别，主要体现在构建基础设施时所采取的环境部署方式之上。<br>
<br><strong>Push流水线</strong><br>
<br>许多流行的CI/CD工具都在使用这种策略。我们将应用程序的源代码及其部署manifest存储在一个repo当中。当应用程序代码中发生新的更新时，构建流水线将触发。流水线将构建容器镜像并将更改推送到环境。这种策略带来了更高的灵活性，足以支持任意类型的基础设施。当然，这种方法也有缺点，即允许CI/CD工具直接访问你的环境。<br>
<br><img src="https://img-blog.csdnimg.cn/20210415213209234.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><strong>Pull流水线</strong><br>
<br>社区普遍认为，pull流水线方法对GitOps来说是一种更为安全的实践方案。这种方法引入引入了操作符。操作符属于流水线和业务流程工具之间的组件，它会不断将环境repo中的目标状态与已部署基础设施中的实际状态进行比较。一旦检测到任何更改，则操作符会更改基础设施以适应环境repo。此外，它还可以监控镜像仓库，识别待部署的新版本镜像。正是这一切，让GitOps变得如此特别。在GitOps中，只有在环境repo中发生了更改时，才会引发环境更新。如果实现的基础设施以环境repo中未经定义的任何其他方式发生更改，系统将恢复所做的任何修改。大多数应用程序可能需要同时使用多个环境。GitOps允许您创建多个可以更改环境repo的流水线。您可以在环境repo中使用单独的分支以管理更多环境。面对分支变更，运维人员可以在响应中将此项变更部署到生产环境当中，同时将来自另一分支的其他变更部署到测试环境。<br>
<br><img src="https://img-blog.csdnimg.cn/20210415213234852.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><h2>GitOps的优势是什么？</h2><strong>DevOps最佳实践</strong><br>
<br>GitOps是一套专注于现有Git工作流、IaC、CI/CD流水线、不可变服务器、跟踪与可观察性最佳实践的模型，也代表着Kubernetes在云原生应用程序管理领域的先进的理念。因此，其技术栈与操作体验能够切实为企业用户带来诸多助益。<br>
<br><strong>持续部署——简化</strong><br>
<br>持续部署意味着更快、更频繁的部署节奏。出于多种不同考量，例如系统的有状态性、宕机弹性、上游/下游的依赖关系，以及组织内常见的其他过程与依赖项，很多朋友可能发现越来越难以建立适当的持续部署机制。GitOps不仅能够实现持续部署，同时也让大家摆脱了对大量工具方案的单独管理——这是因为所有操作都发生在版本控制系统之内。作为另一大助力，部署操作符则负责提供结构和自动化支持。这也提高了生产力并带来更快的MTTD（平均部署时间）。自动化持续部署确保团队每天可以交付30-100倍以上的更改，将平均生产效能提高2-3倍。<br>
<br>Rancher 2.5通过Rancher持续交付（Continuous Delivery）简化了部署和管理。这是一项全新的功能，通过使用Git仓库自动存储和管理应用程序和配置信息，以确保部署的一致性，大大减轻了客户的负担，从而简化跨私有云、公有云、混合云或多云环境的部署流程。<br>
<br>Rancher于2020年推出了海量集群管理项目Fleet，这个项目成为了Rancher持续交付的引擎。Fleet是一个Kubernetes集群控制器，旨在解决全球内成千上万集群的挑战。<br>
<br><strong>低MTTR（平均修复时间）</strong><br>
<br>MTTR是DevOps团队需要衡量的关键指标之一。在微服务架构中，即使是极微小的问题也可能难以修复。由于GitOps将所有更改保存在版本控制系统中，同时辅以自动化管理手段，因此有望显著缩短MTTR。你可以全面了解环境的变化进程，同时极大降低错误恢复难度。<br>
<br><strong>简化Kubernetes管理</strong><br>
<br>即使对Kubernetes不甚了解，开发人员可以使用熟悉的工具(如Git)轻松获取Kubernetes升级与功能实现。新手嵌入式开发人员能够很快跟上进度，将原本需要数月的适应期压缩到几天时间。<br>
<br><strong>改进企业整体的标准化水平</strong><br>
<br>你可以在整个企业中建立起透明的端到端工作流，这要归功GitOps提供的用于呈现应用程序、软件和Kubernetes附加组件修改的呈现框架。Git还能够全面重现你的各项操作活动。<br>
<br><h2>应用GitOps的先决条件</h2><strong>建立稳定的代码审查与测试过程</strong><br>
<br>深入检查代码更改将帮助我们准确识别某些重要操作，例如添加全局变量，借此防止低质量代码被发布到测试甚至生产环境当中。以此为基础，您可以通过pull请求提交验证过的代码，且严格禁止开发人员直接提交更改。一旦pull请求完成审查与合并，即可触发流水线。这是也维护高标准代码、进而增强系统稳定性的第一步。<br>
<br><strong>测试，测试，还是测试</strong><br>
<br>GitOps的介入意味着整个自动化水平都将提升到新的高度，这也要求我们对流水线发布的应用程序进行彻底测试。尽管GitOps能帮助我们相对轻松地完成回滚，但发布经过良好测试的高质量代码才是真正提升进程可靠性的最佳途径。<br>
<br><strong>监控为王</strong><br>
<br>GitOps能够重播操作过程，持续跟踪系统状态并加以改进，最终据此执行发布与回滚。严格的监控体系可以帮助你识别并防止配置中出现任何非预期的漂移与系统更改。因此，在开始使用GitOps之前，请检查你的监控技能并着手加强，确保其有能力处理这种变化。<br>
<br><strong>拥抱新文化</strong><br>
<br>传统的流程约束以及较长的发布时间只会拖慢业务节奏。全面拥抱DevOps文化，意味着我们应当全面利用最佳战略并帮助团队理解开发和运维行动的价值。与此同时，开发与运维团队必须联手协作，建立起整体稳定的基础设施，更快速、更顺畅地运行应用程序，进而提升系统管理效率。而DevOps文化的欠缺将严重阻碍我们享受GitOps带来的好处。<br>
<br><h2>为什么采用GitOps？</h2>GitOps是一种强大的工作流模式，可以帮助您高效治理云基础设施。GitOps可以为工程团队带来诸多优势，极大增强系统的协调能力、透明度、稳定性与持久性。<br>
<br><blockquote><br>原文链接：<a href="https://microtica.com/blog/gitops-devops-for-infrastructure-automation/" rel="nofollow" target="_blank">https://microtica.com/blog/git ... tion/</a></blockquote>文章来源：分布式实验室，点击查看原文
                                
                                                              
</div>
            