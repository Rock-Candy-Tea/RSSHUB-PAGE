
---
title: 'PCIe Gen 5.0显卡满载600W 但ATX 3.0电源需应对1800W瞬时功率'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0420/09bf4eeddf9fd4a.jpg'
author: cnBeta
comments: false
date: Wed, 20 Apr 2022 08:37:09 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0420/09bf4eeddf9fd4a.jpg'
---

<div>   
早在英伟达 GeForce RTX 30 系列台式机显卡上市初期，就有技术大佬（FCPowerUp）分析过新一代显卡的瞬时功率可能超越市售电源的冗余设计，结果导致系统变得不太稳定。后来通过英伟达的驱动 / BIOS 优化，情况似乎已经能够控制在显卡厂商的推荐电源功耗范围内。<strong>不过随着行业向 PCIe Gen 5.0 发展，最高可达 1800W 的“功率偏移”，再次让我们感到有些头疼。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0420/09bf4eeddf9fd4a.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">资料图（来自：Seasonic）</p><p>近日，<a href="https://www.pcworld.com/article/631851/atx-3-0-explained-why-intel-gave-power-supplies-their-first-overhaul-in-20-years.html" target="_self">PCWorld</a> 发表了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>平台电源专家 Stephen Eastman 的专访文章，就大家甚是关心的全新 ATX 3.0 电源标准进行了答疑 —— 尤其是用于下一代显卡等设备的 PCIe Gen 5 12VHPWR 连接器。</p><p>据 PCI-SIG 所述，PCIe Gen 5.0 将允许显卡飙到三倍峰值功率。以标称 450W TGP 的英伟达 GeForce RTX 3090 Ti 为例，这意味着 ATX 3.0 电源将能够承受 1350W 的功率激增。</p><p>此外有报道称，下一代 GPU 甚至可能达到单卡 600W，这样就意味着 ATX 3.0 电源厂商需要承受高达 1800W 的峰值功率。</p><p><img src="https://static.cnbetacdn.com/article/2022/0420/dd8c3db4209bbd3.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">新一代显卡将揭开更多不敢实瓦标注的电源厂商的遮羞布</p><p>从电路设计和硬件成本上来考量（比如堆砌更多的电容），这几乎是逼着厂商去“反向虚标”。</p><p>即使瞬时功耗通常最多只会持续 100 μs，后劲不足的电源还是很可能导致系统崩溃、或触发掉电保护。</p><p>据英特尔预估，适当设计的 ATX 3.0 电源供应器，应该能够轻松应对一张功耗 300W 的显卡。</p><p><img src="https://static.cnbetacdn.com/article/2022/0420/577480e5309aefa.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">老款 ATX 2.X 电源或需 1100W 才能稳定带动相同的 300W GPU</p><p>加上为机箱内其它硬件预留的 150W 功率，想要充分发挥 CPU 性能的 PC DIY 玩家，或许得实打实的 750W 电源起步了。</p><p>对于主流玩家和普通 PC 用户来说，遵循 ATX 3.0 标准标注的电源，或许不会与旧 ATX 2.X 在除 GPU 之外的输出能力上没有太大的差别。</p><p><a href="https://static.cnbetacdn.com/article/2022/0420/c26f9ccb7595311.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/c26f9ccb7595311.png" alt="3-2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（截图 via <a href="https://wccftech.com/atx-3-0-power-supply-standard-pcie-gen-5-0-up-to-1800w-power-excursions-next-gen-graphics-cards/" target="_self">WCCFTech</a>）</p><p>但是为了带动高性能显卡，你不大可能会选择“头重脚轻”的配置。如果升级了 600W 的 GPU，那就意味着你可能需要至少 1600W 的 ATX 2.X 电源，以缓和峰值功率偏移。</p><p>即使勉强还是够用，但在峰值功率持续不足的情况下，GPU 的性能发挥还是会受到制约、更何况长期“小马拉大车”可能导致硬件出现暗病损伤，那样就得不偿失了。</p>   
</div>
            