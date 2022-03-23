
---
title: 'NVIDIA阉割H100 GPU图形功能：1.8万核心砍到512核心'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0323/7263dd61a2bf6ec.png'
author: cnBeta
comments: false
date: Wed, 23 Mar 2022 08:09:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0323/7263dd61a2bf6ec.png'
---

<div>   
昨晚的GTC 2022大会上，NVIDIA正式发布了H100 GPU加速卡，也是万众期待的Hopper新架构，跳过5nm直接上了台积电4nm工艺，800亿晶体管，功耗最高可达700W，各方面性能很好很强大。完整版有8组GPC(图形处理器集群)、72组TPC(纹理处理器集群)、144组SM(流式多处理器单元)，而每组SM有128个FP32
CUDA核心，总计18432个。<br>
 <p>相比目前的Ampere GPU架构的1万个CUDA核心，<strong>Hoper的1.8万CUDA核心提升很大，但是大家不要期待H100的游戏性能了，因为NVIDIA这次一刀砍到底，阉割得非常厉害。</strong></p><p><img src="https://static.cnbetacdn.com/article/2022/0323/7263dd61a2bf6ec.png" referrerpolicy="no-referrer"></p><p>从NVIDIA的白皮书中可以确认，H100砍掉了大量GPU相关功能，不论是PCIe 5.0版还是SMX版的H100核心中，<strong>只有2组TPC单元才可以支持图形运算，包括矢量、几何及像素渲染。</strong></p><p>2组TPC单元也就是4组SM单元，总计512个CUDA核心是可以跑游戏的，相比完整的1.8万核心来说微不足道，<strong>性能只相当于完整版H100核心的1/36，也就3%左右，97%的游戏性能没了。</strong></p><p><strong>NVIDIA解释说H100是专为AI、HPC及数据分析而生的，并不是为了游戏而设计的。</strong></p><p>考虑到H100在AI、HPC等性能上的提升，NVIDIA阉割大量游戏功能以便减少设计难度也是可以理解的，毕竟加速卡也不会用来玩游戏。</p><p>针对游戏玩家的是Ada Lovelace架构，此前爆料也是最多18432个流处理器，但是它会大量阉割计算单元，保留完整的图形及光追单元，跟H100的设计理念反过来。</p><p><img src="https://static.cnbetacdn.com/article/2022/0323/3aff1dc0c021e6f.jpg" referrerpolicy="no-referrer"></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1249911.htm" target="_blank">NVIDIA发布新一代H100 GPU核心：4nm工艺、1.8万核心、700W功耗</a></p><p><a href="https://www.cnbeta.com/articles/tech/1250165.htm" target="_blank">NVIDIA连发七款新卡：最高摸到3080Ti、最低阉割没法看</a></p></div>   
</div>
            