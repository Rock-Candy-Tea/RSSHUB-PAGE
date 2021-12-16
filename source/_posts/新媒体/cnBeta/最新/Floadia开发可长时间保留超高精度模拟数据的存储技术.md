
---
title: 'Floadia开发可长时间保留超高精度模拟数据的存储技术'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1216/69af74511e7c4fa.png'
author: cnBeta
comments: false
date: Thu, 16 Dec 2021 06:20:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1216/69af74511e7c4fa.png'
---

<div>   
<strong>通过独特的存储单元结构设计与控制方法，总部位于东京小平市的 Floadia 公司，刚刚开发出了一种“每单元 7 比特”的闪存芯片原型。</strong>对于熟悉固态硬盘存储器发展历史的朋友，一定不会对 SLC、MLC、TLC、QLC、甚至 PLC 的发展历程感到陌生。在现有的存储单元结构中，由于电荷泄露导致的特性变化和变异问题，无疑对数据的长期保存构成了巨大的挑战。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1216/69af74511e7c4fa.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://floadia.com/" target="_self">Floadia</a>，via <a href="https://www.anandtech.com/show/17116/startup-showcases-7-bits-per-cell-storage-with-10-year-retention" target="_self">AnandTech</a>）</p><p>据悉，基于传统方法的存储单元结构，数据保持时间仅为 100 秒左右。而 Floadia 新开发的 7-bit 闪存芯片原型，却能够在 150 ℃ 温度条件下，将模拟数据保持 10 年。</p><p>为达成通过极低功耗来实现 AI 推理操作的目标，Floadia 还将这项存储技术运用到了专门的内存计算（CiM）架构芯片上。</p><p>该架构将神经网络权重存储在了非易失性存储器中，然后让电流流经存储器阵列，并执行大量乘法累加计算。</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/c7d24f6b020391d.png" referrerpolicy="no-referrer"></p><p>作为边缘计算领域的 AI 加速器，CiM 技术引发了全世界的关注。因其能够从内存中读取大量数据，且比在 CPU / GPU 上执行乘法累加计算的传统 AI 加速器要消耗更少的能源。</p><p>这种存储技术基于 Floadia 新开发的 SONOS 型闪存芯片，能够轻松集成到微控制器和其它装置中。</p><p>为此，Floadia 还开展了多项创新，例如优化电荷俘获层（ONO 薄膜）的结构，以大幅延长存储 7-bit 数据保持时间。</p><p>双 Cell 组合最多可存储 8-bit 神经网络权重，尽管芯片面积很小，但还是能够实现远超现有 AI 加速器、高达 300 TOPS/W 的乘法累加计算性能。</p>   
</div>
            