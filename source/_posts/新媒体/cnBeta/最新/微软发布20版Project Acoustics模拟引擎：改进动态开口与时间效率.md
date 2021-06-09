
---
title: '微软发布2.0版Project Acoustics模拟引擎：改进动态开口与时间效率'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0609/6d9290e789e3678.png'
author: cnBeta
comments: false
date: Wed, 09 Jun 2021 07:45:18 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0609/6d9290e789e3678.png'
---

<div>   
Project Acoustics 是微软推出的基于波的模拟引擎，适用于在游戏、混合现实等 3D 环境中引入沉浸式的声学体验。<strong>比如它能够模拟各种障碍和遮挡物的回声，而无需依赖于硬件密集型的光线追踪（Ray Tracing）功能。</strong>目前，Project Acoustics 运行时（Runtime）已登陆 Windows、Xbox、Android 和 macOS 等平台，且与 Unity 和 Unreal 等游戏引擎实现了集成。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0609/6d9290e789e3678.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0609/6d9290e789e3678.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：Microsoft <a href="https://techcommunity.microsoft.com/t5/mixed-reality-blog/project-acoustics-2-0-is-now-available/ba-p/2412893" target="_self">官网</a>）</p><p>新版本还带来了 Unreal 与 Unity 引擎的一些特色功能，比如支持前者的动态开口（Dynamic Openings）功能，可形成环境的几何网格、并模拟相应的声学效果。</p><p><a href="https://static.cnbetacdn.com/article/2021/0609/698529905b1959f.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0609/698529905b1959f.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>除了依靠自动生成的探针，开发者还可在 3D 环境中手动植入自己的探针，甚至为各个区域指定预生成的探针数量。</p><p>当然，探针数量与声学准确性成正比，数量越多、“渲染”所需的时间也要更久。</p><p><img src="https://static.cnbetacdn.com/article/2021/0609/3c956c7433ee5b3.png" alt="3.png" referrerpolicy="no-referrer"></p><p>此外开发者可借助“材料覆盖”（Material Override）选项，手动设置区域内所有材料的吸收系数。</p><p>Unity 方面，其强调了对 Wwise 集成的支持。最后，除了几个 Bug 修复，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>还表示“烘焙时间”有望提速至旧版本的两倍。</p><p><a href="https://static.cnbetacdn.com/article/2021/0609/e0006d6e2d220e5.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0609/e0006d6e2d220e5.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p>感兴趣的朋友，可移步至微软 <a href="https://docs.microsoft.com/en-us/gaming/acoustics/what-is-acoustics" target="_self">Project Acoustics</a> 官网了解详情。该引擎目前支持将 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 和 macOS 作为编辑器平台，但 Unity 插件暂时仅可在 macOS 上体验。</p>   
</div>
            