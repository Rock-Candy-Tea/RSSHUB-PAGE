
---
title: '英特尔发布适用于现代CPU的快速AV1视频编解码器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0331/7b755ad6bcfed0b.webp'
author: cnBeta
comments: false
date: Sat, 23 Apr 2022 06:52:52 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0331/7b755ad6bcfed0b.webp'
---

<div>   
作为开放媒体联盟（AOMedia）的创始成员之一，英特尔在推广 AV1 编解码器、并使其更容易被内容创作者 / 提供商和最终用户访问方面，开展了相当多的工作。早在 2020 年，该公司就已通过 Xe-LP GPU 引入对 AV1 硬件编码的支持。<strong>本周，这家芯片巨头又发布了适用于所有现代 CPU 的 1.0 版 SVT-AV1 编解码器。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0331/7b755ad6bcfed0b.webp" referrerpolicy="no-referrer"></p><p>据悉，AV1 开源视频编解码器专为超高清分辨率、宽色域和高动态范围的增强体验而设计。早在 2018 年，AOMedia 就宣称 AV1 效率较现有编解码器提升 30%（尤其针对 H.265 / HEVC 的类似 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>+ 内容设计）。</p><p>不过高效编解码器的一个问题，就是相当高的资源开销、且通常需要依赖于硬件加速才能正常工作。与此同时，现代 CPU 拥有大量资源和可用于编解码的新指令集，这正是英特尔 SVT-AV1 可以派上用场的地方。</p><p>英特尔指出，SVT-AV1 是一个可扩展的、且与标准无关的编解码器库，可充分发挥现代 CPU / AVX2 指令的多线程性能。</p><p><img src="https://static.cnbetacdn.com/article/2022/0331/b102c6a511a862e.webp" referrerpolicy="no-referrer"></p><p>此外 Phoronix 指出，SVT-A11 提供了针对 AVX2 的进一步优化，可带来性能和图像质量改进、更多预设级别的快速解码、以及 S 帧支持。</p><p>无论你的现代 x86 计算机运行的是<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a> macOS、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>、还是开源的 Linux 操作系统，新编解码器都可以在英特尔 5 代酷睿（Broadwell 及以上）处理器上良好支持。</p><p>起初英特尔与流媒体平台 Netflix 启动了 SVT-AV1 项目，验证了 AV1 编解码器能够适用于从优质视频点播、到实时编 / 转码的各种应用场景。</p><p><img src="https://static.cnbetacdn.com/article/2022/0423/2c9752fbc5e4ab3.jpg" referrerpolicy="no-referrer"></p><p>2020 年 8 月，SVT-AV1 编 / 解码库正式被 AOMedia 旗下的软件实施工作组（SIWG）所采纳，对其后续流行起到了极大的助推作用。</p><p>现在，随着 SVT-AV1 1.0 版 CPU 编解码库的发布，意味着 AV1 生态又跨越了一个重要的里程碑。</p><p>值得一提的是，英特尔正在为 Netflix 之类的合作伙伴提供基于 DG2 GPU 的 Arctic Sound-M 加速器，支持同时对 8 路 4K 视频流进行 AV1 硬件加速处理。</p><p><img src="https://static.cnbetacdn.com/article/2022/0423/d6209c82b788a56.jpg" referrerpolicy="no-referrer"></p><p>Intel Arctic Sound 1T 加速卡采用了单槽全高设计，热设计功耗（TDP）150W 。Arctic Sound 2T 则是双贴芯片，功耗达到了 300W（需要 8-pin 外接供电）。</p><p>前者采用的 Xe-HP GPU 具有 384 个执行单元（EU）+ 16GB 板载 HBM2E 高带宽显存，峰值带宽高达 716 GB/s（或为 HBM2E 堆栈 @ 2048-bit 位宽）。</p><p>后者采用全长全高（FLFH）外形，具有 960 EU + 32GB HBM2E 高带宽显存。</p><p><a href="https://static.cnbetacdn.com/article/2022/0423/f2375a3603f9c2b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0423/f2375a3603f9c2b.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：Igor's Lab）</p><p>与 Iris Xe 消费级 GPU 使用的 Xe-LP 相比，英特尔 Xe-HP 架构支持更多浮点格式（包括通用的 FP16 / FP32 / FP64 和用于 AI / ML 计算的 bfloat16 格式）、更多计算机专用指令、用于深度学习的 DP4A 卷积指令、以及英特尔的 XMX 扩展。</p><p>此外面向数据中心的 Xe-HPG GPU 使用了具有各种 IPC 改进的全新执行单元（EU）、支持 HBM2E 高带宽显存、并通过 Intel 性能优化的 10nm SuperFin 工艺来制造。简而言之，Xe-HP 与 Xe-LP / Xe-HPG 完全不是同类产品。</p><p>目前英特尔已向部分客户提供 1T / 2T 的 Xe-HP 计算加速卡，且去年宣布的 4T 方案甚至可提供超过 42 TFLOPs 的 FP32 性能（暂无具体出样计划）。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1253095.htm" target="_blank">英特尔Arc独显正式发布：率先支持AV1编码 比软件方案快50倍</a></p></div>   
</div>
            