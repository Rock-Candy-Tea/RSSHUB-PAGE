
---
title: '国际象棋引擎Stockfish 14发布：比2016年版本增加400 Elo分'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0706/5eef086ac148aba.jpg'
author: cnBeta
comments: false
date: Tue, 06 Jul 2021 02:59:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0706/5eef086ac148aba.jpg'
---

<div>   
Stockfish 14 日前正式发布，开发者表示比此前版本要强很多。在<a href="https://tests.stockfishchess.org/tests/view/60dae5363beab81350aca077" target="_blank">超过 6 万场比赛</a>中，新版本赢得了其中的 7500 场，输掉了 2300 场，此外还有 50000 场比赛以平局告终。<a href="https://stockfishchess.org/blog/2021/stockfish-14/" target="_blank">目前新版本已经在 Stockfish 官网开放下载</a>。<br>
<p>下载：<a href="https://stockfishchess.org/download/">stockfishchess.org/download</a>.</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0706/5eef086ac148aba.jpg" alt="k2sv0aqs.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">开发者预估平均每年增加了 80 分国际象棋等级分（Elo 分）。相比较 2016 年推出的 Stockfish 7，现在推出的 Stockfish 14 至少增强了 400 分。相比较上个版本，Stockfish 14 能够更加精准的评估未知，这是因为在定义和训练提供位置评估的高效可更新的神经网络（NNUE）方面取得了两个重大进展。</p><p style="text-align: left;">首先，开发团队之前宣布的和 Leela Chess Zero 团队的合作已经取得了成果。LCZero 团队提供了由 Leela 评估的数十亿个位置，开发团队将这些位置与 Stockfish 评估的数十亿个位置结合起来，训练 NNUE 网络，为 Stockfish 14 提供支持。开发团队可以免费使用和结合这些数据集，这对取得的进展至关重要，也显示了开源和开放数据的力量。</p><p style="text-align: left;">第二是 NNUE 网络的结构得到了显著的改进。新的网络不仅更大，而且更重要的是，它能更好地处理大的物质不平衡，并能专门用于游戏的多个阶段。由 Gary Linscott 和 Tomasz Sobczyk 启动的一个新项目，导致了用 pytorch 编写的 GPU 加速网络训练器。这个工具可以在几个小时内训练出高质量的网络。</p><p style="text-align: left;">最后，新版本还有一些搜索改进、小错误修复和额外的改进。例如，Stockfish现在在短时控制下对 chess960（费舍尔随机棋）强了约 90 个 Elo。</p><p style="text-align: left;"><strong>关于 Stockfish</strong></p><p style="text-align: left;">Stockfish是源自Glaurung 2.1的免费，强大的UCI国际象棋引擎。Stockfish不是完整的国际象棋程序，需要UCI兼容的图形用户界面（GUI）（例如带有PolyGlot，Scid，Cute Chess，eboard，Arena，Sigma Chess，Shredder，Chess Partner或Fritz的XBoard）才能舒适地使用。阅读所选GUI的文档，以获取有关如何与Stockfish一起使用的信息。</p><p style="text-align: left;">Stockfish引擎具有两个国际象棋评估功能，即基于手工术语的经典评估和基于可有效更新的神经网络的NNUE评估。经典评估几乎可以在所有CPU架构上高效运行，而NNUE评估得益于大多数CPU（sse2，avx2，neon或类似CPU）可用的向量内在函数。</p>   
</div>
            