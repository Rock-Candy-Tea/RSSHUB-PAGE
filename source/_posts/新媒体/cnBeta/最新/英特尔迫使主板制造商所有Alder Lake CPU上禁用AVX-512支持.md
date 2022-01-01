
---
title: '英特尔迫使主板制造商所有Alder Lake CPU上禁用AVX-512支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0101/e6c9ed2493f23b7.png'
author: cnBeta
comments: false
date: Sat, 01 Jan 2022 09:01:39 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0101/e6c9ed2493f23b7.png'
---

<div>   
<strong>英特尔Alder Lake台式机CPU将在主板制造商的下一个主要BIOS中失去AVX-512指令集。</strong>虽然英特尔Alder Lake
CPU没有正式声明支持AVX-512指令，但可以通过禁用高能效的"Gracemont"内核，让高性能的"Golden
Cove"内核运行来启用这些指令。这提供了比标准AVX2指令稍好的性能和更高的效率。<br>
 <p>虽然E-cores在一些工作负载中具有自己的优势，但看起来AVX-512指令的效率也更高。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>酷睿i7-12700F非K版Alder Lake CPU在泄露的基准测试中比<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的Ryzen 7 5800X快约10%。</p><p>但这一切都将被改变，因为Igor's Lab报告说，英特尔正在指示主板制造商通过即将到来的BIOS更新，在Alder Lake CPU上取消对AVX-512的支持。在英特尔计划推出其非K型Alder Lake阵容的前几天，此举并不令人惊讶，该阵容将以大多数仅有P核的型号（Core i5和Core i3将是非混合型）为特色。</p><p><a href="https://static.cnbetacdn.com/article/2022/0101/e6c9ed2493f23b7.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0101/e6c9ed2493f23b7.png" title alt="avx512_yc_ptime.png" referrerpolicy="no-referrer"></a></p><p>这些芯片有可能成为入门级服务器和工作站的热门产品，其AVX-512的优点可以在那里得到利用，英特尔不希望这种情况发生，因此，他们正在尽力从阵容中删除对该指令集的支持。然而还不止这么多，Igors实验室解释说，标准的AVX2指令在所有混合芯片中都有一个非常严格的温度墙功能，在WiNFO中被识别为"IA.Max Turbo Limit - Yes"。Max Turbo Limit - Yes"。</p><p><a href="https://static.cnbetacdn.com/article/2022/0101/4ac430f58581e2e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0101/4ac430f58581e2e.png" title alt="intelavx512_microcode_enabled-1.png" referrerpolicy="no-referrer"></a><a href="https://static.cnbetacdn.com/article/2022/0101/f8550eefdc995a9.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0101/f8550eefdc995a9.png" title alt="intelavx512_microcode_disabled.png" referrerpolicy="no-referrer"></a></p><p>温度墙导致了有限的时钟速度，其中一个原因是为了避免新芯片内部的电子迁移退化。现在，由于这些措施，只有少数系统可以达到芯片的5.2GHz最大时钟，因为许多PC没有足够的冷却装置来达到这些高时钟。</p><p>已经拥有这套平台的用户需要注意保留现有的BIOS以保留AVX-512指令，特别是主板库存预计会有旧版BIOS。值的主要的是，用户肯定需要一个比推出时更好的BIOS，以使其Alder Lake CPU具有良好的稳定性和DDR5兼容性，但升级意味着与该指令集说再见。因此，英特尔的这一举动真的很奇怪，如果他们对消费者CPU拥有这一功能感到如此不适，那么他们一开始就不应该提供。</p>   
</div>
            