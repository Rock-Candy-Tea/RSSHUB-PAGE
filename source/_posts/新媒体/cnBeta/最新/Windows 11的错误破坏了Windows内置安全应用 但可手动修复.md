
---
title: 'Windows 11的错误破坏了Windows内置安全应用 但可手动修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0823/c543d2698047047.jpg'
author: cnBeta
comments: false
date: Sun, 22 Aug 2021 23:47:00 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0823/c543d2698047047.jpg'
---

<div>   
Windows 11仍处于测试阶段，它被各种问题所困扰。<strong>根据用户报告，微软最近发布了一个有问题的更新，它似乎给Windows Security应用带来了一些严重的问题，该应用用于管理Windows Defender和其他安全功能。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0823/c543d2698047047.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0823/c543d2698047047.jpg" title alt="Windows-Security-crash.jpg" referrerpolicy="no-referrer"></a></p><p>Windows 11 Build 22000.160或更早的版本正在导致Windows Security显示错误信息，说"你需要一个新的应用程序到这个windowsdefender链接"。虽然用户仍然可以查看防病毒、防火墙和保护状态，但有些人无法再打开不同的保护功能，如账户保护、防火墙和网络保护、应用程序和浏览器控制等。</p><p>"我在Build 22000上无法打开Windows Security。试图这样做会显示一条信息，提示我在商店中寻找一个应用程序，"一位用户在反馈中心写道。</p><p>"在"保护区域"下的任何点击都会提示出现这个消息。加上"在微软商店中寻找一个应用程序"的选项，"另一位用户在反馈中心解释了这个问题。</p><p>要修复一个错误信息，说明将需要一个应用程序来打开windowsdefender链接，执行这些步骤可以缓解目前的错误：<br></p><p>用管理员权限从搜索或开始菜单打开Windows PowerShell。</p><p>复制粘贴并执行以下命令：<strong>Get-AppxPackage Microsoft.SecHealthUI -AllUsers | Reset-AppxPackage</strong>。</p><p>关闭PowerShell窗口。</p><p>一旦完成，你将能够再次启动Windows安全应用程序。</p><p><strong>Windows 11中的其他已知问题</strong></p><p>微软正在调查一个问题的报告，在Beta通道的测试者不会看到新的任务栏和开始菜单。要解决这个问题，请前往Windows更新>更新历史，并卸载最新的累积更新。补丁被移除后，你可以通过检查更新来重新安装它。</p><p>同样，Windows 11也受到以下问题的困扰：</p><p>可能无法在搜索窗口中输入文字。</p><p>当切换输入法时，任务栏会闪动。</p><p>使用搜索框时，设置应用程序会崩溃。</p><p>蓝牙LE设备将经历蓝牙可靠性问题的增加。</p><p>Windows小工具板可能无法正常工作。</p><p>这些问题将在未来几周内，在2021年10月发布之前得到修复。</p>   
</div>
            