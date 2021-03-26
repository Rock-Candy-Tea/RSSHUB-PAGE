
---
title: 'OpenSSL修复可被黑客攻击的服务器崩溃高危漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0326/f169fbc990cdcab.png'
author: cnBeta
comments: false
date: Fri, 26 Mar 2021 07:56:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0326/f169fbc990cdcab.png'
---

<div>   
ArsTechnica 报道称，<strong>OpenSSL 是被许多网站和加密电子邮件服务提供商所广泛采纳的软件库，但不久前，其曝出了一个可能导致服务器被攻击崩溃的高危安全漏洞。</strong>据悉，OpenSSL 提供了久经考验的加密功能，且实现了基于 TLS 的安全传输协议。作为接替 SSL 安全套接层的后继协议，其用于在互联网服务器和最终用户客户端之间的数据流加密。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0326/f169fbc990cdcab.png" referrerpolicy="no-referrer"></p><p>TLS 应用程序的开发者们，可借助 OpenSSL 来节省重复工作，以避免专家们并不建议的常见短板。</p><p>当黑客于 2014 年开始利用开源代码库中的一个严重漏洞时，OpenSSL 在互联网安全领域发挥的关键作用，就得到了充分的体现。</p><p>据悉，黑客可利用这些漏洞，从世界各地的服务器窃取加密密钥等敏感的客户信息。“心脏出血”（Heartbleed）漏洞更是仅凭几行代码就掀翻了银行、新闻站点、律所等大量组织机构。</p><p><img src="https://static.cnbetacdn.com/article/2021/0326/b350905d6acd05e.png" referrerpolicy="no-referrer"></p><p>本周四，OpenSSL 维护团队披露其已经修补了一个严重的安全漏洞。此前受 CVE-2021-3449 漏洞的影响，受影响的服务器可能在收到未经验证的最终用户恶意请求时发生崩溃。</p><p>密码学工程师 Filippo Valsorda 在 Twitter 上表示，问题影响互联网上的大多数 OpenSSL 服务器。</p><p>且黑客只需利用握手期间向服务器发送的恶意请求（重新协商），便可在最终用户和服务器之间建立安全连接。</p><blockquote><p>维护人员在一份通报（<a href="https://www.openssl.org/news/secadv/20210325.txt" target="_self">传送门</a>）中写到：若从客户端发送了经过恶意之作的重协商 ClientHello 消息，则 OpenSSL 服务器可能发生崩溃。</p><p>若最初的 ClientHello 中存在的 TLS v1.2 重协商省略了 signature_algorithms 签名算法扩展名、但包括了 signature_algorithms_cert 证书扩展名，就会导致 NULL 指针取消引用、从而引发崩溃和拒绝服务（DoS）攻击。</p></blockquote><p>对于这个 OpenSSL 高危漏洞，研究人员早在 3 月 17 日就进行了上报。庆幸的是，在诺基亚开发人员 Peter Kästle 和 Samuel Sapalski 的帮助下，OpenSSL 现已正式堵上这一漏洞。</p><p>此外 OpenSSL 还修复了一个可能在极端情况下发生的 CVE-2021-3450 漏洞，以阻止应用程序检测、和拒绝未由浏览器信任的证书颁发机构签名的 TLS 证书。</p><p>需要指出的是，OpenSSL 1.1.1h 及更高版本易受到相关漏洞攻击的影响，而 OpenSSL 1.0.2 并不在其中，不过还是建议大家尽快升级到最新的 OpenSSL 1.1.1k 版本。</p>   
</div>
            