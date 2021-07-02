
---
title: '将一个纯本地应用移植到Web端 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=4474'
author: 技术头条
comments: false
date: 2021-07-02 12:10:07
thumbnail: 'https://picsum.photos/400/300?random=4474'
---

<div>   
在研究一个奇怪的缓存错误（https://actualbudget.com/blog/cursed-caching-curious）时我得到了启发，于是去重新看了一下 Actual 是如何在 Web 端本地存储数据的。这里我需要解释一些历史背景：多年前，Actual 原本是一个单纯的桌面应用程序来着。这意味着我们的所有数据都会存储在本地，没有服务器，自然也不会在网络上存储任何内容。
    
</div>
            