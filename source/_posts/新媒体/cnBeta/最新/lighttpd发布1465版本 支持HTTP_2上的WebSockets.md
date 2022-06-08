
---
title: 'lighttpd发布1.4.65版本 支持HTTP_2上的WebSockets'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0608/804df745304a6c6.png'
author: cnBeta
comments: false
date: Wed, 08 Jun 2022 09:15:10 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0608/804df745304a6c6.png'
---

<div>   
对于那些使用lighttpd轻量级和快速的网络服务器的人来说，这个BSD授权的开源软件现在已经有了新的版本。lighttpd
1.4.65最引人注目的是对HTTP/2的WebSockets的支持。在HTTP/1.1上的WebSockets
protocl升级机制将TCP连接从HTTP过渡到WebSocket。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0608/804df745304a6c6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0608/804df745304a6c6.png" title alt="Lighttpd-Logo.wine.png" referrerpolicy="no-referrer"></a></p><p>然而，由于HTTP/2的基本变化，如不支持升级头字段，需要以不同的方式处理HTTP/2的WebSockets。从HTTP/2引导WebSockets允许HTTP和WebSockets协议共享一个TCP连接，并将HTTP/2对网络的更有效使用扩展到WebSockets。</p><p>所有的HTTP/2 WebSockets的特性都在IETF RFC 8441中列出：</p><p><a href="https://datatracker.ietf.org/doc/html/rfc8441" _src="https://datatracker.ietf.org/doc/html/rfc8441" target="_blank">https://datatracker.ietf.org/doc/html/rfc8441</a><br></p><p>今天的lighttpd 1.4.65版本已经实现了对HTTP/2的WebSockets的支持。</p><p>新的lighttpd 1.4.65版本还增加了对HTTP/2的"PRIORITY_UPDATE"的支持，通过HTTP/2加快了请求的上传速度，各种行为改进，为TLS模块默认使用更强大的现代密码做准备，以及其他各种变化和修复。</p><p>希望了解今天发布的lighttpd 1.4.65网络服务器版本的下载和更多细节，请访问lighttpd.net：</p><p><a href="https://www.lighttpd.net/" _src="https://www.lighttpd.net/" target="_blank">https://www.lighttpd.net/</a><br></p>   
</div>
            