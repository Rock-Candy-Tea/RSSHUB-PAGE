
---
title: 'Linux 5.18将剔除对Andes NDS32 CPU架构的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0324/84343d0fdb4ce9d.jpg'
author: cnBeta
comments: false
date: Thu, 24 Mar 2022 06:43:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0324/84343d0fdb4ce9d.jpg'
---

<div>   
虽然早在 2018 年，就有开发者在 Linux 4.17 内核中添加了对 Andes 的 NDS32 CPU 架构的支持。<strong>但可惜由于缺乏积极维护，Linux 5.18 内核团队已决定将 AndesCore NDS32 架构的支持代码剔除出去。</strong>此前相关内核端口一直被用于支持 Andes Technology 公司老旧的 N13 / N15 / D15 / N10 / D10 系列处理器。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0324/84343d0fdb4ce9d.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Andes N10 是受 NDS32 移除影响的 CPU 设计之一</p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=Andes-Tech-NDS32-Removal" target="_self">Phoronix</a> 指出：这些处理器内核使用 16 / 32-bit 的 AndeStar 类 RISC 架构，特点是兼顾高性能与低空间占用，适用于从物联网到数字信号控制、以及其它嵌入式用例。</p><p>尽管当今世界仍有一些在使用的 AndesCore NDS32 处理器，但由于缺乏对 CPU 架构端口的主动上游维护，它最终还是难以躲过被淘汰的命运。</p><p>由 asm-generic <a href="https://lore.kernel.org/lkml/CAK8P3a0DeZ4Gx6fOqLkjmA7kNYW5ZHq8BUpWTXXdqdtxcHRNLg@mail.gmail.com/" target="_self">查询请求</a>可知，Linux 5.18 将正式剔除 NDS32 的内核代码支持。Arnd Bermann 总结道：</p><blockquote><p>nds32 架构将告别其在 Linux 内核中的旅程，相关硬件仍在使用、代码也处理被合理使用的状态，但可惜主线端口已不再被积极维护。</p><p>正因如此，所有剩余的用户，也都被认为是不再需要更新至未来的供应商内核版本。</p></blockquote><p>鉴于 AndeStar V3 时代的硬件只出现在深度定制的嵌入式系统中，绝大多数现代 Linux 内核用户都不再有继续运行 NDS32 的需求。</p><p>好消息是，诸如 Andes Tech 的 SDK 之类的树外内核端口仍在，且现有的 Linux 长期支持（LTS）内核系列仍会提供一段时间的 NDS32 支持。</p><p>另一方面，基于 32 / 64-bit RISC-V 设计的 AndesCore 处理器（比如 AndesStar V5 指令集架构），前景还是相当光明的。</p>   
</div>
            