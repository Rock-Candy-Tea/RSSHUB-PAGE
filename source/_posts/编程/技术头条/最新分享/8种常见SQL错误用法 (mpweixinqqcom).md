
---
title: '8种常见SQL错误用法 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=7632'
author: 技术头条
comments: false
date: 2022-03-28 04:11:27
thumbnail: 'https://picsum.photos/400/300?random=7632'
---

<div>   
分页查询是最常用的场景之一，但也通常也是最容易出问题的地方。比如对于下面简单的语句，一般 DBA 想到的办法是在 type, name, create_time 字段上加组合索引。这样条件排序都能有效的利用到索引，性能迅速提升。
    
</div>
            