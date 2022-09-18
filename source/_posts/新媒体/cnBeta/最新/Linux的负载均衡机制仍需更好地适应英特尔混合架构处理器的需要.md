
---
title: 'Linux的负载均衡机制仍需更好地适应英特尔混合架构处理器的需要'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0918/8281d1f4a83700e.webp'
author: cnBeta
comments: false
date: Sun, 18 Sep 2022 00:39:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0918/8281d1f4a83700e.webp'
---

<div>   
在推出英特尔Alder
Lake处理器的过去一年里，英特尔工程师已经对Linux内核进行了一些改进，以便更好地处理混合P核与E核的混合处理运算方法。虽然Alder
Lake在最近版本的内核中运行得很好，而且Linux上的P核与E核的任务选择比推出时要更完善，但仍有英特尔工程师本周提出了其中需要改进的地方。<br>
<p>上周有重要的Linux内核补丁系列发布，致力于混合CPU的"任务类"和正确实现Linux上的线程管理支持。本周，在Linux管道工会议上（Linux Plumbers Conference）还提出了如何将Linux的能源意识调度适应于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>混合CPU的议题，因为现在EAS只是为Arm big.LITTLE设计量身定做。</p><p>在本周的LPC2022会议上，英特尔工程师Zhang Rui和Chen Yu提到了英特尔混合Linux的工作仍然需要完善。这次额外的发言是提出Linux内核的负载平衡机制对于英特尔的混合处理器来说依然不尽如人意。</p><p><img src="https://static.cnbetacdn.com/article/2022/0918/8281d1f4a83700e.webp" title alt="1.webp" referrerpolicy="no-referrer"><img src="https://static.cnbetacdn.com/article/2022/0918/83d7f2bc2665c66.webp" title alt="2.webp" referrerpolicy="no-referrer"><img src="https://static.cnbetacdn.com/article/2022/0918/f3054d5e0799b1f.webp" title alt="3.webp" referrerpolicy="no-referrer"></p><p>特别是，用于计算频率刻度的频率最大值是一个全局值，而不是针对不同类型的核心，因为P核和E核在操作过程中有着不同的最大频率值。频率最大值也可以根据睿频模式、热/功率节流等而无法被正确判断，并且最大频率值也不能在运行时调整。</p><p>对这个话题感兴趣的人可以在下面的地址中找到完整的幻灯片，其中概述了目前英特尔混合CPU的Linux负载平衡问题以及可能的改进。</p><p><a href="https://lpc.events/event/16/contributions/1191/attachments/1074/2125/LPC-2022-1-freq.pdf" _src="https://lpc.events/event/16/contributions/1191/attachments/1074/2125/LPC-2022-1-freq.pdf" target="_blank">https://lpc.events/event/16/contributions/1191/attachments/1074/2125/LPC-2022-1-freq.pdf</a><br></p>   
</div>
            