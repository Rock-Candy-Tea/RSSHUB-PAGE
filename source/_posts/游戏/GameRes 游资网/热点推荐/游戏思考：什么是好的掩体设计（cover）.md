
---
title: '游戏思考：什么是好的掩体设计（cover）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/09/092210jrtvtv1yexgyxc2h.jpg'
author: GameRes 游资网
comments: false
date: Wed, 09 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/09/092210jrtvtv1yexgyxc2h.jpg'
---

<div>   
<div align="center">
<img aid="1032966" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092210jrtvtv1yexgyxc2h.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092210jrtvtv1yexgyxc2h.jpg" width="600" id="aimg_1032966" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092210jrtvtv1yexgyxc2h.jpg" referrerpolicy="no-referrer">
</div><br>
<font color="#808080">作者：TokyoRed</font><br>
<font color="#808080">首发知乎:https://zhuanlan.zhihu.com/p/476657793</font><br>
<br>
本文希望通过梳理对掩体设计的系统化思考，去深入理解游戏内部空间组织和玩家行为的逻辑。<br>
<br>
掩体(cover)的设计往往会和游戏的内容体验强相关，尤其在shooter、有动作元素的RPG、FPP潜行等游戏品类中，掩体往往影响单局战术决策和可玩性深度。<br>
<br>
文章的插图部分主要来自游戏设计师Iuliu-Cosmin Oniscu的博客《How to handle cover placement》，以及游戏设计师Tommy Norberg的推特。文字部分编译自两位设计师的注释，并加入了我个人的理解思考。<br>
<br>
<strong><font color="#de5650">1、 怎么解决掩体的放置问题</font></strong><br>
<br>
<strong>游戏品类的视角-潜行/射击</strong><br>
<br>
首先要问游戏设计师的是，怎么处理掩体的放置呢？应该使用怎么样的思考流程？战斗空间是怎么组织的呢?<br>
<br>
设计之前要考虑掩体能给游戏带来什么样的好处，并且要和游戏类型联系起来。<br>
<br>
在潜行游戏中，掩体是一种路径追踪器。玩家可以在掩体之间保持一定的机动性，来绕开放置在地图上的NPC。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032967" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092210ozk81119m0n0irnc.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092210ozk81119m0n0irnc.jpg" width="600" id="aimg_1032967" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092210ozk81119m0n0irnc.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">潜行游戏的掩体放置</font></font></div><br>
在上图这个例子中，掩体的放置基于一些简单的原则：玩家从一个掩体移动到另一个掩体，以避免NPC的发现。这意味着暴露在NPC视线中就像一个机会窗口（window of opportunity moment），玩家等待NPC移开视线，然后移动到另一个遮蔽点。根据Al的行为模式，可以分解出一些参数，这些参数会影响到这个场景的难度。<br>
<br>
下图给出一组参数示例：玩家移动距离和NPC的观察时长。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032968" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092210f8v34qtwq6v6hpcv.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092210f8v34qtwq6v6hpcv.png" width="600" id="aimg_1032968" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092210f8v34qtwq6v6hpcv.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">机会窗口图-移动距离与NPC观察时长</font></font></div><br>
通过改变掩体之间的距离和NPC的视线/转向方向，可能会在游戏体验中产生很多有趣的组合。当然，其他参数也可以应用在设计中。<br>
<br>
而在射击游戏中，掩体则是一种让玩家避开敌人、观察战场、从一个掩蔽点移动到另一个以避开交叉火力的方法。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032969" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092211jczquvapz95ujl6i.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092211jczquvapz95ujl6i.png" width="600" id="aimg_1032969" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092211jczquvapz95ujl6i.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">掩体射击的掩体放置</font></font></div><br>
在这种情况下，我们可以应用与之前相同的图表，但我们需要用射击时间代替观察时间。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032970" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092212p3r0fffk0exlffe3.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092212p3r0fffk0exlffe3.png" width="600" id="aimg_1032970" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092212p3r0fffk0exlffe3.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">机会窗口图-移动距离与射击时长</font></font></div><br>
<strong>隐含空间的利用</strong><br>
<br>
像《GTA》，《看门狗》，《黑手党3》等游戏将潜行和战斗融合成统一的空间，并同时满足上述两种目的。然而由于它们是开放世界游戏，为了沉浸感，必须反映一定的基于现实的世界观。这意味着它们必须从游戏叙事的角度进行掩体设计的修正。<br>
<br>
为了能自然地做到这一点，在这类游戏中放置掩体时，可以考虑以下的概念：<br>
<br>
隐含空间（Implied Spaces），指代那些基于几何或功能划分的空间类型细分。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032971" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092212pcwrrchiiyz9zl90.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092212pcwrrchiiyz9zl90.png" width="445" id="aimg_1032971" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092212pcwrrchiiyz9zl90.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">隐含空间的一些例子</font></font></div><br>
需要说明的是，这个空间概念来自建筑学，但也在一些游戏设计师群体中得到共识，感兴趣的朋友可以看一下2015年Dan Cox的GDC演讲，主要谈的是室内设计原理对于游戏场景的主要作用，其中也举了隐含空间的例子。<br>
<br>
隐含空间怎么和掩体设计结合起来呢？可以参考下面的一些关卡设计原型：<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032972" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092212gviiz3ur0cve3zr6.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092212gviiz3ur0cve3zr6.png" width="600" id="aimg_1032972" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092212gviiz3ur0cve3zr6.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">结合隐含空间的布局实例</font></font></div><br>
通过创建隐含空间，我们可以设计出一系列辅助性空间，既可以作为放置掩体的位置，也可以作为某种游戏仪式感的象征，同时这些设计都不会影响布局图中的主要方向引导。<br>
<br>
<div align="center">
<img aid="1032973" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092213ncz8phtitee9z1fc.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092213ncz8phtitee9z1fc.png" width="600" id="aimg_1032973" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092213ncz8phtitee9z1fc.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">直接应用于实际的关卡布局中</font></font></div><br>
以下是一些关于更加强调战斗导向的空间示例:<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032974" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092214y8ta1m9e09cepty9.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092214y8ta1m9e09cepty9.png" width="600" id="aimg_1032974" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092214y8ta1m9e09cepty9.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《Halo》中关卡探索的示例</font></font></div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032975" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092214wpfffn0qdn0xgxi5.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092214wpfffn0qdn0xgxi5.png" width="600" id="aimg_1032975" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092214wpfffn0qdn0xgxi5.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">写实主义的布局示例</font></font></div><br>
隐含空间的另一个例子是阴影空间（shadow/shade spaces）。这些类型的空间之所以存在，只是因为它们处在阴影中，并为玩家提供了一种不同类型的视觉掩护。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1032976" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092215ntjww4tj94twzr2r.png" data-original="https://di.gameres.com/attachment/forum/202203/09/092215ntjww4tj94twzr2r.png" width="600" id="aimg_1032976" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092215ntjww4tj94twzr2r.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">阴影空间的例子</font></font></div><br>
对于这种掩体位置，我们需要着重去控制环境内部的光源。<br>
<br>
以上是第一部分关于解决掩体放置问题的讨论，着重阐述了潜行和射击游戏品类中的掩体布局基础原则，以及隐含空间的概念是如何应用在关卡设计中的。接下来是第二部分，介绍掩体设计具体的空间规划逻辑。<br>
<br>
<strong><font color="#de5650">2、掩体设计的空间规划逻辑</font></strong><br>
<br>
游戏设计师Tommy Norberg曾经在Twitter上发布过拆解游戏设计元素的系列插图，这里基于他对游戏中掩体的讨论，结合个人理解，浅谈游戏中掩体设计的空间规划逻辑。<br>
<br>
掩体设计的不同阶段<br>
<br>
<div align="center">
<img aid="1032977" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092215tpycdtzbmb8c0kb0.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092215tpycdtzbmb8c0kb0.jpg" width="600" id="aimg_1032977" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092215tpycdtzbmb8c0kb0.jpg" referrerpolicy="no-referrer">
</div><br>
从掩体的平面布局来看，从初级到高级可以分为三个阶段：<br>
<br>
<strong>第一阶段，糟糕的布局</strong><br>
<br>
完全镜像分布，对称式的布局<br>
<br>
敌人以“怪物衣柜”的形式出现（下文中会解释）<br>
<br>
<strong>第二阶段，稍微改善的布局</strong><br>
<br>
掩体像岛屿一样组团式分布<br>
<br>
掩体具有不同的角度和形状<br>
<br>
预留一些敌人增援和强化的空间<br>
<br>
<strong>第三阶段，更成熟的布局</strong><br>
<br>
掩体以可读性更高的组团形式出现<br>
<br>
有逻辑性的布局，符合空间规划<br>
<br>
给玩家多重选择<br>
<br>
初始是简单的AI，然后出现多重敌人的增援<br>
<br>
以及在竖向空间上的高差设计<br>
<br>
<strong>尽量避免“怪物衣柜”设计</strong><br>
<br>
关于第一阶段提到的“怪物衣柜”，可以参考下图：<br>
<br>
左边的布局中可以看到，敌人像是排成队等待在每一个遭遇战的小房间或掩体背后，这就是“怪物衣柜“的简单排列逻辑，整体缺乏动态和变化。而右边的布局图中，敌人是分层级和流动的，一些怪物可能在门后躲着，另外一些可能会逐渐从外围的墙体中涌入房间，还有一些可以被玩家远远观望或是随时发动偷袭。<br>
<br>
一般来说，“怪物衣柜“是设计师们需要避免的坏设计，但也不能一概而论。比如像一些布置“明雷怪”的回合制游戏，或是JRPG中常见的“迷宫”设计，经常会把怪物明确显眼地放在地图中。<br>
<br>
<div align="center">
<img aid="1032978" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092215z424qfk67q4fixxg.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092215z424qfk67q4fixxg.jpg" width="554" id="aimg_1032978" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092215z424qfk67q4fixxg.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>掩体的高度和材质</strong><br>
<br>
继续回到掩体的主题，一般来说，可以把掩体从高度和材质的角度进行区分。<br>
<br>
<strong>从高度来看——</strong><br>
<br>
超低“掩体”：实际上更适宜于做成收集物的储藏区域，而非玩家可以利用的掩体。<br>
<br>
半掩体：一般来说是最重要的度量尺度，无论是从玩法还是从掩体本身的价值来看。这种类型的掩体往往会和窗台、穹顶之类的空间进行结合。<br>
<br>
全掩体：有时候会和具有高度的物件联系起来。<br>
<br>
高海拔：如果地形升高，那么玩家往往是被认定为处于掩体之中。因为在高地一般会具有安全度极高的视野和角度，同时从心理学的角度来看，抬高的位置处在敌人之上，这样也会带来掩体的功能和感觉。<br>
<br>
同时设计师需要注意的是，在掩体前面，要留出足够干净和可辨识的过渡空间。<br>
<br>
<strong>从材质来看——</strong><br>
<br>
硬质掩体：比如石头，墙体等。<br>
<br>
软质掩体：比如草丛，灌木丛等。这种掩体一般会鼓励玩家进行潜行，因为它们会间接地传达出信息——如果玩家做了一些激进的行为，这种介质的掩体功能就会消失。比如很多潜行游戏中都具有的“敌人警戒度”系统，玩家一旦贸然行动，软质掩体提供的庇护就会是极为有限的。<br>
<br>
<div align="center">
<img aid="1032979" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092216jfu46l9jzo4otolq.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092216jfu46l9jzo4otolq.jpg" width="600" id="aimg_1032979" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092216jfu46l9jzo4otolq.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>掩体“无人区”</strong><br>
<br>
下面是无人区的设计策略。<br>
<br>
无人区的设计出发点：<br>
<br>
<ul><li>设计师不希望玩家永远停留在某个点，而是给玩家一定的理由去进入到新区域中。</li><li>即使被敌人集火，玩家也能够希望探索区域。<br>
</li></ul><br>
整体的设计要点：<br>
<br>
<ul><li>无人区要足够深，才能有意义。</li><li>无人区要足够宽，让玩家感觉是正面直对着的，否则会可能成为尴尬的瓶颈区域。</li><li>设计师不一定需要添加侧翼路线，有时候应该鼓励让玩家停下，并且利用自己的智慧去解决手头的问题。</li><li>让敌人提供火力压制，给玩家带来封锁的压力有时候是个好主意。</li><li>同时让敌人不要离开他们的无人区。<br>
</li></ul><br>
在下面这张图中，还有一些具体的设计细节：<br>
<br>
<ul><li>敌人刷新点方位需要是多样的，以试应玩家不同的移动位置。</li><li>不同高度和不同材料的汽车是很好的掩体。</li><li>栅栏有时可以很好地引导移动，同时玩家可以使用投掷物。</li><li>灯柱不能提供掩体，但可以带来空间纵深感和良好的视差。<br>
</li></ul><br>
<div align="center">
<img aid="1032980" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092216rn5qvw55c5z5wwvp.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092216rn5qvw55c5z5wwvp.jpg" width="600" id="aimg_1032980" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092216rn5qvw55c5z5wwvp.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>分层的掩体结构</strong><br>
<br>
关于<strong>掩体的层次</strong>，下图是一个很好的改进案例。<br>
<br>
在设计掩体时，要考虑到游戏本身的体验。如果游戏内有一些紧张激烈的近距离战斗时，尤其是对多人对抗游戏来说，就要尤为注意<strong>分层级的掩体设计。</strong><br>
<br>
<strong>左图为环形结构。</strong><br>
<br>
<ul><li>这种结构简单并有效，每个放置的石头或树掩体都提供了一定的可流动性。</li><li>这种结构几乎无处不在，不管设计师是否是有意的。</li><li>但如果真的设计这种结构，可以考虑：试着使用多层次，结合全掩体和半掩体各自的特征，将会创建一个辨识度高的“掩体岛屿”。<br>
</li></ul><br>
<strong>右图为8字型结构。</strong><br>
<br>
<ul><li>尽量在布局图中隐藏掉“8”这个直观的形式，让设计尽可能的内在化和有机化。</li><li>目标是让玩家和ai能够自然地围绕着这种结构流动。<br>
</li></ul><br>
<div align="center">
<img aid="1032981" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092216uhgdy74wk3dcsgt1.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092216uhgdy74wk3dcsgt1.jpg" width="600" id="aimg_1032981" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092216uhgdy74wk3dcsgt1.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>从掩体到掩体</strong><br>
<br>
最后是关于从<strong>掩体到掩体的设计策略</strong>（cover-to-cover还有从头到尾的意思）。<br>
<br>
首先是关于<strong>掩体之间的放置距离</strong>，主要受到游戏中各种度量尺度的影响，包括：<br>
<br>
<ul><li>人物的移动速度</li><li>武器的数值</li><li>敌人的强度<br>
</li></ul><br>
这里以一个完整的玩家流线为例，玩家从下图中右下角绿色箭头处出发，左边的红色箭头为敌人的攻击方向。<br>
<br>
玩家首先经过一段<strong>长距离的掩体群</strong>，这种尺度的掩体一般标志着无人区，以及充满死亡可能的探索区域。接着是一段<strong>中等距离的掩体群</strong>，这个位置有风险，但同时也具有奖励。再之后是<strong>短距离的掩体群</strong>，类似于之前提到过的“掩体岛屿”概念。<br>
<br>
经过这三段不同的掩体后，玩家进入到图中上部围合起来的<strong>庇护区</strong>，这种区域的设计一般是用于给玩家进行喘息的，或者是进行近距离的紧张对战。这里同时提醒了设计师，要时刻注意着游戏中的<strong>高度紧张时刻，和冷静放松时刻的切换。</strong><br>
<br>
<div align="center">
<img aid="1032982" zoomfile="https://di.gameres.com/attachment/forum/202203/09/092217ujjwpgpicxx6ixyy.jpg" data-original="https://di.gameres.com/attachment/forum/202203/09/092217ujjwpgpicxx6ixyy.jpg" width="600" id="aimg_1032982" inpost="1" src="https://di.gameres.com/attachment/forum/202203/09/092217ujjwpgpicxx6ixyy.jpg" referrerpolicy="no-referrer">
</div><br>
以上就是本期的全部内容了——<br>
<br>
码字不易，欢迎感兴趣的朋友，点赞并关注我的知乎。我会定期学习，梳理，输出 【游戏/游戏设计/游戏建筑】 相关的思考或笔记。<br>
<br>
<font size="2"><font color="#808080">参考来源：</font></font><br>
<font size="2"><font color="#808080">https://iuliu-cosmin-oniscu.medium.com/how-to-handle-cover-placement-d10580faac66</font></font><br>
<font size="2"><font color="#808080">https://twitter.com/the_Norberg</font></font><br>
<br>
<strong><font color="#de5650">相关阅读：</font></strong><br>
<br>
<a href="https://www.gameres.com/893296.html" target="_blank">游戏设计集 · 详解关卡设计的平面布局（Layout）</a><br>
<a href="https://www.gameres.com/892653.html" target="_blank">游戏设计集 · 论关卡设计的节奏（Pacing）</a><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/476657793</font></font><br>
<br>
  
</div>
            