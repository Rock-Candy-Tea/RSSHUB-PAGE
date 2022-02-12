
---
title: '《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220212/1644652007_233150.jpg'
author: 3DMGame
comments: false
date: Sat, 12 Feb 2022 07:47:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220212/1644652007_233150.jpg'
---

<div>   
<p style="text-indent:2em;">
《英雄萨姆：西伯利亚狂想曲》是《英雄萨姆4》的独立资料片，在1月份正式发售，使用Serious Engine 
4开发。外媒DSOGaming对这款作品进行了性能表现分析，一起来看一下。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220212/1644652007_233150.jpg" alt="《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
以下是文章全文：
</p>
<p style="text-indent:2em;">
在这篇性能分析文章中，我们的CPU使用Intel i9 9900K、内存使用16GB DDR4 3800Mhz、显卡分别是AMD Radeon 
RX580、RX Vega 64、RX 6900XT、NVIDIA GTX980Ti、RTX 2080Ti和RTX 3080。操作系统使用Windows 10 
64-bit，驱动分别是GeForce 511.65和Radeon Software Adrenalin 2020 Edition 22.1.2。
</p>
<p style="text-indent:2em;">
Timelock在这款游戏中提供了很多画质选项供玩家调整。PC玩家在本作中可以调整材质、抗锯齿、阴影、环境光遮蔽等方面的品质值得一提的是，《英雄萨姆：西伯利亚狂想曲》支持DirectX 
11和Vulkan，不过我们建议使用DX11，因为在测试Vualkan 
API的过程中我们遇到了严重的卡顿问题。本作还提供FOV设置，还有一些HUD/菜单设置。
</p>
<p style="text-indent:2em;">
为测试本作对不同CPU线程的兼容性，我们分别模拟了双核、四核与六核CPU。从结果来看，本作对单一CPU内核/线程非常依赖。虽然不是完全的单线程，但就像《孤岛惊魂6》一样，一个CPU内核/线程会直接跑满（并成为你所得整体性能的瓶颈）。解决这一问题的办法只有使用IPC性能出色的CPU（或者有杰出单线程性能的CPU）。
</p>
<p style="text-indent:2em;">
有意思的是，超线程在不同CPU环境下对性能的影响也各不相同。我们模拟四核的时候，超线程表现就更好一些。但模拟六核的时候超线程的平均帧率就没有变化（不过我们看到了最佳的帧率下限）。而在八核环境下启用超线程的时候，可以看到性能暴跌的现象。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220212/1644652021_410997.png" alt="《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
由于游戏存在CPU优化问题，所以我们的CPU瓶颈被限制在1080p/终极画面设置（大部分显卡可达1440p/终极画面设置）。值得一提的是，由于DX11 
API的原因，A卡在本作中的表现要比N卡差一些。在4K/终极画面设置下，我们三块最强显卡都可以提供流畅体验。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220212/1644652038_304755.png" alt="《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析" referrerpolicy="no-referrer">
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220212/1644652044_105113.png" alt="《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
我们需要说一下在体验这款游戏的过程中遭遇到的问题。游戏中存在<strong>非常严重的卡顿问题</strong>（即便是在使用DX11 
API时）。我感觉卡顿主要是由于读取新敌人和新场景引起的。另外，这款游戏就没有真正流畅的时候（就连战斗中都会有卡顿）。就算我们把CPU预设降为“高”都会卡。这在一款快节奏动作FPS游戏中是非常致命的。另外，在过场动画里还出现很多材质串流问题。说到过场动画，大部分画面都会卡。你看看下面这张图片，告诉我这种画面怎么可能会卡?Serious 
Engine 4真的需要技术大修，现在问题实在太多了。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220212/1644652056_614139.jpg" alt="《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
《英雄萨姆：西伯利亚狂想曲》的最大卖点是同屏敌人显示数量。这确实是个优点，其它FPS游戏都达不到这种同屏敌人的数量。有时候玩家需要同时面对一百多个敌人。以这个数量来说，《英雄萨姆：西伯利亚狂想曲》确实给玩家带来了一些值得回味的战斗体验。
</p>
<p style="text-indent:2em;">
总而言之，《英雄萨姆：西伯利亚狂想曲》存在严重优化问题。虽然同屏显示敌人数量很多，但卡顿问题和CPU优化问题也很严重。Croteam在《英雄萨姆》续作推出之前应该好好维护一下他们的引擎了。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220212/1644652064_683606.jpg" alt="《英雄萨姆：西伯利亚狂想曲》PC版性能表现分析" referrerpolicy="no-referrer">
</p>          
</div>
            