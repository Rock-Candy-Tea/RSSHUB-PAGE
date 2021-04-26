
---
title: 'Linux 5.13增加来自英特尔的KCPUID组件 帮助准确识别新推出的CPU'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0426/53bbe71ba912e50.jpg'
author: cnBeta
comments: false
date: Mon, 26 Apr 2021 12:00:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0426/53bbe71ba912e50.jpg'
---

<div>   
<strong>今天上午，在新开放的Linux 5.13合并窗口的 "x86/misc "拉动请求中，增加了新的KCPUID实用工具。</strong>KCPUID是由英特尔添加到Linux内核源码树中的，用于报告CPU特性，以替代/proc/cpuinfo等传统的处理器识别命令。<br>
 <p><strong>了解更多：</strong></p><p><a href="http://lkml.iu.edu/hypermail/linux/kernel/2104.3/01182.html" _src="http://lkml.iu.edu/hypermail/linux/kernel/2104.3/01182.html" target="_blank">http://lkml.iu.edu/hypermail/linux/kernel/2104.3/01182.html</a><br></p><p>KCPUID 是一个存在于内核源码树中的工具，用于可靠地报告原始的 CPU 特性，而 /proc/cpuinfo 有时会在启动时和为 /proc/cpuinfo 报告添加新的特性位之前报出错误信息。</p><p>还有其他用户空间的工具来报告CPU特性，但它们不一定是最新的。通过将 KCPUID 保留在内核源码树中，并由开源的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>工程师维护，这就几乎可以确保至少来自英特尔的处理器信息能够一直是最新的。KCPUID 依赖于存储在 CSV 文件中的 CPUID 子定义，因此也非常容易添加新的条目。</p><p>由于添加新的CPUID很容易，只需要写入CSV即可，而且已经是内核源码树的一部分，英特尔方面似乎对使用这个工具在预生产的x86处理器上实现新功能很感兴趣。不过大多数用户使用/proc/cpuinfo去读取CPU信息已经足够，但对于那些要开发新的x86处理器功能的用户来说，内核源码树中的KCPUID可能会被证明是很方便的。</p><p>为 Linux 5.13 添加 KCPUID 是今天 x86/misc pull 的主要变化。</p><p><a href="https://static.cnbetacdn.com/article/2021/0426/53bbe71ba912e50.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0426/53bbe71ba912e50.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            