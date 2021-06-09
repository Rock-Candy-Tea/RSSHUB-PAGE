
---
title: 'Redis 存储对象信息是用 Hash 还是 String (zhuanlan.zhihu.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=257'
author: 技术头条
comments: false
date: 2021-06-09 14:14:50
thumbnail: 'https://picsum.photos/400/300?random=257'
---

<div>   
Redis 内部使用一个 RedisObject 对象来表示所有的 key 和 value，RedisObject 中的 type，则是代表一个 value 对象具体是何种数据类型，它包含字符串（String）、链表（List）、哈希结构（Hash）、集合（Set）、有序集合（Sorted set）。
    
</div>
            