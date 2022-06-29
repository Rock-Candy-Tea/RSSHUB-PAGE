
---
title: '苹果M2设备的Linux起步工作取得了良好进展'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0607/8518eb60ee18401.webp'
author: cnBeta
comments: false
date: Wed, 29 Jun 2022 05:56:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0607/8518eb60ee18401.webp'
---

<div>   
Hector Martin 领导的 Asahi Linux 团队，一直在努力将 Apple Silicon 拉入 Linux 生态。<strong>最近他收到了一台 13 英寸的 2022 款 MacBook Pro，并开始着手为 M2 带来 Linux 支持。</strong>虽然本周才刚起步，但幸运的是，为 M1 编写的大部分 Linux 代码，都可在 M2 上无缝运行。当然，要让 M2 Mac 完美运行 Linux，还得再编写一些新的驱动程序。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0607/8518eb60ee18401.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://github.com/AsahiLinux/docs/wiki/Feature-Support" target="_self">Asahi Linux</a> / <a href="https://github.com/AsahiLinux/linux/tree/t8112/bringup" target="_self">GitHub</a>）</p><p>本月早些时候，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>发布了采用 M2 SoC 的 2022 款 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmac%2F" target="_blank">MacBook</a> Air / MacBook Pro 机型。</p><p>M2 定制芯片采用了 8 核 CPU + 最多 10 核 GPU 的设计，性能分别较 M1 提升 18% 和 35% 。</p><p>此外得益于对最高 24GB LPDDR5 统一内存的支持，内存带宽也增加了 50% 。</p><p><a href="https://static.cnbetacdn.com/article/2022/0629/5591418efd13025.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0629/5591418efd13025.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a></p><p>Hector Martin 周一开始了 Linux M2 启动工作，通过逆向工程和内核破解调试，其确认 NVMe、USB 和 SMC 等功能可无缝启用。</p><p><a href="https://static.cnbetacdn.com/article/2022/0629/c00c254a153929f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0629/c00c254a153929f.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">初次尝试（图自：Hector Martin）</p><p>遗憾的是，苹果 M2 新机需要单独准备键盘和触控板驱动程序，此外 SPMI 和 PCIe 支持也需要 <a href="https://github.com/AsahiLinux/m1n1" target="_self">m1n1</a> 代码中的 fusemap 来完成初始化操作。</p><p><img src="https://static.cnbetacdn.com/article/2022/0629/260b4bcabedbd90.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">NVMe 与 SMC 工作正常（警告文字可忽略）</p><p>目前还有 PCIe、PMU、雷雳（Thunderbolt）和 DP-Alt Mode 等尚未解决的问题，且 Apple Silicon 图形支持工作也需要进一步深入。</p><p><img src="https://static.cnbetacdn.com/article/2022/0629/6077dd941a5bf22.png" alt="5.png" referrerpolicy="no-referrer"></p><p>此前他们已经展示了首个由开源兼容驱动渲染的三角形，但仍需几个月去打造功能完备的 Gallium3D OpenGL 和上游 DRM / KMS 内核驱动程序。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1277175.htm" target="_blank">Asahi Linux展示三角形渲染以庆祝苹果M1开源兼容驱动的出现</a></p></div>   
</div>
            