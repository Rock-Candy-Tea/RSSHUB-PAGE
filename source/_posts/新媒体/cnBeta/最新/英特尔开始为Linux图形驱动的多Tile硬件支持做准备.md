
---
title: '英特尔开始为Linux图形驱动的多Tile硬件支持做准备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1010/eec964d7af8750a.jpg'
author: cnBeta
comments: false
date: Sun, 10 Oct 2021 03:23:55 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1010/eec964d7af8750a.jpg'
---

<div>   
最近几个月，英特尔一直在努力推动 Xe-HP 的 Linux 图形驱动程序堆栈的基础工作，并且涵盖了独显 / 加速卡产品线。<strong>最新消息是，这家芯片巨头已于本周五发布了首个重要的补丁系列，且主要围绕着 Multi-Tile 的初始支持工作。</strong>据悉，英特尔为 Xe-HP / Ponte Vecchio 引入了多 Tile / 小芯片的设计理念。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/1010/eec964d7af8750a.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图 via <a href="https://www.phoronix.com/scan.php?page=news_item&px=Intel-Preps-Linux-Multi-Tile" target="_self">Phoronix</a>）</p><p>此前，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Linux 图形驱动程序仅围绕单 Tile 设计而构建。但周五下午的新补丁，已在 i915 内核 DRM 驱动程序的基础架构中引入了更改，已支持多 Tile 版本。</p><p>以下是补丁描述：</p><blockquote><p>我们即将推出的一些平台（包括 Xe-HP SDV）支持多 Tile 设计，它实际上是一个具有多个 GT 实例和本地内存区域的平台，它们都位于单个 PCI 设备之后。</p><p>这意味着每个 drm_i915_private 拥有多个 intel_gt 结构，而新补丁提供了初始重构，以支持每张卡的多个独立 GT 。</p><p>不过后续仍需进一步的工作（尤其与本地内存相关），才能完全推动多 Tile 平台的启用。</p></blockquote><p>需要指出的是，对于用户空间来说，多个 GT 的存在，在很大程度上都是透明的。多 Tile 平台会向用户空间宣称更大的引擎列表，但用户空间无需直接处理 Tile 的概念。</p><p>由于设备具有多个本地内存区域，它会对 uapi 产生一些影响，但多 Tile 的实际工作并未在本系列补丁中得到体验，而是要靠后续的工作来继续完善。</p><p>初构的一揽子多 Tile 代码现可供所有人审查，只是考虑到需要围绕本地内存处理做更多工作，开发团队不大可能在接下来的 Linux 5.16 内核周期中及时搞定。</p>   
</div>
            