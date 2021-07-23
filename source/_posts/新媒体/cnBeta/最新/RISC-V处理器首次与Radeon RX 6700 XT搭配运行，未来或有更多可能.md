
---
title: 'RISC-V处理器首次与Radeon RX 6700 XT搭配运行，未来或有更多可能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0723/bc1a4bf8d3a2ac0.jpg'
author: cnBeta
comments: false
date: Fri, 23 Jul 2021 06:58:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0723/bc1a4bf8d3a2ac0.jpg'
---

<div>   
近期基于开源RISC-V架构的芯片设计公司SiFive的出镜率颇高，这和RISC-V架构不断推进有关<strong>。在上个月，SiFive发布了新的SiFive
Performance系列处理器内核，包括P270和PP550两款，后者是SiFive迄今为止性能最高的处理器。</strong><br>
 <p style="text-align: left;">新内核还受到了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的青睐，英特尔宣布将会基于Performance P550内核打造自己的RISC-V开发平台“Horse Creek”，而且会采用自家的7nm工艺制造。还传出英特尔有意花费超过20亿美元收购SiFive，并已经开始与SiFive展开谈判。</p><p style="text-align: left;">虽然RISC-V看起来势头不错，但大多数产品仍局限于针对低功耗设备的微控制器和简单的SoC，距离高性能运算等核心领域还有一段距离。不过近日计算机科学家Rene Rebe的一次操作，让我们看到了RISC-V处理器或许可以有更大的舞台。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0723/bc1a4bf8d3a2ac0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0723/bc1a4bf8d3a2ac0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">SiFive在去年推出了一款搭载RISC-V架构SoC的桌面级开发板，名为HiFive Unmatched。</p><p style="text-align: left;">这款Mini-ITX规格的主板基于SiFive FU740 SoC，集成了四个U74-MC内核和一个S7嵌入式内核，带标准的ATX电源连接口，配备了8GB的DDR4内存和32MB SPI 闪存芯片，提供了USB 3.2 Gen 1端口、一个PCI Express x16插槽（x8速率）、一个2280 M.2插槽、一个用于Wi-Fi/蓝牙适配器的2230 M.2插槽、microSD读卡器和千兆以太网。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0723/e089f405aa09da7.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0723/e089f405aa09da7.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">据hackster.io<a href="https://www.hackster.io/news/rene-rebe-patches-the-linux-kernel-for-world-s-first-look-at-a-radeon-rx-6700xt-on-a-risc-v-pc-31fddcb0d468" target="_blank">报道</a>，Rene Rebe通过修补Linux内核，利用这块开发板，让<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon RX 6700 XT与RISC-V处理器在Linux系统下运行。他花了十个小时的时间，在Linux系统里增加了对AMD Radeon RX 6700 XT显卡以及Mesa Gallium 21.1.5驱动程序的支持。不仅让Radeon RX 6700 XT显示Linux的GUI，甚至以硬件加速模式渲染3D图形并解码视频。这是第一次有人尝试使用RISC-V处理器与高性能GPU一起工作，而且挺成功的。</p>   
</div>
            