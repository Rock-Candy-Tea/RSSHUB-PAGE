
---
title: '改hosts不生效？教你清理Chrome的DNS缓存 (hessian.cn)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=4258'
author: 技术头条
comments: false
date: 2022-05-27 07:09:46
thumbnail: 'https://picsum.photos/400/300?random=4258'
---

<div>   
在进行web开发的时候，我们经常会修改hosts文件进行测试，但是偶尔会发现改了hosts文件并不能立刻生效。这是由于浏览器自身对DNS（域名指向）是有进行缓存的，除了缓存之外，由于HTTP1.1支持连接复用，如果之前打开过这个页面，那么即使清理了DNS缓存也会因为复用连接再继续连接到旧的域名指向地址。如果出现连接被复用的情况就需要手动关闭活跃连接了。
    
</div>
            