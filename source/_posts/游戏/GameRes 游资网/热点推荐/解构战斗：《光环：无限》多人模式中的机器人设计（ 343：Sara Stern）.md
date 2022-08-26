
---
title: '解构战斗：《光环：无限》多人模式中的机器人设计（ 343：Sara Stern）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/22/090919i9wwiryyiv9wlr9d.gif'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://di.gameres.com/attachment/forum/202208/22/090919i9wwiryyiv9wlr9d.gif'
---

<div>   
<div align="center">
<img aid="1050938" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090919i9wwiryyiv9wlr9d.gif" data-original="https://di.gameres.com/attachment/forum/202208/22/090919i9wwiryyiv9wlr9d.gif" width="600" id="aimg_1050938" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090919i9wwiryyiv9wlr9d.gif" referrerpolicy="no-referrer">
</div><div align="left"><i><font size="2"><font color="#808080">本文首发公众号“网易雷火UX用户体验中心”</font></font></i></div><br>
GDC是全球游戏行业最具规模、最有权威、最有影响力的专业峰会。每年的GDC大会上，全球顶尖的游戏开发者们将齐聚在这里，交流彼此的想法，构想游戏业的未来方向。<br>
<br>
<div align="center">
<img aid="1050939" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090920h00jij7skxjsem0t.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090920h00jij7skxjsem0t.png" width="600" id="aimg_1050939" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090920h00jij7skxjsem0t.png" referrerpolicy="no-referrer">
</div><br>
本篇为大家介绍的是来自343工作室的资深多人游戏设计师Sara Stern的演讲“Deconstructing the Combat Dance: Designing Multiplayer Bots for 'Halo Infinite'”。<br>
<br>
<div align="center">
<img aid="1050940" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090920sg7imvmfkgix5uyk.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090920sg7imvmfkgix5uyk.png" width="179" id="aimg_1050940" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090920sg7imvmfkgix5uyk.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Sara Stern</font></font></div><div align="center"><font size="2"><font color="#808080">Senior Multiplayer Designer, 343 Industries</font></font></div><br>
<i><font color="#808080">演讲标题：</font></i><br>
<i><font color="#808080">Deconstructing the Combat Dance: Designing Multiplayer Bots for 'Halo Infinite'</font></i><br>
<i><font color="#808080">解构战斗：《光环：无限》多人模式中的机器人设计</font></i><br>
<br>
<strong><font color="#de5650">演讲者信息：</font></strong><br>
<br>
Sara Stern，343工作室的资深多人游戏设计师，负责多人游戏模式中AI机器人的设计。她于2016年加入343工作室，一直从事《光环5：守护者》的持续性开发和运营工作，一年半前转入《光环：无限》游戏的开发。<br>
<br>
<strong><font color="#de5650">演讲概述：</font></strong><br>
<br>
《光环无限》是第一款在多人模式中投放AI机器人的光环系列游戏，团队从一个明确的设计目标开始：创建不同水平的AI机器人，帮助玩家进行训练。通过本篇演讲，观众可以了解到开发团队是如何进行AI机器人设计的：观察玩家游玩游戏的过程，并确定《光环无限》中机器人需要执行的一系列核心操作来模拟玩家行为。<br>
<br>
<strong><font color="#de5650">一、关于《光环:无限》</font></strong><br>
<br>
《光环:无限》是《光环5》的续作，是一款开放世界FPS游戏，这也是343工作室第一次发行免费游戏。玩家在《光环》中扮演的是斯巴达战士（Spartan），战斗中，一旦玩家遭遇攻击，首先会消耗包裹全身的能量护盾，护盾值耗尽后受伤才扣血，在破盾时斯巴达战士也会暴露出脆弱的肉身（一个爆头、近战攻击足以击杀），而玩家保持几秒不受伤后，护盾、血量又都会快速回满。<br>
<br>
<div align="center">
<img aid="1050941" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090921ira6q82evz8j288j.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090921ira6q82evz8j288j.png" width="600" id="aimg_1050941" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090921ira6q82evz8j288j.png" referrerpolicy="no-referrer">
</div><br>
《光环：无限》的一大亮点是在游戏中加入了多人模式，并在该模式中首次加入AI机器人。机器人在帮助玩家快速匹配，训练新手快速上手，制造温暖局方面发挥着相当重要的作用，因此如何对机器人进行设计就变得十分关键。<br>
<br>
<ul><li>首先，由于每名玩家的游戏水平不一样，其掌握的射击技巧也不同，所以机器人设计的目标之一是：创建帮助玩家训练的机器人；</li><li>其次，因为新手玩家在游戏中很难找到与其水平相当的对手，所以机器人设计目标之二是为玩家提供与其水平匹配的对手；</li><li>最后，演讲者回顾自己在《光环5》工作中遇到的一个问题是，很多高段位玩家在打排位赛之前想要体验几局不影响自己排名的匹配赛，所以机器人设计另一个目标是为高段位玩家提供“陪练”。<br>
</li></ul><br>
综上，演讲者认为在为《光环：无限》多人模式设计机器人时，首要目标是确保他们能帮助不同水平的玩家进行训练。<br>
<br>
<div align="center">
<img aid="1050942" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090921ir3zvqvjric3wznr.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090921ir3zvqvjric3wznr.png" width="600" id="aimg_1050942" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090921ir3zvqvjric3wznr.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">二、如何设计《光环：无限》中的机器人</font></strong><br>
<br>
玩家在游戏中会表现出什么样的行为呢？演讲者根据玩家的游戏水平将其分成四种类型：<br>
<br>
<ul><li>第一等级的玩家对游戏非常不熟悉，每一个按键对他们来说都很陌生；</li><li>第二等级的玩家则专注在当前的游戏中，会思考在战斗中应该选择哪种武器等问题；</li><li>第三等级的玩家玩游戏很有信心，会思考游戏策略，例如应当在什么时间夺取敌队的旗帜；</li><li>最高等级的玩家，会思考如何优化游戏，他们会关心非常具体的问题，例如地图上的最佳位置在哪？<br>
</li></ul><br>
<div align="center">
<img aid="1050943" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090921i4nktk2j8kwvte26.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090921i4nktk2j8kwvte26.png" width="515" id="aimg_1050943" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090921i4nktk2j8kwvte26.png" referrerpolicy="no-referrer">
</div><br>
怎样帮助玩家训练以提升他们的游戏水平呢？<br>
<br>
演讲者认为，对于新手玩家，可以投放一些比他们更不熟悉游戏的机器人，让新手玩家体验在游戏中击败敌人的快乐；对于从第一等级过渡到第二等级的玩家，需要投放一些有一定操作水平的机器人，让玩家感觉到充满挑战性，但并不会立即杀死玩家；对于从第二等级升到第三等级的玩家，可以投放一些操作水平更高的机器人，能真正迫使玩家学习战斗的基础知识，开始思考游戏策略问题。最后，为那些技术高超的玩家投放一些操作技巧熟练的机器人，让他们能够练习比较具体的技能，比如对真正动态移动的对手进行狙击。<br>
<br>
<div align="center">
<img aid="1050944" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090922fzkwhk5owfks4olw.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090922fzkwhk5owfks4olw.png" width="514" id="aimg_1050944" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090922fzkwhk5owfks4olw.png" referrerpolicy="no-referrer">
</div><br>
如果将不同水平玩家的行为模式复刻到机器人身上，那么就可以确保玩家匹配到的是与之游戏水平相当的机器人。因此，演讲者及其团队花费了大量时间观看游戏视频，观察不同水平的人类玩家所表现出的战斗行为，记录这些战斗行为是什么，并分析这些战斗行为出现的时间，最后，再试图去解决机器人学习这些行为可能存在的难题。<br>
<br>
<div align="center">
<img aid="1050945" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090922vqdlbnw6jl56unmz.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090922vqdlbnw6jl56unmz.png" width="600" id="aimg_1050945" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090922vqdlbnw6jl56unmz.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">三、分析玩家的战斗行为</font></strong><br>
<br>
《光环：无限》的开发团队提出，“《光环》中的战斗行为是一种动态的参与节奏，是反应式的、脑力式的舞蹈，感觉像是交响乐”，演讲者延续该理念，认为玩家的战斗行为可以分成：扫射、瞄准、投掷手榴弹、近战，以及掌握继续战斗或逃离的时间五种技能，不同水平的玩家在操作这五种技能时会表现出不同的行为模式。<br>
<br>
<div align="center">
<img aid="1050946" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090922bbk43s6ub4h4a736.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090922bbk43s6ub4h4a736.png" width="600" id="aimg_1050946" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090922bbk43s6ub4h4a736.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">扫 射</div><br>
扫射包含4种基本的运动模式：相对于目标的左右水平移动，以跳跃和蹲起的形式移动或躲避攻击，根据敌人的行动来确定自身行动的时间，以及各种行为的复杂组合。<br>
<br>
<div align="center">
<img aid="1050947" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090923pippn5n11vz15908.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090923pippn5n11vz15908.png" width="488" id="aimg_1050947" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090923pippn5n11vz15908.png" referrerpolicy="no-referrer">
</div><br>
那么不同水平玩家的扫射行为是怎样的呢？新手玩家一般只会往前冲，他们很难同时控制扫射和移动的按键；第二等级的玩家能够进行水平移动，控制和对手的距离，并且可以同时进行这两个操作；第三等级的玩家能够在水平移动的基础上增加跳跃的操作；最高水平玩家的动作是非常复杂的，因为这种类型的玩家适应了高操作水平的对手，他们需要通过更高难度的操作以保证生存并击败对手，能够在短时间内可以做出多种行为的操作组合。<br>
<br>
<strong>瞄 准</strong><br>
<br>
遵循与扫射行为相同的过程，演讲者分析了不同水平玩家的瞄准行为。新玩家的瞄准射击水平较低，并且他们对武器的使用和射击距离的把握也很陌生；第二等级的玩家可以更加精确的瞄准目标，并且能考虑到在对方护盾值较低的时候去爆头；第三等级玩家可以轻松地瞄准敌方，并在瞄准时开始考虑武器的后坐力；最高水平的玩家即使在游戏全速进行时，也不会发生任何瞄准错误。<br>
<br>
通过分析，演讲者认为瞄准的要点包括：瞄准准确性（即下图中的绿色圆圈范围），瞄准器到目标的距离，瞄准目标的速度，跟踪目标运动方向变化的反应能力，以及高水平玩家能预期目标出现的位置并进行瞄准的能力。<br>
<br>
<div align="center">
<img aid="1050948" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090923rqruev88cu33e4rd.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090923rqruev88cu33e4rd.png" width="543" id="aimg_1050948" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090923rqruev88cu33e4rd.png" referrerpolicy="no-referrer">
</div><br>
<strong>投掷手榴弹</strong><br>
<br>
当比赛开始时，玩家的库存中会备有手榴弹，手榴弹能够造成较大范围的伤害。低水平的玩家在游戏中往往不会使用手榴弹，因为瞄准，移动和射击等操作对他们来说已经足够复杂；更有经验的玩家，会在近战或者当战斗进行到最后的时候使用，以期给失去视线的对手造成致命伤害；最高水平的玩家往往会花很多时间，用手榴弹来控制对手在战场上的移动位置，而不是直接把手榴弹扔向目标。<br>
<br>
综上，投掷手榴弹的技巧包括：投掷准确性，根据手榴弹类型确定其投掷位置，根据目标护盾的状态改变手榴弹投掷时间，把手榴弹扔在想阻止对手去的地图区域，以及把手榴弹扔到预期对手会出现的位置。<br>
<br>
<div align="center">
<img aid="1050949" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090923vd3162q1c3c2u422.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090923vd3162q1c3c2u422.png" width="532" id="aimg_1050949" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090923vd3162q1c3c2u422.png" referrerpolicy="no-referrer">
</div><br>
<strong>近 战</strong><br>
<br>
近战会产生巨大的伤害值，而且是快速结束战斗的好方法。新手玩家要做到保持对敌方位置的追踪并同时按下近战按钮是非常困难的；较高等级的玩家，能够判断双方的战斗状态，会在观察到对手处于失利状态时开启近战；最高等级的玩家，他们已经完全掌握了每种类型的武器能够造成的伤害值，会通过近战打击获得巨大杀伤力，当这些玩家觉得有信心在不危及自己的情况下击杀对手时，就会拉近和对手的距离，开展近战。因为近战时间短，玩家最需要考虑的是对手的护盾状态，以及估计能造成多少伤害值。<br>
<br>
综上，近战技巧的要点包括：一般的瞄准技能；基于敌人的护盾状态确定开展近战的时间；当自身处于优势时，拉近与对手的距离开展近战。<br>
<br>
<div align="center">
<img aid="1050950" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090923cd9yzpj9jccbzb8p.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090923cd9yzpj9jccbzb8p.png" width="551" id="aimg_1050950" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090923cd9yzpj9jccbzb8p.png" referrerpolicy="no-referrer">
</div><br>
<strong>选择持续或结束战斗</strong><br>
<br>
演讲者及其团队对游戏经验丰富的玩家做了大量的访谈，总结出决定玩家结束战斗的因素包括：与对手之间的距离，玩家自身的弹药状态，玩家自身和对手的护盾状态，地理位置情况。同时，玩家做出决策前也需要掌握两点：第一，护盾、弹药和射击距离等概念的重要性，如果玩家没有护盾，那么再多的弹药也毫无用处；第二，玩家需要对自身以及对手的技术水平有清晰的认知。<br>
<br>
<div align="center">
<img aid="1050951" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090924z8z11b680l1lb805.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090924z8z11b680l1lb805.png" width="600" id="aimg_1050951" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090924z8z11b680l1lb805.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">四、AI机器人战斗行为的例子</font></strong><br>
<br>
总结出不同水平玩家所表现出来的行为模式后，接下来团队需要考虑的就是如何在机器人设计中复刻这些行为。<br>
<br>
机器人行为设计的过程包括：观察人类行为；与优秀的工程团队合作，在现有的人工智能代码库中创建观察到的行为模式；确定投放机器人的大致时间；以及对机器人动作进行随机的变化，确保它们始终是动态的。演讲者以扫射以及选择持续或结束战斗的行为为例，讲解了其团队在设计机器人时是如何做的。<br>
<br>
<div align="center">
<img aid="1050952" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090924gnk92tkn9ayonww8.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090924gnk92tkn9ayonww8.png" width="552" id="aimg_1050952" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090924gnk92tkn9ayonww8.png" referrerpolicy="no-referrer">
</div><br>
<strong>机器人扫射行为</strong><br>
<br>
前面已经确定了人类玩家扫射的基本运动模式，所以只需要让机器人学习同样的行为：当感受到处于敌人的火力之下，机器人会相对于目标向前和向后移动，也会跳跃和蹲下以躲避对手的攻击。<br>
<br>
<div align="center">
<img aid="1050953" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090924ele7l93k63jmn83l.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090924ele7l93k63jmn83l.png" width="488" id="aimg_1050953" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090924ele7l93k63jmn83l.png" referrerpolicy="no-referrer">
</div><br>
但是，扫射技能是基础运动模式的高度复杂组合，所以在设计时需要额外做一些参数调整。演讲者及其团队开发了一套流程，能够复刻不同技能水平玩家的扫射模式，其中最重要的一些参数是：在改变方向之前朝某一方向扫射的时间，在扫射过程中的暂停，停顿时间的长短，跳跃的时机，蹲下的时机，以及保持蹲下的时间。通过各种方式组合这些不同的变量，直到机器人的最终表现与不同水平的人类玩家相匹配。<br>
<br>
<strong>机器人选择逃跑或持续战斗</strong><br>
<br>
首先，机器人可以读取玩家生命值和护盾状态的数据，并且需要对不同值进行权重分析，如护盾状态比弹药更重要。然后，根据读取的数据进行分析输出一个数值，代表机器人的自信程度，如果这个数值高，应该选择持续战斗，如果数值低，则代表需要撤退，此时，机器人会试图找到一种方法来干扰对手的视线。<br>
<br>
下图是机器人信心计算的公式，将对手的护盾状态，自身的护盾状态，目标距离，自身武器状态以及与对手之间的距离差，五个数值进行归一化，并赋予这些值不同的权重，最后加和得到的值再归一化，输出0-1范围内的自信心数值，以此作为选择逃跑还是继续战斗的依据。<br>
<br>
<div align="center">
<img aid="1050954" zoomfile="https://di.gameres.com/attachment/forum/202208/22/090924efdjfx6356dd4r6j.png" data-original="https://di.gameres.com/attachment/forum/202208/22/090924efdjfx6356dd4r6j.png" width="583" id="aimg_1050954" inpost="1" src="https://di.gameres.com/attachment/forum/202208/22/090924efdjfx6356dd4r6j.png" referrerpolicy="no-referrer">
</div><strong><font color="#de5650">总结</font></strong><br>
<br>
演讲者团队通过观察和分析人类玩家的战斗行为，确定了《光环：无限》机器人需要执行的核心操作和行为集合。通过对人类玩家行为的模拟，AI机器人提供了一个有效的学习工具，可以帮助玩家提高在多人游戏中的水平。虽然很多动作是《光环：无限》游戏所特有的，但识别和模拟人类游戏行为的过程，也适用于在其他游戏中建立类似人工智能的团队。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：网易雷火UX用户体验中心</font></font><br>
<br>
  
</div>
            