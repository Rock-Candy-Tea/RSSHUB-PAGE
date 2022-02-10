
---
title: 'Chrome浏览器底部下载栏将被工具栏动画按钮和弹窗给取代'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0210/68e9fc7ffa9d733.png'
author: cnBeta
comments: false
date: Thu, 10 Feb 2022 03:52:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0210/68e9fc7ffa9d733.png'
---

<div>   
2021 年底的时候，Chrome 开发团队在浏览器顶部工具栏中添加了一个下载按钮，然后逐渐加大其信息量和实用性。<strong>随着 Google 向更多用户提供新体验，我们发现 —— 位于窗口底部的下载栏将被逐渐弃用、直至彻底移除。</strong><br><br>
<p><img src="https://static.cnbetacdn.com/article/2022/0210/68e9fc7ffa9d733.png" referrerpolicy="no-referrer"></p><p>Reddit 网友 u/Leopeva64-2 最先指出，改进后的下载图标（以及下载气泡），已经出现在 Canary 分支的 Chrome 工具栏上。</p><p>与基于 Chromium 内核的 Microsoft Edge 类似，Google Chrome 的新下载按钮，可在工具栏上呈现正在进行、以及最近完成的下载内容信息。</p><p><img src="https://static.cnbetacdn.com/article/2022/0210/3d69bf3c0118c9a.gif" referrerpolicy="no-referrer"></p><p>每当用户下载新文件时，Chrome 下载按钮的颜色和大小都会发生变化。下载活动期间，下载图标会适当缩小、并从灰色变成蓝色。</p><p>虽然尚不清楚未来的版本迭代，但下载气泡应该具有与底栏相同的功能选项，包括打开、在文件夹中显示等。</p><p><img src="https://static.cnbetacdn.com/article/2022/0210/14b85593499bbf7.png" referrerpolicy="no-referrer"></p><p>功能<a href="https://chromium-review.googlesource.com/c/chromium/src/+/3442773" target="_self">提交页面</a>写道：</p><blockquote><p>● 添加了下载气泡结构</p><p>● 添加了 DownloadBubbleUIController，以从最近的下载中创建主视图、并通过 DownloadDialogView 在页眉和页脚之间绘制。</p><p>● 添加了 DownloadRowView 和 DownloadRowListView 占位符，后续更新会补上。</p></blockquote>   
</div>
            