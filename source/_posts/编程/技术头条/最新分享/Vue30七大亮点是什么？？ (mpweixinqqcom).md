
---
title: 'Vue3.0七大亮点是什么？？ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8284'
author: 技术头条
comments: false
date: 2022-02-26 06:11:22
thumbnail: 'https://picsum.photos/400/300?random=8284'
---

<div>   
在vue2中，虚拟dom是全量比较的。

在vue3中，增加了静态标记PatchFlag。在创建vnode的时候，会根据vnode的内容是否可以变化，为其添加静态标记PatchFlag。diff的时候，只会比较有PatchFlag的节点。PatchFlag是有类型的，比如一个可变化文本节点，会将其添加PatchFlag枚举值为TEXT的静态标记。这样在diff的时候，只需比对文本内容。需要比对的内容更少了。PatchFlag还有动态class、动态style、动态属性、动态key属性等枚举值。
    
</div>
            