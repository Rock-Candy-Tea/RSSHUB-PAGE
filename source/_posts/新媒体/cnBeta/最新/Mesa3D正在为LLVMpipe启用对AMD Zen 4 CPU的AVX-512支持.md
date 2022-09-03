
---
title: 'Mesa3D正在为LLVMpipe启用对AMD Zen 4 CPU的AVX-512支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0831/87b763b23e769ce.webp'
author: cnBeta
comments: false
date: Sat, 03 Sep 2022 08:50:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0831/87b763b23e769ce.webp'
---

<div>   
<strong>作为 Mesa3D 图形项目的独立贡献者，Yonggang Luo 已开始着手为 LLVMpipe 启用 AVX-512 支持。</strong>至于这么做的原因，主要是 AMD 在 Zen 4 锐龙 7000 系列台式处理器上引入了 AVX-512 指令集。通过驱动方面的优化，Luo 希望为 R9-7950X 等 CPU 带来最佳性能增益。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0831/87b763b23e769ce.webp" alt="62gh122o.webp" referrerpolicy="no-referrer"></p><p>有趣的是，尽管 Intel 多年来一直在力推 AVX-512，但在 12 代酷睿台式处理器身上，该公司还是通过后续的微码更新而禁用了这项高能耗特性。</p><p>出乎意料的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 却选择了在 Zen 4 锐龙 7000 系列台式处理器上提供了 AVX-512 指令集。</p><blockquote><p>至于 LLVMpipie，则是一种独特的 Mesa OpenGL 软解方案。当计算机系统找不到显卡硬件 / GPU 驱动程序时，就可选择基于 CPU 软解的 LLVMpipe 方案。</p><p>不过相较于锐龙 7000 集成的 RNDA 2 核显，软解的优势显然不会如预期那般显著 —— 即便 AMD 用的是 256-bit（而不是 512-bit）路径。</p></blockquote><p>据悉，LLVM 是“用于为任何编程语言创建前端、并为任何指令集架构创建后端的编译器 / 工具链技术的一个集合”。</p><p>LLVMpipe 将允许 LLVM 使用一组特定的扩展，并提供较其它软件软件（比如 Softpipe / OpenGL）的可执行文件更高的性能。</p><p><img src="https://static.cnbetacdn.com/article/2022/0903/2a5bf965a00b720.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/17813" target="_self">FreeDesktop</a>）</p><p>目前尚不清楚 AVX-512 可在 AMD Zen 4 新架构上提供多高的性能，此外本次合并请求中包含了一个被称“GALLIUM_OVERRIDE_CPU_CAPS”的环境变量。</p><p>该变量能够在 Softpipie 和 LLVMpipe 中覆盖 CPU 功能，以禁用或启用 AVX、SSE 和其它指令集功能。</p><p>最后，“LP_NATIVE_VECTOR_WIDTH”将允许更改向量位宽，以在 LLVMpipe 中使用 AVX、AVX2、或 AVX-512 。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1309627.htm" target="_blank">AMD Zen4 16核锐龙9 7950X出现 支持AVX-512</a></p><p><a href="https://www.cnbeta.com/articles/tech/1310701.htm" target="_blank">锐龙7000被指AVX512不满血：Intel 6年前的14nm就做到了</a></p></div>   
</div>
            