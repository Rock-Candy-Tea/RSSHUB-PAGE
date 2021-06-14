
---
title: '十八岁的DDD'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae648f9a24094183b5070ad5c0b150a8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 07:19:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae648f9a24094183b5070ad5c0b150a8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>DDD，一个耳熟似乎不能详的名字。今年，它18岁了。</p>
<p>2017年的年末，我在北京作为志愿者参加了老东家举办的第一届《中国领域驱动设计峰会》，众多国内的大咖们齐聚一堂交流对DDD的实践和感悟，一同参与的还有部分国外的嘉宾。一个多月前，2020年的《峰会》也如期在线上举办。你看，好几年过去了，大家对DDD依旧兴致盎然，DDD在当下软件架构中的地位也可见一斑。</p>
<p>作为一种软件架构思想，它的诞生和流行一定有着某种合理性和必然性。换句话说，DDD之所以会如此炙手可热，应该是因为它洞见了软件开发中的问题，并提出了相应的应对之策。对于软件从业者而言，我们似乎不太能忽视它的存在。</p>
<p>然而，当我们准备走近DDD去了解它时，却又似乎看不清楚它的样子，如雾里看花，终隔一层。看别人玩得不亦乐乎，自己却下不了手，一腔热血却抑郁而止，你说气不气人！难道DDD还自带朦胧美？</p>
<p>当然不是。如果一个流行的事物让大多人摸不着头脑，要么它本身确实很复杂，要么有人希望你认为它很复杂。</p>
<p><strong>幸运的是，DDD本身并不复杂，你要相信它既可远观，也可“亵玩”</strong>。之所以会出让很多人觉得摸不着头脑，并非是因为它高深莫测，而是另有原因。</p>
<h2 data-id="heading-0">DDD与微服务的不解之缘</h2>
<p>时间回到2003年，Eric出版了那本著名的《Domain-driven Design》，这本书花费了它4年的时间。也就是说，Eric从1999年就开始构思编写DDD了，距今已近二十二年。20多年的时间，在其他领域也许不足为道，但在软件和互联网领域已经足够完成一次次的技术跨越。很难想象，一种软件架构思想历经二十多年不仅没有被淘汰，竟然再次青春焕发！</p>
<p>说到这，DDD得感谢微服务的出现。近些年来，由于互联网行业的快速发展，应用系统逐渐复杂，催生出了微服务思想。微服务提倡对业务单元进行分而治之，各模块自治，从而降低系统的复杂度。而恰巧的是，这竟然和DDD在战略设计部分所提出的限定上下文的思路如出一辙。如果你读过Eric的原著，你甚至可能会有微服务似乎是由DDD衍生而来的错觉。而通过DDD来指导微服务设计，你也会发现几乎没有明显违和感。正因如此，DDD得以借着微服务的流行再次焕发活力，这也是DDD“战略设计”的价值体现，也是当下环境中DDD最重要的价值体现。</p>
<h2 data-id="heading-1">DDD的内核是什么？</h2>
<p><strong>要了解这一点，必须撇开业界对DDD的各种解读，直接读原著</strong>。从篇幅上看，洋洋洒洒的文字足以吓退大部分读者，事实上也确实有很多所谓的DDD拥趸们并没有读完整本著作但却给出了各种解读，误人子弟。在读原著时，不用从第一行读到最后一行，<strong>Eric已经在序言中明确指出了重点章节</strong>，阅读时可以注意下。</p>
<p>要理解DDD的内核，必须理解它的定位和它的要义。Eric在编写DDD这本书的时候，给了它一个副标题：</p>
<blockquote>
<p>“Tackling Complexity in the Heart of Software-软件核心复杂性应对之道”。</p>
</blockquote>
<p>这句话是对DDD的<strong>定位</strong>，也是作者立意之本。理解这句话的重点是“<strong>核心</strong>”和“<strong>复杂</strong>”两个词，对DDD的设计思想的理解和落地的实践，都要考虑到<strong>核心复杂</strong>。换句话说，<strong>DDD不是解决所有问题的银弹，它有着明确的应用场景</strong>。理解这一点之后，也就应该意识到DDD只是架构工具箱中的一把锤子，这把锤子什么时候用，要看情况。如果你的问题足够复杂，DDD可能是你的首选。<strong>否则，出门右拐可能有更好的其他选择</strong>。</p>
<p>既然DDD的定位是为了解决软件开发中的核心复杂，那它是如何做到的呢？说穿了，其要义就是下面就是下面这几个点：</p>
<ul>
<li>通过建模<strong>关注业务领域</strong>，解决领域复杂问题；</li>
<li>通过<strong>通用语言</strong>扫清沟通障碍；</li>
<li>通过代码体现领域模型和领域逻辑；</li>
<li>通过持续演进完善模型；</li>
<li>通过上下文划分子域；</li>
</ul>
<p>翻译成大白话，对应的就是下面这样：</p>
<ul>
<li>在软件复杂度中，不要只关心技术复杂度，领域逻辑带来的复杂更为重要且持久；</li>
<li>不管是开发，还是产品或者运营，麻烦各位统一下口径、说辞；</li>
<li>这套通用语言不只是说说，你要通过模型，把领域体现到代码里；</li>
<li>要贴紧业务，拥抱变化，持续调整、优化领域模型；</li>
<li>大泥球要不得，要合理地划分子域和边界，分而治之。</li>
</ul>
<p>你看，DDD的精华也不过如此，很难理解吗？<strong>它无关技术实践，也无关语言选择</strong>，甚至于你可能会觉得你好像已经掌握了DDD，是不是有点恍惚？事实就是这样，与其说是Eric发明了DDD，倒不如说是Eric取了个好名字。要知道，DDD背后对建模和面向对象的讨论，在那个年代十分盛行，各种方法百花齐放。基于领域建模也并非Eric首创，本文下方所引用的关于以数据为中心的设计模式和领域驱动设计模式对比的图片，正是来自于老马的书中，它于2002年出版，比DDD还早一年，至今也仍没有过时。但不得不说，Eric的名字取得非常好，对一些概念提炼得更好。这和同时期出现的敏捷宣言异曲同工，九十年代也是各种软件方法盛行，比如极限编程、水晶方法、DSDM等。这些软件方法看起来也是百花齐放，但其实在内涵上都有相同之处。于是乎，一些老专家们在滑雪之际，结合百家学说，提出了“敏捷宣言”。</p>
<p>DDD不仅在概念上和敏捷类似，在实践上也有相似之处。它们都是开放的软件开发思想，本身并没有固定的玩法，给实践者们提供了丰富的想象空间和交流空间。你可以简单认为DDD提供了一些接口规约，但是具体如何实现你自己定，能够实现其内涵和本质和原则即可。敏捷如此，DDD也是如此。歪个嘴，之所以后来敏捷出现了某些固定玩法，一是因为确定的方法有助于落地，二是因为打包好了容易卖钱。</p>
<p>而在实践方面，很多人可能还会认为敏捷是新潮思想，对其不甚了解。殊不知，历经二十年的发展，敏捷的实践早已遍地开花，潜移默化地成为了当下软件开发过程的一部分，只不过你可能没意识到而已。比如阿里效能部，集结了业界众多敏捷专家，深谙敏捷之道，他们已经将敏捷内嵌到开发流程中，你可能无感知，但实际已置身其中。DDD也是如此，这二十多年来的发展，DDD的诸多精华也已经在不知不觉中落地，比如微服务背后的限界上下文。<strong>某种程度上可以说，它们并非来自于DDD，而是来自于环境和趋势</strong>。</p>
<h2 data-id="heading-2">实践DDD能给我们带来什么好处？</h2>
<p>谈起DDD的好处，大部分人可能都用下面这张图（来自于老马的《企业应用架构模式》，2002年出版）：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae648f9a24094183b5070ad5c0b150a8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这张图所表达的意思是，<strong>相比于以数据为中心的设计模式，领域驱动的设计模式更能经受得住时间的考验，复杂度会随着时间的增长而线性递增，线性意味着有序，不会失控</strong>。那它是怎么做到线性递增的呢？主要是通过下面两种方式：</p>
<ul>
<li><strong>通过分层架构，分离技术和领域复杂度，将重心放在领域上</strong>；</li>
<li><strong>通过限界上下文，划分核心域、支撑域等不同子域，分离领域复杂度</strong>。</li>
</ul>
<p>这两种方式所实现的复杂度控制，使得系统具有以下好处：</p>
<ul>
<li><strong>代码结构优化</strong>：分层后的代码结构更加清晰，易于扩展和维护；</li>
<li><strong>领域逻辑内聚</strong>：领域逻辑在一个地方，领域行为更具复用性；</li>
<li>此外，<strong>良好组织的代码也更具可读性和测试性</strong>。</li>
</ul>
<h2 data-id="heading-3">使用DDD的缺点和代价是什么？</h2>
<p>天下没有免费的午餐，使用DDD也是如此。在享受DDD的价值时，也同时需要付出高昂的代价，比如下面的这些代价都需要我们来买单：</p>
<ul>
<li><strong>学习曲线</strong>：
<ul>
<li>新的设计思想和原则；</li>
<li>新的模式；</li>
<li>新的开发过程；</li>
</ul>
</li>
<li><strong>时间和精力</strong>：
<ul>
<li>建模时需要和领域专家进行沟通讨论；</li>
<li>从错综复杂的信息和模块中提炼领域逻辑；</li>
</ul>
</li>
<li><strong>只有在复杂问题中才能体现DDD的价值</strong>：
<ul>
<li>诸如CRUD就能搞定的问题，不要用DDD，用了反而会把问题搞复杂；</li>
<li>纯技术型应用，也不要用DDD；</li>
</ul>
</li>
<li><strong>推广和传播</strong>：
<ul>
<li>单丝不成线，独木难成林。如果你想仅凭一己之力获得广泛认可，可能低头承包需求开发更合适你；</li>
<li>你需要持续地宣讲、布道，持续地获得组织的支持，持续地和伙伴达成共识，持续地守护架构，以及持续地学习。</li>
</ul>
</li>
</ul>
<p>根据敏捷这些年的推广经验来看，<strong>凡是涉及到改变组织协作关系或者个人开发方式的变革，无论是从上至下还是从下至上，都极具阻力</strong>。因为组织关系关乎个人利益，而开发方式涉及多年的习惯和认知，都不可能一蹴而就。</p>
<h2 data-id="heading-4">为什么DDD难于理解？</h2>
<p>前文已经说过，DDD本身并不复杂。之所以我们觉得复杂、难于理解，<strong>主要原因在于它是开放的软件设计思想，在实践的过程中都可以有不同的落地方案，而DDD本身及周边的方案也在不断演变</strong>。</p>
<p>比如，在团队中实践通用语言时，你打算怎么做？如果你不知道，那就会有人告诉你，你可以使用敏捷软件开发、SCRUM、用户故事、用户故事地图、Inception等等。有没有很懵？如果展开的话，如何实践“用户故事”这一个话题就可以写一本书。而顺着“用户故事”这根线，还可以牵扯出一堆你可能都没听过的工程方法，是不是要疯了？</p>
<p>再比如，通用语言如何写到代码里？如果你不知道，那又有人会告诉你，你要设计领域模型、领域服务，还要使用CQRS、事件溯源、事件风暴、单元测试等等。这么多莫名其妙的概念，是不是又懵了？比如经常被提到CQRS，它真有那么香吗？要记住一个常识，任何一种技术都有它适用的场景，也有着它的局限性。而提到单元测试，那一堆的框架又可以喝两壶的了。</p>
<p><strong>对DDD的无限发散和解读，是导致它看起来不好理解的重要原因，也是人为的原因</strong>。DDD从来就没有什么固定的框架，也从来没有限定于JAVA或某种特定语言。如果有，那大概是因为有人要拿结果，有人要成名，还有人要牟利，人为把它复杂化。这里并没有贬低任何人的意思，我曾就职于咨询公司，也经常混一些软件方法的圈子，相对了解一些套路，堆砌概念、发散话题是一些青铜咨询师的常见做法。比如“复杂”，看起来只有两个字，但你可以发散地谈复杂的本质是什么、软件的复杂度来自哪里等等，还可以引申出Cynefin框架，凡是两句话说不清楚的事情都可以拿出来扯一遍，让别人听起来好像挺那么回事，其实没什么用，主要是用来唬人，我本人也这么干过。</p>
<p><strong>所以要理解DDD，一定要从原著中找它的本来面目，不要听信花里胡哨的说法。本文的这些碎碎念，也不值得你多停留</strong>。</p>
<h2 data-id="heading-5">回到现实，做还是不做？</h2>
<p>这个问题没有固定答案。</p>
<p><strong>我个人认为对待DDD要有一颗平常心，它不过是一种软件架构思想，从问题驱动出发，认清它的本质后量力而行</strong>：</p>
<ul>
<li>DDD并不复杂，它的内核朴实无华，你可能已经在实践了；</li>
<li>DDD不是银弹，大部分简单业务场景不需要考虑使用DDD，复杂业务问题优先考虑DDD；</li>
<li>没有完美的DDD实践，也没有绝对正确的DDD方法；</li>
<li>关注领域模型，关注通用语言，关注面向对象，忘掉对DDD的执念，忘掉框架的束缚；</li>
<li>DDD从来不是架构升级和业务扩展的绊脚石，困扰我们的也从来不是DDD，需要做的事情远不止DDD；</li>
<li>2009年，在伦敦QCON大会上，即DDD出版6年之后，Eric认为DDD的关注点已经从组织业务逻辑改变为<strong>发现领域架构</strong>。同时，Eric也认为领域模型仍然是组织业务逻辑的良好模式，但面向对象、函数式编程、CQRS、三层架构也是不错的模式。想想又过去了十来年，DDD的关注点还在变化中。没法细品，品起来要疯。</li>
</ul>
<p>当然，现在很多人在实践DDD的过程中，似乎都在寻找某种固定的框架。<strong>的确，套用框架是最不用动脑子的事情，也可以有效降低DDD在战术层面的实践门槛，但要清楚它不是DDD的全部，更不是DDD的核心</strong>。否则，任何框架都阻挡不了你倒一碗意大利面条进去。</p>
<p><strong>事实上，对于大部分开发者来说，也不必执念于DDD，看看《重构》、《敏捷软件开发》、《整洁软件架构》这些基础书目，反而更实用</strong>。</p>
<p><strong>延伸阅读与参考资料</strong></p>
<ul>
<li>老专家谈DDD：<a href="https://martinfowler.com/bliki/DomainDrivenDesign.html" target="_blank" rel="nofollow noopener noreferrer">martinfowler.com/bliki/Domai…</a></li>
<li>你想找的可能都在这里：<a href="https://github.com/heynickc/awesome-ddd" target="_blank" rel="nofollow noopener noreferrer">github.com/heynickc/aw…</a></li>
<li>InfoQ <a href="https://www.infoq.com/domain-driven-design/" target="_blank" rel="nofollow noopener noreferrer">www.infoq.com/domain-driv…</a></li>
<li><a href="https://www.domainlanguage.com/" target="_blank" rel="nofollow noopener noreferrer">www.domainlanguage.com</a></li>
<li><a href="https://www.dddcommunity.org/" target="_blank" rel="nofollow noopener noreferrer">www.dddcommunity.org</a></li>
<li>2020年《中国领域驱动设计峰会》</li>
</ul>
<p><strong>关于作者</strong></p>
<p>关注公众号【<a href="https://writting.oss-cn-beijing.aliyuncs.com/2021/05/18/qrcodeforgh61bfe45f82b7200.jpg" target="_blank" rel="nofollow noopener noreferrer">庸人技术笑谈</a>】，获取及时文章更新。记录平凡人的技术故事，分享有品质（尽量）的技术文章，偶尔也聊聊生活和理想。不贩卖焦虑，不做标题党。</p>
<p>如果本文对你有帮助，欢迎<strong>点赞</strong>、<strong>关注</strong>、<strong>监督</strong>，我们一起<strong>从青铜到王者</strong>。</p></div>  
</div>
            