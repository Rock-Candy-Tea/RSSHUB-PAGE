
---
title: '带猜测的二分查找算法 (blog.codingnow.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=3682'
author: 技术头条
comments: false
date: 2022-05-11 14:09:56
thumbnail: 'https://picsum.photos/400/300?random=3682'
---

<div>   
我想用 C 实现一个内存紧凑的 ECS 框架，希望数据结构足够的简单，且能管理海量的对象。所以我让每个 component 就是一个不包含任何引用的 struct ，并带有一个 32bit 的 id 。并把这样的一个数据结构放在一块连续内存中。

        这个 id 没有对外暴露的 API （不是 entity id ），可以在运行过程中调整。如果两个不同类型的 component 有相同的 id ，即认为它们同属一个 entity 。id 的作用是管理 component 的生命期，以及在遍历 component 时，可以找到同个 entity 上其它的组件。
    
</div>
            