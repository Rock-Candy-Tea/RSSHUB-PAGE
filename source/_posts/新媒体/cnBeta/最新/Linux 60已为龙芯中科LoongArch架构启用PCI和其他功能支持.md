
---
title: 'Linux 6.0已为龙芯中科LoongArch架构启用PCI和其他功能支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0812/90de404e27ee269.webp'
author: cnBeta
comments: false
date: Fri, 12 Aug 2022 09:48:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0812/90de404e27ee269.webp'
---

<div>   
虽然在Linux
5.19中合并了对龙芯中科LoongArchCPU指令集架构的支持，但由于一些驱动代码尚未完成并准备好及时合并，这实际上还不足以产生一个启动系统。<strong>LoongArch之前被允许在v5.19中合并这些初步代码，以便Glibc支持可以落地，现在Linux
6.0中更多的CPU端口已经准备好进入内核。</strong><br>
 <p>最值得注意的是，Linux 6.0的LoongArch代码启用了PCI支持，现在PCI和IRQ芯片的变化已经准备就绪。因此，Linux 6.0对Loongson的这个CPU架构的PCI支持已经准备完毕，另外还有其他的变化，如堆栈解除器和堆栈跟踪支持。</p><p><img src="https://static.cnbetacdn.com/article/2022/0812/90de404e27ee269.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>LoongArch的变化还包括用vDSO优化getcpu()，bug修复，构建错误修复，以及更新其默认内核配置文件。</p><p>Linux 6.0内核的LoongArch补丁列表可以通过今天早上的拉动请求找到：</p><p><a href="https://lore.kernel.org/lkml/20220812072403.3075518-1-chenhuacai@loongson.cn/" _src="https://lore.kernel.org/lkml/20220812072403.3075518-1-chenhuacai@loongson.cn/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="8fbdbfbdbdbfb7bebdbfb8bdbbbfbca1bcbfb8bababeb7a2bea2ece7eae1e7faeeeceee6cfe3e0e0e1e8fce0e1a1ece1">[email protected]</span>/</a><br></p>   
</div>
            