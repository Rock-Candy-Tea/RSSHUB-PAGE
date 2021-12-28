
---
title: '《Rogue Land》关卡与战斗设计分析'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202112/20/105748rkrhih6uiztmku6g.jpg'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://di.gameres.com/attachment/forum/202112/20/105748rkrhih6uiztmku6g.jpg'
---

<div>   
笔者最近浏览了Google Play发布的年度游戏榜单，在“最佳竞技游戏”名单中除了《宝可梦大集结》、《英雄联盟：激斗峡谷》、《漫威：未来之战》此类MOBA游戏外，还有一款名叫《Rogue land》的游戏引起了笔者的注意。在好奇心驱使下笔者试玩了几天，下面分享一下在关卡与战斗设计方面的游戏体验心得。<br>
<br>
<strong><font color="#de5650">一、什么是《Rogue Land》?</font></strong><br>
<br>
《Rogue Land》是一款具有“Roguelike”游戏元素的3D射击闯关游戏。游戏背景设定是世界被邪恶力量笼罩出现各种奇形怪状的怪物，一群英雄为了拯救世界拿起各种武器同时驾驭元素的力量向邪恶力量的源头发起了挑战。<br>
<br>
游戏核心玩法是“角色强化+闯关”，前者是局外养成的设计，后者主要围绕关卡内的玩法设计，在轻量的游戏内容下，“Roguelike”的随机性特点以及关卡与战斗设计的可玩性是玩家游戏体验的决定性因素。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1025253" aid="1025253" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105748rkrhih6uiztmku6g.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105748rkrhih6uiztmku6g.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105748rkrhih6uiztmku6g.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">(游戏整体框架）</font></font></div><br>
<strong><font color="#de5650">二、关卡设计</font></strong><br>
<br>
以关卡1为例，关卡基本结构示意图如下：<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1025254" aid="1025254" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105748j99pkv44pgzmtspz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105748j99pkv44pgzmtspz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105748j99pkv44pgzmtspz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">(游戏关卡结构示意图）</font></font></div><br>
可以看出，抛开头尾，《Rogue Land》游戏单个大关卡基本由数个过渡路段+小关卡组成。<br>
<br>
<ul><li><strong>过渡路段：</strong>游戏关卡中的缓冲区，通常存在于关卡开始以及小关卡之间，无位置标识。不存在或存在少量普通怪物，可随时拾取少量的水晶、血包、金币、宝石资源。</li><li><strong>小关卡：</strong>随机出现较多怪物或出现boss怪物。进入前会有明显的提示性标识。在消失小关卡内全部怪物前，不能退出该小关卡游戏区域且不可拾取任何掉落资源。<br>
</li></ul><br>
<div align="center">
<img id="aimg_1025255" aid="1025255" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105749k2c6b24wb4cwkbp2.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105749k2c6b24wb4cwkbp2.jpg" width="281" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105749k2c6b24wb4cwkbp2.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">(小关卡进去前的标识以及进去后的警示标识)</font></font></div><br>
<strong>两个细节：</strong><br>
<br>
<ul type="1" class="litype_1"><li>过渡期间资源获取的自由度高但少量。</li><li>小关卡内的高限制，挑战成功获得高收益。<br>
</li></ul><br>
另外先来看看关卡中怪物的基本属性设计以及ai逻辑：<br>
<div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1025256" aid="1025256" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105749ifnf94yya4ckchi4.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105749ifnf94yya4ckchi4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105749ifnf94yya4ckchi4.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（关卡部分怪物AI基本能力和基本属性）</font></font></div><br>
怪物是玩家在《Rogue land》关卡中的主要挑战，那么作为一款闯关类游戏，《Rogue land》中的怪物同样具有不错的多样性，合理的怪物设计可以给玩家带来适当的障碍。<br>
<br>
在过渡路段和小关卡的怪物AI逻辑有所不同，具体ai逻辑图如下：<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1025257" aid="1025257" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105750hvvvbdm6vv6zenza.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105750hvvvbdm6vv6zenza.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105750hvvvbdm6vv6zenza.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">(过渡段怪物ai逻辑图)</font></font></div><br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1025258" aid="1025258" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105750i4jiv3jfrf392a4f.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105750i4jiv3jfrf392a4f.jpg" width="471" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105750i4jiv3jfrf392a4f.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">(小关卡怪物ai逻辑图)</font></font></div><br>
两个不同的ai逻辑造成的结果是玩家在过渡路段时，可以根据个人选择适当规避怪物，而在小关卡则无法回避（成功或die）。<br>
<br>
综上，过渡路段和小关卡二者的差异化设计反映出了游戏节奏的变化。<br>
<br>
在《Rogue land》的关卡设计中，玩家的关卡体验呈单线体验，小关卡无法被避免。<br>
<br>
在过渡路段，玩家基本无死亡威胁，可以拾取资源回复状态以及选择性战斗，从而保证角色状态准备下一个小关卡的挑战，此时的游戏节奏是轻缓的，玩家情绪比较放松。是设计者给玩家调整游戏状态的空间，一般而言，单个过渡路段长度较短。<br>
<br>
于此相对的是小关卡的设计，玩家在关卡中面对的挑战主要集中在小关卡。玩家面对大量怪物的围堵以及强力boss的挑战，甚至无法通过击杀怪物拾取掉落资源来达到续航的目的。此时玩家面临较大的游戏挑战，由于“Roguelike”游戏的特点（死亡后必须重新开始的失败惩罚），玩家此时情绪存在紧张状态，游戏节奏快。<br>
<br>
<div align="center">
<img id="aimg_1025259" aid="1025259" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105751kw44dsw4h5ha5db4.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105751kw44dsw4h5ha5db4.jpg" width="406" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105751kw44dsw4h5ha5db4.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（小关卡中boss给予玩家的挑战）</font></font></div><br>
于是关卡内形成了游戏节奏的变化。<br>
<br>
<div align="center">
<img id="aimg_1025260" aid="1025260" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105751vqorhqro31eq24rz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105751vqorhqro31eq24rz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105751vqorhqro31eq24rz.jpg" referrerpolicy="no-referrer">
</div><br>
游戏节奏的快慢变化避免了玩家一直处于快节奏的闯关节奏导致出现倦怠心理，此外对于小关卡的限制性设计（不成功即死，成功获得高收益回报）也使得玩家进入和退出“心流”状态更加顺畅。<br>
<br>
当然，随着关卡的不同，关卡内部结构必然会有所不同，甚至会出现纯粹以数个小关卡组成一个完整的关卡，一般而言，此种极端情况会出现在两种情况，一是某个高难度关卡（游戏阶段节点）为了迫使玩家进行局外养成提升能力数值。二是活动性关卡，为了玩家在短时间内获得流畅的游戏体验。<br>
<br>
<strong><font color="#de5650">三、战斗机制</font></strong><br>
<br>
<strong>交互</strong><br>
<br>
有别于《比特小队》、《元气骑士》等Roguelike地牢闯关游戏采用横板游戏的方式，《Rogue Land》采用竖版游戏，在关卡战斗中，仅提供一个控制角色移动按钮。玩家可以控制角色走位从而躲避怪物攻击以及寻找有利射击角度。<br>
<br>
<div align="center">
<img id="aimg_1025261" aid="1025261" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105751c2tv6oente32e9tn.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105751c2tv6oente32e9tn.jpg" width="407" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105751c2tv6oente32e9tn.jpg" referrerpolicy="no-referrer">
</div><br>
从游戏交互的角度来看，横板游戏基本有多个按钮，更适合双手操作，要求玩家进行更多的操作，因此竞技性较强；反观竖版游戏一般以简单交互为主，对于玩家操作不高，更偏于休闲。玩家在《Rogue Land》中面临的操作挑战是通过预判怪物攻击范围躲避攻击，角色攻击模式是自动攻击。<br>
<br>
一个细节：<br>
<br>
因为游戏设计的是角色自动瞄准射程范围内的怪物进行攻击，同时角色的攻击动作是有前摇的（瞄准-攻击），所以在游戏中，是无法做到“走A”的操作（近战武器攻击只是由于攻速快导致前摇极短）。<br>
<br>
这一个细节使得玩家在移动躲避攻击的同时需要找到自己攻击的时机，对于玩家是否了解怪物攻击特点及节奏以及角色攻击节奏有一定的要求，体现了战斗机制的策略性。<br>
<br>
再来看一看玩家伤害公式：<br>
<br>
<ul><li>伤害=（武器伤害+装备伤害）*（1技能增幅伤害BUFF）</li><li>暴击率=武器暴击率+装备暴击率+（1技能暴击率BUFF）<br>
</li></ul><br>
《Rogue Land》中的基础战斗公式只有一条，游戏中没有区别物理/魔法伤害，同时怪物的承伤没有设定相应减伤公式，在难度提升方面，选择的是同种怪物提升数值的办法，这样的简单化设计给予玩家直接的局外养成的反馈，扩大了玩家在攻击怪物获得的数值正反馈。<br>
<br>
那么《RogueLand》在战斗机制的可玩性在哪呢？<br>
<br>
笔者认为主要体现在随机性。<br>
<br>
随机性有两个方面，一是关卡中玩家角色技能的随机性，二是关卡障碍的随机性。<br>
<br>
<strong>角色技能的随机性</strong><br>
<br>
进入关卡前，玩家可以自由选择使用的角色、武器和装备，这三者都具有自身的技能。<br>
<br>
<div align="center">
<img id="aimg_1025262" aid="1025262" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105751nrzlv6jdhr3fj6bc.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105751nrzlv6jdhr3fj6bc.jpg" width="399" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105751nrzlv6jdhr3fj6bc.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1025264" aid="1025264" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105752smq6f4njtmjlbiqf.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105752smq6f4njtmjlbiqf.jpg" width="408" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105752smq6f4njtmjlbiqf.jpg" referrerpolicy="no-referrer">
</div><br>
在关卡中，玩家技能池由角色技能+武器技能+装备技能三者组成。<br>
<br>
<div align="center">
<img id="aimg_1025265" aid="1025265" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105752zz08n8vxknzrzc2u.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105752zz08n8vxknzrzc2u.jpg" width="406" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105752zz08n8vxknzrzc2u.jpg" referrerpolicy="no-referrer">
</div><br>
关卡开始时，会从技能池中随机抽取三个技能供玩家选择一个携带。<br>
<br>
<div align="center">
<img id="aimg_1025266" aid="1025266" zoomfile="https://di.gameres.com/attachment/forum/202112/20/105752a0nu7aavja29nhw0.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/105752a0nu7aavja29nhw0.jpg" width="409" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/105752a0nu7aavja29nhw0.jpg" referrerpolicy="no-referrer">
</div><br>
玩家通过击杀关卡怪物后，拾取怪物死亡后所产生的经验资源－水晶，收集水晶达到一定数值可以获得提升。每一次提升同样会从技能池进行随机抽取后三选一，如此循环。每一个关卡中携带技能的上限是八个。<br>
<br>
这样的规则下，玩家根据自身闯关需要，搭配随机技能可以产生许多不一样的攻击效果，拥有大量的可能性（弓箭变成加特林、魔杖变电网等），增加了战斗的可玩性，丰富了闯关的游戏体验。<br>
<br>
<strong>关卡障碍的随机性</strong><br>
<br>
在《RogueLand》关卡中，玩家主要面临的障碍就是怪物（在中后期关卡会出现一些关于陷阱的设计）。<br>
<br>
游戏中每一个关卡的结构是固定的，不固定的是其中出现的怪物。玩家面对同一个关卡重复闯关时，里面的怪物会出现随机刷新，如怪物数量以及怪物种类。<br>
<br>
值得注意的是，怪物的随机刷新存在两个限制，一是同个关卡中刷新的怪物数值水平会相对稳定，二是普通怪物和boss怪物的独立刷新，即小关卡出现怪物类型（普通和精英怪/boss怪）是固定的。这两点限制避免出现怪物数值波动过大或怪物类型过于随机，保证了单个关卡的难度曲线相对稳定。使得玩家在闯关体验中既能因为随机性体验到重复刷关的乐趣，又不会出现因为运气差（随机性太强）造成被动性刷关导致游戏体验变差。<br>
<br>
<strong>改进点</strong><br>
<br>
1.由于游戏场景设计是3d实景地图，相比2d像素风的Roguelike游戏，3d的游戏场景会更加吸引玩家的注意力。因过多的重复场景（过渡路段）容易导致玩家视觉疲劳。<br>
<br>
2.随机性问题，在笔者看来，单个关卡固定的关卡结构设计稍显普通和死板，容易让玩家轻易对于后续障碍拥有预判，导致难度降低，使得玩家断去“心流”。后续关卡可以设计为关卡结构在一定规则内（过渡数和小关卡数）进行随机变化。<br>
<br>
综上，《RogueLand》还是一款可玩性较高的射击闯关类手游，适合大家闲暇打发时间玩。（吐槽一句，什么时候开发云存档功能！）<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：阿阳的游戏自习室</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/cFHYK6dwD55sH9yzDpeODw</font></font><br>
<br>
  
</div>
            