
---
title: '卡巴斯基报告：黑客利用Windows 11镜像传播恶意程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0724/eef8ba5b7e7c3a3.jpg'
author: cnBeta
comments: false
date: Sat, 24 Jul 2021 01:57:47 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0724/eef8ba5b7e7c3a3.jpg'
---

<div>   
在面向 Windows Insider 项目成员正式发布之前，Windows 11 的系统镜像就已经在网络上偷跑。而偷跑的镜像链接也成为了黑客眼中的攻击武器。<strong>援引卡巴斯基报道，网络上充斥各种包含恶意软件的 ISO 镜像。</strong><br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0724/eef8ba5b7e7c3a3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0724/eef8ba5b7e7c3a3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在卡巴斯基报告的一个典型例子中，就是容量为 1.75GB 的 86307_<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 build 21996.1 x64 + activator.exe 文件。虽然从容量和文字描述来看非常正常、可信，但实际上该文件都是由一个 DLL 文件组成，其中包含了大量无用信息。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0724/53e697e23a44196.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0724/53e697e23a44196.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">打开这个可执行文件，就会启动安装程序，它看起来像一个普通的Windows安装向导。然而，它的主要目的是下载和运行另一个可执行文件。第二个可执行文件也是一个安装程序，它甚至附带一份许可协议（很少有人阅读），称其为"86307_windows 11 build 21996.1 x64+激活器的下载管理器"，并指出它还将安装一些赞助软件。如果你接受该协议，各种恶意程序将被安装在你的机器上。</p><p style="text-align: left;">卡巴斯基表示，他们已经检测到几百次使用类似Windows 11相关计划的感染尝试。这些恶意软件的很大一部分由下载器组成，其任务是下载和运行其他程序。这些其他程序可能非常广泛--从相对无害的广告软件（我们的解决方案将其归类为非病毒）到成熟的木马程序、密码窃取程序、漏洞和其他讨厌的东西。</p>   
</div>
            