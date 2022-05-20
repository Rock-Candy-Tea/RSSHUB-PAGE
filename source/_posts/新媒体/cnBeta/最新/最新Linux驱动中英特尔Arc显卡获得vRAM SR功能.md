
---
title: '最新Linux驱动中英特尔Arc显卡获得vRAM SR功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0520/e8f6acd0f90235e.webp'
author: cnBeta
comments: false
date: Fri, 20 May 2022 06:44:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0520/e8f6acd0f90235e.webp'
---

<div>   
在 Linux Kernel 5.19 中，继续整合了大量关于 AMD、NVIDIA 和 Intel 的更新。针对 Arc Alchemist 和
DG2 开源驱动的支持已进入尾声，英特尔现在朝着更标准的独立显卡启动要求迈进。<strong>近期，为 ARC 显卡设备整合的非核心功能之一是 vRAM
Self-Refresh，简称 vRAM SR。</strong><br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0520/e8f6acd0f90235e.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">新引入的 vRAM SR 支持有助于在整个系统中的 D3cold 和 S0ix 挂起模式。添加此新功能允许用户在节能状态下绕过将本地内存对象强制排放到系统。vRAM SR 提供保留专用视频内存上下文以在退出 D3cold 电源状态时刷新。</p><p style="text-align: left;">当从节能条件中恢复时，用户可以期望更低的延迟水平，只需对功耗进行最小的调整。系统可以通过允许其保持最低限度的活动来继续利用其专用视频内存状态。</p><p style="text-align: left;">英特尔的 Arc 显卡 vRAM SR 功能出现在该公司最近完成了该公司显卡上 Linux 支持的 DG2 电源管理工作之后。该更新包括添加最新的 ID 和对英特尔计算任务的支持，允许最新内核为 Arc Alchemist 系列图形提供增强的电源管理处理。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0520/77a2ccecd45fe6b.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">英特尔的 ARC Graphics 和该公司的客户端显卡不支持 D3Cold-VRSR 模式，该模式提供最高的省电水平——完全为零瓦——退出时延迟增加。</p><p style="text-align: left;">新包含的 vRAM SR 功能及其对用户系统的好处还取决于主机系统 BIOS 的支持。英特尔选择不仅支持 Arc Alchemist DG2 显卡，还允许向后兼容 DG1 显卡。但是，Linux 内核还没有提供同样的帮助，这可能会导致在对开源操作系统的 DG2 支持完全完成后支持它。</p>   
</div>
            