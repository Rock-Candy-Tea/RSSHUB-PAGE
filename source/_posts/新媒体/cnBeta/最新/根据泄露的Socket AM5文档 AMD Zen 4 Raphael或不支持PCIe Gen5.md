
---
title: '根据泄露的Socket AM5文档 AMD Zen 4 Raphael或不支持PCIe Gen5'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0820/047b2f6e23b43a3.jpg'
author: cnBeta
comments: false
date: Fri, 20 Aug 2021 09:01:15 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0820/047b2f6e23b43a3.jpg'
---

<div>   
<strong>在技嘉遭到勒索软件后披露的一些机密文档，在 PCI-Express Gen 5 支持上 AMD 可能要落后于 Intel。</strong>在 PCI-Express Gen 4 时代里，AMD 比 Intel 的“Rocket Lake”处理器早 1 年多进入市场。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0820/047b2f6e23b43a3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0820/047b2f6e23b43a3.jpg" alt="6u9jk2a0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">根据 Socket AM5 的平台框图指出，AM5 SoC 总共有 28 条 PCI-Express Gen 4 通道。其中 16 条分配给 PCI-Express 独立显卡，4 条分配给与 CPU 相连的 M.2 NVMe 插槽，另外 4 条通道分配给独立的 USB4 控制器，其余 4 条通道作为芯片组总线。</p><p style="text-align: left;">与即将推出的"Matisse"和"Vermeer"SoC相比，Socket AM5 SoC似乎有额外的4条通道，这些通道在高端平台上被 USB4 控制器使用，但可以不用于此目的，而是连接到低端主板的额外 M.2 NVMe插槽。</p><p style="text-align: left;">值得庆幸的是，内存是 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 将与 Intel 保持一致的一个领域，因为 Socket AM5 被设计为双通道 DDR5。其他 SoC 集成的 I/O 以及来自芯片组的 I/O 似乎与"Vermeer"相同，但有一些小的例外，如支持 20Gbps USB 3.2x2。</p><p style="text-align: left;">该插座为这一代的 APU 的显示 I/O 做了准备。Intel 即将推出的"Alder Lake-S"处理器实现了PCI-Express Gen 5，但只用于16通道的PEG端口。与CPU相连的NVMe插槽，以及下游的PCIe连接，仅限于PCIe Gen 4。</p>   
</div>
            