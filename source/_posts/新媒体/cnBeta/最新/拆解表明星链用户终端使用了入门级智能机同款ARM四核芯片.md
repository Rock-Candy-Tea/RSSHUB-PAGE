
---
title: '拆解表明星链用户终端使用了入门级智能机同款ARM四核芯片'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0726/f9ac34a319364cf.jpg'
author: cnBeta
comments: false
date: Mon, 26 Jul 2021 02:54:25 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0726/f9ac34a319364cf.jpg'
---

<div>   
本月早些时候，比利时 KU Leven 大学研究人员对 SpaceX 的星链终端进行了新的拆解。结果发现，<strong>SpaceX 不仅对接收器天线部分进行了升级，还使用了入门级智能手机上常见的 ARM Cortex-A53 四核处理器。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2021/0726/f9ac34a319364cf.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0726/f9ac34a319364cf.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：darkpenguin22 / Reddit）</p><p>其实 2020 下半年，Kenneth Keiter 已经对星链客户终端进行过一次拆解。不过那时他主要关注硬件层面，而不是接收器的关键性能规格。</p><p>现在，为了解星链接收器是如何启动和加载软件的，KU Leven 研究人员已进行了新的拆解，从而揭示了天线盘的应用处理器和板载内存的重要细节。</p><p><img src="https://static.cnbetacdn.com/article/2021/0726/b9ec77ea48d1575.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.esat.kuleuven.be/cosic/blog/dumping-and-extracting-the-spacex-starlink-user-terminal-firmware/" target="_self">KU Leven</a>）</p><p>如图所示，星链终端被发现配备了 4GB eMMC 闪存，用于加载系统所需的启动固件，并通过独立的处理器来访问 eMMC 中的内容。</p><p>有趣的是，研究人员还在主板上发现了“安全芯片”。作为近年来移动设备上愈加重要的组件，它还包含了安全生物识别验证所需的代码。</p><p><img src="https://static.cnbetacdn.com/article/2021/0726/aa9a8b3c25ec150.png" alt="4.png" referrerpolicy="no-referrer"></p><p>处理器方面，星链终端使用了四核心的 Cortex-A53 方案。作为 ARM 在 2012 年设计的低功耗计算核心，它既可以单独使用、亦可搭配高性能的 Cortex-A57 协同工作。</p><p>有趣的是，如果在启动阶段输入“Falcon”（猎鹰）一词，星链终端还会中止启动过程，此外研究人员还揭示了新硬件的一些变动。</p><p><a href="https://static.cnbetacdn.com/article/2021/0726/dd8af0b18488b80.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0726/dd8af0b18488b80.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>通过一番艰难的查找，研究人员得知某些部件或有不同的硬件修订。比如在移除白色的塑料盖之前，得先从 PCB 板上卸下以太网 / 电机控制排线。</p><p>最后，SpaceX 已在设计第二代星链用户终端。为了促进早期采用，Starlink 给予了相当丰厚的用户补贴，直到该公司的卫星互联网服务能够达到足够高的市场渗透率。</p><p>公司 CEO 伊隆·马斯克曾表示，其希望将成本从当前的 499 美元（约 3235 RMB）、进一步拉低至 250 美元（约 19621 RMB）。</p>   
</div>
            