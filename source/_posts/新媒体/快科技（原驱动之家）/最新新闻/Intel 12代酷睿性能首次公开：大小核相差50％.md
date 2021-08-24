
---
title: 'Intel 12代酷睿性能首次公开：大小核相差50％'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210824/s_f1b33db2b92f4cf4b720e9e33c65bf18.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 24 Aug 2021 16:47:16 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210824/s_f1b33db2b92f4cf4b720e9e33c65bf18.png'
---

<div>   
<p>Intel已经公开了<a class="f14_link" href="https://news.mydrivers.com/1/777/777623.htm" target="_blank">Alder Lake 12代酷睿的大小核架构设计、规格特性</a>，而对于这种混合架构在主流平台的第一次应用，几乎所有的玩家都在担心：大小核调度效率怎么样？小核的性能怎么样？</p>
<p>Hot Chips 33大会上，Intel首次公开了12代酷睿大小核的性能关系，当然官方分别叫做性能核(P-Core)、能效核(E-Core)。</p>
<p>按照Intel的说法，<strong><span style="color:#ff0000;">在同等功耗下，大核的单线程性能比小核高出50％。</span></strong></p>
<p>当然，大核的实际功耗会高得多，频率也会更高，因此实际单线程性能还会更好，但这也能看出，小核的性能其实并没有那么孱弱，尽管它本质上还是Atom那一套。</p>
<p><strong><span style="color:#ff0000;">多线程性能方面，2大核＋8小核的组合，相比4个大核，在同等功耗下也可以领先50％。</span></strong></p>
<p>按照官方说法，一个大核的面积等于四个小核加其二级缓存，这么算的话2大核＋8小核、4大核的面积基本相当，但换来了更好的多线程性能，比单纯、暴力地堆砌大核还是更高效的。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210824/f1b33db2b92f4cf4b720e9e33c65bf18.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_f1b33db2b92f4cf4b720e9e33c65bf18.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>当然，这些都是官方说法，实际如何还要等待上市后检验，尤其是大小核调度问题，一旦发挥失常，反而会得不偿失。</p>
<p>为此，Intel自然比谁都懂，特别设计了<strong>Thread Director(线程调度器)</strong>，直接集成在CPU核心之中，再搭配特别优化的Windows 11操作系统，在不同核心之间分配工作负载。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210824/3aa5cf41d2434ebea105f107be21ef9b.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_3aa5cf41d2434ebea105f107be21ef9b.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>Thread Director会实时监测每个线程的指令集、每个核心的状态，时间间隔在纳秒级别，然后反馈给操作系统的调度器，便于后者针对工作负载做出最优化分派。</strong></p>
<p>同时，它会根据处理器的散热设计、运行状态、功耗设定，动态调整反馈建议，并调整处理器电压、频率，优化功耗、散热，而这一切都无需用户手动干预。</p>
<p>再深入一点来说，Thread Director在监控线程、核心状态的时候，<strong>会用到机器学习算法，在硬件层面定期写入、刷新一个反馈表(EHFI)，操作系统调度器就以此为准去安排。</strong></p>
<p>不同的线程会分配给不同的优先级，其中后台线程一律交给小核，高优先级线程自然给大核，而如果发生冲突，低优先级线程就会提高并转移到大核。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210824/89e086499f04497a966b5a47e1074b60.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_89e086499f04497a966b5a47e1074b60.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210824/eb3b38d8913944379d8191ebcd4c2e9d.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_eb3b38d8913944379d8191ebcd4c2e9d.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210824/616c7998d1634f82a39588f3d15f2f3e.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_616c7998d1634f82a39588f3d15f2f3e.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210824/ca01b4e1bae941558807c2f68006da1d.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_ca01b4e1bae941558807c2f68006da1d.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210824/01e224b2aabe460eabd355c54dfd03d3.png" target="_blank"><img alt="Intel 12代酷睿大小核性能公开：50％的差异" h="337" src="https://img1.mydrivers.com/img/20210824/s_01e224b2aabe460eabd355c54dfd03d3.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"> </p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/alder_lake.htm"><i>#</i>Alder Lake</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            