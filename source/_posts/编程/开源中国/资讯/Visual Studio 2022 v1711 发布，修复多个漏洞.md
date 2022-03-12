
---
title: 'Visual Studio 2022 v17.1.1 发布，修复多个漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3027'
author: 开源中国
comments: false
date: Sat, 12 Mar 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3027'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio 2022 v17.1.1 正式发布，更新内容如下：</p> 
<h3>来自开发者社区</h3> 
<ul> 
 <li>修复了当在自定义命令中使用 CONFIG 时，17.1.0 版本中 CMake->vcxproj 的回归问题</li> 
 <li>修复了 VSSDK API 的故障，该问题会引发 IDE 崩溃或挂起</li> 
</ul> 
<h3>安全</h3> 
<ul> 
 <li><strong>CVE-2020-8927</strong>：NET 5.0 和 .NET Core 3.1 中存在一个远程代码执行漏洞，其中在 1.0.8 之前的 Brotli 库版本中存在缓冲区溢出。</li> 
 <li><strong>CVE-2022-24464</strong>：在分析某些类型的 http 表单请求时，.NET 6.0、.NET 5.0 和 .NET CORE 3.1 中存在拒绝服务漏洞</li> 
 <li><strong>CVE-2022-24512：</strong>.NET 6.0、.NET 5.0 和 .NET Core 3.1 中存在远程代码执行漏洞，.NET Double Parse 例程中发生堆栈缓冲区溢出。</li> 
 <li><strong>CVE-2021-3711</strong>：OpenSSL 中存在潜在的缓冲区溢出漏洞，该漏洞由 Git for Windows 导致，将 Git for Windows 更新到版本 2.35.1.2 可解决此问题。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fvisualstudio%2Freleases%2F2022%2Frelease-notes%2317.1.1" target="_blank">https://docs.microsoft.com/en-us/visualstudio/releases/2022/release-notes#17.1.1</a></p>
                                        </div>
                                      
</div>
            