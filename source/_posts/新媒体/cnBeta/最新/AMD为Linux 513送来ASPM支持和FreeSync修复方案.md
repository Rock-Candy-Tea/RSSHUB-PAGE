
---
title: 'AMD为Linux 5.13送来ASPM支持和FreeSync修复方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Sat, 24 Apr 2021 07:57:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
在之前为Linux 5.13的AMDGPU功能带来Aldebaran支持、FreeSync
HDMI和其他改进的基础上，周五又有一轮更新被送来。鉴于Linux 5.13合并窗口将在下周启动，DRM-Next的新
"功能"更新时间已经过去，这个最新的AMDGPU拉取请求主要是关于错误修复。<br>
 <p>对新的Aldebaran加速器的支持进行了修复，解决了eDP问题，一些VanGogh APU问题也得到了解决，Renoir SMU问题也得到了解决，除此之外还有一些FreeSync的修复。</p><p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>在这个拉取请求中还加入了ASPM支持，即PCI Express主动状态电源管理功能。正如本月初所写的，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>终于准备为Navi 1x GPU启用ASPM，以帮助降低GPU的功耗。ASPM允许在总线上没有活动时关闭PCIe链接的电源或将其置于低功耗状态。除了一些极个别的硬件/驱动程序有退出延迟问题外，移动和桌面的功耗节省往往是值得的。</p><p>作为这个请求的一部分，现在发送的不仅仅是Navi 1x，还有为Vega和Polaris启用ASPM的补丁。因此，这可以让这些较新一代的GPU在Linux 5.13以上的状态下有一些适度的功率节省。虽然已经拖了很久，但至少终于有了眉目。</p><p>这项工作是通过DRM-Next的这个PR送来的。</p><p><strong>访问这里了解更多：</strong></p><p><a href="https://lists.freedesktop.org/archives/amd-gfx/2021-April/062513.html" _src="https://lists.freedesktop.org/archives/amd-gfx/2021-April/062513.html" target="_blank">https://lists.freedesktop.org/archives/amd-gfx/2021-April/062513.html</a><br></p>   
</div>
            