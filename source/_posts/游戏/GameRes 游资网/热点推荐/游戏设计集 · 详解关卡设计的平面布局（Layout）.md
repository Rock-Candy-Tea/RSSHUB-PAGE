
---
title: '游戏设计集 · 详解关卡设计的平面布局（Layout）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/04/092331fgw51ty33c23p00a.jpg'
author: GameRes 游资网
comments: false
date: Fri, 04 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/04/092331fgw51ty33c23p00a.jpg'
---

<div>   
<div align="center">
<img aid="1032519" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092331fgw51ty33c23p00a.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092331fgw51ty33c23p00a.jpg" width="600" id="aimg_1032519" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092331fgw51ty33c23p00a.jpg" referrerpolicy="no-referrer">
</div><div align="left">作者：<font size="2"><font color="#808080">TokyoRed</font></font></div><div align="left"><font size="2"><font color="#808080">首发知乎:https://zhuanl</font></font>an.zhihu.com/p/474365383</div><br>
本文编译自《The Level Design Book》中《Layout》章节。主要聚焦于：如何绘制自上而下的包含流线、平衡、遭遇战和类型学的关卡平面图。介绍了受到建筑学启发的关卡平面布局设计方法论，并结合了经典游戏的关卡设计案例加以说明。<br>
<br>
<strong><font color="#de5650">为什么要设计平面布局?</font></strong><br>
<br>
布局（layout）在关卡设计中有两个相似的含义:<br>
<br>
<ul type="1" class="litype_1"><li>关卡的整体结构。比如：”这个布局太混乱了，我不知道该往哪里走。”</li><li>用于规划的总览图纸，有时被称为“topdown”的，因为它是从自上而下的角度绘制的。比如：“布局图画好了吗? 我们需要尽快白模测试。”<br>
</li></ul><br>
布局图可以是简单的，也可以是复杂的；可以是象征性的，也可以是具体化的；可以是抽象的，也可以是形象的。它可以是一张潦草的餐巾纸，也可以是一张详细的平面图，这要视情况而论。<br>
<br>
简而言之，一个“好的布局图”可以指代任何能有效传达核心设计理念的图像。<br>
<br>
<div align="center">
<img aid="1032520" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092332b5xay3y66xi6c0y0.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092332b5xay3y66xi6c0y0.jpg" width="600" id="aimg_1032520" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092332b5xay3y66xi6c0y0.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">哪一种布局草图的风格对你最有效? 你必须做出决定</font></font></div><br>
概括来说，布局图是:<br>
<br>
<ul><li>重要的合作</li><li>尤其适用于多人游戏关卡</li><li>游戏行业里，关卡设计师最基本的技能和工作任务之一<br>
</li></ul><br>
<strong><font color="#de5650">平面布局的概念</font></strong><br>
<br>
在设计平面布局时，利用以下设计理念:<br>
<br>
<strong>流线（Flow）是玩家在关卡中移动时的感觉。</strong><br>
<br>
<ul><li>玩家移动的速度是快还是慢，是平稳还是突然?</li><li>理想的流线取决于体验目标。意外的流线并不一定是坏事。<br>
</li></ul><br>
<strong>概念图（Parti）是布局的核心结构/主要思想。</strong><br>
<br>
<ul><li>将整个布局绑定在一起的整体概念是什么?</li><li>清晰的部分可以帮助你专注于设计中最重要的部分。<br>
</li></ul><br>
<strong>类型学（Typology）是关于识别常见的布局模式和功能。</strong><br>
<br>
<ul><li>简化你思考布局的方式。</li><li>共享设计词汇可以帮助你学习其他关卡和交流。<br>
</li></ul><br>
<div align="center">
<img aid="1032521" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092332viqiiqwvtqtmwi9f.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092332viqiiqwvtqtmwi9f.jpg" width="600" id="aimg_1032521" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092332viqiiqwvtqtmwi9f.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">如何设计平面布局</font></strong><br>
<br>
这里详细列出了一个完整的布局过程，作为一个传统最佳实践的例子。如果你在设计布局时遇到了困难，尝试每一步，看看哪一步适合你。<br>
<br>
但设计平面布局并没有最佳的方法。每个人(或项目)都可以用不同的方式进行布局。<br>
<br>
<ul type="1" class="litype_1"><li>前期制作: 定义设计目标</li><li>概念图: 头脑风暴出一些核心形状</li><li>气泡图: 可视化流程和空间关系</li><li>平面图: 更详细的具体房间形状草图</li><li>玩法标记: 添加标签和设计笔记<br>
</li></ul><br>
对于小型的个人项目，如果你感觉良好，你可以中途停止。对于大型的团队项目，你应该尝试在一块共享的白板上完成所有的步骤。<br>
<br>
<div align="center">
<img aid="1032522" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092332hhcr4r8h2jnu9wih.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092332hhcr4r8h2jnu9wih.jpg" width="600" id="aimg_1032522" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092332hhcr4r8h2jnu9wih.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">绘图迭代，从抽象网格(左)到平面图(右)，《Architectural Graphics》，Francis Ching</font></font></div><br>
<strong>1. 前期制作计划</strong><br>
<br>
设计没有任何目标的东西是很困难的。在前期制作阶段，我们尝试着在制作之前定义并计划我们想要做什么。所以在绘制布局之前，至少要确定一个玩家体验目标——在这个关卡中，玩家应该学习、感受或做什么?<br>
<br>
你可以写下特定的体验目标(如“教玩家如何在科幻下水道中进行5分钟的双重跳跃”)，也可以写得更抽象一些(如“与自然融为一体”)。但是，<strong>更具体=更容易设计。</strong><br>
<br>
<div align="center">
<img aid="1032523" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092333poh6senj6neshoeh.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092333poh6senj6neshoeh.jpg" width="600" id="aimg_1032523" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092333poh6senj6neshoeh.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Naughty Dog的《The Last Of Us》(2012)</font></font></div><br>
<strong>有了玩家体验目标，你就可以计划节奏，特定事件和活动的顺序，帮助实现体验目标。</strong><br>
<br>
例如，如果你的体验目标是“逃离可怕的怪物”，那么你就需要将这种体验分解成更小的特定节奏——如：<br>
<br>
<ul type="1" class="litype_1"><li>听到门后婴儿的哭声</li><li>揭示发出婴儿哭声的僵尸熊</li><li>跳出窗户逃离怪物<br>
</li></ul><br>
这个简单的计划已经很有用了，现在我们知道关卡至少需要一扇门和一扇窗。<br>
<br>
<strong>2. 概念图 Parti thumbnails</strong><br>
<br>
在建筑学中，概念图是整个建筑的基本形状/理念，包括：<br>
<br>
<ul type="1" class="litype_1"><li>一个简单的图表(缩略图)</li><li>用简短的短语标记它<br>
</li></ul><br>
这一环节需要回答：<strong>什么类型的基本形状适合你的体验目标或节奏。</strong><br>
<br>
这个部分可以是象征性的(“倒置的船”)，也可以是抽象化的(“消减的盒子”)，或者它可以专注于人们将如何使用建筑(“核心区域公共-私密分离”)，或者与周围环境的关系(“戳进树林的手指”)。<br>
<br>
或者你可以用一些形状来尝试，然后再进行梳理。关键是要在没有压力的环境下进行<strong>视觉化思考</strong>。如果你不喜欢一个概念，没问题，你可以随便再写一个。<br>
<br>
<div align="center">
<img aid="1032524" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092333vudghfyd88fwbydy.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092333vudghfyd88fwbydy.jpg" width="600" id="aimg_1032524" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092333vudghfyd88fwbydy.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">来自Matthew Frederic，《我在建筑学院学到的101件事》</font></font></div><br>
<strong>对概念图的建议：</strong><br>
<br>
<ul type="1" class="litype_1"><li>绘制至少5-10个概念图来生成多种可能。如果你画了100个，那么至少有一个是好的，因为设计100个糟糕的建筑是不可能的。你画得越多，你成功的概率就越大。</li><li>不要在每个上花太多时间。有时候你只需要30秒的时间就能画一些线条，这就足够表达核心思想了。</li><li>如果你很难给它命名，那可能是图太原始了。试着用不同的方式再画一次，或者试着把纸旋转180度，从另一个角度想象它。<br>
</li></ul><br>
<strong>3. 气泡图</strong><br>
<br>
将最有希望的概念图展开成气泡图：一组不同的椭圆，每个椭圆代表不同的房间。<br>
<br>
<ul type="1" class="litype_1"><li>为组成的每个部分画一个气泡</li><li>标记每个气泡</li><li>画箭头强调某些联系或方向<br>
</li></ul><br>
<strong>气泡图的目标是在你的关卡中建立比例和联系。</strong>比如什么部分需要变大?什么部分需要相互连接?<br>
<br>
不要担心细节。最重要的是<strong>理解空间的逻辑。</strong><br>
<br>
请看下面的气泡图示例。哪些空间与客厅相连，为什么?为什么浴室在那里?卧室在哪里?如果有人不能走楼梯，他们怎么才能住在这房子里?<br>
<br>
<div align="center">
<img aid="1032525" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092333t43vukrkqqgrlrcz.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092333t43vukrkqqgrlrcz.jpg" width="600" id="aimg_1032525" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092333t43vukrkqqgrlrcz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">芝加哥F10住宅的气泡图示例，摘自Masengarb等人的《建筑手册:理解建筑的学生指南》。</font></font></div><br>
<strong>关于气泡图的建议：</strong><br>
<br>
前几个气泡图将会不太理想并产生新的问题。有些泡泡可能太大或太小，或者它们可能连接了错误的泡泡。也许你忘了加一些泡泡? 也可能是泡泡太多了。<br>
<br>
<ul type="1" class="litype_1"><li>一个坏的气泡图是好的。这意味着你很早就发现了设计问题，你可以绘制另一个来尝试另一个计划。</li><li>绘制至少3个气泡图来想象多种排列和大小。</li><li>你可以脱离原始概念。概念图的目的是帮你开始画泡泡。如果它不再对你有帮助，那就不要使用它。<br>
</li></ul><br>
<strong>4. 平面图</strong><br>
<br>
在建筑学中，自上而下的布局图被称为平面图。<br>
<br>
<ul type="1" class="litype_1"><li>想象一个平面的切面，想象穿过建筑的水平切面</li><li>在这个平面切割下画出结构的形状——墙段、门、窗户和重要的家具</li><li>用虚线或点段线画上相关物体的平面图<br>
</li></ul><br>
在下面的图表中，注意Ching是如何使用各种线条类型、线条粗细、阴影和色调模式来区分平面图的各个部分的。Ching把墙壁变厚变暗，但用较细的线条标出楼梯或屋子的区域，用较细的线条标出旋转门的弧线。<br>
<br>
<div align="center">
<img aid="1032526" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092333r7itlzynzgxt66kk.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092333r7itlzynzgxt66kk.jpg" width="600" id="aimg_1032526" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092333r7itlzynzgxt66kk.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">来自Francis D. K. Ching的《建筑制图》(第6版)的各种平面图绘制技术</font></font></div><br>
<strong>绘制平面图的建议：</strong><br>
<br>
<ul><li><strong>从大的开始。</strong>使用整个页面，从大的主要形状开始，逐渐细化到较小的特征，如门和窗户。通过整个图纸进行工作，不要试图从一开始就画出100%的细节。</li><li><strong>90/90。</strong>长方形、方框和网格比单角或弯曲的墙更容易建造。一般来说，如果90%以上的角是90度，并与网格对齐，你会感谢自己的。</li><li><strong>使用2倍线厚度。</strong>使用不同的线权重来标记不同类型的墙壁和区域。</li><li><strong>笔比鼠标更实用。</strong>如果要快速绘制布局图，请使用铅笔、钢笔或画板。如果使用鼠标进行绘制，则应尽量保持布局绘制的简单，并避免微调线条或调整精确的形状——在这里，精度并不重要。</li><li><strong>我们不是建筑师。</strong>详细的建筑图纸很漂亮，但在关卡设计的这个阶段，只需要绘制出能够表达空间和玩家体验界限的最低限度的图纸。<br>
</li></ul><br>
<strong>5. 游戏玩法标记</strong><br>
<br>
在你绘制出更具体的房间形状和墙壁后，在平面图上做标记——标记出预期的机制、节奏和遭遇战。<strong>好的布局应该传达出玩家的体验。</strong>当标记楼层平面图时，不要忘记:<br>
<br>
<ul><li><strong>流线。</strong>用直线或一组箭头绘制或标记关键路径。如果关键路径是非线性或复杂的，那么至少要标记出玩家的起始位置和退出点。在多人游戏地图中，轻微着色或突出团队刷出区域和主要循环。</li><li><strong>区域。</strong>标记主要区域、地标和预期的设置。它的主要部分或区块是什么?对于竞争性多人游戏的地图，你可以开始考虑可能的“标注”，即玩家用来快速指代地图不同部分的简短标签。</li><li><strong>对象。</strong>标记重要的目标、npc、敌人、道具、强化物、拾取道、陷阱等，这对于理解玩家体验至关重要。但简化不重要或不在关键路径上的次要对象，以避免过多的内容扰乱绘图。一个忙碌而混乱的布局图是无效的。<br>
</li></ul><br>
<div align="center">
<img aid="1032527" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092334e2n253ycz259g9nw.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092334e2n253ycz259g9nw.jpg" width="600" id="aimg_1032527" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092334e2n253ycz259g9nw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Eric Kirchmer为《半条命2》中的“Nova Prospekt”绘制的等角布局图中的玩法标记</font></font></div><br>
<div align="center">
<img aid="1032528" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092334jpdsqav5r834so5x.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092334jpdsqav5r834so5x.jpg" width="600" id="aimg_1032528" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092334jpdsqav5r834so5x.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《传送门2》具有谜题的等距布局图中玩家的流线，来自Game Informer, 2010年3月</font></font></div><br>
<strong><font color="#de5650">关卡布局图案例</font></strong><br>
<br>
<strong>《半条命2》，“Nova Prospekt”，Eric Kirchmer和David Sawyer设计</strong><br>
<br>
在单人FPS游戏《半条命2》(2004年)中，玩家必须在一个名为Nova Prospekt的废弃监狱中战斗。这是一个很长的章节，充满了许多与快速移动的小队敌人的近距离战斗，旨在充分利用玩家的“虫饵”武器，即能够命令飞行的“蚁狮”怪物去攻击敌对的士兵。<br>
<br>
<ul><li><strong>调研：</strong>灵感来源于加州旧金山的恶魔岛州立监狱</li><li><strong>类型学：</strong>地面上的竞技场两侧有狭窄的通道和监狱牢房，往往有大门</li><li><strong>遭遇战：</strong>设计不同的街区和房间，每个部分提供一个中心构思，在整个章节中为“蚁狮”交战空间增加了一个新的转折<br>
</li></ul><br>
<div align="center">
<img aid="1032529" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092334opm67hkhezzk8nxh.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092334opm67hkhezzk8nxh.jpg" width="600" id="aimg_1032529" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092334opm67hkhezzk8nxh.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Alcatraz(左)，Nova Prospekt气泡图(右)，摘自艺术书籍“半条命2:提高标准”</font></font></div><br>
Nova Prospekt (上图右)是一个相对简单的布局图，标出了区域以及玩家如何通过和前进，同时它省略了每个建筑内部的单独房间和走廊。总之它是一组关卡的布局图，而不仅仅是一个关卡。而且它基本上是一个气泡图，聚焦于每个区域的进程及其连接性。<br>
<br>
对于单个的建筑组块和遭遇战，Valve概念美术师Eric Kirchmer<strong>将关卡设计和玩法标记直接融入到概念美术草图中</strong>，这可能是团队协作设计会议的结果。这些遭遇战带有理想化的关键路径“解决方案”，即将每场战斗视为待解决的谜题。这些草图为关卡设计师David Sawyer提供了有价值的设计文件。<br>
<br>
在所有等距布局图中，可以看到大量的玩法标记：玩家开始的位置、关键路径箭头以及大量文本标签的使用，以帮助我们想象玩家体验。<br>
<br>
<div align="center">
<img aid="1032530" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092335b5ud2uyu1ju25up5.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092335b5ud2uyu1ju25up5.jpg" width="600" id="aimg_1032530" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092335b5ud2uyu1ju25up5.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Nova Prospekt 绘制的各种遭遇战的等距布局图，摘自艺术书籍“半条命2:提高标准”</font></font></div><br>
<strong>《雷神之锤》，“未命名”关卡，Andrew Yoder设计</strong><br>
<br>
在单人游戏《雷神之锤》关卡中，设计师Andrew Yoder重复了一种设定，即在房间中放置悬挂的笼子。在这里，Yoder反复地在平面图和模型图之间流畅地切换，有时会脱离整个房间，并使用布局草图重新审视设计。以下是他的一些笔记:<br>
<br>
<div align="center">
<img aid="1032531" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092335bt5fubekj8efobme.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092335bt5fubekj8efobme.jpg" width="600" id="aimg_1032531" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092335bt5fubekj8efobme.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">带有透视图的关卡布局草图，Andrew Yoder</font></font></div><br>
我们注意到有编号，大量注释，草图中不同部分的标记，偶尔使用透视图来阐明整体结构。当关卡布局涉及高度变化时，透视图尤其有用，因为从上到下的视角很难绘制高度变化。各种草图和丰富的标记帮助Yoder传达他的设计意图，布局过程可以帮助Yoder描述和阐明设计问题。<br>
<br>
<div align="center">
<img aid="1032532" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092335y4k4z7m4kv41op9b.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092335y4k4z7m4kv41op9b.jpg" width="600" id="aimg_1032532" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092335y4k4z7m4kv41op9b.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《雷神之锤》中悬浮笼区域的模型截图，Andrew Yoder</font></font></div><br>
<strong>《看门狗2》，“Automata-电视台”，luliu-Cosmin Oniscu设计</strong><br>
<br>
在开放世界黑客游戏《看门狗2》中，设计师luliu-Cosmin Oniscu创造了一个包含多个目标、入口和关键路径的任务。在他的博文“Watch Dogs 2 - Automata - a level design retrospective”中，他引用了带有大量玩法标记和最小化建筑的布局图:<br>
<br>
<div align="center">
<img aid="1032533" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092336osttaz1jq3fy3zs3.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092336osttaz1jq3fy3zs3.jpg" width="600" id="aimg_1032533" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092336osttaz1jq3fy3zs3.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《看门狗2》的“Automata”中WKZ站的布局，由设计师luliu-Cosmin Oniscu绘制</font></font></div><br>
<strong>以下是设计师的建议和意图:</strong><br>
<br>
在这个特定的场景中，技巧在于玩家可以通过激光并触发警报，但他也可以:<br>
<br>
<ul type="1" class="litype_1"><li>当守卫巡逻时关闭激光，然后进入红色区域并无声地打倒Al。</li><li>使用安装在墙上的摄像机，从一个摄像机的角度移动到另一个摄像机的角度。在游戏的这一点上，这是一种已经建立起来的侦察内部地点的方法。</li><li>使用无人机探索走廊并使守卫瘫痪。<br>
</li></ul><br>
后面的走廊也有一些战略位置上的接线盒，玩家可以切断这些接线盒，从而使两个守卫同时失去能力。<br>
<br>
请注意，关卡设计师的绘图(如上图所示)比实际的游戏内部执行(如下图所示)简单得多。建筑细节，家具，甚至一些游戏玩法元素，如中立的npc和壁挂式摄像机，都没有出现在布局图中。这些都与计划通过打败守卫npc而绕过守备区的核心体验目标无关。<br>
<br>
这里教会我们：<strong>不要让没必要的设计功能扰乱你的布局图。</strong><br>
<br>
<div align="center">
<img aid="1032534" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092336s46hccc40ccb48ja.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092336s46hccc40ccb48ja.jpg" width="600" id="aimg_1032534" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092336s46hccc40ccb48ja.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《看门狗2》“Automata”中WKZ站大厅的玩家视角，Luliu-Cosmin Oniscu</font></font></div><br>
<strong>《军团要塞·经典》(Valve)，“Warpath”，Robin Walker等设计</strong><br>
<br>
在基于职业的多人射击游戏《军团要塞·经典》(1999)中，“Warpath”是Robin Walker和Valve的团队合作设计的控制点地图。《军团要塞·经典》的CP游戏模式与《军团要塞2》或《守望先锋》中的现代CP模式类似，即两支队伍将在中央通道上争夺所有控制点。<br>
<br>
<ul><li><strong>流程：</strong>一个中央通道和侧路，5个控制点和动态的刷新点</li><li><strong>平衡：</strong>对称地图，所有9个职业必须是可用的，攻击/防御在每个CP都可实现</li><li><strong>类型学：</strong>串珠项链，一条长长的走廊，为每个CP点缀着竞技场。<br>
</li></ul><br>
<div align="center">
<img aid="1032535" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092336xuauuf4unl47clj8.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092336xuauuf4unl47clj8.jpg" width="600" id="aimg_1032535" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092336xuauuf4unl47clj8.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">将最初的平面图与最终的关卡布局进行比较，《军团要塞经典》的“Warpath”</font></font></div><br>
在上图中，注意编号的控制点和标记。每个控制点区域就像一个迷你竞技场，带有特定的地标：狙击点、隧道、石拱、兵营等。从最开始就进行命名和主题化地图区域，标签还会突出地图中体验目标的最重要部分。<br>
<br>
同样要注意的是，手绘图只显示了地图的一半，最后的关卡在中央桥上进行了镜像对称。因为他们已经决定地图布局应该是对称的，所以没有必要手绘整个地图。因此，设计的约束条件会影响绘制布局平面的方式。<br>
<br>
<div align="center">
<img aid="1032536" zoomfile="https://di.gameres.com/attachment/forum/202203/04/092336xq44avthb63hf3zl.jpg" data-original="https://di.gameres.com/attachment/forum/202203/04/092336xq44avthb63hf3zl.jpg" width="600" id="aimg_1032536" inpost="1" src="https://di.gameres.com/attachment/forum/202203/04/092336xq44avthb63hf3zl.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">从蓝队的狙击点架向南部中央桥竞技场;《军团要塞经典》中的“Warpath”</font></font></div><br>
<strong><font color="#de5650">批判思考</font></strong><br>
<br>
绘制布局平面可以帮助你更好地计划项目并抓住核心问题。当与他人合作时，它也帮助每个人协调他们的工作，并且相互理解。<br>
<br>
但是<strong>布局图并不是一个关卡，没有人能够测试草图。</strong>这只是个计划，而计划总是会变的。<br>
<br>
也许一个完美的布局图看似能够创造出完美的关卡，而不浪费任何工作，但这却从未发生过。相反地，你不应该仅仅停留在计划阶段，首先“开始绘制地图”——然后构建地图并测试它，接着你就会发现它是否有效。搭建实际关卡的过程将有助于验证设计，而不能仅是花太多时间在纸上设计虚构的关卡。<br>
<br>
<strong><font color="#de5650">回顾小结</font></strong><br>
<br>
传统的设计关卡布局过程开始于设计目标，并以布局平面图结束。这张布局图只是你开始游戏设计的最初计划，你应该期待最终关卡会出现明显的差异。本文中的重要过程总结如下：<br>
<br>
<ul><li><strong>制定一个基本计划</strong>，定义理想的体验目标和节奏。</li><li><strong>绘制概念图</strong>，包括简单的图示和核心形状。</li><li><strong>用气泡图布置空间</strong>，强调整体的比例和关系。</li><li><strong>画出平面图</strong>，自上而下的图纸中具有墙壁和地板。<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>从大的简单形状开始，忽略细节，使用多线型和阴影区域。</li><li>对于多层的房间，绘制等距视图，注意楼层的平面。</li><li>对于重要或复杂的房间，绘制透视图并加以标记。<br>
</li></ul><br>
<ul><li><strong>加上玩家流线和玩法注释</strong>，帮助他人想象这种游戏体验，特别是当你进行团队合作时，标注清晰的名称和区域标签很重要。<br>
</li></ul><br>
PS：我会定期学习，梳理，输出 【游戏/游戏设计/游戏建筑】 相关的思考或笔记，欢迎感兴趣的朋友，关注我的知乎。如需转载，请私信。<br>
<br>
<font color="#808080">参考来源：</font><br>
<font color="#808080">https://book.leveldesignbook.com/process/layout</font><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：:https://zhuanlan.zhihu.com/p/474365383</font></font><br>
<br>
  
</div>
            