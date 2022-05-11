
---
title: '如何通过缓存来提升系统性能 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2665'
author: 技术头条
comments: false
date: 2022-05-11 15:10:44
thumbnail: 'https://picsum.photos/400/300?random=2665'
---

<div>   
在系统中最消耗性能的地方就是对数据库的访问了，一般来说，增、删、改操作不会出现什么性能问题，除非索引太多，并且数据量有十分庞大的情况下，这三个操作才会导致性能问题。一般可以限制单表索引的数量来提升性能，比如单表的索引数量不能超过5个。
    
</div>
            