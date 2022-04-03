
---
title: '写 C C++ 语言时候，如果每次申请内存就把 Free 内存的代码写上，是否能有效避免内存泄漏？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=8540'
author: 知乎
comments: false
date: Sun, 03 Apr 2022 06:02:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=8540'
---

<div>   
DBinary的回答<br><br><p data-pid="OZ59Zumj">不能</p><p data-pid="pRNclQQ8">1.释放内存的代码可能存在后面多个条件分支之上，如果逻辑逻辑考虑不全面，就可能导致泄露。</p><p data-pid="WdYhsp3e">2.申请内存和释放内存可能并不在同一个函数，模块中，因此很多时候没办法写个申请就写好释放，所以这个办法很多时候实用性不高</p><p data-pid="yPSLCgQZ">3.RAII可以帮助你避免忘记释放内存，但无法完全让你避免内存泄露</p><p data-pid="z22kXOzZ">4.你也可以用类似树形结构来管理对象，父对象释放同时释放子对象，用程序设计框架的方式尽量避免内存泄露的可能</p><p data-pid="l-hRXaH1">5.你也可以用内存池的方式管理内存，某一模块或实例销毁时，直接销毁内存池或者可以看看内存池还有没有没释放的内存</p><p data-pid="F1fvo2OR">6.c/c艹内存管理是综合考虑的因素，不能仅依靠某一框架，语言特性来解决，和整个工程设计都有关系</p>  
</div>
            