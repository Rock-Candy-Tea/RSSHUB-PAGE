
---
title: '英特尔为Linux 5.18准备了DG2_Alchemist和Xe HP驱动改进版'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0303/1a3f6a4c3f8e4c9.jpg'
author: cnBeta
comments: false
date: Thu, 03 Mar 2022 12:58:24 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0303/1a3f6a4c3f8e4c9.jpg'
---

<div>   
英特尔继续为其即将推出的专用GPU的开源Linux图形驱动支持进行大量的工作，其开源Linux图形驱动工程团队已经提交了他们的最后一次功能拉动的新材料，以准备将其纳入即将到来的Linux 5.18内核中。与此同时，英特尔的工程师们仍然忙于为DG2/Alchemist Arc显卡以及即将推出的计算加速器启用独立GPU。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0303/1a3f6a4c3f8e4c9.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>在DG2/Alchemist方面，Linux 5.18的最后一个i915内核图形驱动更新有围绕小BAR支持的早期工作，作为其可调BAR处理过程的一部分。现在还为DG2提供了6<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>页面支持，而不是仅限于4K。除此之外还有加速后的内存迁移代码。</p><p>同时，当涉及到<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的Xe HP SDV（软件开发工具）对Ponte Vecchio和其他计算加速器的支持时，现在已经完成了CCS检测和围绕计算命令流支持的初步工作，但硬件依然缺乏3D管道/引擎支持。</p><p>本次拉动请求也包含一些针对ARM平台的GuC微控制器处理修复（作为他们帮助确保英特尔dGPU可以在其他CPU架构上工作的工作的一部分），现在也可以防止i915内核驱动在实时内核配置上构建（PREEMPT_RT）。英特尔Linux图形驱动目前在PREEMPT_RT构建中遇到了锁死和警告。考虑到英特尔最近收购了Linutronix，并将努力使实时补丁通过终点线并进入主线内核，希望英特尔的i915驱动将很快为RT构建修复。</p><p>这批面向Linux 5.18的英特尔内核图形驱动功能工作的最后补丁可以通过这个拉动请求找到：</p><p><a href="https://lore.kernel.org/dri-devel/YiBzY1dM7bKwMQ3H@jlahtine-mobl.ger.corp.intel.com/" _src="https://lore.kernel.org/dri-devel/YiBzY1dM7bKwMQ3H@jlahtine-mobl.ger.corp.intel.com/" target="_blank">https://lore.kernel.org/dri-devel/<span class="__cf_email__" data-cfemail="431a2a01391a72270e742108340e12700b03292f222b372a2d266e2e2c212f6d2426316d202c31336d2a2d37262f6d202c2e">[email protected]</span>/</a><br></p>   
</div>
            