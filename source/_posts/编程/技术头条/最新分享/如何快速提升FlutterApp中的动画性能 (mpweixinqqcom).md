
---
title: '如何快速提升FlutterApp中的动画性能 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9403'
author: 技术头条
comments: false
date: 2021-05-02 00:18:24
thumbnail: 'https://picsum.photos/400/300?random=9403'
---

<div>   
当看到这个效果图的时候，很快啊，啪一下思路就来了。涉及到动画，有状态，用 StatefulWidget ，State 里创建一个 AnimationController，用两个 Container 对应两个圈，外圈的 Container 的宽高监听动画跟着更新就行。
    
</div>
            