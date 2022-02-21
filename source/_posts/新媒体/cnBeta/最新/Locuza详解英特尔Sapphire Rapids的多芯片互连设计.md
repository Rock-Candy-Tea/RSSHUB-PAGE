
---
title: 'Locuza详解英特尔Sapphire Rapids的多芯片互连设计'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0221/bf36d9d47f87f7f.jpg'
author: cnBeta
comments: false
date: Mon, 21 Feb 2022 08:52:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0221/bf36d9d47f87f7f.jpg'
---

<div>   
<strong>英特尔即将推出代号为“Sapphire Rapids”的企业级至强可扩展处理器，且其核心数有望高达 60 。</strong>有趣的是，在 ISSCC 2022 的演示文稿中，英特尔已分享过分辨立案率的芯片图。可知如此多的核心，是通过 EMIB 互连的四个裸片实现的。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0221/bf36d9d47f87f7f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0221/bf36d9d47f87f7f.jpg" alt="1-1.jpg" referrerpolicy="no-referrer"></a></p><p>不过为了帮助大家更好的了解其功能结构，热心的 @Locuza 等网友，还是认真地给原图添加了详细的注释。</p><p>可知 Sapphire Rapids 芯片中的每四个 Tile，都是一组成熟的多核处理器，包含了 CPU 内核、集成的北桥、内存、PCIe 接口，以及平台所需的其它 IO 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0221/1a366e0ccdf9f20.png" alt="1.png" referrerpolicy="no-referrer"></p><p>而将 4-Tiles 结合到一起的，则是一共五组 EMIB 桥接器。这使得裸片中的 CPU 内核能够透明地访问 I/O，以及透明地控制任何其它裸片的存储。</p><p>从逻辑上来讲，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Sapphire Rapids 与竞争对手 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 的 Naples 大同小异，后者使用了 Infinity Fabric over package（IFOP）来互连四组 8 核心的 Zeppelin 芯片。</p><p><a href="https://static.cnbetacdn.com/article/2022/0221/aff7f6a7033ae61.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0221/aff7f6a7033ae61.jpg" alt="1-2.jpg" referrerpolicy="no-referrer"></a></p><p>不过这里的努力，似乎是为了最大限度地减少一种封装互连，转向基于硅桥的高带宽、低延迟方案，且它们之间有着高密度的微观布线（类似于中介层）。</p><p>每个芯片的平面图，和过去几代的英特尔企业级处理器也非常相似。该公司擅长使用 Mesh 互连，并将各种 IP 块放置在环形总线的网格中。</p><p><a href="https://static.cnbetacdn.com/article/2022/0221/c17b1107fa6d795.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0221/c17b1107fa6d795.jpg" alt="2-1.jpg" referrerpolicy="no-referrer"></a></p><p>网状网络是环形总线和全点对点互连的中间地带，网格中的每个单独组件都可称作瓦片（Tile）。</p><p>每 Tile 集成了 15 个 Golden Cove 高性能 CPU 核心（P 核），辅以 2MB L2 专用缓存 + 1.875MB 的末级缓存切片，而 28.125MB 的 L3 缓存则由 60 个核心所共享（总缓存达到 112.5 MB）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0221/bb626bba4ff925a.png" alt="2.png" referrerpolicy="no-referrer"></p><p>每个芯片还具有一个内存控制器块，带有 128-bit DDR5 物理层（包含 ECC 就是 160-bit）。该接口可控制双 DDR5 通道，相当于四组 @ 40-bit 子通道。</p><p>封装中共支持 8 个 DDR5 通道（16 个子通道），且 Sapphire Rapids 的 PCIe / CXL 接口规模异常庞大，每个裸片都有一个 PCI-Express Gen 5 + CXL 1.1 根复合体（具有 32 个通道 / 128 条 PCIe 5.0 或 CXL 1.1 通道）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0221/4284f9b5bbed60a.jpg" alt="2-2.jpg" referrerpolicy="no-referrer"></p><p>至于加速器瓦片，则包含了英特尔的数据流加速器（DSA）、快速辅助技术（QAT）、以及 DLBoost 2.0（可用于加速深度学习神经网络构建和训练的硬件组件）。</p><p>最后一块瓦片包含了 24x UPI 连接，可用于插槽之间的互连。四组核心中都包含了这个，意味着 Sapphire Rapids 芯片最可组建 8 路计算平台。</p>   
</div>
            