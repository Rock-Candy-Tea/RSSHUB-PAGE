
---
title: 'PHP FFI详解 - 一种全新的PHP扩展方式 (www.laruence.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=6511'
author: 技术头条
comments: false
date: 2021-05-29 08:48:03
thumbnail: 'https://picsum.photos/400/300?random=6511'
---

<div>   
随着PHP7.4而来的有一个我认为非常有用的一个扩展:PHP FFI(Foreign Function interface), 引用一段PHP FFI RFC中的一段描述：For PHP, FFI opens a way to write PHP extensions and bindings to C libraries in pure PHP.

是的，FFI提供了高级语言直接的互相调用，而对于PHP来说，FFI让我们可以方便的调用C语言写的各种库。

其实现有大量的PHP扩展是对一些已有的C库的包装，比如常用的mysqli, curl, gettext等，PECL中也有大量的类似扩展。

传统的方式，当我们需要用一些已有的C语言的库的能力的时候，我们需要用C语言写wrapper，把他们包装成扩展，这个过程中就需要大家去学习PHP的扩展怎么写，当然现在也有一些方便的方式，比如Zephir. 但总还是有一些学习成本的，而有了FFI以后，我们就可以直接在PHP脚本中调用C语言写的库中的函数了。

而C语言几十年的历史中，积累了大量的优秀的库，FFI直接让我们可以方便的享受这个庞大的资源了。
    
</div>
            