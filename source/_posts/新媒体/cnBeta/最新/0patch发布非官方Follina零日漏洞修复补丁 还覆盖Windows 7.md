
---
title: '0patch发布非官方Follina零日漏洞修复补丁 还覆盖Windows 7'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0602/4ab09ff5bdd21a3.webp'
author: cnBeta
comments: false
date: Thu, 02 Jun 2022 07:57:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0602/4ab09ff5bdd21a3.webp'
---

<div>   
本周曝光的 Follina 零日漏洞，一旦设备感染之后就可以在受害者计算机上远程执行代码。虽然微软在数周前已承认存在该漏洞，但是微软至今尚未发布有效的漏洞修复补丁，只是提供了比较详细的解决方案。<strong>所幸的是，第三方公司提供了相关的补丁。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0602/4ab09ff5bdd21a3.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0602/810b0efc2127c1e.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">微补丁公司 0patch 已针对 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11、Windows 10、Windows 7 和 Windows Server 2008 R2 发布了针对该漏洞的免费修复程序，该漏洞被跟踪为 CVE-2022-30190，存在于 Microsoft Windows 支持诊断工具 ( MSDT) Windows 组件中。</p><p style="text-align: left;">目前<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>官方提供的解决方案可谓“简单粗暴”，就是禁用有问题的组件；而 0patch 则提供了更微妙的方法。在一篇关于微补丁的博客文章中，Mitja Kolsek 的 0patch 说：</p><blockquote style="text-align: left;"><p style="text-align: left;">对我们来说，通过使用 TerminateProcess() 调用修补它来禁用 msdt.exe 是迄今为止最简单的方法。但是，这会使 Windows 诊断向导无法运行，即使对于非 <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 应用程序也是如此。另一种选择是将微软的建议编入补丁，有效地禁用 ms-msdt: URL 协议处理程序。</p><p style="text-align: left;">但如果可能，我们希望尽量减少除漏洞之外的影响，因此我们决定在调用 RunScript 之前将补丁放在 sdiagnhost.exe 中，并检查用户提供的路径是否包含“$(”序列 - 这是必要的用于注入 PowerShell 子表达式。如果检测到，我们确保在诊断工具继续运行时绕过 RunScript 调用。</p><p style="text-align: left;">无论您安装了哪个版本的 Office，或者您是否安装了 Office，该漏洞也可能通过其他攻击媒介被利用。这就是为什么我们还修补了 Windows 7，其中ms-msdt：根本没有注册 URL 处理程序</p></blockquote><p style="text-align: left;">0patch 提供的补丁适用于以下系统，甚至还包括已经停止支持的 Windows 7 系统：</p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows 11 v21H2</p><p style="text-align: left;">● Windows 10 v21H2</p><p style="text-align: left;">● Windows 10 v21H1</p><p style="text-align: left;">● Windows 10 v20H2</p><p style="text-align: left;">● Windows 10 v2004</p><p style="text-align: left;">● Windows 10 v1909</p><p style="text-align: left;">● Windows 10 v1903</p><p style="text-align: left;">● Windows 10 v1809</p><p style="text-align: left;">● Windows 10 v1803</p><p style="text-align: left;">● Windows 7</p><p style="text-align: left;">● Windows Server 2008 R2</p></blockquote>   
</div>
            