
---
title: 'Intel Xe游戏显卡内部架构曝光：超采样更贴近NVIDIA'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0819/d9a11049e3cbd8b.png'
author: cnBeta
comments: false
date: Thu, 19 Aug 2021 11:55:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0819/d9a11049e3cbd8b.png'
---

<div>   
Intel将于明天举办架构日活动，公布Xe HPG高性能游戏显卡的架构、技术细节，而偷跑成习惯的VCZ已经放出了部分资料。Intel Xe HPG架构的游戏显卡别称DG2，正式代号Alchemist(炼金术师)，品牌名Intel Arc(锐炫)，明年初发布(大概率CES 2022)，支持硬件光追、AI超采样、DX12U。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0819/d9a11049e3cbd8b.png" referrerpolicy="no-referrer"></p><p>架构方面，<strong>DG2 GPU的一个基本组成模块被称为“Xe-Cores”(Xe核心)，每个内部集成16个EU执行单元(128个核心)，还有一个光追单元，就叫做“Ray Tracing Unit”。</strong></p><p>同时，每四个Xe-Cores组成一个<strong>“Render Slice”(渲染区块)</strong>，因此每个区块64个执行单元。</p><p>DG2 GPU一共有8个这样的Render Slice，<strong>总计512个执行单元</strong>，和此前的传闻相符。</p><p>同时，DG2 GPU还将集成更大容量的二级缓存，称之为“<strong>Memory Fabric</strong>”。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0819/19fba6a01c98a64.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0819/19fba6a01c98a64.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0819/19fba6a01c98a64.jpg" referrerpolicy="no-referrer"></a></p><p><strong>DG2 GPU的超采样技术叫做“XeSS”</strong>，技术原理和NVIDIA DLSS、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> FSR都有所不同，<strong>是通过DP4a、XMX指令实现的</strong>，其中MXM矩阵引擎是AI加速的基础。</p><p>每一颗DG2 GPU，都集成16个矩阵引擎、16个矢量引擎。</p><p><strong>XeSS是一种基于时间的缩放技术，这方面更像NVIDIA DLSS，依赖的是运动矢量、前一帧画面，并且会由XMX指令先行处理，再交给后处理。</strong></p><p>Intel表示，XeSS的帧渲染时间会高于传统缩放算法，但远远低于渲染原生<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>画面所需时间。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0819/e8ba869165ffef8.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0819/e8ba869165ffef8.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0819/e8ba869165ffef8.jpg" referrerpolicy="no-referrer"></a></p><p>Intel还确认，DG2 Alchemist采用的是第一代Xe HPG架构，之后的Battlemage、Celestial分别是Xe2 HPG、Xe3 HPG，更远的Druid则是Xe Next，暗示届时架构会大改。</p><p><img src="https://static.cnbetacdn.com/article/2021/0819/c7ecf7897ac6105.jpg" referrerpolicy="no-referrer"></p>   
</div>
            