
---
title: '《怪物猎人崛起》：卡普空如何在Switch上做优化'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/27/140815qp7yppdjhjyw6nc2.jpg'
author: GameRes 游资网
comments: false
date: Fri, 27 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/27/140815qp7yppdjhjyw6nc2.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2511980">
<div align="center">
<img id="aimg_1004302" aid="1004302" zoomfile="https://di.gameres.com/attachment/forum/202108/27/140815qp7yppdjhjyw6nc2.jpg" data-original="https://di.gameres.com/attachment/forum/202108/27/140815qp7yppdjhjyw6nc2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/27/140815qp7yppdjhjyw6nc2.jpg" referrerpolicy="no-referrer">
</div><br>
© Capcom<br>
<br>
怪物猎人 Rise已经推出了几个月，销量惊人，同时也展示了Switch硬件在右手中的功能。该系统中使用RE Engine的仅有的两部作品之一-另一部是Ghosts ' n Goblin Resurrection -将该系列带到了任天堂硬件的另一个层面，同时成功地保留了上一代作品的视觉外观和魅力。<br>
<br>
<strong>然而， 《 怪物猎人 ：世界》的技术方面很有趣。 《 怪物猎人 ：世界》似乎一直超出了任天堂混合系统的能力，然而，该游戏的许多更新方法都有了提升。拥有众多加载屏幕的分割地图时代被无缝的开放区域所取代，而新的游戏玩法允许玩家快速甚至垂直地穿越环境。虽然《 怪物猎人 ：世界》和《世界》的视觉风格不同，但它们的共同点远远超过许多人可能意识到的。</strong><br>
<br>
<strong>这一点最近得到了加强-我们有一个很好的机会向怪物猎人 Rise总监Yasunori Ichinose提问。这次采访的重点是游戏的技术开发，当然还有Capcom旗舰RE Engine的实现。</strong><br>
<br>
<div align="center">
<img id="aimg_1004303" aid="1004303" zoomfile="https://di.gameres.com/attachment/forum/202108/27/140816zd3r3iqt4ptpte9n.jpg" data-original="https://di.gameres.com/attachment/forum/202108/27/140816zd3r3iqt4ptpte9n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/27/140816zd3r3iqt4ptpte9n.jpg" referrerpolicy="no-referrer">
</div><br>
© Capcom /任天堂生活<br>
<br>
<strong>任天堂生命：在任天堂Switch上使用RE引擎用于怪物猎人 Rise的主要技术原因是什么？</strong><br>
<br>
<strong>Yasunori Ichinose ：主要的技术原因是我们可以使用RE Engine强大的C#脚本系统，更不用说RE Engine的最新图形特性（如果硬件规格允许的话）。在MT框架中，所有游戏逻辑都是在C++中实现的，所以构建时间是一个问题；在RE Engine中，游戏逻辑是在C#中实现的，所以构建时间可以大大减少（大约10秒，在C++中需要100倍的时间）。这允许快速迭代尝试和错误，使游戏更有趣。它不是直接可见的，但它是开发的一个非常重要的部分，我认为它间接地促进了游戏的乐趣。</strong><br>
<br>
<strong>除了鬼魂和妖精的复活，这是任天堂硬件上使用引擎的罕见例子。核心RE引擎团队在多大程度上调整了工具以适应开关？</strong><br>
<br>
最初的性能相当严峻，必须进行重大的优化。<br>
<br>
RE Engine从一开始就设计了多个平台，所以简单的移植本身并不那么困难。然而，使用核心图形元素（这涉及任天堂Switch略微独特的图形API NVN）来开发Shader程序的翻译器是相当困难的。<br>
<br>
在RE Engine中，着色器程序是用HLSL（高级着色器语言）编写的，但我们必须实现一个新的翻译器来将它们转换为GLSL（OpenGL着色器语言）。在这个翻译器中，我们实现了一些技巧来输出从HLSL转换为GLSL时的最佳代码，以实现GPU的性能。我们还专门为任天堂Switch GPU添加了支持。例如，我们添加了对ASTC（自适应可伸缩纹理压缩）的支持，这是一种纹理压缩格式，在减少内存和数据大小方面非常有用。<br>
<br>
<strong>早期的RE引擎测试和计划中的Rise可视化是否返回了强大的结果，或者是否需要进行重大的优化以实现您想要的性能？</strong><br>
<br>
最初的性能相当严峻，主要的优化是必须的。首先，我们将图形管道从基于延迟的管道切换到基于前向的管道。过去， RE ENGINE使用基于延迟渲染的图形管道。然而，由于任天堂交换机预期内存带宽，我们为怪物猎人提升构建了一个新的正向渲染图形管道。然后我们逐个进行了许多优化，从大到小。<br>
<br>
这些优化的例子包括：烘焙/应用阴影，应用GPU遮挡剔除，并以新的轻量级替代DOF（视野深度）等。还进行了许多其他杂项优化，包括：以简化计算代替过于严格的计算，以像素着色实现代替计算机着色实现，并添加剔除过程。我们还与艺术家合作调整光线的影响区域，因为光源计算过程在光线太多的区域变得非常繁重。<br>
<br>
<div align="center">
<img id="aimg_1004304" aid="1004304" zoomfile="https://di.gameres.com/attachment/forum/202108/27/140816lgejqbavfqxnz9ga.jpg" data-original="https://di.gameres.com/attachment/forum/202108/27/140816lgejqbavfqxnz9ga.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/27/140816lgejqbavfqxnz9ga.jpg" referrerpolicy="no-referrer">
</div><br>
© Capcom /任天堂生活<br>
<br>
<div align="center">
<img id="aimg_1004305" aid="1004305" zoomfile="https://di.gameres.com/attachment/forum/202108/27/140817yjyy9kppppymtu68.jpg" data-original="https://di.gameres.com/attachment/forum/202108/27/140817yjyy9kppppymtu68.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/27/140817yjyy9kppppymtu68.jpg" referrerpolicy="no-referrer">
</div><br>
© Capcom /任天堂生活<br>
<br>
<strong>就像之前的怪物猎人世界一样， Rise利用了更大、更无缝的环境-这种方法的最大好处是什么？</strong><br>
<br>
在《 怪物猎人崛起》中，你现在可以执行高度灵活的动作，比如跑墙和使用wirect 。你也可以在骑一个新的伙伴角色Palamute时快速绕场，该角色在无缝环境中工作得很好。<br>
<br>
<strong>虽然它是一个新引擎，但视觉设计确实与之前的Wii 、 3DS和Wii U项目有相似之处。 Can你解释了你是如何进化出这种外观的，尽管它的分辨率和细节水平更高？</strong><br>
<br>
为了使怪物猎人上升的新怪物与以往游戏中具有非常不同模型规格的怪物适应同一领域，我们在与运动团队反复验证后，仔细地进行了纹理表达式、多边形计数和关节数量。头发的表达是最困难的部分，但当怪物猎人 : World的阴影可以移植时，它得到了解决。<br>
<br>
<strong>Can你谈到了这个项目中的大量动画工作？例如，这代表了与前3DS作品相比有多大的进步？</strong><br>
<br>
由于任天堂Switch的规格，使用3DS时代的数据本来是最容易的，但自从怪物猎人 : World最近发布以来，让怪物猎人崛起看起来尽可能现代化是很重要的。<br>
<br>
由于任天堂Switch的规格，使用3DS时代的数据本来是最容易的，但自从怪物猎人 : World最近发布以来，让怪物猎人 Rise看起来尽可能现代化是很重要的。从处理的角度来看，最好有更少的关节，运动的柔软性和高度的表达自由。这是我们不想削减的一个元素，所以我正在与程序员密切合作和咨询。 怪物猎人 : World的角色尽可能地保持不变，而一些新角色是通过与模型团队协商创建的，我们将关节切割到最后一分钟。谈到面部动画， 怪物猎人 : World的足够数量的关节是一个不可能的数字，所以我们努力确定这个游戏的数字，然后进行面部护理。<br>
<br>
至于动画工作，我们首先确保怪物猎人 : World的数据可以移植过来。修改和减少链和辅助接头是一项需要建模人员和程序员更多工作的任务。除了怪物猎人 : World Attors and Movies之外， " Wyvern Riding "作为怪物猎人 Rise的一个新功能被添加，所以我们需要创建的动作数量大大增加。创建攻击、动作和技术所需的时间很高，由于还添加了" Wyvern Riding "动作，敌人动画团队由于材料、创建时间和公司成立后检查的数量太大，遇到了困难。<br>
<br>
在球员方面，我们包括很多空中行动，涉及线虫行动和使用墙壁的额外行动，所以除了内部捕获，我们还得到了Katsugekiza（动作MOC - CAP团队）的帮助，以提高质量。对于NPC ，我们专注于这个游戏中每个NPC的位置和相关性。我们希望你会享受到变化的小事情，比如NPC在你来到他们的村庄时问候你的方式，或者NPC在你从一个地区移动到另一个地区后改变他们的位置的方式。<br>
<br>
<div align="center">
<img id="aimg_1004306" aid="1004306" zoomfile="https://di.gameres.com/attachment/forum/202108/27/140817rftitqtntirfrzff.jpg" data-original="https://di.gameres.com/attachment/forum/202108/27/140817rftitqtntirfrzff.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/27/140817rftitqtntirfrzff.jpg" referrerpolicy="no-referrer">
</div><br>
© Capcom /任天堂生活<br>
<br>
<div align="center">
<img id="aimg_1004307" aid="1004307" zoomfile="https://di.gameres.com/attachment/forum/202108/27/140818i0dt9vt91dvty5vc.jpg" data-original="https://di.gameres.com/attachment/forum/202108/27/140818i0dt9vt91dvty5vc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/27/140818i0dt9vt91dvty5vc.jpg" referrerpolicy="no-referrer">
</div><br>
© Capcom /任天堂生活<br>
<br>
<strong>你最自豪的是什么图形技巧和调整，让游戏看起来和表现如此出色的步骤（例如减少远程生物的帧率，分辨率调整）？</strong><br>
<br>
游戏中没有纹理流，但它是在剪切场景中完成的， NPC纹理流并仅在高分辨率的MIPMap部分加载，以提高分辨率。这允许我们在游戏中减少内存使用，同时使剪切场景看起来更好。 怪物猎人 Rise中的图形是许多精细技巧和调整的组合，我们同样为它们感到自豪。<br>
<br>
背景中的小物体（道具）在远离时被擦除，但如果它们突然消失，弹出就会突出。因此，我们使用模煳模式来逐渐擦除它们，使它们不会突出。我们还手动调整了擦除突出的单个项目的距离。由于向前渲染中没有G缓冲区，所以延迟渲染中常用的技术（SSAO和SSR）不能像现在这样使用，但它们是以创造性的方式实现的。 SSAO（屏幕空间环境遮挡）是使用从深度缓冲区深度值中恢复的"正常"计算的方法实现的。 SSR（屏幕空间反射）是特别支持的，只为水面添加了一个专用的绘图路径。水面反射是我们特别努力工作的一部分，即使它稍微增加了处理负载，因为我们想让它看起来现实和美丽。此外， Fog中包含了一个简单的大气散射计算。由于只有很小的背景信息，所以我认为<br>
<br>
我很高兴我们能够创造出人们会认为令人印象深刻的东西，它在任天堂Switch上以这种质量运行。<br>
<br>
<strong>如果你能回到怪物猎人 ，在怪物猎人崛起的发展之初给自己一些建议，那会是什么呢？</strong><br>
<br>
我认为，我们应该早点为自动性能测量创造一个环境。 怪物猎人有各种各样的阶段、怪物、武器类型等组合，所以我们没有覆盖所有这些模式的自动测量环境。这使得检查优化结果有点困难。<br>
<br>
<strong>在怪物猎人 、 RE引擎和任天堂Switch上工作之后，你的总体感觉是什么？</strong><br>
<br>
优化是非常困难的，但它也是具有挑战性和回报的。由于RE引擎的基本设计、工具和开发方法，我们能够挑战优化，直到最后一刻。将大型RE引擎安装到小型任天堂开关是一个挑战，但我很高兴我们能够创造出人们会认为令人印象深刻的东西，它在任天堂开关上以这种质量运行。<br>
<br>
我们要感谢Capcom和Yasunori Ichinose的时间。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：西梅</font></font><br>
<font size="2"><font color="#808080">原文：<a href="https://www.ximeiapp.com/article/3549837" target="_blank">https://www.ximeiapp.com/article/3549837</a></font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            