
---
title: """""""""""'以虚幻GAS系统为核心的《原子之心》'"""""""""""
categories: 
    - 游戏
    - GameRes 游资网 - 列表
author: GameRes 游资网 - 列表
comments: false
date: Mon, 01 Feb 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202102/01/152115blapc0w202awha0a.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2484018">
Andrey Dyakov是即将上市的游戏《原子之心》的开发商Mundfish的技术总监。他拥有10多年的游戏开发经验，在一些知名工作室参与制作过使用虚幻引擎3和虚幻引擎4的3A游戏。<br>
<br>
大家好，我叫Andrey Dyakov，是即将上市的游戏《原子之心（Atomic Heart）》的开发商Mundfish的技术总监。这篇技术博客将讲解一些我们用于开发这一作品的技术，重点讲述我们如何利用虚幻的Gameplay Ability System（GAS）?改变我们的开发流程。<br>
<br>
本文并非手册，只是详细介绍了我们的经验。尽管如此，它还是能够帮助可能已经很熟悉GAS而且在其项目中使用过它的开发者。<br>
<br>
如今外面已经有更多关于GAS的信息了，但我们想要介绍的是，我们在当初关于这个系统的文档和支持还不是很多的时候所作的一些研究。<br>
<br>
那是在2018年，我们有自己的行动过滤器系统，用来区分玩家的行动和定义它们的执行规则，我们总体上对它很满意。它让我们能够控制在玩家进行其他行动时能否开始特定玩家行动或者禁止其开始（例如在蹲下时跳跃）。<br>
<br>
但它只是我们需要的众多子系统之一。对我们来说，还需要解决其他关键开发问题，例如：<br>
<br>
<ul><li>如何处理充能近战武器和远程武器的子弹所发出的酸液、电流和火焰造成的特殊伤害</li><li>如何堆叠和处理施加于一个角色的不同类型伤害</li><li>如何实现玩家角色的特殊能力，以及如何控制它们的执行流</li><li>最后，在我们最终决定将《原子之心》做成单机游戏前，还考虑过如何处理联机复制<br>
</li></ul><br>
有一个系统具备了解决所有这些问题的潜力：虚幻的Gameplay Ability System。我曾经用它准备了一个小型示例项目，用于我在一家外包公司给60个人讲授了几个星期的UE4开发课程。不过，在一个小型教学项目上试用当时还处于试验阶段的系统是一回事，把它应用于一个雄心勃勃的大型商业项目又是另一回事。<br>
<br>
团队最初有许多顾虑，这是完全可以理解的。那时候，Epic为GAS提供的支持很有限。你可能知道，这个插件是Epic终止了它的《虚幻争霸（Paragon）》项目之后放出的，最初它是那个游戏的重要组成部分。但是我把这个事实视作当时GAS已经接近产品级要求的证明，我相信我们的团队能够应对填补差距的挑战。幸运的是，我猜对了。<br>
<br>
<div align="center">
<img id="aimg_957815" aid="957815" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152115blapc0w202awha0a.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152115blapc0w202awha0a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152115blapc0w202awha0a.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">GAS插件在描述中带有[UNSUPPORTED]标记</font></font></div><br>
当时是虚幻引擎4.20发行前后，互联网上除了社区的热心人写的几篇文章，没有多少关于GAS的文档。我们就这样开始了自己的研究。团队检查了这个插件的每一行代码，在头脑风暴讨论会中交流了它的各种优点和缺点。<br>
<br>
最终我们确定，GAS的许多功能如果集成到我们的游戏中，是绝对有利的：<br>
<br>
<ul><li>一切都可以通过游戏性标记?（层级标记）来控制</li><li>所有的行动/技能都可以作为能力来开发</li><li>能力可以绑定到玩家的输入</li><li>所有的效果（加强/削弱）都是一起堆叠和计算的</li><li>任何视觉效果反馈都可以通过游戏性提示?来管理<br>
</li></ul><br>
与此同时，缺点也很明显：系统很复杂，而且缺乏官方的文档与支持。GAS是一套复杂的系统，使用方法因公司、因项目而异。我们也花了一点时间才确定我们自己使用这个系统的最佳实践。<br>
<br>
在集成过程中，我们检查了用于计划目标的所有基本机制，全都做得非常好。此时我们也明白了，GAS可以完全取代我们的行动过滤器系统，因为它有相似却更好的机制来控制能力执行。我们完成系统过渡之后，就开始把所有玩家行为迁移到独立的能力，这使我们的AHBaseCharacter和AHPlayerCharacter类（是的，我们的类都带有AH前缀）大大简化了。<br>
<br>
这样一来，我们就能创建许多能力，而不需要设计我们自己的能力系统的架构。这真的大大节省了时间。不过，我们添加的能力越多，游戏性互连/依赖性就越复杂。<br>
<br>
公正地说，我们在使用GAS的早期遇到了一些挑战，但这些问题与开发和实现我们自己的系统不能相提并论。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_957816" aid="957816" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152115p1vhoohshyy1r11r.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152115p1vhoohshyy1r11r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152115p1vhoohshyy1r11r.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">我们的一次头脑风暴讨论会</font></font></div><br>
在我们找到能力和效果设置的最佳公式后，一切就尽在掌握了。<br>
<br>
最终，我们遵照这种新的思路，开始将AI角色的行动迁移到它们各自的能力。这简化了我们的行为树?，使我们能够更灵活地使用我们数据驱动的AI管线设置角色。现在就来详细说说我们的一些GAS实践。<br>
<br>
有些人可能还不熟悉这个系统，在一般的GAS管线中，主要有四种类：能力系统组件附属于所有者，属性集被定义为所有者的属性，游戏性效果可以应用于能力系统组件的所有者并修改属性集中定义的属性，最后是能力，也就是由游戏性标记和效果控制的行动。还有一些可选的类，例如游戏性任务（它是能力的子对象）和游戏性提示（它帮助提供来自游戏性效果的视觉反馈）。<br>
<br>
<strong><font color="#de5650">游戏性标记管理着所有这些</font></strong><br>
<br>
所以，首先应该详细说说游戏性标记。这个子系统被添加到UE4的时间还要早于GAS。通过它可以定义和使用层级标记（标签），后者可以应用到对象并用于许多不同的用途，例如区分不同类型的伤害。<br>
<br>
<div align="center">
<img id="aimg_957817" aid="957817" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152116d65oon6hh6i6oo6h.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152116d65oon6hh6i6oo6h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152116d65oon6hh6i6oo6h.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">这张图显示了我们常用的游戏性标记类别</font></font></div><br>
在我们的游戏中，严密组织游戏性标记的层级是非常重要的。每一种能力都有其自身的能力标记（能力子树）和自身的禁止标记（禁止子树）。<br>
<br>
把所有东西都组织起来有助于保持控制，可以在整个项目中始终以相同的方法来使用能力。<br>
<br>
<div align="center">
<img id="aimg_957818" aid="957818" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152116i2qvh96zq2g2d9xu.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152116i2qvh96zq2g2d9xu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152116i2qvh96zq2g2d9xu.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">用于基本角色能力的游戏性标记</font></font></div><br>
<strong><font color="#de5650">禁止效果</font></strong><br>
<br>
在集成之初做出的一个决定帮助了我们替换行动过滤器，那就是使用禁止效果。这些效果可以由能力添加到角色，也可以直接来自其他地方。它们的唯一用途就是授予阻止能力激活的标记。<br>
<br>
RestoreStamina能力就是一例。它始终是一个应用RestoreStamina游戏性效果的主动能力。这是一种无限期的效果。它的主要用途是每500毫秒向玩家角色的AttributeSet（一种特殊的类，指定GAS组件所有者的所有属性都需要它）中定义的耐力属性添加一个恒定的浮点值，从而恢复玩家角色的耐力。如果有任何其他能力向效果GE_RestoreStamina授予禁止标记“Prohibitions.RestoreStamina”，那么该效果就会停止，因为在它的资源设置中就是这样定义的（参见下面的截屏）。<br>
<br>
<div align="center">
<img id="aimg_957819" aid="957819" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152117vnlr9rnnj1kqtrzj.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152117vnlr9rnnj1kqtrzj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152117vnlr9rnnj1kqtrzj.jpg" referrerpolicy="no-referrer">
</div><br>
我们游戏中的大部分能力在应用了禁止该能力的禁止标记时都不会激活。在《原子之心》这样的游戏中，玩家拥有50多种能力，有时候情况会非常复杂。<br>
<br>
<strong><font color="#de5650">费用效果</font></strong><br>
<br>
在介绍我们调试基于标记的能力执行规则/先决条件的方法之前，我要再分享一条关于费用效果的最佳实践。如果你必须在执行某种能力时消耗某些资源，就需要这种效果，当然了，如果对能力指定了这样的效果，在应用前就会相应地检查。例如，在我们的游戏中，有一个用于近身超重攻击的能力会即时消耗耐力。如果玩家角色耗尽了耐力，就无法执行这个能力。但如果他有足够的耐力，就可以执行这个能力，而且将会按照费用效果中指定的数值扣减耐力。<br>
<br>
<div align="center">
<img id="aimg_957820" aid="957820" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152117zfvp0m30qwpspqfm.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152117zfvp0m30qwpspqfm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152117zfvp0m30qwpspqfm.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">我们自己的调试工具</font></strong><br>
<br>
在使用GAS进行开发的过程中，很容易积累许多能力、效果、标记和游戏性提示。所以当我们添加新能力时，就必须把这一切都考虑在内。否则就很容易“在能力中卡死”，我们用这个术语来形容当前处于活动状态的一种能力阻止了许多其他能力，导致使玩家事实上什么都做不了的情况。为了解决这种问题，我们创建了一种非常简单、但又能提供有用信息的调试消息，它会显示在视口中。它说明当前在玩家角色上应用的标记和效果。对于AI，我们也设计了在AI角色的位置显示的窗口控件，其中包含同样的信息，而且还有相应的AI角色能力。<br>
<br>
<div align="center">
<img id="aimg_957821" aid="957821" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152118o3y90ymmjyoy40dq.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152118o3y90ymmjyoy40dq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152118o3y90ymmjyoy40dq.jpg" referrerpolicy="no-referrer">
</div><br>
使用这种信息，就可以轻松了解哪些标记/效果应该是活动的，哪些不是。所以大多数情况下，可以通过在编辑器中的游戏性能力资源中添加数据修正的形式来轻松解决问题。<br>
<br>
<div align="center">
<img id="aimg_957822" aid="957822" zoomfile="https://di.gameres.com/attachment/forum/202102/01/152119d2rio9vwvzcsncih.jpg" data-original="https://di.gameres.com/attachment/forum/202102/01/152119d2rio9vwvzcsncih.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/01/152119d2rio9vwvzcsncih.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">乍一看，这显得很混乱，但每个窗口控件都是可以折叠的，而且鼠标移到上面就会高亮显示。</font></font></div><br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
Gameplay Ability System推出后，过了一段时间才通过官方项目示例和直播再次获得支持。如今有越来越多的开发者将这种系统集成到他们的项目中，并在社区中分享他们的知识。<br>
<br>
我们团队非常高兴能获得如此强大而出色的工具来帮助执行日常工作，希望我们在这篇博客中描述的经验能够帮助或启发其他开发者。<br>
<br>
我们还要特别感谢JetBrains为我们提供了在开发中全程帮助我们的工具。<br>
<br>
如果你有兴趣更多地了解我们的工作进展，请在Twitter和Facebook上关注我们，并把《原子之心》添加到你的Steam愿望单！<br>
<br>
<strong><font color="#de5650">文中提及的相关链接</font></strong><br>
<br>
<i><font color="#808080">[1] Gameplay Ability System（GAS）<br>
https://docs.unrealengine.com/zh-CN/InteractiveExperiences/GameplayAbilitySystem/index.html<br>
<br>
[2] 游戏性标记<br>
https://docs.unrealengine.com/zh-CN/ProgrammingAndScripting/Tags/index.html<br>
<br>
[3] 游戏性提示<br>
https://docs.unrealengine.com/en-US/BlueprintAPI/Ability/GameplayCue/index.html<br>
<br>
[4] 行为树<br>
https://docs.unrealengine.com/zh-CN/InteractiveExperiences/ArtificialIntelligence/BehaviorTrees/index.html</font></i><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：虚幻引擎</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/fKoo5ns0EFeEsqbl6FnNXg</font></font><br>
</td></tr></tbody></table>



  
</div>
            