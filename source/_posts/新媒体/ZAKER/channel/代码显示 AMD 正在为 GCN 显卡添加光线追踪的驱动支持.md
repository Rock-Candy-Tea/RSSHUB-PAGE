
---
title: '代码显示 AMD 正在为 GCN 显卡添加光线追踪的驱动支持'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6279cefcb15ec06909457ca1_1024.jpg'
author: ZAKER
comments: false
date: Mon, 09 May 2022 19:02:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6279cefcb15ec06909457ca1_1024.jpg'
---

<div>   
<p>IT 之家 5 月 10 日消息，Radeon Vulkan 新驱动程序 RADV 的源代码已经出现在了 Mesa 上（Mesa 是一个图形 API 的库，库中最出名的就是 OpenGL），这将使前几代 AMD 显卡在驱动的层次上支持 Vulkan 光线追踪。此次更新会使 Vulkan 光线追踪最早支持到 AMD GFX6 硬件，而 GFX6 硬件则是 AMD 的 GCN 1.0 组件，也就是说，它可以支持 GCN 显卡使其使用 Vulkan 光线追踪。虽然光追在没有独立单元的旧显卡运行会很吃力，但这样也可以提高画面质量，总比没有强。</p><p>独立开发者 Konstantin Seurer 创建了对此次更新进行了 " 尝鲜体验 "，发现对于类似于 GravityMark 基准测试这样特定的工作负载，其运行速度从原先的 13FPS 到达了现在的 250FPS。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202205/6279cefcb15ec06909457ca1_1024.jpg" data-height="387" data-width="657" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6279cefcb15ec06909457ca1_1024.jpg" referrerpolicy="no-referrer"></div></div>（打上 Radeon RADV LBVH 补丁后的 GravityMark 基准测试帧率）<p></p><p>如今 Radeon RADV 已经合并进了 Mesa 22.2，但是到上个月，最新合并的 Mesa 22.2 库还是只支持 AMD RDNA 图形处理器。AMD 光线追踪的重心依旧是 AMD RDNA2 架构，这点并不让人惊讶，但是最近的更新中却在 Linux 中加入了对旧硬件的支持，这就很让人惊讶了，AMD 并没有放弃老玩家。</p><p>在国外论坛上已经有玩家对此次更新进行了体验，他们得出的结论是在某些需要光线追踪的特殊开发项目中，RADV 可以带来极大的提升。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202205/6279cefcb15ec06909457ca3_1024.jpg" data-height="123" data-width="985" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6279cefcb15ec06909457ca3_1024.jpg" referrerpolicy="no-referrer"></div></div>但是很多游戏对此更新的兼容性似乎依然不太乐观。<p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            