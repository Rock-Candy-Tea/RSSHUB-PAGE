
---
title: 'Intel Xe游戏显卡内部架构曝光：超采样更贴近NVIDIA'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210819/0680b894-bfd9-40b7-ad41-76d389b343cb.png'
author: 快科技（原驱动之家）
comments: false
date: Thu, 19 Aug 2021 19:44:53 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210819/0680b894-bfd9-40b7-ad41-76d389b343cb.png'
---

<div>   
<p>Intel将于明天举办架构日活动，公布Xe HPG高性能游戏显卡的架构、技术细节，而偷跑成习惯的VCZ已经放出了部分资料。</p>
<p><a class="f14_link" href="https://news.mydrivers.com/1/776/776728.htm" target="_blank">Intel Xe HPG架构的游戏显卡别称DG2</a>，正式代号Alchemist(炼金术师)，品牌名Intel Arc(锐炫)，明年初发布(大概率CES 2022)，支持硬件光追、AI超采样、DX12U。</p>
<p style="text-align: center"><img alt="Intel Xe游戏显卡内部架构曝光：超采样更贴近NVIDIA" h="337" src="https://img1.mydrivers.com/img/20210819/0680b894-bfd9-40b7-ad41-76d389b343cb.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>架构方面，<strong><span style="color:#ff0000;">DG2 GPU的一个基本组成模块被称为“Xe-Cores”(Xe核心)，每个内部集成16个EU执行单元(128个核心)，还有一个光追单元，就叫做“Ray Tracing Unit”。</span></strong></p>
<p>同时，每四个Xe-Cores组成一个<strong>“Render Slice”(渲染区块)</strong>，因此每个区块64个执行单元。</p>
<p>DG2 GPU一共有8个这样的Render Slice，<strong>总计512个执行单元</strong>，和此前的传闻相符。</p>
<p>同时，DG2 GPU还将集成更大容量的二级缓存，称之为“<strong>Memory Fabric</strong>”。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210819/9b3ae7d9e6d44226bb5337c846ef33b6.jpg" target="_blank"><img alt="Intel Xe游戏显卡内部架构曝光：超采样更贴近NVIDIA" h="238" src="https://img1.mydrivers.com/img/20210819/s_9b3ae7d9e6d44226bb5337c846ef33b6.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>DG2 GPU的超采样技术叫做“XeSS”</strong>，技术原理和NVIDIA DLSS、AMD FSR都有所不同，<strong>是通过DP4a、XMX指令实现的</strong>，其中MXM矩阵引擎是AI加速的基础。</p>
<p>每一颗DG2 GPU，都集成16个矩阵引擎、16个矢量引擎。</p>
<p><strong><span style="color:#ff0000;">XeSS是一种基于时间的缩放技术，这方面更像NVIDIA DLSS，依赖的是运动矢量、前一帧画面，并且会由XMX指令先行处理，再交给后处理。</span></strong></p>
<p>Intel表示，XeSS的帧渲染时间会高于传统缩放算法，但远远低于渲染原生4K画面所需时间。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210819/1efa397161a04798a4be05f524deb64c.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel Xe游戏显卡内部架构曝光：超采样更贴近NVIDIA" h="303" src="https://img1.mydrivers.com/img/20210819/s_1efa397161a04798a4be05f524deb64c.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Intel还确认，DG2 Alchemist采用的是第一代Xe HPG架构，之后的Battlemage、Celestial分别是Xe2 HPG、Xe3 HPG，更远的Druid则是Xe Next，暗示届时架构会大改。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210819/3a46c0bde21f45e8891c298e084f7553.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel Xe游戏显卡内部架构曝光：超采样更贴近NVIDIA" h="400" src="https://img1.mydrivers.com/img/20210819/s_3a46c0bde21f45e8891c298e084f7553.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/xianka.htm"><i>#</i>显卡</a><a href="https://news.mydrivers.com/tag/intelruixuan.htm"><i>#</i>Intel锐炫</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            