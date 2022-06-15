
---
title: 'Linux迎来AMD Zen 4与Mendocino APU的新CPU温度驱动补丁'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0615/071eb7503050092.jpg'
author: cnBeta
comments: false
date: Wed, 15 Jun 2022 06:42:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0615/071eb7503050092.jpg'
---

<div>   
在几项针对开源显卡技术的更新之后，<strong>AMD 似乎又在酝酿为 Zen 4 和传说中的 Mendocino APU，制作一个与 CPU 温度驱动（k10temp）有关的新补丁。</strong>通常情况下，开源社区成员会提前获知这方面的改动，以便在 Linux 主线内核发布前做好相应的支持准备。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0615/071eb7503050092.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>此前，我们已经在 AMD Rembrandt APU 正式发布前看到 k10temp 支持。但现在，该公司正寻求为 Zen 4 提供类似的支持。</p><p>尽管对于普通人来说，似乎无需对其保持较高的关注。但对于精通 Linux 技术的人们来说，该技术将方便我们从系统控件上查看各项硬件监测参数（包括 CPU、GPU 和其它组件）。</p><p>若在产品发布后遇到需要修复特定产品在散热等方面的问题，这么做也算是有备无患。</p><p><a href="https://static.cnbetacdn.com/article/2022/0615/99f91eb1ca55938.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0615/99f91eb1ca55938.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">Computex 2022 资料图</p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=AMD-k10temp-Zen-4-v5" target="_self">Phoronix</a> 网站的 Michael Larabel 指出 —— AMD 有在去年的补丁中，提到过下一代架构的新产品 ID 。可即便如此，该公司还是捂着一些产品细节没公开。</p><blockquote><p>AMD Linux 工程师 Mario Limonciello 写道：该系列补丁看起来像是对之前提交的一些更正，但之前的提交是针对相同芯片型号的不同家族。</p><p>同时我们注意到，一些即将推出的芯片，已带有新的 PCIe ID、以及尚不支持的 CCD offsets —— 所以它们将被添加到 amd_nb / k10temp 中。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0615/6f742fd2d000b96.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>以下是第五版 K10temp 启用补丁中支持的产品家族：</p><blockquote><p>● Family 17h A0h-AFh</p><p>● Family 19h 70h-7Fh</p><p>● Family 19h 60h-6Fh</p></blockquote><p>其中 Family 17h 特指 AMD Zen / Zen 2 架构，而 Family 19h 则被分配给了 Zen 3 。</p><p>然后 Larabel 援引从之前的 Linux 内核补丁中提取的信息指出，Family 19h 也将被用于指代 Zen 4 CPU 架构。</p><p><img src="https://static.cnbetacdn.com/article/2022/0615/c76fdda937f2736.png" alt="4.png" referrerpolicy="no-referrer"></p><p><a href="https://wccftech.com/amd-zen-4-and-mendocino-cpus-receive-cpu-temperature-driver-patch-in-linux/" target="_self">WCCFTech</a> 推测，60h / 70h 组件或分别分配给 Zen 4 / Zen 4c 处理器。</p><p>此外随着 AMD 正在为入门级笔记本开发 Mendocino SoC，未来我们或在 Family 17h 系列中看到一些新的 ID 。</p><p>感兴趣的朋友，可到 <a href="https://lore.kernel.org/lkml/20220613192956.4911-1-mario.limonciello@amd.com/" target="_self">Kernel.org</a> 官网上查看有关 k10temp CPU 温度驱动程序的第五版新补丁。</p><p>不过除了即将推出的 Linux 5.20 内核，预计我们不会很快在 AMD 新 CPU 架构发布时看到相关改动的上线。</p>   
</div>
            