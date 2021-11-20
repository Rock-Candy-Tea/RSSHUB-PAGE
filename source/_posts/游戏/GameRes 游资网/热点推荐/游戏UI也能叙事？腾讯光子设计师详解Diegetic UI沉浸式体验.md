
---
title: '游戏UI也能叙事？腾讯光子设计师详解Diegetic UI沉浸式体验'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202111/15/100138pvsk0000d5vr8qfs.png'
author: GameRes 游资网
comments: false
date: Mon, 15 Nov 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202111/15/100138pvsk0000d5vr8qfs.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2518615">
“叙事UI”这个概念从今年初开始出现的频率又逐渐高了起来，而经常伴随它出现的是Diegetic Interface或Diegetic UI这个英文词组，也吸引我想去更多的了解它。在之后阅读文章、翻阅资料的过程中，又发现相关的概念、案例和观点，都更多指向了我们的一个老熟人 —— 沉浸感，因而有了本文的标题《沉浸进行时》。<br><br>
本文主要通过对定义的研究，结合一定的具体案例来学习Diegetic UI本身及其延展概念，然后尝试拓展至沉浸式体验。<br><br><strong><font color="#de5650">一、叙事UI与游戏界面</font></strong><br><br><strong>1.1  初识Diegetic UI</strong><br><br>
Diegetic来源于电影术语，直译是叙事的。在韦氏词典里，特指在一个叙事世界中已存在或正在发生的，而不是这个世界以外的东西。在电影领域，常常和声音结合一起出现:<br><br><ul>
<li>Diegetic Sound —— 剧情声（场景内的声音，角色可听见）</li>
<li>Non-diegetic Sound —— 画外音（旁白，角色不可听见）<br>
</li>
</ul>
<br>
电影本身就是讲故事并以叙事为主，如果游戏也想讲述一个故事，那么游戏和电影就有了高度相似性，得以把电影的概念延伸到游戏UI上，也就有了Diegetic UI的用法。<br><br>
游戏与电影通过互动与相互影响，呈现出不同的艺术形式与作品面貌。在两者的交叉领域，大多数都具备了一定的叙事性内容，为玩家及观众带来不一样的思考和体验。<br><br><strong>1.2  游戏故事与游戏空间</strong><br><br>
游戏要讲述一个故事时，同时也要提供一种体验，这会牵涉到两个重要概念：<br><br>
叙事（Narrative）: 游戏需要叙述的故事本事；<br><br>
第四面墙（The Fourth Wall）：玩家与游戏发生空间之间的想象屏障。<br><br>
基于这两个概念，在设计游戏UI时，就必须回答下面的两个终极问题：<br><br><strong>1. UI是否存在于游戏所叙述的故事情节中？</strong><br><strong>2. UI是否存在于游戏所发生的物质空间中？</strong><br><br><strong><font color="#de5650">二、四种游戏UI类型</font></strong><br><br>
对上述两个问题的不同回答和组织，引出了四种游戏UI的不同类型：<br><br><ul>
<li>Non-Diegetic</li>
<li>Diegetic</li>
<li>Spatial</li>
<li>Meta<br>
</li>
</ul>
<br><div align="center">
<img id="aimg_1021412" aid="1021412" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100138pvsk0000d5vr8qfs.png" data-original="https://di.gameres.com/attachment/forum/202111/15/100138pvsk0000d5vr8qfs.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100138pvsk0000d5vr8qfs.png" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">Level Up: A Guide to Game UI (with Infographic)[3]</font></font></div>
<div align="center"><font size="2"><font color="#808080">左侧栏：UI是否在游戏的故事情节中</font></font></div>
<div align="center"><font size="2"><font color="#808080">上侧：UI是否在游戏的物理空间中</font></font></div>
<div align="center"><font size="2"><font color="#808080">这里先暂时抛开各文章和翻译提供的译名，我们先了解各自的来源和案例，再定下适当的名称，以求描述准确。</font></font></div>
<br><strong>2.1  Non-Diegetic UI</strong><br><br>
既不存在于故事情节中，也不存在于物理空间中 —— 包括玩家所控制的角色，游戏中任何角色都不能感知到它们的存在。<br><br><div align="center">
<img id="aimg_1021413" aid="1021413" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100138iw3h5oaqnwmlr3wy.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100138iw3h5oaqnwmlr3wy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100138iw3h5oaqnwmlr3wy.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">典中典：《超级马里奥》底部UI</font></font></div>
<br>
这类UI通常以2D的HUD方式呈现，承载着统计数据的功能，如：轮盘、血条、小地图等。尤其是在一些快节奏游戏（fast-paced games）如跑酷游戏，以及重度策略游戏中，在某些方面上它们虽然分散了玩家的注意力，容易打破游戏的沉浸感，但提供了更高效的数据阅读方式，让玩家更轻松地评估下一步该如何行动。<br><br>
按照电影术语习惯，可称之为：画外UI，或非叙事UI。<br><br><strong>2.2  Diegetic UI</strong><br><br>
即存在于故事情节中，也存在于物理空间中 —— 游戏角色可以感知到它的存在。<br><br><div align="center">
<img id="aimg_1021414" aid="1021414" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100139b8mugsjodszluzqa.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100139b8mugsjodszluzqa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100139b8mugsjodszluzqa.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">大名鼎鼎：《死亡空间》的背部血条及一切UI</font></font></div>
<br>
这类UI就是游戏世界中的实体本身，能最好地贴合“叙事”的目的，使玩家保持沉浸状态。例如带数据显示的高科技未来感头盔、角色身上的小工具（如怀表），以及角色模型的状态。<br><br>
但由于游戏中的镜头调度或玩家设备上的画面比例不同等种种原因，Diegetic UI可能无法保持良好的持续性。对信息获取率的降低，反而会削弱了体验感。<br><br><div align="center">
<img id="aimg_1021415" aid="1021415" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100140eb5oofiqib6xxr25.png" data-original="https://di.gameres.com/attachment/forum/202111/15/100140eb5oofiqib6xxr25.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100140eb5oofiqib6xxr25.png" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">《赛博朋克2077》中的车辆驾驶，真实但不舒适</font></font></div>
<br><strong>2.3  Spatial UI</strong><br><br>
存在于物理空间中，但不存在于故事情节中。Spatial UI 符合游戏空间里的物理规则，但游戏角色无法感知到它们的存在。<br><br><div align="center">
<img id="aimg_1021416" aid="1021416" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100140vfy123azl58acyzs.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100140vfy123azl58acyzs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100140vfy123azl58acyzs.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">体育竞技：《麦登橄榄球21》的线路展示</font></font></div>
<br>
此类UI通常用于承载空间中的辅助信息，帮助玩家选择一个位置或对象。在《Apex英雄》中，标记系统在物理空间中的标记点也是同类型的UI。其他的例子还有：对物理空间中的对象产生的选中光效，角色靠近物体时出现的文本介绍气泡等等。<br><br>
鉴于其特点，可称作：空间辅助UI。在一些开放世界游戏中，空间辅助UI对玩家快速熟悉游戏世界会非常有帮助。<br><br>
《Apex英雄》中的PING标记系统<br><br>
https://www.youtube.com/watch?v=prBDEKUSPMs<br><br><strong>2.4  Meta UI</strong><br><br>
存在于故事情节中，但不存在于物理空间里。它们和故事情节相关，但不会真实地存在于游戏的物理空间中，因此游戏角色可能或不能感知这些UI的存在。—— 虽然全能的玩家总是什么都知道。<br><br><div align="center">
<img id="aimg_1021417" aid="1021417" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100140su2i4b2qy84u6166.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100140su2i4b2qy84u6166.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100140su2i4b2qy84u6166.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">改良吃鸡：《Apex英雄》的对话文字和受击</font></font></div>
<br>
Meta UI的翻译相当困难，多被译作“元”。考虑到它和叙事的紧密联系，帮助读者更好地理解这个概念，也可以称作叙事辅助UI。和元游戏一样，叙事辅助UI也是很微妙的存在。例如在上图中出现的UI内容，就是FPS游戏里最常见的用途：整个FOV在摇晃、模糊和变红，并表示角色被击中了。<br><br>
元游戏（metagaming），又称“超游”，多指的是包含了游戏制作者为了打破了第四面墙，在游戏中直接和玩家对话的游戏。这会让人想起电影《头号玩家》，以及一些具备互动电影内容的游戏，还有动漫《猎人：Greed Island篇》。<br><br>
叙事辅助UI的另一种用处，就是将作者与玩家的对话信息，进行了文本的可视化呈现。这个用途是最能体验叙事辅助UI 打破了第四面墙 的例子。如果叙事辅助UI的元素过多，而游戏本身也没有明确的世界观设定，容易造对玩家的过度迷惑，从而极大地破坏了游戏的体验质感。<br><br>
在以互动叙事为主的游戏里对Meta UI概念的探索上，以及在很多导演与游戏制作人的努力下，现在已经出现了许多的具备了交叉领域性质的作品。感兴趣的读者可以搜索《孔明的陷阱》(Kaizo Trap)，建议直接在原网页上体验其中的交互操作，以便更好地探索Meta的这个概念。<br><br><div align="center">
<img id="aimg_1021418" aid="1021418" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100141p8wva73axjwd3av2.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100141p8wva73axjwd3av2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100141p8wva73axjwd3av2.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">古早冒险：《塞尔达传说》的滚动文字，带给玩家有用的提示</font></font></div>
<br><strong><font color="#de5650">三、叙事和沉浸感——《死亡空间》与《逃离塔科夫》</font></strong><br><br><strong>3.1  Diegetic及其合适的译名</strong><br><br>
分析了这四种游戏UI后，可以总结出以下的译名：<br><br><ul>
<li>Non-Diegetic UI —— 画外UI，或非叙事UI</li>
<li>Diegetic UI —— 剧情UI，或叙事UI</li>
<li>Spatial UI —— 空间辅助UI</li>
<li>Meta UI —— 叙事辅助UI<br>
</li>
</ul>
<br>
在2018年的GDC游戏开发者大会上，有一个关于UI设计的分享[4]：演讲者Omer Younas将空间辅助UI（Spatial UI）和叙事辅助UI（Meta UI）并入到画外UI（Non-Diegetic UI）的类型中，从”融入游戏世界的程度“的方式进行划分，大家值得一读。<br><br><strong>3.2  沉浸进行时 —— 作为目的</strong><br><br>
既然剧情UI（Diegetic UI）是最贴合叙事目的的UI设计，是不是多使用此类型的UI就能达到沉浸体验呢？<br><br>
不是的，营造沉浸感是目的，而叙事是方法。我们不能把这两者等同。<br><br><strong>3.3  时代的眼泪：《死亡空间》</strong><br><br><div align="center">
<img id="aimg_1021419" aid="1021419" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100141lm6t33sszrluhy3n.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100141lm6t33sszrluhy3n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100141lm6t33sszrluhy3n.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">《死亡空间》在游戏里全部采用了剧情UI</font></font></div>
<br>
《死亡空间》极致地使用了剧情UI：所有玩家可见的UI都真实地存在于游戏世界中，它们被解释为作战服或机器装置所发出的全息影像。游戏还把角色模型作为UI的载体：承载血条和时滞条的信息，这更是深入人心的设计。<br><br>
不得不说，游戏将传统UI全部都融入进了游戏世界的做法，是一个大胆的尝试。它确实验证了剧情UI在沉浸感的营造上有着优势，可是全息影像的设计是取巧的做法，并未对传统的游戏界面有太多的改良，玩家依然会把全息影像想象为传统的2D画外UI。<br><br>
除去角色身上的血条、时滞条以及其他和传统UI差别不大的全息影像外，其实在可交互对象的引导设计上，《死亡空间》也是下了一番功夫。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1021420" aid="1021420" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100141iwxqwvvgdgz2dxex.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100141iwxqwvvgdgz2dxex.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100141iwxqwvvgdgz2dxex.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">可交互的对象必定为蓝色</font></font></div>
<br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1021421" aid="1021421" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100142sek2699hh99ps1dq.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100142sek2699hh99ps1dq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100142sek2699hh99ps1dq.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">不可交互的对象必定为橙色</font></font></div>
<br>
这些提示信息通过剧情UI所呈现出的一致性让人赞叹不已，因此至今人们提起这款游戏仍会津津乐道其UI设计。不过与其说是称赞设计本身，更不如说是赞叹其对设计理念的坚持和统一 —— 里面都是高昂的开发成本。<br><br>
遗憾的是，由于《死亡空间》系列的销量不佳，其工作室已被拆散，但开发人员依然在EA内部发光发热。在《死亡空间》之后，关于对沉浸感营造的游戏，我能想到的激进案例，还得数《逃离塔科夫》。<br><br><strong>3.4  硬核再硬核：《逃离塔克夫》</strong><br><br><div align="center">
<img id="aimg_1021422" aid="1021422" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100142pmmu5nm79bwdmgom.jpg" data-original="https://di.gameres.com/attachment/forum/202111/15/100142pmmu5nm79bwdmgom.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100142pmmu5nm79bwdmgom.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">《逃离塔科夫》中过分干净的游戏界面</font></font></div>
<br>
”硬核得让人崩溃!“——这是不少自媒体对这款游戏的评价。从截图来看，除了右上角的一个模糊的健康状况UI以外，常规FPS游戏中的HUD在这个游戏上都没有。的确，如果手中的武器没有瞄具、准星、弹药数和地图UI等等 —— 那游戏确实营造了一个真实的枪战世界。<br><br>
并且，游戏里所有武器的音效，都是制作组买回真实武器，进行现场录音制作的。<br><br>
《逃离塔克夫》显然非常了解自身的核心玩法。所有的剧情UI（或是没有UI）都围绕着极其真实的逃脱式枪战体验来打造的。2010年EA（制作《逃离塔科夫》的公司）的子公司DICE的设计师Marcus Andrews，对游戏UI在营造游戏沉浸感的研究[6]，对本文的帮助也是极大。<br><br>
尽管在没开始时，游戏里各种局外系统的UI极其难用，但实际游戏中的UI设计和其他元素共同支撑起了玩法，并且创造了独特的游戏体验 —— 所以在谈论《塔科夫》时，我们会更多地谈论它的硬核。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1021423" aid="1021423" zoomfile="https://di.gameres.com/attachment/forum/202111/15/100143y2jukzmdhrh93ure.png" data-original="https://di.gameres.com/attachment/forum/202111/15/100143y2jukzmdhrh93ure.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/15/100143y2jukzmdhrh93ure.png" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">《逃离塔科夫》枪械配件UI</font></font></div>
<br><strong>3.5  相辅相成</strong><br><br>
无论是《死亡空间》还是《逃离塔科夫》，都通过尝试在游戏中打造接近真实的物理世界，让玩家身临其境来营造沉浸感，其剧情UI的使用与游戏整体体验相辅相成。<br><br>
在营造游戏沉浸感的天平两端，起码要有叙事体验与交互体验。剧情UI（Diegetic<br><br>
UI）在将游戏打造得足够真实的同时，也有可能会导致交互体验的不佳 —— 玩家如产生了挫败感，极有可能会打破其中的沉浸感。因此，在把握游戏中细微的叙事性与交互性的平衡尤为重要，在感知、认知和操作的方面，都是我们可以考虑的方向。<br><br>
对沉浸感平衡的把握，是基于目标和结果的。如果调配适当的四类游戏UI能增进沉浸感，他们也许就可被称作“沉浸式UI”：<br><br>
“有效地传递信息，为玩家带来更好的游戏体验，能让玩家沉浸于游戏互动。”<br><br><strong><font color="#de5650">四、后记</font></strong><br><br>
本文从Diegetic UI及其相关的概念定义入手，举例学习、陈述了游戏UI的四个分类，也引申出了关于沉浸感的一些思考。<br><br>
实际上，对这些内容的研究，已经有业界的先锋进行了一些前沿探索，例如前文提到的Micah Bowers、Omer Younas和Marcus Andrews各自都有独特的想法。与游戏沉浸式UI相关的资料，现时来说，在中文网站上显然并不充沛。<br><br>
然而在游戏的体验中，心流体验作为一种认知体验，又是比沉浸感更加深入的体验。<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/1K0OtORAIgtdFsyOFaiIGA</font></font><br><br>
</td></tr></tbody></table>


  
</div>
            