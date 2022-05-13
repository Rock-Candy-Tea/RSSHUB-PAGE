
---
title: 'Ubuntu的Chromium Snap现在允许启用本地Wayland支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0513/a821e393d6be9a1.jpg'
author: cnBeta
comments: false
date: Fri, 13 May 2022 12:56:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0513/a821e393d6be9a1.jpg'
---

<div>   
那些通过Snap软件包在Ubuntu上使用Chromium网络浏览器的用户，最新的构建版本现在已经启用了（可选）Wayland支持。长期以来，X11和Wayland Ozone支持以各种测试程序的形式存在。<br>
<p>然而，用Ubuntu的Chromium Snap启用实验性的本地Wayland支持是不可能的，因为该版本强制关闭了Wayland支持。</p><p>追溯到2020年，Ubuntu的chromium-browser一直有一个关于Chromium的Wayland支持被"DISABLE_WAYLAND"选项禁用的错误报告。</p><p><img src="https://static.cnbetacdn.com/article/2022/0513/a821e393d6be9a1.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>这个bug报告的讨论在3月重新开始，现在随着最新的Chromium snap构建，新的变化已经落地，DISABLE_WAYLAND支持没有被设置，因此迫使Ozone中的Wayland支持代码不能被构建。</p><p>默认情况下，Ubuntu上的Chromium浏览器Snap仍然默认为X11/XWayland，但如果需要的话，至少它现在允许在运行时选择使用本地Wayland代码路径。</p><p>那些在过去一周内运行Chromium Snap构建的用户，如果想使用网络浏览器的本地Wayland代码，可以通过chrome://flags/#ozon-platform-hint调整你的默认偏好。</p><p>了解更多：</p><p><a href="https://git.launchpad.net/~chromium-team/chromium-browser/+git/snap-from-source/commit/?id=a4f41b5c065e14e954bc81d2d3e2b0c7fc26fc4d" _src="https://git.launchpad.net/~chromium-team/chromium-browser/+git/snap-from-source/commit/?id=a4f41b5c065e14e954bc81d2d3e2b0c7fc26fc4d" target="_blank">https://git.launchpad.net/~chromium-team/chromium-browser/+git/snap-from-source/commit/?id=a4f41b5c065e14e954bc81d2d3e2b0c7fc26fc4d</a><br></p>   
</div>
            