
---
title: 'PCIe 7.0标准已在修订？全面普及可能还需要6年'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202207/62cbebdfb15ec044394d92bb_1024.jpg'
author: ZAKER
comments: false
date: Mon, 11 Jul 2022 04:44:32 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202207/62cbebdfb15ec044394d92bb_1024.jpg'
---

<div>   
<p>最近几年 PCIe 版本的更迭进入了快车道。去年 Intel 第 12 代酷睿平台上首发了 PCIe 5.0，今年 AMD 锐龙 7000 平台也加入了对其的支持，不过关于下一代 PCIe 标准的修订早已开始。</p><p>今年 1 月份，PCI-SIG 组织宣布 PCIe 6.0 规范标准 v1.0 版本正式发布，宣告完工。延续了惯例，带宽速度继续增倍，x16 下可达 128GB/s ( 单向 ) ，由于 PCIe 技术允许数据全双工双向流动，因此双向总吞吐量就是 256GB/s。PCIe 6.0 被认为是 PCIe 问世近 20 年以来变化最大的一次。坦率来说，PCIe 4.0/5.0 都是对 3.0 的小修小改，比如依然采用基于 NRZ（Non-Return-to-Zero）的 128b/130b 编码。PCIe 6.0 则改用 PAM4 脉冲调幅信令，1b/1b 编码，单个信号就有能四种编码（00/01/10/11）状态，比之前翻番，允许承载最高 30GHz 频率。不过，由于 PAM4 信号比 NRZ 脆弱，所以配套上马了 FEC 前向纠错机制，纠正链路中的信号错误，保障数据完整性。除了 PAM4 和 FEC，PCIe 6.0 的最后一项主要技术就是在逻辑层使用 FLIT（流量控制单元）编码。其实，PAM4、FLIT 都不算新技术，在 200G+ 的超高速以太网早已应用，其中 PAM4 没能大规模推广的原因在于物理层成本太高。另外，PCIe 6.0 依然保持了向下兼容。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202207/62cbebdfb15ec044394d92bb_1024.jpg" data-height="347" data-width="609" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202207/62cbebdfb15ec044394d92bb_1024.jpg" referrerpolicy="no-referrer"></div></div>至于更新的 PCIe 7.0，标准组织 PCI SIG 今天正式宣布开发 PCIe 7.0，并前瞻了核心参数。SSD 主控芯片大厂慧荣表示，PCIe 7.0 标准正本将会在 2025 年完工，全面普及可能要到 2028 年左右，而有意思的是，PCIe 6.0 规范也不过时 hi 今年初才刚刚对外公布。<p></p><p>和这几代的变化类似，PCIe 7.0 在 PCIe 6.0 的基础上再次实现带宽翻翻，达到 128GT/s，x16 通道双向可以达到 512GB/s。</p><p>即便是 SSD 常走的 x2/x4 通道，理论峰值速度也分别提高到 64GB/s 和 128GB/s，想象空间无限大。</p><p>细节方面，PCIe 7.0 和 6.0 一样，采用全新的 PAM4 调制，1b/1b 编码。值得一提的是，PCIe 7.0 依然保持了向下兼容。</p><p>PCI SIG 组织称，接下来的草案中会着重优化信道参数，并提高能效水平。</p><p>编辑：熊乐</p><p>· END<strong>·</strong></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            