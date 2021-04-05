
---
title: 'AMD承认Zen 3 CPU易受新型类Spectre攻击影响'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210405/1617570814_340685.jpg'
author: 3DMGame
comments: false
date: Sun, 04 Apr 2021 21:13:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210405/1617570814_340685.jpg'
---

<div>   
<p style="text-indent:2em;">
AMD已经证实，Zen 3 CPU内部的微架构优化可以被利用，其方式类似于几代前困扰英特尔CPU的Spectre漏洞。禁用该优化是可能的，但会带来性能上的损失，AMD认为除了最关键的处理器部署外，其他所有处理器都不值得这样做。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210405/1617570814_340685.jpg" alt="AMD承认Zen 3 CPU易受新型类Spectre攻击影响" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
在最近发布的一份名为《AMD预测存储转发的安全分析》的白皮书中，AMD描述了该漏洞的性质，并讨论了相关的后果。简单来说，预测性存储转发(PSF)的实现，由于其性质所致从而重新打开了之前受到Spectre v1、v2和v4威胁的攻击路线。
</p>
<p style="text-indent:2em;">
AMD将PSF描述为一种硬件优化，"旨在通过预测负载和存储之间的依赖关系来提高代码执行的性能"。与分支预测（一种启用了之前Spectre攻击的功能）一样，PSF进行预测，以使处理器更快地执行后续指令，然而当PSF做出错误的预测时，就会产生漏洞。
</p>
<p style="text-indent:2em;">
AMD表示，不正确的预测可能是两种情况的结果。"首先，有可能存储/负载对有一段时间的依赖性，但后来不再有依赖性。" 这种情况是自然发生的，因为存储和负载在程序执行过程中会发生变化。第二种情况发生在 "如果PSF预测器结构中有一个别名"，而这个别名在不该使用的时候被使用了。这两种情况都可以被恶意代码触发，至少理论上是这样。
</p>
<p style="text-indent:2em;">
Ryzen 5000和Epyc
7003系列处理器使用Zen 3架构，受此漏洞影响。
</p>
<p style="text-indent:2em;">
AMD写道："由于PSF推测仅限于当前程序上下文，因此不良PSF推测的影响与推测性存储旁路（Spectre v4）类似。"
</p>
<p style="text-indent:2em;">
与Spectre v4一样，当处理器的一项安全措施被错误的推测绕过时，该漏洞就会发生。与其他攻击相结合；AMD以Spectre v1为例，错误的预测会导致数据泄露。"这与其他Spectre类攻击的安全风险类似，"AMD表示。
</p>
<p style="text-indent:2em;">
依靠软件沙盒来保证安全的程序是最容易受到PSF攻击的。使用硬件隔离的程序 "可能被认为是安全的"，不会受到PSF攻击，因为PSF投机不会跨地址空间发生。它也不会跨权限域发生。
</p>
<p style="text-indent:2em;">
AMD发现，地址空间隔离等技术足以阻止PSF攻击，然而，如果需要的话，他们已经提供了禁用PSF的手段，甚至在每个线程的基础上。但由于安全风险 "很低"，而且 "AMD目前还没有发现任何代码会因为PSF行为而被认为是脆弱的"，他们普遍建议将启用PSF功能作为默认设置，即使在保护措施不可用的情况下。
</p>          
</div>
            