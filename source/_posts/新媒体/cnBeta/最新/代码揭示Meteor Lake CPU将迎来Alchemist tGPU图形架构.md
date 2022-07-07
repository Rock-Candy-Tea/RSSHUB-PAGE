
---
title: '代码揭示Meteor Lake CPU将迎来Alchemist tGPU图形架构'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0707/e005658e6e17960.jpg'
author: cnBeta
comments: false
date: Thu, 07 Jul 2022 02:35:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0707/e005658e6e17960.jpg'
---

<div>   
<strong>Meteor Lake CPU 刚刚迎来了英特尔图形编译器（IGC）的最新支持，并揭示了即将在芯片上启用的 Xe-HPG（Arc Alchemist）核显。</strong>首先，由 Pete Chou 的最新代码提交可知，英特尔 14 代 CPU 将率先采用与该公司独显产品线相同的 Tiled-GPU 图形架构（tGPU）。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0707/e005658e6e17960.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://wccftech.com/intel-meteor-lake-cpu-arc-alchemist-graphics-architecture-gets-compiler-support-xmx-for-xess-missing-partial-fp64-on-board/" target="_self">WCCFTech</a>）</p><p>代码中将之用“Xe_MTL”指代，有趣的是，Coelacanth Dream 发现 Meteor Lake CPU 不具有 DPAS 指令 —— 意味其不包含 XeSS 所用的 XMX 单元。</p><blockquote><p>这项特性对于 AI 加持的技术至关重要，体验上类似于英伟达 DLSS 技术的 AI 升级版。作为弥补，Meteor Lake CPU 配备了一个 VPU 视觉处理单元。</p><p>外媒推测它可能提供某种形式的推理能力（或有助于 XeSS），但相关处理还是依靠主 GPU 芯片来完成。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0707/272f47f47a63e97.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0707/272f47f47a63e97.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>其次，代码提交中列出了 tGPU“部分支持”FP64 双精度计算 —— <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>从 Gen 11 架构中移除了 FP64 和 Int64 支持，但明年的 14 代 Meteor Lake 芯片有望重返。</p><p>至于 Meteor Lake CPU 上使用的 Tiled-GPU，它应该会是一种全新的核显架构 —— 既不是 iGPU、也不是 dGPU，而是下一代的图形引擎（Next-Gen Graphice Engine）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0707/4c00786393d90b1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0707/4c00786393d90b1.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>可以预见的是，得益于全新的 Xe-HPG 图形架构，Meteor Lake CPU 可在同等能耗下达成更高的效率。</p><p>而目前仅限 Alchemist 产品线的 DirectX 12 Ultimate 和 XeSS 支持，也有望在 Meteor Lake 平台上得到进一步的普及。</p>   
</div>
            