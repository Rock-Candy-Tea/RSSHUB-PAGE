
---
title: '龙芯CPU现合并到Linux 5.19内核主线中 但无法在硬件上启动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp'
author: cnBeta
comments: false
date: Sat, 04 Jun 2022 01:51:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp'
---

<div>   
<strong>经过讨论之后，Linus Torvalds 今天宣布将龙芯架构代码合并到 Linux 5.19 内核主线中。</strong>然而，由于一些代码尚未通过审查，而 CPU 架构代码已经到位，一些关键驱动程序尚未登陆，因此 Linux 5.19 无法在所述硬件上启动。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp" referrerpolicy="no-referrer"></a></p><p>龙芯（LoongArch）是基于 MIPS64 的 CPU 架构，但是随着上游的 MIPS64 架构实际上已经消亡，龙芯中科开始着手开发自己的 ISA。 LoongArch 被描述为受到 MIPS64 和 RISC-V 的启发，并且一些 LoongArch 内核代码实际上是在重用或密切复制现有的 MIPS 代码。</p><p>今年早些时候，LoongArch 作为主要的系统编译器被添加到 GCC 12 中。与其他 Arm 或 RISC-V 设计相比，目前这一代龙芯 3A5000 CPU 的性能在这个阶段并不算太强悍。</p><p>即使 Linux Kernel 5.19 中无法启动龙芯的系统，但将 LoongArch 引入 Linux 5.19 是有意义的。龙芯 LoongArch CPU 架构的内核移植已经通过了 10 多轮的审查，以获得 Linux 内核的支持。</p><p>开发人员希望将 CPU 架构代码进行主流化，以便让他们能够为 GNU C 库 (Glibc) 提交 LoongArch 支持代码。对他们的 Glibc 目标进行主流化首先需要使用可靠的用户空间 ABI 确定内核支持。但由于 Glibc 2.38 预计在 8 月发布，因此需要为 Linux 5.19 合并 LoongArch，以便有足够的时间在 7 月发布该版本，并让 Glibc LoongArch 代码完成下一个版本的发布。</p><p>现在合并 LoongArch 还可以减少 Linux 5.20 等中可能出现的任何树范围更改的维护负担。</p><p>所以大部分的 LoongArch 代码是为 Linux 5.19 合并的，但缺少一些启动所需的 EFI 代码，IRQ 驱动程序与 Linux 的 MIPS 代码共享，但那里的复杂性意味着尚未准备好使用，以及 PCI Loongson代码需要通过PCI子系统区域进行修改合并。</p><p>目前 Linux 5.19 合并 LoongArch 包含了 21k 行新代码，还不包括尚未登陆所需的驱动程序。大概到今年夏天晚些时候的 Linux 5.20 内核周期时，其余所需的驱动程序支持将通过审查，以产生可引导的 LoongArch 系统。</p>   
</div>
            