
---
title: 'Btrfs文件系统在Linux 5.16中得到了更多的性能优化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1102/966afd99d60ef74.jpg'
author: cnBeta
comments: false
date: Tue, 02 Nov 2021 12:45:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1102/966afd99d60ef74.jpg'
---

<div>   
Btrfs文件系统的开发团队继续稳步推进其性能优化和其他工作，部分原因是Fedora工作站继续默认使用该文件系统，以及openSUSE和其他Linux发行版对其重新感兴趣。<strong>在Linux
5.16合并窗口最繁忙的第一天，Btrfs的修改由SUSE的maitainer David Sterba提交。</strong><br>
 <p>本次升级最大的变化是性能改进和一些新的功能开始工作，以及通常的各种修复和代码维护。</p><p>新内核的Btrfs继续带来了各种性能优化。在Dbench工作负载的样本上，日志的改进产生3%的吞吐量改进和高达11%的延迟降低，还有更有效的目录记录，加快批量插入的速度，这共同可以带来更低的批量创建运行时间要求和删除时间。</p><p>Linux 5.16中的Btrfs还支持子页面的碎片整理，子页面的压缩写入，支持ZNS（分区命名空间）作为Btrfs分区模式支持的一部分，为发送协议更新做准备工作，错误处理改进，以及各种修复。ZNS是围绕<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a>的分区命名空间的NVMe规范。</p><p><a href="https://static.cnbetacdn.com/article/2021/1102/966afd99d60ef74.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1102/966afd99d60ef74.jpg" title alt="btrfshero.jpg" referrerpolicy="no-referrer"></a></p><p><strong>Linux 5.16的Btrfs变化的完整列表可以见此拉动请求：</strong></p><p><a href="https://lore.kernel.org/lkml/cover.1635773880.git.dsterba@suse.com/" _src="https://lore.kernel.org/lkml/cover.1635773880.git.dsterba@suse.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="e4878b928196cad5d2d7d1d3d3d7dcdcd4ca838d90ca80979081968685a497919781ca878b89">[email protected]</span>/</a><br></p>   
</div>
            