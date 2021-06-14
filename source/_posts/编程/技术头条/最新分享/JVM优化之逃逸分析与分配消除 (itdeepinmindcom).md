
---
title: 'JVM优化之逃逸分析与分配消除 (it.deepinmind.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2351'
author: 技术头条
comments: false
date: 2021-06-14 03:10:09
thumbnail: 'https://picsum.photos/400/300?random=2351'
---

<div>   
在Java Magazine的前几期文章中，我们介绍了just-in- time (JIT) 编译技术的一些理论基础，以及如何使用Java Microbenching Harness（JMH）和开源工具JITWatch来进行可视化分析，以便搞清楚HotSpot VM的内部机制。在这期文章中，我们将要深入介绍一下逃逸分析（escape analysis）技术，这是JVM最有意思的优化手段之一。逃逸分析是JVM的一项自动分析变量作用域的技术，它可以用来实现某些特殊的优化，后续我们也会分析下这些优化。在开始之前，你只需要掌握一些HotSpot JVM的基本工作原理就可以了。
    
</div>
            