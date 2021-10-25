
---
title: '任天堂Switch模拟器Yuzu大幅改进分辨率缩放功能：进一步激发游戏潜力'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1025/2b199cb0653663c.jpg'
author: cnBeta
comments: false
date: Mon, 25 Oct 2021 02:36:27 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1025/2b199cb0653663c.jpg'
---

<div>   
<strong>面向 Early Access 用户，任天堂 Switch 模拟器 Yuzu 在最新更新中引入了用户长期要求的增强版分辨率缩放功能。这项功能将使模拟爱好者能够超越 Switch 硬件的极限，体验任天堂 Switch 游戏的全部潜力。</strong>在最新的 Yuzu Early Access 构建版本中，团队大幅改进了分辨率缩放功能。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1025/2b199cb0653663c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1025/2b199cb0653663c.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">不过 Yuzu 团队也表示，最新的 NVIDIA 驱动程序会导致 OpenGL 的渲染问题。因此，请确保你的系统使用 472.12 版本的 NVIDIA GeForce 驱动程序，因为这是最后一个没有引起任何问题的已知版本。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1025/b706af140fd4a73.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1025/b706af140fd4a73.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1025/14264e3f45f82a6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1025/14264e3f45f82a6.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">顾名思义，分辨率缩放功能就是缩放 Switch 游戏所渲染的纹理尺寸。然后，游戏就会按照缩放后的分辨率进行渲染。这使得 Switch 游戏可以在较低的分辨率下进行渲染，如 720p/900p。然而，Yuzu 也可以用它来远远超出在更高的分辨率下播放的目的，包括 8K。</p><p style="text-align: left;">新的 Yuzu 分辨率缩放器，被称为<a href="https://yuzu-emu.org/entry/yuzu-art/" target="_blank"> Project ART</a>，使用一个评级系统：</p><blockquote style="text-align: left;"><p style="text-align: left;">这个精心设计的评级系统的工作原理是：有一套规则来规定哪些渲染目标可以被缩放，并对每个纹理有一个评级。我们不能简单地使用一个二进制的“是/否”系统，因为我们不知道，有些游戏可能只渲染纹理一次。缩放这些纹理是毫无意义的，而且有可能会破坏它们。</p><p style="text-align: left;">对于不熟悉的人来说，渲染目标只是游戏渲染的纹理。纹理每一帧只能获得一个积分。为了获得这 1 个积分，纹理本身以及该渲染通道中的其他纹理都需要满足我们的一系列规则。在积累了 2 个或更多的积分后，纹理将被缩放，现在所有的渲染都将在该纹理的缩放分辨率下进行。</p><p style="text-align: left;">随着帧数的增加，纹理会不断获得更多的积分。但如果在任何一帧中，即使是渲染通道中的单个纹理未能满足这套规则，所有纹理的分数将被重置为0。如果一个纹理与其他纹理互动，其新的评级将基于这些纹理的当前评级，或者将增加到可能的最大评级，如果这些纹理之一已经被缩放。</p></blockquote>   
</div>
            