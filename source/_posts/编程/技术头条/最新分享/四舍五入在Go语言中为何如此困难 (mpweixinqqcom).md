
---
title: '四舍五入在Go语言中为何如此困难 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2618'
author: 技术头条
comments: false
date: 2022-07-24 05:14:55
thumbnail: 'https://picsum.photos/400/300?random=2618'
---

<div>   
在 Go 语言中这似乎成为了难题，在 stackoverflow 上搜索 [go] Round 会存在大量相关提问，Go 1.10 开始才出现 math.Round 的身影，本以为 Round 的疑问就此结束，但是一看函数注释 Round returns the nearest integer, rounding half away from zero ，这是并不常用的 Round half away from zero 实现呀，说白了就是我们理解的 Round 阉割版，精度为 0 的 Round half up 实现，Round half away from zero 的存在是为了提供一种高效的通过二进制方法得结果，可以作为 Round 精度为 0 时的高效实现分支。
    
</div>
            