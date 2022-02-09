
---
title: '英特尔开源Linux驱动更新 深入支持Vulkan ANV光追方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0107/1618a2a76b798f6.jpg'
author: cnBeta
comments: false
date: Wed, 09 Feb 2022 09:27:38 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0107/1618a2a76b798f6.jpg'
---

<div>   
虽然 ARC Alchemist DG2 独显产品线疑似上市延期，但英特尔驱动团队还是在努力优化 ARC GPU 的开源驱动和相关功能。<strong>在近日更新的版本中，我们就见到了对 VUlkan“ANV”光追方案的进一步支持。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2022/0107/1618a2a76b798f6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0107/1618a2a76b798f6.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via Intel）</p><p>长期以来，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>一直在努力为 Linux 平台上的 Vulkan 光追功能提供重要的驱动程序基础支撑。而在新版驱动程序中，其已被归档到“VK_KHR_ray_query”分支下。</p><p>去年 12 月，该公司驱动团队已经为“VK_KHR_ray_tracing_pipeline”混合了 SPIR-V 和 NIR 光线查询。现在，他们又朝着揭示 VK_KHR_ray_query 容积的方向迈进。</p><blockquote><p>据悉，SPIR-V 属于容积（capacity）、而不是内存内（in-memory）类型的创新，辅以一些合理的改进。</p><p>其主要用于将合并的着色器存储于驱动器上，并转换为其它格式（比如 NIR），以持续改进和减少单纯的 GPU 走向。</p></blockquote><p>而 VK_KHR_ray_query 光线查询的引入，则考虑到了针对所有着色器类型的光追支持 —— 具体取决于即将推出的、具有基础图形支持的 Intel ARC 独显。</p><p><img src="https://static.cnbetacdn.com/article/2022/0126/dc68db71a40cf47.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>至于 Vulkan 1.3，作为面向 3D 设计和处理的低开销、跨阶段（cross-stage）API，其已被许多重量级实时 3D 渲染应用程序所采纳（例如计算机游戏 / intelligent media）。</p><blockquote><p>与相对成熟的 OpenGL 和 Direct3D 11 API 相比，Vulkan 希望带来更高的 CPU / GPU 执行效率。</p><p>对于开发者来说，它能够为应用恒旭提供广泛的低层级 API 和平等托付（equal entrusting），有些类似于 Metal 和 Direct3D 12 。</p><p>即使 CPU 使用率较低，Vulkan 还是希望能够让设计人员更轻松地在以 CPU 为中心的不同场景下循环工作。</p></blockquote><p>在经历了超过 90 天的开发后，Mesa 22.1（一款基于 OpenGL 的主力 API）也被融入了更多的 MR 细节。</p><p><img src="https://static.cnbetacdn.com/article/2022/0209/f3b7f274a7a9459.png" alt="2.png" referrerpolicy="no-referrer"></p><p>此外它也支持 OpenGL ES、Vulkan、EGL、OpenMAX、OpenCL、VDPAU、VA-API、以及 XvMC 。</p><p><strong>以下是提供了 Mesa 22.1 驱动支持的硬件列表：</strong></p><blockquote><p>● 英特尔 GMA / HD Graphics / Iris 核显</p><p>● <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon 系列 GPU</p><p>● 英伟达 GPU，Riva TNT / Tegra K1 及后续版本。</p><p>● 高通 Adreno A2xx-A6xx</p><p>● 博通 VideoCore 4 and 5</p><p>● ARM Mali Utgard / Midgard / Bifrost</p><p>● Vivante GCxxx</p></blockquote><p>最后，Mesa 22.1 将作为此类开源 OpenGL / Vulkan Linux 驱动程序的二季度稳定更新而到来。</p>   
</div>
            