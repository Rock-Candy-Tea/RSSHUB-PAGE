
---
title: 'Chrome版本号升至三位有啥影响？Chrome 96-99版本将进行测试'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0923/4dccebb825e493d.jpg'
author: cnBeta
comments: false
date: Thu, 23 Sep 2021 03:28:56 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0923/4dccebb825e493d.jpg'
---

<div>   
当 Google Chrome 版本号达到 100 切换到三位数之后，网站会如预期那样正常工作还是会出现故障？<strong>在 Chrome 96-99 版本中，Google 通过将 User-Agent 字符串中的版本号替换为三位数的“100”数字进行测试。</strong>目前，Chrome 是全球最受欢迎的浏览器，大多数开发人员确保他们的网站和应用程序在 Chrome 中顺利运行。<br>
<p style="text-align: left;">每当用户访问一个网站时，浏览器就会向网络服务器发送一个包括 User-Agent 的 HTTP 头，以提供适当的版本。UA 显示了用户的浏览器、操作系统和其他设备细节。这些都是出于兼容性的原因，但现在被用来对用户进行指纹识别。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/4dccebb825e493d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/4dccebb825e493d.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">出于对这一问题的关注，Mozilla 正在进行一项 UA 字符串实验，在对 Nightly 人群进行这一测试之前，Mozilla 员工 Chris Peterson 用 100 版的 Firefox 浏览器覆盖了UA字符串，并在四个月内没有发现访问网站的问题（除了Slack，其信息菜单被破坏）。</p><p style="text-align: left;">在Mozilla之后，Google现在正在强制将 Chrome 96-99 版本中的用户代理改为 100，看看是否会导致任何问题。根据 Chrome 和 Firefox 的发布时间表:</p><blockquote style="text-align: left;"><p style="text-align: left;">● Chrome 100 稳定版于 2022 年 3 月 29 日发布</p><p style="text-align: left;">● Firefox 100 在 2022 年 3 月 7 日登陆 Nightly</p></blockquote><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/d0319e6496dd71e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/d0319e6496dd71e.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">因此，很明显，Chrome 浏览器首先达到 100，如果有的话，它可能会比Firefox遇到网站兼容性问题。想要测试，步骤如下：</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 启动 Chrome Canary</p><p style="text-align: left;">2. 访问 chrome://flags</p><p style="text-align: left;">3. 搜索“user agent”，然后将“Force major version to 100 in User-Agent”下拉菜单选择“Enabled”，并重启浏览器</p></blockquote><p style="text-align: left;">打开这个 Flag 后，Chrome 会将 96、97、98 或 99 版本的 UA 设置为100。那么，从技术上讲，尽管实际版本是96或<=99，但 Chrome 仍以版本 100 运行，而且浏览器会向您连接的网站发送以下用户代理信息：</p><blockquote style="text-align: left;"><p style="text-align: left;">Mozilla/5.0 (<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4650.0 Safari/537.36</p></blockquote>   
</div>
            