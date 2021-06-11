
---
title: '黑客可向邮件服务器发送数据以干扰HTTPS连接'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0611/38f5456011ca08d.png'
author: cnBeta
comments: false
date: Fri, 11 Jun 2021 09:48:09 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0611/38f5456011ca08d.png'
---

<div>   
当通过受保护的 HTTPS 连接访问服务时，浏览器不会在验证完网站的数字证书之前将数据传递给网络服务器。<strong>该方案可防止监控 / 篡改数据类的中间人攻击，避免用户被收集身份验证 cookie、或在受害者的设备上运行恶意软件。</strong>然而 Ars Technica 报道称，近期曝出的一种黑客攻击手段，表明攻击者仍可诱使浏览器连接到使用兼容证书的 Email / FTP 服务器，进而引发相应的风险。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0611/38f5456011ca08d.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Alpace-Attack <a href="https://alpaca-attack.com/" target="_self">网站</a>）</p><p>由于网站的域名与电子邮件或 FTP 服务器证书中的域名匹配，因此浏览器通常会将传输层安全（TLS）连接到这些服务器之一，而不是用户原意访问的网站。</p><blockquote><p>在浏览器使用 HTTPS 通信、而 Email / FTP 服务器通过 SMTP / FTPS 或其它协议进行通信时，就有可能遇到严重的错误。</p><p>比如将解密的身份验证 cookie 发送给了攻击者、或在受害者机器上执行恶意代码。</p></blockquote><p>虽然听起来有些牵强，但一项新研究还是揭示了这套攻击手段的可行性。</p><blockquote><p>大约有 144 万台 Web 服务器，使用了与同一组织的 Email / FTP 服务器的加密凭据兼容的域名。</p><p>其中约 11.4 万个站点被认为易受攻击，因为 Email / FTP 服务器使用了已知存在缺陷的软件。</p></blockquote><p>作为被数以百万计的服务器所倚赖的互联网安全基石，TLS 会对在最终用户和服务器之间传输的数据进行加密，以确保没有人可以通过访问连接来读取或篡改。</p><p><a href="https://static.cnbetacdn.com/article/2021/0611/529a743885cb1ea.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0611/529a743885cb1ea.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">风险示意（图 via <a href="https://arstechnica.com/gadgets/2021/06/hackers-can-mess-with-https-connections-by-sending-data-to-your-email-server/" target="_self">Ars Technica</a>）</p><p>然而在周三发表的一篇研究论文中，Brinkmann 等七位研究人员还是深入调查了能否利用所谓的跨协议攻击（cross-protocol attacks）来绕过 TLS 的防护。</p><p>可知问题在于传输层安全（TLS）并不保护 TCP 连接的完整性，而只保护使用 HTTP、SMTP、或它互联网服务器。<strong>攻击的主要组成部分是：</strong></p><blockquote><p>（1）目标最终用户使用的客户端应用程序 -- 此处指 C；</p><p>（2）目前打算访问的服务器 -- 简称 Sint；</p><p>（3）代理服务器、一台通过 SMTP / FTP / 或与 Serverint 使用不同协议连接的计算机、但其 TLS 证书中具有相同的域。</p></blockquote><p>即使中间人（MitM）无法解密 TLS 流量，但攻击者仍可达成其它目的 —— 比如强制目标浏览器连接到 Email / FTP 服务器（而不是预期的 Web 服务器）。</p><p>这可能导致浏览器向 FTP 服务器发送身份验证 cookie，漏出跨站脚本攻击的缺陷，让浏览器下载并执行托管在 Email / FTP 服务器上的恶意 JavaScript 脚本。</p><p>庆幸的是，被研究人员命名为“允许跨协议攻击的应用层协议”（ALPACA）的缺陷，暂时不会对大多数人构成重大的威胁。</p><p>但若有新的攻击途径或漏洞显现、或利用 TLS 来保护其它通信方案，则风险仍有增加的可能。</p>   
</div>
            