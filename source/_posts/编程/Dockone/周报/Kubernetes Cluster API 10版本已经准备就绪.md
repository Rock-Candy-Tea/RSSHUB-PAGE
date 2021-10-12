
---
title: 'Kubernetes Cluster API 1.0版本已经准备就绪'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=149'
author: Dockone
comments: false
date: 2021-10-12 03:08:25
thumbnail: 'https://picsum.photos/400/300?random=149'
---

<div>   
<br>今天（当地时间2021年10月6日），我们宣布Cluster API v1.0已经做好生产准备、并正式迎来v1beta1 API。从alpha项目的早期规划一路发展至今，Cluster API已经用越来越多的采用、更高的功能成熟度与社区中良好的创新包容度践行着项目最初做出的承诺。<br>
<br>Cluster API属于Kubernetes项目，负责为Kubernetes提供声明式管理方案，允许用户通过API轻松创建、配置及更新集群。Cluster API是一种端到端方法，能够简化Kubernetes生命周期的重复性任务，同时在统一的基础设施当中保持一致性与可重复性。<br>
<br>在立项之初，Cluster API就得到了包括VMware、微软、Weaveworks、谷歌、Mattermost、IBM、Red Hat、D2iQ、Equinix、苹果、Talos Systems、Spectro Cloud、戴姆勒TSS、爱立信、Giant Warm、AppsCode、英特尔、Twilio、New Relic以及亚马逊等众多厂商的热情贡献。<br>
<br>Cluster API的主要目标是降低集群生命周期管理工作带来的现实负担。我们的API与可扩展模型经过可靠的生产验证；随着时间推移，我们将进一步巩固基础设施并构建起抽象成果，从而简化最终用户的使用体验。<br>
<h3>Twilio – Cluster API本地裸机</h3>在Twilio，我们正在自己的SendGrid电子邮件基础设施当中以生产形式使用Cluster API。目前，我们在分布各地的数据中心裸机服务器上运行有超过100个生产Kubernets集群。<br>
<br>我们在Cluster API的整体拓扑中获得了巨大价值，并建立起集群管理的重要范式。我们将这种集群管理优势转化为专用基础设施，确保团队能够在此基础之上构建、管理并保护我们公司不断增长的Kubernetes集群与应用套件。<br>
<br>我们对Cluster API 的v1.0版本高度期待，这也标志着我们对项目的发展承诺即将迈入下一阶段。更多贡献、更多成果，就在不远处等待着Cluster API。<br>
<br>Twilio – Kris Nóva – 高级首席工程师<br>
<br>Twilio – J. Brandt Buckley – 首席工程师<br>
<h3>Giant Swarm – 云端与本地中的Cluster API</h3>在Giant Swarm，我们决定全面使用Cluster API，并配合其他上游等效选项替换我们的自定义控制器与API。我们正在将Cluster API与自己的分布式集群管理方法相集成，着手管理数百套工作负载集群，并在此过程中为上游社区贡献我们的知识与经验。<br>
<br>Cluster API的模块化架构与声明性质完全符合我们自己对于基础设施管理的原则方针与愿景，也进一步推动了Kubernetes作为核心平台的技术决策。加入社区并共同努力，让我们获得了人人参与、我为人人的集群管理探索体验，令人振奋、也非常有益。<br>
<br>我们对Cluster API的v1.0版本感到非常兴奋，我们的产品也正在为此次迭代做好准备，确保在明年年初之前为不同供应商客户提供平衡的过渡方案。<br>
<br>Giant Swarm – Puja Abbassi – 产品副总裁<br>
<h3>Spectro Cloud</h3>Cluster API是我们平台的基础开源组件之一，使我们的客户能够在任意位置大规模管理任何类型的集群。随着市场对于企业级生产环境的要求发生转变，对Kubernetes基础设施的全面管理开始成为必需。Cluster API堪称整个社区当中最重要的项目之一，也成为实现Kubernetes乃至整个开源生态系统易于访问与管理的关键所在。<br>
<br>我们对即将发布的Cluster API v1.0感到非常兴奋，也期待有更多客户及供应商加入到这个用户大家庭当中。<br>
<br>Spectro Cloud – Jun Zhou – 首席架构师<br>
<h3>Talos Systems</h3>在Talos，我们一直是Cluster API的忠实粉丝。除了我们自己，我们也有其他多位客户使用CLUSTER API在各类裸机与云环境当中配置并维护Talos集群。<br>
<br>CLUSTER API项目的模块化与总体发展愿景引导我们构建起属于自己的Talos OS提供程序，帮助将Kubernetes的声明式范式扩展到集群配置与操作系统当中。通过这种方式，我们得以在CACPI这一坚实基础之上构建起更多其他项目。拥有这样一套Talos集群处理框架，我们的产品可用性也随之大大提升。<br>
<br>我们很高兴看到此次v1.0版本的发布，也将继续以这一杰出的项目为基础努力工作！<br>
<br>Talos Systems – Spencer Smith – 高级首席软件工程师<br>
<h3>戴姆勒TSS – Cluster API本地OpenStack</h3>作为戴姆勒TSS的平台团队，我们负责在全球范围内的本地数据中心运行并运营约700套Kubernetes集群外加3500台服务器。通过迁移至Cluster API，我们逐步取代了包括Terraform、自定义原研工具及Kubernetes operators等传统配置方案。<br>
<br>在云原生思维方式的指引之下，我们希望建立起具备出色客户体验的完全托管Kubernetes集群。<br>
<br>Cluster API能够支持并管理外部云服务商，进而增强我们的产品组合。与此同时，它还简化了我们现有基础设施的配置与升级方式，为集群提供最为自然的Kubernetes管理风格而且高度契合现有工作流程。<br>
<br>在将我们的本地集群迁移至Cluster API之后，我们期待着采取下一步行动：将集群配置交付给其他供应商，并与Kubernetes社区保持更高水平的交互。<br>
<br>Daimler TSS – Christian Schlotter – 软件工程师<br>
<br>Daimler TSS – Tobias Giese – 软件工程师<br>
<br>Daimler TSS – Sean Schneeweiss – 软件工程师<br>
<h3>New Relic – 为New Relic One可观察性平台管理基础设施</h3>Cluster API在New Relic的Kubernetes集群管理系统当中扮演着重要角色。这套系统帮助我们的工程师们更好地管理着部署在公有云中的各个Kubernetes集群的生命周期。Cluster API带来了一致、简单的声明式API，用以创建、配置并升级Kubernetes集群与节点池，让我们得以轻松简化集群队列自动化。除此之外，Cluster API还让我们轻松为工程师们提供统一的自助服务界面以管理基础设施。在Cluster API的帮助下，我们的工程师几乎不需要查看底层云服务商的控制台与API，而能够以Cluster API资源的形式直接在Kubernetes当中管理基础设施。我们为自己对Cluster API项目做出的贡献而深深自豪，也对此次发布的1.0版本、乃至未来将要推出的更高版本感到兴奋不已！<br>
<br>New Relic – Dane Thorsen – 首席软件工程师<br>
<h3>Red Hat</h3>在Red Hat，我们在Cluster API项目诞生之初就参与到贡献当中，努力将Machine API组件整合到我们Red Hat OpenShift 4集群自动伸缩、节点自动恢复与即席/竞价实例功能当中。以这种共通的上游成果为基础构建起OpenShift基础设施核心管理组件，不仅为我们带来了一次成功的经验、也让我们期待未来通过HyperShift等项目引入更多Cluster API功能，帮助用户轻松将控制平面与管理问题同生产工作负载结合起来。我们很高兴看到Cluster API迎来1.0版本，也向所有参与这一重大里程碑的贡献者们表示祝贺！<br>
<br>Red Hat – Michael McCune – 首席软件工程师<br>
<h3>德国电信技术公司</h3>在德国电信，我们的任务是为4G/5G核心网、IMS、FTTH、RAN、Edge等电信工作负载及相应管理应用（OSS）提供Kubernetes集群。这些工作负载不仅需要部署在大型数据中心之内，还需要被部署在全德国数百个小型本地部署位置当中。从2019年开始，我们就坚信CLUSTER API就是正确的前进道路。因此在2020年初，我们使用v1alpha2支持生产场景，并很快切换至v1alpha3以获取CLUSTER API在可用性与可管理性方面带来的重大突破。我们主要是在vSphere（CAPV）与裸机（Metal3）上通过集中管理集群运行自有集群。<br>
<br>Cluster API为我们提供了巨大帮助，也让多数据中心之间的多基础设施任务管理成为可能，使我们通过一支规模不大但专注度极高的SRE团队就顺利打理好相关管理任务。尤其是声明式方法，它与GitOps配合得天衣无缝，给我们带来了很大帮助。<br>
<br>随着我们将越来越多关键电信服务纳入CLUSTER API管理的集群之内，我们也很高兴看到Cluster API迎来自己的稳定版本。而且结合我们之前积累下的丰富经验，可以负责任地说，Cluster API在软件稳定性方面表现出色。这里要再次感谢每一位参与项目贡献的支持者！<br>
<br>德国电信 – Maximilian Rink – 高级站点可靠性工程师_<br>
<br>德国电信 – Vuk Gojnic – Kubernetes Engine Squad团队负责人<br>
<h3>美国陆军</h3>陆军CIO与陆军Software Factory下辖的企业云管理机构正在生产场景中利用Cluster API实现上游集群自动化。我们在不同级别、不同功能的各类环境当中运行有Kubernetes集群。我们需要一种方法来声明这些集群，从而满足默认的合规性与安全性标准，同时提供一个能够强制执行这些默认标示的区域控制平面。<br>
<br>我们已经体会到Cluster API当中的集群管理价值，它能够作为区域控制平面帮助我们建立起包含不同服务与组件的额外集群。也正因为如此，我们决定将Cluster API作为国防部Enterprise DevSecOps参考设计多集群CNCF Kubernetes的实现基础。<br>
<br>ECMA与陆军Software Factory一直期待着Cluster API的v1.0版本，稳定版的推出使我们能够扩展现有流程并实现流程自动化，进而为陆军用户提供更全面的业务支持。<br>
<br>美国陆军 – Paul Puckett – 企业云管理主管<br>
<br>美国陆军 – LTC Vito Errico – 陆军Software Factory主管<br>
<h3>微软 – Azure</h3>微软自两年前开始认真参与Cluster API项目，希望为包括Azure在内的各类自我管理Kubernetes集群用户提供更好的开源解决方案。在Kubernetes on Azure的探索初期，AKS Engine被指定为Kubernetes集群的配置工具。但其源代码位于Azure GitHub之内，而并非由CNCF（云原生计算基金）所控制。使用AKS Engine，用户能够在Azure上创建自我管理集群，但实际体验与其他基础设施服务商体验之间几乎没有任何一致性。而Cluster API的出现改变了一切，如今我们迎来了一个用于跨服务商构建基础设施的共享接口。<br>
<br>过去一年以来，Azure Container Upstream团队已经将上游Kubernetes测试迁移至Cluster API的生态系统当中，以确保Azure Kubernetes场景的验证流程全面使用开源CNCF工具。这对开源社区及微软自己来说都是一场巨大的胜利。我们得以使用由社区拥有并协同维护的工具在Azure上验证Kubernetes。在不久的未来，Azure上的所有Kubernetes验证测试都将使用Cluster API运行。<br>
<br>微软 – David Justice – 首席工程主管<br>
<h3>亚马逊云科技 – Cluster API面向Amazon EKS Anywhere</h3>Amazon EKS Anywhere的一大核心目标，是使客户能够使用Amazon EKS Distro在自己指定的基础设施服务商上预置Kubernetes集群；而另一个目标，则是提供一套声明式的集群管理方法。Cluster API一直强调基础设施中立性原则，允许用户根据需要通过可插拔模型添加新的服务商，而且项目提供的声明式Kubernetes集群与节点管理方法同我们的目标非常契合。因此，我们决定在Amazon EKS Anywhere当中使用Cluster API实现扩展、升级与删除等集群预置与生命周期管理操作。<br>
<br>在Amazon EKS Anywhere当中，我们得以在GitOps驱动的集群生命周期与配置管理流程中集成Flux，从而进一步发挥Cluster API提供的声明式操作机制。在实现这些目标的过程中，我们也与Cluster API社区充分互动并获得了宝贵的启发。<br>
<br>我们对此次v1.0版本的发布感到兴奋，也期待着与社区开展更多后续合作、为项目做出更多贡献。<br>
<br>亚马逊云科技 – Chandler Hoisington –  EKS Anywhere总经理<br>
<br>亚马逊云科技 – Jackson West – 软件开发经理<br>
<br>亚马逊云科技 – Rajashree Mandaogane – 软件开发经理II<br>
<h3>D2iQ</h3>D2iQ意识到集群生命周期管理是一个复杂的难题，需要灵活且可靠的解决方案作为支持。此外，公司还意识到最好是在社区之内对这两大目标的协调做出探索。我们的软件能够帮助客户跨越不同基础设施管理大量集群。我们使用到多种Cluster API基础设施提供程序，并在维护层面为社区做出了贡献。Cluster API架构允许我们与社区合作以解决各类常见问题，并在必要时插入专用的功能组件。<br>
<br>对我们来说，v1.0版本的发布证明了我们在Cluster API使用当中得出的结论：项目设计随着时间推移而不断发展成熟，其完全能够支持实际生产，而且项目社区拥有着丰富的专业知识与多样化的技术观点。我们期待着Cluster API更多后续版本的陆续推出。<br>
<br>D2iQ Daniel Lipovetsky – 高级软件工程师<br>
<br>D2iQ Deepak Goel – 首席技术官<br>
<h3>三星SDS</h3>三星SDS从很早就对Cluster API项目抱有兴趣，目前也在使用Cluster API作为SDS Cloud中托管Kubernetes服务的核心技术。我们建立起自己的的提供程序，确保Cluster API能够更好地与SDS Cloud的风格相适应。Cluster API使得Kubernetes集群能够在不同IaaS当中保持良好的一致性与可扩展性。我们也在尝试利用这些优势扩展自有服务，以在多混合云环境当中提供Kubernetes服务。<br>
<br>我们相信，Cluster API将继续遵循Kubernetes带来的路径、成为云原生生态系统当中集群生命周期的管理基础，项目v1.0版本的发布也让我们对这一前进方向充满信心。我们衷心感谢每一位为项目做出贡献的成员，也期待着通过社区的各种活动做出更多贡献！恭喜大家！<br>
<br>三星SDS Hansol Park – 高级工程师<br>
<br>三星SDS Kangsub Song – 高级工程师<br>
<br>三星_SDS Moonhyuk Choi – 高级工程师<br>
<h3>SK电讯</h3>在SK电讯，我们一直通过多混合云解决方案为金融、媒体、广播等行业的大型企业提供Kubernetes服务。从2019年初开始，我们就将Cluster API作为对集群生命周期管理的复杂性质加以抽象的正确方法。通过Kustomize、Helm与Argo工具链，我们已经充分运用到Cluster API提供的Kubernetes原生优势与声明式功能。如今，我们开始在公有云上通过Argo CD以GitOps方式为企业就绪型Kubernetes集群提供更多附加服务。我们还计划将这些成果进一步扩展到本地环境。<br>
<br>我们对v1.0版本的发布感到兴奋，从其他社区成员身上学到了很多，也将努力为社区提供回馈。我们期待着这个强大的社区能为世界带来更多振奋人心的成果！<br>
<br>SK电讯 – Jaesuk Ahn – 云原生开发负责人<br>
<br>SK电讯 – Seungkyu Ahn – 高级软件工程师兼韩国Kubernetes社区负责人<br>
<h3>VMware</h3>Cluster API项目是VMware将云原生工具推向更广泛受众群体的核心举措。VMware为企业客户的转型之旅提供支持，而Cluster API负责的正是在多云环境当中为用户提供跨基础设施服务商的统一体验。通过与社区中的其他参与者通力合作，我们成功以一致方式跨越各类基础设施部署与管理Kubernetes集群，具体涵盖vSphere、公有云乃至裸机。新近发布的ClusterClass通过更简单的界面实现了集群模式定义与共享，再次简化了整个流程。通过为平台团队建立起更强大的工具集，各团队又能反过来为应用程序团队提供自动化水平更高、速度更快且更为简单的内部产品，最终帮助应用程序团队获得更快的交付速度与更安全的交付效果。<br>
<br>VMware – Joe Beda – Tanzu项目首席工程师<br>
<br>在VMware，我们相信竞争是推动事物发展的动力，而协作则让这个世界更加美好。我们为自己能够与Kubernetes社区共同走过从CLUSTER API诞生到当前生产就绪阶段的美好旅程而感到自豪。作为一套系统方案，CLUSTER API从根本上重新定义了Kubernetes集群的部署与维护模式，将Kubernetes强大的控制功能引入了大规模基础设施管理领域。衷心祝贺社区此次发布v1.0版本，我们也对项目的未来充满期待。CLUSTER API不只是我们Tanzu产品线的基本组成部分，同时也是充满活力的Kubernetes生态系统当中越来越重要的一员。<br>
<br>VMware – Craig McLuckie – 现代应用与管理副总裁<br>
<h3>常见问题解答（FAQ）</h3><h4>为什么要从alpha迁移至1.0版本？</h4>迁移至v1.0/v1beta1源自众多企业对于CLUSTER API的生产就绪认可，反映出项目团队已经达成生产就绪目标的客观事实。无论先前我们的代码库或标签当中使用哪些语义版本，如今的1.0版都已经为生产场景做好了充分准备。<br>
<h4>CLUSTER API是如何做好准备的？</h4>去年，CLUSTER API社区在代码、API、说明文档以及对稳定性的广泛测试等方面投入了大量精力。<br>
<br>此外，我们还提供各API版本之间的自动转换、通过clusterctl工具进行自动升级，而且新近发布的各个API版本都经历了一年以上的技术支持。<br>
<br>而最后起到一锤定音作用的，是我们用户带来的丰富反馈——正是这些反馈，让我们确定CLUSTER API已经达成生产就绪状态。<br>
<h4>这会给开发速度造成影响吗？</h4>生产就绪不会影响到CLUSTER API的开发速度，因为项目团队已经拥有明确的结构，能够在实现生产级保障的同时推进后续开发。<br>
<br>在实践当中，CLUSTER API项目已经拥有一系列新功能孵化机制，包括功能标签或实验文件夹；目前，Machine Pools与ClusterClass等新功能都在按照这种方式进行开发。<br>
<br>而且恰恰相反，我们预计在升级至v1.0/v1beta1之后，用户群体会快速增长、大量新的用例与功能请求持续涌入，共同驱动我们的路线图快速推进。<br>
<br>未来一定会有更多很棒的思路与机会！<br><br>
<h4>在哪里能找到关于CLUSTER API项目的更多细节信息？</h4>请通过此频道联系我们：Kubernetes <a href="http://slack.k8s.io/">Slack</a>: <a href="https://kubernetes.slack.com/archives/C8TSNPY4T">#cluster-api</a><br>
<br>你也可以加入SIG集群生命周期<a href="https://groups.google.com/g/kubernetes-sig-cluster-lifecycle">Google Group</a> 接收日历邀请并访问说明文档。<br>
<br>另外，我们每周三上午10点（太平洋时间）都会在Zoom上准时召开<a href="https://docs.google.com/document/d/1P2FrRjuCZjGy0Yh72lwWCwmXekSEkqliUVTmJy_ETIk/edit">社区会议</a>。<br>
<h4>项目的下一步将去往哪里？</h4>CLUSTER API社区目前正在努力交付ClusterClass与托管拓扑，旨在大大简化用户以声明方式配置、升级及操作多个Kubernetes集群的操作流程。<br>
<br>后续发展路线图中当然还有更多新内容：更好地与集群自动伸缩器项目相集成、通过新的可扩展点实现可插拔负载均衡器解决方案、托管外部etcd集群、可插拔运行时扩展等等！<br>
<br>敬请关注！<br>
<br>Cluster API维护团队<br>
<br><strong>原文链接：<a href="https://www.cncf.io/blog/2021/10/06/kubernetes-cluster-api-reaches-production-readiness-with-version-1-0/">Kubernetes Cluster API reaches production readiness with version 1.0</a></strong>
                                
                                                              
</div>
            