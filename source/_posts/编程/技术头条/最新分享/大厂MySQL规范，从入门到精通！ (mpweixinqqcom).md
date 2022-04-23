
---
title: '大厂MySQL规范，从入门到精通！ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=617'
author: 技术头条
comments: false
date: 2022-04-23 02:27:20
thumbnail: 'https://picsum.photos/400/300?random=617'
---

<div>   
没有特殊要求（即Innodb无法满足的功能如：列存储，存储空间数据等）的情况下，所有表必须使用Innodb存储引擎（mysql5.5之前默认使用Myisam，5.6以后默认的为Innodb）Innodb 支持事务，支持行级锁，更好的恢复性，高并发下性能更好
    
</div>
            