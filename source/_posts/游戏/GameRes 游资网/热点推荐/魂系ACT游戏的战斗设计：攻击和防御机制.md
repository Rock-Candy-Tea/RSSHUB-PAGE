
---
title: '魂系ACT游戏的战斗设计：攻击和防御机制'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202204/02/091845whdzrd9902zn2pt1.jpg'
author: GameRes 游资网
comments: false
date: Sat, 02 Apr 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202204/02/091845whdzrd9902zn2pt1.jpg'
---

<div>   
<div align="center">
<img aid="1035483" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091845whdzrd9902zn2pt1.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091845whdzrd9902zn2pt1.jpg" width="600" id="aimg_1035483" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091845whdzrd9902zn2pt1.jpg" referrerpolicy="no-referrer">
</div><font size="2"><font color="#808080"><strong>作者：王鑫然</strong></font></font><br>
<font size="2"><font color="#808080">首发知乎:https://zhuanlan.zhihu.com/p/484068545</font></font><br>
<br>
<strong><font color="#de5650">一、前言</font></strong><br>
<br>
本文讨论的是魂系ACT游戏中的战斗设计，但也会简单涉及一些其他类型的ACT。对于魂系游戏，笔者并不是一位魂吹，笔者体验魂系游戏主要是为了学习、借鉴其优秀的游戏设计思路，然后融合到自己的设计风格里。<br>
<br>
文章中的观点为笔者对于魂系游戏的一些思考，并不权威。内容不涉及有付费成长线的设定，因为会很复杂。对思考部分，可能会与魂系游戏战斗设定相同，也可能完全不同。由于写本文时并没有查看其他资料，所以文中的名词，多为笔者自行定义。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1035484" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091845xmfl8j7q8fvxjjmj.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091845xmfl8j7q8fvxjjmj.jpg" width="515" id="aimg_1035484" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091845xmfl8j7q8fvxjjmj.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">英雄帕奇镇楼</font></font></div><br>
文中的内容，主要是对基础机制设计的讨论，仅仅占实际战斗机制设计中的极小部分，实际战斗设计还会包含模型、动作、特效、武器、防具、天赋、技能、AI设定、付费成长设计等内容。本文逻辑推导部分居多，可能会有些晦涩难懂。<br>
<br>
<strong><font color="#de5650">二、策略性的ACT攻防机制是怎么设计出来的</font></strong><br>
<br>
先看一个最简单的即时战斗场景，有AB两个单位，仅有血量、攻击、100%命中这三种战斗属性，这两个单位面对面拿着刀，站桩互砍。<br>
<br>
<div align="center">
<img aid="1035485" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091846w3apd3vvav3183h9.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091846w3apd3vvav3183h9.jpg" width="600" id="aimg_1035485" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091846w3apd3vvav3183h9.jpg" referrerpolicy="no-referrer">
</div><br>
假设AB的各项属性和能力完全一样，若AB一方率先出刀，则这一方必胜，整个战斗过程仅仅是一个等量数值的相互比拼，结果取决于谁先手伤害，且结果毫无悬念，很无趣，为解决这个问题，我们将战斗过程赋予攻防策略，降低先手优势，提高攻防转换频率，并不断加深策略。<br>
<br>
首先，给单位赋予举盾防御（下文简称为防御）能力。防御可以将对方的攻击按照一定百分比抵消（百分比≠100%，因为如果是100%抵消，只要B举着盾牌，A就永远无法对B造成伤害），防御时无法进行攻击。在一次防御行为中，单位可以一直举盾，直到成功抵挡一次攻击或主动解除防御状态。<br>
<br>
为了让防御方能够准确观察攻击方的攻击行为，知道何时应该举起盾牌防御，必须对战斗动作做出信息提示，为此，我们将一个完整的战斗动作分为前摇、生效、后摇三个部分，并规定动作一旦开始便不能被自己强制打断。<br>
<br>
对于攻击动作（以拿刀挥砍动作为例）：<br>
<br>
<ul><li><strong>前摇</strong>指的是挥砍动作开始执行到正式砍到对方身上的这段时间。这个阶段动作开始但并没有造成伤害。防御方可以通过攻击方是否开始攻击前摇来判断攻击方是否要进行攻击。</li><li><strong>生效</strong>指的是砍到对方身上到开始收刀，在生效阶段内，只要刀碰到对方模型的伤害判定体，就可以造成一次性瞬间伤害。</li><li><strong>后摇</strong>指的是开始收刀到恢复战斗待机动作。<br>
</li></ul><br>
<div align="center">
<img aid="1035486" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091846q41731aj4ro1j712.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091846q41731aj4ro1j712.jpg" width="600" id="aimg_1035486" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091846q41731aj4ro1j712.jpg" referrerpolicy="no-referrer">
</div><br>
对于防御动作：<br>
<br>
<ul><li><strong>前摇</strong>指的是举盾动作开始执行到盾牌完全举起的这段时间。这个阶段防御动作开始但并没有防御攻击的能力。攻击方可以通过查看防御方是否开始防御动作前摇，来判断防御方是否要进行防御。</li><li><strong>生效</strong>指的是盾牌完全举起到开始收盾，在举盾期间始终拥有防御攻击的能力，收盾的触发条件是自身主动放下盾牌或成功防御对方的一次攻击。</li><li><strong>后摇</strong>指的是开始收盾到恢复战斗待机动作。<br>
</li></ul><br>
<div align="center">
<img aid="1035487" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091846eurijsuxkjitjaad.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091846eurijsuxkjitjaad.jpg" width="600" id="aimg_1035487" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091846eurijsuxkjitjaad.jpg" referrerpolicy="no-referrer">
</div><br>
实际在战斗配置中，通过时间（ms）设定来划分前摇、生效、后摇三段时间，技术在读取时间后再把它转换到动作帧上。一些动作在设定动作时间机制时会比较特殊，比如在《艾尔登法环》中，经常看到的BOSS先跳上天，再从天上朝玩家蹦下来，有些动作机制则是多种动作机制结合的产物，比如截肢葛瑞克拖着斧子向玩家走过来抡大斧的那个技能，这里就不展开讲了。<br>
<br>
我们再回到对战，当AB两个单位对战时，总会有一方先发动攻击，假设A先发动攻击，从A攻击开始，到攻击结束，我们称其为一个攻击回合。<br>
<br>
在A对B进行攻击的这个攻击回合中，可能会发生以下情况：<br>
<br>
<ul><li>A的攻击被B防御，伤害被抵消了一部分</li><li>A的攻击没有被B防御，A攻击对B造成100%伤害。<br>
</li></ul><br>
如果B一直使用防御，而不去攻击，则最终A会赢得对局，我们希望B有意愿从防御方转为攻击方，完成一次攻防互换。同时要让攻击方A有使用防御的需求。<br>
<br>
为解决这个问题，需要给防御增加一个使用限制。可以是CD，或者是使用时额外的能量消耗，亦或者其他方式，这里暂且不设定具体使用限制是什么，无论如何，单位将无法持续的使用防御。<br>
<br>
为了赢得对局的胜利，B必须在无法使用防御时，对A发动攻击，否则B就会被动挨打掉血。但新的问题又出现了，如果B发起进攻时，A开始使用防御，最终这场对局又变回了先手必胜。我们需要为战斗创造更多变数，使防御或进攻有失效的机会。<br>
<br>
<div align="center">
<img aid="1035488" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091847d7naxaqdzxp3x0c0.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091847d7naxaqdzxp3x0c0.jpg" width="600" id="aimg_1035488" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091847d7naxaqdzxp3x0c0.jpg" referrerpolicy="no-referrer">
</div><br>
为此，我们增加高风险高收益的攻击和防御机制，让单位愿意去冒险应对，当单位应对失败时，会为对手创造造成伤害的时机。为了控制一个完整攻防转换的时间，每一种攻击或防御机制都将消耗能量。<br>
<br>
最终的攻击、防御及其他机制如下：<br>
<br>
<ul><li><strong>能量值：</strong>攻击和防御行为消耗的资源，数值可以小于零，单位的能量上限固定为100，单位能量值为0时，被攻击命中会僵直。当单位当前能量值不足时，依然可以释放攻击或防御，但会将能量值降到0以下。当单位不攻击防御且不被击时，能量值恢复。</li><li><strong>僵直：</strong>单位短时间内会不能攻击、防御的状态。</li><li><strong>轻击：</strong>消耗10能量释放，动作时间短，前摇时间短，造成伤害低。</li><li><strong>重击：</strong>消耗20能量释放，动作时间长，前摇时间长，生效时间短，造成伤害高，造成伤害时降低目标30能量，若命中使目标能量值降到0，则目标僵直。</li><li><strong>盾防：</strong>同上文中举盾防御，防御时被击中消耗13能量，防御成功抵消50%伤害。</li><li><strong>盾反：</strong>消耗20能量释放，用盾牌瞬间弹开对方的攻击，使自身免于伤害，并使攻击方能量值减少30。前摇时间略短于轻击前摇，明显短于重击前摇，生效时间短。<br>
</li></ul><br>
<div align="center">
<img aid="1035489" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091847dm00g9d18n0db15d.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091847dm00g9d18n0db15d.jpg" width="600" id="aimg_1035489" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091847dm00g9d18n0db15d.jpg" referrerpolicy="no-referrer">
</div><br>
这样设定后，AB两个单位就同时拥有了“低风险低收益攻防手段”和“高风险高收益攻防手段”。AB之间的攻防出现了以下情景：<br>
<br>
<ul><li><strong>A使用轻击，B不防御也不攻击。</strong>A消耗10能量，B受到A的100%轻击伤害。</li><li><strong>A使用重击，B不防御也不攻击。</strong>A消耗20能量，B消耗30能量，B受到A的100%重击伤害。</li><li><strong>A使用轻击，B使用轻击。</strong>AB均消耗10能量，均受到对方100%轻击伤害。</li><li><strong>A使用重击，B使用轻击。</strong>A消耗20点能量，对B造成100%重击伤害。B消耗40点能量，对A造成100%轻击伤害。</li><li><strong>A使用重击，B使用重击。</strong>AB均消耗50能量，均受到对方100%重击伤害。</li><li><strong>A使用轻击，B使用盾防。</strong>A消耗10能量，B防御成功消耗13能量，受到50%轻击伤害；B防御失败消耗13能量，受到100%轻击伤害。</li><li><strong>A使用重击，B使用盾防。</strong>A消耗20能量，B盾防成功，B因为被重击命中和盾防本身能量消耗，最终消耗43能量，受到50%重击伤害；B盾防失败，消耗43能量，受到100%重击伤害。</li><li><strong>A使用轻击，B使用盾反。</strong>若B盾反成功，则B消耗20能量，A因为B的盾反和自身轻击本身的能量消耗，最终消耗40能量；若B盾反失败，则B消耗20能量，受到100%轻击伤害，A消耗10能量。</li><li><strong>A使用重击，B使用盾反。</strong>若B盾反成功，由于盾反成功不会受到伤害，即不会被重击消减能量，则B消耗20能量，A则最终消耗50能量；若B盾反失败，则B消耗50能量，受到100%重击伤害，A消耗20能量。<br>
</li></ul><br>
<br>
<div align="center">
<img aid="1035490" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091847hwwuqwfeu3jyvwkc.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091847hwwuqwfeu3jyvwkc.jpg" width="600" id="aimg_1035490" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091847hwwuqwfeu3jyvwkc.jpg" referrerpolicy="no-referrer">
</div><br>
如果抛开具体动作时间、伤害、血量上限不谈。上述战斗具有以下特点：<br>
<br>
<ul><li>由于能量值的设定，攻击和防御行为都不能持续，这就限制了双方攻防行为的最长时长。</li><li>攻击方不能预测防御方下一次将使用何种防御机制来应对攻击，防御方也不能预测攻击方下一次将使用何种攻击机制来进攻。</li><li>当攻击方的攻击前摇开始时，防御方可以通过观察攻击前摇动作来选择使用何种防御机制，以及使用的时机。</li><li>当一方使用重击攻击，另一方使用盾反成功防御是最优解。</li><li>如果一方先受到伤害，这方不考虑创造机会还击则必定输掉对局。</li><li>如果双方都始终使用攻击而不防御，则造成先手伤害的赢得对局。<br>
</li></ul><br>
在上述修改中，我们创造了一些促进攻防互换的攻击和防御机制。同时也出现了一些问题，比如：<br>
<br>
<ul><li>最后一条，因为AB双方都拥有不同的攻击和防御手段，如果双方都自愿来回互砍，造成先手伤害的赢得对局好像没什么问题，但是在实际战斗设计过程中，我们必须让对局双方都清楚，谁先挨了打，否则双方可能会因为对先手的误判影响攻防决策。</li><li>在即时战斗中，一个攻击或防御的效果拥有越多的计算成分，就越影响玩家快速选择出招，决策的时间就越长。比如重击和盾反中使对方能量降低的设定，由其在ACT游戏中，玩家招数的选择应该更取决于对方当前的出招动作来做瞬间判断，而非对于数值的计算。</li><li>动作时间（及前摇、生效、后摇时间的划分）、伤害、血量上限这三种属性，在真实战斗中，对于实际战斗中招数选择的影响，其实是很大的。<br>
</li></ul><br>
ACT游戏中，若对战双方相互进攻，先被伤害到的一方会表现为僵直。僵直看似简单，但如果要带入上文中的战斗设定中，根据实际的僵直设定不同，将对战斗过程带来质的变化。以僵直持续时间为例：<br>
<br>
<div align="center">
<img aid="1035491" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091847u4qwckqzw0zewkpx.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091847u4qwckqzw0zewkpx.jpg" width="600" id="aimg_1035491" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091847u4qwckqzw0zewkpx.jpg" referrerpolicy="no-referrer">
</div><br>
<ul><li>若A先击中B，把B打出僵直，如果在B的僵直动作结束前，A可以再使出攻击，则B又会进入到僵直，此时在A的能量值降至0之前，A可以一直对B造成伤害，即连击。</li><li>若A先击中B，把B打出僵直，如果在B的僵直结束时，A的本次攻击动作后摇部分依然没有结束，若存在一种攻击机制，这个攻击机制的前摇比任何防御机制的前摇动作都短，A的攻击后摇结束时，即便立即使用防御机制也来不及成功防御这个攻击机制，则B可以使用这个攻击机制对A进行攻击，使A进入到僵直，即反击。<br>
</li></ul><br>
将受击僵直带入上文中的攻防设定，再对原本攻防机制进行修改后，我们得到以下攻防机制，修改的部分用加黑标出。<br>
<br>
<ul><li><strong>轻击：</strong>消耗10能量释放，动作时间短，前摇时间短，造成伤害低。击中未防御目标可使目标僵直。</li><li><strong>重击：</strong>消耗15能量释放，动作时间长，前摇时间长，生效时间短，造成伤害高，击中未防御目标可使目标僵直，无视盾防，释放时可免疫轻击僵直。</li><li><strong>盾防：</strong>同上文中举盾防御，防御时被击中消耗8能量，防御成功抵消100%伤害。</li><li><strong>盾反：</strong>消耗15能量释放，用盾牌瞬间弹开对方的攻击，使自身免于伤害。成功防御重击时使攻击方僵直。前摇时间略短于轻击前摇，明显短于重击前摇，生效时间短。<br>
</li></ul><br>
修改后，不同攻防机制之间出现如下关系。<br>
<br>
<div align="center">
<img aid="1035492" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091847sfehzq8shq2fiizy.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091847sfehzq8shq2fiizy.jpg" width="545" id="aimg_1035492" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091847sfehzq8shq2fiizy.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">轻击、盾反、重击、盾防四者克制关系</font></font></div><br>
从克制关系图可以看出，任何一种攻击机制都有相应的防御机制克制，任何一种防御机制也有相应的攻击机制克制。在这种克制关系下，ACT游戏可以打出策略游戏的味道，即魂味的战斗。<br>
<br>
而且在上述攻防机制设定下，先手攻击会相对成为一种劣势，所以AB双方开始对峙时一定是举着盾牌使用盾防面对面站着，然后一方使用重击去克制盾防，打破宁静，假设A用了重击，B看到A使用了重击则会使用盾反进行防御，由于盾反不能百分百防住，失败后的损失很大，但成功的收益也很大，一旦盾反防御成功，A进入僵直，则B可以利用A僵直的这段时间，使用轻击反击A。A从僵直恢复之后再用盾防防住B的轻击，或是再次使用重击，亦或是抓住时机使用轻击将B打出僵直。战斗就在这样的攻防互换中有策略的进行下去，直到一方倒下。<br>
<br>
在上述攻防机制推导过程中，设计了很多有问题的机制设定，但这确是实际战斗设计过程中的常见现象。战斗机制设计和机制平衡调整不像数值设计那样可以简单的使用公式处理，机制设计和机制平衡要在不断地机制修改中迭代下去。当然，如果只做非对称PVE的话，机制平衡和数值平衡就没那么多细节要处理。<br>
<br>
<strong><font color="#de5650">三、职业的划分带来的新机制</font></strong><br>
<br>
上文中，我们假定的AB为同一职业，都可以使用盾牌防御，现在如果要修改一下，B不能使用盾牌，而是一个双持近战，做出职业划分，那么攻防机制又该如何设计？<br>
<br>
<div align="center">
<img aid="1035493" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091848eiqttppxiifkjpqn.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091848eiqttppxiifkjpqn.jpg" width="600" id="aimg_1035493" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091848eiqttppxiifkjpqn.jpg" referrerpolicy="no-referrer">
</div><br>
B可以使用双持武器，意味着他拥有更高的攻击力，可以打出更高的伤害，同时应该承受更高的被伤害风险。我们设定他一旦被打中，就受到100%伤害，没有被打中，则不受伤害。<br>
<br>
在ACT游戏中，有一种防御机制符合以上设定——翻滚。为了加入翻滚，同时要引入移动、转向、指向性攻击（意味着攻击不再是100%命中）、攻击范围4种机制。<br>
<br>
翻滚同样有前摇、生效、后摇的设定：<br>
<br>
<ul><li><strong>前摇：</strong>从翻滚动作开始，到正式发生位移的这段时间。前摇开始时消耗能量，并向角色当前移动方向翻滚。如果前摇过程中，被攻击命中，则翻滚行为被打断。</li><li><strong>生效：</strong>从正式发生位移到位移结束的这段时间。如果生效过程中被攻击命中，则翻滚行为被打断。</li><li><strong>后摇：</strong>位移结束到回到战斗待机动作的这段时间。如果后摇过程中，被攻击命中，则翻滚行为被打断。<br>
</li></ul><br>
有的同学可能会有疑问：你这个翻滚生效时间内不应该有无敌吗？<br>
<br>
是否给翻滚生效时间段设定为无敌，与翻滚能位移的长度有关；也与游戏中怪物的技能设计有关；还与翻滚动作前摇时段时长有关系；甚至与一个指向性技能，它的指向是从前摇开始时判定方向，还是从前摇结束时判定方向有关系，这就是你明明在黑暗弃子那只大蚊子尾巴举起来的时候翻滚，但为什么站起来的时候总是被尾巴抽到的原因。最终是否给翻滚生效时间段设定为无敌，取决于使用翻滚成功避开伤害的难度。在上文中，我们并没有涉及难于避开的伤害，所以这里的翻滚没有无敌。<br>
<br>
<div align="center">
<img aid="1035494" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091848gw7q6kzanknxqsqa.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091848gw7q6kzanknxqsqa.jpg" width="480" id="aimg_1035494" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091848gw7q6kzanknxqsqa.jpg" referrerpolicy="no-referrer">
</div><br>
将翻滚带入，并对上文中攻防机制进行修改后，得出的攻防机制及其他机制如下，修改的部分用加黑标出。<br>
<br>
<ul><li><strong>能量值：</strong>攻击和防御行为消耗的资源，数值可以小于零，单位的能量上限固定为100。当单位当前能量值不足时，依然可以释放攻击或防御，但会将能量值降到0以下。当单位不攻击防御且不被击时，能量值缓慢恢复。</li><li><strong>僵直：</strong>单位短时间内会不能攻击、防御的状态。</li><li><strong>移动：</strong>改变自身位置的能力，移动的速度不足以使近身战斗中的单位躲开攻击。单位可以通过策略的移动来拉开距离，使自身能量值重新回复满。</li><li><strong>转向：</strong>改变模型面向的能力。</li><li><strong>轻击：</strong>消耗10能量向正面100度扇形区域挥砍，攻击距离短，动作时间短，前摇时间短，依据攻击力造成伤害，伤害系数低。动作期间不能转向和位移。击中未防御目标可使目标僵直。</li><li><strong>重击：</strong>消耗15能量向正面100度扇形区域挥砍，攻击距离长，动作时间长，前摇时间长，生效时间短，依据攻击力造成伤害高，伤害系数高，动作期间不能转向和位移。击中未防御目标可使目标僵直，无视盾防，释放时可免疫轻击僵直。</li><li><strong>盾防：</strong>举盾防御来自正面100度范围内伤害，防御时被击中消耗8能量，防御成功抵消100%伤害。</li><li><strong>盾反：</strong>消耗15能量释放，用盾牌瞬间弹开来自正面100度的攻击，使自身免于伤害。成功防御重击时使攻击方僵直。前摇时间略短于轻击前摇，明显短于重击前摇，生效时间短。动作期间不能转向和移动。</li><li><strong>翻滚：</strong>消耗15能量释放，向移动方向位移一段距离，动作时间短于重击前摇时间。<br>
</li></ul><br>
修改后，上述不同攻防机制之间出现如下关系，为方便理解，将AB各自使用的攻防机制用字母标记。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1035495" zoomfile="https://di.gameres.com/attachment/forum/202204/02/091848zmsb4w2mcdcvhhw0.jpg" data-original="https://di.gameres.com/attachment/forum/202204/02/091848zmsb4w2mcdcvhhw0.jpg" width="600" id="aimg_1035495" inpost="1" src="https://di.gameres.com/attachment/forum/202204/02/091848zmsb4w2mcdcvhhw0.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">AB攻防机制克制关系</font></font></div><br>
从上述克制关系可以看出，AB两种职业的每一种攻防机制，都有对方一个攻击机制或防御机制与之形成克制关系。同时也可以看出，B只有翻滚这一种防御机制，B对A的行为主要是进攻——用B的轻击克制A的盾反、翻滚和轻击，用B的重击克制A的轻击、重击和盾防，用翻滚克制A的重击；而A有盾防、盾反和翻滚三种防御机制，A对B的攻防行为更加均衡——用A的盾反和翻滚克制B的重击，用A的盾防克制B的轻击，用A的轻击克制B的翻滚。<br>
<br>
在A的重击和B的轻击之间，我画了一根红色的虚线，这代表二者之间的克制关系必须通过实际伤害数值来判定，如果B轻击消耗10能量造成20点伤害，A重击消耗20能量造成20伤害，不用考虑具体动作时间和生命上限，必定是B轻击克制A重击；如果B轻击消耗10能量造成10伤害，A重击消耗20能量造成50伤害，那么就必定是A重击克制B轻击。实际战斗设计中，按照每种机制都能克制至少一种其他机制的原则，我们更希望A重击克制B轻击。<br>
<br>
在文章的最后，我留一个思考题。<br>
<br>
在上文中，既然有了移动、攻击距离的机制，如果我们再加入一种远程职业，又该以怎样的逻辑推倒其攻防机制？<br>
<br>
简单提示，远程由于有距离上的优势，在近战单位能够追上远程单位的这段时间内，远程可以依托距离输出。同时近战单位必须有能力追上远程，这就意味着要引入加速跑的机制。同时远程在输出时，必须给近战追上来的时机，这意味着远程输出时必须降低移动速度或直接不能移动。<br>
<br>
在伤害上，近战单位在追上远程对远程攻击时，造成的伤害必须能够弥补自己在追人过程中的血量损失，这意味着近战伤害必须高于远程，或是血量上高于远程。具体的机制大家可以依据上文中对于机制的推导过程，自行思考。<br>
<br>
好，感谢大家都阅读。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/484068545</font></font><br>
<br>
  
</div>
            