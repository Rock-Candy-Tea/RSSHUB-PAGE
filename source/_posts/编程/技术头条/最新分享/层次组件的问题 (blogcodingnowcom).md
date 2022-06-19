
---
title: '层次组件的问题 (blog.codingnow.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8826'
author: 技术头条
comments: false
date: 2022-06-19 12:15:12
thumbnail: 'https://picsum.photos/400/300?random=8826'
---

<div>   
最近思考了 ECS 框架中的一些问题。

    具体业务中，有许多组件的构成非常复杂，本质上数据是有层次结构的。用一个二维表的结构很难清晰表述。它还牵扯到另一个问题：是否需要支持一个实体有多个统一类型的组件。例如，玩家实体身上多个装备栏、多个技能 Buf 该如何表达？
    
</div>
            