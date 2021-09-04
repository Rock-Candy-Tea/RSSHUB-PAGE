
---
title: '苹果M1 IOMMU驱动已合并到Linux 5.15 默认启用VT-d可扩展模式'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/613349e98e9f0978692f1e85_1024.jpg'
author: ZAKER
comments: false
date: Sat, 04 Sep 2021 02:41:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/613349e98e9f0978692f1e85_1024.jpg'
---

<div>   
<p>虽然 Linux 5.13 对 Apple Silicon M1 提供了最初的支持，但这只是最初始的部分。现在，在 Linux 5.15 中，我们看到社区创建的苹果 M1 IOMMU 驱动程序被合并，这是该计划的又一重要步骤。</p><p>作为 Linux 5.15 内核的 IOMMU 子系统更新的一部分，苹果 M1 芯片的 DART IOMMU 驱动已被送入。这个 IOMMU 驱动是由社区创建的，是 "Asahi Linux" 项目的一部分。</p><p>对于新架构的 Mac 兼容 Linux 而言，IOMMU 是至关重要的，这有助于让他们正在开发中的示驱动与苹果 Arm 芯片上的其他功能一起运行，比如 USB 和 PCIe，当然，PCIe 对于 M1 上的 WiFi 和以太网的建立也是必要的。</p><p>苹果 M1 上的 IOMMU 对开发者来说是一个挑战，因为硬件被固定为使用 16K 的页面大小，而正在进行的工作是改进基础设施，以便在使用 4K CPU 页面大小的内核时能顺利运行。</p><p>"DART"IOMMU 驱动之前已经并入主线。在 IOMMU 硬件支持的相同页面大小的情况下，该版本还对 IOMMU 映射 / 解映射的性能进行了优化。</p><p>而在英特尔方面，Linux 5.15 还默认开启了 VT-d 可扩展模式。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202109/613349e98e9f0978692f1e85_1024.jpg" data-height="689" data-width="1200" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/613349e98e9f0978692f1e85_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            