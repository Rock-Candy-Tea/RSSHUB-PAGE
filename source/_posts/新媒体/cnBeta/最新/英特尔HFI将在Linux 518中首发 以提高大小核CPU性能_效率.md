
---
title: '英特尔HFI将在Linux 5.18中首发 以提高大小核CPU性能_效率'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0214/03c4068db1c98e9.jpg'
author: cnBeta
comments: false
date: Mon, 14 Feb 2022 01:25:16 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0214/03c4068db1c98e9.jpg'
---

<div>   
今年春天的Linux 5.18内核将增加对英特尔硬件反馈接口（HFI，有时也被称为增强型硬件反馈接口 -
EHFI）的支持。英特尔硬件反馈接口用于交流系统中各个CPU内核的性能和能效能力。反过来，Linux将使用英特尔HFI数据来做出改进的任务安排决定，即在可用的CPU内核/线程中把给定的工作放在哪里。<br>
<p>英特尔HFI对新的英特尔Alder Lake处理器和即将推出的混合处理器设计非常重要，这些处理器被称为"Thread Director"，内核拥有将重要的任务放在具有最大性能潜力的CPU内核上的机制，将背景任务和其他不太重要的工作放在更节能的内核上。</p><p>英特尔的硬件反馈接口并不是静态的（至少从设计上看，一些平台/固件可能只在启动时决定对其进行编程，但HFI的设计是，它可以每"几十毫秒动态变化一次"），但对内核/操作系统的反馈最终可以根据当前的热条件和其他因素而改变。</p><p><img src="https://static.cnbetacdn.com/article/2022/0214/03c4068db1c98e9.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>英特尔的硬件反馈接口已经被<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a><a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11支持，而现在又来到了Linux。早在2020年底，英特尔首次开始记录增强型硬件反馈接口的开发工作，这表明它对未来的英特尔处理器是非常重要的。本周末的消息是，英特尔HFI的Linux内核代码已经被合并到linux-pm的linux-next分支。随着Linux电源管理子系统维护者Rafael Wysocki（英特尔员工）将intel_hfi驱动纳入"-next"代码，这基本上表明它已经准备好在下一个内核周期（即Linux 5.18）出现。</p><p>Linux 5.18的合并窗口将在3月底左右在v5.17发布后正式出现，但Linux 5.18稳定版要到5月底左右才会发布。不幸的是，这使得英特尔HFI驱动程序在所有的春季Linux发行版中不适用（除了那些滚动发行的发行版或像Fedora那样把主要的新内核作为稳定版更新来发行的发行版），但至少到了秋季，所有的Linux发行版应该会全部换装新内核。</p><p>因此，在未来几个月里，英特尔HFI代码将出现在Linux上，以改善内核在其最新处理器中的调度器任务安排，从而提高性能/效率。</p>   
</div>
            