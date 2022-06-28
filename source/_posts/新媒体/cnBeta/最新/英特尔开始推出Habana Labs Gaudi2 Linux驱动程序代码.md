
---
title: '英特尔开始推出Habana Labs Gaudi2 Linux驱动程序代码'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0628/d9e71c3b000c8c3.jpg'
author: cnBeta
comments: false
date: Tue, 28 Jun 2022 05:37:57 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0628/d9e71c3b000c8c3.jpg'
---

<div>   
在上月的 VISION 会议上，英特尔宣布了 Gaudi2 硬件。<strong>作为该公司旗下 Habana Labs 用于训练和推力的第二代加速器，它也同步迎来了开源 Linux 内核驱动 / 用户空间软件堆栈更新。</strong>英特尔宣称 Gaudi2 的 AI 训练性能是英伟达 A100 竞品方案的两倍，且芯片制造工艺也从初代 16nm 升级到了 7nm 。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0628/d9e71c3b000c8c3.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://www.phoronix.com/scan.php?page=news_item&px=Intel-Gaudi2-Linux-Driver" target="_self">Phoronix</a>）</p><p>此外 Gaudi2 迎来了 3 倍的 TPC 改进，32GB HBM2 高带宽内存增加到了 96GB HBM2e、SRAM 缓存也翻倍到了 48MB，辅以 24×100 GbE 连接，但热设计功耗（TDP）也从 350W 提升到了 600W 。</p><p>在发布一个多月后，Habana Labs Gaudi2 的开源驱动程序工作也在有条不紊地推进中。而当前的 Gaudi2 支持，正好建立在现有的 Gaudi 和 Goya 加速器内核驱动程序（habanalabs）的基础上。</p><p><img src="https://static.cnbetacdn.com/article/2022/0628/895862e6130dd16.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Habana.ai 白皮书揭示了与 Gaudi2 架构相关的更多信息</p><p>从驱动角度来看，Gaudi2 与初代非常接近，整体架构也是一个样。启用 Gaudi2 大约需要 15.8 万行新内核代码，但其中大部分属于“头文件”（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>GPU 内核驱动程序也有大量头文件）。</p><p>截至目前，新的头文件主要代表了该主线驱动程序启用 Gaudi2 支持所需的大部分代码变动。除了内核驱动工作，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>今日还发布了 TPC_LLVM 1.1（针对 Habana Labs 加速器的新版开源编译器）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0628/48830e3f6f4994a.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">TPC_LLVM 1.1 添加了对 Gaudi2 及新的 Greco ASIC 编译器的支持</p><p>与此同时，英特尔也在努力更新 SynapseAI Core for Gaudi2 开源组件，新补丁系列用于新的 Gaudi2 内核驱动程序代码。</p><p>鉴于新版是从相同的 Gaudi 架构演变而来，预计后续的代码审核工作也会相当顺利，那样我们就有望在 v5.20 内核周期内尽快添加对 Intel Gaudi2 的支持。</p><p>最后，英特尔还在 VISION 2022 会议上宣布了从 Goya 升级而来、针对深度学习应用而作出效率优化的 Greco 加速卡。</p>   
</div>
            