
---
title: 'AMD正在酝酿一项"PAN"内核功能 可帮助提高Linux性能表现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0131/70360f9463b24dc.jpg'
author: cnBeta
comments: false
date: Mon, 31 Jan 2022 00:44:10 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0131/70360f9463b24dc.jpg'
---

<div>   
AMD公司的开源工程师发出了一个关于新的内核功能"PAN"（即进程适应性自动NUMA）的评论请求。AMD早期显示的数字表明，PAN可以帮助他们最新的服务器硬件上的一些工作负载的性能提高一个可衡量的数量。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0131/70360f9463b24dc.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>拟议的PAN是进程自适应自动NUMA（Process Adaptive autoNUMA），是一种计算自动NUMA扫描周期的自适应算法。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>公司的Bharata B Rao在Linux内核补丁系列的征求意见稿中进一步解释说："在这种新方法（进程自适应自动NUMA或PAN）中，我们在每个进程水平上收集NUMA故障统计数据，这可以更好地捕捉到应用行为。此外，该算法根据远程故障率来学习和调整扫描率。由于不拘泥于一个静态阈值，该算法可以更好地应对不同的工作负载行为。由于进程的线程已经被视为一个群体，我们在任务的[内存管理]过程中添加了一堆指标来跟踪各种类型的故障，并从中得出扫描率。新的每进程故障统计只对每进程扫描周期的计算有贡献，而现有的每线程统计继续对numa_group统计有贡献，这最终决定了跨节点迁移内存和线程的阈值。</p><p>对于终端用户/AMD EPYC客户来说，最重要的价值是PAN如何提升Linux性能。通过PAN的Linux内核构建，他们发现Graph500互连HPC基准与默认的Linux内核构建相比受益高达14.93%，NAS基准快了8%，PageRank只快了约0.37%，其他结果从不到1%到更重要的数字。这只是AMD到目前为止所评估的有限的测试选择--如果这个补丁系列过了RFC阶段的评估，成为其他内核维护者所支持的内容并最终被纳入内核的上游，那么接下来的基准测试值得关注。</p><p>到目前为止，还没有其他内核开发者对进程自适应autoNUMA建议发表评论，但那些感兴趣的人可以看到RFC系列，以了解更多关于这个功能或测试它。目前能够给出的形式仅仅是不到400行的新代码来改善Linux的NUMA行为。</p><p><strong>了解更多:</strong></p><p><a href="https://lore.kernel.org/lkml/20220128052851.17162-1-bharata@amd.com/" _src="https://lore.kernel.org/lkml/20220128052851.17162-1-bharata@amd.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="1c2e2c2e2e2c2d2e242c292e24292d322d2b2d2a2e312d317e747d6e7d687d5c7d7178327f7371">[email protected]</span>/</a><br></p>   
</div>
            