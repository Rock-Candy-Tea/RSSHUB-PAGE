
---
title: '工程师发现20年前的芯片组解决方法一直在伤害现代AMD Linux系统性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0926/403490ff2a2641c.png'
author: cnBeta
comments: false
date: Mon, 26 Sep 2022 14:25:16 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0926/403490ff2a2641c.png'
---

<div>   
<strong>AMD工程师K Prateek Nayak最近发现，Linux内核中一个大约20年前的芯片组解决方法仍被应用于现代AMD系统，在某些情况下，它负责损害现代Zen硬件性能。</strong>幸运的是，一个修复程序正在进行中，它可以限制旧系统的工作方法，从而帮助提升现代系统的性能。<br>
 <p>上周发布了一个ACPI处理器空闲代码的补丁，以避免现代AMD Zen系统上的旧芯片组工作方法。自从ACPI支持在2002年被添加到Linux内核以来，一直有一个"假等待操作"来处理一些芯片组的STPCLK#没有被及时处理的问题。这个假的I/O读数会延迟进一步的指令处理，直到CPU完全停止。这是一些使用威盛芯片组的AMD Athlon时代系统的问题。但在过去20年里，新的芯片组没有这个问题。</p><p>在过去20年里，一个针对现在的古老芯片组的Linux内核解决方法仍然被不必要地应用于现代AMD系统，这反过来又会损害特定工作负载的性能。K Prateek Nayak发现，即使是现代的AMD系统，也仍然在应用这种变通方法。</p><p>在AMD Zen3系统上用IBS对某些工作负载进行采样显示，大量的时间花在假操作上，这被错误地算作C-State驻留。一个大的C-State驻留值可以促使处理器在随后的空闲实例中推荐一个更深的C-State，开始一个恶性循环，导致在繁忙和空闲阶段之间快速切换的工作负载性能下降。</p><p><a href="https://static.cnbetacdn.com/article/2022/0926/403490ff2a2641c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0926/403490ff2a2641c.png" referrerpolicy="no-referrer"><br></a></p><p>一个这样的工作负载是Tbench，在某些运行中可以观察到大规模的性能下降。至少对于Tbench来说，Linux内核中的这种长期的、无条件的工作方法一直在损害AMD Ryzen / Threadripper / EPYC在特定工作负载中的性能。这个变通方法并没有影响到现代<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>系统，因为那些较新的英特尔平台使用替代的基于MWAIT的intel_idle驱动代码路径。</p><p>AMD的补丁演变成了英特尔Linux工程师Dave Hansen的这个补丁。那个将"假等待"的工作方法限制在旧系统上的补丁已经排到了TIP的x86/紧急分支。由于它走的是"x86/紧急"的路线，而且修复了一个在现代硬件上不需要的工作方法，这个补丁很可能会在本周作为Linux 6.0内核提交，而不是需要等到下一个（v6.1）合并窗口再提交。</p>   
</div>
            