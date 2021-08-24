
---
title: '14倍CPI差距？相同游戏创意不同数据表现背后的产品细节差异'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/20/114746mlflluoluov5zube.png'
author: GameRes 游资网
comments: false
date: Fri, 20 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/20/114746mlflluoluov5zube.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2511049">
8月16日，Voodoo在B站（搜索Channel_Voodoo）进行了新一期中文直播。本期直播为《Voodoo开发者加速器第一期——超休闲游戏里的控制、镜头、关卡设计和美术》，希望可以帮助开发者更好的了解超休闲游戏市场趋势及开发技巧。<br>
<br>
Voodoo这次也开放了超休闲美术资源，包括UI、个性化人物定制组件、卡通Shaders、粒子效果、Unity免费资源推荐、超休闲原型监测报告，北美社交趋势市场报告，往期所有中文直播录像（含本次加速器回放），获取方式详见文末。<br>
<br>
另外，提醒大家，下周一（8月23日）下午5点，Voodoo会带来第二期加速器的直播，欢迎大家通过文末的二维码预约。<br>
<br>
<font color="#de5650"><strong>以下为直播内容整理</strong></font><br>
<br>
5月初，Voodoo曾给国内开发者分享了一个“Rich Run”的创意主题，当时有20余款原型参与了测试，但测试结果不尽人意。如果大家近期关注美榜的话，可以发现一款Voodoo的游戏《Run Rich 3D》，是基于相同的概念开发出的游戏原型，目前已成功登顶过美榜，并维持在前10的位置。<br>
<br>
<div align="center">
<img id="aimg_1002266" aid="1002266" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114746mlflluoluov5zube.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114746mlflluoluov5zube.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114746mlflluoluov5zube.png" referrerpolicy="no-referrer">
</div><br>
通过这次的对比我们发现，即使在相同的概念和创意下，游戏的执行、美术等细节可能是决定游戏成败的关键，这就是推出本次开发者加速器的原因。开发加速器从8月16日开始共3期，将循序渐进地讲解超休闲游戏的开发技巧和思路。<br>
<br>
<div align="center">
<img id="aimg_1002267" aid="1002267" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114747scu8yiqyc98ezcq2.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114747scu8yiqyc98ezcq2.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114747scu8yiqyc98ezcq2.png" referrerpolicy="no-referrer">
</div><br>
请注意，这次开发加速器的内容绝大部分是之前直播内容的梳理和归纳，所以会有重复的地方，但本期分享和以往直播有一个不同——为了帮大家深入理解一些概念，我们用到了一些被砍掉的原型予以说明，在此也特别感谢提供案例并授权我们分享的开发者们。<br>
<br>
<strong><font color="#de5650">一、 超休闲游戏的控制：单一输入，多重输出</font></strong><br>
<br>
下图是总结了Voodoo在2020年发行的部分游戏的控制方式，可以看到登顶过榜首的产品，都采用了单一输入的控制方式。为什么推荐开发者使用单一输入的控制呢？<br>
<div align="center">
<img id="aimg_1002268" aid="1002268" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114747bqu3gxggup3409pt.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114747bqu3gxggup3409pt.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114747bqu3gxggup3409pt.png" referrerpolicy="no-referrer">
</div><br>
首先，单一输入是简单的、符合直觉的。对用户而言，不需要教育门槛就可以玩游戏。此外，非游戏玩家也可以快速掌握游戏玩法，因为超休闲用户可能不是传统意义上的游戏玩家，通过采取单一输入是可以提高原型开发成功概率。<br>
<br>
<div align="center">
<img id="aimg_1002269" aid="1002269" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114748ga5yywy4nhcp3yxn.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114748ga5yywy4nhcp3yxn.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114748ga5yywy4nhcp3yxn.png" referrerpolicy="no-referrer">
</div><br>
可能有人会说Voodoo也发行过多重控制的游戏。下面以《Crazy Kick》和《Push’m All》为例说明一下，这两款游戏都采取了双重操作的方式。但大家如果仔细观察，会很容易发现，这两种控制方式中，都会分为主要控制和次要控制。<br>
<br>
在图中两款游戏里，主要控制都是摇杆控制，并且只使用摇杆控制就可以完成游戏，意味着玩家可以在不了解、不知道、不使用次要控制的条件下就能完成游戏，即次要控制其实是非必要的，只是用来锦上添花的，就像《Crazy Kick》和《Psuh’em All》的滑动和松手的操作。<br>
<br>
<div align="center">
<img id="aimg_1002270" aid="1002270" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114748j3kz38z83k3319i9.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114748j3kz38z83k3319i9.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114748j3kz38z83k3319i9.png" referrerpolicy="no-referrer">
</div><br>
在单一控制方面，Voodoo推荐以下4种被验证过的控制：左右连续滑动、按时机点击、按住释放、遥杆。<br>
<br>
<div align="center">
<img id="aimg_1002271" aid="1002271" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114749nfxix4r40i5pz6h0.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114749nfxix4r40i5pz6h0.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114749nfxix4r40i5pz6h0.png" referrerpolicy="no-referrer">
</div><br>
那么只有一种控制方式会不会让游戏非常单调？其实不会。<br>
<br>
我们推荐大家使用单一控制的同时，是可以输出多种结果的。下图两个大热的游戏《Aquapark.io》和《High Heels》仅需左右滑动这种单一的输入，便可游戏中实现移动、跳跃、击败对手、保持平衡、滑行等多种输出结果。<br>
<br>
<div align="center">
<img id="aimg_1002272" aid="1002272" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114750t5eumbeezis58whb.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114750t5eumbeezis58whb.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114750t5eumbeezis58whb.png" referrerpolicy="no-referrer">
</div><br>
另外，在单一控制中，我们建议要奖励用户的每一次输入、操控。这意味着每次操控，屏幕上都会发生什么，用户能看到反馈。并且这种反馈是符合用户预期的。并且无论操作的结果如何，都应该给用户奖励的感觉，而不是被惩罚，这意味着游戏要有足够的宽容度。同时，因为用户要不停的操作，可以引起心流状态，让用户渴望下一步操作，可以带来连锁反应，带来“意外胜利”。如果用户能够提前规划好操作，可以超水平发挥。此外，我们建议开发者为控制加上震动和音效，帮助游戏达成奖励用户操作的目标。<br>
<br>
<div align="center">
<img id="aimg_1002273" aid="1002273" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114750qqv8m3yz9ffyp6q9.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114750qqv8m3yz9ffyp6q9.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114750qqv8m3yz9ffyp6q9.png" referrerpolicy="no-referrer">
</div><br>
下面列举三个被砍掉的原型加以说明。下图中三款游戏共同的问题是：每次操作后的反馈不及时，用户看不清或看不懂操作后能带来哪样变化，甚至看不清如何操作。这可能就不符合奖励用户每一次操作的原则。<br>
<br>
<div align="center">
<img id="aimg_1002274" aid="1002274" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114751cphq8k1h2hpp8l2j.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114751cphq8k1h2hpp8l2j.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114751cphq8k1h2hpp8l2j.png" referrerpolicy="no-referrer">
</div><br>
我们推荐开发者在控制方面选择持续、频繁的输入和操作，用户每2-3秒就需要一次操作，目的是让用户的手指和屏幕产生粘性。反例就是一次操作后，需要等几秒之后再操作，这就是间歇性操作，这是不推荐的。<br>
<br>
同时，我们推荐设计操作的时候加入防呆设计，用户凭直觉通过手指滑动达到预期的目的，甚至用户不了解游戏的控制，同样可以达到同样的效果，几乎不可能错误操作。此外，在操作上要足够的精确和灵敏，不要出现操作延迟。<br>
<br>
<div align="center">
<img id="aimg_1002275" aid="1002275" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114752d4q7h7cbz7hc4kfz.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114752d4q7h7cbz7hc4kfz.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114752d4q7h7cbz7hc4kfz.png" referrerpolicy="no-referrer">
</div><br>
下图左边是《Spiral Roll》，游戏中点击屏幕铲子会下降，松手则升起，在游戏过程中大部分时间用户的手和屏幕是“粘”在一起的。右边是《Knock'em All》，游戏是点击屏幕射击敌人的操作，但因为有些用户会认为自己仅需选择射击时机，不需要控制方向，所以OHM加入了防呆设计，只点击枪械，也可以自动瞄准射击。<br>
<br>
<div align="center">
<img id="aimg_1002276" aid="1002276" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114753rz1t303eaj87tj6t.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114753rz1t303eaj87tj6t.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114753rz1t303eaj87tj6t.png" referrerpolicy="no-referrer">
</div><br>
超休闲游戏的镜头<br>
<br>
我们优先推荐开发者使用被验证过的镜头角度和观测点。例如初始镜头，包括横向角度和纵向角度以及远近。纵向镜头影响用户能否看清前方的收集品和障碍物，远近则决定了游戏主角是否够大、清楚。这些元素结合一起决定了初始镜头。<br>
<br>
除了初始镜头，还有镜头的变化，例如随着堆叠适当的拉远拉近。<br>
<br>
<div align="center">
<img id="aimg_1002277" aid="1002277" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114754dqjtjxyx1tyygj0s.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114754dqjtjxyx1tyygj0s.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114754dqjtjxyx1tyygj0s.png" referrerpolicy="no-referrer">
</div><br>
举个例子，下图左侧《Cube Suffer》中，随着堆叠高度的变化，镜头的远近是在逐步变化的。右侧《Shortcut Run》会随着堆叠的增加和消耗，镜头会缓慢的拉远和拉近。但所有镜头变化都保持在稳定的范围内，游戏主角总是保持在屏幕中央的，可以清楚的看到游戏主角。<br>
<br>
<div align="center">
<img id="aimg_1002278" aid="1002278" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114755j12j0drpoz1zxg9r.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114755j12j0drpoz1zxg9r.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114755j12j0drpoz1zxg9r.png" referrerpolicy="no-referrer">
</div><br>
下面再分享两个常出现的错误。左边的产品镜头是随着锯子的摆动，上下左右不断移动的。这种移动会让用户看不清游戏的主角，建议开发者使用稳定的镜头，不要跟随主角晃动。右边的产品中，在主角左右移动的时候，镜头会剧烈的晃动，虽然主角保持在镜头中央，但会让用户产生晕眩的感觉，也是建议大家应该在原型开发中尽量避免的。<br>
<br>
<div align="center">
<img id="aimg_1002279" aid="1002279" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114756gnnpz5bnflt2txlj.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114756gnnpz5bnflt2txlj.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114756gnnpz5bnflt2txlj.png" referrerpolicy="no-referrer">
</div><br>
还有两个案例，左侧的人物在收集气球，在收集的过程中会剧烈晃动，这会导致CPI偏高。右侧案例也是在晃动的时候，甚至让用户的眼睛跟不上。<br>
<br>
<div align="center">
<img id="aimg_1002280" aid="1002280" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114800og8vzvunlhvrmgvz.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114800og8vzvunlhvrmgvz.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114800og8vzvunlhvrmgvz.png" referrerpolicy="no-referrer">
</div><br>
<font color="#de5650"><strong>二、 超休闲游戏关卡设计：速度、难度、节奏、循环</strong></font><br>
<br>
在关卡设计部分，先以跑酷为例讲一下前进速度。Unity3D里Z轴的速度表示前进的速度，我们建议保持足够快的速度，大家可以参考《Cube Suffer》和《Run Rich》的速度。<br>
<br>
<div align="center">
<img id="aimg_1002281" aid="1002281" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114801oup7pn5or8w3rpo5.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114801oup7pn5or8w3rpo5.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114801oup7pn5or8w3rpo5.png" referrerpolicy="no-referrer">
</div><br>
第二点是关卡摆放。以左右滑动的控制为例，摆放包括收集品、障碍物、以及摆放间隔。在收集品部分，在X轴——和用户左右滑动一致的轴上，需要有收集品的摆放，这种摆放可以让用户看清游戏的动作逻辑是左右滑动。同时在前进方向Z轴上有收集品的摆放，一个小技巧是蛇形摆放，既可以让用户看到操作，又可以看到收集的机制。<br>
<br>
收集品之外是障碍物的摆放，我们建议开发者遵循和收集品相似的逻辑，但也要做出风险与收获的深度，在大的奖励面前摆放一些障碍物。<br>
<br>
<div align="center">
<img id="aimg_1002282" aid="1002282" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114803aq74ud4p0kqw7dvg.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114803aq74ud4p0kqw7dvg.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114803aq74ud4p0kqw7dvg.png" referrerpolicy="no-referrer">
</div><br>
下面讲一下难度平衡，这里量化了一下。首先我们认为在超休闲游戏的第一关和第二关不可能让用户失败，意味着足够简单，能让用户知道游戏的逻辑，不要有任何挫败感。在之后的关卡中，我们建议关卡流失率低于5%，胜率要保持在90%-95%。关卡流失和胜率都可以通过GA的关卡流失工具测试。<br>
<br>
我们认为最优的难度选择，应该少一点挫败感，多一些宽容度。少一些危险，少一些惩罚，多一些乐趣。因为超休闲用户是来找乐子的，不是来找挑战的。如何调整难度呢？以跑酷游戏为例，关卡摆放、镜头角度、物理效果都可以帮助调整关卡难度。<br>
<br>
<div align="center">
<img id="aimg_1002283" aid="1002283" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114803rgekzzh3vsghs7oo.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114803rgekzzh3vsghs7oo.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114803rgekzzh3vsghs7oo.png" referrerpolicy="no-referrer">
</div><br>
难度平衡是超休闲游戏中非常关键的要素，下面是《Flappy Dunk》和《Flappy Bird》的对比，两个游戏的概念非常相似，但在执行层面差异很大。<br>
<br>
《Flappy Dunk》的难度非常平衡，这是一个代表性的超休闲玩法。当球落在篮筐的边框的时候，是可以蹭进去的，而不是碰到就失败。《Flappy Bird》是依赖强烈的挫败感和新奇感才能火爆全球的，并不是一个很好的超休闲玩法。<br>
<br>
我们拆分了可调整的组件，在《Flappy Dunk》重力弱一些，因此速度也慢一些。点击的力量非常轻，障碍物允许侧面进入，减少了惩罚。<br>
<br>
<div align="center">
<img id="aimg_1002284" aid="1002284" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114804djklfzcludlolbz5.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114804djklfzcludlolbz5.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114804djklfzcludlolbz5.png" referrerpolicy="no-referrer">
</div><br>
另一个案例是《Dune》VS《Tiny Wings》。在《Dune》中，镜头角度是可变的，当跳的更高的时候可以得到更高的高度和更远的距离。而《Tiny Wings》镜头角度固定，可获得的回报也更少。<br>
<br>
<div align="center">
<img id="aimg_1002285" aid="1002285" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114805qc85zlama2s81uvm.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114805qc85zlama2s81uvm.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114805qc85zlama2s81uvm.png" referrerpolicy="no-referrer">
</div><br>
接下来是节奏部分。刚才提到跑酷游戏需要足够的速度，还需要摆放的间隔。这都是为了游戏增加节奏。为什么节奏感在泛跑酷游戏中如此重要？简单地说就是为了引导用户达到心流状态。通过节奏和良性的循环，引导用户达到心流状态，进而增加玩家的参与感。<br>
<br>
<div align="center">
<img id="aimg_1002286" aid="1002286" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114806t6fzh0tnp6opg2oh.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114806t6fzh0tnp6opg2oh.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114806t6fzh0tnp6opg2oh.png" referrerpolicy="no-referrer">
</div><br>
心流是一种将个人的精神力、注意力完全投入到某种活动上的感觉，同时伴有高度兴奋感和充实感，是一种正向的情绪。<br>
<br>
当人们处于心流状态，可能会出现四个特征——<br>
<br>
自动运转：事情做起来顺手不需多加思考，身体自动发挥，所以游戏控制应该是防呆的。当身体自动发挥的时候，用户的控制和你设计的控制是不一样的。那么当用户的控制和你希望他做的控制不一样，游戏也可以正常运行，这时候游戏应该做防呆。<br>
<br>
时间流逝：不会在意时间的流逝，直到回到正常状态后，才会注意到时间过了多长时间。可以帮助游戏提升平均游戏时长。<br>
<br>
不觉他物：专注投入事物当中，导致不易察觉像是饥饿、收集震动等感觉与刺激。<br>
<br>
感到愉悦：在事情完成后，感受到愉悦、满足、成就感等正向情绪。<br>
<br>
<div align="center">
<img id="aimg_1002287" aid="1002287" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114807cknnwzw1jmowc3j8.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114807cknnwzw1jmowc3j8.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114807cknnwzw1jmowc3j8.png" referrerpolicy="no-referrer">
</div><br>
那么如何做到这样的节奏呢？我们思考一下游戏如何与用户互动，通常有三种方式。<br>
<br>
一是视觉，前面提到的视觉角度，镜头速度都是视觉上的反馈。<br>
<br>
二是触觉，游戏的第一个版本务必加入振动反馈，可以帮助游戏提升节奏感。<br>
<br>
三是音效，但音效不是必要的，如果有的话更好。<br>
<br>
当视觉，触觉，声音，三者融合起来，就是游戏中的节奏。<br>
<br>
<div align="center">
<img id="aimg_1002288" aid="1002288" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114807eaxbcx45y3xey5m3.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114807eaxbcx45y3xey5m3.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114807eaxbcx45y3xey5m3.png" referrerpolicy="no-referrer">
</div><br>
我们认为，游戏节奏的设置包括两种，一是你给他的，游戏设置的节奏，二是用户选择的节奏。但是用户选择的节奏非常依赖开发者的设计，所以我们更多地讲如何设置。<br>
<br>
游戏节奏首先要有默认的运动方式，无论是Z轴还是Y轴，要有一个稳定、较快的速度，并且加入一些物理感、重力感等。游戏中的收集品或障碍物，建议是连贯的，连贯指的是固定的间距，这样在固定速度的情况下，就会产生固定的节奏。同时加入手机的振动反馈。<br>
<br>
<div align="center">
<img id="aimg_1002289" aid="1002289" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114808c58v663rdy52jjjv.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114808c58v663rdy52jjjv.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114808c58v663rdy52jjjv.png" referrerpolicy="no-referrer">
</div><br>
既然游戏节奏有这么多要素，那么我如何平衡？还是那句话，不要花时间去创造轮子，只要选择对的，拿来用就可以了。《Cube Suffer》和《Stack Colors》都有非常好的游戏节奏。<br>
<br>
这里要强调的是，游戏要避免启停、中断节奏。如何理解呢？举个例子。如果说堆叠是在Z轴前进方向上堆叠杆子进行撑杆跳，这种概念的游戏目前还没有成功进入榜首的产品，我们分析问题在于游戏有很多启停。用户需要收集杆子，在需要跳的时候停止，整个游戏节奏被打断了。这很可能是这类游戏没有成功突破的原因。<br>
<br>
另外，我们建议采取单一控制，避免多重控制。因为多重控制的节奏更难设计。<br>
<br>
<div align="center">
<img id="aimg_1002290" aid="1002290" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114809hmluwx2yw7rhyzly.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114809hmluwx2yw7rhyzly.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114809hmluwx2yw7rhyzly.png" referrerpolicy="no-referrer">
</div><br>
下面讲一下游戏的循环。<br>
<br>
<div align="center">
<img id="aimg_1002291" aid="1002291" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114810hvdwzk2ixb2s9ywx.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114810hvdwzk2ixb2s9ywx.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114810hvdwzk2ixb2s9ywx.png" referrerpolicy="no-referrer">
</div><br>
第一类叫核心循环，为什么叫循环，意味着有操作有反馈，基于反馈再进行操作，这是核心循环，是每2-3秒需要用户体验的。我们认为这是超休闲游戏最重要的循环。<br>
<br>
第二是关卡结束循环，是在关卡结束的时候才能体验的。以超休闲游戏20-35秒的单局时长，意味着每20-35秒才会体验一次。<br>
<br>
第三是Meta循环，简单粗暴的理解为经济系统、皮肤、成就、升级等外层循环。这类循环通常用户玩了3-5关才会看一下，可能是每3-5分钟才会体验的。<br>
<br>
<div align="center">
<img id="aimg_1002292" aid="1002292" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114811l486dw6adiv68wa0.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114811l486dw6adiv68wa0.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114811l486dw6adiv68wa0.png" referrerpolicy="no-referrer">
</div><br>
那么玩家是如何体验这三种循环的呢？首先，用户打开了游戏后会立刻进入核心循环，因为之前看过游戏视频，玩家大约会花2-3秒钟熟悉游戏玩法。大家知道大多数超休闲游戏是没有新手教程的，也不需要新手教程，用户通过你提供的核心循环直接开始和游戏进行交互，通常用户在前10秒就会决定这个游戏会不会继续玩下去。这时留给开发者的非常短的时间窗口，换句话说，这10秒钟是抓住用户的关键时期，也就是游戏的核心循环。<br>
<br>
<div align="center">
<img id="aimg_1002293" aid="1002293" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114811sfskkwxq66o1711o.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114811sfskkwxq66o1711o.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114811sfskkwxq66o1711o.png" referrerpolicy="no-referrer">
</div><br>
只有用户完成第一个关卡后，才会进入后面的关卡循环。关卡循环是为了提升游戏体验，这就意味着，玩家在喜欢核心循环的前提下才会继续体验甚至喜欢上你的关卡循环，反过来说，玩家不会因为关卡循环做的好而接受不喜欢的核心循环——只有核心循环吸引住用户，关卡循环才有意义。<br>
<br>
<div align="center">
<img id="aimg_1002294" aid="1002294" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114811lsthgs112glh7112.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114811lsthgs112glh7112.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114811lsthgs112glh7112.png" referrerpolicy="no-referrer">
</div><br>
到了第三步的Meta循环，游戏的经济系统的循环。刚才提到，Meta循环的使用频次大约是3-5分钟一次，而全球的超休闲游戏每个用户单日平均游戏时长只有10分钟，还是在游戏表现很好的情况下。这意味着，幸运的情况下，用户一天可能只有两次打开Meta循环的机会。<br>
<br>
<div align="center">
<img id="aimg_1002295" aid="1002295" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114812z9fkhh197yrbt16k.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114812z9fkhh197yrbt16k.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114812z9fkhh197yrbt16k.png" referrerpolicy="no-referrer">
</div><br>
通过上述对用户旅程的分析，我们可以了解到，真正关乎到超休闲游戏能否在用户手机里留下，一定是在于最重要的，使用频率最高的核心循环。<br>
<br>
刚才提到核心循环是用户每天操作数百次的东西，也是决定了超休闲游戏概念是否被用户接纳的因素，所以在原型开发阶段，核心循环值得80%的投入。包括在创意阶段，以及原型开发阶段。<br>
<br>
所以在创意阶段要从核心动作开始创意，去思考核心循环的乐趣是什么？令人满意的特点是什么？它和目前市面上的游戏有什么不同？核心循环是否容易理解？视觉是否清晰？诸如此类的内容，应该是创意阶段投入80%的精力去考虑的内容。<br>
<br>
在原型开发阶段也要专注于核心动作，用有竞争力的美术去表现游戏的核心循环。在初次原型开发的时候，我们建议开发者不要花费太多的时间去设计关卡循环，甚至不花时间开发Meta系统，而要把精力放在核心循环上。<br>
<br>
<div align="center">
<img id="aimg_1002296" aid="1002296" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114812qz91yp7uflfoy7n9.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114812qz91yp7uflfoy7n9.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114812qz91yp7uflfoy7n9.png" referrerpolicy="no-referrer">
</div><br>
既然80%放在核心循环，那20%就是关卡结束循环。关卡结束循环有什么作用？首先，我们认为，关卡结束循环可以增加游戏的随机性，吸引玩家继续挑战。图中的案例是《Shortcut Run》，左图是核心循环，右图是关卡结束循环。在关卡结束循环里，可以清楚看见X5、X10、X20，带有一定运气成分。同时可以看见更远处的、倍率更高的台子，帮用户树立了中长期的目标。<br>
<br>
另一个作用是解释收集的目的和玩法。还是以《Shortcut Run》为例，收集了这么多砖块，到结尾有什么用处呢？可以继续搭桥，获得翻倍的奖励。这可以帮助用户树立短期目标，收集更多砖块，在结尾获得更多分数。<br>
<br>
关卡结束循环可以帮助游戏提升Playtime以及显著提升次留。<br>
<br>
<div align="center">
<img id="aimg_1002297" aid="1002297" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114813feeggqzs7y6g7be9.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114813feeggqzs7y6g7be9.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114813feeggqzs7y6g7be9.png" referrerpolicy="no-referrer">
</div><br>
再举两个例子。左侧是《Roof Rails》的核心循环和关卡结束循环，告诉用户要收集更长的杆子，才能到达最远的重点。类似的还有《Tower Run》，人数堆叠得足够高，才能达到顶部，获得更多奖励。<br>
<br>
<div align="center">
<img id="aimg_1002298" aid="1002298" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114813xqcozcwwwy5vyww8.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114813xqcozcwwwy5vyww8.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114813xqcozcwwwy5vyww8.png" referrerpolicy="no-referrer">
</div><br>
关于关卡结束循环，我们有几点建议。首先是使用和核心循环一样的操作，降低用户的学习成本，在进行关卡循环的时候不需要学习使用新的操作。并且关卡结束循环的主题建立和核心循环的主题相关，推荐大家尝试《Run Rich 3D》，就会理解我说的内容。开发时机建议在初始原型就搭建关卡循环的雏形，或者早期完全不考虑，当产品达到30/30或20/30的热原型标准时，才进行关卡结束循环的开发。<br>
<br>
<div align="center">
<img id="aimg_1002299" aid="1002299" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114814znnzn3mi6he3g1gs.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114814znnzn3mi6he3g1gs.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114814znnzn3mi6he3g1gs.png" referrerpolicy="no-referrer">
</div><br>
关于测试原型开发，我们建议5个关卡足矣。不是说只需要5个关卡，而是设计5个关卡，然后开始无限随机循环。如果少于5个关卡，次留和游戏时长数据通常无意义。<br>
<br>
这5个关卡可以是手工调制，也可以是程序自动生成。很多国内开发者的原型已经验证，3天开发出来的“5+∞”的关卡可以达到30%的次留和6分钟以上的游戏时长。<br>
<br>
在这个基础上，我们推荐至少有一个完美关卡。完美关卡可以清晰的展示核心玩法最有趣的一面，并且可以直接用来录制CPI广告测试视频的，甚至广告视频的一切都是按剧本发生的。<br>
<br>
<div align="center">
<img id="aimg_1002300" aid="1002300" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114815oxpxh4649uypnwqf.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114815oxpxh4649uypnwqf.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114815oxpxh4649uypnwqf.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">三、 超休闲游戏的美术：美术效率</font></strong><br>
<br>
美术效率是Voodoo一直强调的超休闲游戏七大要素之一。美术效率是衡量游戏的美术风格是如何支持游戏的澄清度，澄清度就是帮助看广告视频的观众和玩法去理解游戏玩法。并且画面应该简单明了，没有任何不必要的美术资源或视觉干扰，屏幕上的每一个东西都有自己的任务。<br>
<br>
好的美术有助于让你的产品更有卖相，已获得低CPI的优势。<br>
<br>
<div align="center">
<img id="aimg_1002301" aid="1002301" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114815jy7utfrt55c3t573.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114815jy7utfrt55c3t573.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114815jy7utfrt55c3t573.png" referrerpolicy="no-referrer">
</div><br>
以前我们会说美术够用就行，但看看下图这些位于榜单头部的产品，你的美术和他们相比有竞争力么？市场在不断进化，竞争越来越激烈，要保证自己的游戏美术有足够的竞争力。<br>
<br>
<div align="center">
<img id="aimg_1002302" aid="1002302" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114816mfcwccnprh2fn2jc.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114816mfcwccnprh2fn2jc.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114816mfcwccnprh2fn2jc.png" referrerpolicy="no-referrer">
</div><br>
开头提到“run rich”这个概念在5月份给到中国开发者进行原型开发，但最后胜出的是OHM的作品。我想说的是，当你有一个好的创意，美术是可以加成的。当然，这里不只是美术，不同的尝试和执行，会带来不同的结果。但美术是其中最明确的差异。<br>
<br>
<div align="center">
<img id="aimg_1002303" aid="1002303" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114817zqqrq55qg21tlamj.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114817zqqrq55qg21tlamj.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114817zqqrq55qg21tlamj.png" referrerpolicy="no-referrer">
</div><br>
我们认为，在玩法创新的大前提下，满足以下的条件时：<br>
<br>
1、 美术可以清晰传达游戏的玩法机制<br>
<br>
2、 避免任何视觉干扰<br>
<br>
3、 高对比呈现互动元素<br>
<br>
4、 不耽误4-7个工作日出原型<br>
<br>
美术实力越强，产品原型越有竞争力。<br>
<br>
<div align="center">
<img id="aimg_1002304" aid="1002304" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114818yct7getcjtnzf4eb.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114818yct7getcjtnzf4eb.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114818yct7getcjtnzf4eb.png" referrerpolicy="no-referrer">
</div><br>
美术可以帮助游戏提升卖相，但美术风格选择也很重要。下面简单对比抽象和写实。图中游戏从左到右是过去5年的演变，在5年前，抽象游戏还有很大空间。但随着竞争越来越激烈，偏写实的风格更有竞争力。<br>
<br>
但不是说抽象画风不行，而是现在的抽象画风需要玩法极具创新（例如Voodoo今年发行的Bounce & Collect）。当创新不够的时候，写实的美术风格有更强的竞争力。<br>
<br>
<div align="center">
<img id="aimg_1002305" aid="1002305" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114819y44n0nhwwsrugwwi.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114819y44n0nhwwsrugwwi.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114819y44n0nhwwsrugwwi.png" referrerpolicy="no-referrer">
</div><br>
关于美术效率有几点建议。首先是高亮并强调核心玩法中的元素，包括游戏主角、收集品、障碍物、跑道。这些是玩法最核心的元素，希望用户一眼看清，一眼看懂。并且可以突出和核心循环相关的要素，且这一切都是为了增加游戏的澄清度。<br>
<br>
<div align="center">
<img id="aimg_1002306" aid="1002306" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114819wrj33l672lir3f6e.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114819wrj33l672lir3f6e.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114819wrj33l672lir3f6e.png" referrerpolicy="no-referrer">
</div><br>
下面讲一下对比度的原理。对比度越高，眼睛识别的时间会更短，识别时间更短，就可以获得更低的CPI。所以高对比度可以提升CPI的竞争力。<br>
<br>
<div align="center">
<img id="aimg_1002307" aid="1002307" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114820uu6ekrusz7oiozsm.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114820uu6ekrusz7oiozsm.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114820uu6ekrusz7oiozsm.png" referrerpolicy="no-referrer">
</div><br>
我们推荐新晋的超休闲开发者务必在黑白图层下观察对比度。在黑白图层下，越接近黑白，对比度越高。在《Cube Suffer》中可以看到，跑道、障碍物、主角和收集品之间都有强烈的对比度。<br>
<br>
<div align="center">
<img id="aimg_1002308" aid="1002308" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114820ojln7tzgoohj8fzj.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114820ojln7tzgoohj8fzj.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114820ojln7tzgoohj8fzj.png" referrerpolicy="no-referrer">
</div><br>
以《High Heels》为例，同样可以看到黑白图层下的高对比度。<br>
<br>
<div align="center">
<img id="aimg_1002309" aid="1002309" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114821qwgv0nqf3kyy0gqq.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114821qwgv0nqf3kyy0gqq.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114821qwgv0nqf3kyy0gqq.png" referrerpolicy="no-referrer">
</div><br>
这两个案例用来说明黑白图层下，越接近黑白对比度越高，包括地面和跑道、收集品、障碍物。同时在背景里，视觉噪音越少越好。右下角的反例中，在黑白图层下，跑道、主角、收集品则混为了一团。<br>
<br>
<div align="center">
<img id="aimg_1002310" aid="1002310" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114821w7z2evabb68zbzew.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114821w7z2evabb68zbzew.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114821w7z2evabb68zbzew.png" referrerpolicy="no-referrer">
</div><br>
我们鼓励开发者使用积极的配色，想象一下，用户累了一天，他希望看到的是积极的配色，而不是沮丧的配色。非常建议大家使用被市场验证过的配色，而不是你个人喜欢的。<br>
<br>
同时，我们建议游戏达到60FPS，即使在低端机型上。当然我知道这不是美术问题，但胜似美术问题。我们希望游戏和视频足够流畅，不要出现掉帧。<br>
<br>
<div align="center">
<img id="aimg_1002311" aid="1002311" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114822cckrr3h41kl163ru.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114822cckrr3h41kl163ru.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114822cckrr3h41kl163ru.png" referrerpolicy="no-referrer">
</div><br>
我们一直强调减少视觉干扰，那么比较的典型错误是除了游戏主角外，有超过2个物体在同时移动。这样会导致同一时间内信息量太大，用户处理不过来，不知道该看哪里，导致看不懂，导致CPI变高。<br>
<br>
另一个是减少视觉噪音。意味着屏幕上的每一个东西都有自己的任务，如果屏幕上的东西没有任务，就不应该出现在屏幕上。能不出现的，就别出现。好的超休闲游戏，甚至不需要UI。<br>
<br>
<div align="center">
<img id="aimg_1002312" aid="1002312" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114822c93v9c39c9v99jc4.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114822c93v9c39c9v99jc4.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114822c93v9c39c9v99jc4.png" referrerpolicy="no-referrer">
</div><br>
而视觉干扰和视觉噪音，是我们发现的国内开发者经常掉入的陷阱，为了更好说明并帮大家节约开发成本，我们再举三个例子，也再次感谢提供这些案例的开发者们。左侧游戏可以看到，无数的黄色小人在运动，有非常大的视觉干扰。且背景中的房子和道路都会带来背景噪音，因为和游戏的玩法不相关。中间的案例也是同样的道理，飞镖在飞行的时候产生破碎的颗粒，带来严重的视觉干扰。右侧图中主角非常小，视觉干扰很多，看了很多次都不能理解自己要操作什么。<br>
<br>
<div align="center">
<img id="aimg_1002313" aid="1002313" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114823g850xc3cz52220w4.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114823g850xc3cz52220w4.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114823g850xc3cz52220w4.png" referrerpolicy="no-referrer">
</div><br>
更多美术指导、最佳实践和相关资料都在《Voodoo美术手册》里找到。<br>
<br>
<div align="center">
<img id="aimg_1002314" aid="1002314" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114823ezqz57bbc5chhbcq.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114823ezqz57bbc5chhbcq.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114823ezqz57bbc5chhbcq.png" referrerpolicy="no-referrer">
</div><br>
Voodoo已建立Discord开发者加速器沟通群，内含超休闲美术资源，包括UI、个性化人物定制组件、卡通Shaders、粒子效果、Unity免费资源等，这些是完全公开的。<br>
<br>
同时也会分享超休闲原型市场报告，北美社交趋势市场报告，往期所有中文直播录像，这些也是完全公开的。《超休闲技术开发手册》、《Android优化手册》、《美术手册》等资源，则需要册成为Voodoo开发者，方可访问（链接已经共享到Discord）。<br>
<br>
https://is.gd/voodoo_runner_yi<br>
<br>
<div align="center">
<img id="aimg_1002315" aid="1002315" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114824rodkojnq7wdzo9jo.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114824rodkojnq7wdzo9jo.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114824rodkojnq7wdzo9jo.png" referrerpolicy="no-referrer">
</div><br>
也欢迎大家通过网站提交工作室和相关产品信息，注册成为Voodoo开发者，展开测试。同时，可以获得超休闲技术开发手册、Android优化手册、美术手册的访问权限。<br>
<br>
<div align="center">
<img id="aimg_1002316" aid="1002316" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114824jwex0xxsae5lnush.png" data-original="https://di.gameres.com/attachment/forum/202108/20/114824jwex0xxsae5lnush.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114824jwex0xxsae5lnush.png" referrerpolicy="no-referrer">
</div><br>
voodoo.io/publishing/submit-your-game<br>
<br>
8月23日（下周一）下午5点，Voodoo会在B站（搜索Channel_Voodoo）带来新一期的开发者加速器直播，内容是《开启测试、CPI视频录制及项目规划技巧》，欢迎大家关注并预约。我们也会为大家带持续的更新和报道。<br>
<br>
<div align="center">
<img id="aimg_1002317" aid="1002317" zoomfile="https://di.gameres.com/attachment/forum/202108/20/114824mhn50yhvtxn5nxt3.jpg" data-original="https://di.gameres.com/attachment/forum/202108/20/114824mhn50yhvtxn5nxt3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/20/114824mhn50yhvtxn5nxt3.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="left"><font size="2"><font color="#808080"><br>
</font></font><br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080"><br>
</font></font><font size="2"><font color="#808080">来源：罗斯基</font></font><br>
<font size="2"><font color="#808080"><br>
</font></font><font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/3KeAp6TZlJ1qo_AxkjtKWA</font></font><br>
</div><br>
<br>
<br>
<br>
</td></tr></tbody></table>



  
</div>
            