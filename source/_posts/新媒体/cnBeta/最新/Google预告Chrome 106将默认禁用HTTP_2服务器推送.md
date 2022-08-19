
---
title: 'Google预告Chrome 106将默认禁用HTTP_2服务器推送'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0819/105812a03789e92.png'
author: cnBeta
comments: false
date: Fri, 19 Aug 2022 07:55:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0819/105812a03789e92.png'
---

<div>   
在周四的一篇 Chrome Developer 博客文章中，Barry Pollard 介绍了 Chromium 社区的下一发展方向。其中最重要的，莫过于<strong>从 Chrome 106（以及其它基于 Chromium 内核的第三方浏览器的下一个版本）起，开发商将默认禁用对“HTTP/2 服务器推送”功能的支持。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0819/105812a03789e92.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（via <a href="https://jakearchibald.com/2017/h2-push-tougher-than-i-thought/" target="_self">Jake Archibald</a>）</p><p>据悉，HTTP/2 Server Push 允许网站向客户端主动发送页面所需的资源，而无需等待它们被请求。</p><p>然而正如 Jake Archibald 之前唠过的那样，这项功能存在一些问题与争议，且通常难以实现其性能优势。</p><p>结果就是该功能未被太多使用，仅 1.25% 的 HTTP/2 站点启用了这项特性。</p><blockquote><p>对 HTTP/2 服务器推送功能使用状况的分析结果，表明有好有坏（<a href="https://github.com/httpwg/wg-materials/blob/gh-pages/ietf102/chrome_push.pdf" target="_self">Chrome</a>、<a href="https://github.com/httpwg/wg-materials/blob/gh-pages/ietf102/akamai-server-push.pdf" target="_self">Akamai</a>）。</p><p>然而很多时候看不到显著的净性能争议，甚至许多情况下会遇到性能下降。</p></blockquote><p>此外即使被包含在了规范里面，Push 也没有在许多 HTTP/3 服务器和客户端中实现。</p><p>对于使用较新的 HTTP/3 的大部分网络，Push 已被有效地淘汰。</p><p>最近重新观察到的分析结果表明，各网站对 HTTP/2 的支持率，已从 1.25% 滑落至 0.7% 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0819/ac56e8e4621cdb8.png" alt="2.png" referrerpolicy="no-referrer"></p><p>作为一种替代方案，103 Early Hints 响应代码是一个不太容易出错的选项。</p><blockquote><p>与服务器推送资源不同，其仅向浏览器发送可能受益于立即请求的资源的提示。</p><p>这意味着浏览器可自行决断是否需要相关资源 —— 比如已有 HTTP 缓存的情况下。</p></blockquote><p>其次是预加载关键资源，其允许页面和浏览器一起工作，以在页面加载的早期，抢先加载关键部分的资源。</p><blockquote><p>由于仍需发送页面本身，它较服务器推送 / 103 早期提示有一定的速度劣势。</p><p>即便如此，预加载关键资源仍具有不延迟关键页面资源的优点（另外两套方案都可能遇到这种状况）。</p></blockquote><p>最后需要指出的是，所有尝试提前加载资源的解决方案，都有可能导致性能下降、因而需要综合评估并适度使用。</p><blockquote><p>通常情况下，浏览器本身就非常擅长做出正确的选择，仅在某些条件下可获得额外的增益。</p></blockquote><p>当然，Web 社区一直在积极尝试新鲜事物，并在不合时宜的情况下及时弃用，这也是它能保持长久生命力的一个主要原因。</p><p>至于听起来潜力似乎很大的 Push 能够发展到哪一步，仍有待时间去检验。</p>   
</div>
            