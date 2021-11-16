
---
title: '产品经理的思考利器——UML'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/bd12926afb1c4952bee892d9aa99efb5-picture'
author: PMCAFF
comments: false
date: Sun, 14 Nov 2021 16:10:29 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/bd12926afb1c4952bee892d9aa99efb5-picture'
---

<div>   
<div><style>
#articleCont &#123;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  word-wrap: break-word;
&#125;
#articleCont :first-child &#123;
  margin-top: 0 !important;
&#125;
#articleCont h1,
#articleCont h2,
#articleCont h3,
#articleCont h4,
#articleCont h5,
#articleCont h6 &#123;
  margin: 40px 0 20px;
&#125;
#articleCont h1 &#123;
  font-size: 24px;
&#125;
#articleCont h2 &#123;
  font-size: 22px;
&#125;
#articleCont h3 &#123;
  font-size: 20px;
&#125;
#articleCont h4 &#123;
  font-size: 18px;
&#125;
#articleCont h5 &#123;
  font-size: 16px;
&#125;
#articleCont i &#123;
  font-style: italic;
&#125;
#articleCont p,
#articleCont div &#123;
  word-wrap: break-word;
  margin: 14px 0;
  text-align: justify;
&#125;
#articleCont blockquote &#123;
  border-left: 6px solid #ddd;
  padding: 5px 0 5px 10px;
&#125;
#articleCont blockquote p:last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont .simditor-body blockquote :last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont a &#123;
  color: #82b64a;
&#125;
#articleCont a:visited &#123;
  color: #82b64a;
&#125;
#articleCont a:hover &#123;
  color: #74a342;
&#125;
#articleCont img &#123;
  max-width: 100%;
  height: auto;
&#125;
#articleCont hr &#123;
  margin: 19px 0;
  border: none;
  border-top: solid 1px #ddd;
&#125;
#articleCont ol &#123;
  list-style-type: decimal;
&#125;
#articleCont ol li &#123;
  list-style-type: decimal;
&#125;
#articleCont ul &#123;
  list-style-type: disc;
  padding-left: 40px;
&#125;
#articleCont ul li &#123;
  list-style-type: disc;
&#125;
#articleCont table &#123;
  width: 100%;
  font-size: 12px;
  border-collapse: collapse;
  line-height: 1.7;
&#125;
#articleCont table thead &#123;
  background: #f9f9f9;
&#125;
#articleCont table th,
#articleCont table td &#123;
  border: solid 1px #ccc;
  text-align: left;
  vertical-align: top;
  padding: 2px 4px;
  height: 30px;
  min-width: 40px;
  box-sizing: border-box;
&#125;
#articleCont pre &#123;
  white-space: pre-wrap;
&#125;
</style><p>本文长度7000字，预计阅读需要20分钟</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/bd12926afb1c4952bee892d9aa99efb5-picture" alt="UML" coffee-w="900px" coffee-h="383px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>看到这个标题，产品的朋友们大概率会一头雾水，为什么一个产品要学这么“奇怪”的东西？产品把产品本职工作做好就行了吧？</p><p>且听我快速道来~</p><p>在我之前的产品经历里，经常会遇到一个场景，在我拆解（或调研）某个业务系统时，无法梳理出一个系统层面清晰的脉络，思考出整个业务和系统架构的融合方式，即使后期我梳理清楚了，也是一个“大力出奇迹”的方式，一步一步硬推出来的。</p><p>但这种蛮力的方式不是长久之计，如果我以后换了领域或者行业怎么办？我的业务线调整裁掉了该怎么办？都要硬啃吗？显然不行的</p><p>在工作中，我们接触新领域/产品的时候，都会“开头难”，这个难在于没有在这个新领域下有历史经验，以致于用最笨的方法去调研，验证，学习，然后积累出一点点优势，慢慢滚雪球，形成加速。但如果又换一个新领域，我们很大概率还依赖这种行为方式，这就会造成认知的低效率。</p><p><strong>我其实一直想找到一个比较底层的方法工具，便于快速切换领域和习得经验。</strong></p><p>我先后学习与应用了一些思考框架，如<br>·用户体验要素五层框架（战略层/范围层/结构层/框/框架层/表现层）这套思考方式<br>·需求蛋模型（一个集合里画一条线，两侧分别是自身的功能与用户的需求）<br>·用户故事地图（按故事线去梳理一些用户完整的story，然后快速开发）<br>·商业模式画布（一个梳理商业模式的框架图，可用来自己做商业规划，也可以用来调研分析竞品，在执行上顺序会略有不同）<br>但这些框架应用的条件，都是建立在我的需求可以被现实环境承载、以及我有这方面领域的逻辑下才可生效。我想要的是切换领域，最后直到我遇到了UML，只有它才能满足我</p><p>所以我来推荐产品的朋友，或者其他有这方面困惑的朋友，了解UML这个工具</p><p>这篇介绍UML的文章，算是一个引子，后面营销系统相关的文章会引用到这里，避免到时候阅读上有信息割裂感</p><h2>UML到底是个什么？</h2><p>学名叫做“统一建模语言（Unified Modeling Language）”，下面用大白话解释下</p><p><strong>UML这个语言定位是个工具</strong>，是1997年OMG组织（不是哦买噶！是Object ManagementGroup对象管理组织）发布的统一建模语言，是一种编制软蓝图的标准化语言<br>它的目标之一就是为开发团队提供标准通用的设计语言来开发和构建计算机应用，提出了一套IT专业人员期待多年的统一标准建模符号，支持面向对象的技术。<br>通过使用UML，这些人员能够阅读和交流系统架构和设计规划。<strong>（可以理解为想实现在不同世界的研发沟通时，达到车同轨书同文的效果）</strong></p><p>除此之外，工作中还会遇到各种xxML，都是某类领域为了方便业内交流，或者战略上为了制定行业标准而发明的建模语言，如VRML（虚拟现实建模语言），sysML（从UML2.0衍生并进化）等</p><h2>为什么要学UML？我能得到什么？</h2><p>在我看来，UML更是一种思想，诞生之初给研发人员使用，但也适合产品架构师，系统分析师这类的角色使用，掌握以后有这个几个好处</p><h3>好处1 思维方式的扩展</h3><p>UML是一种面向对象的思考方式，用抽象的方式去反映现实世界的某个片段。<strong>如果去和前文提到“用户体验要素（战略层/范围层/结构层/框/框架层/表现层）”联系的话，UML的作用处在范围层&结构层</strong></p><p>UML同时也是分而治之的思想的重要体现，在现实中也有其他类似的体现，比如工程测量中“先整体后局部，由高级到低级，由控制到碎部”</p><p>掌握了它，就可以在思考复杂问题的时候有层次有章法，面对再大再庞杂的系统，也可以逐个解开</p><h3>好处2 识别“领域知识”，跨领域沟通与学习能力的提升</h3><p>“领域知识”是一个元概念，有时候和用户/客户交流，你会被带入到全新的领域（不理解领域的话，可类比行业去理解，实际不太一样）中，和领域内的专家与客户交谈，他们的独有的业务经验，对你来讲，就是一个“领域知识”，这种场景在B端业务中会更为常见。</p><p><strong>如果我们无法定义一件事，就无法注意到它。</strong></p><p>好了，<strong>我现在把定义引入进来了，大家可尝试在工作或生活中注意到它：</strong></p><p>在与客户交谈时，<strong>注意客户描述业务实体的名词术语，这些名词术语会被当成「类」，还要注意听到的动词，这些动词可能会构成「类」中的「操作」，然后还有其他名词可能变为「类」中的「属性」。</strong><br>当梳理出来之后，<strong>再去询问客户每个「类」的作用，客户会告诉你「类」的职责</strong>，这样就能快速了解该领域的基础逻辑。</p><p>就是我开篇提到的痛点，在学习了UML之后，对“领域知识”有了新的认知，有信心在进入陌生领域时系统的建立起认知</p><h3>好处3 完全是私货 对思考的习惯有很大影响</h3><p>学了UML后，我甚至可以对人际关系有了更冷静的感知，比如沟通的时候，沟通的是你，你的关系，别人，还是你身上的某部分属性，都可以想的很透彻，更能接近事实和本质，可提高思考的深度</p><p>这种深度的提高，对我这种傻实在的人来说，很有帮助。或者对社会经验不太足的学生来说，也会有帮助</p><h2>UML都包含哪些内容，如何快速上手？</h2><p>引了这么多，直接看UML有啥东西吧！<br>主要可分为如下图两大类：</p><p>1、<strong>结构元素</strong>，图例左半部分，自上而下为类图，接口，用例图，关系，分组，注释<br>2、<strong>行为元素</strong>，图例右半部分，自上而下为状态图，时序图，协作图，活动图</p><p>可以理解为这就是咱们现实世界的粗暴分解，结构和过程组成了世界上的一切，形成了时空</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/341c3271862c541fcb72644b97ae2c4b-picture" alt="屏幕快照 2021-10-04 下午9.26.15" coffee-w="810px" coffee-h="910px" coffee-format="png" referrerpolicy="no-referrer"></p><p>再奉上一张网上超级经典的图，UML拆解的样例，这里基本用上了UML中高频使用的图例类型，请保存好，后面会持续用到<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/a875eeaf725343d2cb5e7ebd346a97ad-picture" alt coffee-w="703px" coffee-h="670px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p><strong>那么，产品同学要掌握的图有哪些？</strong><br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/652e16da6075e95756e5debd3fb205ec-picture" alt coffee-w="1898px" coffee-h="1060px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><h2>结构元素</h2><h3>结构元素-类图</h3><p><strong>类，是一类或者一组具有类似属性和共同行为的事物</strong>，映射到现实中，可参考我上面的那个黄颜色的图</p><p>类图（Class Diagram）是面向对象系统建模中最常用和最重要的图，是定义其它图的基础，主要是用来显示系统中的类、接口以及它们之间的静态结构和关系的一种静态模型</p><p>类图描述一个类的<strong>属性和操作</strong>，以及对系统的约束。它们是唯一的，可以直接映射到面向对象的语言的 UML图。请看详解</p><p><strong>「类」的实例，叫做「对象」</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/84bef6d97a81c5b8417857caf2172eed-picture" alt coffee-w="1834px" coffee-h="972px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p><strong>类和类之间，也会存在相互关系，这个关系也有专门的标识方式</strong>，这里要先引入“面向对象”的一些相关概念了，如下图</p><p><strong>面向对象的思考方式，是以开发出能够反映出现实世界某个特定片段为目标的，或者叫建模。</strong><br>对象是类的实例，比如你和我都是“人”这个「类」的实例，对象具有自身的结构，属性和操作。</p><p>比如<strong>抽象，是过滤掉对象的一部分属性，保留解决问题所够用的属性和操作</strong>，因为现实生活中，解决问题不一定需要全部的信息</p><p>再就是<strong>继承，我们的电冰箱，电烤箱可以看成单独的「类」，都是电器这个「类」下的子类，继承了电器的“开”与“关”，但冰箱有冷冻功能，烤箱有加热功能。对应的，电器这个「类」也是电冰箱电烤箱的「超类」</strong></p><p>其他的可以看图，要解释下本图不是UML全部的内容，但足够本文章讲和使用了</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/49cabe45f5f5a5f109fdf42374e4b261-picture" alt coffee-w="1910px" coffee-h="1066px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>好了，终于可以讲正题了！</p><p>「类」之间存在的关系，有如图几种，我们详细用图片展示<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/a0a0b06e5c83071980f7f54c5ff15f04-picture" alt coffee-w="1858px" coffee-h="1034px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p><strong>关联</strong><br>接触过数据库的同学对这个定义比较熟悉，基本等同于ER的思考逻辑<br><strong>使用直线表示</strong><br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/520ae17ad382999e2f5905ed0b5ef50f-picture" alt coffee-w="1934px" coffee-h="1050px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>就像「类」和「对象」的层级关系，「类」和「类」之间的“关联”关系，也是一个「类」，且这个「关联类」对应的「对象」叫做「链」。<br>听起来有点套娃，但这个就是核心的思考方式了，可以向上抽象思考，也可以向下实例思考</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/c5500d6765ccc95368de2fd0ed0aa242-picture" alt coffee-w="1752px" coffee-h="960px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>关联讲完了，咱们来讲<br><strong>抽象，继承，泛化</strong><br>这三个放到一块讲，是他们的联系可放到一块去思考，在设计游戏时，「计时器类」是从「投球计时类」和「游戏计时类」抽象出来的，对应的子类用<strong>空心实线箭头指向被继承的类，这个箭头就是泛化关系</strong>，代表“is a kind of……”<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/a138f3f4bbdcd937dcbd0d1ed30e855d-picture" alt coffee-w="1848px" coffee-h="1018px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/66a997f45c59ae515aab15e577b5a980-picture" alt coffee-w="1914px" coffee-h="1052px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>好好琢磨下哈，然后咱们继续介绍下<br><strong>接口和实现</strong><br>接口跟封装可以一起介绍，可以理解为你在使用冰箱的时候，不需要知道冰箱怎么制冷的。只需要插电和开关冰箱门就好了。冰箱把制冷的细节都封装在了里面，给你留下了开关和插电的接口<br>冰箱这个「类」对应的他的开关接口，这之间的关系就是实现，<strong>使用空心虚线箭头标识</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/ec3a0dc07079e29d1b13b93159041dd2-picture" alt coffee-w="1880px" coffee-h="1018px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p><strong>依赖</strong><br>用虚线单箭头表示，一个类使用了另一个类，比如在设计报表类系统时，会存在类似的关系。“展示报表”的功能，使用了“报表”这个类，有一个前置的逻辑，形成了依赖关系<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/55383cc515989021e5196313865074b3-picture" alt coffee-w="1864px" coffee-h="1038px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>最后就是类图里的最后一块</p><p><strong>聚集和组成</strong><br>这其中<strong>有点形似与混合物 与 化合物的区别。</strong><br>聚集，用空心菱形剪头，从部分指向整体，一种混合物的关系<br>组成，用实心菱形剪头，代表强聚集关系，类似化合物的关系，桌子由桌面和桌腿组成。<strong>当然这只是为了没接触的同学好理解，如果有ETC精请克制自己不要自动抬杠……</strong><br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/ef463107ded41b34a35c4723d6ff1f5e-picture" alt coffee-w="1962px" coffee-h="1004px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><h3>结构元素-用例图</h3><p>篇幅最长的类图介绍完了，接下来介绍一个也很常用的用例图，相对简单很多，跟画画一样，一个小人儿和一大堆气泡发生了连线的关系</p><p>用例图可以在设计系统或者需求的时候，理清楚实际的场景，排坑。比如设计某功能时，总会有一些操作场景被遗漏，导致进入测试阶段中了，才发现有问题，要修补。使用用例图，能很大程度上在设计阶段避免这种情况。</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/897e94f5a869fdae7eaabf2a8ee587ec-picture" alt coffee-w="1880px" coffee-h="1056px" coffee-format="jpeg" referrerpolicy="no-referrer"><br>小人儿就是<strong>参与者</strong><br>气泡就是<strong>用例</strong><br>二者之间使用依赖线连接， <strong>上面可以标记<< include>> 或 << extend>>，<< include>>可理解为用例间包含的关系，一个用例包含了下一层级的用例。<< extend>>可以理解为此用例还有其他场景可以使用，扩展出了一个入口<br>用例图只用来标识参与者和用例的关系，并不代表先后顺序</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/0406bfb016c50d0faddcf17d8e2412de-picture" alt coffee-w="1976px" coffee-h="530px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>用例图在交付时通常给客户和开发组参考，每个用例图的场景描述至少占一页文档，包含：<br>·发起用例的参与者<br>·用例的假设条件<br>·用例的前置条件<br>·场景中的步骤<br>·场景完成后的后置条件<br>·从用例中获益的参与者</p><h2>行为元素</h2><p>终于大半篇幅讲完了结构元素，本节开始讲行为元素了，如果小伙伴们看麻了，可以收藏或者转发给自己的小号，后面继续看~</p><p>行为元素对于产品同学来讲，基本是不陌生的，如果经常绘制业务流程图的话，会发现有很多一致的地方，很正常，都是团队的沟通工具嘛</p><h3>行为元素-状态图（状态机图）</h3><p>这种图在制作大型业务系统的时候，肯定会用到，比如我在设计CRM系统的时候，里面的商机就会有多种状态流转，就用到了这个图。</p><p>给研发兄弟看，也会沟通的很顺畅，因为研发在实际工作中会频繁用到这里，他们基于这些状态去设计代码层面的调用逻辑。便于他们设计的时候提前规划，提高研发的效率。研发最怕的，是做一半了中途改了基础底层状态的设计，分分钟掀桌子</p><p>状态图的定义，可以说是对象改变了自己的状态，以响应事件和时间的流逝，比如灯的开与关。</p><p>状态图和类图的差别，是状态图针对的是单个对象来建模，类图可以针对一组类来建模</p><p>绘制方法，圆角矩形代表一个状态，状态间带箭头的实现代表状态的迁移，箭头指向目标状态。实心圆点代表状态转移的起点，牛眼圆圈代表重点</p><p>记不住那么多没关系，有专门的工具，跟visio一样，直接找来拖就行了，文章末尾会介绍绘制工具</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/f6e77e8e417fff3db1b47c03baf79e48-picture" alt coffee-w="1310px" coffee-h="378px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>下图是基于工单类的审批流程绘制的状态图</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/467a3032558e3905423cec542998b28c-picture" alt coffee-w="1854px" coffee-h="1006px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><h3>行为元素-时序图</h3><p>时序图，也叫顺序图，强调了时间维度，时序图的关键思想是强调了对象之间的交互按照特定时间发生，这些特定时间的交互序列，从开始到结束需要一定的时间。</p><p>时序图通常用对象标识，从每个对象下方延展出一条生命线，一个时序图可以用单个或者多个如下单元组成</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/1c8ca241b3003073d6ea56f94fcec6ee-picture" alt coffee-w="1130px" coffee-h="220px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>每个线程对象之间可以用消息通信，有两类</p><p>一类消息叫调用，这是一个来自消息发送者对象的请求，它被传递给消息的接收对象，请求接收者对象执行某种操作。通常，需要发送者等待接收者执行，等待反馈，这种消息又叫做同步消息。</p><p>如下图，带有实心箭头的实线表示发送的消息，带有线状箭头的虚线表示返回消息<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/8d983095e4c2a9a4df0b822af158cd2c-picture" alt coffee-w="598px" coffee-h="162px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>另一类消息叫做异步消息，这种机制下发送者把控制权交给了接收者，并不等待操作完成，这种消息用带有线状箭头的实线表示<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/7a556446908a91fb396a637dfefeb04c-picture" alt coffee-w="516px" coffee-h="118px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>时序图跟跨职能流程图有些许相似，不过时序图可以更清晰的展示每个线程的动作顺序，以及线程之间的通信关系，如果是用跨职能流程图的方式来绘制，就不便于展示每个线程之间的多条通信了</p><p>依然拿请假的流程举例，如图。</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/860662d7e856f285b0f297ac476f48e3-picture" alt coffee-w="1860px" coffee-h="996px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>时序图还有帧化的概念，不过对于非研发工作来讲，没必要学习，基本用不到。不再赘述</p><h3>行为元素-活动图</h3><p>终于到了最后的类型了！活动图，用圆角矩形表示，与状态图不同的是，活动图的图例更接近椭圆。一个活动的处理一旦完成，就自动引起下一个活动发生。</p><p>状态图侧重于描述对象的状态变化，活动图侧重于描述活动，与业务单线流程图大多数逻辑类似，不过区别是活动图更适合展示判断过程，和并发路径。如果用基础的单线流程图标识，会不太直观</p><p>比如判断是类似的表示方法<img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/47106bf848c8d86df1882cc72da5990e-picture" alt coffee-w="1060px" coffee-h="524px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>并行路径的表示方法<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/f5f7f94e609ff7048f2e5c93b46dad6b-picture" alt coffee-w="1436px" coffee-h="498px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>如果日常工作中使用流程图较多，也不必非要用这个，UML本质目的是快速沟通，能沟通清楚就行</p><h2>实战应用</h2><p>下面讲下我平时是怎么应用的，有两类案例，一类是研究一个系统，多数的时候是凭借兴趣研究的，感觉很有意思。另一个是工作里实际使用时展示的</p><h3>拆解与理解saleforce</h3><p>saleforce是CRM业界非常知名的一个产品，因为这个系统太过于庞大，UML的类图是快速理解的一个利器。<br>此时应用UML不是还原到如何实现，而是为了理解它是怎么设计的。通过demo很难有机会能接触到更深层的实现细节<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/f1012ecc099149e61138155cec819f58-picture" alt coffee-w="2064px" coffee-h="1220px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><h3>应用到工作</h3><p>在设计内部BI系统时，用到了类图，和用例图。<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/fd9394c04c7bf49d75de8648962e5ac9-picture" alt coffee-w="1278px" coffee-h="1056px" coffee-format="jpeg" referrerpolicy="no-referrer"><br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/4f7983f58ae75b7314a0329307553834-picture" alt coffee-w="1080px" coffee-h="896px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>在设计CRM系统时，商机（例子）状态的流转图。CRM的设计，我会单起一系列文章讲<br><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/ac2894ba92a662fb8d4615a0113c3c0c-picture" alt coffee-w="712px" coffee-h="1182px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>除了这些还有很多应用，不过都差不多，应该可以给大家足够的帮助了。关于UML的介绍内容，就到此结束，下面我做下对应的答疑</p><h2>高频的疑问解答</h2><p>在调研UML是否值得学习的时候，我也会经常看到这样那样的问题，比如</p><p><strong>1、我看完了，真的有必要学吗？研发不看怎么办？</strong><br>我的个人建议是，如果自身喜欢这方面的思考，可以凭兴趣去学；<br>如果是B端从业且想继续发展的业务产品，建议去学，学了以后会有如虎添翼的功效，不过学习需要时间，建议收藏，或者转发给小号后续常看，我平时看到东西也这么干哈哈，最好能买书学，更系统</p><p>UML本质还是沟通工具，可以跟研发去协商，看团队更倾向用什么方式沟通，UML只是一种，如果有别的更合适的表示方法，能把逻辑梳理清楚，歧义消除干净，最好不过了。</p><p><strong>2、UML和数据建模是否有关系？</strong><br>跟研发同事交流过，他们说UML其实就跟JAVA编程过程中的思考很接近，不断抽象和建模，平时也会用到。<br>数据库建模与UML有一定的联系，数据库建模的过程是逻辑层到物理层的逐层过程，都是构造模型，但侧重点不一样，数据库建模侧重数据层面逻辑效率，模型可用性等等。</p><p><strong>3、UML之后如何使用？</strong><br>除了上面的那些基本功能点以外，使用UML的本质目的就是为了多方理解，尽管UML有一些法则，也不要被禁锢，<strong>能达到沟通顺畅无歧义的目的，就足够了</strong></p><p><strong>4、画图使用什么工具呢？</strong><br>·starUML。win/mac平台都有，win的平台有个版本很复古，但是功能很完善。mac有starUML4.0的版本，颜值很高，但是感觉画起来没win的好用。大家可以百度搜下。<br>·Visio。可以画的图很多，包含了UML的基础图例，不过看个人习惯，我Visio和starUML都用，Visio常用来画流程<br>·其他有用的也可以推荐下，工具嘛，趁手就行</p><p><strong>5、有哪些书籍推荐？</strong><br>·UML基础、案例与应用（入门）<br>·大象UML（进阶）<br>·大话设计模式（感兴趣可以看）<br>·系统架构（值得反复长期啃，我确实还没看完，太大了，不过是本神书）<br>另外其他的书，可以白嫖微信读书无限卡，香滴很！</p><h1>结语</h1><p>未来，我会出一些关于业务系统的相关文章，尽量大白话，可能有些大佬看着文字会评价我的思考肤浅，但能有人听懂和交流，才是我的初衷。</p><p><b>我期望我的些许产出，可以让新手产品同学们不再像我当年那样随机漫步，能快速度过无人带领自己摸索的成长期，我愿意做一块铺路石~</b><br><br></p><p>肝了这么久，不知道你们学废了没有，如果有收获，还请点个赞鼓励一下我~哈哈哈感谢感谢</p><p>如有问题，可评论或者私信交流</p></div>
  
</div>
            