
---
title: "Facebook正持续研究BOLT'ing以提高Linux内核执行性能"
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0925/486e4433287a9d3.jpg'
author: cnBeta
comments: false
date: Sat, 25 Sep 2021 14:40:27 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0925/486e4433287a9d3.jpg'
---

<div>   
几年来，Facebook的工程师们一直在研究BOLT，作为一种加速Linux/ELF二进制文件运行的方法。这个"二进制优化和布局工具"能够在分析后重新排列可执行文件，以产生比编译器的LTO和PGO优化所能达到的更好的性能，BOLT的最新工作之一是优化Linux内核。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0925/486e4433287a9d3.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>与允许对Linux内核进行轮廓引导优化（PGO）的挑战类似，BOLT'ing Linux内核也面临着类似的复杂障碍，这些障碍围绕着对内核的相关工作负载进行适当的轮廓分析/取样优化、内核的庞大代码库、模块与核心内核代码等，而现有的BOLT重点只是优化ELF应用可执行文件。在本周的Linux Plumbers会议上，有人谈到了BOLT'ing内核。</p><p>这是一项值得努力的工作，因为Facebook继续宣传BOLT在PGO+LTO编译器优化之上的"两位数的速度提升"。这些加速是通过优化可执行文件的代码布局来实现的，以便更有效地使用硬件页面和指令缓存。</p><p>那些对Facebook的BOLT优化工具感兴趣的开发者，或者对未来能够完全实现BOLT内核的前景感兴趣的朋友，请参阅Facebook的Maksim Panchenko的演讲（如下）和幻灯片：</p><p><a href="https://www.youtube.com/watch?v=txIgZ31-RHI" _src="https://www.youtube.com/watch?v=txIgZ31-RHI" target="_blank">https://www.youtube.com/watch?v=txIgZ31-RHI</a><br></p><p>BOLT代码本身正继续在GitHub上进行开源和开发：</p><p><a href="https://github.com/facebookincubator/BOLT" _src="https://github.com/facebookincubator/BOLT" target="_blank">https://github.com/facebookincubator/BOLT</a><br></p>   
</div>
            