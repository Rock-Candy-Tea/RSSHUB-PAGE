
---
title: 'Intel驱动改变一行代码：光追性能狂增100倍'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0723/9c215be0438eaa0.jpg'
author: cnBeta
comments: false
date: Sat, 23 Jul 2022 12:22:30 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0723/9c215be0438eaa0.jpg'
---

<div>   
在显卡驱动方面，Intel表现确实相对不怎么样，还经常出现一些神奇的情况。<strong>近日，Intel Linux开源驱动工程师Lionel Landwerlin将一个新的补丁合并到了Intel Mesa Vulkan 22.2开源驱动中，其中简单变更了Intel Vulkan光线追踪代码，从而带来了100倍的性能提升，“没有开玩笑”。</strong><br>
 <p>怎么回事呢？</p><p><a href="https://img1.mydrivers.com/img/20220723/e3012cc40f704bbe94c26e8e7e839623.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0723/9c215be0438eaa0.jpg" referrerpolicy="no-referrer"></a></p><p>其实是原来驱动的一个Bug，没有将光追临时存储放置在显卡的本地显存中，而是放到速度更慢的系统内存，导致性能低下。</p><p><strong>新补丁给驱动加入了一行“ANV_BO_ALLOC_LOCAL_MEM”代码标记，有了它，光追临时存储就会准确地放在显存之中，从而带来性能激增，或者说恢复正常。</strong></p><p>其实，Intel 2020年底就开始在开源驱动中支持Vulkan光追，以迎接Alchemist Arc A系列独立显卡的发布，但时至今日还在打磨之中。</p><p>Intel Mesa 22.2版开源驱动加入了不少光追相关修复、优化，还有其他大量改进，<strong>预计8月底发布稳定版本。</strong></p><p><a href="https://img1.mydrivers.com/img/20220723/1a098fe94f8649578d06abd200bc60a3.jpg" style="text-align: -webkit-center;" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0723/e952b35add37aed.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0723/e952b35add37aed.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0723/e952b35add37aed.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            