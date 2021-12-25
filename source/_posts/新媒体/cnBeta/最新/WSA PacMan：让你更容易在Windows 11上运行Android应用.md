
---
title: 'WSA PacMan：让你更容易在Windows 11上运行Android应用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1225/20ca41e8f936abb.webp'
author: cnBeta
comments: false
date: Sat, 25 Dec 2021 03:14:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1225/20ca41e8f936abb.webp'
---

<div>   
Windows 11 预览版引入了对 Windows SubSystem for Android（WSA）模块的原生支持，允许用户在不借助第三方模拟器的情况下在桌面端运行 Android 应用。不过局限之一是，目前仅支持亚马逊的 AppStore 应用程序。值得庆幸的是，你可以使用命令行工具来安装 Android 应用，甚至在非 Insider PC 上运行 WSA，也可以避免使用 WSA 管理器。<br>
  <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1225/20ca41e8f936abb.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">如果你不想使用命令行（这对初学者来说可能很棘手），有一个更简单的方法来做到这一点。一个名为“WSA PacMan”的新应用程序，可在 Github 上进行审查和反馈，让你在不打开命令提示符或系统设置的情况下安装 Android 应用程序。</p><p style="text-align: left;">顾名思义，它是一个第三方开源软件包管理器，专门为 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Subsystem for Android 构建。它作为一个 GUI，它在后台运行 ADB 命令来安装Android应用，它也依赖于默认端口，所以你不必对应用或 WSA 本身做任何修改。WSA PacMan 是一个 ADB 命令的 GUI，它依赖于操作系统中包含的原始 WSA，所以你确实需要设置一次 WSA。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1225/c38bf17de8e2a06.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">首先，你需要一个运行 Windows 11 并支持 Windows Subsystem for Linux 的设备。其次，确保你已经安装或启用了 Windows Subsystem for Android，并打开了调试选项。否则，软件包管理器将无法在你的设备上安装应用程序。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1225/f812ab926d79000.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1225/e1f7a221181f9dc.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">WSA PacMan 是一个 ADB 命令的 GUI，它依赖于操作系统中包含的原始 WSA，所以你确实需要设置一次 WSA。</p><p style="text-align: left;">如何用 GUI 安装Android应用</p><p style="text-align: left;">● 前往<a href="https://github.com/alesimula/wsa_pacman/releases" target="_blank"> Github 的发布页面</a>，下载 WSA PacMan。</p><p style="text-align: left;">● PackMan应用程序将自动连接到WSA，因为它使用默认端口 58526 进行调试。</p><p style="text-align: left;">● 正如你在上面的截图中看到的，WSA PacMan有一个简单的界面，你只需要找到你想运行的APK文件。</p>   
</div>
            