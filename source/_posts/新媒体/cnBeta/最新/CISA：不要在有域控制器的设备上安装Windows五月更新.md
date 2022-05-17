
---
title: 'CISA：不要在有域控制器的设备上安装Windows五月更新'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0517/b1f72efc8f97e4d.webp'
author: cnBeta
comments: false
date: Tue, 17 May 2022 07:18:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0517/b1f72efc8f97e4d.webp'
---

<div>   
在本月补丁星期二活动日放出的累积更新中，微软修复了追踪号为 CVE-2022-26925 的 Windows Local Security
Authority (LSA) 欺骗漏洞。这个严重性很高的漏洞使未经认证的攻击者能够匿名调用一个方法，并迫使域控制器（DC）通过 NTLM
对他们进行认证。在最坏的情况下，这可能导致权限提升，攻击者控制整个域。<br>
<p style="text-align: left;">这个漏洞是很重要的，因为美国网络安全和基础设施安全局（CISA）曾规定，联邦民用行政部门机构（FCEB）应在三周内安装这些更新，以保护自己免受这个攻击面和其他攻击。然而，它现在已经取消了这一要求，因为最新的"补丁星期二"更新在安装到 DC 上时也会引起认证问题。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0517/b1f72efc8f97e4d.webp" alt="knqh7bx9.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">公告上的说明是这样的:</p><blockquote style="text-align: left;"><p style="text-align: left;">在客户端 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 设备和非域控制器 Windows 服务器上安装 2022 年5月10日发布的更新，不会导致这个问题，仍然强烈鼓励。这个问题只影响到安装在作为域控制器的服务器上的2022年5月10日的更新。组织应该继续对客户端Windows设备和非域控制器Windows服务器应用更新。</p></blockquote><p style="text-align: left;">在关于这个问题的咨询中，微软说：“在你的域控制器上安装 2022 年 5 月 10
日发布的更新后，你可能会在服务器或客户端看到网络策略服务器（NPS）、路由和远程访问服务（RRAS）、Radius、可扩展认证协议（EAP）和受保护可扩展认证协议（PEAP）等服务的认证失败。已发现一个与域控制器如何处理证书与机器账户的映射有关的问题”。</p><p style="text-align: left;"><strong>微软分享了受影响平台列表</strong></p><p style="text-align: left;"><strong>客户端：</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows 11 Version 21H2</p><p style="text-align: left;">● Windows 10 Version 21H2</p><p style="text-align: left;">● Windows 10 Version 21H1</p><p style="text-align: left;">● Windows 10 Version 20H2</p><p style="text-align: left;">● Windows 10 Version 1909</p><p style="text-align: left;">● Windows 10 Version 1809</p><p style="text-align: left;">● Windows 10 Enterprise LTSC 2019</p><p style="text-align: left;">● Windows 10 Enterprise LTSC 2016</p><p style="text-align: left;">● Windows 10 Version 1607</p><p style="text-align: left;">● Windows 10 Enterprise 2015 LTSB</p><p style="text-align: left;">● Windows 8.1</p><p style="text-align: left;">● Windows 7 SP1</p></blockquote><p style="text-align: left;"><strong>服务器:</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows Server 2022</p><p style="text-align: left;">● Windows Server Version 20H2</p><p style="text-align: left;">● Windows Server Version 1909</p><p style="text-align: left;">● Windows Server Version 1809</p><p style="text-align: left;">● Windows Server 2019</p><p style="text-align: left;">● Windows Server 2016</p><p style="text-align: left;">● Windows Server 2012 R2</p><p style="text-align: left;">● Windows Server 2012</p><p style="text-align: left;">● Windows Server 2008 R2 SP1</p><p style="text-align: left;">● Windows Server 2008 SP2</p></blockquote><p style="text-align: left;">这些问题主要是由 Windows Kerberos 和活动目录域服务的两个补丁引起的，分别被追踪为 CVE-2022-26931 和 CVE-2022-26923。而由于不可能在你想安装的补丁中进行挑选，CISA 不再鼓励 IT 管理员不在 DC 上安装5月的补丁星期二。</p><p style="text-align: left;">目前，微软已经提供了一个解决方法，包括手动映射证书。</p><p style="text-align: left;">同时，微软还提供了一个临时解决方案：</p><blockquote style="text-align: left;"><p style="text-align: left;">这个问题的首选缓解措施是手动将证书映射到活动目录中的机器账户。有关说明，请见<a href="https://support.microsoft.com/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16#bkmk_certmap" target="_blank">证书映射</a>。注意：对于将证书映射到活动目录中的用户或机器账户，其说明是相同的。</p><p style="text-align: left;">如果首选的缓解措施在你的环境中不起作用，请参见 <a href="https://support.microsoft.com/topic/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers-ad2c23b0-15d8-4340-a468-4d4f3b188f16" target="_blank">KB5014754-Windows 域控制器上基于证书的认证变化</a>，了解 Schannel 注册表密钥部分的其他可能缓解措施。注意：除了首选的缓解措施，任何其他缓解措施都可能降低或禁用安全加固。</p></blockquote><p style="text-align: left;">它还强烈强调，应用任何其他缓解措施都可能对你的组织的安全态势产生负面影响。鉴于CISA不鼓励FCEB完全在Windows服务器DC上安装5月补丁星期二的更新，微软可能希望尽快推出一个更永久的修复方案。</p>   
</div>
            