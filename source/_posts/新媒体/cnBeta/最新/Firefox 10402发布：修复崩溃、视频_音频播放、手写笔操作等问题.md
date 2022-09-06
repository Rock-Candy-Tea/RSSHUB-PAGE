
---
title: 'Firefox 104.0.2发布：修复崩溃、视频_音频播放、手写笔操作等问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0906/d28eb491e8ea727.webp'
author: cnBeta
comments: false
date: Tue, 06 Sep 2022 08:05:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0906/d28eb491e8ea727.webp'
---

<div>   
Mozilla 计划在今天晚些时候推出 Firefox 104.0.2 稳定版更新。<strong>本次维护版本更新主要修复了内存溢出（out-of-memory）崩溃、视频和音频播放问题，以及在使用触控设备或者手写笔时遇到的一些问题。</strong><br>
 <p style="text-align: left;">下载地址：<a href="https://ftp.mozilla.org/pub/firefox/releases/104.0.2/" _src="https://ftp.mozilla.org/pub/firefox/releases/104.0.2/" target="_blank">https://ftp.mozilla.org/pub/firefox/releases/104.0.2/</a><br style="text-align: left;"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0906/d28eb491e8ea727.webp" alt="jo7otiqg.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Firefox 104.0.2 将会在今天玩些时候发布。由于浏览器内置的升级功能，大部分安装用户都会自动升级。对于等不及的用户来说，也可以通过 Mozilla 的官网进行下载。</p><p style="text-align: left;">Firefox 104.0.2 修复了存在于此前版本中的 4 个非安全漏洞。其中一项修复，修复了自 Firefox 102 版本以来在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 设备上 32 位 Firefox 浏览器的崩溃问题。</p><p style="text-align: left;">根据 Mozilla 错误跟踪网站上的错误报告和 Firefox 中更改的代码，问题似乎是由报告数据规范引起的，可能“任意长”。该问题也在即将发布的 Firefox 102 ESR 更新中得到修复。</p><p style="text-align: left;">Firefox 104.0.2 中修复的另外两个问题解决了浏览器中的视频和播放问题。据 Mozilla 称，两者有时都会影响 Firefox 中视频和音频内容的播放。</p><p style="text-align: left;">问题发生在通过“跨域帧 src 属性”或“Content-Security-Policy:sandbox”加载的视频和音频播放。这两个问题都阻止了媒体的播放，并且有类似的原因。</p><p style="text-align: left;">Firefox 在这两种情况下都重用了初始文档的响应以进行优化。虽然这适用于许多用例，但它阻止了媒体的播放。在 Stable 或 ESR 上安装新版本后，Firefox 用户不应再遇到上述问题。</p><p style="text-align: left;">第四个也是最后一个问题解决了影响触摸设备和触控笔用户的问题。该错误阻止了触摸和手写笔用户在页面上拖动滚动条。Firefox 104.0.2 是第二个版本。 Mozilla 在 8 月下旬发布了 Firefox 104，并推出了 Firefox 104.0.1 以解决 YouTube 上的播放问题。</p>   
</div>
            