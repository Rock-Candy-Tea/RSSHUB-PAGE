
---
title: 'M1 Mac连接4K以下显示器显示模糊？这有一个解决方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1208/5bc285fc3a512b5.webp'
author: cnBeta
comments: false
date: Wed, 08 Dec 2021 01:39:48 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1208/5bc285fc3a512b5.webp'
---

<div>   
自 Apple Silicon 芯片上线以来，在苹果支持论坛、Reddit 社区、Twitter 等社交平台上不断有用户反馈 M1 Mac 设备连接 4K 分辨率以下显示器，会出现文字显示模糊、分辨率低于预期等问题。<strong>应用程序开发人员 Istvan Toth 已经调查了这个问题，并开发了一个解决方案。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1208/5bc285fc3a512b5.webp" alt="ykho1wlw.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Toth 表示这个问题的核心是，在连接某些第三方显示器的时候，macOS 没有启用其基于 Retina 的高像素密度模式（HiDPI）。此外，M1 Mac 可能提供比第三方显示器所能提供的更低的分辨率。</p><p style="text-align: left;">Toth 表示：“这一切都归结为字体和小部件的缩放，以及分辨率的独立性。<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>所谓的 HiDPI 模式只是操作系统识别出插入的显示器以超高的像素数运行，并相应地调整桌面和用户界面的比例”。</p><p style="text-align: left;">Toth 推测，这个问题可能是由于基于 Arm 的 Mac 设备使用与 iOS 或 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>OS 相同的图形驱动代码。那些设备不需要支持多个显示器，或者不在特定范围内的显示器。</p><p style="text-align: left;">他表示：“在一些显示器上，比如那些分辨率为 1080p 或 1440p 的 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a> 以下的显示器，Apple Silicon Mac 不允许高分辨率的显示模式，即 HiDPI，并且不能很好地进行缩放。这导致低分辨率的桌面体验锁定用户，字体和GUI过小或过大，而且没有办法改变”。</p><p style="text-align: left;">在一些显示器上，例如那些在1080p范围内的显示器，这个问题并不明显。但是，拥有更大或更宽的QHD显示器的用户可能会看到字体太小，小工具和图形模糊不清。Toth 说，这个问题是基于软件的，可能在 macOS 更新中得到解决。同时，他已经创建了一个可以缓解这个问题的应用程序。</p><p><img src="https://static.cnbetacdn.com/article/2021/1208/5c90ed92eaecebb.webp" style referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2021/1208/6e93fb78a4e1703.webp" style referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2021/1208/ec17b76814b98cb.webp" style referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2021/1208/9c5f4ceb35bf146.webp" style referrerpolicy="no-referrer"></p><p style="text-align: left;">Toth 的应用程序叫做 <a href="https://github.com/waydabber/BetterDummy" target="_blank">BetterDummy</a>，基本上在软件中创建了一个虚拟显示器，并将其镜像到一个真实的显示器上。这可以哄骗 macOS 启用适当的显示机制。BetterDummy 采用 MIT 授权方式，并且是开源的。</p>   
</div>
            