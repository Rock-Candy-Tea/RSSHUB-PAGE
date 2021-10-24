
---
title: '联发科发布8000余行新Linux内核驱动代码以支持AI处理单元'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1024/574b4cf1746e53f.jpg'
author: cnBeta
comments: false
date: Sat, 23 Oct 2021 23:55:29 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1024/574b4cf1746e53f.jpg'
---

<div>   
<strong>几个月来，联发科的工程师们一直在发布Linux内核驱动代码，用于在MT8192
SoC内启动AI处理单元（APU），而本周末发布的是超过八千行代码的完整补丁系列。</strong>之前MTK已经发布了一些APU电源处理和IOMMU补丁，而周六发布的是一整套补丁，用于启动MT8192
APU的电源控制、tinysys控制器（APU上的微控制器）和中间件支持。总共有8100多行的新内核代码。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1024/574b4cf1746e53f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1024/574b4cf1746e53f.jpg" title alt="MT8192_Chromebook_blog.jpg" referrerpolicy="no-referrer"></a></p><p>联发科关于MT8192的文档宣传其AI处理器是"APU 2.0"设计，算力能够达到2.4 TOPs，是其上一代APU性能的五倍。"这个能力很强的多核人工智能处理器可以与内置的摄像头和麦克风一起工作，以丰富广泛的基于语音和视觉的应用，如语音识别和语音控制、语音和图像识别、语音到文本、实时翻译、物体识别、背景去除、降噪、图像和视频分割、手势控制和基于GoogleAR核心的增强功能，这些都是实时的。"</p><p>MT8192 SoC自去年发布以来，在一些Chromebook和其他设备中被发现。MT8192的八核基础布局是四个Cortex-A76核心和四个A55核心，而在图形方面是Arm Mali G-57担纲。</p><p>支持这个人工智能处理单元的13个补丁现在已经发布出来供人审查。到目前为止，我还没有找到任何支持用户空间的代码以配合这个联发科APU内核驱动，所以我们还需要时间才会看到这个贡献是如何被接受的，以及它最终会发生什么。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/20211023111409.30463-1-flora.fu@mediatek.com/" _src="https://lore.kernel.org/lkml/20211023111409.30463-1-flora.fu@mediatek.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="47757775767677757476767673777e6974777371746a766a212b283526692132072a22232e2633222c6924282a">[email protected]</span>/</a><br></p>   
</div>
            