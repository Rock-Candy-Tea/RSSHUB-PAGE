
---
title: 'NVIDIA解锁GSP方案 以进一步改善系统性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0119/430be9409fe740a.webp'
author: cnBeta
comments: false
date: Wed, 19 Jan 2022 08:51:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0119/430be9409fe740a.webp'
---

<div>   
<strong>2016 年，NVIDIA 公司宣布正在开发基于 RISC-V 指令集架构（ISA）的新型 GPU 系统处理器（GSP）解决方案，以替代现有代号为 Falcon 的快速逻辑控制器处理器。</strong>这种新型 RISC-V 处理器的代号为 NV-RISCV，已经作为 GPU 的控制核心被广泛使用，在庞大的GPU核心池中协调一切。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0119/430be9409fe740a.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">自今天发布的 510.39 驱动开始，NVIDIA 决定开始向更广泛的应用开放 NV-RISCV CPU。根据英伟达的文件，目前这只适用于部分 GPU，主要是以数据为中心的 Tesla 加速器。在文件中写道</p><p style="text-align: left;">● 一些 GPU 包括一个 GPU 系统处理器（GSP），可用于卸载 GPU 初始化和管理任务。该处理器由固件文件 /lib/firmware/nvidia/510.39.01/gsp.bin 驱动。一些特定的产品目前默认使用GSP，而更多的产品将在未来的驱动程序版本中利用GSP的优势。</p><p style="text-align: left;">● 统上由驱动程序在CPU上执行的卸载任务可以提高性能，因为对GPU硬件内部的访问延迟较低。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0119/9c3db0e7530bb20.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">如本文所示，许多任务如 GPU 管理和初始化是由CPU上的驱动程序执行的。CPU在传统上是外部的（相对于GPU），导致在提出请求时有较高的延迟。嵌入到GPU中的CPU导致即时交付所请求的数据/行动，从而能够降低延迟并提高性能。</p><p style="text-align: left;">我们还没有看到英伟达能用它做什么，以及在不启用GSP的情况下，使用旧方法的性能损失有多大。这也为GPU和加速器指出了一个新的方向，一个独立的状态，CPU在片上得到整合，而不是依赖于外部硬件。</p>   
</div>
            