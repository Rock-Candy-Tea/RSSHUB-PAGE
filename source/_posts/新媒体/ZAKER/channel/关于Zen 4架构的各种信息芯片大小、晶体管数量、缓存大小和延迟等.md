
---
title: '关于Zen 4架构的各种信息芯片大小、晶体管数量、缓存大小和延迟等'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/630f319eb15ec06f93564a34_1024.jpg'
author: ZAKER
comments: false
date: Wed, 31 Aug 2022 05:11:28 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/630f319eb15ec06f93564a34_1024.jpg'
---

<div>   
<p>AMD 昨天发布了锐龙 7000 系列处理器，全新的 Zen 4 架构架构和现有的 Zen 3 架构相比 IPC 提升了 13%，其中贡献最大的是全新设计的前端，其次是加载 / 存储系统，后面依次是分支预测器、执行引擎和翻倍的 L2 缓存。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202208/630f319eb15ec06f93564a34_1024.jpg" data-height="483" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/630f319eb15ec06f93564a34_1024.jpg" referrerpolicy="no-referrer"></div></div>Zen 4 的内核图片昨天 AMD 其实已经放在 PPT 里面，@SkyJuice60 对这图片进行了注释，可以看到 Zen 4 内核里面有一个非常大的分支预测单元，微操作缓存和 Zen 3 相比扩大了许多，还有加载 / 存储单元、TLB、分支调度器、支持 AVX-512 的双 256bit FPU，L1 缓存没有变化，而 L2 缓存容量翻了一倍，足足占据了四分之一的芯片面积。<p></p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202208/630f319eb15ec06f93564a35_1024.jpg" data-height="593" data-width="884" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/630f319eb15ec06f93564a35_1024.jpg" referrerpolicy="no-referrer"></div></div>@Chiakokhua<p></p><p>也详细标注了 Zen 4 和 Zen 3 的各种缓存和延迟，其中处理器的微操作缓存从 4K 条目扩展到 6.75K 条目，L1 指令 / 数据缓存没有变动依然是 32KB，L2 缓存从 512KB 扩大到 1MB，延迟从 12 个周期增加到 14 个周期，L3 缓存大小没变化，但延迟从 46 个周期增加到 50 个周期，重新排序缓冲区从 256 个条目扩大到 320 个条目，L1 分支目标缓冲区从 1KB 增加到 1.5KB。</p><p>根据 AMD 的资料，Zen 4 的 CCD 面积为 71mm2，而 Zen 3 的 CCD 面积是 80.7mm2，芯片面积缩小了 12%，但晶体管数量从 41.5 亿增加到了 65.7 亿，增加了 58%，这主要归功于生产工艺从台积电 7nm 升级到了 5nm。</p><p>而 IOD 也有很大变化，此前 Zen 2 和 Zen 3 处理器用的 IOD 都是用 GF 的 12nm 工艺生产的，现在 Zen 4 处理器所搭配的 IOD 改用了台积电 6nm 工艺，改进非常的大，旧的 IOD 芯片面积是 125mm2，而新的 IOD 面积是 122mm2，尺寸略微缩小，新的 IOD 里面除了 DDR5 内存控制器和 PCI-E 5.0 控制器之外，还有一个拥有两组 RDNA2 架构 CU 的核显，并且整合了锐龙 6000 系列 Rembrandt 架构的某些电源管理功能。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            