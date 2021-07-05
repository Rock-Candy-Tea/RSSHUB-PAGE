
---
title: '日本火了十多年的对战游戏：《高达VS》的游戏设计分析'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202106/23/141408w29qud6duqav4pfd.jpg'
author: GameRes 游资网
comments: false
date: Wed, 23 Jun 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202106/23/141408w29qud6duqav4pfd.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2501773">
《高达VS》是一个在日本火了将近20年的游戏IP，该系列游戏每过几年就会推出一个新作品，对游戏的进行迭代式甚至是重构式的升级。其质量之高使得其系列新作哪怕时至今日，依然是日本街机厅投币率最高的游戏。<br>
<br>
在大洋彼岸的日本，日本人还保留着在街机厅玩游戏的文化，他们那边的年轻人一放学不是像国人一样去网吧，而是去街机厅。由于街机厅消费水平非常高，打一把游戏就要投一次币，在街机厅打一下午游戏可能就抵得上手游的一个198大月卡了，所以街机厅的竞争非常之激烈，能在这个激烈竞争中搏杀并且常年的登顶的《高达VS》系列，尤其独到的游戏设计。<br>
<br>
可能很多人会说，“《高达VS》，一听名字那就是靠IP吃饭的，就跟《宝可梦》系列一样，套皮游戏谁还不会做呢”。但各位须知，套着《高达》这个IP的游戏有许许多多，但只有这一个《高达VS》才是投币率常青树。IP固然有着极为重要的作用，但是没有强有力的核心玩法，玩家不会持之以恒的去街机厅为了这个游戏投币。大多数纯靠IP和美术的套皮游戏，都只能支撑极短时间的热度，大多数这种游戏的宿命就是“玩家们兴冲冲地涌进来，骂咧咧走出去”。实际上缺乏了强有力的核心玩法的游戏，寿命都不会长久，这也是游戏业内的“游戏寿命短”的说法的来由，因为大多数游戏确实缺少真正有意思的核心玩法设计。<br>
<br>
本文将会剖析《高达VS》的核心玩法，将其长青不倒的秘密展现出来。<br>
<br>
<div align="center">
<img id="aimg_987375" aid="987375" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141408w29qud6duqav4pfd.jpg" data-original="https://di.gameres.com/attachment/forum/202106/23/141408w29qud6duqav4pfd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141408w29qud6duqav4pfd.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">游戏基础概括</font></strong><br>
<br>
由于笔者并未能去日本玩到《高达VS》系列的最新作，所以本文所有分析将基于移植到了PS4平台上的旧作《高达EXVS MBON》来进行分析。本章节将讲述一下该游戏的一些基本内容以便于读者理解。<br>
<br>
首先既然是《高达VS》，那玩家操作的角色自然就是以“高达”为代表的各式机器人。<br>
<br>
下面这个GIF图非常直观的体现了该游戏的要素。<br>
<br>
<div align="center">
<img id="aimg_987376" aid="987376" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141409sc3z663xxfb6rac5.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141409sc3z663xxfb6rac5.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141409sc3z663xxfb6rac5.gif" referrerpolicy="no-referrer">
</div><br>
图的中心是玩家操作的高达，右下角的UI是高达的武装槽，展示了武装的形态和残弹量（其实就是别的游戏里的技能栏）。左下角的两个大数字是自己机体剩余血量和队友剩余血量，血量清零就会死亡并重新复活。每次死亡以后左上角的绿色COST条就会减少，绿色COST条清零就会输。胜败关键就是保证自己的COST条不清零并把对面COST条清零。<br>
<br>
COST条可以理解为其他游戏里的命数，比方说大家都有三条命，死三次就输。但COST又有别于命数，因为这个游戏里并不是所有机体死亡以后扣除的COST是一样的，也就是说有的机体只有两条命，有的机体能有四条命。这方面的内容留到后面再详细展开。<br>
<br>
然后最独特的来了，图的中心下方，左右两边各有两个计量条。左边的计量条是觉醒槽，觉醒槽过半就可以发动“觉醒”，觉醒能大幅度提升机体的性能甚至是带来新的动作。觉醒的积攒方式是“受到伤害”，“对敌人造成伤害”和“防御”，但主要是靠“受到伤害”来积攒所以一条命基本上就能使用一次觉醒。右边的计量条是行动槽，顾名思义，就是行动时就会消耗，消耗完了就不能做任何行动，机体受到重力影响自由落地，落地以后行动槽就会回复。落地时行动槽消耗的越多，回复行动槽所需的时间也就越长——换句话说，飞得越久，落地硬直就越大。《高达VS》对战的战略和战术核心，就是围绕着觉醒槽和行动槽来构建的。这两个机制是这个游戏的核心，我们后面章节要细讲这个。<br>
<br>
最后就是锁定框，GIF中能看到有个敌方机体身上有一个红色圆圈，这个是锁定框，表示了“你已经锁定这个敌人了，你后续的攻击都会自动跟踪这个敌人”。采用锁定式战斗的3D游戏很多，但大多数都做的不好，所以导致了战斗很无趣。所以我们接下来马上就要讲一讲，围绕着锁定框的玩法设计。<br>
<br>
<strong><font color="#de5650">锁定式射击战斗</font></strong><br>
<br>
在我在开始讲这个章节之前，我想先讲一讲，为什么要有锁定？锁定的优点是什么？锁定式战斗的缺点又是什么？锁定式战斗的缺点很明显，就是游戏很容易变成傻瓜式战斗。那优点呢？为了回答这个问题，我们得先从无锁定的3D战斗开始。<br>
<br>
我们想象一下，玩家操控一架有着导弹，激光枪的人形兵器，在一个无锁定的3D世界里战斗，这是个什么类型的游戏？很明显这是个FPS（第一人称射击）或者TPS（第三人称射击）游戏对吧。因为只要你是一个无锁定式的对战游戏，就必然涉及到一个最根本的问题“要求玩家利用鼠标移动准心去瞄准”。无论你的这个攻击判定多大也好，没有远距离射击武装也好，最终你的游戏逃不开一个问题，“玩家要瞄准”，这个游戏做着做着基本上就会做成一个射击游戏。<br>
<br>
那我们其实都知道，FPS和TPS这种游戏那真的就是年轻人的游戏，过了那个年龄，或者说很多人天生就用鼠标瞄不太准，所以其实有很多人他们是玩不了这种游戏的。那如果这些人他们也想玩个能享受射击的快感的游戏呢？所以这就有了锁定式射击游戏的存在意义。实际上我认为锁定式射击游戏并不只是为了这些人服务的。射击游戏基本上强制要求玩家有个鼠标，用手机和手柄玩射击游戏的体验是非常灾难性的，而锁定式射击在手机上依然还能有个不错的体验。<br>
<br>
而且哪怕是一个重度的射击游戏玩家，他也会对射击游戏感到疲劳，毕竟射击游戏始终逃不开“枪法就是一切”的魔咒，无锁定射击游戏哪怕做再多非射击的机制在里面，玩家击杀始终还是靠的“拖动鼠标对准敌人，按下鼠标开枪射击”这个简单到不能再简单但却又难到不能再难的动作。<br>
<br>
<div align="center">
<img id="aimg_987377" aid="987377" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141410rkz3atewbe7wrp6a.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141410rkz3atewbe7wrp6a.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141410rkz3atewbe7wrp6a.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">锁定距离</font></strong><br>
<br>
所以一个不傻瓜的锁定式战斗该怎么做？让我们先从现实中一个大家都很熟悉的例子中找寻答案——导弹。我们都知道导弹是先锁定再发射的，那导弹有哪些特性呢？<br>
<br>
第一个特性就是“射程“，而射程也就是《高达VS》锁定机制的核心之一。当玩家的锁定目标在玩家的射程之外的时候，玩家的锁定颜色会变成绿色，简称“绿锁”。如果玩家对一个绿锁目标进行射击，这发射击就会是”无诱导“的，换句话说，这发射击并不会持续跟踪敌人，而是直直飞过去。而如果敌人进入了玩家的射程之内，此时锁定颜色就会变成红色，简称”红锁“，提示玩家“此时可以射击了”。此时，玩家射出去的子弹就会像现实中的导弹一样，持续追踪敌人。不同机体的红锁距离是不一样的，而且都是有限的，这就要求玩家能在自己机体的优势距离作战而不是一昧的拉开距离或者拉进距离。<br>
<br>
<div align="center">
<img id="aimg_987378" aid="987378" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141412tbjpj1d7ite1ngpp.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141412tbjpj1d7ite1ngpp.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141412tbjpj1d7ite1ngpp.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">红锁下开枪轻而易举就打中了，而绿锁下开枪对面只需要稍微动一动就打不中</font></font></div><br>
<strong><font color="#de5650">诱导</font></strong><br>
<br>
接下来便是导弹的第二个特性了—跟踪能力，现在的战斗机飞的那么快，对空导弹还是能追着战斗机的屁股命中战斗机，这在《高达VS》中被称作诱导。《高达VS》中几乎所有的射击武装都带有不同程度的诱导，能让高达们的子弹拐着弯命中敌人。所谓不同程度的诱导，就是说，这个游戏中不同武装的诱导强度是不一样的，有的射击武装拐弯幅度大，有的射击武装拐弯幅度小。就像下图中演示的一样，对面一样的飞行轨迹，诱导强的武装能打到对面，诱导差的武装就打歪了。<br>
<br>
<div align="center">
<img id="aimg_987379" aid="987379" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141413r8sasqevszjnk97k.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141413r8sasqevszjnk97k.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141413r8sasqevszjnk97k.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">同样的位置，紫色的光束诱导差所以打歪了，但是导弹诱导强就打中了</font></font></div><br>
<strong><font color="#de5650">弹速</font></strong><br>
<br>
那就有人要说了“那不是诱导强的武装就更强了”？是的，如果只有诱导的话那便是如此，因此《高达VS》里射击武装并不仅仅只是有诱导这个维度的属性。第二个维度就是我要讲的，弹速。<br>
<br>
还记得我在之前提到过“行动槽消耗之后落地会有一段时间不能动嘛”，这个不能动的时间简称为“落地硬直”。设想一下敌人落地之后处于硬直时间，这个时候你诱导强还是弱其实并不能决定你能不能抓到这个硬直，而决定你能不能抓到这个硬直的关键在于“子弹够不够快”。如果子弹够快，快到能在敌人硬直结束之前打中敌人，那诱导差一点是不是也没那么有所谓？当然啦弹速快的作用肯定不仅仅只是局限于抓落地硬直，这个游戏中大部分攻击方式都是有硬直的，而弹速就决定了这个武装能不能抓敌人攻击时的硬直破绽。<br>
<br>
<div align="center">
<img id="aimg_987380" aid="987380" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141414rjpqppk7zpyzrsbs.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141414rjpqppk7zpyzrsbs.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141414rjpqppk7zpyzrsbs.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">第一枪弹速差，打歪了，第二枪弹速好就打中了</font></font></div><br>
<strong><font color="#de5650">判定</font></strong><br>
<br>
第三个维度就是判定了，《高达VS》里面，不同的武装有不同的判定大小，有的判定大，有的判定小。判定大这个很好理解，判定越大，就越容易打中对面，就越强。许多大判定武装还可以用来“歪打正着”，歪着打但是对面却撞了上去，俗称打事故。<br>
<br>
<div align="center">
<img id="aimg_987381" aid="987381" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141415k6zodyxyjpyl7ec5.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141415k6zodyxyjpyl7ec5.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141415k6zodyxyjpyl7ec5.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">枪口补正</font></strong><br>
<br>
第四个维度就是枪口补正。这个设计是非常体现细节的地方。<br>
<br>
大部分锁定式射击游戏都是敌人走到哪，枪就能跟到哪，而《高达VS》则不同。《高达VS》中，枪口补正指的是射击武装的“跟枪能力”。玩家按下射击键之后，子弹并不会立刻射出，而是机体会先有一个瞄准动作，瞄准动作结束之后子弹才会射出来。而在这个瞄准的过程中，敌方一旦上下左右移动，机体就需要进行一个“跟枪”。枪口补正强的武装，这个“跟枪”的速度就更快。<br>
<br>
换而言之，如果对面移动速度够快，而自己这边枪口补正不够强，那么就很有可能发生“子弹射出去时，枪口并没有完全对准对面”这样的情况，简称打歪了。那这个枪口补正主要起到一个什么作用呢？首先第一个，近身作战的时候，由于距离近，敌方的轴速度较之远距离下大得多，枪口补正差的武装很有可能就会打歪了。所以枪口补正强的射击武装在近距离就更加厉害。第二个，弹速快而诱导差的武装，哪怕距离远，也非常依赖于枪口补正，毕竟诱导差就意味着如果它射出去的时候就太歪了，后面会无法及时转过弯来命中敌人。<br>
<br>
<div align="center">
<img id="aimg_987382" aid="987382" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141417yg2vo6ev5v6v6qr9.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141417yg2vo6ev5v6v6qr9.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141417yg2vo6ev5v6v6qr9.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">强枪口补正的武装在近距离抓落地非常好用</font></font></div><br>
<strong><font color="#de5650">有无硬直</font></strong><br>
<br>
《高达VS》中的武装分为有硬直和无硬直武装。无硬直武装可以随时使用而且不影响机体当前做的动作。有硬直武装一但被使用，就会使机体当前动作停止，并在整个武装使用过程中都停滞在空中。这个游戏大部分性能强力的武装都是有硬直的。所以一般有硬直武装都是“高风险高收益”，而无硬直武装则是“低风险低收益”。特别强力的武装还会有特别长的硬直。<br>
<br>
<strong><font color="#de5650">其他属性</font></strong><br>
<br>
综上所述的这些属性和一些其他属性比如前摇后摇、伤害、弹量、再装填速度还有位移等等，构成了一个非常高维度的射击武装深度，使得《高达VS》里的射击武装可以做出其他游戏无法匹及的差异化。在这之上再加上一些特殊机制和行动机制，就使得《高达VS》的射击战变得非常的丰富有趣，甚至要远远有趣过无锁式的射击游戏。而我们下一章就要谈到和射击武装密不可分的行动机制。<br>
<br>
<strong><font color="#de5650">行动机制</font></strong><br>
<br>
大部分的3D游戏的行动机制都是“玩家通过上下左右键操控角色在地上行走”，“玩家松开方向键，角色就会停下”，“玩家按下冲刺键，角色就开始加速跑步”，“玩家按下跳跃键，角色就会起跳”。有的游戏里还会给玩家加入一个体力槽的设定，冲刺和跳跃的时候会消耗体力槽，体力槽在不被消耗的时候会持续恢复。这套设计用于大部分的3D游戏都说不出有什么问题，因为大部分的3D游戏里玩家操控的角色都是人类或者说至少也是个动物，这套设计是一个比较成功的对现实世界人类运动模式的抽象。<br>
<br>
但是这套东西放在高达上面就不太对了，高达是什么？高达是全身上下都有喷气孔的巨大机器人，能够在天空和宇宙翱翔。那套传统3D游戏的运动方式设计显然是无法满足对高达的还原的。<br>
<br>
<div align="center">
<img id="aimg_987383" aid="987383" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141418zg1tgphvg1pg1fgc.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141418zg1tgphvg1pg1fgc.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141418zg1tgphvg1pg1fgc.gif" referrerpolicy="no-referrer">
</div><br>
那让我们直接来看看《高达VS》制作组的答案吧。<br>
<br>
首先《高达VS》里面，所有机体都会受到重力影响而下落直至站到地面。玩家如果只是单纯的按下方向键，机体就只会在地面笨拙缓慢的行走，几乎就是一个纯靶子（行走在《高达VS》里几乎就是一个完全无用的动作）。但如果玩家按下冲刺键，玩家操控的机体背后的喷口就会进行一个喷射，机体会瞬间加速并朝着面向方向移动一大段距离。在这之后，玩家可以选择拉住方向键让机体持续匀速的朝着方向键方向移动，也可以连续喷射让机体进行一个不匀速的运动。<br>
<br>
需要注意的是，在空中，机体一样可以进行喷射的动作，也就是说，借由喷射这个动作，玩家可以自由地让自己的机体在任意高度进行平面的移动。冲刺这个动作还可以取消机体的所有硬直，使得这个游戏的战斗非常的灵活。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_987384" aid="987384" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141419a9nnnmn5mygnigli.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141419a9nnnmn5mygnigli.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141419a9nnnmn5mygnigli.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">行走，喷射冲刺</font></font></div><br>
那么有了平面的移动能力，自然也要有垂直的移动能力。玩家在无硬直的情况下按下跳跃键，机体就会将喷口朝下喷射，让机体往天上攀升。但这个从纯粹往上攀升的动作十分笨拙，因此就需要利用《高达VS》里的惯性系统。<br>
<br>
在《高达VS》里，机体运动的惯性是会保留的，玩家喷射动作结束之后机体并不会立刻停下，而是会受到重力影响进行一个抛物线运动直至落地，在落地之前，玩家只要按下跳跃键，机体就会在保持原来冲刺的横向动量的同时，添加一个向上的动量，做出一个45度角发射炮弹的运动轨迹。这个冲刺-跳的动作在《高达VS》里意义非凡，因为单纯的平面移动是无法躲开交叉火力的，很多时候玩家需要一个既能躲开交叉火力又能大幅度拉进或者拉远距离的动作。这个冲刺跳就赋予了玩家一个穿越重重炮火接近敌机的能力。<br>
<br>
<div align="center">
<img id="aimg_987385" aid="987385" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141421wff7zp6zooeiy6fg.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141421wff7zp6zooeiy6fg.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141421wff7zp6zooeiy6fg.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">利用冲刺跳穿越炮火接近敌机</font></font></div><br>
这个游戏中有一部分武装的诱导强力到光靠飞行完全无法躲开，会死死的跟住敌人直到命中。因此《高达VS》中还存在着一个叫”闪避”的动作。机体的闪避动作会使得此时所有已经锁定了机体的武装都会失去诱导，就像是战斗机使用热诱弹骗掉了导弹的追踪一样。这个动作有着极其强力的闪避性能，机体在闪避发动的时候几乎没有任何武装能打中机体。但是这个动作也有着极大的代价。闪避结束后机体会陷入一个非常长时间的僵直状态，而且闪避会消耗大量的行动槽。因此玩家不能滥用闪避动作，而是利用闪避动作来回避掉有强诱导的武装。<br>
<br>
<strong><font color="#de5650">行动槽</font></strong><br>
<br>
冲刺，跳跃，重力，构成了高达VS最基础的移动体系，这三个机制分别对应了平面，向上，向下的维度。这套动作过于灵活以至于如果一个机体一直这样移动，那几乎没有任何射击武装能打到这个机体，因此就需要有所限制，这个限制机制就是行动槽。也就是我们在文章开头所说的那个UI界面的蓝色条。<br>
<br>
<div align="center">
<img id="aimg_987386" aid="987386" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141424eza6cgyhh88vkzh7.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141424eza6cgyhh88vkzh7.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141424eza6cgyhh88vkzh7.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">行动槽</font></font></div><br>
我们文章开头已经介绍过行动槽了，所以这章我们要更加深入一下行动槽给游戏所带来的变化。<br>
<br>
行动槽简要概况一下就是“离地进行行动就会扣槽”，“落地硬直就会回槽”。这就意味着如果一个玩家他一直在非常低空的位置“贴地移动”，他就可以随时想落地就落地，想回槽就回槽。但是这种贴地式移动的问题就在于，由于缺少了垂直方向上的移动，会非常难以躲避强力的射击武装，也因此难以越过敌方的火力网进行突围。<br>
<br>
而另一方面，冲刺跳这种移动方式，就能提供非常优秀的回避和突防能力，而且由于冲刺跳仅仅只需要在起跳的时候耗槽，后续移动是利用惯性完成的，所以使用冲刺跳的玩家能用更少的槽量做出更久的滞空，能在短时间内获得行动槽量上的优势，能让自己有更多的槽去抓对面的落地。但是冲刺跳却会使得自己置于高空，不能随时想落地回槽就落地回槽，因此使用了冲刺跳的一方就要考虑“这个冲刺跳用完之后这个距离是否足够短到能让我抓到对面？这个位置是否值得我去用这个冲刺跳？”<br>
<br>
简单来说，高空飞行有更优异的回避性能和短时间内更少的槽量消耗，而低空飞行有更灵活的回槽时机，因此玩家需要根据战况灵活选择低空飞行还是高空飞行。<br>
<br>
<div align="center">
<img id="aimg_987387" aid="987387" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141426nmtdn2nahc2kdxcm.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141426nmtdn2nahc2kdxcm.gif" width="260" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141426nmtdn2nahc2kdxcm.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">灵活使用高飞躲避弹幕</font></font></div><br>
机动槽使得玩家必须要对自己的行动进行一个非常严格的资源管理，玩家不能一昧的乱按动作，必须要计算“我这个行动槽能做多少事”。比方说玩家耗费了一半的机动槽去追击敌人，这个时候他就要思考“我是用这剩下的机动槽继续追，还是放弃深追保证自己安全第一”。这种资源限制就使得玩家需要在不同的战局下思考不同的策略，有的时候玩家需要激进一些，而有的时候玩家又需要保守一些。这种设计使得玩家不能一昧的保守，又不能一昧地激进，因为前者会导致玩家打不到人，后者又会导致玩家常常陷入危险之地。<br>
<br>
<div align="center">
<img id="aimg_987388" aid="987388" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141427nyscevh4hp4epn9r.jpg" data-original="https://di.gameres.com/attachment/forum/202106/23/141427nyscevh4hp4epn9r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141427nyscevh4hp4epn9r.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">机动性属性</font></strong><br>
<br>
大部分3D游戏里，影响玩家角色机动性的属性只有“移动速度”，一个角色只要移动速度更快，那这个角色就是更强的。而《高达VS》则有一套级高维度的机动性属性。影响一台机体的机动性的属性有远远不止一个，因此《高达VS》里机体的机动性差异化非常之大。本节就将讲述一下《高达VS》里，影响一台机体机动性的属性。<br>
<br>
<strong><font color="#de5650">行动槽长度</font></strong><br>
<br>
第一个机动性属性就是机动槽长度，这个很好理解。机动槽长度越长，机体一次离地能做出的动作就更多。有的机体最多能冲刺8次，有的只能冲刺6次。能冲刺8次的机体在狗斗上就会有明显优势。<br>
<br>
<div align="center">
<img id="aimg_987389" aid="987389" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141430y99z81sp1bjowmfw.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141430y99z81sp1bjowmfw.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141430y99z81sp1bjowmfw.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">冲刺速度</font></strong><br>
<br>
第二个机动性属性是冲刺速度，这个也很好理解，基本上就是对应着普通3D游戏里的移动速度。但是略微有点不同的是《高达VS》里，还分为冲刺初速度和巡航速度。<br>
<br>
冲刺初速度指的是冲刺动作出来后极短一段时间内的速度，而巡航速度则是冲刺速度过后玩家持续朝一个方向飞行的匀速运动的速度。这两个属性的区别其实很微妙，因为如果一台机体的巡航速度明显要慢过冲刺初速度的话，那玩家只需要一直连续冲刺就好了。而且连续冲刺这种运动模式也较之巡航模式更加灵活，所以说一般来讲都是看一台机体的冲刺初速度，但是也有例外情况。<br>
<br>
<div align="center">
<img id="aimg_987390" aid="987390" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141431t1m5lo9l81f8qqiu.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141431t1m5lo9l81f8qqiu.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141431t1m5lo9l81f8qqiu.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">转向性能</font></strong><br>
<br>
在《高达VS》里更常见的称呼是旋回性能，简单来讲就是在巡航模式下一台机体的转弯角速度。旋回性能越好的机体，转向角速度就越大，也因此就在狗斗中有更大优势。最直观的一个体现就是旋回性能优秀的机体只需要轻轻的一个转向就能躲开追尾而来的子弹，而旋回性能差的机体就被迫要起跳拉高或者向另一个方向冲刺。冲刺转向耗费的行动槽会比旋回转向要更多，因此有着优秀的旋回性能的机体在枪林弹雨下会明显的有槽量优势。<br>
<br>
<div align="center">
<img id="aimg_987391" aid="987391" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141433w8c51cu1z2hukc31.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141433w8c51cu1z2hukc31.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141433w8c51cu1z2hukc31.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">上升速度</font></strong><br>
<br>
不同的机体有着不同的上升速度，对应着的是空战的潘升性能。有着优秀上升速度的机体可以利用冲刺跳轻而易举地拉高到一个对面根本打不到的高度，越过对面火力防线直接贴脸进攻，也可以利用冲刺跳轻而易举地躲开对面的攻击，而且由于跳的比一般的机体更高，机体可以利用这段冲刺跳的惯性拉开更长的距离，对面如果想要追击的话就会陷入机动槽的劣势。当然具体能拉开多长的距离还要看机体的冲刺速度，因为平面的动量是来自于冲刺的。一般来说更快的上升速度就是更强的。<br>
<br>
<div align="center">
<img id="aimg_987392" aid="987392" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141435ykckd0trz0c6p01c.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141435ykckd0trz0c6p01c.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141435ykckd0trz0c6p01c.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">下落速度</font></strong><br>
<br>
这个游戏的机体都是受到重力自由匀速下落的，但是可以理解为不同的机体下降受到的阻力不同，有的机体下降速度要比别的机体更慢。下降更慢的机体会更加的难以落地。<br>
<br>
<div align="center">
<img id="aimg_987393" aid="987393" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141436t23vbfj523tzw552.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141436t23vbfj523tzw552.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141436t23vbfj523tzw552.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">特殊移动</font></strong><br>
<br>
在《高达VS》里，大部分机体都有一到两个特殊的移动方式。有的是一段大幅度的弧形冲刺，有的是瞬间起跳到高处再垂直落下，有的是向侧面进行一个大幅度的侧空翻，这种类似于空战中的特技表演一般的动作。这些动作同样需要消耗行动槽，而且大部分还有冷却时间，不能像冲刺或者跳跃一样连续使用。不少机体在特殊移动的途中还能派生出平时使用不了的强力攻击招式，因此不少机体的进攻是围绕着特殊移动的使用来进行的。<br>
<br>
这种特殊移动本质上是给了机体一个“短时间内突破机体基础机动性限制”的手段，是使得游戏节奏跌宕起伏的“爽点”。因为如果大家都没有特殊移动，那就是大家一直狗斗，直到基础机动性更好的一方取得槽量上的优势然后抓到对方。而特殊移动则给了那些基础基础机动性更差的一方一个“扭转劣势”的机会，这使得《高达VS》的狗斗不再是非常线性的缠斗，而是此起彼伏的博弈，充满着不可预知性。<br>
<br>
而且另一方面，各式各样的特殊移动也使得《高达VS》的战斗十分帅气，令人血脉喷张。特殊移动还大大加强了机体之间的差异性。不少机体的核心战斗方式就是围绕着自己的几个特殊移动进行的，因此《高达VS》里你很难找到战斗方式相似的机体，因为他们都有自己独有的一套特殊移动。特殊移动的种类在《高达VS》里数不胜数，大大增强了《高达VS》的趣味性和爽快度。<br>
<br>
<div align="center">
<img id="aimg_987394" aid="987394" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141438jc2h7w7bcr2j8jfx.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141438jc2h7w7bcr2j8jfx.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141438jc2h7w7bcr2j8jfx.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">高维度数值系统下的平衡和多样性</font></strong><br>
<br>
其实聪明的读者看到标题就应该能想到我这章的内容了。没错，由于有着极高维度的属性，《高达VS》的机体在有着极高多样性的情况下依然保持着相当不错的平衡性。<br>
<br>
想要做一台射击性能比谁都强的机体？可以，那就给他一个诱导极强的射击武装，再给他一个弹速极快的射击武装，而且判定都很大，但是机动性上就让这台机体变得比较差，冲刺速度要比一般机体慢，上升性能也要差点。想要做一台专注近距离战斗的机体？可以，那就赋予它顶级的冲刺速度和冲刺次数，赋予他两个强力的特殊移动，给他近距离枪口补正极为强力而且发生极快的射击武装，但是让他所有的射击武装的距离都非常短而且诱导不佳。<br>
<br>
因此《高达VS》里有着大量的非常“极端”但是又不“过于强力”的机体，也有大量性能上非常“平衡”但是又不“平庸”的机体。这样的多样性就使得玩家必须要去考虑“我的机体的长处是什么？短处是什么？我该怎样利用我的机体的长处去攻击对方机体的短处？”这种不对称对局使得玩家可以去尽情发挥“我的机体与别人不一样的地方”，而不是“所有人都用着一样的东西，比谁用的更好”。而且哪怕玩家一直开同一台机体，他的对手开的机体不一样，就是得玩家需要去钻研对付“不同的机体”所需要的“不同的对策”。再加上《高达VS》还是一个2V2对局，不同的机体组合需要的打法也是不一样的，因此《高达VS》的可玩性可挖掘性非常之高，高到玩家们打了成千上万局都不嫌累不嫌无聊。<br>
<br>
<div align="center">
<img id="aimg_987395" aid="987395" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141440cjwr0110kqjbrp4p.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141440cjwr0110kqjbrp4p.gif" width="260" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141440cjwr0110kqjbrp4p.gif" referrerpolicy="no-referrer">
</div><br>
但是《高达VS》远远不仅如此。如果所有机体的强度都差不多，哪怕数值维度再高，如果大家机体的平均强度是一样的，多样性始终是有限的。<br>
<br>
文章一开头我们提到过，高达VS里的机体有3000 cost，2500 cost, 2000 cost, 和 1500 cost四个档位。这四个档位的机体的基础性能就是四个档位的。<br>
<br>
3000cost的机体在基础性能上几乎全面强于2500cost，而2500 cost又全面强于2000 cost，1500 cost 又再全面强于1500cost。<br>
<br>
举个具体的例子，3000cost的机体平均有7次的冲刺次数，而2000cost的机体平均仅有5次的冲刺次数。而冲刺速度，上升速度这些属性上，3000cost也是要全面优于2000cost的。那有读者就要问了，这样做有什么意义呢？玩家可能都去玩3000cost的机体了啊，玩家肯定都想玩强的啊。这就是《高达VS》制作组设计巧妙的地方了。<br>
<br>
我们文章开头提到过，玩家一局里面总共有6000cost，也就是说，如果玩家使用3000cost的机体，他就有两条命，如果他使用2000cost的机体，他就有三条命。而这个游戏里，3000cost的机体的平均血量是650血，而2000cost的机体平均血量是600血。发现了么？大家都是6000cost, 2000cost的机体总共有1800血，而3000cost机体只有1300血。也就是说3000cost机体其实是“高风险，高收益”，3000cost的基础性能各方面都强于2000cost，但是却挨不起几下，2000cost的基础性能各方面都要弱不少，但是却有着更高的容错率。<br>
<br>
<div align="center">
<img id="aimg_987396" aid="987396" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141440rqkqwg4gbu7u00qb.jpg" data-original="https://di.gameres.com/attachment/forum/202106/23/141440rqkqwg4gbu7u00qb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141440rqkqwg4gbu7u00qb.jpg" referrerpolicy="no-referrer">
</div><br>
经过《高达VS》玩家多年的游玩和探索，大家基本上形成了“一台高cost机体组一台低cost机体“的打法用以谋求”风险和性能“的相对平衡。高达VS是一个2对2的双打游戏，如果一队两台机体都是低cost机体，那么就会因为两台机体性能都太低而无法维持战局，被高性能阵容一边倒的压着打。如果一队两台机体都是3000cost这样的高性能机体，就会因为总血量太少而导致容错率太低，明明是一直在压着对面但是一波失误就会葬送掉胜利。<br>
<br>
玩家对游戏的探索也影响了制作组制作机体的方向，因此3000cost的机体主要都是利用强大的机动性，站在阵线的第一线，为队友撑起整条战线。2500cost的机体则是介于前线和后方之间，一般承担着支援和偷袭的任务。2000cost的机体则大部分都是纯后方支援机体，但是也有少部分是近距离单挑特化机体，虽然机动性很差导致无法在密集火力下存活，但是一旦找到机会近身就会发挥强大的威力。<br>
<br>
而1500cost的机体则最为特殊，1500cost的机体往往是担任着前线的职责，没错，机动性最差的cost却依然是站在前线的位置。这是因为《高达VS》里，1500cost的机体往往由于生存能力太差，而不适合担任后方支援的职责因为太容易被对面一波冲死。但是制作组却赋予了1500cost机体各式各样强大的射击武装，这些强大的武装使得这些1500cost机体可以强行利用优异的射击武装去和对面”换血“。我们知道1500cost的机体的实际血量是最多的，因此虽然1500cost机体的机动性要比高cost机体差得多，但是通过”换血“式打法，1500cost站在前线却依然有可以和3000cost的机体一战的资本。<br>
<br>
而且，这种不对称性还使得场上局面不容易陷入僵持阶段，因为如果双方机体强度差不多，玩家水平差不多，那大家很可能打着打着就陷入僵持阶段，谁也打不到谁。但由于场上有着低cost机体的存在，低cost机体对于高cost机体来说就是突破口，高cost机一旦谁都打不到谁，就会去找对方的小弟麻烦，然后另一边的高cost机体就会为了保护自己的“小弟”而不得不去跟对面拼命。这种性能上的不完全对称使得双方总能找到打破局面的突破口，避免游戏进入僵持的垃圾时间。<br>
<br>
<div align="center">
<img id="aimg_987397" aid="987397" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141444rinjbfbbrxdjbgbd.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141444rinjbfbbrxdjbgbd.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141444rinjbfbbrxdjbgbd.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">觉醒系统</font></strong><br>
<br>
经常看电子竞技比赛的玩家应该都知道，两边一直互相稳重的“摸”对面，“打运营”，打试探，但不实际去进攻，这个是一件非常无聊而且令人沉闷的事。会发生这种事情，主要是因为在大部分对抗类游戏中，“进攻”的风险是比“防守”和“消耗”要大的。这个其实很好理解，因为防守的一方可以以逸待劳，等进攻方消耗了他们的资源冲到防守方脸上，防守方再反击打回去，俗称“打后手”。打后手几乎是任何游戏都无法避免的事情。<br>
<br>
对于《高达VS》这种游戏来说就更是了，两边经常打着打着就变成了大家保持安全距离“抽奖”和“摸枪”以防止自己被对方“打后手”。这种事情不是说不能有，而是说如果一直这样，就太无聊了。玩家需要一个能给游戏节奏带来改变的东西，一个打破均势的“tie-breaker”。这就是设计“觉醒“的意义，一个打破均势的利刃，一个游戏节奏的爽点，而且还是取胜战术的核心。<br>
<br>
<div align="center">
<img id="aimg_987398" aid="987398" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141446toizzoppoc4742pt.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141446toizzoppoc4742pt.gif" width="260" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141446toizzoppoc4742pt.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">双方均势陷入僵持阶段谁也打不中谁</font></font></div><br>
让我们先回忆一下觉醒的基本介绍：当玩家的机体受到伤害或者是造成伤害之后，玩家的觉醒槽就会增长，觉醒槽积累的越长，觉醒时间就越长。当觉醒槽过半之后，玩家就可以发动觉醒，发动觉醒的瞬间会回复大量的行动槽。觉醒状态下机体的机动性、伤害、武装性能都会大幅度提升，甚至部分机体的个别招式形态都会改变。一个2000 cost的机体开了觉醒之后的性能甚至强于3000机许多，而一个3000 cost的机体开了觉醒之后甚至能压着对面两台没有开觉醒的机体打。觉醒如此强横的性能使得觉醒的使用成为了《高达VS》里战术的核心。不少机体甚至是觉醒能力特化型的机体，这种机体在没有觉醒的时候相对较弱，但是开了觉醒之后的爆发力极为强势，一波觉醒进攻就能把对面好不容易建立起来的优势全部摧毁。<br>
<br>
<div align="center">
<img id="aimg_987399" aid="987399" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141447xvuatzprdfnrtru9.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141447xvuatzprdfnrtru9.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141447xvuatzprdfnrtru9.gif" referrerpolicy="no-referrer">
</div><br>
觉醒如此重要，而觉醒槽的积攒却主要来源于受伤扣血，纯靠扣血的话，大部分机体扣掉五分之一的血就能攒出一个觉醒，也就是说基本上大家一条命最多就只能觉醒一次。虽然攻击敌人造成伤害也能积攒觉醒槽，但是积攒的量非常之少，少到哪怕玩家造成了很多伤害，两条命用完也无法攒出第三个觉醒。<br>
<br>
因此，3000cost的机体用完了整整6000csot也就只能出两次觉醒，而2500cost的机体能觉醒三次，2000cost的机体能觉醒四次，1500cost的机体还能觉醒更多。但由于3000cost机体的觉醒质量最高，所以玩家普遍倾向于把cost交给3000cost的机体来用。<br>
<br>
<div align="center">
<img id="aimg_987400" aid="987400" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141449nlgpfmq2kaak2f3y.gif" data-original="https://di.gameres.com/attachment/forum/202106/23/141449nlgpfmq2kaak2f3y.gif" width="280" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141449nlgpfmq2kaak2f3y.gif" referrerpolicy="no-referrer">
</div><br>
前面说到觉醒是为了破坏僵局而存在的。那为什么因为有了觉醒僵局就会被破坏呢？玩家不能捏着觉醒继续打后手么？实际上是可以的，但是，这样就很有可能会输掉比赛。<br>
<br>
我举个例子来说明。<br>
<br>
假设说一台3000cost的机体在第一条命被人打掉了五分之四的血量，他这个就有了第一个觉醒，如果他这个时候把觉醒用掉而且还没有掉血，那么第一个觉醒结束之后，包括第二条命在内，他会有五分之六的血量去攒第二个觉醒，那他基本上稳稳的能攒出第二个觉醒。<br>
<br>
<div align="center">
<img id="aimg_987401" aid="987401" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141450o9s1u50u93vv3933.jpg" data-original="https://di.gameres.com/attachment/forum/202106/23/141450o9s1u50u93vv3933.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141450o9s1u50u93vv3933.jpg" referrerpolicy="no-referrer">
</div><br>
而如果这台机体第一条命没用把这个觉醒放出来，他捏着觉醒死了，他就只剩下五分之五的血量去攒第二个觉醒，如果他第一个觉醒使用的时候还被人打了几下，那等到第一个觉醒结束的时候，他就只剩下不到五分之四的血量，这个血量下他已经无法再攒出第二个觉醒了，最终的结果就是残局时刻敌人会带着觉醒过来进攻，而他却没有觉醒去反制对面。《高达VS》中多的是因为想要捏着第一个觉醒不用等机会而失误扣血，导致第二命攒不出第二个觉醒，最后被敌人用第二个觉醒一波进攻击败的事例。因此，觉醒不仅仅是一个进攻的利刃，这还是一个烫手山芋，如果玩家有了觉醒以后不赶紧把觉醒用了，很有可能就会输掉比赛。这个设计促使玩家必须积极去考虑使用觉醒来进攻，推进整盘游戏的节奏，而不是消极防守。<br>
<br>
<div align="center">
<img id="aimg_987402" aid="987402" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141454stkaca78o5zlfcil.jpg" data-original="https://di.gameres.com/attachment/forum/202106/23/141454stkaca78o5zlfcil.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141454stkaca78o5zlfcil.jpg" referrerpolicy="no-referrer">
</div><br>
捏着觉醒被打的惩罚极大，反过来说，如果能主动利用觉醒去打掉对面的血量，比方说对面快要有觉醒了，而我们这边已经有了觉醒。如果我们这个时候主动开启觉醒去进攻对面，把对面的血量打掉一大截，就可以让对面被迫“无法在刚攒出觉醒的血量就开启觉醒”，使得对面的第二个觉醒变得格外难以攒出来。<br>
<br>
<div align="center">
<img id="aimg_987403" aid="987403" zoomfile="https://di.gameres.com/attachment/forum/202106/23/141454ntahhxut6tqjt1ya.jpg" data-original="https://di.gameres.com/attachment/forum/202106/23/141454ntahhxut6tqjt1ya.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/23/141454ntahhxut6tqjt1ya.jpg" referrerpolicy="no-referrer">
</div><br>
《高达VS MBON》里还有三种不同种类的觉醒，分别是格斗觉醒，射击觉醒和防御觉醒。格斗觉醒会大幅度强化机体的格斗性能，射击觉醒则大幅度强化了机体的设计性能，防御觉醒则是允许机体在被攻击的时候开启觉醒脱离受击硬直。《高达VS》后续最新作里还添加了更多的觉醒类型，比如机动性强化的觉醒，比如辅助队友的觉醒等等等等。<br>
<br>
<strong><font color="#de5650">尾声</font></strong><br>
<br>
本文到这里就结束了。<br>
<br>
实际上仍然有大量《高达VS》的设计和机制并未在本文中被提及，但受限于篇幅，我想还是在这里停笔比较好。本文仅仅只是讲述了高达VS的机制中最为核心的“基石“部分。以后可能会再分析一下《高达VS》中格斗战的机制，分析一下在这个锁定式的射击框架下，格斗战系统该如何制作。但无论如何，那也是以后的事了。我个人认为《高达VS》的这套机制并不仅仅只适用于制作 “锁定式射击战斗对战游戏”，其中大量的设计理念比如“非对称对抗”，“僵局破坏机制”，“高风险高收益和低风险低收益并存”，“行动槽管理机制”，“高维度招式属性和机体属性”，“惩罚捏着觉醒不使用机制”都非常值得各式对战游戏进行学习。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：机核</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/9aOnJWS7zgHe1l4kBqt8vA</font></font><br>
</td></tr></tbody></table>



  
</div>
            