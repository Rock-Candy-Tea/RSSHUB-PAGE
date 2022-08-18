
---
title: 'Flutter_Dart release 模式下屏蔽 debugPrint 与 print 输出 (droidyue.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=4837'
author: 技术头条
comments: false
date: 2022-08-18 15:18:58
thumbnail: 'https://picsum.photos/400/300?random=4837'
---

<div>   
当我们在写 Flutter，Dart程序时，release 模式下，我们很奇怪的发现debugPrint和 print 这两个的输出内容，还是能够通过 flutter logs 展示出来。这一点尤其在端上暴露的问题要严重一些，比如涉及到一些敏感信息的日志打印。

本文，将会有两个超级简单的方法，来实现对这些输出的屏蔽，并且是专门治理 release 模式下的问题，debug 模式不受影响。
    
</div>
            