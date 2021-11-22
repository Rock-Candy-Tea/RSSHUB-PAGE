
---
title: '一文理解MySQL中的page页 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=3630'
author: 技术头条
comments: false
date: 2021-11-22 12:12:13
thumbnail: 'https://picsum.photos/400/300?random=3630'
---

<div>   
从InnoDB存储引擎的逻辑结构看，所有数据都被逻辑地存放在一个空间内，称为表空间(tablespace)，而表空间由段（sengment）、区（extent）、页（page）组成。在一些文档中extend又称块（block）。
    
</div>
            