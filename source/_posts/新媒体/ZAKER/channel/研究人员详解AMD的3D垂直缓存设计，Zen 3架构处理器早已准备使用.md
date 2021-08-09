
---
title: '研究人员详解AMD的3D垂直缓存设计，Zen 3架构处理器早已准备使用'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6110fcebb15ec0425471f17f_1024.jpg'
author: ZAKER
comments: false
date: Mon, 09 Aug 2021 05:27:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6110fcebb15ec0425471f17f_1024.jpg'
---

<div>   
<p>在今年的 Computex 2021 主题演讲上，AMD 首席执行官苏姿丰博士展示了采用 3D 垂直缓存（3D V-Cache）技术的 Zen 3 架构桌面处理器。这项创新的技术可以为每个 CCD 带来额外的 64MB 7nm SRAM 缓存，使得处理器的 L3 缓存容量由 32MB 增加到 96MB，容量增加到原来的三倍。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202108/6110fcebb15ec0425471f17f_1024.jpg" data-height="603" data-width="1200" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6110fcebb15ec0425471f17f_1024.jpg" referrerpolicy="no-referrer"></div></div>近日，高级技术研究员 Yuzo Fukuzaki 发表了一篇文章，阐明了 AMD 的这项技术在处理器缓存层次结构中的最合理位置。显然通过 3D 垂直缓存技术，可以扩展处理器的 L3 缓存，而不是作为所谓 "L4 缓存 " 使用，而 16 核心的 Ryzen 9 5950X 处理器共拥有 192MB 的 L3 缓存。<p></p><p>作为一颗 SRAM 芯片，3D 垂直缓存芯片采用了 7nm 工艺制造，尺寸为 6×6 m㎡。据推测，3D 垂直缓存芯片大约有 2300 个硅通孔（TSV），单孔直径约 17μm，让底层 CCX 与 3D 垂直缓存芯片紧密相连。Zen 3 架构处理器应该在设计之初就考虑到使用 3D 垂直缓存芯片的可能性，这说明 AMD 在该技术上已开发多年。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202108/6110fcebb15ec0425471f180_1024.jpg" data-height="882" data-width="1100" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202108/6110fcebb15ec0425471f180_1024.jpg" referrerpolicy="no-referrer"></div></div>根据此前 AMD 的官方介绍，3D 垂直缓存技术是基于台积电的 SoIC 技术。作为一种无损芯片堆叠技术，意味着不使用微凸点或焊料来连接两个芯片，两个芯片被铣成一个完美的平面。底层 CCX 与顶层 L3 缓存之间是一个完美的对齐，硅通孔可以在没有任何类型的粘合材料的情况下进行匹配。<p></p><p>其 CCX 做了翻转（由面向顶部改为面向底部）处理，然后削去了顶部 95% 的硅，再将 3D 垂直缓存芯片安装在上面，让缓存和核心之间的距离缩短了 1000 倍，减少了发热、功耗和延迟。</p><p></p><div class="img_box" id="id_imagebox_2" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_2" data-original="http://zkres2.myzaker.com/202108/6110fcebb15ec0425471f181_1024.jpg" data-height="675" data-width="1200" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6110fcebb15ec0425471f181_1024.jpg" referrerpolicy="no-referrer"></div></div>Yuzo Fukuzaki 表示，为了应对 Memory Wall（内存墙）问题，处理器的缓存设计非常重要。更大容量的缓存在高端处理器上早已成为一种趋势，而 3D 垂直缓存技术有助于提供处理器的性能，同时可以解决低良品率问题，更好地控制成本。<p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            