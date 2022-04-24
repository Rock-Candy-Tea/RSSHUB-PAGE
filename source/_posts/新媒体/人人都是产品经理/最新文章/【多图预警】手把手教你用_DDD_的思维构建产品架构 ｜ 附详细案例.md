
---
title: '【多图预警】手把手教你用_DDD_的思维构建产品架构 ｜ 附详细案例'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/u6xoZr09NSBbT3WvlriT.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 24 Apr 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/u6xoZr09NSBbT3WvlriT.jpg'
---

<div>   
<blockquote><p>编辑导语：逻辑思维对于构建产品架构十分重要，产品架构设计是一个系统化的大工程，对于个人能力也有一定的要求，本篇文章作者分享了用“DDD”的思维来构建产品架构，结合作者的设计理念总结出了一套完整的方法论，一起来学习一下吧，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5409828 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/u6xoZr09NSBbT3WvlriT.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近带的产品经理请教我如何思考并绘制产品架构图，他在网上看了一些文章，要么大段概念介绍，无法实操，要么不好理解，所以想问问我有没有什么经验。</p>
<p>其实关于产品架构的设计，我自己基于“领域驱动设计（DDD）”理念，创造了一套“一二三四”模型，不知是否具有广泛性和应用性，遂整理成文，并附加案例，供大家讨论并验证。</p>
<h2 id="toc-1">一、前言</h2>
<p>作为产品经理，只专注于功能设计是不够的，需要清楚地了解产品的定位、要解决的问题、系统的组成、每个系统承担的角色以及未来的发展，因此对产品的架构能力必不可少。</p>
<p>当我刚开始负责一个产品的时候，对于产品架构的要求不是那么明显，觉得那只是换了一种漂亮的形式来展现系统中的功能。而且也不注重前期的规划，往往是要做相关的材料，才根据现有的系统反推架构。</p>
<p>但是随着产品的发展，出现了一些之前没有考虑到的需求，此时再去加新功能，难点不在于要怎么设计，而是如何兼容已有的设计，久而久之，产品逻辑会越来越复杂，牵一发而动全身，最终只能重构，不管是对设计还是对开发都是如此。</p>
<p>当我开始负责一条业务线的多个产品的时候，又发现不同产品之间会有相同的功能模块，但是他们是分别开发的，可能逻辑不同，也可能技术方案不同，造成这样原因有很多，比如沟通问题、制度问题等，但最重要的还是由于对新需求“打补丁”的方式导致产品越来越臃肿，一些共用的模块无法抽离出来，所以形成了重复造轮子的情况。</p>
<p>以上，让我越来越明白前期设计好产品架构的重要性，同时纠正了我的一个思想：<strong>产品架构设计是一个系统性的工程，不是随便罗列功能模块就能完成的</strong>。</p>
<p>我开始研究方法论，看了一些文章，每个人都有每个人的看法，但尚没有一种权威的理论作为支撑。</p>
<p>于是我尝试跳出产品范畴，去看看旁边比我们先发展好几十年的开发领域，试图从中找到一些灵感。</p>
<p>近年来技术架构都在围绕<strong>“高内聚低耦合”</strong>的思想不断完善，从MVC、三层架构到微服务、中台、DDD，无一例外。</p>
<p>其实对于产品架构来说也是一样，在设计系统时不仅要考虑全面，还要考虑未来的可拓展性。</p>
<p>本文介绍了我在研究“DDD”后，借助其通过分解控制复杂性的思想，并结合自身经验总结的一套构建产品架构的方法论，我将其命名为<strong>“一二三四”</strong>模型。</p>
<h2 id="toc-2">二、一个【关键链路】</h2>
<p>客观世界中，存在能量守恒定律，一种物质通过周围环境的影响会变成另一种/几种物质，但总能量不会变。如果我们把环境因素想象成一个黑盒，那么可以抽象出下图模型：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/D1eb1V25rcTlBF7rSRdc.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="308" referrerpolicy="no-referrer"></p>
<p>同理，我们将互联网产品也想象成一个黑盒，它并不会创造新事物，而是通过将事物<strong>线上化</strong>和<strong>协同化</strong>，并通过<strong>数据智能</strong>的方式加速“输入→输出”这一过程，从而为用户提升效率、创造价值。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/eQpJUc4wFtPYqmrVuY3D.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="368" referrerpolicy="no-referrer"></p>
<p>任何一个产品不管它现在发展得有多庞大，都有且存在着一条关键链路，用来连接各实体。</p>
<p>比如在没有滴滴前，我们是靠运气打车，乘客和司机之间不存在其他的联系。</p>
<p>而滴滴是将周围的司机、周围的车辆和需要打车的乘客都联系在了一起，从而提升了打车体验。</p>
<p>尽管现在的滴滴已经不止“打车”业务，还发展了货运、顺风车、代驾、共享自行车、金融等其他业务，但都是在这条关键链路上，对输入和输出进行扩展。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/WzqFtQKSDqJxretYb6io.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="558" height="286" referrerpolicy="no-referrer"></p>
<p>所以在绘制产品架构图之前，应该先思考：<strong>你所负责的产品，它的核心链路是什么，连接了哪些实体？</strong></p>
<p><strong>这样做有两个好处：</strong></p>
<ol>
<li>避免其他干扰，直击产品核心价值，类似于“第一性原理”；</li>
<li>不需要对业务很熟悉，只要有产品定位，就可以得到。</li>
</ol>
<p>例如在疫情当下，高校无法组织线下考试，因此需要做一个线上考试平台，即便你以前没有接触过教育信息化行业，你也知道考试的输入是考生、考官和试卷。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/dS1fIKodhQ35xLmUNTyC.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="367.2" referrerpolicy="no-referrer"></p>
<p>值得注意的是，产品的核心链路不是一成不变的，它会随着产品定位的变化而变化，比如下图是小红书历次slogan的变化，每一次定位的变更都意味着输入和输出的调整。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/qSq3pBd9RzOQ1sWPTo1Y.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="409.6" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、两个【思维】</h2>
<p>找到了核心链路，接下来就是利用“<strong>分解思维</strong>”对核心链路进行梳理，并利用“<strong>聚合思维</strong>”对系统进行构建。</p>
<h3>1. 分解思维——6W2H</h3>
<p>通过第一步，我们找到了与系统相关的、最直接的输入和输出实体，接下来就是分析实体与实体、实体与系统之间的联系。最全面且有效的方法就是6W2H：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/V8F5ybwEqcDQwj1GWauJ.png" alt width="570" height="259" referrerpolicy="no-referrer"></p>
<p><strong>1）分解输入</strong></p>
<p>回到线上考试系统，先按照上图的方法分析试卷：对于输入，我们要寻根溯源，思考它从哪来，如何来、与系统的关系等。</p>
<ul>
<li>what（属性）：试卷类型、分值；</li>
<li>who（谁参与输入）：出题老师；</li>
<li>when（什么时候输入）：考试前；</li>
<li>where（从哪来）：题目；</li>
<li>how（怎样输入）：创建、导入；</li>
<li>how much（数量受什么影响）：考试方式。</li>
</ul>
<p>通过以上分析，我们新发现了两个实体：出题老师和题目，需要继续对其分解至最细（见下图），过程中可省略一些维度（考生、考官也按照相同的办法进行分解，此处略）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/d0UverrQgmOMQANlqxcd.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="447.2" referrerpolicy="no-referrer"></p>
<p><strong>2）分解输出</strong></p>
<p>对于输出的分解思路会有少许不一样：我们要发散思维，思考它到哪去，如何去、如何扩大输出等。</p>
<ul>
<li>what（属性）：考试模式、考试时间、考试公告；</li>
<li>who（谁参与输入）：学校负责人；</li>
<li>when（什么时候输入）：考试前；</li>
<li>where（到哪去）：考场。</li>
</ul>
<p><strong>同样对找出的实体用相同方法进行再分解：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/bS10XrehsWyi8tqZ2Xpp.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="451.2" referrerpolicy="no-referrer"></p>
<p>至此，我们已经有了一个非常庞大的包含各角色、各事物及信息流转方向的对象关联画布。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/A0pZGUoyCg3K3zvnD7tE.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="791" height="286" referrerpolicy="no-referrer"></p>
<h3>2. 聚合思维——划分子域</h3>
<p>如果把我们面对的问题叫做“领域”，接下来，就要利用聚合的思想将一个或多个分散的实体封装为一个整体，使“领域”划分为几个“子域”（子系统）。</p>
<p>在领域驱动设计思想中，关于如何聚合可遵循以下四个原则：</p>
<ol>
<li>生命周期一致性原则</li>
<li>问题域一致性原则</li>
<li>场景频率一致性原则</li>
<li>聚合应尽可能的小原则</li>
</ol>
<p><strong>翻译成产品经理能听懂的话就是：</strong></p>
<ul>
<li><strong>实体A脱离另外一个实体B是否有存在的意义</strong>。例如如果没有考试，那么也就不存在考场</li>
<li><strong>不属于一个问题域的实体不能放在一起</strong>。比如在线监考和在线考场，根据生命周期原则可能会把这两个实体放在一个子域，因为有正在进行的考场才需要监考，但实际上他们解决的是两个不同领域的问题</li>
<li><strong>实体A和实体B能否被同时操作</strong>。以“试卷”、“考场”和“题目”为例，试卷包含了很多题目，这些题目会通过线上考场展示给每个考生。但是，站在操作层面，如果你要查看试卷列表，其实并不需要关心里面的题目，也不需要了解试卷所在的考场。尽管考务人员在编排考场的时候会查看题目以验证是否添加正确，但是大多数时候并不会去查看题目的分数，更不可能在创建考场的时候修改题目</li>
<li><strong>剩余的实体均划分成单独的子域。</strong></li>
<li><strong>好的划分可以让整个系统更灵活，拓展性更高。</strong>但是也不能一味追求分化，需要根据自己业务的实际场景去衡量。还是拿题目和试卷举例，如果你的业务比较简单，只需要对试卷进行操作，那么可以把题目和试卷划分为一个“试卷子域”；如果你的业务复杂，试卷既可以直接创建，也可以通过题目组卷，那么就需要划分为两个子域“题库子域”和“试卷子域”。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/Apa7HstjVKlFx2X8U2rh.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="653" height="108" referrerpolicy="no-referrer"></p>
<p><strong>因此对于线上考试平台可以做如下划分：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/7woq9OU0WbLyKX3dfODw.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="703" height="189" referrerpolicy="no-referrer"></p>
<h3>3. 分解思维——界限上下文</h3>
<p>在DDD中，对界限上下文的定义是：动态的业务流程被边界静态切分的产物。可以简单理解为再次利用分解思维把每个子域内涉及到的模块分解出来（此处不一一举例）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/DP2Au0DwBGiSw2V60MR6.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="364" referrerpolicy="no-referrer"></p>
<h3>4. 关于该步骤的答疑</h3>
<p>个人认为，本部分是本篇最重要也是最难理解的内容，因此有必要做一些解释。</p>
<p>我做过几个从0-1的产品，在进行用户调研前，首先会提前构思好可能的业务流程，再通过调研去验证和补充。因为没有相关业务经验，提前想的流程就会不全面，在这种情况下我开始寻找一种能够快速熟悉业务的方法。</p>
<p>经过不断总结经验，我发现任何一个产品都只会关注于一个基本问题，所以我直接从这个基本问题入手，找出相关的输入输出，再通过各个维度的不断分解，不仅能找到所涉及的所有实体和过程，同时还找到了他们之间的联系（业务流程）。各位看官不妨一试。</p>
<h2 id="toc-4">四、三个【完善】</h2>
<p>一个系统要想好用，有完善可拓展的功能只是第一步，还必须保证系统的稳定性和安全性。</p>
<p>这些不只是技术人员需要考虑的问题，产品经理也需要设计相应的产品架构、业务流程和功能逻辑来规避这些问题，有时甚至要牺牲用户体验。</p>
<p>在稳定性上，我们已经从业务的角度把一个大系统划分成了一个个高内聚、低耦合的小模块，接下来就要从运行维护的角度考虑如何检测预警以及出问题时的上报和解决。</p>
<p>此外还要找出所依赖的第三方服务，做好及时监控和应急方案，下图是我在网上找的通过设计维护稳定性的两个例子。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/LG0OGfuaUQmv5Qv33y5v.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="341.8000183105469" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/omAZsATTk2TNrZRORpwP.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="396" referrerpolicy="no-referrer"></p>
<p>同样在安全性上，除了要保证基本的数据安全、网络安全，产品经理还要做一些提升安全性的设计，如二次认证、CA加密、二级密码等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/MMMSAdmkiaiZF2jkROS7.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="366" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、四个【层次】</h2>
<p>至此，我们已经将整个业务划分出了多个领域（系统/模块），接下来就是纵向地对层次进行划分。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/iEWMSzYMttL0bNeS2YXN.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="468" referrerpolicy="no-referrer"></p>
<p><strong>这里先介绍一下产品层面的三层架构（虽不是但源于技术层面）：</strong></p>
<ul>
<li><strong>表示层：</strong>与用户直接接触的软件和硬件形态</li>
<li><strong>业务逻辑层：</strong>通过上述步骤划分出来的各领域模块</li>
<li><strong>数据层：</strong>使用到的数据库和数据服务</li>
</ul>
<p>这种架构本身没有什么问题，但是如果站在更高的视角看整个产品矩阵，你会发现随着业务场景越来越复杂，每条业务线都会变得非常臃肿，并且业务线与业务线之间会存在重复造轮子的情况。</p>
<p>比如公司要做一个企业培训的新业务，其中题库、试卷模块可以完全复用考试系统（类似于技术开发中的“组件”“中台”概念），但在现有三层架构下不好进行抽离。</p>
<p>因此在设计产品架构时，还要根据产品经理的经验，对业务依赖性不高，通用性、复用性较强的子域单独抽离出来，组成新的一层——通用业务层。</p>
<ul>
<li>表示层；</li>
<li>业务逻辑层；</li>
<li>通用业务层；</li>
<li>数据层。</li>
</ul>
<p>至此，我们将上述步骤得出的结果进行整理，再找设计同事帮忙美化一下，即可得到下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/KxoANi6QpO2sVbB1GkNz.png" alt="【多图预警】手把手教你用“DDD”的思维构建产品架构 ｜ 附详细案例" width="571" height="346" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、总结</h2>
<ul>
<li><strong>一个关键路径</strong>：找出核心的输入输出；</li>
<li><strong>两个思维</strong>：分解出各实体，聚合出各子域；</li>
<li><strong>三个完善</strong>：考虑稳定性、安全性、第三方服务；</li>
<li><strong>四个层次</strong>：按表示层、业务逻辑层、通用业务层、数据层划分。</li>
</ul>
<p> </p>
<p>本文由 @产品乱弹 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5408567" data-author="53146" data-avatar="http://image.woshipm.com/wp-files/2022/04/8y6kwQm5ZKujwmYa80IY.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            