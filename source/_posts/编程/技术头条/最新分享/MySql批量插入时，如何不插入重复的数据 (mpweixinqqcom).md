
---
title: 'MySql批量插入时，如何不插入重复的数据 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=5621'
author: 技术头条
comments: false
date: 2022-02-18 12:13:53
thumbnail: 'https://picsum.photos/400/300?random=5621'
---

<div>   
业务很简单：需要批量插入一些数据，数据来源可能是其他数据库的表，也可能是一个外部excel的导入

那么问题来了，是不是每次插入之前都要查一遍，看看重不重复，在代码里筛选一下数据，重复的就过滤掉呢？
    
</div>
            