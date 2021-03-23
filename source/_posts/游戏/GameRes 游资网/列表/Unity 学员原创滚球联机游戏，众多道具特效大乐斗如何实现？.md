
---
title: 'Unity 学员原创滚球联机游戏，众多道具特效大乐斗如何实现？'
categories: 
    - 游戏
    - GameRes 游资网
    - 列表

author: GameRes 游资网
comments: false
date: Tue, 02 Mar 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202103/02/131442b886v4tm5n4init4.gif'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2487023">
Hi，这里是小U。<br>
<br>
话说在刚刚过去的春节假期中，各类联机的游戏热度有增无减，毕竟亲朋好友聚在一起，除了看看电视聊聊天，一起打打游戏也是一个不错的选择。<br>
<br>
《Over-hitting》就是这样一款可以联网的派对游戏。<br>
<br>
这款由 Unity 大学三期学员原创的游戏可支持多位玩家联机对战。每个玩家需要现在准备室里挑选代表自己人物的颜色，然后点击准备进行匹配，就像现在的大多数联机手游一样，需要所有的玩家准备完成后，进入竞技房间。<br>
<br>
<div align="center">
<img id="aimg_962761" aid="962761" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131442b886v4tm5n4init4.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131442b886v4tm5n4init4.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131442b886v4tm5n4init4.gif" referrerpolicy="no-referrer">
</div><br>
玩家需要推动手中的道具球，在有限的时间内，获得更多的分数，分数越高球的体积就越大，游戏开场时有一个争夺皇冠的环节先抢到地图中央皇冠的玩家，可以获得一定的分数优势。<br>
<br>
<div align="center">
<img id="aimg_962762" aid="962762" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131443gh8z718e6vnhqei6.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131443gh8z718e6vnhqei6.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131443gh8z718e6vnhqei6.gif" referrerpolicy="no-referrer">
</div><br>
雪场内有着不同的机关和障碍物，触碰他们会产生不同的效果，比如雪地中的加速器可以增加雪球的速度，雪场边缘的跳板可以把雪球重新弹回雪场的中心地带，雪地中的圣诞树则是让雪球减小体积的障碍物，玩家需要避免触碰到它。<br>
<br>
<div align="center">
<img id="aimg_962763" aid="962763" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131445juag70gbot7puuep.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131445juag70gbot7puuep.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131445juag70gbot7puuep.gif" referrerpolicy="no-referrer">
</div><br>
雪场中还有许多不同颜色的礼盒，礼盒中有很多意想不到功能的道具。玩家可以通过撞击礼盒，获得道具，收获不同的 BUFF 效果，比如火焰道具，可以让雪球加速，获得伐木工道具的雪球，可以获得一定时间通过砍树加分，有的道具则可以让玩家直接加分。<br>
<br>
<div align="center">
<img id="aimg_962764" aid="962764" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131446gj3xujdj4u3cdzgu.png" data-original="https://di.gameres.com/attachment/forum/202103/02/131446gj3xujdj4u3cdzgu.png" width="480" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131446gj3xujdj4u3cdzgu.png" referrerpolicy="no-referrer">
</div><br>
另外玩家还可以通过撞击别的玩家的后背偷得一定的分数，但是玩家又要注意避免与体积更大的雪球正面相撞，因为对方能把你的雪球变小。<br>
<br>
有限的空间，众多道具效果，这款拥有简单玩法的《Over-hitting》刺激程度堪比 switch 上的《马里奥赛车》，而且这款游戏支持手柄、键盘、触摸屏三种方式，意味着它有着兼容多个平台游戏联机的潜能。<br>
<br>
当然从游戏机制的角度来看，《Over-hitting》是一款并不复杂的多人竞技游戏，但实际上开发团队在制作这一款游戏的时候依旧遇到了一些问题。<br>
<br>
在李同学的策划中，丰富多样的道具是《Over-hitting》的一个亮点。比如火焰道具，比如伐木工道具。但如何高效地作出各种道具效果呢？负责道具效果制作的李同学在和 Unity 大学的导师及同学交流之后，最终开发者给道具做了一系列的基础效果的代码。<br>
<br>
<div align="center">
<img id="aimg_962765" aid="962765" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131448yono68hqhh7ztawm.png" data-original="https://di.gameres.com/attachment/forum/202103/02/131448yono68hqhh7ztawm.png" width="480" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131448yono68hqhh7ztawm.png" referrerpolicy="no-referrer">
</div><br>
比如突然变大，或者变异，或者加快速度，策划可以通过输入不同的参数，来进行组合，这样方便策划去组装做出各种效果不同的道具。<br>
<br>
作为《Over-hitting》玩法中的重要一环，雪球之间的碰撞效果也是《Over-hitting》需要考虑的因素，游戏中，涉及到不同形式的雪球碰撞，而且每种雪球碰撞的形式都会产生不同的物理效果，有的会让对方雪球的体积较小，有的则不变但能够减小对方的分数，制造这些效果，这就需要处理不同的雪球撞击逻辑。<br>
<br>
<div align="center">
<img id="aimg_962766" aid="962766" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131451gre9tbrqtey6uerj.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131451gre9tbrqtey6uerj.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131451gre9tbrqtey6uerj.gif" referrerpolicy="no-referrer">
</div><br>
编辑雪球逻辑的同学刚开始处理代码的时候比较随意，雪球发生碰撞的时候直接获取了对方的脚本来进行调动的办法，但是通过和负责网络功能的同学交流之后发现，游戏内和“我”发生碰撞的，只是对方玩家在我客户端内的一个分身，“我”对对方的处理并不会同步到（对方的本体）上面。<br>
<br>
所以这时候就需要改变一下处理的逻辑，改为“我”在背刺、或者被背刺、被侧击、或者发生对撞的时候，仅调动自己的这样一个方法，而不需要涉及调动到对方的网络。<br>
<br>
这个游戏还涉及到一个雪地数据的问题，玩家滚雪球之后会“吃”掉经过路径（位置）的雪，而这些“被吃掉的雪”，在一定时间后又需要自动恢复。<br>
<br>
罗同学在处理这一问题的时候，使用了一个二维数组来保存整个地图里的雪地的数据，然后每帧根据玩家的位置和体积，来查找相应的数组内，所对应的位置有“多少可以吃到的雪”。然后将“被吃掉的雪”加入到恢复列表里。<br>
<br>
<div align="center">
<img id="aimg_962767" aid="962767" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131452x5zoxzifqq5q807l.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131452x5zoxzifqq5q807l.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131452x5zoxzifqq5q807l.gif" referrerpolicy="no-referrer">
</div><br>
但这样一来就会遇到一个问题：原本的逻辑只能检测到玩家每帧所在的位置，但实际上当玩家速度过快的时候，每帧之间的位置可能会相差非常大，有的地方就会检测不到，检测不到的地方雪地的雪就会依旧保留，给人感觉非常卡顿。<br>
<br>
<div align="center">
<img id="aimg_962768" aid="962768" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131452c1cmxmm0lqulq95l.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131452c1cmxmm0lqulq95l.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131452c1cmxmm0lqulq95l.gif" referrerpolicy="no-referrer">
</div><br>
针对这一问题，开发者重新写了一个补帧的方法，记录上一帧的位置，连成一条线到当前的位置。这样既保证了游戏流畅的运行，也让游戏效果更贴近现实生活中的下雪场景。<br>
<br>
<div align="center">
<img id="aimg_962769" aid="962769" zoomfile="https://di.gameres.com/attachment/forum/202103/02/131452ofnxsushhuvju8ss.gif" data-original="https://di.gameres.com/attachment/forum/202103/02/131452ofnxsushhuvju8ss.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202103/02/131452ofnxsushhuvju8ss.gif" referrerpolicy="no-referrer">
</div><br>
说了那么多功能和机制，负责游戏策划的李同学在最后悄悄的告诉小 U，这些功能可能只是为《Over-hitting》里的雪地地图打造的，其实他们的游戏计划中有更多玩法，模型蓝本。比如他们想设计更多有着不同环境效果的地图，每种地图有着不同的地形，制造更多的凹陷和凸起，玩家可以利用地形的特点进行撞击，跳跃，防御。<br>
<br>
最终因为时间的原因，《Over-hitting》项目团队先完成了雪地地图的小 Demo，当然作为一款支持键盘、手柄、平板，等多个操作模式的联机游戏，《Over-hitting》的多平台跨界潜力不容小视，李同学表示：如果时间允许的话，《Over-hitting》团队会进一步完善游戏内容，添加更多玩法，或许在不久的将来，你能在安卓平台上和其他小伙伴来一场简单刺激的雪球大战呢！<br>
<br>
<font size="2"><font color="#808080">来源：Unity官方平台</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/RS4PuSk2tXdkC1-wYgwtLA</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            