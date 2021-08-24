
---
title: 'Intel 12代酷睿性能首次公开：大小核相差50％'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0824/2854c491ffe1972.png'
author: cnBeta
comments: false
date: Tue, 24 Aug 2021 08:55:21 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0824/2854c491ffe1972.png'
---

<div>   
Intel已经公开了Alder Lake
12代酷睿的大小核架构设计、规格特性，而对于这种混合架构在主流平台的第一次应用，几乎所有的玩家都在担心：大小核调度效率怎么样？小核的性能怎么样？Hot
Chips 33大会上，Intel首次公开了12代酷睿大小核的性能关系，当然官方分别叫做性能核(P-Core)、能效核(E-Core)。<br>
 <p>按照Intel的说法，<strong>在同等功耗下，大核的单线程性能比小核高出50％。</strong></p><p>当然，大核的实际功耗会高得多，频率也会更高，因此实际单线程性能还会更好，但这也能看出，小核的性能其实并没有那么孱弱，尽管它本质上还是Atom那一套。</p><p><strong>多线程性能方面，2大核＋8小核的组合，相比4个大核，在同等功耗下也可以领先50％。</strong></p><p>按照官方说法，一个大核的面积等于四个小核加其二级缓存，这么算的话2大核＋8小核、4大核的面积基本相当，但换来了更好的多线程性能，比单纯、暴力地堆砌大核还是更高效的。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/2854c491ffe1972.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/2854c491ffe1972.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/2854c491ffe1972.png" referrerpolicy="no-referrer"></a></p><p>当然，这些都是官方说法，实际如何还要等待上市后检验，尤其是大小核调度问题，一旦发挥失常，反而会得不偿失。</p><p>为此，Intel自然比谁都懂，特别设计了<strong>Thread Director(线程调度器)</strong>，直接集成在CPU核心之中，再搭配特别优化的<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11操作系统，在不同核心之间分配工作负载。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/ae958e2e946a0dd.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/ae958e2e946a0dd.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/ae958e2e946a0dd.png" referrerpolicy="no-referrer"></a></p><p><strong>Thread Director会实时监测每个线程的指令集、每个核心的状态，时间间隔在纳秒级别，然后反馈给操作系统的调度器，便于后者针对工作负载做出最优化分派。</strong></p><p>同时，它会根据处理器的散热设计、运行状态、功耗设定，动态调整反馈建议，并调整处理器电压、频率，优化功耗、散热，而这一切都无需用户手动干预。</p><p>再深入一点来说，Thread Director在监控线程、核心状态的时候，<strong>会用到机器学习算法，在硬件层面定期写入、刷新一个反馈表(EHFI)，操作系统调度器就以此为准去安排。</strong></p><p>不同的线程会分配给不同的优先级，其中后台线程一律交给小核，高优先级线程自然给大核，而如果发生冲突，低优先级线程就会提高并转移到大核。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/fa64829bdb98cb1.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/fa64829bdb98cb1.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/fa64829bdb98cb1.png" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/478c2df500503a2.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/478c2df500503a2.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/478c2df500503a2.png" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/52f09e2076e953a.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/52f09e2076e953a.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/52f09e2076e953a.png" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/b6216723693af0f.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/b6216723693af0f.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/b6216723693af0f.png" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0824/511476a1378119b.png"><img data-original="https://static.cnbetacdn.com/article/2021/0824/511476a1378119b.png" src="https://static.cnbetacdn.com/thumb/article/2021/0824/511476a1378119b.png" referrerpolicy="no-referrer"></a></p>   
</div>
            