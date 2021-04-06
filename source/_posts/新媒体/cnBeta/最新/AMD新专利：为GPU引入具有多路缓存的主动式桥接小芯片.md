
---
title: 'AMD新专利：为GPU引入具有多路缓存的主动式桥接小芯片'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0406/fe835dae31083e8.png'
author: cnBeta
comments: false
date: Tue, 06 Apr 2021 03:51:27 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0406/fe835dae31083e8.png'
---

<div>   
<strong>近日曝光的一项新专利表明，在 CPU 领域成功运用小芯片设计之后，AMD 还有望在即将到来的 RDNA 3 GPU 架构上落实同样的设计理念。</strong>Videocardz 指出，专利中描绘了集成有缓存的主动式桥接小芯片，且适用于多个小芯片的设计，能够在多个 GPU 核心之间架起沟通达到桥梁。展望未来，我们或在基于 RNDA 3 GPU 的独显或 APU 产品线上见到它的身影。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0406/fe835dae31083e8.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/fe835dae31083e8.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">AMD Big Navi RDNA 2 GPU 资料图</p><p>WCCFTech 指出，除了 AMD，竞争对手英伟达也有在考虑为下一代 GPU 引入 MCM 设计。</p><p><a href="https://static.cnbetacdn.com/article/2021/0406/1458a7244dcc953.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/1458a7244dcc953.png" alt="0.png" referrerpolicy="no-referrer"></a></p><p>在芯片制程工艺的缩进越来越困难的情况下，类似 CPU 的多芯片封装，显然也会成为 GPU 的下一个发展方向。</p><p><a href="https://static.cnbetacdn.com/article/2021/0406/ca40c51a1c567ab.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/ca40c51a1c567ab.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>与多年前的 CrossFire 多卡交火方案相比，基于主动式桥接小芯片的 GPU 设计方案，能够通过编程来实现更加灵活高效的产品与性能组合。</p><p><a href="https://static.cnbetacdn.com/article/2021/0406/ab5fd09dd1abc03.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/ab5fd09dd1abc03.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>由 AMD 在概念设计框图中所展示的内容可知，CPU 能够通过 Infinity Fabric 通信总线连接到 GPU 上的第一个小芯片，而后者又可负责与其它 n 个 GPU 小芯片的沟通。</p><p><img src="https://static.cnbetacdn.com/article/2021/0406/8172149e14bb0cb.png" alt="3.png" referrerpolicy="no-referrer"></p><p>有趣的是，我们还在小桥接芯片上见到了 L3 LLC 缓存。其具有一致且统一的规格，旨在减少缓存瓶颈。</p><p><a href="https://static.cnbetacdn.com/article/2021/0406/1b8f7c91b3a4d09.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/1b8f7c91b3a4d09.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p>从开发角度上来说，这么做使得 AMD 能够沿用现有的编程模型，并减少为每个 GPU 小芯片配备单独的 L3 缓存的需求。</p><p><a href="https://static.cnbetacdn.com/article/2021/0406/bb01e5308efd7ea.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/bb01e5308efd7ea.png" alt="5.png" referrerpolicy="no-referrer"></a></p><p>由于框图主要描述的是 SoC 的整体细节，因而我们尚不清楚有关 GPU 主动式小芯片设计的更多细节。</p><p><a href="https://static.cnbetacdn.com/article/2021/0406/6612bd339cb18ec.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0406/6612bd339cb18ec.png" alt="6.png" referrerpolicy="no-referrer"></a></p><p>但从理论上来说，RDNA 3 架构显然可以灵活地应用于独显和 APU 等台式机 / 移动 / 主机 / 甚至未来的高性能计算（HPC）等平台上（比如 Radeon Instinct GPU 加速卡）。</p>   
</div>
            