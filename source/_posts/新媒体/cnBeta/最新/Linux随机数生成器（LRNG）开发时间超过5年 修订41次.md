
---
title: 'Linux随机数生成器（LRNG）开发时间超过5年 修订41次'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Wed, 14 Jul 2021 09:57:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>作为/dev/random的新替代品，"Linux随机数生成器"（LRNG）的工作现在已经进行到第41次修订，并且已经开发了超过5年。</strong>Stephan
Müller今天发布了他对LRNG的最新补丁系列，作为他提出的处理/dev/random的新方法，同时也是对现有随机数生成器的API/ABI兼容的替代品。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>与目前的/dev/random相比，LRNG的目标是要快 "达130%"，还有其他各种性能优化，各种加密处理的改进，可测试能力的提高，选项的更多可配置性，以及更现代的设计。</p><p>LRNG的v41补丁对初始播种代码进行了清理，将种子缓冲区归零，在熵值不足的情况下初始化熵值，加强了熵源配置，并对该随机数生成器代码进行了其他各种低级别的改进。</p><p>LRNG是否/何时最终被认为可以用于主线内核还有待观察，但那些对围绕新的Linux随机数发生器实现的这一漫长旅程感到好奇的人可以在内核邮件列表中找到今天的13个补丁系列。</p><p><strong>访问邮件列表了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/7822794.ITf6fX9eNu@positron.chronox.de/" _src="https://lore.kernel.org/lkml/7822794.ITf6fX9eNu@positron.chronox.de/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="ecdbd4dededbd5d8c2a5b88ada8ab4d589a299ac9c839f85989e8382c28f849e83828394c28889">[email protected]</span>/</a><br></p>   
</div>
            