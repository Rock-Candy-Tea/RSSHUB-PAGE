
---
title: '英特尔Arc Alchemist独显无法让PCIe 4.0通道达到饱和'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0518/a4feccb89e4b8e6.jpg'
author: cnBeta
comments: false
date: Wed, 18 May 2022 02:23:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0518/a4feccb89e4b8e6.jpg'
---

<div>   
想要和 AMD、NVIDIA 正面竞争，英特尔的 Arc Alchemist 独显还有一段路要走。Twitter 网友 Löschzwerg 对 Intel Xe LP-based DG1 显卡进行一段时间的实测之后，发现了和 PCIe 4.0 吞吐量有关的错误。<strong>在 3DMark 的 PCI Express 功能测试中，Gunnir Index V2 DG1 无法让 PCIe 4.0 通道达到饱和。</strong><br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0518/a4feccb89e4b8e6.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Index V2 似乎在以前所有的 PCIe 接口上都能很好地工作。但是在 PCIe 4.0 上，该卡的性能与 PCIe 3.0 相同，尽管它应该得到大约两倍的分数。这说明 DG1 存在某种形式的瓶颈或错误。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0518/9732a19741b60ae.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0518/5bd83056feb56ba.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0518/6ca7882d49cc0d6.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0518/4a2eb8795a597d7.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">接下来是基于Xe HPG架构的Arc Alchemist，它是Xe LP的继任者，Arc A350M的首次评测也表明，英特尔的动态调整技术（DTT），一个类似于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的SmartShift技术的功能，正在损害Arc GPU的性能。当DTT被关闭时，帧率几乎翻倍，从下面的图片中可以看出。</p><p style="text-align: left;">英特尔应该很容易解决，因为它可能只需要对电源状态（P状态）进行一些优化。同时，修复PCIe错误可能有点困难，因为这个问题在AMD Radeon或NVIDIA GeForce GPU中一般不是那么常见。</p>   
</div>
            