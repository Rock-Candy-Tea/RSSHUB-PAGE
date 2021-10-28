
---
title: '_技巧_非Windows Insider如何在Windows 10上安装新版Microsoft Store'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1028/dfa082f7673834a.jpg'
author: cnBeta
comments: false
date: Thu, 28 Oct 2021 00:23:20 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1028/dfa082f7673834a.jpg'
---

<div>   
今年 6 月，微软宣布了 Windows 11 系统中的新 Microsoft Store。<strong>在测试超过 3 个月之后，全新的 Microsoft Store 开始分阶段向 Windows 10 用户开放，预估会在未来几个月内完成部署。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1028/dfa082f7673834a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1028/dfa082f7673834a.jpg" alt="t3dprreg.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">如果目前你身处 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Insider 项目的 Release Preview 频道，且运行 Windows 10 Version 21H2，那么可以通过更新方式获得全新的 Microsoft Store。不过对于那些非 Windows Insider 项目用户，你也可以通过以下方式手动安装新版 Microsoft Store。</p><blockquote style="text-align: left;"><p style="text-align: left;">1. 从这里<a href="https://1drv.ms/u/s!AjvFtGmbbS1LhD6mFSiZ5TNPieM0?e=cbtZ9d" target="_blank">下载新版 Microsoft Store</a></p><p style="text-align: left;">2. 打开 PowerShell</p><p style="text-align: left;">3. 使用 cd 命令，导航到你保存商店更新的位置。例如，如果你的浏览器的默认下载位置是“下载”"文件夹，输入 cd C:\Users\username\Downloads。</p><p style="text-align: left;">4. 输入 Add-AppxPackage <package name.<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>xbundle>，最终的命令可能是 Add-AppxPackage Microsoft.WindowsStore_22110.1401.10.0_neutral___8wekyb3d8bbwe.Msixbundle</p></blockquote><p style="text-align: left;">与目前的应用商店相比，它看起来不那么杂乱，而且新的商店是基于XAML（UWP）代码，而不是WebView，所以你可以期待更好的性能，特别是在互联网连接缓慢的时候。</p>   
</div>
            