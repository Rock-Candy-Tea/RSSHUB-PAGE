
---
title: 'SiSoftware放出Core i9-12900K性能预览，AVX-512真的没了'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc1e_1024.jpg'
author: ZAKER
comments: false
date: Sun, 26 Sep 2021 06:15:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc1e_1024.jpg'
---

<div>   
<p>Intel 将会在下月底发布第 12 代酷睿处理器 Alder Lake，而评测解禁与开卖都得等到 11 月初，但现在各测试数据库里面已经有不少这些处理器的测试数据了，SiSoftware Sandra 就拿了他们数据库里面 Core i9-12900K 的数据来做了个预览，需要注意的是这些数据并不是他们自己测出来的，而是拿别人上传的数据整合出来的，所以不能说是评测，而且这篇原文已经被删除了，只不过有人把网页截图传到了 imgur 上。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc1e_1024.jpg" data-height="608" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc1e_1024.jpg" referrerpolicy="no-referrer"></div></div>Core i9-12900K 是由 8 个性能核与 8 个效能核组成的，性能核其实就是 Golden Cove，每个核心拥有 48KB L1 数据缓存和 32KB L1 指令缓存，还有 1.25MB 的 L2 缓存；效能核则是 Gracemont，每核心拥有 64KB L1 数据缓存和 32KB L1 指令缓存，四个核心共享 4MB L2 缓存，性能核支持超线程而效能核不支持，所以 Core i9-12900K 是 16 核 24 线程，频率方面基础频率 3.6GHz，性能核全核睿频 5.0GHz，最大睿频 5.3GHz，效能核则是 3.7GHz 全核与 3.9GHz 最高，所有核心共享 30MB L3 缓存，PL1 是 125W，PL2 则是 228W。<p></p><p>需要注意的是 Alder Lake 并不支持 AVX-512，虽然说 Golden Cove 是支持 AVX-512 与 AMX 的，但由于是混合架构，可能调度会有问题，所以并没有放出来给用户使用，至少目前还没有。</p><p>SiSoftware Sandra 给出了四个测试表，但 Core i9-12900K 有些项目是没有测试结果的，测试内容包括矢量 SIMD、加密和金融分析，并且放出了 Core i9-11900K、Ryzen 9 5900X、Core i9-10900K 的数据给大家对比：</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc1f_1024.jpg" data-height="770" data-width="900" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc1f_1024.jpg" referrerpolicy="no-referrer"></div></div><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc20_1024.jpg" data-height="702" data-width="900" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc20_1024.jpg" referrerpolicy="no-referrer"></div></div><div class="img_box" id="id_imagebox_3" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_3" data-original="http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc21_1024.jpg" data-height="742" data-width="900" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/61507a29b15ec057b665fc21_1024.jpg" referrerpolicy="no-referrer"></div></div>实际上 Core i9-12900K 在这些测试里的表现并不算好，大部分测试项目它的表现都不如 Ryzen 9 5900X，而且由于 AVX-512 的缺失，甚至连 Core i9-11900K 都打不过。需要注意的是这些未必是最终测试结果，因为原文并没有提及测试平台以及 CPU 的功耗设置，甚至有些测试是在 Windows 11 下跑有些是在 Windows 10 下跑的，所以上面的成绩真是只能用来大致预览。<p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            