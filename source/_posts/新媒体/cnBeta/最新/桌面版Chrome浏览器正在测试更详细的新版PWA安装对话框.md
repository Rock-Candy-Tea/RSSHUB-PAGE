
---
title: '桌面版Chrome浏览器正在测试更详细的新版PWA安装对话框'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0716/08324921a971162.jpg'
author: cnBeta
comments: false
date: Sat, 16 Jul 2022 05:19:32 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0716/08324921a971162.jpg'
---

<div>   
近年来，渐进式 Web 应用程序（简称 PWA）已在某些网站上变得愈加普遍。<strong>对于桌面版 Chrome 浏览器的老用户来说，应该不会对当前的 PWA 应用安装的弹窗感到陌生。</strong>遗憾的是，当前该弹窗所能呈现的信息仍相当有限。不过在最新 Canary 开发分支中，我们已经预见了它的最新变化。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0716/08324921a971162.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0716/08324921a971162.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：<a href="https://techdows.com/2022/07/chrome-desktop-pwa-new-install-dialog.html" target="_self">Techdows</a>）</p><p>如图所示，若某个站点希望用户下载安装 PWA 应用，浏览器会在屏幕上某处弹出这样一个对话框。</p><p>与此同时，Android / 移动版 Chrome 浏览器也在过去一年里积极调整，以便用户能够更准确地了解到当前正在安装的内容。</p><p><img src="https://static.cnbetacdn.com/article/2022/0716/b8c1e8baf4691d5.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p>现阶段桌面版 Chrome 浏览器，只会在 PWA 安装弹窗中显示应用图标和名称，但缺乏其它重要的信息。</p><p>而隐藏在 <a href="https://bugs.chromium.org/p/chromium/issues/detail?id=1326252" target="_self">Chrome Canary</a> 尝鲜频道的最新变化， 已经能够在 PWA 安装弹窗中显示更详细的产品描述。</p><p><img src="https://static.cnbetacdn.com/article/2022/0716/ce2c923d118dfef.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>感兴趣的朋友，可参照如下方法，为桌面版 Chrome 浏览器启用新版 PWA 安装弹窗样式：</p><blockquote><p>（1）如已开启，请先关闭所有已打开的 Chrome 进程。</p><p>（2）右键点击桌面图标，在其‘属性’页面的‘目标’路径中添加如下内容。</p><p>（3）在 chrome.exe 可执行文件后头补上 --enable-features=DesktopPWAsDetailedInstallDialog</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0716/dec3ea8b0e0a7f9.jpg" alt="4.jpg" referrerpolicy="no-referrer"></p><p>（4）通过修改后的桌面快捷方式，重新启动 Chrome 浏览器。</p><p>（5）访问任意支持 PWA 的站点，比如 Twitter.com 。</p><p>（6）点击地址栏上的‘安装’图标，然后就可以看到更细致的 PWA 应用安装描述了。</p>   
</div>
            