
---
title: 'Java IO类型 (it.deepinmind.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6715'
author: 技术头条
comments: false
date: 2022-05-05 05:16:54
thumbnail: 'https://picsum.photos/400/300?random=6715'
---

<div>   
描述IO类型时经常会交替地使用非阻塞、异步等术语，但这两个词是有着很大的区别的。本文将从理论和实践两个方面来说明下Java编程里的非阻塞和异步IO。

TCP和UDP协议使用了套接字进行双端通信。Java的套接字 API则是底层操作系统具体实现的的适配器。兼容POSIX规范的操作系统（如Unix, Linux, Mac OS X, BSD, Solaris， AIX等）中使用的socket通信被称作伯克利套接字（Berkeley sockets）。Windows中的套接字叫winsock，它也是基于伯克利套接字，但增加了额外的功能用于支持windows的编程模型。
    
</div>
            