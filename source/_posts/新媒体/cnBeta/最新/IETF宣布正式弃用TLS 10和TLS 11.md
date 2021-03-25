
---
title: 'IETF宣布正式弃用TLS 1.0和TLS 1.1'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0325/3aba190e279cf5e.jpg'
author: cnBeta
comments: false
date: Thu, 25 Mar 2021 03:20:45 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0325/3aba190e279cf5e.jpg'
---

<div>   
<strong>IETF（国际互联网工程任务组）今天正式发布 <a href="https://datatracker.ietf.org/doc/draft-ietf-tls-oldversions-deprecate/12/" target="_blank">RFC 8996</a>，正式宣布弃用 TLS 1.0 和 TLS 1.1。</strong>根据 SSL Pulse 服务，截至今年 1 月 16 日，95.2% 的接受安全连接的网站支持 TLS 1.2，14.2% 的网站支持 TLS 1.3。77.4% 的 HTTPS 站点接受 TLS 1.1 连接，68% 接受 TLS 1.0。在 Alexa 排名所反映的前 10 万个网站中，大约有 21% 的网站仍然没有使用 HTTPS。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0325/3aba190e279cf5e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0325/3aba190e279cf5e.jpg" alt="QQ截图20210325111018.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">TLS 全称为：Transport Layer Security——安全传输层协议，用于在两个通信应用程序之间提供保密性和数据完整性。目前 TLS 协议存在四个个版本：TLS 1.0、1.1 和 1.2、1.3。 TLS 1.0 规范于 1999 年 1 月发布，TLS 1.1 在 7 年之后发布，主要在生成初始化向量和预填充方面进行安全增强。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0325/5a7eacb9108c2c0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0325/5a7eacb9108c2c0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0325/219a6f8ac1d7c98.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0325/219a6f8ac1d7c98.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0325/c5ccad4dcaa8113.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0325/c5ccad4dcaa8113.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">TLS 1.0 于 1999 年发行，至今将近有 20 年，业内公认的过时并且多年来易受各种攻击的版本，其支持较弱加密，对当今网络连接的安全已失去应有的保护效力。TLS 1.1 虽没有任何已知的协议漏洞，但是它却共享支持错误加密。因而存在一个现象，就是大部分软件都会跳过直接使用 TLS 1.2，而很少看到使用 TLS 1.1。</p><p style="text-align: left;">TLS 1.0/1.1 的主要问题是缺乏对现代密码的支持(如ECDHE和AEAD)，在规范中存在支持旧密码的要求，在计算机工程发展的现阶段，其可靠性受到质疑(例如，要求支持 TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA，MD5 和 SHA-1 用于完整性检查和认证)。对传统算法的支持已经导致了ROBOT、DROWN、BEAST、Logjam和FREAK等攻击。</p><p style="text-align: left;">然而，这些问题并不是协议的直接漏洞，而是在执行层面上被关闭了。TLS 1.0/1.1协议本身并不包含可以被利用来进行实际攻击的关键漏洞。</p>   
</div>
            