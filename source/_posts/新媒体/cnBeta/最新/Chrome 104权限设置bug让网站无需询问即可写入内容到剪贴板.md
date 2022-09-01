
---
title: 'Chrome 104权限设置bug让网站无需询问即可写入内容到剪贴板'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0901/2330d9bdd7f697c.png'
author: cnBeta
comments: false
date: Thu, 01 Sep 2022 08:58:05 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0901/2330d9bdd7f697c.png'
---

<div>   
开发人员 Jeff Johnson 在一篇博客文章中指出，Google 在 Chrome 104 中意外引入了一个 bug 。<strong>由于一个权限设置失误，导致网站无需获准用户许可、即可将相关内容写入系统剪贴板。</strong>虽然 Safari 和 Firefox 也有类似的功能，但至少 Apple 和 Mozilla 有设置相应的防护措施。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0901/2330d9bdd7f697c.png" referrerpolicy="no-referrer"></p><p>据悉，剪贴板是操作系统上的一个临时存储空间。但由于常用于复制 / 粘贴的中转站，剪贴板很可能涉及银行账号、加密货币钱包字符串、以及密码等敏感信息。</p><blockquote><p>当用户选择从网页上复制一段文本时，某些网站可能会加上额外的内容 —— 比如当前页面的网址（URL）—— 而没有任何可见的指示或交互。</p><p>若被任意内容覆盖这个临时存储空间，用户将面临较高的风险，导致其成为潜在恶意活动的受害者。</p></blockquote><p>Jeff Johnson 在<a href="https://lapcatsoftware.com/articles/clipboard.html" target="_self">博客文章</a>中强调 —— 所有支持剪贴板写入的 Web 浏览器，都具有较差且不充分的防护措施。</p><p>举个例子，攻击者可能引诱用户访问冒充合法加密货币服务的特制网站。当用户尝试付款、并将钱包地址复制到剪贴板时，该 bug 或导致相关信息被篡改。</p><p><img src="https://static.cnbetacdn.com/article/2022/0901/317d9367a741087.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://www.bleepingcomputer.com/news/security/google-chrome-bug-lets-sites-write-to-clipboard-without-asking/" target="_self">BleepingComputer</a>）</p><p>虽然许多剪贴板 API 交互都是通过 Ctrl+C 这样的快捷键实现的，但在许多情况下，网站交互可以做到更加神不知鬼不觉。</p><blockquote><p>Johnson 在 Safari 和 Firefox 上的测试表明，即使按了向下 ↓ 箭头、或使用鼠标滚轮在网站上导航，都可被授予当前加载页面的剪贴板写入权限。</p><p>要确定该问题是否影响您的 Web 浏览器，可移步至 webplatform.news 示例站点，看相关操作是否会将内容注入到用户系统的剪贴板里、然后尝试将内容‘粘贴’到 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 记事本。</p></blockquote><p>目前 Chrome 开发团队已经意识到了这个问题，但尚未立即修复。庆幸的是，它对当前版本的移动 / 桌面版 Chrome 浏览器的影响并不大。</p>   
</div>
            