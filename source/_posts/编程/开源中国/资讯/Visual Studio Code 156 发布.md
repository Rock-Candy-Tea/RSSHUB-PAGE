
---
title: 'Visual Studio Code 1.56 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-757a60f978c8057ff220816a618c03074c5.gif'
author: 开源中国
comments: false
date: Thu, 06 May 2021 23:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-757a60f978c8057ff220816a618c03074c5.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Visual Studio Code 1.56 稳定版已发布，其中一些主要<strong>亮点内容如下：</strong></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_improved-action-hover-feedback" target="_blank">改进的</a></strong> <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_improved-action-hover-feedback" target="_blank">hover feedback</a>：</strong>帮助你快速找到可点击的编辑器操作。</li> 
</ul> 
<p><img alt height="387" src="https://oscimg.oschina.net/oscnet/up-757a60f978c8057ff220816a618c03074c5.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_terminal" target="_blank">终端配置文件的改进</a>：</strong>创建自定义默认终端配置文件。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_inline-values-by-default-for-some-languages" target="_blank">Debugger inline values</a></strong><strong>：</strong>在调试会话期间内联显示变量值。</li> 
</ul> 
<p>VS Code 的调试器 UI 支持 Inline values，可在 stepping through source code 时在编辑器中内联显示变量值。此功能基于 VS Code 核心中的通用实现，因此可能无法完美地适合所有语言，甚至有时显示不正确的值，因为通用方法无法理解底层的源语言。由于这些原因，默认情况下未启用该功能。使用新的 debugger 扩展 API，语言扩展现在可以提供正确的 inline value 支持；默认情况下，还启用了 <strong>Improved inline values</strong> 功能。</p> 
<p>为了启用此功能，<code>debug.inlineValues</code>设置有一个新的（默认）值<code>auto</code>。设置<code>auto</code>为时，将自动为那些具有“<strong>Improved inline values</strong>”支持的语言启用 inline values。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dvscjava.vscode-java-debug" target="_blank">Debugger for Java</a> 扩展，是第一批采用该 API 的 debugger 扩展之一。在下面的截图中，Java 变量的准确值就显示在它们的用法旁边：</p> 
<p><img alt height="262" src="https://oscimg.oschina.net/oscnet/up-e93ee3a8f94fb0a285aa0adf53f7f7a7912.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_math-support-in-markdown-cells" target="_blank">Notebook</a></strong> <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_math-support-in-markdown-cells" target="_blank">KaTeX 支持</a></strong>：notebook Markdown cells 中的数学支持。</li> 
</ul> 
<p><img alt height="192" src="https://oscimg.oschina.net/oscnet/up-079bf5426f0e14072b18836b7b55ea1b6a7.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_remote-development" target="_blank">Remote - Containers volumes view</a>：</strong>管理 Docker 容器中已安装的卷。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_windows-installers-consolidated-in-windows-package-manager" target="_blank">winget 安装</a></strong>：可以通过 Windows 软件包管理器获得 VS Code。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_documentation" target="_blank">新的入门视频</a></strong>：关于开始使用 VS Code 以及使用 C++ 的视频。</li> 
</ul> 
<p><img alt height="334" src="https://oscimg.oschina.net/oscnet/up-2d9b821f370ddfd21ca1c1e74490262805c.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_terminal-tabs" target="_blank">Terminal tabs</a></strong> <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56%23_terminal-tabs" target="_blank">预览</a></strong>：通过新的 tabs 视图初步了解管理 open terminals 的情况。可以通过以下设置启用：</li> 
</ul> 
<pre><code>"terminal.integrated.tabs.enabled": true</code></pre> 
<p><img alt height="209" src="https://oscimg.oschina.net/oscnet/up-808614c082031b900f6d769af91a47d38d4.png" width="500" referrerpolicy="no-referrer"></p> 
<p><strong> 更多详情可查看：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_56" target="_blank">https://code.visualstudio.com/updates/v1_56</a></p> 
<p><strong>下载：</strong>Windows: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Fwin32-x64-user%2Fstable" target="_blank">User</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Fwin32-x64%2Fstable" target="_blank">System</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Fwin32-arm64-user%2Fstable" target="_blank">ARM</a> | Mac: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Fdarwin-universal%2Fstable" target="_blank">Universal</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Fdarwin%2Fstable" target="_blank">64 bit</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Fdarwin-arm64%2Fstable" target="_blank">Arm64</a> | Linux: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Flinux-snap-x64%2Fstable" target="_blank">snap</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Flinux-deb-x64%2Fstable" target="_blank">deb</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Flinux-rpm-x64%2Fstable" target="_blank">rpm</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.56.0%2Flinux-x64%2Fstable" target="_blank">tarball</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Fsupporting%2Ffaq%23_previous-release-versions" target="_blank">ARM</a></p>
                                        </div>
                                      
</div>
            