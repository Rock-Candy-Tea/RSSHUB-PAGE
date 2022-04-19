
---
title: '玩家的第三只眼睛——游戏中的_相机_与UI'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202204/18/095710ax0zzqqxmy5qbf50.gif'
author: GameRes 游资网
comments: false
date: Mon, 18 Apr 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202204/18/095710ax0zzqqxmy5qbf50.gif'
---

<div>   
<div align="center">
<img aid="1036704" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095710ax0zzqqxmy5qbf50.gif" data-original="https://di.gameres.com/attachment/forum/202204/18/095710ax0zzqqxmy5qbf50.gif" width="600" id="aimg_1036704" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095710ax0zzqqxmy5qbf50.gif" referrerpolicy="no-referrer">
</div><br>
<i><font color="#808080">「“相机”的起源与定义」</font></i><br>
<br>
在游戏设计与开发中，相机有其作为技术实体的定义，广泛而言人们也将其用于阐述“游戏叙事视角”。自 1990 年代以来，“相机”一词已成为游戏中常见表达方式，行业内外都使用它来指定游戏的视角，即游戏世界中在屏幕上呈现给玩家的特定框架。<br>
<br>
<strong><font color="#de5650">一、游戏中“相机”概念的发展演进</font></strong><br>
<br>
<strong>单角度视窗</strong><br>
<br>
1984年 Branigan 所撰写的文章中探讨了“什么是相机”这一问题。根据 Branigan 的认知观点，该术语经常被观众和评论家用作“标签”，以聚合构成电影空间的各种“空间效果”。不可否认，“相机”一词最初是源于影视行业的概念。而当人们将“相机”概念从一种媒体迁移到另一种媒体、从电影迁移到电子游戏时，“相机”一词的语义差异就更加明显了。<br>
<br>
电子游戏背景下“相机”的兴起通常与 1990 年代实时 3D 图形的广泛使用有关。早期的例子包括1992年的《Alone in the Dark》、《古墓丽影：劳拉克罗夫特》以及任天堂在1996年制作的《超级马里奥 64》等。在那段时间中，3D热潮席卷了电脑端平台，游戏类别涉及探索和益智游戏、射击游戏和太空探索游戏等等。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036705" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095710t5z0vppuoy0vyn0h.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095710t5z0vppuoy0vyn0h.jpg" width="600" id="aimg_1036705" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095710t5z0vppuoy0vyn0h.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Alone in the Dark，1992</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1036706" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095713oc5r742acwcz2h46.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095713oc5r742acwcz2h46.jpg" width="600" id="aimg_1036706" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095713oc5r742acwcz2h46.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">超级马里奥 64，1996</font></font></div><br>
然而，虽然1980年代后半期的电脑游戏中大量使用了实时3D图像和多边形填充，产业界和新闻界并没有使用“相机”这一名词进行设计说明，而是将这一概念复杂化。例如，作为实时3D游戏的早期案例，电脑游戏 《Driller》的游戏手册将屏幕内呈现玩家的部分描述为“视窗”，而宣传语则吹嘘“革命性的 3D 缩放和视角”。<br>
<br>
术语“相机”的第一个实例出现在《Starglider》的说明书中，含义是游戏中的远程记录设备暂时占据了飞行员（玩家）的游戏画面。此时《Starglider》中的相机已经脱离了技术层面，并非与3D建模相关的计算机图像渲染技术，而是更接近游戏世界中实际存在的相机。<br>
<br>
<div align="center">
<img aid="1036707" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095715fa7tezei5tkk8677.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095715fa7tezei5tkk8677.jpg" width="350" id="aimg_1036707" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095715fa7tezei5tkk8677.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《Starglider》的相机遥控导弹</font></font></div><br>
<strong>多镜头切换</strong><br>
<br>
“相机”概念最初的变化也同样发生这一游戏系列中。可以说，经由这一系列的游戏，媒体逐渐开始使用“相机”来表述游戏场景画面中的多个视角切换。在《Starglider II》中，虽然游戏中并未出现这一词语，但是媒体使用“相机”来描述除了位于飞船内部的标准“驾驶舱视图”之外，玩家可以使用的“外部视图”。而在第四代游戏的报道中，记者表示游戏“提供了多种相机角度，让您可以从周围任何一点观察空间”。<br>
<br>
<div align="center">
<img aid="1036708" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095716doercecloxgxem5c.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095716doercecloxgxem5c.jpg" width="350" id="aimg_1036708" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095716doercecloxgxem5c.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《Starglider II》中被媒体称为“相机”的“外部视图”</font></font></div><br>
<strong>回放模式</strong><br>
<br>
与此同时，自 1980 年代末以来，“回放”选项极大地促进了视频游戏文本中“相机”一词的传播。<br>
<br>
《Battelhawks》的各种拨盘开关包括一个“相机指示灯”，一旦玩家使用“回放相机”，它就会打开。根据游戏手册，“回放相机是学习飞行战术的绝佳工具，也是一种像电影一样享受游戏的方式”。<br>
<br>
<div align="center">
<img aid="1036709" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095717qkazy89jihd7874q.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095717qkazy89jihd7874q.jpg" width="350" id="aimg_1036709" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095717qkazy89jihd7874q.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《Battlehawks 1942》的回访</font></font></div><br>
更重要的是，伴随着计算机可视化进程的推进，回放选项以及丰富的各种“视图”逐渐在市场和行业中占据一席之地，并成为运动模拟和驾驶模拟的基础模型。<br>
<br>
<strong>运动模拟</strong><br>
<br>
在运动和驾驶模拟类型的游戏中，“相机”被广泛运用。Distinctive Software 的 4D 运动系列游戏提供了多种运动模拟画面。正如一位评论家所说，由摄像头、旋转和变焦组成的系统可以让玩家完全自定义自己的相机视角。<br>
<br>
<div align="center">
<img aid="1036710" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095717s7rcebgc8vjz7hib.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095717s7rcebgc8vjz7hib.jpg" width="350" id="aimg_1036710" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095717s7rcebgc8vjz7hib.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《4D 网球》主菜单中的“主相机位置”以及“相机控制”面板</font></font></div><br>
<strong><font color="#de5650">二、“相机”画面与UI结合的表现力</font></strong><br>
<br>
直至现在的游戏业界，相机的概念已经逐渐固定化。在游戏中，画面与UI相结合，带来了较强的张力和表现力。一方面，相机画面弥补了传统游戏叙事上代入感和表现力的不足；另一方面，UI强化了单纯画面中的指向性引导，包括显性的视觉引导和隐形的情感渲染。通常UI设计师会结合相机画面，通过情绪激化、目标引导、等手段增强玩家的过程体验，营造流畅感、操控感、参与感。<br>
<br>
例如，以潜行战斗为核心的《MGSV》对于玩家被敌人发现时的画面进行了精心设计。在“子弹时间”这一过程中，首先设计师将画面模糊化并减低亮度，使玩家将注意力锁定在目标敌人身上；随后将镜头加速对焦，强化玩家紧张的情绪；同时使用简洁的红色准星和白色标记强化了目标，富有沉浸感和代入感。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036711" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095717i013fndzffy09efo.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095717i013fndzffy09efo.jpg" width="556" id="aimg_1036711" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095717i013fndzffy09efo.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《MGSV》子弹时间</font></font></div><br>
《狂野飙车》游戏内，比赛过程中相机视角主要位于靠近地面的水平空间内，根据玩家对于车辆的操控进行微小移动反馈。开启氮气爆发模式后，画面呈具有速度感的径向模糊，同时顶部速度显示条的颜色变化为霓虹光效果，增加玩家的正向情感反馈。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036712" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095717m65bh5megxrrrzgn.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095717m65bh5megxrrrzgn.jpg" width="600" id="aimg_1036712" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095717m65bh5megxrrrzgn.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《狂野飙车》氮气爆发</font></font></div><br>
在众多射击类游戏中，狙击枪的开镜也是相机画面张力的又一种案例。除了瞄准镜以外的界面以纯黑色显示，同样使得玩家的注意力集中在画面中心，镜内准星再次收束玩家注意力，达到仿真射击的效果。同时极小的可视区域提高了玩家的紧张感，加强游戏体验。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036713" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095718v9n2n7aaqq8cn882.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095718v9n2n7aaqq8cn882.jpg" width="600" id="aimg_1036713" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095718v9n2n7aaqq8cn882.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《csgo》狙击枪开镜</font></font></div><br>
<strong><font color="#de5650">三、当相机掌握在玩家手中</font></strong><br>
<br>
“切记你的游戏不仅仅只是一堆有趣的选择，”席德·梅尔曾经这么强调。相机的定位和画面细节的把控往往是掌握在游戏设计师手中的工具。一方面，将玩家们的精力和时间花费在调整相机上着实是一种负向体验；同时，正如前文所说，对于相机的合理把控有助于设计师们强化玩家的过程体验。<br>
<br>
这看上去有百利而无一害的事——不过玩家对于自由度和视角转移的需求自从计算机3D图像兴起时就存在。随着产业的发展，游戏制作方也逐渐开始以一些聪明的方式将相机的使用权提供给玩家。当相机掌握在玩家手中，有时会产生一些奇妙的反应。<br>
<br>
最简单也是最常用的方式就是让玩家在几个既有相机的视角中进行切换，正如上文中所提及的《Starglider》系列游戏以及运动和驾驶模拟游戏一般。这既满足了玩家自由掌握相机的需求，又降低了风险，保证玩家不会因为调整相机角度而手忙脚乱。<br>
<br>
同一游戏局内自由切换视角时，UI也会根据画面产生相应的变化。拿最具代表性的驾驶模拟类型游戏举例，《GT Sports》在局内提供了四种相机视角供玩家选择，其驾驶仪表盘的UI也产生了适应性的改变。<br>
<br>
<div align="center">
<img aid="1036714" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095718pcv3cf3chc33dydd.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095718pcv3cf3chc33dydd.jpg" width="600" id="aimg_1036714" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095718pcv3cf3chc33dydd.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1036715" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095718gmm7pap6ltvqvalw.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095718gmm7pap6ltvqvalw.jpg" width="600" id="aimg_1036715" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095718gmm7pap6ltvqvalw.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1036716" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095719jfp6kppik2f8cwh6.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095719jfp6kppik2f8cwh6.jpg" width="600" id="aimg_1036716" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095719jfp6kppik2f8cwh6.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1036717" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095719agjclzzlgijvwlz3.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095719agjclzzlgijvwlz3.jpg" width="600" id="aimg_1036717" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095719agjclzzlgijvwlz3.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《GT Sports》四种视角</font></font></div><br>
总体而言，这类UI的变化特点主要包括：（1）通过拟物化设计、情景化设计营造代入感；（2）使用更直观的控件，合理弱化并简化UI，减少视觉干扰；（3）根据场景提供特化的视觉显示。<br>
<br>
此外，出于玩家分享和社交性的考虑，游戏中也出现了“真实”的相机——游戏内照相系统。这是一种自由度更高的相机模式，可以说是“相机中的相机”。风景、npc、角色……游戏中的一切都可以被玩家记录下来，以此为目的，相机位置和细节的一遍遍调整都能让玩家乐此不疲。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036718" zoomfile="https://di.gameres.com/attachment/forum/202204/18/095719rlbqyfgtbbgyq1zm.jpg" data-original="https://di.gameres.com/attachment/forum/202204/18/095719rlbqyfgtbbgyq1zm.jpg" width="468" id="aimg_1036718" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/095719rlbqyfgtbbgyq1zm.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《光遇》中玩家的自拍</font></font></div><br>
<strong><font color="#de5650">结  语</font></strong><br>
<br>
“相机”这一概念从电影行业中汲取养分，由叙事到表现，由技术到虚拟，它在游戏技术和产业发展过程中一步步进行演变。游戏中的“相机”与UI相结合，成为了玩家的第三只眼睛，带其领略那个缤纷的电子虚拟世界。<br>
<br>
<font size="2"><font color="#808080"><strong><i>参考资料</i></strong></font></font><br>
<font size="2"><font color="#808080"><i>https://www.gcores.com/articles/111376</i></font></font><br>
<font size="2"><font color="#808080"><i>https://www.gameres.com/465489.html</i></font></font><br>
<font size="2"><font color="#808080"><i>http://gamestudies.org/2102/articles/krichane</i></font></font><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<br>
  
</div>
            