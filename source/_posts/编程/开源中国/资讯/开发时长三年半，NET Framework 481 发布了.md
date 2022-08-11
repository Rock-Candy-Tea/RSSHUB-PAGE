
---
title: '开发时长三年半，.NET Framework 4.8.1 发布了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8047'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8047'
---

<div>   
<div class="content">
                                                                                            <p>.NET 开发平台.NET Framework 最新的 4.8.1 版本随着 Visual Studio 2022 17.3 版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fdotnet%2Fblob%2Fmaster%2Freleases%2Fnet481%2FREADME.md" target="_blank">发布</a>了。它的上一个版本还是 2019 年 4 月的 <a href="https://www.oschina.net/news/106116/dot-net-framework-4-8-released" target="_blank">.NET Framework 4.8</a> ，开发时长约三年半的 .NET Framework 带来了一些新东西：</p> 
<h3><strong>原生 Arm64 支持</strong></h3> 
<p>.NET Framework 4.8.1 新增原生 Arm64 支持，利用在 Arm64 上本机运行工作负载的优势，比在 Arm64 上运行模拟 x64 代码拥有更好的性能。</p> 
<h3><strong>可访问的工具提示</strong></h3> 
<p>.NET Framework 的工具提示符合 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG21%2FUnderstanding%2Fcontent-on-hover-or-focus.html" target="_blank">WCAG2.1 </a>（Web 内容无障碍指南）中“关于悬停或焦点指引”的规定。新增如下规定：</p> 
<ul> 
 <li>工具提示必须通过<strong>鼠标悬停</strong>或<strong>键盘快捷键</strong>导航到控件才能显示。</li> 
 <li>工具提示应该是可<strong>忽略</strong>的。也就是说，像 ESC 键这样的简单命令应该关闭工具提示。</li> 
 <li>工具提示应该是可<strong>悬停的</strong>。用户应该能够将鼠标光标放在工具提示上。这使得使用放大镜等场景能够为低视力用户阅读工具提示。</li> 
 <li>工具提示应该是<strong>持久</strong>的。一定时间过后，工具提示不应自动消失。相反，用户将鼠标移动到另一个控件或者手动关闭提示时，才能关闭上一个工具提示。</li> 
</ul> 
<h3><strong>Windows Forms</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fwindows%2Fwin32%2Fwinauto%2Fuiauto-implementingtextandtextrange" target="_blank">文本模式支持</a> —— 新版本的 WinForms 添加了对 UIA 文本模式的支持。此模式使辅助技术（放大镜、机器朗读等）能够逐字母遍历 TextBox 这种基于文本控制的内容。总体来说，添加了对 TextBox、DataGridView 单元格、ComboBox 控件等的支持。</li> 
 <li>解决对比度问题 —— 解决了几个控件中的高对比度问题，并将选择矩形的对比度改得更暗、更明显。</li> 
 <li>修复了几个 DataGridView 问题 —— 更新了滚动条名称以保持一致。解决了机器朗读无法处理空 DataGridView 单元格的问题。另外，现在可以为自定义 DataGridView 单元格设置本地化控件类型属性。DataGridViewLink 单元格的链接颜色已更新，与背景形成更好的对比。</li> 
</ul> 
<p> </p> 
<p>上面是主要功能更新，其他内容则是一些杂项和修复。总的来说，这个版本有点东西，但并不多。</p> 
<p>在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-framework-481%2F" target="_blank">微软博客</a>中可以阅读更详细的版本解读，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fzh-cn%2Fdownload%2Fdotnet-framework" target="_blank">点此</a>下载最新版本。</p>
                                        </div>
                                      
</div>
            