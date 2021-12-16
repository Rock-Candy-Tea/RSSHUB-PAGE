
---
title: '争抢默认浏览器：微软通过周二累积更新屏蔽了EdgeDeflector'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1216/0951b9c61de8724.png'
author: cnBeta
comments: false
date: Thu, 16 Dec 2021 09:00:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1216/0951b9c61de8724.png'
---

<div>   
<strong>在周二向 Windows 10 / 11 操作系统用户推送的 KB5008212 / KB5008215 累积更新中，微软也悄然引入了对 EdgeDeflector 的屏蔽措施。</strong>大约一个月前，该公司开始阻止其它应用程序接管 microsoft-edge:// 协议，以强制用户通过 Edge 来体验 Windows Search Console 搜索控制台、通过 Your Phone 分享的链接、Cortana 人工智能助理、新闻和兴趣等功能。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1216/0951b9c61de8724.png" referrerpolicy="no-referrer"></p><p>当时<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>正在面向 Windows 11 Insider 测试者们提供小范围体验，不过通过周二的 KB5008212 / KB5008215 累积更新，现相关功能已正式向广大 Windows 10 / 11 用户推出。</p><blockquote><p>安装累积更新后，用户为 microsoft-edge:// 协议指定的备用程序选项（比如 EdgeDeflector）将被剔除。</p><p>当你再次打开此类链接（如新闻和兴趣）时，将需要选择一款不同的默认应用程序。</p><p>然而当前唯一可用的就是 Microsoft Edge 浏览器，另一个所谓的‘在商店中搜索应用程序’的选项毫无用处。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/1113/cd6e576b223c068.webp" referrerpolicy="no-referrer"></p><p>今年早些时候，微软曾表示希望为广大用户提供可预测的端到端体验，同时为 Edge 保留对 microsoft-edge:// 协议的支持。</p><blockquote><p>Windows 平台对应用程序和服务的启用持开放态度，包括各种 Web 浏览器。</p><p>与此同时，微软还在 Windows 10 / 11 中提供了某些端到端的客户体验。</p><p>以任务栏上的搜索体验为例，它们一开始就不是为了重定向而设计的。</p></blockquote><p>其实当微软放话称“当意识到重定向不当，于是考虑推出修补程序”时，就已经暗示了 Windows 用户可能在不久的将来遇到麻烦。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1216/65fb908f0c4d3fc.png" referrerpolicy="no-referrer"></p><p>作为 EdgeDeflector 的替代应用程序，现在有个 MSEdgeRedirect（<a href="https://github.com/rcmaehl/MSEdgeRedirect" target="_self">Github</a>）。与前者类似，其允许用户将新闻、搜索和天气结果，重定向至用户指定的默认浏览器。</p><blockquote><p>不同的是，MSEdgeRedirect，这款应用程序会过滤 Microsoft Edge 进程的命令行参数、并将其传递到默认浏览器。</p><p>由于并不与 microsoft-edge:// 协议挂钩，所以 MSEdgeRedirect 将来有望具有更高的修改弹性。</p></blockquote><p>更棒的是，只要程序在后台运行（可在系统托盘上看到图标），即可实现相关操作。怕麻烦的用户，也可选择让它在启动时自动运行。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1202469.htm" target="_blank">神仙斗法：MSEdgeRedirect又成突破微软第三方浏览器限制新选择</a></p></div>   
</div>
            