
---
title: 'NPC会在游戏地图中迷路吗？——自动寻路的发展由来与应用前景'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202105/31/132523mt8itjx6q7li6jmq.png'
author: GameRes 游资网
comments: false
date: Mon, 31 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/31/132523mt8itjx6q7li6jmq.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2498805">
<div align="center">
<img id="aimg_981964" aid="981964" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132523mt8itjx6q7li6jmq.png" data-original="https://di.gameres.com/attachment/forum/202105/31/132523mt8itjx6q7li6jmq.png" width="571" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132523mt8itjx6q7li6jmq.png" referrerpolicy="no-referrer">
</div><br>
没想到我还会再写星帖奖的征文。回看自己过去的文字，多少有些"为赋新词强说愁"的意味。原本的立意我想放在表达个人游戏经历的杂谈上，名字我都想好了，就叫YOLO1……但是看了大家用心之至的文章，我发觉我的想法错了，因为这并不是一个适合宣泄个人情感的舞台——游戏依旧是这里的主旋律，永远都是。<br>
<br>
值得注意的是，本文涉及一些技术发展和算法设计的内容，会有一点点（真的只有一点点）的专业性（硬核? 枯燥?）的说教，请酌情食用。<br>
<br>
<strong><font color="#de5650">前言</font></strong><br>
<br>
本期星帖奖的题目是“虚拟游戏和现实世界”，倘若直观破题，将很容易陷入“寻找一款风格写实的游戏进行介绍”的窠臼；亦或者，陷入对游戏世界和真实世界的横向对比甚至无端畅想。<br>
<br>
然而只需要简单观察，我们就可以发现，一些游戏中所采用的技术其实脱胎自现实需求，而由游戏引发的技术进步也可以反哺现实应用场景。<br>
<br>
<div align="center">
<img id="aimg_981965" aid="981965" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132523cqo2qo7zwawqfaq3.png" data-original="https://di.gameres.com/attachment/forum/202105/31/132523cqo2qo7zwawqfaq3.png" width="564" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132523cqo2qo7zwawqfaq3.png" referrerpolicy="no-referrer">
</div><br>
以此为突破口进行索引，如今，自动驾驶成为电动汽车产业新的技术热点，然而复杂的城市街道、实时路况和突发事件无一不是考验车载自动驾驶系统模型的重大课题。<br>
<br>
但是回归本质，自动驾驶技术的实现却离不开自动寻路功能，这是一个拥有较长发展历史的研究领域。体现在游戏中，尤其是拥有复杂世界地图的RPG游戏中，自动寻路也是方便玩家操作的常见功能。<br>
<br>
宏观来看，无论是“逮虾户”的汽车自动驾驶，还是分拣包裹的机器人，亦或者在偌大地图上指引玩家纵横四海的游戏指引，全都离不开这项简单但实用的技术。<br>
<br>
本文以自动寻路的演化和应用作为展开，简单阐述这项改变人类生活（至少改变了一丢丢）的技术。<br>
<br>
<strong><font color="#de5650">自动寻路技术的演化历史</font></strong><br>
<br>
我曾经在无法登录联机模式的一个多月里，把《泰坦陨落2》的主线剧情玩了两遍，甚至挑战了大师难度。<br>
<br>
体验剧情期间，我逐渐对游戏中伴随主角库伯的泰坦BT-7274产生了兴趣。BT是位看似榆木脑袋实则富含人情味，可以“抄近路”掉坑或“协议三：保护铁驭”的亲密战友。<br>
<br>
<div align="center">
<img id="aimg_981966" aid="981966" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132523c8hytp8ps80trati.png" data-original="https://di.gameres.com/attachment/forum/202105/31/132523c8hytp8ps80trati.png" width="571" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132523c8hytp8ps80trati.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《泰坦陨落2》，BT和库伯之间的信赖超乎一般人机交互，AI显然更加“像人”</font></font></div><br>
可惜的是，现实中此类技术水平的辅助AI是不存在的，因为即使是为了完成“找条近路或者不堵的路”这一诉求，研究者们也已历经十数载，付出无数的熬夜，收获颈椎病和掉头发……<br>
<br>
我首先对这个词进行分解，“自动寻路”的母命题是“寻路 Wayfinding”，根据维基百科的介绍2，寻路指代：<br>
<br>
人（动物）在物理空间上定位以及从一个地点去往另一个地点的所有导航方法的集合。<br>
<br>
因此自动寻路是“导航 Navigation”功能的一种延伸或者发展3，而导航则具体指代：<br>
<br>
监控载具从一个地点到另一个地点移动的过程。<br>
<br>
然而广域的历史维度里，导航技术的发展几乎伴随着人类的发展4。<br>
<br>
历史上最早的导航法认为是波利尼西亚航海法（Polynesian Navigation，1761）5。从迁徙到航海再到航天，从腓尼基到麦哲伦再到加加林，导航技术的不断革新催生社会进步，这是先驱者所汲汲的科学之力也是推动历史车轮的驾辕之马。<br>
<br>
<div align="center">
<img id="aimg_981967" aid="981967" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132524i25pa688kl2wz982.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132524i25pa688kl2wz982.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132524i25pa688kl2wz982.jpg" referrerpolicy="no-referrer">
</div><br>
抛开长篇巨制的航海史，当代自动寻路功能的实现是来自寻路算法“路径探索 Pathfinding6” ，它的目的是用程序绘制两个点之间最短的路径。<br>
<br>
在这个研究领域中，在加权图上寻找最短路径的算法——迪杰斯特拉算法（Dijkstra's algorithm）7，是数据结构课本上最经典的算法之一。而绝大多数的研究成果都源自计算机科学家埃德斯格·迪杰斯特拉（Edsger W. Dijkstra）8于1956年构思。，<br>
<br>
在2001年接受《ACM通讯》杂志采访时，迪杰斯特拉回忆和分享了他当年构思该算法的故事：<br>
<br>
从鹿特丹到格罗宁根的最短旅行线路是什么？我大概花了二十分钟去构思这个最短路径问题。<br>
<br>
那是一天早上，我和未婚妻在阿姆斯特丹购物，我们觉得累了于是便坐在咖啡馆的露台上喝杯咖啡，当时我只是疑虑自己是否能做到这一点，于是我设计出了这个最短路径算法。正如我之前所说，这只是一个只用了二十分钟的发明。<br>
<br>
同样的，贝尔实验室的罗伯特·普里姆（Robert C. Prim）和同事约瑟夫·克鲁斯卡尔（Joseph Kruskal）也开发了两种不同的寻路算法，即Prim算法和Kruskal算法9，但是Prim算法是在迪杰斯特拉在解决“最大限度地减少连接机器后面板上引脚所需的电线量”这一问题时重新发现。<br>
<div align="center">
<img id="aimg_981968" aid="981968" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132524tnubos6yz131bnbu.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132524tnubos6yz131bnbu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132524tnubos6yz131bnbu.jpg" referrerpolicy="no-referrer">
、</div><br>
<div align="center">
<img id="aimg_981980" aid="981980" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132651dcgzkojkuc6aeg1e.gif" data-original="https://di.gameres.com/attachment/forum/202105/31/132651dcgzkojkuc6aeg1e.gif" width="210" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132651dcgzkojkuc6aeg1e.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">迪杰斯特拉算法的演示动画</font></div><br>
除了迪杰斯特拉算法，各种更有趣的经典算法，比如弗洛伊德算法、Bellman-Ford算法、SPFA算法等也被陆续提出（觉得陌生不用担心，因为它们最终会出现在计算机系同学的期末试卷上）。<br>
<br>
在这篇文稿中，我不准备去介绍这些专业内觉得简单，专业外觉得晦涩的知识，我们只要知道，在迪杰斯特拉算法提出之后，诸如A* algorithm，Sample algorithm等方法也被陆续提出。<br>
<br>
在这其中，A*算法是常见的在游戏中使用的最短路径算法，它的实质则是一个迪杰斯特拉算法的变体10。<br>
<br>
随着游戏产品的功能日渐丰富，各式算法也逐渐应用在这一产业领域，游戏的AI寻路功能作为基础需求也被提出。<br>
<br>
在1982年，克里斯·克劳福德（Chris Crawford）11回顾了他在游戏《Tanktics》（1976）12中为坦克设计寻路功能而煞费苦心，为此，我找到了1982年的Vol,2 Number 1期的《Computer Gaming World》杂志，幸运的是，此杂志的往期是公开的，我有幸回顾了关于《Tanktics》和设计师克劳福德的专题报道。<br>
<br>
<div align="center">
<img id="aimg_981969" aid="981969" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132524qcc9pq7v7u92va9z.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132524qcc9pq7v7u92va9z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132524qcc9pq7v7u92va9z.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_981970" aid="981970" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132525qbielx7jdevv5jky.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132525qbielx7jdevv5jky.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132525qbielx7jdevv5jky.jpg" referrerpolicy="no-referrer">
</div><br>
我必须讲明，《Tanktics》并未查证是世界上第一款拥有寻路功能的游戏，我以他举例是参考wiki词条编辑者的观点：这个游戏以及游戏设计者遇到的困难（寻路难）非常具有典型性。<br>
<br>
为了解决寻路问题，克劳福德在《Tanktics》中不得不对游戏地图的山脉湖泊进行大量修改，删除许多地形结构，以适应AI的行为逻辑（在电脑游戏中，AI一方面需要对大地图中的行为路径进行规划，一方面又必须保证该算法具有较少的CPU资源和时间调用）。<br>
<br>
A*算法是一种启发式算法，它的运行方法依赖于创建位置对应的节点， 这些节点同时也存储着搜索的进度，但是显而易见的是，这种方法仅仅适合在2D地图的游戏中进行路径搜索。<br>
<br>
在图形处理能力暴涨的当前，3D游戏场景带来的“空间z轴”使得A*算法需要处理的节点呈现指数增长13。经典算法亟待进化以适应新的需求。<br>
<br>
这部分的资料很难找，幸好我在CNKI上找到了一篇硕士论文《人工智能寻路算法在电子游戏中的研究和应用》，该作者称本篇论文的研究基础源于《圣铠传说》14游戏中的寻路算法，其中就有关于A*算法在游戏中的优化，接下来我将简要概括一下这些论文内容15。<br>
<br>
<div align="center">
<img id="aimg_981971" aid="981971" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132525mj6ef633jmrtb0bb.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132525mj6ef633jmrtb0bb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132525mj6ef633jmrtb0bb.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_981972" aid="981972" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132525umeht6dhsfhyhyts.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132525umeht6dhsfhyhyts.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132525umeht6dhsfhyhyts.jpg" referrerpolicy="no-referrer">
</div><br>
因此，以地图尺寸（宏观的大地图和微观的小地图）为衡量建立的分层寻路体系，可以在兼顾硬件资源的前提下更好地实现AI角色寻路要求，该改进型算法在《帝国时代》《星际争霸》等RTS作品都有所体现。<br>
<br>
而在如Unity3D等游戏引擎中，基于A*算法的WayPoint算法依旧是AI寻路功能实现的主要方法。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">饱受争议的游戏功能</font></strong><br>
<br>
从上节中可以获知，寻路功能最初是为了方便电脑AI拥有更好的性能，提升游戏的游戏性。但是随着游戏市场的规模扩大以及游戏受众的扩大，很多人对于游戏中的自动寻路功能提出质疑和不满。<br>
<br>
有人指出，“自动寻路”功能会削弱玩家在游戏中的操纵体验，降低游戏的游玩乐趣。但是也有人坚持，自动寻路可以简化游戏操作，降低准入下限，从而提升玩家游戏体验。<br>
<br>
比如以下这三部作品，可以姑且算作RTS、MMORPG、（部分劣质的）网页游戏的代表，从中我们不难体会寻路功能和其算法在过去十数年中为无数玩家带来的乐趣、回忆以及烦恼。<br>
<br>
<div align="center">
<img id="aimg_981973" aid="981973" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132526yfult6xnipntbinr.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132526yfult6xnipntbinr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132526yfult6xnipntbinr.jpg" referrerpolicy="no-referrer">
</div><br>
然而，这个问题并不怪罪于寻路功能本身，自动寻路带来的争议源自游戏产品设计思路和玩家心理作用。准确来说，它本质上是一个心理学/社会学问题。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_981974" aid="981974" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132526jbgjpees5tjh5s7e.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132526jbgjpees5tjh5s7e.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132526jbgjpees5tjh5s7e.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">“风暴要火” ：MOBA或者说DOTA-LIKE游戏脱胎自RTS游戏，玩家操作单个角色进行多人合作竞技，这类游戏兼顾玩家的成就心和社交属性</font></font></div><br>
首先自动寻路功能大多出现在大型多人在线网络游戏——MMORPG中，此类游戏的世界地图往往相当庞大，玩家在多个地点之间的移动往往会造成画面卡顿、寻路效率低等问题。<br>
<br>
造成这些问题的原因在前文关于A*算法的讲解中已经提到，无非是节点数量过多导致的资源占用导致的。<br>
<br>
为了解决这个问题，MMORPG游戏往往采取以下几种方法16：<br>
<br>
首先是地图的动态加载。通过玩家的角色位置动态加载位置，并建立动态的索引表实时进行寻路，或者是建立评估函数，对路径进行估算建立代价最低的通路。<br>
<br>
从此角度看，自动寻路系统确实让玩家能高效游玩，避免了因为在地图中辗转跑路所带来的繁琐重复操作、大量时间浪费以及游戏体验下降等弊端。<br>
<br>
然而，不可以“抛开计量谈毒性”。<br>
<br>
难以否认的是，如今大量劣质游戏充斥游戏市场，它们最普遍的特征就是几乎完全自动化的操作，游玩时可能只需要寥寥点按几下按键；大量趋同且夸张的游戏装备系统和反馈机制（一刀999）；在部分手机游戏也包含了大量的自动操作内容，降低玩家的手控操作需求。<br>
<br>
凡此种种，以自动寻路功能为代表的自动化功能已经烙上“快餐化，劣质化”的标签。<br>
<br>
但是我认为：<br>
<br>
忽视体验的功能堆叠、对于产品游戏性的无视、诱导用户消费的急功近利才是导致游戏产品劣质化的原因，而自动寻路等功能仅仅作为其比较突出的外部特征，却成为了被批评的众矢之的。<br>
<br>
<div align="center">
<img id="aimg_981975" aid="981975" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132526z4zu0jtui7ztq2zy.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132526z4zu0jtui7ztq2zy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132526z4zu0jtui7ztq2zy.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">鲲吞的不是亘古巨兽，而是玩家的热爱和感情。可惜的是，劣币驱良币的丑剧依旧在不断上演</font></font></div><br>
介于端游与手游之间，轻量化Web网页游戏几乎见证了游戏市场的繁荣和畸变。以此为例（仅指代部分劣质网页游戏），我将从游戏运营、玩家体验两方面介绍造成游戏功能和体验之间矛盾的咎因。<br>
<br>
<strong>1.逐渐跑偏的游戏运营</strong><br>
<br>
在2000年前后，“免费游戏”机制代替“月卡”机制成为各种网络游戏的运营方式17，以此为分水岭，玩家的游戏门槛大大降低，而点卡计时收费也转变为购买道具。<br>
<br>
这种商业模式在极大提升游戏营收的同时，带来了许多危及行业生态的隐患。<br>
<br>
首先便是业界普遍存在的抄袭现象，这一现象最直观体验就是游戏中的图像（外向）、背景（内在）、可独立部分（设计）等的同质化18，然而在规章约束有限的当下，这种不正之风依然司空见惯。<br>
<br>
除此以外，诸如自动寻路等功能在游戏中的保留目的是尽可能简化游戏操作流程，玩家从游戏中获取的心理预期来自于简单的数值比拼和虚拟社区中的声望。<br>
<br>
加之交易体系和类似赌博的概率抽奖机制，此类游戏的运营目的已经从“以玩家体验为中心”向“满足玩家成就感（满足心态）”转变，玩家的心态和情绪其实已经被刻意扭曲。<br>
<br>
<strong>2.逐渐淡薄的游戏体验</strong><br>
<br>
正如部分玩家所批评的，自动寻路过度简化游戏内容，全自动化的流程淡薄了游戏体验；而数值化、功利化的社区环境（运营有意为之）还造成了游戏的戾气。<br>
<br>
游戏社区是一个虚拟的社交平台，根据社会网络理论，亲密性、互动时间、互动频率和互惠互利是衡量社交关系强度的四个指标19，和谐的社交关系有助于玩家在人际中保持乐观和积极的态度，反之，充满竞争的社区中则会诞生交往障碍，人际疏离。<br>
<br>
（没错，有的人线上打的火热，线下孤独一人……比如我。即使没有直观的感受，但这也是游戏开发者刻意营造或者蓄意引导的玩家感受。）<br>
<br>
在游戏中，玩家往往会追求成就感，这就形成了“游戏等级（数值）→ 玩家之间的竞争（良性/恶性）→ 成就感”的游戏体验脉络20。<br>
<br>
围绕数值促成竞争，以成就感为目标价值的玩家往往会更乐意争取额外奖励（显眼的形态、罕见物品或者称号等），而这一切的代价就是急功近利的支出资金和精力（土豪也不例外的）。<br>
<br>
<div align="center">
<img id="aimg_981976" aid="981976" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132526m333ztv22jx3vo35.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132526m333ztv22jx3vo35.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132526m333ztv22jx3vo35.jpg" referrerpolicy="no-referrer">
</div><br>
这一章节内容与“自动寻路”功能似乎有些不搭界，实际上，联系前文所讲述的算法更迭历史，我想表达的是：<br>
<br>
这是一个颇具“讽刺意味”的寓言故事：<br>
<br>
寻路功能与算法最初是为了给游戏带来更棒的游戏体验，在五十几年前，开发者们做到了，更聪明的电脑AI诞生，更高效低费的算法实现，于是玩法多样，好玩有趣的游戏不断诞生。最终在发展顶峰即RTS游戏里，F2A千军万马也能井然有序地换家。<br>
<br>
只是后来，大家忘记了这个功能的本意，在几乎畸形的游戏市场环境中，诞生了一堆以玩家成就感为诱导的，充满氪金，以恶性竞争为核心的游戏产品。<br>
<br>
说开发者抓住了玩家“人”的劣性，以社区生态为代价大肆收割利益，自动寻路作为游戏操作自动化的基础被他们大肆滥用，开发者全然不顾产品的游戏性，“滚服”走过，素材拼凑又是整装待发。<br>
<br>
他们就像史矛革，眼里只有黄金。<br>
<br>
<strong><font color="#de5650">值得期待的应用前景</font></strong><br>
<br>
<div align="center">
<img id="aimg_981977" aid="981977" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132527nbrmwyehfzeftwme.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132527nbrmwyehfzeftwme.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132527nbrmwyehfzeftwme.jpg" referrerpolicy="no-referrer">
</div><br>
“算法永远不会骗人”，即使发展已有数十年，自动寻路功能依旧在现实生活中起着重要作用。<br>
<br>
在此最值得介绍的就是导航技术和无人驾驶技术。但是它已不再是需要兼顾效费的经典算法，目前的寻路算法依托AI技术（Artificial Intelligence和前文的游戏AI不同，这里指一个广泛的研究领域21，包含机器学习、神经网络、深度学习等领域）。<br>
<br>
随着物联网技术的发展，一些跨学科应用被不断提出，其中，一个利用无人机（UAV）进行高空拍摄单幅全景图像来评估空气质量指数的文章22就是其中典型，作者在研究中指出，他们为无人机指定飞行路线时便采用了经典最短路的优化算法。<br>
<br>
这是我最近精读的一篇文章，似乎与本文主题有点搭，于是拿出来稍稍讲一下，哒哒哒~<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_981978" aid="981978" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132527whh6q13t6sloowp6.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132527whh6q13t6sloowp6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132527whh6q13t6sloowp6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">这是本文 AQ360: UAV-aided air quality monitoring by 360-degree aerial panoramic images in urban areas 的图摘要</font></font></div><br>
<div align="center">
<img id="aimg_981979" aid="981979" zoomfile="https://di.gameres.com/attachment/forum/202105/31/132527pq0qir6z75nci506.jpg" data-original="https://di.gameres.com/attachment/forum/202105/31/132527pq0qir6z75nci506.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/31/132527pq0qir6z75nci506.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">无人机寻路原理的示意图，路径上的权值决定了它的下一个目标区块，最终达到最短路径完成拍摄任务</font></font></div><br>
无人机的算法将目标区域划分为一个个六边形区块，然后依据区块内建筑物的高低（因为高层建筑会遮蔽拍摄视角）设计飞行路线。在电池耗能的前提下，保证拍摄的照片可以最大程度的囊括区域内所有场景，提升评估准确率。<br>
<br>
类似的应用还有很多，包括不仅限于“扫地机器人规划房间清扫线路”和“战斗机器人规划巡逻线路（这个真的有）”<br>
<br>
但是这些看似智能的路径规划，其原理“只是”一种可以自学习的网络结构，它来自于简单的线性和非线性函数，通过权值和偏差值的变化对目标进行自适应以总结特征规律，并封装为模型路径，成为可以适用在各种场景中的“算法模型”。<br>
<br>
在真实世界里，它们几乎可以应用在现实生活中的各种领域内，只是不像“BT”“查亚塔”或者“傀儡师”，由于模型不存在内在的逻辑性，这些电子神经网络并不会产生奇特的”脑波“，更别提没有足够的存储。所以并不会产生科幻电影中的“智械危机”“天网灭世”。<br>
<br>
最后的最后，回到游戏中，随着开放世界成为越来越多开发商所热衷的游戏要素，自动寻路也在以不同的形象登场在各个游戏世界中。<br>
<br>
但是作为一种最常见的游戏功能，无论它的算法历经多少次迭代，优化，编译，封装，调用，它依旧会忠实地履行自己的使命。<br>
<br>
在GTA5中它是小地图上标记紫色的通路，在《巫师3》里它是不断扭动的点线指引，在《辐射4》里它是不怎么好用的距离光标，在《无主之地3》中它是一个变化大小的菱形图标......<br>
<br>
忘记现实，迷失在游戏世界里也是游戏的一部分。<br>
<br>
<strong><font color="#de5650">后记</font></strong><br>
<br>
真没想到星帖奖还可以再回来。由于我最近在写一些学习上的东西，不自觉地，自己写文的思路就会随着平时看的文献一起互相交织，于是原本侃侃而谈的文字竟然也变得严肃起来。<br>
<br>
这一次征文，我决心跳脱“介绍游戏”的思路。我决定尝试阐述游戏功能的发展历史、现状以及前景，这是一次很有意思的尝试，文中既有大量历史背景的科普，同时也包含部分领域专业知识，甚至还有心理学的讨论。同样的，这篇文字也带给我巨大的工作量，我需要查阅大量文献，从中一点点整理有用的知识点和思想，CNKI和谷歌学术可以帮我写游戏杂谈，SCI一区的核心顶刊被我引用拿来打豆豆，这是我最近的重大发现，跑。<br>
<br>
文字写得仓促和粗糙，纰漏也所难免，希望我的文字能对大家有所帮助，或者博君一笑也足够了。<br>
<br>
南大鳥<br>
<br>
2021年5月19日 金城 大雨<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：TapTap发现好游戏</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/t_iSEMqITKEU_zRbelzueg</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            