
---
title: '记 python 超时的一个坑 (www.felix021.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=3600'
author: 技术头条
comments: false
date: 2021-05-28 12:27:07
thumbnail: 'https://picsum.photos/400/300?random=3600'
---

<div>   
背景：
有一个 python 脚本调用 A 服务的 x 接口获取若干 GB 的数据（大量对象），读取和解析大约需要 5 分钟。
由于 x 接口的改造，需要改成调用 B 服务的 y 接口。
A、B 服务都是基于字节跳动的 KITE 框架开发的，通信协议是 thrift 0.9.2 。
    
</div>
            