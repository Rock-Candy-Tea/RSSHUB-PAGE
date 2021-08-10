
---
title: '_图_微软Google正合作 为Chromium浏览器开发全新虚拟键盘API'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0810/0b901d7d5a25393.jpg'
author: cnBeta
comments: false
date: Mon, 09 Aug 2021 23:51:38 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0810/0b901d7d5a25393.jpg'
---

<div>   
<strong>微软和Google正在开展合作，为基于 Chromium 的浏览器开发名为“VirtualKeyboard”的全新 API。</strong>通过 API，开发者能够更好地对 Windows、macOS、Chrome OS 和 Android 端的现有虚拟输入法进行更新，并提供更好的控制。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0810/0b901d7d5a25393.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0810/0b901d7d5a25393.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">根据官方披露的文件，“VirtualKeyboard” 是一个公共的 JS API，它将屏幕键盘的控制权交给了网络开发者。目前，开发者不能显示/隐藏以提高/取消 VK，而且键盘的性能对于开发者希望用户使用网站的内置/渲染键盘在 Android 上输入密码的场景并不理想。</p><p style="text-align: left;">该文件写道：“另外，在某些情况下，作者只想让光标显示在一个可编辑的元素里面，直到用户再次点击显示 VK。这在 inputMode=none 的情况下是可行的，但 inputMode 混淆了两个不同的概念（布局和VK的可见性），应该分开来以满足更复杂的情况”。</p><p style="text-align: left;">微软和Google正在研究一项新的功能，它将处理隐藏/显示键盘和控制虚拟键盘改变可见性时视觉视口是否调整大小的问题。理论上，VirtualKeyboard APIs将为开发者更新，对虚拟键盘何时显示或隐藏有更多控制。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0810/a79343f36d52550.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0810/a79343f36d52550.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">微软表示：“该 API 还会影响触发事件，描述VK和布局视口的交叉点，并可以选择浏览器不调整其视觉视口的大小，以响应VK可见性的变化”。</p><p style="text-align: left;">与网络浏览器或网络应用不同，原生Android或<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>应用有能力监听操作系统的事件。利用这个新的API，开发者在桌面和移动端为网络带来了增强的体验。因此，网站上的可编辑区域将始终保持可见。</p><p style="text-align: left;">开发人员可以选择加入一种新的风格，停靠的虚拟键盘将覆盖内容，开发人员将能够为虚拟键盘优化布局视口。例如，当虚拟键盘出现在你的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>上时，浏览器不会将可编辑的元素滚动到视图中，也不会在设置overlayscontent标志时调整视觉/布局视口的大小以匹配新窗口的大小。</p>   
</div>
            