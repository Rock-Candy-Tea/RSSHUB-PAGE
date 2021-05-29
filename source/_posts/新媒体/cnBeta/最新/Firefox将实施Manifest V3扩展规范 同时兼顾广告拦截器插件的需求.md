
---
title: 'Firefox将实施Manifest V3扩展规范 同时兼顾广告拦截器插件的需求'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0529/d7d78f33e6ace46.jpg'
author: cnBeta
comments: false
date: Sat, 29 May 2021 04:33:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0529/d7d78f33e6ace46.jpg'
---

<div>   
作为谷歌 Chrome 力推的新版扩展规范，Manifest V3 也引发了一些争议，尤其是它对广告拦截器插件造成了较大的影响。即便如此，谷歌还是坚持认为隐私至上。<strong>另一方面，Mozilla 在昨日宣布了 Firefox 将支持 Manifest V3 扩展，以保持高度的兼容性和支持跨浏览器开发。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0529/d7d78f33e6ace46.jpg" referrerpolicy="no-referrer"></p><p>不过在实施 Manifest V3 时，与 Google Chrome 价值观有所不同的 Mozilla Firefox，还考虑到了更多重要的细节，尤其是旨在取代 webRequest API 的 declarativeNetRequest（DNR）。</p><p>谷歌称 webRequest API 提供了对潜在敏感的用户数据的访问，但 Mozilla 认为它也被许多流行的广告拦截插件所使用，所以不该盲目地一刀切。</p><p>为此，Firefox 将继续提供这方面的支持，以便开发者能够选择最适合他们和用户的方法。在 Mozilla 带动下，Chrome 开发团队的想法也有所改变，并将根据反馈对 Manifest V3 予以修改。</p><blockquote><p>在与多位拦截器插件开发者进行讨论后，我们决定实施 DNR、并继续维护对阻止 webRequest 的支持。</p><p>我们实现 DNR 的最初目的，是为了确保 Chrome 的兼容性、以及让开发者无需支持多个代码库（如果他们不想的话）。</p><p>同时我们将支持阻止 webRequest，直到有更好的解决方案来涵盖我们认为重要的所有用例。因为当前的 DNR 实施，尚不足以满足广大开发者的需求。</p></blockquote><p>其它方面，Firefox 开发者对谷歌的决定还是相当赞成的，即确保扩展程序不会在后台打开一个完整的页面后才能运行。反之，浏览器将支持相关服务的后台任务和事件处理。</p><p>最后，Mozilla 将实施跨源保护、以增强浏览器用户的 cookie 隐私保护体验（类似于 Chrome 上所做的），让最终用户能够控制哪些网站附加组件可处于活动状态。</p><blockquote><p>据悉，Firefox 计划在 2021 年 4 季度开启 Manifest V3 的开发人员测试，同时在明年初开始接受新版扩展。</p><p>但由于这是一个‘大型平台项目’，Mozilla 也无法准确预测后续的进展有多顺利，所以仍存在着延期的可能。</p><p>至于 Manifest V2 的弃用日期，Mozilla 尚未正式敲定，预计它会在 Manifest V3 正式引入稳定版后，继续提供至少一年的支持。</p></blockquote>   
</div>
            