
---
title: '控制兵线、多变关卡，从《Infinitode2》看塔防游戏数值设计'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202209/05/093650yw7159mb491159uf.jpg'
author: GameRes 游资网
comments: false
date: Mon, 05 Sep 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202209/05/093650yw7159mb491159uf.jpg'
---

<div>   
<div align="center">
<img aid="1052402" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093650yw7159mb491159uf.jpg" data-original="https://di.gameres.com/attachment/forum/202209/05/093650yw7159mb491159uf.jpg" width="600" id="aimg_1052402" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093650yw7159mb491159uf.jpg" referrerpolicy="no-referrer">
</div><br>
<i><font color="#808080">首发“游戏设计理论”公众号</font></i><br>
<br>
<strong><font color="#de5650">引言</font></strong><br>
<br>
以前本来打算做一个塔防游戏，因为这是个小众但有市场的赛道，所以关注了一批塔防游戏。<br>
<br>
其中个人认为最好的就是《Infinitode 2》，它基本是个单机游戏，只有部分功能需要联网。<br>
<br>
未来市场上可能会有一些不错的塔防游戏，我自己也在以塔防为基础研究一些设计理论，本文就拆解一下这个游戏。<br>
<br>
通过这个游戏先建立一个“传统数值塔防游戏设计模型”，为后续研究和设计做准备。<br>
<br>
<strong><font color="#de5650">塔防游戏的定义</font></strong><br>
<br>
在定义之前，必须先回答一个问题：塔防游戏最底层的乐趣是什么呢？个人认为，是控制兵线。<br>
<br>
从游戏的本质是情绪出发，兵线距离终点的距离是影响我们情绪变化的直接原因，离远了会无聊，离近了会紧张。<br>
<br>
所以传统塔防游戏的定义就是把恰当的塔放在恰当的位置上，利用各种手段阻止敌人抵达终点。<br>
<br>
<strong><font color="#de5650">塔防游戏的要素</font></strong><br>
<br>
有了基础定义，再找到组成核心机制的要素，建立基础模型。塔防游戏各有各的不同，只讨论几个必备的要素。<br>
<br>
设计者就是要利用各种要素，设计多变、丰富的关卡。<br>
<br>
玩家利用游戏机制控制兵线，设计者设计各种敌人试图突破玩家的布局，两者不断的动态平衡，影响玩家情绪。<br>
<br>
塔防游戏的核心要素比较简单，就三个：塔、路线、敌人。<br>
<br>
其它要素都是非核心，是设计者用来提供附加体验和改变游戏节奏用的。<br>
<br>
路线是塔防游戏特殊的地方，大部分游戏的路线没有太强的策略性，而塔防游戏的路线可以做出比较强的策略，这个特性需要利用好。<br>
<br>
当然每个游戏的核心体验不同，有的游戏就是不想有太强的策略性，也可以弱化路线的策略。<br>
<br>
<strong><font color="#de5650">拆解《Infinitode 2》</font></strong><br>
<br>
《Infinitode 2》的核心玩法相对传统塔防有两个特殊的地方，一个是它加入了挖矿系统，另一个是关卡基本都是无限波数，这都是为了一个目的：挖矿。<br>
<br>
关卡中可以造矿机挖矿，守的时间越长收益越多，矿在局外养成有需求。整个游戏中后期的目的就是为了挖更多矿。<br>
<br>
这就相对传统塔防游戏多了一层“意义”，或者说目标，有点类似《植物大战僵尸》后期收集金币。<br>
<br>
不一样的地方在于《Infinitode 2》把挖矿融入到了战斗策略中，追求更多收益的手段是升级矿机提高挖矿效率还是造塔守更多波数增加挖矿时间，需要在两者之间达成平衡。<br>
<br>
相对常规的“守更多波”又增加了一个更高级的目标，还增加了一条策略路径，整个游戏的耐玩性增强了很多。<br>
<br>
<div align="center">
<img aid="1052403" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093651l1f1oadrftawdjlw.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093651l1f1oadrftawdjlw.png" width="554" id="aimg_1052403" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093651l1f1oadrftawdjlw.png" referrerpolicy="no-referrer">
</div><br>
这种“抽象一层”的设计思路值得借鉴。<br>
<br>
本文拆解会按之前写的游戏六层结构来拆解，忽略情绪、体验和世界观层，只讨论核心机制、系统结构、目标规划。<br>
<br>
由于不希望重点跑偏，《Infinitode 2》后期的自制地图、晶片、音乐、无尽模式和一些小功能都会略过。目前版本距离我玩的时间略久，可能跟我体验的版本略有出入。<br>
<br>
<strong><font color="#de5650">核心机制要素构成</font></strong><br>
<br>
《Infinitode 2》的核心机制由几个要素构成：塔、路线（包括传送门、逻辑门、塔位等）、敌人、矿和矿机、技能、金币、规则。<br>
<br>
这些机制一起构成了一整局游戏所需的所有要素，通过要素的组合变化给玩家营造独特的游戏体验。<br>
<br>
<strong>塔</strong><br>
<br>
<div align="center">
<img aid="1052404" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093651qzcckqo00ozc3rul.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093651qzcckqo00ozc3rul.png" width="554" id="aimg_1052404" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093651qzcckqo00ozc3rul.png" referrerpolicy="no-referrer">
</div><br>
《Infinitode 2》的塔目前共有16种，我玩的时候是14种。每种塔都有自己独特的效果，这里就不一一介绍了。<br>
<br>
每种塔不仅特性不同，属性也是跟敌人匹配的，对不同敌人的伤害比例也不同，在0——200%之间浮动，这样可以有效避免只培养少数塔通所有关。<br>
<br>
所有塔都有两个等级，一个常规等级，需要花金币升级，可以提高所有属性；一个经验等级，通过击败敌人获得经验升级，提高基础属性和解锁升级特性。<br>
<br>
塔的升级特性可以针对不同敌人选择，比如散弹塔可以升级对空能力，就可以不造防空塔，节省一个塔位。<br>
<br>
所以一个塔有三种效果影响策略：特性、属性、升级特性。路线和敌人影响玩家选择放置哪种塔和选择哪个升级特性。<br>
<br>
<strong>路线</strong><br>
<br>
《Infinitode 2》的地图没有像《明日方舟》、《球球英雄》那样迎合泛用户，地图有大有小，有复杂有简单，而且有一定策略性。<br>
<br>
新手期的关卡只有简单的路径，后面增加了逻辑门，只能通过特定的怪物，玩家可以根据逻辑门的提示在这条路线上放置相应的塔。<br>
<br>
还有传送门，可以改变敌人前进的路线，设计传送门可以更有效的利用地图，整个地图都利用上又不显得路线单调。<br>
<br>
塔必须放置在指定的格子类型上，在恰当的位置放恰当的塔是一个策略。此外部分格子还有属性加成，可以弥补不同塔的劣势，比如狙击塔攻速慢，放在攻速加成的格子上效果很好。<br>
<br>
在无尽模式中会更复杂，敌人可以不按路线前进，而是走最短路径。此时需要玩家造塔堵路，让敌人回到路线上，策略难度更大。<br>
<br>
<strong>敌人</strong><br>
<br>
<div align="center">
<img aid="1052405" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093652x5laii1rakrn9pkv.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093652x5laii1rakrn9pkv.png" width="554" id="aimg_1052405" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093652x5laii1rakrn9pkv.png" referrerpolicy="no-referrer">
</div><br>
普通敌人11种，BOSS5种，特性各异，也不一一介绍了。<br>
<br>
敌人的特性和属性区别导致总是被某种塔克制，所以需要根据关卡中不同怪物放置针对的塔，这是塔防游戏的常规策略。<br>
<br>
但是又由于养成数值的作用，不追求排名的话只养成比较通用的塔其实也可以，导致敌人特性的策略价值被弱化。<br>
<br>
这是数值游戏的特性，五种胜负因素中，数值因素权重过高，一定会产生数值碾压，导致策略失效。可以通过急速降低塔的养成性价比缓解，但不可能完全解决。<br>
<br>
当然这种特性也有好的地方，就是成长感强，养成一下过关立刻变简单了。<br>
<br>
<strong>矿和矿机</strong><br>
<br>
<div align="center">
<img aid="1052406" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093652y51geoz5ze88u9g8.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093652y51geoz5ze88u9g8.png" width="554" id="aimg_1052406" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093652y51geoz5ze88u9g8.png" referrerpolicy="no-referrer">
</div><br>
共5种矿和5种矿机，一一对应，高级的矿机可挖低级矿，反之不行。<br>
<br>
越高级的矿机建造和升级越贵，越高级的矿越难挖。<br>
<br>
由于矿机和塔的资源消耗相同，这就成了博弈点。日常刷图都是为了资源，是升级塔守更多波，还是升级矿机更快挖矿，需要一些权衡。<br>
<br>
不过由于中期塔的强度上来了，这个博弈也就逐渐弱化了，几个塔守住就开始造矿机，然后升级塔再升级矿机。<br>
<br>
但设计者通过设计矿机的养成属性，让这个策略在后期又接近平衡，即升级矿机跟塔之间又需要稍微衡量一下。<br>
<br>
<strong>技能</strong><br>
<br>
<div align="center">
<img aid="1052407" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093653oe4q8199t4w77be4.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093653oe4q8199t4w77be4.png" width="554" id="aimg_1052407" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093653oe4q8199t4w77be4.png" referrerpolicy="no-referrer">
</div><br>
一共有12种技能，通过研究科技树解锁，效果各有特色，具体可见：https://infinitode-2.fandom.com/wiki/Abilities。<br>
<br>
技能的伤害是根据当前所有塔的10秒内最高平均每秒伤害计算的，这是个比较有意思的设计，如果塔的伤害不高，用技能也没太大用处。但玩家可以通过堆积敌人，瞬时造成更多伤害，以提高技能伤害。<br>
<br>
技能击败的敌人获得的金币是减少的，可以降低关卡前期玩家对技能的依赖。<br>
<br>
每种技能释放都消耗不同的能量，未养成状态能量每60秒回复一格，上限10格。所以不能连续用多个技能。<br>
<br>
<strong>金币</strong><br>
<br>
造塔和矿机的资源，主要通过击败敌人获得，提前进入下一波和科技树也可以少量获得。<br>
<br>
特殊地块上的塔击败敌人能获得额外金币奖励。<br>
<br>
<strong>规则</strong><br>
<br>
这里的规则指核心机制涉及到的所有规则，包括胜负判定、技能能量机制、塔的经验获得、敌人死亡判定、塔的命中判定、索敌规则等等。<br>
<br>
这些规则非常复杂，我也没完全搞清楚，就挑几个值得学习的规则讲讲。<br>
<br>
《Infinitode 2》可以控制每个塔的索敌规则：选择攻击第一个、最后一个、血最少的、血最多的。这就给策略上限留出空间，不同塔有适合的攻击目标。比如机枪塔随时间伤害增高，就适合打血最多的。<br>
<br>
这就让操作空间大了起来，手动操作部分塔的攻击目标，能减少漏怪。<br>
<br>
另一个规则，塔的经验是通过击败敌人获得，未击败敌人的塔只能缓慢自动升级。这就让“获得经验加成”、“满级后获得被动经验加成”两个属性更有价值。<br>
<br>
《Infinitode 2》的数值拆解得非常细致，有很多看似没多大用的数值，极限情况下变得非常有用。类似的设计挺多，让整个游戏的策略上限变得非常高。<br>
<br>
<strong><font color="#de5650">小结</font></strong><br>
<br>
之前的文章说过，决定胜负的因素就五种：推理、策略、操作、数值、运气。塔防游戏一般重策略和数值。<br>
<br>
《Infinitode 2》通过塔的特性、属性、升级特性，结合路线和敌人的特性，通过每波的敌人的变化对玩家形成了策略压力，玩家必须把正确的塔放在正确的位置，还要决策是先升塔还是先升矿。<br>
<br>
整个游戏过程玩家需要持续关注兵线，下一波刷什么怪，提前做好应对策略，很容易进入心流。<br>
<br>
还有一些规则决定了游戏的策略上限，理解深的玩家跟普通玩家能防住的波数差距极大。<br>
<br>
<strong><font color="#de5650">系统结构</font></strong><br>
<br>
正常设计是先做目标规划，再设计系统。但是分析现成的游戏，就要搞清楚现有系统。<br>
<br>
《Infinitode 2》的系统结构比较简单，除了关卡以外重要的系统只有科技树、任务系统、赛季系统、成就系统、奖杯系统。<br>
<br>
这些系统在局外形成了养成循环:通过任务、成就给玩家目标，完成目标的奖励和完成的过程获得资源，再去科技树养成，属性提高后完成更难的任务，赛季排名则是最终追求目标。<br>
<br>
奖杯系统类似成就系统，达成条件获得，奖杯增加少量属性。<br>
<br>
<strong>科技树</strong><br>
<br>
<div align="center">
<img aid="1052408" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093653bvi5bxbwhmihw55i.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093653bvi5bxbwhmihw55i.png" width="554" id="aimg_1052408" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093653bvi5bxbwhmihw55i.png" referrerpolicy="no-referrer">
</div><br>
科技树大概可以分成三个部分：1区是用通关评星升级，每个关卡有3个星星，可以用来升级。这部分主要研究塔、矿机、技能、芯片的属性和一些特殊效果，比如敌人移动速度降低、战利品稀有度等。<br>
<br>
2区是通用区，研究技能、任务、塔的通用属性、矿机属性、解锁一些功能。<br>
<br>
3区是每个塔独立的科技树，只能研究加成该塔的属性。<br>
<br>
研究消耗矿机挖出的矿，还有钞票、蓝图，这些可以通过挖矿、任务和敌人掉落获得。<br>
<br>
科技树是几乎所有属性的来源，数值目标非常集中。集中的好处就是目标感强，不需要想太多，只需要想怎么获取更多资源。<br>
<br>
集中的缺点则是后期养成反馈变慢，要很久才能升一级。所以一般网游都会做多个养成点慢慢开放，增强反馈频率。<br>
<br>
《Infinitode 2》的数值拆解得非常丰富、多元，也可以说复杂，但是由于核心机制设计得很巧妙，这些属性还都比较有用。<br>
<br>
于是对玩家来说养成的过程显得“有价值”，如果属性拆得不好，有部分没用的属性，养成的体验就会弱化。<br>
<br>
<strong>任务</strong><br>
<br>
任务分为局内和局外两种：<br>
<br>
<div align="center">
<img aid="1052409" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093653ghp46ah007303lmo.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093653ghp46ah007303lmo.png" width="600" id="aimg_1052409" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093653ghp46ah007303lmo.png" referrerpolicy="no-referrer">
</div><br>
每日挑战是比较简单的副本，一般都可以拿到，且奖励不错。每日任务则比较困难，且有排行榜的任务，两者的翻译有点反常识。<br>
<br>
每日任务的副本比较特殊，它是个公平玩法，需要联网，而且所有玩家的属性是一样的，不考虑科技树和奖杯系统的属性加成。它会奖励Skill point，上传自定义地图时消耗。<br>
<br>
局内任务类似成就条件，达成任务条件会给一些不错的奖励，大部分都是一次性的，且部分任务条件需要用不同塔完成，算是一种强制横向养成。<br>
<br>
<strong>赛季系统</strong><br>
<br>
<div align="center">
<img aid="1052410" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093654oqlc3llc58523aqj.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093654oqlc3llc58523aqj.png" width="554" id="aimg_1052410" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093654oqlc3llc58523aqj.png" referrerpolicy="no-referrer">
</div><br>
由于我的游戏时间不算长，分数不高，暂时不清楚具体的算法，只能通过描述简单判断。<br>
<br>
赛季积分应该是根据每个副本的“正常模式”下的分数综合计算的，猜测每个副本有自己的权重。<br>
<br>
<strong>模式介绍如下：</strong><br>
<br>
<div align="center">
<img aid="1052411" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093654mpfouvgk8g82uovb.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093654mpfouvgk8g82uovb.png" width="554" id="aimg_1052411" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093654mpfouvgk8g82uovb.png" referrerpolicy="no-referrer">
</div><br>
赛季模式是各个高阶玩家最终的追求，需要对游戏理解非常深。<br>
<br>
<strong>成就系统</strong><br>
<br>
<div align="center">
<img aid="1052412" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093654tnlujj4vfihuljsh.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093654tnlujj4vfihuljsh.png" width="554" id="aimg_1052412" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093654tnlujj4vfihuljsh.png" referrerpolicy="no-referrer">
</div><br>
成就比较常规，就是一堆成就条件，达成获得少量奖励。<br>
<br>
成就条件算是中期目标，但由于奖励不多，界面隐藏也较深，目标感不强。<br>
<br>
<strong>奖杯系统</strong><br>
<br>
<div align="center">
<img aid="1052413" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093655gjrbbrdyj3ljjb46.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093655gjrbbrdyj3ljjb46.png" width="554" id="aimg_1052413" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093655gjrbbrdyj3ljjb46.png" referrerpolicy="no-referrer">
</div><br>
图中是部分奖杯，大多数奖杯都是在指定关卡守过指定波数获得，增加指定塔的极少量属性。<br>
<br>
所以纪念意义远大于数值价值。<br>
<br>
<strong><font color="#de5650">小结</font></strong><br>
<br>
这几个主要系统结合关卡构成了游戏的完整循环，让整个游戏的生命周期变得非常长，且过程比较有趣。<br>
<br>
虽然好玩最关键的是核心机制，但恰当的养成节奏和系统设计能极大的促进玩家留存。<br>
<br>
<strong><font color="#de5650">目标规划</font></strong><br>
<br>
这个“简单”的塔防游戏已经3年了，并且可见的未来3年应该还会不错，是为什么呢？<br>
<br>
这跟整个游戏是如何运行的有关，前面简单的提了一下，接下来详细讲讲。<br>
<br>
<strong>游戏是通过目标驱动的。</strong><br>
<br>
以前讲过，游戏目标可以分成两种：系统目标和数值目标。<br>
<br>
系统目标是潜移默化影响人的目标，比如塔防，大家默认目标就是守更多波。RPG游戏，就是默认要打败最终BOSS。<br>
<br>
数值目标就是非常明确的数值成长，新技能、新属性，能直接量化帮助过关的都是数值目标。<br>
<br>
要注意区分系统和数值目标，举个例子：“装备系统”是系统目标，“更好的装备”是数值目标。<br>
<br>
<strong>系统目标</strong><br>
<br>
系统目标的重点是如何让玩家本能的觉得“这系统不错，值得追求”，并且有节奏的展开，持续不断的有新东西让玩家建立短期目标，即心流中的反馈机制。<br>
<br>
《Infinitode 2》的世界观比较简单，就是个抽象的几何数据世界，代入感不算太强，所以世界观对建立目标的影响不大。<br>
<br>
它的系统设计除了科技树外不算复杂，随时间开启的能建立目标的系统有关卡、科技树、奖杯系统、赛季、自制地图模式。<br>
<br>
<strong>关卡目标</strong><br>
<br>
<div align="center">
<img aid="1052414" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093655znnxxizy7svsi99y.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093655znnxxizy7svsi99y.png" width="554" id="aimg_1052414" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093655znnxxizy7svsi99y.png" referrerpolicy="no-referrer">
</div><br>
关卡是最核心的驱动力，需要打过更多关卡解锁塔、高级矿、科技树材料、评星数量，这些资源是提高属性的必要条件。<br>
<br>
关卡仅会显示当前正在进行的“阶段”，类似网游副本的章节。并且通过某关卡解锁的塔会显示在关卡选项上。好处是压力小，目标强。<br>
<br>
初期关卡非常简单，就是玩法教学。慢慢开始通过不同怪物引导建造新塔，再引入特殊地块、BOSS、矿机等元素，逐渐通过这些元素丰富关卡策略。<br>
<br>
这些要素逐渐让整个游戏的乐趣丰富起来，玩家更愿意往后推关，这是最关键的成功条件。<br>
<br>
除了新手教学关卡，每个关卡都有排行榜，大部分关卡都是无限波数的。所以每次游戏都可以奔着打更多波数去，不会像一般塔防那样玩几次就很烦了。<br>
<br>
每个无限波的关卡都有渐进的系列任务，奖励还不错，形成了有吸引力的中短期目标。而且一直显示在关卡内，目标感非常强。<br>
<br>
所以如果卡关了，玩家会主动去之前简单的关卡刷材料养成。<br>
<br>
关卡的难度递进也很有节奏，越往后怪物种类越多，地形越来越复杂，必需要养成多种塔，只养成通用的几种塔守不了几波。并且前期也会通过任务需求让玩家培养一些少用的塔，降低后期突然需要养成的压力。<br>
<br>
总的来说，关卡通过逐渐增加新敌人和塔提供策略深度，通过任务引导玩家防守更多波，通过产出后置强迫玩家往后打。<br>
<br>
<strong>科技树目标</strong><br>
<br>
<div align="center">
<img aid="1052415" zoomfile="https://di.gameres.com/attachment/forum/202209/05/093655hbc4o9a90zg3uyd3.png" data-original="https://di.gameres.com/attachment/forum/202209/05/093655hbc4o9a90zg3uyd3.png" width="554" id="aimg_1052415" inpost="1" src="https://di.gameres.com/attachment/forum/202209/05/093655hbc4o9a90zg3uyd3.png" referrerpolicy="no-referrer">
</div><br>
科技树是个极大的养成坑，为了避免一开始选择太多容易迷茫，塔的科技树是一点点展开的。<br>
<br>
未获得的塔只显示塔本身的属性，获得后会展开该塔的科技树，同时显示下一个未获得的塔，也会标明解锁的关卡。<br>
<br>
科技树的通用部分和消耗关卡评星升级的部分是全部开启的。<br>
<br>
一般会优先升级解锁通用部分的科技树，开启一些功能性的属性，如技能、矿机。每个功能都是必须要开的，开启这些功能就成了很强的短期目标。为了这个短期目标就需要去关卡获取资源。<br>
<br>
评星部分的每个科技只有1级，较远的价值更高，所以要稍微选择一下路线，并且不可避免的要选择一些价值不高的。为了多点一些科技，就需要每个关卡都拿到3星，是个短期挑战目标。为了这个目标就需要提高塔的属性。<br>
<br>
最终目标还是会转移到塔自身的科技树上，这部分的消耗非常大，尤其是在无尽模式，会开启额外的科技点和等级，消耗几十倍于正常模式的资源。<br>
<br>
塔的科技树的升级节奏也很好，每个塔有3个点性价比极高，只能升1次，消耗的资源档次也是递进的。<br>
<br>
塔的其它科技每升一级也会增加材料档次，需要玩家打更高级的关卡获取，形成了很强的短期目标。<br>
<br>
<strong>奖杯系统目标</strong><br>
<br>
由于前期拿奖杯的较难，且奖杯加的属性非常少，它就是一个收集向的系统，属于玩家的次要追求，目标感不太强。<br>
<br>
<strong>赛季目标</strong><br>
<br>
赛季是个高阶玩家追求的最终目标，对游戏理解足够深刻之后打排行榜就变成了乐趣所在。<br>
<br>
这个游戏的可玩性非常高，比一般塔防游戏要深很多，会玩不会玩的区别极大。<br>
<br>
这是个成就驱动型玩家的玩法，普通玩家不太会追求。<br>
<br>
<strong>数值目标</strong><br>
<br>
数值目标一般都是中短期目标，属于努力一下就能得到的目标。太长期的数值目标是没办法建立的。<br>
<br>
告诉玩家努力3个月能获得一个极强的装备，中间也没什么进度积累，现在的市场环境基本不会有人愿意追这个目标。<br>
<br>
本来数值目标是嵌套在系统目标中的，没必要单独写，但是《Infinitode 2》的数值拆解得非常好，如果没有拆得这么好，系统中的数值目标也建立不起来，因为玩家会觉得没用。<br>
<br>
正是因为拆得大部分属性都有用，才能建立起系统和数值目标。下面分类讲讲它的数值拆解得哪里好，因为属性太多了，就只讲几个有意思的设计。<br>
<br>
<strong>等级类属性</strong><br>
<br>
《Infinitode 2》有两个等级，一个常规等级，一个经验等级。在无尽模式，常规等级最高到10级，经验等级最高到100级。<br>
<br>
经验等级是个巨大的升级坑，但等级上限升到100级，也需要把获取经验的速度提上来才可能升得到。<br>
<br>
所以它又设计了几个属性：经验加成、升级等级满时被动获得经验值、初始经验等级，想要在关卡内快速提高等级，这几个属性不得不升级，整个等级相关的升级坑非常深。<br>
<br>
<strong>攻击类属性</strong><br>
<br>
《Infinitode 2》的塔各有特性，所以每个塔的科技还有所区别。比如特斯拉塔可以升级闪电链的长度，散弹塔可以升级子弹数量。<br>
<br>
还有一个大部分塔防游戏没有的属性：旋转速度，因为《Infinitode 2》部分塔只有面对敌人才能攻击，所以要转过去才能攻击，转得慢就打不了几下，升级这个属性的收益就非常高。<br>
<br>
<strong>经济类属性</strong><br>
<br>
经济属性分关卡内外两部分，关卡内就是指塔和矿机升级用的金币，关卡外则是产出局外养成的资源。<br>
<br>
金币相关的属性有：建造价格降低、升级价格降低、卖出塔返还金币、强制呼叫下一波奖励、每分钟自动产生金币、开局起始金币。<br>
<br>
这些属性前后期各有不同性价比，刚开始建造价格降低和开局金币最有用，塔等级高了以后升级价格降低更有用。<br>
<br>
局外养成资源相关的属性有：战利品稀有度、额外绿钞、矿机可获得的战利品数量、微量尘埃掉率、重生券掉率、任务奖励。<br>
<br>
为了提高局外养成速度，这些属性也是必须要升级的。<br>
<br>
<strong>技能类属性</strong><br>
<br>
技能的属性就比较简单了，基本都是加伤害或持续时间。<br>
<br>
技能虽然是消耗品，但消耗很少，所以使用技能的性价比非常高，这就让玩家必须要升级技能。<br>
<br>
<strong><font color="#de5650">小结</font></strong><br>
<br>
整个游戏的驱动力是不断迭代的目标，而目标又是通过系统和数值建立的。<br>
<br>
系统设计简洁，只有几个必要的关键系统，各自负责不同的短中长期目标，也负责不同水平的玩家。<br>
<br>
系统中的数值种类拆解得有用，数值节奏合理，能让玩家不断有新的短中期目标以及反馈，慢慢奔着长期目标前进。<br>
<br>
再叠加有趣的关卡设计，整个游戏的循环非常顺畅，非常耐玩。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
通过分析《Infinitode 2》，我们大概了解一个好的数值塔防大概要有哪些要点：高可玩性的核心机制、有趣的关卡设计、简洁有效的系统结构、合理有价值的目标规划。<br>
<br>
当然大部分好的数值游戏都符合这些点，这么说有点无趣。所以重点在于“如何做到”。<br>
<br>
《Infinitode 2》给了我们一个很好的具体的例子，深入研究这个游戏之后，发现不止核心玩法、系统结构很好，很多细节设计得也非常好，无论数值设计、路线设计、画面表现、操作，都非常细致，除模型外设计者居然只有一个人，确实很厉害。<br>
<br>
作为一个数值塔防游戏，数值是策略重要的一部分，每个塔每一级的性价比、技能的伤害计算公式、敌人的数量、塔的特性选择等等，都构成了需要仔细研究的规则，这些规则极大的提高了这个游戏的上限，让整个游戏非常耐玩。<br>
<br>
如果没有自己认真深入体验过这个游戏，可能无法理解这种设计的亮点，自己也很难设计出高策略上限的游戏。<br>
<br>
足够的数值深度让这个游戏的生命力非常长，但可惜它的关卡场景必须用较小的模型，没有美术发挥的余地，市场规模不太能做大。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：游戏设计理论</font></font><br>
<br>
  
</div>
            