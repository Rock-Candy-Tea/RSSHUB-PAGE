
---
title: 'Redis 如何设计及使用内存友好的数据结构？'
categories: 
 - 编程
 - GitChat
 - 最新文章
headimg: 'https://picsum.photos/400/300?random=7887'
author: GitChat
comments: false
date: Sun, 05 Sep 2021 09:07:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=7887'
---

<div>   
<p>Redis 作为内存数据库，高效地使用内存对 Redis 来说肯定是必不可少的。实际上主要通过两方面技术来保证。一方面是控制数据对内存的消耗，主要按照一定的淘汰策略自动淘汰（Evict）一些缓存数据，比如采用 LRU 将最近很少使用的...</p>  
</div>
            