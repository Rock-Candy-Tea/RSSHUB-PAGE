
---
title: '五月更新导致Windows域控制器认证失败'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0513/42f2b9253a1a0f1.webp'
author: cnBeta
comments: false
date: Fri, 13 May 2022 08:29:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0513/42f2b9253a1a0f1.webp'
---

<div>   
在本月补丁星期二更新发布之后，微软发出警告：安装 KB5013943 更新可能导致各种 Windows 服务的认证问题。该更新于 5 月 10
日发布，主要修复安全模式下的屏幕闪烁问题。<strong>但是，除了给一些用户带来错误信息外，KB5013943 更新还导致了 Windows
域控制器的认证失败。</strong><br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0513/42f2b9253a1a0f1.webp" alt="79cl197z.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在关于这个问题的咨询中，微软说：“在你的域控制器上安装 2022 年 5 月 10 日发布的更新后，你可能会在服务器或客户端看到网络策略服务器（NPS）、路由和远程访问服务（RRAS）、Radius、可扩展认证协议（EAP）和受保护可扩展认证协议（PEAP）等服务的认证失败。已发现一个与域控制器如何处理证书与机器账户的映射有关的问题”。</p><p style="text-align: left;">该公司指出，这个问题只影响到安装2022年5月10日更新并作为域控制器的服务器上。任何在客户端 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 设备和非域控制器 Windows 服务器上安装更新的人应该不会遇到同样的问题。</p><p style="text-align: left;"><strong>微软分享了受影响平台列表</strong></p><p style="text-align: left;"><strong>客户端：</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows 11 Version 21H2</p><p style="text-align: left;">● Windows 10 Version 21H2</p><p style="text-align: left;">● Windows 10 Version 21H1</p><p style="text-align: left;">● Windows 10 Version 20H2</p><p style="text-align: left;">● Windows 10 Version 1909</p><p style="text-align: left;">● Windows 10 Version 1809</p><p style="text-align: left;">● Windows 10 Enterprise LTSC 2019</p><p style="text-align: left;">● Windows 10 Enterprise LTSC 2016</p><p style="text-align: left;">● Windows 10 Version 1607</p><p style="text-align: left;">● Windows 10 Enterprise 2015 LTSB</p><p style="text-align: left;">● Windows 8.1</p><p style="text-align: left;">● Windows 7 SP1</p></blockquote><p style="text-align: left;"><strong>服务器:</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows Server 2022</p><p style="text-align: left;">● Windows Server Version 20H2</p><p style="text-align: left;">● Windows Server Version 1909</p><p style="text-align: left;">● Windows Server Version 1809</p><p style="text-align: left;">● Windows Server 2019</p><p style="text-align: left;">● Windows Server 2016</p><p style="text-align: left;">● Windows Server 2012 R2</p><p style="text-align: left;">● Windows Server 2012</p><p style="text-align: left;">● Windows Server 2008 R2 SP1</p><p style="text-align: left;">● Windows Server 2008 SP2</p></blockquote><p style="text-align: left;">虽然微软没有说什么时候会有一个修复方案，但该公司表示，它“目前正在调查，并将在即将发布的版本中提供一个更新”。</p><p style="text-align: left;">同时，微软还提供了一个临时解决方案：</p><blockquote style="text-align: left;"><p style="text-align: left;">这个问题的首选缓解措施是手动将证书映射到活动目录中的机器账户。有关说明，请见<a href="https://support.microsoft.com/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16#bkmk_certmap" target="_blank">证书映射</a>。注意：对于将证书映射到活动目录中的用户或机器账户，其说明是相同的。</p><p style="text-align: left;">如果首选的缓解措施在你的环境中不起作用，请参见 <a href="https://support.microsoft.com/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16" target="_blank">KB5014754-Windows 域控制器上基于证书的认证变化</a>，了解 Schannel 注册表密钥部分的其他可能缓解措施。注意：除了首选的缓解措施，任何其他缓解措施都可能降低或禁用安全加固。</p></blockquote>   
</div>
            