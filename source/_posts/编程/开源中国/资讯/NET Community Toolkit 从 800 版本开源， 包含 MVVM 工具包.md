
---
title: '.NET Community Toolkit 从 8.0.0 版本开源， 包含 MVVM 工具包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c4c667928cd9c918d21f896c5af8ed0f72c.png'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 07:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c4c667928cd9c918d21f896c5af8ed0f72c.png'
---

<div>   
<div class="content">
                                                                                            <p>.NET 社区工具包（.NET Community Toolkit ）现已以 8.0.0 版发布！</p> 
<blockquote> 
 <p>.NET 社区工具包是一组适用于所有 .NET 开发人员，且与任何特定 UI 平台无关的帮助程序和 API。该工具包由 Microsoft 维护和发布，是 .NET 基金会的一部分，它还被多个微软内部项目和应用程序使用，例如 Microsoft Store。</p> 
 <p>.NET 社区工具包的所有库最初都是 Windows 社区工具包的一部分，但随着时间的推移，仅针对 .NET 且不特定于 Windows 依赖项的 API 数量不断增加，微软决定将 .NET 相关内容拆分到一个单独的项目中，以便它们可以独立发展，.NET Community Toolkit 由此诞生。</p> 
 <p>由于分支之前的 Windows 社区工具包的最后一个版本是 7.1.x，因此，拆分出来的 .NET 社区工具包从 8.0.0 版本号开始。</p> 
</blockquote> 
<p>.NET 社区工具包现在位于 GitHub 上的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCommunityToolkit%2Fdotnet" target="_blank">CommunityToolkit/dotnet</a> 存储库中，<span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>包括以下内容：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><code><span>CommunityToolkit</span><span>.</span><span>Common</span></code></li> 
 <li><code><span>CommunityToolkit</span><span>.</span><span>Mvvm</span></code>（又名“微软 MVVM 工具包”）</li> 
 <li><code><span>CommunityToolkit</span><span>.</span><span>Diagnostics</span></code></li> 
 <li><code><span>CommunityToolkit</span><span>.</span><span>HighPerformance</span></code></li> 
</ul> 
<p><img alt height="394" src="https://oscimg.oschina.net/oscnet/up-c4c667928cd9c918d21f896c5af8ed0f72c.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>MVVM Toolkit</h2> 
<p>.NET 社区工具包的主要组件之一是 MVVM 工具包：一个现代、快速、平台无关的模块化 MVVM 库，也是 Microsoft Store、照片等应用使用的 MVVM 库。</p> 
<p>MVVM Toolkit 受到 MvvmLight 的启发，由于 MvvmLight 已被弃置，它也是 MvvmLight 的官方替代品。</p> 
<h2>MVVM Toolkit source generators</h2> 
<p><span style="background-color:#ffffff; color:#333333">MVVM Toolkit 8.0.0 版本中最大的新特性是新的 MVVM 源码生成器，它可以大大​​减少使用 MVVM 设置应用程序所需的样板代码。</span></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>它的运行速度将比以前快得多，并且即使在处理大型项目时也有助于保持 IDE 的快速响应。可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fcommunitytoolkit%2Fmvvm%2Fgenerators%2Foverview" target="_blank">此处</a>找到关于新的 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>source generators <span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>的所有文档。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>.NET 6 支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这个新版本的 .NET Community Toolkit 还增加了对 .NET 6 的支持。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>该版本还包含大量 MVVM 工具包和其他 API 的介绍，详细信息可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-the-dotnet-community-toolkit-800%2F" target="_blank">微软博客</a>中阅读。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            