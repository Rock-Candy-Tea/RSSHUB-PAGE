
---
title: 'Firefox 87将默认修剪HTTP Referrers以保护用户粉丝'
categories: 
    - 新媒体
    - cnBeta
    - 最新

author: cnBeta
comments: false
date: Tue, 23 Mar 2021 06:24:36 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0323/48df1cee2bccef0.jpeg'
---

<div>   
Mozilla 刚刚宣布，其将为 Firefox 87 引入更加严格的隐私保护选项。<strong>在默认情况下，Firefox 将修剪 HTTP 引荐来源标头（Referrer Headers）中的路径和查询字符串等信息，以防站点意外地泄露了用户的敏感数据。</strong>据悉，浏览器通常会向网站发送 HTTP Referrer 标头信号，以指示当前用户“引用”了该网站的服务器。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0323/48df1cee2bccef0.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0323/48df1cee2bccef0.jpeg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：<a href="https://blog.mozilla.org/security/2021/03/22/firefox-87-trims-http-referrers-by-default-to-protect-user-privacy/" target="_self">Mozilla Blog</a>）</p><p>更准确的说法是，传统浏览器会在 HTTP Referrer 标头中发送参考文档的完整 URL（地址栏常见），且几乎包含了每个导航或子资源的图像、样式和脚本请求。</p><p>对于目标网站来说，可将引荐来源的网址信息用于许多无害的用途，包括分析、日志记录、或缓存优化。</p><p>遗憾的是，HTTP Referrer 标头中也常常包含用户的隐私数据，比如可显示用户正在引荐网站上阅读哪些文章、甚至可包含有关该公司在网站上的账户信息。</p><blockquote><p>于是在 2016 ~ 2018 年间，浏览器开始引入的‘引荐来源网址政策’（Referrer Policy），使得网站可以更好地控制其站点上的引荐来源信息，进而为用户提供了额外的保护机制。</p><p>但若网站未能设置任何类型的引荐来源网址政策，则 Web 浏览器通常会默认启用降级的“no-referrer-when-downgrade”政策。</p></blockquote><p>该政策会在导航至不太安全的目的地时，对引荐来源网址进行修剪，否则就会发送完整的 URL（包括 path 路径）和原始文档的查询信息（作为引荐来源）。</p><p>庆幸的是，为了不断提升用户隐私的保护力度，Mozilla 等浏览器开发商正在付出更多的努力。</p><p>除了推动安全超文本传输协议（HTTPs）和 Let's Encrypt 加密，Firefox 87 也将默认启用针对引荐来源网址的修剪政策。</p><blockquote><p>从 Firefox 87 开始，我们将把 Referrer Policy 默认设置为对跨域来源进行限制（strict-origin-when-cross-origin），以清理 URL 中可访问的用户敏感信息。</p><p>通过实施更严格的引荐来源网址政策，浏览器不仅可以修剪从 HTTPs 到 HTTP 的请求信息，还会修剪所有跨域请求的路径和查询信息。</p></blockquote><p>如果你是 Firefox 浏览器用户，那无需执行任何操作，即可享受到新版本带来的这一益处。</p><p>如果尚未自动更新，也可手动升级至 Firefox 87，届时新的默认政策将对用户访问的每个网站都生效。</p>   
</div>
            