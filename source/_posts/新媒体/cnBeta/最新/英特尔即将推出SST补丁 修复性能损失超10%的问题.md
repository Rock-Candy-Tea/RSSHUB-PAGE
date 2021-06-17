
---
title: '英特尔即将推出SST补丁 修复性能损失超10%的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0617/2b7bb1b9803f678.png'
author: cnBeta
comments: false
date: Thu, 17 Jun 2021 08:02:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0617/2b7bb1b9803f678.png'
---

<div>   
<strong>Speed Select Technology 是英特尔推出的一套电源管理解决方案，特点是能够根据用户工作负载而调节频率和管理内核优先级，以达成性能与效率的双赢。</strong>尴尬的是，正如英特尔自家工程师所观察到的那样，在启用了该模式的基准测试中，SST 竟然可能导致超过 10% 的性能下降。尽管未说明对实际工作负载的影响有多大，但此事还是引发了相当高的关注。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0617/2b7bb1b9803f678.png" alt="Intel SST - 0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">资料图（来自：Intel <a href="https://www.intel.com/content/www/us/en/architecture-and-technology/speed-select-technology-article.html" target="_self">官网</a>）</p><p>工程师解释称，问题源于 Linux PCI 接口导致的延迟，因其在映射期间搜索了连接到系统的数百个 PCI 设备。</p><p><img src="https://static.cnbetacdn.com/article/2021/0617/9f738d67c0526ec.png" alt="Inetl SST - 1.png" referrerpolicy="no-referrer"></p><p>虽然难以理解这里为何设计数百个 PCI 设备，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> SST 确实是一套相当复杂的解决方案，并且仅可在基于至强处理器的平台上使用（主流消费级酷睿产品线与之无缘）。</p><p><img src="https://static.cnbetacdn.com/article/2021/0617/be4789a4efef30e.png" alt="Intel SST - 2.png" referrerpolicy="no-referrer"></p><p>在找到问题根源之后，英特尔已承诺将很快通过固件更新的形式进行修复。打补丁的原理也相当简单，即利用缓存数据来提速搜索过程。</p><p><a href="https://static.cnbetacdn.com/article/2021/0617/6a7c2748f8237ce.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/6a7c2748f8237ce.png" alt="Intel SST - 3.png" referrerpolicy="no-referrer"></a></p><p>以下是 Linux 内核邮件公告（<a href="https://lore.kernel.org/lkml/20210616201856.1690143-1-srinivas.pandruvada@linux.intel.com/" target="_self">LKML</a>）中的消息摘要：</p><blockquote><p>我们观察到一些高性能基准测试在内核中耗费了更多的时间，具体取决于它们正在执行的 CPU 数据包，且可能导致超过 10% 的显著差异。</p><p>SST 本该提升这些基准测试的服务优先级，以带来更高的并行运行线程效能，但这种服务级别的变动又导致了需要访问 Intel Speed Select PCI 设备的 MMIO 区域。</p></blockquote><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=265389292&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">1 - Intel SST - 概述（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjY1Mzg5MjkyLnNodG1s.html" target="_self">via</a>）</p><p>这种从 CPU 到 PCI 设备实例的映射，使用了标准的 Linux PCI 接口 —— 即 <strong>pci_get_domain_bus_and_slot()</strong> 。</p><p>此函数执行抵达 PCI 设备的线性搜索，但由于测试平台上拥有 100 多个 PCI 设备，结果导致基准测试的快速路径代价异常高昂。</p><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=265389399&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">2 - Inter SST - 设置（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjY1Mzg5Mzk5LnNodG1s.html" target="_self">via</a>）</p><p>由于这里的 PCI 设备和功能都是相对固定的，因而 Intel SST 能够在实际执行时缓存 CPU 到 PCI 的设备信息，从而在再次访问时显著提升相关基准测试的性能。</p><p>据悉，英特尔在 2019 年的 Cascade Lake 至强处理器平台上隆重介绍了非常通用的 SST 技术，并且提供了包括设置核心优先级、基础始终速率等在内的多种选项。</p><p>不过正如上文所述，SST 功能需要在固件中实现、并由处理器的电源控制单元（PCU）来执行。至于更多细节，还请移步至英特尔官网（<a href="https://software.intel.com/content/www/us/en/develop/articles/third-generation-xeon-scalable-family-overview.html" target="_self">传送门</a>）查看。</p>   
</div>
            