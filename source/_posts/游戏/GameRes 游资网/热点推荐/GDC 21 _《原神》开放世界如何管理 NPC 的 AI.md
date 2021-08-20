
---
title: 'GDC 21 _《原神》开放世界如何管理 NPC 的 AI'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/12/111514kmy5x75aedrvavaa.jpg'
author: GameRes 游资网
comments: false
date: Thu, 12 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/12/111514kmy5x75aedrvavaa.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2509799">
原文发表于4Gamer.net，GNN繁体中文编译，此处仅做简单的简中转换以及部分词语的更改。<br>
<br>
2021 年 7 月 22 日，以线上形式举办的世界最大级游戏开发者会议 Game Developers Conference 2021 当中，由 miHoYo 的 Lead AI Programmer Shuo Xu 发表了以「’Genshin Impact’: Building Scalable AI System」为主题的演讲。<br>
<br>
《原神》（PC / PS5 / PS4 / iOS / Android）是一款 2020 年推出的开放世界 RPG，在手机与 PC 等平台博得世界级的人气。据说 Xu 先生是以负责人的身分参与设计该作的 AI 系统（在 3 年的制作下完成……）。本次演讲，为各位介绍一款在广大地图展开的开放世界型线上游戏，是透过什麽样的 AI 建构而成。<br>
<br>
<div align="center">
<img id="aimg_1000307" aid="1000307" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111514kmy5x75aedrvavaa.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111514kmy5x75aedrvavaa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111514kmy5x75aedrvavaa.jpg" referrerpolicy="no-referrer">
</div><br>
最初为各位解说的是 AI 系统结构（AI architecture），《原神》采用了多种类型的 AI。<br>
<br>
人类、野生动物、战斗中的 NPC 都分别采用个别的 AI，据说在推出的初期阶段有 200 种以上的数量。因此孕育出游戏设计师对於更有效率地制作出 AI 的工作流（Workflow）的需求。作为一款会持续改版更新的线上游戏，管理这些相关事务的工作便是 AI 框架（AI framework）的职责所在。<br>
<br>
<div align="center">
<img id="aimg_1000308" aid="1000308" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111514jsl88brl8as3capu.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111514jsl88brl8as3capu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111514jsl88brl8as3capu.jpg" referrerpolicy="no-referrer">
</div><br>
最初是以较为阳春的方法透过 AI 框架来组织出行为树（Behavior Tree），但是树状结构逐渐膨大，并且还有副行为树与大量节点的连结，在追加新的逻辑（Logic）时变更树状结构已经是很复杂的工程，同时判断难以持续维持这样的体系。<br>
<br>
从此开始建构出独立的 AI 管道（AI Pipeline），能够根据每个功能的推论模组（Inference Module）打散成不同的团体（Group），针对有需求的地方进行更新。接下来进入决策树（Decision Tree）的部分。这是一项近似於行为树的功能，但是仅只会做出各项决定与判断的轻量化功能。以这些决策为基础，决定发动技能或是进行移动等行为。具体的表现形态将以动画呈现，而这部分则是透过传输适当的参数给动画系统执行。这一连串的工作处理将在每一个框架的管理下进行运作。<br>
<br>
讲者表示，采用这项系统结构，能够以模组分类的方式开发各项功能，并且在制作新种类 AI 的时候还可以组合原本既有的模组来进行使用。功能上来说都各自独立，因此在开发新的 AI 功能模组的时候，也不会有对其他功能产生影响的疑虑。<br>
<br>
也因此能够赋予每个 NPC 个体不同的个性以及特殊能力。不只如此，就连 BOSS 级角色也能够轻易实现出独具特色的行动方式。<br>
<br>
<div align="center">
<img id="aimg_1000309" aid="1000309" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111515ahs9hfc7v7amrncs.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111515ahs9hfc7v7amrncs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111515ahs9hfc7v7amrncs.jpg" referrerpolicy="no-referrer">
</div><br>
为了综合满足以上需求所开发的工具就是 Key State Manager。这是一项有限性的状态机（State Machine），在战斗等时刻会启动，根据 BUFF 的状况或其他数值情况驱动。以此举例的是 Fire Slime 的例子，游戏设计师能够编辑好适当的状态转移（State Transition），并组织进入 AI 的系统之中。<br>
<br>
透过上述的 AI 管道与 Key State Manager 的运用，构筑出新的 AI 框架。<br>
<br>
<div align="center">
<img id="aimg_1000310" aid="1000310" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111515fpty9rgvh9k9e9dh.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111515fpty9rgvh9k9e9dh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111515fpty9rgvh9k9e9dh.jpg" referrerpolicy="no-referrer">
</div><br>
《原神》有一些开放世界性质上的制约存在。在移动时所使用的导航网格（Navigation Mesh），在刚推出时超过 70 平方 km 的地图上，必须采用到高达 6GB 大小的导航网格。话虽如此，这个容量本身并不是什麽太大的问题。现在已经是连手机都能运行 10GB 左右的时代，并且《原神》的导航是由伺服器端进行处理，6GB 程度的话似乎完全不算什麽问题。<br>
<br>
<div align="center">
<img id="aimg_1000311" aid="1000311" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111516n7jzajqoeaoo1kek.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111516n7jzajqoeaoo1kek.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111516n7jzajqoeaoo1kek.jpg" referrerpolicy="no-referrer">
</div><br>
投影片中显示的导航网格的例子，是横跨多层的 3 次元结构的地图，构造上来说相当复雑。据说这是 1 平方 km 左右的范围。<br>
<br>
<div align="center">
<img id="aimg_1000312" aid="1000312" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111516dusizf5ryrcyeq5y.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111516dusizf5ryrcyeq5y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111516dusizf5ryrcyeq5y.jpg" referrerpolicy="no-referrer">
</div><br>
再加上城镇中到处放有 2m 左右的狭窄道路，相当考验导航网格的精密度。对此曾反覆进行过多次实验，最终决定 Tile Size 为 128，Pozel Size 为 0.125m 是理想的配置。<br>
<br>
<div align="center">
<img id="aimg_1000313" aid="1000313" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111517neiaufh2ma2ui7zq.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111517neiaufh2ma2ui7zq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111517neiaufh2ma2ui7zq.jpg" referrerpolicy="no-referrer">
</div><br>
如上所述，导航的部分由伺服器端进行处理，发送出现在位置与目的地以後，就会自动回应出可行的路径（或者是没有路径）。<br>
<br>
<div align="center">
<img id="aimg_1000314" aid="1000314" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111518rlqhlm55etnumtqz.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111518rlqhlm55etnumtqz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111518rlqhlm55etnumtqz.jpg" referrerpolicy="no-referrer">
</div><br>
话虽如此，地图内存在着许多移动性的障碍物。为了对应这些状况，会根据连接的玩家个别留有一定的记忆体，并且能够应对各种可能发生的情况。在玩家识别出会阻碍道路的岩石的时候，伺服器会确保更新後的导航网格用拥有追加的记忆体，并用来对应此玩家的状况。<br>
<br>
<div align="center">
<img id="aimg_1000315" aid="1000315" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111520urw4xo7s4grnhf7j.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111520urw4xo7s4grnhf7j.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111520urw4xo7s4grnhf7j.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1000316" aid="1000316" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111522mx876y1yigzxoh8w.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111522mx876y1yigzxoh8w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111522mx876y1yigzxoh8w.jpg" referrerpolicy="no-referrer">
 
<img id="aimg_1000317" aid="1000317" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111524yacedkckhdnbbcue.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111524yacedkckhdnbbcue.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111524yacedkckhdnbbcue.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090">放置障碍物以前的路与放置後的路</font></font></div><br>
这个系统是以有 30 人以上 NPC 移动的状态，在 60fps 下运作的前提下设计而成，在最优化以前的阶段据说需用到 2～3ms 程度的 AI 处理。在当时似乎也遇到过热方面的问题，在本次演讲里面并没有多提。但毕竟是需要处理过热问题的情况，单纯以多执行绪（multithreading）来进行处理似乎是不可行的（处理效率的确会提升但热能也会升高）。<br>
<br>
因此导入 AI 团队的就是这项 LoD（Level of Deteil）的概念。在过去介绍过「Death Stranding」的 AI 相关报导中也有采用 LoD，看来在必须处理多名 NPC 的开放世界算是一项必须的技术也说不定。<br>
<br>
言归正传，《原神》之中使用了 3 个阶段的 LoD AI。根据距离切换的 2 个阶段以及战斗中的 1 个阶段。在战斗中虽然会全面运作，非战斗的情况下在玩家周围的 AI 处理也会以 30fps 的情况进行。较远的情况下则会以 5fps 的方式省略动画的处理。<br>
<br>
<div align="center">
<img id="aimg_1000318" aid="1000318" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111526uvx2lwx20vqzpsw7.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111526uvx2lwx20vqzpsw7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111526uvx2lwx20vqzpsw7.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1000319" aid="1000319" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111528p519bl1d9e9zbnnh.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111528p519bl1d9e9zbnnh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111528p519bl1d9e9zbnnh.jpg" referrerpolicy="no-referrer">
</div><br>
方才虽提到不太可行，但是为了提升 CPU 的计算能力仍然会采用多执行绪的作法。这部分的使用时机是在每个 AI 模组从主执行绪呼叫出来的时候，建立出工作执行绪（Worker thread）。然而，直接运作仍会对 AI 处理上造成较重的负担，对此需要进行优化的作业，让每个框架中 2～3ms 减少至 0.5ms 的目标。演讲中并没有提及具体作法如何，但能够看出整体上投入相当的工程。<br>
<br>
<div align="center">
<img id="aimg_1000320" aid="1000320" zoomfile="https://di.gameres.com/attachment/forum/202108/12/111530x5byl5ykcs3wn5zw.jpg" data-original="https://di.gameres.com/attachment/forum/202108/12/111530x5byl5ykcs3wn5zw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/12/111530x5byl5ykcs3wn5zw.jpg" referrerpolicy="no-referrer">
</div><br>
作为统整，为了管理广大开放世界的 AI，需要建构出新型态的 AI 框架，庞大的道路探索资讯交由伺服器端来综合处理，透过 LoD 减轻负荷等多元手段进行处理上的优化作业，才能实现出这等规模下的 AI 处理。能够认识到支持当红游戏的诸项技术，着实是令人深感兴趣的一堂课。<br>
<br>
<font size="2"><font color="#708090">来源：GNN</font></font><br>
<font size="2"><font color="#708090">地址：https://gnn.gamer.com.tw/detail.php?sn=218855【编译自</font></font><font size="2"><a href="https://www.4gamer.net/games/486/G048621/20210722010/" target="_blank">4gamer</a><font color="#708090">】</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            