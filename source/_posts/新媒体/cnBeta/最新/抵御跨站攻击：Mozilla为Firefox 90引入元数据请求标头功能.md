
---
title: '抵御跨站攻击：Mozilla为Firefox 90引入元数据请求标头功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0713/b3b70b97ec706cf.jpg'
author: cnBeta
comments: false
date: Tue, 13 Jul 2021 04:52:41 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0713/b3b70b97ec706cf.jpg'
---

<div>   
<strong>Mozilla 很高兴地宣布，Firefox 90 版本将支持基于“元数据请求标头”的获取功能，使得 Web 应用程序能够保护自身和用户免受各种跨源威胁。</strong>据悉，此类威胁涵盖了跨站点请求伪造（CSRF）、跨站点泄露（XS-Leaks）、以及投机性跨站点执行侧信道（Spectre）攻击。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0713/b3b70b97ec706cf.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0713/b3b70b97ec706cf.jpg" alt="fetch_metadata-scaled.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：Mozilla <a href="https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/" target="_self">Blog</a>）</p><p>跨站攻击的背后，其实涉及 Web 的基本安全问题。出于开放的特性，其难以允许 Web 服务器端严格区分自身应用程序（浏览器选项卡）的请求、或源自可能以不同方式打开的恶意（跨站点）应用程序的请求。</p><blockquote><p>如上图所示，假设用户登录了托管于 https://banking.com 的银行网站，并开展了网银相关的某些活动。</p><p>与此同时，被恶意攻击者控制的网站、也可在不同的浏览器标签页中打开并执行来自 https://attacker.com 的一些恶意操作。</p></blockquote><p>于是在用户正常交互的过程中，网银 Web 服务器端可能收到某些例外操作，但却几乎无法分辨到底由用户本人、还是另一标签页中的恶意攻击代码发起的操作。</p><p>最终导致网银或常见的 Web 应用程序服务器刻板地接收任意操作，并允许发起相关攻击。</p><p><img src="https://static.cnbetacdn.com/article/2021/0712/849ccadb2ef5085.png" referrerpolicy="no-referrer"></p><p>好消息是，从 Firefox 90 开始，Mozilla 将允许 Web 浏览器通过 HTTP 请求头来获取元数据（Sec-Fetch-*），从而让 Web 服务器更好地区分同源 / 跨站攻击请求。</p><blockquote><p>借助 Sec-Fetch-* 系列请求标头中提供的附加上下文（支持 Dest、Mode、Site、以及 User 这四种请求标头），Web 服务器将能够火眼金睛地拒绝或忽略恶意请求。</p></blockquote><p>Fetch Metadate 请求标头的启用，可为各种 Web 应用服务带来深度防御机制。此外 Firefox 将很快推出新的站点隔离安全架构，以进一步解决上述某些问题。</p><p><strong>Mozilla Firefox 90 下载地址：</strong></p><blockquote><p><a href="https://ftp.mozilla.org/pub/firefox/releases/90.0/" _src="http://ftp.mozilla.org/pub/firefox/releases/90.0/" target="_blank">http://ftp.mozilla.org/pub/firefox/releases/90.0/</a></p></blockquote><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1152099.htm" target="_blank">Mozilla Firefox 90发布：引入后台升级特性 终止FTP支持并加强了安全性</a></p></div>   
</div>
            