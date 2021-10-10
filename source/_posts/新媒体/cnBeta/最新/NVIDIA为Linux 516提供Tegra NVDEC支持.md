
---
title: 'NVIDIA为Linux 5.16提供Tegra NVDEC支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1010/f620729858efeac.jpg'
author: cnBeta
comments: false
date: Sun, 10 Oct 2021 12:16:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1010/f620729858efeac.jpg'
---

<div>   
<strong>Tegra DRM驱动程序的最新变化是在本周五发出的，主要是为Linux
5.16准备的新材料，这次值得注意的是，NVIDIA的NVDEC驱动程序被纳入其中。</strong>在经历了多轮公共代码审查之后，Linux
5.16的Tegra DRM驱动更新包括引入NVDEC驱动以加速视频解码。这项开源的视频解码引擎工作是针对Tegra
X1（Tegra210）和更新的产品，包括目前的Tegra X2和Xavier SoC。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/1010/f620729858efeac.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>早在2月份，NVIDIA提供了Tegra视频文档，作为其"开放GPU文档"的一部分，其中包括NVDEC和NVENC接口。为Linux 5.16合并的这套NVDEC代码也是由NVIDIA编写的。</p><p>除了内核代码，在用户空间当中还有VAAPI-Tegra-Driver，它为使用该内核代码的Tegra SoC提供视频加速API（VA-API）接口，目前支持的是H.264和MPEG2的解码。</p><p>除了NVDEC驱动程序，Linux 5.16的Tegra变化还包括对其缓冲区对象代码进行"相当大的"重写，以使其与DMA-UF基础设施的预期更加一致。这反过来又使翻页和其他改进更加有效。用于Linux 5.16的Tegra显示/图形驱动补丁列表可通过该拉动请求找到：</p><p><a href="https://lists.freedesktop.org/archives/dri-devel/2021-October/326743.html" _src="https://lists.freedesktop.org/archives/dri-devel/2021-October/326743.html" target="_blank">https://lists.freedesktop.org/archives/dri-devel/2021-October/326743.html</a><br></p><p>当涉及到GeForce桌面方面的开源NVIDIA图形，如Nouveau驱动，目前没有任何新的报告，目前，任何比GeForce GTX 700系列（开普勒或麦克斯韦）更新的产品基本上在Linux的表现还是一团糟。</p>    
</div>
            