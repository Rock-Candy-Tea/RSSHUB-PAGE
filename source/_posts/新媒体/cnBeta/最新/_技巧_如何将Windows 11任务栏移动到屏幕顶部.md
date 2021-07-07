
---
title: '_技巧_如何将Windows 11任务栏移动到屏幕顶部'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0707/d12a1e7c8c50fdc.jpg'
author: cnBeta
comments: false
date: Wed, 07 Jul 2021 05:40:41 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0707/d12a1e7c8c50fdc.jpg'
---

<div>   
当微软推出 Windows 11 操作系统的时候，争论的焦点之一，就是任务栏图标被强制居中、并且固定在了底部。<strong>如果想要像旧版 Windows 操作系统那样，将 Windows 11 任务栏调整到两侧或顶部，显然已经无法轻松实现。</strong>然而从 MajorGeeks 分享的一段视频来看，我们还是可以试着将 Windows 11 的任务栏，切换到屏幕的顶部的。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0707/d12a1e7c8c50fdc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0707/d12a1e7c8c50fdc.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>MSPU 指出，此举需要修改 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 操作系统的注册表。方法如下：</p><blockquote><p>（1）打开 Regedit；</p><p>（2）导航至 Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer \StuckRects3；</p><p>（3）设置 Settings 值。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/0707/ef6e7e6cd8d8f18.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0707/ef6e7e6cd8d8f18.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>（4）如图所示，你需要将该路径下的注册表项的数值改为“01”。</p><p>（5）通过 任务管理器 重启 Windows 资源管理器（Explorer）进程。</p><p><a href="https://static.cnbetacdn.com/article/2021/0707/8dd87101fa18ab7.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0707/8dd87101fa18ab7.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">最终效果如上图所示</p><p>遗憾的是，Windows 11 操作系统本身仍未做好应对这种变化的准备。比如通知中心（Action Center）等功能，仍会在屏幕底部弹出来。</p><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=270157364&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">How to Move the Windows 11 Taskbar to the Top Of Your Screen（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjcwMTU3MzY0LnNodG1s.html" target="_self">via</a>）</p><p>感兴趣的朋友，可查看 MajorGeek 在 YouTube 上分享的这段演示视频。</p>   
</div>
            