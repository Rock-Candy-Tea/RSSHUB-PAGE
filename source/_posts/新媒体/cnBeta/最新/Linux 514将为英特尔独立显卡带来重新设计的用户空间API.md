
---
title: 'Linux 5.14将为英特尔独立显卡带来重新设计的用户空间API'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0402/e3df7610ff36a7b.jpg'
author: cnBeta
comments: false
date: Fri, 28 May 2021 11:44:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0402/e3df7610ff36a7b.jpg'
---

<div>   
<strong>今年夏天的Linux 5.14内核将为英特尔的DG1显卡和他们未来的独立显卡产品带来一个重新设计的用户空间API（User-Space
API）。</strong>对英特尔内核图形驱动的的这一改变，目前被标记为
"broken"，直到它被证明足以满足用户空间的需求并保持稳定，主要是为了处理设备卡上的板载显存（专用vRAM）。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0402/e3df7610ff36a7b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0402/e3df7610ff36a7b.jpg" referrerpolicy="no-referrer"></a></p><p>一段时间以来，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的开源驱动工程师一直在研究重新设计的用户空间API，以适应DG1和未来的英特尔独立图形处理器。这个改变后的uAPI对于用户空间能够控制他们想要的内存区域是必要的，无论他们是想利用系统内存还是现在连接到dGPU的设备本地内存。</p><p>新的API已经允许查询可用的内存区域（即系统或本地设备内存的可用性），一个类似于GEM创建的新的ioctl，可以接受一连串可能的扩展，然后一个可以在那里使用的扩展，允许指定一个内存区域来用于分配。</p><p>虽然这个重新设计的用户空间API已经通过DRM-Next的方式送入了Linux 5.14，但在这个内核中，它被隐藏在CONFIG_BROKEN选项后面，还不能保证API的可用性与稳定性。仍然在解决的是英特尔内核驱动程序在利用TTM内存管理方面的工作。一旦完成了向TTM内存管理的转换，并且发布了使用新uAPI的最新Mesa补丁，在所有这些都得到验证之后，新的用户空间API代码将真正暴露出来（而不是隐藏在broken选项之后），并且最终在Linux内核中加入DG1显卡的PCI ID。</p><p>这个为英特尔独立显卡重新设计的用户空间API今天作为drm-intel-gt-next的一部分被推送，用于在Linux 5.14合并窗口启动前的一个月内，在DRM-Next中进行最后的准备工作。在英特尔图形方面，Linux 5.14还将启用Alder Lake P和其他变化。</p>   
</div>
            