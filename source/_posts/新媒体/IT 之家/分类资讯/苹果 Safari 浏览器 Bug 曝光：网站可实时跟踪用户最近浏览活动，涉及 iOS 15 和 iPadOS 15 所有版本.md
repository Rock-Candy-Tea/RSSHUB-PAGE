
---
title: '苹果 Safari 浏览器 Bug 曝光：网站可实时跟踪用户最近浏览活动，涉及 iOS 15 和 iPadOS 15 所有版本'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2020/11/20201106100854_3280.jpg'
author: IT 之家
comments: false
date: Mon, 17 Jan 2022 00:18:53 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2020/11/20201106100854_3280.jpg'
---

<div>   
<p data-vmark="f7a0"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 1 月 17 日消息，据 MacRumors 报道，根据<a class="s_tag" href="https://qiyu.ruanmei.com/" target="_blank">浏览器</a>指纹识别服务提供商 FingerprintJS 周五分享的一篇博客文章，WebKit 的一个名为 IndexedDB 的 JavaScript API 中的一个 Bug <span class="accentTextColor">可以泄露用户最近的浏览历史甚至身份</span>。</p><p data-vmark="f6ae"><img src="https://img.ithome.com/newsuploadfiles/2020/11/20201106100854_3280.jpg" alt="苹果 Safari 浏览" title="苹果 Safari 浏览器 Bug 曝光：网站可实时跟踪用户最近浏览活动，涉及 iOS 15 和 iPadOS 15 所有版本" referrerpolicy="no-referrer"></p><p data-vmark="2fe3">该 Bug 允许任何使用 IndexedDB 的网站在用户浏览会话期间访问其他网站生成的 IndexedDB 数据库的名称。这个漏洞<span class="accentTextColor">可以让一个网站跟踪用户访问的其他网站</span>，因为每个网站的数据库名称通常是唯一的。<span class="accentTextColor">正确的行为应该是，网站只能访问自己的 IndexedDB 数据库</span>。</p><p data-vmark="ffe6">IT之家了解到，根据 FingerprintJS 的描述，YouTube 创建的数据库包含经过认证的谷歌用户 ID，这个标识符可以与谷歌 API 一起获取头像等用户的个人信息。</p><p data-vmark="f86d">据介绍，这一 Bug 会影响使用苹果开源浏览器引擎 WebKit 的新版本浏览器，<span class="accentTextColor">包括 Mac 版的 Safari 15 以及 iOS 15 和 <a class="s_tag" href="https://ipad.ithome.com/" target="_blank">iPad</a>OS 15 所有版本的 Safari 浏览器</span>。该漏洞也会影响第三方浏览器，如 iOS 15 和 iPadOS 15 上的 Chrome，因为苹果要求所有浏览器在 <a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone</a> 和 iPad 上使用 WebKit。FingerprintJS 演示显示，Mac 版的 Safari 14 等旧版浏览器不受影响。</p>
          
</div>
            