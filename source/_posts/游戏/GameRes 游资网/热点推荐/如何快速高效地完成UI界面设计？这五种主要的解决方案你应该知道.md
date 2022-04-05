
---
title: '如何快速高效地完成UI界面设计？这五种主要的解决方案你应该知道'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/25/091638ustkheksz8huwrst.png'
author: GameRes 游资网
comments: false
date: Fri, 25 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/25/091638ustkheksz8huwrst.png'
---

<div>   
<i><font color="#808080">本文首发“腾讯GWB游戏无界”</font></i><br>
<i><font color="#808080">作者：W</font></i><br>
<br>
在游戏制作时，UI界面设计是非常重要的工作，不仅仅是考虑排版布局、美术风格，还要考虑到玩家的交互行为。另外，采取哪种实现方案也是需要慎重考虑的，一个好方案让我们在保质保量的前提下，能快速高效地完成。笔者将为大家介绍业界常用的UI解决方案，并对它们做简单地分析对比。同时，也欢迎大家留言，分享你在UI设计时所积累的经验，或是遇到的困难，咱们共同成长进步。<br>
<br>
<strong><font color="#de5650">一、UI方案选择时参考点有哪些</font></strong><br>
<br>
笔者自14年毕业参加工作以来，一直使用Unity引擎来开发各种项目，如儿童启蒙教育类绘本、大型3D网络海战、三消、视频VR以及NBA体育竞技等，大部分工作内容是与UI界面相关。使用过的UI系统插件包括Unity原始的GUI、第3方插件NGUI、Unity进阶版的UGUI以及第3方的UI编辑器FairyGUI。另外，经网上了解还有EZ GUI、IGUI等第3方插件，以及Unity近推出的高阶版UIToolkit。这些偏冷门的或者新出炉的，笔者暂没在公司项目中使用过。你知道的，公司项目对稳定性有较高的要求，不会一味地追求新技术。读者不用惊讶，有公司还在使用Unity 4.x或者5.x旧版本的呢，哈哈！<br>
<br>
经前面介绍，这么多种实现方案，我们在实际项目中应该如何做选择呢？有木有最佳方案？通吃的那种？答案是否定的。每种方案都有其适用性，需要结合项目本身以及开发者自身情况综合来考量。那在选择方案时，有木有一些具体的参考点呢？这个是有的，笔者归结为以下2点：<br>
<br>
1）可视化程度：Unity原始的UI系统，需要在运行时才能显示，这给我们搭建UI界面时带来很多不便。正因为此，许多像NGUI一样的高度可视化的插件陆续诞生。搭建UI界面时，只需将对应组件拖入场景即可显示和调整，达到所见即所得的目的。另外，像是否支持图文混排、虚拟列表等组件以及对策划美术是否友好等问题，也都可以归结为插件的可视化程度高不高的体现。<br>
<br>
2）性能：DrawCall，每次CPU准备数据并通知GPU的过程。这个操作是比较好性能的，原则上我们是希望它越少越好的。影响它的因素：一方面表现为UI资源的管理方式，这主要与程序猿技术能力有关，知道啥时候加载，又啥时候卸载，什么类型资源共享，什么类型资源进行九宫格。另一方面表现为与UI系统本身的渲染原理相关，这是UI方案的“硬伤”，关于UI方案的硬伤，对于熟知该UI渲染原理的程序猿来说，他知道该怎么去做，一定程度“规避”产生太多DrawCall。嘻嘻，这很考验咱程序猿功底咯！如果UI方案本身这方面就做的很好，那岂不是更好，哈哈。<br>
<br>
<strong><font color="#de5650">二、常用UI方案介绍</font></strong><br>
<br>
限于篇幅，我不能对这些UI方案深入展开，希望简短的介绍能讲清楚它们各自特点。至于具体怎么使用，我会附上官网或学习地址，那里通常配有技术文档、教程帮助上手。<br>
<br>
<strong>2.1 Unity原始GUI</strong><br>
<br>
因性能和可视化方面都不足，自打好用的如NGUI等第3方插件问世后，Unity的原始GUI系统，基本不会用于游戏运行模式时的UI设计中；一般只是在编辑器工具扩展时使用。但现如今Unity又推出新的UIElement框架，可用于编辑器工具的扩展，原生GUI系统会越来越失宠，究其最终原因就是性能差且不好用。目前来看，原始GUI在编辑器工具扩展领域的地位应该不太可能迅速被UIElement取代，因为扩展工具时，原始GUI还是可以胜任的，且很多开发者应该已经习惯用它来编写工具和扩展。其实，程序猿也是有情怀的，哈哈！<br>
<br>
<div align="center">
<img aid="1034630" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091638ustkheksz8huwrst.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091638ustkheksz8huwrst.png" width="600" id="aimg_1034630" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091638ustkheksz8huwrst.png" referrerpolicy="no-referrer">
</div><br>
<strong>2.2 NGUI</strong><br>
<br>
资源地址：<br>
<br>
https://assetstore.unity.com/packages/tools/gui/ngui-next-gen-ui-2413#description<br>
<br>
其特点如下：<br>
<br>
图集：需要自己规划好后，手动打图集。<br>
<br>
渲染原理：先根据Panel的Depth排序，Panel面板内部再根据Depth排序。将相同材质的Widget进行Mesh合并。<br>
<br>
支持图文混排。<br>
<br>
支持循环列表组件。<br>
<br>
<div align="center">
<img aid="1034631" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091641wp1o4plio1pp41g1.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091641wp1o4plio1pp41g1.png" width="600" id="aimg_1034631" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091641wp1o4plio1pp41g1.png" referrerpolicy="no-referrer">
</div><br>
<strong>2.3 Unity进阶版UGUI</strong><br>
<br>
学习地址：<br>
<br>
http://c.biancheng.net/view/2712.html<br>
<br>
UGUI是在NGUI之后Unity官方推出的，一定程度上借鉴了NGUI的设计理念，在某些方面做了改进优化，如自适应、图集等。其特点如下：<br>
<br>
图集：图集概念不重，会自动打包成图集。要注意的是，放在Resources文件夹下的贴图不会被打入图集；<br>
<br>
渲染原理：根据Hierarchy的顺序来排序，越下面渲染在越顶层。Canvas与NGUI的UIPanel类似，每个Canvas将优化合并为1个Mesh或多个SubMesh；<br>
<br>
不支持图文混排，需要自己实现；<br>
<br>
不支持循环列表组件，需要自己实现；<br>
<br>
有锚点，方便屏幕自适应。<br>
<br>
<div align="center">
<img aid="1034632" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091642mfub5ebt77htttf7.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091642mfub5ebt77htttf7.png" width="600" id="aimg_1034632" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091642mfub5ebt77htttf7.png" referrerpolicy="no-referrer">
</div><br>
<strong>2.4 FairyGUI</strong><br>
<br>
官网地址：<br>
<br>
https://www.fairygui.com/download<br>
<br>
它是独立的UI编辑器，且对美术、策划都友好。其特点如下：<br>
<br>
目前主流的游戏开发引擎都支持；<br>
<br>
渲染原理：没有采取Mesh合并的策略，而是基于类似于Unity的Dynamic Batching技术，对DrawCall进行优化。它在不改变显示效果的前提下，尽可能的把相同材质的物体调整到连续的RenderingOrder值上，以促使它们能够被Unity DynamicBatching优化；<br>
<br>
支持图文混排；<br>
<br>
支持虚拟列表，即使数量巨大的列表也不会感觉太卡顿。<br>
<br>
<div align="center">
<img aid="1034633" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091642pqpojipue5bipnov.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091642pqpojipue5bipnov.png" width="600" id="aimg_1034633" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091642pqpojipue5bipnov.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1034634" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091643y4tmfuttutttv7zu.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091643y4tmfuttutttv7zu.png" width="600" id="aimg_1034634" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091643y4tmfuttutttv7zu.png" referrerpolicy="no-referrer">
</div><br>
<strong>2.5 其他方案</strong><br>
<br>
因为笔者未在实际项目中使用过，所以这里不做评述了，读者可以根据贴出的链接跳转过去瞅一瞅哈！<br>
<br>
<strong>1）Unity高阶版UIToolkit</strong><br>
<br>
学习地址：<br>
<br>
https://docs.unity3d.com/cn/2020.1/Manual/UIElements.html<br>
<br>
是Unity新推出的新一代UI系统，既支持游戏编辑模式也支持运行时模式。但目前还不够完善。读者可以尝尝鲜，试用一下。<br>
<br>
<div align="center">
<img aid="1034635" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091643cnw04i1468gfqo7g.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091643cnw04i1468gfqo7g.png" width="591" id="aimg_1034635" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091643cnw04i1468gfqo7g.png" referrerpolicy="no-referrer">
</div><br>
<strong>2）EZGUI</strong><br>
<br>
资源地址：<br>
<br>
https://assetstore.unity.com/packages/tools/ez-gui-32<br>
<br>
【注：官方资源下架 已购买可以继续使用】<br>
<br>
<div align="center">
<img aid="1034636" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091644j44eq8ep8h30pw4x.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091644j44eq8ep8h30pw4x.png" width="600" id="aimg_1034636" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091644j44eq8ep8h30pw4x.png" referrerpolicy="no-referrer">
</div><br>
<strong>3）IGUI</strong><br>
<br>
资源地址：<br>
<br>
https://assetstore.unity.com/packages/tools/gui/igui-basic-1946<br>
<br>
【注：官方资源下架 已购买可以继续使用】<br>
<br>
<div align="center">
<img aid="1034637" zoomfile="https://di.gameres.com/attachment/forum/202203/25/091644k91ivjq0iurwwsvw.png" data-original="https://di.gameres.com/attachment/forum/202203/25/091644k91ivjq0iurwwsvw.png" width="600" id="aimg_1034637" inpost="1" src="https://di.gameres.com/attachment/forum/202203/25/091644k91ivjq0iurwwsvw.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">结语</font></strong><br>
<br>
本篇主要介绍了Unity项目比较流行的UI解决方案，笔者在这里只是做一个汇总概述，并没有去深究。至于读者该如何选择，仁者见仁，智者见智。一句话总结：没有最好的，只有最适合的！<br>
<br>
<font size="2"><font color="#808080"><strong>参考资料</strong></font></font><br>
<font size="2"><font color="#808080">1、Unity官网：https://unity.cn/</font></font><br>
<font size="2"><font color="#808080">2、Siki学院：</font></font><br>
<font size="2"><font color="#808080">http://www.sikiedu.com/course/explore/unity?subCategory=&selectedthirdLevelCategory=&filter%5Btype%5D=all&filter%5Bprice%5D=all&filter%5BcurrentLevelId%5D=all&orderBy=hotSeq&from_flag=baidu_unity</font></font><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：腾讯GWB游戏无界</font></font><br>
<br>
  
</div>
            