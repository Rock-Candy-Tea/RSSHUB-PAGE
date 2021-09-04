
---
title: '如何基于DDD构建微服务架构'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/def3c5c310b8d2bf7f93182e2bc23c09.jpg'
author: Dockone
comments: false
date: 2021-09-04 02:22:12
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/def3c5c310b8d2bf7f93182e2bc23c09.jpg'
---

<div>   
<br>微服务构建本质上是软件构建过程中长期演进积累的一系列理念、架构原则、工具和最佳实践。<br>
<br><strong>领域驱动设计的软件思想体系和方法论</strong>可以用于指导微服务建模、微服务划分、微服务架构设计等相关工作，它可以促使技术人员与领域专家达成共识，构建领域边界合理、具备明确界限上下文、关注点分离、独立自治的微服务。<br>
<h3>领域驱动设计概述</h3><strong>领域驱动设计</strong>（Domain Driven Design）概念的兴起可以追溯到1986年，《人月神话》的作者Brooks提出软件的本质复杂性（Essential Complexity）存在于复杂的业务领域中，技术仅仅是辅助工具，它解决的问题是帮助业务领域从现实问题映射转换成软件实现。  <br>
<br>领域驱动设计在战略设计层面，从业务视角出发使技术人员专注于问题域，从领域专家那里获得领域见解，通过模块划分建立领域服务边界，通过界限上下文明确服务的职责。<br>
<br>领域驱动设计在战术设计层面，从技术的视角出发，提炼有效的业务模型，实施领域建模、架构设计完成软件的落地。<br>
<br>领域驱动设计通过隔离业务与技术的复杂性，成为程式化、标准化的软件架构设计范式。<br>
<h4>软件复杂度的来源</h4><ul><li><strong>业务的复杂性</strong>：业务的复杂性体现在业务流程不清晰、业务参与人员多、业务与技术耦合等方面。在业务的早期阶段，为了快速满足功能需求容易形成面条式的代码风格，这样的代码风格会导致软件模块膨胀、开发效率降低、功能扩展步伐放缓、业务模型与代码脱节等。</li><li><strong>技术的复杂性</strong>：技术的复杂性来源于对项目的质量属性需求，诸如系统的性能、客户体验、服务高可用性等。为解决服务的响应延迟、吞吐、安全等问题，我们会引入缓存、消息队列、第三方模块组件，而这些技术的整合给系统引入了额外的复杂性和技术挑战。</li></ul><br>
<br>质量属性需求：系统非功能（也叫非行为）部分的需求。<br>
<h4>领域驱动解决之道</h4>解决这种软件构建中面临的复杂性问题，我们需要从领域开始着手，与业务专家一起获得领域见解，促使软件利益干系方在领域内建立通用语言。技术人员通过建模的手段提炼出事物的本质，以便更好地指导应用系统的构建和规划。<br>
<br>领域驱动设计中包含了大量成熟的理论、概念、模式和架构，它包含一套解决复杂领域模型的软件架构方法，思想是围绕业务模型来连接和实现核心业务概念。<br>
<br>领域驱动设计可以让业务和技术的变化产生的不可预知因素互相分离，将人员变动、团队规模、协作沟通等外界因素变化对产品和项目的影响封装在一个可控的容器和框架下，从而解决软件面临的复杂性问题，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/def3c5c310b8d2bf7f93182e2bc23c09.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/def3c5c310b8d2bf7f93182e2bc23c09.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>事务脚本模式与领域建模模式</h4><ul><li><strong>事务脚本模式</strong>：事物脚本模式常见于单体应用中，它将所有逻辑全部组织在一个单一过程方法中，从数据库的调用到不同业务逻辑、策略的执行全部集成在一个大的方法块中。它的好处是简单、容易实现，它的缺点是没有自己的状态，也无法扩展，容易将服务组件与数据存储模型之间的刚性依赖引入业务逻辑中。</li><li><strong>领域建模模式</strong>：领域建模模式将业务逻辑转移到了领域对象（Domain Object）中，每个领域对象完成属于自己的业务行为。同时数据存储层的逻辑也变得相对简单，数据库不再参与领域模型的业务逻辑，而是回归数据“持久化”的本质。</li></ul><br>
<br>使用领域模式可以提升系统的内聚性和可重用性，通过不同类之间的协同完成所有功能。另外，多态的模式也让扩展新的策略更加方便，业务语义更加通用、显性化。领域建模过程遵循“SOLID”原则并实现业务域的逻辑解决方案。<br>
<br><blockquote><br>说明：<br>
  SOLID原则：<br>
  <ol><li>Single Responsibility Principle：单一职责原则</li><li>Open Closed Principle：开闭原则</li><li>Liskov Substitution Principle：里氏替换原则</li><li>Interface Segregation Principle：接口隔离原则</li><li>Dependence Inversion Principle：依赖倒置原则</li></ol></blockquote><h4>领域驱动设计核心要素</h4>如下图所示是领域驱动设计的核心要素，包含领域驱动设计中的通用模型术语和重要的战术模式。这些模式不仅可以捕获和传递领域中的概念、关系及逻辑，也能帮助我们管理业务的复杂性并确保领域模型的行为清晰明确。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/d90cfed7f88d6c5c76bb530484e6006e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/d90cfed7f88d6c5c76bb530484e6006e.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>领域</strong>：相对于软件系统来说就是系统要解决的现实问题。</li><li><strong>子域</strong>：对于领域进行不同维度切分的相对内聚的子系统单元。</li><li><strong>分层架构</strong>：通过分层架构将业务域和技术逻辑域隔离。</li><li><strong>服务</strong>：服务通常是领域对象的调用方，用来协调领域对象完成指定业务逻辑职责。</li><li><strong>实体</strong>：实体与面向对象中的概念类似，它是领域模型的基本元素，在领域模型中，实体应该具有唯一的标识符。</li><li><strong>值对象</strong>：值对象是没有唯一标识符的实体。值对象在领域模型中是可以被共享的，它们应该是不可变的，当有其他地方需要用到值对象时，可以将它的副本作为参数传递。</li><li><strong>聚合</strong>：聚合使用边界将内部和外部的对象划分开来。每个聚合有一个根，这个根是一个实体作为外部可以访问的唯一对象。</li><li><strong>资源库</strong>：是封装的所有获取对象引用所需的逻辑单元。</li><li><strong>工厂</strong>：工厂用来封装对象创建所必需的信息，当聚合根建立时，所有聚合包含的对象将随之建立。</li></ul><br>
<br><h3>专注问题域</h3>解决一个业务场景中的复杂问题从理解问题域开始，通过专注于问题域并理解复杂问题背后的实质，你才能设计有效的模型来应对业务的挑战。<br>
<br>在项目初期，尽量避免沉溺于技术实现，而要把焦点集中在问题领域，不要忘记技术服务业务的原则。<br><br>
<h4>理解问题域</h4>我们以一个金融场景下的“业务运营监控系统”为例进行分析。经过与运营管理专家和相关业务方的多轮需求探论，我们初步了解了用户的业务诉求和痛点。需要强调的是对于问题域的充分理解是我们的首要任务。<br>
<br>这里整理了一份需求文档，它详细地记录了问题域的具体范围和详细需求。这份文档不仅是业务与技术团队之间的一份沟通文档，也可以作为软件生命周期在需求分析阶段的一个清晰的、规范化的知识协作产物。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/287ba298d5d2caf475dce7e9c325119a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/287ba298d5d2caf475dce7e9c325119a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>提炼问题域</h4>理解复杂问题并从中识别、提炼出关键的业务模型，即提炼问题域是领域驱动设计的关键环节。团队可以通过头脑风暴的形式罗列出领域中的所有事件，整合之后形成最终的领域事件集合。<br>
<br>你需要在关键事件标记的范围里，参照不同利益干系方的业务诉求，组织领域事件和模型，同时，你需要整理出与项目关联的上下游系统，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/73a1f989985f7d1757d9ed0bcc72d0cd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/73a1f989985f7d1757d9ed0bcc72d0cd.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
通过挖掘隐藏在领域事件中的核心领域模型，我们可以找到从问题空间到方案空间的对应映射关系。针对上述业务监控系统案例，“进件存量”和“进件流量”的概念成为我们发现的重要领域模型。<br>
<br><blockquote><ul><li>进件存量：是指在某一指定的时间点，过去生产与积累起来的进件的结存数量。</li><li>进件流量：单位时间内流过某一段管道的进件体积流量。</li></ul></blockquote>作为衡量业务系统运转状态的重要指标，业务的“存量”状态可以表示业务的积压情况，而业务的“流量”状态可以表示业务流转的变化情况。<br>
<br>如下图所示是我们总结的监控系统概要视图，其中实线表示的是城市信贷业务工作流中进件在不同系统的流向，而虚线表示的则是业务的存量、流量在业务监控系统的事件记录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/eae716ea726f0ece6e8cb90dfcbdea68.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/eae716ea726f0ece6e8cb90dfcbdea68.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>服务的拆分</h3>完成问题域的理解和提炼后，我们需要对整体系统做进一步的服务拆分。下图是我们根据业务领域能力对“业务运营监控系统”进行拆分后的子领域服务及模块划分说明。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/2d205a3c99955ead30292c526a692f4e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/2d205a3c99955ead30292c526a692f4e.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
业务事件收集（如下图和表所示）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/99c472af1ab7e22020c92d6d90934f61.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/99c472af1ab7e22020c92d6d90934f61.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/bfbddf23ca920e566aa06ae13478d8eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/bfbddf23ca920e566aa06ae13478d8eb.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
事件过滤聚合（如下图和表所示）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/ca6e76f54689ae59d6eb1907f56fb5c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/ca6e76f54689ae59d6eb1907f56fb5c8.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/a4e097e90877ef2432118e95930f27e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/a4e097e90877ef2432118e95930f27e7.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
规则配置（如下图和表所示）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/ce7813a33b9d93d15975552f07adee99.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/ce7813a33b9d93d15975552f07adee99.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/adefda0f5eaa0651ddc3b69cfb963a9e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/adefda0f5eaa0651ddc3b69cfb963a9e.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
监控查询展示（如下图和表所示）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/8337614ccd1a0f9bd582ed1593035118.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/8337614ccd1a0f9bd582ed1593035118.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/49b1500e4d0befb80baf104b3ccc78d0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/49b1500e4d0befb80baf104b3ccc78d0.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>为什么要做服务拆分</h4><ul><li><strong>降低系统的整体复杂性</strong>：根据业务领域进行合理的服务拆分是一个有效控制系统复杂性的方法。</li><li><strong>提高效率</strong>：服务拆分后，代码模块相互隔离，并发的开发模式可以提升开发人员的效率。</li><li><strong>团队人员各司其职</strong>：拆分的项目可分派给擅长相关方面技术的人员，让团队成员各司其职，降低工作的耦合度。</li><li><strong>共享和自治</strong>：可以通过定义好的服务接口进行服务共享，同时拆分后的服务也更加自治。</li><li><strong>解决依赖问题</strong>：通过服务拆分，可以清晰地了解哪些服务依赖会对业务造成影响，从而准备预案。</li></ul><br>
<br><h4>服务拆分的依据</h4>高内聚、低耦合是服务拆分的主要依据，下面我们列举一些常用的服务拆分策略，了解如何对单体架构进行拆分。<br>
<ul><li><strong>区分服务类型</strong>：工具服务区别于业务服务，它的特点是与业务领域无关，根据其用途可以进一步细分，一般包括的形式有公共工具服务、资源工具服务、包装器服务等。</li><li><strong>根据功能定义划分服务</strong>：领域驱动设计通过分析问题空间和业务逻辑，将应用程序定义为域，域由多个子域组成，每个子域对应于业务的不同功能部分。</li><li><strong>根据技术边界划分服务</strong>：对于产品类型的服务使用技术能力划分服务边界，前后端分离架构就是通过技术栈划分服务边界的典型架构模式。</li></ul><br>
<br><h4>服务拆分范式</h4>通过增加服务实例或者机器来解决服务的容量和可用性问题是常用的可扩展架构解决方案。在《可扩展艺术》一书中提出了系统的可扩展性模型：AKF可扩展立方，可以作为服务拆分的范式。<br>
<br><blockquote><br>AKF可扩展立方：描述从单体应用到分布式可扩展应用的可扩展模型。</blockquote>如下图所示是使用Scale Cube的3D模型实现的一个微服务架构模型，在X轴上通过API网关进行水平扩展，在Y轴上进行单体拆分后的微服务构建，服务之间可以通过REST API进行简单交互，Z轴是数据维度的拆分。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/4673a0bdebf2793925ae967cd5a5730f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/4673a0bdebf2793925ae967cd5a5730f.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>X轴</strong>：服务扩展，通过克隆的方式水平扩展。一般是负载均衡后运行多个应用副本，达到某个服务的高吞吐量和高可用性。</li><li><strong>Y轴</strong>：功能拆分，通过拆分不同的事务进行扩展。微服务对应着Y轴，即将单体应用拆分为微服务应用。</li><li><strong>Z轴</strong>：数据分区，通过分隔相同的事务进行扩展，例如数据库分库分表。</li></ul><br>
<br>总之，服务支持水平扩展以提升容量；对功能的拆分体现在对业务模型的切入和深入理解上；应用数据的划分是微服务的重要原则，如果数据的耦合问题无法解决，那么应用服务的划分还会有代码耦合和级联影响。<br>
<h3>界限上下文</h3>在找到服务边界并把系统拆分后，我们需要使用“界限上下文”的概念明确服务之间的交互共享模型和行为接口，它不仅可以有效地限定领域的职责边界和特性范围，也可以控制问题域的规模，进而以化整为零的方式控制整个系统的复杂性。  <br>
<br>在业务运营监控项目中，存量项模型作为业务过滤聚合服务和存量查询统计服务的共享模型，关系如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/4fb02dbe2b04df1738afc4836272c1c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/4fb02dbe2b04df1738afc4836272c1c7.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
为了实现捕获和统计监控业务运营过程中的不同阶段存量的业务状态，我们将存量项作为上述两个服务上下文的共享模型，但我们不会暴露“过滤聚合服务”中的存量明细、Flow、Stream等模块的实现细节。<br>
<br>作为两个独立的服务主体，它们应该在边界上有明确的界线划分和通信机制。如果服务边界与领域的界限上下文能够保持一致，那么我们已经为高内聚、低耦合的微服务架构实现了关键的一步。<br>
<h3>领域建模</h3>领域建模是领域驱动设计的核心，通过领域模型可以封装对业务的抽象，建立业务概念与领域规则的关系。领域模型更关注的是业务语义的显性表达，而不是具体的数据存储及代码逻辑实现细节，它可以有效地降低业务人员和技术人员之间的沟通成本。<br><br>
<h4>案例分析</h4>回到“业务运营监控系统”中，我们把业务监控的核心诉求聚焦在“业务事件”，以及业务的存量和流量领域模型。<br>
<br>在整理了领域服务的核心模块后，我们可以把业务方关注的组织信息、业务类型信息、业务阶段信息进行进一步领域模型细化，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/9c30efbae3b5f4df76dc4346e7e1e44e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/9c30efbae3b5f4df76dc4346e7e1e44e.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>BizEvent</strong>：业务事件是业务监控的数据源，使用统一的JSON格式记录消息事件，以日志方式封装当前业务系统发生的事件详情。</li><li><strong>Stream</strong>：对应一个端到端的数据流转概念，通常我们会将BizEvent事件发送到Kafka的一个Topic上，通过建立Stream可以在消费端处理指定Topic上的数据流。</li><li><strong>Flow</strong>：Flow对应一个监控业务计算逻辑，存量Flow可以统计对应的存量状态，流量Flow统计当前业务的流量状态。</li><li><strong>Service</strong>：它并非领域对象，表示一个通用的服务层，Service提供业务存量和流量的查询、备份、预警等业务方法。</li><li><strong>Provision</strong>：用户配置前置通用服务，不对应领域对象，主要接收用户的配置请求，并保存为业务规则。</li><li><strong>Rule</strong>：即规则模型，属于核心领域模型，业务方可以通过它灵活地定制关心的业务状态并进行预警、过滤等。</li><li><strong>Detail</strong>：属于业务的中间监控过程详情，属于领域对象，同时包含组织、阶段、业务类型等明细对象属性（Org、Phase、BizType）。</li></ul><br>
<br>使用领域建模的设计方法可以进一步将“业务监控系统”内部的领域服务与领域模型对象关联，显性地表达每个领域模型的具体工作职责及业务行为事件与领域对象之间的上下文映射关系，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/756eaaf3f8d6aca92a55d15bf9e9daa1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/756eaaf3f8d6aca92a55d15bf9e9daa1.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>架构设计</h3>架构设计的本质是管理业务和技术复杂性，使系统易于有序化重构及扩展。高质量的架构一定是高度抽象的、围绕业务的、易于理解的、面向演进的。<br>
<h4>分层架构设计</h4>领域驱动设计遵循“关注点分离”原则，将技术实现逻辑封装在基础设施层；将业务逻辑封装在领域层，尽量使领域层代码与其他层技术细节分割开来；将应用层作为黏合剂，实现前两者的协作；同时UI层可以基于Swagger技术暴露REST API。分层架构如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/7fcfe328b1dc4ac1163afa7517037941.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/7fcfe328b1dc4ac1163afa7517037941.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>六边形（Hexagonal）架构模式</h4>六边形架构模式又称为“端口-适配器”模式，它将系统分为内部和外部。内部代表应用的业务逻辑，外部代表应用的驱动逻辑、基础设施或其他应用。内部以API接口呈现，通过端口和外部系统通信。外部系统需要使用不同的适配器，适配器负责对协议进行转换。应用程序能够以一致的方式与实际运行的设备和数据库相隔离，方便开发和测试，六边形架构模式如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/eab868aaa1c4dded2acd77995438dcc0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/eab868aaa1c4dded2acd77995438dcc0.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>微服务架构模式</h4>微服务架构是强调细粒度、单一职责的架构模式。微服务架构更关注的是系统的非功能需求：质量属性、演进能力、扩展性、观测性、软件交付效率等。微服务使用CQRS（命令/查询职责分离）中的事务脚本模式应对查询场景，而对于复杂的业务逻辑场景，使用领域驱动设计模式。微服务架构模式如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210901/6c91aa0262572b16ec9de947997e57e9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210901/6c91aa0262572b16ec9de947997e57e9.jpg" class="img-polaroid" title="21.jpg" alt="21.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>本文内容摘自《微服务架构深度解析：原理、实践与进阶》一书，经出版社授权转载。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            