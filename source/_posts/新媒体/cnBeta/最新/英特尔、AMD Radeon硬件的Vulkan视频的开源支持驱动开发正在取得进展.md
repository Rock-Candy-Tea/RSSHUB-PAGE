
---
title: '英特尔、AMD Radeon硬件的Vulkan视频的开源支持驱动开发正在取得进展'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1115/ea1f28d30cbc970.jpg'
author: cnBeta
comments: false
date: Mon, 15 Nov 2021 14:30:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1115/ea1f28d30cbc970.jpg'
---

<div>   
<strong>开源Vulkan驱动对视频解码（未来编码可能也会出现）扩展的支持继续在Radeon"RADV"和Intel"ANV"Mesa驱动中推进。</strong>本月早些时候，著名的开源Linux图形驱动专家David
Airlie（Red Hat）开始试验RADV
Vulkan视频支持，之后也在调试英特尔的Mesa驱动的Vulkan视频。这些努力一直在继续，并取得了最新的阶段性成果。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1115/ea1f28d30cbc970.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>最初，Airlie正在为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> VCN"Video Core Next"引擎进行Vulkan视频H.264解码工作，该引擎由较新的Radeon图形处理器使用。今天，他合并了对能够使用旧的UVD"统一视频解码器"引擎的支持。反过来，这现在允许H.264解码适用于从Vega一直到最初的GCN 1.0"南方群岛"GPU的旧AMD GPU。</p><p>Airlie在这篇博文中提到了对Vulkan视频的UVD支持。</p><p>了解更多：</p><p><a href="https://airlied.blogspot.com/2021/11/h264-more-amd-hw-worked-on.html" _src="https://airlied.blogspot.com/2021/11/h264-more-amd-hw-worked-on.html" target="_blank">https://airlied.blogspot.com/2021/11/h264-more-amd-hw-worked-on.html</a></p><p>在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>方面，他已经通过这个Gitlab分支发布了英特尔ANV Vulkan视频的初步修改，供感兴趣的人参考：</p><p>获取扩展：</p><p><a href="https://gitlab.freedesktop.org/airlied/mesa/-/tree/anv-vulkan-video-prelim-decode" _src="https://gitlab.freedesktop.org/airlied/mesa/-/tree/anv-vulkan-video-prelim-decode" target="_blank">https://gitlab.freedesktop.org/airlied/mesa/-/tree/anv-vulkan-video-prelim-decode</a></p><p><a href="https://static.cnbetacdn.com/article/2021/1115/8cb133ed6f847b2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1115/8cb133ed6f847b2.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>Airlie正在继续研究代码，并找出如何在驱动之间最好地分享/利用Vulkan视频支持，并最终找出将这种支持上移到主线Mesa的路径。目前，他的重点是H.264和H.265，以及Vulkan视频编码扩展。希望在看到VP9和AV1等拥有Vulkan视频扩展的上游之前不会有太多的时间。</p><p>Vulkan视频扩展在今年早些时候就已经以临时形式出现了。希望它们能很快得到确认，并反过来看到更广泛的驱动程序支持和发现跨平台多媒体软件开始使用这些扩展作为基于GPU的视频编码/解码的行业标准。</p>   
</div>
            