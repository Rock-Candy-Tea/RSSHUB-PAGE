
---
title: '给 ECS 增加分组功能 (blog.codingnow.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8475'
author: 技术头条
comments: false
date: 2022-06-20 02:50:15
thumbnail: 'https://picsum.photos/400/300?random=8475'
---

<div>   
目前，我们用 ECS 管理游戏引擎中的对象。当游戏场景大到一定程度，就需要有一个机制来快速筛选出需要渲染的对象子集。换句话说，如果你创建了 100K 个 Entity ，但是只有 1K 个 Entity 需要同时渲染，虽然遍历所有可渲染对象的成本最小是 O(n) ，但这个 n 是 100K 这个数量级，还是 1K 这个数量级，区别还是很大的。

        我们的 ECS 系统已经支持了 tag 这个特性，可以利用 visible tag 做主 key 快速筛选可见对象。但当镜头移动时，需要重置这些 tag 又可能有性能问题。重置这些 visible tags 怎样才能避免在 100K 这个数量级的 O(n) 复杂度下工作？
    
</div>
            