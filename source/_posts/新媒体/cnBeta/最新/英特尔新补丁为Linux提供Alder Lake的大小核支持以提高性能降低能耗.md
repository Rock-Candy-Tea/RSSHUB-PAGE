
---
title: '英特尔新补丁为Linux提供Alder Lake的大小核支持以提高性能降低能耗'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0103/79db490ed058ac3.jpg'
author: cnBeta
comments: false
date: Mon, 03 Jan 2022 03:34:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0103/79db490ed058ac3.jpg'
---

<div>   
英特尔为Linux系列操作系统推出了几个补丁，以帮助通过P和E内核（即性能和效率内核）提高Alder
Lake的性能并降低能耗。Linux操作系统将通过即将推出的补丁获得对英特尔Alder Lake Golden
Cove和Gracemont性能和效率内核的支持。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0103/79db490ed058ac3.jpg" title alt="Intel-linux-support-patch.jpg" referrerpolicy="no-referrer"></p><p>随着英特尔第12代酷睿Alder Lake系列CPU的发布，人们发现新CPU的性能在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a><a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11中比在Linux操作系统中更有效率。这是由于Linux对英特尔的线程主管技术没有足够的支持，该技术允许操作系统正确访问高性能的Golden Cove核心和节能的Gracemont核心，英特尔的线程主管是由增强型硬件反馈接口或HFI创建的。</p><p>网站Phoronix报道说，目前Linux中的固件使用一种算法来规划ITMT/Turbo Boost Max 3.0驱动所利用的性能或效率核心中的哪一个在当时被访问。反过来，由于Linux的性质选择更倾向于更高的性能，例如在Golden Cove的时钟速度中发现的，这减少了对节能的Gracemont核心的利用。</p><p>英特尔硬件反馈接口是一个由HFI创建的表格，帮助提供计算机处理器的性能和能源效率的信息。HFI表与操作系统和硬件一起工作，根据当时操作条件的任何变化或来自外部因素的任何行动不断进行更新。这个过程的一个例子是操作系统达到的热极限或热设计能力的变化。</p><p><a href="https://static.cnbetacdn.com/article/2022/0103/b2a5395111a4258.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0103/b2a5395111a4258.jpg" title alt="21ADL_Chip_Angle_2_Color_BKG_3000pixels-scaled.jpg" referrerpolicy="no-referrer"></a></p><p>简而言之，英特尔的HFI计算处理器的电源效率和性能能力，给它一个数字值的核心（0 - 255），并将该信息传达给操作系统。HFI的这种实时通信使硬件能够适应系统当前的能力，并与操作系统沟通，就在给定时间限制什么提出建议，例如尽量减少任何会影响能源效率、性能水平或系统温度的预定任务。</p><p>目前，最新的补丁系列正处于修订阶段，还没有消息表明这些补丁是否会成为即将到来的Linux 5.17更新的一部分，或者在今年某个时候进一步发布。</p><p>了解更多：</p><p><a href="https://lore.kernel.org/lkml/20211220151438.1196-1-ricardo.neri-calderon@linux.intel.com/" _src="https://lore.kernel.org/lkml/20211220151438.1196-1-ricardo.neri-calderon@linux.intel.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="95a7a5a7a4a4a7a7a5a4a0a4a1a6adbba4a4aca3b8a4b8e7fcf6f4e7f1fabbfbf0e7fcb8f6f4f9f1f0e7fafbd5f9fcfbe0edbbfcfbe1f0f9bbf6faf8">[email protected]</span>/</a><br></p>   
</div>
            