
---
title: 'Safari浏览器曝出API漏洞 可泄露浏览数据和用户身份'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0117/877298c2bbd80f8.jpg'
author: cnBeta
comments: false
date: Mon, 17 Jan 2022 03:04:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0117/877298c2bbd80f8.jpg'
---

<div>   
长期以来，苹果一直以隐私保护为主要卖点，大力推荐自家的 Safari 浏览器，比如部署了防止跨站点追踪的举措和隐私报告。<strong>然而近日，该软件却曝出了处理 IndexedDB API 时的一个漏洞，或导致签署努力功亏一篑、泄露与用户浏览习惯相关的隐私信息。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0117/877298c2bbd80f8.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://fingerprintjs.com/blog/indexeddb-api-browser-vulnerability-safari-15/" target="_self">FingerprintJS</a>）</p><p>浏览器指纹识别服务 FingerprintJS 在一篇博客文章中指出，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>在 Safari 15 中的 IndexedDB API 实现方式，存在一个严重的隐私数据泄露隐患。</p><p>研究人员指出，该漏洞使得任何 Web 追踪器能够窥探用户的互联网活动，并最终确定其身份。</p><blockquote><p>据悉，IndexedDB 是被广大浏览器客户端所采纳的一款存储 API，多用于保存数据库等数据。</p><p>通常情况下，同源策略会限制哪些数据可被某个特定的网站访问。</p><p>此外一般只允许一个网站只能访问其生成的数据、而不能摸到其它网站的数据。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0117/183dcebdb76df9d.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>尴尬的是，在 Safari 15 for macOS、iOS 和 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>OS 版本中，我们惊讶地发现 ——</p><blockquote><p>每当网站与其数据库交互时，处于同一浏览器会话中的所有其它活动框架、选项卡、以及窗口，都会创建一个使用相同名称的新空数据库。</p><p>由此造成的数据泄露是个问题，因其可让别有用心的站点知悉处在同一会话中的不同选项卡、或窗口中访问的其它站点。</p></blockquote><p>此外考虑到部分数据库具有唯一、且特定于某个网站的名称，问题就变得更加糟糕。</p><p>对于可共享相同身份验证凭据的站点（比如 Gmail 和 YouTube），数据库名称还可包含经过身份验证的相同 Google 用户 ID 。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=319154191&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">How IndexedDB in Safari 15 leaks your browsing activity（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzE5MTU0MTkxLnNodG1s.html" target="_self">via</a>）</p><p>测试发现，具有普遍唯一标识符的索引数据库，是由广告网络所创建的。庆幸的是，Safari 的追踪预防功能阻止了这些数据库名称以这种方式泄露。</p><p>即使隐私浏览窗口也无法避免受到该问题的影响，但浏览会话仅限于单个选项卡，因而能够在一定程度上缓解 IndexedDB API 这一缺陷的影响。</p><p>目前用户对该问题几乎无能为力，只有在默认情况下阻止 JavaScript 才行（仅在受信任的站点上启用，但可能对浏览体验造成不利影响）。</p><p>macOS 用户可临时选用其它浏览器（Google Chrome / Mozilla Firefox 等），但 iOS / iPadOS 用户就没有那么幸运了，只能等待苹果和 WebKit 开发团队在下一版更新中修复。</p>   
</div>
            