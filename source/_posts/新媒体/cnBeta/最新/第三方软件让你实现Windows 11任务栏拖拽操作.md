
---
title: '第三方软件让你实现Windows 11任务栏拖拽操作'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1230/dbc3c770cc179f2.webp'
author: cnBeta
comments: false
date: Thu, 30 Dec 2021 01:27:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1230/dbc3c770cc179f2.webp'
---

<div>   
Windows 11 的任务栏是重新使用 XAML 编写的，因此在很多任务栏的功能都已经缺失，其中一项就是不支持拖放。也就是说，你无法像 Windows 10 系统那样，将文件拖到已固定在任务栏上的应用程序中来启用该应用来打开该文件。<strong>如果你想要在 Windows 11 上实现该任务栏操作，那么现在有个开源的第三方软件能够实现。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1230/dbc3c770cc179f2.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">当前 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 任务栏操作</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1230/203372f73112088.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">启用第三方软件后实现效果</p><p style="text-align: left;">这款应用名为“Windows11DragAndDropToTaskbarFix”，是一个独立的应用程序，在启用之后会出现在你的系统托盘中。它不会改变任何系统注册表项（除了手动配置时为自己自动启动），也不会向其他进程注入任何 DLLs，因此它是一个非常便携的解决方案。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1230/3012f215b3a5cef.webp" alt="us7ogoqw.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">该程序检测你当前是按鼠标左键还是右键，并确定你将鼠标指针悬停在任务栏的哪个图标上。如果光标在同一区域停留了几毫秒--它就会模拟 Win+T 快捷方式和方向键，以恢复预定的窗口，使用的方法相当复杂。它还支持将文件投放到"显示桌面"按钮（屏幕右下方）。该程序支持多屏幕，自动启动，并有许多配置选项。</p><p style="text-align: left;">下载：<a href="https://github.com/HerMajestyDrMona/Windows11DragAndDropToTaskbarFix/releases/" _src="https://github.com/HerMajestyDrMona/Windows11DragAndDropToTaskbarFix/releases/" target="_blank">https://github.com/HerMajestyDrMona/Windows11DragAndDropToTaskbarFix/releases/</a></p>   
</div>
            