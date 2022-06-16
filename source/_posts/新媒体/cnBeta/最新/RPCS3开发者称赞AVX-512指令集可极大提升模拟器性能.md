
---
title: 'RPCS3开发者称赞AVX-512指令集可极大提升模拟器性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0616/e48629bcc991349.jpg'
author: cnBeta
comments: false
date: Thu, 16 Jun 2022 06:59:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0616/e48629bcc991349.jpg'
---

<div>   
<strong>RPCS3“PlayStation 3 模拟器”开发者，刚刚在一篇冗长的博客文章中，详细介绍了 AVX2 指令集可带来的仿真性能提升。</strong>Whatcookie 指出：与传统软解方案相比，现代 CPU 上的 AVX-512 能够带来高达 30% 的领先优势。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0616/e48629bcc991349.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Whatcookie <a href="https://whatcookie.github.io/posts/why-is-avx-512-useful-for-rpcs3/" target="_self">Blog</a>，via <a href="https://wccftech.com/avx-512-rpcs3-playstation-3-emulator-do-wonders-together-30-performance-boost-over-cpus-with-avx2/" target="_self">WCCFTech</a>）</p><p><strong>可知 AVX-512 的优势，主要体现在：</strong></p><blockquote><p>● 更大的寄存器文件</p><p>● 为旧指令带来新的形式</p><p>● 屏蔽寄存器（mask registers）</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0616/706f55c13264cc4.png" alt="2.png" referrerpolicy="no-referrer"></p><p>作为最受玩家欢迎的 PS3 模拟器之一，RPCS3 开发团队在 Intel 酷睿 i9-12900K 平台上展开了测试。其频率设置为默认的 5.2 GHz，并且启用了 AVX-512 。</p><p>结果发现，如果使用标准的  SSE2 指令集，模拟器的帧率只能达到 5 FPS 。若迁移至 SSE 4.1 指令集，则可带来 160 FPS 的巨大增益。</p><p>显然，缺少对 PS3 模拟器至关重要的 SSE3 指令集，将对其性能产生极大的制约。</p><p><a href="https://static.cnbetacdn.com/article/2022/0616/623a41a51d47293.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0616/623a41a51d47293.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>如果迁移到 AVX2 / FMA，可获得额外的 13% 性能提升。而从 AVX2 切换到 AVX-512，更是可以获得 30% 的性能提升（帧率达到 242 FPS）。</p><blockquote><p>● 此外 SSE 4.1 的目标平均帧率有 160 FPS，而 AVX2 / FMA 为 190 FPS —— 较前者提升 18% 。</p><p>● AVX2 在 SSE 4.1 上没有包含多少新指令，但确实提供了一套新颖的 3 操作数形式指令 —— 免去了大量的寄存器间 mov 指令。</p><p>● 更重要的是，所有支持 AVX2 的 CPU，也都支持 FMA 指令。</p></blockquote><p>FMA 指令不仅比乘法 + 加法指令链更快，且由于在它们之间没有四舍五入到单精度、因而可以避免输出结果不一致的问题。</p><p>而要在缺乏 FMA 指令的情况下准确模拟，必然会增加一些额外的开销，因而原生 FMA 操作将对此大有裨益。</p><p><a href="https://static.cnbetacdn.com/article/2022/0616/9c52e1deca7ebc4.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0616/9c52e1deca7ebc4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p>Icelake 级别的 AVX-512 操作，目标平均速度达到了夸张的 235 FPS —— 较 AVX2 / FMA 领先 23% 。</p><p>鉴于 AVX-512 中新添加的指令数量如此之多，以至于其中相当多一部分都可在 RPCS3 模拟器中派上用场。</p><p>尴尬的是，为了控制消费级平台的功耗（使用率也没有那么高），<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>最终决定在 12 代 Alder Lake CPU 中移除了对 AVX-512 指令集的支持。</p><p>另一方面，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 却证实将在下一代 Zen 4 锐龙 7000 系列 CPU 上充分利用这一点。至于后续 Intel 是否会后悔这一决定，仍有待时间去检验。</p>   
</div>
            