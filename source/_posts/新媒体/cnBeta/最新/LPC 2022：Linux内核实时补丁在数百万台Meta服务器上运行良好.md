
---
title: 'LPC 2022：Linux内核实时补丁在数百万台Meta服务器上运行良好'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0916/e77395a961c21f1.jpg'
author: cnBeta
comments: false
date: Fri, 16 Sep 2022 09:37:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0916/e77395a961c21f1.jpg'
---

<div>   
<strong>在本周的 LPC 2022 大会上，Meta / Facebook 披露旗下的数百万台服务器，已转向使用 Red Hat 的 Kpatch 内核实时补丁（KLP）解决方案。</strong>同时 Meta 工程师分享了他们在这项实时补丁基础设施上取得的成功，以及在此过程中遇到的麻烦。可知与大多数组织一样，这项转进旨在减少内核更新导致的服务器停机时间 —— 尤其是无止境的安全更新流程。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0916/e77395a961c21f1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://www.phoronix.com/news/Meta-Linux-Kernel-Live-Patching" target="_self">Phoronix</a>）</p><p>熟悉服务器应用场景的朋友，一定不会对冗长的开机自检（POST）和完全重启所需的时间感到陌生。</p><p>而通过引入内核实时修补方案，当一切按计划进行时，服务器将能够实现近乎无缝的新内核迁移。</p><blockquote><p>具体说来是，livepatching 允许内核函数在运行时安全地实施就地修补。</p><p>而除了内核基础设施，Meta 还选用了 Red Hat 的 Kpatch 解决方案。</p><p>同时 SUSE 有在持续维护 kGraft，Oracle 也有提供 Ksplice 方案。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0916/f0008844cc7e1e4.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>不过在针对数百万台服务器的 Linux 实时补丁试验过程中，Meta 工程师们也追踪记录了需要克服的一些问题（比如性能方面）。</p><p>报告的内容，主要涉及在实时修补更高的 I/O、fsync 延迟、以及 TCP 重传率期间，可能出现持续 1~2 秒的问题。</p><p>Meta 工程师们一直在努力应对极端状况，尤其是更好地处理 Clang 编译的 PGO 优化内核构建等方面、以及其它有助于提升稳健性的项目。</p><p>最后，对 Meta 大规模内核修补工作感到好奇的朋友，可移步查看 LPC 2022 大会的幻灯片和完整视频记录。</p>   
</div>
            