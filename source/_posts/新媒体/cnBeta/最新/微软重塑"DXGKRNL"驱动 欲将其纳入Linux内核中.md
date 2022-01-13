
---
title: '微软重塑"DXGKRNL"驱动 欲将其纳入Linux内核中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0113/2d3c475f8b13a7d.jpg'
author: cnBeta
comments: false
date: Thu, 13 Jan 2022 11:04:21 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0113/2d3c475f8b13a7d.jpg'
---

<div>   
<strong>早在2020年，微软宣布DXGKRNL驱动为内核驱动组件，用于支持Windows Subsystem for Linux（WSL2）中的GPU加速用例。</strong>最初的DXGKRNL驱动很快就被上游内核开发者提出了各种问题，而现在，在过去的一年里，微软一直在重新制作这个内核驱动，并在周三发布了新版本。<br>
 <p>DXGKRNL是他们的"DirectX"内核驱动组件，用于<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Subsystem for Linux（WSL2），支持Hyper-V环境下的图形加速和GPU计算。DXGKRNL也将用于他们即将推出的Android Windows子系统（WSA）。DXGKRNL作为Hyper-V虚拟计算设备的驱动程序，主要是用于GPU，但也可以扩展到其他AI/ML加速器和Windows主机的类似设备。OpenGL、Vulkan、OpenCL、OpenVINO、oneAPI和CUDA等API旨在与支持的用户空间库/组件一起使用时，可以在DXGKRNL上运行。</p><p><a href="https://static.cnbetacdn.com/article/2022/0113/2d3c475f8b13a7d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0113/2d3c475f8b13a7d.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>新版本的DXGKRNL解决了上游代码审查人员在前一轮补丁中提出的问题。微软还更好地完成了其vGPU/计算硬件虚拟化支持代码。这些补丁也是"从头开始重建"，比之前的补丁组织得更有效。</p><p>微软最初也因为DXGKRNL而受到批评，因为它依靠闭源的CUDA和DirectX用户空间组件来运行。对此，他们现在正在庆祝<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>提供的开源用户空间API支持，现在OpenCL/OpenVINO/oneAPI支持在这个内核驱动上用于英特尔图形硬件。</p><p>补丁系列的介绍信指出："在英特尔计算运行时间项目和libdxg之间，我们现在在WSL内部有一个完全开源的虚拟化计算栈的实现。我们将继续支持针对我们的计算抽象的开源用户空间API，以及闭源的API（CUDA、DX12），让API所有者和合作伙伴决定什么对他们最有意义。"</p><p><img src="https://static.cnbetacdn.com/article/2022/0113/506c78beefd4322.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>更新的微软DXGKRNL补丁系列可以在内核邮件列表中找到。到目前为止，Greg Kroah-Hartman已经对新的补丁进行了评论，有一些技术问题需要解决，同时我们等待着看这个微软内核驱动程序是否在2022年有机会进入主线内核，或者只是能够让微软Windows主机上的Windows Subsystem for Linux / Windows Subsystem for Android受益的内容。</p><p>不计算用户空间的工作，DXKGRNL内核驱动要增加了16800行的新代码。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/cover.1641937419.git.iourit@linux.microsoft.com/" _src="https://lore.kernel.org/lkml/cover.1641937419.git.iourit@linux.microsoft.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="fc9f938a998ed2cdcac8cdc5cfcbc8cdc5d29b9588d29593898e9588bc9095928984d291959f8e938f939a88d29f9391">[email protected]</span>/</a><br></p>   
</div>
            