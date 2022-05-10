
---
title: 'AMD为10年前的GCN显卡添加光线追踪驱动支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0510/38fc19bbe632465.png'
author: cnBeta
comments: false
date: Tue, 10 May 2022 06:04:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0510/38fc19bbe632465.png'
---

<div>   
早些时候，曾有消息称，AMD将为10年前的GCN显卡用户加入RSR技术的支持，轻松实现3倍的性能提升。根据Radeon Vulkan新驱动程序RADV的源码，<strong>AMD并不满足于仅为GCN加入RSR技术，而是计划为其加入Vulkan光线追踪的驱动支持。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2022/0510/38fc19bbe632465.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0510/38fc19bbe632465.png" title alt="linux-raytracing.png" referrerpolicy="no-referrer"></a></p><p>虽然在没有独立单元的老显卡上，运行光追会相对比较吃力，但这也确实能够提升画面质量，带来跟好的游戏体验。</p><p>目前，已经有部分用户对此次更新进行了测试体验，在一些需要使用光线追踪的开发项目中，该技术的加入确实能够大幅提升使用体验：</p><p><a href="https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/16203" _src="https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/16203" target="_blank">https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/16203</a><br></p><p>独立开发者Konstantin Seurer的测试中显示，在GravityMark基准测试中，<strong>打上了Radeon RADV LBVH补丁后的GCN显卡，运行速度从原有的13FPS提升到了250FPS，成效显著。</strong></p><p>不过，需要注意的是，<strong>现阶段很多游戏对此次更新的兼容性并不理想</strong>，想要获得更好的游戏体验还需要一段时间。</p>   
</div>
            