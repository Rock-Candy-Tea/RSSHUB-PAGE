
---
title: '如何在3D空间打造2D艺术，《Season》插画外观创作分享'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/07/095855prr22wd9i2rrx70r.jpg'
author: GameRes 游资网
comments: false
date: Tue, 07 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/07/095855prr22wd9i2rrx70r.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2513463">
2020年的Game Awards中，我们Scavengers Studio尚待发布的游戏《Season》一经亮相，就凭借其美术设计收获了大量积极反馈。我们的团队希望为玩家创造一个富有魅力的暖调世界，让玩家骑着自行车去探索美丽的风景，揭开隐藏在表面之下的秘密。我们的美术设计发挥着关键作用，它将迎接玩家记录《Season》中的低语，因为这个世界已注定会被毁灭。<br><br>
《Season》的美术设计从插画家、油画家和自然光摄影师那里汲取了灵感。我们用来描绘现实的极简主义手法类似于早期日本浮世绘画家和Norman Wilkinson等20世纪中期的海报艺术家。这种剔除细节而非增加细节的简化思维方式，成为我们在开发整体外观时牢记在心的准则。你会注意到，我们心中的美术风格灵感源自2D，而我们将它融入到了3D场景中。<br><br><strong><font color="#de5650">这就引出了一个问题：如何在3D空间中创造2D美术风格？</font></strong><br><br>
为了找出答案，我们找到了三名美术师和开发者：负责角色和技术美术的Felix Arsenault（Feu）、环境美术师Geneviève Bachand以及3D程序员Irwin Chiu Hau。<br><br>
我们的3D场景最初由虚幻引擎提供的工具搭建。不可否认，我们的一些美术师在开始使用虚幻引擎时并没有感觉非常顺手。但他们还是对蓝图和基于节点的工具赞赏有加，这些工具易于上手，简化了他们的学习过程。Felix说：“虚幻引擎包含了操作便捷的优秀工具，地形、植被和自动细节层次（LOD）等工具尤其有用。”<br><br>
团队需要灵活地创造和迭代自定义工具，将绘制的美术设计外观转移到可探索的3D世界中。“因为一切都是基于节点的，我们可以通过可视化编程节点快速制作工具并自定义着色器，并且不需要传统的编程背景。”Felix说。我们的美术师参考了其他引擎中对应的节点型功能，但发现它们都不如虚幻引擎优秀。<br><br>
Geneviève解释说：“虚幻引擎的功能允许我们自由创作，使我们能够专注于遵循美术设计。在虚幻引擎功能的帮助下，我们构建了自定义着色器来实现《Season》的特定外观，而不是被迫只使用引擎中的现有内容。”虚幻引擎中的创作灵活性赋予了团队自由，Felix补充说：“作为美术师，我认为，我们不可能在其他引擎中做到这一点。”<br><br>
《Season》团队依靠迭代各种游戏功能，探索完美展现这种氛围的方法，即使美术方面也不例外。虚幻引擎的灵活性允许我们将各种工具与其他现有功能搭配使用，这使得我们的美术师能够进行实验，并根据需要添加新功能。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1006521" aid="1006521" zoomfile="https://di.gameres.com/attachment/forum/202109/07/095855prr22wd9i2rrx70r.jpg" data-original="https://di.gameres.com/attachment/forum/202109/07/095855prr22wd9i2rrx70r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/07/095855prr22wd9i2rrx70r.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">图片由Scavengers Studio提供</font></font></div>
<br>
我们的一项美术迭代是基于这样的想法：剔除细节，捕捉世界的美。然而，虚幻引擎的光照和阴影解决方案旨在使用基于物理的渲染（PBR）和光线追踪等功能，保留真实度和细节。<br><br>
虚幻引擎或虚幻商城中的后期处理解决方案并未提供我们想要的功能或外观，所以我们必须为此展开一些额外的工作。<br><br>
为了匹配我们美术设计所追求的有限细节层次，我们决定重点了解传统绘画中如何运用局部色彩，以及数字绘画家如何模仿这些技法。来自Artifact5的Mohannad Al-Khatib和Ramy Daghstani为我们创建了一个着色器，专门按照插画技法中的方式使用反射率（或局部色彩）。<br><br>
首先要选择反射率，也就是画家所说的每种材质的局部颜色，然后选择与各类物体关联的阴影色调。着色器会自动取得阴影色调的颜色与反射率的颜色，并计算出最终的阴影颜色。接下来，虚幻引擎会根据光线的入射角判断，是选择阴影颜色还是反射率。<br><br>
着色器会使用颜色和阴影的错觉来重现插画作品的深度和纹理。用Mohannad的话来说，通过创建这样的着色器，在“让美术师控制”和“让引擎完成大部分工作”这两种选择之间找到了平衡点。使用虚幻引擎，美术师可以简单地公开特定参数，通过对参数的修改来控制最终结果。在材质节点编辑器中，一切都是可单独编辑的，如此一来，我们就能够制作并完善主材质，并将它们连接至我们的自定义工具。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1006522" aid="1006522" zoomfile="https://di.gameres.com/attachment/forum/202109/07/095856j355h5jj8wz35j8k.jpg" data-original="https://di.gameres.com/attachment/forum/202109/07/095856j355h5jj8wz35j8k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/07/095856j355h5jj8wz35j8k.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">图片由Scavengers Studio提供</font></font></div>
<br>
但这种美术设计使我们遇到了一个技术问题。如果一切都可单独编辑，我们就很难使用全局光照统一各个区域。因为每个物体都具有特定的阴影色调颜色和反射率颜色，它可以包含一个纹理颜色，这使得在不同的光照场景下，整个纹理很难有一致的阴影颜色。这就是说如果游戏中的天色发生改变，我们必须单独编辑所有这些物体，才能反映出变化。如果清晨的金色阳光洒在游戏中的所有物体上，需要逐个更改它们，才能反射正午清爽的蓝色光线。我们得到了一个美丽的静态场景，物体展示着各不相同的外观，但它们不能有不同的颜色或对比度。<br><br>
我们修改了美术设计，创建更容易建模的场景，展现物换星移，能够在高地和生物群区等位置间轮换。这迫使我们重新拾起虚幻引擎的PBR模型，但必须做一些调整。如此一来，我们就能接收到基于入射光线的“真实”照明，这意味着光线将始终来自于某个自然光源，例如天空或闪烁的烛火。获得这种光照之后，我们会确定亮度阈值或入射角阈值，根据光源颜色计算每个图像像素的阴影颜色。<br><br>
我们的卡通着色器专门用于改变材质中的颜色，而我们全新的美术设计则专注于使用光照的变化营造更美丽的场景。例如，如果我们想在场景中提升对比度，可以增强直射的阳光，移除天空中柔和的光照，从而形成一股来自太阳的直射强光。如果我们想进一步控制对比度，可以使用后期处理工具。<br><br>
我们新制定的光照决策引出了一项新特色：转向使用天空球体的静态光照。天空光照与光源类似，根据来自天空的光线，使整个场景的卡通渲染保持一致。天空光照产生的光线和阴影颜色将投射在场景中的所有物体上。我们还有一些设置项，可为天空设定一种基调，为场景的整体氛围添加一种色调。例如，在安全而熟悉的地方，天空光照将为所有资产投下暖色调的光线。<br><br>
现在，所有的光照都包含了接近于次表面散射的效果，光线将被物体吸收或反射，营造光线发散的效果。想象在晴朗的夏日，光线透过树叶，被绿叶吸收，使它们显得更加闪耀。另一个例子是，白色路面上的阳光反射进你的眼中，眩光让人分不清方向，但感觉温暖。我们的光照着色器是能量恒定的，这意味着，无论我们向场景中添加多少光线，它始终会保持一致。而如果我们为同一物体添加两处光源，它的亮度就会变成两倍。这些写实的瞬间激发了《Season》中光照设计的改变，创造出玩家更熟悉的世界。<br><br><strong><font color="#de5650">Look Dev Manager</font></strong><br><br>
另一个障碍是，当我们得到着色器并开始构建材质和各种自定义工具时，这些工具不够自动化，缺乏易用性。我们最初就有许多可用的功能，但它们全都散布在多个关卡中，需要手动执行。<br><br>
我们的解决方案是创建“Look Dev Manager”。Felix解释说：“这是一个基于蓝图的工具，如果没有可视化编程，我永远无法制作出来。”这是一个简单的拖放工具，可以在游戏的任何关卡中使用。它能够连接和控制所有自定义着色器、后期处理工具等美术师所必需的功能，并将它们紧密地封装在一个位置。<br><br><div align="center">
<img id="aimg_1006523" aid="1006523" zoomfile="https://di.gameres.com/attachment/forum/202109/07/095856oks6sxms36pms3au.jpg" data-original="https://di.gameres.com/attachment/forum/202109/07/095856oks6sxms36pms3au.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/07/095856oks6sxms36pms3au.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">图片由Scavengers Studio提供</font></font></div>
<br>
它还能与虚幻引擎的光照场景相结合，允许我们加载和卸载影响光照、云、天空盒、雾和阴影等一切与氛围和意境相关的光照场景子关卡。<br><br>
它包含多种功能，并易于维护。它可以灵活地删除或添加我们想要的任何功能，而且对艺术家来说，创建和使用都很容易。<br><br>
接下来，让我们来深入挖掘Look Dev Manager中内置的一些功能。所有功能都是通过可视化编程实现的。<br><br><strong><font color="#de5650">关键帧序列</font></strong><br><br>
为了控制一天中不同时间的光照，我们在Look Dev Manager中使用了一个关卡序列管理器，它可以控制一天中太阳颜色和位置的变化。关卡序列管理器控制着太阳转移时间和位置的关键帧，随着时间和关键帧编号的向前推移，一天也将过去。所有的自然光照都是连接在一起的，可在代表当天时间的关键帧内进行控制。<br><br>
我们也可以使用光照动画来混合不同的时间和天气系统，从而在两个不同的光照场景之间实现平滑过渡。<br><br><div align="center">
<img id="aimg_1006524" aid="1006524" zoomfile="https://di.gameres.com/attachment/forum/202109/07/095857lmim26et1oo3ub10.jpg" data-original="https://di.gameres.com/attachment/forum/202109/07/095857lmim26et1oo3ub10.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/07/095857lmim26et1oo3ub10.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">图片由Scavengers Studio提供</font></font></div>
<br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1006525" aid="1006525" zoomfile="https://di.gameres.com/attachment/forum/202109/07/095857ad5zltlrncplujjt.jpg" data-original="https://di.gameres.com/attachment/forum/202109/07/095857ad5zltlrncplujjt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/07/095857ad5zltlrncplujjt.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">图片由Scavengers Studio提供</font></font></div>
<br><strong><font color="#de5650">《Season》的氛围和环境</font></strong><br><br>
我们面临的另一个挑战就是为《Season》创造氛围和环境。如果玩家望向山丘，与周围环境的大气相比，他们将如何感知天空的颜色和纹理？我们再次从2D媒介中寻找灵感。<br><br>
我们通过一层累加的大气看到远处的地形，它染上了天空的颜色。团队通过研究画中的地形，模拟画家如何使用色彩在云端、地形以及一切其他物体之上创造一层大气。<br><br>
露天派画家的作品是我们调配大气的重要参考。他们倾向于将阴影中的信息分组，比起明亮区域，阴影中的细节会被果断地舍弃，保留更高级别的细节层次和纹理。<br><br>
尽管虚幻引擎中默认提供了很好的大气和雾工具，但它们无法表现出我们想要的行为，并且在很大程度上，会受虚幻引擎默认使用的各种光照系统影响。我们需要更简单、更灵活的解决方案来实现插画风格外观。幸运的是，开始使用可视化编程迭代和开发替代方案并不困难。<br><br>
我们转而采用数字绘画家的一种方法，来重现传统画家的这种大气透视。为了控制游戏的氛围，我们使用了定向光源（太阳/月亮）、自然天空光照、天空大气和雾。<br><br>
“我最终创建了两种类型的后期处理：大气透视后期处理，以及基于高度的雾后期处理。”Felix说。<br><br>
我们的自定义大气透视后期处理是基于距离的，此外，它还采用了一种增亮和滤光系统来控制雾的行为。我们为美术师提供各种参数，用来定制和控制场景氛围。另一方面，我们自定义的基于高度的雾后期处理提供了多种混合模式可供选择，并支持基于纹理的风，我们可以定制风并为它制作动画。<br><br>
同样，这些都被排除在大多数默认的自动化系统之外，美术师们可以自由地使用它们。<br><br>
这些后期处理是可叠加、可混合的，可以在Look Dev Manager内部或外部使用，我们可以使用它们的多个版本相互叠加，以达到预期的结果。有了这两种类型的大气后期处理，我们就可以实现足够的深度和准确度，满足为游戏渲染心境和气氛的需要。<br><br>
我们尝试尽可能地保持Look Dev Manager的灵活性，并将它模块化，这也确保了各个功能的灵活性和模块化。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1006526" aid="1006526" zoomfile="https://di.gameres.com/attachment/forum/202109/07/095858u4ywzalpls2559bd.jpg" data-original="https://di.gameres.com/attachment/forum/202109/07/095858u4ywzalpls2559bd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/07/095858u4ywzalpls2559bd.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">图片由Scavengers Studio提供</font></font></div>
<br><font color="#de5650"><strong>《Season》的后续工作</strong></font><br><br>
这只是《Season》目前开发工作的一瞥，我们仍在虚幻引擎中为这个世界创造活力。随着时间的推移，我们看到这些自定义工具不断地诞生和完善。它们帮助我们创造了从未见过的氛围和环境，拓展了电子游戏美术设计的极限。<br><br>
我们期待着打开这个世界，供玩家探索。欢迎大家现在就将《Season》加入Steam或Epic Games愿望单。<br><br>
Epic Games商城链接：<br><br>
https://www.epicgames.com/store/zh-CN/p/season<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">来源：虚幻引擎 </font></font><br>
</td></tr></tbody></table>


  
</div>
            