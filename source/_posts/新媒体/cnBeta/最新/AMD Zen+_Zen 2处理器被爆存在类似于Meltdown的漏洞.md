
---
title: 'AMD Zen+_Zen 2处理器被爆存在类似于Meltdown的漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0830/2e185065a889303.jpg'
author: cnBeta
comments: false
date: Mon, 30 Aug 2021 03:02:30 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0830/2e185065a889303.jpg'
---

<div>   
来自德累斯顿工业大学的 Saidgani Musaev 和 Christof Fetzer 两位网络安全研究人员，在基于“Zen+”和“Zen2”微架构的 AMD 处理器上发现了一种强迫在微架构元素之间进行非法数据流的新方法，并将其命名为“Transient Execution of Non-canonical Accesses”（非经典访问的瞬时执行）。<br>
 <p style="text-align: left;">安全研究报告[<a href="https://arxiv.org/ftp/arxiv/papers/2108/2108.10771.pdf" target="_blank">PDF</a>] | AMD <a href="http://herehttps//www.amd.com/en/corporate/product-security/bulletin/amd-sb-1010" target="_blank">安全公告</a> | 相关的<a href="https://developer.amd.com/wp-content/resources/90343-D_SoftwareTechniquesforManagingSpeculation_WP_9-20Update_R2.pdf" target="_blank">缓解措施</a><br style="text-align: left;"></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0830/2e185065a889303.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0830/2e185065a889303.jpg" alt="545.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">该方法在 2020 年 10 月被发现，但研究人员遵循负责任的披露规范，给了 AMD 时间来解决该漏洞并开发缓解措施。该漏洞被记录在 CVE-2020-12965 和AMD安全公告ID"AMD-SB-1010"下。</p><p style="text-align: left;">AMD 公司对这一漏洞的单行摘要是这样写的：“当与特定的软件序列相结合时，AMD CPU 可能会暂时执行非经典的加载和存储，只使用较低的48个地址位，可能会导致数据泄漏”。</p><p style="text-align: left;">研究人员在三种处理器上研究了这个漏洞，即基于"Zen 2"的EPYC 7262，以及基于"Zen +"的Ryzen 7 2700X和Ryzen Threadripper 2990WX。他们提到，所有容易受到 MDS 攻击的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>处理器"本质上都有相同的缺陷"。AMD是该论文的主题，因为AMD"Zen +"（以及后来的）处理器对英特尔处理器上展示的MDS有免疫力。AMD 为该漏洞开发了一个缓解措施，其中包括修补脆弱软件的方法。</p>   
</div>
            