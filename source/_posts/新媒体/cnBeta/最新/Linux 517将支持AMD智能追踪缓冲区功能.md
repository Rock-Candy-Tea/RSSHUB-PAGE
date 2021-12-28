
---
title: 'Linux 5.17将支持AMD智能追踪缓冲区功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1228/c01703df854a617.png'
author: cnBeta
comments: false
date: Tue, 28 Dec 2021 08:43:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1228/c01703df854a617.png'
---

<div>   
作为 AMD APU / SoC 芯片的新特性之一，“智能追踪缓冲区”（简称 STB）可分析系统在遇到故障时调用的最后一项功能。<strong>通过在后台保持透明运行，AMD STB 得以帮助隔离系统故障，以便用户在后续借助 DebugFS 接口来读取分析。</strong>最新消息是，其已做好了为 Linux 5.17 提供支持的准备。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1228/c01703df854a617.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://git.kernel.org/pub/scm/linux/kernel/git/pdx86/platform-drivers-x86.git/commit/?h=for-next&id=426c0ff27b833939ed434b4a468bdc010864922a" target="_self">Kernel.org</a>）</p><p>虽然补丁代码描述中没有明确提及 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> STB 支持的硬件类型，但其它代码有指代它至少支持 Cezanne SoC 。</p><p>Radeon 图形方面，AMD 已经为 Linux 5.17 的 STB 支持做好了初始准备。至于下个内核版本，AMD PMC 驱动程序也已集成 STB 支持。</p><p><img src="https://static.cnbetacdn.com/article/2021/1228/f24acfdec7e2cf9.jpg" referrerpolicy="no-referrer"></p><p>目前该补丁位于 platform-drivers-x86 for-next 分支，为电源管理控制器（PMC）驱动程序添加了 AMD 智能跟踪缓冲区支持。</p><p>按照计划，Linux 5.17 合并窗口将于 2022 年 1 月正式开启。如果一切顺利，稳定版内核有望于 3 月下旬前后正式发布。</p>   
</div>
            