
---
title: 'Stockfish 14 正式发布，开源国际象棋引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-127fa83113a039d87edbc66d1d31f2682f9.png'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 06:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-127fa83113a039d87edbc66d1d31f2682f9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstockfishchess.org%2Fblog%2F2021%2Fstockfish-14%2F" target="_blank">Stockfish 14</a> 已正式发布。Stockfish 是一款开源的国际象棋引擎，但它不是完整的国际象棋程序，需要 UCI 兼容的图形用户界面（例如带有 PolyGlot，Scid，Cute Chess，eboard，Arena，Sigma Chess，Shredder，Chess Partner或 Fritz 的 XBoard）才能正常地使用。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-127fa83113a039d87edbc66d1d31f2682f9.png" referrerpolicy="no-referrer"></p> 
<p>去年 9 月发布的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstockfishchess.org%2Fblog%2F2020%2Fstockfish-12%2F" target="_blank"> Stockfish 12</a> 开始支持 NNUE，此特性带来的变化是可在 CPU 上快速地运行神经网络，并且显著改进了 Stockfish，恢复了其作为现有最强大的国际象棋引擎的地位。</p> 
<p>到了最新的 14 版本，发布公告写道，Stockfish 14 的象棋等级分现在比 2016 年发布的 Stockfish 7 至少高 400 Elo。在过去五年里，Stockfish 的象棋等级分平均每年增加 80 Elo。此外，由于在定义和训练提供位置评估的高效可更新神经网络 (NNUE) 方面取得了两项重大进展，Stockfish 14 比 Stockfish 13 更准确地评估位置。</p> 
<p>首先，Stockfish 团队表示此前和 Leela Chess Zero 团队的合作已经取得了成果。LCZero 团队提供了由 Leela 评估的数十亿个位置，Stockfish 团队将这些位置与 Stockfish 评估的数十亿个位置结合起来，用于训练 NNUE 网络，为 Stockfish 14 提供支持。Stockfish 团队可以免费使用和结合这些数据集，这对取得的进展至关重要，也显示了开源和开放数据的力量。</p> 
<p>第二是 NNUE 网络的结构得到了显著的改进。新的网络不仅更大，而且更重要的是，它能更好地处理大的物质不平衡，并能为游戏的多个阶段提供专业服务。由 Gary Linscott 和 Tomasz Sobczyk 启动的一个新项目，诞生了用 Pytorch 编写的 GPU 加速网络训练器。这个工具可以在几个小时内训练出高质量的网络。</p> 
<p>最后，新版本还有一些搜索改进、小错误修复和额外的改进。例如，Stockfish 现在在短时控制下对 chess960（费舍尔随机棋）强了约 90 个 Elo。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstockfishchess.org%2Fdownload%2F" target="_blank">https://stockfishchess.org/download/</a></p>
                                        </div>
                                      
</div>
            