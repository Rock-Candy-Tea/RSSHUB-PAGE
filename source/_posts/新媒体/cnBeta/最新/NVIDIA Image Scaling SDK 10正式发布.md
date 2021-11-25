
---
title: 'NVIDIA Image Scaling SDK 1.0正式发布'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1125/e37ce061cfb2059.webp'
author: cnBeta
comments: false
date: Thu, 25 Nov 2021 06:08:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1125/e37ce061cfb2059.webp'
---

<div>   
以开源、跨平台的 GPU 图像缩放实现，上周 NVIDIA 推出了 Image Scaling SDK，以配合 NVIDIA 公司硬件更好优化 DLSS。在过去 1 周的短暂曝光之后，<strong>NVIDIA Image Scaling SDK 1.0 已被正式发布。</strong><br>
 <p style="text-align: left;">下载：<a href="https://github.com/NVIDIAGameWorks/NVIDIAImageScaling/releases/tag/v1.0.0" target="_blank">GitHub</a><br style="text-align: left;"></p><p style="text-align: left;">Image Scaling SDK 可以通过 SDK 的通用计算着色器在 Intel 和 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon 等硬件上工作，这些着色器是经过 MIT 许可的。整合 NVIDIA Image Scaling SDK 确实需要游戏/引擎开发者的整合。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1125/e37ce061cfb2059.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1125/160d476edf94255.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">正如该项目代码库所言：</p><blockquote style="text-align: left;"><p style="text-align: left;">NVIDIA图像缩放SDK提供了一种跨平台支持的单一空间缩放和锐化算法。该缩放算法使用了一个6抽头的缩放过滤器，结合了4个方向性的缩放和自适应锐化过滤器，从而创造出漂亮的平滑图像和锐利的边缘。</p><p style="text-align: left;">此外，SDK还提供了一个最先进的自适应定向锐化算法，用于不需要缩放的应用中。方向性缩放和锐化算法被命名为NVScaler，而仅有的自适应方向性锐化算法被命名为NVSharpen。</p><p style="text-align: left;">这两种算法都是作为计算着色器提供的，开发者可以在他们的应用程序中自由地集成它们。请注意，如果你集成了NVScaler，你不应该集成NVSharpen，因为NVScaler已经包括了一个锐化通道。</p></blockquote>   
</div>
            