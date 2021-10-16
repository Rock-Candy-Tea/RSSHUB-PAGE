
---
title: 'Explorer Patcher_让Windows 11恢复Windows 10的行为特征'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1016/ff086e04076dd81.jpg'
author: cnBeta
comments: false
date: Fri, 15 Oct 2021 23:37:04 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1016/ff086e04076dd81.jpg'
---

<div>   
在升级 Windows 11 系统之后，如果你想要让任务栏和文件管理器恢复成 Windows 10 的行为特征，<strong>那么借助 Explorer
Patcher 这款应用是非常简单的方法。</strong>用户只需要将一个.DLL 文件添加到 C:\Windows，微软就会下载其余的文件，使之成为可能。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1016/ff086e04076dd81.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1016/ff086e04076dd81.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1016/ea825b375bc2f47.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1016/ea825b375bc2f47.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">开发者表示该项目的目的是在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 上带回一个富有成效的工作环境。或者更确切地说，恢复 Windows 10 中已经没有破损的东西。</p><p style="text-align: left;">这个软件的功能包括：</p><blockquote style="text-align: left;"><p style="text-align: left;"><strong>来自 Windows 10 系统的任务栏</strong></p><p style="text-align: left;">● 主任务栏和副任务栏的“总是合并”、“满时合并”、“从不合并”选项</p><p style="text-align: left;">● 搜索按钮</p><p style="text-align: left;">● 任务视图按钮</p><p style="text-align: left;">● 可选的皮肤、居中和切换的弹出式菜单，或无皮肤（对经典主题用户有用）</p><p style="text-align: left;">● 当点击系统托盘网络图标的弹出式菜单中的"打开网络和互联网设置"时，打开"网络和共享中心"</p><p style="text-align: left;">● 隐藏控制中心按钮</p><p style="text-align: left;">● 在任务栏上显示人脉（People）</p><p style="text-align: left;">● 显示触摸键盘按钮</p><p style="text-align: left;"><strong>文件资源管理器</strong></p><p style="text-align: left;">● 禁用 Windows 11 的命令栏</p><p style="text-align: left;">● 禁用 Windows 11 的右键菜单</p><p style="text-align: left;">● 甚至禁用Windows 10（沉浸式）右键菜单（对经典主题用户很有用）</p><p style="text-align: left;">● 禁用现代搜索栏（恢复到早期Windows 10构建或Windows 7/8的搜索栏）。</p><p style="text-align: left;">● 完全禁用搜索栏</p><p style="text-align: left;"><strong>来自 Windows 11 的开始菜单</strong></p><p style="text-align: left;">● 在包含光标的显示器上打开“开始”</p><p style="text-align: left;">● 在登录时打开“开始”菜单</p><p style="text-align: left;">● 默认在“所有应用程序”中打开“开始”。</p><p style="text-align: left;">● 在屏幕上的定位</p><p style="text-align: left;">● 显示的频繁应用程序的最大数量</p><p style="text-align: left;"><strong>来自 Windows 10 的窗口切换</strong></p><p style="text-align: left;">● 选择是否在窗口列表中包括桌面</p><p style="text-align: left;">● 能够设置窗口列表的不透明度</p><p style="text-align: left;">● 设置行的大小，最大的延伸等</p><p style="text-align: left;"><strong>其他功能：</strong></p><p style="text-align: left;">● 当按下Win+C（而不是Microsoft Teams）时，弹出时间和日期。</p><p style="text-align: left;">● 为桌面上的Alt+F4设置默认关机动作</p><p style="text-align: left;">● 在Win+X菜单中显示命令提示符而不是PowerShell</p></blockquote><p style="text-align: left;"><strong>安装</strong></p><p style="text-align: left;">在“<a href="https://github.com/valinet/ExplorerPatcher/releases" target="_blank">Release</a>”部分下载最新版本的 Explorer Patcher 补丁，你会发现一个名为 dxgi.dll 的 DLL 下载。它已经在外媒最新的 Windows 11 稳定版（22000.258）上进行了测试，但开发者声称它在较新的版本上应该也能正常工作。这是应用程序的运行时部分。你需要把这个DLL放在以下位置:C:\Windows，这也意味着你将需要管理员权限。</p><p style="text-align: left;">完成上述工作后，确保你有一个活跃的互联网连接，并使用任务管理器或通过发出以下命令重新启动资源管理器进程。</p><blockquote style="text-align: left;"><p style="text-align: left;">taskkill /f /im explorer.exe</p></blockquote><p style="text-align: left;">一旦文件浏览器重新启动，一些必要的文件（符号文件）将从<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>下载（大约50MB）。这应该是比较快的，取决于你的互联网连接速度。完成后，文件浏览器将再次重启，并准备好使用。</p>   
</div>
            