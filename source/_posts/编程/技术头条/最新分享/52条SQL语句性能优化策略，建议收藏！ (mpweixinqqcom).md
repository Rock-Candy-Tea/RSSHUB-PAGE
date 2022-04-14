
---
title: '52条SQL语句性能优化策略，建议收藏！ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6278'
author: 技术头条
comments: false
date: 2022-04-14 03:33:13
thumbnail: 'https://picsum.photos/400/300?random=6278'
---

<div>   
本文会提到 52 条 SQL 语句性能优化策略。

1、对查询进行优化，应尽量避免全表扫描，首先应考虑在 WHERE 及 ORDER BY 涉及的列上建立索引。

2、应尽量避免在 WHERE 子句中对字段进行 NULL 值判断，创建表时 NULL 是默认值，但大多数时候应该使用 NOT NULL，或者使用一个特殊的值，如 0，-1 作为默认值。
    
</div>
            