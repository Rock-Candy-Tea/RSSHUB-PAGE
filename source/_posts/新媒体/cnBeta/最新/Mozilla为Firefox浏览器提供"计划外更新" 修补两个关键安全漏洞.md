
---
title: 'Mozilla为Firefox浏览器提供"计划外更新" 修补两个关键安全漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0306/572b3c144c01a31.png'
author: cnBeta
comments: false
date: Sat, 05 Mar 2022 23:42:14 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0306/572b3c144c01a31.png'
---

<div>   
Mozilla今天发布了Firefox 97.0.2。这个"计划外更新"更新并不包含任何功能，但修补了两个被列为"关键"的安全漏洞。用户必须紧急应用该更新，因为Mozilla已经确认这两个安全漏洞正在被积极利用。<br>
 <p>Mozilla Firefox 97.0.2更新包含两个零日漏洞的补丁，这些漏洞目前在外部呈现活动状态。在"Mozilla基金会安全咨询2022-09"中官方表示："我们已经收到了关于在滥用[这些]缺陷的攻击报告。"</p><p><a href="https://static.cnbetacdn.com/article/2022/0306/572b3c144c01a31.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0306/572b3c144c01a31.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>安全公告的细节不多，可能是因为Mozilla不希望攻击者获得关于如何利用这些漏洞的技术方面的信息。尽管如此，它提供了关于这两个缺陷的一些细节，这两个缺陷被标记为"关键"。</p><p>CVE-2022-26485 (漏洞位于XSLT参数处理中)。这个缺陷被用于远程代码执行（RCE），这意味着在计算机上没有现有权限或账户的攻击者可能会在受害者的计算机上运行他们选择的恶意软件代码，只需将用户引诱到一个看起来无害但充满恶意软件的网站。</p><p>CVE-2022-26486（漏洞位于WebGPU IPC框架中）。这个漏洞是"沙盒逃脱"的一部分，这种安全漏洞既可以单独滥用（攻击者获得对本应禁止的文件的访问权），也可以与RCE漏洞结合使用，使播种的恶意软件从浏览器部署的安全围栏当中逃脱。</p><p>这两个安全缺陷都被列为"自由使用后"的错误。在编程方面，这指的是一个应用程序表明它打算停止访问系统内存，基本上是"释放"给其他应用程序使用。然而，在某些情况下可能继续使用或占用系统内存，这可能对其他等待访问内存的应用程序产生不利影响。通常情况下，这将导致程序崩溃，但有时，甚至数据也会被破坏。这两种情况都可以被认为是安全问题。攻击者也可以利用这些问题来欺骗程序运行不受信任的代码。</p><p>要更新Mozilla Firefox，请前往应用程序菜单，点击帮助>关于Firefox就可以开始升级。除了标准用户的Firefox 97，该更新也适用于Firefox 91.6.1 ESR（扩展支持版本）和Firefox 97.3.0 for Android。</p><p><strong>了解更多：</strong></p><p><a href="https://www.mozilla.org/en-US/security/advisories/mfsa2022-09/" _src="https://www.mozilla.org/en-US/security/advisories/mfsa2022-09/" target="_blank">https://www.mozilla.org/en-US/security/advisories/mfsa2022-09/</a><br></p>   
</div>
            