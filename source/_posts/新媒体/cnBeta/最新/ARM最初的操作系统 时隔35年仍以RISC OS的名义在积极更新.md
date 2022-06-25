
---
title: 'ARM最初的操作系统 时隔35年仍以RISC OS的名义在积极更新'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0625/69ab6ce254941ed.webp'
author: cnBeta
comments: false
date: Sat, 25 Jun 2022 05:05:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0625/69ab6ce254941ed.webp'
---

<div>   
<strong>作为初代 ARM 计算机 Acorn Archimedes 所使用的操作系统，RISC OS 在 35 年后的今天依然表现良好。</strong>1987 年 6 月，Acron 推出了起价 800 英镑的 Archimedes A305 / A310 计算机。在那个年代，其产品性能设计相当激进，且提供了当时名为 Arthur 的新操作系统。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0625/69ab6ce254941ed.webp" referrerpolicy="no-referrer"></p><p>Dick Pountain 在 PC 世界的报道中激动地表示 —— 即使加载大型应用程序，它也能够游刃有余，转瞬间就能够完成任务。</p><p>不过 Arthur 和 Acorn 早期 MOS（BBC Micro 操作系统）之间的联系，其实也相当有趣。只是由于采用了 BBC BASIC 实现的原型图形桌面，才看起来非常不同。</p><p>1989 年的时候，Arthur 被更名为 RISC OS，并于次年迎来了第二个大版本。同年 Sun 开始销售 7500 英镑的 SPARCstation 1，DEC 也推出了基于 MIPS R2000 芯片组、售价 8800 英镑的 DECstation 3100。</p><p>然而 RISC OS 的发展历史还是有些坎坷，部分原因可归咎于 Acron 剥离了 ARM、并最终退出了计算机市场。其后续更名为 Element 14，接着被博通（Broadcom）给收购。</p><p>值得一提的是，ARM 联合设计师 Sophie Wilson 至今仍在工作，且这与该操作系统的所有权发生了戏剧性变化有关。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/46d73b64b22e084.jpg" referrerpolicy="no-referrer"></p><p>RISC OS 的一个分支，仍然有对 Acron 时代独特的 26-bit 模式提供支持，不过今天它主要在商业 Virtual Acron 模拟器上运行。</p><p>另一个分支则为最近的 ARM 芯片 32-bit 模式而设计，现归于 RISC OS Developments 旗下，2018 年时已完全开源。</p><p>开发与维护工作由 RISC OS Open Ltd 的 ROOL 团队负责，目前有提供各种现有 ARM 硬件的下载支持（比如 Titanium 桌面）。</p><p>如果你没有配套的硬件，但又想要在 21 世纪体验一把 RISC OS，那不妨下载一个名为《RPCemu》的 FOSS 模拟器去尝试一下。</p><p>同时 RISC OS Developments 提供了一个名为 RISC OS Direct 的树莓派特殊发行版，它基于 ROOL 的最新稳定版本（5.28）、并且提供了各种额外的应用程序。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/0c07cff8a3fe87f.png" alt="RISC OS Direct.png" referrerpolicy="no-referrer"></p><p>时至今日，RISC OS Developments 仍在积极为 RISC OS 开发新功能。比如近日发布的一个源自 OpenBSD 的新 TCP/IP 堆栈，特点是带来了对 IPv6 的支持，不过 Wi-Fi 支持还得再等待一段时间。</p><p>此外还有一款仍在开发中的 Iris 网络浏览器，具有 RISC OS 的外观风格 + WebKit 引擎、以更好地兼容现代网络，但它仅供付费支持者使用。不过除了原生浏览器， 我们也可选择 NetSurf 和其它应用程序。</p><p>剩余限制主要是 SMP，毕竟作为 1980 年代的操作系统，它并没有预见到对 21 世纪主流多核处理器技术的底层支持（RISC OS 实际上仅支持单个 CPU 内核），目前官方正在努力搞定这个问题。</p><p>其中一项实验是让 NetBSD 在另一个内核上运行、另一项实验是让 Genode OS 与 RISC OS 一起运行，此外还有考虑为 RISC OS 内核本身添加对 SMP 的支持。</p><p>最后，现时 Reg FOSS 唯一能想到的一个仍在积极维护、并于现代硬件上运行的操作系统，就是<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a> macOS 的前身 —— NeXTstep 。</p><p>奇妙的是，最新版本的 Apple Silicon Mac 设备，也已从 Intel x86 CPU、转而采用自研的 ARM 芯片组。</p>   
</div>
            