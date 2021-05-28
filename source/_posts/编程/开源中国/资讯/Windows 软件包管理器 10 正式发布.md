
---
title: 'Windows 软件包管理器 1.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png'
author: 开源中国
comments: false
date: Fri, 28 May 2021 09:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>微软在近日举办的 Build 2021 上宣布 Windows 软件包管理器 —— Windows Package Manager 1.0 正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-package-manager-1-0%2F" target="_blank">推出</a>。Windows 软件包管理器于去年的 Build 2020 <a href="https://www.oschina.net/news/115817/microsoft-release-winget" target="_blank">宣布开源</a>并发布了预览版。</p> 
<p>Windows Package Manager 是一个综合的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fpackage-manager%2F%23understanding-package-managers" target="_blank">程序包管理器解决方案</a>，由一个命令行工具和一组用于在 Windows 10 上安装应用程序的服务组成。winget 是 Windows Package Manager 的 CLI（命令行界面），因此它也是大多数人使用 Windows Package Manager 管理软件包的主要工具。</p> 
<p>用户可以通过 winget 命令行工具发现、安装、升级、删除和配置特选应用程序集。安装后，用户可以通过 Windows Terminal、PowerShell 或 CMD 访问 winget。</p> 
<p>下图为<code>winget</code>通过 PowerShell 在 Windows Terminal 中运行的截图。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fpackage-manager%2F" target="_blank">点此查阅详细使用文档</a>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png" referrerpolicy="no-referrer"></p> 
<p><strong>获取方式</strong></p> 
<p style="text-align:left">Windows Package Manager <span style="color:#333333"><span style="background-color:#ffffff">随 Microsoft Store 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fp%2Fapp-installer%2F9nblggh4nns1" target="_blank">App Installer</a> 一起分发。此外还可以从 GitHub <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fwinget-cli%2Freleases%2F" target="_blank">release 页面</a>下载并安装 </span></span>Windows Package Manager，<span style="color:#333333"><span style="background-color:#ffffff">也可以<a href="ms-appinstaller:?source=https://aka.ms/getwinget">直接安装</a>最新的可用版本。</span></span></p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-83bcfe79d91e3cfc6d44e93d11e464393a3.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">据介绍，目前微软已提供超过 1400 个可供用户使用的软件包。</p> 
<p style="text-align:left">除此之外，微软还发布了另一个开源工具，以帮助用户将软件包提交到社区仓库，此工具为 Windows Package Manager Manifest Creator (aka wingetcreate)。用户在命令行界面执行<code>winget install wingetcreate</code>即可完成安装。使用方式见下图。</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-0dc5433c25e5da906fe3df55324fe8a917b.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            