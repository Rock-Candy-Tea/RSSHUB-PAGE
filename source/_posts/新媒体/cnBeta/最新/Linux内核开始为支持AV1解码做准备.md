
---
title: 'Linux内核开始为支持AV1解码做准备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0122/61068983813769a.png'
author: cnBeta
comments: false
date: Thu, 12 Aug 2021 07:35:04 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0122/61068983813769a.png'
---

<div>   
目前，提供加速AV1编码的硬件平台数量仍然相当有限，但随着越来越多的硬件进入市场，支持这种免版税视频编解码变得越来越要紧，Linux内核的媒体子系统也正在准备完善这一点。周二，Collabora公司的Daniel
Almeida发出了一个"征求意见"系列补丁，用于在媒体子系统中实现Linux内核的无状态AV1用户空间API。<br>
 <p>AV1 uAPI是围绕AOMedia AV1规范的设计和需求而建立的，并且是媒体子系统一直在努力发展的无状态设计。</p><p><a href="https://static.cnbetacdn.com/article/2021/0122/61068983813769a.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0122/61068983813769a.png" referrerpolicy="no-referrer"></a></p><p>随着这个补丁系列的推出，"VIVPU"也将成为一个虚拟驱动来展示用户空间的API。VIVPU并不尝试任何实际的解码/编码，而只是为了实现用户空间API的测试目的。Collabora也已经针对这个虚拟驱动开发了一个GStreamer解码器。</p><p>VIVPU驱动补丁指出："用户空间的实现可以使用vivpu来运行解码循环，即使在没有硬件的情况下，或者在编解码器的内核uAPI还没有被上游化的时候。这可以在早期阶段揭示出错误。这也使得我们有可能同时研究编解码器的内核uAPI和相应的用户空间实现。"</p><p>对Linux媒体子系统围绕无状态AV1解码的工作感兴趣的人，可以参考这个补丁系列：</p><p><a href="https://lore.kernel.org/lkml/20210810220552.298140-1-daniel.almeida@collabora.com/" _src="https://lore.kernel.org/lkml/20210810220552.298140-1-daniel.almeida@collabora.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="0537353734353d34353737353030372b373c3d34313528342861646b6c60692b646968606c616445666a696964676a77642b666a68">[email protected]</span>/</a><br></p>   
</div>
            