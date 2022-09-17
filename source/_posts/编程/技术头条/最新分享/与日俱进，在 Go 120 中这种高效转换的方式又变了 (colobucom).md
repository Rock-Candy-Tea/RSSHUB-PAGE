
---
title: '与日俱进，在 Go 1.20 中这种高效转换的方式又变了 (colobu.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2639'
author: 技术头条
comments: false
date: 2022-09-17 00:55:15
thumbnail: 'https://picsum.photos/400/300?random=2639'
---

<div>   
在 Go 1.19 的开发中, string.SliceHeader和string.StringHeader经历了一个生死存亡的争斗，这两个类型一度被标记为弃用(deprecated),但是这两个类型经常用在 slice of byte 和 string 高效互转的场景中，如果被标记为弃用，但是目前还没有可替代的方法，所以这两个类型又把弃用标记去掉了，如无意外，它们也会在 Go 1.20 再次被标记为弃用。
    
</div>
            