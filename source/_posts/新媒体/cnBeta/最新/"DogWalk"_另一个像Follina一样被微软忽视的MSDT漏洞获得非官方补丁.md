
---
title: '"DogWalk"_另一个像Follina一样被微软忽视的MSDT漏洞获得非官方补丁'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0608/27a1207bbd44289.png'
author: cnBeta
comments: false
date: Wed, 08 Jun 2022 09:10:12 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0608/27a1207bbd44289.png'
---

<div>   
最近，一个被称为"Follina"的微软支持诊断工具（MSDT）零日漏洞浮出水面，当时安全研究人员发现了这个漏洞，而且由于媒体的报道，这个消息已经传开。微软最初显然忽视了这个漏洞，认为它是一个非安全问题（，不过后来，该公司承认这是一个远程代码执行（RCE）漏洞，并为其分配了跟踪ID
CVE-2022-30190。<br>
 <p>虽然除了禁用MSDT的步骤外，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>没有提供官方补丁，但0patch团队发布了一个微补丁，你可以从其官方博客文章的链接中下载。</p><p><img src="https://static.cnbetacdn.com/article/2022/0608/27a1207bbd44289.png" title alt="Vuln_7418_NO-CVE_DogWalk_PatchCard_1024x512.png" referrerpolicy="no-referrer"></p><p>继Follina之后，另一个两年前首次报告的零日威胁也浮出水面，与Follina一样，这个威胁显然也被微软忽略了，因为该公司认为它不符合"即时服务要求"。</p><p><img src="https://static.cnbetacdn.com/article/2022/0608/2e0f7c0a4382792.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2022/0608/cddc17f06a2d82d.png" title alt="Invalid_filename.png" referrerpolicy="no-referrer"></p><p>这个还没有跟踪ID或CVE的漏洞被命名为"DogWalk"，它被发现是一个路径穿越漏洞，其载荷可以被落在Windows启动文件夹位置。</p><p>C:\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup</p><p>这意味着当用户下次登录他们的系统时，恶意软件会被执行。下载的diagcab文件有一个网络标记（MOTW），但MSDT忽略了这个警告并仍然运行它，使用户容易受到这种潜在的利用。</p><p><img src="https://static.cnbetacdn.com/article/2022/0608/35d7632dfc67549.png" title alt="DogWalk_patch.png" referrerpolicy="no-referrer"></p><p>0patch的微补丁由简单的11条指令构成，基本上可以阻止这个MSDT文件的运行。和Follina一样，它也适用于以下Windows版本：</p><p>Windows 11 21H2</p><p>Windows 10 21H2</p><p>Windows 10 21H1</p><p>Windows 10 20H2</p><p>Windows 10 2004</p><p>Windows 10 1909</p><p>Windows 10 1903</p><p>Windows 10 1809</p><p>Windows 10 1803</p><p>Windows 7</p><p>Windows Server 2008 R2</p><p>Windows Server 2012</p><p>Windows Server 2012 R2</p><p>Windows Server 2016</p><p>Windows Server 2019</p><p>Windows Server 2022</p><p>要下载该第三方补丁，请到这里链接的0patch官方博客文章，你还可以在文章中找到更多技术细节：</p><p><a href="https://blog.0patch.com/2022/06/microsoft-diagnostic-tools-dogwalk.html" _src="https://blog.0patch.com/2022/06/microsoft-diagnostic-tools-dogwalk.html" target="_blank">https://blog.0patch.com/2022/06/microsoft-diagnostic-tools-dogwalk.html</a><br></p>   
</div>
            