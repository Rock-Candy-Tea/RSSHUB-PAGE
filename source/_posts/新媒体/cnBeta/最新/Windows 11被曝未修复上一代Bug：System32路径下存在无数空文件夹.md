
---
title: 'Windows 11被曝未修复上一代Bug：System32路径下存在无数空文件夹'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1102/95f86ea4e64b3d6.png'
author: cnBeta
comments: false
date: Tue, 02 Nov 2021 03:57:44 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1102/95f86ea4e64b3d6.png'
---

<div>   
GHacks 的 Martin Brinkmann 指出：<strong>基于 21H2 开发分支的 Windows 11 操作系统，似乎继承了 Windows 10 时代的一个 Bug —— 在 C:\Windows\System32 的某个路径下，竟然出现了数百上千的空文件夹。</strong>一番调查后发现，该问题似乎由名为 ProvTool.exe 的“配置包运行时处理”工具导致，能够无视之直接删除而不会导致任何问题。<br>
 <p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1102/95f86ea4e64b3d6.png"><img data-original="https://static.cnbetacdn.com/article/2021/1102/95f86ea4e64b3d6.png" src="https://static.cnbetacdn.com/thumb/article/2021/1102/95f86ea4e64b3d6.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（来自：<a href="https://www.ghacks.net/2021/11/01/windows-11-creates-lots-of-empty-folders-in-a-system32-directory/" target="_self">GHacks</a>）</p><p>事实上，Provisioning Package Runtime Processing 工具导致的问题，自 2019 年以来就一直困扰着许多 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 用户。</p><p>但没想到的是，它竟然一路延续到了基于 21H2 开发分支的 Windows 11 操作系统上。</p><p>如果你也对系统文件（夹）的“纯洁性”持有一定的强迫症，还请移步至 C:\Windows\System32\config\systemprofile\AppData\Local 路径下检视一番。</p>   
</div>
            