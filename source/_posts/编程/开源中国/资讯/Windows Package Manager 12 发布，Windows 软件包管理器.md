
---
title: 'Windows Package Manager 1.2 发布，Windows 软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0cd6a28a3c898c222252b6a989a2d41d0ed.png'
author: 开源中国
comments: false
date: Tue, 08 Mar 2022 07:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0cd6a28a3c898c222252b6a989a2d41d0ed.png'
---

<div>   
<div class="content">
                                                                                            <p>Windows 软件包管理器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-package-manager-1-2%2F" target="_blank">发布</a>了 1.2 版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0cd6a28a3c898c222252b6a989a2d41d0ed.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Windows Package Manager 是一个综合的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fpackage-manager%2F%23understanding-package-managers" target="_blank">程序包管理器解决方案</a>，由一个命令行工具和一组用于在 Windows 10 上安装应用程序的服务组成。winget 是 Windows Package Manager 的 CLI（命令行界面），因此它也是大多数人使用 Windows Package Manager 管理软件包的主要工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用户可以通过 winget 命令行工具发现、安装、升级、删除和配置特选应用程序集。安装后，用户可以通过 Windows Terminal、PowerShell 或 CMD 访问 winget。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图为<code>winget</code>通过 PowerShell 在 Windows Terminal 中运行的截图。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fpackage-manager%2F" target="_blank">点此查阅详细使用文档</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png" referrerpolicy="no-referrer"></p> 
<p><strong>新特性</strong></p> 
<p><strong>支持 ARM64</strong></p> 
<p>在新版本中，Windows 软件包管理器会根据硬件架构自动匹配最合适的可用软件包，这是专门面向 ARM64 设备（例如 Surface Pro X, Lenovo X13s 和 Samsung Galaxy Book Go 等）的优化。下方视频是关于此特性的演示：</p> 
<div class="ckeditor-html5-video" style="text-align:center"> 
 <video controls="controls" controlslist="nodownload" src="https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2022/03/WinGetARM64.mp4">
   
 </video> 
</div> 
<p><strong>优化错误处理 (Error Handling)</strong></p> 
<p>新版本支持将“神秘”的错误消息映射成更易于理解的内容。开发团队表示，对于常见的返回 10 位数错误代码，它们往往只是针对单个软件包的提示，代表了常见的错误类型，如存储和内存不足。现在，manifests 支持在安装程序的<strong>自定义错误代码</strong>和 Windows 软件包管理器的<strong>通用代码</strong>之间建立映射。</p> 
<p><strong>针对 local manifests 的新设置项</strong></p> 
<p>新版本为从本地清单文件 (local manifest file) 进行测试或安装相关的 security conscious 添加了新设置。这是要求用户在将软件包提交到 Windows 包管理器社区应用程序存储库之前执行的操作。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-db13df2a95382ee4ab4085130b740b4f32d.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>获取方式</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Windows Package Manager <span style="color:#333333"><span style="background-color:#ffffff">随 Microsoft Store 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fp%2Fapp-installer%2F9nblggh4nns1" target="_blank">App Installer</a> 一起分发。此外还可以从 GitHub <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fwinget-cli%2Freleases%2F" target="_blank">release 页面</a>下载并安装<span> </span></span></span>Windows Package Manager，<span style="color:#333333"><span style="background-color:#ffffff">也可以<a href="ms-appinstaller:?source=https://aka.ms/getwinget" target="_blank">直接安装</a>最新的可用版本。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-83bcfe79d91e3cfc6d44e93d11e464393a3.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-package-manager-1-2%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            