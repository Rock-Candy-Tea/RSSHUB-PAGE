
---
title: 'Intel超级GPU计算卡亮相：63个小芯片合体、600W功耗'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0222/597fcf664d5bb7c.png'
author: cnBeta
comments: false
date: Tue, 22 Feb 2022 10:59:20 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0222/597fcf664d5bb7c.png'
---

<div>   
ISSCC 2022国际固态电路会议期间，Intel不但公布了初代“矿卡”的细节，还深入介绍了Ponte Vecchio计算加速卡的情况。Ponte Vecchio计算加速卡是基于Xe HPC高性能计算架构的第一款产品，专门面向超级计算机，将在今年晚些时候按计划出货，首批供给美国能源部的超算“Aurora”。<br>
 <p>Intel此前曾经披露过，它使用了5种不同的制造工艺，内部封装多达47个芯片/单元(Tile)，晶体管数量突破1000亿个。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0222/597fcf664d5bb7c.png"><img data-original="https://static.cnbetacdn.com/article/2022/0222/597fcf664d5bb7c.png" src="https://static.cnbetacdn.com/thumb/article/2022/0222/597fcf664d5bb7c.png" referrerpolicy="no-referrer"></a></p><p>根据最新资料，Ponte Vecchio整体面积达<strong>77.5×62.5＝4844平方毫米，多达4468个针脚</strong>，采用了特殊的<strong>空腔封装(Cavity Package)</strong>，共有四个186平方毫米的空腔，<strong>共分为24层(11-2-11的布局)，还有11个2.5D互连通道。</strong></p><p>它通过Foveros、EMIB等先进封装技术，<strong>集成了总共多达63个Tile，其中47个是功能性的，包括16个计算单元、8个RAMBO缓存单元、2个Foveros封装基础单元、8个HBM2E单元、2个Xe链路单元、11个EMIB互连单元，总面积2330平方毫米。</strong></p><p>它们还负责提供内存控制器、FIVR、电源管理、16条PCIe 5.0、CXL。</p><p><strong>另外还有16个Tile，是专门是辅助散热的，总面积770平方毫米，合计达到了惊人的3100平方毫米。</strong></p><p>为什么设置这么多散热Tile？<strong>因为整体功耗达到了恐怖的600W！</strong></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0222/267b6f07727855f.png"><img data-original="https://static.cnbetacdn.com/article/2022/0222/267b6f07727855f.png" src="https://static.cnbetacdn.com/thumb/article/2022/0222/267b6f07727855f.png" referrerpolicy="no-referrer"></a></p><p>这是不同Tile布局的顶视图、侧视图。</p><p><strong>蓝色的是核心计算单元，台积电N5 5nm工艺制造，每个集成8个Xe核心、4MB一级缓存。</strong></p><p>位于计算单元中间的，是<strong>特殊的RAMBO缓存，可以称之为三级缓存，Intel 7工艺制造(10nm ESF)，是一种专门针对高带宽优化的RAM缓存，每个TIle 15MB，合计120MB。</strong></p><p>承载它们的是基础单元(Base Tile)，负责通信传输，Intel 7工艺加Foveros封装，面积646平方毫米，共有17层。</p><p>基础单元和HBM2E高带宽内存、Xe Link链路单元之间，则通过Co-EMIB来封装、通信，其中<strong>Xe Link链路单元是台积电N7 7nm工艺</strong>，负责链接不同的Ponte Vecchio GPU。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0222/1f9cb6bf153de91.png"><img data-original="https://static.cnbetacdn.com/article/2022/0222/1f9cb6bf153de91.png" src="https://static.cnbetacdn.com/thumb/article/2022/0222/1f9cb6bf153de91.png" referrerpolicy="no-referrer"></a></p><p>带宽方面，<strong>计算单元对外高达2.6TB/s，RAMBO缓存对外则是1.3TB/s。</strong></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0222/109576f1d065dd2.png"><img data-original="https://static.cnbetacdn.com/article/2022/0222/109576f1d065dd2.png" src="https://static.cnbetacdn.com/thumb/article/2022/0222/109576f1d065dd2.png" referrerpolicy="no-referrer"></a></p><p>Ponte Vecchio其实有两种功耗指标，<strong>风冷下最高450W，水冷最高才是600W。</strong></p><p>风冷模式下，计算单元、RAMBO缓存、HBM内存、Xe Link等不同部位的最高允许温度<strong>66-73℃不等</strong>，水冷模式下则是<strong>63-70℃</strong>。</p><p><img src="https://static.cnbetacdn.com/article/2022/0222/6b3d2f1f6627590.png" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2022/0222/fcf85a6a5fdccf1.jpg" referrerpolicy="no-referrer"></p>   
</div>
            