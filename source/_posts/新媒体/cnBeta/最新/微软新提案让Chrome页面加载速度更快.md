
---
title: '微软新提案让Chrome页面加载速度更快'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0727/ee0c8666dede440.jpg'
author: cnBeta
comments: false
date: Tue, 27 Jul 2021 03:48:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0727/ee0c8666dede440.jpg'
---

<div>   
得益于微软的新提案，Chrome 浏览器有望进一步提速。在一个新的 Chromium 提案中，微软正通过 chrome://protocol 为获取的脚本开发新的“代码缓存”。在启用之后，能提高 Chrome 在 Windows、Linux、macOS 和其他桌面平台上的页面加载速度。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0727/ee0c8666dede440.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0727/ee0c8666dede440.jpg" alt="ziudizsd.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在提案中写道：“在加载和执行一个脚本后，V8 可以将为该脚本生成的解释器字节码序列化。之后，如果 Blink 告诉 V8 再次运行相同的脚本，并提供以前的序列化字节码，那么 V8 可以跳过最初的解析步骤，脚本运行得更快。这对于页面加载时间来说非常重要”。</p><p style="text-align: left;">目前包括 Chrome 在内很多基于 Chromium 的浏览器，在 WebUI 页面中通常会包含一些大型脚本。在使用新功能之后，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>已经观察到在新标签页上首次绘制内容的时间减少了 11%-20%。</p><p style="text-align: left;">目前，许多 WebUI 数据源选择不使用网络缓存，响应时间并不是衡量脚本内容是否发生变化的一个有意义的指标，而且响应时间比较总是拒绝来自字节码缓存的任何数据。微软指出：“该功能目前默认是禁用的，可以通过用 -enable-features=WebUICodeCache 来启用”。</p><p style="text-align: left;">此外，Google也在为其网络浏览器进行更新，这将提高网页的加载速度。这项功能在桌面上被称为“back-forward cache”，它将装备在 Chrome 92 版本中。</p>   
</div>
            