
---
title: 干货！一文解决产品经理对UML的全部疑问
categories: 
    - 新媒体
    - PMCAFF - 今日推荐 / 精选
author: PMCAFF - 今日推荐 / 精选
comments: false
date: Thu, 11 Mar 2021 20:17:29 GMT
thumbnail: 'http://img.pmcaff.com/b2461c428ab9bf5f429f8302835d0c8b-picture'
---

<div>   
<pre><style>
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
</style><p><span style="color:rgb(88,88,88);"><br>第一次接触UML</span><span style="color:rgb(136,136,136);">（Unified Modeling Language统一建模语言）</span><span style="color:rgb(88,88,88);">是在2年前，当时正在学项目管理。当书中讲到系统设计阶段时，作者引入了UML的相关内容，但是2年过去了，笔者对UML的印象也就只停留在概念和样式上，并没有进行实操理解。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><blockquote><span style="color:rgb(136,136,136);">统一建模语言(Unified Modeling Language，UML)是一种为面向对象系统的产品进行说明、可视化和编制文档的一种标准语言，是非专利的第三代建模和规约语言。UML是面向对象设计的建模工具，独立于任何具体程序设计语言。</span><br></blockquote><p><span style="color:rgb(88,88,88);">​<br></span></p><p><span style="color:rgb(88,88,88);">在这2年期间，在笔者PRD中出现频率最多的就是<strong>流程图（+泳道）以及状态机图</strong>。对这些图的使用和理解都是凭直觉和经验，并没有过多去深挖他们的区别和原理，也没有想过是否还有其他能够更好表述自己思想的图。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">巧合的是，在最近正在上的产品训练营课中，再次听到主讲老师讲到了他使用UML来向工程师描述需求的案例，同时课堂中的一些引导和实操也让我对「系统了解和学习UML」产生了好奇心。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">于是，在经过学习后笔者整理输出了下面4个产品经理对UML最关注的4个问题：</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><ul><li>产品经理是否有必要学习UML？<br></li><li>如何学习UML？<br></li><li>如何选择哪种图来表达？<br></li><li>如何把控画图的粒度？<br></li></ul><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">话不多说，下面将就上述4个问题进行一一解答。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h1 style="margin-left:8px;text-align:center;"><strong><span style="color:rgb(123,12,0);">一、产品经理是否有必要学习UML？</span></strong></h1><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">答案是肯定的，但是没有必要全学。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">UML，表面上是一种以图来展示的语言，但其本质是一种看待事物的思想和角度。通过UML，我们能够拥有一个抓手，快速去挖掘到事物背后的属性、特征和行为。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">举个例子，当你要向公司请假时，需要先向leader沟通审批；leader同意后，再将请假条拿给HR存档；财务则要在核对上班和请假天数后计算出你的当月最终工资。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">这件事涉及到了时间、请假、4个岗位部门的人、请假条、薪资等多个角度的内容，其中有人、有物、有事，怎样才能有一个抓手让我们快速去捋清楚这件事的全貌和特征呢？</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">我们最惯用的就是流程图，而流程图就正和UML中的活动图不谋而合，通过时间的先后顺序去捋清楚事件（活动）的时间线及逻辑，这是我们最常惯用的一种角度；</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">但是，在这种角度下，如果我想快速了解请假这整件事的当前状态和状态之间的变换方式时，就需要依赖UML中的状态机图，这样我们就能快速了解做哪些事可以发起请假、哪些事会被leader拒绝等。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">由UML中的活动图和状态机图举例来看，UML能够赋予我们看待事物的不同角度，帮助我们快速找到问题和事物的本质。看到这里，是不是就和我们进行需求分析的目标有共同之处了？</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">因此，个人是比较推荐产品经理去学习一下UML的，我们不仅可以用UML对事物的本质进行更多视角的解读，也可以借用它在我们和工程师之间搭建一座沟通的桥梁，更好地向工程师表达和阐述我们的产品和思想。</span></p><h1 style="margin-left:8px;text-align:center;"><strong><span style="color:rgb(123,12,0);">二、如何学习UML？</span></strong></h1><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">UML总共有十多种图，包含类图、活动图、状态机图、顺序图、用例图、部署图、构建图、包图、时序图、交互概览图、组合结构图。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">我们是不是要全部掌握呢？</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">当然不是！作为一般的业务型产品经理，只需要掌握类图、活动图、状态机图、顺序图和用例图即可。这5种图能够帮助我们更好地进行问题解构和需求分析，也是没有技术背景的产品经理很好掌握的5种图。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">一般我们会把UML图分为结构型图和行为型图2种。结构型图描述的是事物及事物之间的结构，这个结构在某段时间内应该是稳定的、静态的；而行为图则描述的是事物的行为，是动态的。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">在这5种图中，类图是其中唯一的一种静态结构型图，其余4种都是行为型图。</span><span style="color:rgb(88,88,88);">下面我们逐一来和大家讲解一下这5种图：</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h2 style="margin-left:8px;"><strong><span style="color:rgb(123,12,0);">2.1  类图 class diagram</span></strong></h2><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">在这5种图中，类图可谓作是其他图的基础。因为每个系统都涉及到了大量的人、事、物，这些抽象出来的人事物或者概念就是我们所说的类。而任何UML图都需要建立在有概念和类的基础上才能展开结构和行为的描述。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">其实在了解类图时，我不自觉联想到了之前学习数据库时的E-R图</span><span style="color:rgb(136,136,136);">（Entity-Relationship实体-关系图）</span><span style="color:rgb(88,88,88);">，这里类和实体的概念其实是有一些相似之处的。类图也是一种帮助我们快速提炼出业务概念并识别出其属性和关系的工具。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">类的属性我们这里不过多展开，下面重点来了解下类之间的关系。常见的类与类之间的关系有：包含、继承、依赖，其中包含又分为聚合</span><span style="color:rgb(136,136,136);">aggregation</span><span style="color:rgb(88,88,88);">和组合</span><span style="color:rgb(136,136,136);">composition</span><span style="color:rgb(88,88,88);">。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h3 style="margin-left:8px;"><strong><span style="color:rgb(88,88,88);">包含</span></strong></h3><p><span style="color:rgb(88,88,88);">类的包含关系分为聚合aggregation和组合composition2种，从中文上看起来有些不直观，我们直接用图说话。</span></p><p><span style="color:rgb(88,88,88);">下图为聚合关系，其中A只能属于B一个类，那么我们称A和B是聚合（强包含）关系。例如A员工只能属于某一个部门。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p style="text-align:center;"><img src="http://img.pmcaff.com/b2461c428ab9bf5f429f8302835d0c8b-picture" alt="b2461c428ab9bf5f429f8302835d0c8b-picture" coffee-w="300px" coffee-h="300px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:center;"><span style="color:rgb(136,136,136);">（聚合关系）</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">而这张图中A既可以属于B，也可以属于C，二者不是强包含关系，则他们为组合（弱包含）关系。例如A员工既在B部门工作，又兼任C部门的部分工作。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p style="text-align:center;"><img src="http://img.pmcaff.com/59c45b947a62bfaaa1abbce8b3654c04-picture" alt="59c45b947a62bfaaa1abbce8b3654c04-picture" coffee-w="600px" coffee-h="300px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:center;"><span style="color:rgb(136,136,136);">（组合关系）</span></p><h3 style="margin-left:8px;"><span style="color:rgb(88,88,88);"><br></span></h3><p><span style="color:rgb(88,88,88);"><br></span></p><h3 style="margin-left:8px;"><strong><span style="color:rgb(88,88,88);">继承</span></strong></h3><p><span style="color:rgb(88,88,88);">继承关系指A继承了B的属性，但同时也有自己特有的特点。例如，老师和学生都是「人」，但是老师和学生各自有各自的特性，那么他们就和「人」之间是一种继承关系。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">继承关系有助于我们抽丝剥茧地观测到事物之间的本质，是一种进行业务提炼的重要手段。</span></p><h3 style="margin-left:8px;"><strong><span style="color:rgb(88,88,88);">依赖</span></strong></h3><p><span style="color:rgb(88,88,88);">依赖关系指A需要B协助才能完成某事，但并不是必须和赖以生存的关系。就像我们开会依赖于使用投影仪一样，但没有投影仪我们也照样完成会议，只是可能没那么方便。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">下面，我们用一个例子来完整表示一下类图。以大家阅读这篇文章为例，这次阅读事件所涉及到的类有：读者、作者、文章、微信公众平台。</span></p><p><img src="http://img.pmcaff.com/1c5c883d5abc14a9e8465f74e0de764c-picture" alt="1c5c883d5abc14a9e8465f74e0de764c-picture" coffee-w="661px" coffee-h="281px" coffee-format="png" referrerpolicy="no-referrer"></p><ul><li>作者将文章发表在微信公众平台<br></li><li>读者前往微信公众平台阅读文章<br></li><li>作者可以发布0到多篇文章，但一篇文章仅属于1个作者<br></li><li>读者也可以阅读0到多篇文章，1篇文章也可以被0到多个读者阅读</li></ul><p><span style="color:rgb(88,88,88);"><br></span></p><h2 style="margin-left:8px;"><strong><span style="color:rgb(123,12,0);">2.2 活动图 activity diagram</span></strong></h2><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">活动图应该是这5种图中最不需要多废口舌的，因为它和我们常见的流程图很像，就是按照时间顺序将活动的逻辑整理出来。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">下图就是一个简单的审批活动图，通过该图我们能清晰地了解一个完整的审批流程和逻辑。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p style="text-align:center;"><img src="http://img.pmcaff.com/a4331894e4c2cb18d007e01a05a9ee10-picture" alt="a4331894e4c2cb18d007e01a05a9ee10-picture" coffee-w="471px" coffee-h="441px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:center;"><br></p><p><span style="color:rgb(88,88,88);">看到这里，自然有人会问，这些实心圆圈、圆角矩形等的具体UML绘图语法必须要全部掌握吗？按下图这样「原始」的画法去画有没有问题？</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p style="text-align:center;"><img src="http://img.pmcaff.com/94c2e71fe7df949383367ca5c7686f9f-picture" alt="94c2e71fe7df949383367ca5c7686f9f-picture" coffee-w="471px" coffee-h="441px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:center;"><br></p><p><span style="color:rgb(88,88,88);">其实，在日常的工作中，基本没有工程师会太过于纠结你的绘图语法正确与否。因此，形式和语法不用太过学院派，只要能够向读者清晰表达和传递意思即可。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h2 style="margin-left:8px;"><strong><span style="color:rgb(123,12,0);">2.3 状态机图 state machine diagram</span></strong></h2><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">活动图是将流程分解为一个个的活动，通过活动的先后顺序来展示流程；而状态机图则是围绕一个事物的状态为中心来讲述流程。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">还是以审批为例，这次我们围绕<strong>审批单</strong>为中心来描述流程。假设审批单有待审批、已撤销、审批通过和审批拒绝这4种状态，那么我们绘制的状态机图如下：</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p style="text-align:center;"><img src="http://img.pmcaff.com/bfaedd8b689380e49e15c970522f620f-picture" alt="bfaedd8b689380e49e15c970522f620f-picture" coffee-w="621px" coffee-h="451px" coffee-format="png" referrerpolicy="no-referrer"></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">通过这个审批单的状态机图，我们能够清晰地看出审批单的状态以及影响其状态的原因和活动。在一定程度上，它帮助我们减轻了设计审批单的工作量，也帮助工程师对审批流程有更好的理解。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h2 style="margin-left:8px;"><strong><span style="color:rgb(123,12,0);">2.4 顺序图 sequence diagram</span></strong></h2><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">顺序图，有时候也会被混称为时序图，中文名字大家可以不用纠结，重点记住sequence这个单词就好。</span></p><p><span style="color:rgb(88,88,88);">在前述的活动图中，虽然流程较为清晰，但我们很难清晰地定义角色的具体职责边界和通信交互，而顺序图则帮助我们补充到了这一点。</span><br></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">下面，我们尝试一下从顺序图的角度来描述审批流程：</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><img src="http://img.pmcaff.com/352db673b8dc287bcb50c11f0cc1102f-picture" alt="352db673b8dc287bcb50c11f0cc1102f-picture" coffee-w="731px" coffee-h="631px" coffee-format="png" referrerpolicy="no-referrer"></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">从上图中能够很明显的看出销售负责什么、系统负责什么、而管理员又负责什么；同时也能清晰看出这3个角色各自的输入输出。由此可见，顺序图能够帮助我们逐层拨开一个复杂业务的内部运作。</span></p><p><br></p><h2 style="margin-left:8px;"><strong><span style="color:rgb(123,12,0);">2.5 用例图 use case diagram</span></strong></h2><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">对于产品经理而言，用例图应该也是相对比较容易掌握的一种图。</span></p><p><span style="color:rgb(88,88,88);">用例图是以操作者的角度出发，去看这个产品能够带给他哪些价值、支持他去操作和查看哪些东西。继续沿用审批举例：</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><img src="http://img.pmcaff.com/bad2ecdef3834335d212212ad563f6f5-picture" alt="bad2ecdef3834335d212212ad563f6f5-picture" coffee-w="703px" coffee-h="711px" coffee-format="png" referrerpolicy="no-referrer"></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">如上图所示，我们能够清晰地看出销售能够发起审批、撤销审批和编辑审批，管理员能够查看和执行审批。换言之，用例图能够帮助业务方、产品和工程师以最直观的角度认识到产品能给客户带来什么价值，产品在帮助客户做什么事。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">用例图关注的是系统的外在表现、系统与人的交互、系统与其他系统的交互。用例图没有太多的技术用语和实现细节，在需求初期对团队和客户都是一种非常好的沟通工具。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h1 style="margin-left:8px;text-align:center;"><strong><span style="color:rgb(123,12,0);">三、如何选择哪种图来表达？</span></strong></h1><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">UML有这么多种图，如何去快速选择最适合自己当前需要的图呢？</span></p><p><span style="color:rgb(88,88,88);">笔者的建议是按照</span><span style="color:rgb(123,12,0);"><strong>「类图-用例图-状态机图/顺序图/活动图」</strong></span><span style="color:rgb(88,88,88);">这样的顺序去使用。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">在需求前期，我们可以先使用类图来识别类、类的属性和关系。就像读一段英语句子时，老师告诉我们要快速抓住句子的主谓宾结构，从而更快地理解句子意思。类图也是一样，在我们两眼一抹黑的时候，能够先让我们了解到这件事中牵扯到的所有人事物，之后我们才能根据这些「素材」去展开后续的分析。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">接下来，我们可以通过用例图去和客户、工程师沟通产品的价值和能做的事，以一个粗粒度的角度框定产品范围，看当前的范围是否能够满足客户需求，帮助我们确立能够开发出有价值有意义的产品。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">同时借助用例图，产品也能够向研发积极传递当前所做产品的价值，避免工程师因功能价值理解不足而产生开发受阻的问题。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">最后，我们就要在状态机图、顺序图、活动图中去做抉择来描述具体流程了。这3种图各自有各自的优缺点，下面给出一些选择上的参考建议：</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h3 style="margin-left:8px;"><span style="color:rgb(123,12,0);"><strong>顺序图的特点</strong></span></h3><p><span style="color:rgb(123,12,0);"><strong><br></strong></span></p><ul><li>强调角色之间的交互，信息传递很明确<br></li><li>强调按时间顺序分别发生了什么事情<br></li><li>不太适合表达复杂的特殊流程（循环分支、条件分支、可选分支）<br></li></ul><p><span style="color:rgb(88,88,88);"><br></span></p><h3 style="margin-left:8px;"><span style="color:rgb(123,12,0);"><strong>活动图的特点</strong></span></h3><p><span style="color:rgb(123,12,0);"><strong><br></strong></span></p><ul><li>强调每个角色做了什么事情，这些事情的先后关系<br></li><li>适合表达各种特殊流程，如分支、并发等<br></li></ul><p><span style="color:rgb(88,88,88);"><br></span></p><h3 style="margin-left:8px;"><strong><span style="color:rgb(123,12,0);">状态机图的特点</span></strong></h3><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><ul><li>事情围绕某东西开展<br></li><li>该东西有不同的状态，状态会因为发生了一些事情而变化<br></li></ul><p><span style="color:rgb(136,136,136);">（来自《火球uml》）</span></p><p><span style="color:rgb(136,136,136);"><br></span></p><p><span style="color:rgb(88,88,88);">从上述三个点中，我们能够看出这3种流程分析图之间的区别，在使用时加以选择即可；同时也不要限制自己只能选择一种，完成可以同时使用多种图来从多个角度分析问题。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);"><br></span></p><h1 style="margin-left:8px;text-align:center;"><strong><span style="color:rgb(123,12,0);">四、如何把控画图的粒度？</span></strong></h1><p><strong><span style="color:rgb(123,12,0);"><br></span></strong></p><p><span style="color:rgb(88,88,88);">画图相对是一个主观性比较高的行为，看似掌握了，但实操中往往会容易遇到粒度把控的问题：要不粒度过细了、什么细节都想往图上添；要不就是粒度不一致，这一分支的粒度很粗、而另一粒度的分支则很细，让读者看得云里雾里。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">对于新手而言，粒度把控是一个需要持续练习后才能逐渐掌握的难点。那么，我们应该如何掌控画图的粒度呢？</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><ul><li>明确该图背后想表达的内容和重点，以目标为导向，看看自己的图能否表达出对方想要理解到的内容<br></li><li>先用宏观的绘制一版粗粒度的图出来，随后再进行粒度的逐层细化<br></li><li>画完后可以多与读者（工程师）交流，希望对方从阅读角度提出改善建议，帮助自己持续贴近粒度的最佳把控点<br></li></ul><p><br></p><p><span style="color:rgb(88,88,88);">看到这里，是不是觉得UML也没有那么地高深和难懂，不过是一种看待事物的角度和思想罢了。本文没有太细讲绘图语法，如果大家有兴趣继续深挖和学习，推荐几本还不错的书《火球UML》《大象UML》《UML和模式应用》。其中，《火球UML》更适合缺少技术背景的产品经理来看，基本可以无障碍学完。</span></p><p><span style="color:rgb(88,88,88);"><br></span></p><p><span style="color:rgb(88,88,88);">u1s1，最好的UML学习方式就是边学边画，如果你跃跃欲试，那就快找一个案例上手试试吧。</span></p></pre>
  
</div>
            