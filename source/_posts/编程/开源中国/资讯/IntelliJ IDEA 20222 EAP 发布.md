
---
title: 'IntelliJ IDEA 2022.2 EAP 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9a7f91d33bb211171f391fdb806ada89c2e.png'
author: 开源中国
comments: false
date: Mon, 23 May 2022 23:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9a7f91d33bb211171f391fdb806ada89c2e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>IntelliJ IDEA 2022.2 首个 EAP 版本现已发布，带来了许多有用的改进；同时将 IDE 迁移至 JBR 17，以提高 IDE 性能。开发者可以从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fidea%2Fnextversion%2F" target="_blank">网站</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Ftoolbox-app%2F" target="_blank">Toolbox 应用程序</a>，或通过使用 Ubuntu 的 snaps 下载最新版本。</p> 
<p><img alt height="234" src="https://oscimg.oschina.net/oscnet/up-9a7f91d33bb211171f391fdb806ada89c2e.png" width="500" referrerpolicy="no-referrer"></p> 
<p>具体更新内容如下：</p> 
<h4><strong>用户界面</strong></h4> 
<p><strong>在 MacOS 上合并所有项目的 Windows action</strong></p> 
<p>针对 macOS 用户引入了将所有打开的项目窗口合并为一个的功能，将它们变成 tab。此操作可从“Window”菜单中获得。</p> 
<p><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-2cf4d080c660cbc8290da255c39f5b24878.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>Mnemonic Bookmarks 的新描述字段</strong></p> 
<p>在"Add Mnemonic Bookmark"对话框中集成了一个描述字段，这样你就可以立即为你的书签添加一个可选的描述。</p> 
<p><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-5095730927ea5ac6f86ef9e0cda5821e4b0.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>缩放时的字体大小指示器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>当你在编辑器中放大或缩小代码时，现在可以看到一个显示当前字体大小的指示器以及将其恢复为默认值的选项。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-d9ca754d1f2364651d80d0695aeb347da58.gif" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4><strong><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>VCS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Welcome screen 上的 Cloning repository 进度条</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start">更新了 Cloning repository 进度在 IDE 的 Welcome screen 上的显示方式。现在，进度条直接显示在 Projects 列表中，使其更加清晰和易于使用。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-5a0176717101ad7ab745d4d788399e81a4d.png" width="500" referrerpolicy="no-referrer"></p> 
<h4><strong><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Editor</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>New setting to disable automatic block comment closure</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>现在可以在按下 Enter 键时禁用 automatic block comment closure。可通过，Settings / Preferences | Editor | Smart Keys，取消勾选"Enter"部分的"Close block comment"复选框。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-42adabfc13981d81784e79c692101bb9d00.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#000000"><strong><span style="background-color:#ffffff">Code Completion Popup 中提供的 Code Completion Settings</span></strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">现在可以直接从 Code Completion Popup 中的三个垂直点菜单按钮访问<em> </em>Code Completion Settings 并配置你的 preferences。</span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-288b929391aad354b03cfde4c3306739d0d.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4><span style="color:#000000"><strong>JetBrains Runtime</strong></span></h4> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">随着 IntelliJ IDEA 2022.2 EAP 的推出，开发团队正在从 JetBrains Runtime 11 (JBR11) 迁移到 JetBrains Runtime 17 (JBR17)。从此构建开始，所有 IntelliJ IDEA 2022.2 更新都将随附 JBR17。带来的影响包括：</span></span></p> 
<ul> 
 <li><span style="color:#000000">显着的性能改进，使 IDE 运行更快、更顺畅。</span></li> 
 <li><span style="color:#000000">更好的安全性，因为 JBR17 基于最新的 OpenJDK LTS。</span></li> 
 <li><span style="color:#000000">JetBrains Runtime 17 利用 Metal API 在 macOS 上提供更好的渲染性能。</span></li> 
 <li><span style="color:#000000">提高 macOS 上的可访问性，因为 JBR17 具有与</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.apple.com%2Fen-gb%2Fguide%2Fvoiceover-guide%2Fwelcome%2Fweb" target="_blank">VoiceOver screen reader</a> <span style="color:#000000">的集成。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F417" target="_blank">Vector API</a><span style="color:#000000"> 的使用旨在表达在运行时编译为支持的 CPU 架构上的<span style="background-color:#ffffff">向量指令的向量计算</span>，从而实现优于等效标量计算的性能。</span></li> 
</ul> 
<p><span style="color:#000000">详情可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F05%2Fintellij-idea-2022-2-eap-1%2F" target="_blank">查看官方公告</a><span style="color:#000000">。 </span></p>
                                        </div>
                                      
</div>
            