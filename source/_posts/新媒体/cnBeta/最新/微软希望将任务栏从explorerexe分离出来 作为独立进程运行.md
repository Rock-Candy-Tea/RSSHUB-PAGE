
---
title: '微软希望将任务栏从explorer.exe分离出来 作为独立进程运行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0326/6423c034c474af2.jpg'
author: cnBeta
comments: false
date: Fri, 26 Mar 2021 03:36:48 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0326/6423c034c474af2.jpg'
---

<div>   
<strong>在代号为“Sun Valley”的 Windows 10 21H2 功能更新中，微软有计划将任务栏从 Windows 文件资源管理器进程(explorer.exe)中分离出来，作为独立的进程运行。</strong>在当前 Windows 10 系统中，explorer.exe 进程负责文件资源管理器以及大部分的用户界面（UI）显示，其中就包括任务栏、操作中心等等。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0326/6423c034c474af2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0326/6423c034c474af2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">通常情况下，explorer.exe 进程能够稳定运行，不过当它卡顿的时候就可能会导致桌面停止响应，让任务栏隐藏。当发生这种情况时，您无法与任务栏或其他体验进行交互，这包括钉在任务栏或跳转列表（右键菜单）上的应用程序。</p><p style="text-align: left;">在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 系统中，用户需要通过任务管理器来从重启电脑或者 Windows Explorer 进程。为了彻底解决这些问题，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>现在计划将任务栏从 explorer.exe 进程中剥离出来。在最新的预览版中，已经发现了对 "taskbar.dll "的引用，这似乎表明微软希望在未来为任务栏保留一个单独的进程。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0326/80542c2427c03fa.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">值得注意的是，目前只是将任务栏的部分内容从 explorer.exe中移出，任务栏并不会在短期内获得自己的进程。资源管理器仍然包含任务栏代码，但将来可以改用 DLL 实现，这样可以减少对 explorer.exe 的依赖。</p><p style="text-align: left;">在进程独立之后也可以让任务栏运行的更加流畅。通过减少对资源管理器的依赖，微软应该可以保护它免受文件资源管理器可能引起的潜在问题。对于消费者来说，最终的结果是更可靠的任务栏体验和更灵敏的响应，因为它将不再依赖于文件资源管理器。</p>   
</div>
            