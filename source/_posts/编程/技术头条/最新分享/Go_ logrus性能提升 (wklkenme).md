
---
title: 'Go_ logrus性能提升 (wklken.me)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8484'
author: 技术头条
comments: false
date: 2022-07-25 04:41:17
thumbnail: 'https://picsum.photos/400/300?random=8484'
---

<div>   
在Go项目中，logrus是一个相对完备的第三方日志库，用起来非常顺手, 特别是WithField/WithFields/WithError。我们开发一些对性能要求非常高的应用，例如API网关/权限服务等，需要记录流水日志，此时日志库的性能直接会影响整体接口性能，所以针对性地做了一些优化。
    
</div>
            