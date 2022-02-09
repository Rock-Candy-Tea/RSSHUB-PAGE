
---
title: 'C 中访问 Lua 配置表的优化 (blog.codingnow.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=1292'
author: 技术头条
comments: false
date: 2022-02-09 11:06:55
thumbnail: 'https://picsum.photos/400/300?random=1292'
---

<div>   
这两天写代码时用到之前写的一个对 Lua 配置表的 cache 模块 。感觉用起来还是不够简洁方便。我今天动手重新设计了一下。

需求是这样的：

项目有非常多的配置信息保存在 Lua 的 （树状层级的）table 中，大部分逻辑代码直接用 Lua 的语法便可直接访问。但是，有少量有性能要求的业务是在 C 中实现的，C function 中也需要读取这些存放在 Lua 中的配置数据。

配置项随着项目开发，变更非常频繁。如果我设计一个小语言，定义出配置表，用代码生成的方式把表项翻译成对应的 C/C++ 结构，再在 C side 根据 Lua 中的数据重建一组 C 数据也未尝不可。这就是 google protobuf 官方采用的方式（用代码生成的方式，根据数据的 schema 构建出 C++ 类，让 C++ 可以方便访问这些数据）。

但我不想搞得这么复杂（浪费？
    
</div>
            