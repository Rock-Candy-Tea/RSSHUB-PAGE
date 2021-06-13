
---
title: 'Flutter MVVM 实用框架 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9337'
author: 技术头条
comments: false
date: 2021-06-13 01:55:48
thumbnail: 'https://picsum.photos/400/300?random=9337'
---

<div>   
基于Provider实现MVVM框架，常用的方式是 ViewModel 继承 ChangeNotifier ，再通过 ChangeNotifierProvider 提供给子Widget，ViewModel数据刷新通过调用 notifyListeners() 来通知Widget进行刷新，Widget 通过 Provider.of 、Consumer、Selector 来监听数据变化重新 build 更新UI。这种方式存在的问题有：
    
</div>
            