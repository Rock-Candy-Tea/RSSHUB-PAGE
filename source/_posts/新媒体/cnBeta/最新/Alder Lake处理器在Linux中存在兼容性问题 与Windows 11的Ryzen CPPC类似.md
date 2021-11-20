
---
title: 'Alder Lake处理器在Linux中存在兼容性问题 与Windows 11的Ryzen CPPC类似'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1120/0e65688ea9c934e.jpg'
author: cnBeta
comments: false
date: Sat, 20 Nov 2021 12:42:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1120/0e65688ea9c934e.jpg'
---

<div>   
当英特尔在2021年架构日活动中介绍其Alder Lake架构时，该公司着重介绍其围绕微软Windows
11的性能优化。然而，对于Linux来说，似乎不能这么说。<strong>就在几天前，我们报道了一个Alder Lake的bug，该bug在即将到来的Linux
5.16内核上导致性能下降；昨天，针对Alder Lake上检测到的相关问题收到了一个新相关性补丁。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1120/0e65688ea9c934e.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>这个新问题围绕着协作处理器性能控制（CPPC）或最快内核优先级，并且很容易让人想起最近<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11上的Ryzen CPPC2 bug。</p><p>Alder Lake带来了新的性能混合架构，带来了大小核价格，但目前，当系统处于超频状态时，Linux无法分别识别这些内核。因此，操作系统为所有内核分配了同等的性能潜力，而不管它们是P内核还是E内核。</p><p>这导致了与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的Turbo Boost Max技术（ITMT）的冲突，该技术有助于将优先单线程工作负载安排在最快的内核上。然而，由于现在所有的核心都分配了相等的性能值，ITMT在这种超频系统中无法工作。</p><p>即将推出的补丁希望在MSR_HWP_CAPABILITIES或硬件控制的P-States（HWP）的帮助下解决这个问题。但是这个补丁可能无法在缺乏MSR_HWP_CAPABILITIES的旧式系统上工作。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/linux-pm/20211119051801.1432724-1-srinivas.pandruvada@linux.intel.com/T/#u" _src="https://lore.kernel.org/linux-pm/20211119051801.1432724-1-srinivas.pandruvada@linux.intel.com/T/#u" target="_blank">https://lore.kernel.org/linux-pm/<span class="__cf_email__" data-cfemail="596b696b6868686860696c6861696877686d6a6b6e6b6d7468742a2b3037302f382a772938373d2b2c2f383d38193530372c217730372d3c35773a3634">[email protected]</span>/T/#u</a><br></p>   
</div>
            