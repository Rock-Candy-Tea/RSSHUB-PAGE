
---
title: 'Google Chrome 100 Beta发布 用户代理字符串作用开始逐渐降低'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0306/aa6b18410c7832e.png'
author: cnBeta
comments: false
date: Sat, 05 Mar 2022 23:53:14 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0306/aa6b18410c7832e.png'
---

<div>   
Google Chrome和Mozilla
Firefox都在迅速接近100版本，这有可能破坏一些错误识别浏览器版本的网站（可能导致访问不正常，这有点类似于众所周知的千年虫）。两种浏览器都在研究可能的解决方案，现在Chrome
100已经到达Beta通道，对版本报告和其他新功能进行了修改。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0306/aa6b18410c7832e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0306/aa6b18410c7832e.png" title alt="Chrome-100-beta-launches-for-Android.png" referrerpolicy="no-referrer"></a></p><p>Google在Chromium博客文章中写道："Chromium 100将是最后一个默认支持未减少的用户代理字符串（UA）的版本（以及相关的navigator.userAgent、navigator.appVersion和navigator.platform DOM API）。允许网站测试User-Agent的起源试验将于2022年4月19日结束。在该日期之后，用户代理字符串将逐渐减少"。</p><p>几十年来，用户代理字符串一直是网络浏览器的核心组成部分，允许网站根据浏览器、浏览器的版本、CPU架构和其他数据改变其行为。为了保障隐私，浏览器已经慢慢开始限制用户代理字符串中的信息（例如，所有<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a>的用户代理字符串不包括iPhone的型号），因为它们很容易被用于指纹识别。Google建议使用较新的用户代理客户端提示API来代替，这比用户代理字符串更安全，更加难以破坏网站。</p><p>Chrome Beta 100还包括其他一些新功能。例如，在桌面平台上有一个新的多屏幕窗口放置API，它允许网站检测计算机的显示器，并将不同的窗口放置在特定的屏幕上。还有数字商品API和一些新的JavaScript功能的Origin Trials。</p><p>你可以通过从Google官方网站下载后在桌面平台上试用Chrome Beta。Android设备也可以通过Google Play商店下载Chrome Beta，链接如下：</p><p><a href="https://www.google.com/chrome/beta/" _src="https://www.google.com/chrome/beta/" target="_blank">https://www.google.com/chrome/beta/</a></p><p>在所有平台上，Chrome测试版可以与其他版本的Chrome浏览器一起运行，因此不会对已有的用户配置文件造成任何破坏。</p>   
</div>
            