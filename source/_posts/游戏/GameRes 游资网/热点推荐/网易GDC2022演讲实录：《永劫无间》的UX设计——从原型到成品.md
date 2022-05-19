
---
title: '网易GDC2022演讲实录：《永劫无间》的UX设计——从原型到成品'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202205/16/101040ho4j2116y0jjj76n.gif'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://di.gameres.com/attachment/forum/202205/16/101040ho4j2116y0jjj76n.gif'
---

<div>   
<div align="center">
<img aid="1039631" zoomfile="https://di.gameres.com/attachment/forum/202205/16/101040ho4j2116y0jjj76n.gif" data-original="https://di.gameres.com/attachment/forum/202205/16/101040ho4j2116y0jjj76n.gif" width="600" id="aimg_1039631" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/101040ho4j2116y0jjj76n.gif" referrerpolicy="no-referrer">
</div><font color="#808080"><i>本文首发公众号“网易雷火UX用户体验中心”</i></font><br>
<br>
今年3月21日至3月25日，全球游戏行业最具规模、最有权威、最有影响力的专业峰会GDC2022在旧金山莫斯康中心盛大召开。本届GDC中，雷火UX共获邀17场演讲，分布在9个核心演讲以及8个峰会演讲，再度刷新中国游戏行业纪录，领跑全球。<br>
<br>
<div align="center">
<img aid="1039621" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100749w7eosownlo69etno.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100749w7eosownlo69etno.jpg" width="600" id="aimg_1039621" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100749w7eosownlo69etno.jpg" referrerpolicy="no-referrer">
</div><br>
接下来雷火UX公众号将陆续为大家进行介绍。本篇为大家介绍的是来自雷火UX交互体验师觉觉和Nero的演讲——“《永劫无间》的UX设计：从原型到成品”，以下是演讲实录。<br>
<br>
<div align="center">
<img aid="1039622" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100750dcc8ctrqzu2bcyua.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100750dcc8ctrqzu2bcyua.jpg" width="600" id="aimg_1039622" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100750dcc8ctrqzu2bcyua.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">关于永劫无间</font></strong><br>
<br>
《永劫无间》是网易旗下24 Entertainment于2021年7月正式公测的游戏，8月全球上线。这是一款60人的动作生存竞技游戏。在游戏中，玩家可以使用技能、飞索、远近战武器来夺取胜利。凭借高超的近战和反重力的动作，《永劫无间》巧妙地从传统大逃杀中脱颖而出。<br>
<br>
<div align="center">
<img aid="1039623" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100750a92ehegzz848l8dp.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100750a92ehegzz848l8dp.jpg" width="600" id="aimg_1039623" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100750a92ehegzz848l8dp.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">一、我身无拘的自由战斗体验</font></strong><br>
<br>
自《PUBG》发售以来，全球游戏厂商纷纷开发生存竞技玩法类型的游戏。这些游戏中诞生了不少爆款，像《堡垒之夜》、《Apex》。我们发现在这些游戏里，除了射击元素外，开发商往往加入了自己独特的游戏元素。像《PUBG》，是在生存竞技玩法上加入拟真射击元素；《堡垒之夜》则新增了建筑机制；而《Apex》增加了英雄机制。在生存竞技领域的红海里，只有具有独特的亮点才能占据一席之地。《永劫无间》正是凭借着近战博弈等机制和高自由度的战斗体验在竞争激烈的生存竞技游戏市场上取得成功。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039624" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100750ux9j6t7v6jfajw4v.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100750ux9j6t7v6jfajw4v.jpg" width="600" id="aimg_1039624" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100750ux9j6t7v6jfajw4v.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">当前游戏市场中的生存竞技游戏</font></font></div><br>
在游戏的开发过程中，我们将游戏系统分为核心系统、重要系统和外围系统，本次分享中我们会重点介绍核心系统和重要系统的设计。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039625" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100750rj50gm7iym59sasa.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100750rj50gm7iym59sasa.jpg" width="600" id="aimg_1039625" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100750rj50gm7iym59sasa.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏系统分类</font></font></div><br>
<strong><font color="#de5650">二、四个阶段的设计挑战</font></strong><br>
<br>
在整个游戏的开发过程中，我们遇到过很多设计挑战。《永劫无间》在上线前一共经历四个阶段。游戏从刚开始的只有近战武器格斗的原型慢慢变成最终具有局内外复杂系统、远近战皆宜的正式版本。<br>
<br>
<div align="center">
<img aid="1039626" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100751bdbedmir3tdwdbdy.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100751bdbedmir3tdwdbdy.jpg" width="600" id="aimg_1039626" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100751bdbedmir3tdwdbdy.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">原型测试阶段、实验室测试阶段、封闭测试、上线版本</font></font></div><br>
<div align="center">
<img aid="1039627" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100751gk6mzbhf488442wb.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100751gk6mzbhf488442wb.jpg" width="600" id="aimg_1039627" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100751gk6mzbhf488442wb.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">从游戏的大厅界面，也可以看出明显的进步</font></font></div><br>
<strong>核心概念</strong><br>
<br>
设计伊始，为了和现有市场做出差异化，我们希望能做一个基于中国传统武术的游戏。于是我们的团队结合游戏的世界观进行了桌面研究和脑暴。当提到古武的时候，大家会第一时间想到哪些。<br>
<br>
我们最终得到了一个核心词汇：“无拘”。它也是我们游戏的核心概念。基于这个概念，我们引申了三个主要的设计价值观：自由度，多元化，随机性。<br>
<br>
<ul><li><strong>自由度</strong>，意味着更自然的体验，包含扩展性，易用，极简等方面；</li><li><strong>多元化</strong>，意味着更包容的体验，包含统一性、本地化、适配等方面；</li><li><strong>随机性</strong>，意味着更真实的体验，包含临场感、制造惊喜等方面。<br>
</li></ul><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039628" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100751jwz7ymy9bsnf9dym.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100751jwz7ymy9bsnf9dym.jpg" width="600" id="aimg_1039628" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100751jwz7ymy9bsnf9dym.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">“无拘”引出的设计价值观</font></font></div><br>
<strong><font color="#de5650">三、四个阶段的设计重心</font></strong><br>
<br>
<strong>原型测试：核心玩法打磨</strong><br>
<br>
在游戏的原型阶段，我们的游戏把重心放在游戏的核心玩法打磨上，游戏体验设计也主要是针对飞索，近战以及死斗玩法等方面。然而游戏的原型测试结果却并不令人满意。在用研团队的帮助下，我们发现不同玩家群体对游戏的反馈具有较大差异。具有丰富游戏经验并且喜欢硬核游戏的高玩群体对我们游戏的评价很高，但是游戏能力稍弱的大众玩家对我们游戏评价要低上不少。这代表如果我们游戏如果保持当时的核心玩法不做改动的话，将会损失大量大众玩家群体。这对游戏的发行非常不利。在定量的评分之后，我们的用研团队继续做了定性研究，来发掘评分背后的原因：游戏过于硬核了，大众玩家在游戏中的挫败感很强。被击杀带来强烈的负面情绪让玩家对游戏失去了兴趣。<br>
<br>
<strong>战斗机制简化</strong><br>
<br>
所以我们尽量简化了近战格斗的机制。在我们的游戏中，为了鼓励攻击，我们所有操作都是攻击行为，包含短按的轻击，长按的重击以及振刀。为了让新手玩家快速上手，在激烈的战斗中识别敌人的操作，我们用颜色表示当前操作，例如：白色轻击，蓝色重击，红色振刀，这样玩家就可以快速通过敌人身上的颜色了解敌人马上进行的操作，从而采取对应克制的操作。不仅如此，玩家可以随意打断当前操作从而进入其他操作，这也给技术能力更高的玩家提供了“假动作”的操作空间，从而提升了整个对战博弈的深度。<br>
<br>
总的来说，战斗的设计带来了以下优点：<br>
<br>
<ul><li>符合玩家心理预期</li><li>新手容易上手</li><li>高手有操作空间<br>
</li></ul><br>
<strong>武器多样化</strong><br>
<br>
近战武器因为连招等原因有一定的上手难度，为了吸引更多玩家，我们在游戏中也引入了中国古代的远程武器。这样，喜欢射击游戏的玩家可以和喜欢格斗游戏的玩家进行同台竞技。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039629" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100751biofm6f442o31gkm.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100751biofm6f442o31gkm.jpg" width="600" id="aimg_1039629" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100751biofm6f442o31gkm.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">远程武器设计</font></font></div><br>
<strong>实验室测试：注重战斗平衡</strong><br>
<br>
基于上个版本的游戏迭代，我们的用研同学进行了再一次测试。在本次测试中，我们发现远近程武器的平衡性有了比较大的问题。由于作战距离的原因，近战玩家在面对远程玩家时拥有天生的劣势。因此玩家往往只使用远程武器而放弃近身战斗。但这样，我们的游戏和其他生存竞技游戏显得过于同质化，各个元素之间缝合的不协调感也更强了。<br>
<br>
在《永劫无间》之前，国内有两款近战生存竞技游戏也曾经上线过，不过他们最终还是表现不佳。我们的团队在深入调研他们的流失玩家以后发现了一个共同特点，很多玩家反馈在现有的近战生存竞技游戏中，追击玩家非常困难。为了平衡远近程武器，光靠改变数值是没有意义的，团队决定引入飞索这一新元素。飞索在近几年的游戏中也被广泛使用，玩家往往可以利用飞索在各个位置之间快速移动。但是在《永劫无间》中，玩家不仅可以利用飞索在场景间移动，也可以利用飞索快速追踪敌人，拉近距离。<br>
<br>
<strong>封闭测试：其他玩法体验优化</strong><br>
<br>
在之前版本的测试中，我们对游戏的核心玩法进行了打磨和优化，提升了玩家的核心战斗体验。在封闭测试中，我们设计的重点在其他重要玩法和成长系统的体验优化上。<br>
<br>
游戏中，角色死亡往往会带来极强的挫败感。在生存竞技游戏中，20队游戏玩家大部分时候只有1队人能获得胜利，其他人都将失败。很多玩家甚至有可能落地成盒。《永劫无间》为了帮助玩家控制被击败的负面情绪，激励玩家继续战斗，做了很多努力。<br>
<br>
我们最开始参考了《Apex》的复活机制，玩家死亡后队友需要拾取其背包中的令牌才能去特定地点复活玩家。但是实际测试中，这种复活方式产生了不少问题，玩家能否复活完全依赖于队友的想法。因为沟通、距离等原因，很多玩家往往放弃救援队友。<br>
<br>
因此，我们改进了救援方式,玩家死亡后可以以灵魂状态自行前往提示的地点复活。玩家个人提升了游戏容错率，队伍也能重新聚合起来继续战斗。<br>
<br>
<strong>上线版本：捏脸系统带来的意外惊喜</strong><br>
<br>
在《永劫无间》中，“无拘”不仅是体现在游戏玩法上，也在局外的相关系统中。游戏上线后，我们发现游戏的捏脸系统大受欢迎，很多玩家沉迷于我们的捏脸系统，纷纷在各种社交、内容平台进行分享和讨论他们自己的创意作品。<br>
<br>
其实在游戏初始阶段，团队中很多人是反对捏脸系统的。因为在其他拥有英雄角色的游戏,例如《Apex》和《守望先锋》中，并没有捏脸系统。这是因为面容可以帮助玩家来识别一个英雄角色。如果允许玩家自定义，那角色的独特性和商业性就会降低。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039630" zoomfile="https://di.gameres.com/attachment/forum/202205/16/100752pmc0mwrtbrcbt0wz.jpg" data-original="https://di.gameres.com/attachment/forum/202205/16/100752pmc0mwrtbrcbt0wz.jpg" width="600" id="aimg_1039630" inpost="1" src="https://di.gameres.com/attachment/forum/202205/16/100752pmc0mwrtbrcbt0wz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《永劫无间》的捏脸系统</font></font></div><br>
幸亏产品经理和其他同事们的坚持，我们最终开发了捏脸系统，并且提供了100多个参数允许玩家自行调整。因为捏脸，游戏也能更广泛的在玩家之间形成自发传播。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
在游戏的设计开发过程中，为了达到初始设定的体验目标，游戏开发者们往往会引入一系列新的机制和元素。然而，这些新元素新机制可能互相之间相对独立，缺乏耦合，使得整个游戏像一个缝合怪。对游戏开发者来说，最重要的任务就是确立一个核心的体验目标，然后围绕这个目标，在所有机制和元素的基础上做加法和减法。<br>
<br>
就像《永劫无间》一样，我们一直的核心体验目标就是“无拘”。<br>
<br>
<font size="2"><font color="#808080">来源：网易雷火UX用户体验中心</font></font><br>
<br>
  
</div>
            