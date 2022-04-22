
---
title: 'OpenBSD 7.1正式发布：完善对Apple Silicon的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0422/b1af9a52a75ee42.webp'
author: cnBeta
comments: false
date: Fri, 22 Apr 2022 00:24:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0422/b1af9a52a75ee42.webp'
---

<div>   
<a href="https://www.openbsd.org/71.html" target="_blank"><strong>OpenBSD 7.1 于今天正式发布</strong></a><strong>。新版本亮点之一就是完善了对 Apple Silicon（苹果 M1 芯片）的支持。</strong>在 OpenBSD 7.1 中，Apple Silicon 的支持现在被认为是“可普遍使用”，支持 M1 设备的键盘/触控板，增加了电源管理控制器驱动，I2C 和 SPI 控制器驱动，以及其他各种支持 Apple Silicon 硬件的驱动。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0422/b1af9a52a75ee42.webp" alt="6iernrky.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">OpenBSD 7.1 还针对 64 位 ARM（ARM64）和 RISC-V 架构进行了优化。OpenBSD 7.1 还带来了 SMP 内核的改进，支持共享匿名内存的 futexes，以及更多。</p><p style="text-align: left;">在图形方面，根据 Linux 5.15.26 中的状态更新了 Linux DRM 代码，以及现在启用了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>Elkhart Lake / Jasper Lake / Rocket Lake 支持。在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>方面，现在支持Van Gogh APU、Rembrandt / Yellow Carp APU和Navi 22/23/24 GPU。BSD操作系统中的图形驱动支持仍然主要是对现有的开源Linux图形驱动代码的移植。</p><p style="text-align: left;">OpenBSD 7.1具有对Apple Silicon和AMD Radeon RX 6000系列图形的可用支持，以及其他硬件的改进。OpenBSD 7.1还包括VMM的改进，libc解析器对DNSSEC的支持，其他各种英特尔Jasper Lake和Tiger Lake硬件支持的改进，IGC现在被合并为英特尔2.5Gb以太网控制器的驱动程序。</p>   
</div>
            