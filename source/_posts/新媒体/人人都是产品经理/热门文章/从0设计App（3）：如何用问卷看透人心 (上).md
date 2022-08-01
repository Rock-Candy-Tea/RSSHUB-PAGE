
---
title: '从0设计App（3）：如何用问卷看透人心 (上)'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.woshipm.com/wp-files/2019/08/31uin8uRVXtMJNz3gV9k.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 16 Aug 2019 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2019/08/31uin8uRVXtMJNz3gV9k.jpg'
---

<div>   
<blockquote><p>如果说市场分析和竞品分析你都觉得有点虚，那么用户调研就是真刀真枪到战场上了。我们要通过用户调研来验证自己之前的猜想是否真实，另外，用户调研也是产品狗日常的工作，如何做好用户调研是核心关键。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-2712759 aligncenter" src="https://image.woshipm.com/wp-files/2019/08/31uin8uRVXtMJNz3gV9k.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>笔者会从以下几个维度逐步拆开来写进程，慢慢形成一个系列。先前的文章可以在笔者的个人主页查看~</p>
<ul>
<li>一、市场分析篇：<a href="http://www.woshipm.com/pd/2697788.html" target="_blank" rel="noopener">市场分析（上）</a>；<a href="http://www.woshipm.com/pd/2697841.html" target="_blank" rel="noopener">市场分析（下）</a></li>
<li>二、竞品分析篇：<a href="http://www.woshipm.com/pd/2710311.html" target="_blank" rel="noopener">竞品分析；</a></li>
<li>三、<strong>用户调研篇</strong></li>
<li>四、需求管理篇</li>
<li>五、架构流程篇</li>
<li>六、原型设计篇</li>
<li>七、UI设计篇</li>
<li>八、PRD文档篇</li>
<li>九、开发管理篇</li>
<li>十、未完待续……</li>
</ul>
<p><strong>在此声明：本系列的产品内容原创且非商用，如有雷同，你抄我的。</strong></p>
<h2 id="toc-1">一、前言</h2>
<p>大家都知道产品经理日常要管理各种各样的需求。其中很重要的一方面便是用户调研。</p>
<p>无论是什么形式的调研，其目的只有一个：挖掘用户的需求!尤其是对于C端产品来说，用户体验的很大程度上基于是否GET他们的点（参考KANO需求模型）</p>
<p>形式有很多种，定性定量什么的，随便百度一下都能查到。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2019/08/fmpr062Bw0YeT5qEE6Tn.png" alt width="801" height="397" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来自：百度</p>
<p>笔者这次就通过2种主要的用户调研方式①问卷调查 ②线下访谈 来设计我们的App。这两种最常见的方式进行用户调研，一方面是验证在之前市场调研、竞品调研中的发现的机会点，另一方面是去感受用户视角下的需求（场景）。</p>
<h2 id="toc-2">二、要点解析</h2>
<p>用户画像（Persona），这个词大家应该不会太陌生。用户调研的其一功能就是为自己的产品建立典型的用户画像，产品初期大概是1~2幅画像就足够了。</p>
<p>做问卷调查的好处和坏处就不赘述了，还是挺明显的。我们就来说说如何设计一份问卷。依据刚刚提到用户画像，其实只要我们定义下来，用户画像包括什么，那么问卷的主干自然而然呼之欲出了。</p>
<p>先百度一下“用户画像”，如下图，我们能看到信息比较多和杂。实际中我们不需要画图，除非是路演或者汇报给Boss。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/8NXDOm0kDmrGX5ysX6SH.png" width="599" height="449" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来源：百度图片</p>
<p>那么用户画像包含什么信息呢？</p>
<p>根据笔者的拙见，一共有4个层面内容比较有用。</p>
<ol>
<li>基本属性：年龄、性别、职业、地域、家庭关系等；</li>
<li>经济能力：月收入、消费习惯、贷款情况（花呗也算）；</li>
<li>行为习惯：如：经常加班，喜欢周末团购等；</li>
<li>心理特征：如：贪小便宜、果断、上进勤奋等。</li>
</ol>
<p>包括一些行为标签，也可以依据这4个层面来打标签。</p>
<p>只要能够理清楚这4条，并在实际工作中不断去完善这4点，作为产品经理你会对用户有一种“掌控感”。</p>
<p>题外话：大数据的应用，物联网等等都让大公司拥有越来越完备的用户数据中心，是下个时代开启的钥匙。</p>
<p>另外，如果你想要美化，可以采取“用户故事”的方式，把上面4点串起来。更方便自团队中其他成员以及其他部门的同事理解。</p>
<p>好了，知道用户画像有哪些之后，我们就可以基于最核心的4条，根据自己的产品业务逐项开展设计问题！当你的画像出来后，其需求在过程中也会呼之欲出。</p>
<h2 id="toc-3">三、原始问卷</h2>
<p>接续回到我们的案例系列中，先直接抛出问卷。我们再一点一点拆开来讲解。</p>
<p>问卷原地址：<a href="https://www.wjx.cn/hj/xsenioks0ywsz2s2aveba.aspx" target="_blank" rel="noopener">https://www.wjx.cn/hj/xsenioks0ywsz2s2aveba.aspx</a></p>
<p>（建议大家粗略做一遍题目之后再继续看文章。）</p>
<h2 id="toc-4">四、问卷设计技巧</h2>
<p>刚刚我们提到了4点用户画像的要点，没错，但是这里一个非常重要的技巧，也是原则。</p>
<p>那就是顺序很重要。通过合理的顺序组织，渐进式问到用户的4个方向。</p>
<ol>
<li>开头鼓励；</li>
<li>设置用户筛选题；</li>
<li>挖掘用户行为特征；</li>
<li>挖掘用户消费特征；</li>
<li>询问基本信息。</li>
</ol>
<p>看到这里，你可能会有3个问题，</p>
<p>第一：为什么是这个顺序？</p>
<p>第二：怎么没有挖掘心理特征呢？</p>
<p>第三：什么叫用户筛选题？</p>
<p>先回答第一个问题：因为人有一种“禀赋效应”加持，即对自己投入的东西会更加不舍得放弃和更加珍惜。哪怕是做个问卷也是，必须形成前面的问题很轻松，很简单，没有侵略性(不问隐私）。</p>
<p>因此先挖掘用户行为特征是最简单的，比如“你平时早上吃什么？”“一周上几天班”这种可以马上想出答案的题。</p>
<p>做了一些题后，放弃的成本就比较大了，用户往往会继续填写完，一些比较敏感的问题就可以放置结尾。如消费情况和个人情况：“月收入范围”“还贷情况”。</p>
<p>第二个问题：因为心理特征要从行为特征上发现，你不能直接问，因为用户很可能也不知道自己的价值观，如果你问了，用户很可能随便选，或者按照“美好”或者“期望”的方向选，就会让蒙蔽你的判断。</p>
<p>题外话：<strong>弗洛伊德提出过“本我”“自我”“超我”的人格模型</strong>。正常人呢，在对外时，尤其面对陌生人，几乎都会尽量表现”超我”的一面。展现美好、自己所追逐的、自己所渴求的东西，这些都会展现在言行举止上，即“面具”。</p>
<p>而<strong>我们想要挖掘的是面具后的人，也就是人们的“本我”，这才是人们底层的需求本质</strong>，如何透过行为去发现用户的本我，就是用户调研的难度和产品经理的功力了。</p>
<p>第三个问题：举个栗子，比如你目标用户是“有过贷款的大学生”，但是很可能投放渠道不能直接区分用户，如果不在第一二题设置一些筛选题筛掉那些“从未贷款过的人”，那将会是巨大灾难，后期数据分析的结论会产生巨大偏差。</p>
<p>基于这些原则，我建议你可以再看一次问卷：</p>
<p><a href="https://www.wjx.cn/hj/xsenioks0ywsz2s2aveba.aspx" target="_blank" rel="noopener">https://www.wjx.cn/hj/xsenioks0ywsz2s2aveba.aspx</a></p>
<p>一些比较基础的原则，比如简介里告知匿名告知题目数量、比如题目顺序要随机、比如设置一些奖励机制来鼓励答题等等，这些做过两次问卷设计后都能体会到。</p>
<h2 id="toc-5">五、问卷投放</h2>
<p>回到笔者的0-1设计APP中，本次共发出问卷101份，涉及全国各地，没有地域限制。年龄覆盖18-50岁，其中80%的用户年龄在18-30岁之间，符合当下主流的互联网职场群体。</p>
<p>回收有效问卷101份，其中目标用户上班族（含裸辞）共49份，次目标用户在校大三、大四学生共38份，其中使用过职场学习类App（1次+）的用户共61人（70%），从未使用职场学习类App共26人（30%）。</p>
<p>因此，最终实际有效问卷共61份参与分析（实际中有效问卷控制在200份效果较好）</p>
<h2 id="toc-6">六、用户基本特征</h2>
<h3>6.1 年龄/性别分析</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/5HwUtzfshRBW2jl8cxmn.png" width="604" height="323" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">年龄分析</p>
<p>在全国批次的调查过程中，受访者主要年龄集中在18⾄30岁，其中18-25 岁、26-30 岁群体成为本次调查⼈数最多的群体，样本年龄分布与调查群体年龄分布相近，均为当下职场人士的主力人群和自主学习的年龄段，因此，数据具备⼀定参考价值。</p>
<p>61人中，男性26名，女性35名，比例较为接近，使数据具备一定参考价值。</p>
<h3>6.2 学历分析</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/zA9eF8TZU4sBaHMWafLo.png" width="604" height="249" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">学历分析</p>
<p>本科学历成为被调用户的主要学历，这与当前在线学职场学习App的目标用户一致，且占据绝对占比。同时也有20%硕士以上用户，增加本次调查的完整性。</p>
<h3>6.3 工作年限</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/YFjqdgReH0H1p2QpSVXr.png" width="603" height="260" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">工龄分析</p>
<p>本次被调用户覆盖各工龄的职场人（0-6年），覆盖面较为广泛，让本次调研更具价值。同时，后续可以根据不同工作年限来精准识别他们的差异需求，对我们产品设计更有帮助。</p>
<h3>6.4 月收入情况</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/y16AjMT4PNQ4wznjTyNI.png" width="610" height="357" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">月收入分析</p>
<p>月收入情况覆盖各阶层，平均薪资约10000元，符合一二线城市职场人士的平均薪资情况，证明本次目标人群符合产品定位。另外，高薪资者少，15000元/月以上的薪资只有一位，符合网络学习用户的特征。</p>
<h3>6.5 地域</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/jCVr3azvvsf6IKkcy2wj.png" width="598" height="405" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">地域分析</p>
<p>来源全国各地，主要来自一二线城市。与主流知识付费用户相符。</p>
<h3>6.6 小结</h3>
<p>初步画像：</p>
<ul>
<li>年龄：26岁</li>
<li>性别：女</li>
<li>职场年龄：3年</li>
<li>工资：10k</li>
<li>城市：一二线城市</li>
</ul>
<h2 id="toc-7">七、用户行为特征</h2>
<h3>7.1 使用情况</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/ndIAXrcgFyq8IIVzgzhA.png" width="698" height="263" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">使用情况</p>
<p>高达80%的目标用户会有规划使用、高频使用职场学习软件，20%用户至少使用过。</p>
<h3>7.2 学习目的</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/fxnHCYgPl3jsCPPPJ4DM.png" width="704" height="338" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">学习目的分析</p>
<p>经折合，有51%的用户关注【软技能】和【硬技能】，其中用户更关注软技能，想要全面提升自身能力。有21%的用户也关注【前沿资讯、大佬发言】，有13%的用户关注【就业工作】。结交志同道合成为最弱的需求。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/6HgyDELYPcSPWY60BZmv.png" width="702" height="306" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">课程系统性分析</p>
<p>有84%的用户看重课程的实操性和系统性。并且大部分用户比较理智，会根据课程的价格和所耗时间综合判断是否购买“系统性”课程。</p>
<p>因此如何设计更好的付费机制和课程分时机制能极大程度降低用户的选择成本，给优质课程更多机会</p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/wKFM7NeorBPgw0b5ocOZ.png" width="700" height="400" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">购课标准</p>
<p>看重系统性、实操性课程的用户，会从多方面评判课程质量。其中57%的用户最看重【讲师/老师】的背书、背景、互动性、可沟通答疑等。</p>
<p>说明老师的IP程度将极为重要，寻找大厂的讲师、或将垂直领域KOL教师化，并与学员形成社交互动，是一大关键。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/vPcgvZalXq5FXluYpqjU.png" width="702" height="262" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">讲师水平</p>
<p>进一步探究，发现【课前判断】（包括老师和课程两部分）是95%用户所需要的。而且用户较为理智，有32%的用户认为当下试听课等课前体验有水分，被过度包装。</p>
<p>因此，优化用户的【课前判断】是核心需求，且简单的试听课已满足不了用户，用户需要的不仅是课程的一部分，而且还是讲师能力、课程落地性甚至其他学员口碑的综合预知。</p>
<h3>7.3 用户学习习惯</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/tQh8w5Wh2jzJe9lKVDT0.png" width="702" height="353" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">学习时间</p>
<p>再结合线下用户访谈和该数据，51%的用户会选择【大段时间】作为学习在线课程的时间，如工作日晚上和空闲周末。另外49%用户会选择【碎片时间】进行前沿资讯阅读，听音频，如饭点、路上、工作休息时间。</p>
<p>且这两者并不冲突，有明显时间区分，发生于多名用户身上。一定程度上，在线课程App已不再是碎片化时间的产品，如三节课、网易云课堂、混沌大学等。</p>
<p>相反，信息获取类App成为碎片化时间学习的占有者，如人人都是产品经理、喜马拉雅、36Kr等。</p>
<p>启发：二者可以相结合，一静一动互补，通过短视频的形式承载碎片化信息来弥补在线课程App的静态。让讲师“活”过来，成为真正的“前辈”。</p>
<p>通过讲师，发起话题、动态、知识短视频等内容，碎片化一些见解和分析，强化讲师的IP作用，同时也强化与同学的互动。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/4tmKi8Il5sKJHmh59mxK.png" width="700" height="349" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">产品功能要素排序</p>
<p>对于用户所关心的功能，其重要程度是：<strong>课程内容>课后资料>动态知识>课前体验>作业系统>课程工具</strong>。</p>
<p>简化来说：</p>
<ul>
<li>★★★★★课程内容本身（含各类资料）</li>
<li>★★★动态学习（购课前预知、上课中互动、未来持续跟进）</li>
<li>★辅助工具（作业系统、效率提升）</li>
</ul>
<h3>7.4 用户消费能力</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/qNjIaEKZJyPl8Vn0wItM.png" width="697" height="357" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">用户消费单价</p>
<p>自2016年知识付费元年起，根据用户的消费能力逐步养成，可以看到平均购买课程的单价在1000元左右，说明用户对课程质量和课程整体服务的看重。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/5iSmuAKPBPpIlW9PRfx1.png" width="698" height="247" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">付费意愿分析</p>
<p>有82%的用户愿意为学习效果多花钱，符合上面的分析。且能够考虑的价格范围在500~1200元，部分用户愿意承担2000左右的学费。</p>
<p>说明知识付费目标用户的整体消费水平已不成为太大的阻碍，相反，用户对优质课程、学习交付的诉求越来越高。用户的甄别能力和评判能力也是如此，这与之前的市场分析相一致。</p>
<h2 id="toc-8">八、用户画像</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/QCMtxdoZxAmxSkze8O9m.png" width="701" height="831" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://image.woshipm.com/wp-files/2019/08/SoIbnQxI3dGnFTCTfrQM.png" width="700" height="874" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">用户画像</p>
<h2 id="toc-9">九、总结</h2>
<p>由于本份问卷质量不是特别高，因此数据分析时总感觉缺少一丝深度，对人性的理解。但是问题不大，我们还有用户访谈。</p>
<p>用户调研实际上是一个非常重要的过程，不是简单的问卷就能说“哦，原来用户是这么想的”。往往还是配合其他方法一起解决问题。问卷能够承载的职责是有限的。</p>
<p>而问卷调研在笔者看来，一个“前哨兵”。问卷有简单方便、成本低的优点。<strong>我们可以通过设计一份好的问卷来帮助我们获取粗略的用户需求，更深层次和有把握的判断还是得来自与用户沟通过程中产生。</strong></p>
<p>相传，腾讯有一个“10/100/1000法则”：产品经理每个月必须做10个用户调查，关注100个用户博客，收集反馈1000个用户体验。注意，排在最前面的是10次调查，而不是多少份问卷。</p>
<p>最后，笔者想说，问卷设计是一项基本功，需要不断锻炼，笔者也在学习中。一份好的问卷一定是对人性有所精准把握的。</p>
<p>OK，本系列第三篇：用户调研篇（上）。利用市场调研和产品调研中发现的机会点，我们进一步做成问卷到市场中投放，形成了初步的用户画像，但是这还不够，还要我们进一步发现机会。下一篇，我们来讲讲用户访谈。</p>
<p>感觉对你有点用的话，可以点个收藏！</p>
<p> </p>
<p>作者：朱鲁斌@猪是大吉。同花顺产品经理（B端方向）。</p>
<p>本文由@ 朱鲁斌@猪是大吉 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash， 基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="2710458" data-author="874138" data-avatar="https://image.woshipm.com/wp-files/2020/05/LMtPQqW5zOJ3hzUzA4pK.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            