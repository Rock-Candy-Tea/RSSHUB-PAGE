
---
title: '开发指南：关卡设计概念 Level Design Concepts'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/16/142634xz4gpwlzswllwudd.jpg'
author: GameRes 游资网
comments: false
date: Fri, 16 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/16/142634xz4gpwlzswllwudd.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2505122">
伟大的游戏设计师在创建游戏世界时，会使用类似相同的概念。如果你身在这个行业内，你会知道什么有效，什么无效。其中一些，你很自然地便已理解，而另一些，则只能通过反复试错。<br>
<br>
<i><font color="#808080">作者：Nathan Cheever</font></i><br>
<br>
目前在加州光子工作室任开放世界设计师，前黑手党3和老Prey(被Zenimax社通过法律漏洞强行流产掉的项目)开放世界设计师<br>
<br>
<i><font color="#808080">译者:Katana</font></i><br>
<br>
十九流技术美术&业余关卡设计师&Modder，www.katanaproduction.cn<br>
<br>
每个人都有一个属于自己的个人设计概念清单。但重点是，每个公司或团队都会通过带来另一层的称谓(Label)，来持续跟踪这些概念。因此，通过为这些Idea提供通用语言，可以帮助你快速与他人分享Idea、建议和反馈。<br>
<br>
本文所介绍的内容，可以让你的关卡和玩法变得更加出色！并且这是一个不断发展的系列文章，所以记得偶尔回来看看。<br>
<br>
2008年的演讲<br>
<br>
几年前，我向Six Days in Fallujah的团队展示了这个旧版本。它的PPT演讲被包含在下文中。不不过首先警告一下......其中一部分内容已经过时了，然而，我相信观看它也可以让你了解一下大致粗略的想法。<br>
<br>
https://youtu.be/kBAl0CysTiU<br>
<br>
<ul><li>主题(Topics)</li><li>概述(Update)</li><li>概念元素(Update)</li><li>布局元素(Layout Elements)</li><li>缺失的元素(Missing Elements)</li><li>关卡节奏(Level Rhythm)</li><li>游戏区域(Game Zones)</li><li>战斗区域(Combat Zones)</li><li>概述(Overview)<br>
</li></ul><br>
想要在我们的游戏中创造出，足以让玩家在通关游戏后的几个月，还能去谈论和回味的精彩游戏回忆。那么我们需要做到，玩家每次在游戏中的遭遇战(Encounter)，都要比上次更具挑战和创新。而通过保持玩法(Gameplay)的新鲜感，可以在游戏中激励玩家期待下一次的遭遇战和通关游戏—还想要更多更多内容！<br>
<br>
<i><font color="#808080">本文讨论的一些想法来自于以下内容：</font></i><br>
<br>
<i><font color="#808080">Josh Bridge’s The Anatomy of a Combat Zone (战斗区域剖析)</font></i><br>
<i><font color="#808080">Joseph Campbell’s The Hero With a Thousand Faces 《千面英雄》</font></i><br>
<i><font color="#808080">Kevin Lynch’s The Image of the City 《城市意象》</font></i><br>
<i><font color="#808080">Brian Upton’s Narrative Landscapes</font></i><br>
<i><font color="#808080">Narrative Landscapes Shaping Player Experience (gdcvault.com)</font></i><br>
<i><font color="#808080">Rainbow_Sixs_Upton_Talks_Landscaping_Game_Worlds (gamasutra.com)</font></i><br>
<br>
请记住，规则总有例外，这里所提出的想法，仅仅是帮助我们进行游戏开发的指南，我们应该始终对它们进行重新评估，以得以找到帮助我们改进过程的方法—当然，也请时刻记得，如何保持简单和专注！<br>
<br>
译者：Encounter: 遭遇，相遇，邂逅，交锋等<br>
<br>
<strong><font color="#de5650">什么是关卡？(What is a Level?)</font></strong><br>
<br>
大多数人会说它是游戏实际发生的场所。实际上，它是游戏呈现给玩家的媒介。可以说，没有关卡就没有游戏。它不仅仅只是一个简单的场所，我们应当将其视为，它是将游戏推向新玩法的载体。它会影响玩家遇到和进入下一个事件时的速度(Speed)，风格(Style)和技能(Skills)。<br>
<br>
<strong><font color="#de5650">为什么需要关卡设计师？(Why are Level Designers Needed?)</font></strong><br>
<br>
在当今市场上，人们会以自己是某个领域出类拔萃的专家而自豪。一个好的关卡设计师了解布局，而一个伟大的关卡设计师则是一个千斤顶的交易，因为他了解游戏开发的所有方面。不要将一个搭建关卡的人，和一个将经验阅历所凝聚起来的人混淆一谈。<br>
<br>
关卡设计师不仅需要意识到布局，还需要意识到建筑、照明和构图，是如何影响玩家当下的情绪反应。他们需要在没有对话的情况下进行叙事，以及在其他时候提供引人入胜的对话。他们需要能够编写代码、脚本和设计玩法。还需要搭建模型，和理解节奏和动画。<br>
<br>
<div align="center"><strong>关卡设计师是艺术，音效，玩法和叙事的胶水。</strong></div><br>
有些人认为，玩游戏和懂游戏的环境艺术家是成为关卡设计师的精髓。毕竟，艺术家也可以创建布局，构想玩法，和检查游戏性能。不幸的是，艺术家总是会选择美学而不是玩法。身处一个在媒体中画面截图胜过玩法的时代，这就是他们的工作。<br>
<br>
一个典型配置的团队，拥有比关卡设计师多2—3倍的环境艺术家。在不提供同等或更好玩法的情况下，不要让这种不平衡抑制玩法需求。玩家玩了几个小时的游戏后，将更关注于玩法，而不是图形画面的惊艳程度。<br>
<br>
然而，艺术家应当被视为共同开发者。让他们从初始阶段就参与到关卡设计的过程，将会非常重要。概念艺术影响一个关卡的开发。通过和他们一起分享开发进程，他们将成为关卡的部分所有者，并在准备给其他人审查Poke关卡时，共同努力捍卫。并且，永远不要在还不了解游戏将如何运用他们的付出时，要求他们做出贡献。例如，对于某物外观的简单改变，就可完全破坏游戏。<br>
<br>
<strong><font color="#de5650">概念元素(Conceptual Elements)</font></strong><br>
<br>
通常，玩家会逐渐熟悉游戏内部，并思考，甚至会在潜意识层面去分析他们周遭环境。在电子游戏中，去描述这种Push&Pull的心理反应并不新鲜。在我们握住操控杆或是滑动鼠标之前，它便已存在很久。这些想法，早已被用于城市规划、主题公园设计，和绝大多数的常用景观设计。他们运用这些概念为居民提供方向，兴趣区域，以及创造出充满惊奇感的区域。<br>
<br>
这里是世界上最出名的游戏关卡之一。数百万人曾经玩过......<br>
<br>
<div align="center">
<img id="aimg_993222" aid="993222" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142634xz4gpwlzswllwudd.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142634xz4gpwlzswllwudd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142634xz4gpwlzswllwudd.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图1：迪士尼乐园的Main Street USA</font></font></div><br>
主题公园设计与关卡设计相同。它通过运用建筑和景观去放大游客将见证的叙述内容，从而被动地塑造交互体验。<br>
<br>
在迪士尼世界，你从Main Street USA开始—一个一望无际满是商店的入口，最终通往远处雄伟的灰姑娘城堡。但，这里却只有一百码长的纪念品商店......没有景点，没有游乐设施？到底有多蹩脚？然而，这种步伐节奏，却早已悄悄为冒险定下心理基调！<br>
<br>
在任何故事的开头，都会布置一个基线，来讲述先前发生之事，以此表明何为日常生活，而我们可以透过未来的事件来向其展示成长。<br>
<br>
在约瑟夫·坎贝尔的《千面英雄》中，它描述了这个已经存在了几个世纪的故事模式。人们渴望并期待这种模式，以此心满意足地踏入虚构之旅。<br>
<br>
<strong>第一幕(Act I)</strong><br>
<br>
<div align="center">
<img id="aimg_993223" aid="993223" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142635q93jy539ps32vj3h.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142635q93jy539ps32vj3h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142635q93jy539ps32vj3h.jpg" referrerpolicy="no-referrer">
</div><br>
Main Street USA稳固了参与者在熟悉环境中所感受到的舒适常态，而城堡则作为我们内心深处英雄之旅的召唤。<br>
<br>
<strong>第二幕(Act II)</strong><br>
<br>
<div align="center">
<img id="aimg_993224" aid="993224" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142636wsisom7nljcy3loc.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142636wsisom7nljcy3loc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142636wsisom7nljcy3loc.jpg" referrerpolicy="no-referrer">
</div><br>
在我们迈过门槛时瞬间点燃—例如经过吊桥—开始一系列冒险<br>
<br>
<strong>第三幕 (Act III)</strong><br>
<br>
<div align="center">
<img id="aimg_993225" aid="993225" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142636mfy0xyy36cpt343w.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142636mfy0xyy36cpt343w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142636mfy0xyy36cpt343w.jpg" referrerpolicy="no-referrer">
</div><br>
我们返回家乡，回归正常生活，但如今却已永远被此经历所改变<br>
<br>
Main Street USA的设计为整个体验定下基调。它把人们置于英雄的心态之中。没有戏剧性的节奏和期待，就不会有回报，探索感和冒险！<br>
<br>
本文目的之一便是展示如何精心组织关卡以创造此类叙事时刻。<br>
<br>
坎贝尔的书描述了叙事结构，凯文林奇的《城市印象》则描述了场所结构。在书中，他分享了用于主题公园设计，城市规范和景观美化的称谓。它确立了人们是如何概念化城市的理论基础。<br>
<br>
例如，通过采访波士顿的居民，他得以分解区域中的每个区域。<br>
<br>
<div align="center">
<img id="aimg_993226" aid="993226" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142636mvk5ljh9l5nkhfvq.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142636mvk5ljh9l5nkhfvq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142636mvk5ljh9l5nkhfvq.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图7：波士顿及其主要道路的鸟瞰图</font></font></div><br>
通过绘制加权路径和方向来展示令人难忘的区域，波士顿的景观与人们对它的记忆相匹配。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_993227" aid="993227" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142637pvyjsstzdlssr2ss.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142637pvyjsstzdlssr2ss.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142637pvyjsstzdlssr2ss.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图8：基于人们印象的波士顿</font></font></div><br>
<strong><font color="#de5650">寻找灵感(Finding Inspiration)</font></strong><br>
<br>
窃取想法！如果你相信的话，不要感觉尴尬或是将其伪装成新的东西。为什么我们要不断花时间去思考别人过去没有做过的事情呢？没有绝对原创的想法。任何新事物，都会受到过去思想的影响：不论是好的还是坏的。重要的是你的想法需要比之前的任何想法都要好。所以，寻找一些令你受到启发的事物，让它成为你自己的。当它在发展过程中不断演变，直到得以看到曙光的那一天，出现在人们面前时，它将成为一个可以独立存在的新想法。<br>
<br>
<strong><font color="#de5650">布局元素(Layout Elements)</font></strong><br>
<br>
通过运用通用语言描述关键元素，我们可以超越最初想法，达到协同创新的目的。以下是每个关卡应当具有的五个核心元素......<br>
<br>
<strong><font color="#de5650">地标(Landmarks)</font></strong><br>
<br>
地标给人一种独特感和比例感。玩家使用它们进行三角测量，这样他们就不会迷路。通过创造一些有趣的事物，玩家会自然而然地走向它。它们还可作为同他人分享经验的参考点。<br>
<br>
<div align="center">
<img id="aimg_993228" aid="993228" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142637qf58lr58wyhgi1c4.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142637qf58lr58wyhgi1c4.jpg" width="430" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142637qf58lr58wyhgi1c4.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_993229" aid="993229" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142637ndo85s18krofxpng.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142637ndo85s18krofxpng.jpg" width="430" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142637ndo85s18krofxpng.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_993230" aid="993230" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142638sf8xfozcglxfgmjz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142638sf8xfozcglxfgmjz.jpg" width="430" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142638sf8xfozcglxfgmjz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图9：著名地标</font></font></div><br>
<strong><font color="#de5650">路径(Paths)</font></strong><br>
<br>
一条路径是连接两个区域的路线。然而，并非所有路线都是路径。例如，你可以有一条不被视为路径的街道，因为它不会导致任何有趣的事情。如果是从未使用过的路径，请将其删除以防止混淆。<br>
<br>
记住，玩家走的是阻力最小的路径。阻力最小的路径可以吸引玩家的注意力，而最小的障碍可以把玩家赶走。路径也可以由其动量(momentum)来定义。除非是被什么有趣的事情所吸引(Pulled)，否则，当一条路径结束时，玩家会倾向于朝着同一方向保持移动。<br>
<br>
路径有两种：<br>
<br>
显式路径(Explicit Path)—使用清晰明朗的线条，例如小径，走廊，街道等等。<br>
<br>
隐式路径(Implicit Path)—由缺口和障碍所暗示，环绕着区域的负空间。<br>
<br>
<div align="center">
<img id="aimg_993231" aid="993231" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142640dxv1f2qiuia0al4f.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142640dxv1f2qiuia0al4f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142640dxv1f2qiuia0al4f.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图10：显式路径</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993232" aid="993232" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142641y98tybykpy1b2ydo.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142641y98tybykpy1b2ydo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142641y98tybykpy1b2ydo.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图11：隐式路径</font></font></div><br>
这些变化可以用来控制玩家的运动，尤其关卡是开放和自由形式时。<br>
<br>
<strong><font color="#de5650">边界(Points—of—Interest)</font></strong><br>
<br>
边界是区域之间的界限。一旦越过了界限，就会有新的事物出现！当玩家穿过门槛时，应当揭示(Reveal)出一个景观、埋伏或奖励。边界可以由门，明确的角落(Corner)或是地形中的山脊来定义。<br>
<br>
它们改变了当下环境，正因如此，它们将转化为戏剧性的节奏—这也被一些人称之为"揭示"。通过管理边界，设计师可以控制玩家跨越游戏世界时每时每刻的情绪。<br>
<br>
<div align="center">
<img id="aimg_993233" aid="993233" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142641ewwizfkkavqp61st.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142641ewwizfkkavqp61st.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142641ewwizfkkavqp61st.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图12：抵达边界</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993234" aid="993234" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142642sp5pvxtdpzdvv57t.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142642sp5pvxtdpzdvv57t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142642sp5pvxtdpzdvv57t.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图13：穿过边界抵达高潮</font></font></div><br>
像彩虹六号这样的游戏，几乎完全使用边界。他们甚至具有一个围绕边界本身所构建的游戏机制：“偷袭另一边的家伙！”一旦门被打开，行动瞬间爆发，玩法逐渐显现......<br>
<br>
<div align="center">
<img id="aimg_993235" aid="993235" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142643htcbpkdzxssl23sx.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142643htcbpkdzxssl23sx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142643htcbpkdzxssl23sx.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图14：穿越边界</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993236" aid="993236" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142643hylnzkxcre8blnyz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142643hylnzkxcre8blnyz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142643hylnzkxcre8blnyz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图15：穿过窗口的边界</font></font></div><br>
<strong><font color="#de5650">兴趣点(Points—of—Interest)</font></strong><br>
<br>
兴趣点(POI)可以是房间，森林空地或是城镇中心，比如农贸市场， 甚至可以是大厅楼下的火车车厢。它们可以是聚会，休息或是思考下一步将去何处。兴趣点由空间的组织方式来定义。它们的边界不一定是一堵字面意义上的墙，它们可以用"概念上的墙"作为边界，如树木或丘陵。它们可以为该区域提供一种场所感，并可为其增添令人印象深刻的权重。而事件往往发生在兴趣点，有关其更多用法，可以参考面包屑理论。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_993237" aid="993237" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142644wqoau88oufxvs8q6.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142644wqoau88oufxvs8q6.jpg" width="430" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142644wqoau88oufxvs8q6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图16：巨石阵</font></font></div><br>
<strong><font color="#de5650">地区(Districts)</font></strong><br>
<br>
最后，一个地区是一块区域的集合，有一个整体主题或是装饰风格。它与原始几何体无关。我们可以将它们看作“局部氛围”—例如唐人街或威利街。每个地区都应至少拥有一个地标，以赋予它一个用途或焦点。<br>
<br>
像迪士尼乐园这样的主题公园都是关于地区的。每个区域都专门介绍了一个主题，包括它所包含的一组景点。Frontier—Land, Tomorrow—Land…甚至Main Street USA。<br>
<br>
<div align="center">
<img id="aimg_993238" aid="993238" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142645tdjl3zlrxlx9xljz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142645tdjl3zlrxlx9xljz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142645tdjl3zlrxlx9xljz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图17：迪士尼乐园各区域字面意思上的划分</font></font></div><br>
<strong><font color="#de5650">缺失的元素(Missing Elements)</font></strong><br>
<br>
当一个关卡令人感到混乱或是提不起兴趣时，可能是由于它缺少布局元素。以下是缺少元素的八个常见例子......<br>
<br>
<strong><font color="#de5650">“一模一样的该死走廊”(The Same Damn Corridor)</font></strong><br>
<br>
每个人都有可能会在一些游戏中遇到这种情况—"一模一样的该死走廊"。当关卡看起来到处都一模一样，变得无聊和重复时，就会发生这种情况。<br>
<br>
还记得第一代Halo吗？几乎所有地方看起来都长这样！<br>
<br>
<div align="center">
<img id="aimg_993239" aid="993239" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142645vpda79u93t9q3tuz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142645vpda79u93t9q3tuz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142645vpda79u93t9q3tuz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图18：Halo走廊 'A'</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993240" aid="993240" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142645qcwww9vv555s9o10.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142645qcwww9vv555s9o10.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142645qcwww9vv555s9o10.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图19：光环走廊 'B'</font></font></div><br>
当下列情况出现时会遇到这些问题：<br>
<br>
缺少地标—没有独特的视觉包装(糖果)或参照点<br>
<br>
对称或重复—包括过度使用实例化的几何体<br>
<br>
太多路径—到处都是死路，然而在那里没有真正发生什么<br>
<br>
<strong><font color="#de5650">“隐藏通道”(The Secret Passage)</font></strong><br>
<br>
当玩家错过一个转角时就会发生这种情况。除非是受到什么有趣的东西（如地标）的提示，否则玩家会一直倾向于直线行进。每个转角都应显而易见—至少开始时是如此。如果你可以通过游戏早期的关卡，来教导玩家寻找替代路径并适应变化，那么你便有理由让玩家在后续关卡中更加努力地寻找这些选项。<br>
<br>
例如，你是否可以在以下左图中，找到一些隐藏通道可能存在的线索？<br>
<br>
<div align="center">
<img id="aimg_993241" aid="993241" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142646hd93xc3ej9b898xe.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142646hd93xc3ej9b898xe.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142646hd93xc3ej9b898xe.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图20：隐藏门在哪？</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993242" aid="993242" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142646qv5vbbjx0p9rgppp.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142646qv5vbbjx0p9rgppp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142646qv5vbbjx0p9rgppp.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图 21：......藏在角落！</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993243" aid="993243" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142647pxd77e77sb5brbr4.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142647pxd77e77sb5brbr4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142647pxd77e77sb5brbr4.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图22：隐藏门在哪？</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993244" aid="993244" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142648h3gzgp89ut07bg09.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142648h3gzgp89ut07bg09.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142648h3gzgp89ut07bg09.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图 23：......就在你面前！</font></font></div><br>
造成这些混乱的原因是：<br>
<br>
缺少地标—没有独特的视觉包装(糖果)或参照点<br>
<br>
较低路径权重—重要路径没有受到足够重视<br>
<br>
屏幕外边界—画框的重要变化，以确保玩家可以清楚辨别<br>
<br>
取决于你的受众，实际上你可能非常想要一段晦涩难懂的章节，但它永远不应该是完成这一关的关键。<br>
<br>
<strong><font color="#de5650">"无处可走"(The Road to Nowhere)</font></strong><br>
<br>
这是低级关卡设计的常见示例。当没有什么有趣的东西存在时，它便会粉碎玩家的成就感，并质疑他为什么浪费时间玩这款游戏。<br>
<br>
<div align="center">
<img id="aimg_993245" aid="993245" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142649alhi2usa6cyyhil2.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142649alhi2usa6cyyhil2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142649alhi2usa6cyyhil2.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图24：神枪手可不会有这种鸟瞰式的奢侈享受。</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993246" aid="993246" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142653qdqrv4ofobgq4pfo.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142653qdqrv4ofobgq4pfo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142653qdqrv4ofobgq4pfo.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图25：用一个死胡同来奖励探索......</font></font></div><br>
探索应当会导致一些很Cool的东西，而突然玩消失或结束，会令玩家感到非常沮丧！小心：<br>
<br>
缺少兴趣点<br>
<br>
<strong><font color="#de5650">"错误的入口"(The Wrong Doorway)</font></strong><br>
<br>
同上述问题类似，但是在穿越边界时会更加具体—如果一扇奇妙的大门，打开后却里面藏的却是一个储物柜，这样就会伤害玩家的期望。<br>
<br>
例如在ICO里，如果你奋力冲向一扇沉重大门，进去后却仅仅发现了一个又小又空的房间，你就会觉得你漏掉了一些明显的东西。你会思考，自己是否忽略了一个隐藏门或是开关？一个精心设计的边界应当奖励玩家同样精妙的东西。<br>
<br>
<div align="center">
<img id="aimg_993247" aid="993247" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142654sv440c0umu7cmv71.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142654sv440c0umu7cmv71.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142654sv440c0umu7cmv71.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图26：重要的入口通往何处？</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993248" aid="993248" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142654i6bfq4q46jl21cdf.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142654i6bfq4q46jl21cdf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142654i6bfq4q46jl21cdf.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图27：简单的入口通往何处?</font></font></div><br>
事实恰好相反。一个简单的入口应当通向一个简单的区域。但是，如果一个看似毫不起眼的壁橱却通向一个隐藏的冬季幻想世界呢？嗯，一个存在于C.S. Lewi故事中的例子是， 衣柜是玩家很早便会意识到的兴趣点。在其他任何游戏中，它都仅仅只是一件微不足道的家具，玩家往往会因为它过于缺乏存在感而感到混乱。<br>
<br>
译者：参考恶灵附身和某些恐怖生存游戏的惯用伎俩，玩家可以藏匿在衣柜或是床底等区域。<br>
<br>
为了避免这种混乱，请注意：<br>
<br>
<ul><li>较小边界比例—被用于兴趣点或是地标</li><li>较小路径比例—被用于兴趣点或是地标<br>
</li></ul><br>
错误的比例可能无法向玩家预示下个区域的范围和重要性。一个好的经验法则：玩家的移动距离，永远不应小于其目标边界的比例。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">“不够稳健的角落”(The Weak Corner)</font></strong><br>
<br>
当元素以一种缓慢渐进的速度被发现时，就会导致缺乏戏剧性。而这样会造成下一个地点的作用变得模棱两可。当一个角落忘记被视为垂直边界时，就会发生这种情况。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_993249" aid="993249" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142654ppppqvmqpfuhy901.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142654ppppqvmqpfuhy901.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142654ppppqvmqpfuhy901.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图28：这里没什么大发现。</font></font></div><br>
缺失的边界—记得使用角落。它们是触发事件的好地方。<br>
<br>
<strong><font color="#de5650">“缺失的墙”(The Missing Wall)</font></strong><br>
<br>
类似于同样的事物太多，太少会给玩家带来一种不确定感。一个没有明确边界而模棱两可的地方，可能会导致玩家去探索一条预期之外的路径，该区域的用途被稀释。<br>
<br>
<div align="center">
<img id="aimg_993250" aid="993250" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142655pdidrm4cuudaluci.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142655pdidrm4cuudaluci.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142655pdidrm4cuudaluci.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图29：当你需要指南针的时候，指南针在哪儿？</font></font></div><br>
<strong><font color="#de5650">"无路森林"(The Trackless Forest)</font></strong><br>
<br>
类似于上面的例子，玩家没有方向—而这次，则是因为同样的事物太多。为了避免这种问题，应当创建并安排一个具有人造结构感的区域。<br>
<br>
<div align="center">
<img id="aimg_993251" aid="993251" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142655rjkcvy2qtrkj5c3h.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142655rjkcvy2qtrkj5c3h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142655rjkcvy2qtrkj5c3h.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图30：同样的事物太多......</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993252" aid="993252" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142656t6snnxxzokksnsko.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142656t6snnxxzokksnsko.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142656t6snnxxzokksnsko.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图31：......玩家在目的地中感到混乱。</font></font></div><br>
要想解决以下问题：<br>
<br>
缺失的路径—引导玩家沿着直线继续<br>
<br>
缺失的边界—告诉玩家为什么和他们在何处移动<br>
<br>
通常，在一款线性事件驱动型的游戏中，这种自由形式的外观，或许有可能在关卡中使用。在《生化危机》系列中，探索会受到摄像机角度和屏幕边界，以及限制性的玩家方向选择束缚。<br>
<br>
<strong><font color="#de5650">“消防水管”(Fire Hosing)</font></strong><br>
<br>
当兴趣点相互叠加时，体验会变得平淡且疲惫。事件的强度，应当有起伏变化，以帮助激发玩家的情绪反应。如果游戏缺乏这种节奏变化，那么固定的强度，将会很快成为未来所有遭遇战的新起点。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_993253" aid="993253" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142657hoe2kh423ko2j3hh.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142657hoe2kh423ko2j3hh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142657hoe2kh423ko2j3hh.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图32：越来越多的行动！</font></font></div><br>
兴趣点太多—无法为下一个事件建立预期时间<br>
<br>
电影《加勒比海盗》系列，因为其每个场景，都有着过度的爆炸行为而臭名昭著。这导致，最终创造一种合理的强度时会失败—因为它破坏了观众的悬念。一旦发生这种情况，玩家就不会再相信你为他们所创造的世界。<br>
<br>
<strong><font color="#de5650">关卡节奏(Level Rhythm)</font></strong><br>
<br>
关卡节奏是控制玩家叙事体验的最基本方法之一。每一次的相遇（在书籍、电影、游戏中）都有高潮和低谷的体验。运用关卡的结构去控制游戏节奏，可以帮助激发玩家的情绪反应。<br>
<br>
<strong><font color="#de5650">关卡风格(Level Styles)</font></strong><br>
<br>
不同的模式(Pattern)会导致玩家不同的情绪状态。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">路径主导(Path—Dominated)</font></strong><br>
<br>
玩法需要通过强调连续运动的快速本能反应，并且具有少数的边界和兴趣点的，则是路径主导。这些通常是(距离/时间)漫长的线性关卡，其中经典，例如GT赛车或刺猬索尼克。<br>
<br>
<div align="center">
<img id="aimg_993254" aid="993254" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142658b4fo8zfxo7n85oxw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142658b4fo8zfxo7n85oxw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142658b4fo8zfxo7n85oxw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图33：GT赛车</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993255" aid="993255" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142658piar3aak6wtktfkr.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142658piar3aak6wtktfkr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142658piar3aak6wtktfkr.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图34：刺猬索尼克</font></font></div><br>
在赛车游戏中，边界和兴趣点可能会降低玩家的速度。当边界真的出现时，它往往较为柔软，且伴随着很长的远景。<br>
<br>
路径主导的关卡特征：<br>
<br>
<ul><li>漫长的线性关卡</li><li>少数的边界</li><li>少数的兴趣区域</li><li>强调连续运动<br>
</li></ul><br>
<strong><font color="#de5650">边界主导(Edge—Dominated)</font></strong><br>
<br>
相比之下，边界主导的关卡通过使用较短的视线来创造更高压力(可能是走廊或门)。这种连续的固定节奏，着重于一连串令人印象深刻(戏剧性)的揭示，其中最经典的例子便是生化危机。每道门槛对于玩家来说都是一件大事。<br>
<br>
<div align="center">
<img id="aimg_993256" aid="993256" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142658hb39fe3mi31u53iu.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142658hb39fe3mi31u53iu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142658hb39fe3mi31u53iu.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图35：生化危机</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993257" aid="993257" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142659fy8gzyyzvpd25y5l.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142659fy8gzyyzvpd25y5l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142659fy8gzyyzvpd25y5l.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图36：惊喜！</font></font></div><br>
边界主导的关卡特征：<br>
<br>
<ul><li>近视线</li><li>许多走廊和入口</li><li>一连串令人印象深刻(戏剧性)的揭示<br>
</li></ul><br>
<strong><font color="#de5650">兴趣点主导(POI—Dominated)</font></strong><br>
<br>
最后一种更常见的游戏类型的节奏，涉及由兴趣点主导的关卡。而这些令人敬佩的游戏，则是由开放空间和许多与之交互的事物，再结合普遍缺乏的时间压力所定义(请参阅随后讨论的探索和解谜区域)。<br>
<br>
例如，在ICO或马里奥世界中，探索是玩家花费时间所带来的奖励。<br>
<br>
<div align="center">
<img id="aimg_993258" aid="993258" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142659k77r8idv7moamovm.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142659k77r8idv7moamovm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142659k77r8idv7moamovm.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图37：ICO</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_993259" aid="993259" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142700wklna7m2wamazmom.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142700wklna7m2wamazmom.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142700wklna7m2wamazmom.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图38：马里奥世界</font></font></div><br>
兴趣点主导区域的特征：<br>
<br>
<ul><li>开放空间</li><li>丰富的交互</li><li>缺乏时间压力<br>
</li></ul><br>
有趣的是，这两张截图都有一座城堡在背景中，作为一个服务于体验的焦点。<br>
<br>
<strong><font color="#de5650">游戏范例(Examples of Games)</font></strong><br>
<br>
让我们将其中的一些想法应用于以下两款动作射击游戏。他们的玩法截然相反，但他们却存在于同一类型之中。<br>
<br>
<strong><font color="#de5650">彩虹六号：拉斯维加斯</font></strong><br>
<br>
<ul><li>幽闭恐惧症—由牢固紧凑的内部和固定的边界，来充当掩体</li><li>近视线—小而激烈的击杀区域(Kill Zones)</li><li>许多走廊和门—关卡发生在一个地标性建筑</li><li>路径是安全的—作为从一场遭遇战到下一场遭遇战的过渡</li><li>边界是危险的—闯入隔壁房间时会爆发冲突<br>
</li></ul><br>
幽灵行动颠倒了彩虹六号的公式。对近距离的恐惧已经被对开放空间的恐惧所取代，从而颠倒了安全/危险的关系。<br>
<br>
<strong><font color="#de5650">幽灵行动:尖峰战士</font></strong><br>
<br>
<ul><li>陌生环境恐惧症—具有分散掩体的开放空间</li><li>远视线—大而灵活的击杀区域</li><li>少数的内部空间—关卡发生在一个较大地区或区域</li><li>路径是危险的—由长或宽阔的街道去调查冲突</li><li>边界是安全的—作为从一场遭遇战到下一场遭遇战的过渡<br>
</li></ul><br>
<strong><font color="#de5650">猜猜游戏风格</font></strong><br>
<br>
<strong>神秘海域</strong>是什么类型的游戏？答案<br>
<br>
<strong>镜之边缘</strong>是什么类型的游戏？答案<br>
<br>
<strong>暴雨</strong>是什么类型的游戏？答案<br>
<br>
<strong><font color="#de5650">其他帮助(Additional Helpers)</font></strong><br>
<br>
我们也可以运用其他一些不可忽视的技巧…...<br>
<br>
<strong><font color="#de5650">面包屑(Breadcrumbs)</font></strong><br>
<br>
面包屑是一系列兴趣点或游戏中引导玩家的事件。<br>
<br>
<ul><li>跟随队友—引导玩家进入一个区域最直接的方法！</li><li>发现敌人—他们从何处攻击可以提示玩家去寻找该区域。</li><li>镜头—一个短镜头剪辑或缩放聚焦到一个物体，可以突出其重要性。</li><li>贴花—一些比较微妙或明显的内容，例如血迹、墙壁刮痕或涂鸦。</li><li>照明—光影和明暗，色彩和明度(Value)，甚至是舞动的(Animated)照明。</li><li>运动—运动物体可以吸引玩家的注意力，比如正在关闭的大门或是舞动的符号。</li><li>拾取放置</li><li>标识牌—一些比较微妙或明显的内容，例如，一个巨大的发光箭头或是一张"你在这里"的地图。</li><li>声音—有时会很难指望的上，声音是另一个玩家会作出反应的元素。<br>
</li></ul><br>
<strong><font color="#de5650">UI帮助(UI Helpers)</font></strong><br>
<br>
除了塑造实际环境之外，我们还可以使用UI来帮助我们引导玩家，具体方法因游戏而异。而如果所有其他方法均已失败（或该游戏的本质是更为开放的环境）时，应当使用以下方法。<br>
<br>
<ul><li>地图—屏幕或屏幕的一部分，专门用来描述布局。它可以是静态的，也可以是动态的，用来揭示所有或只揭示已发现的内容。</li><li>指针—指向视线之外的关键地点，有时会依附在一个小地图或标线上。</li><li>增强现实—突出显示环境中的关键物体。<br>
</li></ul><br>
<strong><font color="#de5650">框架吸引力(Framing Interest)</font></strong><br>
<br>
关于信息是如何向玩家传递的最后一个说明。<br>
<br>
游戏通过视频屏幕所呈现，而这个像素框架为玩家勾画了游戏世界，使得屏幕上物体的方向和位置，对于理解当前游戏世界中所正发生的事情而言，至关重要。<br>
<br>
如果一个物体或事件对玩家至关重要，那么它应该呈现在屏幕中央附近。虽然我们无法保证玩家会看向何处，但我们可以料想到，他们通常会看向一些有趣的事情。比如说，通常情况下，玩家会先朝着新出现的游戏素材看去。<br>
<br>
如果一个物体或事件对玩家的游戏体验而言并不重要，那么它可以在屏幕上的任何地方存在。而此时，玩家唯一看不到的东西（即屏幕外）则应当是真正的隐藏物品，这种方法只能在特殊情况下使用。举个例子，如果玩家需要爬上悬崖抵达一个隐藏洞穴，而底部却没有梯子 —引导他向上的方向—那么屏幕顶部下方应该可以看到一个明显的抓取点—而不是在屏幕之外所看不见的。<br>
<br>
<ul><li>关键元素—屏幕中央的50%之内</li><li>非关键元素—屏幕上的任何地方</li><li>隐藏元素—可以位于屏幕之外<br>
</li></ul><br>
通过理解符合自然规律的部分来进行有效布局，我们可以保证游戏中的每个区域都很有趣，并且具有不断升级的遭遇战节奏。<br>
<br>
<strong><font color="#de5650">启发灵感的布局(Inspiring Layouts)</font></strong><br>
<br>
设计师面临着一遍又一遍地去呈现相同核心玩法的挑战。为了保持事物的新鲜感和趣味，呈现出和以往不同的新布局至关重要。<br>
<br>
每次遭遇战的理想结果是：<br>
<br>
<ul><li>玩家得到"令人难忘的回忆"—在令人兴奋的地点进行一场扣人心弦的遭遇战。</li><li>玩家不想停止游戏—他们渴望继续进行下一场遭遇战，直到游戏结束。<br>
</li></ul><br>
创造出令人兴奋的布局的灵感有多种来源：<br>
<br>
<ul><li>故事中的故事节奏和故事情节点。</li><li>一天中的时间和天气状况(特别是如果这些对玩法有影响的话)。</li><li>该区域的主要地标（和普遍建筑）。</li><li>电影，书籍，其他游戏—甚至不是同一类型或主题的游戏！<br>
</li></ul><br>
创造奇景包括：漫长的道路、雄伟的地标、向上的斜坡，以及比例变化。创造喜悦感需要“兴趣点终点”(Terminal Points—of—Interest)—即重大高潮事件的兴趣点。它们的特征是经常出现的预示(Foreshadowing，也称伏笔)和一个长距离接近目标的关卡。在某种程度上，电子游戏中情节与关卡几何体的关系，与音乐乐谱的构成方式非常相似。被嵌入的弧线—高峰和低谷，反映了主人公的情绪状态—逐渐抵达高潮。这便是一个有节奏的关卡......<br>
<br>
Foreshadowing：可以理解为在每关卡开头时的一次镜头或者各种形式的引导，告知玩家本关的目标和终点。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">游戏区域(Game Zones)</font></strong><br>
<br>
动作游戏创造了一个独一无二的宇宙。它让我们得以从更大的游戏世界(Game World)的概念去缩放，由领域(Realm)开始，穿越层层界限(Boundarie)：<br>
<br>
译者：想要正确理解以下内容前，请确保能够理解 Realm、District、Zone、Area、Region之间的差异。具体参考此链接(https://bbs.iikx.com/blog—4—4150.html)。由于译者语言水平有限，无法找到更为准备描述的词语，因此暂用以下词语代替。<br>
<br>
<ul type="1" class="litype_1"><li>每个领域(Realm)都具有不同于其他领域的整体风格。它包含地区(Districts)。</li><li>每个地区(District)都有一个独特的艺术主题，用以补充游戏风格（一个典型关卡）。它包含活动区域(Action Zones)。</li><li>一个活动区域(Action Zones)可以是一个相邻地区（一个典型的子关卡Prefab）。它包含地带和*区域(*Zone)。</li><li>地带(Region)是活动区域中物品(Items)的特殊区域(Specific Area)。它包含节点组(Node Group)。节点组是游戏逻辑中所使用的物品集合。有关地带和节点(Nodes)的更多详细信息，请阅读关卡设计结构。</li><li>*区域是活动区域中的基本区域(Organic Area)。它们被用于标记该区域将主要使用哪些类型的玩法（战斗、探索、解密、叙事）。它也可以在地带和节点组之间进行转型。*区域通常不会重叠。它们不一定会勾勒出交互区域(Interactive Area)的范围，并且也可能具有温和的边界(Soft Edge)。<br>
</li></ul><br>
译者：关于地区(District)的一些具体设计，可以参考镜之边缘：催化剂是如何设计玻璃城中不同地区的。https://archive.mirrorsedgearchive.org/<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_993260" aid="993260" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142700kjwpkpeo5pkpgkgw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142700kjwpkpeo5pkpgkgw.jpg" width="520" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142700kjwpkpeo5pkpgkgw.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图41：一个游戏世界的拆解</font></font></div><br>
注：除了地区和活动区域以外，所有其他Group都仅仅只是概念或游戏对象。只有地区和活动区域才是实际文件（关卡和子关卡Prefab）。<br>
<br>
<strong><font color="#de5650">活动区域(Action Zones)</font></strong><br>
<br>
关卡被划分为活动区域(AZ)。而在这些AZ内，则是游戏实际所发生的场所！如果你正在与一辆大坦克战斗或追捕猎物时，它便会在此出现。<br>
<br>
在实际游戏中，由一个AZ过渡(Transition)到其他AZ时，将会成为一个正常高低节奏的第一步。<br>
<br>
然而，AZ并不仅仅局限于战斗：它们还可以包含故事事件或探索区域。这个多功能区域是我们耗费了大量资源和时间，使得游戏变得更加刺激和令人印象深刻的地方。<br>
<br>
AZ应当是由独立体块的玩法和几何体所组成。正因如此，它们也是一个关卡中，你能将其所有权提供给施工团队的最大的一部分。<br>
<br>
确保一个AZ与其他AZ相隔离，可以为游戏开发提供许多优势：<br>
<br>
<ul><li>AZ可以被保存为其它更大关卡中的Prefab。</li><li>AZ允许多人同时在一个关卡中工作。</li><li>当出现了关卡内存或性能上的问题时，我们可以更为轻松地移动或删除AZ。因为，只有将两个AZ连接在一起的路径(Path)才需要调整。<br>
</li></ul><br>
<strong><font color="#de5650">*区域类型(*Zone Types)</font></strong><br>
<br>
在AZ中，由常用用途所定义的区域，被称作*区域。除了追逐区域(Chase Zone)和过渡区域(Transition Zone)之外，所有其他的区域(Zone)都应仅与一个AZ相关联。但其中仍有一些其他可以重叠(Overlap)的区域，比如，一个探索区域内的一个解密区域。<br>
<br>
译者：作者的文章诞生至今已经间隔一两个世代，游戏关卡设计的变化却没有太大变化。在第八世代和本世代游戏中，区域(Zone)由于各种丰富多样的玩法变得五花八门。但它的核心思想仍未过时 —在AZ中依据区域的功能特性进行划分，功能将决定其自身是否可以重叠交错于其他区域。<br>
<br>
<strong><font color="#de5650">战斗区域(Combat Zone)</font></strong><br>
<br>
游戏中玩家所花费的绝大多数时间都在此区域，具体时长取决于关键的游戏指标。所以一定要好好注意！有关更多详细信息，请参阅下文的战斗区域部分。<br>
<br>
译者：CP2077的一名关卡设计师，大梨子(Max Pears)编写了两本短小精悍而又生动有趣的关卡设计书籍，其主要探讨的内容是战斗(Combat)和探索(Exploration)。<br>
<br>
<strong><font color="#de5650">追逐区域(Chase Zone)</font></strong><br>
<br>
从A点到B点的"轨道式"序列......不要随便在穿越高细节环境时溜达。追逐序列是唯一可以跨越其他AZ或*区域的事件。该区域也可用于节奏较慢的追踪X人踪迹的玩法。<br>
<br>
<strong><font color="#de5650">探索区域(Exploration Zone)</font></strong><br>
<br>
物理导航或"平台(Platforming)"，为该区域提供了非线性的探索(Discovery)。该区域也可用于涉及搜索关键物品的区域，例如玩家资源 。<br>
<br>
译者：这里译者个人认为描述的比较模糊，物理导航可能是指，在该区域内提供了例如指示牌、POI或地图等多种空间引导的手段，而Platforming则可能是在区域内提供多块平台状空间，令玩家以一种非固定的顺序去执行目标(寻宝？寻找信息？etc...)。这种本人理解的方式可能比较狭隘，欢迎交流和反馈。<br>
<br>
<strong><font color="#de5650">解密区域(Puzzle Zone)</font></strong><br>
<br>
类似于探索区域，不同之处在于它们专注于兴趣点，在继续推进之前需要时间来解决。<br>
<br>
<strong><font color="#de5650">安全区域(Safe Zone)</font></strong><br>
<br>
可以保证玩家在此处没有生命危险。<br>
<br>
<strong><font color="#de5650">叙事区域(Story Zone)</font></strong><br>
<br>
禁止战斗，通常是提供了影视化叙事(Cinematic，译者：电影化CG过场)的区域。（MMO则会提供社交区域(Social Zones)）。<br>
<br>
<strong><font color="#de5650">过渡区域(Transition Zone)</font></strong><br>
<br>
此类区域的作用是将AZ和其它AZ相连接。由于性能原因，它们也导致了能见度的瓶颈(限制)。在此类区域中，不应存在任何重要的兴趣点。<br>
<br>
过渡区域还平衡了在AZ中所发现的精彩部分(Hightlight)，他们为玩家的活动提供了一小段间歇，让玩家有时间为下一次的遭遇战做准备。通过控制玩法或是踏入安全区域，AZ中可以存在休息时间，但这些都是可选的。唯一始终提供休息时间的区域是过渡区域。<br>
<br>
将遇到彼此分开的简单性质可增强内容清晰度，从而更容易在游戏中管理、添加或减去遇到。<br>
<br>
将遭遇战彼此分离的简单本质加强了内容的清晰性，使得在游戏中更容易管理、添加或减少遭遇战。<br>
<br>
将遭遇战彼此之间相互分离的简单本质，增强了内容的清晰度，从而使遭遇战在游戏中管理、添加或减少时更容易。<br>
<br>
过渡区域提供了 ：<br>
<br>
<ul><li>一个可以让玩家休息和重新部署的安全区域。</li><li>肾上腺素回归基准线的"重置按钮"。</li><li>保存游戏的地方。</li><li>为下一次的遭遇战，提供了流式加载新内容的时机。</li><li>出于性能考虑，一个现有的关卡可以很轻松地拆分为两个部分。<br>
</li></ul><br>
<strong><font color="#de5650">遭遇战(Encounters)</font></strong><br>
<br>
一场出色的遭遇战，需要由正确要素所组成—这里有一个清单：<br>
<br>
<strong><font color="#de5650">场所(Location)</font></strong><br>
<br>
玩法类型和规模(Scale)有助于确定细节的密度：<br>
<br>
<ul><li>街道到街道—最低细节，通常只有建筑表面。（即GTA系列）</li><li>建筑到建筑—外部和内部混合。（即神秘海域系列）</li><li>房间到房间—最高细节，非常适合近距离战斗或深入搜查。（即蝙蝠侠阿卡姆系列）<br>
</li></ul><br>
<strong><font color="#de5650">游戏玩法(Gameplay)</font></strong><br>
<br>
专门的目标，有助于聚焦游戏中已发现的大多数玩法风格：<br>
<br>
<ul><li>获得(Acquire)—得到X物品</li><li>捕获(Capture)—得到X人</li><li>追逐(Chase)—追赶X人</li><li>战斗(Combat)—与人战斗</li><li>逃跑 (Escape)— 找到一种方法以离开该区域</li><li>护送(Escort)—保护X人（或物品）......通常会减缓移动并限制攻击。</li><li>潜入(Infiltrate)—潜入X区域</li><li>定位(Locate)—寻找X物品（或区域）</li><li>跟踪(Track)—寻找X人<br>
</li></ul><br>
<strong><font color="#de5650">活动区域（和*区域）调节</font></strong><br>
<br>
最初的玩法和动态的每一分钟的玩法，都会影响场景难度。<br>
<br>
<ul><li>掩体密度(Cover density)—数量，静态的，动态的，可破坏的，甚至可以将周围环境的NPC作为人质(掩体)。</li><li>势力类型(Faction type)—数量，密度和所占比率（黑帮、警察、帮派等）</li><li>分区(Partitioned)—不是全部都在视野范围之内，例如多层楼层或平台（促进攀爬）。</li><li>人口密度(Population density)—更多的NPC，通常意味着更少的敌方AI计算和复杂度。</li><li>资源(Resources)—弹药和HP利用率。</li><li>尺寸(Size)—大或小（在上述场所类型的背景下）。</li><li>垂直度(Verticality)—运用场景元素升高或降低它们。（更高/更低）</li><li>能见度(Visibility)—照明、雾、烟尘等等。<br>
</li></ul><br>
<strong><font color="#de5650">战斗区域(Combat Zones)</font></strong><br>
<br>
AZ并不局限于一次遭遇战，在同一个空间里可能会发生多次。被指定用于战斗的区域是战斗区域(CZ)。CZ可以由有形界限(Physical boundaries)定义，也可以不由有形界限来定义—<br>
<br>
它可以是一座庭院，也可以是一块空地。玩家应当能够很轻松地，通过辨别核心Gameplay元素来辨别 CZ，例如：一个目标、一个出口、掩体、阻塞点(CheckPoint)、次要路线，当然还有敌人！<br>
<br>
每一场战斗都可以分解为战术上的要素：<br>
<br>
<ul type="1" class="litype_1"><li>确认敌人—找到坏人！</li><li>确认环境中的可变因素—掩体在哪里？击杀区域在哪里？</li><li>规划进攻</li><li>进攻敌人—击杀！<br>
</li></ul><br>
<strong><font color="#de5650">布局(The Layout)</font></strong><br>
<br>
是什么造就了一个伟大的CZ？是布局！它定义了玩家将在何处留神、移动、射击、躲避和被射击。第一步是为该区域创建3D草图，并放置将定义CZ的所有关键对象。<br>
<br>
但这绝不应该是最终版本！总之无论如何，3D草图都应该充分传达出布局的独特性。<br>
<br>
<strong><font color="#de5650">竞技场形态(Arena Shape)</font></strong><br>
<br>
绝大多数的战场被归类为以下三种形态之一：<br>
<br>
<ul><li>走廊(Corridor)—门厅(Hallway)或街道</li><li>场地(Field)—屋顶或房间</li><li>障碍(Bottleneck)—具有锥形区域（例如沙漏状的阻塞点）。<br>
</li></ul><br>
<strong><font color="#de5650">世界不是平的(The World Isn’t Flat)!</font></strong><br>
<br>
最常见且最容易制作的是带有随机掩体碎块的平面布局。<br>
<br>
或许作为一个早期的训练关卡，勉强还OK，因为早期几乎不需要自由探索。但是当它们充斥在整个游戏过程时，就会变得非常无聊—“去过那里，就那样吧......”。为了避免出现这些低谷，我们需要充分利用世界是三维的这个事实，通过创建布局，提供各种路径，掩蔽点和射击点以供玩家利用。<br>
<br>
需要记住的一个关键是，"上面"和"下面"是引导玩家注意新的威胁和时机的好地方。<br>
<br>
<strong><font color="#de5650">为玩家提供选择(Give the Player Choices)</font></strong><br>
<br>
让玩家决定在枪林弹雨中他是想要开火，还是移动。又或者是潜行接近前方敌人并偷袭，阻止敌人知道他在附近。动作射击游戏支持不同的游戏风格：奔跑&喷射，弹出&射击(砰砰)，或偷袭&暗杀。在设计CZ布局时，需要适应这些不同的玩法风格，以确保玩家不仅有选择，而且还可选择他们所喜欢的风格。<br>
<br>
比如说，有没有方法绕过敌人而不被发现？有多种掩体选择吗？玩家能否利用关卡中的某物来"欺骗"AI，使其以某种方式行事？它可以是简单的，例如诱使敌人进入一个阻塞点，也可以是复杂的，例如制造一个分身，吸引敌人远离玩家想去的地方。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">它明显吗(Is it Obvious)？</font></strong><br>
<br>
在CZ中为玩家提供多种选择和路径，可以增加许多重玩价值。但是，如果玩家看不到它，一切都将白费心思。因此，请尽量避免试图向玩家隐藏备用路线和选项。<br>
<br>
<strong><font color="#de5650">风险与回报(Risk and Reward)</font></strong><br>
<br>
让玩家感到被赋予力量和无人能挡并没有错，即使是很短的一段时间。被猎杀的人转变为猎人是很有吸引力的（吃豆人吃能量丸）。在布局中，考虑放置物体或道具，将在战斗中为玩家带来巨大优势。例如：一把强大的武器被显著的放置在战场中央—玩家可以选择安全地躲在掩体下继续战斗，或者也可以选择，尝试冒着生命危险冲向武器。<br>
<br>
<strong><font color="#de5650">非传统掩体(Unorthodox Cover)</font></strong><br>
<br>
通过在整个关卡中使用外观相似的掩体对象，玩家将逐渐察觉游戏机制并失去沉浸感。玩家可以察觉到即将到来的战斗。当玩家靠近一个区域时，一堆类似的物体被放置在一条“冲刺&掩护”的路径上，原本令人惊喜的元素就会消失。尝试使用各种不同的物体来提供掩体，并思考它看起来怎样才会更加自然。比如说，为什么不用倒下生物的尸体或车辆作为掩体呢？<br>
<br>
<strong><font color="#de5650">动态掩体(Dynamic Cover)</font></strong><br>
<br>
理想情况下，游戏引擎支持动态掩体。动态掩体分为两方面：减少或创建它。通过允许掩体对象受到伤害来减少掩体。当物体受到伤害时，掩体会被逐渐破坏，甚至被消除。可以通过允许在Gameplay过程中移动或修建掩体对象的方法，来创建掩体。一个简单的例子便是移动装甲车，玩家可以将它作为掩体躲在后面。而另外一种更为复杂的方法，则取决于可以变形的地形，它将爆炸引起的大坑作为掩体。<br>
<br>
<strong><font color="#de5650">证明它(Justify it)</font></strong><br>
<br>
为什么掩体会出现在那里？让我们从头开始回答这个问题：<br>
<br>
<ul><li>地形是光滑平坦的、起伏的、凹凸不平的还是陡降的？</li><li>这里有小溪、河流或是干涸的河床吗？</li><li>植被是稀疏还是茂密旺盛？</li><li>建筑物或树木有被推倒吗？</li><li>人们如何进出这个区域？</li><li>它是旧的还是新的？</li><li>掩体是人造的吗？为何它们会在这里？<br>
</li></ul><br>
为了强化暂停怀疑(Suspension of disbelief)，布局必须可信。这并不是说现实世界中的结构总是完全有道理，当你在现实世界中遇到一些愚蠢的东西时，你会接受它的存在，并把它当作怪异的东西，然后不屑一顾。然而，在游戏中，玩家会认为这是关卡设计师的怠惰，这会影响到他们的暂停怀疑。<br>
<br>
<i><font color="#808080">译者：有关Suspension of disbelief的更多补充，可以阅读知乎老师们的相关回答https://www.zhihu.com/question/323172891/answer/674510624</font></i><br>
<br>
以下是一些有助于保持玩家沉浸感的注意事项：<br>
<br>
<strong>功能(Functionality)</strong>—布局必须呈现出功能性。只有当一个起作用的CZ需要奇怪地放置物体时，才会有例外。比如说，如果它是一个仓库，它是如何装卸物体的？所有东西都能穿过出入口吗？很多游戏的特点是，成吨的板条箱漫无目的地散落在逻辑上不该有板条箱的区域......为什么？<br>
<br>
<strong>历史(History)</strong>—这个区域存在多久了？如果它很古老，布局是否反映了这一点？它是满目苍夷还是乱七八糟？对于布局历史的思考，有助于产生关于结构及其状态的想法。如果它很古老，你能否从前门直接进来？它是杂草丛生的吗？它衰落了吗？也许另一条从倒塌的围墙进去的路径，会更加符合这个布局的年龄。<br>
<br>
<strong>有目标的角色(Characters with purpose)</strong>—没有什么能够比那些在可预测循环中巡逻，或是傻站着和闲逛等待被击杀的敌人更能打破玩家的幻想了。他们的职能是什么？当你进入这个区域时，他们应该正在做什么？如果他们刚刚抵达，他们会在基地进行装卸吗？如果他们已经在那里呆了一段时间，他们会做什么来消磨时间？<br>
<br>
证明其合理性并为之创造一个可信环境，简单来讲是指，物体的随机装配，并非严格服务于，创建令人难忘的CZ这个目标。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">堆叠战斗区域(Stacked Combat Zones)</font></strong><br>
<br>
同时激活多个CZ时要小心。如果多个CZ被搁置在次要位置，就有可能"火上浇油"，导致玩家的体验被冲淡，或是本应前进的方向被混淆。<br>
<br>
<strong><font color="#de5650">战斗区域指南(Combat Zone Companions)</font></strong><br>
<br>
以下元素有助于创建一场有效的战斗......<br>
<br>
<ul><li><strong>击杀区域(Kill Zone)</strong>—穿越生死临界点。</li><li><strong>防御区域(Defense Zone)</strong>—位于击杀区域的边界，用以帮助玩家决定应如何应对。</li><li><strong>安全区域(Safe Zone)</strong>—并不总是存在，可以提供绕过冲突的捷径。</li><li><strong>战略点(Strategic Points)</strong>—可以倾斜胜利天平的地方。</li><li><strong>进攻方向(Attack Direction)</strong>—(敌人)从一个紧密集中的方向开始，直到(玩家)被完全包围。<br>
</li></ul><br>
<strong><font color="#de5650">击杀区域(Kill Zone)</font></strong><br>
<br>
击杀区域是指，玩家或 AI 没有掩体，会受到攻击，并可能会被击杀的区域。这个区域有可能是可见的（地面上的地雷），也有可能是虚拟的（曳光弹）。击杀区域的有效性决定了交火的难度。如果没有一个有效的击杀区域，就会导致玩家不需要掩体，一个原本被用于玩法的关键要素被消除。<br>
<br>
<strong><font color="#de5650">让它充满挑战(Make it Challenging)！</font></strong><br>
<br>
随着逐渐习惯了击杀区域的概念，玩家会感觉CZs越来越老套和缺乏变化，而此时游戏玩法就会面临过时的风险。如果玩家在整个战斗过程中，只不过是反复在同一防御区域表演“弹出&射击”时，这一点会格外正确。设计令玩家改变角度和位置的击杀区域，并迫使其找到一个新的防御区域。将有助于为玩家带来，这是一个充满变数世界的印象，和聪明而又逼真的AI的错觉。<br>
<br>
实现充满挑战的击杀区域的方法：<br>
<br>
<ul><li>AI从防御区域的侧翼包抄玩家</li><li>AI会撤退或冲锋—取决于玩家是否正在削减他们的人手，或者是否出现了僵局</li><li>区域内的破坏变化</li><li>......建筑物或树木倒塌从而改变布局</li><li>......摧毁了一座桥，导致敌人跌落</li><li>......墙壁可能会被推倒，或者在上面打个大洞<br>
</li></ul><br>
<strong><font color="#de5650">让它生效！</font></strong><br>
<br>
根据过往的经验，建立一个有效的击杀区域时会存在一些问题：<br>
<br>
<ul><li>玩家没有真正的防御区域</li><li>......AI的行为允许他们进攻防御区域，却不会关注自身的死活</li><li>......当可破坏掩体被用作防御区域唯一的掩体时</li><li>......当进攻直接绕过了玩家所使用的掩体时；比如爆炸时的溅射伤害</li><li>玩家无法辨别"击杀区域"。没有它，防御区域也就不得而知了</li><li>玩家看不到替代路径或玩法选项</li><li>......如果作为设计师都很难找到，那么玩家就更不用提了(对于玩家而言，它是看不见的)</li><li>击杀区域超出预定区域</li><li>......由于AI的视距，在防御区域之外时他们仍然在战斗</li><li>......当玩家脱离战斗达到一定距离时，AI应当撤退</li><li>每一场战斗都不一定是最后一场。积极在关卡中为玩家提供一些“轻而易举”的战斗，作为节奏的一部分，让玩家感觉他很强<br>
</li></ul><br>
玩家很可能会从他们认为过于棘手的击杀区域撤退，并采用远距离狙击的策略来削弱对手。其结果将导致，游戏的节奏和强度急剧下降。对此，玩家所产生的印象是：游戏并不是真的非常困难，除非他们发挥地超级谨慎......玩家会因此丧失乐趣<br>
<br>
<strong><font color="#de5650">防御区域(Defense Zone)</font></strong><br>
<br>
与击杀区域所对应的是防御区域。它是玩家或AI在掩体保持安全的区域。如果没有它，游戏将被归纳为射击或被射击。因此，我们需要几种不同的掩体选择以供玩家使用—最好是不同形状、大小和强度（无论是永久的还是可破坏的）<br>
<br>
<strong><font color="#de5650">安全区域(Safe Zone)</font></strong><br>
<br>
安全区域可以提供以下几种选择：<br>
<br>
<ul><li><strong>重组点(Regroup Point)</strong>—让玩家有时间去思考该如何继续进行的地方 。</li><li><strong>秘密侧袭(Secret Flanking)</strong>—一种得以让玩家在不被发现的情况下，通往敌人防御区域侧翼，并潜入部分（或全部）击杀区域的方法。<br>
</li></ul><br>
<strong><font color="#de5650">战略点(Strategic Point)</font></strong><br>
<br>
在这些子区域（击杀区域、防御区域或安全区域）中的任何一个子区域，都可能会有让某人占据优势的场所，这些都是战略点。比如说，虽然位于击杀区域的山顶由于太过柔软，而无法提供任何掩体，但它确实提供了高于众人的高度。而防御区域则可能会有一个面向正门的击杀孔眼，作为战略点（击杀区域的阻塞点）。<br>
<font color="#de5650"><br>
</font><br>
<strong><font color="#de5650">自由形式VS明确定义(Freeform vs. Defined)</font></strong><br>
<br>
CZ主要有两种类型：<br>
<br>
<ul><li><strong>明确定义</strong>—具有明确的阻塞点，玩家必须在其中穿过并战胜一个击杀区域。</li><li><strong>自由形式</strong>—一种零散的以探索为主的CZ，在此类CZ中击杀区域并没有被严格执行。在CZ内部，各种各样的区域有可能会被连接在一起。<br>
</li></ul><br>
包含两种类型且平衡的关卡，将有助于防止玩家疲劳。明确定义的CZ，通常会对玩家的技能要求很高。从整个游戏过程中的整体难度曲线来看，后期关卡中，明确定义的CZ通常会比自由形式的CZ多一些。<br>
<br>
需要注意的是，一个具有大量敌人的自由形式区域，最终可能会导致玩家被包围，造成难以想象的困难局势。<br>
<br>
<strong><font color="#de5650">相互转变(Switching it up)</font></strong><br>
<br>
是否可以设计一种CZ，开始时是自由形式，随后变成明确定义的，反之亦然？转变有可能会是令人兴奋的部分，从而创建一个"令人难忘的时刻"。<br>
<br>
<strong><font color="#de5650">增加难度(Increasing Difficulty)</font></strong><br>
<br>
在创建 CZ 时，需要仔细考虑增加CZ难度的方法。一些比较明显的方法，例如调整敌人的数量和位置。另外一种方法则是，调整道具和武器的位置。更具创意的选择则有可能会影响到实际的几何体，比如改变布局，以创造一个更小的防御区域或更大的击杀区域！<br>
<font color="#de5650"><br>
</font><br>
<strong><font color="#de5650">攻击方向(Attack Direction)</font></strong><br>
<br>
从一个紧密集中的方向开始，直到(玩家)被完全包围（具体细节很快就会补充）。<br>
<br>
译者：作者不会在补充了，有兴趣了解更多相关内容，可以去阅读本Blog中翻译的有关接近矢量相关的文章。<br>
<br>
<strong><font color="#de5650">总结(Summary)</font></strong><br>
<br>
通过理解一场遭遇战所需的正确要素，我们准备一个重大事件就会变得容易许多。因为玩家会记得，是什么使这个事件不同于上一个事件？<br>
<br>
设计一个新场所时需要记住的首要概念：<br>
<br>
<ul><li>布局(The layout)</li><li>关键结构(Key structures)</li><li>掩体对象(Cover objects)</li><li>多种选择(Multiple choices)</li><li>有效击杀区域(Effective Kill Zones)</li><li>安全区域(Safe Zones)<br>
</li></ul><br>
为了制造紧张感，必须确保在关卡的安全和区域之间存在冲突。而如果没有休息时间，玩家的情绪很难会有上升。游戏必须通过持续的威胁线索来建立预期。例如，《生化危机》在游戏开始时就精心地将走廊定义为安全区域—结果一只僵尸狗突然从一扇窗户外撞到游戏里，打破了玩家刚刚建立起的安全感，并给玩家带来了一种没有任何地方绝对安全的感觉。为玩家“设计恐惧”时请注意 !!!<br>
<br>
<div align="center">
<img id="aimg_993261" aid="993261" zoomfile="https://di.gameres.com/attachment/forum/202107/16/142701q5uq5u5zbdgnusbb.jpg" data-original="https://di.gameres.com/attachment/forum/202107/16/142701q5uq5u5zbdgnusbb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/16/142701q5uq5u5zbdgnusbb.jpg" referrerpolicy="no-referrer">
</div><br>
<i><font size="2"><font color="#808080">原作者主页：https://www.curiousconstructs.com/about/</font></font></i><br>
<font size="2"><font color="#808080"><br>
</font></font><br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：开放世界设计研究所</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/mneo_0BqxOw_e5weixJ6Hg</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            