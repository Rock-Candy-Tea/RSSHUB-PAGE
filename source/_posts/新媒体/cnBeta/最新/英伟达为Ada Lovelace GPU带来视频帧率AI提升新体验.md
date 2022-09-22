
---
title: '英伟达为Ada Lovelace GPU带来视频帧率AI提升新体验'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0922/e58e1e1cf0dbca6.jpg'
author: cnBeta
comments: false
date: Thu, 22 Sep 2022 09:35:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0922/e58e1e1cf0dbca6.jpg'
---

<div>   
随着 GeForce RTX 40 系列显卡的发布，发展到第三代的深度学习超级采样（DLSS 3）功能，也带来了一项“AI 帧生成”的定义特性。<strong>TechPowerUp 指出，Ada Lovelace GPU 能够预测交给 GPU 去渲染的下一帧，并在不涉及任何图形渲染管道的情况下生成帧。</strong>有趣的是，英伟达还将这一概念运用到了视频编码上，以借助该“魔法”提升视频的帧速率。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0922/e58e1e1cf0dbca6.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Nvidia <a href="https://developer.nvidia.com/blog/av1-encoding-and-fruc-video-performance-boosts-and-higher-fidelity-on-the-nvidia-ada-architecture/" target="_self">Technical Blog</a>）</p><p>据悉，Ada Lovelace GPU 的光流加速器（NVOFA）组件，可对视频应用和图形渲染套用相同的光流（Optical Flow）逻辑。</p><p><img src="https://static.cnbetacdn.com/article/2022/0922/9e611d10b57731f.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>在预测下一帧的同时，GPU 还可通过 AI 生成该帧，来提升画面的流畅度 —— 英伟达称之为“引擎辅助帧率转换”（FRUC）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0922/c26830f18d6661d.gif" alt="FRUC.gif" referrerpolicy="no-referrer"></p><p>此前我们有在一些<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_76344%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">电视</a>机（以及 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 显卡驱动）上见到过其它形式的“提升流畅度”解决方案，但这里 NVENC 还可比较视频中的两个真实帧、确定运动矢量、并设置光流阶段，以确保生成帧的准确性。</p><p><img src="https://static.cnbetacdn.com/article/2022/0922/4c8dcbe0e0dd786.jpg" alt="4 New-interpolated-frame.jpg" referrerpolicy="no-referrer"></p><p>最后，英伟达将以库（Library）的形式来发布 FRUC，以帮助它更好地集成于内容创建和媒体消费类应用程序中。</p>   
</div>
            