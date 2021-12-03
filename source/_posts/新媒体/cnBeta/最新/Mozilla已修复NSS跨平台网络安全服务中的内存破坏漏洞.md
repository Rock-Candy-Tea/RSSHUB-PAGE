
---
title: 'Mozilla已修复NSS跨平台网络安全服务中的内存破坏漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1203/0aa4543150ec09d.png'
author: cnBeta
comments: false
date: Fri, 03 Dec 2021 02:17:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1203/0aa4543150ec09d.png'
---

<div>   
作为安全客户端 / 服务器应用程序开发的一款工具，NSS 可用于支持 SSL v3、TLS、PKCS #5、PKCS #7、PKCS #11、PKCS #12、S/MIME、X.509 v3 证书，以及其它各种安全标准。<strong>然而在 3.73 / 3.68.1 ESR 之前的版本中，Google 安全研究员 Tavis Ormandy 却发现了一个严重的内存破坏漏洞。</strong><br><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1203/0aa4543150ec09d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1203/0aa4543150ec09d.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（来自：Mozilla <a href="https://www.mozilla.org/en-US/security/advisories/mfsa2021-51/" target="_self">官网</a>）</p><p>Tavis Ormandy 将这种漏洞称作 BigSig，且现已分配 CVE-2021-43527 这个漏洞披露追踪编号。</p><p>若使用易受攻击的 NSS 版本，用户很可能在电子邮件客户端和 PDF 阅读器中处理 DER 编码（DSA）或 RSA-PSS 签名时，遭遇堆缓冲区溢出（<a href="https://cwe.mitre.org/data/definitions/122.html" target="_self">heap-based buffer overflow</a>）。</p><p>庆幸的是，Mozilla 已在 NSS 3.73 / 3.68.1 ESR 版本中修复了这个 bug 。但未及时打补丁的平台，仍存在程序崩溃、或被攻击者利用于任意代码执行（绕过安全软件）的风险。</p><blockquote><p>Mozilla 在周三发布的一份安全公告中称，使用 NSS 处理 CMS、S/MIME、PKCS #7、PKCS #12 签名编码的各应用程序，都有可能受到 BigSig 漏洞的影响。</p><p>此外使用 NSS 开展证书验证（或其它 TLS、X.509、OCSP、CRL 功能）的应用程序，也可能受到一定的影响，具体取决于它们是如何配置的。</p></blockquote><p>Tavis Ormandy 在 Project Zero 漏洞追踪页面上指出，问题可一直追溯到 2012 年 10 月发布的 3.14 版本。</p><p>Mozilla 计划生成一份受影响 API 的完整列表，但简单总结就是任何 NSS 的标准使用都会受到影响，该漏洞很容易重现并影响多种算法。</p><p><img src="https://static.cnbetacdn.com/article/2021/1203/4d50bea86803fc2.png" referrerpolicy="no-referrer"></p><p>让人松口气的是，Mozilla 声称 CVE-2021-43527 漏洞并未波及 Firefox 网络浏览器。不过所有使用 NSS 进行签名验证的 PDF 阅读器 / 电子邮件客户端，都应该慎重评估。</p><p>除了 Mozilla 旗下的 Firefox 网络浏览器 / Thunderbird 邮件客户端 / Firefox OS 移动操作系统 / SeaMonkey 跨平台开源网络套装软件，红帽、SUSE 等公司也有大量产品在使用 NSS 。</p><blockquote><p>● 开源客户端应用程序：包括 Evolution、Pidgin、Apache Open<a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a>、LibreOffice 。</p><p>● Red Hat 服务器产品：Red Hat Directory Server、Red Hat Certificate System、以及用于 Apache 网络服务器的 mod_nss SSL 模块。</p><p>● Oracle（Sun Java Enterprise System）服务器产品：包括 Oracle Communications Messaging Server 和 Oracle Directory Server Enterprise Edition 。</p><p>● SUSE Linux Enterprise Server：支持 Apache 网络服务器的 NSS 和 mod_nss SSL 模块。</p></blockquote><p>最后，Tavis Ormandy 提醒那些在自家产品中分发 NSS 的供应商，也尽快提供更新或向后移植补丁。</p>   
</div>
            