
---
title: '微软推出全新开源工具 可在Android_Linux上用于测试浏览器性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1208/0412543ca3c4460.jpg'
author: cnBeta
comments: false
date: Wed, 08 Dec 2021 08:48:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1208/0412543ca3c4460.jpg'
---

<div>   
对于在不同网络浏览选项之间做决定的消费者来说，性能通常是一个非常重要的指标。微软和 Google 都在不断寻找方法，以提高 Edge 和 Chrome 浏览器的性能。现在，<a href="https://devblogs.microsoft.com/performance-diagnostics/new-tools-for-analyzing-android-linux-and-chromium-browser-performance/" target="_blank">微软推出了名为 Microsoft-Performance-Tools for Linux-Android 的开源工具</a>，以衡量不同浏览器在 Android 和 Linux 上的浏览器性能。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1208/0412543ca3c4460.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1208/0412543ca3c4460.jpg" alt="60a3rxv1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">虽然该工具集看起来是通用的，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>强调它可以用来监测和测量浏览器的性能。基于过去几十年微软改善 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 系统性能的方法，该跟踪处理工具可以用来提供更多关于操作系统和应用代码在某一时间点上的洞察力。</p><p style="text-align: left;">如果你愿意，你还可以将这些痕迹与 Windows 性能分析器（WPA）联系起来。该工具集本身是建立在 .NET 核心和 microsoft-performance-toolkit-sdk 上的，这意味着理论上它可以支持任何.NET核心支持的操作系统。</p><p style="text-align: left;">当 Linux 方面，该工具集包括 LTTng、perf 和 Perfetto。同时，只有 Perfetto在Chromium和Android环境下被支持。每个单独的工具所支持的追踪指标如下：</p><p style="text-align: left;">● LTTng（Linux内核CPU调度、进程、线程、块IO/磁盘、系统调用、文件事件等）</p><p style="text-align: left;">● perf Linux CPU采样(cpu-clock)</p><p style="text-align: left;">● Perfetto Android & Chromium (CPU调度、CPU采样、CPU频率、FCrace、Android日志、通用事件/默认轨迹、GPU计数器)</p><p style="text-align: left;">通过该工具集，你可以分析追踪、记录追踪、启用对它们的编程访问，甚至可以将其与 WPA 整合，这样你就有了一个 GUI，可以更容易进行分析。</p>   
</div>
            