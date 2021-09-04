
---
title: '苹果M1 IOMMU驱动已合并到Linux 5.15 默认启用VT-d可扩展模式'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/09/f0297b48bb0d849.png'
author: cnBeta
comments: false
date: Sat, 04 Sep 2021 10:02:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/09/f0297b48bb0d849.png'
---

<div>   
虽然Linux 5.13对Apple Silicon M1提供了最初的支持，但这只是最初始的部分。现在，在Linux 5.15中，我们看到社区创建的苹果M1 IOMMU驱动程序被合并，这是该计划的又一重要步骤。<br>
 <p>作为Linux 5.15内核的IOMMU子系统更新的一部分，苹果M1芯片的DART IOMMU驱动已被送入。这个IOMMU驱动是由社区创建的，是"Asahi Linux"项目的一部分。</p><p>对于新架构的Mac兼容Linux而言，IOMMU是至关重要的，这有助于让他们正在开发中的示驱动与苹果Arm芯片上的其他功能一起运行，比如USB和PCIe，当然，PCIe对于M1上的WiFi和以太网的建立也是必要的。</p><p>苹果M1上的IOMMU对开发者来说是一个挑战，因为硬件被固定为使用16K的页面大小，而正在进行的工作是改进基础设施，以便在使用<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a> CPU页面大小的内核时能顺利运行。</p><p>"DART"IOMMU驱动之前已经并入主线。在IOMMU硬件支持的相同页面大小的情况下，该版本还对IOMMU映射/解映射的性能进行了优化。</p><p>而在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>方面，Linux 5.15还默认开启了VT-d可扩展模式。</p><p><a href="https://static.cnbetacdn.com/article/2021/09/f0297b48bb0d849.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/09/f0297b48bb0d849.png" referrerpolicy="no-referrer"></a></p>   
</div>
            