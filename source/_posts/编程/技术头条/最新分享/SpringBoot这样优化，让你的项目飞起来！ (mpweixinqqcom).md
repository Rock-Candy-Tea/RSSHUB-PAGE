
---
title: 'SpringBoot这样优化，让你的项目飞起来！ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6965'
author: 技术头条
comments: false
date: 2022-06-30 11:07:44
thumbnail: 'https://picsum.photos/400/300?random=6965'
---

<div>   
针对上述的优化点来说，首先线程数是一个重点，初始线程数和最大线程数，初始线程数保障启动的时候，如果有大量用户访问，能够很稳定的接受请求。

而最大线程数量用来保证系统的稳定性，而超时时间用来保障连接数不容易被压垮，如果大批量的请求过来，延迟比较高，不容易把线程打满。这种情况在生产中是比较常见的 ，一旦网络不稳定，宁愿丢包也不愿意把机器压垮。
    
</div>
            