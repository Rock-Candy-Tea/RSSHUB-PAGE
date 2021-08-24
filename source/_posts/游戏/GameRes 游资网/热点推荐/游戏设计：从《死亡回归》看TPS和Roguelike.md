
---
title: '游戏设计：从《死亡回归》看TPS和Roguelike'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/13/101217we3yrb06ztb5zgb0.jpg'
author: GameRes 游资网
comments: false
date: Fri, 13 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/13/101217we3yrb06ztb5zgb0.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2509962">
<div align="center">
<img id="aimg_1000555" aid="1000555" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101217we3yrb06ztb5zgb0.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101217we3yrb06ztb5zgb0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101217we3yrb06ztb5zgb0.jpg" referrerpolicy="no-referrer">
</div><br>
本篇主要围绕《死亡回归》的核心玩法以及Boss、关卡设计进行思考，主要是针对其弹幕躲避的核心玩法和以首章Boss为例的技能设计进行分析，也作为对TPS类游戏的思考和记录。<br>
<br>
<strong><font color="#de5650">核心玩法分析</font></strong><br>
<br>
《死亡回归》的核心玩法由TPS和弹幕躲避组成，TPS是战斗内玩家的核心输出表现，弹幕躲避则是战斗内玩家的生存考验。TPS的核心体验通常围绕“移动”“瞄准”“射击”构成，其中“移动”也是弹幕躲避的核心能力考验。如下图所示，玩家在游戏内的核心玩法表现大概可以分为两块：躲避弹幕和有效射击（两者可能单独发生也可能同时发生）。躲避弹幕意味着玩家躲避怪物攻击、弹道的玩法表现，有效射击则对应了玩家瞄准目标并且进行有效伤害打击的过程。因为关卡对于玩家要求是击败敌人，因此输出和生存对于玩家是同等级的能力考验。因此，就需要保证不同的玩家在同样的玩法下都能够有不同的正向体验和乐趣反馈。<br>
<br>
<div align="center">
<img id="aimg_1000556" aid="1000556" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101218sa2zlt12ljw1aszb.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101218sa2zlt12ljw1aszb.jpg" width="394" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101218sa2zlt12ljw1aszb.jpg" referrerpolicy="no-referrer">
</div><br>
而由于两者的能力考验是同时存在的，因此《死亡回归》在普通关卡中弱化了对于弹幕躲避的能力要求，通过降低弹幕攻击的频率和范围以及提供大量的环境掩体来降低玩家的躲避操作成本。对于新手玩家来说只需要保证活着并且抽空打怪就可以，关卡内的大量掩体成为了他们有效躲避弹幕的辅助工具，而怪物较长的攻击间隔也保证给玩家预留了足够的瞄准输出空间。除了利用掩体躲避怪物之外，角色的冲刺技能也是玩家躲避弹幕的主要操作方式。但冲刺技能的内置冷却时间以及冲刺后的无法开枪的衔接阶段，都需要玩家在面对大量弹幕或是怪物时进行谨慎的选择和操作。玩家也会在一次次冲刺或受击之后，不断强化自身对于游戏内机制的认知。<br>
<br>
<div align="center">
<img id="aimg_1000557" aid="1000557" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101218j66byuuteyfe2kek.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101218j66byuuteyfe2kek.jpg" width="525" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101218j66byuuteyfe2kek.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">冲刺到落地后开枪大概有10帧间的动作持续</font></font></div><br>
大部分玩家都属于普通玩家一档，因此《死亡回归》给普通玩家提供了更多的可操作空间和目标，其中的整体难度也不会有太大的差距。普通玩家的目标是以尽可能小的代价去打败怪物，同时也追求和怪物正面对抗来获取更大的成就感反馈。因此，对于普通玩家而言首先要保证弹幕的机制足够简单和明确，玩家在面对、躲避弹幕的过程也是一个不断学习怪物攻击循环从而锻炼自身操作能力的过程。其次就是以尽量小的代价击败怪物，要求的就是玩家在尽量短的时间内对怪物造成尽可能多的伤害。除了伤害数值成长的因素之外，玩家通过操作能够实现的就是短时间内进行尽可能多的输出和保证输出的有效性。游戏内子弹的自动回复和完美换弹的机制，都能够保证玩家能够尽可能多的进行输出并且作为进阶操作的奖励反馈给予玩家正向的游戏体验。<br>
<br>
<div align="center">
<img id="aimg_1000559" aid="1000559" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101218uuoowe0ct0q22cos.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101218uuoowe0ct0q22cos.jpg" width="269" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101218uuoowe0ct0q22cos.jpg" referrerpolicy="no-referrer">
</div><br>
而辅助瞄准则被动降低了玩家的瞄准操作成本，保证玩家输出的有效性。和其他辅助瞄准不同的是，在《死亡回归》中对玩家躲避弹幕的操作要求极高，因此辅助瞄准的影响度相较于其他射击类游戏更高，但常见的目标引力和粘性辅助方式属于在玩家主动操作时的辅助方式，如果一味提高引力或粘性会极大影响玩家的射击手感并且让玩家感知到辅助机制的存在。《死亡回归》主要放大了怪物的Hitbox和利用磁力子弹的方式来帮助玩家命中目标。一方面是怪物体型相对于玩家来说都是更大的，所以放大Hitbox对于玩家感知不会过分突兀；另一方面玩家为了躲避弹幕大多会在离boss较远的距离进行攻击，并且准星本身就有一个较大的扩散范围以至于磁力子弹看上去就更加合理。<br>
<br>
<div align="center">
<img id="aimg_1000560" aid="1000560" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101219hgrop7rripsgg1y7.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101219hgrop7rripsgg1y7.jpg" width="465" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101219hgrop7rripsgg1y7.jpg" referrerpolicy="no-referrer">
</div><br>
此外，值得一提的是游戏内子弹自动回复的设计，PVE游戏内战斗节奏是玩家掌控战斗的核心点之一。这里的战斗节奏包括怪物的（攻防）节奏和玩家的（攻防）节奏。在玩家进行弹幕躲避的同时，为了避免给予玩家过高的攻防转换压力，让玩家聚焦有效射击和弹幕躲避，自动回复的弹量能够保证玩家攻击节奏的一致性和平稳性。<br>
<br>
最后就是对进阶玩家，怪物死后掉落的资源对应了玩家局内能够养成的强度。而有时间限制的掉落资源，则要求玩家在击杀怪物后及时拾取掉落的资源。由于怪物大多是成群地出现，因此在躲避弹幕的同时还要去收集击杀怪物的掉落资源，给玩家除了弹幕躲避之外的移动操作又增加了大量的考验空间和反馈。<br>
<br>
在保证和新玩法深度的同时《死亡回归》给不同的玩家群体都提供了对应的玩法追求目标和操作空间，并且提供大量的辅助设计来帮助下层的玩家向上层进行转变。移动、瞄准玩法本身提供给玩家极大锻炼提升的空间，瞄准搭配射击能给予玩家即时的有效反馈，而操作的躲避和收集，则属于长线的反馈孕育，也从侧面辅助强化了有效射击带来的反馈体验。玩家能够从玩法本身中就收获多种不同的正向体验反馈。<br>
<br>
<div align="center">
<img id="aimg_1000561" aid="1000561" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101219ywiqdowhoiqnqw8r.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101219ywiqdowhoiqnqw8r.jpg" width="441" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101219ywiqdowhoiqnqw8r.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">Boss设计</font></strong><br>
<br>
《死亡回归》Boss的设计可以从两个部分进行思考：攻击方式的循环和记忆点。<br>
<br>
以《死亡回归》第一章的Boss弗莱基为例，Boss一共分为三个阶段。每个阶段的攻击方式都是固定的六种，整体攻击的机制固定，随着阶段的变化对应攻击的顺序和波次表现会发生变化。以下图中的第一阶段为例，六种弹幕攻击方式通过不同的机制分别考验了玩家不同的能力水平。玩家应对单个攻击循环的过程中，整个难度曲线如下图所示是由易逐渐到难的一个过程：黄色的弹幕数量多，但是弹道速度较慢，玩家有大量的时间可以进行躲避；紫色弹幕在出射时会追踪玩家所在的方向，玩家进行一定的位移即可躲避；红色弹幕则是全程对玩家进行追踪，玩家必须要进行冲刺和长距离的跑动来进行躲避；近战攻击的Boss会产生一定的位移，玩家需要快速地反应以及冲刺才能躲避；其余的红色激光则是范围大但是弹道速度或是抬手较慢，玩家有足够的时间进行反应和操作。<br>
<br>
<div align="center">
<img id="aimg_1000562" aid="1000562" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101219wzooxqi8np3o9a9l.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101219wzooxqi8np3o9a9l.jpg" width="330" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101219wzooxqi8np3o9a9l.jpg" referrerpolicy="no-referrer">
</div><br>
在单个技能循环链中，除了攻击的间隔留给玩家进行输出之外，玩家会逐渐将整个Boss攻击循环学习融合成自身的攻击循环，通过进行对应的躲避操作来保证自身的输出空间。而整个由易到难的技能循环保证了玩家上手的节奏会逐渐熟练，并且多次重复强化玩家对于怪物攻击循环的记忆。Boss的每次攻击可以看做一个独立的记忆点，在每轮循环的攻击中，不同记忆点的深刻程度也会有所区别。在Boss不同阶段的变化间所有技能的基本逻辑是一致的，技能的顺序和波次会发生改变。例如在二阶段下的Boss在释放完全屏的光圈弹幕后，会立刻发动一次位移近战攻击，玩家除了需要躲避近战的攻击还需要躲避逐渐靠近的全屏弹幕。玩家对于所有弹幕规律的认知不会发生改变，应对方式也都是一致，只是玩家需要更加精确合理地安排自己的操作顺序和轨迹来保证不被连续的攻击命中。玩家在应对攻击循环的过程中不断认知怪物的攻击方式并且合理地使用应对能力，随着挑战次数的不断增加，玩家除了操作水平不断得到锻炼之外，对于自身的能力可覆盖范围认知也在不断提高。尽管存在死亡惩罚，但是玩家能够获得实打实的能力成长累积，玩家也就越倾向于再次挑战证明自己。<br>
<br>
<div align="center">
<img id="aimg_1000563" aid="1000563" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101220os6z4hyfjxu2efmy.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101220os6z4hyfjxu2efmy.jpg" width="276" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101220os6z4hyfjxu2efmy.jpg" referrerpolicy="no-referrer">
</div><br>
这个时候回过头来看一下各个独立的弹幕设计，最初设计的时候就已经确定好了弹幕对玩家的能力考验维度，高区分度的弹幕颜色，保证弹幕给玩家留下记忆点的区分度，玩家能够根据颜色的特征来清楚认知对应弹幕的效果和攻击方式，而Boss的后续阶段变化只是将多个能力考验维度叠加到了一起并且保证不会在同一时间使得相同的能力考验产生冲突。以及最初小怪的攻击方式都是Boss技能的提前展现，弹幕考验的玩家能力都是一致的，玩家早就已经身处“循环”之中，Boss战是之前所有攻击记忆点形成的完整循环。<br>
<br>
<div align="center">
<img id="aimg_1000564" aid="1000564" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101220jcrbrzaa0ch2vuxl.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101220jcrbrzaa0ch2vuxl.jpg" width="386" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101220jcrbrzaa0ch2vuxl.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">关卡设计</font></strong><br>
<br>
关卡属于始终围绕游戏的核心玩法和体验，帮助玩家提升、验证实力的部分。这里主要以《死亡回归》第一章的关卡为例，分析一下其多因素（怪物、场景）汇集下的关卡节奏、目标的设计。《死亡回归》本身结合了弹幕躲避和Roguelike的玩法，因为并不涉及到局外成长，所以核心玩法更多地专注于考验玩家的操作技术（弹幕躲避）。并且在玩家重复体验游戏的整个过程中，除了随机性带来的变化之外，游戏的整体难度曲线是固定的，对玩家的核心考验就是其自身能力和对游戏机制的理解，因此关卡的作用就是帮助玩家摸清规则、练习操作和不断熟悉游戏环境。<br>
<br>
<strong><font color="#de5650">难度/节奏</font></strong><br>
<br>
在具体分析怪物、关卡设计之前先分析一下弹幕躲避和TPS玩法相关的难度设计与衡量，后续的怪物、关卡设计也都是以此为依托进行展开的具体设计。对于弹幕躲避类游戏来说，难度的来源以及玩家的能力考验核心是“有效地躲避弹幕”，简单来说就是“移动”；而TPS的难度和能力的核心考验点则是“有效射击”，换句话说就是“瞄准”。而将这两者具体拆解成玩家所执行的操作，就是如下图所示。整个流程中的子元素可以分为两类：认知和操作，尽管整个行为链的速度较快，但对于整个行为而言，想要做出有效地操作，依然需要按照“先认知、后操作”的顺序，而导致实现速度差异的主要原因就是认知速度和操作速度的不同。因此，“难度”就意味着玩家需要进行更多的认知/操作行为或是在有限的时间内完成一定量的对应行为。<br>
<br>
<div align="center">
<img id="aimg_1000565" aid="1000565" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101221ve45ql5aqwv2thqz.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101221ve45ql5aqwv2thqz.jpg" width="402" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101221ve45ql5aqwv2thqz.jpg" referrerpolicy="no-referrer">
</div><br>
移动的核心目标是躲避“弹幕”，因此弹幕的数量、速度、方向是影响移动行为难度的核心，而瞄准的核心目标是怪物对象，因此怪物的大小、移动速度（还有一些侧面因素。包括环境等）都是影响玩家瞄准行为的核心难度。此外，当两者同时存在时，玩家就需要一边关注移动目标一边进行瞄准操作。而整个“移动”、“瞄准”、“射击”操作所形成的攻防转换以及有效攻击，就构成了战斗中的节奏。玩家在攻防转换的同时，除了对于战场信息的观察之外，同时还在构筑和积累自身战斗中情绪感受，而随后的进行攻击的窗口，则是玩家情绪释放的空间。这种不断累积的紧张度辅以合适的输出窗口，构成了让玩家情绪上感到爽快的关键。<br>
<br>
难度与节奏共同相关的属性就是战斗中各种情况发生的“频率”，用《死亡回归》中的战斗表现来看，就是在“一段时间内，玩家需要躲避的弹幕数量”和“一次躲避后，能够进行的攻击次数”，围绕这一点就能够抽象出设计者期望玩家获取的体验。<br>
<br>
<div align="center">
<img id="aimg_1000566" aid="1000566" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101221s7p388owdny8osyn.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101221s7p388owdny8osyn.jpg" width="322" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101221s7p388owdny8osyn.jpg" referrerpolicy="no-referrer">
</div><br>
当然在玩家的操作维度之外，还有自身和怪物的血量、攻击力一类容错性的侧面因素。因为玩家的反馈主要来自弹幕的紧张压力与成功躲避后的情绪宣泄，因此玩家在受到攻击后感受到的更多还是负面的反馈。对于单纯的弹幕躲避来说，血量更多的属于一种压力容错，而并非操作本身的难度上限。<br>
<br>
<strong><font color="#de5650">怪物设计</font></strong><br>
<br>
《死亡回归》的关卡难度可以看作由主要和次要因素两部分组成，主要因素是关卡内怪物的难度，包括怪物的数量、种类；次要因素则是关卡的场景、环境和定位。而由于Rogue重复永久死亡的特点，玩家在重复挑战的初期必然会经历“手无缚鸡之力”的阶段，因此关卡的难度务必需要满足由易到难的过程，除了让玩家实现单局强度的逐渐养成之外，通过低难度向高难度递进的方式，帮助玩家“热身”进入战斗节奏以及重复循环认知和操作方式，来提高玩家的“局外”操作能力。<br>
<br>
既然关卡的难度顺序是相对固定的，而关卡的难度主要还是由其内部怪物布置决定的，这里以第一章内的怪物种类和行为方式为例：<br>
<br>
<div align="center">
<img id="aimg_1000567" aid="1000567" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101222xk72s3zsn24h2j18.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101222xk72s3zsn24h2j18.jpg" width="356" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101222xk72s3zsn24h2j18.jpg" referrerpolicy="no-referrer">
</div><br>
以地狱犬的攻击行为表现来看：在距离玩家较远时进行弹幕攻击，而距离较近时则会进行近战挥击。地狱犬在游戏中的定位是玩家初入游戏就会遇到的初级怪，因此回到其攻击表现上能够看到弹幕的特点是速度极慢，危险范围明显且易躲避，而近战攻击则有明显的前摇动画提示。并且在不同的攻击之间会有较长的破绽时间，一方面保证了对玩家攻防节奏的引导，另一方面给玩家留下了多种战斗的策略选择空间，玩家可以选择安全地在远处进行射击，也可以选择近战进行攻击。<br>
<br>
按下图所示的综合作战流程，当关卡中出现多种类多数量怪物时，尽管怪物有不同的攻防行为，但是其行为的重叠期间会给玩家留出充足的作战窗口，高频转换的攻防压力配合留有余地的作战窗口，促使玩家在整个过程中不断闪避走位，需要玩家专注以连贯的动作进行应对。在此期间，不仅玩家整个情绪处于一种紧张专注的状态之中，其操作能力也能够不停地得到锻炼。<br>
<br>
<div align="center">
<img id="aimg_1000568" aid="1000568" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101223jko8r8of1s7k1eku.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101223jko8r8of1s7k1eku.jpg" width="421" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101223jko8r8of1s7k1eku.jpg" referrerpolicy="no-referrer">
</div><br>
怪物设计除了带给玩家不同的战斗节奏和体验之外，还同时服务于考验和锻炼玩家的不同能力，基于此就能够衍生出具体的攻击方式和规则。例如有了明确的怪物设计之后，只需要在对应定位的关卡，摆放对应难度的怪物组合即可。需要注意的是，由于弹幕的叠加，即使是单纯增加同一种怪物的数量也会导致弹幕数量瞬间增加从而压迫玩家短时间内的操作空间使得关卡难度瞬间提升，因此《死亡回归》关卡内的怪物数量基本都比较有限，或是通过批次刷新来保证难度的可控。<br>
<br>
<strong><font color="#de5650">关卡节奏（难度节奏和探索节奏）</font></strong><br>
<br>
尽管延续了Roguelike的随机地图，但在整体关卡难度顺序确定的情况下，《死亡回归》的随机关卡还是建立在确定路径和障碍的基础上，再从关卡库中选择对应难度的障碍关卡进行填充。在实际生成时依照难度从“小怪关”、“精英关”不同的关卡库中选择不同的关卡拼接到一起，中间再穿插一些能够承载剧情的“事件关”和“场景关”，使得整个流程看起来“饱满”。<br>
<br>
因此，随着多次遍历会发现《死亡回归》的关卡大多是固定的场景搭配固定的怪物内容，以下图的关卡分布为例，核心进度关卡的难度依照“先易后难”的顺序，与进入的先后顺序无关，并行关卡的难度也基本相同。玩家首先面对“小怪关”随后是“精英关”，最后再是Boss关。至于战斗关卡外的分支，则是作为一种随机空间开放给玩家，伴随玩家主动选择带来的节奏变化之外，同时作为玩家养成的空间投放。这样的关卡设计保证了整个流程、难度可控，但同时也失去了较大的随机空间。<br>
<br>
<div align="center">
<img id="aimg_1000569" aid="1000569" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101224jk11e0k11eft0d1z.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101224jk11e0k11eft0d1z.jpg" width="421" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101224jk11e0k11eft0d1z.jpg" referrerpolicy="no-referrer">
</div><br>
而在单个章节内也是以小怪预演Boss机制的模式所设计的。以第一章为例，初期的地狱犬的攻击方式就是简单的横扫弹幕以及近战挥击；随后是多个地狱犬的同时出现，玩家需要同时应对多个相同的怪物；接着开始出现空中的拉弥亚顿，玩家的瞄准能力开始得到考验和锻炼；同时，开始多个类型的怪物叠加出现，玩家应对的维度进一步增加；随后就是精英怪的出现，开始有追踪弹，大范围扑击等攻击方式，对玩家移动和瞄准的能力要求更进一步提高，并且玩家开始逐渐接受更多的弹幕攻击方式。最后就是面对章节的Boss，Boss的攻击方式基本是该章节内小怪的统合，尽管表现方式（颜色、数量）发生了一定的变化，但核心应对方式玩家早已在之前的小怪身上得到过充分的锻炼。<br>
<br>
除了通过不同的怪物种类及其攻击方式，事先在关卡内给玩家进行Boss攻击的预演之外。由于关卡环境直接关系到了玩家的（信息、操作）收益和对于能力体验、验证的要求（瞄准、操作），因此弹幕躲避考验对于关卡环境设计的要求更高。所以这里的难度节奏分别从怪物难度和场景难度来分析：怪物难度（攻击方式、伤害数值）主要影响玩家的攻击选择；而场景难度（掩体数量、危险区域）则影响玩家移动的选择。当在某个关卡内两者难度都很高时，两者的结合就会对玩家能力产生1+1>2的能力要求。而《死亡回归》中部分精英怪关的难度总和会和Boss关较为接近，一方面是精英怪的攻击方式更加复杂、对操作要求更高；另一方面是多变的地形环境要求玩家在有限的移动环境内处理复杂的怪物攻击。<br>
<br>
<div align="center">
<img id="aimg_1000570" aid="1000570" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101225aew3ozz9t6mswntd.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101225aew3ozz9t6mswntd.jpg" width="469" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101225aew3ozz9t6mswntd.jpg" referrerpolicy="no-referrer">
</div><br>
因此关卡内通常会通过一些辅助手段来帮助玩家进行认知和准备，例如在刷怪机制上：精英怪的刷新通常伴随着时间较长且非常显眼的动画特效，玩家可以在精英怪刷新之前进行小怪的处理或是寻找合适的作战时机、空间。并且除了Boss外所有怪物（除炮台外）都是在玩家进入场景之后进行刷新，且从关卡入口到与怪物战斗的区域还有较长的空间距离留给玩家准备和观测，包括根据敌人的种类和分布位置来决定自身的移动、攻击策略。<br>
<br>
而在关卡场景上，由于地图本身是随机生成的，玩家在进入关卡房间之前并不知道门背后地图的样式，因此需要提供一定的辅助措施来降低玩家进入的压力和帮助玩家做好战斗准备，以关卡的其起始位置为例：让玩家进入关卡的位置在房间的高处以便玩家能够观察到整个关卡内的整体构造或是通过初入关卡时的洞穴、墙壁的掩体来保证玩家可以在没有威胁感的情况下确定方位和关卡布置，并且后续的关卡的打开会显得空间更大，玩家通过移动、操作慢慢占用这个空间，信息和选择也随着玩家的操作逐渐呈现，玩家可以感觉到到随着自己的前进关卡内的空间在变得更大。<br>
<br>
<div align="center">
<img id="aimg_1000571" aid="1000571" zoomfile="https://di.gameres.com/attachment/forum/202108/13/101225w6h84yd84c7k7lr4.jpg" data-original="https://di.gameres.com/attachment/forum/202108/13/101225w6h84yd84c7k7lr4.jpg" width="304" inpost="1" src="https://di.gameres.com/attachment/forum/202108/13/101225w6h84yd84c7k7lr4.jpg" referrerpolicy="no-referrer">
</div><br>
<i><font size="2"><font color="#808080"></font></font></i><br>
<i><font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/360346151</font></font></i><br>
</td></tr></tbody></table>



  
</div>
            