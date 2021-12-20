
---
title: 'Mozilla为Firefox 97引入Windows 11样式的滚动条'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1220/49f33a1ccccb575.jpg'
author: cnBeta
comments: false
date: Mon, 20 Dec 2021 06:39:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1220/49f33a1ccccb575.jpg'
---

<div>   
Windows 11 正式推出已有两个月，包括照片、画图、记事本等在内的原生应用，均已用上全新的 UI 设计（尤其是圆角风格）。浏览器方面，Microsoft Edge 和 Google Chrome 的转进也是相当迅速的。<strong>现在，Mozilla 也终于制定了要为 Firefox 97 引入 Windows 11 样式的滚动条的计划，预计稳定版的发布窗口为 2022 年 2 月。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1220/49f33a1ccccb575.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">默认 UI 示例（图 via <a href="https://techdows.com/2021/12/firefox-windows-11-overlay-scrollbar.html" target="_self">Techdows</a>）</p><p>从文件资源管理器、设置应用，以及操作系统的其它部分来看，你会发现某些 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 组件程序的滚动条显得既纤薄又时尚。</p><p>以 Microsoft Edge 为例，其引入了 Fluent Design、圆角、Mica 效果，并且在 Edge 浏览器中启用了现代的覆盖滚动条（Overlay Scrollbars）。</p><p>鉴于非经典版 Edge 浏览器早就转投 Chromium 内核，我们对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>和 Google 在 Windows 平台上的浏览器合作并不感到意外。</p><p>相比之下，Mozilla 不大可能针对 Windows 11 实施用户体验上的大修，尽管大家还是可以通过 Microsoft Store 应用商店来下载程序并获得自动更新。</p><p>目前 Firefox 已经提供了对 Snip Layouts 的支持，且 Nightly 每夜构建版也用上了全新的 Windows 11 风格滚动条设计。</p><p><img src="https://static.cnbetacdn.com/article/2021/1220/fe9809ad87901f8.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">夜间模式 UI 示例</p><p>事实上，Mozilla 在 Android、Linux、Mac、Windows 10 / 11 等主流平台上的 Firefox 浏览器中，都重新构建了该软件的滚动条。</p><p>感兴趣的朋友，可移步至“首选项”查看。相信随着 Firefox 97 的正式到来，会有更多人留意到这方面的更改。</p><p><strong>以下是当前 Pref widget.non-native-theme.scrollbar.style 已提供的选项：</strong></p><blockquote><p>“0”：平台默认滚动条样式</p><p>“1”：macOS 滚动条样式</p><p>“2”：GTK 滚动条样式</p><p>“3”：Android 滚动条样式</p><p>“4”：Windows 10 滚动条样式</p><p>“5”：Windows 11 滚动条样式</p></blockquote><p>不过由于新的滚动条代码尚未“稳定”，pref 选项值暂无法指定“5”或“0”并生效。</p>   
</div>
            