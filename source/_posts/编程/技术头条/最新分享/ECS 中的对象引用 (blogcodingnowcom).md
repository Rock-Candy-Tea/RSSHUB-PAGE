
---
title: 'ECS 中的对象引用 (blog.codingnow.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=1850'
author: 技术头条
comments: false
date: 2022-06-21 13:35:13
thumbnail: 'https://picsum.photos/400/300?random=1850'
---

<div>   
我们很难避免在 ECS 系统中相互引用 Entity 。而我对 ECS 模式的使用是鼓励去引用的。为此，我对许多常见依赖引用的模式给了对应的解决方案。

    最近的一个 luaecs 开发版本中，提供了一种 Lua 层面的引用方案 ：在创建 Entity 时，可以指定一个 table 作为该对象的引用。系统会更新它，让它保持为一个有效的（形如 select 过程中的）迭代器。这样，业务层就可以随时通过它 sync entity 中的数据。

    我一直不是太喜欢这个方案，所以一直再考虑不同的解决方法。念念不忘 必有回响。昨天，我尝试了一个新的、更满意一点的方案。
    
</div>
            