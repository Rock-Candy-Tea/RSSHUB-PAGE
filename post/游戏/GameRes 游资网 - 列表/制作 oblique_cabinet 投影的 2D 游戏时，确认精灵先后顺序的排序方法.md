
---
title: 制作 oblique_cabinet 投影的 2D 游戏时，确认精灵先后顺序的排序方法
categories: 
    - 游戏
    - GameRes 游资网 - 列表
author: GameRes 游资网 - 列表
comments: false
date: Fri, 05 Feb 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202102/05/102814onqttzcgpzrtgllh.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2484558">
<div align="center">
<img id="aimg_959051" aid="959051" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102814onqttzcgpzrtgllh.jpg" data-original="https://di.gameres.com/attachment/forum/202102/05/102814onqttzcgpzrtgllh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102814onqttzcgpzrtgllh.jpg" referrerpolicy="no-referrer">
</div><br>
我经常说，我们以前玩过的很多游戏虽然看上去是 2D 的，但其实是 3D 游戏——比如热血物语、双截龙系列，它们具有一套三维的立体空间逻辑，从而不再使得游戏的舞台限制在只有左右移动和上下跳跃这两种轴向——拥有三个维度极为自由开放的移动范围相信也给很多玩家留下了深刻的印象，在上次的文章里，我们已经介绍了这种游戏的物理部分简单实现，本次将会聊到这类游戏在渲染上的重要技巧。<br>
<br>
<div align="center">
<img id="aimg_959052" aid="959052" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102814ofyzwy626yk45nj4.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102814ofyzwy626yk45nj4.png" width="183" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102814ofyzwy626yk45nj4.png" referrerpolicy="no-referrer">
</div><br>
显然，在用 2D 精灵模拟的 3D 空间里，任何一个物体都不简单：如图所示的一个立方体，具有一个<font color="#4169e1"> oblique 视角</font>(或者，我们叫 <font color="#4169e1">cabinet 视角</font>更准确)的造型。这样的视角下，如果有另外一个精灵和它相互遮挡，应该怎么处理它们的渲染顺序关系呢？<br>
<br>
<font size="2">注：为了简化描述，本文章的 3D 空间假设所有物件的<font color="#4169e1"> z 坐标</font>都相同，即“没有和地面的高度差”。</font><br>
<br>
<strong><font color="#de5650">任意两个物体之间的排序</font></strong><br>
<br>
按照我们一般的简单思路（比如在经典的 topdown 视角下，如 RPGMAKER 系列），谁在世界上具有较大的<font color="#4169e1"> y 值</font>，谁就靠近屏幕，谁就应该更靠后地渲染，对吧？不过在这样的视角下，就没有那么简单了，来看一个例子：<br>
<br>
<div align="center">
<img id="aimg_959053" aid="959053" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102814czba3l5laj26wns2.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102814czba3l5laj26wns2.png" width="234" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102814czba3l5laj26wns2.png" referrerpolicy="no-referrer">
</div><br>
如图，根据十字形标记，我们可以轻松地发现 shari 的 <font color="#4169e1">y 坐标</font>小于立方体的坐标，所以她理应被挡在立方体的后面（先于立方体渲染），对吧？可是当她来到另外一侧的时候，情况就变化了：<br>
<br>
<div align="center">
<img id="aimg_959054" aid="959054" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102815oji55m20xtxx889m.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102815oji55m20xtxx889m.png" width="207" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102815oji55m20xtxx889m.png" referrerpolicy="no-referrer">
</div><br>
如图，shari 的 <font color="#4169e1">y 坐标</font>仍然小于立方体的 <font color="#4169e1">y 坐标</font>，但这个位置上，我们是希望 shari 遮挡立方体而不是被立方体遮挡的，所以我们需要考虑到更多的情况。<br>
<br>
<div align="center">
<img id="aimg_959055" aid="959055" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102815mkt1vp8o9cgbmc1o.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102815mkt1vp8o9cgbmc1o.png" width="162" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102815mkt1vp8o9cgbmc1o.png" referrerpolicy="no-referrer">
</div><br>
显然，这个世界里的任何一个物体都应该携带它的"底座"信息。如图，红色的平行四边形就是上面立方体的"底座"信息，而绿色是它的高度信息（如果你需要一些更细致的排序，比如算上<font color="#4169e1"> z 轴</font>，本文暂不讨论）有了这个信息，我们就可以确定任意两个对象之间的绘制顺序。<br>
<br>
我们把两个要排序的物体分别命名为 A 和 B，A 底座的上边缘称为 <font color="#4169e1">aTop</font>，下边缘称为 <font color="#4169e1">aBottom</font>；B 底座的上边缘称为 <font color="#4169e1">bTop</font>，下边缘称为<font color="#4169e1"> bBottom</font>。<br>
<br>
<font color="#4169e1">aBottom </font>的 <font color="#4169e1">y 坐标</font>小于 <font color="#4169e1">bTop</font> 的<font color="#4169e1"> y 坐标</font>：<br>
<br>
<div align="center">
<img id="aimg_959056" aid="959056" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102815gxnbdnk9ak9xfzfx.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102815gxnbdnk9ak9xfzfx.png" width="273" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102815gxnbdnk9ak9xfzfx.png" referrerpolicy="no-referrer">
</div><br>
这时候 A 显然是在 B 的后方，也就是 A 先于 B 渲染。<br>
<br>
<font color="#4169e1">aTop</font> 的 <font color="#4169e1">y 坐标</font>大于 <font color="#4169e1">bBottom</font> 的<font color="#4169e1">y 坐标</font>：<br>
<br>
<div align="center">
<img id="aimg_959057" aid="959057" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102816lrvg11krnb1kpkrt.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102816lrvg11krnb1kpkrt.png" width="273" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102816lrvg11krnb1kpkrt.png" referrerpolicy="no-referrer">
</div><br>
这时候 A 显然是在 B 的前方，也就是 B 先于 A 渲染。<br>
<br>
其它的情况：<br>
<br>
<div align="center">
<img id="aimg_959058" aid="959058" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102816qvzo22je8y2vy8vv.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102816qvzo22je8y2vy8vv.png" width="330" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102816qvzo22je8y2vy8vv.png" referrerpolicy="no-referrer">
</div><br>
由于我们这里的视角下，侧面是一个 45 度的斜线，所以我们可以很轻松地把两个物体下边缘的 <font color="#4169e1">y 轴</font>距离加到<font color="#4169e1"> aBottom </font>的右端点去进行判断，像是这样：<br>
<br>
<div class="quote"><blockquote>distanceY = bBottom.y - aBottom.y</blockquote></div>（我们用<font color="#4169e1"> left </font>和<font color="#4169e1"> right</font> 表示一个线段的左端点和右端点）<br>
<br>
<div class="quote"><blockquote>aBottom.left.x > bBottom.right.x + distanceY</blockquote></div><br>
如果这个判断是成立的，那就是上图所述的情况：A 在 B 的前方，也就是 B 先于 A 渲染。<br>
<br>
否则就是下图所述的情况：A 在 B 的后方，也就是 A 先于 B 渲染。<br>
<br>
<div align="center">
<img id="aimg_959059" aid="959059" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102816hr2s8rrssrf2jf06.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102816hr2s8rrssrf2jf06.png" width="327" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102816hr2s8rrssrf2jf06.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">对场景内所有物体的排序</font></strong><br>
<br>
好，至此我们已经可以为场景内任意的两个对象进行排序了，那么，我们也可以为场景中所有的对象组织排序。很多人的第一反应是，直接用冒泡/选择/归并/快排这样的算法来对场景中需要排序的物体进行排序不就好了吗？其实这是不合适的，因为场景中的物体遮挡存在拓扑关系，如果直接使用线性表的排序方法，可能在 swap 一对物体以确保他们遮挡关系的同时又会直接破坏了另一对物体的遮挡关系，因此，我们的第一步是对场景中需要排序的物体进行连线。<br>
<br>
图片带有弧线的那一端是射线的末端，末端的物体比首端的物体更先渲染(位置更靠后)。<br>
<br>
这里说明一下，<font color="#ff0000">我们只对需要排序的一对物体进行连线（出于性能考虑）</font>，所以你的显示对象可能需要有相应的 <font color="#4169e1">bounding_box</font> 或是什么的。<br>
<br>
<div align="center">
<img id="aimg_959060" aid="959060" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102816w14sf553byt3h3j3.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102816w14sf553byt3h3j3.png" width="183" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102816w14sf553byt3h3j3.png" referrerpolicy="no-referrer">
</div><br>
当场景中的物体足够多，遮挡关系足够复杂时，不难发现，我们的物体遮挡关系实际上构建出了一个有向图。而有向图可以通过拓扑排序来获取一个不唯一的线性序列，照着这个线性序列进行渲染就可以获得正确的场景排序了。<br>
<br>
<div align="center">
<img id="aimg_959061" aid="959061" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102816xg62j8roam6c1rge.png" data-original="https://di.gameres.com/attachment/forum/202102/05/102816xg62j8roam6c1rge.png" width="143" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102816xg62j8roam6c1rge.png" referrerpolicy="no-referrer">
</div><br>
（图中蓝绿色的矩形是判断精灵相交/重叠用的 <font color="#4169e1">bounding_box</font>，<font color="#4169e1">DRAWIDX</font> 则是拓扑排序后得到的渲染顺序值）<br>
<br>
这样，就得到了整个场景的正确呈现顺序。<br>
<br>
<div align="center">
<img id="aimg_959062" aid="959062" zoomfile="https://di.gameres.com/attachment/forum/202102/05/102817n9zn9zdseauumave.gif" data-original="https://di.gameres.com/attachment/forum/202102/05/102817n9zn9zdseauumave.gif" width="242" inpost="1" src="https://di.gameres.com/attachment/forum/202102/05/102817n9zn9zdseauumave.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">最后一点问题</font></strong><br>
<br>
相信我们都看到过一些"视觉错觉"的趣味图片，对吧？譬如三个无限循环的台阶，相互遮挡的三个棱柱……之类的，很有意思，不过在游戏开发当中可一点也不有趣。很显然，当游戏场景中出现了几个互相存在遮挡和被遮挡关系的对象时，我们构造出的有向图就成环了。而成环的有向图是不能进行拓扑排序的，这就导致我们没有办法去按正确顺序呈现画面。解决这个问题的最好方法就是把容易引起该问题的那个物体分割为两个物体，使得其中的一个部分"专门遮挡"而另一个部分"专门被遮挡"，这样就可以消除我们构造的有向图中的环。<br>
<br>
本次的讨论就到这里，祝大家开发顺利，新年快乐！<br>
<br>
<font size="2"><font color="#708090">作者：lanza</font></font><br>
<font size="2"><font color="#708090">来源：indienova</font></font><br>
<font size="2"><font color="#708090">地址：https://mp.weixin.qq.com/s/-8-cXkJ9hG8Di-yeJcPo7w</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            