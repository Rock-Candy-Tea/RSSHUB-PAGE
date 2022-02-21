
---
title: '十位游戏开发者共话_游戏 UI_：定义、设计和实践案例'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202202/09/094201vata8tn7aa7hchin.jpg'
author: GameRes 游资网
comments: false
date: Wed, 09 Feb 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202202/09/094201vata8tn7aa7hchin.jpg'
---

<div>   
<div align="center">
<img aid="1030189" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094201vata8tn7aa7hchin.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094201vata8tn7aa7hchin.jpg" width="600" id="aimg_1030189" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094201vata8tn7aa7hchin.jpg" referrerpolicy="no-referrer">
</div><br>
<font size="2"><font color="#808080">作者：董晶晖</font></font><br>
<font size="2"><font color="#808080">本文首发公众号“六十和二四的世界”</font></font><br>
<br>
我最近和十位游戏开发者，分别就游戏 UI 进行了探讨。十位开发者来自于游戏业界的不同公司/组织，从事不同方向的游戏开发。他们拥有很多共同点：具备出色的技能；对游戏充满了热情；从事非 UI 领域开发。我试图通过这样一个谈话，重新审视 UI 在游戏开发中扮演的角色。我相信这样的交流能产生认知的碰撞。而事实证明，我在此过程中获取的信息量，远远超过我的预估。<br>
<br>
<strong><font color="#de5650">一、什么是 UI?</font></strong><br>
<br>
尽管我们可以通过资料查阅，找到 UI 的定义：<br>
<br>
用户界面（ User Interface ）是系统和用户之间进行交互和信息交换的媒介，它实现信息的内部形式与人类可以接受形式之间的转换。<br>
<br>
然而概念是“静止”的。游戏开发者在工作生产中所形成的理解，更能体现 UI 对于当下的意义。我大致把大家关于此问题的回答分为两类：广义 UI 和狭义 UI。<br>
<br>
这里所说的广义 UI 是指不单把图形界面（ GUI ) 视为 UI。<br>
<br>
“ 游戏就是 UI。游戏本身就是一种互动，它是一个交互的过程。”（ 游戏美术师 speedTurtle3.0 )<br>
<br>
即 UI 不仅包含传统定义中的用户图形界面，还包含游戏的实时画面以及其他部分。这种理解非常有意思，因为它把游戏本体变成了载体的一部分，即游戏也是交互媒介的一部分。与其说我们是在“玩游戏”，到不如说整个过程我们是在“玩 UI ”。根据这种定义，玩家和 UI 的接触范围被远远地扩大了，同时游戏中的各个系统更有可能和 UI 产生更强的交集。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1030190" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094202bxg9ak8d3tkmhtmt.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094202bxg9ak8d3tkmhtmt.jpg" width="600" id="aimg_1030190" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094202bxg9ak8d3tkmhtmt.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《Destiny 2》 中的 Tower 本质上就是一个巨大的 UI 空间</font></font></div><br>
数名游戏设计师，则强调 UI 作为一个媒介的特质:<br>
<br>
“（ UI 是 ）使用多种元素（ 图像、文字、声音 ）将一个游戏的内容以更高效率的方式呈现给玩家的一个方法集合。”（ 游戏设计师 Bigby ）<br>
<br>
“UI 是帮助我与硬件交互的中介。”（ 游戏主设计师 金潮 ）<br>
<br>
“它是用户与产品沟通的工具和手段。”( 游戏设计师 空力使 ）<br>
<br>
大家都着重提到了“交互”，即玩家与游戏的互动：游戏会根据玩家的输入，及时给予反馈，帮助玩家以最友好、最有效的方式做出操作。同时大家提及的媒介类别，分别涉及到硬件部分、图像部分、文字部分、声音部分、触觉部分、体感部分。这基本涵盖了游戏 UI 的所有类别。在其他产品中，UI 还包含嗅觉部分、味觉部分。这些特殊的类别虽然目前没有应用到游戏产品中，但我们不能忽视这种可能性。<br>
<br>
<div align="center">
<img aid="1030191" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094202yu2ne2ozirn77hie.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094202yu2ne2ozirn77hie.jpg" width="600" id="aimg_1030191" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094202yu2ne2ozirn77hie.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">基于人类嗅觉设计的 UI 作品《Bouquet》</font></font></div><br>
狭义 UI 更多是基于用户图形界面（ Graphical User Interface ，简称 UI ），即传统意义上的游戏 2D UI 界面。<br>
<br>
“User Interface，就是我在应用中能看到的界面，但不包括界面中的内容。比如菜单中的武器信息、子弹的数量、血量的数值。而游戏中的内容不是 UI。简单来说，除了玩家的实际游戏内容，其他的都可以被认为是 UI。”（ 游戏概念设计师 鱼丸 ）<br>
<br>
“UI 就是一个视觉化的界面，能让玩家完成交互。”（ 游戏制作人 Daniel )<br>
<br>
无论是作为玩家还是开发者，用户图形界面无疑是我们接触最多的 UI 形式。而正是 GUI 定义了我们与电子游戏，乃至当代数码产品的交互方式。相比于过去我们与硬件工具直接进行交流，GUI 帮助用户/玩家以一种更能理解的方式，去完成操作和解读机器的反馈，从而打破了专家和普通人之间的壁垒，为民用计算机（ 和家用游戏机 ）的普及扫除了障碍。<br>
<br>
<div align="center">
<img aid="1030192" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094202ov472y7tvzeltl44.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094202ov472y7tvzeltl44.jpg" width="600" id="aimg_1030192" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094202ov472y7tvzeltl44.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">为 GUI 推广做出巨大贡献的产品 Apple Macintosh</font></font></div><br>
尽管大家对于 UI 的定义存在少许差别，但是我们基本明确了 UI 的几个关键要素：交互，媒介，效率，信息。<br>
<br>
<strong><font color="#de5650">二、游戏过程中，什么时候你会注意到 UI 的存在？</font></strong><br>
<br>
关于这个问题，大家最多的回答便是：游戏 UI 做得特别差的时候。<br>
<br>
“（ 我什么时候会注意到 UI 的存在 ）另一种情况，就是 UI 特别差的时候。这会特别影响我的游戏体验。比如某游戏胜利画面的 Victory 字体极其难看，导致我最后删除了这个游戏。因为玩家和 UI 的互动非常频繁，如果出现 UI 动画不流畅、排版很差、字体不好看的情况，游戏体验势必会受到极大的影响。”（ 游戏概念美术 鱼丸 ）<br>
<br>
<div align="center">
<img aid="1030193" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094203qj8z038j40g483cp.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094203qj8z038j40g483cp.jpg" width="600" id="aimg_1030193" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094203qj8z038j40g483cp.jpg" referrerpolicy="no-referrer">
</div><br>
相比英文字体只需要考虑字母（ 大小写字母共 52 个 ）和数字符号，中文字体的常用字数量动辄上万。如此高昂的设计成本和工作量，导致好看的中文字体是如此缺乏。这成为了影响中文游戏 UI 设计的重要因素之一。图为可口可乐以中国早期老商标字体为灵感，专门设计的“可口可乐在乎体”。<br>
<br>
“UI 特别难用的情况下，我会注意到 UI 的存在。比如找不到目标信息。与之相比，好的 UI 体验往往是当玩家试图找到某个功能时，下意识便能找到目标界面。整个过程没有太多的刻意思考，是一个下意识的行为。”（ 游戏概念美术师 羊羊羊 ）<br>
<br>
“当我注意到 UI 的存在，往往是 UI 设计不好的时候。比如玩家界面的 UI 信息过载，玩家不知道应该把视觉焦点放在哪里。”（ 游戏制作人 Daniel ）<br>
<br>
“当 UI 设计非常糟糕的时候（ 我会注意到 UI 的存在 ）。比如在游戏 《 Cyberpunk 2077》中，各个功能相互之间叠加太多，设计师无法在一级二级界面的框架下把所有功能呈现出来。”（ 游戏设计师 空力使 ）<br>
<br>
可以看到，大家都倾向于看到 UI 在游戏中以一种不被人注意的方式，完成处理玩家输入和反馈信息的任务，即 “Good design is invisible”。当它无法保证玩家与游戏之间的交流，玩家处理游戏信息的成本过高，这样的 UI 势必令人诟病。无论是玩家无法找到目标界面，或者是信息呈现方式过于繁杂，这些情况都会打破玩家的沉浸感，让玩家的注意力从游戏本身，转移到如何解决 UI 问题上面。<br>
<br>
而关于好的游戏 UI：<br>
<br>
“玩家和虚拟世界的交互方式，如同一种语言。不同语言的人，肯定无法交流。但是如果使用同一种语言，这种交流便是可行的。UI 能很清晰地告诉玩家什么能做，什么不能做。如果没有 UI ，玩家可能无法以正确方式，或以设计师期望的方式和游戏交互。”（ 游戏设计师 Byonet ）<br>
<br>
“虽然诸如像《Last of Us Part 2》的游戏会弱化 UI，看似把 UI 隐藏了。但是这种设计实际是为了和 gameplay 融合，帮助玩家进入心流。等于弱化的 UI 也在这个过程中发挥了作用。”（ 游戏美术师 speedTurtle3.0 )<br>
<br>
<div align="center">
<img aid="1030194" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094203ia7xfsfyal5jczjx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094203ia7xfsfyal5jczjx.jpg" width="600" id="aimg_1030194" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094203ia7xfsfyal5jczjx.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《Last of Us Part 2》基本上是一个无 UI 界面</font></font></div><br>
不难发现，大家对于 UI 的部分期望，已经从“确保信息存在”，变成了“确保信息被需要时存在”。当玩家不需要查看特定信息的时候，UI 最好是隐藏或者是降低存在感。<br>
<br>
这也是现在常被提到的极简主义设计。在此我想做一点延申：我认为，这种风格的流行，不只是基于美术风格的需求，同时还和玩家与虚拟世界的认知演变有关。<br>
<br>
<div align="center">
<img aid="1030195" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094203d497965617v7amd1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094203d497965617v7amd1.jpg" width="600" id="aimg_1030195" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094203d497965617v7amd1.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Susan Kare 于 1984 年 3 月 14 日在电视转播中介绍如何使用 Apple Macintosh UI。从截图中可以看到她演示如何拖动文件图标，而简明易懂的回收站图标，位于桌面下方</font></font></div><br>
在人们最早接触虚拟世界（ 包括早期的操作系统 ）的时候，很多抽象信息对于大众都是全新的概念。这也许能部分解释为何早期的 UI 美术风格，都是倾向于拟物化设计。因为当我们试图用图标（ icon ) 代替文字来浓缩信息时，如果采用能让用户与现实产生直接联系的美术风格，就会降低用户的学习成本。所以早期的 UI 设计，很多内容对于新用户，都是简明易懂。比如回收站图标，便是一个垃圾桶造型。用户很容易理解回收站的用处。<br>
<br>
同时，早期 UI 设计倾向于将用户需要的信息尽可能都呈现出来，这样能确保用户可以找到所需信息。这种设计风格，经常出现在早年的 MMORPG 中。<br>
<br>
随着用户对于图形用户界面的熟悉，各个平台的交互方式对于个人不再陌生。此时 UI 设计开始强调效率和简洁。设计师开始追求高效率的信息传递和更为清晰的层级结构。<br>
<br>
游戏中，越来越多的场景式 UI 和极简式 UI 开始出现。两者的共同特点便是去 UI 化。实际上，它们本身依旧是 UI，去除的只是偏冗余的信息，或是隐藏信息。这些设计都是以用户拥有基本图形界面常识为基础。而这种简化行为，首先，不意味着视觉体验上的简单化。我注意到现在很多采用极简风格的 UI 设计，都是采用了“简单的图标 + 精美的动画”。用户接收到的视觉体验，并没有被简化。<br>
<br>
<div align="center">
<img aid="1030196" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094204di0mfff271qel3ic.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094204di0mfff271qel3ic.jpg" width="600" id="aimg_1030196" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094204di0mfff271qel3ic.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《In other waters》UI 设计可以说是当代游戏的一个典范</font></font></div><br>
其次，隐藏信息不等同于减少信息。被隐藏的信息会在玩家需要时显示。玩家不需要记住目标信息的具体位置，只需要知道在哪里能找到它们就行。这就好比我们为玩家提供了收纳盒。过去我们也许更注重收纳盒中装的内容，现在我们更注重玩家如何使用这个收纳盒。加上游戏本身的独特性（ 这一点会在下一篇文章中详说 ），这能解释当前我们定义一个好的游戏 UI 时，为何开始强调 UI 的弱存在感。<br>
<br>
<div align="center">
<img aid="1030197" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094204gttyw4pok7yopyp7.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094204gttyw4pok7yopyp7.jpg" width="600" id="aimg_1030197" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094204gttyw4pok7yopyp7.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">使用轮盘式 UI 的经验便是“平时不存在，用时即显现”</font></font></div><br>
<strong><font color="#de5650">三、能谈谈 UI 和 UX 之间的关系吗？</font></strong><br>
<br>
“UX 通过分析用户的需求来设计功能，即基于用户行为的系统。UI 是更偏视觉的反馈。”( 游戏技术美术 Magenta )<br>
<br>
“UI 是 UX 的一个子集。UX 讲的是用户的体验，UI 就是体验中偏表层的东西，即视觉上能被看到且互动的东西。UX 则强调底层逻辑，以保证很好的用户体验。这里面会包含 UX 的具体原则，比如如何引导用户，保证操作的效率。UI 就是整个体验的表层，如同一层外壳。实际开发过程中的 wireframe，就是 UX 设计完成后，UI 如何放置到这个框架中。”（ 游戏概念美术 鱼丸）<br>
<br>
“UX 是用户的一个体验，涉及到很多 UI 的叠加，是一个 flow。玩家需要在不同的 UI 之间转换。”（ 游戏主设计师 金潮 )<br>
<br>
<div align="center">
<img aid="1030198" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094205frwrxhaopwx7hoph.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094205frwrxhaopwx7hoph.jpg" width="600" id="aimg_1030198" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094205frwrxhaopwx7hoph.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">游戏《Durang：Wild Lands》 UX wireframe 设计</font></font></div><br>
“UI 更偏向美术，它有自己的艺术效果，整体设计跟游戏的风格相关。UX 可以脱离 UI，它关乎纯粹的玩家体验。就设计来说，UX 在这个过程中，更关注玩家如何以最直觉的方式来使用 UI。归纳起来，如果 UI 是游戏和玩家之间的交流媒介，UX 就是 UI 和玩家之间的交流媒介” （ 游戏设计师 Jonathan )<br>
<br>
一谈到 UI，我们都无法忽略用户体验（ User Experience，简称 UX ）。单独探讨 UI 设计对于游戏制作已没有太多意义。基于大家的讨论，我发现大家都倾向于用动态和静态两种维度来讨论 UX 与 UI 的关系。UX 侧重于一个完整的动态流程，基于底层的逻辑，以特定用户体验作为目标，并且它是一个主观的过程。而 UI 是 UX 具体实现的一种静态方式。它更像是 UX 过程中，特定状态的具体交互形式。我们可以发现，UX 和 UI 是如此紧密，在实际游戏开发过程中，我们愈发需要设计师同时具备两方面的能力。<br>
<br>
游戏设计师 Bigby 在谈论 UX 和 UI 时，提及的有一点让我非常感兴趣：<br>
<br>
<div align="center">
<img aid="1030199" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094205zsvcwk6vdc2jw0v0.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094205zsvcwk6vdc2jw0v0.jpg" width="600" id="aimg_1030199" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094205zsvcwk6vdc2jw0v0.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《This War of Min》的背包系统</font></font></div><br>
“UI 是游戏界面的统称，它不会具体包含用户交互的方法论。UX 更偏向底层的逻辑，主要探讨的是玩家使用 UI 时所经历的过程。<br>
<br>
但在实际开发过程中，很多时候是先有 UI 再有 UX 。大家会有一套固定的方法论，在此基础之上探讨相关的优化和改良。比如背包 UI 系统，常见的格子放置和自动排列功能，很多时候都是默认的设计。以此作为前提的条件下，设计师再从具体 UX 需求出发，进一步开发。这可能会造成设计师无法从设计本源出发去研究设计，创造出更有新意的 UI。”( 游戏设计师 Bigby )<br>
<br>
Bigby 所提到的现象，即设计师本应该以 UX 出发，针对实际需求设计 UI ，现实中却变成了先从 UI 实例出发，再在此基础上改进。这似乎有点本末倒置，不过我们可以从两个方面探讨这个现象。首先，我们不能忽略游戏 UI 在发展过程中，逐渐形成的设计准则。很多游戏工作室都有自己定义的 UI 设计书，其目的是确保 UI 设计规范化，统一化，高效化。这种方式已经在互联网 UI/UX 领域变得非常普遍。<br>
<br>
<div align="center">
<img aid="1030200" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094205ugaa424a9bm19i91.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094205ugaa424a9bm19i91.jpg" width="600" id="aimg_1030200" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094205ugaa424a9bm19i91.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">非常著名的 Apple human interace guideliens / 用户界面指南</font></font></div><br>
与之相对的，这种趋势会导致设计思路逐渐僵化，各类产品开始趋同。回到游戏领域，我们在设计游戏 UI 时，从已有实例出发并没有问题。但是设计师需要从 UX 需求出发，对已有实例进行验证，而不是直接采纳。不能“为了这口醋包了一顿饺子”。考虑到当前越来越多的游戏产品瞄准细分市场，打破当前设计准则，基于 UX 需求进行再创造，这种行为应该被鼓励。毕竟准则本身只是一个指南，并不是金科玉律。随着游戏平台环境的快速更新，以及玩家品味的多元化趋势，我相信基于相同的用户体验需求，我们可以提出更好的解决方案。不然我们无法解释这几年游戏作品中，出现的令人耳目一新的各种设计。<br>
<br>
<strong><font color="#de5650">四、对于游戏产品的 UI 和非游戏产品 UI（ 比如 APP ），您认为有什么异同吗?</font></strong><br>
<br>
其实在日常生活中，大家更容易在互联网产品中接触到 UI 。相比之下，这些 UI 和游戏 UI 存在怎样的异同呢？两者之间存在什么联系吗？<br>
<br>
“对于其他产品，用户很容易注意到 UI。UI 很容易抓住用户的注意力，因为所有信息都表现在这个界面上。而游戏 UI 不太容易被注意到。也许游戏内容本身的冲击感太强，因此可能会让玩家忽略游戏和 UI 的联系，而忘记 UI 本身也是游戏的一部分。我们本能会把游戏和 UI 放在对立面上：游戏是游戏，UI 是 UI。实际上，两者是需要统一去考量的。这在很多游戏策划的访谈中都有印证”（ 游戏美术师 speedTurtle3.0 )<br>
<br>
<div align="center">
<img aid="1030201" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094206qnc3nrhzuyi6ifj5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094206qnc3nrhzuyi6ifj5.jpg" width="600" id="aimg_1030201" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094206qnc3nrhzuyi6ifj5.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">UI 几乎构成了 APP 的所有部分</font></font></div><br>
“两者功能上区别不大。它们都为玩家和游戏设计师（ 抑或用户和产品设计师 ）提供一种交流方式。UI 是一种语言，帮助我们进行交流。所以从功能上来看，UI 需要非常清楚，无需说明（ self explanatory ）。但是二者的实现形式有很多区别。游戏 UI 都涉及到 gameplay，因此会更为简洁，不会影响到玩家玩游戏的过程，不能吸引玩家太多的注意力。非游戏产品类 UI 则更为突出，因为交互的单一性，更能吸引用户的注意力。最好的状态是 UI 被使用，但是没有被玩家意识到存在。”（ 游戏设计师 Byonet ）<br>
<br>
关于此问题，speedTurtle3.0 和 Byonet 都提到了一个关键词：存在。相比于互联网产品，UI 在游戏中，并不是支配般地存在。UI 的存在与否，会影响到玩家的注意力，从而对玩家的操作造成影响。这种影响可以是积极的，也可以是的消极的。<br>
<br>
值得注意的是，我们需要在设计过程中明确，让玩家忽略 UI 的存在，究竟是不是体验的目标（ 让玩家进入沉浸状态 ）。<br>
<br>
与此对应的，互联网产品 UI 非常讲究便捷和效率。这甚至影响了当前 UI 的视觉风格。对此，游戏设计师 Bigby 这样说道：<br>
<br>
“非游戏产品 UI 设计是以便捷为出发点，不会让玩家感到别扭，不会让信息获取出现偏差或者交互效率变低。游戏 UI 在某些情况下，会降低玩家获取信息的效率，达到服务于游戏玩法的目的。因为游戏 UI 是服务于游戏设计本身，而不是仅仅达成信息获取的便捷。比如游戏地图的信息获取，就不会像现实世界中那么方便。一个反例便是育碧开放世界中的问号设计，这种设计对于玩家的探索感具有毁灭性的打击，极大影响了游戏体验（尽管它做到了信息获取的便捷）。<br>
<br>
<div align="center">
<img aid="1030202" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094206t333djh6lonkj6mn.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094206t333djh6lonkj6mn.jpg" width="600" id="aimg_1030202" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094206t333djh6lonkj6mn.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">当所有任务都标注在地图上时，其实等于没有标注</font></font></div><br>
另一个反例便是敌人血量信息的显示。如果玩家能清晰地获取敌人的血量信息，那么玩家可能会忽略敌人的其他信息（ 比如敌人的行为、动画等等 ），只专注于血量数字。这会让战斗更像是一个数字游戏，玩家战斗体验可能变得单一。如果设计者尝试其他方式显示血量信息，比如 boss 的动画和音效，玩家可以据此推算 boss 的血量状况。在这个过程中，玩家可以建立一套认知。而建立的过程可以创造出更强的沉浸感。”（ 游戏设计师 Bigby ）<br>
<br>
<div align="center">
<img aid="1030203" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094206l1vakd6axupwjvyd.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094206l1vakd6axupwjvyd.jpg" width="600" id="aimg_1030203" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094206l1vakd6axupwjvyd.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">是否直接使用 UI 显示敌人的血量，会影响到玩家的战斗风格</font></font></div><br>
游戏设计师金潮则认为：<br>
<br>
“互联网产品注重实用性，简单实用，容易交互就好。而游戏是一个艺术品。游戏 UI 不只是关乎易读性和实用性，不能追求过度的简单。不然游戏会显得十分无聊。除非极简主义本身就是游戏追求的风格。很多游戏的 UI，其界面需要体现出游戏的风格，需要和当前的游戏场景很好地结合。因此游戏 UI 会比其他互联网产品复杂很多。” （ 游戏设计师 金潮 )<br>
<br>
两位设计师分别从玩法设计，和艺术效果，提到了游戏 UI 的“低效率”。这一点我非常赞同。很多游戏产品中，都或多或少存在玩家过于依赖游戏 UI 的情况。这种依赖有可能会让玩家的体验偏离了设计师的初衷。比如很多游戏中都使用了小地图 （ minimap ）的 UI 设计，它是一个显示游戏战斗信息的辅助工具，玩家可以从小地图上获取游戏的全局信息和其他战斗相关信息 。<br>
<br>
然而它的存在，有可能会让玩家将所有注意力放在小地图上。玩家只需要通过小地图完成定位和移动，当有目标信息出现时（ 比如敌人 ），玩家才会将视线转回到游戏实际画面当中。从玩家的角度来说，这样的战斗策略没有任何问题。但是从长期角度来说，这种战斗方式会忽略游戏中的其他信息。比如不管游戏地图如何变化，小地图信息几乎不会发生变化。最后的结果依旧是体验变得单一。<br>
<br>
需要明确的是，如果游戏的设计目标就是让玩家通过辅助 UI 完成操作，或者玩家极其需要小地图获取关卡的信息（ 比如多人对战游戏 ），那么上述小地图的案例分析便有失偏颇。现实的案例中，部分游戏会给小地图增加限制，最终的呈现形式便是两位设计师提到的“低效率”。<br>
<br>
<div align="center">
<img aid="1030204" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094207mgmwi0og0em0g9ig.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094207mgmwi0og0em0g9ig.jpg" width="600" id="aimg_1030204" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094207mgmwi0og0em0g9ig.jpg" referrerpolicy="no-referrer">
</div><br>
科幻电影中呈现的 UI 设计：UI 信息和现实物体绑定在一起，用户可以同时关注 UI 信息和现实信息<br>
<br>
另一方面，结合 AR 技术并采用 Diegetic UI ( 剧情 UI ）的设计形式，也许会是另一种有效的解决方案。因为篇幅限制，在此不多作分析。<br>
<br>
游戏概念美术鱼丸则提到了游戏 UI 和互联网 UI 共同发展的过程：<br>
<br>
“从一定程度上来说，尤其是在菜单设计方面，很多游戏 UI 都是走向趋同。本来很多传统游戏 UI 具有很强的文本主义，即游戏 UI 和游戏主题是一致的。<br>
<br>
<div align="center">
<img aid="1030205" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094208fuxoprwzkoi8rfbi.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094208fuxoprwzkoi8rfbi.jpg" width="600" id="aimg_1030205" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094208fuxoprwzkoi8rfbi.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">2010 年的 Windows Phone 7 采取了扁平化设计，对后来的产品产生了很大的影响</font></font></div><br>
以 BioWare 的游戏为例，《博德之门》的 UI 就是非常实物化，具有物理材质。为了契合奇幻的主题，UI 还会添加类似符文的镶边。但是在《龙腾世纪》 中，UI 变得特别简洁，渐渐趋向于现代软件的视觉风格。尽管当时苹果产品还在走实体化风格，但是 Windows 产品已经开始尝试扁平化的设计。<br>
<br>
毕竟在游戏中，玩家操作的不是实物。简洁化的设计，能让操作更有效率。在这方面，很多游戏都开始倾向扁平化，缺少文本主义。相比于过去实物化的风格，现在的设计更讲究效率优先。<br>
<br>
<div align="center">
<img aid="1030206" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094208vc6dtvyuegmeyd11.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094208vc6dtvyuegmeyd11.jpg" width="600" id="aimg_1030206" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094208vc6dtvyuegmeyd11.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《龙腾世纪：审判》扁平化的 UI 设计</font></font></div><br>
当然这个过程会有进一步的改变。比如手游的 UI，还是有文本主义的倾向。像游戏炉石最早也想尝试简洁的 UI，但是最后还是选择了略微复杂的写实风格。炉石 UX 设计师的一个想法是：玩家玩炉石时打开盒子，这个盒子就像是卡牌的收集盒一样。虽然这个逻辑和设计会很复杂，但是玩家有一个翻找的乐趣。<br>
<br>
另一方面，相比于非游戏产品，游戏包含一个玩的过程。某些游戏可能有大量的内容，这就需要 UI 去辅助游戏的玩法。比如魔幻类游戏中魔法的特效。这种情况下，特效也是 UI 的一部分。”（ 游戏概念美术 鱼丸 ）<br>
<br>
游戏概念美术羊羊羊则从世界观的角度分析了游戏 UI 和非游戏 UI 的异同：<br>
<br>
“（ 二者 ）某些方面差别会比较大。追求沉浸感的游戏中，UI 和游戏世界观融合比较好。UI 不会太多影响玩家的体验，或者说 UI 本身不会太吸引玩家的注意力。<br>
<br>
互联网产品则不会太注意这一点。比如游戏 UI 中，常见的武器子弹信息。如果是互联网产品，可能直接使用数字显示，而不是将子弹信息作为武器的一部分来显示。而现在很多游戏设计会尝试把游戏 UI ，整合到游戏的物件中。<br>
<br>
比如游戏《尼尔：机械纪元》，它的 UI 便和世界观整合在一起。UI 界面的特定功能，是需要玩家在游戏世界中找到特定物品才可以被实现。另外因为剧情需要，玩家在战斗过程中受伤后，UI 也会相应受到很大影响。整个界面可能处于一种崩溃的状态：画面会掉帧，清晰度会降低。这也是之前有玩家在玩《赛博朋克 2077 》的“黑梦”关卡时，遇到黑屏后，还会以为是游戏设计的原因。<br>
<br>
简言之，在这一类游戏中，UI 的任何行为都可以被游戏的世界观解释过去。因此 UI 的 bug 可能都会被玩家当作游戏的一部分。<br>
<br>
<div align="center">
<img aid="1030207" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094208jnbhhv15oh1if4w1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094208jnbhhv15oh1if4w1.jpg" width="600" id="aimg_1030207" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094208jnbhhv15oh1if4w1.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">从垃圾场爬出时可能遇见的黑屏，关卡名翻译为“黑梦”真是绝了</font></font></div><br>
另外，追求沉浸感的游戏，可能不会刻意把游戏功能呈现在玩家面前。比如《魔兽世界》和 《最终生还者 2》。前者会把有些游戏功能放在屏幕上，后者会尽量隐藏这些信息，当玩家需要的时候，再以某种交互触发，呈现出信息。比如游戏中的轮盘 UI。” （ 游戏概念美术 羊羊羊）<br>
<br>
<strong><font color="#de5650">五、在您的日常游戏开发中，会和 UI 打交道吗?</font></strong><br>
<br>
关于这个问题，尽管大家不是从事 UI 方面的工作，但是或多或少都会和 UI 打交道。<br>
<br>
“很多时候，我需要设计 gameplay 的功能。为了让玩家能够明白设计者的意图，正确理解功能的机制，我会给玩家提供 UI 的提示，以指引玩家的操作。在初期设计中，我们会做很多原型，设计师会添加很多临时 UI（ 我们称为 messaging ）。这时候 UI 只在意是否传递到信息，不在意信息的组织方式和呈现方式。当设计被验证过后，会进入正式的迭代。UI 设计师会完成临时 UI 的最终设计，确保当前设计能达到最好的效果。”（ 游戏设计师 Jonathan )<br>
<br>
“我会参与 UI 的优化，会涉及到 UI 的渲染优化，比如图集打包。每周也会看 UI 组的进度和成果” （ 游戏技术美术 Magenta )<br>
<br>
<div align="center">
<img aid="1030208" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094208gpednvnvtbntcndv.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094208gpednvnvtbntcndv.jpg" width="600" id="aimg_1030208" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094208gpednvnvtbntcndv.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">美术工具 UI 的任意一次改版，都可能直接影响到创作者的工作效率</font></font></div><br>
“游戏美术所使用的工具，都需要有很好的 UI 设计。日常工作中，我会频繁使用到这些工具。差的 UI/UX 设计会影响到我们的工作效率。因此 UI 和我们的日常太相关了。（ 我再次觉得 ）UI/UX 就应该是游戏本身。游戏应该是 UI/UX 框架之下，而不是 UI/UX 是游戏框架之下。” （ 游戏美术师 speedTurtle3.0 )<br>
<br>
<strong><font color="#de5650">六、您认为是否存在 UI 和玩法设计等同（ 或者存在很大交集 ）的情况?</font></strong><br>
<br>
既然大家都不断提到 UI 和玩法设计，我们是否可以重新定义 UI 和玩法的关系？作为非 UI 方向的游戏开发者，大家对此也各抒己见。<br>
<br>
首先游戏制作人 Daniel 认为二者关联很大：<br>
<br>
“非常大的交集。玩法设计、UI 设计，乃至游戏设计本身，相互之间都有很大的关系。它们都需要让玩家在体验的过程中，保持一个连贯性。<br>
<br>
比如开放世界游戏中，玩家任务状态和非任务状态下，玩家应该感受到二者都是同一个游戏。在 UI 方面，虽然 UI 在这个过程中可能会发生变化，但它都是游戏功能和感受的延伸。因此尽管表现形式有所不同，但站在玩家的角度，其整体感受可以是连贯的。UI 和游戏玩法要有统一性。比如开门，爬窗户，开大门，这些类似的场景，UI 都应该保持统一（ 或者相似 ）。” （ 游戏制作人 Daniel )<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1030209" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094209gaactpgbcqatlkaz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094209gaactpgbcqatlkaz.jpg" width="600" id="aimg_1030209" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094209gaactpgbcqatlkaz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">工具是人体的延伸</font></font></div><br>
我非常同意 UI 是游戏功能和感受的延伸，这就如同“工具是人的延伸”一样。玩家通过 UI 获取信息和完成操作，虽然是通过接口操作，但是等同于玩家身体的一部分，乃至感受的一部分。如果忽略这一点，玩家很难拥有连贯的游戏体验。<br>
<br>
而游戏设计师 Byonet 则认为两者差异很大：<br>
<br>
“游戏的核心依旧是关乎于设计。而 UI 是很好的工具，去把设计内容展示出来。<br>
<br>
游戏设计关注玩家怎么和虚拟世界交互，UI 是用比较通俗简单的方式告诉玩家如何和这个世界进行交互。因此 UI 不可能做得特别复杂，它本身更像是帮助玩家去完成交互。然而玩法设计的复杂度可以非常深，比如会涉及到学习曲线。然而 UI 则是无需说明（ self explanatory ）。<br>
<br>
但我觉得游戏玩法设计和 UI 设计需要同时进行。如果游戏的玩法设计特别复杂，如果没有好的 UI 辅助，玩家是无法理解的。比如 《 废土 2 》和《 废土3 》, 二者区别就很大。尽管本质都是非常复杂的 RPG 游戏，《 废土 2 》就更难上手。因为它的 UI 非常复杂。当然它的 UI 涵盖了游戏很多方面的信息，但是玩家无法有效地进入交互界面。这对于玩家是一件非常困惑的事情。<br>
<br>
<div align="center">
<img aid="1030210" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094209mbg8c2w55owmnwnw.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094209mbg8c2w55owmnwnw.jpg" width="600" id="aimg_1030210" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094209mbg8c2w55owmnwnw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《废土2》游戏 UI 截图：酒好也怕巷子深</font></font></div><br>
简单说，玩法设计可以特别深入，但是 UI 设计不能特别复杂。UI 本质上在教玩家如何和世界交互。《 全境封锁2 》 在我心目中，将 UI 做到了极致，玩家不需要从 cinematic 场景中获取信息，玩家直接和 UI 交互获取足够的信息。但是反过来，这似乎剥夺了玩家体会整个游戏世界的乐趣。” （ 游戏设计师 Byonet ）<br>
<br>
游戏设计师空力使则认为这需要具体情况具体分析：<br>
<br>
“这要看游戏的类型。比如游戏《 2048 》，这就是纯 UI 构建的游戏。UI 本身作为交互的一部分，尤其是在超休闲（ Hyper-casual ）游戏领域，UI 设计师有可能就是游戏设计师。<br>
<br>
那什么时候二者会分开呢？一般是确定核心玩法之后，如果设计师没有能力将所有信息传达给玩家的话，这就需要 UI 设计师整理这些信息，并呈现给玩家。总的来说，这个问题我觉得很难回答。因为这两者始终会存在交集。我很难想象一个 UI 完全不存在的游戏，任何游戏都有一定量的 UI 存在，和玩法之间都有不同程度的交集。” （ 游戏设计师 空力使 ）<br>
<br>
<div align="center">
<img aid="1030211" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094210w05kk5srnmkl4ksw.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094210w05kk5srnmkl4ksw.jpg" width="600" id="aimg_1030211" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094210w05kk5srnmkl4ksw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《Two Dots》就是纯 UI 构建游戏的典型例子</font></font></div><br>
小结一下，游戏 UI 和玩法存在交集是毋庸置疑的。如何让 UI 服务于游戏的体验目标，辅助玩法设计达成特定效果，这是每个游戏 UI 开发者需要思考的问题。而大家提及的游戏 UI “低效率” 现象，这是非常有趣且独特的角度。如果一味追求高效率和易用性，而忽略了“玩” 这个过程，这将使 UI 设计本末倒置。<br>
<br>
<strong><font color="#de5650">七、您经常在游戏中发现什么样的 UI 问题？</font></strong><br>
<br>
大部分被采访者都提到了一个现象：UI 学习成本过高。过高的学习成本会造成玩家无法快速完成游戏中的各个操作。每次玩游戏的间隔都会导致再次学习。<br>
<br>
游戏美术 speedTurtle3.0 提到：<br>
<br>
“很多看似设计非常绚丽的游戏 UI ，其实存在非常高的学习曲线。反而看起来平平无奇的设计，更容易让玩家上手操作。究其原因，是因为这类设计都遵循一定的设计规则。比如游戏中常见的背包系统或者存档方式。当然追求规则会导致UI 多样性的下降。不过站在玩家的角度，实用的操作体验更为重要。不妨少一些多样性，让玩家快速学习整个系统。” （ 游戏美术师 speedTurtle3.0 )<br>
<br>
<div align="center">
<img aid="1030212" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094210qgrjiohiosqiogxo.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094210qgrjiohiosqiogxo.jpg" width="600" id="aimg_1030212" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094210qgrjiohiosqiogxo.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">遗忘曲线永远是我们必须面对的敌人</font></font></div><br>
speedTurtle3.0 在后来的论述中，分别使用了 PUBG Mobile和《黑色行动4》（ Black Ops 4 ）作为正反例子：<br>
<br>
“我希望游戏 UI 设计和gameplay 设计一样，最基本的设计都是简单的规则，但是可以延伸出不同的子系统。哪怕游戏系统的复杂度偏高，但是玩家需要有一个基本的交互方式作为核心参考（ 如同沙盘游戏中的基本规则 ）。” （ 游戏美术师 speedTurtle3.0 )<br>
<br>
这种解释我个人非常同意。基本的规则如同语言中的词根，一旦玩家掌握了之后，哪怕遇见设计更为复杂的系统，玩家可以基于已有的设计语言，推导出目标信息。类似我们可以根据词根大致猜测生词的意思一样。<br>
<br>
游戏设计师金潮也有类似的观点：<br>
<br>
“ （ 常见的 UI 问题是 ）操作无法符合预期，玩家感到非常不顺手。每次操作都需要刻意学习。这往往是因为设计语言的混乱，缺乏统一性。好的UI 设计，学习成本应该非常低。玩家一旦学会了操作，就不需要额外的学习成本。<br>
<br>
另外信息层级的设计也经常出现问题。理想情况下，各个信息的层级位置需要基于信息的权重来决定。但在某些设计比较差的游戏中，一些基本的功能会被埋藏在比较深的层级中。玩家如果需要找寻一个东西（ 比如某菜单 ），需要经过几个层级才能找到。” （ 游戏设计师 金潮 )<br>
<br>
<div align="center">
<img aid="1030213" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094211dmh6hc205kc20ebt.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094211dmh6hc205kc20ebt.jpg" width="555" id="aimg_1030213" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094211dmh6hc205kc20ebt.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">iTunes 移动版本中的重复/随机播放按钮，就埋藏在子菜单中。很多用户对此抱怨。</font></font></div><br>
金潮也强调了统一的设计规则，对于玩家学习成本的降低起到了非常关键的作用。尽管特定游戏类型可能存在极高的复杂度，但这不是让玩家承受高昂学习成本的借口。从长远来看，当一个游戏产品形成了自己的设计规则，它就如同一个品牌，会被游戏玩家更为熟知。玩家的学习曲线也会不断下降。<br>
<br>
游戏设计师 Byonet 则说道：<br>
<br>
“UI 系统需要提供一种辅助工具，帮助玩家即使在长时间没有玩游戏的情况下，很快回忆起上次游戏的内容，从而知道自己接下来需要做什么。而很多游戏中，游戏没有提供有效的方式帮助玩家记录信息（比如游戏任务 ）。有些游戏的 log 并没有准确地记录信息，或者没有将重点信息记录下来。玩家需要从大段的文字中找到关键信息。” （ 游戏设计师 Byonet ）<br>
<br>
关于信息层级的内容，Byonet 还补充道：<br>
<br>
“这些信息的权重对于个体都有差异。以多人射击游戏为例，小地图在有些游戏中是在屏幕左上角。这个位置会让我的视野远离十字瞄准线（crosshair ）。相比之下，左下角和右下角的位置我会觉得更加合理。我会倾向于让所有的 UI 信息不要远离瞄准区域。再举一个例子，游戏中的武器信息对我没有那么重要。因为我在进入战局之前就选择了武器，这个信息对于我来说是已知的。相比之下，我更关注血条的位置。” （ 游戏设计师 Byonet ）<br>
<br>
<div align="center">
<img aid="1030214" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094211mzhrxbe556ezcbh5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094211mzhrxbe556ezcbh5.jpg" width="600" id="aimg_1030214" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094211mzhrxbe556ezcbh5.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">战地系列中的小地图，其水平线位置和瞄准十字的位置非常相近</font></font></div><br>
Byonet 的个人体验再次验证了前期调研的重要性。各种层级的权重是围绕玩家操作服务的，停留在字面上的理论必须经过玩家实际操作的验证。<br>
<br>
<strong><font color="#de5650">八、能列举几个您认为好的游戏 UI 或欠妥的游戏 UI 的例子吗？</font></strong><br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1030215" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094212cbzk7fgjgq77gfsj.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094212cbzk7fgjgq77gfsj.jpg" width="600" id="aimg_1030215" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094212cbzk7fgjgq77gfsj.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图中游戏的 UI 设计普遍被视为典范</font></font></div><br>
游戏概念设计师羊羊羊非常喜欢《守望先锋》（ Overwatch ）的 UI：<br>
<br>
“UI 层级关系十分清晰，没有太复杂的结构。另外我很喜欢《女神异闻录》（ Persona 5）的 UI，非常很风格化的设计，融合了都市街头的时尚感。尽管 UI 视觉非常风格化，但是不影响玩家使用。至于较差的游戏 UI，其中一个例子便是《圣歌》（ Anthem ）。由于层级非常复杂，游戏的很多功能无法被找到。而常用的功能并没有放置在非常明显的地方。玩家无法预判目标功能的位置。” （ 游戏概念美术羊羊羊 )<br>
<br>
游戏制作人 Daniel 更喜欢极简的游戏 UI：<br>
<br>
“我很喜欢《最后生还者第二章》（ Last of Us Part 2 ）简化的 UI 设计，我不需要花费太多精力，便能了解当前的操作（ 比如手持的是什么武器 ）我个人很讨厌满屏幕充满信息的游戏。另外在某些游戏中，设计师会加入装饰性 UI 元素，但它们不具备功能。这会让玩家非常困惑。《赛博朋克 2077》（ cyberpunk 2077 ）便存在这样的问题。” （ 游戏制作人 Daniel )<br>
<br>
<div align="center">
<img aid="1030216" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094212e6alqed3jqqlahql.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094212e6alqed3jqqlahql.jpg" width="600" id="aimg_1030216" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094212e6alqed3jqqlahql.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">关于装饰性元素的必要性，建筑界在上个世纪就已经有相关的讨论。图为上海的百老汇大厦。</font></font></div><br>
Bayonet 是这样评价好游戏 UI：<br>
<br>
“'好'是一个比较微妙的词。比如《全面封锁2》（The Division 2 ）。虽然各种 UI 功能被发挥到极致，但是不一定是一件好事。有时候好的游戏UI 更需要确保所有信息的清晰度，并准确传递给玩家。《战地》（ Battlefield ) 的 UI 就非常简洁，玩家很容易理解 UI 的内容。比如其图标都简单且准确，玩家可以凭借图标本身理解意思。相比之下，《彩虹六号》的一些图标释义就很模糊，玩家需要花费一定时间学习。<br>
<br>
<div align="center">
<img aid="1030217" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094212ixf6yt69fx4xf9st.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094212ixf6yt69fx4xf9st.jpg" width="600" id="aimg_1030217" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094212ixf6yt69fx4xf9st.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">你能快速告诉我，这个 UI 的哪些部分是可以和玩家交互？来自游戏《Observer System Redux》</font></font></div><br>
很多游戏为了加强代入感，把UI 做得非常绚丽。跟gameplay 无关的东西，也放在了UI 里面。玩家如果无法轻易判断出UI 的功能，他们会因为害怕操作失误而很难有勇气去上手。学习曲线非常高。<br>
<br>
UI的风格不一定要和游戏风格完全契合。能确保基本功能就已经达标了。如果UI 为了追求风格，可能会影响到 gameplay 本身。比如《战地》UI 字体的荧光效果，虽然很好还原了这种军事设备屏幕的效果，但是可读性非常差。” （ 游戏设计师Byonet )<br>
<br>
我对此的理解是，UI的存在感和形式感固然重要，但是如果没有很好融入到游戏本身，这样的UI 系统会显得冗余。也许UI 本身是很好的设计，但是放在游戏中，反而造成了负面的效果。<br>
<br>
<div align="center">
<img aid="1030218" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094212j8q2q7syaen887ix.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094212j8q2q7syaen887ix.jpg" width="600" id="aimg_1030218" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094212j8q2q7syaen887ix.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">来自于电视剧《包豪斯时代 第一季》</font></font></div><br>
关于这一点，不禁让我想到了“形式追随功能” ( Form follows function ) 的理念。它最早来自于19 世纪末期至20 世纪初期的建筑和工业设计领域。简单来说，就是产品的形式应该追随于功能本身，其形式应该基于功能的要求。这种设计哲学诞生于建筑界，由包豪斯发扬光大，最后直接影响了当今的互联网开发。虽然很多人会认为，按照这种理念，游戏UI 设计应该抛弃装饰性的内容。但实际上，如果装饰性内容符合UI 功能的需求，那么这也是成功的设计。<br>
<br>
另外被大家还提到的拥有优秀 UI 设计的游戏还包括：《死亡空间》（ Dead Space ）、《艾迪芬奇的记忆》( What Remains of Edith Finch )、《 Inside》、Supercell旗下的游戏和《半衰期：爱莉克斯》（ Half-Life: Alyx ）。<br>
<br>
<strong><font color="#de5650">九、您会用一个什么关键词来形容优秀的游戏 UI？</font></strong><br>
<br>
<div align="center">
<img aid="1030219" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094213ngjyqnn7qf77obqx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094213ngjyqnn7qf77obqx.jpg" width="600" id="aimg_1030219" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094213ngjyqnn7qf77obqx.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>流畅</strong><br>
<br>
“除了指动画视觉方面的流畅，还包括整个交互流程的流畅。比如玩家为找到特定的界面（语言选择界面）却遇到特定的困难，这就会影响流畅度。即玩家遇到了信息匮乏。之所以会出现这样的问题，是因为设计者过多熟悉这些信息，因此很难站在玩家的角度，去思考游戏信息能否有效传递给玩家。”（ 游戏概念美术 鱼丸 ）<br>
<br>
<strong>直觉</strong><br>
<br>
“这更多针对 UI 的交互过程，而不是呈现信息。交互应该在 UI 设计中占更大的比重。” （ 游戏设计师 Bigby ）<br>
<br>
“目标菜单处在它应该在（ 玩家认为在）的地方，任何操作都能符合直觉。” （ 游戏技术美术 Magenta )<br>
<br>
“新手不需要经过太多指导完成操作。当玩家熟练掌握之后，UI 的常规操作不会过于繁琐。”（ 游戏设计师 空力使 ）<br>
<br>
<strong>简洁</strong><br>
<br>
“比如 Supercell的游戏，UI 非常干净但又很鲜艳，符合游戏的主题。整体有很强的gaming 的感觉。使用起来很顺手，但是整个过程都很有乐趣。” （ 游戏设计师 金潮 )<br>
<br>
<strong>觉察不到</strong><br>
<br>
“平时意识不到 UI 的存在，但是想要查看信息的时候，可以轻易看到。( 游戏设计师 Bayonet ）<br>
<br>
<strong>高效</strong><br>
<br>
“UI 是让玩家能和游戏交互的功能集合。玩家需要能够通过 UI 快速完成操作。不需要 UI 的时候，UI的存在不影响游戏体验。” ( 游戏设计师空力使 ）<br>
<br>
<strong><font color="#de5650">十、您还有什么想要分享的吗？</font></strong><br>
<br>
最后我想分享一下游戏设计师金潮的补充内容。当我们谈论到创新和现实的冲突时，她是这样思考的：<br>
<br>
“不同的UI/UX 设计师在同一个项目工作时，大家都会想做出新的东西。这种创作冲动很容易被理解，但是创新的成果不一定见效。之所以会这样，其一是团队可能缺乏统一的设计语言，没有提前设定好的设计准则。在这种情况下，团队成员的创新，更容易带着个人的标签。最后导致不同的设计风格同时出现，产品的统一性遭到破坏。其二是很多我们习以为常的设计，很可能经过了无数次验证。我们所设想的创新方案，甚至早已被尝试过。这就是为什么对于经常更新的游戏UI ，最好的版本往往是最初的版本。” （ 游戏设计师 金潮 ）<br>
<br>
<div align="center">
<img aid="1030220" zoomfile="https://di.gameres.com/attachment/forum/202202/09/094213vz80vb3u7w0jjm3m.jpg" data-original="https://di.gameres.com/attachment/forum/202202/09/094213vz80vb3u7w0jjm3m.jpg" width="600" id="aimg_1030220" inpost="1" src="https://di.gameres.com/attachment/forum/202202/09/094213vz80vb3u7w0jjm3m.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">在此向大家推荐书籍《The design of everyday things》，你会发现日常生活中平平无奇的事物，其实包含了很多设计的结晶</font></font></div><br>
我觉得归根到一点，创造者不能为了创造而创造。这个过程中，我们时常注重于“怎么创新”（ How ），而不是“为何要创新” （ Why ）。其实回头看看很多创新设计，本质上它们都是在解决设计上的问题。<br>
<br>
<strong><font color="#de5650">最后</font></strong><br>
<br>
在此再次感谢金潮, Bigby, Byonet，Daniel, Magenta, Jonathan,speedTurtle3.0, 空力使，鱼丸，羊羊羊 在百忙之中抽出时间，参与讨论和回答问题。<br>
<br>
本人公众号”六十和二四的世界“，除了分享游戏随笔，同时涉及电影话题。各位若有兴趣，进来坐坐。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：六十和二四的世界</font></font><br>
<br>
  
</div>
            