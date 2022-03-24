
---
title: 'Unity震撼首发，最新一代高清数字人短片《Enemies》'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/22/103912oyliccc050zijl1n.jpg'
author: GameRes 游资网
comments: false
date: Tue, 22 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/22/103912oyliccc050zijl1n.jpg'
---

<div>   
我们屡获殊荣的 Demo 团队又一次在《异教徒（The Heretic）》（累积了超 400 万观众）的基础上取得了进展，推出了《Enemies》：一支全新的电影式预告片，以 4K 分辨率的实时渲染来展示眼睛、头发和皮肤渲染等方面的重大突破。<br>
<br>
<div align="center"><img aid="1034226" zoomfile="https://di.gameres.com/attachment/forum/202203/22/103912oyliccc050zijl1n.jpg" data-original="https://di.gameres.com/attachment/forum/202203/22/103912oyliccc050zijl1n.jpg" width="600" id="aimg_1034226" inpost="1" src="https://di.gameres.com/attachment/forum/202203/22/103912oyliccc050zijl1n.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">更全面的质量改进</font></strong><br>
<br>
通过与 Unity 工程师团队的路线图和开发工作密切协调，Demo 团队在制作早期就用上了许多新技术。短片的制作还促进了多种 Unity 技术的改进和修复，填补了各产品路线图中的空白，并针对自身的需要开发了新技术。<br>
<br>
在《Enemies》短片中，我们集中攻坚了三个方向：头发制作解决方案，提升面部的逼真程度，将这些技术应用到一个真正的作品中。<br>
<br>
所有新出的、开发中的和已推出的 Unity 图形和核心功能都被发挥到了极致，包括各系统之间流畅地协调运行，以提高整体图像质量。具体来说，《Enemies》用到了 Unity 的高清渲染管线（HDRP）中的所有技术、屏幕空间全局光照（SSGI）、新的 Adaptive Probe Volumes（适应性探针体积）、实时光线追踪、NVIDIA 深度学习超采样（DLSS）以及其他为实现短片艺术效果所使用的大大小小的功能。<br>
<br>
<div align="center">
<img aid="1034227" zoomfile="https://di.gameres.com/attachment/forum/202203/22/103912n4b2koz7pk1co392.jpg" data-original="https://di.gameres.com/attachment/forum/202203/22/103912n4b2koz7pk1co392.jpg" width="600" id="aimg_1034227" inpost="1" src="https://di.gameres.com/attachment/forum/202203/22/103912n4b2koz7pk1co392.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">在 Unity Lookdev 中不同光线角度下的场景截图</font></font></div><br>
<strong><font color="#de5650">我们全新的数字人类</font></strong><br>
<br>
制作一个人种和面部特征不同的角色给我们带来了一些额外的挑战，这也是在制作《异教徒》角色 Gawain 时所未曾解决的。在《Enemies》中，我们选择了一名 40 多岁的女演员作为主角，这位演员更符合故事的背景，也带来了新层次的技术挑战。<br>
<br>
首先，主角浅色的皮肤更为透明，因此在移动和说话时面部毛细血管会更明显，我们专门为此开发了一种张力技术。角色的面部还带有较为突显的皱纹，需要在着色和光照上特别注意。角色的眼睛更是有一系列独特的挑战（其中一些已经解决）。为了增强眼球的写实感，我们还添加了焦散（Caustic）效果。角色面部的“桃毛”或汗毛为皮肤添加了微妙且重要的真实感，我们通过将 Skin Attachment 系统移到 GPU 上计算来完成这部分毛发的渲染。最后，我们还给了她一头长发。<br>
<br>
<div align="center">
<img aid="1034228" zoomfile="https://di.gameres.com/attachment/forum/202203/22/103913pzz11cz4ch1711d2.jpg" data-original="https://di.gameres.com/attachment/forum/202203/22/103913pzz11cz4ch1711d2.jpg" width="493" id="aimg_1034228" inpost="1" src="https://di.gameres.com/attachment/forum/202203/22/103913pzz11cz4ch1711d2.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">Unity全新的头发渲染方案</font></strong><br>
<br>
全新的 Unity Hair Solution 包含三个部分，三部分协调运行才产生了主角自然的外观和动作.<br>
<br>
Hair 系统（以发丝作为渲染单位）是一种用于头发创作、模型蒙皮、发丝模拟和头发渲染的一体化解决方案。此系统兼容所有能够输出以 Alembic 为文件格式的发型数据，因此你可以自由选择创作工具以创建角色的发型。在《Enemies》中，我们使用了 Maya XGen 来制作头发，我们也正在通过 Weta Barbershop 验证这一流程。Hair 系统也可以兼容你所选择的着色器，你可以在任何一种渲染管线中使用它。系统目前支持高清渲染管线（HDRP）、通用渲染管线（URP）和内置渲染管线。<br>
<br>
为了使头发和短毛看起来更真实，Unity 为 HDRP 开发了 Hair 着色，其效果与特效电影和动画电影中所用的模型类似（比如 Marschner、迪士尼的电影）。我们能够使用该技术在每种光线条件下创造出更精致的视效，而不需要特意改变参数来取得较高的性能。<br>
<br>
Hair 渲染可以高效地渲染非常细的发丝，还能有效防止因发丝过细导致无法正确地光栅化所造成的锯齿。在《Enemies》中，我们在一个可见度缓冲区中多次采样，以减少发丝过细所产生的锯齿，而发丝的着色则是在一张单独的着色图集中完成的，独立于发丝的可见度。<br>
<br>
<div align="center">
<img aid="1034229" zoomfile="https://di.gameres.com/attachment/forum/202203/22/103913vmzfscmumgxubn6x.jpg" data-original="https://di.gameres.com/attachment/forum/202203/22/103913vmzfscmumgxubn6x.jpg" width="600" id="aimg_1034229" inpost="1" src="https://di.gameres.com/attachment/forum/202203/22/103913vmzfscmumgxubn6x.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">什么时候能公开项目？</font></strong><br>
<br>
与以往一样，Demo 团队将与社区分享《Enemies》中的技术，以便让大家能在自己的 Unity 项目中进行尝试。<br>
<br>
我们将在一两个月内发布 Digital Human 2.0 软件包，其中包含自《异教徒》以来我们所做的所有更新和改进。<br>
<br>
支持发丝渲染的 Hair 系统将以软件包的形式发布到 GitHub，我们非常欢迎大家前来试用、反馈，以便我们完善系统、并最终发布为官方支持的功能。请关注 Unity 的博客和社媒账号，第一时间获悉资源包的公布消息。<br>
<br>
在制作《Enemies》期间做出的或已经应用的引擎改进部分已在 Unity 2021.2 中推出，部分将在 2022.1 或 2022.2 中推出。<br>
<br>
<div align="center">
<img aid="1034230" zoomfile="https://di.gameres.com/attachment/forum/202203/22/103914xzzto4wrzltrazqt.jpg" data-original="https://di.gameres.com/attachment/forum/202203/22/103914xzzto4wrzltrazqt.jpg" width="600" id="aimg_1034230" inpost="1" src="https://di.gameres.com/attachment/forum/202203/22/103914xzzto4wrzltrazqt.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">《Enemies》技术分享</font></strong><br>
<br>
我们会在 GDC 活动上公布更多技术细节，稍后会进行本地化，并发布在 B 站官方平台。<br>
<br>
欢迎关注国内 GDC 官网，收藏不迷路：<br>
<br>
https://unity.cn/gdc2022<br>
<br>
<div align="center">
<img aid="1034231" zoomfile="https://di.gameres.com/attachment/forum/202203/22/103915hzq2deqhge2mzbmb.jpg" data-original="https://di.gameres.com/attachment/forum/202203/22/103915hzq2deqhge2mzbmb.jpg" width="600" id="aimg_1034231" inpost="1" src="https://di.gameres.com/attachment/forum/202203/22/103915hzq2deqhge2mzbmb.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="left"><font size="2"><font color="#808080"></font></font></div><div align="left"><font size="2"><font color="#808080">来源：Unity官方平台</font></font></div><br>
  
</div>
            