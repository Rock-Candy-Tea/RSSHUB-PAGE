
---
title: 'Linux 5.16将带来AMDGPU开源驱动的初步DisplayPort 2.0支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0928/89f45dbedf4caaf.jpg'
author: cnBeta
comments: false
date: Tue, 28 Sep 2021 06:38:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0928/89f45dbedf4caaf.jpg'
---

<div>   
由今日提交的 DRM-Next 功能更新可知，下一版 Linux 5.16 内核将带来诸多功能更新，以期在新年伊始推出稳定版本。<strong>其中比较引人关注的，就包括 AMDGPU 开源内核驱动程序的 DisplayPort 2.0 补丁，尤其是针对超高比特率（UHBR 10）的初始支持。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2021/0928/89f45dbedf4caaf.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">资料图</p><p>考虑到当前一代 Radeon RX 6000 系列显卡最高仅支持到 DisplayPort 1.4，新版内核驱动程序似乎正在为支持 DisplayPort 2.0 的下一代 GPU 做准备。</p><p>除了 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>GPU 的 DP 2.0 初始工作，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>开源驱动工程师们也在努力为 Linux 5.16 引入内核驱动支持，预计 2022 年的市场将迎来一些备受期待的应用。</p><p><img src="https://static.cnbetacdn.com/article/2021/0928/7303977205501f1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://lists.freedesktop.org/archives/amd-gfx/2021-September/069487.html" target="_self">FreeDesktop.org</a>）</p><p><strong>以下是今日针对 DRM-Next 的 AMDGPU 查询请求的一些重点概括：</strong></p><blockquote><p>● 对 DisplayPort 2.0 的初步支持现已到位。</p><p>● 更新支持最新推出的 Yellow Carp 和 Cyan Skillfish 图形。</p><p>● Video Core Next 优先级队列调整。</p><p>● DCN 3.1 节电改进（随 Yellow Carp / Rembrandt 到来）。</p><p>● 其它 Bug 修复和代码更新，包括电源管理 / BACO 前端、RAS 等。</p></blockquote><p>感兴趣的朋友，还请留意今年 11 月随 Linux 5.16 合并窗口而来的完整补丁列表。</p>   
</div>
            