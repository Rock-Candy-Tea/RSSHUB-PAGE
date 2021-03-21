
---
title: GDC演讲翻译——看门狗2的载具同步
categories: 
    - 游戏
    - GameRes 游资网 - 列表
author: GameRes 游资网 - 列表
comments: false
date: Tue, 02 Mar 2021 00:00:00 GMT
thumbnail: https://di.gameres.com/attachment/forum/202103/02/132355v172otmmjxtox7zx.jpg
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2487026">
在《网络同步在游戏历史上的发展变化（五）——物理同步》一文中，我们提到了游戏看门狗2的物理同步策略，但是由于篇幅问题略过了不少技术细节。在这一篇文章中，我们会对该GDC演讲《Replicating Chaos: Vehicle Replication in Watch Dogs 2》做详细的翻译与梳理。<br>
<br>
文章转自Funny David的知乎专栏（文末可点击原文链接查看），我根据自身理解对部分内容做了调整和优化。之前腾讯游戏团队也出过一篇讲物理载具的文章《手游中载具物理同步的实现方案》，基本的实现方式也是参考这个GDC分享。<br>
<br>
<font size="2"><font color="#808080">下面是视频链接，长按图片识别二维码打开</font></font><br>
<br>
<div align="center">
<img id="aimg_962770" aid="962770" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132355v172otmmjxtox7zx.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132355v172otmmjxtox7zx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132355v172otmmjxtox7zx.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">以下是GDC演讲分享的具体内容：</font></strong><br>
<br>
<div align="center">
<img id="aimg_962771" aid="962771" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132356kkss537eu5fkfnd3.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132356kkss537eu5fkfnd3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132356kkss537eu5fkfnd3.jpg" referrerpolicy="no-referrer">
</div><br>
这是在GDC 2017上的一篇关于《看门狗2》中车辆系统同步的分享。<br>
<br>
<div align="center">
<img id="aimg_962772" aid="962772" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132356etljlju2t475ft0l.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132356etljlju2t475ft0l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132356etljlju2t475ft0l.jpg" referrerpolicy="no-referrer">
</div><br>
上来先放了一段视频，描述Watch Dogs 2里“混乱”的车辆碰撞情况。(0:19)<br>
<br>
<div align="center">
<img id="aimg_962773" aid="962773" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132356cst9nd11mqydbxam.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132356cst9nd11mqydbxam.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132356cst9nd11mqydbxam.jpg" referrerpolicy="no-referrer">
</div><br>
然后讲了一下网络架构：没有中心服务器的P2P形式（状态同步），支持4个玩家，有很多实体要去同步，而且这些实体属于不同的分布式所有者。<br>
<br>
文章中本地（Master）和复制方（replica）都是针对某个对象而言的。<br>
<br>
假如有两个客户端，玩家A控制小车1，玩家B控制小车2。小车1在玩家A的客户端上就是主控的，小车2在玩家A的客户端上就是模拟的。同理，小车2在B客户端上就是主控的，小车1在B客户端上就是模拟的。<br>
<br>
<div align="center">
<img id="aimg_962774" aid="962774" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132356hvepdz60w69pwm0j.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132356hvepdz60w69pwm0j.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132356hvepdz60w69pwm0j.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">一、载具同步的难点分析</font></strong><br>
<br>
<div align="center">
<img id="aimg_962775" aid="962775" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132356beb4b1zbz7xn2a4n.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132356beb4b1zbz7xn2a4n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132356beb4b1zbz7xn2a4n.jpg" referrerpolicy="no-referrer">
</div><br>
讲车辆同步的困难<br>
<br>
<ul><li>移动速度快，100ms的网络延迟就意味着2-3米的差异</li><li>存在碰撞，看门狗2的开放世界中有大量的交通工具，不仅限于玩家之间</li><li>人眼对于不规则的速度很敏感<br>
</li></ul><br>
<div align="center">
<img id="aimg_962776" aid="962776" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132357pj4dacpd0rdfkjnc.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132357pj4dacpd0rdfkjnc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132357pj4dacpd0rdfkjnc.jpg" referrerpolicy="no-referrer">
</div><br>
涵盖内容：<br>
<br>
<ul><li>轨迹调试工具</li><li>标准的技术：投影速度混合（有小调整）</li><li>基于快照缓存的外插值和/或内插值</li><li>混合物理模拟来处理碰撞</li><li>未解决问题</li><li>未来研究方向<br>
</li></ul><br>
<strong><font color="#de5650">二、轨迹调试工具</font></strong><br>
<br>
<div align="center">
<img id="aimg_962777" aid="962777" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132357cr6dh3dd3afe6fro.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132357cr6dh3dd3afe6fro.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132357cr6dh3dd3afe6fro.jpg" referrerpolicy="no-referrer">
</div><br>
轨迹调试工具是most important thing，所以放前面讲，通过调试工具可以看到物体移动的位置信息。<br>
<br>
绿色的轨迹是车辆经过的真实路径，蓝色的是通过dead reckoning（外插值）预测的路径，红色的点是做同步的快照点（即从主控端Master同步过来的准确位置）。<br>
<br>
<div align="center">
<img id="aimg_962778" aid="962778" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132357yppqzif0epae3pff.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132357yppqzif0epae3pff.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132357yppqzif0epae3pff.jpg" referrerpolicy="no-referrer">
</div><strong><font color="#de5650">三、投影速度混合技术</font></strong><br>
<br>
接着讲最为标准的做法，就是投影速度混合（Projective Velocity Blending）。分享者说这个公式来自于wikipedia，追溯了下，最终来源是《Game Engine Gems 2》（游戏引擎精粹）这本书中的一篇文章《Believable Dead Reckoning for Networked Games 》。<br>
<br>
首先大前提是使用航位推测（Dead reckoning）法来做位置的同步预测：<br>
<br>
航位推测法（英语：Dead reckoning，缩写：DR）是一种利用现在物体位置及速度推定未来位置方向的航海技术，现已应用至许多交通技术层面，但容易受到误差累积的影响。英语中“Dead”是从“deduced（推导）”转化而来。这里就理解成位置预测就行。<br>
<br>
然后一个运动学状态会（对应这里的快照）包含位置、速度、加速度、朝向和角速度。最简单的解决方案是基于线性物理的模拟：<br>
<br>
<div align="center">
<img id="aimg_962779" aid="962779" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132357blj5jqnouwj1up7p.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132357blj5jqnouwj1up7p.jpg" width="300" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132357blj5jqnouwj1up7p.jpg" referrerpolicy="no-referrer">
</div><br>
这是高中物理的知识，但这里有一个问题就是我们有两个运动学状态，当前模拟的位置和最近收到的真实位置。一种解决方法是通过在这两个状态之间创建一条曲线来进行模拟，另外一个技术就是分享者选择的投影速度混合。<br>
<br>
P0表示车辆所在位置，V0表示当前的速度，P0‘是上一个运动学状态的位置，V0'是上一个运行学状态的速度，Tt表示从T0开始经历过的时间长度，而头顶带个尖的T表示归一化之后的比例，即它是一个0-1之间的值。<br>
<br>
<div align="center">
<img id="aimg_962780" aid="962780" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132358xw30bsxwkriupc8s.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132358xw30bsxwkriupc8s.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132358xw30bsxwkriupc8s.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_962781" aid="962781" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132358uhhq0rqjw6hzjrb2.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132358uhhq0rqjw6hzjrb2.jpg" width="461" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132358uhhq0rqjw6hzjrb2.jpg" referrerpolicy="no-referrer">
</div><br>
这样这里的几个公式就比较清晰了，先对速度做融合，然后使用融合后的速度计算位置Pt，注意这里已经在使用A0'的加速了，接着计算根据收到的运动学状态预算一个位置，最后根据归一化之后的时间比例对两个位置做差值融合。<br>
<br>
跑出来的结果是这样的：<br>
<br>
<div align="center">
<img id="aimg_962782" aid="962782" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132358vvn6gs3341nsqs6n.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132358vvn6gs3341nsqs6n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132358vvn6gs3341nsqs6n.jpg" referrerpolicy="no-referrer">
</div><br>
可以看出，绿色的原始轨迹是一个圆形，而蓝色的根据快照数据预测的结果是带有比较强的锯齿状的，通过视频可以看出车呈现出了很强烈的抖动。（5:30）<br>
<br>
<div align="center">
<img id="aimg_962783" aid="962783" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132358j0vfazafvt0otfof.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132358j0vfazafvt0otfof.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132358j0vfazafvt0otfof.jpg" referrerpolicy="no-referrer">
</div><br>
接着就讲twist（转弯）的内容了：<br>
<br>
<ul><li>对正在转弯的车辆使用直线进行外插值是不理想的；</li><li>添加了方向盘（或者说车轮）角度信息<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>但是车辆的物理模拟很复杂</li><li>无法依据方向盘的角度准确预测转向轨迹，因为虽然方向盘角度给出了车辆未来运行的方向，但是在物理世界中速度、地表材质等等因素都会影响结果。<br>
</li></ul><br>
<ul><li>传输了车辆的位置、速度和角速度<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>使用角速度中的水平朝向（yaw）值来预测转向</li><li>对于漂移的车辆不管用，但是对于Watch Dog 2来说并不是个问题（因为不是个赛车游戏=_=）<br>
</li></ul><br>
<div align="center">
<img id="aimg_962784" aid="962784" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132358sfvld5h4p4dxfo54.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132358sfvld5h4p4dxfo54.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132358sfvld5h4p4dxfo54.jpg" referrerpolicy="no-referrer">
</div><br>
这样就很圆了……(7:45)<br>
<br>
<strong><font color="#de5650">四、基于快照缓存的外插值和/或内插值?</font></strong><br>
<br>
<div align="center">
<img id="aimg_962785" aid="962785" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132359dv73zm33f6mtpbvs.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132359dv73zm33f6mtpbvs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132359dv73zm33f6mtpbvs.jpg" referrerpolicy="no-referrer">
</div><br>
接着说快照缓存的使用部分：(8:53)<br>
<br>
<ul><li>在最近的两个快照中做内插值的做法</li><li>优势是轨迹精准（因为等待主控的权威数据到来后才插值模拟）</li><li>劣势是渲染对象轨迹其实是在模拟一段时间之前的状态，比如图中渲染的就是晚了5帧之前的状态<br>
</li></ul><br>
<div align="center">
<img id="aimg_962786" aid="962786" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132359yf3rxr3lt1pls33o.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132359yf3rxr3lt1pls33o.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132359yf3rxr3lt1pls33o.jpg" referrerpolicy="no-referrer">
</div><br>
这会带来“在不同客户端上因为位置不一致而导致结果不同”（A客户端上发生了碰撞，但是B客户端上没有发生碰撞），所以下面要解决这个问题。<br>
<br>
<div align="center">
<img id="aimg_962787" aid="962787" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132359qnngyyysiq2lxzzs.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132359qnngyyysiq2lxzzs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132359qnngyyysiq2lxzzs.jpg" referrerpolicy="no-referrer">
</div><br>
外插值和内插值的对比<br>
<br>
<ul><li>我们不是一定要完全使用内插值<br>
</li></ul><br>
依然可以从上一个收到的快照进行外插值<br>
<br>
<ul><li>引入一个“时间偏移”（TimeOffset）<br>
</li></ul><br>
<br>
<ul type="1" class="litype_1"><li>我们渲染出来的这辆车在时间上晚了多久</li><li>检查 当前时间 - 时间偏移</li><li>如果这个插值落在了两个已经收到的快照时间之间的话，使用内插值</li><li>如果比最后收到的一个快照还要晚的话，使用外插值</li><li>快照要带时间戳<br>
</li></ul><br>
<br>
<div align="center">
<img id="aimg_962788" aid="962788" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132400x9sojw5jx8izwz5y.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132400x9sojw5jx8izwz5y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132400x9sojw5jx8izwz5y.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_962789" aid="962789" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132400ejfonm9momphytff.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132400ejfonm9momphytff.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132400ejfonm9momphytff.jpg" referrerpolicy="no-referrer">
</div><br>
这里用视频讲解了具体效果，最好直接看视频更直观。(11:01)<br>
<br>
<div align="center">
<img id="aimg_962790" aid="962790" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132401vl9hp55arrsrtrrr.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132401vl9hp55arrsrtrrr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132401vl9hp55arrsrtrrr.jpg" referrerpolicy="no-referrer">
</div><br>
时间偏移相关<br>
<ul><li>选择不是一件容易的事情<br>
</li></ul><ul type="1" class="litype_1"><li>太多内插值导致错误的碰撞</li><li>太多外插值导致轨迹不连续</li><li>要找平衡<br>
</li></ul><br>
<ul><li>使用 平均度量延迟 + 常量值<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>减震</li><li>最多300ms</li><li>常量值范围在100ms-200ms的区间<br>
</li></ul><br>
根据车辆速度成比例改变，当车辆以较慢的速度运行的时候，错失碰撞的概率比较小，因此可以尽量使用内插值来做，这时候对应的就是增大时间偏移的值。<br>
<br>
<strong><font color="#de5650">五、混合物理模拟来处理碰撞</font></strong><br>
<br>
<div align="center">
<img id="aimg_962791" aid="962791" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132401p7o4fbplu4gc4j5q.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132401p7o4fbplu4gc4j5q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132401p7o4fbplu4gc4j5q.jpg" referrerpolicy="no-referrer">
</div><br>
这样下来航位推测出来的轨迹就看着不错了，现在我们让车相撞看看<br>
<br>
<div align="center">
<img id="aimg_962792" aid="962792" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132401c9ts1o9zldl91nd1.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132401c9ts1o9zldl91nd1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132401c9ts1o9zldl91nd1.jpg" referrerpolicy="no-referrer">
</div><br>
看视频，车辆在相撞的时候会互相向后退，这和我们预期的不太一样。(13:22)<br>
<br>
<div align="center">
<img id="aimg_962793" aid="962793" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132401d14j8xt48a4s0a4x.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132401d14j8xt48a4s0a4x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132401d14j8xt48a4s0a4x.jpg" referrerpolicy="no-referrer">
</div><br>
相撞的车应当都停住，或者把对方推开的力量更小一些。但是游戏里面，两边的车辆都推到很远的位置。<br>
<br>
借助网络工具帮助我们逐帧来看发生了什么。<br>
<br>
<div align="center">
<img id="aimg_962794" aid="962794" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132401hqg4gk1qz8fzwfnb.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132401hqg4gk1qz8fzwfnb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132401hqg4gk1qz8fzwfnb.jpg" referrerpolicy="no-referrer">
</div><br>
这里是一段逐帧视频，白色的车在这里是第三方，它在黑车的客户端上发生碰撞之后，因为它自身没有开ragdoll（但其实有碰撞体），要等在它自己所在的客户端把碰撞之后的位置数据同步过来之后才会后退（这个时候还处于外插值的状态），于是它继续往前走，就把当前客户端用物理模拟（开了ragdoll）的那辆车给推到更远的位置去了。在白车自己的客户端上，黑车也有同样的行为，因此两辆车都产生了更大的碰撞后退效果，而实际上两个车相撞不应该产生如此大的位移。(14:30)<br>
<br>
<div align="center">
<img id="aimg_962795" aid="962795" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132402ilxs4okxrx6suvxv.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132402ilxs4okxrx6suvxv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132402ilxs4okxrx6suvxv.jpg" referrerpolicy="no-referrer">
</div><br>
如何解决？<br>
<br>
<ul><li>把你推开的复制方（replica）并不知道碰撞的发生<br>
</li></ul><br>
他会保持前进的状态直到一个新的包到达<br>
<br>
<ul><li>这是一个无解的问题<br>
</li></ul><br>
因为没有人有碰撞的完整决定权（因为网络框架是P2P的）<br>
<br>
<ul><li>这时候很希望有个权威服务器……<br>
</li></ul><br>
<div align="center">
<img id="aimg_962796" aid="962796" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132402dbbpvipikrc222i1.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132402dbbpvipikrc222i1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132402dbbpvipikrc222i1.jpg" referrerpolicy="no-referrer">
</div><br>
但是问题还是要处理，这时候就引入了物理模拟融合（Physics Simulation Blending），即在发生碰撞前打开其他车的物理模拟（打开ragdoll），然后在模拟位置与快照发送的位置之间进行blend<br>
<br>
<ul><li>无论我们是否喜欢，碰撞总会发生</li><li>给本地物理一个机会来模拟碰撞</li><li>然后融合回航位推测得出的轨迹</li><li>需要调校两种速度之间的融合参数：<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>一种速度来自刚体模拟</li><li>一种速度要达到航位推测得到的位置<br>
</li></ul><br>
<ul><li>表现本地可信的一些效果，然后将碰撞考虑在内的情况下融合进快照。<br>
</li></ul><br>
关于Blend方案的问题：文中提到的"Physics Simulation Blending"是用本地模拟的与服务器快照进行混合。而本地计算是先行的，收到的服务器快照皆是过去的位置，所以混合的并不是同一时刻的位置，所以理论上可能会有一些不正常的情况（而且无法预测）。这里的例子都是汽车相撞然后一段时间内趋于静止，所以通常情况下没什么问题。<br>
<br>
<div align="center">
<img id="aimg_962797" aid="962797" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132402h45fcb24n745w82m.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132402h45fcb24n745w82m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132402h45fcb24n745w82m.jpg" referrerpolicy="no-referrer">
</div><br>
融合参数调整（不同阶段调整物理模拟以及快照位置的权重）<br>
<br>
<ul><li>通过播放多次碰撞选择看上去表现好的融合参数，包括<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>在碰撞发生时融合比例的最大值</li><li>在结束之后以多快的速度回到完全的航位推测算法中<br>
</li></ul><br>
图中展现了对于自行车和汽车，恢复的时间长度是不同的，其中汽车较重，相对需要更长的时间。<br>
<br>
<div align="center">
<img id="aimg_962798" aid="962798" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132402xwex3bi67i6wc0dx.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132402xwex3bi67i6wc0dx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132402xwex3bi67i6wc0dx.jpg" referrerpolicy="no-referrer">
</div><br>
效果已经不错了哦，这块要看视频。虽然不完美，还是会有一些推开的情况，但是没有之前那么远了。(19:10)<br>
<br>
<div align="center">
<img id="aimg_962799" aid="962799" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132402uwt26wa9fttf269t.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132402uwt26wa9fttf269t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132402uwt26wa9fttf269t.jpg" referrerpolicy="no-referrer">
</div><br>
接下来说说进一步可能发生的问题——碰撞结果的不可预测性<br>
<br>
<ul><li>本地模拟的碰撞在不同的客户端上结果可能不同，比如两辆车相撞，在两个客户端上一个可能被撞到了左侧，一个被撞到了右侧。</li><li>将复制品从本地碰撞模拟融合回航位推测轨迹的时候可能会比较“震撼”，来回抖动</li><li>使用的优化方法是当碰撞开始的时候，尽量将车辆放置到他们主机所在的位置<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>让它们更可能得到一致的碰撞结果<br>
</li></ul><br>
<br>
其实由于看门狗2采用的带有预测的状态同步，所以误差是无法避免的，在物理模拟的参与下更难保证一致性，只能通过快照来纠正错误信息<br>
<br>
<div align="center">
<img id="aimg_962800" aid="962800" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132403gtllflhhuikff6l9.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132403gtllflhhuikff6l9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132403gtllflhhuikff6l9.jpg" referrerpolicy="no-referrer">
</div><br>
如何做到让在碰撞发生时将车辆放置到他们主机所在的位置呢？这里就要做碰撞预测了。<br>
<br>
<ul><li>在如下几种情况会预测即将发生的碰撞并做外插值（通过调小时间偏移那个值）<br>
</li></ul><br>
<br>
<ul type="1" class="litype_1"><li>不太能够避开的情况，车辆要转向毕竟是需要一个时间的，当两辆车距离太过接近的时候，通过射线检测之类的方式（我猜）来预测碰撞是否很可能要发生了。貌似这种效果并不是非常好，但是有任何一点可以改善的点都值得做。</li><li>使用AI系统中已经存在的碰撞预测算法，这里没讲算法细节。<br>
</li></ul><br>
<strong><font color="#de5650">六、未解决的同步问题</font></strong><br>
<br>
<div align="center">
<img id="aimg_962801" aid="962801" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132403furbb47774yo724r.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132403furbb47774yo724r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132403furbb47774yo724r.jpg" referrerpolicy="no-referrer">
</div><br>
一些没解决的问题，其实有更多，这里只列举一部分。<br>
<br>
<ul><li>和静态网格的碰撞</li><li>时间偏移差异</li><li>恐怖谷效应<br>
</li></ul><br>
<div align="center">
<img id="aimg_962802" aid="962802" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132403lv1oo17xzyuuyvdw.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132403lv1oo17xzyuuyvdw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132403lv1oo17xzyuuyvdw.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_962803" aid="962803" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132404ejajnhh1zshh8lb0.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132404ejajnhh1zshh8lb0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132404ejajnhh1zshh8lb0.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>静态碰撞的问题：</strong><br>
<br>
这块看视频更直观，真正的快照目标点在树的左侧，而碰撞模拟到了右侧，由于中间有一颗树的遮挡，这时候需要融合过来就很奇怪。（视频中可以看到剧烈的抖动，火花四射，然后一点点滑过去）(22:35)<br>
<br>
<ul><li>静态物体不会让路</li><li>树是最坏的一种情况</li><li>一些选择：<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>保持当前位置</li><li>软物理碰撞</li><li>最终直接传送，虽然效果不好，但是在一些特定情况下还是需要的。<br>
</li></ul><br>
<ul><li>消除抖动是最为重要的部分<br>
</li></ul><br>
<br>
他们最终的做法是如果发现你被挡住了，但是又无法移动到目标位置，就让你保持当前位置的，等有之后新的位置同步之后再处理。<br>
<br>
<div align="center">
<img id="aimg_962804" aid="962804" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132404jlxuze16115kdugj.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132404jlxuze16115kdugj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132404jlxuze16115kdugj.jpg" referrerpolicy="no-referrer">
</div><br>
不同的时间偏移：<br>
<br>
<ul><li>人物角色比较倾向于内插值（速度慢）<br>
</li></ul><br>
不同的时间偏移导致了在不同客户端上的碰撞效果不同，左侧的图车完全没碰到人，右侧的把人撞飞了。分享者说这块可以基于前面碰撞预测的同样思路来解决或者优化<br>
<br>
<ul><li>对于可破坏物有同样的问题，但是对于玩法的影响比较小。<br>
</li></ul><br>
<div align="center">
<img id="aimg_962805" aid="962805" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132404x1qqpiiezp41dcpw.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132404x1qqpiiezp41dcpw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132404x1qqpiiezp41dcpw.jpg" referrerpolicy="no-referrer">
</div><br>
恐怖谷效应：<br>
<br>
<ul><li>运动轨迹已经正确了，但是依然感觉不好<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>轻微的摇摆效果在复制方（远端）丢失了</li><li>车不能围着它们的重心旋转</li><li>人眼对于甚至很微小的不连贯现象都很敏感<br>
</li></ul><br>
<ul><li>应用一些后处理平滑<br>
</li></ul><br>
<ul type="1" class="litype_1"><li>平滑速度和角速度，而不是位置和旋转</li><li>需要和投影速度融合共存，它在航位预测之上，因为航位预测法虽然希望给出一个平滑的曲线过渡，但是在实际结果中可能并不是这样，还是会有位置和速度上的突变。虽然加这个有点脏，但是效果好，管他呢。=_=<br>
</li></ul><br>
<div align="center">
<img id="aimg_962806" aid="962806" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132404rrjphvmnrp32d3m5.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132404rrjphvmnrp32d3m5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132404rrjphvmnrp32d3m5.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">七、未来的研究方向</font></strong><br>
<br>
<ul><li>调参数太难了，希望用机器学习的方法让AI来调</li><li>平滑算法<br>
</li></ul><br>
<br>
卡尔曼滤波（Kalman filter）<br>
<br>
卡尔曼滤波（Kalman filter）是一种高效的自回归滤波器，它能在存在诸多不确定性情况的组合信息中估计动态系统的状态，是一种强大的、通用性极强的工具。<br>
<br>
https://zhuanlan.zhihu.com/p/39912633<br>
<br>
<div align="center">
<img id="aimg_962807" aid="962807" zoomfile="https://di.gameres.com/attachment/forum/202103/02/132404i9hviiun8g82rkni.jpg" data-original="https://di.gameres.com/attachment/forum/202103/02/132404i9hviiun8g82rkni.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/132404i9hviiun8g82rkni.jpg" referrerpolicy="no-referrer">
</div><br>
最后强调调试器的重要性，然后说虽然在这个过程中做了很多数学工作，是科学性的，但是依然有很多内容是需要从艺术/美术的视角去思考和改进的，毕竟要做到的最终结果是让玩家feeling good。（其实这个调试器本质是一个回放工具，需要把每一帧当前所有的对象位置以及行为信息都记录下来，方便后面做调试）<br>
<br>
<strong><font color="#de5650">八、问答</font></strong><br>
<br>
问题：第一个问题关于timehop（跳时）的，如果某辆汽车在运行时切换了控制权（比如玩家A中途掉线，AI计算由客户端A切换到客户端B）如何处理这个跳时造成的问题？<br>
<br>
回答：这个时候一般你会知道当前的汽车运行情况，比如车是沿着直线开的时候，就减速等着新的控制端计算位置逐渐追上去。<br>
<br>
问题：车辆在爬坡之类的情况下的颠簸在同步方怎么表现，会限制外插值在一个平面么？<br>
<br>
回答：一个解决方案是用物理模拟Z轴的变化，然后在车离地面比较近的情况下Z方向上不要外插值，但是比如飞跃到空中的时候还是需要切换到航位预测法来预测落点位置。<br>
<br>
问题：似乎是在讨论是否有必要区分不同的物理对象，决定是否使用物理或者调整同步方式？<br>
<br>
回答：其实在游戏里面是有区分的，比如自行车和汽车的物理模拟融合时的权重计算曲线不同。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：游戏开发那些事</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/WMLWEVnBwWVaGwwP1mH8XA</font></font><br>
</td></tr></tbody></table>



  
</div>
            