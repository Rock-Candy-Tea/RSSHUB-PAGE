
---
title: 'AMD"Zen 4"芯片、晶体管数量、缓存大小和延迟细节初步解析'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0830/0800e4dfd67ede7.jpg'
author: cnBeta
comments: false
date: Tue, 30 Aug 2022 09:45:49 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0830/0800e4dfd67ede7.jpg'
---

<div>   
我们正在等待AMD详细介绍其新的"Zen 4"微架构的技术文件，特别是所有重要的CPU核心前端和分支预测单元，这些单元为比上一代"Zen 3"核心多出13%的IPC贡献了三分之二，虽然实物还没有出现，技术爱好者社区已经在解读Ryzen 7000系列发布会上的图片。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0830/0800e4dfd67ede7.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0830/0800e4dfd67ede7.jpg" title alt="WuHAyr6QC7Ch2JCm.jpg" referrerpolicy="no-referrer"></a></p><p>"Skyjuice"展示了"Zen 4"内核的第一个注释，揭示了它的大型分支预测单元、扩大的微操作缓存、TLB、加载/存储单元以及能够支持AVX-512的双泵送256位FPU。该核心四分之一的芯片面积也被1MB的专用二级缓存所占用。</p><p>Chiakokhua（又名退休工程师）发布了一张表格，详细介绍了各种缓存及其延迟，并与"Zen 3"内核的缓存进行了比较。正如<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的Mark Papermaster在Ryzen 7000发布会上透露的那样，该公司已经将该核心的微操作缓存从<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>B扩大到6.75KB。L1I和L1D缓存的大小仍为32KB；而L2缓存的大小增加了一倍。L2高速缓存的扩大略微增加了延迟，从12个周期增加到14个周期。共享L3高速缓存的延迟也增加了，从46个周期增加到50个周期。调度阶段的重新排序缓冲器（ROB）已经从256个条目扩大到320个条目。L1分支目标缓冲器（BTB）的大小从1KB增加到1.5KB。</p><p>尽管晶体管数量较多，但Zen 4的CCD比Zen 3的CCD略小，这要归功于5纳米（TSMC N5工艺）制程的转换。新一代CCD的尺寸为70mm²，而"Zen 3"的CCD尺寸为83mm²。Zen 4"CCD的晶体管数量为65.7亿，比"Zen 3"CCD及其41.5亿晶体管数量增加了58%。</p><p><a href="https://static.cnbetacdn.com/article/2022/0830/2631842c8d967ea.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0830/2631842c8d967ea.jpg" title alt="ACyDDBZfOvkFm1js.jpg" referrerpolicy="no-referrer"></a></p><p>cIOD（客户端I/O芯片）有很大一部分创新。它建立在6纳米（台积电N6）节点上，与Ryzen 5000系列处理器的cIOD所采用的GlobalFoundries 12纳米节点相比，这是一个巨大的飞跃。它还吸收了Ryzen 6000"Rembrandt"处理器的某些电源管理功能。除了DDR5内存控制器和一个PCI-Express Gen 5根复合体，这个CIOD还配备了一个基于RDNA2图形架构的iGPU。新的6纳米cIOD尺寸为124.7平方毫米，相比之下，Ryzen 5000系列的cIOD略大124.9平方毫米。</p><p>"Raphael"多芯片模块为6核和8核SKU配备一个CCD，为12核和16核SKU配备两个CCD。"Raphael"是在Socket AM5封装中构建的。据传，AMD正在为高性能笔记本平台准备一种薄BGA封装的"Raphael"，它的代号为"Dragon Range"。这些处理器将有各种45W、55W和65W的TDP选项，可以为高端游戏笔记本提供多种选择。</p>   
</div>
            