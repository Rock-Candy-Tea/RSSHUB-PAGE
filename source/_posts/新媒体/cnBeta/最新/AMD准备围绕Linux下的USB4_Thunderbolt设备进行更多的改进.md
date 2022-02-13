
---
title: 'AMD准备围绕Linux下的USB4_Thunderbolt设备进行更多的改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0213/9e9251a9fb5bae3.jpg'
author: cnBeta
comments: false
date: Sun, 13 Feb 2022 12:47:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0213/9e9251a9fb5bae3.jpg'
---

<div>   
作为AMD Rembrandt APU支持USB4和基于Thunderbolt
3协议的规范的一部分，AMD最近几个月一直在进行一些Linux驱动改进，以加强对其平台的USB4/Thunderbolt支持。AMD近来的补丁系列包括USB4
DisplayPort通道和其他USB4/Thunderbolt工作。<br>
<p>他们的最新成果是围绕"is_thunderbolt"检查重构各种Linux内核，如果设备是通过Thunderbolt连接，而不是直接通过PCIe连接，内核内的驱动程序就会改变其行为，并作为确定设备是否有可能被移除/外部连接的一种手段。is_thunderbolt检查过程原本是为早期的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>Thunderbolt控制器设计的，它不包含命令完成这一事件。</p><p>AMD Linux工程师Mario Limonciello在过去一周发布了"is_thunderbolt"系列补丁的几个修订版，因此最终预期的驱动行为涵盖了"并非来自英特尔的USB4设计"（也就是AMD）。is_thunderbolt检查被认为是非常规的，其他各种与Thunderbolt相关的内核代码变化也是拟议的补丁系列的一部分。</p><p>作为12个补丁的一部分，本次补丁还清理了AMD和Nouveau驱动代码中涉及eGPU/可移动GPU支持和其他怪异的路径。</p><p><img src="https://static.cnbetacdn.com/article/2022/0213/9e9251a9fb5bae3.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>更多细节见这个补丁系列：</p><p><a href="https://lists.freedesktop.org/archives/dri-devel/2022-February/341724.html" _src="https://lists.freedesktop.org/archives/dri-devel/2022-February/341724.html" target="_blank">https://lists.freedesktop.org/archives/dri-devel/2022-February/341724.html</a><br></p><p>可以看出，AMD正在为Linux进行更多的USB4/Thunderbolt处理改进，以改善非Intel平台下的表现，而AMD方面的USB4正在与Ryzen 6000移动系列APU一起引入。</p>   
</div>
            