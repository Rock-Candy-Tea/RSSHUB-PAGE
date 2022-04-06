
---
title: 'Prodspec和Annealing'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/9d5c60809d65da79829ea62a75ab9704.jpg'
author: Dockone
comments: false
date: 2022-04-06 06:11:26
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/9d5c60809d65da79829ea62a75ab9704.jpg'
---

<div>   
<br><strong>Google生产环境上基于intent（意图）的actuation（执行）</strong><br>
<br>随着企业的逐步成熟，他们会开发更多工具。在Google，我们持续创建新的外部和内部服务，以及支持这些服务的基础架构。从2013年起，我们开始放弃之前用来更新和维护服务的简单的自动化工作流。每个服务都要求复杂的更新逻辑，并且还需要适应基础架构的变化，经常性的集群的启动关闭等等。配置多个，互相交互的服务的工作流变得难以维护。我们需要一种全新的方案来适应业务的增长以及所涉及到的配置的复杂性。为此，我们开发了声明式的自动化系统，作为统一的控制层，并且取代了工作流。这个系统包括两个主要的工具：Podspec，描述服务基础架构的工具，和Annealing，更新生产环境来匹配Prodspec输出的工具。本文讨论我们解决过的问题，以及我们所选择的架构。<br>
<br>Prodspec和Annealing有一个根本共同点：不再关注于给生产环境推送单独的变更，而是关注于想要达到的状态。不再维护一步一步的工作流，而是让服务所有者使用配置来描述他们想要基础架构达到的样子：运行什么job，负载均衡器的搭建，数据库schema的位置等等。基于这些信息，Prodspec和Annealing将这些配置转化成统一的结构，随后被执行。执行是安全并且持续性的：自动化系统重复地比较用户模型所表达的预期状态和生产环境的状态，并且在安全的时候自动触发reconciliation。服务所有者不再需要将配置变更手动推送到生产环境里。<br>
因为我们从2015年左右就开始开发Prodspec和Annealing，基于intent的执行（intent-based actuation）这一简单明了的理念如今已经成了实际的标准。Google生产系统的很大一部分现在已经有了这样的预期状态抽象层，而不再依赖工作流的状态——这是一个广泛影响业界的趋势。<br>
<h3>术语</h3>运行一个现代化的服务有很多必要部分。特别在谈论基础架构即服务时，有些术语很混乱。比如，谁是“用户”？人还是使用基础架构的服务？还是终端用户？或者别的什么？<br>
<br>图1展示了本文所设计的各个参与方：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/9d5c60809d65da79829ea62a75ab9704.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/9d5c60809d65da79829ea62a75ab9704.jpg" class="img-polaroid" title="01.jpg" alt="01.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1：围绕“服务”的术语</em><br>
<br>服务是某个团队想要运行的面向用户的系统，比如Gmail或者Map。服务由多个内部子服务组成——比如，Gmail服务的检测垃圾邮件的服务仅仅是组成Gmail的众多服务之一。<br>
<br>为了帮助解释本文的观点，我们会提到<a href="https://sre.google/sre-book/production-environment/">Shakespeare服务</a>的服务器部分，这是一个假象的服务，如图2所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/2957e7e59212da07265520a585bcdd76.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/2957e7e59212da07265520a585bcdd76.jpg" class="img-polaroid" title="02.jpg" alt="02.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2：简单的Shakespeare服务，LB是“负载均衡器”。</em><br>
<br>这个服务是个简化的Web应用，由这些部分组成：<br>
<ul><li>为了冗余而在两个集群上运行的二进制文件，实现前段逻辑</li><li>负载均衡，有集群前和全局的配置</li><li>全局的<a href="https://cloud.google.com/spanner">Spanner</a>数据库</li></ul><br>
<br>生产或者服务基础架构提供服务所需的基础模块来服务用户的请求，比如，<a href="https://research.google/pubs/pub43438/">Borg集群管理系统</a>，网络交换机的firmware等等。每个这些组件都是一个asset。<br>
<br>Shakespeare服务使用多个基础架构提供者：Borg来运行二进制文件，<a href="https://sre.google/sre-book/production-environment/">GSLB</a>管理负载均衡，以及Google共享的Spanner基础架构。<br>
<br><strong>控制平面</strong>是服务用于管理生产服务基础结构的平面——比如，添加一台VM或者搭建负载均衡器。控制平面可以包括人工（“我会把新的二进制文件拷贝到服务器上”）到复杂的自动化系统（“我使用机器学习来控制变更”）。控制平面包括<strong>变更管理</strong>：控制平面里的逻辑允许服务以安全且受控的方式从生产环境的一种状态变化到另一种状态。<br>
<br>在Shakespeare服务里，前端的<em>控制平面</em>是Borg API，它配置了相应的job并且在每个集群里运行这些job。<br>
<br>本文将<strong><em>job</em></strong>定义为一系列类似的任务，和Kubernetes的ReplicaSet类似。<strong><em>任务</em></strong>是单个运行着的实例，通常是单个进程，类似于Kubernetes的Pod。某个job在单个集群里运行所有任务。集群是一系列能够运行多个任务和集群的计算节点，通常物理上是放在一起的。<br>
<br>在Shakespeare服务里，每个前端是给定集群里的一个job。<br>
<br>下一节我们重点介绍如何为生产环境引入控制平面来改进变更管理。<br>
<h4>我们的挑战</h4>服务设计倾向于关注服务基础架构，解决重要也很基础的问题：用户请求如何响应？你的服务使用哪些服务器和数据库？服务需要支持多大的流量？<br>
<br>这些都是很重要的问题，但服务是动态并且变化的：二进制版本不断更新，实例被添加和删除。架构也就需要随之演进：可能需要在某个特定的集群添加新的缓存，移除一些过时的日志等等。<br>
<br>在2014年，我们发现自己不能充分地适应服务的灵活性。对于绝大多数服务，我们使用人工编制的工作流来变更基础架构：推送x，然后y；手动执行不常见的变更。<br>
<br>但是团队通常需要管理数十个服务，每个服务都有很多job，数据库，配置以及自定义的管理流程。已有的解决方案因为如下两大原因无法扩展：<br>
<ul><li>基础架构配置和API是异构的，并且很难连接在一起——比如，不同的服务使用不同的配置语言，抽象级别，存储和推送机制等等。因此，基础架构不一致，很难确定出通用的变更管理。</li><li>生产变更管理的流程很脆弱，不理解变更之间的联系。</li></ul><br>
<br><h4>配置Gap</h4>从基础架构提供者的角度看，给定服务的配置很容易有很多冗余。在Shakespeare服务里，所有东西都是用相同的用户完成的，因此给每个前端job指定用户就是多余的。但是，因为基础架构需要运行很多服务的job，配置上仍然必须为每个job指定用户。<br>
<br>基础架构提供者的简单解决方案是提供更为强大的配置界面——比如，一种模版语言。但是，从服务的角度来看，这样的方案并没有根本性地消除冗余。服务需要配置多个提供者，这些提供者的一些信息通常是一样的。比如，数据库名字对于使用它的job（计算提供者）和配置数据库的job（数据库提供者）都是需要的。<br>
<br>在这些场景里，配置系统都很有用。不管谁维护服务，都可以创建这些服务的高层级描述（比如，在集群x，y，z里运行N任务），并且配置系统将这些描述扩展成更适合每个基础架构提供者的格式。<br>
<br>但是没有两个服务是完全相同的，服务有很多类型，有时候称其为服务模型。服务模型可能构成像Shakespeare服务的简单服务：有前端，负载均衡器以及数据库。服务模型仅需要知道运行哪个二进制文件，在多少集群里运行它，以及数据库schema。服务模型的逻辑随后扩展该服务的配置。比如，服务模型能够将集群列表转化为负载均衡器基础架构的配置。<br>
<br>实际上，<strong>服务模型</strong>可能就是简单的一段脚本，将一个配置文件扩展为基础架构所需要的东西：服务模型也可能是复杂的piepeline。<br>
<br>如果你在处理多个服务模型以及多个基础架构提供者，就不得不维护N个服务模型和M个基础架构提供者之间的集成。这样的集成包括为每个提供者生成特定的配置并且部署它们——这个程序对于不同的提供者可能大不相同。<br>
<br>我们称之为N<em>M问题，详见图3。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/7b1343a678c687a9db61646ea8e49bf8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/7b1343a678c687a9db61646ea8e49bf8.jpg" class="img-polaroid" title="03.jpg" alt="03.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
*图3：每个服务模型必须和每个基础架构提供者集成</em><br>
<br>如果只需要处理几个基础架构提供者，N*M问题还是可以管理的。随着基础架构提供者数量的增多（看看Google Cloud，AWS和Microsoft Azure上的产品数量），这些集成的数量和质量问题就开始出现了。<br>
<br>实际上减少基础架构提供者的数量不太实际。每个提供者都在提供不同的服务（比如，键值存储，pub/sub系统等），并且一些冗余不得不存在，就算定义好规则也会有很多异常情况出现。使用单个服务模型也不现实——这个模型必须能够暴露所有基础架构提供者的每一个特性，这违反了服务模型的初心。<br>
<br>Google的工程师们花费了大量时间将他们需要的服务模型连接到想要使用的基础架构上。我们显然需要一种不同的配置方案。<br>
<h3>大规模部署</h3>在解决这个问题之前，我们依赖于传统的工作流引擎。比如，一个工作流列出部署新二进制文件的步骤：在集群X上做金丝雀测试，然后将N部署到集群Y和Z上，运行测试等等。创建工作流本身就需要大量工作，因此我们只为经常需要做的事情创建工作流，比如二进制文件的版本更新。我们通常手动处理不那么常见的情况，比如重启。已有的脚本经常会过期而不再适用。<br>
<br>对于运维人员来说，这些工作流很容易实现：做X，然后Y。想要添加压力测试？只需要添加一个步骤。但是随着工作流使用规模的扩大，它的问题也显露出来。<br>
<br>首先，扩展工作流会造成很多重复。每个服务都有很好的理由要求一些特殊逻辑，这意味着需要定制化的实现。尝试了几次整合工作流的实现，但是只有适用于某个特定模型的服务才能使用。这样导致的重复让服务变得不一致。最佳实践，比如跨集群的有序迁出，就很难总结出共同的部分。<br>
<br>工作流也很脆弱。原生工作流有很多关于生产状态的隐性假设，这会导致不可预期的故障。要避免错误，我们添加了前提条件：金丝雀集群是否服务于真实流量？底层有没有运行中断？但是因为我们需要扩展到数十个基础架构提供者和上百个服务，这些web的前提条件变得非常tricky。每个工作流都需要知道其他工作流的状态。<br>
<br>交互变成了N²问题，这里N是组成服务基础架构的asset数量。当你更新单个asset时，需要考虑它可能带给别的asset或者工作流的影响。比如，现在是否能够重启缓存，或者是否需要等待另一个缓存稳定了之后？如果需要手动变更某个在线的工作流，有没有哪些别的工作流也需要操作的？<br>
<h3>我们的方案：Prodspec和Annealing</h3>手动设计每个工作流变得不太可能了。必须要改变什么来减少交互和预期的数量。面对激增的服务模型和大规模部署的痛点，我们通过Prodspec管理的intent以及Annealing针对该intent的持续执行，来实现生产环境的声明化管理。<br>
<br>在面向工作流的生产管理模型里，生产环境状态的大部分仅仅存在于生产环境里。比如，前端运行的是版本X，因为几天之前你才升级到这个特定版本。<br>
<br>相对应的，声明式生产意味着编写生产状态的intent——生产环境应该运行版本X——使用某个配置文件或者数据库。生产状态现在是从intent派生出来的。配合持续推进，就可以确保生产状态和用户预期相匹配。<br>
<br>在我们的实践里，intent通常是直观的，很少有歧义。但是，维护intent是困难的，要求大量的逻辑。Prodspec（下一节会更深入地讨论）是这个建模问题的解决方案。<br>
<br>基于intent的执行需要首先转变对如何修改生产环境的看法。可以用“宠物vs牛群”理论来描述这个问题：以前，我们把工作流当作宠物：维护每个工作流的运行，手动调优，并且单个交互。而基于intent的执行将生产asset当作牛群：特殊情况很少，扩展变得很容易。因此，我们创建了成为Annealing的持续执行系统。<br>
<br>生产管理的大部分现在都是基于intent的，并且每秒可以向生产环境推送上百个变更——这里每个变更推送整个job，变更配置，应用新的数据库schema等。当然，在某些领域工作流仍然存在。很多时候是因为工具还不能覆盖特殊领域（比如，批量pipeline），但是也有些情况是特定的需求下工作流更为合适。<br>
<h3>其他解决方案</h3>本文描述的很多理念可能在服务部署和管理领域比较常见。声明式自动化在过去几年变得很常见，因此可以在你自己的生产管理环境里发现和Google的声明式自动化系统（Prodspec和Annealing）很类似的东西。<br>
<br><strong>Kubernetes</strong>可能是最为类似的系统。Kubernetes项目在Google内部启动的时间和Prodspec和Annealing项目差不多。最初Kubernetes的定位是在声明式服务管理框架之上构建的容器编排系统。在Google之后很多服务使用Kubernetes。开源的属性让Kubernetes必须很灵活，可以兼容很多不同风格的生产管理。<br>
<br>与之对应，Prodspec和Annealing则必须能够和已有的基础架构以及配置兼容，因此一开始就是针对大量服务的。不过这两个项目都是Google内部使用的，这就和外部世界有些不同。<br>
<br>因此虽然问题域是类似的，但是Kubernetes的目标和限制条件和Prodspec，Annealing是不同的。因此，它们的优先级和解决方案是不同的。这是共同进化的一个实例，很明显很多项目的基本理念都是类似的——至少表面上看是这样。比如，Kubernetes CRD和Prodspec的asset解决的问题类似。Prodspec创建asset时有严格的参数要求，而Kubernetes就更为灵活，允许资源的部分mutation。<br>
<br><strong>Terraform</strong>是使用声明化配置语言定义并且提供数据中心基础架构的开源工具。在2014年推出首个版本，时间线和Kubernetes，Annealing类似。Annealing和Terraform之间有很多相似之处，虽然它们是完全独立开发的。比如，Terraform提供者类似于Annealing的插件，都是提供和任意基础架构集成的。Terraform的目标是更新生产状态去匹配用户提供的intent——这和Annealing一样。当然，它们也有一些主要的不同，比如：<br>
<ul><li>Annealing是为了持续执行而构建的。Annealing仅在安全的时候去应用更新过的配置，不需要人工交互。Annealing在应用变更后会监控服务健康情况。</li><li>Terraform有统一的配置界面HCL。与之对比，Prodspec直接使用已有的配置资源。</li><li>Prodspec强制密封性，允许生成配置数据，而无需访问其所描述的生产环境。配置数据可以跨版本进行比较，并由任何工具读取， 而不仅仅是驱动层。</li><li>Prodspec是权威的，Annealing是为了能从生产中恢复状态而构建的。这避免了像Terraform这样需要一个状态文件，但它要求基础架构提供者提供干净的资源命名，并会影响下线的管理。</li><li>Prodspec和Annealing扩展到了Google需要管理的数百万资源。</li></ul><br>
<br>Annealing集成了很多其他工具来驱动生产环境，有时候包括Terraform。<br>
本文剩下的部分仅仅关注于我们如何在内部服务上使用Prodspec和Annealing。<br>
<h3>Intent管理：Prodspec</h3>为了解决NxM问题，我们引入了一个明确的统一生产模型，称为"Intent"。<br>
<br>如图4所示，intent模型适用于服务模型和基础架构提供者。不用处理很多不同的服务模型，基础架构提供者获得统一的intent输入。不用适应每个基础架构提供者的不同，服务模型可以使用标准化的表示方式（intent模型）。<br>
<br>回到Shakespeare服务：配置驱动服务模型，随后生成intent来配置Borg，负载均衡器和Spanner。<br>
<br>这样，我们把intent的生成和驱动分离开，将NxM问题变为N+M问题，让配置和服务模型变得可管理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/e01970839dd8f40f4f719018df1adf54.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/e01970839dd8f40f4f719018df1adf54.jpg" class="img-polaroid" title="04.jpg" alt="04.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4：变成N+M问题，驱动层没有展示</em><br>
<br>这种明确的intent也让我们能够检视配置，可以更容易地对复杂设置进行故障排除。比如，使用直接集成进提供者的模版系统，很难分辨问题是由于模版逻辑，还是提供者的逻辑导致的。明确的intent使得很容易分辨是哪一层导致问题（见图4）。这是预期的intent吗？如果是，问题就出在提供者那里。如果不是，那就是服务模型的问题。<br>
<br>基于intent的生产模型及其工具称为Prodspec。它是从2000年中的Gmail演进出来的想法。包括这些组件：<br>
<ul><li>组织内容的数据模型</li><li>生成内容的pipeline</li><li>服务基础架构</li></ul><br>
<br>下面的小节讨论数据模型的细节以及如何生成内容。不会介绍服务内容的细节，因为我们使用了相对标准的搭建。<br>
<h4>数据模型</h4>Prodspec的声明式intent是通过一些抽象建模的，如图5、6所示：<br>
<ul><li>资产（asset）：每个asset描述生产环境的一个特定方面</li><li>分区（partition）：组织管理域中的asset。</li><li>化身（incarnation）：表示给定时间点的分区快照。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/4251f9fa6cdf02a7941de3edd934a874.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/4251f9fa6cdf02a7941de3edd934a874.jpg" class="img-polaroid" title="05.jpg" alt="05.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5：Prodspec的数据模型</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/c96015baeca83b5d7ef504206082395c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/c96015baeca83b5d7ef504206082395c.jpg" class="img-polaroid" title="06.jpg" alt="06.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6：Prodspec里Shakespeare服务的简化视图。LB代表负载均衡器</em><br>
<h4>Asset</h4>asset是Prodspec数据模型的核心。asset包含给定基础架构提供者某个特定资源的配置。比如，asset可以代表给定集群的资源或者如何配置某个特定job的指令。<br>
在Shakespeare服务（见图6）里，需要代表每个前端job的asset，表示每个cell负载均衡器配置的asset，全局负载均衡器配置的asset，以及Spanner DB schema的asset。<br>
<br>asset是具有以下结构的通用抽象：<br>
<ul><li>string标识符，简称为“asset ID”。</li><li>负载</li><li>0个或者多个插件</li></ul><br>
<br>负载和插件是任意<a href="https://developers.google.com/protocol-buffers/docs/overview">protobuf</a>消息。负载的类型定义了asset的类型。比如，如果负载是类型为prodspec.asset.BorgJob的protobuf消息，意味着这个asset表示运行在Borg上的job，并且会作为BorgJob asset被引用。<br>
<br>插件使得可以给asset添加任意元数据，无论是什么类型。插件对于跨领域问题特别有用。比如，常见的“受影响集群”插件让大家能够了解asset的影响域——如果这个asset不健康，它仅仅会导致某个集群的运行中断，还是会影响全球的服务？插件还给用户特定的数据提供了空间，而不用占用负载的定义。<br>
<br>asset一般少于1kb数据，通常少于10kb，我们的最大值限制的是150kb。这个限制是为了让asset更容易被使用。这样，工具可以在内存里加载asset，无需担心这么做会造成过多的消耗。这个方案是受<a href="https://en.wikipedia.org/wiki/Entity_component_system">实体-组件系统</a>的启发。<br>
<br>asset的内容提供了足够的信息来构建建模资源的完整状态。具体来说，应该可以重新创建生产状态，而不必查看当前的生产状态——这是一个单向过程。<br>
<br>但是，所有的配置必须在asset里。比如，我们肯定有些情况需要MB级别的配置。这时，可以保存对外部数据源（比如包，数据库和版本控制）的引用。这些引用必须指向不可变外部数据。<br>
<br>在Shakespeare服务里，这可能意味着Spanner的asset只包含一个指针，指向被引用的数据库schema存储的位置。<br>
<br>asset通常会引用特定的资源——数据库，job，配置等等。但是，建模高层级概念也是很常见的。比如，asset可以描述最终想要部署的二进制文件的版本，而单独的job asset可能会引用前一个版本。代表其他asset组合（比如，每个故障域）的asset也很常见。<br>
<h4>分区</h4>asset被分组到称为分区的管理边界中。分区通常与服务 1：1 匹配，但是也有例外。例如，给定用户可能希望其 QA 环境有一个分区，Prod 环境有另一个分区。另一个用户可能对其 QA 和 Prod 环境使用相同的分区。在实践中，我们利用分区的概念来简化管理。仅举几个例子：<br>
<ul><li>内容生成是按分区发生的</li><li>很多ACL都是按照分区设置的</li><li>执行是按分区严格隔离的</li><li>asset ID在分区内必须唯一</li></ul><br>
<br>分区内的asset不是结构化的，而是组织成非排序列表的形式。这些年的经验告诉我们，对于结构化服务asset来说，真的没有一个size适应所有的方案。但是，我们并不完全放弃结构：asset字段可以包含对其他asset的<strong>引用</strong>，而不是构建asset本身。这样就可以在同一asset上创建多个层次结构。例如，集群层次结构不同于依赖项层次结构。这些引用字段被显式标记为此类，从而允许以编程的方式发现。<br>
<h4>Incarnation</h4>我们通常给分区内容打快照。这些快照成为incarnation，每个incarnation都有唯一ID。incarnation是访问Prodspec数据的唯一方式。incarnation模型不仅是生成逻辑的自然结果（见生成pipeline），而且提供了<strong>不可变性</strong>和<strong>一致性</strong>。<br>
<br><strong>不可变性</strong>确保所有访问Prodspec的执行者都能基于相同的数据做决策。比如，如果一个服务器负责认证某个asset是否可以安全地推送，执行推送的服务器保证是在相同的数据上工作。缓存变得至关重要，可以在事后检查用于自动决策的信息。<br>
<br><strong>一致性</strong>很重要，因为我们很少孤立地查找asset。asset可能需要引用其他asset来组合出完整的配置。如果这些asset的内容来自不同的时间点，则可能最终得到错误的假设。想象一下，在Shakespeare服务中，一个集群的容量减少了，这个变更需要减小该集群中前端job的大小和相应的负载均衡器配置。如果没有一定的一致性，Annealing可能会在更新负载均衡器配置之前就减少了job的大小，这可能会导致服务的过载。<br>
<h4>生成pipeline</h4>在之前Prodspec的开发中，我们决定将asset如何创建和如何消费分离开。<br>
<br>我们本可以采用更简单的方法，使用数据库来存储asset，并使用这个数据库来更新内容（例如，更改asset字段的值）和读取内容。Kubernetes使用的就是这种模型，有其优点。但是，当直接在数据库中更新字段和asset内容时，它们很容易变得不一致。比如，job重命名可能会丢失一些job，因此写或更新内容的每个人都需要保证信息一致性。<br>
<br>相反，Prodspec将内容创建和内容消费分离开。incarnation及其asset是从“真相来源”（Sources of Truth，SoTs）生成的。SoTs通常只是简单的配置文件，但有时候是更为复杂的来源，比如任意数据库。和更为传统的数据库模型相比，Prodspec的方案有如下优势：<br>
<ul><li>可以优化数据模型，让数据更容易被消费。大多数数据模型避免冗余，因为冗余会让写入者一致性地编辑数据变得困难。因为我们的模型不允许编辑数据，所以可以生成重复的信息。这样，消费者那边的逻辑可以比较简单——比如，它们不需要特殊逻辑来找出某个字段的默认值存储在哪里，而只需要依赖扩展后的数据就可以了。</li><li>和已有配置的集成。这是创建自己的生成pipeline的主要驱动力。在实践中，用户已将Prodspec与大量配置格式和实践集成在一起。</li><li>"真相来源"可以针对人工或编程编辑进行优化。这很有用，因为我们需要用和配置Google Maps前端完全不同的方式来配置网络交换机。例如，你可能希望同时变更所有前端服务器的二进制版本。使用简单的数据库方案时，这需要编辑每个asset，从而导致潜在的不一致性，特别是在其他更为复杂的情况下。相反，使用Prodspec，就只有一处真相来源，定义二进制版本的字段，然后可以生成所有前端asset，确保一致性。</li><li>更容易地向后兼容性。我们通常添加一个新字段来修复或者扩展已有字段的语义。当这么做的时候，在生成pipeline里添加逻辑，就会自动填入内容的某个字段。这样，生产者和消费者就会被更新，从而逐渐地使用新字段，并且无需执行任何有风险的同步更新。</li></ul><br>
<br>图7展示生成Prodspec内容的Pipeline：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/bab8c7317d424c5452d6fc4acdf752c0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/bab8c7317d424c5452d6fc4acdf752c0.jpg" class="img-polaroid" title="07.jpg" alt="07.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7：Prodspec的Pipeline</em><br>
<br><strong><em>真相来源（SoT）</em></strong>是pipeline的起点。当SoT发生变化时，我们重新运行整个pipeline，这会创建新的incarnation。该流程持续发生。因为一些分区底层可能有变更，所以合并了重新生成。因此，新的incarnation可能是由多个 SoT 更改引起的。<br>
<br>Prodspec的新用户必须选择用哪个SoT描述其服务。实际上，绝大多数用户都可以使用非常通用的模式，并且选择一种即刻可用的搭建。对于有更多特定需求的用户来说，我们允许自定义的SoT格式和生成器。<br>
<br>在Shakespeare服务里，用简单的manifest定义哪里运行前端，二进制版本及其大小。这些SoT对于前端及其负载均衡器asset的配置是足够的。数据库schema则很可能来自其他SoT。<br>
<br>我们在版本控制系统里维护大多数SoT，并且作为<a href="http://google-engtools.blogspot.com/2011/08/build-in-cloud-how-build-system-works.html">密封build</a>的一部分执行生成逻辑。在版本控制系统里维护SoT让我们可以观测到发生的变更并且跟踪这些变更。密封build允许可重复性，这是一个有用的工具，有助于保证稳定的配置和更好的可调试性。<br>
<br>生成器将SoT转化为asset。一些生成器基于其他生成器的输出，而不是SoT，组成一个pipeline。比如，一个生成器通过推断有效负载内容，为每个asset添加一个插件，描述该资产的“物理集群”。<br>
<br>生成器允许任意逻辑，因为将服务模型扩展到生产模型可能很复杂。虽然我们希望避免复杂性，但通过某种形式的模板强制做简化可能没有帮助。相反，我们选择接受这种复杂性：将创建服务配置视为与技术栈中任何其他过程一样的过程，因此值得使用常规的编程语言。不再依赖于模版或者配置语言，而是从转化中分离数据（配置）。<br>
<br>使用SoT，大多数用户只需要重用常见的生成器，仅仅有特殊需求的用户需要维护自定义的生成器。<br>
<br>Shakespeare服务的生成器会为manifest里列出的每个集群创建两个asset：一个针对job，一个针对本地负载均衡器配置。<br>
<br><strong><em>验证</em></strong>：我们通过一系列广泛的验证器运行每个生成的incarnation。大多数验证器会验证incarnation的一致性，而有些验证器则使用外部数据库交叉检查内容。准备一系列的验证器是极其重要的——损坏是非常常见的配置问题，验证器可以有效地检测损坏并防止错误配置进入生产环境。在添加新的asset类型或插件时，我们几乎总会同时添加多个验证器。<br>
<br><strong><em>存储</em></strong>：一旦验证了某个incarnation，结果就会存储到Spanner里。虽然特定的incarnation很少使用很长时间，但是在事后保留结果以辅助问题的调试是很有价值的。<br>
<strong><em>服务</em></strong>：通过查询服务器访问存储的incarnation。消费者可以请求最新的incarnation，特定的incarnation，或者其他的。它们还可以过滤出想看到的asset，这在处理有上千个asset的incarnation时很有用。我们使用Spanner索引来快速过滤数据。过滤语言不是那么精准的：它的目标是减少需要处理的数据量。更为复杂的索引在客户端执行。<br>
<br><h3>安全的持续部署：Annealing</h3>我们创建Annealing来驱动持续部署。一旦在Prodspec里声明intent，就是想要生产环境匹配这个intent。更新intent通常涉及手动工作和审批，但是在这之后，自动化应该能够代替人工干预。Annealing就起的这个作用。<br>
<br>持续实施的目标是让生产环境安全快速地匹配intent。Annealing逐渐变更应用——比如，通过管理金丝雀部署或者受控的滚动升级。这个工具支持应用多个安全策略：因为Annealing可以看到应用的所有变更，它可以决定哪些变化是安全的，并且什么时候应用这些变更。考虑限速这个场景：Annealing可以限制某个job的变更数量，即使有多个流程或者人在同步和该job交互。<br>
<br>作为规则，我们想在reconcil生产环境的时候避免人工审批，因为在我们的经验里，这类人工干预很少带来有用的东西。我们仍然允许人工审核特定重要的变更（比如，数据删除），以及所有标准的自动检查。我们将这些事件保持在最低限度，以避免人工批准者的脱敏。<br>
<br>Annealing负责所有基础架构的配置，从二进制文件版本更新到定额管理，数据库schema或者负载均衡器的配置。多年来，我们发现基础架构始终比预期的更为动态——比如，执行集群的"一次性设置"的次数，可能比启动测试实例的次数更多。因此，我们鼓励用户将生产环境的所有方面编码到Prodspec中，并通过Annealing来强制执行它们。虽然这种方法最初成本很高，但很快就能得到回报。<br>
<br>我们还发现Prodspec的扩展建模特别有助于turnup。turnup的传统方案是文档和自定义工作流。这些工作流会不可避免地出错，因此使用它们需要很多人工处理。广泛持续的执行在很大程度上消除了这个问题。由于服务的所有基础架构方面都是被持续评估的，因此问题会立即出现，而不仅仅是在下次执行turnup工作流时才被发现。<br>
<br>持续执行由这两层驱动：<br>
<ul><li><strong>执行层</strong>，由Enforcer驱动，推动Prodspec的intent变更到生产环境</li><li><strong>策略层</strong>，由Strategist驱动，通过变更intent来计划执行</li></ul><br>
<br>如果可能，我们更喜欢在 Enforcer 级别表达执行逻辑和约束，这是无状态层，更容易理解和操作。但是，这种方法并不总是可行或可取的 —— 比如，对新的二进制版本进行为期一周的仔细部署可能需要慢慢更新intent。<br>
<h4>Enforcement（执行）</h4>Enforer负责acutation的最后一公里。如图8所示，Enforcer跟踪intent，并且调用插件来更新生产环境的状态。Enforcer对intent没有控制：它唯一做的决策是现在能否推送特定的asset还是需要推迟。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/04ffdaa5080fffc4b4065dd1a7d2c6fd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/04ffdaa5080fffc4b4065dd1a7d2c6fd.jpg" class="img-polaroid" title="08.jpg" alt="08.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图8：Enforcer及其插件</em><br>
<br>所有和基础架构的交互都是通过插件完成的，因为Enforcer不会直接接触或者查看生产系统。这让任意用户都可以添加更多的集成点，这是很有用的，因为服务通常都有一些特殊需求，比如自定义配置或者API。插件方案也有助于部署：不用滚动升级一个单体应用二进制，而是升级很多个小的二进制文件，每个都有自己的生命周期。<br>
<br>当enforcer调用某个插件时，它仅仅提供incarnation ID以及需要操作的asset ID。插件在需要时从Prodspec处得到更多的信息。<br>
<br>Annealing有两种主要的插件类型：<br>
<ul><li><br>asset插件管理Annealing和给定类型的asset的生产环境的交互。asset插件实现两个方法：<br>
<ul><li>Diff，来决定给定incarnation是否匹配生产环境。这是获得intent信息或者生产环境状态的唯一机制。</li><li>Push，来更新生产环境，使用intent里指定的配置。</li></ul></li><li><br>check插件来决定能否在现在推送某个asset还是需要延迟。对于要推送的asset的所有检查都必须通过。</li></ul><br>
<br>在Shakespeare服务里，所有asset类型都需要asset插件：Borg job，负载均衡器资源以及Spanner数据schema。我们还需要检查check插件来避免周末的推送。<br>
<br>Annealing插件和Kubernetes控制器在有些方面很类似，它们都抽象了操作生产环境特殊方面的逻辑。但是，实现上这两有所不同：<br>
<ul><li>Kubernetes控制器监控资源的变化。Annealing插件除非被显式调用否则什么也不做。</li><li>Annealing插件更细粒度。一个Kubernetes控制器可能会检查某个操作是否需要（asset插件diff），验证现在是否可以推送这个变更（check插件），以及执行变更（asset插件push）。</li></ul><br>
<br>Enforcer独立处理每个asset。最初，我们在决策之前都会尝试评估所有asset，但是遇到了可扩展性的问题。<br>
<br>如图9所示，Enforcer按照如下步骤为每个asset运行着一个永久的循环：<br>
<ul><li>Pinning：决定使用哪个incarnation作为intent</li><li>Diff：如果intent和生产环境没有不同，循环结束</li><li>Check：当需要推送时，验证现在是否可以推送，如果不能，循环结束</li><li>Push：基于intent变更基础架构</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/38c7ee6e88ebb68cfd40d980d0903aa2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/38c7ee6e88ebb68cfd40d980d0903aa2.jpg" class="img-polaroid" title="09.jpg" alt="09.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图9：Enforcer的asset循环</em><br>
<br>这个循环不会一个接一个地检查每个incarnation，并且不保证每个incarnation都被执行，每个迭代使用最新的incarnation。该方案可以避免卡在受损的incarnation里。相反，有机会可以修复intent，这是自动的。因此，如果某个特定的中间状态必须在生产环境中反映，则必须等待强制实施了该状态，之后才能再进一步更新intent。<br>
<br>每个asset都是独立的，并且循环对于每个asset来说是独立运行的。但是，我们不会随意推送asset——这是检查的基础。我们使用检查来延迟（而不是拒绝）对生产的更改。<br>
<br>Annealing可以洞察并且控制它执行的整个服务。这让Annealing拥有独特的中央视角，允许检查在整个生产过程中轻松实施不变量。这让检查在概念上通常很简单，但功能很强大。比如：<br>
<ul><li>日历检查避免在周末或者节假日推送</li><li>监控检查验证当前没有警报，或者系统现在没有过载</li><li>容量检查会阻止将服务容量降低到最近最大使用率之下的推送</li><li>依赖解决器对并发更改进行排序，以确保正确的执行顺序。</li></ul><br>
<br>依赖解决器是我们介绍的第一个check。它确保以正确的顺序推送asset。想一想图6的Shakespeare服务：当减少某个集群的占用空间时，通常需要更新负载均衡器的配置，以减少该群集提供的最大容量，然后再减少前端的副本数量——这样，你不会遇到前端无法承担发送给它的负载的情况。解决器check让你可以在一次变更中同时更新负载均衡器和前端的容量，而Annealing会以安全的顺序推送这些变更。依赖解决器check使用如下逻辑：<br>
<ol><li>发送推送asset A的请求</li><li>Enforcer调用check插件，包括解决器</li><li>解决器检查asset A的diff。如果diff认为这个变更不会影响容量，那么check通过。</li><li>如果check发现容量的变化，解决器查询该asset的依赖。这些依赖显式地列在带有插件的Prodspec里，通常在Prodspec生成pipeline里自动生成。</li><li>解决器请求为每个依赖B做生产环境diff。</li><li>如果asset B的diff表示需要在asset A推送后变更容量才能保证服务运行正常，那么A的推送会被阻止，直到asset B的diff消失。否则，asset A可以被处理以及推送。</li></ol><br>
<br>虽然决定推送是否可以进行的实际逻辑可能很复杂，但是这种模式很通用——比如，你可以定制解决器执行静态顺序（“在推送asset B前总是先推送asset A”）或者版本式顺序（“运行的asset A的版本必须和asset B的一样或者更大”）。<br>
<h4>渐进式推出</h4>Enforcer只关心最后一公里：一旦它决定了给定asset的特定intent，Enforcer检查执行该变更是否安全，然后就执行这个变更。<br>
<br>但是如果我们想要在大规模下渐进式部署呢？假定Shakespeare服务在10个集群，而不是一个集群上运行。你不会希望一次只能更新一个单独的集群。相反，你想设置新的目标状态（比如，运行二进制文件的v2版本），随后能以受控的方式更新每个asset。<br>
<br>名为Strategist的服务器通过持续运行如下三个步骤来执行渐进式推出，如图10所示：<br>
<ul><li>Select：基于推出决策和check，决定在上线的这个点可以变更哪些asset。需要挑选一个特殊的集群吗？现在能否更新不止一个asset？</li><li>Update：为所选的asset改变生产环境的状态到新状态。</li><li>Validate：决定变更是否是好的。如果不是，推出应该在这里停止，可能还需要回滚。</li><li>Strategist持续运行这三个步骤，直到受推出影响的所有asset都已经被更新，或者遇到了什么问题。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/9f0e34e2e3b3e9b0db1c82bc4956fcc1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/9f0e34e2e3b3e9b0db1c82bc4956fcc1.jpg" class="img-polaroid" title="010.jpg" alt="010.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图10：Select-Update-Validate循环</em><br>
<h4>Select</h4>Select这一步的目标是找到现在就可以更新的asset。如果没有assest准备好推送，这一步可以不返回任何东西。通常，推出策略是在这里编码的——比如，一个策略指定应首先推送金丝雀部署，然后是一段时间的延迟，然后增量到生产环境的其余部分，每个步骤之间还有一些进一步的延迟。<br>
<br>select步骤是通过名为Target Selection的无状态服务来实现的。这个服务提供了一个RPC方法：<br>
<ul><li>输入是上线的asset列表和哪些asset已经更新的信息</li><li>输出是还没有更新，但是已经准备更新的asset列表。这个列表通常是空的——比如，因为推出阶段中间配置了一些延迟。</li></ul><br>
<br>Target Selection通过Prodspec配置，并且实现如下策略：<br>
<ul><li>一次性推送所有东西</li><li>以预先定义好的顺序，一次推送一个集群</li><li>推送一个asset，随后所有其他asset</li></ul><br>
<br>我们发现，即使在单次推出的时间范围内，也需要能够应对不断变化的环境。比如，如果推出持续两周并影响数百个asset，则在推出过程中可能会添加和删除某些asset。推出政策本身可能会发生变化——无论是有机的还是由于外部约束。比如，关键问题可能需要快速推出才能部署某个缓解措施。在这些情况下，Target Selection的无状态化就很有用。由于Target Selection只关心更新和未更新的内容，因此它可以处理动态环境。<br>
<br><h4>Update</h4>一旦选中了需要更新的asset，Enforcer将驱动实际生产环境的变更。有两种基本方法来驱动变更：<br>
<ul><li>基于actuation的更新小心地推送intent。intent表示所有asset的最终预期状态。更新步骤触发选中的asset的执行，而其他asset不会被执行。</li><li>基于intent的更新小心的改变intent。intent表示递增的预期状态。更新步骤为选中的asset更新SoT；所有asset会在后台持续快速地执行。</li></ul><br>
<br>在其他系统里也可以发现这两种解决方案。每个方案都有一些不同的权衡，我们使用了两种。<br>
<br>如图11所示，基于actuation的推出是由SoT的变化立即改变所有asset的intent。随后生成新的Prodspec的incarnation。但是Enforcer持续使用之前的incarnation，因此生产环境没有被更新。之后，因为有asset被选出来更新，Enforcer被要求使用新的incarnation。<br>
<br>在Shakespeare服务里，这意味着单一版本被用来配置所有集群的前端二进制文件，之后每个集群仅在需要的时候被推送。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/1eae487be54d72ed0849a025df4f8e43.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/1eae487be54d72ed0849a025df4f8e43.jpg" class="img-polaroid" title="011.jpg" alt="011.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图11：基于actuation的推出</em><br>
<br>这个方案的优势就是很简单：我们只是控制沿着incarnation前进的速度。它是一个包罗万象的机制：对SoT的具体更改并不重要，因为在实践中，我们仔细地推出了整个incarnation的内容。<br>
<br>但是，这个方案缺少灵活性。考虑这样的场景：多个正在进行的推出改变了相同的asset——比如，为期一周的新标志与每日版本更新并行推出。这个用例无法通过纯粹的基于actuation的推出来管理。在实践中，需要对更改进行批处理。<br>
<br>如图12所示，基于intent的推出仅仅在特定asset选中后才会更新asset的intent。随后intent立即通过Enforcer被执行。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220406/a66b493740b166b3cc014cf5711d660c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220406/a66b493740b166b3cc014cf5711d660c.jpg" class="img-polaroid" title="012.jpg" alt="012.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图12：基于intent的推出</em><br>
<br>基于intent的推出比基于acutation的推出复杂很多。它们要求能够程序化地改变intent的能力。在Prodsepc模型里，这个需求意味着依赖于可以以编程方式编辑的SoT。SoT还应允许足够的粒度来匹配asset的选择方式。<br>
<br>在Shakespeare服务里使用这个模型，需要SoT来独立指定每个集群的前端二进制版本。<br>
<br>基于intent的推出允许推出影响并行运行的相同asset——这在基于actuation的推出中是不可能的。唯一的约束是这些推出必须修改asset的不同方面——比如，一个推出可能会更改二进制版本，而另一个推出可能会更新标志。<br>
<h3>验证</h3>启动更新后，Annealing将评估影响，以确定推出是否可以继续，或者是否应停止甚至回滚。此步骤是自动的——我们不鼓励早期阶段之后手动验证推送。<br>
<br>会在两个层面检查推出中的服务健康状态：<br>
<ul><li>Enforcer级别：一些Annealing插件有内置的asset特定的健康检查。如果有问题发生，推送被标记为失败。</li><li>Strategist级别：当选择并且更新一些asset之后，我们会验证服务的健康。我们经常引入各种等待时间，以考虑诸如服务器在推送后稳定等因素。</li></ul><br>
<br>健康检查可以包括验证运行状况，而不仅仅是更新的资产。在 Shakespeare 服务中，这可能意味着在更新数据库schema后验证前端job的运行状况。<br>
<br>我们在更新后监控数据来验证系统健康状态。有两种广泛使用的验证方法：<br>
<ul><li>绝对值：把监控和配置的值做比较——比如，是否触发了警报，或者错误率是否高于2%。只要能确定baseline，这个方案是很稳健的。</li><li>统计法：把监控和过去的值或者和受控的asset做比较。虽然这种方法往往更不精准，但它几乎不需要配置，并且可以跨许多指标工作。它还可以捕获超出服务维护者设想的故障模式的异常。</li></ul><br>
<br>自动健康评估是一个广泛而复杂的主题，多年来我们学习和调整了许多微妙之处，这不在本文的讨论范围。<br>
<h4>和工作流集成</h4>使用Prodspec和Annealing的目标是将更多的生产环境管理切换到intent驱动的模型上。理论上，可以通过intent的使用管理所有生产环境变更。但是，我们显然并不想把所有生产环境都转化为intent驱动的模型。在一些情况下，传统的工作流更有用。<br>
<br>什么时候使用基于intent的actuation，什么时候使用传统工作流，这之间并没有清晰的界限，但是有一些通用的考虑准则：<br>
<ul><li><strong>系统大小</strong>：在同时发生很多变更的时候，基于intent的acutation很有用，因为可以以更直观的方式对规则进行编码。对于低并发性的小型系统，工作流往往更容易理解。</li><li><strong>思维模型</strong>：是否有理由关心确切的详细步骤并希望能够对其进行微调，或者只需要保证正确的事情会发生，因为它是基础架构的细节？后者要求intent；前者需要工作流。</li><li><strong>复杂度</strong>：变更是否要求一些特殊步骤——比如，批处理job的一次性运行，一些用户输入等？如果是这样，工作流可能更合适。你是否更在意一致性而不是更好的调优？Intent这时候更好。</li></ul><br>
<br>直接的后果是基于intent的执行和基于工作流的执行必须总是能够相互集成。我们使用两种集成机制。<br>
<br>第一种机制通过改变SoT的内容让高层级工作流驱动intent的更新。比如，服务器二进制的创建大部分由工作流驱动，随后Annealing和Prodspec部署这些二进制文件。<br>
<br>另一种机制是在技术栈的另一端：可以使用工作流引擎实现Annealing插件Push操作。比如，我们使用这个模型来更新网络交换机的firmware：专有的工作流系统实现许多自定义逻辑，然后Annealing自行启动工作流。<br>
<br>不管使用哪种模型，都需要确保：<br>
<ul><li>生产环境的给定部分只由一个自动化系统负责。比如，常见的请求是一个系统负责turnup，另一个系统负责正在进行的更新。我们的经验表明，这种做法会带来许多同步问题，尤其是在更复杂的asset上。</li><li>状态的保持要最小化：你应该依赖生产环境的状态以及预期的最终状态。生产状态的发展原因往往比预期的要多，而且保持的状态越多，自动化就越有可能做出错误的选择。我们经常试图通过存储额外的状态来简化某些插件或工作流程的设计，但这样做通常会使系统更加脆弱和难以调试。这不是一个硬性规定——有时保持额外的状态确实有意义，但确定何时这是正确的选择可能很困难。</li></ul><br>
<br><h3>控制平面的优势</h3>Prodspec和Annealing作为服务配置和基础架构之间的控制平面存在。这种中央化控制平面的最明显的优势是管理生产的方式是一致的，但也有其他好处。<br>
<br>Prodspec给对给定服务模型有兴趣的多种工具提供结构化的精准信息。工具负责监控，分析以及审计，甚至一次性脚本可以访问相同的权威数据。<br>
<br>中央化控制平面还让我们可以封装最佳实践。在配置层，可以很容易地侦测某个服务是不是配置恰当，甚至可以在多个基础架构之上。这大大减少了运行时的意外情况，因为你不会姗姗来迟地发现为了支持前端，需要配置某些关键的基础架构。<br>
<br>acutation和执行层的最佳实践也得益于Annealing。在工作流模型里，通常需要为服务裁剪每个工作流。Annealing的持续执行模型让我们可以指定工作流之间的共性。我们可以使用插件将用于驱动推送的通用逻辑从actuation的粒度细节中分离出来。比如，check插件可以自动确保以正确的顺序调整前端和后端的大小，而不是要求每个工作流实现自己的逻辑。<br>
<br>统一的控制平面还为基础架构提供者提供支持。在许多情况下，提供者可以通过简单地更新相应的Annealing插件来更改某些行为或增加额外的安全性，而不是与许多单独的客户打交道，这些客户各自使用不同的机制来配置其服务。<br>
<br>统一的控制平面还提供了跨asset类型的安全性。Annealing之前的工作流通常只关注一种类型——比如，使用一个工作流来更新二进制文件，一个工作流来更新数据库schema，这使得同步变得困难。通过Annealing，我们可以在插件中编码保证和安全，特别是在check插件中。check插件可以验证数据库schema的版本是否兼容运行着的job版本，而无论多个推送和回滚之间都发生了什么。<br>
<br>最终，Prodspec和Annealing让我们可以可靠地自动化——或者至少流水线化——复杂的流程，比如重新放置服务。之前使用的自定义工作流更多地依赖人工而不是自动化来检测问题。相反，控制平面做如下事情：<br>
<ul><li>完全建模服务：不再需要猜测依赖或者其他应该考虑的方面</li><li>生成配置：不再需要编辑多个异构的配置文件</li><li>推送变更，并且确保系统正在使用持续化执行。</li><li>使用安全检查确保操作都是安全的并且顺序是正确的。</li></ul><br>
<br><h4>经验教训</h4>转向基于intent的生产管理以来的这几年里，我们学到了很多关于什么有效和什么无效的知识。以下是其中的一些经验教训。<br>
<h3>执行</h3>具有某种形式的持续执行是基于intent的配置的基础。 简单地对intent进行建模会导致信息的过时和缺失。我们已经在仅为管理turnup而创建的工作流中看到了此问题，这些工作流有在需要时中断的记录，并且需要大量精力来修复工作流，而不是手动执行turnup。持续执行保证当变更影响intent时intent是正确的或者能够快速修复。这反过来又鼓励人们通过更新intent来管理他们的生产环境，并让许多其他工具从intent中获得输入。这些行为强化了intent的质量，带来了良性循环。<br>
<br>早期的一个实现错误是让Enforcer分批工作。它首先比较分区的所有asset，然后触发已准备就绪的更改的推送。只有当推送完成后，另一波才能开始。该模型易于掌握和调试。比如，与目前的实现相比，集中式决策（例如依赖关系求解器）要简单得多。然而，它的速度慢得令人难以忍受。我们希望推送最多在几分钟内开始。在Enforcer的早期实施中，长时间的推送使其他更改延迟了数小时。<br>
<h3>建模</h3>并非生产环境的所有东西都适用于intent模型。数据pipeline和批处理job就是这样的例子。比如，可以构造一个代表批处理job的intent——asset可以表示“这个job必须在过去24小时运行至少一次”——当约束条件不再有效时，插件负责启动job。但是，这种设置有点尴尬，我们尚未探索通过Prodspec和Annealing对数据pipeline和批处理job的适当支持。<br>
<br>管理turndown时间（从生产环境中移除一些基础设施）也很棘手。我们的许多用户都要求"因缺失而关闭"，即让系统将从Prodspec中消失的asset视为必须删除相应基础设施的隐含信号。这种方法在某些有限的情况下是可以的，但我们通常不会支持它，因为它给整个生产环境带来了太大的风险。配置系统里更为常见的故障模式是返回部分内容——比如，如果在分析的中间发生了错误，系统仅仅发送了一半配置。这时，“因缺失而关闭”会对生产造成严重破坏：想象一下，自动化错误地删除了数据库！<br>
<br>为了处理turndown，我们要求在实现代码下架给定asset类型之前要有额外的安全保证。然后，我们要求turndown的显式信号：asset上turndown的额外插件。虽然这个方案不完美——管理插件有点麻烦——但它避免了大量意外的turndown。<br>
<h3>使用</h3>使用Prodspec和Annealing的难度是我们面临的最大挑战。切换到基于intent的actuation要求思想的改变，这需要时间。随着我们发展到现在，使用不是一个问题，至少在技术栈的较低层。但是，现有服务的初始建模可能很困难。这项工作通常需要调整复杂的SoT，它们可能还不包含所有必要的信息。一些生产过程可能需要适应，以便转向基于intent的actuation。比如，如果需要在日常维护期间手动将警报静音，则可能需要使该警报更为精确，以便下次不必将其静音。<br>
<br>我们发现拆分onboarding过程会有所帮助。服务很少直接使用 Prodspec和Annealing。相反，他们使用集成器，这些集成器为特定的服务原型提供服务模型。这些集成器通常处理多种类型的asset和基础架构。比如，一个集成器帮助pipeline配置临时存储、发出通知、在需要时运行计算等。这种方法允许服务通过与其用例匹配的模型轻松配置其基础结构。然后，这些集成器提供必要的逻辑来生成Prodspec，从而使Annealing能够管理服务生产。<br>
<br>“看不见的决定”是使用的另一个挑战。我们观察到的一个常见模式是，建立在持续执行基础上的系统与人类处理异常情况的系统之间的需求存在未被承认的差距。即使在计划转向Annealing时，也很容易丢失运维人员手动执行的许多决策。虽然有时这种差距不是问题，但当难以自动执行直观的手动步骤时，它可能会成为一个障碍。重试失败的推送是不可见决策的典型示例。工作流系统很少自动重新运行特定步骤，通常会人工处理重试——估计失败的推送是否是暂时的，以及重新尝试推送是否合理。持续执行可能比人工更正确。但是，持续执行也会使这些决策更为频繁，并且可能更难调试。这意味着，为了获得良好的最终用户体验，自动化必须比人工好一个数量级。<br>
<h3>下一步</h3>如今，基于intent的配置和持续执行现在已经在Google里被广泛接受和使用。随着我们从挑战和成功中不断进步，基于intent的actuation的方案也在持续演进。<br>
<br>在迁移到此类系统时，了解基于intent的actuation和持续执行的目标的局限性非常重要。所包含的内容的边界不是固定的，我们一直在探索这个限制。一般来说，随着人们对这些概念越来越熟悉，基于intent和持续执行的生产环境会随之增长，但这个过程既不是即时的，也不是简单的。<br>
<br>在我们的例子中，在几天和几周内为大型部署推动更长的推出仍然是大量迭代的领域。我们的建模还不能很好地处理这个用例——如何表达应该在多个集群和时间窗口上部署的各种版本的intent？用户（尚未）对这种级别的持续执行感到满意，并且仍然密切关注特定版本等方面。我们正在探索这个领域的各种选择，包括放宽对高层次intent的持续执行。<br>
<br>我们还在投资提高可调试性。与传统工作流程相比，基于intent的生产管理在这一领域本质上是不利的。用户只有在出现问题时才会查看系统，并且通常没有一个好的调查起点。我们正在努力更好地表示系统的状态，以及为什么以及如何做出决定，以便在出现问题时改善内省。<br>
<br><strong>原文链接：<a href="https://www.usenix.org/publications/loginonline/prodspec-and-annealing-intent-based-actuation-google-production">Prodspec and Annealing</a>（翻译：崔婧雯）</strong><br>
<br>＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br><br>
译者介绍<br><br>
崔婧雯，现就职于IBM，高级软件工程师，负责IBM WebSphere业务流程管理软件的系统测试工作。曾就职于VMware从事桌面虚拟化产品的质量保证工作。对虚拟化，中间件技术，业务流程管理有浓厚的兴趣。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            