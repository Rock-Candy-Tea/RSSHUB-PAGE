
---
title: 'Intel Xe HPG锐炫游戏显卡架构公开：台积电6nm、驱动完全重写'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202108/611efbd68e9f0972d25236fd_1024.jpg'
author: ZAKER
comments: false
date: Thu, 19 Aug 2021 17:58:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202108/611efbd68e9f0972d25236fd_1024.jpg'
---

<div>   
<p>品玩 8 月 20 日讯，Intel 日前宣布基于 Xe HPG 架构的高性能独立显卡命名为 " 锐炫 " ( Intel Arc ) ，首款产品 Alchemist ( DG2 ) 将在明年初发布。</p><p>Intel GPU 多年来的基本模块一直都是 " 执行单元 " ( EU ) ，这次变成了全新的 "Xe 核心 " ( Xe Core ) ，包含矢量和矩阵 ( 张量 ) ALU 单元、零级和一级缓存、载入存储单元等等。</p><p>大致看来，Intel Xe 核心的组织方式有点像 NVIDIA SM，只是少了纹理单元，当然内部结构肯定是迥异的。</p><p>Xe 核心内有 16 个矢量单元，或者叫矢量引擎，每个每时钟周期可处理 256 位，又可细分为 8 个 FP32 ALU 单元，因此每个 Xe 核心每时钟周期颗处理器 128 个 FP32 操作。</p><p>同时还有 16 个矩阵数学单元，或者叫矩阵引擎 ( XMX ) ，处理矩阵、张量操作，每个每时钟周期可处理 1024 位，可以是 64 个 FP16 操作，也可以是 128 个 INT8 操作。</p><p>Xe 核心的上一层级是 " 渲染切片 " ( Render Slice ) ，专为 DX12 Ultimate 设计，每个包含 4 个 Xe 核心、4 个光追单元、4 个纹理采样器、几何前端、光栅前端、2 个像素后端。</p><p>值得一提的是，光追部分支持 DirectX 光追 ( DXR ) 、Vulkan 光追。Alchemist DG2 GPU 包含最多 8 个渲染切片，共享大容量二级缓存。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202108/611efbd68e9f0972d25236fd_1024.jpg" data-height="422" data-width="750" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202108/611efbd68e9f0972d25236fd_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            