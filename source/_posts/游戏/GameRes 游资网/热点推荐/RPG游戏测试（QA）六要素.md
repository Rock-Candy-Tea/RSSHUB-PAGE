
---
title: 'RPG游戏测试（QA）六要素'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202103/23/132220w1s6g44h9p6ne9of.jpg'
author: GameRes 游资网
comments: false
date: Tue, 23 Mar 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202103/23/132220w1s6g44h9p6ne9of.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2490047">
无论是什么类型的游戏，都需要数月的测试来确保其成功发行，角色扮演游戏（RPG）尤其需要完善的测试。<br>
<br>
<div align="center">
<img id="aimg_967365" aid="967365" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132220w1s6g44h9p6ne9of.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132220w1s6g44h9p6ne9of.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132220w1s6g44h9p6ne9of.jpg" referrerpolicy="no-referrer">
</div><br>
RPG游戏通常会让玩家控制一个核心人物，在魔法或科幻世界中探索。游戏中包含了深度定制的功能，上千的道具，和一个无尽的开放世界。应对RPG的这些特点，游戏测试（QA）团队的任务艰巨，如果游戏是大型多人线上（MMO）RPG，挑战更是成数量级地增加了。<br>
<br>
由于需要测试的元素众多，RPG游戏要求探索性的及计划性的测试。<br>
<br>
<strong><font color="#de5650">1、游戏世界</font></strong><br>
<br>
RPG通常拥有某种形式的开放世界，或完全开放，或中心式，大大增加了需要测试的内容。<br>
<br>
这些开放世界需要大量的测试人员频繁且规律地检查物理碰撞、贴图、光照和渲染的问题。这不是最后时刻进行的突击检查或阶段性的测试，它需要一个长期的过程来保证开放世界没有漏洞。<br>
<br>
这些漏洞会藏匿在任何地方，每一个没被查出来的漏洞都会被玩家发现。<br>
<br>
<div align="center">
<img id="aimg_967366" aid="967366" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132220gsyi2br702g92beg.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132220gsyi2br702g92beg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132220gsyi2br702g92beg.jpg" referrerpolicy="no-referrer">
</div><br>
贴图，渲染和光照问题就属于最糟糕的漏洞，它们非常明显，很容易暴露给玩家，而且再现和录制起来也特别容易。幸运的是这些问题不会被恶意利用，除了一些特定的情况外，它们也不会影响玩家继续下面的游戏。<br>
<br>
物理碰撞问题可能是最令人懊恼的，而且容易被恶意利用。例如，玩家能穿过建筑墙壁，导致任务的脚本崩溃。想象一下在一个有着上千建筑的大型开放式世界中测试这个问题！<br>
<br>
这些建筑会影响游戏的性能——这也是开放世界RPG会出现特定问题的地方。玩家期待/要求游戏必须能顺畅运行。要让开放世界始终保持高性能的运行，需要对RPG游戏的每个要素进行仔细的测试，然后再在整体的游戏世界中再进行测试。<br>
<br>
<strong><font color="#de5650">2、道具</font></strong><br>
<br>
在RPG游戏中一般都有个长长的道具列表，涵盖了从药剂到宠物的所有物品。对QA团队来说，这会产生一大堆细微且枯燥的检查。<br>
<br>
<div align="center">
<img id="aimg_967367" aid="967367" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132220cf6rhurky6ysffur.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132220cf6rhurky6ysffur.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132220cf6rhurky6ysffur.jpg" referrerpolicy="no-referrer">
</div><br>
为了保证道具的正常运作，要对每一个道具的效果和功能进行人工或自动化的测试。除了单个道具的检查，这些道具的交互又会产生一组需要仔细考量的全新测试内容。<br>
<br>
由于道具和词条的数量庞大，LQA（语言质量保证）团队也将面对繁重的检查。<br>
<br>
同时，多种道具的设定需要进行大量的平衡测试来保证游戏的一致性。然而，在实际应用之前，平衡所有道具通常是不可能的。<br>
<br>
平衡检查需要在整个开发过程中持续进行，当添加了新的道具和技能，每一个道具和效果的组合都需要检查。在RPG中的道具组合数目通常十分庞大，仅仅检查几个道具的组合是不够的。团队需要检查每一种组合并确认没有任何明显的问题，这是个非常耗时的过程。<br>
<br>
<strong><font color="#de5650">3、玩家角色</font></strong><br>
<br>
RPG通常会允许玩家们自定义角色，包括角色的属性鉴定，衣着和外观，及其他的特定鉴定。保证玩家角色的功能正常对一个RPG的成功来说至关重要；比起一个标准的主人公，自定义角色会让玩家感到亲切得多。<br>
<br>
<div align="center">
<img id="aimg_967368" aid="967368" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132220ibtslgkm7s7lnbgw.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132220ibtslgkm7s7lnbgw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132220ibtslgkm7s7lnbgw.jpg" referrerpolicy="no-referrer">
</div><br>
测试中会部分使用到与检查道具相同的方法，因为皮肤/装备通常会提升角色的属性。但由于这些道具的物理属性将显示在玩家角色身上，测试中还要进行一系列的渲染检查，以保证外观上的变化正常显示在角色身上。<br>
<br>
这也许看上去简单直接，但与道具一样，有很多极端案例和特殊情况需要被测试，例如在装备多个衣着装备后检查角色的外观是否正常，检查角色在所有菜单界面是否都显示正常。<br>
<br>
<div align="center">
<img id="aimg_967370" aid="967370" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132221y8gmwatmi5d8y8yw.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132221y8gmwatmi5d8y8yw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132221y8gmwatmi5d8y8yw.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">4、NPC和敌人</font></strong><br>
<br>
典型的RPG游戏都有各种各样的NPC（非玩家角色）和敌人，与其自己的对话元素、行为、功能和外观。<br>
<br>
<div align="center">
<img id="aimg_967371" aid="967371" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132221kx8ajmayaojfbhhh.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132221kx8ajmayaojfbhhh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132221kx8ajmayaojfbhhh.jpg" referrerpolicy="no-referrer">
</div><br>
标准的测试检查项目包括确保所有敌人和NPC都能<br>
<br>
<ul><li>正常显示和渲染</li><li>正常与物体碰撞</li><li>在没有障碍的情况下自由行动</li><li>名字和数据都正常显示等<br>
</li></ul><br>
除此之外，检查AI角色的行为也十分重要。这部分的测试要求很高，需要QA和开发团队密切合作，多次反复测试。<br>
<br>
正确且细致地测试AI是十分有益的，不仅在功能上，也因为遇到的情况本身十分有趣。每个人在游戏里都曾在看见敌人的时候说过，“那家伙在做什么！？”，或者如果您的运气不好，那甚至可能是个友好的NPC！<br>
<br>
<div align="center">
<img id="aimg_967372" aid="967372" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132221nxlstv0ijj4dt05l.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132221nxlstv0ijj4dt05l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132221nxlstv0ijj4dt05l.jpg" referrerpolicy="no-referrer">
</div><br>
没有什么比看见角色撞墙或行为不自然更能破坏玩家的沉浸感了。除此之外，疏忽了对难度的测试也会破坏玩家沉浸感。<br>
<br>
如果玩家遇到了难度远远超过其等级的战斗，就会很容易感到烦躁且失去沉浸感。这是RPG游戏不容忽视的问题，因为玩家通常被允许自行选择战斗或敌人，如果总觉得自己处于一种不公平的劣势，那么战斗的乐趣就消失殆尽了。这种烦躁的情绪将影响玩家的游戏体验，所以需要避免这种不必要的“烦躁”。QA团队需多次体验每一场战斗，他们是评价其乐趣、难度和代入感的最佳人选。<br>
<br>
与RPG游戏中的其他元素一样，NPC需要检查的不单只是战斗行为，还有许多需要测试的非战斗行为。您不会希望NPC在游戏中一直撞墙，也不会希望它们总往墙壁上射击。非战斗行为能使游戏身临其境，相反，其明显的漏洞将很快打破玩家们的沉浸感。<br>
<br>
<strong><font color="#de5650">5、菜单和UI</font></strong><br>
<br>
除了道具，RPG游戏的菜单也十分庞大。自定义菜单、地图、制作界面都有很多选项，需要对菜单和UI进行大量的检查和测试。幸运的是，菜单一般不会出现装备多个道具/装备的复杂情况，除非包括了特定的快捷键菜单。<br>
<br>
<div align="center">
<img id="aimg_967373" aid="967373" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132222cyte6c666e76l2tc.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132222cyte6c666e76l2tc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132222cyte6c666e76l2tc.jpg" referrerpolicy="no-referrer">
</div><br>
RPG的菜单和UI并不一定会比其他游戏要复杂或精致（虽然时常如此），但其菜单、UI和词条的数量造成了庞大的测试工作量。无论是语言上还是功能上，菜单的统一对玩家体验十分重要。一些游戏由于忽略这点，每个界面都需要玩家按下不同的按键来进行导航。虽然玩家会慢慢习惯这些操作，但对交互和一致性的关注不足会显得很不专业。<br>
<br>
<strong><font color="#de5650">6、分支故事和随机事件</font></strong><br>
<br>
RPG游戏通常会根据玩家的选择设定一些分支故事和随机事件。这些分支选项大大增加了测试量，QA团队将需要多次通关游戏来测试每个分支。<br>
<br>
<div align="center">
<img id="aimg_967374" aid="967374" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132222efjyy5ywmjzzyjkl.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132222efjyy5ywmjzzyjkl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132222efjyy5ywmjzzyjkl.jpg" referrerpolicy="no-referrer">
</div><br>
不同的分支可能会出现不同的对话、不同的角色，甚至整个区域发生变化等无数种可能性。需要保证功能测试和语言测试团队进行仔细的检查，测试到所有的分支。故事和玩法的不同选择会对极大地影响到游戏的后续部分，这也进一步增加了测试的工作量。<br>
<br>
随机事件的影响没有分支事件大。它不大会提升测试团队需要检查的事件数量，但因其随机性会使测试比较困难。随机事件可能是NPC的对话内容，也可能是世界事件，需要功能测试团队和语言测试团队的共同关注。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
投入时间进行游戏测试、发现潜在的问题对游戏、开发者和发行商来说都十分重要，一个充满bug的游戏会对每个参与者带来不好的影响。<br>
<br>
在大型RPG游戏中，总是不难找到漏洞，这主要是由游戏的巨大尺寸和庞大要素数量导致的。这也是为什么RPG游戏是一个展示您测试能力、对玩家的关注和RPG血统的地方。稳定上线的RPG游戏能瞬间给玩家留下深刻印象，并在玩家讨论和新闻报道中轻松地获得正面的评价和关注。您或许可以找到充满漏洞却仍受人喜爱的RPG游戏，但其数量是极少的。<br>
<br>
<div align="center">
<img id="aimg_967375" aid="967375" zoomfile="https://di.gameres.com/attachment/forum/202103/23/132222b6mdbdu6snsnzbqi.jpg" data-original="https://di.gameres.com/attachment/forum/202103/23/132222b6mdbdu6snsnzbqi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/23/132222b6mdbdu6snsnzbqi.jpg" referrerpolicy="no-referrer">
</div><br>
所以，给游戏测试留下充足的时间十分必要。在开发晚期匆忙测试会占用更多的时间，对您的资源和员工都造成负面影响。别把检查的工作积压在最后一秒，花时间进行测试，除了提升游戏本身的质量，也将保证游戏所支持的所有语言的质量。保证游戏的各版本在语言上匹配不仅仅对RPG游戏有好处，对其他任何类型的游戏都很重要。<br>
<br>
概括来说，测试RPG游戏的最大挑战就在于内容的深度和可变要素的数量。第一人称射击（FPS）游戏有一个玩家角色，30种武器，一些道具，和几个技能，而RPG将会有多个玩家角色，几百种武器，一大堆道具和因情况变化的各种技能。RPG要素的庞大数量，及相互之间的互动，将显著增加测试数量及时间，确保游戏成功上线。<br>
<br>
因此，RPG开发者必须尽量在开发早期就考虑测试工作和测试战略，包括与第三方的测试伙伴合作。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：博特盈 PTW</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/qnECznyKt6ixUY5EgDRsKQ</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            