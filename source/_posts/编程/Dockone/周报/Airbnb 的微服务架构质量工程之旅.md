
---
title: 'Airbnb 的微服务架构质量工程之旅'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/cab57367262e8e874addeb9103469941.png'
author: Dockone
comments: false
date: 2022-06-26 07:08:12
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/cab57367262e8e874addeb9103469941.png'
---

<div>   
<br>【编者的话】本文通过介绍 Airbnb 在将“纯微服务架构”改造为“Micro macroservices 架构”过程中，所采用的四个实践步骤：1）提供基础设施即代码以提高开发人员的生产力，2）明确所有权并通过工具和可观察性进行改进，3）定义由组织和方法支持的新架构，4）引入一个弃用工作组以加速迁移，并详细阐述了质量工程（Quality Engineering）的增量迭代解决问题方法：1）定义问题，2）找到改进的解决方案，3）使用解决方案，4）提高解决方案采用率，5）处理解决方案的扩展挑战，为我们实践质量工程提供了一个很好的范例。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/cab57367262e8e874addeb9103469941.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/cab57367262e8e874addeb9103469941.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
实现平衡是一个永无止境的开始。<br>
<br>当业务依赖软件质量和速度来生存时，这种平衡就更难维持了。<br>
<br>许多公司都面临着持续快速交付高质量软件的挑战，这些软件通过<a href="https://qeunit.com/blog/quality-engineering-is-about-surviving-the-digital-transformation/">质量工程</a>限制生命周期。<br>
<br>Airbnb 在加速和扩展其价值主张的过程中面临着众多挑战，尤其是其信息系统的发展过程。<br>
<br>本文分享了 Airbnb 在质量工程方面的架构迭代之旅，并附有实用要点。参考文献可在文章末尾找到。<br>
<br><a href="https://qeunit.com/follow">关注 QE 社区</a>以获取来自社区的更多质量工程信息。<br>
<h3>从单体应用到微服务，什么都没改变</h3>Airbnb 和许多软件公司一样，也是由一些积极进取的工程师发起构建最小可行产品以进入他们的市场从而发展起来的。<br>
<br>该产品最初是单仓内的单体架构（在此处访问完整的<a href="https://qeunit.com/blog/airbnbs-monorepo-journey-to-quality-engineering/"> Airbnb 单仓旅程</a>）。 Airbnb 在这种模式下从 2008 年开始发展，其功能由各小团队完成，小团队之间的依赖及其有限。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/54c69723f209240e2e9040afa24f99bd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/54c69723f209240e2e9040afa24f99bd.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
但在 2017 年，这个集中式架构达到了它的极限：<br>
<ul><li>软件变更速度降低</li><li>平行演进面临限制因素</li><li>组件所有权混乱</li></ul><br>
<br>Airbnb 决定采用微服务。<br>
<br>现有的单体应用被拆分为前台和后台（分别是为了速度的<em>Hyperloop</em>和为了稳定性的<em>Treehouse</em>）。 微服务出现在各自仓库中，而专门的服务迁移团队负责组件的转换。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/9f10d16448db68d3c383dc0224f6fa93.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/9f10d16448db68d3c383dc0224f6fa93.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
3 年后的 2020 年，该业务的收入<a href="https://www.statista.com/statistics/1193134/airbnb-revenue-worldwide/">达到 50 亿美元</a>（直到 COVID 爆发）。团队和微服务持续增加。但是，原来的问题又回来了：功能需要由多个服务和不同团队同时开发。<br>
<br>在他们的架构口号“我们不能影响业务增长”的推动下，工程团队跳出原有方式，为这些反复出现的问题寻找可持续的解决方案。<br>
<h3>Airbnb 架构演进的挑战</h3>Airbnb 面临着架构解决方案的挑战，不但要解决现在的问题，同时要支持未来的扩张；这就是质量工程要解决的问题。<br>
<br>Airbnb 采用了增量和迭代过程：<br>
<ol><li>定义问题</li><li>找到改进的解决方案</li><li>使用解决方案</li><li>提高解决方案采用率</li><li>处理解决方案的扩展挑战</li></ol><br>
<br>这种方法能够分离每个问题的关注点，找到结构化的解决方案并在以后扩展它们。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/107f70a6db294b33709c8533a5371372.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/107f70a6db294b33709c8533a5371372.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Airbnb 在采用上述方法过程中实施了以下做法：<br>
<ol><li>提供基础设施即代码以提高开发人员的生产力</li><li>明确所有权并通过工具和可观察性进行改进</li><li>定义由组织和方法支持的新架构</li><li>引入一个弃用工作组以加速迁移</li></ol><br>
<br>让我们看看前述问题是如何解决的。<br>
<h3>1. 提供基础设施即代码以提高开发人员的生产力</h3>当业务变革能力依赖于软件时，缓慢和错误的软件开发直接影响公司的竞争力。<br>
<br>凭借在微服务架构方面的经验，Airbnb 投资了自动化和工具化。但在一系列不断发展的技术中需要更快的迭代周期。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/9ac6b32ebd4b3870dde84c8d391f6aed.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/9ac6b32ebd4b3870dde84c8d391f6aed.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
务实的解决方案是在单个仓库中投资基础设施即代码，从而逐步并行提升各个服务的采用率。<br>
<br>当运行更多服务时，就会出现理解这种复杂性的扩展挑战。<br>
<h3>2. 明确所有权并通过工具和可观察性进行改进</h3>有太多的微服务相互捆绑；即使很小的变化也会导致相互依赖的变化和影响，掌握起来很复杂。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/ca744bdfae9020cc0ac4dd4d97dbf959.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/ca744bdfae9020cc0ac4dd4d97dbf959.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Airbnb 投资于提高生产力，重点支持三个领域的新架构：<br>
<h4>所有权</h4>Airbnb 部署了“Scry Ownership”，它是技术组件所有权数据（如所有者、维护者、通信渠道）的应用管理者。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/72f8ebf61f52044a984e3d5973d15151.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/72f8ebf61f52044a984e3d5973d15151.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>可观察性</h4>Airbnb  设置了一系列可观察性仪表板，以系统地审查实施过程。 下面是一个仪表板示例，用于跟踪正在设置的所有权：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/93dbf464b64795b5e3099d6c95fb0662.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/93dbf464b64795b5e3099d6c95fb0662.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>工具</h4>数据空间仍然存在挑战。定制的 <a href="https://thrift.apache.org/">Thrift</a> 模式是有用的序列化器和数据描述符，但它们需要其他组件来检索产品中的数据。<br>
<br>Airbnb 利用 GraphQL 构建了统一的数据访问层，直接提供查询能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/a23a762bc24ee29848789d8e97ee29b9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/a23a762bc24ee29848789d8e97ee29b9.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
代码生成是提高开发人员生产力的最后一步。 随着技术的增加，Airbnb 为每一层的标准组件提供了模板。<br>
<br>通过设计指明数据类型和访问类型的代码注释，数据的访问甚至直接就被嵌入在了代码中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/8370ebc27e3c66f3ecf771e9a9554d00.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/8370ebc27e3c66f3ecf771e9a9554d00.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当星号看起来对齐时，就会出现另一个速度问题。 这一次，中央数据聚合器组件成为了限制因素。<br>
<h3>3. 定义由组织和方法支持的新架构</h3>中央数据聚合器的构建和部署时间太慢，团队无法按时迭代。<br>
<br>即使提高了生产力，累积的结构复杂性仍然太高而无法在中央组件中处理。需要一个新的组织。<br>
<br>熵是系统随着时间的推移变得更加复杂的自然趋势，需要支持和反作用力来平衡生态系统。<br>
<br>质量工程力量在架构、组织和<a href="https://qeunit.com/blog/this-is-why-you-need-methods-for-quality-at-speed/">方法</a>领域发挥作用。<br>
<h4>支持增长的架构</h4>太复杂了；团队必须对不同领域执行缓慢且成本高昂的影响分析，协调多个团队并纠正副作用错误。<br>
<br>让我们分析一下“<em>纯微服务架构</em>”级联问题树：<br>
<ul><li>复杂性过度分布在细粒度服务中</li><li>这些细粒度的微服务缺乏稳定的协作点</li><li>缺失的粘合剂最终分布在组件和团队之间</li><li>即使是很小的变化也往往会导致混合影响。</li></ul><br>
<br>核心问题是缺乏城市化，导致单体或微服务架构缺乏模块化和关注点分离。<br>
<br>Airbnb 采用了一种新的架构风格 <em>Micro   macroservices</em>：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/4019bd77722a419587c4f96bd69925c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/4019bd77722a419587c4f96bd69925c8.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在这样的架构中，每种类型的复杂性分布是一个清晰的层：<br>
<ul><li><strong>统一 API</strong>是支持产品快速迭代的微服务</li><li><strong>中央数据聚合器</strong>是具有紧密耦合的稳定单体</li><li><strong>服务块外观 API</strong>抽象了提供实体块的微服务。</li></ul><br>
<br>阅读本文，了解有关<a href="https://qeunit.com/blog/how-architecture-contributes-to-quality-at-speed/">速度和质量架构的价值</a>的更多信息。<br>
<h4>组织一致性支持新架构</h4>旨在支持业务目标的组织可以改变游戏规则。 这种调整对于 Airbnb 的加速发展至关重要。<br>
<br>该组织与不断发展的架构保持一致，产品团队在统一 API 之上工作，数据聚合团队在中央数据层（即“胶水”），以及每个数据方面的域平台团队（预留、用户）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/1e94b044ee441f38ab054f650d92aff0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/1e94b044ee441f38ab054f650d92aff0.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>方法强制通往新架构的铺平道路</h4><em>架构审查、IT 委员会、工艺治理</em>——这些都是用于根据当前环境和未来架构审查提出的解决方案的方法。<br>
<br>这种方法的价值在于作为一种反力量，在由其他目标驱动的项目环境之外，以平衡选择。<br>
<br>Airbnb 使用这些方法为 <em>Micro   macroservices</em> 架构铺平了道路。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/73f4b49e0c9d254639162e0d74e63be5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/73f4b49e0c9d254639162e0d74e63be5.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
即使不包括在内，Airbnb 的*管理层**肯定对领导转型和发展新模式的文化以及发展*技能*产生了巨大影响，从而完成了 <a href="http://qeunit.com/mamos/">MAMOS</a> 的范围。<br>
<br>有了这些变化，Airbnb 能够引领平行的迁移轨道。但是弃用 Monolith 仍然需要太多时间。<br>
<h3>4. 引入弃用工作组加速迁移</h3>单独更改我们的银行账户已经是一场噩梦。当需要数年时间与多个团队协调才能完成时，这项任务就更加复杂了。<br>
<br>Airbnb 就像许多其他拥有遗留系统和持续业务的组织一样：他们无法在建造新房子的同时炸毁他们居住的房子。<br>
<br>一个特定的组织单位致力于加速从单体架构中迁移出来，领导以下工作：<br>
<ul><li>移动应用程序弃用达12个月以上</li><li>提升和跟踪整体债务以获得可见性</li><li>日落低使用率的终端以加速删除</li><li>迁移的长期所有权</li><li>认识到折旧对估值有影响</li></ul><br>
<br>这个团体有游说的反击力量，但对于实现迁移目标至关重要。反对单体应用不能是“每个人的责任”。<br>
<br>当这项任务完成时，将面临其他挑战。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220620/8a9be1009129cac79c1b1b4cce61fb82.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220620/8a9be1009129cac79c1b1b4cce61fb82.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Airbnb 的架构质量工程之旅</h3>Airbnb 架构演变的这一观点为 Quality at Speed 软件提供了具体的质量工程要点。<br>
<br>首先，区分局部问题或扩展问题可以更好地识别潜在原因，从而更好地采用增量解决方案。<br>
<br>在精益方法中，Airbnb 的团队在遇到问题时解决问题，避免不必要的预优化等浪费。<br>
<br>从我的角度来看，一个可行的要点在于架构，MAMOS 的其他元素是这个结构块的对齐。<br>
<br>从单仓内的单体应用出发，然后根据业务发展对其进行划分，就像他们对两个存储库所做的那样。<br>
<br>然后，他们的故事举例说明了“<em>纯微服务架构</em>”的问题，并被具有延迟的反馈循环的 <em>Micro macroservices</em> 架构所取代。<br>
<br>您将使用哪种架构风格？<br>
<br><strong>原文链接：<a href="https://medium.com/qe-unit/airbnbs-microservices-architecture-journey-to-quality-engineering-d5a490e6ba4f">Airbnb’s Microservices Architecture Journey To Quality Engineering</a>（翻译：池剑锋）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            