
---
title: '网易雷火GDC：让玩家在等待复活时忙起来-战意的死亡系统设计'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/23/104225h39azjk3jx88ghbw.jpg'
author: GameRes 游资网
comments: false
date: Fri, 23 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/23/104225h39azjk3jx88ghbw.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2506239">
北京时间7月23日，在今年游戏开发者大会（GDC2021）上，来自网易雷火UX用户体验中心的体验设计师书桓进行了精彩的分享，游戏开发者大会每年在旧金山举办，如今已有35届，是一场高质量的大型游戏开发者盛会。<br>
<br>
<div align="center">
<img id="aimg_994837" aid="994837" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104225h39azjk3jx88ghbw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104225h39azjk3jx88ghbw.jpg" width="318" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104225h39azjk3jx88ghbw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">网易雷火UX用户体验中心体验设计师书桓</font></font></div><br>
书桓于2019年校招进入网易，参与了多款端手游项目的研发工作，具有丰富的体验设计经验，他所在的网易雷火UX用户体验中心是全球知名的一流用户体验团队，业务包含用户研究，大数据开发，体验设计等领域。GDC 全球游戏开发者大会二十年来的非赞助类演讲中，雷火UX入围数占据中国游戏行业的40%以上，与多所高校建立了密切的合作关系。<br>
<br>
<div align="center">
<img id="aimg_994838" aid="994838" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104226uz080c57wcav084k.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104226uz080c57wcav084k.jpg" width="137" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104226uz080c57wcav084k.jpg" referrerpolicy="no-referrer">
</div><br>
本次分享的内容是基于他对游戏死亡系统的思考和运用实践得出的。以下是分享实录：<br>
<br>
书桓：大家好，感谢大家来听我的本次分享，我是书桓，今天我要分享的主题是《让玩家在等待复活时忙起来：战意的死亡系统设计》。今天，我将和大家讨论我们是怎样从系统设计到体验设计构建《战意》这款游戏的死亡系统的。<br>
<br>
今天的分享主要会分为以下几个部分：首先是战斗中死亡所带来的机遇与威胁，它们之间的博弈所带来的游戏的趣味性，以及我们对游戏中死亡所代表的感受的思考。然后我将深入游戏中不同元素的死亡的设计以及我们对其中机会与风险的权衡，比如战马，兵团和武将本身。在这之后，我将从游戏中最重要的武将这一元素进行深入展开，讲述我们的具体设计和思考。最后，是玩家在游戏中死亡的情感体验和我们如何设计优化他们的情感体验的。<br>
<br>
首先给大家介绍一下《战意》这款游戏。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994839" aid="994839" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104226y6mv4cmt03gk56f6.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104226y6mv4cmt03gk56f6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104226y6mv4cmt03gk56f6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《战意》最新赛季——“王朝”</font></font></div><br>
《战意》是一款中世纪背景的在线战术动作游戏。作为一个将军，你将指挥你的军队，在15VS15的史诗级攻城战中杀死敌人、攻占土地。在辽阔的大陆上，与人结盟，攻城略地，成为大陆最强的统治者。<br>
<br>
战斗中会有一千多名士兵参与战斗，你在其中作为一名骁勇善战的将领，可以选择不同的兵团通过射击、防御、近战等战术击穿敌人的防御。你可以命令英国长弓手远距离射击敌人，带领一堆波兰翼骑兵从高地冲溃敌军，或者使用强大的攻城器械摧毁敌人的防御工事。在这个史诗级战场上，两支各15名玩家的队伍互相厮杀直至胜利。<br>
<br>
在攻城战中，进攻方必须夺取最后一面旗帜才能获胜，而防守方必须在游戏结束时至少守住一面旗帜。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994840" aid="994840" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104227wo7uqvwvq1qq2g7u.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104227wo7uqvwvq1qq2g7u.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104227wo7uqvwvq1qq2g7u.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《战意》宏伟的战斗场面</font></font></div><br>
从介绍中，我们将死亡视为对玩家的一种风险，就像现实生活中一样。但是从另一方面来说，如果他们的敌人死亡，这也是他们的一次机会。这种机遇与风险并存的情况和其他很多游戏类似。<br>
<br>
比如在一些射击游戏中，玩家唯一需要考虑的就是杀戮本身。杀敌最多的玩家赢得最后的胜利，这也是玩家的乐趣所在，这就是他们唯一想在游戏中做的事情。但是在一些大逃杀游戏中情况变得不同。因为只有一次生命，所以只有活下来的人才能赢得比赛，因此死亡的威胁要远大于杀死一个人所带来的优势和机遇，这也就使得玩家变得更为谨慎。而在MOBA类游戏中，玩家死后可以重生，而游戏的目标则变成了摧毁敌人的防御塔和水晶。虽然目标不是杀人，但是杀人能够为你带来优势，可以更容易的摧毁敌人防御塔或者发育经济，因此在MOBA游戏中，杀戮和死亡代表着机遇和风险。<br>
<br>
所以在《战意》中，死亡和杀戮代表着什么呢？我们的胜利目标是夺得旗帜或者坚守阵地，防止进攻方夺得旗帜。这就和MOBA游戏比较相似了，不过《战意》还是有些不同的地方，并且我们在某些方面更为复杂。<br>
<br>
如之前所说，《战意》是15VS15的古战场战斗，在其中，我们定义了三种战斗元素：武将，兵团，和战马。这三种元素的死亡会带来非常不同的结果。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994841" aid="994841" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104227jjrp0j8wsc922y0c.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104227jjrp0j8wsc922y0c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104227jjrp0j8wsc922y0c.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">武将，兵团和战马</font></font></div><br>
我们首先来讲兵团。在2020年，有超过40亿的士兵在游戏中死亡。在游戏中，我们将一个排的士兵叫做兵团，他们一般由10-30个士兵构成，你可以选择很多个兵团作为替补，但是只能在战场上带领一队兵团进行作战。不同的兵团之间有克制关系，比如防御型兵团擅长防御弓箭手的攻击，但是容易被骑兵冲散阵型而消灭。这就给玩家更多的博弈和操作空间。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994842" aid="994842" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104229lbpzp8cplzgatrnt.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104229lbpzp8cplzgatrnt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104229lbpzp8cplzgatrnt.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《战意》的多种兵团</font></font></div><br>
在战斗中我们不希望看到玩家反复的进行无意义的拉锯战，所以我们局决定一旦在战场中阵亡的士兵便不能重返本场战斗。因此，玩家必须非常重视自己的兵团。他们需要考虑如何用更少的牺牲换取更大的杀敌数目。在有限的作战资源下，战斗时间得以控制，进而有效避免拉锯战的产生。在这部分中，玩家必须思考使用哪个兵团，什么时候冲锋，以及如何和队友配合以达到更好的效果。<br>
<br>
第二部分是战马。坐骑意味着速度，也意味着玩家的生存可能。有了战马，你可以快速逃离战斗，或者追赶敌军，亦或者帮助队友。战马的作用很强大，击杀敌人的战马能为你创造很大的优势，就像有句谚语这样说的：擒贼先擒王，射人先射马。此外，还有一些武将和兵团的技能是专门针对战马和骑兵的。战马在战斗中会被杀死，也可以回复血量，同时可以再补给点进行更换，这有些类似兵团，你也需要小心并且明智的使用它们。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994843" aid="994843" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104229fhdpzjzrhdhsryry.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104229fhdpzjzrhdhsryry.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104229fhdpzjzrhdhsryry.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">骑马快速逃离敌人包围</font></font></div><br>
最后是最重要的部分，也就是玩家自己——武将。武将的死亡会给战局带来巨大的变化，我们在设计的时候对他们的机制非常的谨慎。武将是战斗中玩家的化身，玩家通过控制武将进行战斗，并看到武将所看到的内容，当武将死亡时，兵团会变得群龙无首，战斗能力急剧下降并且很容易被消灭，进而带来一系列的连环损失。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994844" aid="994844" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104229sgnnyz4wgj9o8wfe.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104229sgnnyz4wgj9o8wfe.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104229sgnnyz4wgj9o8wfe.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《战意》武将</font></font></div><br>
那么问题来了：当武将死亡时，他会变得一无所有么？或者说我们想让武将在死亡时失去什么？这是个很艰难的话题，我们尝试了很多设计方案，和大家一起来看一下。<br>
<br>
一开始，我们试图让兵团在武将死后立即撤退，但这让游戏变得非常个人英雄主义，这不是我们在游戏中所期望的。兵团在游戏中不再是必要的，你所要做的就是集中精力杀死敌方武将，同时避免被杀。在这种情况下，古老的史诗级战场变成了刺客或弓箭手互相偷袭的战场。<br>
<br>
<div align="center">
<img id="aimg_994845" aid="994845" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104230j10irgtreqtzliy3.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104230j10irgtreqtzliy3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104230j10irgtreqtzliy3.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">武将死后兵团立即撤退（开发工程）</font></font></div><br>
因此我们做出了一些改变。兵团会在武将死亡后的一段时间自动撤退，但是在此期间，你可以命令你的兵团进行战斗，防守或者追随其他武将。这个版本明显要比最初的版本好很多，但是兵团常常会在武将死亡期间遭受巨大的损失，导致后期的战斗受到影响。同事玩家也不喜欢失去对自己兵团的控制权的感觉，他们想要更自由的撤退和进攻。<br>
<br>
<div align="center">
<img id="aimg_994846" aid="994846" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104231cofnd9n9znnnfjnn.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104231cofnd9n9znnnfjnn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104231cofnd9n9znnnfjnn.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">武将死后兵团仍可战斗（开发工程）</font></font></div><br>
因此在我们最新的版本中，我们给玩家更多的选择。首先还是有规定的强制撤退时间以平衡和控制游戏节奏，但是玩家可以在规定时间前选择撤退或者继续战斗。这种有限的选择一方面是为了游戏节奏考虑，另一方面也是希望玩家仍会在他们死亡的时候受到一定的惩罚和损失，否则武将的角色便会变得很没有存在感。<br>
<br>
时间是我们需要平衡的另外一件事。当武将死亡，他需要多长时间复活呢？我们都知道，武将复活的时间越长，敌人杀死武将获得的优势就越大。因此死亡时间是决定游戏节奏的重要因素。在游戏的早期阶段，玩家很容易复活，死亡的代价较低，玩家可以尝试和犯错，然而随着战斗的推进，玩家复活的时间就会越长，玩家死亡的成本就越高，杀敌更加的有利可图，但同时你也需要更加的小心不要被敌人杀死。<br>
<br>
<div align="center">
<img id="aimg_994847" aid="994847" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104231xzll0lsni9a0l09a.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104231xzll0lsni9a0l09a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104231xzll0lsni9a0l09a.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">玩家的死亡损失和死亡时间的模拟曲线</font></font></div><br>
最终的复活时间如图所示，我们决定将玩家的死亡次数作为影响玩家重生时间长度的唯一变量。换句话说，每死亡一次，都会延长下次的复活时间，这种压力使得局势更加的紧张和刺激。玩家必须非常谨慎，并且随着玩家的死亡，节奏也会发生巨大的变化。但是如果时间太长，玩家会在死亡的时候非常无聊，因此我们设定了时间上限，这是游戏机制和用户体验之间的权衡。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994848" aid="994848" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104231ryyicn0ti0ftbo65.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104231ryyicn0ti0ftbo65.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104231ryyicn0ti0ftbo65.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">复活时间和死亡次数关系</font></font></div><br>
另外我们还可以通过其他的方式控制玩家返回战场的时间，比如玩家复活的出生点设计，离核心战斗区域越远，玩家复活返回战场的时间就越长。<br>
<br>
在介绍完《战意》的几种不同战斗元素的死亡后，我们开始进入玩家的死后体验和优化，在这部分，我们主要关注武将，因为武将一方面更加重要，另一方面，武将作为玩家在游戏中的化身，他们有更强烈的感情。<br>
<br>
死亡是可怕的，死亡也会带来一系列的负面情绪。所以我们有针对性的做了一些设计去消除他们的负面情绪。<br>
<br>
就像我们在一些战争类的电影中所看到的，当角色的朋友去世时，首先他会否认和怀疑，之后他会很愤怒的想去报仇，杀死更多的敌人，然后在战斗后陷入悲伤和回忆。<br>
<br>
玩家在游戏中也会经历类似的心理过程，从最初的困惑和抵抗到接受现实后的挫败感，再到等待回到游戏中的无聊感。这些都是我们希望玩家能够尽快摆脱的消极情绪，这样他们才不会因这些情绪而退出游戏。那么，让我们逐一讨论。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994849" aid="994849" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104232us18665dt5r66tpq.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104232us18665dt5r66tpq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104232us18665dt5r66tpq.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">电影和游戏中的死亡情绪曲线</font></font></div><br>
玩家死后首先出现在脑海中的不是悲伤，而是困惑。玩家首先想到的是我是怎么死的？除非这一问题得到解决，否则我们无法继续。因此，我们需要一些游戏数据和细节展示。死亡信息一般有两种形式。一种是死亡回放，它让你从杀手的角度直观地理解自己是如何死亡的，但这并不适合我们的游戏。让我们做一个简单的计算。我们的游戏是15vs15的战斗。同时，每个英雄会带领3-5个单位(10-30个士兵)参与战斗，这意味着有成千上万的士兵和英雄可能会对玩家造成伤害或杀死玩家。仅仅通过摄像头很难看到死因。<br>
<br>
所以，我们使用图表和数据来展现。两件事需要考虑：我们要呈现什么信息以及如何呈现。因为上百种伤害源可能导致玩家最终死亡，所以我们必须忽略一些不重要的伤害源，以便玩家能够更容易地理解这些数据。否则，数字就只是数字，无法让玩家理解。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994850" aid="994850" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104234q12v1501aaan90ek.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104234q12v1501aaan90ek.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104234q12v1501aaan90ek.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">死亡信息弹窗</font></font></div><br>
最终，我们选择显示不同伤害类型的比例，前三种伤害来源和杀手这些数据。玩家可以很快知道是什么杀死了他们，谁对他们造成了最大的伤害。<br>
<br>
我们应该何时以及如何向玩家呈现这些内容？在屏幕上弹出这么大的弹窗并不是一个好主意，因为玩家可能讨厌在观看自己的士兵战斗时被打断。因此，我们采用了一个双层逻辑。玩家死后，仍然可以看到游戏画面，以及杀手的名字出现在屏幕左侧。如果玩家不知道自己是如何死亡的，他便会出于好奇而点击，进而弹出死亡信息弹窗。如果玩家不太关心具体数据，他仍然知道是谁杀了他。这就像是在向玩家耳语：“有人杀了你，你不愤怒吗？不想复仇么？”<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994851" aid="994851" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104235odo1okg11oo2zxsk.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104235odo1okg11oo2zxsk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104235odo1okg11oo2zxsk.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">玩家死后的击杀者信息</font></font></div><br>
在此之后，玩家可能会感到受挫。我们需要他们恢复士气，或者转移他们对死亡的沮丧。<br>
<br>
我们已经讨论过的第一种方法是在他们死后可以控制兵团。即使武将死了，你仍然可以进行反击，如果你能够通过控制自己的兵团成功地进行复仇反杀，能够获得巨大的快感。<br>
<br>
此外，玩家可以观战自己的队友。在《战意》这样的游戏中，团队成员之间的交流是至关重要的，这是了解队友战略和如何战斗的好方法。为了加快游戏的节奏，我们在战斗中随着时间的推移增加了杀戮收益和死亡成本。然而，死亡时间越长，玩家就越感到无聊。为了解决这个问题，一方面，他们可以通过观战来消磨时间。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994852" aid="994852" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104236cspns9pb6q9bsnzz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104236cspns9pb6q9bsnzz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104236cspns9pb6q9bsnzz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">死后观战队友</font></font></div><br>
另外我们还有鹰眼模式，可以让你从更高的角度思考。玩家也可以在死后考虑策略。因为随着游戏的发展，后援兵团越来越少，兵团之间存在克制关系，带合适的兵团比无脑战斗更重要。与此同时，弩或大炮等攻城武器如果使用得当也能扭转战局。决定你将在哪里重生以及你出生后的道路也是至关重要的。较长的重生时间也让杀死地方武将的玩家能够巩固自己的胜利或扭转局势对抗敌人。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_994853" aid="994853" zoomfile="https://di.gameres.com/attachment/forum/202107/23/104237kt2k2lw4z8w2j4yl.jpg" data-original="https://di.gameres.com/attachment/forum/202107/23/104237kt2k2lw4z8w2j4yl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/104237kt2k2lw4z8w2j4yl.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">鹰眼模式</font></font></div><br>
你可以想象，游戏中的这种死亡机制一定会带来一些意想不到的结果。我们在游戏中为玩家设计了一个补给点来替换他们的兵团或获得补给，但它通常离玩家想要战斗的目标很远，所以他们需要花时间去更换兵团。然而，有些玩家可能会利用我们的死亡机制，通过自杀重生来更快地替换自己的兵团。他们可以带着新兵团在更近的重生点回到战斗中，这样他们就不需要跑回补给点再跑回来。这不是我们设计时想到的玩家的操作，但看到玩家探索游戏的创造性方式确实很棒。<br>
<br>
最后，我想谈谈我们在死亡系统的设计过程中所学到的一些东西。<br>
<br>
首先，从死亡和死亡后体验的博弈入手，考虑相应的游戏玩法是对游戏设计非常有帮助的。死亡是游戏的终点，还是仅仅是一次休息？死亡在游戏中意味着什么？规则和死亡之间有什么关系？<br>
<br>
之后，我们应该分析死亡所带来的消极体验，并提供设计解决方案来缓解这些消极体验，如困惑，沮丧，无聊。<br>
<br>
最后，在完成这两件事之后，我们必须进行整合计划和设计，权衡利弊，确保死亡体验是全面的，并且和游戏风格是同步的。<br>
<br>
以上就是我这次分享的全部内容，这次分享的不仅仅是我自己的设计思考和结果，也是很多《战意》设计师共同的设计成果。在此也要特别感谢在其中为我提供极大帮助的制作人王希和不鸣科技的小伙伴们。<br>
<br>
</td></tr></tbody></table>



  
</div>
            