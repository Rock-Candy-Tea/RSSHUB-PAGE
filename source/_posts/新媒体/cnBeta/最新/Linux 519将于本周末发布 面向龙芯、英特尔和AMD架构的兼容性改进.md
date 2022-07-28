
---
title: 'Linux 5.19将于本周末发布 面向龙芯、英特尔和AMD架构的兼容性改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png'
author: cnBeta
comments: false
date: Thu, 28 Jul 2022 13:37:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png'
---

<div>   
Linux 5.19将于本周末发布，与大多数内核周期一样，Linux 5.19是另一个大周期。从英特尔和AMD继续为即将到来的硬件支持做准备，大量的网络改进，持续在IO_uring上的努力，各种优化以及其他新功能，Linux 5.19的所有改进都令人激动。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" referrerpolicy="no-referrer"></a></p><p><strong>在6月初的Linux 5.19合并窗口之后，这里是v5.19到来以后的首要亮点：</strong></p><p>- LoongArch作为最新的CPU架构登陆内核。然而，在Linux 5.19中，由于一些驱动代码还没有被主线化，它还不能在实机上使用。但LoongArch为Linux 5.19提供支持为LoongArch下一步进入Glibc打开了大门，另一方面，由于瑞萨H8/300的支持被放弃，Linux 5.19的架构数量保持不变。</p><p>- 继续为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Zen 4处理器做准备，包括新的IBS扩展、PerfMonV2和其他改进。</p><p>- 在AMD兼容性方面，令人振奋的是AMD SEV-SNP在主机方面的支持终于被主流化了。在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>方面，最初的英特尔TDX主机对信任域扩展的支持也得以实现。</p><p>- 引入许多英特尔电源管理的改进，如Alder Lake在英特尔空闲驱动程序中的支持，Sapphire Rapids对英特尔P-State的带外模式支持，以及其他变化。</p><p>- 继续启用下一代AMD Radeon显卡的工作，包括兼容所有RDNA3消费者显卡和AMD Instinct MI300 / GFX940加速器。这项启用工作会一直持续到Linux 5.20周期，所以从外界看来，至少要到5.20，RDNA3才可能对Linux游戏玩家等显示出良好的状态。</p><p>- 英特尔Raptor Lake P图形获得支持。</p><p>- 继续DG2/Alchemist的启用工作，包括现在将计算支持暴露给用户空间，并为主板集成的（笔记本）独立图形添加PCI ID。随着Linux 5.20的到来，英特尔Arc Graphics桌面显卡将处于可用的状态。</p><p>- 由于Asahi Linux项目的努力，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>M1 NVMe控制器支持已经被合并，苹果eFuse驱动程序也被合并了。</p><p>- Zstd压缩固件支持。</p><p>- 一些性能优化，如在AMD Ryzen HP Dev One上展示的那些。</p>   
</div>
            