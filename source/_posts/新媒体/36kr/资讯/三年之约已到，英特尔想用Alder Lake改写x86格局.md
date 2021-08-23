
---
title: '三年之约已到，英特尔想用Alder Lake改写x86格局'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210822/v2_221733fed7194a15ac3777d01e67ec14_img_000'
author: 36kr
comments: false
date: Mon, 23 Aug 2021 02:40:43 GMT
thumbnail: 'https://img.36krcdn.com/20210822/v2_221733fed7194a15ac3777d01e67ec14_img_000'
---

<div>   
<p>北京时间2021年8月20日，<a class="project-link" data-id="3968654" data-name="英特尔" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968654" target="_blank">英特尔</a>在「英特尔架构日2021」的主题演讲中正式展示了英特尔全新一代计算结构Alder Lake，同时也推出了两大x86 CPU内核、两大数据中心SoC、两款独立GPU，掀起了2021英特尔产品布局的序幕。</p> 
<h2 label="一级标题" style><strong>性能混合架构Alder Lake</strong></h2> 
<p>一般来说，x86电脑的处理器由多个相同的处理器核心组成，即使核心与核心之间体质不同，本质上还是当成同样的核心来调用。但英特尔全新的Alder Lake架构，为x86处理器带来了全新的性能分配方案：它搭载了两款不同的新一代x86内核以及智能英特尔硬件线程调度器。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210822/v2_221733fed7194a15ac3777d01e67ec14_img_000" referrerpolicy="no-referrer"></p> 
<p>简单来说，<strong>Alder Lake架构下桌面处理器的核心会分为能效核（Efficient-core，下文简称E-core）与性能核（Performance-core，下文简称P-core）</strong>。其中E-Core采用了高度可拓展的x86微架构，能在有限的空间内实现多核任务负载，并具有更大的频率范围。凭借低电压的优势，E-core可以降低整体功率消耗，在同样的负载下能为电脑带来更出色的放热与能耗表现。</p> 
<p>与Skylake内核相比，在单线程的情况下，E-core能实现约40%的性能提升。多线程负载下的表现则更为出色，在特定情况下，更是能带来80%的性能提升，同时整体功耗也更低。</p> 
<p>至于P-core，这是英特尔迄今为止性能最强的CPU内核，能为CPU架构和性能带来显著的提升。更多的解码器与运行端口、更大的寄存器与更智能的预测准确度为它带来了更强大的性能表现。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210822/v2_897a9f2d217e472ebe5738c1b2ce23d3_img_000" referrerpolicy="no-referrer"></p> 
<p>为了更高的协调性能核与能效核，英特尔在Alder Lake中加入了一个全新的资源调度方式：Intel Thread Director（ITD）。在ITD的支持下，CPU会主动向操作系统汇报不同核心的可用状况。<strong>操作系统在接到软件发出的进程请求后，会根据进程对硬件资源的要求与优先级，将进程分配到不同的核心中。</strong></p> 
<p>举个例子，在核心资源可用的情况下，对资源要求更高的游戏进程都会交给性能核处理，而对资源要求不高的语音进程则会分配给能效核。不过根据英特尔在发布会后群访环节中给出的答复，核心的分配方式并不是一成不变的，ITD会根据当前的使用状况给出最符合当前情况的调整。当然了，如果有必要的话，软件也可以与特定核心绑定。但英特尔并不建议采用这样的调度方式，Alder Lake与Windows 11配合开发，让操作系统来调度资源显然更加合适。</p> 
<h2 label="一级标题" style><strong>12代酷睿前瞻</strong></h2> 
<p>在架构日上，英特尔也介绍了关于下一代酷<a class="project-link" data-id="197428" data-name="睿芯" data-logo="https://img.36krcdn.com/20210813/v2_2fc1e315cebe4e5d80f1e69d98230f78_img_000" data-refer-type="1" href="https://p.36kr.com/space/3390010143" target="_blank">睿芯</a>片的更多消息。首先，12代酷睿将提供三种不同的封装方式，对应三种不同的功耗版本。第一种是大家相对更为熟悉的桌面独立封装，最高提供8+8（P+E）的组合。适用于平台的移动版最高可以来到6+8（P+E）组合，而功耗最低的超低功耗「Ultra Mobile」封装为2+8（P+E）封装，功耗最低仅9W。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210822/v2_5f86c623d1944e4db2cca6436f45ea04_img_000" referrerpolicy="no-referrer"></p> 
<p>至于为什么无论所有封装，都有8个能效核「保底」呢？英特尔给出的解释是能效核拥有更高的集成度，在多线程的处理上也担当了重要的角色。再加上能耗核并不会对芯片的整体功耗带来太大影响，因此在移动平台更多地会采用能耗核。</p> 
<p>虽然三种封装的配置与功耗各不相同，缓存大小与对内存频率的支持也有一定差异，但如果从微处理器的角度看，三款封装其实也有异曲同工的地方。比如三个方案都包含了新一代的高斯神经加速器GNA 3.0。但由于实际产品需要等到10月才会正式公布，所以目前英特尔也没有透露太多关于下一代处理器的详细规格，还要等到10月份才会有进一步的消息披露。</p> 
<h2 label="一级标题" style><strong>新显卡与新技术</strong></h2> 
<p>在架构日上，英特尔也公布了关于新一代独立显卡的最新消息：英特尔锐炫（Intelk Arc）将采用Xe HPG微架构、采用全新的Xe内核。消费级显卡路线图包括Alchemist（此前称之为DG2）、Batt<a class="project-link" data-id="542543" data-name="LEM" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/542543" target="_blank">lem</a>age、Celestial和Druid SoC。但这并不是新显卡最大的亮点。真正奠定新显卡地位的，还是全新的XeSS技术。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210822/v2_8d1b8958ae3845f78f7ef7d7282ed8c7_img_000" referrerpolicy="no-referrer"></p> 
<p>凭借Alchemist的内置XMX AI加速，XeSS技术采用了深度学习技术，能用低分辨率的素材合成出接近原生高分辨率的画面。在主题演讲中英特尔展示了原生4K与XeSS技术下的1080P画面，可以看到两者的表现非常接近。</p> 
<h2 label="一级标题" style><strong>数据中心</strong></h2> 
<p>除了大家更为熟悉的消费级产品，英特尔也同步推出了适用于数据中心的下一代英特尔至强可扩展处理器——Sapphire Rapids。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210822/v2_3404ec29c224401a8a9699e1397b2dca_img_000" referrerpolicy="no-referrer"></p> 
<p>Sapphire Rapids基于Intel 7制程工艺，采用英特尔全新的性能核微架构（Golden Cove），该架构旨在提高速度，突破低时延和单线程应用性能的极限。同时，Sapphire Rapids也内置了多个全新的加速引擎，可以针对设备调度、深度学习与数据吞吐做出专门的优化。全新的基础设施处理器IPU也可以降低云服务或通讯服务的CPU开销，以更低的部署门槛提供更安全、更智能、更高效的运算服务。 </p> 
<h2 label="一级标题" style><strong>总结</strong></h2> 
<p>在架构日上，英特尔一次性拿出了多款围绕Golden Cove的全新运算平台，推出的产品也横跨消费级与数据中心级别，这不仅是英特尔技术的展示，同时也是英特尔main对激烈的市场竞争，做出的最好回应。由于7nm工艺久未成熟，英特尔过去在消费级产品领域失去了先机。但Alder Lake多核心架构的出现与实打实的性能提升打消了消费者对英特尔的顾虑，同时全新的设计理念也为x86带来更多的新活力。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210822/v2_d4b7fc7adec242b3bd7a03f2ba78569e_img_000" referrerpolicy="no-referrer"></p> 
<p>性能核与能效核的过去已被广泛应用在ARM架构中，但与移动处理器不通，Alder Lake独特的资源调度方式让操作系统可以更好地分配运算核心，实现性能与能效的平衡。可以预见的是，找到了新方向的英特尔有望拿下更多的PC与数据中心市场份额，同时对未来的电脑发展也能起到带头的作用。 </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MjM5MTg5NTU0MQ==&mid=2653904997&idx=4&sn=c7b47981b62e94f461c5134adc202c33&chksm=bd755aff8a02d3e93be94efdbe93061725ab3d09b619ebdd48ecb73e6f7f3531bc8eb245df2b&scene=27#wechat_redirect">“雷科技”（ID：leitech）</a>，作者：<a class="project-link" data-id="41584" data-name="雷科技" data-logo="https://img.36krcdn.com/20210807/v2_90b8b3556dcd4c35a365dce0eaf3bf83_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/41584" target="_blank">雷科技</a>数码3C组，编辑：一位天明 ，36氪经授权发布。</p>  
</div>
            