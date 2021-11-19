
---
title: '用立方体色块造就千军万马之势，《银河破裂者》中的AI系统竟是这样做出来的'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.699h5.com/attachment/forum/202111/16/092139vcbwww7mszms27rz.jpg'
author: GameRes 游资网
comments: false
date: Tue, 16 Nov 2021 00:00:00 GMT
thumbnail: 'https://di.699h5.com/attachment/forum/202111/16/092139vcbwww7mszms27rz.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2518705">
《银河破裂者》是一款内容丰富，趣味横生的游戏。在探索自己所在的外星球时，您永远没有真正安全的时刻。即使你躲在基地的墙后，尝试熬过夜晚，也会有成千上万的敌人准备攻击你。生成成群的外星生物不是问题，让它们以令人信服的方式行事才是。笔者会向大家展示开发人员必须采取哪些步骤才能让这个游戏世界充满活力。<br><br><div align="center">
<img id="aimg_1021507" aid="1021507" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092139vcbwww7mszms27rz.jpg" data-original="https://di.699h5.com/attachment/forum/202111/16/092139vcbwww7mszms27rz.jpg" width="600" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092139vcbwww7mszms27rz.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#808080">作者：Piotr Bomak</font><br><font color="#808080">校稿：maggiemmi</font><br><font color="#808080">本文内容首发Game Developer，经由GWB编译首发自“腾讯GWB游戏无界”公众号</font><br><font color="#808080">https://www.gamedeveloper.com/disciplines/the-puppet-master---the-development-of-the-ai-system-for-the-riftbreaker</font><br><br>
前文回顾（点击下方文字即可查看全文）：<br><br><a href="https://www.699h5.com/890875.html" target="_blank">万物皆可随机化！浅谈《银河破裂者》中程序化地图生成</a><br><br>
即使您的目标是让数以千计的敌人同时攻击玩家，最开始也只是从几个敌人开始。下面展示的是《银河破裂者》的首批原型之一。基本上什么都没有，甚至连物体的比例都有问题，但足以进行第一次实验。占位符立方体象征着敌人，您可以看到他们正试图定位并接近玩家。当时我们尝试使用我们在Zombie Driver中使用的旧款生物碰撞检测系统。每个敌人在其碰撞体前都有 3 条光线轨迹，以避开其他实体和世界部分。<br><br><div align="center">
<img id="aimg_1021508" aid="1021508" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092141p31unln3a3hvrki3.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092141p31unln3a3hvrki3.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092141p31unln3a3hvrki3.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">这些看起来可能不怎么样，但这确实是《银河破裂者》在 2018 年初的样子</font></font></div>
<br>
好吧，即使它看起来干得还不错，但算法有点过时了。它还不够好。我们希望我们的生物快速而狂暴，而不是笨拙。我们移除了所有的光线轨迹并开始使用分离力和内聚力。这给了我们更好的移动，这是我们未来工作的第一步。在那段时间里，我们通过数学和物理，测试我们所有的想法。在这个例子中，几十个敌人正在追赶玩家，同时他们在墙壁之间回旋。敌人穿过狭窄的通道，一旦到达空地，就会再次散开。整洁，一切似乎都运行良好，但这只是开始。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1021509" aid="1021509" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092141wy7z4j1ycz22l20k.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092141wy7z4j1ycz22l20k.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092141wy7z4j1ycz22l20k.gif" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">你们永远抓不住我</font></font></div>
<br>
如果游戏中只有一种敌方单位，任何游戏都会很快变得无聊。即使在《吃豆人》中，每个鬼魂也以独特的方式行事。（说真的！看看这篇文章）。Galatea 37 是多个物种的家园，每个物种都彼此不同。<br><br>
有一条重要的规则，如果一个系统对一件事起作用，那么它对其他事也同样起作用。我们需要测试我们的数学方程如何处理不同大小和速度的生物。他们会互相粘在一起吗？他们能避开所有世界物体吗？当时有很多问题需要回答。而唯一的方法就是将每一个想法和解决方案付诸实践。看吧！我们为您带来终极的 Canoptrix、Arachnoid 和 Hammerroceros 冲刺！（它们一点也不慢，这里只是慢放了。100% 正确。）<br><br><div align="center">
<img id="aimg_1021510" aid="1021510" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092141qrbqbqtckvrpryb6.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092141qrbqbqtckvrpryb6.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092141qrbqbqtckvrpryb6.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">准确的把学生在几何测试前的噩梦可视化了</font></font></div>
<br>
现在是第一次考验战斗能力的时候了。在这一点上，我们有点厌倦了在灰色空间中运行的彩色立方体，因此我们用Zombie Driver中狗狗的模型替换了橙色立方体。在此片段中，您可以看到狗试图攻击玩家，但是途中有一些防御塔。怪物和防御塔进行的攻击以您可以看到飞来飞去的红色和绿色立方体来表示。这不仅是对寻路的测试，也是对攻击优先级的测试。我们可以命令敌人首先攻击玩家、能量结构、防御或其他建筑物。玩家是这里的重中之重，但如果有什么阻碍，它也会被摧毁。<br><br><div align="center">
<img id="aimg_1021511" aid="1021511" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092142p7nu8na0ruhxw66n.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092142p7nu8na0ruhxw66n.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092142p7nu8na0ruhxw66n.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">《银河破裂者》中众多史诗战斗的第一场</font></font></div>
<br>
到目前为止，我们向您展示的所有内容的规模都非常小。我们并不满足。我们希望您在玩《银河破裂者》时能感受到玩星河战队的感觉——一次有成千上万的敌人的进攻。我们设置这个场景是为了检查各种类型的生物在地图上的各自位置生成时的行为。红色立方体代表将它们推开的流场，这是解决碰撞问题的一种非常快速的方法。他们都有一个共同的目标——摧毁人类基地。一路上，这些组合不可避免地会相遇——让我们看看会发生什么。<br><br><div align="center">
<img id="aimg_1021512" aid="1021512" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092142wbbx6d0i07dvbcp7.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092142wbbx6d0i07dvbcp7.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092142wbbx6d0i07dvbcp7.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">尽管起点不同，但这些生物在前往共同目标的途中融合在一起</font></font></div>
<br>
尽管单位受到悬崖和深坑地形障碍的限制，但各群体仍设法融合在一起，不会阻碍彼此到达目标的道路。当他们遇到严重的瓶颈时，他们仍然摇摆不定，试图将自己定位到最好的状态。这就是最终使外星部落变得既可怕又美丽的原因——模拟一群活的有机体，而不是机器人，一个个排队等着穿过通道。<br><br><div align="center">
<img id="aimg_1021513" aid="1021513" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092142ro0mss9ddlmbehmb.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092142ro0mss9ddlmbehmb.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092142ro0mss9ddlmbehmb.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">更新模型和动画后，一切都开始有模有样</font></font></div>
<br>
即使一切正常，但还是少了一样东西。如何达到《星际争霸》那样酷炫的单位运动水平？在那款游戏中，一切都如此顺畅和快速，没有移动延迟。我们尝试了很多东西。祈祷，看电视，看漫画书。你猜怎么着，这对我们没有多大帮助（哭脸）但是有一天，我们的程序员在和他小儿子玩耍时找到了一个解决方案。他们把小球放在桶里摇晃。每一次，球都填满了桶中的空隙。是什么神奇力量促成的呢？答案是——重力。通过将每个生物独特的重力与非常简单的软体模拟相结合，我们终于得到了类似于星际争霸的移动效果。添加了适当的外观和动画后，这突然看起来像个游戏了！<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1021514" aid="1021514" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092142twrumo5w5kzznkkw.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092142twrumo5w5kzznkkw.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092142twrumo5w5kzznkkw.gif" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">生物拼命地试图到达中间的机甲</font></font></div>
<br>
我们之前提到过，让生物以可信的方式行事对我们来说很重要。我们最不想让玩家看到的就是一群狂暴的太空犬仅仅因为暂时找不到到达目标的方法，而站在地面上什么也不做。这对我们来说还不够狂暴。取而代之的是，这些生物在目标周围聚集，填补空白，表现得像被蜂巢控制一样。只有一个目标，并且必须通过任何必要的手段实现。说实话，这看起来像一个活生生的细胞！<br><br>
基地的虫害。小型 Quelvers（甲壳动物）和其他单位一样，被这套系统控制。我们用于处理《银河破裂者》中单位行为的系统既可以支持攻击性生物，也可以支持中立生物。我们的计划是在游戏发生的星球 Galatea 37 中填充各种“环境”生物。他们的工作非常简单——只是过着普通的一天，寻找食物和水，从一个地方搬到另一个地方。这一切背后的原因是让世界更加身临其境和自然。Quelver 就是这样的一种生物——一种小小的清道夫，在大多数 Galatea 生物群落中掠过地面。<br><br><div align="center">
<img id="aimg_1021515" aid="1021515" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092143vvbi7gmmvqlllctv.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092143vvbi7gmmvqlllctv.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092143vvbi7gmmvqlllctv.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">幸运的是，Quelvers 害怕玩家和他们的行为，所以很容易摆脱他们</font></font></div>
<br>
Quelvers 的动作由与其他单位相同的 AI 系统控制。为了不对 CPU 造成太大压力，这些生物只出现在战斗之外。如果游戏检测到“进攻性”模式中的单位数量阈值已被超过，Quelvers 将立即停止生成。这并不是这些生物的唯一性能优化。游戏会检查 Quelvers 的位置，并仅在设定半径之外生成它们，以避免它们聚集在一起。在这个游戏中没有虫群喷泉。不过如果你真的想的话还是有可能的......<br><br>
这些虫子在 Galatea 37 的食物链中扮演着重要的角色，负责清理遗骸。<br><br>
这些家伙也使用与侵略性单位相同的分组机制，但原因略有不同。他们在尸体周围成群结队，而《银河破裂者》中战斗波次后有非常多的尸体。一旦战斗结束并且侵略性生物数量再次低于阈值，Quelvers 将再次开始产卵并寻找可以啃食的尸体。经过一段时间后，我们溶解了尸体，但是虫子的加入使它们看起来好像真的吃了尸体。<br><br><div align="center">
<img id="aimg_1021516" aid="1021516" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092143sz9qddmqqkackal3.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092143sz9qddmqqkackal3.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092143sz9qddmqqkackal3.gif" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">这些生物在追逐玩家时会尽力避开障碍物</font></font></div>
<br>
最后，是时候推出杀手锏了。在开发复杂系统和算法一年后，在写了数千行代码，喝了无数杯咖啡之后，我们搞定了数千个单位。话不多说，看图片你就懂了。<br><br><div align="center">
<img id="aimg_1021517" aid="1021517" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092143dwcjp6eevv6jicpt.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092143dwcjp6eevv6jicpt.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092143dwcjp6eevv6jicpt.gif" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1021518" aid="1021518" zoomfile="https://di.699h5.com/attachment/forum/202111/16/092146gy3e3is3xwoszb11.gif" data-original="https://di.699h5.com/attachment/forum/202111/16/092146gy3e3is3xwoszb11.gif" width="320" inpost="1" src="https://di.699h5.com/attachment/forum/202111/16/092146gy3e3is3xwoszb11.gif" referrerpolicy="no-referrer">
</div>
<br><font size="2"><font color="#808080"></font></font><br><br>
</td></tr></tbody></table>


  
</div>
            