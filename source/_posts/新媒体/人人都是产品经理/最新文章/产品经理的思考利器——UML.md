
---
title: '产品经理的思考利器——UML'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/11/UevtctgxxGOiDn11d6RZ.png'
author: 人人都是产品经理
comments: false
date: Tue, 16 Nov 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/11/UevtctgxxGOiDn11d6RZ.png'
---

<div>   
<blockquote><p>编辑导语：可能很多产品经理会有疑问，UML是什么？为什么要学习这个？学习了之后会有什么作用？它其实是一个工具，是IT专业人员期待多年的统一标准建模符号，支持面向对象的技术。学习UML，有助于快速切换领域和习得经验，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-714093 aligncenter" src="https://image.yunyingpai.com/wp/2021/11/UevtctgxxGOiDn11d6RZ.png" alt referrerpolicy="no-referrer"></p>
<p>看到这个标题，产品的朋友们大概率会一头雾水，为什么一个产品要学这么“奇怪”的东西？产品把产品本职工作做好就行了吧？且听我快速道来~</p>
<p>在我之前的产品经历里，<strong>经常会遇到一个场景，在我拆解（或调研）某个业务系统时，无法梳理出一个系统层面清晰的脉络，思考出整个业务和系统架构的融合方式，即使后期我梳理清楚了，也是一个“大力出奇迹”的方式，一步一步硬推出来的</strong>。</p>
<p>但这种蛮力的方式不是长久之计，如果我以后换了领域或者行业怎么办？我的业务线调整裁掉了该怎么办？都要硬啃吗？显然不行的在工作中，我们接触新领域/产品的时候，都会“开头难”，这个难在于没有在这个新领域下有历史经验，以致于用最笨的方法去调研，验证，学习，然后积累出一点点优势，慢慢滚雪球，形成加速。</p>
<p>但如果又换一个新领域，我们很大概率还依赖这种行为方式，这就会造成认知的低效率。<strong>我其实一直想找到一个比较底层的方法工具，便于快速切换领域和习得经验。</strong></p>
<p>我先后学习与应用了一些思考框架：</p>
<ul>
<li>用户体验要素五层框架（战略层/范围层/结构层/框/框架层/表现层）</li>
<li>需求蛋模型（一个集合里画一条线，两侧分别是自身的功能与用户的需求）</li>
<li>用户故事地图（按故事线去梳理一些用户完整的story，然后快速开发）</li>
<li>商业模式画布（一个梳理商业模式的框架图，可用来自己做商业规划，也可以用来调研分析竞品，在执行上顺序会略有不同）</li>
</ul>
<p>但这些框架应用的条件，都是建立在我的需求可以被现实环境承载、以及我有这方面领域的逻辑下才可生效。</p>
<p>我想要的是切换领域，最后直到我遇到了UML，只有它才能满足我所以我来推荐产品的朋友，或者其他有这方面困惑的朋友，了解UML这个工具这篇介绍UML的文章，算是一个引子，后面营销系统相关的文章会引用到这里，避免到时候阅读上有信息割裂感</p>
<h2 id="toc-1">一、UML到底是个什么？</h2>
<p>学名叫做“统一建模语言（Unified Modeling Language）”，下面用大白话解释下<strong>UML这个语言定位是个工具</strong>，是1997年OMG组织（不是哦买噶！是Object ManagementGroup对象管理组织）发布的统一建模语言，是一种编制软蓝图的标准化语言它的目标之一就是为开发团队提供标准通用的设计语言来开发和构建计算机应用，提出了一套IT专业人员期待多年的统一标准建模符号，支持面向对象的技术。</p>
<p>通过使用UML，这些人员能够阅读和交流系统架构和设计规划。<strong>（可以理解为想实现在不同世界的研发沟通时，达到车同轨书同文的效果）</strong>除此之外，工作中还会遇到各种xxML，都是某类领域为了方便业内交流，或者战略上为了制定行业标准而发明的建模语言，如VRML（虚拟现实建模语言），sysML（从UML2.0衍生并进化）等</p>
<h2 id="toc-2">二、为什么要学UML？我能得到什么？</h2>
<p>在我看来，UML更是一种思想，诞生之初给研发人员使用，但也适合产品架构师，系统分析师这类的角色使用，掌握以后有这个几个好处。</p>
<h3>1. 思维方式的扩展</h3>
<p>UML是一种面向对象的思考方式，用抽象的方式去反映现实世界的某个片段。</p>
<p><strong>如果去和前文提到“用户体验要素（战略层/范围层/结构层/框/框架层/表现层）”联系的话，UML的作用处在范围层&结构层。</strong>UML同时也是分而治之的思想的重要体现，在现实中也有其他类似的体现，比如工程测量中“先整体后局部，由高级到低级，由控制到碎部”掌握了它，就可以在思考复杂问题的时候有层次有章法，面对再大再庞杂的系统，也可以逐个解开。</p>
<h3>2. 识别“领域知识”，跨领域沟通与学习能力的提升</h3>
<p><strong>“领域知识”是一个元概念</strong>，有时候和用户/客户交流，你会被带入到全新的领域（不理解领域的话，可类比行业去理解，实际不太一样）中，和领域内的专家与客户交谈，他们的独有的业务经验，对你来讲，就是一个“领域知识”，这种场景在B端业务中会更为常见。</p>
<p><strong>如果我们无法定义一件事，就无法注意到它。</strong></p>
<p>好了，我现在把定义引入进来了，大家可尝试在工作或生活中注意到它：在与客户交谈时，注意客户描述业务实体的名词术语，这些名词术语会被当成「类」，还要注意听到的动词，这些动词可能会构成「类」中的「操作」，然后还有其他名词可能变为「类」中的「属性」。</p>
<p>当梳理出来之后，再去询问客户每个「类」的作用，客户会告诉你「类」的职责，这样就能快速了解该领域的基础逻辑。就是我开篇提到的痛点，在学习了UML之后，对“领域知识”有了新的认知，有信心在进入陌生领域时系统的建立起认知。</p>
<h3>3. 完全是私货→对思考的习惯有很大影响</h3>
<p>学了UML后，我甚至可以对人际关系有了更冷静的感知，比如沟通的时候，沟通的是你，你的关系，别人，还是你身上的某部分属性，都可以想的很透彻，更能接近事实和本质，可提高思考的深度这种深度的提高，对我这种傻实在的人来说，很有帮助。或者对社会经验不太足的学生来说，也会有帮助。</p>
<h2 id="toc-3">三、UML都包含哪些内容，如何快速上手？</h2>
<p><strong>引了这么多，直接看UML有啥东西吧！</strong>主要可分为如下图两大类：</p>
<ul>
<li>结构元素，图例左半部分，自上而下为类图，接口，用例图，关系，分组，注释。</li>
<li>行为元素，图例右半部分，自上而下为状态图，时序图，协作图，活动图可以理解为这就是咱们现实世界的粗暴分解，结构和过程组成了世界上的一切，形成了时空。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/ZdqQqE5tq0Cuf96uxmyK.png" alt="产品经理的思考利器——UML（7000字长文）" width="493" height="554" referrerpolicy="no-referrer"></p>
<p>再奉上一张网上超级经典的图，UML拆解的样例，这里基本用上了UML中高频使用的图例类型，请保存好，后面会持续用到。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/4PxXauHt96x42TBzx2Y1.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="577" height="550" referrerpolicy="no-referrer"></p>
<p>那么，产品同学要掌握的图有哪些？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/ARsnHSPcANBsHDN6eNFx.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="540" height="302" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、结构元素</h2>
<h3>1. 结构元素-类图</h3>
<p><strong>类，是一类或者一组具有类似属性和共同行为的事物</strong>，映射到现实中，可参考我上面的那个黄颜色的图类图（Class Diagram）是面向对象系统建模中最常用和最重要的图，是定义其它图的基础，主要是用来显示系统中的类、接口以及它们之间的静态结构和关系的一种静态模型类图描述一个类的<strong>属性和操作</strong>，以及对系统的约束。</p>
<p>它们是唯一的，可以直接映射到面向对象的语言的 UML图。请看详解<strong>「类」的实例，叫做「对象」。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/9Bpkm2kXtfDmccvgffWa.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="618" height="329" referrerpolicy="no-referrer"></p>
<p><strong>类和类之间，也会存在相互关系，这个关系也有专门的标识方式</strong>，这里要先引入“面向对象”的一些相关概念了，如下图<strong>面向对象的思考方式，是以开发出能够反映出现实世界某个特定片段为目标的，或者叫建模。</strong></p>
<p>对象是类的实例，比如你和我都是“人”这个「类」的实例，对象具有自身的结构，属性和操作。比如抽象，是过滤掉对象的一部分属性，保留解决问题所够用的属性和操作，因为现实生活中，解决问题不一定需要全部的信息再就是继承，我们的电冰箱，电烤箱可以看成单独的「类」，都是电器这个「类」下的子类，继承了电器的“开”与“关”，但冰箱有冷冻功能，烤箱有加热功能。</p>
<p><strong>对应的，电器这个「类」也是电冰箱电烤箱的「超类」</strong>其他的可以看图，要解释下本图不是UML全部的内容，但足够本文章讲和使用了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/eop124HwzJ2fxizwjvZ4.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="640" height="357" referrerpolicy="no-referrer"></p>
<p>好了，终于可以讲正题了！「类」之间存在的关系，有如图几种，我们详细用图片展示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/uQBo5GePNSMRtmCuH0yc.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="627" height="349" referrerpolicy="no-referrer"></p>
<p><strong>关联</strong>接触过数据库的同学对这个定义比较熟悉，基本等同于ER的思考逻辑<strong>使用直线表示。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/zajBhTPu5yi18oxfUrZy.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="677" height="367" referrerpolicy="no-referrer"></p>
<p><strong>就像「类」和「对象」的层级关系，「类」和「类」之间的“关联”关系，也是一个「类」，且这个「关联类」对应的「对象」叫做「链」。</strong></p>
<p>听起来有点套娃，但这个就是核心的思考方式了，可以向上抽象思考，也可以向下实例思考。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/27RMmh5dyh3WsQCxpnII.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="655" height="359" referrerpolicy="no-referrer"></p>
<p>关联讲完了，咱们来讲<strong>抽象，继承，泛化</strong>这三个放到一块讲，是他们的联系可放到一块去思考，在设计游戏时，「计时器类」是从「投球计时类」和「游戏计时类」抽象出来的，对应的子类用<strong>空心实线箭头指向被继承的类，这个箭头就是泛化关系</strong>，代表“is a kind of……”</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/grEO1s4z61xCMxqEzZWy.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="649" height="357" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/bDRISL0dbSsx80Wlhb36.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="642" height="353" referrerpolicy="no-referrer"></p>
<p>好好琢磨下哈，然后咱们继续介绍下<strong>接口和实现</strong>接口跟封装可以一起介绍，可以理解为你在使用冰箱的时候，不需要知道冰箱怎么制冷的。只需要插电和开关冰箱门就好了。</p>
<p>冰箱把制冷的细节都封装在了里面，给你留下了开关和插电的接口冰箱这个「类」对应的他的开关接口，这之间的关系就是实现，<strong>使用空心虚线箭头标识。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/QNjCCfojjOvWF6lb6mOJ.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="630" height="342" referrerpolicy="no-referrer"></p>
<p><strong>依赖</strong>用虚线单箭头表示，一个类使用了另一个类，比如在设计报表类系统时，会存在类似的关系。“展示报表”的功能，使用了“报表”这个类，有一个前置的逻辑，形成了依赖关系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/uXohx229W0LtnIrKQD4D.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="632" height="351" referrerpolicy="no-referrer"></p>
<p>最后就是类图里的最后一块<strong>聚集和组成</strong>这其中<strong>有点形似与混合物 与 化合物的区别。</strong>聚集，用空心菱形剪头，从部分指向整体，一种混合物的关系组成，用实心菱形剪头，代表强聚集关系，类似化合物的关系，桌子由桌面和桌腿组成。<strong>当然这只是为了没接触的同学好理解，如果有ETC精请克制自己不要自动抬杠……</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/RPTLUoGRJT46UqOvBf2g.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="646" height="331" referrerpolicy="no-referrer"></p>
<h3>2. 结构元素-用例图</h3>
<p>篇幅最长的类图介绍完了，接下来介绍一个也很常用的用例图，相对简单很多，跟画画一样，一个小人儿和一大堆气泡发生了连线的关系用例图可以在设计系统或者需求的时候，理清楚实际的场景，排坑。比如设计某功能时，总会有一些操作场景被遗漏，导致进入测试阶段中了，才发现有问题，要修补。</p>
<p>使用用例图，能很大程度上在设计阶段避免这种情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/0BO1Ss6ZcAbQjPIa5aMQ.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="660" height="371" referrerpolicy="no-referrer"></p>
<p>小人儿就是<strong>参与者</strong>气泡就是<strong>用例</strong>二者之间使用依赖线连接， 上面可以标记<< include>> 或 << extend>><< include>>可理解为用例间包含的关系，一个用例包含了下一层级的用例。</p>
<p><strong><< extend>>可以理解为此用例还有其他场景可以使用，扩展出了一个入口用例图只用来标识参与者和用例的关系，并不代表先后顺序。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/ohc607fdVOwwUZL2WYjM.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="658" height="177" referrerpolicy="no-referrer"></p>
<p>用例图在交付时通常给客户和开发组参考，每个用例图的场景描述至少占一页文档，包含：·发起用例的参与者·用例的假设条件·用例的前置条件·场景中的步骤·场景完成后的后置条件·从用例中获益的参与者。</p>
<h2 id="toc-5">五、行为元素</h2>
<p>终于大半篇幅讲完了结构元素，本节开始讲行为元素了，如果小伙伴们看麻了，可以收藏后面继续看~</p>
<p>行为元素对于产品同学来讲，基本是不陌生的，如果经常绘制业务流程图的话，会发现有很多一致的地方，很正常，都是团队的沟通工具嘛。</p>
<h3>1. 行为元素-状态图（状态机图）</h3>
<p>这种图在制作大型业务系统的时候，肯定会用到，比如我在设计CRM系统的时候，里面的商机就会有多种状态流转，就用到了这个图。给研发兄弟看，也会沟通的很顺畅，因为研发在实际工作中会频繁用到这里，他们基于这些状态去设计代码层面的调用逻辑。便于他们设计的时候提前规划，提高研发的效率。</p>
<p>研发最怕的，是做一半了中途改了基础底层状态的设计，分分钟掀桌子状态图的定义，可以说是对象改变了自己的状态，以响应事件和时间的流逝，比如灯的开与关。</p>
<p>状态图和类图的差别，是状态图针对的是单个对象来建模，类图可以针对一组类来建模绘制方法，圆角矩形代表一个状态，状态间带箭头的实现代表状态的迁移，箭头指向目标状态。实心圆点代表状态转移的起点，牛眼圆圈代表重点记不住那么多没关系，有专门的工具，跟visio一样，直接找来拖就行了，文章末尾会介绍绘制工具。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/agxfbvUvk8Lxf6E7dUCv.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="661" height="191" referrerpolicy="no-referrer"></p>
<p>下图是基于工单类的审批流程绘制的状态图。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/WlzjYwM5kVeelNc5B6Dy.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="620" height="336" referrerpolicy="no-referrer"></p>
<h3>2. 行为元素-时序图</h3>
<p>时序图，也叫顺序图，强调了时间维度，时序图的关键思想是强调了对象之间的交互按照特定时间发生，这些特定时间的交互序列，从开始到结束需要一定的时间。时序图通常用对象标识，从每个对象下方延展出一条生命线，一个时序图可以用单个或者多个如下单元组成。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/qhWmp9WFU0LV0QjXlhoq.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="701" height="137" referrerpolicy="no-referrer"></p>
<p>每个线程对象之间可以用消息通信，有两类一类消息叫调用，这是一个来自消息发送者对象的请求，它被传递给消息的接收对象，请求接收者对象执行某种操作。通常，需要发送者等待接收者执行，等待反馈，这种消息又叫做同步消息。</p>
<p>如下图，带有实心箭头的实线表示发送的消息，带有线状箭头的虚线表示返回消息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/DYQw0jqXyDTy97DiUhJW.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="554" height="150" referrerpolicy="no-referrer"></p>
<p>另一类消息叫做异步消息，这种机制下发送者把控制权交给了接收者，并不等待操作完成，这种消息用带有线状箭头的实线表示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/XEQLbx38ClRYbIr05x2O.jpeg" alt="产品经理的思考利器——UML（7000字长文）" referrerpolicy="no-referrer"></p>
<p>时序图跟跨职能流程图有些许相似，不过时序图可以更清晰的展示每个线程的动作顺序，以及线程之间的通信关系，如果是用跨职能流程图的方式来绘制，就不便于展示每个线程之间的多条通信了依然拿请假的流程举例，如图。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/C67WiTokKATAieefnSQd.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="534" height="286" referrerpolicy="no-referrer"></p>
<p>时序图还有帧化的概念，不过对于非研发工作来讲，没必要学习，基本用不到。不再赘述。</p>
<h3>3. 行为元素-活动图</h3>
<p>终于到了最后的类型了！活动图，用圆角矩形表示，与状态图不同的是，活动图的图例更接近椭圆。一个活动的处理一旦完成，就自动引起下一个活动发生。</p>
<p>状态图侧重于描述对象的状态变化，活动图侧重于描述活动，与业务单线流程图大多数逻辑类似，不过区别是活动图更适合展示判断过程，和并发路径。如果用基础的单线流程图标识，会不太直观比如判断是类似的表示方法。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/gEsn7msu33zTmBFLw3JN.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="540" height="267" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">并行路径的表示方法</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/hP9KJju9F9C9CIJJTSBE.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="619" height="215" referrerpolicy="no-referrer"></p>
<p>如果日常工作中使用流程图较多，也不必非要用这个，UML本质目的是快速沟通，能沟通清楚就行。</p>
<h2 id="toc-6">六、实战应用</h2>
<p>下面讲下我平时是怎么应用的，有两类案例，一类是研究一个系统，多数的时候是凭借兴趣研究的，感觉很有意思。另一个是工作里实际使用时展示的。</p>
<h3>1. 拆解与理解saleforce</h3>
<p>saleforce是CRM业界非常知名的一个产品，因为这个系统太过于庞大，UML的类图是快速理解的一个利器。此时应用UML不是还原到如何实现，而是为了理解它是怎么设计的。通过demo很难有机会能接触到更深层的实现细节。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/dm4uS0VzMjElsyUo8aiJ.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="650" height="384" referrerpolicy="no-referrer"></p>
<h3>2. 应用到工作</h3>
<p>在设计内部BI系统时，用到了类图，和用例图。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/Eed7u3CCzvoPTUgznvtq.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="631" height="522" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/G47IXwZb2DlsqaoTmD9r.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="690" height="573" referrerpolicy="no-referrer"></p>
<p>在设计CRM系统时，商机（例子）状态的流转图。CRM的设计，我会单起一系列文章讲。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="产品经理的思考利器——UML（7000字长文）" src="http://image.woshipm.com/wp-files/2021/11/BmsoAWnmAipJZldU6DqI.jpeg" alt="产品经理的思考利器——UML（7000字长文）" width="595" height="988" referrerpolicy="no-referrer"></p>
<p>除了这些还有很多应用，不过都差不多，应该可以给大家足够的帮助了。关于UML的介绍内容，就到此结束，下面我做下对应的答疑。</p>
<h2 id="toc-7">七、高频的疑问解答</h2>
<p>在调研UML是否值得学习的时候，我也会经常看到这样那样的问题，比如：</p>
<p><strong>我看完了，真的有必要学吗？研发不看怎么办？</strong></p>
<p>我的个人建议是，如果自身喜欢这方面的思考，可以凭兴趣去学；如果是B端从业且想继续发展的业务产品，建议去学，学了以后会有如虎添翼的功效，不过学习需要时间，建议收藏，或者转发给小号后续常看，我平时看到东西也这么干哈哈。</p>
<p>最好能买书学，更系统UML本质还是沟通工具，可以跟研发去协商，看团队更倾向用什么方式沟通，UML只是一种，如果有别的更合适的表示方法，能把逻辑梳理清楚，歧义消除干净，最好不过了。</p>
<p><strong>UML和数据建模是否有关系？</strong></p>
<p>跟研发同事交流过，他们说UML其实就跟JAVA编程过程中的思考很接近，不断抽象和建模，平时也会用到。数据库建模与UML有一定的联系，数据库建模的过程是逻辑层到物理层的逐层过程，都是构造模型，但侧重点不一样，数据库建模侧重数据层面逻辑效率，模型可用性等等。</p>
<p><strong>UML之后如何使用？</strong></p>
<p>除了上面的那些基本功能点以外，使用UML的本质目的就是为了多方理解，尽管UML有一些法则，也不要被禁锢，<strong>能达到沟通顺畅无歧义的目的，就足够了。</strong></p>
<p><strong>画图使用什么工具呢？</strong></p>
<p>starUML。win/mac平台都有，win的平台有个版本很复古，但是功能很完善。mac有starUML4.0的版本，颜值很高，但是感觉画起来没win的好用。</p>
<p>大家可以百度搜下。·Visio。可以画的图很多，包含了UML的基础图例，不过看个人习惯，我Visio和starUML都用，Visio常用来画流程·其他有用的也可以推荐下，工具嘛，趁手就行。</p>
<p><strong>有哪些书籍推荐？</strong></p>
<p>UML基础、案例与应用（入门），大象UML（进阶），大话设计模式（感兴趣可以看），系统架构（值得反复长期啃，我确实还没看完，太大了，不过是本神书）另外其他的书，可以白嫖微信读书无限卡，香滴很！</p>
<h2 id="toc-8">八、结语</h2>
<p>未来，我会出一些关于业务系统的相关文章，尽量大白话，可能有些大佬看着文字会评价我的思考肤浅，但能有人听懂和交流，才是我的初衷。</p>
<p>我期望我的些许产出，可以让新手产品同学们不再像我当年那样随机漫步，能快速度过无人带领自己摸索的成长期，我愿意做一块铺路石~肝了这么久，不知道你们学废了没有，如果有收获，还请点个赞鼓励一下我~哈哈哈感谢感谢。</p>
<p> </p>
<p>作者：罗文正雄；公众号：罗文正雄</p>
<p>本文由 @罗文正雄 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Pixabay，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5215683" data-author="38624" data-avatar="https://static.woshipm.com/APP_U_202101_20210116211936_8030.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            