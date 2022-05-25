
---
title: 'Windows Server 2022现在开始支持WSL2 Linux发行版'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0525/f2d18104598849a.jpg'
author: cnBeta
comments: false
date: Wed, 25 May 2022 15:09:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0525/f2d18104598849a.jpg'
---

<div>   
微软已经宣布，现在可以在Windows Server
2022中运行基于WSL2的Linux发行版。这一变化是随着最新的累积版推出的，它使操作系统的构建号达到了20348.740，尽管官方更新日志中没有提到这一变化，但微软的Craig
Loewen在GitHub的评论中确认了对WSL2的支持，这是对Windows Server 2022中缺乏对它的支持的持续关注的回应。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0525/f2d18104598849a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0525/f2d18104598849a.jpg" title alt="7-Zip-Linux-WSL-Windows-10.jpg" referrerpolicy="no-referrer"></a></p><p>WSL2（<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Subsystem for Linux 2的缩写）于2019年5月首次公布，它在Windows 10中首次出现的版本为2004，于2020年上半年发布。当时，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>也是通过半年一次的更新来支持Windows Server，就像Windows 10一样，只有运行Windows Server半年更新频率的渠道用户才能得到对WSL2的支持，因此如果你使用的是Windows Server 2019，那就不太走运。</p><p>去年，微软停止了Windows Server的半年期渠道，回到了主要版本，如Windows Server 2022。然而，就像Windows Server 2019一样，这个新版本仍然不包括对WSL2的支持。现在，几乎一年之后，它终于来了。</p><p>有了WSL2，微软开始将一个完整的Linux内核与Windows一起运行，这使得系统调用可以完全兼容。Linux发行版的性能明显比基于WSL原始版本的发行版要好。现在，Linux在一种虚拟机（VM）中运行，但它被设计成比传统的虚拟机更轻、更有原生感觉的体验。</p><p>如果你正在运行Windows Server 2022，并且你想使用WSL2 Linux发行版，你可以从Windows Update获取最新的更新（需要手动寻找），或者你可以在这里下载：</p><p><a href="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5014021" _src="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5014021" target="_blank">https://www.catalog.update.microsoft.com/Search.aspx?q=KB5014021</a><br></p><p>如果你不着急，这一变化将包括在下一个"补丁星期二"更新中，该更新将于6月14日到来。</p>   
</div>
            