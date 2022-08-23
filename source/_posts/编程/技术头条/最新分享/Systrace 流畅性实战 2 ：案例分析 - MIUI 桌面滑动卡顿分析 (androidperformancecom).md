
---
title: 'Systrace 流畅性实战 2 ：案例分析 - MIUI 桌面滑动卡顿分析 (androidperformance.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8505'
author: 技术头条
comments: false
date: 2022-08-23 03:34:24
thumbnail: 'https://picsum.photos/400/300?random=8505'
---

<div>   
Systrace 作为分析卡顿问题的第一手工具，给开发者提供了一个从手机全局角度去看问题的方式，通过 Systrace 工具进行分析，我们可以大致确定卡顿问题的原因：是系统导致的还是应用自身的问题

当然 Systrace 作为一个工具，再进行深入的分析的时候就会有点力不从心，需要配合 TraceView + 源码来进一步定位和解决问题，最后再使用 Systrace 进行验证

所以本文更多地是讲如何发现和分析卡顿问题，至于如何解决，就需要后续自己寻找合适的解决方案了，比如对比竞品的 Systrace 表现、优化代码逻辑、优化系统调度、优化布局等
    
</div>
            