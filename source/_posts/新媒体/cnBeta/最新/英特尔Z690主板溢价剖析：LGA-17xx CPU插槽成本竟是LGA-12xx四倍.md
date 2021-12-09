
---
title: '英特尔Z690主板溢价剖析：LGA-17xx CPU插槽成本竟是LGA-12xx四倍'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1209/50dbc571c90b187.jpg'
author: cnBeta
comments: false
date: Thu, 09 Dec 2021 03:40:14 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1209/50dbc571c90b187.jpg'
---

<div>   
<strong>在英特尔正式发布了 12 代 Alder Lake 酷睿桌面处理器之后，许多人也对配套的 Z690 高端芯片组的实际成本感到了好奇。为此，TechPowerUp 等媒体也决定帮助大家四处打听一下。</strong>可知在诸多影响因素中，因为支持 DDR5 内存而导致的 PCB 物料成本增加，反而是其次的。最让我们感到意外的是，代价最高的单个部件，反而是 LGA-17xx CPU 插槽及其固定组件 —— 是 LGA-12xx 的四倍左右！<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1209/50dbc571c90b187.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1209/50dbc571c90b187.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://wccftech.com/intel-releases-600-chipset-specifications-and-the-real-costs-of-current-z690-motherboards/" target="_self">WCCFTech</a>）</p><p>按照计划，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>将于 2022 年初揭晓高端 Z690 之外的主流 H670 / B660 芯片组、以及入门级的 H610 型号。</p><blockquote><p>● 规格方面，H670 将涵盖 Z690 的大部分 I/O 功能，但砍掉了多余的 CPU 超频支持。</p><p>● 但对于广大消费者来说，B660 系列仍将凭借相对丰富的 I/O 功能集（同时这代将解锁对内存超频的支持 / 前提是 CPU 也支持），成为市场上的性价比首选。</p><p>● 至于最实惠 H610，其提供的 I/O 选项最为简洁，甚至会砍掉与 CPU 直连的 NVMe <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 插槽。</p></blockquote><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1207/c3268beca98ece0.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1207/c3268beca98ece0.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1207/c3268beca98ece0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">PCIe 通道与 I/O 端口对比（via <a href="https://www.techpowerup.com/289728/intel-z690-motherboard-costs-explained" target="_self">TechPowerUp</a>）</p><p>共同特性方面，12 代 Alder Lake 桌面处理器将支持最新的 PCIE 5.0 x16（PEG），但最终决定权还是下放到了主板厂商手中（目前仍有部分 Z690 主板仅提供对 PCIe 4.0 的支持）。</p><p>Z690 / H670 / B660 上“逐级递减”的规格变化，还是比较好理解的。USB 方面，H670 / B660 都提供了两个 20 Gbps 的 USB 3.2 Gen 2×2，但 H610 芯片组直接缩没了。</p><p>与英特尔 11 代酷睿处理器搭配的 500 系列主板相比，12 代台式处理器搭配的 600 系列主板的成本溢价，更多体现在某些关键组件的获取难度上。</p><p><img src="https://static.cnbetacdn.com/article/2021/1209/a74159aaba4e42e.jpg" referrerpolicy="no-referrer"></p><p>除了 DDR5 内存等新功能支持导致的 PCB 成本略有上升，LGA-17xx CPU 插槽及其固定机构的成本（51 美元）更是让人感到震惊，其成本直接飙到了 LGA-12xx 的四倍。</p><p>作为参考，LGA-115x 的小批量报价仅为 5 美元。不过随着供应链的成熟，LGA-17xx 处理器插槽的价格也有望回落到合理的水平。</p><p>其次是供电方面，随着英特尔从 IMVP8 升级到 IMVP9.1，主板厂商也需要将 DrMOS 换成 Smart Power Stage（简称 SPS）模组。</p><p>但由于供应链的持续不畅，Z690 成本几乎较 Z590 翻倍 —— 除非厂家顶风减少供电的相数来削减这部分成本。</p><p><img src="https://static.cnbetacdn.com/article/2021/1209/17af30c24cc29e6.jpg" referrerpolicy="no-referrer"></p><p>至于主板上的 PCIe 5.0 插槽数量，想要提供两条及以上的高端型号，就需要配备额外的重定时器芯片才能实现，目前小批量报价为 45 美元左右。</p><p>作为参考，PCIe 4.0 重定时器的大批量采购价在 20~30 美元左右。想要控制成本的话，主流 600 系列芯片组应该还是会只保留一条标准的 PCIe 5.0 x16 显卡插槽。</p><p>然后是 PCIe 5.0 的 SMT 物理组件，其与 PCIe 4.0 版本的成本差距或在 10~20% 之间。但在大规模订购时，每个连接器付出的额外代价几可忽略不计。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1211823.htm" target="_blank">Intel H670/B660/H610主板集体曝光：全线支持DDR5、PCIe 5.0</a></p></div>   
</div>
            