
---
title: '英特尔酷睿i9 12900K在Linux上继续保有"单核IOPS之王"地位'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0219/9e6a3ed0f5833c9.jpg'
author: cnBeta
comments: false
date: Sat, 19 Feb 2022 10:55:07 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0219/9e6a3ed0f5833c9.jpg'
---

<div>   
距离上次听到Linux块子系统维护者Jens
Axboe关于实现最大可能的每核IOPS的性能压榨已经有一段时间了。上周五他发表了他的最新见解，结果没有变化，他仍然表示英特尔的Core i9
12900K"Alder Lake"处理器是单核IOPS性能的王者，在他的优化下，这款旗舰产品的单个CPU核心的IOPS接近13M。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0219/9e6a3ed0f5833c9.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>去年夏天，实现单核3.5M的IOPS已经令人印象深刻，但块子系统维护者和IO_uring首席开发人员Jens Axboe正在进行许多优化工作，并不断更好地调整内核代码。当他测试一台Zen 3台式机时，单核IOPS超过了500万。就在10月份，他实现了每核1000万的IOPS的重大突破。</p><p><img src="https://static.cnbetacdn.com/article/2022/0219/d6b71494e1bc667.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>现在最新的进展是他使用酷睿i9 12900K搭配Optane P5800X NVMe存储，最新的Linux内核下能够实现每CPU核心13.07 IOPS，这是一个相当大的成就。</p><p>Axboe周五在Twitter上说："用目前的-git重新测试，结果显示12900K仍然是每核IOPS之王。"</p>   
</div>
            