
---
title: '索尼提议为Linux提供新的软件看门狗以维持系统健康运行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Sat, 24 Apr 2021 11:41:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>索尼Linux工程师Peter Enderborg为Linux内核提出了一种软看门狗（Soft Watchdog）概念，主要用于在某些情况下执行预定义的任务</strong>，它不像常用的硬看门狗那样在出现问题时自动重新启动系统。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>这个提议的"软看门狗"将执行除硬重启之外的任务，例如在系统运行缓慢或内存不足的情况下采取预定义的行动。</p><p>这个软看门狗可以和各种低内存/内存超限的守护程序集成，以帮助在这种情况出现时对大量占用内存/低优先级的应用程序提前采取行动。这个软看门狗也可以独立工作，在内存不足的情况下自己采取行动杀死进程。也可以创建其他规则来保证系统持续稳定运行。</p><p>不过，索尼今天发出的软看门狗建议是一个 "征求意见"，未来我们将在这一点上看到Linux内核工作的进展。对于索尼本身来说，提出这个概念似乎是出于对Android/嵌入式应用的考虑。</p><p>这个软看门狗提案可以在内核邮件列表中找到：</p><p><a href="https://lore.kernel.org/lkml/20210424102555.28203-2-peter.enderborg@sony.com/" _src="https://lore.kernel.org/lkml/20210424102555.28203-2-peter.enderborg@sony.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="46747674777672747277767473737368747e7476756b746b362332233468232822233424293421063529283f6825292b">[email protected]</span>/</a><br></p>   
</div>
            