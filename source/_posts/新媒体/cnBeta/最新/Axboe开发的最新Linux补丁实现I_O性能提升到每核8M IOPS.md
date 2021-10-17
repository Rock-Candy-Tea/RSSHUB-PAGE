
---
title: 'Axboe开发的最新Linux补丁实现I_O性能提升到每核8M IOPS'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1017/cd93c2997a14d7b.png'
author: cnBeta
comments: false
date: Sun, 17 Oct 2021 06:54:10 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1017/cd93c2997a14d7b.png'
---

<div>   
<strong>就在上周，Linux内核优化带来6M IOPS的好成绩，更大的突破在持续，持续的优化下，新的补丁将Linux在理想的硬件配置下推到了每核7M
IOPS，到了本周结束时，已经达到了800万IOPS。</strong>Facebook的Jens
Axboe是Linux内核块子系统的负责人，他也因开发IO_uring而闻名，他一直在挑战Linux I/O性能的极限。<br>
 <p>就在上个月，在升级到带有<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>Optane Gen2存储的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Ryzen 9 5950X台式机后，他实现了3M以上的IOPS。</p><p><img src="https://static.cnbetacdn.com/article/2021/1017/cd93c2997a14d7b.png" title alt="%C1ZB9]@4NBF30@~LGW)ZD2.png" referrerpolicy="no-referrer"></p><p>自从他将自己得硬件升级以来，兴奋他一直在不懈地追求整个块子系统和IO_uring的新优化，据称现在已经达到了接近硬件的极限。</p><p>本周末的最新补丁跑分结果显示他确实成功突破了每核8M IOPS。这些Linux I/O改进会继续通过perf-wip分支排队列入内核。部分改进最终会在Linux 5.16周期中被发现，其合并窗口将在下个月开始启动。</p><p>让我们为Jens Axboe和他为提高Linux I/O性能而进行的令人难以置信的优化工作喝彩。</p><p><a href="https://static.cnbetacdn.com/article/2021/1017/7a9a63952590b0a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1017/7a9a63952590b0a.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            