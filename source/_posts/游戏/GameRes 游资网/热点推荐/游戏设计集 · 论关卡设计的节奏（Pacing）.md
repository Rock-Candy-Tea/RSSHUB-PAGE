
---
title: '游戏设计集 · 论关卡设计的节奏（Pacing）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202201/26/092924dquc1g5e1q0z0rcp.jpg'
author: GameRes 游资网
comments: false
date: Wed, 26 Jan 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202201/26/092924dquc1g5e1q0z0rcp.jpg'
---

<div>   
<div align="center">
<img aid="1029341" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092924dquc1g5e1q0z0rcp.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092924dquc1g5e1q0z0rcp.jpg" width="600" id="aimg_1029341" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092924dquc1g5e1q0z0rcp.jpg" referrerpolicy="no-referrer">
</div><br>
<font color="#808080">作者：TokyoRed，知乎主页：</font><br>
<font color="#808080">https://zhuanlan.zhihu.com/p/460785796</font><br>
<br>
本文翻译自开放式在线阅读书籍《Level Design Book》中pacing章节内容<br>
<br>
https://book.leveldesignbook.com/process/preproduction/pacing<br>
<br>
——节奏（Pacing ），指在一个关卡中，为玩家设计各种可以体验的活动和事件。<br>
<br>
本文编译自《The Level Design Book》中 Pre-production 部分的《Pacing》章节。<br>
<br>
文章在总结游戏关卡设计理论的同时，结合了一些厂家的实践案例。主要聚焦于：什么是游戏关卡设计的节奏，有哪些游戏节奏的图表，以及关卡节奏设计中常见的一些问题。<br>
<br>
<strong><font color="#de5650">目录</font></strong><br>
<br>
<font color="#808080">什么是节奏</font><br>
<font color="#808080">节拍和变奏</font><br>
<font color="#808080">固定套路</font><br>
<font color="#808080">设计“节拍堆”的方法</font><br>
<font color="#808080">教学、测试和扭转</font><br>
<font color="#808080">关键路径</font><br>
<font color="#808080">绘图和文档</font><br>
<font color="#808080">节奏的建议</font><br>
<font color="#808080">多人游戏的节奏</font><br>
<font color="#808080">开放世界/非线性的节奏</font><br>
<font color="#808080">反节奏</font><br>
<font color="#808080">要点回顾</font><br>
<br>
<strong><font color="#de5650">什么是节奏</font></strong><br>
<br>
节奏是指关卡中活动/事件的顺序和韵律。<br>
<br>
单人游戏关卡往往需要强力的节奏。如果玩家对关卡中发生的事情，或他们能做什么感到困惑，那么这可能就是关卡节奏的问题。<br>
<br>
有效的节奏规划应该包括：<br>
<br>
<strong>1.范围: </strong>玩家在每个关卡中可以做什么?<br>
<br>
<strong>2.层级: </strong>关卡的哪些部分是最重要的?<br>
<br>
<strong>3.因果关系: </strong>为什么玩家要在某个活动之前进行另外的活动?<br>
<br>
<strong>4.信息:</strong> 我们应该在何时告诉玩家什么内容?<br>
<br>
<strong>5.强度: </strong>玩家应该在什么时候给予更多关注，玩家什么时候可以休息/恢复?<br>
<br>
<div align="center">
<img aid="1029342" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092924yvl375qbsu930y90.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092924yvl375qbsu930y90.jpg" width="554" id="aimg_1029342" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092924yvl375qbsu930y90.jpg" referrerpolicy="no-referrer">
</div><br>
《Journey》(2012)的节奏图表，来自2013年GDC上的“Designing Journey”演讲<br>
<br>
<strong><font color="#de5650">节拍和变奏</font></strong><br>
<br>
关卡中会发生什么? 有哪些不同的时刻、地点来定义关卡中的体验?<br>
<br>
节拍是关卡中一个独立的小块。比如单一的区域，事件，活动，或元素。<br>
<br>
我们可以把关卡的节拍比作歌曲中的音乐节拍。当这些节拍一起演奏时，就形成了旋律和节奏。它们可以分开理解，也可以作为整体的一部分来理解。为了使节奏更有趣，作曲家用不同的方式来安排节奏来创造变奏，比如：<br>
<br>
<ul><li>脉搏: 建立一个有规律的重复的跳动模式，就像心跳一样（如: 在每个关卡的末尾设置一个独特的出口）</li><li>重音: 强调或加强某些节拍（如: 偶尔设计很难找到的出口）</li><li>休止符: 结合较弱的节拍或沉默，让观众再次对重音敏感（如：有时候设计的出口很容易找到）</li><li>母题：一个短的节拍序列（如：有时候，玩家在到达出口之前会与boss战斗）</li><li>变奏: 以不同的旋律、节奏等重复一系列的节拍（如：有些楼层有多个出口）</li><li>切分: 现代流行音乐的基础（如：在boss战斗的中途，另一个boss出现了；有时候假的出口里藏着一个怪物；最终boss摧毁出口，现在已无路可逃；玩家获得创造出口的能力）<br>
</li></ul><br>
<div align="center">
<img aid="1029343" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092924anlfn42ytmzlttbb.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092924anlfn42ytmzlttbb.jpg" width="600" id="aimg_1029343" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092924anlfn42ytmzlttbb.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">在音乐理论中强调不同的节拍 (韵律，节奏，切分)，来自Jack Perricone的“歌曲写作的旋律”</font></font></div><br>
<strong><font color="#de5650">固定套路 （Set pieces）</font></strong><br>
<br>
固定套路是一种具有独特概念（或难忘的活动）的精心制作的节拍。<br>
<br>
这种做法来自电影制作，预算高的电影项目通常会委托制作昂贵的大型场景，需要独特的设计和复杂的规划，这种紧张的场面会让观众记忆深刻。<br>
<br>
例如，好莱坞大片的动作电影本质上是一系列的固定场景——大型的精心设计的打斗、追逐序列或挑战死亡的特技。电影的其余部分主要是将这些场景以一种半连贯的方式连接在一起，并在这些紧张的场景之间为观众提供一些休息。大型动作游戏也是如此。<br>
<br>
但是场景并不一定是爆炸性的动作场面。喜剧以滑稽尴尬的场景为特征，爱情剧可能强调第一次约会或婚礼，正剧可能以催人泪下的坦白或背叛为特征，谋杀悬疑剧以侦探叙述真实事件为结尾。<br>
<br>
固定套路包括电影/游戏中的任何场景。重要的，难忘的，亦或是昂贵的。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1029344" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092925p9gcr11z8aaza9rz.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092925p9gcr11z8aaza9rz.jpg" width="600" id="aimg_1029344" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092925p9gcr11z8aaza9rz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">来自1999年动作片《黑客帝国》中令人难忘的大厅枪战场景</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1029345" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092925nbtthcb59b9pzwwz.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092925nbtthcb59b9pzwwz.jpg" width="600" id="aimg_1029345" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092925nbtthcb59b9pzwwz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">选自电影《低俗小说》(1994)中令人难忘的舞蹈场景。</font></font></div><br>
在游戏中，这种场面往往是：<br>
<br>
<strong>昂贵的</strong>，需要许多独特的美术和动画资源，以及不断的迭代。不容易缩减范围，也不容易改变用途，所以这种生产行为本身就有风险。<br>
<br>
<strong>不可跳过的</strong>，与游戏的核心支柱/主要体验目标紧密相连。否则为什么要花这么多时间和金钱，去创造一些可能让玩家错过并抱怨游戏的内容呢?<br>
<br>
<strong>大量的脚本化</strong>，以及线性的/框架化的，以确保可靠的体验。假如固定套路以三种不同的方式呈现，那么就相当于三倍的场面，制作成本也是原来的三倍。<br>
<br>
制作该类场面的关卡设计往往包括：<br>
<br>
<strong>Boss战、大型谜题或场景编排</strong>——这些都需要大量的关卡脚本。<br>
<br>
<strong>竞技场类型</strong>，一个大的房间来困住玩家，直到他们完成到过场动画。<br>
<br>
<strong>英雄道具</strong>（hero props系电影术语），通过独特的环境美术资源让关卡感觉特别。<br>
<br>
在任何一个给定的项目中，尝试设计和计划至少一个固定套路，这些序列可以锚定项目的其余部分。理想情况下，这个部分应该是使你非常兴奋的内容，是你迫不及待想让玩家去经历的体验。<br>
<br>
如果你害怕建立固定套路的工作，或者更糟的是，你没有希望让任何玩家都能做到把它玩一遍，那么你可能就不应该这么做。如果你正在学习一个新的工具集，那么不要计划一个巨大的宏伟布景。如果你是游戏开发新手，那么你便需要衡量固定套路的范围，特别是在你有更多的经验之前，不要设计得太困难。记住: 最好的固定套路是你能够最终完成和发布的。<br>
<br>
<strong><font color="#de5650">设计“节拍堆”的方法</font></strong><br>
<br>
对抗类游戏和解密游戏可以通过分开设计多个节拍，然后再将它们组合在一起，从而获得成功。<br>
<br>
工作流程是这样的:<br>
<br>
1. 概念化、布局并建立出一个孤立的战斗/谜题草模。<br>
<br>
2. 在草模内进行测试和迭代。直到它被证明要么有希望，要么是个坏主意。<br>
<br>
3. 重复步骤1-2，直到你创造出许多战斗/谜题的原型。<br>
<br>
4. 根据共同的(或相反的)元素安排最好的节拍。<br>
<br>
第一人称解密游戏《传送门》(2007年)的原型是一系列互不相连的谜题室，在设计师选择了他们最喜欢的谜题后，才凝结成一个连贯的关卡战役。每个房间介绍海报上显示的谜题元素图标，都是在“节拍堆”这个设计过程中留下的。<br>
<br>
<div align="center">
<img aid="1029346" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092925gzmpomack22701po.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092925gzmpomack22701po.jpg" width="600" id="aimg_1029346" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092925gzmpomack22701po.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《传送门1》中的房间标志的截图，图标显示谜题中出现的不同元素</font></font></div><br>
<strong><font color="#de5650">教学、测试和扭转</font></strong><br>
<br>
“教学-测试-扭转”是关卡设计中常见的“3拍模式”。<br>
<br>
<strong>教学: </strong>教导玩家有关游戏中行为的知识（如: 在《传送门1》密室10中，玩家学习了一个简单的“投掷”动作）<br>
<br>
<strong>测试: </strong>通过提示测试玩家是否能够重复和识别活动（如: 在《传送门1》密室10中，玩家学会动作后将进行更深入的游戏）<br>
<br>
<strong>扭转: </strong>扭转活动的框架; 如果提示较少，玩家是否能够回忆起它?（如: 在《传送门1》密室12中，玩家从更高的位置投掷；在密室15，玩家完成了空中的“双掷”；在密室18中，玩家以“无限投掷”挑战结束）<br>
<br>
注意在这些“扭转”中，节拍是如何间隔的，它们不是统统连在“测试”环节之后的。<br>
<br>
<strong><font color="#de5650">关键路径</font></strong><br>
<br>
如前所述，“节奏设计”假设我们能够影响、预测和限制玩家在游戏中的行为。“关键路径”则是每个玩家完成游戏所必须经历的核心节奏进程，不管这包括什么。<br>
<br>
关键路径可以有多种形式:<br>
<br>
对于遭遇战，关键路径可能是击败敌人的理想策略。<br>
<br>
对于谜题，关键路径是谜题的解决方案，或者至少是最令人满意的解决方案。<br>
<br>
对于移动，关键路径是完成关卡的理想路径。<br>
<br>
<strong><font color="#de5650">绘图和文档</font></strong><br>
<br>
列出和记录关卡节奏的方法有以下几种:<br>
<br>
节拍表：节拍的简单列表<br>
<br>
流程图：节拍如何连接到彼此的图表<br>
<br>
强度图：根据玩家指标绘制的节拍分段条形图<br>
<br>
<strong>节拍表</strong><br>
<br>
在电影和电视剧本创作中，节拍表是列出主要场景和情节要点的列表。我们也可以在游戏关卡中设计节奏: 写下主要事件、场景和关卡的列表。<br>
<br>
把节拍表写在纸上，或一个在线文档/电子表格，或作为一个项目板与可安排的卡片。然后为固定套路、场景、关卡、Boss战等编写构思。比如可以写下段落/行数/笔记/便签，然后重新安排这些节奏，形成一个连贯的大纲。<br>
<br>
下图是《最后生还者》(2013年)的内部规划钉板，顽皮狗的设计师在整个游戏过程中重新安排了不同的关卡、故事时刻和主题。这个“节拍板”帮助他们规划最终游戏的节奏。<br>
<br>
<div align="center">
<img aid="1029347" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092926ffnnkn5z2nnk4b5p.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092926ffnnkn5z2nnk4b5p.jpg" width="554" id="aimg_1029347" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092926ffnnkn5z2nnk4b5p.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">为规划《最后的我们》(2013年)美国电子游戏的内部钉板，顽皮狗公司 （2018）</font></font></div><br>
<strong>流程图</strong><br>
<br>
流程图是过程/程序的可视化图表，有线条、箭头和分支。它将节拍连接的逻辑形象化。这对于具有多种策略和事件链的解密游戏或非线性关卡来说是一种很好的方法。当因果关系非常重要时，使用流程图。在纸上或白板上绘制流程图，或使用在线白板/流程图工具。<br>
<br>
让流程图尽可能的简单。<br>
<br>
试着让流程图沿着一个方向“流动”，例如从上到下，左到右。<br>
<br>
根据节拍类型给流程块涂上不同的颜色。<br>
<br>
把它分成几个小流程图，而不是一个大流程图。<br>
<br>
<div align="center">
<img aid="1029348" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092926h8dw8sfqfv7kqmkl.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092926h8dw8sfqfv7kqmkl.jpg" width="600" id="aimg_1029348" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092926h8dw8sfqfv7kqmkl.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">达纳·南丁格尔 (Dana Nightingale) 设计的《耻辱》中遭遇潜行boss的流程图设计文件</font></font></div><br>
<strong>强度图</strong><br>
<br>
为了更详细地计划节奏，可以根据玩家的指标来排列关卡，并将情节可视化成图表。在《半条命2: 第二章》和《求生之路》的关卡中，Valve公司的设计师将节奏分为4类:<br>
<br>
探索，漫步和导航的空间，通常是关卡的开始和结束。<br>
<br>
战斗，打败敌人。<br>
<br>
演出，一些对话或编排好的脚本序列。用于战斗前或战斗后，在战斗开始或结束时提供帮助的信号。<br>
<br>
谜题，找到道具，打开一扇门等。用来隔开战斗序列。<br>
<br>
因为是基于动作的射击游戏，所以这些设计师关注的是强度。在横轴上，他们以分钟为单位绘制时间。在垂直的Y轴上，用0-100%、0-5或0-10的简单数字刻度来绘制强度。<br>
<br>
<div align="center">
<img aid="1029349" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092926adeqgdt999x9kogo.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092926adeqgdt999x9kogo.jpg" width="600" id="aimg_1029349" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092926adeqgdt999x9kogo.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《半条命2: 第二章》白森林遭遇战的强度图, GDC China 2014</font></font></div><br>
但是“4 / 5强度”是什么意思呢? 强度数值只是一种直觉，是通过了解游戏和观察游戏测试而产生的。这不是一门科学。对于每个项目，必须设计自己的类别和度量标准，比如说如何定义“强度”。<br>
<br>
在《Journey》中，强度并不一定等同于游戏难度。例如，一个受人喜爱的角色死亡后，可能是一个没有玩家介入的低难度过场动画，但它仍然具有较高的情感强度。在这个意义上，强度更适合理解为悬念、玩家的赌注或游戏体验的投入。<br>
<br>
<div align="center">
<img aid="1029350" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092927zkdqz5z56d5rerrr.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092927zkdqz5z56d5rerrr.jpg" width="600" id="aimg_1029350" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092927zkdqz5z56d5rerrr.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《Journey》(2012) 的表格，来自V&amp;amp;amp;A Videogames(2018)。标注了不同体验目标，以及顶部的强度条</font></font></div><br>
<strong><font color="#de5650">节奏的建议</font></strong><br>
<br>
<strong>开始时要慢且安静</strong><br>
<br>
《半条命》(1998)以平凡的6分钟电车之旅开始。以一些低强度的内容开始游戏或关卡，如介绍过场动画或低风险的探索，它为世界建设创造了气氛和时间。甚至像《毁灭战士》或《雷神之锤》这样的强动作射击游戏都是在安静的房间中开始的，玩家可以在这里测试自己的控制并在开始战斗前“热身”。<br>
<br>
<strong>高低交替</strong><br>
<br>
玩家需要适应长时间的高强度训练。任何激烈的boss战在10分钟以上后都会让人觉得很艰难。为了保持新鲜可以利用偶尔的停歇时间，作为对比和调色中的清洁剂，否则玩家将会变得麻木。不要试图强迫玩家一直处于“启动状态”。在高强度的boss战后，过场动画和低强度区域就像是奖励。或者你的核心机制可以鼓励玩家休息并返回城镇，如出售战利品，修理设备，交付任务等。<br>
<br>
<strong>避免最大强度的最终boss /遭遇战</strong><br>
<br>
Thatgamecompany公司读到Joseph Campbell的《Hero’s Journey》后，非常喜欢，并将其游戏命名为《Journey》。其他游戏设计师则将目光投向经典叙事理论，如三幕结构、Gustav Freytag的五幕结构和亚里士多德的诗学。这些传统的叙事理论以失败的行动/“结局”（denouement）/打败最后的反派作为高潮的必然结果，否则就会破坏高潮的冲击力。以下是一些来自游戏的例子：<br>
<br>
《黑暗之魂》的最后一个boss拥有多血条，但其战斗风格却相对简单: 它给人一种挑战性，但却不是游戏中最困难的遭遇战<br>
<br>
《传送门1》和《传送门2》的最终谜题预示了简化的解决方案，它们绝对不是游戏中最困难的谜题<br>
<br>
《半条命2》最后一个关卡，以低压力不平衡的遭遇战为特色，主要的反派人物则在讲述他们不可避免的失败<br>
<br>
<div align="center">
<img aid="1029351" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092927s45lhgl64t6aaatt.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092927s45lhgl64t6aaatt.jpg" width="600" id="aimg_1029351" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092927s45lhgl64t6aaatt.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">典型的五幕情节结构组成图，纵轴更容易理解作为“悬念”而不是“强度”</font></font></div><br>
经典的叙事理论是有用的，但是请注意:<br>
<br>
故事中的紧张感与游戏中的紧张感可能并不相同。<br>
<br>
大多数游戏进程/学习曲线很少有“跌落感的行动”，大多数游戏都是关于避免失败的。熟练的玩法意味着玩家将避免坠落或犯错误。然而，失败和错误往往可以造就更好的故事。<br>
<br>
在游戏之外，这些都是许多作家试图避免的经典叙事理论。使用这些模式通常会让人觉得死记硬背或公式化。<br>
<br>
<strong><font color="#de5650">多人游戏的节奏</font></strong><br>
<br>
竞技性多人游戏中的节奏更多地体现在：整体玩法循环和模式规则中。像《PUBG》、《堡垒之夜》或《Apex Legends》等BR游戏中，当最后几名玩家被困在一个非常小的区域时，比赛将变得更加有趣。但是，这些最后的玩家究竟会在哪里，在什么时候决出胜负呢? 每一场比赛都不同。我们不能把比赛如何进行写进剧本或情节。<br>
<br>
而对于像《反恐精英》《军团要塞》或《守望先锋》之类的团队游戏，关卡设计师必须小心地调整刷新区域和阻塞点之间的移动时间。如果某个团队在某个阻塞点的路径不公平，那么地图就会失去平衡。这种情况下，节奏更像是地图流线、平面布局和参数的直接功能。<br>
<br>
<div align="center">
<img aid="1029352" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092928go4acjyj604qmaxf.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092928go4acjyj604qmaxf.jpg" width="600" id="aimg_1029352" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092928go4acjyj604qmaxf.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《LOL》(左)或《Dust2》(右)等多人游戏地图的节奏很大程度上取决于移动时间、布局和流线</font></font></div><br>
<strong><font color="#de5650">开放世界/非线性的节奏</font></strong><br>
<br>
在开放世界游戏中，玩家通常可以采取多种可能的路线去实现一个目标。设计单一的路径是没有用的，因为我们是有意让玩家拥有一些自由，去创造自己的路径和进程。但与多人游戏节奏一样，开放世界游戏将脚本化节奏最小化，所以平面布局和参数是我们规划玩家穿越关卡的主要工具。<br>
<br>
在潜行类的开放世界游戏《刺客信条》中，关卡设计师创建了一些区域，然后将任务规划为一系列同心圆。随着玩家接近目标，每个阶段/部分将逐渐变得更小更密集。随着玩家逐渐解决敌人防御的各层问题，每个部分的挑战和危机感都会升级。<br>
<br>
<div align="center">
<img aid="1029353" zoomfile="https://di.gameres.com/attachment/forum/202201/26/092929v1jjzc1zrc7vi35v.jpg" data-original="https://di.gameres.com/attachment/forum/202201/26/092929v1jjzc1zrc7vi35v.jpg" width="600" id="aimg_1029353" inpost="1" src="https://di.gameres.com/attachment/forum/202201/26/092929v1jjzc1zrc7vi35v.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《刺客信条》关卡图，绿色为安全观察区域，红色为高防护目标区域，来自Philippe Bergeron在GDC 2016演讲</font></font></div><br>
<strong><font color="#de5650">反节奏</font></strong><br>
<br>
计划和文档在项目的早期阶段是非常有用的，然而：<br>
<br>
文档很快就会过时，需要维护<br>
<br>
许多项目太大了，以至于一个文档无法捕捉其复杂性<br>
<br>
大型工作室和团队维护内部的wiki：可能有数百个设计文件<br>
<br>
你不能测试某份文件；设计文件永远无法脱离现实<br>
<br>
一份最初的计划很重要，因为它能让每个人在同一页上使用共同的语言。但在某些情况下，你必须将注意力放在你所创造的真正游戏上，而不是你所计划的假想游戏。<br>
<br>
<strong><font color="#de5650">要点回顾</font></strong><br>
<br>
<ul><li><strong>节奏是指关卡中活动/事件的理想秩序和节奏。</strong></li><li><strong>节拍是一种活动/事件。</strong></li><li><strong>单人游戏关卡通常都有明确的关键路径和大型的固定套路。</strong></li><li><strong>对于带有战斗和谜题系统的遭遇战游戏来说，“节奏堆”的方法是有效的——先创造一堆遭遇战和谜题，然后再将它们安排好，也许会变成一种“教学-测试-扭转”的模式。</strong></li><li><strong>多人游戏节奏更多地来自于布局，而非创作的事件。</strong></li><li><strong>开放世界/非线性节奏需求更"区域性"的方法。</strong><br>
</li></ul><br>
节奏设计文件可能包括:<br>
<br>
<ul type="1" class="litype_1"><li><strong>节拍表: </strong>写好的大纲，节拍表(或白板)</li><li><strong>流程图: </strong>带有箭头和标识的视觉轮廓图</li><li><strong>强度图: </strong>基于玩家指标(如强度)绘制节拍图表<br>
</li></ul><br>
而当你致力于游戏本身时，这些文件便会变得过时。你可以更新这些文档，也可以忽略它们。<br>
<br>
<font size="2"><font color="#808080">PS：我会定期学习，梳理，输出 【游戏/游戏设计/游戏建筑】 相关的思考或笔记，欢迎感兴趣的朋友，关注我的知乎。如需转载，请私信。</font></font><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/460785796</font></font><br>
<br>
  
</div>
            