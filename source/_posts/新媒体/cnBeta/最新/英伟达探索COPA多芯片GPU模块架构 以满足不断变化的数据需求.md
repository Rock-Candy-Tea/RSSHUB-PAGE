
---
title: '英伟达探索COPA多芯片GPU模块架构 以满足不断变化的数据需求'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0110/4962f88218c464b.png'
author: cnBeta
comments: false
date: Mon, 10 Jan 2022 05:08:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0110/4962f88218c464b.png'
---

<div>   
当前的深度学习应用，正收到复杂性增长、资源需求多样化、以及现有硬件架构的限制。<strong>不过近日，英伟达研究人员发表了一篇技术文章，概述了该公司对多芯片模块（MCM）的探索。</strong>具体说来是，该团队讲述了“可组合封装”（COPA）GPU 的各项优势，尤其是能够适应各种类型的深度学习工作负载。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0110/4962f88218c464b.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">资料图（via Nvidia 官网）</p><p>得益于固有的功能和优化，图形处理单元（GPU）已成为大量深度学习（DL）研究项目的首选。但由于传统融合 GPU 解决方案正迅速变得不太实用，研究人员才想到到 COPA-GPU 的理念。</p><p>这些融合 GPU 解决方案依赖于由传统芯片组成的架构，辅以高带宽内存（HBM）、张量核心（NVIDIA）/ 矩阵核心（Matrix Cores）、光线追踪（RT）等专用硬件的结合。</p><p>此类硬件或在某些任务下非常合适，但在面对其它情况时却效率低下。与当前将所有特定执行组件和缓存组合到一个包中的单片 GPU 设计不同，COPA-GPU 架构具有混合 / 匹配多个硬件块的能力。</p><p>如此一来，它就能够更好地适应当今高性能计算（HPC）只能够呈现的动态工作负载、以及深度学习（DL）环境。</p><p><a href="https://static.cnbetacdn.com/article/2022/0110/e3279d82c882b4f.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0110/e3279d82c882b4f.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：ACM.org | <a href="https://dl.acm.org/doi/pdf/10.1145/3484505" target="_self">PDF</a>）</p><p>这种整合更多功能和适应多种类型工作负载的能力，可带来更高水平的 GPU 重用。更重要的是，对于数据科学家们来说，这使得他们更有能力利用现有资源，来突破潜在的界限。</p><p>尽管经常混为一谈，但人工智能（AI）、机器学习（ML）和深度学习的概念，却有着明显的区别。DL 可视作 AI 和 ML 的子集，主要通过各种过滤器来预测和分类信息，来模拟人脑的信息处理方式。</p><p>作为诸多自动化 AI 功能背后的技术支撑，深度学习可助力其实现各项功能 —— 涵盖从自动驾驶、到监控金融系统的欺诈活动等领域。</p><p>另一方面，MCM 概念已于过去几年被炒得火热（其实可追溯到 70~80 年代的 IBM 气泡内存 / 3081 大型机），且 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 等厂商早已将小芯片 / 芯片堆叠技术作为其下一代产品的重要演变。</p>   
</div>
            