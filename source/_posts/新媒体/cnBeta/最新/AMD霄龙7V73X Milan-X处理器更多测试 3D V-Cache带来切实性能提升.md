
---
title: 'AMD霄龙7V73X Milan-X处理器更多测试 3D V-Cache带来切实性能提升'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0117/1cac19ca90c0b5d.jpg'
author: cnBeta
comments: false
date: Sat, 22 Jan 2022 04:51:36 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0117/1cac19ca90c0b5d.jpg'
---

<div>   
上周，Chips and Cheese 分享了 AMD 霄龙 7V73X 数据中心旗舰处理器的首份实测数据，证实了 3D V-Cahce 为 Milan-X CPU 架构带来的巨大性能提升。<strong>早期数据多集中在延迟性能方面，但本周，我们又看到了更细致的相关基准测试。</strong>可知在特定工作负载下，EPYC 7V73X 可领先 7763 CPU 达 12.5% 。<br>
 <p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2022/0117/1cac19ca90c0b5d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0117/1cac19ca90c0b5d.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p>本轮测试涉及更多延迟基准、针对 EPYC 7763 CPU 的整体带宽和特定工作负载的横向对比，并且加入了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Ice Lake / Cascade Lake 至强竞品。</p><p>有趣的是，英特尔 CPU 基于单片设计 + Mesh 互连架构，而 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 选用了环形总线。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0122/1ed4394933553f8.png" alt="1.png" referrerpolicy="no-referrer"></p><p>环形总线具有更低延迟 / 更高带宽的特性，而 Mesh 设计又让芯片更具可扩展性。</p><p>即便如此，拥有较小的 L2 缓存 / 较大的 L3 缓存的 AMD Milan / Milan CPU，其带宽还是更具优势。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0122/520ec307f487374.png" alt="2.png" referrerpolicy="no-referrer"></p><p>EPYC 7V73X（Milan-X）拥有 64C / 128T 和惊人的 768MB 缓存容量（标准 256MB + 堆叠 512MB SRAM），基础频率 2.2GHz / 加速可达 3.5GHz，最大热设计功耗（TDP）为 280W 。</p><p>在 Chips and Cheese 分享的五项基准测试中，EPYC 7V73X 有四项全面领先，仅在 OpenSSL 一项被 EPYC 7763 反超。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0122/cc94a4093cd9217.png" alt="3.png" referrerpolicy="no-referrer"></p><p>原因是 OpenSSL 工作负载根本未对缓存造成压力，且 Milan-X CPU 在调用所有 CCD 时的持续性能损失，也是一眼能够看穿的。</p><p>不过就算这样，在 Gem5 基准测试项目中，Milan-X 还是能够在频率低 5% 的情况下、性能较 Milan-X 提升 7.6%（意味着 V-Cache 性能提升 12.5%）。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0122/c456a01e58ac81b.png" alt="4.png" referrerpolicy="no-referrer"></p><p>其它基准测试也表现出了类似的性能提升，EPYC 7V73X 在 Y-Cruncher 项目中有 1.5% 的领先优势。即使该测试非常依赖于 FPU 和内存，3D V-Cache 还是很好地弥补了频率上的损失。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0122/65d49b9198a2ab3.png" alt="5.png" referrerpolicy="no-referrer"></p><p>综上所述，Chips and Cheese 指出，3D V-Cache 给 EPYC Milan-X CPU 带来了切实的性能提升，且他们迫不及待地想要看到进一步的发展。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1226691.htm" target="_blank">AMD霄龙7V73X实测：3D V-Cache让Milan-X处理器刮目相看</a></p></div>   
</div>
            