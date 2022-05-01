
---
title: '驱动参数显示AMD RDNA3(RX 7000系列)IPC将翻倍'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0501/018a67baa6f47ff.webp'
author: cnBeta
comments: false
date: Sun, 01 May 2022 00:38:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0501/018a67baa6f47ff.webp'
---

<div>   
适用于 AMD 即将推出的 Radeon RDNA 3 GPU 架构的 Linux 驱动显示，AMD 正在全面修改 Workgroup Processor（WGP），并将 RDNA 1 和 RDNA 2 上每个 CU 的两个 SIMD32 改为四个 SIMD32。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0501/018a67baa6f47ff.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">AMD 在 RDNA 1 中引入了 WGP，每个 WGP 由两个 CU 组成。因此，与 RDNA 1（RX 5000系列）和RDNA 2（RX 6000）GPU相比，RDNA 3似乎有两倍的SIMD32能力。</p><p style="text-align: left;">新的 WGP 方法允许 AMD 在一个时钟周期内执行一条指令，而在以前的图形核心 Next（GCN）架构中，即Vega、Polaris和更早的架构，需要四个时钟周期来完成一条指令。这就是为什么 GCN 的设计与 NVIDIA 的同类产品相比往往效率低得多，至少在游戏方面是如此。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0501/83586cb5a7ab26b.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">因此，由于这一变化，理论上RDNA 3可以在半个时钟周期内执行一条指令，而RDNA 1和2则是一个周期。如果架构的其他部分在必要时也进行类似的改革，这有可能导致RDNA 3的每时钟周期指令（IPC）增加一倍。与更高的时钟和更多的CU搭配，最终产品的性能可能是目前最好的Radeon RX 6900 XT的两倍以上。</p>   
</div>
            