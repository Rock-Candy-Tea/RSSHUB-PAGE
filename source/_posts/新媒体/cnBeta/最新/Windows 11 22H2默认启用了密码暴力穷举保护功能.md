
---
title: 'Windows 11 22H2默认启用了密码暴力穷举保护功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0721/718878c24291490.png'
author: cnBeta
comments: false
date: Thu, 21 Jul 2022 14:52:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0721/718878c24291490.png'
---

<div>   
Windows 11 22H2目前可供Windows Insider计划中的测试者们试用，它带来了大量的新功能和变化。其中一些改进乍看之下并不明显，用户必须深入挖掘才能发现它们，其中一个重要变化是改进了对暴力攻击的保护。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0721/718878c24291490.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>微软操作系统安全和企业副总裁David Weston最近在Twitter上介绍了<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11的新安全措施。该操作系统现在默认使用暴力攻击保护，在尝试猜测本地密码十次失败后有效锁定系统。暴力穷举攻击是不良分子利用进入系统的一种流行方式，他们有时会使用远程桌面协议（RDP），得手后直接开始控制计算机。</p><p>用户可以在本地组策略编辑器中查看新的策略，方法是导航到计算机配置>Windows设置>安全设置>账户锁定策略。默认情况下，Windows 11在十分钟内尝试猜测密码失败多于一定次数后就会锁定，IT管理员可以根据他们的需要配置这些值。</p><p><a href="https://static.cnbetacdn.com/article/2022/0721/21685a7c92e8f62.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0721/21685a7c92e8f62.jpg" title alt="FYI-dWYUcAAZ5GE.jpg" referrerpolicy="no-referrer"></a></p><p>值得一提的是，锁定策略并不是Windows 11独有的；它们也存在于早期的Windows版本中（尽管默认是禁用的）。随着Windows 11 22H2（从build 22528.1000和更高版本开始），微软打开了开关，让使用暴力穷举方式进入操作系统的难度大大增加。</p>   
</div>
            