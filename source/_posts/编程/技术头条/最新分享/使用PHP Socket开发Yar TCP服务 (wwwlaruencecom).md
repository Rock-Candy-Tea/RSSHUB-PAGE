
---
title: '使用PHP Socket开发Yar TCP服务 (www.laruence.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=721'
author: 技术头条
comments: false
date: 2022-05-07 12:15:43
thumbnail: 'https://picsum.photos/400/300?random=721'
---

<div>   
Yar支持HTTP和TCP俩种Transporter， HTTP的是基于CURL，PHP中的Yar默认就是走的HTTP Transporter， 这个大家应该都不陌生， 但是基于TCP的， 可能大家会用的少一些。

事实上，我6年前也写过一个C的Yar server框架，叫做Yar-c, 代码地址在Yar-C at Github, 当时我们用这个框架，实现了高性能的微博白名单等服务，以供PHP端使用Yar Client来调用。

只不过，Yar C需要用C来写Handle， 可能对于不少PHPer来说，会稍微有点陌生，那今天我们尝试用PHP来写一个TCP的Server，来介绍下如何实现对Yar RPC协议的处理， 这个例子可以方便的结合Swoole等异步PHP框架，实现一个高性能的Yar TCP Server。 这个过程中， 会让大家了解Yar的RPC通信协议，以及捎带了解下Socket编程。
    
</div>
            