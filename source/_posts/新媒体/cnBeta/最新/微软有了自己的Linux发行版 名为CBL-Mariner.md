
---
title: '微软有了自己的Linux发行版 名为CBL-Mariner'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0712/fd47a6c5483a58f.jpg'
author: cnBeta
comments: false
date: Mon, 12 Jul 2021 11:36:07 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0712/fd47a6c5483a58f.jpg'
---

<div>   
近年来，微软对Linux的爱越来越多，这已经不是什么秘密了--看看Windows Subsystem for
Linux就是一个例子。<strong>尽管如此，在得知微软还有自己的Linux发行版时，你还是可能会感到惊讶。微软Azure团队的一名成员最近发表的一篇博文分享了该公司的Linux发行版的细节。</strong><br>
 <p>在这篇文章中，胡安-曼努埃尔-雷伊（Juan Manuel Rey）揭示了这一创造，被称为CBL-Mariner的发行版被<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>工程团队用来构建其云基础设施和边缘产品和服务。</p><p><img src="https://static.cnbetacdn.com/article/2021/0712/fd47a6c5483a58f.jpg" title alt="microsoft_mariner.jpg" referrerpolicy="no-referrer"></p><p>在他的博文中，雷伊一开始就说。"地狱是冰冷的，因为在微软有自己的Linux发行版"。他继续解释说，这个内部发行版不是像Ubuntu或Fedora那样的通用发行版，它虽然与我们熟悉的Fedora或Photon-OS等比较相似，源代码也是完全开放的，用户可以自行编译试玩，但没有对外生成和分发ISO镜像。<br></p><p>CBL-Mariner是由微软的Linux系统组创建的，也就是<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Subsystem for Linux版本2背后的那些人，CBL是Common Base Linux的缩写。</p><p>CBL-Mariner软件包系统是基于RPM的，软件包更新系统同时使用dnf和tdnf，后者全称Tiny DNF，是一个基于dnf的软件包管理器，来自VMware的Photon OS。</p><p>CBL-Mariner还支持基于镜像的更新机制，其使用RPM-OSTree来实现，rpm-ostree是一个基于OSTree的开源工具，用于管理可启动的、不可变的、版本化的文件系统树。rpm-ostree背后的想法是使用一个客户-服务器架构，以可靠的方式保持Linux主机的更新和与最新的软件包同步。</p><p>CBL-Mariner遵循 "默认安全"原则，操作系统的大部分方面都是以安全为重点的。它有一个加固的内核、签名更新、ASLR、基于编译器的加固和防篡改日志等许多功能。</p><p>如果你对它的源代码感兴趣，可以去GitHub看看：</p><p><a href="https://github.com/microsoft/CBL-Mariner/releases/tag/1.0.20210628-1.0" _src="https://github.com/microsoft/CBL-Mariner/releases/tag/1.0.20210628-1.0" target="_blank">https://github.com/microsoft/CBL-Mariner/releases/tag/1.0.20210628-1.0</a><br></p>   
</div>
            