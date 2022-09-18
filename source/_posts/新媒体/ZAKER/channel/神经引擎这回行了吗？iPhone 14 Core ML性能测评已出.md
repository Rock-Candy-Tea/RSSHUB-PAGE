
---
title: '神经引擎这回行了吗？iPhone 14 Core ML性能测评已出'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/6325fa228e9f09432f065f4b_1024.jpg'
author: ZAKER
comments: false
date: Sun, 18 Sep 2022 00:18:06 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/6325fa228e9f09432f065f4b_1024.jpg'
---

<div>   
<p>机器之心报道</p><p><strong>机器之心编辑部</strong></p><p>你的 iPhone 14 到货了吗？有人已经把 Core ML 的性能测试出来了。</p><p>每年苹果发布新版 iPhone 之后，图片编辑软件 PhotoRoom 的公司团队都会测试一下新 iPhone 的 Core ML 性能。现在，前几天发布的 iPhone 14 的基准测试结果出炉了。</p><p>PhotoRoom 团队的这项系列测试旨在探究苹果公司最新硬件的计算能力，以及计算能力的提升对设备上的机器学习系统意味着什么。</p><p>Core ML 是苹果集成多个 API 构建的机器学习框架，允许 iOS 开发人员发布和执行机器学习模型，以加速在 iPhone、iPad、Apple Watch 上的人工智能任务。</p><p>今年，PhotoRoom 分析了多个 iPhone 机型和 iOS 版本上的 Core ML 性能。</p><p><strong>实验设置</strong></p><p><strong></strong></p><p>作为一款图片编辑软件 ‍，图片裁剪和抠图是 PhotoRoom 非常重要的基础功能。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202209/6325fa228e9f09432f065f4b_1024.jpg" data-height="1164" data-width="538" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/6325fa228e9f09432f065f4b_1024.jpg" referrerpolicy="no-referrer"></div></div>这项功能依托于 iPhone 上的 Core ML 框架执行，PhotoRoom 团队基于此任务在多个 iPhone 机型和 iOS 版本上进行了基准测试，包括：<p></p><p>iPhone 12 Pro A14 Bionic ( iOS 15 + iOS 16 ) </p><p>iPhone 13 Pro A15 Bionic ( iOS 15 + iOS 16 ) </p><p>iPhone 14 Pro A16 Bionic ( iOS 16 ) </p><p>iPad Pro 2021 M1 ( iOS 15 + iOS 16 ) </p><p>MacBook Pro 2021 M1 Pro ( macOS 12 ) </p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202209/6325fa228e9f09432f065f4c_1024.jpg" data-height="720" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202209/6325fa228e9f09432f065f4c_1024.jpg" referrerpolicy="no-referrer"></div></div>对于每个设备，该团队根据不同的 Core ML 计算配置（包括仅在 CPU 上运行、GPU+CPU、ALL、神经网络引擎（ANE）+CPU），统计了模型的平均执行时间（不包括模型加载时间）。其中，每个设备、操作系统版本和计算单元配置都测量了 40 次并取平均值，结果如下：<p></p><p></p><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres1.myzaker.com/202209/6325fa228e9f09432f065f4d_1024.jpg" data-height="328" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202209/6325fa228e9f09432f065f4d_1024.jpg" referrerpolicy="no-referrer"></div></div>这些测试结果表明：<p></p><p>从 CPU 到 GPU 再到 ANE ，运行速度持续提升；</p><p>当在 iOS 16 上从 ALL 转到 ANE+CPU 时，推理时间（几乎）持续增加，这表明模型中的一些层无法在 ANE 上运行，而是默认使用 GPU；</p><p>操作系统版本对整体性能的影响似乎可以忽略不计；</p><p>在 A 系列芯片（A14 Bionic - A15 Bionic - A16 Bionic）中，所有配置的性能都有缓慢而稳定的提升。苹果公司也称其新的 A16 Bionic 芯片（17 TFlops）比 A15 Bionic（15.8 TFlops）提高了 7.5%，使得推理时间从 iPhone 13 Pro 的 45ms 缩短到 iPhone 14 Pro 的 41ms；</p><p>iPad Pro 的 M1 芯片与新的 A16 Bionic 相比，CPU 和 ANE 的性能相当，并其 M1 的 GPU 似乎更强一些。这也许和 M1 芯片比 A16 Bionic 具有更多 GPU 内核有关。</p><p>值得注意的是，从这项基准测试看，MacBook Pro 中 M1 Pro 芯片的性能似乎并不比 iPad Pro 中的 M1 芯片好很多，甚至 ANE 的表现要差一些。</p><p>对于新发布的产品，iPhone 14 Pro 的推理时间缩短至 41ms，这是一个重要的突破。但这项测试也显示出苹果神经网络引擎还存在一些问题。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            