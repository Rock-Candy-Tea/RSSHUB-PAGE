
---
title: 'Linux用户吐槽微软packages网站故障后迟迟未能恢复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0620/5e9e00230866209.png'
author: cnBeta
comments: false
date: Sun, 20 Jun 2021 05:17:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0620/5e9e00230866209.png'
---

<div>   
The Register 报道称：<strong>尽管微软近年来积极表达了对 Linux 的热爱，但刚刚发生在 packages.microsoft.com 网站上的事情，还是伤了不少铁杆粉丝们的心。</strong>由于网站服务离线，不少人在尝试 aapt-get 时遭遇了 404 错误。乍一看，这个问题似乎仅影响 Ubuntu，但微软 OpenJDK 及其 .NET 旗舰平台的一些用户也都陷入了挣扎。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0620/5e9e00230866209.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://github.com/dotnet/core/issues/6381" target="_self">GitHub</a>）</p><p>更糟糕的时候，ODBC、<a data-link="1" href="https://microsoft.pvxt.net/zaZYr" target="_blank">Visual Studio</a> Code、甚至 Microsoft Edge 包链接也都被破坏了。<strong>微软软件工程师 Rahul Bhandari 在 GitHub 上发帖称：</strong></p><blockquote><p>我们的基础设施团队仍在努力解决这个问题，他们遇到了一些空间方面的困扰，但应该很快就能解决。至于确切的修复时间，目前还无法给出预估。</p></blockquote><p>对于此事，一些开发者吐槽道：“要是微软有一些超级可扩展的云来存储数据就好了，那样它就能切实满足用户的需求。如果搞不定的话，大不了换成亚马逊 AWS S3 存储桶嘛！”</p><p><img src="https://static.cnbetacdn.com/article/2021/0620/89bfd2eeb904a51.png" referrerpolicy="no-referrer"></p><p>从当前汇总的多方信息来看，问题似乎主要集中于 packages.microsoft.com 本身，一些用户汇报通过 Snap 来安装 .NET 能够成功。</p><p>另有用户表示，通过虚拟专用网连接至不同区域的端点时，是可以找到丢失的包的。</p><p>据此猜测，微软可能在镜像站点的配置上出现了 bug，尽管我们无法想象到底要闹出怎样的乌龙，才会让微软在自家的服务器上折腾出这样的故障。</p><p>截止发稿时，The Register 的 Richard Speed 仍无法在测试用的 Ubuntu 平台上顺利实现 apet-get 功能。</p><p>最后，但愿微软爱 Linux 的行动不止停留在口头上，而是能够尽快地让 packages.microsoft.com 站点速恢复正常。</p>   
</div>
            