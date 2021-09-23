
---
title: 'Chrome安全团队正计划牺牲部分性能 换取更安全的使用环境'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0831/10fe8576d94a11e.jpg'
author: cnBeta
comments: false
date: Thu, 23 Sep 2021 04:11:25 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0831/10fe8576d94a11e.jpg'
---

<div>   
安全是一场猫捉老鼠的游戏。攻击者会不断创新攻击方式，而浏览器厂商也在采取新的防御措施以保持领先。Chrome
在沙盒和网站隔离的基础上不断打造更强大的多进程架构。通过整合模糊处理，为用户构建起更牢固的安全防线。但这道主要防线已达到了极限，Google
不能再仅仅依靠这种策略来打败野蛮的攻击。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/thumb/article/2021/0831/10fe8576d94a11e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0831/10fe8576d94a11e.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Chrome 软件工程师在去年 5 月 23 日发布的报告中指出，70% 的严重安全漏洞都来自内存安全问题。更重要的是，Chrome 浏览器有一半的安全缺陷是“use-after-free”漏洞，这些安全问题来自于对内存指针的不正确管理，使 Chrome 浏览器进一步受到攻击。</p><p style="text-align: left;"><strong>牺牲性能来换取安全</strong></p><p style="text-align: left;">今天，Chrome 安全团队公布他们对浏览器内存安全问题的解决方案，其中一个涉及到以性能为代价。Chrome 浏览器的安全团队由 Andrew Whalley、Dana Jansens、Adrian Taylor 和 Nasko Oskov 组成。该团队进一步列举了所提到的来自内存安全缺陷的安全漏洞的统计数据。</p><p style="text-align: left;">这三个方案包括</p><blockquote style="text-align: left;"><p style="text-align: left;">● 通过 compile-time 检查指针是否正确让 C++ 变得更安全</p><p style="text-align: left;">● 通过 runtime 检查指针是否正确让 C++ 变得更安全</p><p style="text-align: left;">● 研究在代码库中的某些代码使用内存安全语言</p></blockquote><p style="text-align: left;">因此，为了应对浏览器内存管理中普遍存在的错误，Chrome 浏览器的开发人员提出了通过增加 runtime 检查使其更加安全的想法。</p><p style="text-align: left;">尽管 runtime 检查使 Chrome 的 C++ 语言比以往任何时候都更安全，不受内存安全漏洞的影响，但它也有一些性能成本。安全团队进一步写道：“检查指针的正确性在内存和 CPU 时间上是一个无限小的成本。但对于数百万个指针来说，它就会增加”。</p><p style="text-align: left;">也就是说，对内存缺陷的修复可能是以一些内存和CPU时间为代价。因此，影响了浏览器的整体性能。对于 Chrome 浏览器的用户来说，这种权衡变得更加明显，因为他们的设备并不具备最高性能的 CPU，而且内存不足。因此，额外的 runtime 检查可能会导致网页浏览的性能略微变慢。</p><p style="text-align: left;">然而，Chrome 安全团队仍然指出，它愿意就更安全但更慢的选项进行实验。但该团队也在努力为浏览器编写一种不同的语言，不需要额外的运行时间。</p>   
</div>
            