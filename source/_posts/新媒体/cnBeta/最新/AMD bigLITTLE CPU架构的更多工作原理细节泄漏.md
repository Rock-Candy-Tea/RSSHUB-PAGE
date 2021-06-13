
---
title: 'AMD big.LITTLE CPU架构的更多工作原理细节泄漏'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0613/8b20161a0de84c5.jpg'
author: cnBeta
comments: false
date: Sun, 13 Jun 2021 07:45:44 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0613/8b20161a0de84c5.jpg'
---

<div>   
和英特尔的做法差不多，AMD也一直在研究自己的混合处理器架构，其中包括大核和小核。我们去年从一个泄露的专利中曾了解到这一点。<strong>今天我们有了关于这一发展的新信息，Twitter用户@Kepler_L2发现了AMD几天前发布的与big.LITTLE有关的一项新专利。</strong><br>
 <p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2021/0613/8b20161a0de84c5.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0613/8b20161a0de84c5.jpg" title alt="1623560063_amd_big_little_arch.jpg" referrerpolicy="no-referrer"></a></p><p>该专利概述了在这种混合方法中如何处理两类核心之间的任务处理。</p><p>根据这项专利，小核心将内置一个时间阈值，传感器将监测它以全时钟速度运行的时间长度。一旦越过阈值，该任务将被移交给大核心。如果它在最高频率状态下运行的时间高于阈值时间，将对内存密集型工作负载进行类似处理。</p><p>这是因为使用小内核的想法是为了节省电力，而长时间以全速运行会违背这一目的。</p><p>对于大内核来说，其实现方式恰恰相反。从本质上讲，如果在大核心上运行的工作负载没有越过阈值，该任务就会被发送到小核心上，因为显然这么多的处理能力对小工作负载来说似乎是不必要的。</p><p>回到去年的专利，其中描述了big.LITTLE设计方法的架构图，两个内核都有自己的专用L1缓存，但它们之间将共享L2池。：</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2021/0613/cb6304ee0e5132c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0613/cb6304ee0e5132c.jpg" title alt="1623561632_amd_big_little_core_plan.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">显示<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> bigLITTLE核心计划的图表</p>   
</div>
            