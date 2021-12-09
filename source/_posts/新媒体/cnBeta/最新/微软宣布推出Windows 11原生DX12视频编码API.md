
---
title: '微软宣布推出Windows 11原生DX12视频编码API'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1209/3d2c089d9bf3d44.png'
author: cnBeta
comments: false
date: Thu, 09 Dec 2021 07:38:14 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1209/3d2c089d9bf3d44.png'
---

<div>   
作为一套 Windows 平台上的多媒体解决方案，DirectX 12 在游戏和视频领域颇有建树。此前，微软已经提供了用于 GPU 加速的视频解码处理、以及运动估算的应用程序接口。<strong>而在周三的一篇 DirectX 开发者博客文章中，软件工程师 Sil Vilerino 又详细介绍了为 Windows 11 操作系统新引入的 DX12 视频编码 API 。</strong><br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1209/3d2c089d9bf3d44.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://devblogs.microsoft.com/directx/announcing-new-directx-12-feature-video-encoding/" target="_self">DirectX Developer Blog</a>）</p><p>作为 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 平台的原生 DX12 视频编码 API，它又有哪些独到之处呢？</p><p>本质上，该 API 允许视频引擎利用 GPU 来执行符合 DX12 标准的视频编码，意味着第三方开发者可在其应用程序中轻松调用。</p><p>以被广大游戏开发项目采用的 Vulkan 为例，它就包含了面向 H264 / H265 视频的编解码器 API 。</p><p><img src="https://static.cnbetacdn.com/article/2021/1209/45b9b1d83b6f858.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">最低硬件平台 / 驱动版本要求</p><p>虽然目前 Windows 11 平台上的 DX12 视频编码器 API 仅支持 H264 / HEVC 格式，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>已建议开发者预先了解各个对应的编解码器和驱动工具支持。</p><p>除了默认包含在 Windows 11 中的视频编码 API，感兴趣的开发者还可通过 DX12 Agility 软件开发套件（SDK 版本号 1.70.10-preview 或更高版本）来获取。</p><p>如果想要了解更细致的视频编码流程和调用方法，还请移步至微软 DX12 开发者网站查看。</p>   
</div>
            