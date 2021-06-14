
---
title: 'JVM优化之逃逸分析及锁消除 (it.deepinmind.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2546'
author: 技术头条
comments: false
date: 2021-06-14 03:10:09
thumbnail: 'https://picsum.photos/400/300?random=2546'
---

<div>   
逃逸分析——我们在上一篇文章中所介绍的由编译器完成的一项的分析技术——使得删除锁的优化成为了可能。如果它能确认某个加锁的对象不会逃逸出局部作用域，就可以进行锁删除。这意味着这个对象同时只可能被一个线程访问，因此也就没有必要防止其它线程对它进行访问了。这样的话这个锁就是可以删除的。这个便叫做锁消除，本文是JVM实现机制的系列文章，这也正是今天要讲的主题。

众所周知，java.lang.StringBuffer是一个使用同步方法的线程安全的类，它可以用来很好地诠释锁消除。StringBuffer是Java1.0的时候开始引入的，可以用来高效地拼接不可变的字符串对象。它对所有append方法都进行了同步操作，以确保当多个线程同时写入同一个StringBuffer对象的时候也能够保证构造中的字符串可以安全地创建出来。
    
</div>
            