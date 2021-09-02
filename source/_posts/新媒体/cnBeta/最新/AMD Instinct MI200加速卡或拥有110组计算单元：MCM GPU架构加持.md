
---
title: 'AMD Instinct MI200加速卡或拥有110组计算单元：MCM GPU架构加持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0729/2b9eec00ebf909a.jpg'
author: cnBeta
comments: false
date: Thu, 02 Sep 2021 02:44:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0729/2b9eec00ebf909a.jpg'
---

<div>   
<strong>Coelacanth's Dream 刚刚在 GitHub 上发现了一份近期提交的代码，可知其中揭示了有关即将到来的基于 AMD Aldebaran GPU 的 Instinct 加速卡的一些细节。</strong>据悉，代号为“GFX90A”的该系列 GPU 将采用 CDNA 2 架构，同时它也是 GFX 9th Family（Vega 家族）的衍生型号。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0729/2b9eec00ebf909a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0729/2b9eec00ebf909a.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://wccftech.com/amd-instinct-mi200-speculated-to-utilize-110-compute-units-per-mcm-gpu/" target="_self">WCCFTech</a>）</p><p>其中包括了 GFX906_60、GFX908_120 和 GFX90A_110 三个代码，预计分别对应 Instinct MI60、MI100、以及新一代 HPC 加速器 SKU 。</p><p>从型号命名规则上来看，猜测 MI60 / MI100 分别拥有 60 / 120 组计算单元（CU）。奇怪的是，GFX90A_110 的计算单元竟然比 MI100 更少。</p><p><img src="https://static.cnbetacdn.com/article/2021/0902/796811923aefe1d.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（截图 via <a href="https://videocardz.com/newz/amd-instinct-mi200-with-mcm-aldebaran-gpu-might-feature-110-compute-units" target="_self">VideoCardz</a>）</p><p>虽然有消息称 Aldebaran GPU 将拥有 128 组 CU，但这与我们看到的有关 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 下一代 Instinct 加速卡的规格有些不符。</p><p>不过考虑到厂商会按需屏蔽部分瑕疵单元（渲染引擎 / 计算单元），我们对 110 CU 的 GPU SKU 也并不感到意外。</p><p><a href="https://www.coelacanth-dream.com/posts/2021/09/01/aldebaran-gfx90a-cu/" target="_self">Coelacanth's Dream</a> 预计：MI200 的 Aldebaran GPU 采用了双拼的 MCM 设计，每边都有 56 个 CU 。分别屏蔽其中一个的话，就组成了 110 个。</p><p><img src="https://static.cnbetacdn.com/article/2021/0902/9fa9275c760359a.png" alt="2.png" referrerpolicy="no-referrer"></p><p>目前尚不清楚 AMD 是否计划将 CDNA 2 架构上的 FP32 内核数量增加一倍。</p><p>假使该公司这么做，那下一代 Instinct 计算卡有望在 1500 MHz 的时钟频率下，达成 42.2 TFLOPs 的单精度算力（即 MI100 的 1.82 倍）。</p><p>若没有这么做，则 MI200 需要将 GPU 频率至少提升至 1650 MHz，才能达到 23 TFLOPs 的 FP32 吞吐量。</p><p><a href="https://static.cnbetacdn.com/article/2021/0902/3a3b5e16d69ee48.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0902/3a3b5e16d69ee48.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p>不过对于 MI200 之类的 HPC 加速卡来说，FP64 的性能显然更加重要。由早前泄露的消息可知，MI200 将具有全速率的 FP64 性能，意味其性能可达到 MI100 的两倍或四倍（具体取决于选用了怎样的架构设计）。</p><p>如果一切顺利，AMD 或在 2021 年底前发布 MI200 。作为该公司革命性的 MCM 多芯片 HPC 加速卡，它还将板载 128GB 的 HBM2e 高带宽缓存。</p>   
</div>
            