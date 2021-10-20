
---
title: '开源趣闻：AMDGPU驱动调用了Linux内核中的Intel新伙伴分配器代码'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1020/dbd454321e877cd.jpg'
author: cnBeta
comments: false
date: Wed, 20 Oct 2021 11:31:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1020/dbd454321e877cd.jpg'
---

<div>   
Phoronix 报道称：<strong>作为改善视频内存管理工作的一部分，负责开发 AMDGPU 内核图形驱动程序的工程师们，现正希望利用英特尔在 i915 更新中引入的伙伴系统内存分配器（Buddy Allocator）代码。</strong>据悉，后者是英特尔为其专用 GPU 提供设备本地内存支持工作的一部分，其中包含了内存区域和其它概念变动。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1020/dbd454321e877cd.jpg" referrerpolicy="no-referrer"></p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=AMD-Intel-Buddy-Allocator" target="_self">Phoronix</a> 指出，Buddy Allocator 用于将系统内存资源执行等分操作，直到满足内存请求的需求为止。</p><p>而本文提到的新伙伴分配器代码，正是<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> i915 内核驱动程序的一部分。现在，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>GPU 开发团队出于同样的目的，也希望在其功能改进工作中调用这一最佳开源用例。</p><blockquote><p>据悉，周二推出的一组 13 个补丁，将伙伴分配器挪到了 i915 驱动程序本体之外，并转入了公共直接渲染管理器（DRM）区域。</p><p>这使得包括 AMDGPU 在内的第三方驱动开发者，都可在兴趣加持下轻松使用、并对相关代码实施各种底层改进。</p></blockquote><p>对于非 Linux 爱好者来说，这种互惠互利的开源举措似乎有些陌生。</p><p>但通过分享共用 Linux 内核中的现有优秀代码，即使竞争厂商，亦可在其驱动程序之间融入大量基于通用许可的 DRM 内核与 Mesa 用户空间代码。</p><blockquote><p>有趣的是，早在几年前，AMDGPU 的调度程序，也转成过类似的 DRM 通用代码。</p><p>在那之后，其已被英特尔和其它 DRM 内核驱动程序改编再利用，因为它已被证明工作良好。</p></blockquote><p>最后，AMD 借鉴 Intel i915 伙伴分配器代码的补丁和其它相关改进，目前正出于接受公众审查的阶段。</p>   
</div>
            