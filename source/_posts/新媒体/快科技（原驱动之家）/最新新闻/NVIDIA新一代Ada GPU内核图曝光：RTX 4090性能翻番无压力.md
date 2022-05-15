
---
title: 'NVIDIA新一代Ada GPU内核图曝光：RTX 4090性能翻番无压力'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220515/s_4687e320d62d43ab9f169ba4d13225d3.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sun, 15 May 2022 12:09:20 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220515/s_4687e320d62d43ab9f169ba4d13225d3.jpg'
---

<div>   
<p>5月24日上午11点，NVIDIA将亮相台北电脑展举办专题演讲，虽然老黄缺席，但GeForce业务高级副总裁在列，还是有希望公布RTX 40系显卡的消息甚至是提前发布。</p>
<p>在此之前，爆料达人Kopte7kimi分享了号称是AD102 GPU的内核设计图。</p>
<p>AD102也就是Ada Lovelace家族的次顶配核心，也是RTX 40系游戏旗舰卡的配置，大概率对应RTX 4090 Ti、RTX 4090显卡。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220515/4687e320d62d43ab9f169ba4d13225d3.jpg" target="_blank"><img alt="NVIDIA新一代Ada GPU内核图曝光：RTX 4090性能翻番无压力" h="336" src="https://img1.mydrivers.com/img/20220515/s_4687e320d62d43ab9f169ba4d13225d3.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>分析来看，AD102内建多大12组GPC（显示计算簇），比上代GA102多出70%。每组GPC包括6个TPC（2个SM），每个SM单元包括4个子核心，这都与安培相同，但不同的是，每个SM子核心包含128组FP32单元，加上IN32整数单元合计达到192。</p>
<p><strong>完整AD102包括24组SM，所有就是12288个FP32单元加上6144 INT32，说通俗易懂点就是18432个CUDA。</strong></p>
<p>缓存方面，AD102核心中，每组SM享有192KB L1，比安培增加50%，共计4.5MB。L2增加到96MB，是安培的16倍。</p>
<p>相应的，ROP和RT光追单元规模自然也是水涨船高，AD102最多384个ROP，RTX 3090 Ti不过112个。另外，光追单元升级到第三代，Tensor单元升级到第四代。</p>
<p>基于此，RTX 4090最终实现性能翻番似乎并不是可望不可及的虚妄，就FP32单精度浮点来说，外界预期能到90T，而RTX 3090 Ti不过40T，代价就是超600W的功耗……</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220515/be2d1dc05afe4e17a3733a2d1d6bb607.png" target="_blank"><img alt="NVIDIA新一代Ada GPU内核图曝光：RTX 4090性能翻番无压力" h="615" src="https://img1.mydrivers.com/img/20220515/s_be2d1dc05afe4e17a3733a2d1d6bb607.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：万南</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/rtx_4090.htm">RTX 4090</a><a href="https://news.mydrivers.com/tag/nvidia.htm">NVIDIA</a><a href="https://news.mydrivers.com/tag/ada_lovelace.htm">Ada Lovelace</a>  </p>
        
</div>
            