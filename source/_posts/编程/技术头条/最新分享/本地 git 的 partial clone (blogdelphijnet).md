
---
title: '本地 git 的 partial clone (blog.delphij.net)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6389'
author: 技术头条
comments: false
date: 2021-06-14 01:55:18
thumbnail: 'https://picsum.photos/400/300?random=6389'
---

<div>   
partial clone 是 git 的一项旨在减少空间和网络带宽占用的特性。它会跳过下载那些可能不会用到的 git 对象，而是仅仅在需要时才去下载。对于网络延迟较低且带宽不愁的用户来说，这样做往往会节省掉不少不必要的磁盘空间占用，而代价是可能失去离线访问的能力。除此之外，有些操作，例如 git blame 或者 git log -p 很可能会需要与服务器交互，从而会变得略慢一些。

    比较有用的场景是在使用某些历史比较久，或是对文件整体替换较多，而大部分情况下只关注最新版本的代码库。与较早的 --depth 1 相比，partial clone的优点在于想要访问历史时仍然可以像正常的clone一样访问。

    今天闲来无事打算把机房的服务器稍微升级一下，于是顺手弄了一下 partial clone，稍微记一笔作弊条。
    
</div>
            