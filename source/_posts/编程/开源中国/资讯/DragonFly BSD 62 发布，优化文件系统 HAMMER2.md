
---
title: 'DragonFly BSD 6.2 发布，优化文件系统 HAMMER2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0112/071840_7B7N_4252687.png'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 07:18:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0112/071840_7B7N_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p>DragonFly BSD 6.2 已发布，6.2 是 6.x 系列的重要版本，此版本具有对包含 NVMM 的虚拟机监视器 (type-2) 的硬件支持、amdgpu 驱动程序、远程挂载 HAMMER2 卷的试验性功能以及许多其他更改。</p> 
<p>DragonFlyBSD 6.2 通过从 Linux 内核移植的“AMDGPU”DRM 内核驱动程序获得了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DAMDGPU-Ported-DragonFlyBSD" target="_blank">现代 AMD Radeon 图形支持</a>。虽然 DragonFlyBSD 6.2 具有 AMDGPU Linux 驱动程序的移植，但与上游 5.16 相比，它基于 Linux 4.19 内核，这意味着 RDNA2、Aldebaran 和其他最新一代的版本没有登陆，也没有任何最近的优化和功能。因此在 GPU 驱动程序支持方面，DragonFlyBSD 以及整个 BSD 继续远远落后于 Linux。</p> 
<p>此外在 DragonFlyBSD 6.2 中，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DDragonFlyBSD-WhiskeyLake" target="_blank">对 Intel Whiskey Lake Gen9 显卡的支持</a>也正在进行。</p> 
<p>另一个值得一提的变化是，DragonFlyBSD 6.2 的移植工作添加了 NVMM，它是 NetBSD 的管理程序，支持现代 Intel 和 AMD 处理器。DragonFlyBSD 6.2 包含 NVMM 管理程序在 BSD 上的完整移植。</p> 
<p><img height="379" src="https://static.oschina.net/uploads/space/2022/0112/071840_7B7N_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p>此版本继续改进了 DragonFly 的原始 HAMMER2 文件系统。DragonFlyBSD 6.2 的 HAMMER2 现在支持 growfs，可以改变现有卷的大小，xdisk 也包含在构建中，这样就可以远程挂载 HAMMER2 磁盘。不过远程 HAMMER2 安装目前处于试验性阶段。新版本还修复了 HAMMER2 的多项问题。</p> 
<p>最后，DragonFlyBSD 6.2 还修复了安全问题，增加了 Family 19h AMD Zen 3 温度监控支持，改进了内核的分页算法，支持 makefs FAT，更新多个软件包更新，以及改进 DSynth。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dragonflybsd.org%2Frelease62%2F" target="_blank">详情点此查看</a>。</p> 
<p style="margin-left:0">DragonFly 是一份作为 FreeBSD-4.x 系列在逻辑上的延续而设计的操作系统及应用环境。这些操作系统与 Linux 可归为相同的类别，因为它们都基于 UNIX 理念及应用程序接口。DragonFly 是这条发展道路上的一个分支，可以说，是给了 BSD 一个向着不同于 FreeBSD-5 系列的崭新方向而发展的机会。</p> 
<p style="margin-left:0"><img height="284" src="https://static.oschina.net/uploads/space/2022/0112/071805_Fi79_4252687.png" width="500" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            