
---
title: '微软又进行了一次DirectX Linux内核驱动的移植尝试'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0302/3fc0fefeb73beb4.jpg'
author: cnBeta
comments: false
date: Wed, 02 Mar 2022 12:31:49 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0302/3fc0fefeb73beb4.jpg'
---

<div>   
微软在周二发布了他们的"DXGKRNL"Linux内核驱动的第三次迭代，主要用于实现DirectX/Hyper-V计算支持，特别是在Windows Subsystem for Linux/Windows Subsystem for Android中使用。<br>
 <p>这个内核驱动是<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>在WSL中的GPU加速工作的一部分，自从最初在2020年发布以来，一直受到上游Linux内核开发者的抵制。</p><p><a href="https://static.cnbetacdn.com/article/2022/0302/3fc0fefeb73beb4.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0302/3fc0fefeb73beb4.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>早在一月份，微软发布了一个重新设计的DXGKRNL驱动，用于支持WSL/WSA的Hyper-V计算设备，并允许OpenGL、OpenCL、Vulkan、OpenVINO、oneAPI和CUDA等进行加速。除了内核补丁系列被"从头开始重建"之外，为它可能被主流化打开了一点大门：至少完全开源的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>计算运行时栈可以在DXGKRNL栈之上工作。区别在于最初只有闭源的用户空间驱动程序可用，而现在至少有一个"开源"的用户空间驱动程序可用，以解决成为主线包容障碍的问题，微软也有开源的libdxg库作为其计算设备抽象的接口。</p><p>本周推出的是DXGKRNL v3驱动。这个驱动现在有30个补丁（v2版有24个补丁），这个驱动的新内核代码有16190行。</p><p>与前一轮补丁相比，v3补丁带来了各种低级别的改进。然而，要让这些代码被接受到主线内核中去，仍然是一个艰难的过程。著名的Linux内核开发者Christoph Hellwig已经对这一系列进行了评论，认为它并没有解决什么实际问题。</p><p>了解更多：</p><p><a href="https://lore.kernel.org/lkml/cover.1646161341.git.iourit@linux.microsoft.com/" _src="https://lore.kernel.org/lkml/cover.1646161341.git.iourit@linux.microsoft.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="24474b5241560a151210121512151710150a434d500a4d4b51564d5064484d4a515c0a494d47564b574b42500a474b49">[email protected]</span>/</a><br></p>   
</div>
            