
---
title: 'MOBA动作类游戏技能设计模块指南：从技能触发方式谈起'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202105/10/095837uhtm87tejpem5ipp.jpg'
author: GameRes 游资网
comments: false
date: Mon, 10 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/10/095837uhtm87tejpem5ipp.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2496082">
<i><font color="#808080">本文首发腾讯游戏学院GWB</font></i><br>
<i><font color="#808080">作者：Bruce 腾讯互动娱乐 高级游戏策划</font></i><br>
<br>
“当你想要设计一个角色或者BOSS，需要用到技能表现。通常从设计方案出来，到程序同步实现再反馈到设计者验证环节，一般会需要经过很长时间才能验证设计思路，对于技能设计者是一件非常痛苦的事情。那有没有办法在过程中，提供设计者快速调整技能设计的技能工具模块？”<br>
<br>
之所以想写这个文章，是因为2019年在做公线-技能模块设计，公线-技能模块简单来说就是用UE4Gas的底子，搭建一个策划自主技能设计的工具模块，希望策划应用到技能设计时，能通过模块化组合的方式，提供快速满足策划设计思路的工具和工作管线。<br>
<br>
经过几个月的摸索，算是出了点成果，所以就想总结制作过程中的一些东西，跟大家分享一下自己关于技能设计模块的想法思路。<br>
<br>
<strong><font color="#de5650">一、游戏技能是什么？</font></strong><br>
<br>
<div align="center">
<img id="aimg_977142" aid="977142" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095837uhtm87tejpem5ipp.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095837uhtm87tejpem5ipp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095837uhtm87tejpem5ipp.jpg" referrerpolicy="no-referrer">
</div><br>
既然咱们说到模块技能设计，先来看看游戏技能指什么？我找了各种说明，综合对比后，给出这么一段话。<br>
<br>
游戏技能指的是游戏中通过游戏行为造成攻击、防御、辅助等效果的方式。<br>
<br>
随着游戏玩法元素更多的衍生融合，我们可以看到，在主流的游戏类型中，大多都会涉及游戏技能的应用。<br>
<br>
所以针对不同的游戏类型，关于游戏技能定义，我这里加了一条个人看法，游戏技能的表现会依托于不同游戏环境，有不同的效果和表现方式。<br>
<br>
<strong><font color="#de5650">二、如何打造满足多种游戏类型的技能设计模块？</font></strong><br>
<br>
<div align="center">
<img id="aimg_977143" aid="977143" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095838au0p8a8u5575jrru.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095838au0p8a8u5575jrru.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095838au0p8a8u5575jrru.jpg" referrerpolicy="no-referrer">
</div><br>
我当时在做这个内容的时候，在想虽然是面对不同类型的游戏技能，但我们先不用陷入到具体的技能设计中，而是从各种类型的游戏技能具体效果上抽离出来，找出游戏技能的必要元素。<br>
<br>
必要元素也就是组成技能的基础类型模块，希望类似于乐高的大颗粒积木一样，可以用这些基础类型模块去自由组合成不同技能的方式；<br>
<br>
<div align="center">
<img id="aimg_977144" aid="977144" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095838ljlc5l8ca8yaz58c.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095838ljlc5l8ca8yaz58c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095838ljlc5l8ca8yaz58c.jpg" referrerpolicy="no-referrer">
</div><br>
带着这个思路，重新梳理了市面不同类型的主流游戏技能，咱们不管游戏技能类型的差异化多大，无非逃不开六个基础类型模块，依次为：<br>
<br>
技能的触发方式；<br>
<br>
技能的释放条件；<br>
<br>
技能的释放选择；<br>
<br>
技能的表现方式；<br>
<br>
技能的生成机制；<br>
<br>
技能的影响效果；<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">三、技能的触发事件</font></strong><br>
<br>
<div align="center">
<img id="aimg_977145" aid="977145" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095838sfwkv4oih3kzhal6.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095838sfwkv4oih3kzhal6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095838sfwkv4oih3kzhal6.jpg" referrerpolicy="no-referrer">
</div><br>
关于技能的触发方式，通常大家的理解，也就是说技能是怎么触发的？<br>
<br>
传统的触发方式理解为：<br>
<br>
一种是主动触发：也就是主动按键触发的方式；<br>
<br>
另一种是被动触发：而被动触发的条件就非常广泛，比如受伤触发、死亡触发、命中触发等等触发方式。<br>
<br>
而我们所说的触发方式，不会只归纳为主动和被动的方式，而是依照触发事件来划分。<br>
<br>
比如有些主动技能中，也存在主动按键之后，需要满足某个触发事件，才会触发技能行为；<br>
<br>
<div align="center">
<img id="aimg_977146" aid="977146" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095839oaf5x5ts5gazes5q.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095839oaf5x5ts5gazes5q.jpg" width="446" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095839oaf5x5ts5gazes5q.jpg" referrerpolicy="no-referrer">
</div><br>
比如莫甘娜的‘灵魂镣铐’技能，从传统意义上来说，是个主动按键的技能，但触发的方式中，还需要验证范围触发的方式，也就是说范围中检测到敌人后，才能够触发。<br>
<br>
说到这里，大家伙可能就会吐槽了，这东西我也知道啊，不就是设定触发事件吗，这个设计技能的时候都会做，这有啥可瞎白活的？<br>
<br>
别急：待我一一道来。<br>
<br>
<div align="center">
<img id="aimg_977147" aid="977147" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095839cngcy484vyyq4bvq.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095839cngcy484vyyq4bvq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095839cngcy484vyyq4bvq.jpg" referrerpolicy="no-referrer">
</div><br>
为了选择足够通用和样本性的触发事件，我对市面上技能机制比较全的几款知名产品进行分析后，横向对比了四百多个技能的设计，发现这些技能虽然各有特色，但是技能触发的方式几乎囊括在八种触发事件中；<br>
<br>
给八种事件做了简单命名，分为：<br>
<br>
攻击、命中、时间、空间、状态、属性、死亡、验证；<br>
<br>
<div align="center">
<img id="aimg_977148" aid="977148" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095839mjhj2rhcnuc2chjj.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095839mjhj2rhcnuc2chjj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095839mjhj2rhcnuc2chjj.jpg" referrerpolicy="no-referrer">
</div><br>
当然这八种类型的事件，不是单独存在的，还可以通过多种事件耦合的方式，做出更多特性的展现，不夸张的说，这八种事件已经能够满足绝大部分的技能设计需求。<br>
<br>
<strong>1、攻击触发事件</strong><br>
<br>
<div align="center">
<img id="aimg_977149" aid="977149" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095840n39c9h8h9agp9cgh.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095840n39c9h8h9agp9cgh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095840n39c9h8h9agp9cgh.jpg" referrerpolicy="no-referrer">
</div><br>
攻击触发：简单理解来说，就是发起攻击之后，会触发的行为事件；<br>
<br>
常用在攻击方式变化和攻击发起后，影响角色属性和效果的技能效果中；<br>
<br>
需要说明的是，攻击触发事件，只跟攻击发出有关，逻辑上只要攻击发出就会触发事件，而不需要检测是否命中；<br>
<br>
当然这种用法的方式会通过额外的判定条件，来给攻击触发事件增加不同的特色用法；<br>
<br>
<div align="center">
<img id="aimg_977150" aid="977150" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095840jfb0e9bbkowkbvxv.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095840jfb0e9bbkowkbvxv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095840jfb0e9bbkowkbvxv.jpg" referrerpolicy="no-referrer">
</div><br>
比如在射击类型游戏‘无主之地’的枪械特性中：攻击行为之前会判定是否满足消耗子弹数量；<br>
<br>
如果满足，则每次射击会判定消耗两发子弹，继而触发了攻击事件，通过消耗2发子弹的方式，提升了枪械的攻击效果。<br>
<br>
<div align="center">
<img id="aimg_977151" aid="977151" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095840qlo46opx6j1xnjne.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095840qlo46opx6j1xnjne.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095840qlo46opx6j1xnjne.jpg" referrerpolicy="no-referrer">
</div><br>
再说一下攻击触发事件的另外一种应用方式，在王者荣耀中有这样的设定，英雄在普通攻击到一定次数之后，会触发攻击方式的改变；<br>
<br>
以MOBA游戏‘王者荣耀’中鲁班举例：<br>
<br>
每次攻击行为事件会触发记录攻击次数的行为，当攻击次数=4的时候，下一次攻击行为会改变攻击方式；<br>
<br>
<div align="center">
<img id="aimg_977152" aid="977152" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095840lcgs96g8966gwvvn.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095840lcgs96g8966gwvvn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095840lcgs96g8966gwvvn.jpg" referrerpolicy="no-referrer">
</div><br>
而在SLG类型的游戏‘鸿图之下’中，有一类连击技能，攻击触发事件中通过概率判定的方式，触发技能效果；<br>
<br>
关于攻击触发事件的应用方式还有很多，这里只是列举了一些常用案例；<br>
<br>
当然无论应用方式怎么变化，攻击触发事件的核心，就是逻辑上通过攻击触发的行为事件；而在这个应用过程中，设计者通过添加不同的条件判定，就会为攻击触发事件增加有趣的特性使用方式，以丰富技能的效果；<br>
<br>
<strong>2、命中触发事件</strong><br>
<br>
<div align="center">
<img id="aimg_977153" aid="977153" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095840tjiafeh3da5ff5j5.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095840tjiafeh3da5ff5j5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095840tjiafeh3da5ff5j5.jpg" referrerpolicy="no-referrer">
</div><br>
命中触发：判定单位（敌人/自己）在程序逻辑上被有效命中之后，会触发的行为事件；<br>
<br>
在命中触发事件中，通常用到的是判定命中之后，针对‘发出攻击者’和‘被攻击者’的效果反馈，以及命中之后的条件判定的反馈；<br>
<br>
<div align="center">
<img id="aimg_977154" aid="977154" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095841towtjhho4fbotzw6.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095841towtjhho4fbotzw6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095841towtjhho4fbotzw6.jpg" referrerpolicy="no-referrer">
</div><br>
比如APEX英雄中‘班加罗尔’的‘疾步’技能：当自身被命中后，触发了持续时间内，提升自身移动速度的技能效果；<br>
<br>
在这个技能案例中，命中触发事件所判定的命中目标为自己，当自己被命中后，移动速度属性提升；<br>
<br>
<div align="center">
<img id="aimg_977155" aid="977155" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095841nup5w1oitgubouc3.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095841nup5w1oitgubouc3.jpg" width="477" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095841nup5w1oitgubouc3.jpg" referrerpolicy="no-referrer">
</div><br>
而在魔兽世界战士的‘新鲜血肉’技能中：则判定为我命中敌人之后，会触发的行为事件。这种情况下，所判定的命中个体就是敌人。<br>
<br>
以上两种技能，说明在命中触发事件的这种机制，除了要判定命中的逻辑之外，还要记录命中发生的双方单位的信息；<br>
<br>
<div align="center">
<img id="aimg_977156" aid="977156" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095841nbytzvhzbvh4xtxx.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095841nbytzvhzbvh4xtxx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095841nbytzvhzbvh4xtxx.jpg" referrerpolicy="no-referrer">
</div><br>
还有一种命中触发的应用方式，是对攻击命中发起人和被命中的人产生了双向影响；<br>
<br>
英雄联盟中‘披甲龙龟’的‘尖刺防御’技能，在命中触发事件的用法中，首先是敌人命中自己会对自己造成伤害，但在自己被命中后，也会反弹给命中自己的人造成伤害。<br>
<br>
当然我们这里所说的命中事件，不单只是用在角色命中的技能当中，还会用在命中Actor（逻辑判定为可被攻击命中的物体）的判定当中。<br>
<br>
例如‘APEX英雄’中，瘟疫释放的毒气罐，就可以被攻击命中，提前触发爆炸的效果；<br>
<br>
这个也是游戏技能中，最常用的一种方式，对于某个特定Actor的命中判定的反馈。<br>
<br>
所以受击行为，首先是从程序逻辑中如何定义命中，而在命中行为事件的应用中，最基本的用法就是记录‘攻击’和‘被攻击者’信息，从而在技能效果中，扩展受击行为事件的技能效果；<br>
<br>
<strong>3、时间触发事件</strong><br>
<br>
<div align="center">
<img id="aimg_977157" aid="977157" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095841t1178u171iid82vn.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095841t1178u171iid82vn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095841t1178u171iid82vn.jpg" referrerpolicy="no-referrer">
</div><br>
时间触发：满足特定时间区间或节点的行为结果，触发的行为事件；<br>
<br>
那么问题来了，特定时间区间、特定时间节点到底该怎么解释？<br>
<br>
<div align="center">
<img id="aimg_977158" aid="977158" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095841krqzgrac31a6l6hu.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095841krqzgrac31a6l6hu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095841krqzgrac31a6l6hu.jpg" referrerpolicy="no-referrer">
</div><br>
首先是满足特定时间区间的用法，我会解释为在持续时间内的才能触发的行为事件，各种游戏类型中常用的持续性技能都会用到类似的方式；<br>
<br>
比如‘APEX英雄’恶灵的维度裂隙：开启技能后，持续时间内，开启两座传送门，己方队员碰触传送门，会触发在两座传送门中传送角色的技能行为。<br>
<br>
这里的时间触发事件的先决前提是满足在传送门存在的特定时间区间内；<br>
<br>
<div align="center">
<img id="aimg_977159" aid="977159" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095842zzofl82u9u2o0el8.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095842zzofl82u9u2o0el8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095842zzofl82u9u2o0el8.jpg" referrerpolicy="no-referrer">
</div><br>
而满足特定时间节点的用法，则是要求时间到达某个特定的节点时，才能触发的行为事件，在很多游戏中，延迟生效的技能多会用到类似的方式；<br>
<br>
比如‘英雄联盟’时光老人的‘定时炸弹’：指定目标地点投掷一个定时炸弹，3秒倒计时之后炸弹会爆炸；这里所描述的3秒之后，就是满足特定时间节点最常用的一种方式；<br>
<br>
<div align="center">
<img id="aimg_977160" aid="977160" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095842u49g99j44rez69sc.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095842u49g99j44rez69sc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095842u49g99j44rez69sc.jpg" referrerpolicy="no-referrer">
</div><br>
在满足特定时间节点的用法中，还有一种满足游戏规则定义的特殊时间节点，比如四季、昼夜、年份,甚至是通过技能效果改变当前时间节点，以满足触发技能行为事件；<br>
<br>
在‘DOTA2’的暗夜魔王就属于这种的典型应用，在‘DOTA2’的游戏规则中，设定了关于昼夜切换的游戏规则，暗夜魔王在黑夜这个特定时间节点阶段中，自身的技能会获得额外加成，甚至自身还拥有着直接改变当前时间节点的技能方式；<br>
<br>
当然关于‘时间’这个概念，还有很多衍生的用法，在这里我们主要是提炼‘时间触发事件’的概念，以上的三种案例是用来阐述关于时间触发的应用方式；<br>
<br>
<strong>4、空间触发事件</strong><br>
<br>
<div align="center">
<img id="aimg_977161" aid="977161" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095842orhrza8nvn86k84c.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095842orhrza8nvn86k84c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095842orhrza8nvn86k84c.jpg" referrerpolicy="no-referrer">
</div><br>
空间触发：以指定Actor为中心进行空间范围检测，满足预设条件后，触发的技能行为事件；<br>
<br>
在空间触发事件中，通常大家会看到两种方式的应用，范围内有效条件的持续监测和范围边界的条件检测，前者应用途径更广，几乎各种游戏类型都能看到，而后者应用的环境相对较少；<br>
<br>
<div align="center">
<img id="aimg_977162" aid="977162" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095842nj9tj6rh9oregjb9.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095842nj9tj6rh9oregjb9.jpg" width="563" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095842nj9tj6rh9oregjb9.jpg" referrerpolicy="no-referrer">
</div><br>
对于范围触发的事件，我们最多接触的就是类似光环类型的技能，比如‘APEX英雄’中恶灵的‘魔音传脑’，都是类似的应用方式，以自身为中心进行对范围的目标，进行实时检测，只要目标触及范围内，并且满足判定条件，则触发技能事件；<br>
<br>
<div align="center">
<img id="aimg_977163" aid="977163" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095842y58puscp8oznkg7r.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095842y58puscp8oznkg7r.jpg" width="500" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095842y58puscp8oznkg7r.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_977164" aid="977164" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095843po1kyothvypvkiwk.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095843po1kyothvypvkiwk.jpg" width="462" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095843po1kyothvypvkiwk.jpg" referrerpolicy="no-referrer">
</div><br>
除了实时检测直接生效技能效果，还有对于主动触发的判定，比如‘英雄联盟’中堕落天使的‘灵魂镣铐’：<br>
<br>
在释放技能前，以自身为中心进行范围检测，当检测到敌方目标后，满足技能触发条件，触发了对范围内敌人进行伤害和减速效果；如果没有检测到，技能则无法被触发；<br>
<br>
<div align="center">
<img id="aimg_977165" aid="977165" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095843bpk6tklplsopvs5r.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095843bpk6tklplsopvs5r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095843bpk6tklplsopvs5r.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_977166" aid="977166" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095843ck303k66ce50e3c0.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095843ck303k66ce50e3c0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095843ck303k66ce50e3c0.jpg" referrerpolicy="no-referrer">
</div><br>
在‘APEX英雄’的直布罗陀中防护罩技能，则是空间边界的条件检测，以召唤Actor的位置为中心，一定空间范围边界，开启一个立体的防护罩，防护子弹和爆炸伤害；<br>
<br>
这里的防护罩是设置空间范围边界的条件检测，当爆炸发生且爆炸会影响空间边界时，进行空间范围条件检测，检测爆炸点处于防护罩的边界位置，当爆炸发生在防护罩的一侧时，护罩将会挡住爆炸伤害<br>
<br>
关于‘空间’这个事件的应用，除了我们这里的示例介绍，以圆形/球形范围的单次或者持续时间的检测触发的方式；还有在空间范围的形状变化，以及更多在条件判定的应用。<br>
<br>
<div align="center">
<img id="aimg_977167" aid="977167" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095844cs8stsy0iaehsheh.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095844cs8stsy0iaehsheh.jpg" width="484" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095844cs8stsy0iaehsheh.jpg" referrerpolicy="no-referrer">
</div><br>
比如‘英雄联盟’的安妮的焚烧技能，她的技能空间范围检测的则是锥形的范围；<br>
<br>
<strong>5、死亡触发事件</strong><br>
<br>
<div align="center">
<img id="aimg_977168" aid="977168" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095844nmgcmsgkp5s8rwa9.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095844nmgcmsgkp5s8rwa9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095844nmgcmsgkp5s8rwa9.jpg" referrerpolicy="no-referrer">
</div><br>
死亡触发：以指定Actor处于逻辑死亡状态判定后，触发技能行为事件；<br>
<br>
死亡状态，大多数游戏中对死亡的逻辑判定，会聚聚焦为生命属性为0，并且无法进行输入指令操作；是游戏中最长接触的一种状态效果；<br>
<br>
比如‘APEX英雄’中的幻象，当幻象出于逻辑‘死亡’的状态时，在死亡位置生成了假的Actor,自己短暂隐身。<br>
<br>
所以关于死亡触发行为，核心都是判定Actor处于逻辑死亡状态，触发的技能效果。<br>
<br>
<div align="center">
<img id="aimg_977169" aid="977169" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095845xnygmwt9dw339su0.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095845xnygmwt9dw339su0.jpg" width="576" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095845xnygmwt9dw339su0.jpg" referrerpolicy="no-referrer">
</div><br>
比如‘APEX英雄’亡灵的‘死亡图腾’技能应用，在指定的位置生成一个图腾，处于图腾有效范围内，玩家进入死亡状态后，会触发在图腾附近复活重生。<br>
<br>
<div align="center">
<img id="aimg_977170" aid="977170" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095845ph4y6h9c4z4vzc6m.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095845ph4y6h9c4z4vzc6m.jpg" width="477" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095845ph4y6h9c4z4vzc6m.jpg" referrerpolicy="no-referrer">
</div><br>
而在魔兽中关于死亡的另外一种用法，是在遭受判定为死亡状态的时候，转化为抵挡伤害，暂时保持存活状态。<br>
<br>
这两种都是死亡状态时，立刻触发了技能效果，从而改变了死亡状态；<br>
<br>
还有一种是确认了死亡状态，但是设置了即使处于死亡状态，玩家依然在死亡状态下的技能效果；<br>
<br>
<div align="center">
<img id="aimg_977171" aid="977171" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095845p05ugi2zeboi0g02.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095845p05ugi2zeboi0g02.jpg" width="562" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095845p05ugi2zeboi0g02.jpg" referrerpolicy="no-referrer">
</div><br>
英雄联盟中死歌的死亡契约技能效果，当自身出于死亡状态时，改变了死亡的逻辑判定，在延长的技能效果时间内，玩家可以继续释放技能。<br>
<br>
关于这种用法就是一种复合机制的使用方式，首先是在死亡状态触发时，其次是关联了时间触发事件的应用，所以在触发行为事件的应用中，除了单一触发机制判定以外，通常还有多种机制的复合应用方式。<br>
<br>
<strong>6、属性触发事件</strong><br>
<br>
<div align="center">
<img id="aimg_977172" aid="977172" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095846eqpzeq0na0tjq20c.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095846eqpzeq0na0tjq20c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095846eqpzeq0na0tjq20c.jpg" referrerpolicy="no-referrer">
</div><br>
属性触发：检测游戏中Actor属性数值的变化，触发技能行为事件；<br>
<br>
通常在游戏制作的时候，都会对游戏中的Acotr,这里我统称为游戏角色，设定基础属性，用来衡量各种行为状态的标准。<br>
<br>
比如最基础的比如生命值，移动速度，攻击速度等等，而技能相关的还有用来衡量技能消耗的蓝条，或者能量等。<br>
<br>
<div align="center">
<img id="aimg_977173" aid="977173" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095846m9oj0j939lsst9ot.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095846m9oj0j939lsst9ot.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095846m9oj0j939lsst9ot.jpg" referrerpolicy="no-referrer">
</div><br>
英雄联盟中奥拉夫的狂战之怒，是最典型的属性触发方式，每次当血量属性降低的时候，提升自身的移动速度。这种属性触发的应用方式，实质上就是实时监测自身某种属性的变化，满足条件判定后，触发技能行为效果。<br>
<br>
<div align="center">
<img id="aimg_977174" aid="977174" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095847v06qkndg8djgedj4.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095847v06qkndg8djgedj4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095847v06qkndg8djgedj4.jpg" referrerpolicy="no-referrer">
</div><br>
而APEX英雄辛烷的兴奋药剂技能，对比狂战之怒，同样是减少生命值，提升移动速度的技能效果；<br>
<br>
但是在兴奋药剂技能中，是主动触发的方式，技能逻辑是当辛烷使用兴奋药剂技能的时候，持续时间内，提升移动速度，并且自身‘生命值’属性发生变化；<br>
<br>
<div align="center">
<img id="aimg_977175" aid="977175" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095847gi0hiihe4ijei0ah.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095847gi0hiihe4ijei0ah.jpg" width="474" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095847gi0hiihe4ijei0ah.jpg" referrerpolicy="no-referrer">
</div><br>
还有一种是当属性发生变化后，需要判定属性是否达到临界值，这就需要触发的同时针对这一次属性变化进行验证，来确定是否达到技能触发的条件临界值。<br>
<br>
属性触发事件中最常见的触发方式，就是针对属性数值的变化进行判定，当满足条件时就会触发技能效果；<br>
<br>
<strong>7、状态触发方式</strong><br>
<br>
<div align="center">
<img id="aimg_977176" aid="977176" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095847v4pgnngrz7i7ha8h.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095847v4pgnngrz7i7ha8h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095847v4pgnngrz7i7ha8h.jpg" referrerpolicy="no-referrer">
</div><br>
状态触发：检测游戏中Actor状态效果的变化，触发技能行为事件；<br>
<br>
我们在游戏制作中，除了属性数值之外，还有一种常见定义的内容，就是Actor在不同行为下的状态效果；比如最常见的，加速、减速、晕眩、沉默等异常状态效果，通常是游戏中定义Actor在游戏中附加得正向或负面状态效果；<br>
<br>
以‘沉默’这个状态效果为例，游戏中通常定义为Actor处于沉默状态下将无法释放主动技能；当然每个游戏中关于状态的逻辑定义会有些差异，关于各种状态效果和定义方式，将会在后续的状态篇中详细说明；<br>
<br>
<div align="center">
<img id="aimg_977177" aid="977177" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095848k1wwtfwquj8fquct.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095848k1wwtfwquj8fquct.jpg" width="581" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095848k1wwtfwquj8fquct.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_977178" aid="977178" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095848fpr245rcryb2cq6u.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095848fpr245rcryb2cq6u.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095848fpr245rcryb2cq6u.jpg" referrerpolicy="no-referrer">
</div><br>
比如‘APEX英雄’亡灵的‘沉默’技能应用，投掷装置，对范围内得敌人造成无法使用技能得状态效果；<br>
<br>
当然大家有可能会疑惑，这不是‘沉默’技能的直接效果吗？怎么会归到状态出发效果中。<br>
<br>
通常游戏中对于属性和状态触发的用法，是针对属性或者状态发生变化后，验证这两种变化的标准。当满足变化标准后，就会触发技能行为事件；<br>
<br>
<div align="center">
<img id="aimg_977179" aid="977179" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095848ym7r0vvxkn74zj70.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095848ym7r0vvxkn74zj70.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095848ym7r0vvxkn74zj70.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_977180" aid="977180" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095848er6nnmhhlm3bno8l.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095848er6nnmhhlm3bno8l.jpg" width="349" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095848er6nnmhhlm3bno8l.jpg" referrerpolicy="no-referrer">
</div><br>
以魔兽世界中刺客的‘药膏专家’为例，技能效果是针对目标验证是否中毒，如果满足中毒状态的话，将会返还8点能量。<br>
<br>
此处的状态触发事件的使用方式就是针对特定状态‘中毒’的目标进行验证，满足验证目标，将会触发技能事件；<br>
<br>
<div align="center">
<img id="aimg_977181" aid="977181" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095848bmsx9mqpiipswyfx.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095848bmsx9mqpiipswyfx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095848bmsx9mqpiipswyfx.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_977182" aid="977182" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095849xfk8gtqkmd9zk39m.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095849xfk8gtqkmd9zk39m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095849xfk8gtqkmd9zk39m.jpg" referrerpolicy="no-referrer">
</div><br>
当然还有图上这位，玩过英雄联盟的玩家，都知道是谁，疾风剑豪，经常有我方‘托儿索’，敌方剑豪的美誉。<br>
<br>
‘狂风绝息斩’的技能是个典型的状态判定的触发行为；技能触发的条件，是判定当目标处于被击飞的敌方目标空间范围内，才会触发技能事件；<br>
<br>
疾风剑豪的触发机制，是一种需要高端技巧或者队友配合的机制，所以发挥的场景，需要玩家对于技能的衔接理解和熟练度都有一定的要求。<br>
<br>
而通常这种需要状态触发的机制，一般都会定义为游戏中的通用机制。比如减速、击飞、击退等这种大多数条件下满足的技能机制。<br>
<br>
<strong>8、叠层验证触发</strong><br>
<br>
<div align="center">
<img id="aimg_977183" aid="977183" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095849myrc0mqc50rcv00c.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095849myrc0mqc50rcv00c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095849myrc0mqc50rcv00c.jpg" referrerpolicy="no-referrer">
</div><br>
叠层验证触发：验证游戏中Actor上的叠层BUFF，满足验证条件后，触发技能行为事件；<br>
<br>
从严格意义上来说，叠层验证并不是游戏中统一归类的一种触发事件，更多是一种辅助其他触发事件的条件验证方式，使用场景，也是会跟其他的触发机制融合使用。<br>
<br>
不过叠层验证这个机制出现的频率太高，几乎在任何游戏类型，任何游戏方式中都会出现，所以在这里把叠层验证当成一种归类的触发方式来说明；<br>
<br>
<div align="center">
<img id="aimg_977184" aid="977184" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095849n999f2ea6xe2kk8a.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095849n999f2ea6xe2kk8a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095849n999f2ea6xe2kk8a.jpg" referrerpolicy="no-referrer">
</div><br>
例如在英雄联盟中，这种叠层验证的使用方式就层出不穷，目前英雄总共155位英雄，技能中带有叠层验证的英雄超过了100位，<br>
<br>
<div align="center">
<img id="aimg_977185" aid="977185" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095849gc9fu02ugku09ucu.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095849gc9fu02ugku09ucu.jpg" width="592" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095849gc9fu02ugku09ucu.jpg" referrerpolicy="no-referrer">
</div><br>
以黑暗之女安妮为例，嗜火，在施放4次技能后，安妮的下一个伤害技能将会造成晕眩；<br>
<br>
此时的叠层验证应用，是将安妮每次释放技能后，给自身添加BUFF，满足叠层验证次数后将会触发‘晕眩‘状态效果；<br>
<br>
<div align="center">
<img id="aimg_977186" aid="977186" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095850t277y7stk882d8km.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095850t277y7stk882d8km.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095850t277y7stk882d8km.jpg" referrerpolicy="no-referrer">
</div><br>
而沙漠死神内瑟斯的痛苦汲取，则是叠层验证和死亡触发的融合应用方式，判定当敌人死于痛苦汲取的技能效果时，会给自身叠加伤害值；<br>
<br>
<div align="center">
<img id="aimg_977187" aid="977187" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095850gk85o67udd188g6a.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095850gk85o67udd188g6a.jpg" width="550" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095850gk85o67udd188g6a.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_977188" aid="977188" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095850h7244cb4pts2mqxl.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095850h7244cb4pts2mqxl.jpg" width="396" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095850h7244cb4pts2mqxl.jpg" referrerpolicy="no-referrer">
</div><br>
在魔兽世界术士的翻腾痛楚技能中，则进一步把叠层验证的应用方式进一步融合。首先是验证当痛楚BUFF叠加到第4层时，开始造成伤害，其次是痛楚BUFF叠加层数后，将会增加伤害效果；<br>
<br>
在叠层BUFF中，通常我会把BUFF分为两种：<br>
<br>
一种是游戏意义中的有效BUFF，意味着对于Actor有实质意义上的效果BUFF，比如刚才提到的翻腾痛楚BUFF的应用效果，此类型BUFF拥有实质的效果，并且承担了叠层验证的功能；<br>
<br>
而另一种则是无效BUFF，这种BUFF，对于Actor没有实质意义，是作为记录需要验证的标准，比如黑暗之女安妮的技能次数的应用效果；<br>
<br>
写到这里，关于技能模块化技能设计之-触发事件篇也暂时告一段落，个人在写文章的过程中，又重新梳理了一篇过程，深觉的游戏中技能应用的广博，所以本文中的总结仅代表个人的理解，大家如果有什么其他见解，也希望能够跟作者交流。<br>
<br>
来源：腾讯GWB游戏无界<br>
原文：https://mp.weixin.qq.com/s/1_DmKtgYuo71bsWMpEsKIQ<br>
<br>
</td></tr></tbody></table>



  
</div>
            