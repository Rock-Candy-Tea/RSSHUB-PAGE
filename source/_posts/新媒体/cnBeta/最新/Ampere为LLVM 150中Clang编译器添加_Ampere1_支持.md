
---
title: 'Ampere为LLVM 15.0中Clang编译器添加_Ampere1_支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0504/5a207098548544f.webp'
author: cnBeta
comments: false
date: Tue, 03 May 2022 23:52:14 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0504/5a207098548544f.webp'
---

<div>   
<strong>今天整合到 mainline LLVM 15.0 的代码中，为 Clang 编译器添加了 Ampere Computing 的“Ampere1”支持。</strong>这是他们的下一代服务器处理器，采用了内部的“Ampere Cores”内核设计。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0504/5a207098548544f.webp" alt="y49v9fjn.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Ampere 当前一代的 Ampere Altra 和 Ampere Altra Max 处理器已经非常具有竞争力，每个插座有多达 128 个物理核心，并采用了 Arm Neoverse-N1 7 纳米设计。然而，正如去年所指出的，Ampere 已经开始研究他们自己的核心设计，预计在 2022 年晚些时候推出。</p><p style="text-align: left;">去年，Ampere Next-Generation 被确认基于 5 纳米，具有符合 Arm ISA 的设计和下一代内存（DDR5）和存储能力。然而，这个 Ampere Altra/Altra Max 继任者的细节仍然不多，将迎来他们自己的核心设计。安培的2022年设计代号也称之为 Siryn。</p><p style="text-align: left;">被纳入LLVM的是"Ampere1"。对"Ampere1"目标的初始编译器支持被添加进来，并且符合Armv8.6-A ISA。这至少证实了Armv8.6-A用于这个最初的内部Ampere核心设计，而不是Armv9，但与Neoverse N1核心的Armv8.2相比已经有了明显的改进。</p><p style="text-align: left;">Ampere1编译器目标确认了Armv8.6-A与FP16和MTE（内存标签）扩展，以及启用投机障碍（SB）和（投机存储旁路安全（SSBS））选项。这个LLVM支持补丁是在11月添加到GCC编译器中的Ampere-1支持。</p>   
</div>
            