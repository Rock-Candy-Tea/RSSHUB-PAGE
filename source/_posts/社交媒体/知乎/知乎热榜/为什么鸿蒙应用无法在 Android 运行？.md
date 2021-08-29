
---
title: '为什么鸿蒙应用无法在 Android 运行？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic1.zhimg.com/v2-a9d3c93d1671ad79884e29fb95770cbd_1440w.jpg'
author: 知乎
comments: false
date: Sun, 29 Aug 2021 03:51:11 GMT
thumbnail: 'https://pic1.zhimg.com/v2-a9d3c93d1671ad79884e29fb95770cbd_1440w.jpg'
---

<div>   
Abel小智的回答<br><br><p>从技术角度来看，尽管大家都是基于ARM架构，Linux内核，但鸿蒙app用的是自己封装的API，如果要让鸿蒙app运行在Android上，<b>也比较简单，需要让google的开发人员做一套能编译鸿蒙Api并且兼容Androidapi的安方舟编译器就可以了。</b></p><p>这是Android的系统架构图，</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-a9d3c93d1671ad79884e29fb95770cbd_1440w.jpg" data-caption data-size="normal" data-rawwidth="727" data-rawheight="600" data-default-watermark-src="https://pic2.zhimg.com/v2-a05c35c7e5c88dddf3e55db88f599891_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-a9d3c93d1671ad79884e29fb95770cbd_r.jpg" referrerpolicy="no-referrer"></figure><p>这是鸿蒙的系统架构图，</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-4bb549c9ea2a01a1380c8a98716f5a1f_1440w.jpg" data-caption data-size="normal" data-rawwidth="1141" data-rawheight="554" data-default-watermark-src="https://pic1.zhimg.com/v2-ac22f3df8c80a2991d1693e4c4ee40df_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-4bb549c9ea2a01a1380c8a98716f5a1f_r.jpg" referrerpolicy="no-referrer"></figure><p>可以看到，现阶段鸿蒙做的更多是的往系统服务层、应用服务层添加更多和场景、业务相关功能模块，例如IOT、Ability、UI、安全等等，另外就是逐步兼容或替换Android原生的Api，内核层没有太多的讨论点，因为只和平台、外设驱动有关。</p><p>而鸿蒙想要完全抛弃aosp、Runtime、Hal、Native、Framwork相关的框架和思想，短时间来说基本不可能，那技术层面如何切入？如何建立开发者认同感？如何打造生态？路还很远。</p><p>我的观点是，谁能承担责任、站得最前、被骂被调侃得最多。那我就支持谁，毕竟总会有一个能做成功的，但你们不能影响我干饭。</p><p></p>  
</div>
            