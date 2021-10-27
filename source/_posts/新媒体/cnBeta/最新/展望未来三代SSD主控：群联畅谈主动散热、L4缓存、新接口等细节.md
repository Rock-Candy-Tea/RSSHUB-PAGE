
---
title: '展望未来三代SSD主控：群联畅谈主动散热、L4缓存、新接口等细节'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1027/a545d7cc56360de.jpg'
author: cnBeta
comments: false
date: Wed, 27 Oct 2021 02:08:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1027/a545d7cc56360de.jpg'
---

<div>   
<strong>在微星近日举办的 Insider 直播活动期间，群联（Phison）首席技术官 Sebastian Jean 展望了与未来几代 SSD 有关的 PCIe Gen 5 / Gen 6 / Gen 7 主控。</strong>他表示：虽然开发全新的 SSD 设计需要大约 16~18 个月的时间，但新一代硅工艺节点的技术启用要提前 2-3 年开始。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1027/a545d7cc56360de.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>以当前最受关注的 PCIe 5.0 芯片为例，群联定于明年开始向客户发货。据此倒推一下时间，该公司显然也已经在为 2025~2026 年出现的 PCIe Gen 6 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 做底层设计。</p><p>规格方面，报道称 PCIe 5.0 SSD 可带来高达 14 GB/s 的传输速率 —— 与单通道 DDR4-2133 内存的带宽相当。</p><p>尽管 SSD 无法彻底取代现代 DRAM 系统内存解决方案，但两者相结合的话、或为更多应用开辟出基于“L4 缓存”的新场景。</p><p><a href="https://wccftech.com/phison-talks-next-gen-pcie-gen-5-gen-6-gen-7-ssds-active-cooling-solutions-l4-cache-new-interfaces-up-to-14w-gen-5-28w-gen-6-tdps/" target="_self">WCCFTech</a> 指出，现代 CPU 架构已经包含了 L1 / L2 / L3 级别的缓存。得益于类似的设计架构，PCIe 5.0 级未来版本的 SSD，将能够作为 CPU 的最后一级缓存（LLC / L4）来更高效地使用。</p><p><a href="https://static.cnbetacdn.com/article/2021/1027/a5f048b0981b3db.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1027/a5f048b0981b3db.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>至于未来的 SSD 将如何发展，不难想象我们会迎来更实惠的价格、更高的 NAND 闪存密度、以及化解尺寸方面的限制。</p><p>此外随着 PCIe 标准的迭代，我们可以使用更少的通道来满足存储需求，比如从 PCIe 6.0 x4 改成 PCIe 7.0 x2 。</p><p>有趣的是，群联声称 3-bit（TLC）闪存仍将继续发展，同时 4-bit（QLC）闪存会在游戏读取速度方面具有更大的优势，此外厂商们也会在 PCIe 6.0 / 7.0 时代更细地花粉工作站 / 企业级 SSD 产品线。</p><p>软件层面，由<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>主导的直接存储（Direct Storage）API 等技术，将让下一代平台消费者体验到性能方面的巨大提升。</p><p><a href="https://static.cnbetacdn.com/article/2021/1027/28c02ff732b2bf3.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1027/28c02ff732b2bf3.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>至于散热和功耗，虽然群联“建议”PCIe 4.0 SSD 厂商配备散热器，但 PCIe 5.0 时代将成为标配。由于性能压榨会造成更高的发热，甚至不少厂商都会选择为它加装主动式的散热<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C738%2C751" target="_blank">风扇</a>。</p><p>据悉，PCIe 5.0 SSD 的平均热设计功耗（TDP）为 14W，而 PCIe 6.0 SSD 将增长到 28W、且热管理是横亘在行业发展面前的一个主要挑战。</p><p>目前 30% 的热量通过 M.2 连接器来散热、70% 通过螺丝固定传导，因而新接口 / 插槽也将在设计之初就考虑到这方面的巨大作用。</p><p><a href="https://static.cnbetacdn.com/article/2021/1027/50c4f85dfd81e1f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1027/50c4f85dfd81e1f.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p>即使当前的 PCIe 4.0 SSD 主控 / DRAM 缓存可承受高达 125℃ 的运行温度，但 NAND 闪存还是需要极佳的散热来保持长期工作的稳定 —— 超过 80℃ 或触发过热保护。</p><p>群联希望 SSD 能够维持在 50℃ 上下的基准运行温度，否则 SSD 性能会随着温度增长而加大节流。以铠侠新发布的 PCIe 5.0 SSD 原型为例，其读速达到了 14 GB/s、IO 性能也较 PCIe 4.0 SSD 翻倍。</p><p>最后，群联将在高端 PCIe 5.0 SSD 主控市场与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>展开激烈的交锋，同时 Marvell 也宣布了旗下支持 NVMe 1.4b 标准的新款 Bravera SC5 SSD 主控，可知其定于 2022 年与慧荣（Silicon Motion）一道投放市场。</p>   
</div>
            