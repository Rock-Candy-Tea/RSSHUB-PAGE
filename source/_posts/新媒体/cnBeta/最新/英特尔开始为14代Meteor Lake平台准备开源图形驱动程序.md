
---
title: '英特尔开始为14代Meteor Lake平台准备开源图形驱动程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1108/300de1c57a17ad4.jpg'
author: cnBeta
comments: false
date: Thu, 07 Jul 2022 02:54:00 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1108/300de1c57a17ad4.jpg'
---

<div>   
<strong>英特尔开源 Linux 驱动程序的开发团队，正忙于完善其 DG2 / Alchemist 启用补丁。</strong>相关工作从 Linux 5.20 的“Ponte Vecchio”主线支持开始，到 13 代 Raptor Lake CPU 的核显（基于 12 代 Alder Lake 的小幅升级），并已着手 14 代 Meteor Lake 相关内容的开发。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1108/300de1c57a17ad4.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1108/300de1c57a17ad4.jpg" referrerpolicy="no-referrer"></a></p><p>作为 Raptor Lake 的继任者，Meteor Lake 预计不会在 2023 下半年前到来，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>依然保持着一个优良传统 —— 为其处理器与核显带来早期 Linux 支持。</p><p>通常情况下，这家芯片巨头会提前一年或更长时间，来规划相关硬件支持工作，以期在正式发布前通过各项上游代码审核、并确保与 Linux 内核和 Mesa 等组件的稳定兼容。</p><p>早前 <a href="https://www.phoronix.com/scan.php?page=news_item&px=Intel-Meteor-Lake-IGC" target="_self">Phoronix</a> 已经聊过一些围绕网络等领域的支持，且英特尔工程师们提交了一些围绕 Meteor Lake 的 Coreboot 工作补丁。</p><p>现在，蓝厂似乎也处于为 Meteor Lake 启用核显图形支持的早期阶段。该公司的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> / Linux 开源图形编译器（IGC），已经为 Meteor Lake 提供了 virtual ISA target 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0707/41b31ba482cbf47.jpg" referrerpolicy="no-referrer"></p><p>截止周二晚间，Meteor Lake 的“MTL”相关代码已经被合并到了 IDV 编译器代码中（via <a href="https://github.com/intel/intel-graphics-compiler/commit/20ef9c5a42f4154c9e18c65cafd55e8af5f67c17" target="_self">GitHub</a>）。</p><p>当前其在很大程度上遵循了与 DG2 / Alchemist 相同的路径，且在某些情况下与 Alder Lake 一致。</p><p>需要指出的是，14 代平台用上了与 Alchemist 独显相同的“Xe HPG”图形架构，而不像 11 代 Tiger Lake / 12 代 Alder Lake / 13 代 Raptor Lake 那样用的是“Xe”图形架构。</p><p>即便如此，这些仍只是 Meteor Lake 支持的冰山一角，后续肯定还会有很多与 Mesa 和 Linux 内核 i915 DRM 相关的补丁等待陆续发布。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1289517.htm" target="_blank">代码揭示Meteor Lake CPU将迎来Alchemist tGPU图形架构</a></p></div>   
</div>
            