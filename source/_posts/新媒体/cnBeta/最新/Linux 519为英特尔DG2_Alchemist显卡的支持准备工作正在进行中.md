
---
title: 'Linux 5.19为英特尔DG2_Alchemist显卡的支持准备工作正在进行中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0508/736cb479a9ca3ad.jpg'
author: cnBeta
comments: false
date: Sun, 08 May 2022 09:16:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0508/736cb479a9ca3ad.jpg'
---

<div>   
英特尔的开源Linux图形驱动工程师为即将到来的Linux 5.19合并窗口送来了另一个"i915"内核图形驱动的大杂烩。周五的拉动请求最终加入了DG2/Alchemist PCI IDs，用于"向下"设计。这标志着Linux 5.19版本可能是英特尔Arc显卡正常工作的基本版本要求。<br>
<p>为确定的DG2设计的PCI ID是周五的这些改动的一部分，并与其他DG2改进一起出现在Linux 5.19中。正如早先的DRM-Next版本所涵盖的那样，Linux 5.19也是第一个支持DG2计算的版本。</p><p><img src="https://static.cnbetacdn.com/article/2022/0508/736cb479a9ca3ad.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>周五的版本还带来了最初的一组Raptor Lake P ID。早在Linux 5.17中就有了最早的Raptor Lake S支持，而对于v5.19则率先开始支持Raptor Lake P。RPL-P支持是基于现有的Alder Lake P代码作为继承者。Raptor Lake P的Linux内核图形驱动支持是在过去一个月里形成的，它也被添加到Mesa的OpenGL和Vulkan用户空间驱动支持中。</p><p>这个更新版本的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>DRM驱动还包含对电源井代码的重构，GVT-g的改进，以及各种错误的修复。</p><p>用于Linux 5.19的DRM-Next的新功能代码的时期已经接近尾声，而那些想看到周五送来的最新一批补丁的人可以看到这个拉动请求的所有细节：</p><p><a href="https://lore.kernel.org/dri-devel/87bkwbkkdo.fsf@intel.com/" _src="https://lore.kernel.org/dri-devel/87bkwbkkdo.fsf@intel.com/" target="_blank">https://lore.kernel.org/dri-devel/<span class="__cf_email__" data-cfemail="3b030c59504c5950505f54155d485d7b52554f5e5715585456">[email protected]</span>/</a><br></p>   
</div>
            