
---
title: '字节跳动火山引擎在移动端已实现 H.266 4K 单线程实时解码，iPhone 13 为测试机'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/1/c7aeabd4-68d3-482b-ad78-8d909890eb26.png'
author: IT 之家
comments: false
date: Sat, 29 Jan 2022 13:58:11 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/1/c7aeabd4-68d3-482b-ad78-8d909890eb26.png'
---

<div>   
<p data-vmark="28ae"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 1 月 29 日消息，近日，字节跳动旗下火山引擎多媒体实验室宣布实现技术突破：BVC2 解码器利用异构平台（CPU+GPU）已在移动端实现 H.266 4K 单线程的实时解码，解码速度达到 30FPS 以上。据公开资料显示，BVC2 成为业界首个在移动端实现 H.266 4K 单线程实时解码的解码器。</p><p style="text-align: center;" data-vmark="6f2b"><img src="https://img.ithome.com/newsuploadfiles/2022/1/c7aeabd4-68d3-482b-ad78-8d909890eb26.png" w="1440" h="839" alt="火山引擎" title="字节跳动火山引擎在移动端已实现 H.266 4K 单线程实时解码，iPhone 13 为测试机" width="1440" height="478" referrerpolicy="no-referrer"></p><p data-vmark="4187">H.266 是最新一代视频编码标准，由联合视频专家组（JVET）于 2020 年 7 月确定。相比前一代 H.265 标准，H.266 标准在主观质量相当的情况下可以节省 50% 码率。虽然 H.266 能够大大节省带宽成本，但由于解码器计算复杂度是 H.265 解码器的 1.5-2 倍，计算资源的需求也是成倍增加，使得 H.266 在移动端的应用备受挑战。</p><p data-vmark="c553">火山引擎多媒体实验室发现，新的移动端 GPU 有比较强的算力资源，所以考虑在 BVC2 解码器里协同 CPU+GPU 解码。进一步的研究发现，CPU+GPU 组成的异构平台解码方案除了兼具软解码的灵活性和硬解码的速度优势外，还拥有功耗优势。此外，GPU 解码联合 GPU AI 后处理算法，整个播放系统的呈现延时还能做到进一步的优化。</p><p data-vmark="ab8f">因此，火山引擎多媒体实验室在 BVC2 解码器上优化了解码时 CPU 和 GPU 之间的通信、GPU 重度资源分配；同时根据不同解码算法的特点，有针对性的优化 GPU 内核 Kernel，充分利用 GPU 的线程数量，以及 GPU 线程之间的负载均衡。</p><p style="text-align: center;" data-vmark="a581"><img src="https://img.ithome.com/newsuploadfiles/2022/1/ade14f49-ecd1-4b9a-bb52-01f732bc4df2.png" w="1080" h="661" alt="火山引擎" title="字节跳动火山引擎在移动端已实现 H.266 4K 单线程实时解码，iPhone 13 为测试机" width="1080" height="502" referrerpolicy="no-referrer"></p><p style="text-align: center;" data-vmark="d34c">▲ BVC2 解码器与 VTM11.0 标准解码器在 <a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone 13</a> 上的测试结果（T-1 为单线程）</p><p data-vmark="c2b1">在 <a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone</a> 13 设备上的单线程测试结果显示，相比 VTM11.0 标准解码器，BVC2 解码器在 classB 1080P 视频上有接近 15 倍的速度提升，在 classA1、classA2 4K 视频上解码速度稳定达到 30FPS 以上，实现单线程实时解码 4K。</p><p data-vmark="3738">火山引擎多媒体实验室此前研发了针对屏幕内容的视频编解码器 BVC1S，在移动平台上支持 H.266 标准 8K 解码，以及实现 H.266 端云一体视频解决方案。</p>
          
</div>
            