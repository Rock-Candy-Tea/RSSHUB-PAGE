
---
title: 'AMD霄龙7V73X实测：3D V-Cache让Milan-X处理器刮目相看'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0112/2e8f5e8f0e2df25.jpg'
author: cnBeta
comments: false
date: Mon, 17 Jan 2022 03:32:57 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0112/2e8f5e8f0e2df25.jpg'
---

<div>   
Chips and Cheese 刚刚分享了 AMD 霄龙（EPYC）Milan 和 Milan-X 处理器的首份对比测试数据，<strong>可知除了 3D V-Cache 的加持、Milan-X CPU 在延时和加速频率等方面的表现也更优异。</strong>采用堆叠设计的 512MB L3 SRAM，无疑在其中扮演了至关重要的角色，每个 Zen 3 CCD 模组都分配了多倍的 64MB L3 缓存。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0112/2e8f5e8f0e2df25.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>本次对比测试在 EPYC 7V73X（Milan-X）和 EYPC 7763（Milan）两款服务器 CPU 之间展开：</p><blockquote><p>● EPYC 7V73X 具有 64C / 128T，拥有总计 768MB 缓存（含 256MB L3）。基础频率 2.2 GHz / 加速可达 3.5 GHz，最大热设计功耗（TDP）280W 。</p><p>● EPYC 7763 也是 64C / 128T，拥有 32MB L2 + 256MB L3 缓存（无 3D V-Cache）。基础频率 2.45 GHz / 加速可达 3.5 GHz，最大 TDP 280W 。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0117/e68b01a19c4b01d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0117/e68b01a19c4b01d.png" alt="1-1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">缓存与内存延迟（周期）对比</p><p>在缓存提升至三倍的同时，Milan-X 在延迟上却与 Milan CPU 几乎保持一致。与新处理器获得的 LLC 总量提升相比，3-4 个周期是延迟增加，其对性能的影响，几可忽略不计。</p><p>其次，Chips and Cheese 发现了另一件趣事 —— Milan-X 能够较 Milan CPU 维持更高的加速时钟频率。</p><p>即使两者的纸面参数一样，但 3D V-Cache 设计的引入，显然有效抵消了延迟周期增加的负面影响。</p><p><a href="https://static.cnbetacdn.com/article/2022/0117/324349d7673d83c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0117/324349d7673d83c.png" alt="1-2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">缓存与内存延迟（ns）对比</p><p>单个 3D V-Cahce 堆栈包含了 64MB L3 缓存，并通过 TSV 硅通孔工艺部署在现有的 Zen 3 CCD（以及 32MB L3 缓存）之上，从而让每组 CCD 总计拥有 96MB 缓存。</p><p>AMD 还表示，其能够让 V-Cache 做到 8-hi 堆叠，意味着理论上每组 Zen 3 CCD 可拥有最高 32MB L3 + 512MB SRAM 缓存。如果搭配 64MB L3，则是最高 768MB 。</p><p><a href="https://static.cnbetacdn.com/article/2022/0117/1cac19ca90c0b5d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0117/1cac19ca90c0b5d.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>参考 AMD 的 RTL 验证测试，Milan-X 性能可领先 Milan CPU 高达 66% 。此外现场展示的 Milan-X 16 核 SKU，可较对应的 Milan 型号更快地完成 Synopsys VCS 功能验证测试。</p><p>最后，Chips and Cheese 表示他们将很快开展更加全面的 Milan-X 对比性能测试，后续将分享包括带宽在内的详细数据、以及与其它数据中心类竞品 CPU 的比较。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1224935.htm" target="_blank">AMD霄龙7773X ES处理器跑分曝光：双路测试平台 多线程得分近30000</a></p></div>   
</div>
            