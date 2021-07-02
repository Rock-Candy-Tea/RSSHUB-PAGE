
---
title: '英特尔开始为Linux提供DG2与Xe_HP SDV支持补丁'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0629/5522cf1b3085b72.jpg'
author: cnBeta
comments: false
date: Fri, 02 Jul 2021 06:30:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0629/5522cf1b3085b72.jpg'
---

<div>   
早前有报道称，英特尔已开始向开发者送去 Xe-HPG DG2 显卡，且网络上涌现了许多与新一代显卡有关的爆料。<strong>最新消息是，英特尔的开源 Linux 驱动工程师们，已开始提供可用于启用 DG2 和 Xe_HP SDV 的补丁。</strong>而在 DG2 到达更多用户手上之前，英特尔已迅速提供了可为 Linux 桌面提供 DG1 独显加速的工作补丁。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0629/5522cf1b3085b72.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0629/5522cf1b3085b72.jpg" referrerpolicy="no-referrer"></a></p><p>早些时候，英特尔开源 Linux 驱动程序工程师们带来了一组 <a href="https://patchwork.kernel.org/project/intel-gfx/patch/20210701202427.1547543-2-matthew.d.roper@intel.com/" target="_self">53 个补丁</a>，以启用对 DG2 和 Xe_HP SDV 平台的支持。</p><p>DG2 独显采用了 Xe_HPG 12.55 图形 IP，并结合了 Xe_LPD v13 显示 IP。后者是 Alder Lake-P 处理器上将采用的显示模块，而 Xe_HP SDV 是其下一代加速卡的软件开发工具。</p><p>英特尔在补丁中指出，Xe_HP 12.50 图形 IP 硬件中搭配了许多额外的媒体引擎，包括四个解码引擎 + 两个视频增强引擎。</p><p>不过今天放出的这 53 个补丁，只能算是初始占位，距离“切实可用”的阶段，还有较长的一段路要走。因为这些补丁尚未提供针对多 Tile 和专用计算引擎等功能模块的支持。</p><p>按照现在的速度推进，预计英特尔 DG2 与 Xe-HP SDV 的相关支持，或于今年晚些时候被 Linux 5.15 内核给正式收录。</p>   
</div>
            