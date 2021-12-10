
---
title: 'Linux新内核补丁有望大幅改善多CPU内核服务器的启动时间'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1210/15191807cdf5c57.jpg'
author: cnBeta
comments: false
date: Fri, 10 Dec 2021 12:43:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1210/15191807cdf5c57.jpg'
---

<div>   
<strong>今年早些时候开始的一项 Linux 补丁工作，致力于改善 x86_64 处理器的系统启动体验。最新消息是，该补丁已于本周四送去审核，且有望很快合并。</strong>据悉，影响数百行代码的补丁集的重点，落在了 x86_64 CPU 内核的并行启动辅助上。在这之后，Linux 内核引导过程还有可能引入更大规模的并行优化。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1210/15191807cdf5c57.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1210/15191807cdf5c57.jpg" alt="Intel Xeon.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">资料图（来自：Intel 官网）</p><p>来自亚马逊的 David Woodhouse 通过实测发现，<a href="https://lore.kernel.org/lkml/20211209150938.3518-1-dwmw2@infradead.org/" target="_self">今日补丁</a>已经能够让<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>至强服务器的启动速度提升近 15 倍。</p><p>具体说来是，当前启动一个 96 线程的 Skylake 服务器，大约需要 500ms 时间。但在打上补丁后，其已大幅缩减至 34ms 左右。</p><p>此外还有一套 28 线程的 Haswell 系统，其从 EFI 启动到 Linux 的时间开销，也从 120ms 左右下降到了 49.5ms 。</p><p><a href="https://static.cnbetacdn.com/article/2021/1210/e2c807ae94c0424.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1210/e2c807ae94c0424.jpg" alt="AMD EPYC.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">高端 HEDT 台式机 / 工作站将颇为受益（图 via <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 官网）</p><p>如果考虑拥有更多核心数的最新款英特尔至强（Xeon）可扩展 Ice Lake、或者 AMD 霄龙（EPYC）服务器平台，这方面的差异会更加明显。</p><p>目前市面上已经有许多采用 64 核 EPYC 处理器的双路服务器，其核心数达到了 128 / 线程数更是高达 256 。而明年的 Genoa / Bergamo 产品线，还会将“核心大战”推向新的水平。</p><p>言归正传，刚被送去审核的 Linux 内核补丁，位于 Linux x86 / x86_64 代码中，因而不会对 Ampere Altra Max 之类的单槽 128 核心 CPU 造成直接的影响。</p>   
</div>
            