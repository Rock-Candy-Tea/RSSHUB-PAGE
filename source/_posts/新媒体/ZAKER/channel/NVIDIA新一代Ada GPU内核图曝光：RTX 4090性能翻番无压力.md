
---
title: 'NVIDIA新一代Ada GPU内核图曝光：RTX 4090性能翻番无压力'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6281176cb15ec056c5256f1d_1024.jpg'
author: ZAKER
comments: false
date: Sun, 15 May 2022 15:44:52 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6281176cb15ec056c5256f1d_1024.jpg'
---

<div>   
<p>5 月 24 日上午 11 点，NVIDIA 将亮相台北电脑展举办专题演讲，虽然老黄缺席，但 GeForce 业务高级副总裁在列，还是有希望公布 RTX 40 系显卡的消息甚至是提前发布。在此之前，爆料达人 Kopte7kimi 分享了号称是 AD102 GPU 的内核设计图。</p><p>AD102 也就是 Ada Lovelace 家族的次顶配核心，也是 RTX 40 系游戏旗舰卡的配置，大概率对应 RTX 4090 Ti、RTX 4090 显卡。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202205/6281176cb15ec056c5256f1d_1024.jpg" data-height="392" data-width="700" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6281176cb15ec056c5256f1d_1024.jpg" referrerpolicy="no-referrer"></div></div>分析来看，AD102 内建多大 12 组 GPC（显示计算簇），比上代 GA102 多出 70%。每组 GPC 包括 6 个 TPC（2 个 SM），每个 SM 单元包括 4 个子核心，这都与安培相同，但不同的是，每个 SM 子核心包含 128 组 FP32 单元，加上 IN32 整数单元合计达到 192。<p></p><p><strong>完整 AD102 包括 24 组 SM，所有就是 12288 个 FP32 单元加上 6144 INT32，说通俗易懂点就是 18432 个 CUDA。</strong></p><p>缓存方面，AD102 核心中，每组 SM 享有 192KB L1，比安培增加 50%，共计 4.5MB。L2 增加到 96MB，是安培的 16 倍。</p><p>相应的，ROP 和 RT 光追单元规模自然也是水涨船高，AD102 最多 384 个 ROP，RTX 3090 Ti 不过 112 个。另外，光追单元升级到第三代，Tensor 单元升级到第四代。</p><p>基于此，RTX 4090 最终实现性能翻番似乎并不是可望不可及的虚妄，就 FP32 单精度浮点来说，外界预期能到 90T，而 RTX 3090 Ti 不过 40T，代价就是超 600W 的功耗 ……</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202205/6281176cb15ec056c5256f1e_1024.jpg" data-height="719" data-width="700" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202205/6281176cb15ec056c5256f1e_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            