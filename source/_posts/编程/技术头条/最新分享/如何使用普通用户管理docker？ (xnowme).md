
---
title: '如何使用普通用户管理docker？ (xnow.me)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6680'
author: 技术头条
comments: false
date: 2021-05-30 00:37:56
thumbnail: 'https://picsum.photos/400/300?random=6680'
---

<div>   
首先，比”如何使用普通用户管理docker“更重要的问题是：”为什么要使用普通用户管理docker“？

1、使用普通用户登录服务器执行管理操作才是符合运维规范的，而不是给所有人都授予root权限，这有利于权限管理的标准化。
2、恶意破坏很难避免，但是要尽量不让用户做傻事，虽然普通用户进入docker之后，可以拥有root身份，但是这是恶意操作，避免的难度太高。

接下来就是怎么让普通用户也能使用docker的配置步骤了。
    
</div>
            