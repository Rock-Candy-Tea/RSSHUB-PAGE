
---
title: 'Windows Package Manager 1.3 发布，Windows 软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 07:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Windows 软件包管理器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-package-manager-1-3%2F" target="_blank">发布</a>了 1.3 版本。Windows Package Manager 是一个综合的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fpackage-manager%2F%23understanding-package-managers" target="_blank">程序包管理器解决方案</a>，由一个命令行工具和一组用于在 Windows 10 上安装应用程序的服务组成。winget 是 Windows Package Manager 的 CLI（命令行界面），因此它也是大多数人使用 Windows Package Manager 管理软件包的主要工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用户可以通过 winget 命令行工具发现、安装、升级、删除和配置特选应用程序集。安装后，用户可以通过 Windows Terminal、PowerShell 或 CMD 访问 winget。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图为<span> </span><code>winget</code><span> </span>通过 PowerShell 在 Windows Terminal 中运行的截图。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fwindows%2Fpackage-manager%2F" target="_blank">点此查阅详细使用文档</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="269" src="https://oscimg.oschina.net/oscnet/up-7232e71d56cb6a4acb94c608c5bc4a3f571.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本带来了更好的包版本报告、新设置允许默认情况下启用详细日志、运行 winget -–info 显示系统架构、改进了进度条的样式等功能。此外，Windows 包管理器现在支持便携式应用程序。</p> 
<h2>更好的包版本报告</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一些软件包可能附带与包版本相关的文档。 现在运行 winget show <package> 能够看到文档和关联的 URL。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="342" src="https://oscimg.oschina.net/oscnet/up-5967c96e8e169c8ca38e7be67cad694a4f5.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">其次，安装软件包后会显示安装说明。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="341" src="https://oscimg.oschina.net/oscnet/up-ff54cff6621458f44aeef5a4f34cb65ad3c.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">其次，Windows 包管理器支持发布者选择显示的首选版本，并且该工具在有新版本可用时能够进行比较。</p> 
<h2>显示系统架构</h2> 
<p>新命令 winget –info 可以显示系统架构，以便快速查看硬件的架构。</p> 
<p><img alt height="342" src="https://oscimg.oschina.net/oscnet/up-65cd353dd05eee8ff008dd4e3f698ffe05c.png" width="600" referrerpolicy="no-referrer"></p> 
<h2>更细致的进度条</h2> 
<p>新版本新增了可自定义的进度条，额外的细粒度块使进度条变得光滑，可以在设置中自定义进度条。</p> 
<pre><code>“visual”: &#123;“progressBar”: “rainbow”&#125;</code></pre> 
<h2>支持便携包</h2> 
<p>可以使用 Windows 包管理器管理可移植包，将它们视为已安装的应用程序。</p> 
<p><img alt height="386" src="https://oscimg.oschina.net/oscnet/up-7c731120dbdcb3cf7e006dbc40a58f43aed.png" width="600" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>更详细的版本介绍可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-package-manager-1-3%2F" target="_blank">微软博客</a>中查阅。</p>
                                        </div>
                                      
</div>
            