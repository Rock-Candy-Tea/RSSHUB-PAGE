
---
title: '从《Stray》拆解游戏关卡设计和美术（二）'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/11/094856n60a7nga5056p752.jpg'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://di.gameres.com/attachment/forum/202208/11/094856n60a7nga5056p752.jpg'
---

<div>   
<div align="center">
<img aid="1049541" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094856n60a7nga5056p752.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094856n60a7nga5056p752.jpg" width="600" id="aimg_1049541" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094856n60a7nga5056p752.jpg" referrerpolicy="no-referrer">
</div><br>
<i><font color="#808080">作者：枕鹤，前腾讯游戏技术美术实习生，深耕关卡设计与美术、灯光，目前23应届挂个求职，联系邮箱：630647752@qq.com</font></i><br>
<i><font color="#808080">首发知乎：https://zhuanlan.zhihu.com/p/550192071</font></i><br>
<br>
<strong><font color="#de5650">前言</font></strong><br>
<br>
在上一篇中，我们着重讨论了线性空间下的关卡，我在最后更新了一些内容关于单空间内如何塑造空间感和逻辑光源与装饰光的知识点，没看的朋友可以先看一下前篇的内容结尾。<br>
<br>
<a href="https://www.gameres.com/896219.html" target="_blank">前篇：<从《Stray》拆解游戏关卡设计和美术></a><br>
<br>
上一章严格按照《Stray》的剧情和游戏关卡顺序，为了不打乱读者的阅读节奏，不会引用还未提及的关卡作为例子，也没有大量使用东拼西凑的游戏来引用，但一些简单的知识点需要尽早提及，所以可能不是最合适的图例，大家了解其知识点的含义即可。<br>
<br>
<div align="center">
<img aid="1049542" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094856lllyxe2696relrrt.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094856lllyxe2696relrrt.jpg" width="600" id="aimg_1049542" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094856lllyxe2696relrrt.jpg" referrerpolicy="no-referrer">
</div><br>
入门的东西想必大家都看腻了，那么我们本章开始深入一些。<br>
<br>
<strong><font color="#de5650">第四章-贫民窟</font></strong><br>
<br>
<div align="center">
<img aid="1049543" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094857c6k7sq6q6v67kctk.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094857c6k7sq6q6v67kctk.jpg" width="600" id="aimg_1049543" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094857c6k7sq6q6v67kctk.jpg" referrerpolicy="no-referrer">
</div><br>
游戏从这个关卡开始，由原来的线性游戏关卡空间模式，变为一个更加自由探索的关卡空间，玩家并不再按照线性关卡打造的固定节奏和单向空间去进行游戏体验。游戏的节奏也从设计师完全的掌控逐渐放手，更大的控制权放在玩家手上，只能动态地控制玩家的行为，这对于任务的设计以及空间的布置都提出了更高的要求。<br>
<br>
所以新开一章内容，与前篇做出区分，在本篇文章专注拆解“贫民窟”这个空间的内容，会更大程度上涉及多空间和自由探索的关卡内容。<br>
<br>
<strong>遮挡</strong><br>
<br>
在上一章的末尾简单提及了遮挡，在这里再次提及，因为其在关卡设计中是一个非常实用的技巧。<br>
<br>
在建筑学的虚实理论中，不得不提到的是实体的一大体质：遮挡。<br>
<br>
任何与现实相关的场景都不能避免这一点，你放一个实体，这个实体就会挡住其后的物体；这迫使关卡和游戏设计师仔细斟酌，判断哪些东西应该被同时看到，又有哪些是不应该被同时看到的。<br>
<br>
实体信息传达的性质就在于，它会在后方创造一片遮挡阴影，内部信息我们无从得知。<br>
<br>
在玩家首次进入贫民窟时，是需要指引其走到最后的电梯前的，那么，巧妙地规划玩家路线就是一个关键。除了使用一些可以封闭起来的门，以外，也巧妙利用了遮挡。<br>
<br>
<div align="center">
<img aid="1049544" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094857icyunkyz72zcpi22.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094857icyunkyz72zcpi22.jpg" width="600" id="aimg_1049544" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094857icyunkyz72zcpi22.jpg" referrerpolicy="no-referrer">
</div><br>
左侧的水管挡住了原来机器人逃脱的路，当然它也被临时关闭了。其次，根据上面的线的指引，从高到低也是指向右边。<br>
<br>
<strong><font color="#de5650">弱化影响</font></strong><br>
<br>
遮挡的另一种作用是弱化影响。<br>
<br>
我们可以用遮挡来隐藏那些喧宾夺主，会与我们重心冲突的元素。在这个关键镜头下，左右两侧的道路都被前景的凸出结构给遮挡了，让观众把焦点放在电梯间。<br>
<br>
<div align="center">
<img aid="1049545" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094857ytzueudjujjuoxd1.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094857ytzueudjujjuoxd1.jpg" width="600" id="aimg_1049545" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094857ytzueudjujjuoxd1.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>利用遮挡提高空间理解的难度</strong><br>
<br>
当我们想要提高玩家理解空间结构的难度时，也可也使用遮挡。<br>
<br>
如果我们想要提高难度，可以在多角度放置遮挡关键要素的物体，如此一来，我们就可以减少单一角度的信息完整性和清晰度，迫使玩家从多个角度更加仔细观察环境。<br>
<br>
类似的做法顽皮狗在《神秘海域4》中的【莱伯塔利亚金融区】中被使用，他们使用连续三层的遮挡，让目标地点被隐藏起来。当玩家寻找出口一筹莫展之时，玩家再次回头走下楼梯，看到出口明明只有几步之遥，但却被物体挡住了。<br>
<br>
<div align="center">
<img aid="1049546" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094857asxketze9zvzyee8.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094857asxketze9zvzyee8.jpg" width="600" id="aimg_1049546" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094857asxketze9zvzyee8.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049547" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094858b24x112k2uu1ef2u.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094858b24x112k2uu1ef2u.jpg" width="600" id="aimg_1049547" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094858b24x112k2uu1ef2u.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049548" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094858c009qs20xssz9a9w.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094858c009qs20xssz9a9w.jpg" width="600" id="aimg_1049548" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094858c009qs20xssz9a9w.jpg" referrerpolicy="no-referrer">
</div><br>
即使光线指向了那里，并且是明暗差距最大的位置，但是仍然没有第一时间让玩家发现，而顽皮狗精湛的关卡设计，让玩家下意识地去探索他们设计的关卡空间，基本上为玩家做出了决定，尽管顽皮狗并没有强迫你去探索这些角落。<br>
<br>
遮挡同样也可以调整空间的体积感，正如上一篇【调整空间定义】中，利用实体遮挡骨骼结构的知识点，可以让玩家无法第一时间清晰地了解这个空间的全貌。<br>
<br>
《Stray》同样使用类似的手法，提高玩家理解这一区域的难度，让玩家在探索时有新发现。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049549" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094859q187ciif2eco7qj5.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094859q187ciif2eco7qj5.jpg" width="600" id="aimg_1049549" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094859q187ciif2eco7qj5.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">来时没有发现的路</font></font></div><br>
<strong><font color="#de5650">重叠</font></strong><br>
<br>
重叠本质意义上是遮挡的一种类型，指在实体背后的东西并不完全被覆盖，并非无法获取信息。<br>
<br>
当作为设计师，想要为玩家传达清晰的信息时，这时考虑的第一要素；但另一方面，我们在设计时也会偶尔有目的性地使用遮挡。<br>
<br>
当我们有一些奖励宝箱之类的东西，我们不想让玩家轻易地找到，想让他们在探索的时候给予奖励，我们显然可以放一个东西把它挡住，只有在仔细探索时才有资格拿到这个奖励。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049550" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094859nb3co7oozoocoknn.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094859nb3co7oozoocoknn.jpg" width="600" id="aimg_1049550" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094859nb3co7oozoocoknn.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">被书堆挡住的保险箱</font></font></div><br>
亦或者使用遮挡“暗示”为玩家引导某个目标。通过隐晦的让奖励露出一点点边角，将其与前面的遮挡物区分开来，能够引导激励玩家绕过去进行探索，寻找遮挡在另一侧的物体。<br>
<br>
<div align="center">
<img aid="1049551" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094859lb4c24vszqfvaj2q.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094859lb4c24vszqfvaj2q.jpg" width="600" id="aimg_1049551" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094859lb4c24vszqfvaj2q.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">加强结构纵深</font></strong><br>
<br>
重叠还可以用于加强结构纵深。<br>
<br>
如果场景中有大量的物体，他们各自分离，那么物体之间的距离和前后关系就会变得模糊。玩家无法很好地定位到自己与不同物体之间的距离关系，这对于其移动的欲望是不利的。<br>
<br>
<div align="center">
<img aid="1049552" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094900hqbq5qvqzkbk5pjj.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094900hqbq5qvqzkbk5pjj.jpg" width="600" id="aimg_1049552" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094900hqbq5qvqzkbk5pjj.jpg" referrerpolicy="no-referrer">
</div><br>
也许在【屋顶】关卡时的感知会更加明显。<br>
<br>
<strong>利用不同形状遮挡规划玩家路径与预期</strong><br>
<br>
任天堂《旷野之息》中的开放世界在CEDEC 2017发表的演讲中，讲解了形状的妙用，玩家路径和遮挡关系息息相关。<br>
<br>
他们的环境设计师注意到一点在于，引导玩家左右绕过三角形的驱动力，三角形会分散玩家的前进力，将他们向左右两侧推进，也有多花费一点力气之前爬上去的，这将玩家前进欲望拆分成三种。<br>
<br>
<div align="center">
<img aid="1049553" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094900tit2dd41dvei2d4e.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094900tit2dd41dvei2d4e.jpg" width="600" id="aimg_1049553" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094900tit2dd41dvei2d4e.jpg" referrerpolicy="no-referrer">
</div><br>
方形的引导力则强制玩家从左右两侧分开，所以立方体基本只能为玩家提供左右两种的选择。<br>
<br>
<div align="center">
<img aid="1049554" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094900mf5o2ua1xolmaz8e.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094900mf5o2ua1xolmaz8e.jpg" width="600" id="aimg_1049554" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094900mf5o2ua1xolmaz8e.jpg" referrerpolicy="no-referrer">
</div><br>
同时他在遮挡关系上还有独特的能力，当你在绕过三角形的时候，之后的物体会循序渐进地展现出来，玩家越前进，就越有更强的动力和目标。<br>
<br>
当你绕过正方体时，后方的物体会一次性暴露出来，所以它们多利用三角形为引导，方体作为障碍。<br>
<br>
<div align="center">
<img aid="1049555" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094900seienea5ge7fe0q7.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094900seienea5ge7fe0q7.jpg" width="600" id="aimg_1049555" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094900seienea5ge7fe0q7.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049556" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094901a8s5wswonpggb8dc.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094901a8s5wswonpggb8dc.jpg" width="600" id="aimg_1049556" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094901a8s5wswonpggb8dc.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">利用视觉元素指引</font></strong><br>
<br>
<strong>色彩对比</strong><br>
<br>
游戏中的色彩与各类视觉对比的使用是非常具有关卡设计意义的，设计师使用视觉线索，依靠特定的颜色来突出物体，拥有很强的吸引玩家注意力的效果，让他们免于花费很多时间去寻找下一个目标。<br>
<br>
当玩家需要进行类似于跳跃这种本能操作时，他们需要快速可识别的目标，而不是需要动脑思考和犯错。在本能基础操作上失去目标，会让玩家感到很沮丧！<br>
<br>
<div align="center">
<img aid="1049557" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094901jtzyrjjtd1fb1j4t.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094901jtzyrjjtd1fb1j4t.jpg" width="600" id="aimg_1049557" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094901jtzyrjjtd1fb1j4t.jpg" referrerpolicy="no-referrer">
</div><br>
而在并不需要强指引的位置，没有意义地指引则会打乱玩家的移动意图，则最好不要使用视觉元素。在后续的【中城】关卡中就有很多颜色鲜明的跳跃点，跳到最后发现只是用于截图与观景的。<br>
<br>
<div align="center">
<img aid="1049558" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094902zbe78e7kk6crke4o.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094902zbe78e7kk6crke4o.jpg" width="600" id="aimg_1049558" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094902zbe78e7kk6crke4o.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>重复元素</strong><br>
<br>
顽皮狗从《神秘海域2》开始发现利用色彩对比进行指引的规则，随着时间的推移，他们使用一种更为巧妙的方式来实现这一目标，这种模式在很多公司至今仍在使用，比如一些重复的视觉元素。<br>
<br>
<div align="center">
<img aid="1049559" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094902fcyw05m0yayahypz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094902fcyw05m0yayahypz.jpg" width="600" id="aimg_1049559" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094902fcyw05m0yayahypz.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《神秘海域》</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1049560" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094903z4o4e0oz8o8eu0cu.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094903z4o4e0oz8o8eu0cu.jpg" width="600" id="aimg_1049560" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094903z4o4e0oz8o8eu0cu.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《战神4》</font></font></div><br>
《Stray》中的重复元素设计则是这种类似于电箱的东西，发出蓝光。<br>
<br>
<div align="center">
<img aid="1049561" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094903dra74d738b37f70f.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094903dra74d738b37f70f.jpg" width="600" id="aimg_1049561" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094903dra74d738b37f70f.jpg" referrerpolicy="no-referrer">
</div><br>
这在半开放的关卡中是非常有意义的设计，当没有HUD时怎么去无形地规划玩家移动趋势，不让他们迷路，使用重复的元素会让玩家感到熟悉。<br>
<br>
虽然你可以前往那些人迹罕至的区域，找到几个宝藏或者敌人的藏身处，但大多数玩家不会在意这个，他们一心盯着正确的方向。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049562" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094904f2wpi6ydodyoy7ow.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094904f2wpi6ydodyoy7ow.jpg" width="600" id="aimg_1049562" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094904f2wpi6ydodyoy7ow.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《神秘海域4》开放关卡</font></font></div><br>
<strong><font color="#de5650">NPC/敌人引导</font></strong><br>
<br>
在很多后期的游戏中，这一设计有着更特殊的扩展，比如使用强烈的光线，还有敌人的位置，而有时使用敌人掉落的收集品去引导玩家路线也是很巧妙的设计。<br>
<br>
在《战神4》中这种引导方式被大量地使用，玩家在看似开放的空间，被一些敌人给不停地引导到设计师想让他们去的区域。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049563" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094904npgpz7cazoaz8jzt.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094904npgpz7cazoaz8jzt.jpg" width="600" id="aimg_1049563" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094904npgpz7cazoaz8jzt.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《战神4》</font></font></div><br>
在贫民窟中，有一些小路其实玩家很少会使用到，但那里有一些世界观设计和任务收集品，为了让玩家有机会去探索这些区域，专门设计了一个会在这些小路不停走动的NPC。<br>
<br>
好奇的玩家会跟着它探索这一块为世界观服务的区域，当然，不去也不会影响主线流程。<br>
<br>
<div align="center">
<img aid="1049564" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094904gkys35pluwbyaq5z.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094904gkys35pluwbyaq5z.jpg" width="600" id="aimg_1049564" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094904gkys35pluwbyaq5z.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">欺骗与领悟</font></strong><br>
<br>
在游戏关卡设计中，如果指引过于明显和简单，也会让玩家感到过于容易和无趣。所以并不是每次都要给予玩家完美的反馈，而是利用一些欺诈性行为“玩弄”玩家预期。<br>
<br>
这与叙事有着异曲同工之妙，冲突是故事的灵魂和价值所在，故事不能一帆风顺，主角总是要跌入低谷，再达到高潮，关卡在电影化游戏中一定程度上就充当了其叙事意义，所以也不能一帆风顺，总有一些地方指向了新的任务。<br>
<br>
<div align="center">
<img aid="1049565" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094905wlntanz9mmvdraqt.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094905wlntanz9mmvdraqt.jpg" width="600" id="aimg_1049565" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094905wlntanz9mmvdraqt.jpg" referrerpolicy="no-referrer">
</div><br>
当然我们不仅仅可以利用任务来使用这种遭遇困难的技巧，我们可以在我们打造的重复元素或者视觉元素上去做文章。<br>
<br>
同样是《神秘海域4》，在【拍卖会】关卡，顽皮狗的技巧被反复使用，把玩家引到错误的道路，最后发现正确的路竟然就在背后。在拍卖会通风口的时候，你总可以瞥见左边的画面，以允许你观察外面的情况，顽皮狗故意这么做，让你会错过右侧的入口。<br>
<br>
<div align="center">
<img aid="1049566" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094905x787jijwqj7qxzox.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094905x787jijwqj7qxzox.jpg" width="600" id="aimg_1049566" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094905x787jijwqj7qxzox.jpg" referrerpolicy="no-referrer">
</div><br>
而当玩家意识到“原来是这里”的时候则会获取一种恍然大悟的情感，这大概与解半天的数学题，最后终于解出来的感觉差不多。<br>
<br>
<strong>领悟和完成的感觉是很好的正反馈。</strong><br>
<br>
<strong><font color="#de5650">定义空间</font></strong><br>
<br>
接下来的几个小节会着重讲诉和拆解关于空间的定义，是关卡设计与美术紧密结合的内容。<br>
<br>
我长达15个小时徘徊在贫民窟这一章的地图中，观察各个空间的结构。不得不感叹，这绝对是教科书级别的小地图箱庭设计，所有的细节都并不是过度解读，是关卡设计师精湛的设计和长时间的打磨，我这里仅仅拆了第一层的空间设计。<br>
<br>
我们除了在一个室内以外，我们在室外也可以感觉自己在一个广义的空间内，正如第一章所讲诉的空间的场，当几个实体结构放在一片空地上，他们会相互产生场力，形成一个空间。<br>
<br>
比如你站在巨石阵中，即使只有一些石头，但是他们仍然让你感觉你处于空间中。<br>
<br>
<div align="center">
<img aid="1049567" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094905fwr6t8wymrz6ro0u.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094905fwr6t8wymrz6ro0u.jpg" width="600" id="aimg_1049567" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094905fwr6t8wymrz6ro0u.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">用点定义空间</font></strong><br>
<br>
我们可以使用点来定义空间，分别放置四个杂物或者其他实体在四个点上，这时候杂物充当了点的作用，这种案例在实际游戏关卡中其实是比较难找的，但是恰好游戏中有着这样的空间。<br>
<br>
<div align="center">
<img aid="1049568" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094905ffznhyp1dnjwwpwo.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094905ffznhyp1dnjwwpwo.jpg" width="600" id="aimg_1049568" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094905ffznhyp1dnjwwpwo.jpg" referrerpolicy="no-referrer">
</div><br>
虽然没有太多的高度和体积感，但是这个空间有一种联系感，这些杂物创造了一个正形空间。它们与外面的负形空间是对立的，你会觉得置身于这些杂物中有一种封闭感，这也同样划分了这两个npc（这个我们后面再谈）<br>
<br>
可以上面的看到左侧的铁桶是层叠的，它们已经不是一个完美的点了，它们有点像一条线。它带有一种方向感，它们暗示了这里有一个空间的体积和意图。<br>
<br>
<strong><font color="#de5650">用线定义空间</font></strong><br>
<br>
让我们放入一个完整的柱子进去，这个柱子的主要意义在于定义了一个空间体积的上限。<br>
<br>
即使四个角的点并不完整了，但是一条线的加入仍然让这个空间被定义了。这形成了一个更明确的边界，至少比点更清楚，创造了一种沿着地面的正方形图像，创造了体积感。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049569" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094906e32635h23973m5h6.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094906e32635h23973m5h6.jpg" width="600" id="aimg_1049569" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094906e32635h23973m5h6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">为什么屋顶上要放一个叠这么高的路障，是不是过度解读了</font></font></div><br>
当这条引导用的霓虹灯线和柱子连接，中间使用路障加固这个形体，这形成更多隐形的线，它们创造了一个平面的强烈图像，线性元素能够创造出一种可以度量空间的感觉。<br>
<br>
<div align="center">
<img aid="1049570" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094906waznwi46zqz4nlci.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094906waznwi46zqz4nlci.jpg" width="600" id="aimg_1049570" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094906waznwi46zqz4nlci.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">用面定义空间</font></strong><br>
<br>
上图使用了虚拟的面来定义空间，当然也借助了底面，面对于空间的定义已经非常直接了。<br>
<br>
面可以简单分为三种类型：<strong>底面（地面）、墙面、顶面。</strong><br>
<br>
这三个平面的类型，影响了我们如何寻找空间，也影响了我们如何想象空间，以及我们如何与空间互动和被空间影响。<br>
<br>
<strong>用地面定义空间</strong><br>
<br>
如果想要打造体积感，用地面是很难做到的，但把它和一些线性元素结合起来很快就会唤起那种感觉。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049571" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094906xovdedb2oobb4u5l.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094906xovdedb2oobb4u5l.jpg" width="600" id="aimg_1049571" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094906xovdedb2oobb4u5l.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">仅仅使用一条线</font></font></div><br>
将它与单一的线结合，就可以几乎创造整个体积感，虽然看不见这个结构任何的其他细节，但是这个结构的概念依然存在。<br>
<br>
当然我们也可以只是用一个具有体积的地面来打造一个不是那么具有体积感的开放空间。<br>
<br>
<div align="center">
<img aid="1049572" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094907xezl5l2ehqsg5arb.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094907xezl5l2ehqsg5arb.jpg" width="600" id="aimg_1049572" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094907xezl5l2ehqsg5arb.jpg" referrerpolicy="no-referrer">
</div><br>
我们仅仅使用台阶，无论是往高还是内凹，会让我们的结构更稳定，为了进入这个空间有了更多的障碍，我们必须走上台阶，当然从进入来说并不是很大的障碍。但这很重要，这把它定义成一个有作用的空间。<br>
<br>
如果使用陷入地面的方法来观察它，可能会更具有体积感，这实际上更像是对一个既定空间的观察，而不是上台阶。<br>
<br>
<div align="center">
<img aid="1049573" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094907uhalhg299zhl5u0b.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094907uhalhg299zhl5u0b.jpg" width="600" id="aimg_1049573" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094907uhalhg299zhl5u0b.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>用墙面定义空间</strong><br>
<br>
当然你也可以用墙面来打造空间，是同样的道理。比如说利用一个完整墙面和一些矮墙或者栏杆。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049574" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094907m6f0kkzkk9v5ekkk.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094907m6f0kkzkk9v5ekkk.jpg" width="600" id="aimg_1049574" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094907m6f0kkzkk9v5ekkk.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">为什么盆栽放在右侧角落而不是中间</font></font></div><br>
这个空间很有意思，各位现在应该知道为什么盆栽和桌子杂物要放在左右侧角落了。但是这个空间的这块木板斜坡，把原本定义空间的台阶打破了，衔接和外部的空间。这个空间应该当成一个单空间内的子空间来看待，铁桶堆也印证了这一点。<br>
<br>
<div align="center">
<img aid="1049575" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094907e93sx9u6z66ymuxu.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094907e93sx9u6z66ymuxu.jpg" width="600" id="aimg_1049575" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094907e93sx9u6z66ymuxu.jpg" referrerpolicy="no-referrer">
</div><br>
这个后面我们再讲。<br>
<br>
<strong>用顶面定义空间</strong><br>
<br>
很少有只使用一个顶面来打造空间的例子，就像上图，很多顶面是无法单独存在的（在物理情况下），它需要一些支撑物。但是《Stray》中就有，不然为什么叫做教科书呢？<br>
<br>
<div align="center">
<img aid="1049576" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094908r2hbu63hl2hz2dz2.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094908r2hbu63hl2hz2dz2.jpg" width="600" id="aimg_1049576" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094908r2hbu63hl2hz2dz2.jpg" referrerpolicy="no-referrer">
</div><br>
当我们谈到圈地的时候，关注的想法除了定义以及空间如何被很好地定义之外，还有一些点：<br>
<br>
<ul><li>观众是否能够理解你试图表达的空间类型？</li><li>空间是正形空间还是负形空间？</li><li>如何影响玩家路线的流动？</li><li>空间是如何被定义，如何暗示空间？</li><li>空间中的空间是如何影响整体的？<br>
</li></ul><br>
就比如这个用顶面定义的空间，它是开放的，它的正形性很低，玩家几乎不会在这里停留太久。<br>
<br>
<div align="center">
<img aid="1049577" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094908avq8284tq7qrvrnv.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094908avq8284tq7qrvrnv.jpg" width="600" id="aimg_1049577" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094908avq8284tq7qrvrnv.jpg" referrerpolicy="no-referrer">
</div><br>
当我们定义了空间，我们可以使用上一章里的【调整空间定义】的方法，来对于玩家认知这个空间，以及这个空间的开放程度进行调节，这有利于控制玩家对于自己目前的空间位置的认知，以及出入一个空间的意图影响。我这里不再赘述。<br>
<br>
<strong><font color="#de5650">多空间构成</font></strong><br>
<br>
空间的构成和图像的构成很多时候是息息相关的，其本质上的差异只是三维与二维的不同，人们在理解空间上，很多时候仍然依靠视觉图像上的思维去认知。这里就不提及图像构成的内容了。<br>
<br>
<div align="center">
<img aid="1049578" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094908s88z7q9ag7dbhn7a.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094908s88z7q9ag7dbhn7a.jpg" width="600" id="aimg_1049578" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094908s88z7q9ag7dbhn7a.jpg" referrerpolicy="no-referrer">
</div><br>
假设这是一个空间建筑的顶视图，我们很难通过场景来理解，这些物体是如何联系组织的，这里有太多的信息了，没有什么特殊的意义，这么多身份意味着所有身份在这里都是失去了。<br>
<br>
但是我们仍然可以对其进行一些归类，因为他们的长短是有异同之处的。<br>
<br>
我们可以用各种方法去加强他们之间的联系性，比如大小，形状，颜色。我这里就使用颜色。<br>
<br>
<div align="center">
<img aid="1049579" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094909z6556f2f3k54665x.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094909z6556f2f3k54665x.jpg" width="600" id="aimg_1049579" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094909z6556f2f3k54665x.jpg" referrerpolicy="no-referrer">
</div><br>
可以看到，即使在左上角的矩形与其他的矩形没有连接关系，但是我们仍然能感受到他们之间有某种联系。<br>
<br>
我们可以看到一些不同的空间之间彼此关联，当我们进入空间构成，空间构成帮助我们布置空间，探索空间，我们了解我们的位置，我们在整个空间的位置。更多时候我们使用连接，或者其他更隐晦的方式来联系多个空间。<br>
<br>
<strong><font color="#de5650">节点网格与决策点</font></strong><br>
<br>
这是贫民窟关卡的第一层空间地图。<br>
<br>
<div align="center">
<img aid="1049580" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094909xlk10lc0c99scc09.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094909xlk10lc0c99scc09.jpg" width="600" id="aimg_1049580" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094909xlk10lc0c99scc09.jpg" referrerpolicy="no-referrer">
</div><br>
我们可以画出这个空间玩家的行进路线可能。虽然他们肯定会走弯路或者斜线，甚至可能在一些地方绕圈，但本质上是这样的。<br>
<br>
<div align="center">
<img aid="1049581" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094909jd2d4hvvvvjpvqdd.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094909jd2d4hvvvvjpvqdd.jpg" width="600" id="aimg_1049581" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094909jd2d4hvvvvjpvqdd.jpg" referrerpolicy="no-referrer">
</div><br>
玩家可能在一些位置发生选择，我们叫做决策点。<br>
<br>
<div align="center">
<img aid="1049582" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094909n48d5u6kn7m8nrkk.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094909n48d5u6kn7m8nrkk.jpg" width="600" id="aimg_1049582" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094909n48d5u6kn7m8nrkk.jpg" referrerpolicy="no-referrer">
</div><br>
在建筑学中的寻路设计里，这被称为节点网格（Node Network）。<br>
<br>
本质上，这就是给玩家发信息，当你创造关卡的时候，你应该想在哪里保证玩家会经过，我想让他们把注意力转移到哪里。<br>
<br>
一旦进入这个空间，我们需要给玩家设置一个探索的步骤构图，这些空间如何引导玩家流向另一个空间。你可以发现在贫民窟关卡的决策点附近，一般都有明显的指向性方式或者指示牌。<br>
<br>
<div align="center">
<img aid="1049583" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094910wfp78fzczymzd8f5.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094910wfp78fzczymzd8f5.jpg" width="600" id="aimg_1049583" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094910wfp78fzczymzd8f5.jpg" referrerpolicy="no-referrer">
</div><br>
而每个决策点，都是一个玩家会经过的关键点，是单独的摄像机镜头，静态的图像，但这一整个关卡整体流动的是空间构成，比如建筑和建筑，空间和空间是如何连接的。<br>
<br>
我们可以回头使用玩家第一次进入贫民窟的关卡流向来举例。<br>
<br>
<strong><font color="#de5650">利用空间构成打造叙事节奏</font></strong><br>
<br>
单个空间打造的Mood是固定，我们姑且称之为“氛围”；而多空间之间切换时，可以理解为多个氛围之间变换，这形成了叙事的节奏。<br>
<br>
空间构成传达世界观，利用建筑和空间构成，尤其是空间的层次和组织，它能够讲述很多特定空间的意图。<br>
<br>
<div align="center">
<img aid="1049584" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094910qal41a4t5474ij5z.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094910qal41a4t5474ij5z.jpg" width="600" id="aimg_1049584" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094910qal41a4t5474ij5z.jpg" referrerpolicy="no-referrer">
</div><br>
当玩家第一次进入这个空间，狭窄的通道加上前侧的冷光，这里的氛围是谨慎小心的，有一些胆怯。而远处的暖黄色光则让人觉得那里的空间氛围会更温暖，更安全。<br>
<br>
<div align="center">
<img aid="1049585" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094910ikl0q0o02znr3pv0.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094910ikl0q0o02znr3pv0.jpg" width="600" id="aimg_1049585" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094910ikl0q0o02znr3pv0.jpg" referrerpolicy="no-referrer">
</div><br>
不幸的是当机器人原住民发现我们之后拉响了警报，全新的红色光效出现，加上BGM和这里狭窄的空间构成，我们开始紧张起来，叙事节奏加快。<br>
<br>
与此同时，玩家的移动意向也加强，大多数玩家会加快脚步前往下一个空间。<br>
<br>
<div align="center">
<img aid="1049586" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094910oqqt8qqqpt2upn2v.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094910oqqt8qqqpt2upn2v.jpg" width="600" id="aimg_1049586" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094910oqqt8qqqpt2upn2v.jpg" referrerpolicy="no-referrer">
</div><br>
当我们来到这个空间时，蓝色的墙和青黄色的灯光，打散了红光的危机感，空间构成也更加开阔。好奇的氛围取代了之前的紧张感，玩家会倾向于在这里进行一些观察，当然这里也很值得观察，这里有奶奶的围巾店，编程店和路牌。<br>
<br>
特别是围巾店，这是一个元素很多的空间，并且它是面向路口开放的，可以进入这个空间进行一段时间的探索，这里面是一个单独的正形空间！<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049587" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094911gzhkk8xdu1h8d8ld.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094911gzhkk8xdu1h8d8ld.jpg" width="600" id="aimg_1049587" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094911gzhkk8xdu1h8d8ld.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">奶奶第一次是不在的</font></font></div><br>
这是同时使用了三个面（地面，墙面，顶面）以及许多点与线的元素打造的空间，它的正形性是非常完善的，它有强烈的理由让玩家在里面看一看。<br>
<br>
当然这里的地毯也是一个会让玩家稍作停留的空间（反正我是跟这个招财猫玩了一会<br>
<br>
<div align="center">
<img aid="1049588" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094911bor1k1soyyosn9rp.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094911bor1k1soyyosn9rp.jpg" width="600" id="aimg_1049588" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094911bor1k1soyyosn9rp.jpg" referrerpolicy="no-referrer">
</div><br>
接下来我们转过弯之后，又重新被警报灯和红光带回略微紧张的情绪。这里有一小段台阶，如果你注意的话，这台阶的正上方有一段管道穿过上空，这个细节我们后面会提到。<br>
<br>
<div align="center">
<img aid="1049589" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094911kpakdfj9s0zd4wzj.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094911kpakdfj9s0zd4wzj.jpg" width="600" id="aimg_1049589" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094911kpakdfj9s0zd4wzj.jpg" referrerpolicy="no-referrer">
</div><br>
如果你这时候在这个台阶两侧左右横跳，你会很明显感受到两种不同的氛围在这里被无形的墙隔离。<br>
<br>
<div align="center">
<img aid="1049590" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094912qj8gwhw4m6dws844.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094912qj8gwhw4m6dws844.jpg" width="600" id="aimg_1049590" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094912qj8gwhw4m6dws844.jpg" referrerpolicy="no-referrer">
</div><br>
我并不觉得这是PPV的作用，我认为很大程度上这里的氛围取决于玩家身上是什么颜色的灯光效果，这其实是色彩心理学的进一步内容。<br>
<br>
当红色的光占领了那一块区域的GI时，玩家一旦进入光照探针范围内，身上的光即会变红，人们对于自己身上的颜色非常在意，当你身上被红光渗透时，你感到更加紧张。<br>
<br>
我在Research《刺客信条：英灵殿》的Lightning时，也同样发现了这样的意图。当玩家进入那块灯光GI下时，气氛开始变得令人紧张。<br>
<br>
当来到这里时，你是否会觉得接下来会进行战斗？可以想想是什么影响了你的判断。<br>
<br>
<div align="center">
<img aid="1049591" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094912sby1c7lx4meyl5ty.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094912sby1c7lx4meyl5ty.jpg" width="600" id="aimg_1049591" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094912sby1c7lx4meyl5ty.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">在决策点打造关键构图</font></strong><br>
<br>
很多时候，决策点的镜头是很单纯的。单纯的艺术表达，什么感觉好，什么有趣，让人兴奋。我们希望玩家能够感受到他们不断移动的空间，有很多很棒的静态构图，这让我们感到关卡很有活力，赏心悦目。<br>
<br>
当我在这里发现这面青蓝色的墙被红光影响时，是非常漂亮的，并且远处的路灯和指示牌也是很完美的构图。<br>
<br>
<div align="center">
<img aid="1049592" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094912q141zmf21c3ansk9.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094912q141zmf21c3ansk9.jpg" width="600" id="aimg_1049592" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094912q141zmf21c3ansk9.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">色彩故事板（Color Script）</font></strong><br>
<br>
色彩脚本是一个用于讲述故事的画面插图集，我们在整个游戏中应用的颜色脚本阐述每个关卡的色调和氛围。<br>
<br>
这是一个游戏关卡设计前期的美术脚本，是关卡构成，色彩，当然包括灯光的指导脚本，它将会定义一个关卡的节奏是什么样的叙事节奏。<br>
<br>
正如我们上面小节提到的利用空间打造故事节奏，这种方案不仅仅是被使用在《Stray》中，在很多游戏中也同样被使用。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049593" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094913y6mmg6mfm699gfww.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094913y6mmg6mfm699gfww.jpg" width="600" id="aimg_1049593" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094913y6mmg6mfm699gfww.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《SIFU》色彩脚本</font></font></div><br>
最基础的“起承转合”，游戏关卡也遵循这个叙事节奏原理，我们在第一次进入【贫民窟】关卡时正是这样的节奏。<br>
<br>
<strong><font color="#de5650">空间组织</font></strong><br>
<br>
正如上面【多空间构成】小节所述，当我有多个空间时，如果他们是无序的，身份混乱的，那么是非常难以让人理解的。我们需要为其进行构图，就像图像一样，创造它们之间的联系与差异，通过规则和对比来方便于理解。<br>
<br>
<div align="center">
<img aid="1049594" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094913hg0dzbxrxzgq5v99.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094913hg0dzbxrxzgq5v99.jpg" width="600" id="aimg_1049594" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094913hg0dzbxrxzgq5v99.jpg" referrerpolicy="no-referrer">
</div><br>
如果玩家的决策点是如此多的，且关卡流向是复杂的，这让这些空间看起来并没有什么联系，很多时候它们甚至没有连接在一起。<br>
<br>
为此，关卡设计师在规划玩家第一次进入的路线时，制造了很多限制，让玩家只能按照设计师的意图进行空间流动。因为玩家最后是需要在电梯间前进行过场动画剧情的。<br>
<br>
<div align="center">
<img aid="1049595" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094913go4nzzf8ilf4zzhn.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094913go4nzzf8ilf4zzhn.jpg" width="600" id="aimg_1049595" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094913go4nzzf8ilf4zzhn.jpg" referrerpolicy="no-referrer">
</div><br>
关卡设计师使用了可关闭的门和不可直接通过的铁丝网来限制玩家的流向，并且限制跳跃。确保玩家按照规划到达目标区域。<br>
<br>
除了门和铁丝网之外，还有我们之前谈论定义空间时候使用的一些元素，比如台阶。<br>
<br>
<div align="center">
<img aid="1049596" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094914lphr1hqrpt7mhshv.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094914lphr1hqrpt7mhshv.jpg" width="600" id="aimg_1049596" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094914lphr1hqrpt7mhshv.jpg" referrerpolicy="no-referrer">
</div><br>
这些边界给空间定义了组织，哪几个空间是连接的，哪一些空间的身份是相同或者有联系的。通过边界去进行归类和组织，有关系的空间同归属在一个组织下，这也与世界观和空间内的叙事有关系。<br>
<br>
<div align="center">
<img aid="1049597" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094914vakm1kooaiapaeka.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094914vakm1kooaiapaeka.jpg" width="600" id="aimg_1049597" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094914vakm1kooaiapaeka.jpg" referrerpolicy="no-referrer">
</div><br>
空间组织并不是完全跟距离呈正比关系，而是在于如何通过划分去组织空间。<br>
<br>
坐在【编程店】门前面的两位NPC，完全跟编程空间组织下的理性身份不符合，而于【奶奶编织】的感性形象更类似，并且它们有着类似的元素——披巾。因此这里的阶梯是非常必要的，它划分了空间组织，把主导空间给确定下来。<br>
<br>
<div align="center">
<img aid="1049598" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094914pdzlfedxjwq2jxx2.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094914pdzlfedxjwq2jxx2.jpg" width="600" id="aimg_1049598" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094914pdzlfedxjwq2jxx2.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">主导空间</font></strong><br>
<br>
我对于上面划分出来的空间组织进行了简要的身份和其代表的内涵描述。<br>
<br>
<div align="center">
<img aid="1049599" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094915iefe7v7d4et7du3e.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094915iefe7v7d4et7du3e.jpg" width="600" id="aimg_1049599" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094915iefe7v7d4et7du3e.jpg" referrerpolicy="no-referrer">
</div><br>
一般空间的组织中，会存在主导空间和其卫星空间，主导空间对其卫星空间具有支配关系，可以理解为主导空间的身份会溢出到卫星空间，卫星空间会拥有主导空间的属性。<br>
<br>
有很多因素会影响一个空间组织中的主导关系，如何让一个空间成为主导空间，这里简单来说就是一个有着强身份的空间，影响了周围的空间。<br>
<br>
<strong><font color="#de5650">划分空间组织</font></strong><br>
<br>
划分空间组织的方法本质上和定义空间是类似的，比如我们看【死路口】这块区域，为什么它的空间组织到达这里就中断了？<br>
<br>
<div align="center">
<img aid="1049600" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094915gyphfg3fpfjxgps3.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094915gyphfg3fpfjxgps3.jpg" width="600" id="aimg_1049600" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094915gyphfg3fpfjxgps3.jpg" referrerpolicy="no-referrer">
</div><br>
这里的空间地面上有一个木板倒在这条线上，创造了一个线的划分，而上面顶面也与【死路口】的组织空间不同，形成了一个边界。<br>
<br>
<div align="center">
<img aid="1049601" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094915kmqo3mq80amspjus.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094915kmqo3mq80amspjus.jpg" width="600" id="aimg_1049601" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094915kmqo3mq80amspjus.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049602" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094915b1gjmevj2e2cc2ul.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094915b1gjmevj2e2cc2ul.jpg" width="600" id="aimg_1049602" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094915b1gjmevj2e2cc2ul.jpg" referrerpolicy="no-referrer">
</div><br>
在游戏中，当玩家走过这个边界之后，可以明显的感觉到氛围的不同，类似的例子还有很多。<br>
<br>
在贫民窟也有一些弱划分的例子，比如在洗衣店门口的区域，使用从天上穿过的管道进行划分。<br>
<br>
<div align="center">
<img aid="1049603" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094916uqsqlxe08j0l6qwc.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094916uqsqlxe08j0l6qwc.jpg" width="600" id="aimg_1049603" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094916uqsqlxe08j0l6qwc.jpg" referrerpolicy="no-referrer">
</div><br>
这些结构和定义与“门”的作用相似，目的在于让玩家知道自己来到了一个新的空间组织内，这里有全新的空间身份。同样我们也可以使用氛围来区分身份，比如使用灯光来切换氛围。<br>
<br>
<div align="center">
<img aid="1049604" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094916h2xhww9s0zpgpaga.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094916h2xhww9s0zpgpaga.jpg" width="600" id="aimg_1049604" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094916h2xhww9s0zpgpaga.jpg" referrerpolicy="no-referrer">
</div><br>
空间的组织非常重要，因为其可以帮助玩家快速地记住这些空间之间的关系，就像在文字游戏时，随机无序的词组会让我们难以记住，而将其归类成有意义的近义词进行记忆时，则拥有了层次，这会把书面练习变为思考练习。<br>
<br>
当我们的空间具有联系时，它们会变成一种相对关系，玩家可以很快理解整个关卡地图的关系。<br>
<br>
<strong><font color="#de5650">空间身份与叙事</font></strong><br>
<br>
当我们在一个空间组织内时，我们可以通过其中的元素来获取这个空间的身份，而其中的叙事也需要具有联系性。同样我们也可以通过其叙事内容，来对空间的组织进行划分。<br>
<br>
在《Stray》中我们可以通过与NPC进行对话，来了解这一空间组织下的身份归属。比如在【洗衣店】门前的这个通过上方管道的弱划分，其实并没完全将这两块区域分开，而是一种父子关系。<br>
<br>
<div align="center">
<img aid="1049605" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094916wf6q6qqozqc3uq3c.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094916wf6q6qqozqc3uq3c.jpg" width="600" id="aimg_1049605" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094916wf6q6qqozqc3uq3c.jpg" referrerpolicy="no-referrer">
</div><br>
我们可以通过一位NPC进行验证。<br>
<br>
<div align="center">
<img aid="1049606" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094917oww205b3ssmfqfms.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094917oww205b3ssmfqfms.jpg" width="600" id="aimg_1049606" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094917oww205b3ssmfqfms.jpg" referrerpolicy="no-referrer">
</div><br>
这位坐在角落的NPC虽然距离洗衣店门口有一些距离，并且是被管道划分在外的，但是它仍是归属于【洗衣/油漆店】的组织下。它仍在谈论着楼上那两个家伙，这里有一种生活的日常感。<br>
<br>
空间的叙事内容除了被这个空间本身自带的身份属性，比如【酒吧】的安逸随性，也被空间中的一些特殊元素所影响。这个在电梯间里的“寺庙”就是最好的例子。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049607" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094917h6z74gtu7xu5uu7c.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094917h6z74gtu7xu5uu7c.jpg" width="600" id="aimg_1049607" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094917h6z74gtu7xu5uu7c.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">为什么这里是个寺庙？</font></font></div><br>
<strong><font color="#de5650">空间的象征意义</font></strong><br>
<br>
可能接下来的内容会偏向哲学，可能可以当作一些参考或者抛砖引玉的解读，我想这一部分文案策划同学会更感兴趣，当然这也是美术发展为艺术应该拥有的知觉。<br>
<br>
<strong>纪念性建筑</strong><br>
<br>
<div align="center">
<img aid="1049608" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094917tfzuutovmrf8tve2.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094917tfzuutovmrf8tve2.jpg" width="600" id="aimg_1049608" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094917tfzuutovmrf8tve2.jpg" referrerpolicy="no-referrer">
</div><br>
纪念性在建筑学中，是指一种可以唤起一种伟大的光环，一种要求公众认可的力量和重力感特性的建筑。通常是大教堂，寺庙之类的。这些空间是拥有很高的顶面，用于激发敬畏的，通过极高的顶面，在我们无法触及的地方。<br>
<br>
这个设计利用了原来宗教建筑的纪念性，让政府或政权取代了神的角色，为了让机器人们去赞美和崇拜它。这个世界观中的上层权力机构成为一种新的宗教。<br>
<br>
<strong>电梯间寺庙</strong><br>
<br>
这个电梯间寺庙是很有趣的一个空间，首先它位于这座纪念性建筑的最底层，它代表了被压迫的意义。其次，它是一个很封闭的场所，它的有三个墙面，门也是卷帘门，类似于墙面。<br>
<br>
<div align="center">
<img aid="1049609" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094918f4bjqyxbjyjbsij2.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094918f4bjqyxbjyjbsij2.jpg" width="600" id="aimg_1049609" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094918f4bjqyxbjyjbsij2.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>墙面</strong><br>
<br>
墙面代表社会，主要用来创造空间的边界，和我们的基平面相反。我们通过触摸与它互动，只有在我们想和墙面对抗的时候，我们才会选择互动。<br>
<br>
所以墙面是对立的，因为它们会限制我们的能力，可能还限制了我们无声地运动，我们不能轻易地通过它们，需要对抗它，但它们也可以让人感到舒适，它们可以很友好，提供隐私和安全，免受敌人伤害。<br>
<br>
四个墙面代表着这个空间中的居民的胆怯，守旧。如果你给它们出示一些“外来者”的物品时，你会得到不可能离开这里的回答。<br>
<br>
顶面本该是很高的，但是因为电梯的掉落，吊在上方，用一些篷布临时保护了上方的空间。<br>
<br>
<div align="center">
<img aid="1049610" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094918k6cmswu9u9db0zwz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094918k6cmswu9u9db0zwz.jpg" width="600" id="aimg_1049610" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094918k6cmswu9u9db0zwz.jpg" referrerpolicy="no-referrer">
</div><br>
如果我们走进里面，去翻译墙上的内容时，我们会知道，它们的信仰对象是人类。掉落的顶面意味着它们的信仰已经陨落。<br>
<br>
<strong>顶面的象征</strong><br>
<br>
它的存在比其他两个面有着更强烈的庇护和封闭的感觉，你知道顶面就在上方，并不只是物理边界，它们倾向于定义一种情感基调。<br>
<br>
<div align="center">
<img aid="1049611" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094918g8d56k66dieep5d6.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094918g8d56k66dieep5d6.jpg" width="600" id="aimg_1049611" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094918g8d56k66dieep5d6.jpg" referrerpolicy="no-referrer">
</div><br>
我们第一次发觉我们一直处于一个穹顶之下是在这里。而后我们的剧情也暗示了这个世界观：人类为了在环境恶化中庇护自己，把自己关在了这个穹顶之下，但是却没想到因为封闭权力机构的自私贪婪，让人类最终走向了灭绝。<br>
<br>
而这个穹顶，包括这个纪念性的电梯，也会一直伴随游戏的世界观，在后续都会遇到信仰权力机构宗教的信徒和类似的穿着的机器人。<br>
<br>
<strong>空间层次象征</strong><br>
<br>
如果学过高中地理，应该知道高档住宅区一般都会选择位于上风上水的地方。上风，即风向的上风向；上水，即地势高的地方。住的地势高逐渐成为了一种地位的象征，对于空间来说也是如此。<br>
<br>
在【贫民窟】这个关卡中，有着向往中城区，逃离贫民窟的“外来者”都住在，或者曾经住在高层公寓里。<br>
<br>
<div align="center">
<img aid="1049612" zoomfile="https://di.gameres.com/attachment/forum/202208/11/094919a8t7jm4z9hjtzppz.jpg" data-original="https://di.gameres.com/attachment/forum/202208/11/094919a8t7jm4z9hjtzppz.jpg" width="600" id="aimg_1049612" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/094919a8t7jm4z9hjtzppz.jpg" referrerpolicy="no-referrer">
</div><br>
而向往真实的蓝天的NPC，也躺在楼顶，最高权力机构则在电梯顶层，最守旧的信徒在电梯底层。这些都是空间层次的象征。<br>
<br>
<i><font color="#808080">未完待续</font></i><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/550192071</font></font><br>
<br>
  
</div>
            