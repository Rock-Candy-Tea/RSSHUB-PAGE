
---
title: '阿里巴巴为Linux内核调度器提出组平衡器（GB）概念'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0104/2556cecd3b6b689.jpg'
author: cnBeta
comments: false
date: Tue, 04 Jan 2022 14:04:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0104/2556cecd3b6b689.jpg'
---

<div>   
随着越来越多的组织为了发展云计算等业务配置他们的服务器在应用程序之间共享CPU核心/资源，而不是专门分配CPU核心给单个应用程序/任务，<strong>中国公司阿里巴巴正在为Linux内核调度器提出一个新的"组平衡器"概念以提升系统资源利用表现。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0104/2556cecd3b6b689.jpg" title alt="image.jpg" referrerpolicy="no-referrer"><br></p><p>拟议中的的Linux组平衡器主要是在任务间共享资源时减少资源冲突。这个平衡器的重点是在各组CPU核心之间平衡各组任务。</p><p>关于这个组平衡器（GB）的"征求意见"今天被发出，并被总结为：</p><p>"我们需要的是一种缓解共享模式下冲突的方法，使组尽可能地排他，以获得性能和资源效率。组平衡器的主要想法是通过在各组CPU之间平衡任务组来满足这一要求，将其视为一种动态的半排他模式。</p><p>就像在CPU之间平衡任务一样，现在有了GB，用户可以把CPU X,Y,Z分成三个分区，并在这些分区中平衡A,B,C组，使它们尽可能地实现独占，而任务触发器的工作是把它的组安顿到一个适当的分区（最小的预测负载），然后尝试把自己迁移到这个区，随后逐步将组安顿到最能实现独占的区中"。</p><p>阿里巴巴在一台128核CPU服务器上的基准测试发现，与标准共享模式相比，Redis在GB模式下可以提升2~10%的性能。</p><p>您可以在这里了解更多：</p><p><a href="https://lore.kernel.org/lkml/98f41efd-74b2-198a-839c-51b785b748a6@linux.alibaba.com/" _src="https://lore.kernel.org/lkml/98f41efd-74b2-198a-839c-51b785b748a6@linux.alibaba.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="a29b9ac49693c7c4c68f9596c0908f939b9ac38f9a919bc18f9793c0959a97c095969ac394e2cecbccd7da8cc3cecbc0c3c0c38cc1cdcf">[email protected]</span>/</a><br></p>   
</div>
            