
---
title: '做好FPS游戏中的那把武器：枪械数值从入门到精通'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202207/18/090746typey2vp3xnnnfq2.png'
author: GameRes 游资网
comments: false
date: Mon, 18 Jul 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202207/18/090746typey2vp3xnnnfq2.png'
---

<div>   
<i><font color="#808080">本文首发“TiMi Club 天美俱乐部”公众号</font></i><br>
<br>
大家好，我是来自天美《CF手游》的策划senz，在团队中我主要负责武器手感，写这个系列的文章目的有两个：<br>
<br>
对于自己，总结过去，积累当下，迎战未来。<br>
<br>
对于同行，与君共勉，共同进步，取精去糟。<br>
<br>
本文作为三部曲中的基础篇，主要介绍主流FPS游戏中枪械数值的构成，简单分析各个参数的设计目，并总结了一些个人见解，希望能启发到同行的同学。<br>
<br>
<strong><font color="#de5650">一、TTK（Time to Kill）</font></strong><br>
<br>
TTK：开第一枪后，子弹全部命中，击杀敌人所需要的时间。TTK越短，枪械理论强度越高。<br>
<br>
比如血量是100。<br>
<br>
AK伤害是35，射速是0.108秒/发，它的理论TTK就是 (3-1)*0.108=0.216秒。<br>
<br>
M4伤害是30，射速是0.095秒/发。它的理论TTK就是 (4-1)*0.095=0.285秒。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046463" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090746typey2vp3xnnnfq2.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090746typey2vp3xnnnfq2.png" width="600" id="aimg_1046463" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090746typey2vp3xnnnfq2.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">AK/M4 TTK对比</font></font></div><br>
但在实际交战中，有很多影响实际TTK的因素，下面就来拆解一下，一颗子弹从发射到命中，中间会经历些什么。<br>
<br>
<div align="center">
<img aid="1046464" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090746karc71jww6wz977c.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090746karc71jww6wz977c.png" width="600" id="aimg_1046464" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090746karc71jww6wz977c.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">子弹的一生</font></font></div><br>
<strong>基础伤害</strong><br>
<br>
首先是常规的步枪，以大家最熟悉的M4A1和AK47来举例，在CF中，M4伤害是30，AK伤害是35，这5点的伤害，会拉开两个枪型的子弹价值，因为M4是4枪死，AK是3枪死，所以他们的子弹价值就是1/4和1/3的区别。<br>
<br>
对步枪来说，每次开火的弹片数是1，但对于某些双持武器和霰弹枪来说，单次消耗的弹片数会大于1。<br>
<br>
实际伤害=单发伤害*弹片数。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046465" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090746afntxoyn4ty7axla.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090746afntxoyn4ty7axla.png" width="171" id="aimg_1046465" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090746afntxoyn4ty7axla.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">霰弹枪弹痕</font></font></div><br>
<strong>射速</strong><br>
<br>
每发子弹之间的开火间隔，间隔越小，射速越快，跟伤害共同组成理论TTK。<br>
<br>
通常为了保持整体TTK平衡，射速跟伤害是此消彼长的。<br>
<br>
<strong>距离衰减</strong><br>
<br>
随双方交战距离变远，伤害会随距离衰减。但在不同游戏中，衰减曲线需要匹配游戏关卡和枪械调性，并结合游戏3C来进行选择。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046466" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090747v8dp3i0noo00ldoe.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090747v8dp3i0noo00ldoe.png" width="600" id="aimg_1046466" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090747v8dp3i0noo00ldoe.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">4种常用衰减曲线</font></font></div><br>
分段衰减，优点是简单灵活，TTK稳定可控，可以精准控制距离区间的伤害，并确保衰减后的伤害是常数。<br>
<br>
其余的三种，线性和非线性衰减曲线的选择，主要看设计目的。比如游戏鼓励玩家近距离对枪，那选择图3（非线性衰减-）的曲线，可以让枪械前期伤害衰减迅速，同时搭配游戏中各种加强角色身法的3C机制，如滑铲、翻墙、钩锁、枪托攻击等，最终玩家行为就会比较符合策划的近距离对枪预期。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046467" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090747c9yzwo3zievie33v.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090747c9yzwo3zievie33v.gif" width="320" id="aimg_1046467" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090747c9yzwo3zievie33v.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">HALO无限：钩爪近身</font></font></div><br>
距离衰减也是区分枪系的重要参数，用来调控玩家的交战距离，影响玩家打法，比如拐角老六。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046468" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090747le89hcw35taamzzw.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090747le89hcw35taamzzw.png" width="488" id="aimg_1046468" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090747le89hcw35taamzzw.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CSGO：电击枪</font></font></div><br>
极限伤害距离，某些特殊武器，比如喷火枪，还会用极限伤害距离来控制武器的最远射程，是更直接粗暴的距离衰减。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046469" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090748ctla2lby2hqgbl2w.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090748ctla2lby2hqgbl2w.png" width="600" id="aimg_1046469" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090748ctla2lby2hqgbl2w.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CF葫芦娃喷火枪</font></font></div><font size="2"><font color="#808080"><br>
</font></font><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046470" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090748cjzwulzkl5ppwzlk.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090748cjzwulzkl5ppwzlk.png" width="600" id="aimg_1046470" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090748cjzwulzkl5ppwzlk.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">虚线后的距离无法造成伤害</font></font></div><br>
<strong>穿透衰减</strong><br>
<br>
交战双方之间如果有可穿透物体，伤害也会存在衰减。从市面上主流的射击游戏总结起来看，需要考虑下面几个因素：<br>
<br>
根据不同枪械确定其可穿透的材质（木头/石头/金属/玻璃/水面/冰块/草堆/人体）。<br>
<br>
根据不同的材质，分别给定衰减倍率，同时配套给一个最大穿透层数来收敛。一般来说一个BOX算1层，例如一个木箱和一扇木门都算1层。<br>
<br>
<div align="center">
<img aid="1046471" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090748xaa7iuukjzxwuzr0.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090748xaa7iuukjzxwuzr0.png" width="600" id="aimg_1046471" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090748xaa7iuukjzxwuzr0.png" referrerpolicy="no-referrer">
</div><br>
在不同材质衰减倍率的基础上，再加上厚度的计算，物体越厚，穿透衰减越大（CSGO引入了这个参数）。<br>
<br>
<div align="center">
<img aid="1046472" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090749v3cqyrjcdx4jbjrh.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090749v3cqyrjcdx4jbjrh.png" width="600" id="aimg_1046472" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090749v3cqyrjcdx4jbjrh.png" referrerpolicy="no-referrer">
</div><br>
穿透衰减除了用来区分枪系，平衡枪械强度外，还会影响玩家对局内信息的重视程度和续航能力。因为穿透会暴露枪线和枪声，大量消耗子弹。<br>
<br>
游戏越鼓励穿透行为，玩家对信息越不重视，对续航的要求越高。所以不同游戏要根据自己游戏的需要，调控玩家的穿透行为。<br>
<br>
受击部位<br>
<br>
子弹命中不同部位，伤害也会有区别。一般都会起码分为头、躯干、手、腿四个部位：<br>
<br>
头部伤害＞躯干伤害≈手部伤害≈基础伤害＞腿部伤害<br>
<br>
头：眉心/面/颈<br>
<br>
手：腕/臂<br>
<br>
躯干：胸/腹/背<br>
<br>
腿：大/小腿<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046473" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090749pf0l2vfafa2vw6fy.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090749pf0l2vfafa2vw6fy.png" width="445" id="aimg_1046473" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090749pf0l2vfafa2vw6fy.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">角色3P受击框</font></font></div><br>
冷知识：手游上头部面积太小了，把头部受击框稍微放大点，降低爆头门槛，体验会更好！<br>
<br>
命中不同部位会直接影响子弹价值和TTK：<br>
<br>
<div align="center">
<img aid="1046474" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090749ex3pioswlgl42zs7.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090749ex3pioswlgl42zs7.png" width="339" id="aimg_1046474" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090749ex3pioswlgl42zs7.png" referrerpolicy="no-referrer">
</div><br>
从平衡性角度来说，所有角色的3P受击框应该一致。这里有两个设计方案：<br>
<br>
在角色设计之初，就尽量贴合受击框，但是对美术同学会有限制。<br>
<br>
参考R6的做法，为了保持命中一致性，在命中非受击框区域时产生一些不一样的视觉/音效。<br>
<br>
<strong>护甲衰减</strong><br>
<br>
接着受击框，再讲讲防具：防弹衣/头盔。顾名思义，防具就是覆盖在角色受击框上的护甲，一般覆盖躯干和头部。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046475" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090749s0zwz3akw388pwom.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090749s0zwz3akw388pwom.png" width="600" id="aimg_1046475" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090749s0zwz3akw388pwom.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">我爱罗 砂の铠甲 看过吧</font></font></div><br>
对于不同游戏来说，防具服务于不同的目的，但基本上都是射击游戏的标配。<br>
<br>
<div align="center">
<img aid="1046476" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090750fawjcg7otzuaouog.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090750fawjcg7otzuaouog.png" width="530" id="aimg_1046476" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090750fawjcg7otzuaouog.png" referrerpolicy="no-referrer">
</div><br>
子弹命中这些受击框的时候伤害会有对应的伤害衰减，直接影响TTK，以M4为例，是否穿防具直接影响是否能一枪爆头：<br>
<br>
<div align="center">
<img aid="1046477" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090750tpqzgg7x7o1wnyxx.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090750tpqzgg7x7o1wnyxx.png" width="600" id="aimg_1046477" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090750tpqzgg7x7o1wnyxx.png" referrerpolicy="no-referrer">
</div>上面的图都是T-Pose，但实际局内的持枪动作各不相同。<br>
<br>
<div align="center">
<img aid="1046478" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090750plkqmggqzudkc4cg.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090750plkqmggqzudkc4cg.png" width="497" id="aimg_1046478" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090750plkqmggqzudkc4cg.png" referrerpolicy="no-referrer">
</div><br>
比如上面两张图，在正面交战的时候，面对步枪玩家的3P更容易命中无甲的手部，而面对手枪玩家的3P则更容易命中有甲的胸腹，所以3P持枪动作在一定程度上也可以作为枪械的“防御属性”，同时进攻方也会采取不同的游戏行为去针对这种防御属性，比如偷侧身。<br>
<br>
<div align="center">
<img aid="1046479" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090751bnk4j0z2oaj1ylta.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090751bnk4j0z2oaj1ylta.png" width="321" id="aimg_1046479" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090751bnk4j0z2oaj1ylta.png" referrerpolicy="no-referrer">
</div><br>
<strong>子弹飞行轨迹和速度</strong><br>
<br>
<strong>Hit-Scan</strong><br>
<br>
在传统巷战射击游戏，如CSGO和CF中，全都是激光射线，也叫做Hit-Scan。只要开火瞬间，激光射线跟敌人受击框相交，就算命中。可以理解为是一颗没有重力，速度无限大的子弹。<br>
<br>
巷战游戏用Hit-Scan是因为地图小、交战距离短、预期TTK短，选用Hit-Scan更适合玩法。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046480" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090751ddrre7rehxxltw7d.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090751ddrre7rehxxltw7d.png" width="536" id="aimg_1046480" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090751ddrre7rehxxltw7d.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CSGO：Hit-Scan</font></font></div><br>
<strong>Projectile</strong><br>
<br>
但随着现象级PUBG爆火，大地图BR逐渐成为主流，子弹也变成了有重力和飞行速度的Projectile。在大地图中，远距离对枪场景多，Projectile变成了射击体验的一部分。<br>
<br>
1.重力下坠：根据双方距离，在目标上方开火。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046481" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090751idpzszr3pkwshpvp.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090751idpzszr3pkwshpvp.gif" width="320" id="aimg_1046481" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090751idpzszr3pkwshpvp.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">PUBG：子弹下坠</font></font></div><br>
2.飞行弹速：根据双方距离和目标移动方向，打提前量。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046482" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090751oii8yc84yym1u4u5.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090751oii8yc84yym1u4u5.gif" width="320" id="aimg_1046482" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090751oii8yc84yym1u4u5.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">PUBG：飞行弹速</font></font></div><br>
3. 远距离TTK由于飞行弹速的加入而变长，对游戏节奏和玩家行为有影响。<br>
<br>
<strong>彩蛋1：伤害公式计算</strong><br>
<br>
TTK相关的参数有如此多，产生最终伤害之前会有伤害公式的运算。那必然会产生两个问题：<br>
<br>
1. 伤害是否取整？<br>
<br>
2. 公式运算顺序是否有影响？<br>
<br>
首先要确定是否要取整。不取整的优点是会让数值设计的颗粒度更细，与设计预期更相符。但假如游戏中明明白白地告诉了玩家HP=100，并且每次命中还会飘数字，那么建议还是要取整，不然前端显示和后台运算不一致，会让玩家产生疑惑“为什么他打我99我就死了？！”<br>
<br>
<div align="center">
<img aid="1046483" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090751stt62j65kjbh07zt.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090751stt62j65kjbh07zt.png" width="140" id="aimg_1046483" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090751stt62j65kjbh07zt.png" referrerpolicy="no-referrer">
</div><br>
其次取整的规则，四舍五入、进一、退一，根据自己游戏需要选择。<br>
<br>
如果不取整，那无须考虑公式运算顺序的问题。<br>
<br>
但如果取整，何时取整就显得很重要，比如下面的表格，取整的时机会直接影响到最终伤害。<br>
<br>
<div align="center">
<img aid="1046484" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090751xcmxchx8yncjycqj.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090751xcmxchx8yncjycqj.png" width="600" id="aimg_1046484" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090751xcmxchx8yncjycqj.png" referrerpolicy="no-referrer">
</div><br>
所以建议如果要取整，公式中间不要取整，全部用浮点计算，等实实在在算完之后，再最后统一取整（来自一个过来人，血的教训）。<br>
<br>
<strong>彩蛋2：绝对数值空间</strong><br>
<br>
枪械的绝对数值空间其实就是枪械TTK允许减少的程度。<br>
<br>
众所周知，CF的英雄级武器和普通武器之间存在数值差异。这里举一个CF手游的例子。<br>
<br>
M4A1-雷神的伤害比普通M4的伤害+1（31/30），那为什么AK47-火麒麟不+1（36/35）？<br>
<br>
首先，假设火麒麟伤害是36，我们把各个部位的伤害算出来。<br>
<br>
<div align="center">
<img aid="1046485" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090752px005neza9my0pza.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090752px005neza9my0pza.png" width="600" id="aimg_1046485" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090752px005neza9my0pza.png" referrerpolicy="no-referrer">
</div><br>
可以看到，M4伤害+1对子弹价值没有任何变化，如果射速一致，对TTK没有任何影响。<br>
<br>
反观AK，命中4枪腿和命中2枪手+1枪躯干，都从不致死变成了击杀，对TTK产生巨大影响。<br>
<br>
那后面能不能出32伤害的M4呢？显然不行，1枪爆头的M4，出了就凉了……<br>
<br>
<strong><font color="#de5650">二、弹道轨迹</font></strong><br>
<br>
这部分就是玩家口中的“枪械稳定性”，由后坐力和散发组成。<br>
<br>
<div align="center">
<img aid="1046486" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090752tcco60ygr0arivzl.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090752tcco60ygr0arivzl.png" width="600" id="aimg_1046486" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090752tcco60ygr0arivzl.png" referrerpolicy="no-referrer">
</div><br>
枪械的理论TTK决定了枪械强度的上限，而弹道轨迹决定了枪械强度的下限，以及枪械实际TTK达到理论TTK的难易程度。<br>
<br>
除此之外，弹道轨迹还有下面几个作用：<br>
<br>
1. 锚定枪械受众，决定一把枪适合新手还是高手。<br>
<br>
<div align="center">
<img aid="1046487" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090752mazrpoczdyuaiuoa.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090752mazrpoczdyuaiuoa.png" width="96" id="aimg_1046487" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090752mazrpoczdyuaiuoa.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1046488" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090752tbbybbheyxwxwxwb.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090752tbbybbheyxwxwxwb.png" width="96" id="aimg_1046488" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090752tbbybbheyxwxwxwb.png" referrerpolicy="no-referrer">
</div><br>
2. 枪械手感差异化的重要因素。<br>
<br>
<div align="center">
<img aid="1046489" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090752c12vbb1r337qcqd2.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090752c12vbb1r337qcqd2.png" width="600" id="aimg_1046489" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090752c12vbb1r337qcqd2.png" referrerpolicy="no-referrer">
</div><br>
3. 在TTK基础上，调控玩家行为和枪械外网K/D数据的手感数值空间。<br>
<br>
<div align="center">
<img aid="1046490" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090753s7syopy47plqmzmx.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090753s7syopy47plqmzmx.png" width="480" id="aimg_1046490" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090753s7syopy47plqmzmx.png" referrerpolicy="no-referrer">
</div><br>
弹道轨迹一般包括两个核心参数：后坐力、散发。主流的弹道模型有两种：<br>
<br>
1. CSGO、Valorant、CF：7形弹道<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046491" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090753bmbggl19lb9z594n.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090753bmbggl19lb9z594n.png" width="212" id="aimg_1046491" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090753bmbggl19lb9z594n.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Valorant弹道</font></font></div><br>
2. COD、PUBG：S形弹道<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046492" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090753smvco4znmjrvnrht.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090753smvco4znmjrvnrht.png" width="118" id="aimg_1046492" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090753smvco4znmjrvnrht.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">PUBG弹道</font></font></div><br>
因为我工作内容主要是7形弹道，所以下面主要以7形弹道展开。<br>
<br>
<strong>后坐力</strong><br>
<br>
首先解释一下压枪的概念：通过鼠标/手柄/划屏/陀螺仪等输入，去对抗后坐力的过程。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046493" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090753ae0s4zrmyyyj1gmn.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090753ae0s4zrmyyyj1gmn.gif" width="372" id="aimg_1046493" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090753ae0s4zrmyyyj1gmn.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CSGO：AK47压枪轨迹</font></font></div><br>
<strong>垂直后坐力</strong><br>
<br>
垂直方向的后坐力，一般固定向上，所以垂直后坐力是经过练习后能够完全掌握压枪的参数。触发垂直后坐力时，Camera会也会向上旋转一定角度来模拟后坐力。垂直后坐力在打出第一发子弹后触发，并通过Camera上抬来影响下一发的着弹点。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046494" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090753uipilveznvvisovr.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090753uipilveznvvisovr.gif" width="331" id="aimg_1046494" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090753uipilveznvvisovr.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">仅触发垂直后坐力演示</font></font></div><br>
<strong>水平后坐力</strong><br>
<br>
水平方向的后坐力，概率左右偏转，所以水平后坐力是经过练习后能够部分掌握压枪的参数。跟垂直类似，触发水平后坐力时，Camera会水平旋转一定角度，并影响后续着弹点。水平和垂直后坐力共同组成了枪械的基础弹道骨架。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046495" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090754l54x5gfu14xn5zfv.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090754l54x5gfu14xn5zfv.gif" width="331" id="aimg_1046495" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090754l54x5gfu14xn5zfv.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">仅触发水平后坐力演示</font></font></div><br>
<strong>最大后坐力</strong><br>
<br>
7形和S形弹道的区别，主要体现在这里。对于7型弹道来说，必须有最大后坐力来限制弹道骨架；但对于S形弹道来说，则不一定。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046496" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090754jpefv9pubhmhvb9i.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090754jpefv9pubhmhvb9i.png" width="600" id="aimg_1046496" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090754jpefv9pubhmhvb9i.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（7形弹道） （S形弹道）</font></font></div><br>
对于7形弹道来说，一般前5-8发子弹以纵向后坐力为主。之后达到最大纵向后坐力，然后只触发横向后坐力，并在最大横向后坐力的范围内，概率左右偏转。<br>
<br>
而横向后坐力的这个概率，也可以玩出很多花样，也可以玩出很多花样，可以做出正7、倒7、T形等弹道，体现手感差异。<br>
<br>
而对于S形弹道来说，可以没有最大后坐力，子弹足够可以达到仰角极限。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046497" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090754xq4pbr6t44g4gz4q.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090754xq4pbr6t44g4gz4q.gif" width="320" id="aimg_1046497" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090754xq4pbr6t44g4gz4q.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">PUBG：不压枪扫射</font></font></div><br>
S形弹道还可以引入分段的概念，不同子弹区间内的后坐力，可以设计成不一样，调控枪械的强势时期。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046498" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090754ltty5bl6kggttul2.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090754ltty5bl6kggttul2.png" width="600" id="aimg_1046498" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090754ltty5bl6kggttul2.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">后坐力修正</font></font></div><br>
在开火过程中，后坐力不一定是固定的，基础后坐力有一个Base值，后续后坐力在Base的基础上加上一个修正值。这个修正值如果是正数，就会越扫越飘；如果是负数，就会越扫越准。这个主要看枪械定位，和游戏是鼓励点射还是扫射。<br>
<br>
<div align="center">
<img aid="1046499" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090755sjzaddxawavzajwv.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090755sjzaddxawavzajwv.png" width="600" id="aimg_1046499" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090755sjzaddxawavzajwv.png" referrerpolicy="no-referrer">
</div><br>
1P不同状态下的后坐力修正也不一样，一般1P速度越慢，后坐力修正越小。<br>
<br>
<div align="center">
<img aid="1046500" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090755a2jxnm6wz2uauqu5.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090755a2jxnm6wz2uauqu5.png" width="514" id="aimg_1046500" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090755a2jxnm6wz2uauqu5.png" referrerpolicy="no-referrer">
</div><br>
像COD这种Locomotion特别强大的游戏，还会有滑铲、趴下、架枪等操作，也会对后坐力修正有影响。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046501" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090755s1jx41viaqvajwmv.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090755s1jx41viaqvajwmv.gif" width="556" id="aimg_1046501" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090755s1jx41viaqvajwmv.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（站立后坐力） （下蹲后坐力）</font></font></div><br>
这里也可以根据不同枪系的定位特点，去设计手感差异，让一些枪适合站撸，一些适合跑打。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046502" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090755if4p6c1j2g9f272g.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090755if4p6c1j2g9f272g.png" width="291" id="aimg_1046502" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090755if4p6c1j2g9f272g.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">全部起P90！这把RushB！</font></font></div><br>
<strong>点射机制</strong><br>
<br>
后坐力修正还会受到点射机制的影响，什么是点射机制？<br>
<br>
<div align="center">
<img aid="1046503" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090756kd3n3kvk3avv363l.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090756kd3n3kvk3avv363l.gif" width="209" id="aimg_1046503" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090756kd3n3kvk3avv363l.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">Valorant中的点射机制</font></font></div><br>
如上面的视频所示，点射机制就是：在冷却时间内再次输入开火指令，后坐力修正也会累积。直到在冷却时间后再开火，累积才会重置，表现就是视频中的速点会越点越飘。<br>
<br>
累积值可以小于1，这样可以让累积值的颗粒度比后坐力修正值的颗粒度更细。<br>
<br>
<div align="center">
<img aid="1046504" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090756sno9wsnzz9u1swqs.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090756sno9wsnzz9u1swqs.png" width="600" id="aimg_1046504" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090756sno9wsnzz9u1swqs.png" referrerpolicy="no-referrer">
</div><br>
冷却时间越短，触发后坐力修正要求的手速越快；累积值越小，触发后坐力修正的子弹数越靠后。两种做法都会让枪械的点射手感更舒服，速点时的后坐力表现更稳定。不同的枪械可以有不同的冷却时间和累积值，灵活使用点射机制，可以塑造多样性的点射手感。<br>
<br>
<strong>后坐力恢复</strong><br>
<br>
后坐力恢复：在后坐力触发后，延迟于后坐力触发的Camera回弹速度，一般单位是°/秒，纵向和横向的恢复可以区分配置。<br>
<br>
后坐力恢复对于点射和小连发非常重要，恢复速度越快，越精准。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046505" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090756a88izlevqeqlvbtt.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090756a88izlevqeqlvbtt.gif" width="600" id="aimg_1046505" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090756a88izlevqeqlvbtt.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（后坐力恢复慢） （后坐力恢复快）</font></font></div><br>
但对于扫射来说，影响不大，因为扫射过程中基本上不会触发到后坐力恢复。甚至如果枪械的最大后坐力太大，准星恢复对下一次开火还会有负体验，压枪之后镜头会往下掉。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046506" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090757t8ca6qivieiyleo8.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090757t8ca6qivieiyleo8.gif" width="292" id="aimg_1046506" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090757t8ca6qivieiyleo8.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">后坐力恢复镜头掉</font></font></div><br>
针对这种情况，当玩家压枪时，可以减去对应的Camera角度再进行后坐力恢复，避免对下次瞄准造成影响。比如COD和B4B都做了类似的处理。<br>
<br>
<div align="center">
<img aid="1046507" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090806qvd7y47aurr75a33.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090806qvd7y47aurr75a33.png" width="100" id="aimg_1046507" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090806qvd7y47aurr75a33.png" referrerpolicy="no-referrer">
<font size="2"><font color="#808080">
<img aid="1046508" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090806x8ybssbcqy88q07c.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090806x8ybssbcqy88q07c.png" width="102" id="aimg_1046508" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090806x8ybssbcqy88q07c.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（不压枪恢复） （压枪恢复）</font></font></div><br>
但在手游上要注意，如果玩家开启了陀螺仪，最好就不要对压枪做后坐力恢复处理，因为陀螺仪压枪后的手机回正，刚好可以把压枪的操作给抵消。<br>
<br>
<div align="center">
<img aid="1046509" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090806jeeo66eaqoubbeu9.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090806jeeo66eaqoubbeu9.png" width="527" id="aimg_1046509" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090806jeeo66eaqoubbeu9.png" referrerpolicy="no-referrer">
</div><br>
另外，后坐力恢复不一定会恢复到原点，比如PUBG的弹道，它是恢复到下一发子弹的落点，所以即使是点射也需要压枪。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046510" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090807xv6bqepppesx6crs.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090807xv6bqepppesx6crs.gif" width="600" id="aimg_1046510" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090807xv6bqepppesx6crs.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">PUBG后坐力恢复</font></font></div><br>
<strong>散发</strong><br>
<br>
讲完后坐力，接下来讲散发。<br>
<br>
散发：基于后坐力骨架，着弹点一定区域内随机散布。所以随机散发是玩家完全不可控的。<br>
<br>
<strong>基础散发</strong><br>
<br>
散发分布是一个投影在场景里的圆，所以交战距离越远，散发对实际TTK影响越大。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046511" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090807nov9jxy9xglrxxo9.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090807nov9jxy9xglrxxo9.png" width="600" id="aimg_1046511" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090807nov9jxy9xglrxxo9.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">散发概念示意图</font></font></div><br>
但因为散发是一个玩家不可控的参数，所以如果散发分布过于随机，尤其是当散发的子弹出现在后坐力的反方向时，射击体验就会很差。所以我们要在混沌中创造秩序，给这个圆一定的角度，根据不同的枪械去收敛散发的随机面积。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046512" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090808w76rr9xtitvi9nxp.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090808w76rr9xtitvi9nxp.png" width="600" id="aimg_1046512" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090808w76rr9xtitvi9nxp.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">不同枪系的散发面积收敛</font></font></div><br>
收敛后的面积应该在后坐力的方向上，因为这样玩家在压枪过程中，同时也在把随机面积拉往Camera中心。经过长时间的练习，玩家能提前让下一发的面积处于Camera中心附近，让玩家觉得枪被他压住了。<br>
<br>
<div align="center">
<img aid="1046513" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090808al1u31zjd314upff.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090808al1u31zjd314upff.png" width="438" id="aimg_1046513" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090808al1u31zjd314upff.png" referrerpolicy="no-referrer">
</div><br>
这里需要注意，第一枪没有后坐力向量，所以第一发的散发面积是个整圆；同时第一枪如果不准，会降低瞄准和卡点的收益，甚至会让玩家觉得被吞子弹了，所以基础散发的Base值不能太大。（霰弹枪：我呢？？？）<br>
<br>
<strong>散发修正/点射机制</strong><br>
<br>
和后坐力类似，散发也有修正值，可以越打越散，也可以越打越准，任君选择。同时散发修正也可以受到点射机制的影响，速点越点越飘。1P不同状态下的散发修正也不一样，跟后坐力类似。<br>
<br>
<div align="center">
<img aid="1046514" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090809uochl9hllof2k5xx.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090809uochl9hllof2k5xx.png" width="518" id="aimg_1046514" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090809uochl9hllof2k5xx.png" referrerpolicy="no-referrer">
</div><br>
但跟后坐力有所区别的是：因为散发存在随机，不可控，所以策划想让这把枪跑打不准，你练多久都没用！所以P90，YYDS！全部起P90！这把继续RushB！<br>
<br>
<div align="center">
<img aid="1046515" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090809lupvvgg5r8debvll.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090809lupvvgg5r8debvll.png" width="328" id="aimg_1046515" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090809lupvvgg5r8debvll.png" referrerpolicy="no-referrer">
</div><br>
另外是否鼓励跑打也跟游戏调性有关系：<br>
<br>
1.CSGO、Valorant强调爆破，信息博弈、技能道具施放，不鼓励玩家大身位干拉，所以移动散发很大，站撸才能打准。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046516" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090810ku74xjjr9rurr35u.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090810ku74xjjr9rurr35u.png" width="600" id="aimg_1046516" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090810ku74xjjr9rurr35u.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Valorant移动散发</font></font></div><br>
2.COD强调激爽突突突，本身角色运动能力就强，那就钢枪战个痛快，移动散发较小；CF作为大盘向下沉版的CSGO，既保留了钢枪爽快，也保留了爆破的战术博弈，移动散发也较小。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046517" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090810eze6jyyyi09nzi9j.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090810eze6jyyyi09nzi9j.png" width="600" id="aimg_1046517" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090810eze6jyyyi09nzi9j.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CF移动散发</font></font></div><br>
<strong>整体弹道</strong><br>
<br>
后坐力和散发都介绍完了，一个完整的弹道就有了。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046518" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090811xtt28m6nyovau265.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090811xtt28m6nyovau265.gif" width="372" id="aimg_1046518" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090811xtt28m6nyovau265.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CSGO：AK47弹道</font></font></div><br>
还是以7形弹道为例，前期的弹道主要压纵向后坐力，考验压枪技巧。<br>
<br>
中后期弹道一直在最大横向后座力中间概率偏转，这里除了考验压枪之外，其实还提供了一个容错率，并且随着交战距离越来越远，角色的宽度占横向后坐力宽度的比例会越来越低，子弹覆盖范围会越来越大，但子弹命中的概率会越来越低。<br>
<br>
<div align="center">
<img aid="1046519" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090812fp4aff4xzu6zfbbf.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090812fp4aff4xzu6zfbbf.png" width="600" id="aimg_1046519" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090812fp4aff4xzu6zfbbf.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">最大横向后坐力形成的容错率区间</font></font></div><br>
最后加上散发，调控枪械命中率。<br>
<br>
从长期的练枪收益上看：<br>
<br>
1.纵向后坐力：能完全掌握<br>
<br>
2.横向后坐力：能部分掌握<br>
<br>
3.散发：无法掌握<br>
<br>
所以，针对高玩，要提高压枪难度和上手门槛，但可以通过长期练习掌握，并尽量接近理论TTK；<br>
<br>
而对新手玩家，要降低门槛，通过无法完全掌握的参数，控制实际TTK分布。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046520" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090813zo94nb9q2qnnqooq.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090813zo94nb9q2qnnqooq.png" width="529" id="aimg_1046520" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090813zo94nb9q2qnnqooq.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">不同受众枪的数值分布</font></font></div><br>
<strong>准星</strong><br>
<br>
射击游戏必备，永远在Camera中心的视觉提示。<br>
<br>
<strong>准星颜色</strong><br>
<br>
准星默认颜色要根据场景的主色调来选择，玩家玩得最多的地图，比如CSGO的Dust_2、CF的沙漠灰、PUBG的绿岛。准星颜色跟场景主色调的辨识要拉开，所以CSGO和CF的准星默认颜色是绿色，PUBG是白色。<br>
<br>
<div align="center">
<img aid="1046521" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090814lf8akeaqa0u61ae8.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090814lf8akeaqa0u61ae8.png" width="543" id="aimg_1046521" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090814lf8akeaqa0u61ae8.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（PUBG默认准星颜色）</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1046522" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090815bsxm9aszgukzzs8r.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090815bsxm9aszgukzzs8r.png" width="486" id="aimg_1046522" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090815bsxm9aszgukzzs8r.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（CF默认准星颜色）</font></font></div><br>
<strong>准星扩散</strong><br>
<br>
在开火后，准星中间的空隙会扩大，主要有两个作用：<br>
<br>
1.作为开火手感延续的一部分，模拟武器开火后坐力以及回到待机动作的过程。<br>
<br>
2.提示玩家散发随着开火逐渐变化的过程。<br>
<br>
所以比较好的手感是：准星扩散速度与开火动作一致、准星缩小速度与开火后摇一致、散发面积与准星空隙吻合。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046523" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090815xto3qxoroct2o2b7.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090815xto3qxoroct2o2b7.gif" width="377" id="aimg_1046523" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090815xto3qxoroct2o2b7.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">准星扩散开火后摇</font></font></div><br>
<strong>准星偏移</strong><br>
<br>
准星偏移常见于7形弹道，CF、CSGO、Valorant的弹道都有准星偏移的设计。CF里是通过准星下坠实现，CSGO和Valorant是通过着弹点上移实现。<br>
<br>
<div align="center">
<img aid="1046524" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090816p88p25h7dvm02qq8.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090816p88p25h7dvm02qq8.gif" width="293" id="aimg_1046524" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090816p88p25h7dvm02qq8.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">CF准星偏移：准星下坠</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1046525" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090816jvyfavuyv0poszcf.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090816jvyfavuyv0poszcf.gif" width="404" id="aimg_1046525" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090816jvyfavuyv0poszcf.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Valorant准星偏移：着弹点上跳</font></font></div><br>
可以看到在扫射到最大纵向后坐力时，下一发子弹会突然与Camera中心脱离，偏移一定的比例，着弹点此时会在准星的上沿。这个现象其实早在CS1.5时代就有，这样设计的目的和好处是什么：<br>
<br>
1. 扫射到最大纵向后坐力之后，此时散发已经很大，准星也会扩散到很大，中间空隙过大导致准星已经有点失去了瞄准的作用。但是准星偏移后，着弹点在准星上沿，可以把准星上沿当作一个箭头的作用，指向性更明确，类似于PUBG的三角准星。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046526" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090817uzk6io6uu16qq6mu.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090817uzk6io6uu16qq6mu.gif" width="519" id="aimg_1046526" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090817uzk6io6uu16qq6mu.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">三角准星</font></font></div><br>
2. 扫到最大纵向后坐力后，Camera不再上抬，只会左右偏转。因为横向后坐力存在概率，比较难压，所以玩家在扫到这个阶段时，都会去瞄敌人的爆头线，提高命中收益。而准星上沿，跟敌人的头部可以更好地重合，瞄准手感更好。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046527" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090819v39b3ysgooo5lgme.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090819v39b3ysgooo5lgme.gif" width="520" id="aimg_1046527" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090819v39b3ysgooo5lgme.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">准星上沿瞄头</font></font></div><br>
3. 准星的突然偏移需要玩家进行额外的突变压枪，难度更高。<br>
<br>
对于大盘玩家，会鼓励他们在5-8发子弹时收枪，别直接跪倒30发，符合爆破信息博弈的游戏调性。<br>
<br>
<div align="center">
<img aid="1046528" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090819phhhhr1dhgu6sisr.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090819phhhhr1dhgu6sisr.png" width="333" id="aimg_1046528" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090819phhhhr1dhgu6sisr.png" referrerpolicy="no-referrer">
</div><br>
对于高玩，也深挖了压枪体验，不同的枪械可以根据散发有不同的偏移幅度。<br>
<br>
所以不管这个准星偏移在CS1.5的时候是不是BUG，现在它已经演变成了射击体验的一环，所以在CSGO和Valorant中都保留了下来。<br>
<br>
<strong>准星自定义</strong><br>
<br>
上面的都是废话，因为准星自定义现在基本上是射击游戏的标配。不管你官配设计得有多好，萝卜青菜各有所爱，玩家说：“我自己调的才是最好的”。<br>
<br>
CSGO和Valorant的准星自定义系统是最详细最专业的。<br>
<br>
<div align="center">
<img aid="1046529" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090820d2mjh9ngwa9pjjls.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090820d2mjh9ngwa9pjjls.png" width="132" id="aimg_1046529" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090820d2mjh9ngwa9pjjls.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1046530" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090820wdkd7mmmlo7jnb2a.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090820wdkd7mmmlo7jnb2a.png" width="185" id="aimg_1046530" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090820wdkd7mmmlo7jnb2a.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046531" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090820bf1xfggz6iq6qgqq.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090820bf1xfggz6iq6qgqq.png" width="600" id="aimg_1046531" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090820bf1xfggz6iq6qgqq.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">B站上玩家的自定义准星</font></font></div><br>
但准星自定义里有一个神器：准星不扩散。就是不管怎么开火，准星都不会变。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046532" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090821kfr6mc3d3f36utz3.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090821kfr6mc3d3f36utz3.gif" width="293" id="aimg_1046532" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090821kfr6mc3d3f36utz3.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">准星不扩散</font></font></div><br>
不扩散的准星，从视觉感官上给玩家一种散发没有变大的错觉，对手感会有提升。并且如果是极致的不扩散准星，还可以清晰地看到弹痕特效形成的弹道轨迹，帮助玩家压枪。<br>
<br>
但准星不扩散也有缺点，就是扫射到最大纵向后坐力之后，由于准星偏移，爆头线和准星之间的距离就不好掌握了。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046533" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090822zj8o8tcmzcscym33.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090822zj8o8tcmzcscym33.gif" width="477" id="aimg_1046533" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090822zj8o8tcmzcscym33.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">准星不扩散下的压枪</font></font></div><br>
Valorant给出了两种解决方案：<br>
<br>
1. 再提供一个额外的外围准星，外围准星的间隔可以设置为常用枪械准星偏移的距离，偏移后用外围准星去压爆头线。<br>
<br>
<div align="center">
<img aid="1046534" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090822fqeqlve8ahu8eney.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090822fqeqlve8ahu8eney.png" width="600" id="aimg_1046534" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090822fqeqlve8ahu8eney.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046535" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090824w6561r0jglw65lfj.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090824w6561r0jglw65lfj.png" width="278" id="aimg_1046535" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090824w6561r0jglw65lfj.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">外围准星</font></font></div><br>
2. 在准星偏移时，上边准星消失。准星消失不仅可以提示玩家准星偏移的时间，还防止准星干扰玩家观察着弹点。<br>
<br>
<div align="center">
<img aid="1046536" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090824ee300p2qgm33qxx9.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090824ee300p2qgm33qxx9.png" width="600" id="aimg_1046536" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090824ee300p2qgm33qxx9.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046537" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090825f41se1zjf1zh1zfh.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090825f41se1zjf1zh1zfh.png" width="211" id="aimg_1046537" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090825f41se1zjf1zh1zfh.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">准星偏移淡出</font></font></div><br>
<strong>命中反馈</strong><br>
<br>
准星还承担了一个很重要的功能，命中敌人的视觉反馈，这个反馈不仅能获取信息，还能加强打击感。命中反馈还可以在爆头或击杀的时候做更强的提示，来跟普通命中区分开。<br>
<br>
<div align="center">
<img aid="1046538" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090826c3lv6x3gz3vvazqb.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090826c3lv6x3gz3vvazqb.png" width="178" id="aimg_1046538" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090826c3lv6x3gz3vvazqb.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046539" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090826khwzegee383xkzlg.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090826khwzegee383xkzlg.gif" width="354" id="aimg_1046539" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090826khwzegee383xkzlg.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">命中反馈</font></font></div><br>
<strong>非腰射准星</strong><br>
<br>
上面讲到的准星是腰射HUD准星，但随着主流游戏机瞄和枪匠系统的普及，准星已经越来越写实并多样化。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046540" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090827kyjww88wwjj8xhhg.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090827kyjww88wwjj8xhhg.png" width="600" id="aimg_1046540" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090827kyjww88wwjj8xhhg.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">各个游戏的非腰射准星</font></font></div><br>
在玩家举镜/开镜之后，就能看到这些非腰射准星。他们都有一个共同的作用，降低视场角（FOV），看得更远，但视野减少。但其实它们还有很多实用的功能：<br>
<br>
1. 举镜后，减小散发或后坐力。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046541" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090827px2xrwaafjkzxjc2.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090827px2xrwaafjkzxjc2.gif" width="574" id="aimg_1046541" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090827px2xrwaafjkzxjc2.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">COD腰射机瞄散发对比</font></font></div><br>
2. 用准星上的基准点提示，计算对应距离的子弹重力下坠。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046542" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090828jah99nadaj1c59xx.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090828jah99nadaj1c59xx.png" width="550" id="aimg_1046542" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090828jah99nadaj1c59xx.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">PUBG瞄镜</font></font></div><br>
3. 遮挡玩家视野，影响机瞄手感，是枪械数值空间的一部分。比如COD的GRAU 5.56机瞄视野非常开阔，所以相比于M4，可以省下1个瞄镜的配件给其他部位装配。<br>
<br>
<div align="center">
<img aid="1046543" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090828ioelxjktj7ieokxl.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090828ioelxjktj7ieokxl.png" width="600" id="aimg_1046543" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090828ioelxjktj7ieokxl.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（GRAU 5.56机瞄）</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1046544" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090854g8jjm0fe0p8vxesf.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090854g8jjm0fe0p8vxesf.png" width="600" id="aimg_1046544" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090854g8jjm0fe0p8vxesf.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（M4机瞄）</font></font></div><br>
4. Valorant顶级融合。不仅玩法上完美融合了英雄技能和射击，而且射击手感也完美融合了两种习惯。不开镜是传统的准星偏移手感，开镜是指哪打哪的手感。顶级拓盘全民游戏，Valorant真好玩！<br>
<br>
<div align="center">
<img aid="1046545" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090855br14qiqhhr03izwi.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090855br14qiqhhr03izwi.gif" width="320" id="aimg_1046545" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090855br14qiqhhr03izwi.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（腰射准星偏移）（开镜准星不偏移）</font></font></div><br>
5. COD中还有提高敌人视觉辨识的热力和夜视瞄镜，辅助玩家瞄准<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046546" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090855moowlzp5z6iat3io.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090855moowlzp5z6iat3io.gif" width="320" id="aimg_1046546" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090855moowlzp5z6iat3io.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">COD热力瞄镜</font></font></div><br>
<strong>受击上扬/血弧</strong><br>
<br>
受击上扬和血弧一般是同时触发的。<br>
<br>
受击上扬：被命中时，Camera会有叠加于后坐力的突然上抬，上抬速度和恢复速度的单位跟后坐力类似，也是°/秒。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046547" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090856xn0rvir3vktztyrv.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090856xn0rvir3vktztyrv.gif" width="277" id="aimg_1046547" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090856xn0rvir3vktztyrv.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">步枪受击上扬</font></font></div><br>
受击上扬可以作为进攻属性，命中后给敌人造成的上扬；也可以作为防御属性，被命中后自己的上扬，可以根据游戏需要来设计。<br>
<br>
不同的枪械可以拥有不同的上扬幅度，尤其是对于狙击枪这种FOV比较小的武器来说，受击上扬是一个非常重要的数值。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046548" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090858kec1sfjdg47ugg4x.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090858kec1sfjdg47ugg4x.gif" width="287" id="aimg_1046548" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090858kec1sfjdg47ugg4x.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">狙击枪受击上扬</font></font></div><br>
命中不同的部位，上扬的幅度也可以有区别，比如CSGO钉头和普通命中的上扬就有明显的区别，以提高爆头的收益。<br>
<br>
血弧：被命中时，在HUD上提示受击的方向，记住这个口诀：上前下后，左左右右。<br>
<br>
血弧提示的强度可以根据游戏需要决定。可以只提供瞬间的受击方向；也可以随着玩家镜头转向；也可以让血弧和血线结合，不仅提示来向，还提示丢失/剩余多少血量。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046549" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090901em6g4ez5iqo6zqi5.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090901em6g4ez5iqo6zqi5.gif" width="519" id="aimg_1046549" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090901em6g4ez5iqo6zqi5.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">COD血弧</font></font></div><br>
<strong>彩蛋：什么枪好压</strong><br>
<br>
首先祭出一张跨时代的图，乔布斯的iPhone4，手指最大可触摸的范围。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046550" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090901gs87ssgm0m5g8038.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090901gs87ssgm0m5g8038.png" width="334" id="aimg_1046550" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090901gs87ssgm0m5g8038.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">iPhone4 拇指操作舒适区</font></font></div><br>
从竖屏操作演变到现在的横屏手游，操作热区变成了这样的一个内八热区。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046551" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090904e6cfcdc6dl5cqqmw.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090904e6cfcdc6dl5cqqmw.png" width="600" id="aimg_1046551" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090904e6cfcdc6dl5cqqmw.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">射击手游交互分布</font></font></div><br>
对于键鼠来说也是类似的内八。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046552" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090904xd2b5ykm2sd7dsd1.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090904xd2b5ykm2sd7dsd1.png" width="600" id="aimg_1046552" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090904xd2b5ykm2sd7dsd1.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">韦神键鼠位</font></font></div><br>
因为人体的构造，手指和手肘的关节都只允许内翻，不能外翻，所以往内操作比往外操作要更舒服。所以正7字弹道要比反7字弹道更好压。大家可以在屏幕上比划一下，右图会比左图划起来更舒服。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046553" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090905dd9qg9c9nvc6acrk.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090905dd9qg9c9nvc6acrk.gif" width="595" id="aimg_1046553" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090905dd9qg9c9nvc6acrk.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">右图压枪更符合人体结构</font></font></div><br>
同样道理，遭遇敌人时，往他的左边横拉，对面也更难命中你。而且往左边横拉还有一个好处，大部分玩家都习惯右手持枪，枪模也可以遮挡他的一部分视野。（如果对面是陀螺仪，以上方法没用）。<br>
<br>
<div align="center">
<img aid="1046554" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090906k8l5x3eiv8ax66lq.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090906k8l5x3eiv8ax66lq.png" width="590" id="aimg_1046554" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090906k8l5x3eiv8ax66lq.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">三、机动能力</font></strong><br>
<br>
<strong>移速</strong><br>
<br>
<strong>最高移速</strong><br>
<br>
不同枪械和当前1P的不同状态，都会影响枪械的手持最高移速<br>
<br>
<div align="center">
<img aid="1046555" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090907xbiff7r7xoelbenm.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090907xbiff7r7xoelbenm.png" width="518" id="aimg_1046555" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090907xbiff7r7xoelbenm.png" referrerpolicy="no-referrer">
</div><br>
移速是一项攻守兼备的数值：<br>
<br>
1. 进攻性：移速快，可以提前卡点，拥有更好的对枪条件，所以开局一般都会切刀跑路。<br>
<br>
2. 防守性：移速越快的枪械在横移时，敌人跟枪难度更高。<br>
<br>
在地面时，切枪时1P移速就会变成对应枪械的手持移速；但如果在空中切枪，滞空时依然会保留上一把武器的移速，直到落地才会变。所以在横跳拉枪线或者打信息的时候，在空中切枪是更好的选择。<br>
<br>
<strong>加速减速</strong><br>
<br>
刚刚说到的是枪械对应的最高移速，但在启停时，速度不是瞬时切换的，会有对应的加速度和减速度。加减速度越大，移动的操控感会越灵敏，否则会更迟滞。游戏调性不同，启停的加减速度也不同。鼓励跑打的CF加减速度大，鼓励信息博弈的CSGO加减速度小。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046556" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090908fe6yba633bqyvbd0.gif" data-original="https://di.gameres.com/attachment/forum/202207/18/090908fe6yba633bqyvbd0.gif" width="320" id="aimg_1046556" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090908fe6yba633bqyvbd0.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">CSGO：加速度/减速度</font></font></div><br>
所以在CSGO这种移动散发惩罚很大的游戏中，会有急停的操作，在停下来时，额外输入1次反方向移动的指令，加快散发恢复成静止散发的时间。<br>
<br>
<div align="center">
<img aid="1046557" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090908u9chvbbuc1rmzc99.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090908u9chvbbuc1rmzc99.png" width="361" id="aimg_1046557" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090908u9chvbbuc1rmzc99.png" referrerpolicy="no-referrer">
</div><br>
同时，减速度对散发的影响很大，因为散发对应的是当前状态的散发，所以减速度越小，从移动到静止的时间越长，移动散发恢复到站立散发的时间就越长。<br>
<br>
减速度同样可以体现武器定位和手感差异，比如现在要做一把冲锋狙，在散发的考虑上，首先它的移动散发可以比正常的卡点狙更小，同时它的减速度可以比卡点狙更大，这样它恢复到静止散发的时间也就更短，符合其冲锋狙的定位。<br>
<br>
<div align="center">
<img aid="1046558" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090909yozoj4ehjmpdgjcj.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090909yozoj4ehjmpdgjcj.png" width="600" id="aimg_1046558" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090909yozoj4ehjmpdgjcj.png" referrerpolicy="no-referrer">
</div><br>
除了启停的加减速度，还有受击减速。在CSGO或Valorant这种短TTK和强调战术博弈的游戏中比较常见。受击减速可以让命中方更好跟枪，但是对受击方会有强烈的负反馈，所以这个设计要谨慎选择。<br>
<br>
比如说CF作为移动散发比较小的射击游戏，强调钢枪体验，不应该有受击减速，但是CF的“空尖弹”，让它拥有了命中减速的进攻属性，例如EVO系列。而且EVO还是一把高射速的冲锋枪，高射速可以放大命中减速的效果，让EVO更粘人。<br>
<br>
<div align="center">
<img aid="1046559" zoomfile="https://di.gameres.com/attachment/forum/202207/18/090910e3f50o2fwisfllnp.png" data-original="https://di.gameres.com/attachment/forum/202207/18/090910e3f50o2fwisfllnp.png" width="488" id="aimg_1046559" inpost="1" src="https://di.gameres.com/attachment/forum/202207/18/090910e3f50o2fwisfllnp.png" referrerpolicy="no-referrer">
</div><br>
受击减速也是攻守兼备的数值，可以针对不同的枪械配置命中减速或受击减速减免。但要注意减速倍率和减速持续时间一定不能叠加，只能下一次命中把上次一次的给重置，不然受击者的负反馈会更加强烈。<br>
<br>
<strong>切枪速度</strong><br>
<br>
<strong>切枪</strong><br>
<br>
传统的CF、C  
</div>
            