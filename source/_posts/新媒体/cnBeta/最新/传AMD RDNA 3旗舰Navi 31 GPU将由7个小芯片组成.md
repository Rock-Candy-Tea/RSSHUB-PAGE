
---
title: '传AMD RDNA 3旗舰Navi 31 GPU将由7个小芯片组成'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0918/bf39f8195c5ba86.jpg'
author: cnBeta
comments: false
date: Thu, 14 Apr 2022 08:24:21 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0918/bf39f8195c5ba86.jpg'
---

<div>   
对于即将推出的英伟达 GeForce RTX 4090 和 AMD Radeon RX 7900 XT 旗舰游戏显卡，<strong>有着长期靠谱爆料记录的 @Kopite7kimi 和 @Greymon55，分别在 Twitter 上分享了一些最新的细节。</strong>传闻称 AMD 首款 RNDA 3 GPU 将用上具有多达 7 个小芯片的设计，这种革命性的图形架构，可充分利用各种图形、显存和 IO 芯片组件。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0918/bf39f8195c5ba86.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0918/bf39f8195c5ba86.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://wccftech.com/amd-rdna-3-navi-31-gpu-radeon-rx-7000-flagship-7-chiplet-mcm-rumor/" target="_self">WCCFTech</a>）</p><p>作为“小芯片”技术的先行者，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 已通过锐龙（Ryzen）CPU 将之带到主流消费级市场。现在，该公司又在 Radeon GPU 上做着同样的事情。</p><p>在 @Greymon55 最新发布的推文中，其声称 Radeon RX 7000 系列旗舰 GPU（Navi 31）或配备多达 7 个小芯片。</p><p>此前有消息称，AMD RDNA 3 GPU 将采用 MCM 多芯片和 Monilithic 设计，并给予台积电 6nm 和 5n 工艺节点打造。</p><p><img src="https://static.cnbetacdn.com/article/2022/0414/ec0dca15b9635f2.png" alt="2.png" referrerpolicy="no-referrer"></p><p>至于 Navi 31 这款旗舰 GPU，推测它会用上两个基于 5nm 工艺节点的 GCD 集群、四个基于 6nm 工艺节点的 MCD 模块、以及一个同样基于 6nm 工艺节点的 IO 芯片。</p><p>GCD 是 RDNA 3 GPU 中的主要“图形计算芯片”，而 MCD 可视作“内存复合 / 多缓存芯片”，后者与 Infinity Cache 无限缓存和显存控制器密切相关。</p><p>此外 IO 芯片将由媒体引擎和芯片的其它 IO 层组成，目前尚不清楚 MCD 是否会用上片上 3D 堆叠工艺、还是单独依靠于中介层。</p><p><a href="https://static.cnbetacdn.com/article/2022/0414/e6226c4bdb8eb9a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0414/e6226c4bdb8eb9a.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">RX 7900 XT 图块示例（图自：Olrak）</p><p>此前，AMD 已披露会在基于 RDNA 3 GPU 的新一代 Radeon RX 7000 系列显卡上弃用所谓的“计算单元”（CU）描述，转而使用 WGP“工作集群”。</p><p>上图所示的 Navi 31 GPU，就配备了两块 GCD 和一组 MCD 。每块 GCD 包含了 3 个着色器引擎（共 6 个），后者分别由 2 个着色器阵列组成（每 SE 2 个 / 每 GCD 6 个 / 总计 12 个）。</p><p>然后每个着色器阵列又分为 5 组 WGP（每 SE 10 个 / 每 GCD 30 个 / 总计 60 个），每 WGP 进一步包含了 8 个 SIMD32 + 32 个 ALU 单元（每 SA 40 个 SIMD32 / 每 SE 80 个 / 每 GCD 240 个 / 总计 480 个）。</p><p>这些 SIMD32 单元共同组成了每 GCD / 7680 个内核，总计就是 15360 个内核。</p><p><a href="https://static.cnbetacdn.com/article/2022/0414/4f006bbef5e7baa.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0414/4f006bbef5e7baa.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（截图 via <a href="https://videocardz.com/newz/next-gen-flagship-gpu-rumors-nvidia-ada-ga102-with-21-gbps-memory-amds-rdna3-navi-31-with-7-chiplets-intel-battlemage-with-20480-cores" target="_self">VideoCardz</a>）</p><p>Navi 31（RNDA 3）的两组 MCD，还使用了下一代 Infinity Fabric 互连，辅以 256-512 MB 的 Infinity Cache 。</p><p>每个 GPU 还具有 4 路 @ 32-bit 内存连接链路（memory connect links），如果一张显卡标注具有 256-bit 显存位宽，那它合计就有 8 路 @ 32-bit 控制器。</p><p><img src="https://static.cnbetacdn.com/article/2022/0414/53f3fddd6e64883.png" alt="5.png" referrerpolicy="no-referrer"></p><p>不过更让人感到激动的，还是有传闻称 RDNA 3 GPU 将在光栅化性能方面超越英伟达竞品。</p><p>而绿厂这边据说也会迅速过渡到 MCM GPU 设计，从而带来 3+ 倍于 Ampere GPU 的性能。</p>   
</div>
            