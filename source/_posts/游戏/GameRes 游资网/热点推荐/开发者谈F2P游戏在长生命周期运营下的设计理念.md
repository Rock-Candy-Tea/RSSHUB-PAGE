
---
title: '开发者谈F2P游戏在长生命周期运营下的设计理念'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202205/26/112017dqojxy2s2so99xch.jpg'
author: GameRes 游资网
comments: false
date: Thu, 26 May 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202205/26/112017dqojxy2s2so99xch.jpg'
---

<div>   
游戏平衡长久以来都是一款游戏能否成功长久运营下去的关键成分。<br>
<br>
游戏做的太简单吧，赚不了钱；游戏做得太复杂吧，很难留住玩家。<br>
<br>
从现在F2P成为了游戏主要的付费模式的形势来看，让游戏达到平衡状态以留住玩家并鼓励玩家消费就起到至关重要的作用了。<br>
<br>
这种非对称平衡模式主要由三个支柱组成：<br>
<br>
<strong>时间</strong><br>
<br>
<strong>资源短缺</strong><br>
<br>
<strong>session频率</strong><br>
<br>
这是我们iLogo公司用来平衡游戏采用的系统模式——自从我们基于该理论基础进行实践后，我们在用户留存率和KPI上看到了显著成效。<br>
<br>
<strong>平衡关系</strong><br>
<br>
这三个支柱都是以为达到目标而付出努力的那些玩家为基础的，我们将这些目标定义为——玩家为了取得进步而必须完成的一项操作或者是一系列操作。<br>
<br>
要想达到这些目标，玩家就要在游戏中花费资源、时间和金钱。<br>
<br>
第一个微目标可能是让玩家花更多的时间，其次是让玩家在游戏中进行更多操作，而第三个目标则需要玩家结合前两个目标。<br>
<br>
从某些角度上来讲，玩家对花钱比对被要求在游戏中进行操作更有所准备。<br>
<br>
尤其是在教程中，目标和时间需要保持一致<br>
<br>
<div align="center"><font size="2">
<img aid="1040876" zoomfile="https://di.gameres.com/attachment/forum/202205/26/112017dqojxy2s2so99xch.jpg" data-original="https://di.gameres.com/attachment/forum/202205/26/112017dqojxy2s2so99xch.jpg" width="471" id="aimg_1040876" inpost="1" src="https://di.gameres.com/attachment/forum/202205/26/112017dqojxy2s2so99xch.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">goals and time（from pocketgamer.biz）</font></div><br>
首先，这些目标最好在短时间内达成，这样玩家才能尽快熟悉游戏机制。在这个阶段，最好要在5到15分钟内达成这些目标。<br>
<br>
随着玩家被游戏吸引，这时目标达成时间可以增加，但是一天实现的目标不要少于一个，因为这里似乎是玩家容易变得沮丧然后弃游的临界点。<br>
<br>
我们发现最佳的目标达成时间是12小时，也就是每天2个目标。<br>
<br>
举例：《Hay Day（卡通农场）》中的“装船”<br>
<br>
货船每天仅抵达农场一次，过了一定时间后离开。每次它都会让玩家收集一定量的某类货物，但是其平衡的方式表明玩家是无法凭一己之力在给定的时间内完成货船所指定的量的。<br>
<br>
玩家农场以最高的收成效率也只能完成规定量的70%左右；另外的30%则需要玩家通过真实货币来弥补，或者是用外挂（？）。<br>
<br>
创造性地利用赤字（所缺少的资源）<br>
<br>
达成目标的第二个指标参数是赤字。<br>
<br>
<div align="center"><font size="2">
<img aid="1040877" zoomfile="https://di.gameres.com/attachment/forum/202205/26/112017a51yb1isg1brsras.jpg" data-original="https://di.gameres.com/attachment/forum/202205/26/112017a51yb1isg1brsras.jpg" width="471" id="aimg_1040877" inpost="1" src="https://di.gameres.com/attachment/forum/202205/26/112017a51yb1isg1brsras.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">balance（from pocketgamer.biz）</font></div><br>
正如你在下图表中所看到的，我们对产品对每个等级的产量下了定义，现在我们就可以形成一种赤字——玩家在达成下一个目标所缺少的资源量。<br>
<br>
通过这种方法，我们预先确定了操作量（以及其等价的现金数）然后把这个赤字放到目标中。<br>
<br>
F2P游戏要确保玩家实际掌握资源与所需资源之间存在差距<br>
<br>
例如：为了升级，我们不得不完成3个有关联的相似目标。第一个是在花园里收获17个苹果作物。不过这里有个问题——你的花园里只有5颗苹果树。因此，在一个session中，玩家只能收获5个苹果作物。<br>
<br>
在第三个session中，现在玩家已经完成了三个目标中的两个了，而为了完成第三个目标——就是收集苹果——玩家还缺少2个苹果（5X3=15）。升级的希望就在眼前了，但是这2个苹果让玩家没法完成升级。从这点上来看，很多玩家都会选择去买未完成的这2个作物，而不是去等第四次收获。<br>
<br>
这里怎么设置费用？<br>
<br>
问题来了，2个苹果作物值多少钱？<br>
<br>
让我们把目标时间设为X轴。由Newzoo进行的研究表明，美国玩家可以接受每天在游戏上花费10到20美元。<br>
<br>
因此，我们把这个数额分配到赤字上，会看到目标价格会随着达成这个目标的时间增长而增加。<br>
<br>
如果需要2个小时来种苹果，那么2个苹果作物的目标斥资就应该不超过2美元。<br>
<br>
玩家在实际拥有资源和所需资源之间的差距需要在IAPs成本方面有所延迟。<br>
<br>
如果每个新目标需要玩家投入更多的精力才能完成，最终他们都会放弃游戏的。<br>
<br>
为了保持游戏的新鲜感，你得通过改变消费曲线来进行游戏内容的混合，所以在某些时候它等于0，而在其他时候它有可能超过最高值。<br>
<br>
所以有时玩家会“赢过”游戏，有时却需要购买额外资源来继续游戏。<br>
<br>
良好的设计会让玩家不停游移在两条曲线之间<br>
<br>
当赤字上升到超过最高水平时，流失率越高，这种假设是有逻辑的。因此通过谨慎地管理赤字，我们将能够对流失率形成有利影响从而避免收益降低。<br>
<br>
你可能注意到了，赤字在前四个等级基本为零——这不是巧合！<br>
<br>
从新手教程到了解游戏再到投入游戏这整个流程会一直持续到玩家遇到游戏中的第一个困难为止。<br>
<br>
如果你想要让他们持续享受游戏一个礼拜再要求付款，并假设你用的是同样的时间框架，那么这时赤字会持续为零直到第10级。<br>
<br>
把它分解为多个sessions<br>
<br>
我们已经解决了所有关于目标时间和赤字的问题了。<br>
<br>
我们目标的第三个组成部分是玩家游戏操作的频率。<br>
<br>
我们可以假设要达成目标需要3个游戏sessions——就和“收集苹果”的例子类似。但是这次，为了达到一个新的层次水平，我不得重复3次完成这个目标。<br>
<br>
我每次达成目标时，可以多种五棵苹果树，由此我便减少了完成下一个所需的session数量。一旦我升到了我想要的等级，这时目标就改变了，而且难度也会基于赤字图表所示而增加。<br>
<br>
那么现在，玩家要求达成的目标从15个作物变成了45个——而且同样需要3个sessions（重复3次完成目标）……<br>
<br>
另外的例子——目标包含了两个无法在一开始的时候就通过单个session完成的动作。<br>
<br>
在游戏每个session中绘制出越来越多的目标<br>
<br>
在《Hay Day卡通农场》中，你需要种植小麦、收小麦、用小麦做鸡饲料喂鸡、然后机会下蛋，蛋又能用来做培根煎蛋。目标是制作10个培根煎蛋。<br>
<br>
通过管理操作的频率，我们预先确定了sessions的数量和它们的长度，设置了计时器、推送通知并调整游戏难度。<br>
<br>
最终的目标<br>
<br>
目标管理的第四个参数是每个等级所应设的目标数量。<br>
<br>
正如你在上文图表中所看到的，每上升一个等级就增加一个session。但是你可以按照你的喜好调整这个参数从而生成最高收益。<br>
<br>
作为一种选择，一个目标还可以基于多种资源设定。如果你的游戏使用了多种资源，你可以变换赤字——根据等级对赤字资源进行组合。<br>
<br>
把多种赤字资源进行组合从而管理目标设定。<br>
<br>
你还可以改变一个等级内达成目标所需某种资源的赤字、或者对一些目标循环使用、还有致力于提高游戏LTV指标而进行各种实验。<br>
<br>
希望这个解释（我已经尽量简化了）可以帮你建立有效的非对称平衡来保证你的游戏的指标具备竞争性，至少对iLogos来说，它行之非常有效。<br>
<br>
平衡多种资源的范例：<br>
<br>
为了升到新的一级，我得收获不止15个苹果，还有同样数量的草莓。苹果的手机很顺利，于是我开始投资草莓。当我进入下一个等级，收获了很多苹果和草莓以后，好的新的赤字目标出现了——土豆。<br>
<br>
为了升级，我不得不升级武器的伤害值来打败我的对手。这个伤害值对下一个等级来说也足够了，不过现在我需要先升级我的盔甲。等升了级以后，光升级武器和盔甲已经不够了——我将还得升级我的魔力。<br>
<br>
为了赢得比赛，我不得不去获得更高能的引擎，换制动器。<br>
<br>
概括地说来，你在平衡一款游戏时需要将哪些内容铭记于心？<br>
<br>
<div align="center"><font size="2">
<img aid="1040878" zoomfile="https://di.gameres.com/attachment/forum/202205/26/112018skkdef7ll8ejksld.jpg" data-original="https://di.gameres.com/attachment/forum/202205/26/112018skkdef7ll8ejksld.jpg" width="471" id="aimg_1040878" inpost="1" src="https://di.gameres.com/attachment/forum/202205/26/112018skkdef7ll8ejksld.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">sessions-per-goal（from pocketgamer.biz）</font></div><br>
定义衡量你的游戏进度的指标（比如说等级）。<br>
<br>
玩家需要达成什么目标（或者如何操作）来在你的游戏里取得进展？<br>
<br>
玩家达成每个游戏目标所需要花费的时间是多少？频率如何？<br>
<br>
每个目标的赤字（所短缺的资源）是什么？<br>
<br>
游戏中每升一级需要完成多少个目标？<br>
<br>
玩家每达成一个目标需要进行多少游戏的sessions？<br>
<br>
正如我们在正文引入中所提到的，iLogos就是用这个模式将游戏平衡化且达成了游戏的变现（盈利）。我们发现这个模式非常有效。<br>
<br>
虽然这些原则被解释得很有道理，但是当然了，这个模式还需要进一步的反复试验以及用户反馈来进行微调。<br>
<br>
<font size="2"></font><br>
<font size="2">来源：游戏邦</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/auzbbvKU7vqumDKecbbnGg</font><br>
<br>
<br>
  
</div>
            