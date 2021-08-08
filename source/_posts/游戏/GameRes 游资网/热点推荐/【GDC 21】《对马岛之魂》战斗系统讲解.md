
---
title: '【GDC 21】《对马岛之魂》战斗系统讲解'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/27/140930pcvtt9ha09t5tv2w.jpg'
author: GameRes 游资网
comments: false
date: Tue, 27 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/27/140930pcvtt9ha09t5tv2w.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2506787">
原文发表于4Gamer.net，GNN繁体中文编译，此处仅做简单的简中转换以及部分词语的更改。<br>
<br>
<hr class="l"><br>
在改为线上活动方式的世界最大规模游戏开发者相关活动「游戏开发者大会 2021（Game Developers Conference 2021）」中，举办了许多关於 AAA 级大作、独立开发作品以及经典游戏等等，以各种不同游戏作品当主题的讲座。<br>
<br>
<div align="center">
<img id="aimg_995784" aid="995784" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140930pcvtt9ha09t5tv2w.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140930pcvtt9ha09t5tv2w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140930pcvtt9ha09t5tv2w.jpg" referrerpolicy="no-referrer">
</div><br>
在其中很引人瞩目的活动，就是由 Sony Interactive Entertainment 公司在 2020 年 7 月 17 日推出的开放世界式时代剧动作冒险游戏《对马岛之魂（Ghost of Tsushima）》为主题的关联讲座。本作在由游戏开发者与媒体投票决定获奖游戏的「游戏开发者优选奖（Game Developers Choice Awards）」，也获得包含年度大奖在内的七个部门提名，并得到最佳视觉艺术与爱好者奖等两个奖项，在游戏业关系人士当中，也是很受到瞩目的一款作品，所以今年举办了许多以本作故事、视觉效果以及音乐等方面为主题的讲座。<br>
<br>
<div align="center">
<img id="aimg_995785" aid="995785" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140930a0c9pj0amiswd80p.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140930a0c9pj0amiswd80p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140930a0c9pj0amiswd80p.jpg" referrerpolicy="no-referrer">
</div><br>
而其中特别令人在意的讲座之一，就是在活动第三天（7 月 22 日）举行的「武士刀大师：《对马岛之魂》的肉搏战斗（Master of the Katana: Melee Combat in Ghost of Tsushima）」讲座，这是一场以游戏进行与战斗系统的关联为主题，针对游戏开发者的实例讲解。<br>
<br>
<div align="center">
<img id="aimg_995786" aid="995786" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140931omteqamdescqctet.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140931omteqamdescqctet.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140931omteqamdescqctet.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090">左边出现的人物是主讲者克里斯·齐默尔曼（Chris Zimmerman），</font></font></div><div align="center"><font size="2"><font color="#708090">开发工作室 Sucker Punch Productions 的 Studio head at Emeritus，在本作主要负责战斗系统</font></font></div><br>
<strong><font color="#de5650">在游戏中最有效的玩法，也应该要是最有趣的玩法</font></strong><br>
<br>
<div align="center">
<img id="aimg_995787" aid="995787" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140932twa421yw9aav0sz4.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140932twa421yw9aav0sz4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140932twa421yw9aav0sz4.jpg" referrerpolicy="no-referrer">
</div><br>
《对马岛之魂》是一款以蒙古军发动侵攻（西元 1274 年文永之役）这个历史事件作为主题的作品，成为游戏舞台的对马岛，根据记载在文永之役当中有超过八十名武士战死，以此作为蓝本的本作故事，是以少数幸存下来的「武士」之一，游戏主角境井仁下定决心要对蒙古军展开反击开始。<br>
<br>
但俗话说寡不敌众，就算想要从正面来一场堂堂正正的战斗，只靠一个人也不可能对抗强悍的蒙古军团。於是仁一点一点舍弃由伯父志村教导自己的「武士作战守则」，开始使用苦无手里剑、烟雾弹以及火绳枪等武士刀以外的暗器，或者是直接进行暗杀等手段，作为一位战鬼持续奋战。<br>
<br>
<div align="center">
<img id="aimg_995788" aid="995788" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140932f2tt69vtv5kit34z.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140932f2tt69vtv5kit34z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140932f2tt69vtv5kit34z.jpg" referrerpolicy="no-referrer">
</div><br>
团队在建构这个世界观和故事时有三大目标，<font color="#ff0000">第一个就是要「让玩家沉浸在游戏里面」</font>，他们的目标是要把玩家带到古早时代的日本，制造出让玩家能和当时世界融为一体的「时光机」。<br>
<br>
<font color="#ff0000">第二个则是「要是一款脚踏实地的游戏</font>」，不过比起说是要做一款完全依照正确史实的游戏，应该说更重视要制作出一款以确切存在之事实为基础，「富有真实感的游戏」才对。他们使用了一句叫作「没有怪物也没有魔法，只有泥与血与铁的游戏（No monsters and no magic, just mud, blood and steel.）」的标语，并以一贯之打造出极富真实感的游戏。<br>
<br>
<font color="#ff0000">至於第三个是「让玩家更容易接触游戏」</font>，这是一个希望能获得更多用户族群的目标，其中一部份也是考虑到游戏开发成本并不便宜，所以并不是要做一款口味很偏门的游戏，而是要做出一款能够让数百万大众都可以享受到乐趣的游戏。<br>
<br>
<div align="center">
<img id="aimg_995789" aid="995789" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140933z44iibf5dfb5wwb2.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140933z44iibf5dfb5wwb2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140933z44iibf5dfb5wwb2.jpg" referrerpolicy="no-referrer">
</div><br>
这三项目标和限制就成为设计游戏时的蓝图，而反应了这些目标被制作出来的游戏重要元素，就是这次讲座主题的<font color="#ff0000">近战肉搏（Melee Combat）</font>。<br>
<br>
本作身为一款「武士幻想」故事，战斗是以接近战斗，特别是使用武士刀作为中心。如果不让这个以刀剑为主的战斗，从外观到实际触感都足够优秀的话，就无法获得成功。而且接近战斗同时也要反应出，因为敌人无比强悍所以非得要使用「卑劣手段」，这个游戏主角境井仁在故事中设定的处境才行，在剧情叙事上也是很重要的元素。<br>
<br>
如果玩家不使用暗器或是暗杀，光靠正面对决来进行战斗的话，那故事就会显得自我矛盾。被大群敌人包围的拚死血战、与伙伴并肩作战、和强敌的一对一决斗…… 这些不仅仅是要有一款刀剑动作游戏的趣味性，在剧情叙事方面也必须要描写得足够通顺才行。<br>
<br>
<div align="center">
<img id="aimg_995790" aid="995790" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140934g4znif419f4i4crn.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140934g4znif419f4i4crn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140934g4znif419f4i4crn.jpg" referrerpolicy="no-referrer">
</div><br>
而他们认为作为游戏重点要素的接近战斗，其核心应该是「Discipline and Precision」，虽然直接翻译过来应该是「规则性和正确性」，但其中应该也包含了<font color="#ff0000">「静与动」</font>以及<font color="#ff0000">「紧张与缓和」</font>的意思存在才对。是指所有动作都有其明确的目的存在，必须要正确地加以控制。在危险的状况下要采取安静的行动来等待时机，在正确的那一瞬间发动爆发性的动作等要素。<br>
<br>
他们觉得必须要让玩家能够施展出这些要素，所以打造出能让玩家经过长时间练习、亲身经历并研究後，<font color="#ff0000">与境井仁一起「成长」的游戏历程。</font><br>
<br>
<div align="center">
<img id="aimg_995791" aid="995791" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140934xehgeptqqpzdyhhz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140934xehgeptqqpzdyhhz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140934xehgeptqqpzdyhhz.jpg" referrerpolicy="no-referrer">
</div><br>
与境井仁一起踏上旅程，在旅途中一起成长的感觉，想要更加深化这个要素，重点就在於能产生正确接近战斗的刀剑动作。但是在制作这个部份时却碰上一个问题，那就是「人类的反应速度比想像中还要慢」。<br>
<br>
在开发初期原本是打算要让游戏角色的反应时间更贴近真实人类，但这个做法十分失败。因为动作太慢，反而让人有一种不对劲的突兀感。因为这次失败的关系，让团队产生以时代剧的杀阵作为灵感来源，并且在游戏中重现出来的想法。一套设计完整的杀阵，并不是仅靠演员的反应，还包含因为原本就有决定好动作而可以「预测」的行动，如果想要在游戏中重现杀阵，就必须要考虑到这一点才行。<br>
<br>
<div align="center">
<img id="aimg_995792" aid="995792" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140937xmer6bbfomebgnlv.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140937xmer6bbfomebgnlv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140937xmer6bbfomebgnlv.jpg" referrerpolicy="no-referrer">
</div><br>
这时最大的目标同时也是妥协点，就是想要把游戏制作成一款单纯以技能为底的作品。之所以会设计这个目标，有一部份是因为想要做到「只要能完美地进行游戏，就可以在不受任何损伤的状况下前进」。不管是被多少敌人一起袭击，只要能够在适当的时机施展出适当的动作，就可以表现得像是时代剧主角一样，毫发无伤地击退敌人。<br>
<br>
但是想要重现出这种感觉，也一样碰上了其他问题。一开始是设计成只要能够用快速动作发动攻击，就可以中断敌人行动持续施展出连续斩击，但是这样子就太过有效，无法让玩家感受到有技巧性的乐趣。在因为想要描写出武士在战斗时迅速而又威力十足的动作，所以持续不断重覆这类修正的过程中，出现了就算被武士刀刺中也不会轻易被中断攻击的盾兵，以及本身耐久力就高的壮汉士兵，以及在砍中敌人的那一瞬间，到动作完成之前就会接着朝下一个敌人发动劈砍，这种在同时面对复数敌人时可运用的连续攻击。<br>
<br>
<div align="center">
<img id="aimg_995793" aid="995793" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140937h74x4llo4cece1xg.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140937h74x4llo4cece1xg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140937h74x4llo4cece1xg.jpg" referrerpolicy="no-referrer">
</div><br>
第一个能让人感觉到有做到一款「以技能为底的游戏」，是能够捉准时机反弹敌人攻击的「招架」。这并不是一个只要按下按钮就可以施展出动作的招式，所以并不会让玩家感觉单纯是使用游戏控制器在操作角色，而是会有一种自己实际挥刀招架起敌人攻击的感觉，是能够催生出这种沉浸感的成功范例。<br>
<br>
在本作的接近战斗中，玩家应该知道招架是个有点万能过头的动作。不过几乎所有的玩家，都会使用自己认为最有效果的方法来进行游戏，同时也代表<font color="#ff0000">「玩家感觉最有效果的方法，就是玩起游戏来最有趣的玩法」</font>。所以在让玩家能够获得乐趣这点上，招架应该也扮演了很重要的角色。<br>
<br>
<div align="center">
<img id="aimg_995794" aid="995794" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140938zzga27ia8lga0plj.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140938zzga27ia8lga0plj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140938zzga27ia8lga0plj.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">不要在玩家没做到时给予惩罚，要在做到後给予报酬</font></strong><br>
<br>
<div align="center">
<img id="aimg_995795" aid="995795" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140939xhs2gwz0xz6w8miy.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140939xhs2gwz0xz6w8miy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140939xhs2gwz0xz6w8miy.jpg" referrerpolicy="no-referrer">
</div><br>
在透过以实际游玩的方式来进行测试後，得知更多变的游玩风格，是让人感觉游戏更加有趣的关键。在统计资料後更是可以知道，除了以日本刀发动互相劈砍之外，有使用境井仁的技能、暗器以及暗杀（匿踪技能）等各种不同方法来游玩游戏的玩家，不仅是更能够深了享受游戏本身，战斗的结果也会变得更为出色。<br>
<br>
不过在这时也碰上另外一个要解决的问题，那就是大部份的游戏玩家，只要发现一种自己认为最有效果的战术之後，通常就会持续使用该战术，不再去尝试新的方法。对於这些玩家<font color="#ff0000">，就必须要想办法引导他们主动选择全新战术。</font><br>
<br>
<div align="center">
<img id="aimg_995796" aid="995796" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140940s2rrrm208crbrgdr.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140940s2rrrm208crbrgdr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140940s2rrrm208crbrgdr.jpg" referrerpolicy="no-referrer">
</div><br>
想要让玩家选择一种全新风格的玩法，大致上可以采用两种不同的方法。「阻止玩家使用他已经用过头的游戏玩法」，以及「突显全新风格的魅力，促进玩家主动选择这种玩法」。<br>
<br>
以前者来说，可以用像是推出原本玩法完全无法通用的敌人，或是反过来让全新玩法会对其特别有效的敌人登场。又或者是对用起来方便的招式与道具加上数量或是时间上的限制，还有让它们会因为时间经过以及使用次数而被弱化等等的方法。但是采用这种做法，就等於是从玩家身上夺走他们感觉最有效而且最有趣的玩法，同时还会让玩家明显感觉到「自己正在玩一款游戏」，因此有损玩家对世界观的沉浸感。如果有考虑到玩家的感受，那选择後者就是一件理所当然的事情。<br>
<br>
<div align="center">
<img id="aimg_995797" aid="995797" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140941borrqsyqo9zh2c0a.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140941borrqsyqo9zh2c0a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140941borrqsyqo9zh2c0a.jpg" referrerpolicy="no-referrer">
</div><br>
不是要去妨碍会被使用过头的玩法，而是促进玩家使用原本没有在用的玩法。就这点上开发团队第一个去思考的问题是，<font color="#ff0000">如何让玩家在作战时会去运用强攻击。</font><br>
<br>
在测试初期，完全不去使用动作比较迟钝的强攻击，只用动作较快的弱攻击施展出连续攻击的玩家，占了 90％ 以上的压倒性多数。但另一方面，却也可以知道在攻击时有使用包含强攻击在内各种不同招式的玩家，除了比较能够享受游戏乐趣以外，其实在作战时也更有效率。<br>
<br>
强攻击主要是用在打破敌人的防御上面，必须要让玩家更积极使用强攻击才行。但是只要施展一次强攻击就可以解除敌人防御，就显得太过机械化而没有趣味性，所以才设计成必须要施展多次强攻击一点一点削除敌人的防御能力，但光是这样吸引玩家使用强攻击的诱因并不是很强。<br>
<br>
<div align="center">
<img id="aimg_995798" aid="995798" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140942o764avyf725f1x7j.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140942o764avyf725f1x7j.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140942o764avyf725f1x7j.jpg" referrerpolicy="no-referrer">
</div><br>
到最後虽然团队也希望尽可能避免在游戏画面上显示过多情报，但还是为此妥协，准备了「震摄计量表」。也就是以视觉效果，来传达正在削弱对手防御的感觉给玩家。目的并非只是单纯要显示剩余量表，还加入在以激烈攻击命中对手时会闪烁的特效，是为了让玩家更容易感觉到自己施展的强攻击有击中对手。<br>
<br>
之後还提昇攻击力，在尽可能遵守要「脚踏实地」的前提下加快攻击速度，最後才成为现在的强攻击。<br>
<br>
<div align="center">
<img id="aimg_995799" aid="995799" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140943odirxhg9ipgzgggx.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140943odirxhg9ipgzgggx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140943odirxhg9ipgzgggx.jpg" referrerpolicy="no-referrer">
</div><br>
和强攻击一样，暗器在测试初期也很少有玩家会使用。如同前面提到的一样，为了让玩家体验到境井仁的故事，必须要施展出使用这些武器道具的战术。然而虽然方便的暗杀很多玩家用运用，但大部份的玩家主要都选用日本刀或弓箭，很少有人会选用暗器。<br>
<br>
虽然也有推出只能使用特定暗器才有办法打倒的敌人这种解决方法，但是这样就变成在限制玩家可使用的玩法。在暗器这方面也希望能和强攻击一样，打造成会促使玩家主动选择的选项。到最後想到的解决方法，就是「让道具使用起来更轻松方便」。<br>
<br>
首先是把苦无手里剑改良得更加好用，原本因为射程距离还不算短的关系，所以并不是很好瞄准，就被玩家认定是打不中的武器，因此没有人要用。为了改变玩家的认知，就追加了可以同时投出复数把的技能（暗刃），改良成一把能打中的武器。<br>
<br>
另外还修改成苦无手里剑、沥青炸弹和烟雾弹任选一种装备在身上的设计，一开始是想要使用不同按钮的组合键，让玩家在战斗中也可以马上切换使用，但这样就会让玩家「必须要思考的事情增加过头」，感觉会对玩家造成一种压力。所以在本作的战斗中，是认为尽可能把使用方式做得更单纯，才能够让玩家会想要配合其他动作一起使用。<br>
<br>
<div align="center">
<img id="aimg_995800" aid="995800" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140943tzbby1wgyobpgklw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140943tzbby1wgyobpgklw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140943tzbby1wgyobpgklw.jpg" referrerpolicy="no-referrer">
</div><br>
另外还提高苦无手里剑的掉落机率，这是因为能够取得的数量如果不够多，玩家就会很在意还剩下多少，为了保留下来在关键时间使用，就会降少使用的次数。为了避免这种现象发生，（虽然说还是带有一定的运气成份）就调整到已经拿满了都还有机会拿到更多的程度。<br>
<br>
想要让玩家使用不同风格战术或技术时，绝对不能勉强玩家去使用。不能为了达成这个目标，就采取阻碍玩家原本运用战术的方法。<br>
<br>
必须要让玩家能够理解这个全新风格战术能派上用场的理由，突显出其优势和魅力，并且如果有必要的话，还得准备使用了这种战术能获得的报酬。靠着这种设计方式，就能够解决「玩家不会主动选择新方法」的问题。<br>
<br>
<div align="center">
<img id="aimg_995801" aid="995801" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140945hghgkdnnvvlfv8ho.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140945hghgkdnnvvlfv8ho.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140945hghgkdnnvvlfv8ho.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">对玩家提出全新状况，让游戏产生变化</font></strong><br>
<br>
<div align="center">
<img id="aimg_995802" aid="995802" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140946cvnd8xld9z5ztnzp.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140946cvnd8xld9z5ztnzp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140946cvnd8xld9z5ztnzp.jpg" referrerpolicy="no-referrer">
</div><br>
想要让玩家持续游玩一款游戏，最重要的就是「游戏要对玩家提出全新的状况」。如果状况的复杂程度会随着游戏进展而增加，就可以提昇更多挑战性，让玩家在成功时可以获得更高的成就感。<br>
<br>
只不过如果追求复杂程度太过头的话，就有可能会让玩家感受到压力，反过来说如果太过单纯，又会让玩家马上找出固定攻略方式，令游戏因为简单过头而令人感觉到无趣。为了打造出一款富挑战性而又公平的游戏，开发团队认为重点就在加入玩家有办法克服的「适当程度复杂性」。<br>
<br>
<div align="center">
<img id="aimg_995803" aid="995803" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140947g3r8flfj5sfhlz5h.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140947g3r8flfj5sfhlz5h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140947g3r8flfj5sfhlz5h.jpg" referrerpolicy="no-referrer">
</div><br>
举例说明就像是敌人的弓兵，由於是要描写蒙古的军队，所以当然不可能不让弓兵登场。只不过要把弓兵加入本作成为战斗的一环，却有一些问题存在。<br>
<br>
境井仁采用的是以日本刀作为中心的接近战斗方式，在这个前提下，如果只是加入弓兵担任负责射箭的角色，玩家就可能会碰上在自己看不到的画面之外，不断有箭飞过来，会令人感到十分不悦。结果会让玩家一看到敌人，就马上先去暗杀所有弓兵，让战斗产生一种固定的模式不断重覆，最终令人感觉到很无趣。<br>
<br>
但话虽如此，如果设定成只要是在接近战斗下，画面外就一定不会有弓兵射箭，那反而变成对战斗没有任何影响的存在。有弓兵存在的接近战斗，必须要产生和没有弓兵存在的战斗完全不一样的刺激性才行。所以这两个选项，不管是选哪一个都无法创造出精彩的结果。<br>
<br>
<div align="center">
<img id="aimg_995804" aid="995804" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140948v5sschss5slas929.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140948v5sschss5slas929.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140948v5sschss5slas929.jpg" referrerpolicy="no-referrer">
</div><br>
於是开发团队找到的解决方案，就是在射箭时会发出声音来传送讯号。就算是从画面外发动的攻击，玩家只要在听到声音後施展回避动作，就可以闪过这发攻击，而且除了眼前的敌人动作之外，还必须要对声音也有反应，就变成一种带给玩家全新体验的方法。<br>
<br>
因为会听到敌人大喊「要射啦」，可能会让人感觉到有一些突兀，但在实际测试之後，大部份玩家都对於这种「出於游戏设计的虚构」给予友善的反应。<br>
<br>
游戏就像这样，透过制造出许多不同种类的敌人，改变他们可能会出现的组合，或是使用机动力会受到限制的场地，以及让玩家与友军并肩作战等等，为了让战斗不会令人感觉单调，所以准备了许许多多不同的状况与情境。<br>
<br>
而这同时也成为前面有提到的，促进玩家使用全新风格战术的方法。玩家当然可以不要选用游戏提供的不同风格战术，但是却没有办法闪过游戏准备的状况。如果在这种时候，有一种和自己原本惯用的战术不同，但是却十分有效的战术时，那自然就会有人下去尝试。像这样灵活设计出来的状况变化，就成为促进玩家自然变更使用战术的强悍武器。<br>
<br>
<div align="center">
<img id="aimg_995805" aid="995805" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140949d3mob3cwm9qkf530.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140949d3mob3cwm9qkf530.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140949d3mob3cwm9qkf530.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">为了让玩家与仁一起旅行的重点在於一开始的体验</font></strong><br>
<br>
<div align="center">
<img id="aimg_995806" aid="995806" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140950ep4wk2i4juwfkk14.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140950ep4wk2i4juwfkk14.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140950ep4wk2i4juwfkk14.jpg" referrerpolicy="no-referrer">
</div><br>
境井仁在本作当中，会因为经历过各种不同的事情与难关，慢慢开始「接受」身为战鬼的作战方式。而这个历程，同时也是玩家本身会经过的道路。这种让仁的旅途与玩家的旅途可以重叠在一起的设计，正是本作在考虑到游戏进展之後的重点部份。<br>
<br>
境井仁在持续推进本身故事的过程中，会取得各式各样不同的新道具和战术，同时也得面对需要使用这些元素来进行的战斗。虽然过去从来都没有使用过，就连基本用法可能都不是很了解，但要努力锻链，在反覆多次的战斗当中去习惯熟练。<br>
<br>
这点对玩家来说也是一样，在刚学到的时候会因为不熟悉操作法而必须要多加练习，但在反覆使用多次过後，就可以在战斗中自然施展出来。需要额外思考的事情会开始变少，能够把这个动作变成有如本能一样的反应，这一点与境井仁的 Progression（进步）也可以互相连结在一起。<br>
<br>
<div align="center">
<img id="aimg_995807" aid="995807" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140951bwaewvifa3piczwf.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140951bwaewvifa3piczwf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140951bwaewvifa3piczwf.jpg" referrerpolicy="no-referrer">
</div><br>
为了让玩家在游戏中有这种体验，就必须要具备前面说中的那些使用新道具的战斗风格，但是不管把这些风格做得多有魅力，依然会有许多并不会特别想要去挑战全新事物的玩家存在。该如何创造出让他们想去挑战的临门一脚是最重要的一点，而解答就在於让他们觉得一开始的体验十分精彩。<br>
<br>
当玩家遇见一个全新的道具或风格时，它必须要是一个可以简单使用，而且有明显效果，最终还得让玩家满足的产物才行。如果不是这样的话，那玩家就会回去使用自己原本用习惯的方法。<br>
<br>
<div align="center">
<img id="aimg_995808" aid="995808" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140953hujmj5mmjkmbtz5l.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140953hujmj5mmjkmbtz5l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140953hujmj5mmjkmbtz5l.jpg" referrerpolicy="no-referrer">
</div><br>
以具体实例来说明，在本作战斗当中有一个名为「架势」的重要元素。其实这是在开发过程中在另外追加的系统，一开始团队担心这可能会让已经开始有些复杂的游戏变得更加复杂，所以原本并没有打算要加入。这种顾虑实际上也没有错，刚加入时的确让玩家负担变得更重，在实施的测试过程中普及率比想像中还要低。不管是谁都不想要当一个笨拙的武士，所以会坚持自己已经习惯的作战风格，希望打得足够帅气。<br>
<br>
但是因为架槷这个构想本身的评价很好，所以团队没有因此放弃，而是选择在玩家第一次碰上架槷时表现出其优势所在，希望能够让架槷普及开来。在讲座中举出来说明的例子，是最早一个能获得的新架势「水之型」。这是一个和初期就能够使用的架槷「石之型」相比之下，能以加倍速度解除对手格挡，面对持盾敌人相当有利的架槷，为了让玩家能感受到其优势何在，所以在取得架槷後马上准备了一个和盾兵作战的场面作为「游戏教学」。<br>
<br>
苦无手里剑身为第一个取得的暗器，也是一样准备了一个能让玩家有良好首次体验的场面。透过推进主线故事能够取得铠甲，除了所有能力和初期铠甲相比都比较高之外，在外观上也看起来比较帅气。<br>
<br>
一开始的经验，会成为之後一切所有的基准。如果让玩家感觉不好的话，他就不会对该项功能产生兴趣。为了让玩家能够持续游玩一款游戏，第一印象是很重要的一点。<br>
<br>
<div align="center">
<img id="aimg_995809" aid="995809" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140954ipwggzuygbxscsud.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140954ipwggzuygbxscsud.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140954ipwggzuygbxscsud.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">首先该做的事情是找到你的「魔法」</font></strong><br>
<br>
<div align="center">
<img id="aimg_995810" aid="995810" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140956xsbyy9ye98ybt5et.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140956xsbyy9ye98ybt5et.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140956xsbyy9ye98ybt5et.jpg" referrerpolicy="no-referrer">
</div><br>
《对马岛之魂》从开始开发到完成，就像上面说述有极大幅度的进化，不过在开发过程中有一件十分重要的事情一以贯之，<font color="#ff0000">那就是尽可能不要在做到尽善尽美前，放弃自己一开始想到的点子。</font><br>
<br>
但是也有一个最糟糕的可能性，<font color="#ff0000">就是无法放弃根本就不可能做到好的点子。</font>想要避免碰上这种问题，就必须要制作出够多的游戏原型加以实测，从测试当中获得足以信赖的资料。本作在整整六年的开发期间当中，一直不断反覆构思并执行这此测试。由整体团队执行的内部测试约有三十五次，请外部人士执行的测试约有二十五次，在外部测试当中，有一半是以花上一星期让测试者自然而然游玩游戏的方式执行。<br>
<br>
<div align="center">
<img id="aimg_995811" aid="995811" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140957j5zzl0hqqely0taa.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140957j5zzl0hqqely0taa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140957j5zzl0hqqely0taa.jpg" referrerpolicy="no-referrer">
</div><br>
在这种过程中有一个名为「单挑」的点子被催生出来，喜欢时代剧或类似题材电影的人应该能够理解，这是日本大导黑泽明作品《椿三十郎》当中，可说是会名留电影史的一幕，在最後电影主角三十郎，与其宿敌室户半兵卫决斗的场面。<br>
<br>
即使是在还不确定应该要在游戏整体脉络当中什麽地方活用这个点子的阶段，团队也对於这个要素很有自信，认为可以充份表现出本作的紧张感以及静与动的对比，甚至都还只停留在原型时，就已经在 E3 2018 展览上公开展示。虽然从最终结果来看是有一点过度盲信，在让这个点子成为实际游戏系统发挥功能为止，需要许多在技术层面上的作业，但实际上也是成为本作一个很重要的部份。<br>
<br>
<div align="center">
<img id="aimg_995812" aid="995812" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140958buc8f1xl1rlllvzc.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140958buc8f1xl1rlllvzc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140958buc8f1xl1rlllvzc.jpg" referrerpolicy="no-referrer">
</div><br>
当你在尝试一项新事物的时候，首先应该要做的事情，就是找到其「魔法」所在。过去累积下来的经验，以及想要带给玩家什麽体验的想法，也可以帮助你更了解自己的点子。虽然并不能保证每一次都会很顺利，但的确能够让魔法成为更加确实的产物。<br>
<br>
<font color="#ff0000">「并不是游戏的一切事物都需要魔法，但如果没有一个像魔法一样的瞬间那就很难成功」，</font>主讲者克里斯?齐默尔曼在最後以这一句话，并且提出在开发《对马岛之魂》的过程中，学习到的「设计游戏时的五项规则」，为这次讲座划上句点。<br>
<br>
<div align="center">
<img id="aimg_995813" aid="995813" zoomfile="https://di.gameres.com/attachment/forum/202107/27/140959duka3yb3uf1ya2zz.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/140959duka3yb3uf1ya2zz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/140959duka3yb3uf1ya2zz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090"><br>
</font></font></div><div align="left"><font size="2"><font color="#708090">来源：GNN</font></font></div><div align="left"><font size="2"><font color="#708090">地址：<a href="https://gnn.gamer.com.tw/detail.php?sn=218547" target="_blank">https://gnn.gamer.com.tw/detail.php?sn=218547</a>【编译自<a href="https://www.4gamer.net/games/400/G040041/20210723010/" target="_blank">4Gamer.net</a>】</font></font></div><br>
</td></tr></tbody></table>



  
</div>
            