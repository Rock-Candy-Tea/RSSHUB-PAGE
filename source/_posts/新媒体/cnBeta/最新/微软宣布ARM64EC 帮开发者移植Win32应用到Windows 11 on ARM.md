
---
title: '微软宣布ARM64EC 帮开发者移植Win32应用到Windows 11 on ARM'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0630/fcee68ec9e25f1a.jpg'
author: cnBeta
comments: false
date: Wed, 30 Jun 2021 01:53:25 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0630/fcee68ec9e25f1a.jpg'
---

<div>   
<a href="https://blogs.windows.com/windowsdeveloper/2021/06/28/announcing-arm64ec-building-native-and-interoperable-apps-for-windows-11-on-arm/?WT.mc_id=twitter-0000-windowsdocs" target="_blank">微软昨日宣布了 ARM64EC（Emulation Compatible，模拟兼容）</a>，这是一种为 Windows 11 on ARM 系统创建应用的新方式。ARM64EC 使开发者能够轻松地将其现有的 Win32 应用程序移植到 Windows 11 on ARM 系统上。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0630/fcee68ec9e25f1a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0630/fcee68ec9e25f1a.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0630/50665e1ae3c56e7.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0630/50665e1ae3c56e7.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">对于 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 on ARM，开发者必须为 ARM 设备重新编译他们的 Win32 应用程序。如果有问题，开发者就需要为 ARM 设备重写他们的整个应用程序。</p><p style="text-align: left;">而利用 ARM64EC，开发者能够逐步开发他们的 ARM 应用程序。首先，他们可以确定其代码库中最受益于本地性能的部分，并将其重建为 ARM64EC。应用程序的其他部分将保持模拟 x64 的完全功能，但重新编译的 ARM64EC 部分现在将具有本地速度。 随着时间的推移，他们可以将更多的应用程序重新编译为 ARM64EC，以进一步提高性能并节省 ARM 设备的续航。</p><p style="text-align: left;">ARM64EC 是适用于 Windows 11 on ARM 的新应用安装接口（ABI），它以原生速度运行，并可与 x64 互操作。应用程序、进程甚至模块可以根据需要自由混合和匹配ARM64EC和x64。应用程序中的 ARM64EC 代码将原生运行，而任何 x64 代码将使用 Windows 11 on ARM 的内置仿真运行。</p><p style="text-align: left;">微软的内部团队已经在使用 ARM64EC。事实上，<a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 团队在即将推出的 64 位 Office for ARM 中使用了 ARM64EC，这样现有的 x64 插件就可以在 Windows 11 on ARM 设备上正常地运行。</p>   
</div>
            