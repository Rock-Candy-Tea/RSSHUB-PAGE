
---
title: 'Linux 6.0将其H.265_HEVC用户空间API提升到稳定状态'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0809/73c1537351332ad.webp'
author: cnBeta
comments: false
date: Tue, 09 Aug 2022 07:34:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0809/73c1537351332ad.webp'
---

<div>   
随着Linux 6.0多媒体子系统的变化，H.265/HEVC用户空间API现在被视为稳定状态。Linux 6.0最新补丁已经将HEVC无状态控制移出暂存区，并使"HEVC uapi表现稳定并可用于硬件解码器"。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0809/73c1537351332ad.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>目前行使Linux内核HEVC用户空间API的是全志SoC的Cedrus驱动和Hantro媒体驱动，以及用于瑞芯微和恩智浦SoC内VPU的Hantro视频IP。此外，还有目前树外的瑞芯微RKVDEC和Raspberry Pi"RPI"驱动程序，它们都使用了这个HEVC用户空间API。</p><p>通过这些使用API的驱动程序和持续的开源代码完善，它已经是一个稳定的状态，而不是一个暂存接口。</p><p>除了最终确定用户空间API之外，Linux 6.0的媒体子系统更新还增加了Semi AR0521传感器驱动，更新了Cedrus和Hantro对H.265的支持，STKWebCam驱动已经从暂存状态中升级出来，Intel AtomISP驱动也进行了一些修复/清理，以及其他较小的驱动修复/改进。</p><p>关于Linux 6.0的媒体子系统更新的完整列表，请阅读这份拉动请求：</p><p><a href="https://lore.kernel.org/lkml/20220802164658.4e533a24@coco.lan/" _src="https://lore.kernel.org/lkml/20220802164658.4e533a24@coco.lan/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="e9dbd9dbdbd9d1d9dbd8dfdddfdcd1c7dd8cdcdada88dbdda98a868a86c7858887">[email protected]</span>/</a><br></p>   
</div>
            