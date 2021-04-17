
---
title: 'Firefox Nightly_Beta已默认支持QUIC和HTTP_3'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0417/f3b35c94a2a8fe5.jpg'
author: cnBeta
comments: false
date: Sat, 17 Apr 2021 03:44:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0417/f3b35c94a2a8fe5.jpg'
---

<div>   
在 Firefox Nightly 和 Firefox Beta 中，已经默认启用了对 QUIC 和 HTTP/3 的支持。Mozilla 官方表示这些支持将在 Firefox Stable Release 88 版本中开始支持。HTTP/3 将会在 5 月底前默认支持。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0417/f3b35c94a2a8fe5.jpg" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0417/1d96bf4ea03173e.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">HTTP/3 是基于 QUIC 的 HTTP（网络协议）的新版本。与HTTP/2相比，HTTP/3有三个主要的性能改进：</p><blockquote style="text-align: left;"><p style="text-align: left;">● 因为它是基于 UDP 的，因此它的连接时间更短</p><p style="text-align: left;">● 没有连线阻塞（line blocking），即传送数据包的延迟会导致整个连接延迟</p><p style="text-align: left;">● 它能够更好地检测和修复数据包丢失。</p></blockquote><p style="text-align: left;">QUIC 还提供了连接迁移和其他功能，应该可以提高性能和可靠性。有关 QUIC 的更多信息，请参阅 Cloudflare 的这篇优秀博客文章。</p><p style="text-align: left;"><strong>如何使用它？</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">如果 Web 服务器（例如，Google 或 Facebook）提供 HTTP/3，Firefox Nightly 和 Firefox Beta 将自动尝试使用 HTTP/3。Web 服务器可以通过使用 Alt-Svc 响应头或通过使用 HTTPS DNS 记录宣传 HTTP/3 支持来表示支持。</p><p style="text-align: left;">客户端和服务器都必须支持相同的 QUIC 和 HTTP/3 草案版本才能相互连接。例如，Firefox目前支持规范的草案27至32，因此服务器必须在Alt-Svc或HTTPS记录中报告对这些版本之一的支持（例如 "h3-32"），以便Firefox尝试与该服务器使用QUIC和HTTP/3。</p><p style="text-align: left;">当访问这样的网站时，在Dev Tools中查看网络请求信息应该会显示Alt-Svc头，同时也会显示使用了HTTP/3。</p></blockquote>   
</div>
            