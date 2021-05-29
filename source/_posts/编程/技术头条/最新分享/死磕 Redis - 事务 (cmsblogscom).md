
---
title: '死磕 Redis - 事务 (cmsblogs.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=7019'
author: 技术头条
comments: false
date: 2021-05-29 12:23:54
thumbnail: 'https://picsum.photos/400/300?random=7019'
---

<div>   
Redis 通过 MULTI、EXEC、DISCARD、WATCH 、UNWATCH 来实现事务功能，Redis 事务具备如下几个特性：

1、Redis 会将事务中的多个命令一次性、按顺序一次执行，在执行期间可以保证不会中断事务去执行其他命令；
2、Redis 的事务机制是不能保证原子性的，它只保证隔离性和一致性。
    
</div>
            