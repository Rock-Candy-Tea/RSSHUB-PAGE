
---
title: '.NET 6 Preview 5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7715'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 08:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7715'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6-preview-5%2F" target="_blank">.NET 6 Preview 5 已发布</a>，此版本已包含 .NET 6 的大部分新功能，更新内容主要是优化性能和其他改进。</p> 
<h2 style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">.NET SDK：可选的 Workflow 改进</span></span></h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fdesigns%2Fblob%2Fmain%2Faccepted%2F2020%2Fworkloads%2Fworkloads.md" target="_blank">SDK workloads</a> 是一项新的 .NET SDK 特性，可帮助开发者在不增加 SDK 大小的情况下添加对新应用程序类型（如<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-maui-preview-4%2F" target="_blank">移动应用</a>和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Faspnet%2Fasp-net-core-updates-in-net-6-preview-4%2F%23blazor-webassembly-ahead-of-time-aot-compilation" target="_blank">WebAssembly</a>）的支持。</p> 
<p>此功能已更新到支持<code>list</code>和<code>update</code> ：</p> 
<ul> 
 <li><code>dotnet workload list</code>命令会提示已安装的 workload</li> 
 <li><code>dotnet workload update</code>命令会将所有已安装的 workload 升级到最新的可用版本</li> 
</ul> 
<h2>.NET SDK：验证 NuGet 包</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F5700" target="_blank">包验证工具</a>将使 NuGet 库开发者能够验证他们的包是否一致且格式良好</p> 
<p style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">这包括：</span></span></p> 
<ul> 
 <li>验证跨版本是否重大更改</li> 
 <li>验证包对于所有特定于 runtime 的实现是否具有相同的公共 API 集</li> 
 <li>确定目标框架或 runtime 适用性的差距</li> 
</ul> 
<p style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">此工具可通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FMicrosoft.DotNet.PackageValidation" target="_blank">Microsoft.DotNet.PackageValidation </a>获得。</span></span></p> 
<h2 style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">函数库：放弃对旧框架的支持</span></span></h2> 
<p style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">从 .NET 6 Preview 5 开始，官方将放弃</span></span>比以下这些更旧的任何框架的支持：</p> 
<ul> 
 <li>.NET Framework 4.6.1</li> 
 <li>.NET Core 3.1</li> 
 <li>.NET Standard 2.0</li> 
</ul> 
<p style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">如果开发者当前正在引用来自早期框架的受影响的软件包，那么无法再将引用的包更新到更高版本。因此开发者只能将项目</span></span><span style="color:#333333"><span style="background-color:#ffffff">重新定位到更高的框架版本，或者不更新引用的包。</span></span></p> 
<p style="text-align:left"><span style="color:#333333">这是一个破坏性变更，不过官方认为如果继续保留旧框架，会</span><span style="color:#333333"><span style="background-color:#ffffff">为他们发布的所有框架构建增加包的复杂性和大小。</span></span></p> 
<p style="text-align:left"><span style="color:#333333"><span style="background-color:#ffffff">更多详细信息，包括受影响软件包的完整列表，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fannouncements%2Fissues%2F190" target="_blank">访问此链接</a>。</span></span></p> 
<p style="text-align:left">完整更新说明查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6-preview-5%2F" target="_blank"> 发布公告</a>。</p>
                                        </div>
                                      
</div>
            