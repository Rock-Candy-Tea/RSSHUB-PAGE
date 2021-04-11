
---
title: '创建一个成熟的GitOps流水线，需要做哪些决定？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/2021040723493641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center'
author: Dockone
comments: false
date: 2021-04-11 00:29:10
thumbnail: 'https://img-blog.csdnimg.cn/2021040723493641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center'
---

<div>   
<br>在软件交付领域，GitOps是近期的热门趋势，它沿袭并扩展了DevOps、基础架构即代码和CI/CD等趋势。我们此前发布了许多关于GitOps的入门文章，您可以在【Rancherlabs】公众号后台回复【Git文章】获取GitOps文章合集。<br>
<br>GitOps的优势可以简单地归纳如下：<br>
<ul><li>自由地审计更改 </li><li>持续集成和交付 </li><li>更好地控制更改管理</li></ul><br>
<br>然而，现实情况却是构建GitOps流水线并非易事，它涉及到许多大大小小的决定，而这些决定会给实施工作带来许多麻烦。我们将这些决定称为“GitOps架构”，它可能会导致实施过程中面临许多挑战。<br>
<br>好的方面是只要有一定的规划和经验，就可以大大减少过渡到GitOps交付模式的痛苦。<br>
<br>在本文中，我将通过一家公司的故事来解释其中的一些挑战。这家公司从一个零散的小创业公司采用GitOps，成长为一家规范的跨国企业。虽然这种加速成长的情况很少见，但它确实反映了大型组织中的许多团队从概念验证，到最小可行性产品（minimum viable product），再到成熟系统的经验。<br>
<br><h2>简单的开始</h2>如果你刚刚开始，最简单的做法是创建一个单一的Git repo，将所有需要的代码都放在里面。其中可能包括：<br>
<ul><li>应用程序代码</li><li>Dockerfile，用于构建应用程序镜像</li><li><br>一些CI/CD流水线代码（例如GitLab CI/CD或GitHub<br>
Actions）</li><li><br>Terraform，以配置运行应用程序所需资源</li></ul><br>
<br>此外，所有的更改都是直接对master进行改动，因此更改可以直接生效。<br>
<br>这一方法的主要优势在于你有单一的参考点，以及所有代码都会紧密集成在一起。如果您的所有开发人员都受到完全信任，并且速度就是一切，那么这一方法会持续生效。<br>
<br>不幸的是，随着你的业务量不断增长，这种方法的弊端很快就会显现出来。<br>
<br>首先，随着越来越多的代码被添加到代码库中，代码库规模的膨胀会使得工程师们陷入困惑，因为他们会遇到更多必须解决的更改之间的冲突。如果团队成员大幅增长，那么随之而来的重新分配工作或合并会导致进一步的混乱。<br>
<br>其次，如果您需要分开控制流水线运行，则会遇到困难。有时，您只想快速测试对代码的更改，而不是进行部署以实现完整的端到端交付。这种方法在整体性方面产生了越来越多需要解决的问题，随着这些更改的进行可能会影响其他人的工作。<br>
<br>第三，随着您的成长，您可能会希望工程师和团队之间的责任边界更加细化。这可以通过一个单一的repo来实现，并且一个repo通常是一个更清晰和更干净的边界。<img src="https://img-blog.csdnimg.cn/2021040723493641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><h2>分离Repository</h2>随着业务的增长，流水线会越来越拥挤，merge开始变得痛苦。此外，您的团队也需要专业化，将不同的责任领域划分给不同的成员。<br>
<br>所以你需要将Repo分离出来。这时，你首先要面对大量的决定，譬如repo应该分离到什么程度？是否需要为应用程序代码建立一个单独的repo？看起来是不是很合理？然后把Docker构建的东西也一起放进去？那这样的分离其实没有什么意义。<br>
<br>那所有团队的Terraform代码呢？应该放在一个新的repo里吗？这听起来很合理，但是：新创建的中央“平台”团队想要控制对AWS中核心IAM（身份和访问管理）规则定义的访问，而团队RDS配置代码也在其中，开发团队需要定期对其进行调整。<br>
<br>所以你决定将Terraform分离成两个repo：一个是“平台”repo，一个是“特定应用程序”repo。这就带来了另一个挑战，因为你现在还需要分离Terraform的状态文件。这并不是一个无法解决的问题，但这也并不是您所习惯的快速功能交付，所以产品经理将不得不解释为什么功能请求所需的时间比之前更长。<br>
<br>不幸的是，这些GitOps决策还没有既定的最佳实践或模式。<br>
<br>分离的问题还不止于此。以前，流水线内构建的组件之间的协调是微不足道的（因为所有需要的组件都是共处的），而现在你必须协调repo之间的信息流。例如：当构建一个新的Docker镜像时，这可能需要触发集中式平台repo中的部署，同时将新的镜像名称作为触发的一部分传递过来。<br>
<br>同样，这些也不是无法解决的问题，但在构建GitOps流水线的早期，这些挑战更容易实现。后来，当步骤、政策和流程更加成熟时，再做出改变就需要付出更多的时间代价。<br>
<br><h2>分布式vs集中式</h2>你的业务正在增长，你正在构建越来越多的应用程序和服务。越来越明显的是，在如何构建和部署应用程序方面，你需要某种结构上的一致性。中央平台团队需要尝试执行这些标准。但是你可能会遭到开发团队的反对，他们认为与在DevOps和GitOps出现之前，在集中式IT中他们被赋予了更多的自治和控制权。<br>
<br>如果上述情况您觉得似曾相识，那可能是因为GitOps和应用架构领域的单体与微服务争论之间有些类似。就像你在这些争论中看到的那样，随着系统的成熟，规模和范围的扩大，分布式和集中式IT之间的紧张关系会越来越频繁地出现。<br>
<br>从某种层面上来说，你的GitOps流程就像其他分布式系统一样，如果你设计得不好，其中一个部分出现问题可能会产生难以预料的问题。<br>
<br><h2>环　境</h2>在你决定分离repo的同时，你意识到你需要一种一致的方式来管理不同的部署环境。而直接上线已经行不通了，因为此时需要QA团队，在上线之前测试更改。<br>
<br>现在你需要为你的应用镜像在测试和QA环境中指定不同的Docker标签，你可能还希望在不同的环境中启用不同大小的实例大小或副本功能。你如何在源码中管理这些不同环境的配置？一个比较直接的方法是为每个环境建立一个单独的Git仓库（如：super-app-dev，super-app-qa，super-app-live）。<br>
<br>分离repo有 “泾渭分明” 的好处，就像我们在上面划分Terraform代码时看到的那样。然而，很少有人最终会喜欢这种解决方案，因为大多数团队不具备Git知识和相关专业水平，进而在不同的repo之间移植更改。更为复杂的是，repo之间必然会存在很多重复的代码，而且随着时间的推移，也可能会出现很多漂移（drift）。<br>
<br>如果你想把事情保持在一个单一的repo中，你至少有三种选择：<br>
<ul><li>每个环境都有一个目录 </li><li>每个环境都有一个分支 </li><li>每个环境有一个标签</li></ul><br>
<br><img src="https://img-blog.csdnimg.cn/20210407235104160.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><h2>同步步骤选择</h2>如果你严重依赖YAML生成工具或模板，您可以考虑另一种方式。例如，Kustomize强烈鼓励基于目录的环境分离。如果您使用的是原始YAML，那么分支或标记的方法会更适合您。<br>
<img src="https://img-blog.csdnimg.cn/20210407235129122.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><h2>运行时环境颗粒度</h2>然而，在您的运行时环境中，可以选择您想要什么级别的分离。在集群层面，如果您使用的是Kubernetes，你可以在以下几种情况下选择：<br>
<ul><li>一个集群管理所有 </li><li>每个环境一个集群 </li><li>每个团队一个集群</li></ul><br>
<br>在极端情况下，你可以把所有的环境放到一个集群中。不过通常情况下，在大多数组织中至少有一个单独的集群用于生产。<br>
<br>一旦你想好了你的集群策略，在命名空间层面，你仍然可以选择：<br>
<ul><li>每个环境都有一个命名空间 </li><li>每个应用程序/服务拥有一个命名空间</li><li>每个工程师拥有一个命名空间 </li><li>每个构建都有一个命名空间</li></ul><br>
<br>平台团队通常从 “dev”、“test”、“prod” 的命名空间设置开始，然后才意识到他们想要更精细地分化团队的工作。<br>
<br>你也可以混合和匹配这些选项——例如，为每个工程师提供"desk testing "命名空间，以及每个团队的命名空间。<br>
<br><h2>总  结</h2>我们在这里只是对成熟的GitOps流程所需的决策领域做了一些简单的介绍。如果您的企业真的成长为那家跨国企业，你也可以考虑RBAC/IAM等要求。<br>
<br>通常情况下，推出GitOps会让人觉得只是一种投资，可能最终没有太多令人满意的产出。但是在GitOps之前，团队常常会经历混乱和延迟，因为没有人能够确定任何东西应该是什么状态。这些都会导致二次成本，因为审计人员会进行抽查，而因意外和未记录的更改而导致的中断则占据了员工大量的注意力，这是一个很高的成本。<br>
<br>然而，随着你的GitOps流程的愈发成熟，好处倍增，该流程会解决许多之前存在的问题。但更多的时候，你面临的压力是要更快地展现出GitOps流程的优势。<br>
<br>目前GitOps最大的挑战是，没有既定的模式或是最佳实践来指导你的选择。GitOps顾问，通常也只是引导团队找到最适合他们的解决方案，并根据经验将团队往某些方向引导。<br>
<br>但我观察到的情况是，早期因为看起来 “太复杂”而被放弃的选择，往往后来都会为此后悔。这并不意味着你应该直接跳到为每个构建创建一个命名空间，每个团队拥有一个Kubernetes集群的程度，原因有二：<br>
<br>每当你给GitOps架构增加复杂性时，你最终都会增加交付一个可行的GitOps解决方案的成本和时间<br>
你可能真的永远都不需要这种设置<br>
<br>在我们接受这个领域的可行标准之前，正确的 GitOps 架构永远是一门艺术，而不是科学。<br>
<br><blockquote><br>原文链接： <br>
  <a href="https://blog.container-solutions.com/gitops-decisions" rel="nofollow" target="_blank">https://blog.container-solutio ... sions</a></blockquote><h2>关于Rancher Labs</h2>Rancher Labs由CloudStack之父梁胜创建。旗舰产品Rancher是一个开源的企业级Kubernetes管理平台，实现了Kubernetes集群在混合云+本地数据中心的集中部署与管理。Rancher一向因操作体验的直观、极简备受用户青睐，被Forrester评为2018年全球容器管理平台领导厂商，被Gartner评为2017年全球最酷的云基础设施供应商。<br>
<br>目前Rancher在全球拥有超过三亿的核心镜像下载量，并拥有包括中国人寿、华为、中国平安、兴业银行、民生银行、平安证券、海航科技、厦门航空、上汽集团、海尔、米其林、丰田、本田、中船重工、中联重科、迪斯尼、IBM、Cisco、Nvidia、辉瑞制药、西门子、CCTV、中国联通等全球著名企业在内的共40000家企业客户。
                                
                                                              
</div>
            