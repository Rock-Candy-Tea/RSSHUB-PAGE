
---
title: 'LPC 2022：谷歌工程师介绍Ghost Linux内核调度API的最新进展'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0913/20236e620554ddc.jpg'
author: cnBeta
comments: false
date: Tue, 13 Sep 2022 06:31:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0913/20236e620554ddc.jpg'
---

<div>   
<strong>在都柏林举办的 Linux Plumbers Conference 活动期间，Google 介绍了其长期研究的“Ghost”项目的最新进展。</strong>可知作为从用户空间或 eBPF 程序控制 Linux 内核调度程序的一种方法，Ghost 提供了相当广泛的 API 。对于开发者来说，他们还可根据系统偏好，而对调度行为进行微调。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0913/20236e620554ddc.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>在周一的 LPC 2022 Dublin 线下活动期间，Google 工程师 Barret Rhoden 介绍了 Ghost 内核调度事件的最新进展。</p><p>首先，用户空间（User-Space）或 eBPF 程序的多个“代理”（agents），可在同一系统上运行以影响内核调度行为。</p><p>其次，开发团队计划在未来版本中实现 Linux 的现有 CFS 算法（包括 eBPF 和其它新功能）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0913/e6e1933fce8bda5.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p>感兴趣的朋友，可回顾 Barret Rhoden 分享的这份演示文稿（<a href="https://lpc.events/event/16/contributions/1365/attachments/986/1912/lpc22-ebpf-kernel-scheduling-with-ghost.pdf" target="_self">PDF</a>），以了解与 Ghost 开发相关的更多细节。</p><p>目前该项目正通过 GitHub 上的 <a href="https://github.com/google/ghost-kernel/" target="_self">ghost-kernel</a> 和 <a href="https://github.com/google/ghost-userspace/" target="_self">ghost-userspace</a> 这两个存储库进行托管，且今日还有 <a href="https://www.phoronix.com/news/HID-eBPF-New-Attempt" target="_self">HID-BPF</a> 方面的更新。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1315409.htm" target="_blank">User-Space Hinting将助力AMD霄龙处理器实现更好的任务性能发挥</a></p></div>   
</div>
            