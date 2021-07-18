
---
title: '游戏设计-Roguelike类游戏的一些思考'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/05/094303hfg0wjfe6gsgkg09.jpg'
author: GameRes 游资网
comments: false
date: Mon, 05 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/05/094303hfg0wjfe6gsgkg09.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2503118">
<div align="center">
<img id="aimg_989886" aid="989886" zoomfile="https://di.gameres.com/attachment/forum/202107/05/094303hfg0wjfe6gsgkg09.jpg" data-original="https://di.gameres.com/attachment/forum/202107/05/094303hfg0wjfe6gsgkg09.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/05/094303hfg0wjfe6gsgkg09.jpg" referrerpolicy="no-referrer">
</div><br>
<i><font color="#808080">作者/Rothy，知乎原文地址：</font></i><br>
<i><font color="#808080">https://zhuanlan.zhihu.com/p/210896992</font></i><br>
<br>
本文主要围绕Roguelike类游戏的设计进行一些思考，主要从以下两点出发：<br>
<br>
<ul><li>什么样的游戏可以被称作Roguelike类游戏？</li><li>好的Roguelike类游戏是怎么样的？<br>
</li></ul><br>
<strong>什么样的游戏可以被称作Roguelike类游戏？</strong><br>
<br>
从2008年的柏林诠释开始，众多的Roguelike开发者与爱好者共同制定了，规定了Roguelike游戏需要具备如下的重要元素：<br>
<br>
<ul><li><strong>随机生成地图：</strong>使用过程生成地图来增加可重玩性。</li><li><strong>永久死亡：</strong>角色会永久死亡，存档无法用来从永久死亡状态恢复角色。</li><li><strong>网格化地图：</strong>采用回合制、网格化地图，玩家可以有足够的时间思考每一步的决策。</li><li><strong>非模式化状态：</strong>玩家可以采取的行动不根据游戏的状态而变化。</li><li><strong>非线性流程：</strong>路线非线性，玩家可以用不同的手段来达成相同的游戏目标。</li><li><strong>资源管理：</strong>具备资源管理玩法，玩家必须合理配置其资源的消耗来最大化生存的可能。</li><li><strong>核心战斗：</strong>专注于怪物战斗，玩家没有和平选项来跳过战斗。</li><li><strong>鼓励探索：</strong>鼓励玩家探索地图来获取随机分布在地图上的各类道具。<br>
</li></ul><br>
<strong>常见的Roguelike类（包括Roguelite）游戏有：</strong><br>
<br>
<ul><li>以撒的结合：地牢类的Roguelike</li><li>死亡细胞：类银河恶魔城风格的Roguelike</li><li>杀戮尖塔：卡牌构筑Roguelike</li><li>元气骑士：像素地牢Roguelike<br>
</li></ul><br>
<br>
<div align="center">
<img id="aimg_989887" aid="989887" zoomfile="https://di.gameres.com/attachment/forum/202107/05/094304tsa2kcqq1f1fwsqq.jpg" data-original="https://di.gameres.com/attachment/forum/202107/05/094304tsa2kcqq1f1fwsqq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/05/094304tsa2kcqq1f1fwsqq.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">以撒的结合</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_989888" aid="989888" zoomfile="https://di.gameres.com/attachment/forum/202107/05/094304k59fv7uq9zu09o9o.jpg" data-original="https://di.gameres.com/attachment/forum/202107/05/094304k59fv7uq9zu09o9o.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/05/094304k59fv7uq9zu09o9o.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">死亡细胞</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_989889" aid="989889" zoomfile="https://di.gameres.com/attachment/forum/202107/05/094304w8ykoh6rkw5yyh1h.jpg" data-original="https://di.gameres.com/attachment/forum/202107/05/094304w8ykoh6rkw5yyh1h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/05/094304w8ykoh6rkw5yyh1h.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">杀戮尖塔</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_989890" aid="989890" zoomfile="https://di.gameres.com/attachment/forum/202107/05/094305z1wndiiiiqd0lize.jpg" data-original="https://di.gameres.com/attachment/forum/202107/05/094305z1wndiiiiqd0lize.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/05/094305z1wndiiiiqd0lize.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">元气骑士</font></font></div><br>
但随着时间的推移，如今的游戏早已不全满足以上的条件，大多没有网格化的地图，也并非再是回合制。因此，继续沿用极其细致的游戏内容来规定这个游戏大类早已没有必要。在我看来，如今的Roguelike类游戏主要满足以下三大内容：<br>
<br>
<ul type="1" class="litype_1"><li>随机内容</li><li>永久死亡</li><li>资源管理<br>
</li></ul><br>
<strong>好的Roguelike游戏是怎么样的？</strong><br>
<br>
根据之前所说的三个三大内容，可以总结出一款好的Roguelike游戏需要以下几个特点：<br>
<br>
<strong>1、随机内容：丰富且平衡的决策池</strong><br>
<br>
<ul><li>丰富的装备、增益搭配：提供多种包含不同玩法、效果的装备和增益。</li><li>有效的装备、增益搭配：装备和增益之间需要存在一定的协同效应，即1+1>2。</li><li>玩家的所有决策收益都必须和当下的游戏状态紧密相连，鼓励玩家接受局部最优解。<br>
</li></ul><br>
<strong>2、永久死亡：提供一定措施挽回单个循环内的死亡</strong><br>
<br>
<ul><li>S/L机制</li><li>额外的道具组合<br>
</li></ul><br>
<strong>3、资源管理：有深度的成长组合</strong><br>
<br>
<ul type="1" class="litype_1"><li>局内成长：强调单局体验，关注当下的局部最优解，避免出现长期全局最优解。</li><li>局外成长：主导玩家的长期决策，延长游戏可玩性。<br>
</li></ul><br>
<strong><font color="#de5650">永久死亡</font></strong><br>
<br>
永久死亡的机制，意味着玩家每回合需要从零开始挑战，意味着上一回合内所做的努力在一定程度上前功尽弃，并且依旧需要玩家去重新游玩大致相同的游戏流程。在这期间对于玩家来说，完全的前功尽弃一定程度上会提高其心理负担，而S/L机制能够在一定程度上帮助玩家逃避永久死亡带来的惩罚；除此之外，游戏中还可以通过额外的游戏道具，例如杀戮尖塔中的遗物和药水，来帮助玩家提高其整体实力强度，从而降低死亡发生的概率，能够专注于游戏本身。<br>
<br>
<strong><font color="#de5650">随机内容</font></strong><br>
<br>
Roguelike游戏给予玩家最直接的感受即是<strong>不确定性</strong>——包括地图的随机和游戏中一系列其他随机生成的内容（装备、增益等）。从叙事角度看，玩家每回合的游戏经历都具备唯一性与不可回溯性，而当玩家通关或是死亡之后，不仅会失去那段游戏时间的努力，也会失去那段时间内的记忆。因此，在永久死亡机制下，过程生成系统及其带来的非线性体验，对于玩家来说具有一定的两面性，能够避免内容的高度重复，带来独特的游玩体验，但这种体验都是无法重复和记录的。<br>
<br>
而一个游戏的“决策池”，则是玩家当下能进行的、对游戏会产生深远影响的行为总和。根据“有意义的选择”这一观点，<strong>所有的决策收益都必须和当下的游戏状态紧密相连</strong>。而引入随机元素制造非线性体验的有两个重要目标：<br>
<br>
<ul><li>让玩家做决策时面临的情况更加丰富</li><li>鼓励玩家接受局部最优解<br>
</li></ul><br>
<br>
随机内容使得玩家选择极难达成全局最优，必须必须接受“非最优”的选择无处不在这个事实，关注当下的局部最优解，减少玩家追求长期全局最优解的动力，把精力转向“继续游戏”这件事情上。<br>
<br>
然而对于缺乏经验的玩家来说，在一个高度随机的游戏中，很难时刻分辨游戏中的的决策优劣和当前游戏状况。因此，当角色死亡的高惩罚到来之时 ，玩家可能会倾向归因为“这游戏没教会我，我才失败的”，甚至是“运气不好才失败的”，而不是“之前有几个决策做的不对，才失败的”。这样的决策系统，即使玩家失败了，想要从头再来，学习如何掌握这样的游戏，也会因为缺少相关的线索而无从下手。<br>
<br>
<strong><font color="#de5650">资源管理</font></strong><br>
<br>
Roguelike在资源管理层面，是更多地运用于“局外”的游戏养成部分。资源管理使玩家在战前的准备和战斗的结果上能够<strong>得到量化</strong>，主导长期决策，便于玩家从中学习。虽然有随机因素的干扰，但玩家资源越多的地方，在这上面得到的帮助也越大；在玩家失败并接受删档惩罚的时候，可以从资源的角度分析失败的原因，从而在下次重来时重新配置资源分配。而有深度的资源管理玩法，需要规避出现的一种情况是，全局最优解可以很容易通过数值意义上的迭代来逼近和达成；而在Roguelike这里，随机生成的游戏内容恰好一定程度隐藏和限制了全局最优解，帮助达到了延长游戏可重玩性的目的。但仍需注意的是例如战魂铭人中的吸血装备，由于其效果，在游戏过程中出现后对于玩家来说仍有着相较于其他装备更高的选择优先级，在一定程度上是不平衡的，<br>
<br>
<strong><font color="#de5650">额外的</font></strong><br>
<br>
除了以上所说的三大点之外，以下的一些特质同样能够帮助Roguelike游戏的可玩性锦上添花：<br>
<br>
<ul><li>教学式的关卡设计：阶段式的实战教学，有效地帮助玩家验证当前自身实力强度</li><li>重复体验成本降低：有效的增强了游戏的前期差异，减轻前期的重复体验成本</li><li>游戏内容介绍图鉴：收集图鉴允许玩家查看已获取的内容并且清楚地阐明其效果<br>
</li></ul><br>
总的来说，优秀的Roguelike游戏需要让玩家有充足的动力去挑战随机生成的内容，游戏中的有多样的情形等待着玩家，其所做的决策都有协同的收益和一定的风险，并通过结合长线的资源管理让玩家有成长感同时可以承受永久死亡带来的损失。<br>
<br>
<strong>然而，Roguelike游戏后期无法避免的其游玩性价比会逐渐降低，可以通过以下方式来提高游戏的可玩性：</strong><br>
<br>
<ul><li>加入间接PVP玩法，结合Roguelike成长机制，让玩家比拼成长速度和效果</li><li>随机道具带有适当的负面反馈，让道具组合也带有一定的博弈性<br>
</li></ul><br>
<strong>除此之外，Roguelike游戏仍有一些避免不了的问题：</strong><br>
<br>
<strong>有限的游戏难度：</strong>Roguelike高度随机的关卡、怪物和奖励除了考验玩家的运气和对游戏机制的了解以外，很难有其他拔高难度的做法；而后者是会很快被玩家摸清的，导致高难度的回合制roguelike在压榨数值时，往往变成一个纯看脸的游戏，看脸的游戏结合高死亡惩罚会带来无效的重复劳动和糟糕的体验。<br>
<br>
<strong>孱弱的游戏剧情：</strong>非线性的游戏的游戏结构导致其无法有效地为叙事创造条件，玩家无法与游戏角色具备紧密的情感联结。例如在<死亡细胞>中，通常在玩家达成一定条件、通关后才能够触发剧情的发生，玩家在游戏过程中能够找到的更多的只是类似于剧情线索的设置，无法有效地营造代入感。<br>
<br>
<strong>玩法与叙事能力结合的不足：</strong>游戏的玩法和叙事的融合能力，从商业角度上很大程度决定了该游戏与竞品相比的差异，而Roguelike游戏往往更注重其核心玩法的打磨，但一旦打磨不成功便很难在同类中制造足够的区分度，这也是许多Roguelike游戏带给玩家的体验都没有大的变化的原因。<br>
<br>
<i><font size="2"><font color="#808080"></font></font></i><br>
<i><font size="2"><font color="#808080">来源：https://zhuanlan.zhihu.com/p/210896992</font></font></i><br>
</td></tr></tbody></table>



  
</div>
            