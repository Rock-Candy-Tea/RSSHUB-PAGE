
---
title: '【死磕 Redis】—– 如何排查 Redis 中的慢查询 (cmsblogs.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=1867'
author: 技术头条
comments: false
date: 2022-05-13 14:13:35
thumbnail: 'https://picsum.photos/400/300?random=1867'
---

<div>   
我们知道 MySQL 提供了慢查询日志帮助我们定位系统存在的慢操作，同样在 Redis 里面也提供了类似的功能。所谓慢查询日志就是系统记录那些执行时间超过预设阀值的命令，包括发生时间、耗时、命令的详细信息等相关信息都记录下来。

    慢查询的作用：通过慢查询分析，找到有问题的命令进行优化。

    Redis 执行命令分为四个步骤：发送命令、命令排队、执行命令、返回结果。需要注意的是，慢查询只统计步骤 3 的时间,所以没有慢查询并不代表客户端没有超时问题。
    
</div>
            