
---
title: 'APEX关卡设计分析，它是如何做到横空出世依旧保持热度至今？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/14/093713z6zyu6hucuhu6coc.jpg'
author: GameRes 游资网
comments: false
date: Thu, 14 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/14/093713z6zyu6hucuhu6coc.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516630">
<div align="center">
<img id="aimg_1014492" aid="1014492" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093713z6zyu6hucuhu6coc.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093713z6zyu6hucuhu6coc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093713z6zyu6hucuhu6coc.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#808080">本文首发知乎：</font><br><font color="#808080">https://zhuanlan.zhihu.com/p/415125826</font><br><br><strong><font color="#de5650">一、前言</font></strong><br><br>
距离“战术竞技”这一游戏类型的兴起已经四年了，在此期间涌现了许多优秀的作品，其中《APEX英雄》的横空出世引发了现象级的热度，直至今日都仍是热度最高的几款战术竞技射击类游戏之一，笔者也深深的沉浸其中数百小时。<br><br>
笔者作为一名关卡设计师，想试图将自身几百小时的游戏体验，以关卡设计的角度，从感性认识发展到理性认识，希望能与大家一起交流<br><br>
如果看完觉得有所启发，别忘点个赞哦~，你们的赞赏是我分享的最大动力<br><br><strong>1.1战术竞技类游戏的定义以及特点</strong><br><br>
《APEX》作为一款战术竞技射击游戏，想要分析其关卡，首先需要理解什么是战术竞技游戏。<br><br><font color="#de5650">1）广义定义</font><br><br>
广义的战术竞技类游戏是指多方玩家在一局游戏中同台竞技，直至战至只剩最后一方玩家存活。<br><br>
广义的战术竞技游戏除了包括《PUBG》《APEX英雄》《Fortnite》《COD战区》外，还包括了《糖豆人终极淘汰赛》《俄罗斯方块 99》等另类的战术竞技游戏，今天我们要讨论的《APEX》属于狭义上的战术竞技游戏。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014493" aid="1014493" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093714wjqi11n10m60966o.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093714wjqi11n10m60966o.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093714wjqi11n10m60966o.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">广义上的战术竞技游戏</font></font></div>
<br><font color="#de5650">2）狭义定义</font><br><br>
狭义上的战术竞技类游戏是指多方玩家在一块大地图上收集物资，前往越缩越小的安全区，进行玩家间死斗直至最后一方玩家获胜的游戏类型<br><br>
《PUBG》、《APEX英雄》、《Fortnite》以及最近在Steam上大热的国产武侠题材多人竞技游戏《永劫无间》都属于狭义上的战术竞技游戏<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014494" aid="1014494" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093714p026fotszttmfnsv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093714p026fotszttmfnsv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093714p026fotszttmfnsv.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">永劫无间</font></font></div>
<br><font color="#de5650">3）狭义的战术竞技类游戏的特点</font><br><br><ul><li>参战方众多<br>
</li></ul>
<br>
与传统的双方竞技游戏不同，其往往有数十人组成的数十只小队同台竞技，除了队友之外，你所见到的一切人皆为敌人<br><br><ul><li>大地图<br>
</li></ul>
<br>
与传统的双方竞技的百米以内宽度的小地图关卡不同，该类游戏往往地图的宽度有数公里，以容纳数量众多的参战玩家<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014495" aid="1014495" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093714n46nzjs9jeah7yzs.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093714n46nzjs9jeah7yzs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093714n46nzjs9jeah7yzs.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">《APEX英雄》奥林匹斯</font></font></div>
<br><ul><li>强调生存<br>
</li></ul>
<br>
获胜者只有一方，存活下来是游戏的第一目标<br><br><ul><li>逐渐紧张的情感体验<br>
</li></ul>
<br>
随着安全区越缩越小，玩家的紧张情绪逐渐拔高，在决赛圈时玩家的情绪是高度紧张的<br><br><ul><li>高随机性<br>
</li></ul>
<br>
航线、物资、安全区等随机要素，使每局游戏都充满不确定性，让玩家每局体验都不同<br><br><ul><li>收集乐趣<br>
</li></ul>
<br>
满足收集欲，谁能拒绝捡垃圾的快乐呢（笑<br><br><strong><font color="#de5650">二、OPER循环与关卡可读性</font></strong><br><br>
在分析《APEX英雄》关卡设计之前，先引入两个理论概念，本篇文章后续的分析，将会根据这两个理论为基础<br><br><strong>2.1 OPER循环</strong><br><br>
OPER循环是玩家游戏行为的内在逻辑规律，OPER循环可以为关卡设计分析提供一方面的理论框架<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014496" aid="1014496" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093715t64bj7y5570zmbt4.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093715t64bj7y5570zmbt4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093715t64bj7y5570zmbt4.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">OPER循环</font></font></div>
<br><font color="#de5650">1）Observe观察</font><br><br>
玩家观察场景并从中获取信息<br><br><font color="#de5650">2）Plan计划</font><br><br>
玩家根据观察所获取的信息，结合他们的目标来制定计划<br><br><font color="#de5650">3）Execute执行</font><br><br>
计划已制定，玩家开始执行计划<br><br><font color="#de5650">4）React反馈</font><br><br>
玩家得到计划执行的反馈，计划执行完成后，玩家重新观察，进行下一次循环<br><br><strong>以跑毒为例</strong><br><br>
以跑毒为例，玩家观察进圈路线，观察其他敌人动向尽可能的收集信息（观察），然后制定进圈计划（计划），执行计划（执行），在跑毒的过程中并不一定会如计划所料，当计划完成或计划出现变故，比如出现了意料之外的敌人（反馈），那么玩家将重新观察进行下一步的循环（观察）<br><br><strong>2.2 关卡可读性</strong><br><br><font color="#de5650">1）定义</font><br><br>
玩家获取关卡中包含信息的难易程度，关卡的可被玩家记忆的难易程度也包含在关卡可读性中<br><br><font color="#de5650">2）作用</font><br><br><ul>
<li>关卡可读性是为OPER循环中的Observe观察服务的</li>
<li>关卡可读性好，玩家就更容易获取信息，以便制定计划，使玩家的OPER循环更为流畅</li>
<li>可读性烂，玩家就得在获取信息这一步耗费更多的时间，使得OPER循环中的一环受阻，玩家的体验就会很糟糕<br>
</li>
</ul>
<br><strong><font color="#de5650">三、资源点等级设计</font></strong><br><br>
APEX中的资源点等级从低到高为白（低级）、蓝（中级）、紫（高级），高级资源点更容易产出高级资源<br><br>
这样设计的好处是更显性的告诉玩家一个资源点的富裕程度，提升关卡可读性，跳伞阶段玩家通过这些信息，可以更好的决定该降落在哪里<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014497" aid="1014497" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093715bjc3p6z963ooywtw.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093715bjc3p6z963ooywtw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093715bjc3p6z963ooywtw.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">诸王峡谷各资源点等级分布</font></font></div>
<br><strong><font color="#de5650">四、资源点的关卡设计分析</font></strong><br><br>
在这一节笔者将分析《APEX英雄》的资源点设计思路<br><br><strong>4.1 资源点的关卡设计维度</strong><br><br><font color="#de5650">1）资源点定位</font><br><br>
资源点定位包含以下维度：<br><br><ul><li>位置定位<br>
</li></ul>
<br>
资源点在地图中处于什么位置（影响跑毒），与其他资源点的关系是什么等等<br><br><ul><li>资源点等级定位<br>
</li></ul>
<br>
资源点等级是什么样的，资源点资源数量是多少？<br><br><ul><li>资源点面积<br>
</li></ul>
<br>
资源点面积有多大？能容纳几个小队？<br><br><font color="#de5650">2）区块划分</font><br><br>
资源点内有几块区域，这些区域的特征是怎么样的？<br><br>
清晰的区块划分容易被玩家记忆，从而提高关卡可读性，进而使OPER循环更顺畅，提升玩家体验<br><br><font color="#de5650">3）连接路径</font><br><br>
区块与区块之间通过什么样的路径连接？<br><br>
清晰的路径连接容易观察，并且容易被玩家记忆，从而提高关卡可读性，进而使OPER循环更顺畅，提升玩家体验<br><br><font color="#de5650">4）区块关系</font><br><br>
区块与区块之间的关系是怎么样的？<br><br>
比如某块区域中包含了资源点的制高点，可以威胁所有区块等等这种类似的设计，如果区域之间的关系清晰，那么玩家就可以轻松利用这些信息，来制定计划<br><br><strong>4.2 奥林匹斯-绿洲的关卡设计</strong><br><br>
接下来笔者会奥林匹斯的绿洲为例以更好的说明笔者的分析维度，这也是笔者最喜欢的APEX BR模式关卡，因为绿洲场景漂亮，区块划分、区块关系、连接路径都十分清晰，且有趣<br><br>
废话不多说，开始正题<br><br><div align="center">
<img id="aimg_1014498" aid="1014498" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093716yhhwgagiagfgwsi6.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093716yhhwgagiagfgwsi6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093716yhhwgagiagfgwsi6.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#de5650">1）资源点定位</font><br><br><ul>
<li>绿洲位于地图左侧的地图边缘，需要跑毒的概率高</li>
<li>绿洲的北、东、南端都各分布了一个野点，在跳伞阶段如果发现绿洲去的人太多，飞去这几个野点等劝绿洲的架也是一个不错的选择</li>
<li>绿洲是高级资源点，长宽为200M*160M，能容纳两支小队<br>
</li>
</ul>
<br><div align="center">
<img id="aimg_1014499" aid="1014499" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093716pac1hlxn1ndbsznh.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093716pac1hlxn1ndbsznh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093716pac1hlxn1ndbsznh.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#de5650">2）区块划分</font><br><br><ul>
<li>绿洲总共分为3个区块，区块划分非常清晰，可读性很强</li>
<li>区块1、区块2各由一栋三层建筑为主体，建筑下方还有地下室，通过滑索与一楼相连</li>
<li>区块3相对高度较低，但是可以从侧面前往地下室<br>
</li>
</ul>
<br><div align="center">
<img id="aimg_1014500" aid="1014500" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093716wzsbk5z0l546rdgt.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093716wzsbk5z0l546rdgt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093716wzsbk5z0l546rdgt.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">地上区域划分角度1</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014501" aid="1014501" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093717l0qb53e00ng50z05.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093717l0qb53e00ng50z05.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093717l0qb53e00ng50z05.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">地上区域划分角度2</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014502" aid="1014502" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093717tfsckssb22gffh98.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093717tfsckssb22gffh98.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093717tfsckssb22gffh98.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">地下区域划分</font></font></div>
<br><font color="#de5650">3）连接路径</font><br><br>
从平面图上看，区域1、2、3无论是地上空间还是地下空间，路径连接都是十分的清晰的，清晰的路径可以使玩家更好的去制定进攻计划或防御计划<br><br><div align="center">
<img id="aimg_1014503" aid="1014503" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093717re2sfeccng8tttcs.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093717re2sfeccng8tttcs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093717re2sfeccng8tttcs.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">地上区域平面图简图</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014504" aid="1014504" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093718jnjjzjkkvcbe5bu4.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093718jnjjzjkkvcbe5bu4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093718jnjjzjkkvcbe5bu4.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">地上区域平面图简图</font></font></div>
<br><font color="#de5650">4）区块关系</font><br><br>
地上区域<br><br><ul>
<li>区块1、2的三层建筑的第三层是资源点地上区域的制高点，且两栋楼的三层高度相同，相互形成相互平衡的对峙关系</li>
<li>区块1、2的高度相对区块3高，对区块3是被高打低的一个区块<br>
</li>
</ul>
<br>
地下区域<br><br><ul>
<li>地下部分的区块1、2高度相同，仍处于相互平衡的对峙关系</li>
<li>区块3在地下部分咸鱼翻身，区块3的地下高度比区块1、2高，区块1、2被区块3高打低<br>
</li>
</ul>
<br><div align="center">
<img id="aimg_1014505" aid="1014505" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093718hzv5z4q8vv441pfq.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093718hzv5z4q8vv441pfq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093718hzv5z4q8vv441pfq.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">地上区域区域关系图</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014506" aid="1014506" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093718rciigh4gb8nihbfp.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093718rciigh4gb8nihbfp.jpg" width="551" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093718rciigh4gb8nihbfp.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">地下部分区域关系图</font></font></div>
<br><strong>5）总结</strong><br><br><ul>
<li>区域划分清晰，可读性强，可以使玩家跳伞选择绿洲的落点时，有着明确的选择，落区域1、2？还是落区块3？这些选择都是十分明确的，降落时的OPER循环是流畅的</li>
<li>连接路径清晰，可读性强，可以使玩家在进攻或防御时有着明确的策略选择，OPER循环也是流畅的</li>
<li>区域关系清晰，玩家十分清楚每个区域之间是什么样的关系，玩家可以利用这些信息来制定明确的计划</li>
<li>《APEX英雄》中还有许多优秀的资源点设计，例如奥林匹斯的盆栽广场、世界边缘的倒计时、发射场等等，此处对绿洲的分析仅作为抛砖引玉<br>
</li>
</ul>
<br><strong><font color="#de5650">五、资源点间的路径连接</font></strong><br><br>
很多玩家刚玩APEX时，会发现APEX的每张地图上都会有非常多的不可逾越的高山（瓦鸡除外）这是其他战术竞技游戏所没有的，APEX为什么要设计这么多高山呢？笔者想分享以下自己的见解。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014507" aid="1014507" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093718bl1pfvp2vyvylhfy.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093718bl1pfvp2vyvylhfy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093718bl1pfvp2vyvylhfy.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">世界边缘的高山</font></font></div>
<br><strong>5.1 高山的作用其一：分割战场</strong><br><br><font color="#de5650">1）分割视野、枪线、玩家位置</font><br><br><ul>
<li>由于APEX是一款TTK长的游戏，APEX打完一场架的时间偏长，如果没有高山分割视野和枪线，打架的双方不管谁赢了，都会非常容易被劝架，玩家就会变得越来越不想打架，这与APEX鼓励战斗的设计理念相违背。</li>
<li>如下面两张图所示，当没有高山的时候，小队2与小队3打起来，小队1非常容易就能劝架，甚至能原地劝架。</li>
<li>而有高山的时候，小队3赶来劝架还需要绕过高山，并且有高山作为枪线阻隔，小队1无法原地劝架，这就给了小队2、3更多的打架时间，只要在小队1赶来劝架前结束战斗就万事大吉。<br>
</li>
</ul>
<br><div align="center">
<img id="aimg_1014508" aid="1014508" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093719a3l3lbs0usxxsau9.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093719a3l3lbs0usxxsau9.jpg" width="333" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093719a3l3lbs0usxxsau9.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1014509" aid="1014509" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093719ekp2x4qqkrdkktxr.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093719ekp2x4qqkrdkktxr.jpg" width="462" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093719ekp2x4qqkrdkktxr.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>5.2 高山的作用其二：创造阻塞点</strong><br><br>
阻塞点的含义大家可以参考我的上一篇文章：<CSGO关卡设计要点>链接：https://zhuanlan.zhihu.com/p/165137244<br><br>
两座高山之间形成的小关口，就是一个阻塞点。<br><br>
阻塞点的作用是控制玩家流向，将玩家的移动路径收缩为几个点，玩家想要进圈，必须要越过这些阻塞点的其中之一，这就给自由的大地图带来了一些确定的因素。<br><br><ul>
<li>对于跑毒的玩家来说，确定数量的阻塞点，将限制玩家的策略选择，使关卡变得易读，这会使玩家的OPER循环变得流畅。</li>
<li>对于靠近安全区一侧的玩家来说，确定数量的阻塞点可以让玩家清晰的知道跑毒玩家一定会通过这些阻塞点的其中之一，这给靠近安全区预测的玩家提供了明确的策略选择的选项，堵不堵阻塞点？堵哪个？</li>
<li>这种确定性会使双方玩家进行精彩的博弈，阻塞点的设计真令人拍案叫绝。<br>
</li>
</ul>
<br><strong>在下面的例子中：</strong><br><br><ul>
<li>小队1（无瓦鸡）想进圈就必须要通过阻塞点1或者阻塞点2才能抵达安全区。</li>
<li>小队2如果知道山的另一侧有一支小队的话，小队2也会明确的知道小队1想进入安全区必须要通过这两个阻塞点的其中一个，这时小队2就可以选择是否要在某个阻塞点等待小队1过来。<br>
</li>
</ul>
<br><div align="center">
<img id="aimg_1014510" aid="1014510" zoomfile="https://di.gameres.com/attachment/forum/202110/14/093719mtx888bobtb8sasx.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/093719mtx888bobtb8sasx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/093719mtx888bobtb8sasx.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">结语</font></strong><br><br>
至此笔者对于《APEX英雄》的关卡分析就暂时告一段落啦，之后笔者会继续实践学习，完善这篇文章，诸君共勉！<br><br><font color="#808080">参考资料</font><br><br><div align="center">
<span id="flv_qmc"></span>
</div>
<br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/415125826</font></font><br><br>
</td></tr></tbody></table>


  
</div>
            