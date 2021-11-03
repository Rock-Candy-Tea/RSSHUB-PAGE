
---
title: '_BIGC嘉宾说_——FunPlus首席特效专家张韶勇'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/22/181457oyzcz3ux82jzd5yw.jpg'
author: GameRes 游资网
comments: false
date: Fri, 22 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/22/181457oyzcz3ux82jzd5yw.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2517226">
<div align="center">
<img id="aimg_1016804" aid="1016804" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181457oyzcz3ux82jzd5yw.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181457oyzcz3ux82jzd5yw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181457oyzcz3ux82jzd5yw.jpg" referrerpolicy="no-referrer">
</div>
<br>
BIGC北京国际游戏创新大会每年9月底在北京举办，大会致力于打造游戏行业经验分享的平台，通过制作人、内容、技术、硬件、发行平台、商业营销等方向的经验分享，促进中国游戏产业健康向上发展。<br><br>
有些用于主机端的特效工具和插件可以和手游工具相结合，从而提高手游特效品质和制作效率。<br><br>
FunPlus首席特效专家张韶勇对此感受颇深。他拥有16年特效工作经验，此前在海外做主机游戏的特效，回国后曾在网易阿里等公司负责手游的特效，目前加入了FunPlus，负责美术特效的工作。<br><br>
在今年的北京国际游戏创新大会（BIGC）上，张韶勇分享了他对游戏特效技巧-像素动画制作的心得。不仅从美术角度思考如何在手游上呈现出更好的美术表现，还尝试引入主机端的开发技术，让冗杂的特效制作过程简化，到快速落地在手游中。<br><br>
在他看来，艺术挑战技术，技术启发艺术。新的技术和工具的出现，为艺术创作的实现带来新的可能性和便捷。数字艺术的创作常常受限于游戏开发所使用的引擎和插件。但是如果美术多一点对数学的理解，就会发现很多工具是相通的。<br><br>
一些在主机游戏中使用的技术可以消化，简化或局部地应用到手游开发中。比如 FluidNinjia 是在 Unreal engine 里使用的插件，但是它输出的序列帧流程图等资源可以在ASE中使用。这样我们就可以使用 Unreal Cascade，Niagara 粒子系统来设计特效需要的动态，通过 FluidNinjia 输出贴图资源。将其材质在ASE中简化重构。<br><br>
这样把跨平台的工具融会贯通地使用，极大扩展了特效的创作和实现的空间。这需要特效师对工具后面的数学多一点理解。<br><br><div align="center">
<img id="aimg_1016805" aid="1016805" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181457o976el3u5p17un1n.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181457o976el3u5p17un1n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181457o976el3u5p17un1n.jpg" referrerpolicy="no-referrer">
</div>
<br>
以下是通过整理的演讲实录：<br><br>
今天和大家分享的内容是：「像素动画的原理和应用」。我很想把它讲到就算外行也能弄懂。同时也通过这个案例，和大家分享一下美术岗位怎么用形象思维来解释数学。<br><br>
我做了16年的特效。之前在美国、加拿大做过《使命召唤》《暗黑血统》等主机游戏，回国之后先后在网易，阿里游戏，最后来到FunPlus，现在主要负责手游的项目。<br><br>
从主机游戏到手游转变，我本能地考虑怎么把一些主机的游戏技术应用到手游上面。其中的一个典型例子就是像素动画在手游上的应用。<br><br>
我是一名特效师，这个岗位也可以叫做特效动画师。动画师动的是角色的胳膊和腿，而特效师动的图片的像素，因为大多数时候，我们都是利用像素运动来模拟各种特效。<br><br>
比如这个《星空》。现在大家看到的是运动的数字版，它就代表了像素动画要呈现的效果。<br><br><div align="center">
<img id="aimg_1016806" aid="1016806" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181457s5lfizw2mbauwmvl.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181457s5lfizw2mbauwmvl.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181457s5lfizw2mbauwmvl.gif" referrerpolicy="no-referrer">
</div>
<br>
要实现这种效果并不难，最近有个叫Fluid Ninja的Unreal的插件，特效师可以应用Cascade，Niagara粒子系统，贴图，或者力场在其中模拟出我们想要的运动形式，产出流程图等贴图资源，然后再应用到Unity的ASE材质中。这个过程给了特效师设计像素动画的极大自由，而且十分便捷。<br><br><div align="center">
<img id="aimg_1016807" aid="1016807" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181458x3gjp4aixsiup6m6.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181458x3gjp4aixsiup6m6.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181458x3gjp4aixsiup6m6.gif" referrerpolicy="no-referrer">
</div>
<br>
我们先讲一下像素动画的基本原理：<br><br>
每一张图片其实都是由像素构成的。假如图片的分辨率是1024x1024，那么这1024个像素点都有其对应的坐标。<br><br>
我们可以用一张“流程图”来操纵一张图片像素坐标的运动方向和强度，以得到我们想要的运动形式。<br><br>
它涉及到两个最基本的概念：<br><br>
其一是平面坐标系，这个就是上下左右4个方向。<br><br>
其二，通道。我们的图片有百万种颜色都是由RGB三个不同的通道组合产生的。<br><br><div align="center">
<img id="aimg_1016808" aid="1016808" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181458c5zjqib36q5bxmii.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181458c5zjqib36q5bxmii.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181458c5zjqib36q5bxmii.jpg" referrerpolicy="no-referrer">
</div>
<br>
那么我们可以试着将他们合在一起：把红绿通道分别对应坐标系的X值和Y值，这样就可以把图片的「灰度」和坐标系的数值对应起来。<br><br><div align="center">
<img id="aimg_1016809" aid="1016809" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181458jj2yioxcoillxiol.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181458jj2yioxcoillxiol.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181458jj2yioxcoillxiol.jpg" referrerpolicy="no-referrer">
</div>
<br>
坐标系大家都很清楚。下图在坐标系中左下角是（0,0），右上角可以设为（1,1），这就是一张相片最基本的的坐标系。当然，电脑里的坐标有些不太一样，它是左上角（0,0），右下（1,1）。<br><br>
但是为了产生上下左右四个方向的运动，我们就得处理出正值和负值的区别。<br><br><div align="center">
<img id="aimg_1016810" aid="1016810" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181458gc1cei1pfk77ihzp.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181458gc1cei1pfk77ihzp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181458gc1cei1pfk77ihzp.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们让X和Y分别减去0.5，那么我的图片就能居中，中间点到了（0, 0）的位置；<br><br>
原本（0, 1）的区间就变成（-0.5, 0.5）的区间，由此我们就能拥有正负两个方向的运动。<br><br>
这张图是 Unreal 和 Unity 中的坐标节点图标：<br><br><div align="center">
<img id="aimg_1016811" aid="1016811" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181459a989l46p99kuxpb4.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181459a989l46p99kuxpb4.jpg" width="578" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181459a989l46p99kuxpb4.jpg" referrerpolicy="no-referrer">
</div>
<br>
你看到当中红绿的过度，其实就是两个通道灰度从黑到白的渐变过程，左边在红色通道里面，我们将黑色<br><br>
设置为0，白色设置为1，那么就有0到1的渐变；右边的绿色通道也同理，不过我们将它的位置设置为纵向，从黑色0到白色1。<br><br><div align="center">
<img id="aimg_1016812" aid="1016812" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181459e0rasiy2srd11rzd.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181459e0rasiy2srd11rzd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181459e0rasiy2srd11rzd.jpg" referrerpolicy="no-referrer">
</div>
<br>
这就是红绿通道的灰度值，对应坐标系的值。<br><br>
知道了颜色的坐标运动，我们简单地描述成这样：<br><br><div align="center">
<img id="aimg_1016813" aid="1016813" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181459lwe5hffh25eho2qt.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181459lwe5hffh25eho2qt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181459lwe5hffh25eho2qt.jpg" referrerpolicy="no-referrer">
</div>
<br>
通常图片的灰度值是0到256，在流程图的红色通道里面，黑色产生向右的运动，白色向左运动；如果是绿色通道就是黑色向上，白色向下。128的中间灰为静止状态。换句话说，它不会产生任何的运动。<br><br>
那么举一个实例，假如我们有这样一张图A：<br><br><div align="center">
<img id="aimg_1016814" aid="1016814" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181459bpqfmf8l20al2ppw.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181459bpqfmf8l20al2ppw.jpg" width="131" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181459bpqfmf8l20al2ppw.jpg" referrerpolicy="no-referrer">
</div>
<br>
怎样让他做左右运动成这样？<br><br><div align="center">
<img id="aimg_1016815" aid="1016815" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181500tddywoayoe717z3o.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181500tddywoayoe717z3o.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181500tddywoayoe717z3o.gif" referrerpolicy="no-referrer">
</div>
<br>
或者又怎样如此上下运动呢？<br><br><div align="center">
<img id="aimg_1016816" aid="1016816" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181500ef3pazq6nwqz7rzw.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181500ef3pazq6nwqz7rzw.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181500ef3pazq6nwqz7rzw.gif" referrerpolicy="no-referrer">
</div>
<br>
答案就是做出一张流程图。<br><br><div align="center">
<img id="aimg_1016817" aid="1016817" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181500js36roj7cd3miaja.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181500js36roj7cd3miaja.jpg" width="130" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181500js36roj7cd3miaja.jpg" referrerpolicy="no-referrer">
</div>
<br>
这张流程图就是黑白两个条组成，红色通道、绿色通道是相同的黑白条（因为不用其他方向运动，所以我们把蓝色通道设置为黑色）。<br><br><div align="center">
<img id="aimg_1016818" aid="1016818" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181501h7mqod7dmaax2qq4.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181501h7mqod7dmaax2qq4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181501h7mqod7dmaax2qq4.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们现在回头看一下，这个左右运动就是红色通道起作用（绿色通道的灰度值是128的中间灰）；而上下运动就是绿色通道起了作用（红色通道的灰度值是128的中间灰）。<br><br>
这张图就可以解释背后的原理：当我们需要左右运动的时候，我们让红色通有黑白，让绿色通道是128灰度，不产生运动。<br><br><div align="center">
<img id="aimg_1016819" aid="1016819" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181501y745rx55t1r5ky1b.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181501y745rx55t1r5ky1b.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181501y745rx55t1r5ky1b.jpg" referrerpolicy="no-referrer">
</div>
<br>
同样的图，我们将红色通道设置为128的灰度，绿色通道有黑白，那么他只有上下运动。<br><br><div align="center">
<img id="aimg_1016820" aid="1016820" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181501dy2j12zm32lmt2v9.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181501dy2j12zm32lmt2v9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181501dy2j12zm32lmt2v9.jpg" referrerpolicy="no-referrer">
</div>
<br>
基于这个原理，我们找3张图来说明实操。平常工作当中，我们经常要做河流、烟雾、岩浆的运动，这几张静止的图片，几分钟之内就可以做成运动的图片。<br><br><div align="center">
<img id="aimg_1016821" aid="1016821" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181501nshhtlul9cnlo699.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181501nshhtlul9cnlo699.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181501nshhtlul9cnlo699.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们只需要在Flowmap Painter软件里，像手指划过一样，顺着运动方向抹一下，它就会根据轨迹流动。<br><br>
我们打开“涂抹”出来的流程图，原理就很显而易见了：因为除了我们需要运动的部分，其他部分都是128的灰度，运动着的部分就是比中间灰或亮或暗一些。<br><br><div align="center">
<img id="aimg_1016822" aid="1016822" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181502wrt911nazl1r1rou.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181502wrt911nazl1r1rou.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181502wrt911nazl1r1rou.gif" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016823" aid="1016823" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181502syhxyhuy9iiyh6b4.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181502syhxyhuy9iiyh6b4.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181502syhxyhuy9iiyh6b4.gif" referrerpolicy="no-referrer">
</div>
<br>
下面这个是像素动画用到的材质球，我用一张流程图扭曲了自己的照片。为了说明白一些，我将它分为ABC三个部分。<br><br><div align="center">
<img id="aimg_1016824" aid="1016824" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181502qwcej8ssev01zie0.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181502qwcej8ssev01zie0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181502qwcej8ssev01zie0.jpg" referrerpolicy="no-referrer">
</div>
<br>
A部分看似复杂，其实只是加减乘除一样的算法，目的就是让图片的坐标移动：<br><br><div align="center">
<img id="aimg_1016825" aid="1016825" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181502wm1vxwy6l52r5ooo.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181502wm1vxwy6l52r5ooo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181502wm1vxwy6l52r5ooo.jpg" referrerpolicy="no-referrer">
</div>
<br>
One Minus——减1，其实就是首先把（0,0）放到左上角去，符合电脑的坐标规则；Append是将横纵两个方向坐标合在一起；Flow_Strength则是控制扭曲强度；<br><br>
下面是B部分，Time，也是很重要的节点。打个比方，我们这里有个坐标，时间就是穿过0的过程，往下是过去，往上是未来，它是一条无限延伸的对角线。<br><br>
而我们想获得重复的效果，就是让时间来回重复，就可以用Fract节点去掉整数。<br><br><div align="center">
<img id="aimg_1016826" aid="1016826" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181503u5irllzcxxqlmibl.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181503u5irllzcxxqlmibl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181503u5irllzcxxqlmibl.jpg" referrerpolicy="no-referrer">
</div>
<br>
让时间这一条线，从0开始，0.1走到0.9，到1的时候再重复回到0。意味着时间永远不会有的整数，他只会在0.1 - 0.9之间往复。这就产生了循环。<br><br><div align="center">
<img id="aimg_1016827" aid="1016827" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181503crayi085zhbzy040.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181503crayi085zhbzy040.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181503crayi085zhbzy040.jpg" referrerpolicy="no-referrer">
</div>
<br>
B部分和A部分是一样的运动，只是慢了0.5秒。但是可以看到都有跳帧的现象。我们用淡入淡出的遮罩来过滤掉跳帧部分——也就是C部分的工作。<br><br><div align="center">
<img id="aimg_1016828" aid="1016828" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181504s3bquybbhu4hjbbs.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181504s3bquybbhu4hjbbs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181504s3bquybbhu4hjbbs.jpg" referrerpolicy="no-referrer">
</div>
<br>
试着把它还原成更形象的坐标图，这是Time原始的样子：<br><br>
我们第一步把它变成小数往复：<br><br><div align="center">
<img id="aimg_1016829" aid="1016829" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181504a6qdwwoh6shk666w.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181504a6qdwwoh6shk666w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181504a6qdwwoh6shk666w.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016830" aid="1016830" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181504tpappn4tsddlluud.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181504tpappn4tsddlluud.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181504tpappn4tsddlluud.jpg" referrerpolicy="no-referrer">
</div>
<br>
再减去0.5以获得负值：<br><br><div align="center">
<img id="aimg_1016831" aid="1016831" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181504ri4i608wgrr0w7g2.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181504ri4i608wgrr0w7g2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181504ri4i608wgrr0w7g2.jpg" referrerpolicy="no-referrer">
</div>
<br>
再用Abs把负值翻正过来，让它连续：<br><br><div align="center">
<img id="aimg_1016832" aid="1016832" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181505kkait5yiiafs8fzl.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181505kkait5yiiafs8fzl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181505kkait5yiiafs8fzl.jpg" referrerpolicy="no-referrer">
</div>
<br>
最后再乘以2来增大波动幅度，形成连续的波浪线。<br><br>
最终我们得到这样一个淡入淡出的遮罩图融合A和B两部分，形成无缝循环。<br><br><div align="center">
<img id="aimg_1016834" aid="1016834" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181506y66oaitazig2bt26.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181506y66oaitazig2bt26.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181506y66oaitazig2bt26.jpg" referrerpolicy="no-referrer">
</div>
<br>
像素动画可以用到很多的地方。比如说这个星球的游戏界面里，巨型风暴原本是一张静止的图片。<br><br><div align="center">
<img id="aimg_1016835" aid="1016835" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181506h6em4lwjq7rr996e.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181506h6em4lwjq7rr996e.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181506h6em4lwjq7rr996e.gif" referrerpolicy="no-referrer">
</div>
<br>
银河的运动、太阳的火焰、木星的风暴，全部都是用这种材质球处理的，而且效率非常高<br><br><div align="center">
<img id="aimg_1016836" aid="1016836" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181506w30qgiwabgct30cv.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181506w30qgiwabgct30cv.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181506w30qgiwabgct30cv.gif" referrerpolicy="no-referrer">
</div>
<br>
在这个特效里，一张很多小点的黑白图和一张螺旋形状的流程图，两者合在一起，便可以做出一个近似黑洞的旋转结果。<br><br><div align="center">
<img id="aimg_1016837" aid="1016837" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181506yzqw8q81ww74t847.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181506yzqw8q81ww74t847.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181506yzqw8q81ww74t847.gif" referrerpolicy="no-referrer">
</div>
<br>
这是我们的一款三消游戏，里面云的动态、怪物的斗篷、水的运动，都用到了这种Flowmap效果。<br><br><div align="center">
<img id="aimg_1016838" aid="1016838" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181507hniw4rlenid4k9qq.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181507hniw4rlenid4k9qq.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181507hniw4rlenid4k9qq.gif" referrerpolicy="no-referrer">
</div>
<br>
这个将怪物吸进瓶子的效果，烟雾消散的效果也是用Flowmap处理的像素动画。<br><br>
制作流程图有很多讨巧的方法：<br><br>
拿这张图片来举例，先将原图导入Flowmap Painter里面，用涂抹工具顺着运动方向抹几下，于是就可以导出这样一张流程图，十分钟不到。<br><br><div align="center">
<img id="aimg_1016841" aid="1016841" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181509dak5kkbiyfuf5kky.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181509dak5kkbiyfuf5kky.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181509dak5kkbiyfuf5kky.jpg" referrerpolicy="no-referrer">
</div>
<br>
如果是像木星上这么复杂的风暴运动我肯定是没有时间顺着方向一点点抹的，太复杂了，不过这也有办法。<br><br><div align="center">
<img id="aimg_1016842" aid="1016842" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181509y5qeehvactjvot3v.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181509y5qeehvactjvot3v.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181509y5qeehvactjvot3v.jpg" referrerpolicy="no-referrer">
</div>
<br>
可以用PS将它的红色通道灰度调整，不动的部分刷成128灰度；然后把绿色通黑白反相，把不想运动的地方用128灰度的刷一刷，于是，几分钟不到的时间就得到了一张木星风暴的流程图。<br><br><div align="center">
<img id="aimg_1016845" aid="1016845" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181510e1545g3zgu45fghh.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181510e1545g3zgu45fghh.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181510e1545g3zgu45fghh.jpg" referrerpolicy="no-referrer">
</div>
<br>
再比如我只有这样一个灰度图，它的运动也是有很多细节：<br><br><div align="center">
<img id="aimg_1016846" aid="1016846" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181511nhhyqqagqmdatq6w.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181511nhhyqqagqmdatq6w.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181511nhhyqqagqmdatq6w.gif" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016847" aid="1016847" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181511weic9h3ci44747e7.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181511weic9h3ci44747e7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181511weic9h3ci44747e7.jpg" referrerpolicy="no-referrer">
</div>
<br>
可以用CrazyBump拿这张灰度图直接产生Normal Map，我把蓝色通道设置黑的，只用红绿通道，就变成了流程图：<br><br>
不过最酷的还是用FluidNinja这个插件，如火球、烟雾、爆炸，流体等各种运动，我们都可以用3种方式百分百地控制生产它们的运动。<br><br>
第一种就是粒子系统。无非是用运动的粒子产生不同的黑白间隔比例，配上算法，就有了种种流体模拟的效果。不光是单帧，也可以设置成序列帧。第二种是用黑白图片，第三种是用力场。它让像素动画特效设计增加了极大的空间。<br><br><div align="center">
<img id="aimg_1016848" aid="1016848" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181512vtfte0t1endmjjdd.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181512vtfte0t1endmjjdd.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181512vtfte0t1endmjjdd.gif" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016849" aid="1016849" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181512xui6fo6ocmm99fc6.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181512xui6fo6ocmm99fc6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181512xui6fo6ocmm99fc6.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们做手游因为包体的大小会受到控制，特效贴图用512x512就会是常大的图了，尤其我们做序列帧的时候。比如说512x512，我们把它分割成4x4=16帧，每个单位都是256，低于这个值，手机上就会看得很模糊。<br><br>
游戏是每秒30帧播放，16帧的序列图勉强可以在1s内让你觉得特效过得去。现在有了序列帧的流动图，我们就可以将它做到几倍的特效时长。<br><br><div align="center">
<img id="aimg_1016850" aid="1016850" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181513e8o1sda51yurud8a.gif" data-original="https://di.gameres.com/attachment/forum/202110/22/181513e8o1sda51yurud8a.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181513e8o1sda51yurud8a.gif" referrerpolicy="no-referrer">
</div>
<br>
比如一个爆炸特效，左边这个爆炸是用8x8 64的序列帧，2秒的特效，很顺滑。但假如这是一个原子弹爆炸，让你做30s以上， 1秒就是30帧，30秒就得900帧，那得多大的序列帧贴图啊？右边这个就是用了序列帧流程图的效果，很长但没有卡顿。<br><br><div align="center">
<img id="aimg_1016851" aid="1016851" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181514c2konmf3stmgog32.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181514c2konmf3stmgog32.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181514c2konmf3stmgog32.jpg" referrerpolicy="no-referrer">
</div>
<br>
材质球就会稍微复杂一些：<br><br><div align="center">
<img id="aimg_1016852" aid="1016852" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181514iaqlquzonl43loqq.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181514iaqlquzonl43loqq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181514iaqlquzonl43loqq.jpg" referrerpolicy="no-referrer">
</div>
<br>
目的是用序列帧的流动图为序列帧增加中间帧：<br><br>
基本道理就是将当前帧往外扭曲，然后下一帧往内扭曲，关键帧缩紧放大后，就出现了两个中间帧，帧数变多，画面自然变丝滑。<br><br><strong>最后总结一下像素动画的优缺点：</strong><br><br>
优点是可以很快、精确地产生我们想要的运动。方法非常简单，制作流程图可以用Flowmap Painter、PS、CrazyBump，还有现在最酷的FluidNinja，借助它我们可以把Unreal、Unity结合起来使用。<br><br>
序列帧流动图除了产生很细节的运动以外，可以大幅度降低我们的图片大小。<br><br><div align="center">
<img id="aimg_1016853" aid="1016853" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181515ohiqzq3irn6dqycx.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181515ohiqzq3irn6dqycx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181515ohiqzq3irn6dqycx.jpg" referrerpolicy="no-referrer">
</div>
<br>
像素动画的的缺点就是动作是重复的。<br><br><div align="center">
<img id="aimg_1016854" aid="1016854" zoomfile="https://di.gameres.com/attachment/forum/202110/22/181515et7kn77789czv3tv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/22/181515et7kn77789czv3tv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/22/181515et7kn77789czv3tv.jpg" referrerpolicy="no-referrer">
</div>
<br>
</td></tr></tbody></table>

<div class="pattl">


<img src="https://www.gameres.com/static/image/common/rleft.gif" class="vm" referrerpolicy="no-referrer">
</div>

  
</div>
            