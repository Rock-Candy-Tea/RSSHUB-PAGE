
---
title: '网友直言Debian上的Web浏览器安全更新支持很是糟糕'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1216/821c1df62ebf94d.jpg'
author: cnBeta
comments: false
date: Thu, 16 Dec 2021 10:12:46 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1216/821c1df62ebf94d.jpg'
---

<div>   
在谈到 Debian GNU / Linux 的 Web 浏览器时，我们必须承认，目前它还有很多不足之处。对于那些追求安全和最新体验的用户，这意味着你们需要寻找专有、或未打包的构建版本。然而近日，一位不愿透露姓名的 Phoronix 网友指出 —— <strong>所有 Debian 平台上的浏览器 —— 包括 Chromium、Firefox ESR、Falkon 等）—— 都存在着严重的开放式安全问题。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1216/821c1df62ebf94d.jpg" alt="Debian Web Browser.jpg" referrerpolicy="no-referrer"></p><p>更糟糕的是，软件包维护人员无法轻松解决相关问题。以 Chromium 为例，其仍停留于 90.0.4430.212-1 版本。</p><blockquote><p>这意味它尚未修补大量安全问题，而 Debian 维基页面给出的建议只是换用其它浏览器。</p><p>对于已经安装了浏览器、但依赖于自动更新推送的用户，他们也将在疏忽的情况下、于互联网上冒险奔跑。<br></p></blockquote><p>即使是 Debian 的默认 Web 浏览器，Mozilla Firefox（ESR）的版本号也停留于 78.15.0 。</p><blockquote><p>该版本同样存在不少未修补的安全问题，且 Firefox 78.x ESR 分支不再由 Mozilla 维护。</p><p>这部分用户需要更新到 Firefox 91.x ESR 分支，但在追求稳定的 Debian 平台上，它又会造成较大的问题。</p></blockquote><p>在某个 issue 对话中，许多人抱怨 Firefox 91.x 版本容易卡住，这导致 ESR 版本也难以被认定为“稳定且安全”。</p><blockquote><p>此外有人指出，Firefox-ESR 91.3 不再使用 OpenGL GLX，而是默认启用了 EGL 。</p><p>问题在于，EGL 至少需要 21.x 版本的 mesa 提供支撑，但 Debian 稳定版（bullseye）只附带了 20.3.5 版本。</p><p>顺道一提，Mozilla Thunderbird 电子邮件客户端也受到了该问题的影响。</p></blockquote><p>至于 Debian 发行版中包含的其它浏览器（以 Falkon 为例），它们也很长时间没收到任何安全补丁了（Falkon 的 QtWebEngine 包将需要更新）。</p><p>考虑到这些就是目前 Debian 上 Web 浏览器支持的现状，注重安全体验的用户，似乎也只剩下了最后一条路 —— 主动获取 Mozilla Firefox / Google Chrome 的二进制包 —— 尽管就算用上了最新版的 Firefox，Debian 稳定版在 EGL / GLX 方面仍可能遇到一些问题。</p><p>最后，如果开源社区不积极解决的话，迟早也会将人们推向其它非开源浏览器。</p>   
</div>
            