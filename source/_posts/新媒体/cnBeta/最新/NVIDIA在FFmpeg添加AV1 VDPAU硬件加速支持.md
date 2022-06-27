
---
title: 'NVIDIA在FFmpeg添加AV1 VDPAU硬件加速支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0627/8b0c4076cbc2314.webp'
author: cnBeta
comments: false
date: Mon, 27 Jun 2022 00:18:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0627/8b0c4076cbc2314.webp'
---

<div>   
通过添加对 FFmpeg 多媒体库的支持，在使用最新一代 NVIDIA RTX 30"Ampere"GPU 的时候，能够以 VDPAU API 的方式充分利用 AV1 GPU 加速的视频解码。周六，<a href="https://github.com/FFmpeg/FFmpeg/commit/a44fba0b5b3b4090f9238751736198ddd1f0f1d5" target="_blank">此提交</a>将 AV1 VDPAU 支持合并到 FFmpeg。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0627/8b0c4076cbc2314.webp" alt="ptkxl54q.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">NVIDIA 已将 AV1 VDPAU 硬件加速解码的支持落地到上游 FFmpeg 项目中。此 AV1 视频解码与 1.5 版本以上的 libvdpau 结合使用，并使用具有必要硬件功能的 Ampere 或更新的 GPU。</p><p style="text-align: left;">从 FFmpeg 4.4 开始，通过 NVDEC“NVIDIA 解码”接口在 NVIDIA GPU 上进行 AV1 解码，该接口是其视频编解码器 SDK 的一部分。 FFmpeg 还支持 Intel QSV 加速解码、<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> DXVA2/D3D11VA AV1 解码以及通过 DAV1D 项目基于 CPU 的解码。</p><p style="text-align: left;">通过<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的 SVT-AV1，FFmpeg 也支持 AV1 编码。现在有了 FFmpeg Git，AV1 VDPAU 解码已经为那些更喜欢 VDPAU 而不是新的 NVDEC 的人准备好了。</p><p style="text-align: left;">在 NVIDIA 领域之外，随着更多 GPU 开始具有 AV1 解码硬件块，这种 AV1 VDPAU 曝光可能有助于支持 VDPAU 视频加速状态跟踪器的 Mesa Gallium3D 驱动程序。</p>   
</div>
            