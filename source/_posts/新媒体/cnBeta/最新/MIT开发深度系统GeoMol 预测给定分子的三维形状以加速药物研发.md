
---
title: 'MIT开发深度系统GeoMol 预测给定分子的三维形状以加速药物研发'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1213/8a381763322f81b.jpg'
author: cnBeta
comments: false
date: Mon, 13 Dec 2021 06:22:07 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1213/8a381763322f81b.jpg'
---

<div>   
在寻求有效新药的过程中，通常科学家希望找到能附着于致病蛋白质并改变其功能的类药分子。其中至关重要的是，他们要知道一个分子的三维形状，以了解它将如何附着在蛋白质的特定表面。<a href="https://arxiv.org/abs/2106.07802" target="_blank"><strong>近日麻省理工学院（MIT）的研究人员开发了一种深度学习模型</strong></a><strong>，可以在给定分子结构的二维图形后迅速预测其可能的三维形状。这项技术可以加速药物发现。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1213/8a381763322f81b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1213/8a381763322f81b.jpg" alt="1xq9o23h.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在实际探索过程中，一个分子可以以数千种不同的方式折叠，因此通过实验解决这一难题是一个耗时且昂贵的过程，就像在分子干草堆中寻找一根针。麻省理工学院的研究人员正在使用机器学习来简化这项复杂的任务。他们创建了一个深度学习模型，仅根据分子结构的二维图形就能预测分子的三维形状。分子通常被表示为小图形。</p><p style="text-align: left;">他们的系统 GeoMol 只需几秒钟就能处理分子，并且比其他机器学习模型，包括一些商业方法表现得更好。计算机科学与人工智能实验室（CSAIL）的博士后、该论文的共同第一作者 Octavian-Eugen Ganea 说，GeoMol可以帮助制药公司加快药物发现过程，缩小他们需要在实验室实验中测试的分子数量。</p><p style="text-align: left;">化学工程系的研究生、该论文的共同第一作者 Lagnajit Pattanaik 说：“当你在考虑这些结构如何在三维空间移动时，实际上只有分子的某些部分是灵活的，这些可旋转的键。我们工作的关键创新之一是，我们考虑像化学工程师那样对构象灵活性进行建模。这实际上是在试图预测结构中可旋转键的潜在分布”。</p><p style="text-align: left;">GeoMol 利用了深度学习中的一个最新工具，即消息传递神经网络，它是专门为在图上操作而设计的。研究人员调整了消息传递神经网络，以预测分子几何的特定元素。给定一个分子图，GeoMol最初预测原子之间的化学键的长度和这些单个键的角度。原子的排列和连接方式决定了哪些键可以旋转。</p><p style="text-align: left;">然后，GeoMol 单独预测每个原子的局部邻域的结构，并通过计算扭转角来组装相邻的可旋转键对，然后将它们对齐。扭转角决定了三个连接段的运动，在这种情况下，三个连接四个原子的化学键。</p>   
</div>
            