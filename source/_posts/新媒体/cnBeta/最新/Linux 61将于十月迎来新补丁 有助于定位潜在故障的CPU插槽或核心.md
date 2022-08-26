
---
title: 'Linux 6.1将于十月迎来新补丁 有助于定位潜在故障的CPU插槽或核心'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0826/0ef0ea98d8d42de.png'
author: cnBeta
comments: false
date: Fri, 26 Aug 2022 08:09:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0826/0ef0ea98d8d42de.png'
---

<div>   
对于日常需要接触并维护大量硬件的服务器管理员来说，这里有个好消息 —— <strong>Linux 6.1 将能够在发生 Segmentation Fault 分段错误时，报告潜在有问题的 CPU 插槽 / 核心。</strong>当发现某个 CPU / 核心经常引发同样问题的时候，这项新特性就能够帮你更轻松的排查相关故障。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0826/0ef0ea98d8d42de.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（截图 via <a href="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/cpu&id=c926087eb38520b268515ae1a842db6db62554cc" target="_self">Kernel.org</a>）</p><p><a href="https://www.phoronix.com/news/Linux-6.1-Seg-Fault-Report-CPU" target="_self">Phoronix</a> 指出：当前正在 TIP 排队的 x86 / cpu 分支合并窗口，将于 10 月份带来一项改进。该补丁用于在分段错误发生时，记录下有故障嫌疑的 CPU / 核心。</p><p>若经常发现某一颗处理器、或特定内核遇到 Segmentation Fault，打印下的内容将有助于排场插槽或 CPU 核心问题。<strong>Rik van Riel 在公告中写道：</strong></p><blockquote><p>在规模足够大的计算机群中，坏掉个别 CPU 还是相当常见的。按照设想，我们可通过内核代码的运行来辨识，以找出在特定系统上不断重复崩溃的 CPU 内核。</p>不过多年来，出现问题的 CPU 故障模式，并不是千篇一律的。有时你可能只会揪出 bash、Python，或在在其它地方运行良好的各种系统守护程序中遇到分段错误。<p>有鉴于此，通过将 printk() 添加到 show_signal_msg()，我们便可在遇到 Segmentation Fault 时，打印出有潜在故障的处理器插槽或内核等信息。</p>尽管这项工作仍不够完美 —— 因为在故障发生和打印消息之间，任务可能还会在另一个 CPU 上被重新安排 —— 但这项工作已足够帮助人们定位到哪几个可能有内核损坏的 CPU 上。</blockquote><p>如果一切顺利，这个实用补丁将于今年晚些时候正式并入 Linux 6.1 。此外你可将它视作<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>现场扫描（Intel In-Field Scan）、MCEs、EDAC 报告等解决方案的一个有力补充。</p>   
</div>
            