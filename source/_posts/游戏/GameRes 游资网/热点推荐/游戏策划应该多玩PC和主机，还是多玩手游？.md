
---
title: '游戏策划应该多玩PC和主机，还是多玩手游？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/24/100526n05m9p5qd4umpgq4.jpg'
author: GameRes 游资网
comments: false
date: Tue, 24 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/24/100526n05m9p5qd4umpgq4.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2511443">
原文是在知乎的一篇答案，写完之后觉得还是把很久以来想说的写出来了，转过来和大家一起讨论一下吧。https://www.zhihu.com/question/419846609/answer/1672270196<br>
<br>
<strong>摘要</strong><br>
<br>
PC、主机、手游的分析深度如何把握才合适；<br>
<br>
不同段位的策划眼中项目是什么样子，低段位的策划会带来怎样的灾难；<br>
<br>
通过数据库，wiki，官方资料配合 Python 爬虫，获得原始数据，生成可用于分析的表格；<br>
<br>
捕获系统与数值之下的设计意向；<br>
<br>
研究过时的游戏版本是否有价值，变化趋势的意义；<br>
<br>
跨品类游戏底层设计意向的共性；<br>
<br>
经典的疏漏也是学习的素材——魔兽世界标准化武器速度；<br>
<br>
对日系游戏的一点感慨；<br>
<br>
<strong><font color="#de5650">先说一个我个人对策划段位的理解：</font></strong><br>
<br>
优秀的系统策划 > 优秀的数值策划 > 一般的数值策划 > 一般的系统策划<br>
<br>
各段位特点后文详述。<br>
<br>
对于策划通过玩游戏来获取自我提升，或素材积累，本文的能提供的可实操路径，止步于准优秀的数值策划，至于想成为优秀的系统策划的读者，除非是天赋异禀，不然本文的路径也有一定的参考意义。<br>
<br>
本文更适用于手游项目，已有品类，不适用于创意性、开辟新品类的项目，但即便是这种类型的项目很多底层的设计理念也是继承自现有的优秀作品，这一点见后文的 “跨游戏品类，理解共通性的设计” 读过之后可能会有一些对底层设计共性的体会。<br>
<br>
PC、主机和手机游戏，如何选择，这取决于你想成为一个怎样的策划。<br>
<br>
A 线路：做换皮项目；紧跟风口，拥抱热点；避免过度纠结于底层设计，快速出产品起流水是最高原则；<br>
<br>
B 线路：掌握设计框架，理解经典的设计意向及演化过程，熟悉其优势、缺陷及应用场景，搭建自己的设计体系来应对不断变化的需求。<br>
<br>
PS:此处无褒贬之意，完全要看就职的公司的需求，两条路径走得用心都是好策划。<br>
<br>
如果选择A，那么多玩手游更有优势，工作产出才能更有保证。<br>
<br>
如果选择B，且把策划当做一个长久的职业生涯，而不只是一个门槛不太高，待遇还说的过去的活儿的话，那么应该多玩 PC 和主机，且最好是有一定复杂度支撑的经典大作，因为这类作品的体系更为成熟、严谨，且汇聚了大量硬核玩家，能够更方便地站在巨人的肩膀上理解游戏。<br>
<br>
重视主机和PC，那么对于手游要做到一个怎样的尺度呢？我个人认为最终产品虽然是面向手游的，但除非是重度参考的目标项目，否则分品类，挑选爆款、付费设计优秀的项目，将系统、数值、付费一起分析，以导图形式来描绘一个框架，对游戏内的泛货币、玩家游戏参与时间、消费人民币绘制循环系统，做到这个程度就可以了。如果时间仓促则把握大体结构，确保不产生量级错误即可。<br>
<br>
贴个当年分析《放开那三国》的一个答案，虽然比较古老了，但有那么个意思就行了，明白尺度即可。（手游《放开那三国》靠什么维持持续的付费和高ARPU？https://www.zhihu.com/question/22607942/answer/23072185）<br>
<br>
算是仓促分析的一个尺度吧，如果是要作为参考作品来进行缝合的话自然会把拆解细腻度再提高一级。<br>
<br>
除去体验、引导与付费设计以外【注释1】，手游中能学到的设计、结构、游戏性及乐趣塑造确实不多，这既有作品本身的素质问题（这并非设计团队能力的问题，更多的是用户群导致的产品定位问题），也有玩家群体对游戏的剖析意愿和能力的影响，毕竟手游更多的是快节奏的娱乐。因此可以看到玩家在魔兽世界中用插件记录几万次的测试数据，猜测公式来拟合数据，比较每条属性对战斗的影响，追求极致的搭配和手法，而在手游中则几乎不会存在。<br>
<br>
鉴于以上两点，使用手游作品就很难站到巨人的肩膀上实现策划的自我提升。<br>
<br>
【注释1】对于体验、引导和计费设计，这部分手游博大精深，可挖掘的点，甚至成体系的大块结构都很多，以前写过一篇《正向情感体验的创造》（链接：https://zhuanlan.zhihu.com/p/20363616）。本文是站在心理学角度（主要是社会心理学和行为经济学方向）分析游戏的计费设计，算是在一个视角下的抛砖引玉吧，文中聊了交易效用、损失厌恶、沉默成本、认知失调、心理账户、媒介干扰、大脑的负载水平等等，有兴趣的朋友可以看看，刚入行的朋友也不必惊慌，这单纯是在讨论通用的设计思路底层是否有足够的支撑，适用性在当下还是否有效等等。通用的设计绝大部分都是对的，这就好像一个函数或者方法，遇到合适的问题，调用就好了，无需关心它内部的逻辑是如何执行的。sort() 或 .sort 就好了，背后是归并、快速还是堆不用去管它。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">系统策划与数值策划的段位</font></strong><br>
<br>
对系统策划和数值策划的工作内容先做个简单的比喻：<br>
<br>
假设一个项目要克服千沟万壑，最终架起一座桥梁通向成功的彼岸，那么最好的方式就是知道这座桥梁应该是什么样，主策需要明确最原始的需求，如桥梁可能的最大通行量带来的动态载荷，桥梁的自重的恒定荷载，恶劣天气造成的风荷、雪荷等特殊荷载。通过对这些原始数据的预估，选择合适的桥梁结构来承载这些重量。<br>
<br>
能相对准确预估这些要素，这种级别的主策现实里不多见（按系统策划从业基数和成功产品数量，项目反复修改的普遍现象，逻辑推演也是这个结论），退一步说能够通过有目的性的试错来迭代修正设计使得这座桥能跨到彼岸，我认为已经可以称得上是个优秀的系统策划或者主策划了。<br>
<br>
那一般的系统策划是什么状态呢？玩过一些游戏，大体了解系统，实际做的时候多半得拿出游戏来现抄，缝合出来一个自己的系统文档，可能很多小伙伴觉得这很正常，很多人都是这么做的。现在来说说这么做糟糕在什么地方。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1002989" aid="1002989" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100526n05m9p5qd4umpgq4.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100526n05m9p5qd4umpgq4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100526n05m9p5qd4umpgq4.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图1：悬索桥简单结构示例</font></font></div><br>
还是用桥梁来打比方，上面提到的那些载荷，必须有足够的承载力来提供支撑才能保证桥梁的不会垮塌，如图1动载（车辆、行人）与静载（自重）的传递路径主梁 -> 吊索 -> 悬索 -> 索塔 -> 桥墩 -> 桩基础 -> 大地。系统策划眼中应该不仅是桥梁的外观（玩家层次的关注点），同时也要在心中绘制结构图，再由数值策划去完善、细化整体的力学参数，选取合适施工方法和建材，从而实现设计意向和用户体验。<br>
<br>
<strong><font color="#de5650">不同段位的系统策划眼中的参考作品和自身项目的认知</font></strong><br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1002990" aid="1002990" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100527c7kn4z7ogavak4pk.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100527c7kn4z7ogavak4pk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100527c7kn4z7ogavak4pk.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图2：金门大桥</font></font></div><br>
<strong>入门级系统策划</strong>眼中的参考作品，“哇，雄伟壮丽，《星球崛起》就是这拍的，抄它准没毛病！”<br>
<br>
<strong>一般级系统策划</strong>眼中的参考作品，“梁板的跨度好大啊，桥下的通航空间好开阔。两个边的索塔通过悬索吊着梁板，结构真巧妙，让数值拆解一下力学结构。” 回顾图1。<br>
<br>
而桥梁的力学结构就好像游戏的数值公式，在不知道明确的设计意向和体验要求直接看一个产品时，你可以看到它的上层表现，但不通过多组取值，分析规律，猜测公式，再取值验证猜测，修正猜测，反复这个过程直到能完全拟合，是无法真正的把握它的。即便完全拟合的把握，也只能说大体掌握了设计意向，体验方面仍然很难讲，因为与体验相关的不只是系统和数值，甚至系统和数值在一定的局部范围还要去扭曲自身来强化体验（手游中尤其明显，为了破冰首充啥操作都可能招呼）。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1002991" aid="1002991" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100527hj2v66us6gdds5j5.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100527hj2v66us6gdds5j5.jpg" width="403" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100527hj2v66us6gdds5j5.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图3：简支梁</font></font></div><br>
<strong>优秀级系统策划</strong>眼中的参考作品，“我去，就这么短的开发周期，这么小众的用户群定位（也就是个步行桥），这么点的盈利期望（不需要啥承载力），桥下又不过船（没有通航净空要求），造毛线大跨度悬索桥啊，来个简支梁赶紧过河是真的。团队虽然人不多 996 搞一下应该也来得及。”<br>
<br>
这叫透过现象看本质，根据产品要求，可调动资源，规划合适的方案来满足商业要求。<br>
<br>
当然如果资金、时间、技术顶得住优秀级系统策划也得造得出大规模的桥梁工程（金门大桥属于超级工程了，也许应该对应魔兽争霸3这种级别的杰出作品），如此才能算优秀级，只能玩小作坊的话，尽管可以说是审时度势，但也不能算作优秀级。<br>
<br>
当系统策划能指明原始需求，或者在缝合时能站在捕捉参考作品设计意向的层级来融合出自己的系统时，数值体系的构建就是一个自顶而下逐步细化的工作，它可以天然的避免矛盾，对于细节的调整和处理可以锁定到一个或一系列的子系统或模块来完成，只要明确这个部分在整个系统中的要承担的任务就可以了。<br>
<br>
即便是采用多作品借鉴缝合的做法，同样也非常考验策划功力的，如果一般的系统策划操刀对其他作品的借鉴只停留在表象时，这是非常危险的，很容易诱发矛盾，这时再修正很可能就不是局部操作能解决的了。<br>
<br>
“你看金门大桥中间连桥墩都没有，一跨就做了好几百米，抄它不就得了”，他可能根本没分析参考作品的力学结构。这可能就是最糟的系统策划——只看表象，毫无拆解深入能力，如果是缝合模式在做项目，这个级别的系统策划也是最危险的，东拼西凑带来的矛盾是难以弥合的，如果数值策划缺乏预见能力，自底而上，逐步积累的部署数据，到了中高层要向顶点汇聚时，发现自己盖的不是金字塔，而是吉隆坡双子时，心理得有多崩溃。<br>
<br>
<strong><font color="#de5650">策划自我提升的基础素材</font></strong><br>
<br>
类比性的问题描绘到此结束，后面谈实际的解决思路。先看解决问题需要的基础：<br>
<br>
<strong>1.足量的原始数据；</strong><br>
<br>
数据量足够大时，游戏分配数值的趋势和节奏是可以看出来，这不需要什么天赋，只要耐心去汇总、处理数据都能找到大体的感觉，把握游戏大体的框架、数值和资源释放节奏，如果是初级策划，做到这一步，那么已经是在自我提升的路上了，如果是系统策划我想你已经跑赢了一半的同行了。<br>
<br>
<strong>2.正确的捕捉设计意向；</strong><br>
<br>
<strong>获取原始数据</strong><br>
<br>
对于手游项目这两个基础能搞到手吗？除非你能直接搭上关系拿到目标项目原始的配置表，还能有机会直接和核心成员聊大天，那OK！一切都不再是问题，只要这个表是一个合格的数值策划搭建的，顺着这个表你找到项目绝大部分数值的推演过程。不能推演的数值，一般就是设计意向了，比如这个版本的生命周期，期望的充值上限等等。这些数值一般会写备注。实再玩不转了还能聊天呢，对吧！<br>
<br>
但这种解决方式不具备通用性，也不应该对此抱有期待。<br>
<br>
也许有人会说通过拆包拿数值配置表可不可以？即便是程序没对表格动手脚，表头说明都完全暴露的情况下也是没啥用的。因为数值的搭建大都是从一个设计意向表的原始数据，里面部分数值还是拍脑门。。。呃，凭借丰富的经验设置的，通过对这些值的层层引用，公式计算产生出最终的数值表，而那些设计意向是不会直接体现在部署的表中的。<br>
<br>
使用层层引用计算的模式来部署，倒不是数值策划不怕麻烦的故作高深，而是这些原始数据随时可能被系统策划或者数值自己修正（甚至推翻），如果不是从单点出发，通过引用与公式计算来生成，改起来就要人命了。没概念的可以想象一下，代码里有个值大量的被调用计算，程序没把它声明成变量，而是直接把值写进代码里了，现在需要统一变更一下这个值，还不允许你 Ctrl + H。<br>
<br>
获取有效原始数据的路基本被堵的差不多了，但这个工作仍然必须得做，因为这些原始素材是一切分析进而实现能力提升的出发点。那么要获取数据最直接的、无法被堵的道路是什么呢？在游戏中提取，手工记录，这是必然成功的方式，但工作量太大，耗费的时间成本难以接受。也许有主策或是主数想让执行策划来完成，手工做得事你敢100%的信？<br>
<br>
另外如果是去取手游的数值，你能确定参考作品是个严谨的作品？不是赶上风口稀里糊涂就成了？它演的时候是正剧，你仿出来时风口过了，玩家对该品类的口味刁了，最后很可能仿成了一出闹剧，除了制作的时候热火朝天，最后剩下的是一地鸡毛。<br>
<br>
如果是去扒成熟、严谨的PC作品，你如何才能说服老板让他觉得这个工作与进行的项目有足够高的相关性，不是空耗人力工时？同时还要说服执行策划这个工作是有价值的，调动他的积极性来保质保量的完成任务。即便这些都被你克服了，还要面对手工取出的数据可能存在的偏差，比如你要看人物属性的成长节奏，但执行策划取值时忘了脱装备了或者中途换了装备忘了记录，基本你很难指望执行策划们边取值边验证，他也得兼顾效率。于是乎最终历尽万难拿到的数据还得清洗、修订。<br>
<br>
看起来又变得无路可走了是吧？这也就是为什么在开篇说的最好是玩大作的原因！通常大作更方便获取数据，比如 WoW 有高质量的数据库。<br>
<br>
<div align="center">
<img id="aimg_1002992" aid="1002992" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100527o9blkbbc4byfsvyc.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100527o9blkbbc4byfsvyc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100527o9blkbbc4byfsvyc.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图4：魔兽世界数据库 法师套装</font></font></div><br>
这里用了个比较老的数据做示例，使用 https://cn.warcraftlogs.com/ 与时俱进的库自然更好，不过我没找到各职业套装列表，爬数据时会略微麻烦一些。<br>
<br>
获取数据导入表格也是很大的体力劳动对吧？游戏数据库通常是 web 形式，数据也都是文本，必然存在呈现的规律性，网站肯定不是拿静态页堆出来的，只要存在规律，获取可用来分析的数据就相对容易。<br>
<br>
简单的学习一下 HTML，JavaScript 有个基本认知，利用 Python 的第三方库 urllib 或 Selenium 来获取页面代码，在 BeautifulSoup 处理 HTML 节点提取文本（对个别文本可能还需要正则表达式来处理一下），OpenXML 写入 Excel，基本上高质量的原始数据就拿到了。<br>
<br>
通常这些数据库是不需要登录的，也就不需要去拿 Cookie，费力的伪造 Request，，或是使用 Selenium 等等。最多遇到一段时间内请求量过大封 IP 的问题，等一段时间就OK了，毕竟取数据这个工作进行的没那么频繁。真紧急换个 IP 或 使用 poxy。<br>
<br>
当数据进入到 Excel，这就变得对数值策划有意义了，数据的趋势、节奏、份额等等才能够进行分析。<br>
<br>
<div align="center">
<img id="aimg_1002993" aid="1002993" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100528lrnn818v7svbndg7.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100528lrnn818v7svbndg7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100528lrnn818v7svbndg7.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图5：通过 Python 将魔兽世界数据库表格化</font></font></div><br>
这里在补充一点对我个人提倡对 PC 大作的分析要足够的细腻，有深度，充分体会设计意向，对手游掌握框架和泛货币流转，但也要做到大面上把握数据。还是用《放开那三国》举例如下图，起码有这种细度的把控。再细腻除非是想复制体验，否则意义不大，毕竟付费是需要系统、剧情等等一系列的配套与之相呼应的，每个产品应当走出自己的节奏。<br>
<br>
<div align="center">
<img id="aimg_1002994" aid="1002994" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100528lnxcs2t8s5201100.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100528lnxcs2t8s5201100.jpg" width="530" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100528lnxcs2t8s5201100.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图6：《放开那三国》曹操属性的各系统占比</font></font></div><br>
<strong><font color="#de5650">设计意向的捕获渠道</font></strong><br>
<br>
取数据聊了不少，这是一切的起点，但手握大量数据只能保证我们可以进行分析，归纳，在一定程度上捕获设计意向，做出来的东西不会犯大错。但我们捕获的设计意向是否是对的，设计意向是否深入本质就很难讲了。这也就是为什么说最好是玩汇聚了大量核心玩家的大作的原因！<br>
<br>
只有足够数量的核心玩家，足够多的讨论、分享，才能更好，更正确的捕获设计意向。<br>
<br>
举个例子：当年 NGA 坦克角色关于减免率收益的争论。<br>
<br>
一派观点认为：提升护甲收益是边际递减的。因为随着你护甲的提升，减免率的提升是递减的。<br>
<br>
另一派则认为：护甲的提升带来的减免虽然是递减，但有效生命的提升是线性增加的。最终此派玩家以代数的方式证明了这个论点；现在来看这可能是公理了，但如果时间你倒退到2005年的时候，这确实没有那么显而易见。<br>
<br>
<div align="center">
<img id="aimg_1002995" aid="1002995" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100528wjzoh6dsx2wrz5sn.png" data-original="https://di.gameres.com/attachment/forum/202108/24/100528wjzoh6dsx2wrz5sn.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100528wjzoh6dsx2wrz5sn.png" referrerpolicy="no-referrer">
</div><br>
以TBC为例，首领Boss视为 Lv73，护甲等级 = 73 + 4.5 * (73-59) = 136；<br>
<br>
60级之前护甲等级等于人物等级。<br>
<br>
<div align="center">
<img id="aimg_1002996" aid="1002996" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100528uxgrdi9drnid09gl.png" data-original="https://di.gameres.com/attachment/forum/202108/24/100528uxgrdi9drnid09gl.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100528uxgrdi9drnid09gl.png" referrerpolicy="no-referrer">
</div><br>
顺便说一下类似设计模式被应用于 Combat Rating，意在快速淘汰上个版本的装备，也使得物品投放获得更大的数值空间，同时也让新人玩家能够以较低的门槛（大幅削弱先期积累的价值，提高了当下参与的收益）投入到游戏中来。<br>
<br>
另外插一句数值心得，核心玩家更容易帮我们建立界限思维，这对数值相当重要，就是一定要知道最好和最差的情形。<br>
<br>
比如与有效生命相对应的伤害，RPG的最终是落实在玩家的输出循环上，通常数值会计算一个自己认为的最优状态及循环，可一旦系统复杂了难免会造成一些遗漏，造成玩家的最优输出能力超越了数值的预估，这就很糟糕。<br>
<br>
如何来避免这个问题呢？参考大作的技能设计是个思路，但如果能拿到一些极限玩家的输出行为，则会帮助你更好的理解玩家是如何在既定的框架下寻求突破的。<br>
<br>
<div align="center">
<img id="aimg_1002997" aid="1002997" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100529mq1uazvo2gba6xp0.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100529mq1uazvo2gba6xp0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100529mq1uazvo2gba6xp0.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图7：cwl Boss 整体统计</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1002998" aid="1002998" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100529baf3c34o9iaz445z.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100529baf3c34o9iaz445z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100529baf3c34o9iaz445z.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图8：cwl 单一玩家在一场战斗中的行为细节</font></font></div><br>
这是cn.warcraftlogs.com玩家上传的战斗记录，在此可以方便地查看，玩家对战 Boss 的装备状态，Buff 状态，战斗时的技能技能释放循环，其中硬核玩家的占比远远高于其他社群，这也就更便于我们去参考极限玩家的行为，并作出有价值的分析。<br>
<br>
<strong><font color="#de5650">巨人的肩膀——wiki 和 官方资料</font></strong><br>
<br>
核心玩家的讨论很多是尚未形成共识的内容，需要自身强大的分辨能力，甚至设计测试方法到游戏中去验证的耐心。对于新手更快捷的方式是直接学习已经形成共识的结论——大作的 wiki，甚至官方亲自出来给你讲设计意向，这将使你站在巨人的肩膀上，获取成熟的设计意向。<br>
<br>
WoW Combat Rating 与 百分比值的转换，玩家基于实测数据进行的公式拟合。（链接https://wowwiki.fandom.com/wiki/Combat_rating_system）<br>
<br>
<div align="center">
<img id="aimg_1002999" aid="1002999" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100529mkhddtjb8gd7zzkh.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100529mkhddtjb8gd7zzkh.jpg" width="522" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100529mkhddtjb8gd7zzkh.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图9：Combat Rating 折算百分率</font></font></div><br>
对急速属性的改变，官方的解释，也就是常说的暴雪蓝贴。（链接https://wowwiki.fandom.com/wiki/Haste）<br>
<br>
<div align="center">
<img id="aimg_1003000" aid="1003000" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100529e1pgksa666nkwnwy.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100529e1pgksa666nkwnwy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100529e1pgksa666nkwnwy.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图10：wowwiki.fandom 保留的暴雪蓝贴</font></font></div><br>
也许有人觉得 WoW 特例性太强，那看看《异度之刃2》的 乐园数据管理室。数据的丰富程度同样相当高。爬取分析也相当省心。（xenoblade2.cn）<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1003001" aid="1003001" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100530wi247pi99p7299s1.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100530wi247pi99p7299s1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100530wi247pi99p7299s1.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图11：乐园数据管理室</font></font></div><br>
再比如 怪物猎人：世界 冰原 的官方手册，以及 wiki，基本上想查想算都能搞到。<br>
<br>
<div align="center">
<img id="aimg_1003002" aid="1003002" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100530v9nrz1u6r13000xz.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100530v9nrz1u6r13000xz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100530v9nrz1u6r13000xz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图12：怪物猎人：世界 冰原 官方手册</font></font></div><br>
Kindle 版的 怪物猎人世界：冰原官方指南截图。中文的话可以用 UCG 的 《怪物猎人世界：冰原世纪》典藏攻略本，内容大体就是官方的译本。<br>
<br>
找数据的途径多种多样，难易兼有，唯有游戏策划始终如一的自我提升追求才能引领我们走向远方。<br>
<br>
<strong><font color="#de5650">过时的游戏版本是否有价值？变化趋势的意义</font></strong><br>
<br>
对于策划，如何理解游戏的过时的版本，我认为无所谓，重点是设计意向，如果就是当前本版，优势在于可以亲自去验证结论，但如果提供结论的人同时上传了测试数据，或者足够的可信证据，那么这个验证的过程就可以省略。<br>
<br>
<div align="center">
<img id="aimg_1003003" aid="1003003" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100530drwedyyeruyfedw9.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100530drwedyyeruyfedw9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100530drwedyyeruyfedw9.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图13：NGA 用户 youngx 2010年的技术贴</font></font></div><div align="center"><font size="2"><font color="#808080">https://bbs.nga.cn/read.php?tid=3381288</font></font></div><br>
版本如果足够的多，对于取数据，找可以采信的结论，是个困难，但它也带来一个好处，就是可以去学习设计意向的变化趋势，这同样极为重要，随着时间的推移，玩家被游戏作品的洗礼，市场的需求是动态变化的，足够多的版本说明游戏的玩家群还足够大，能够支撑起游戏更新的商业价值，而变化趋势则是这个被玩家认可的公司，交出的对市场变化的答卷。<br>
<br>
这在一定程度上我认为已经超越了理解精妙的静态设计意向的意义了，因为理解变化趋势，才能把握设计意向演进的方向，也就是说它更有助于策划自身形成一套动态的设计理念来应对千变万化的市场。<br>
<br>
花些时间仔细地剖析一个游戏的数值计算体系实际是一个挺超值的工作，因为一系游戏的设计都有其继承的血脉，深度把握一款对于快速理解同系下的其他游戏非常有帮助，这就好比写面向对象的代码，熟悉了一个类的接口，如果是看它的子类或兄弟的话专注于增加、修改的内容就可以。<br>
<br>
比如日系单机游戏，伤害通常是一连串的叠乘，如果仔细的拆解了《异度之刃2》或《怪物猎人》，再去理解《八方旅人》，那就好像 Ori 你冲破银之树后，在常规跑图中使用猛击般惬意。<br>
<br>
额外提一句个人觉得《异度之刃2》绝对是战斗操作带来的游戏性和数值计算的完美结合，有机会写一篇来分析一下，个人感觉站在心理学角度，《异度之刃2》在纯粹战斗方面，对大脑的负载水平、奖励机制的拿捏也是典范级的。<br>
<br>
<strong><font color="#de5650">跨游戏品类，理解共通性的设计</font></strong><br>
<br>
再聊聊设计意图，或者说透过表现层之下的底层逻辑。<br>
<br>
魔兽世界-WoW 和 怪物猎人-MHW 差异很大对吗？但造成伤害的底层逻辑是很相似的，伤害的高低追根溯源是玩家发动攻击的时间成本。这又分两个方面：<br>
<br>
其一是玩家获取装备，buff的时间成本（buff 是广义的嗑药算作buff，此处的时间成本就是采集原料，以及烧生活技能这种一次性的成本投入）；<br>
<br>
其二是在单场战斗中装备，buff不变的情况下伤害的时间成本。<br>
<br>
前者对于点卡计费的游戏，角色强度是对投入时间、从事活动的挑战难度、运气值等因素的综合反映，对于手游则要加入人民币对以上因素的部分或完全的替代作用。<br>
<br>
此处重点来谈后者，WoW 的近战技能的描述文本通常都是 “造成 XXX% 武器伤害，再加 XXX 点伤害”，前半句随着武器的品质提升会提高伤害的结果，驱动玩家去获取更好的武器；后半句随着技能等级的提升而增加，驱动玩家提升等级学习技能。<br>
<br>
在一场 PVE 战斗中玩家造成的伤害量可以认为是一串技能的组合，玩家努力的方向则是权衡技能的释放限制，技能CD，公共CD等要素使得这串组合造成的伤害获得一个尽可能高的结果。近战的成本体现在技能的CD，这与怪物猎人比较起来可能有点绕，暂时换成 WoW 的法系职业可能更有助于理解，但对于伤害的处理在本质上是一致的，只不过策划需要针对不同的职业特点，战斗操作手感，去营造不同的游戏体验。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1003004" aid="1003004" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100530cwi8ii4j2rtdbm44.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100530cwi8ii4j2rtdbm44.jpg" width="325" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100530cwi8ii4j2rtdbm44.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图14 魔兽世界 法系 头部</font></font></div><br>
魔兽世界，提高所有法术和魔法效果所造成的伤害和治疗效果，最多XX点。<br>
<br>
<div align="center">
<img id="aimg_1003005" aid="1003005" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100530at5uu3y6pu5ukupb.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100530at5uu3y6pu5ukupb.jpg" width="421" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100530at5uu3y6pu5ukupb.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图15：怪物猎人：世界 冰原 饰品</font></font></div><br>
怪物猎人，饰品-攻击珠（理解成用于镶嵌的宝石吧），基础攻击力+XX；<br>
<br>
魔兽世界中，最多XX点，由施法时间来决定加成的高低，按法系3.5秒规则计算，即当法术的施法时间大于等于 3.5 秒时，享受最大加成。小于 3.5 秒时，以 （施法时间 / 3.5） 作为系数来计算，瞬发按 1.5 秒计算施法时间。<br>
<br>
怪物猎人中，基础攻击力+XX点，由动作值、武器倍率来控制加成的高低；<br>
<br>
怪物猎人要分两个方向来说加成。<br>
<br>
<div align="center">
<img id="aimg_1003006" aid="1003006" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100531e62f6sef7gzeqq72.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100531e62f6sef7gzeqq72.jpg" width="303" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100531e62f6sef7gzeqq72.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图16：怪物猎人 武器倍率</font></font></div><br>
首先武器倍率，它体现在面板，武器处于相同的档位时，不同武器的面板值虽然各有不同，但如果用面板值除以武器倍率，则会发现近战的基础攻击力是一样。<br>
<br>
增加基础攻击力的数值，会乘以武器倍率反应到面板上。<br>
<br>
例如装一颗 攻击珠2，增加 6 点基础攻击力，对于大剑来说，面板会增加 6 * 4.8，计算结果会取整。<br>
<br>
这个值更多的是 CAPCOM 让玩家对各个武器的伤害力道有个直观的感觉。<br>
<br>
面板攻击力高的武器通常对应招式高动作值。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1003007" aid="1003007" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100531wufsf8g8w0087pn5.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100531wufsf8g8w0087pn5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100531wufsf8g8w0087pn5.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图17：怪物猎人 双刀</font></font></div><br>
双刀、片手剑的动作招式相对更灵巧，一套攻击如暴风骤雨，面板攻击力较低，各个招式的动作值通常在 3 - 20；<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1003008" aid="1003008" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100531ti87cq2q80j72f8g.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100531ti87cq2q80j72f8g.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100531ti87cq2q80j72f8g.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图18：怪物猎人 大剑</font></font></div><br>
大剑、大锤的动作招式相对迟缓，但招招劲道，面板攻击力也较高，各个招式的动作值通常在 30 - 200 之间；<br>
<br>
其次是实际战斗中每次命中的伤害结果，这与武器招式的动作值相关，也就是上表中攻击力一列。<br>
<br>
例如，使用巨剑3（大剑），面板攻击力 480，使用直斩攻击训练场的木桩（物理吸收率为 0.8），在只拿一把大剑无任何技能、猫饭、药剂、护符的状态下：<br>
<br>
<div align="center">
<img id="aimg_1003009" aid="1003009" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100531dc8roqqoa2s8ro2j.png" data-original="https://di.gameres.com/attachment/forum/202108/24/100531dc8roqqoa2s8ro2j.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100531dc8roqqoa2s8ro2j.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1003010" aid="1003010" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100532cggxsfg4dkn2xxts.png" data-original="https://di.gameres.com/attachment/forum/202108/24/100532cggxsfg4dkn2xxts.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100532cggxsfg4dkn2xxts.png" referrerpolicy="no-referrer">
</div><br>
在游戏中会有两个返回值，40 和 42，这是大剑、太刀和盾斧斧形态特有的修正系数，使用武器刃中造成的攻击判断 * 1.03，武器尖端造成的伤害不享受这个奖励系数。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1003011" aid="1003011" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100532rvvn83mx6mp969qu.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100532rvvn83mx6mp969qu.jpg" width="513" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100532rvvn83mx6mp969qu.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图19：怪物猎人 大剑计算示例</font></font></div><br>
这里用了最简单的结算影响参数，有机会写一遍怪物猎人的完整公式计算例子吧。<br>
<br>
完整公式涉及的技能、物品 buff 还是蛮多，其次物理与元素伤害独立计算，近战、远程算法也有差异，网上倒是有不少，但大部分都是只说公式或者只做局部计算，对新手着实不太友好。<br>
<br>
在 怪物猎人 中造成伤害的时间成本可以理解为完成一个招式所花费的时间，造成伤害的难度可以理解为触发这个招式的条件。<br>
<br>
花费的时间越长，触发的条件越苛刻，则造成的伤害也就越高。<br>
<br>
再对比魔兽世界，比较明显的是法系读条，读条时间对应 怪物猎人 的动作值，触发难度对应读条期间遭到攻击延迟施法、或被打断施法，读条时间越长被阻止的可能性也就越大；<br>
<br>
读一个炎爆术是不是有点大剑3段蓄力斩的赶脚。<br>
<br>
<strong><font color="#de5650">大作的疏漏同样是学习的素材——魔兽世界标准化武器速度</font></strong><br>
<br>
伤害计算这块对于有战斗的游戏基本都是很核心的内容，上文说到观察游戏不同版本，以及演化趋势可以学到很多设计思路，以及对市场的反应。<br>
<br>
另外即便是大厂在进行设计的时候也难免犯错，而这些典型错误也同样是很好的学习对象。<br>
<br>
例如当年 WoW 在标准化武器速度推出之前，对于近战而言是存在一定的不平衡性的，WoW 中武器平砍与技能是无关的，在平砍当中武器速度不存在问题，因为每次攻击间隔都是武器速度，攻击强度（AP）也是按武器速度来吃加成。<br>
<br>
但使用技能就出现问题了，技能的释放周期是按自身的冷却时间进行的，但却按武器速度来吃加成，同一段时间内用使用技能的节奏一致，一个吃 3.3 秒武器速度加成，一个吃 3.8 秒，差异还是很大的，这使得付出了相同操作强度的玩家得到收益产生了差异，也就严重限制了玩家对武器的选择，单一化是对游戏性的伤害，因此标准化武器速度也就登场了。<br>
<br>
利用大作的疏漏进行触类旁通地学习，在搭建数值计算公式中始终保持警戒，例如怪物猎人的伤害结算公式，大量的加法参数，乘法补正系数，如果是在实际项目设计类似的公式，每一个运算节点都会需要停下来思考一下，在当前的节点不同的职业，不同的装备，不同的 buff，会不会造成其中一部分选择相较于其他拥有超额收益，这就会这会明显的左右玩家的选择。<br>
<br>
这里补充一点，在怪物猎人中，武器的物理伤害通过基础攻击力带来的加成体现在动作值中，平衡性在这里进行调平，也就是需要在公式设计时仔细斟酌的点。<br>
<br>
而对于属性伤害 CAPCOM 则单独搞了属性补正、弓蓄补正，特殊的招式还有特别处理，比如龙之一矢还针对不同的蓄力，不同的 Hit 数进行差异化补正，而非使用一个统一的体系（如，动作值）来进行调节，透过这一现象猜测 CAPCOM 设计意图，应该是希望游戏中存在的武器、防具和饰品都有针对性的应用场合，带来游戏配装的多样性和可挖掘深度的提升，换句话说这是设计团队在利用战斗收益引导玩家向着既定一种或几种打斗模式去靠拢。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">写在最后</font></strong><br>
<br>
给我个人的感觉日系游戏挺匠人精神的（特指玩法、系统设计），针对一个武器，设计玩法，设置独立参数，再回归全局调节平衡性，这相比于非日系的游戏，建立统一机制，日系游戏耗费的气力要大的多。<br>
<br>
这感觉特别像是老师出了道题，设置了数个踩分点，玩家作为应试者努力的方向是在所有的踩分点都不犯错，而且这个踩分的过程每一个点都给予了奖励，来引导你向这个方向靠拢。<br>
<br>
这一点让我感受最深的就是《异度之刃2》的公式，其中有一个 “取消倍率” 的参数，相当于在平砍完成的瞬间使用技能，从而取消平砍的后摇。<br>
<br>
取消后摇的带来的加速以提高 DPS 收益或避免敌方取消后摇来压制其伤害，比如 MOBA 类利用移动和释放技能来取消后摇；<br>
<br>
WoW 在 wlk 之前除了 T 以外的近战是要求背后输出的，一个原因是避免吃到正面的范围攻击，另一个原因则是避免自己的攻击被躲闪和招架，损失 DPS，同时也避免自己的攻击触发招架重置 BOSS 普攻，造成倒 T。<br>
<br>
上面的两个例子取消后摇的带来的收益在于更快的释放普通攻击，但在《异度之刃2》中取消后摇被的价值被极大的放大了：<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1003012" aid="1003012" zoomfile="https://di.gameres.com/attachment/forum/202108/24/100532ou1u8vi8n8ihczai.jpg" data-original="https://di.gameres.com/attachment/forum/202108/24/100532ou1u8vi8n8ihczai.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/24/100532ou1u8vi8n8ihczai.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图20：异度之刃2 “取消攻击”教学</font></font></div><br>
“自动攻击击中敌人的瞬间 使用武技追加攻击 的话，玩家的周围会有 光环 扩散开，这个光环就代表已经成功发动了取消攻击，如果成功发动取消攻击比起直接发动武技攻击力会提升。<br>
<br>
此外必杀技的填充也会迅速积累，因此能够在战斗中获得更有利的局势，并且取消攻击的效果会随着自动攻击的阶段进展而不断提高。”<br>
<br>
普通攻击的三段攻击对应的取消系数是 0.1、0.2、0.3，这才《异度之刃2》这种叠乘式的伤害结算公式中，放大作用相当的明显。<br>
<br>
这部分我个人觉得是非常有目的性的设计，因为取消攻击的教学点在非常的初期，此时战斗相对而言是比较枯燥的，使用一个高收益，同时需要强意识参与的系统来提高大脑负载水平，避免初期战斗可操作量少带来的无聊感。<br>
<br>
顺便说一句《异度之刃2》的前期的流失可能性还是蛮高的，除了战斗问题叠加初期怪物分布不合理造成的意外死亡的挫折感，初期信息量投放量过大造成的无助感等等。<br>
<br>
这个 “踩分” 的感觉在研究《异度之刃2》的公式时感觉相当的明显，但当时我没想起来这样做比，直到后来看到怪物猎人 Peppo 的视频 4 人黑龙<br>
<br>
【怪物猎人世界：冰原】当你狩猎1000只黑龙之后<br>
<br>
https://www.bilibili.com/video/BV1Xv41167BN<br>
<br>
2分20秒移动速射弩炮伤害触发倒地，三把太刀连登龙剑的升空都做到了完全同步，我当时的心里的想法是 “你们真不是脚本吗？这要是试卷你们都是按参考答案刻出来！”<br>
<br>
就此收尾吧，写得有点太长了，超出我最初的预期，怪物猎人、异度之刃2回头另开文，感谢阅读！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://www.zhihu.com/question/419846609/answer/1672270196</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            