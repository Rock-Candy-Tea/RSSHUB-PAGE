
---
title: 'Deno 如何同步获取指定目录下所有文件？ (www.jeffjade.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6840'
author: 技术头条
comments: false
date: 2021-03-30 12:11:09
thumbnail: 'https://picsum.photos/400/300?random=6840'
---

<div>   
在基于 Deno / Node.js 编写程序，时常会遇到类似这样的需求：“列出（遍历）目录下的所有文件，包括子目录“。如何实现这一点呢，很显然可以使用一些已写好的工具库，如 node-rd、node-walk、glob 等；但她们或多或少，都有些弊端，不方便使用；那么手动写一个方法，来实现“同步获取指定目录下所有文件“呢？本篇文章，即同大家一起探讨下这个问题。
    
</div>
            