
---
title: 'PowerToys 0.58 发布，完全使用 .NET 6、支持 ARM64'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8630'
author: 开源中国
comments: false
date: Fri, 06 May 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8630'
---

<div>   
<div class="content">
                                                                                            <p>Microsoft PowerToys 是 Windows 系统实用程序，供高级用户调整和简化其 Windows 体验，可最大限度地提高生产力。</p> 
<p>该版本主要集中在升级到新的依赖以及为原生 ARM64 构建，以下是该版本的一些重点更新内容：</p> 
<h3>亮点</h3> 
<ul> 
 <li>大部分用于原生在 ARM64 上运行的工作都已包含在该版本中</li> 
 <li>使用过时的 WebBrowser 控件被替换成 WebView 2</li> 
 <li>所有对 .NET Core 3.1 的使用都被删除，PowerToys 现在运行在 .NET 6 上</li> 
 <li>设置不再运行于 XAML Islands，现在运行于 WinUI 3，修复了许多与 XAML Islands 有关的错误</li> 
</ul> 
<h3>常规</h3> 
<ul> 
 <li>修复代码中的拼写检查</li> 
 <li>修复了因 GitHub API 变化而导致的与拼写检查有关的 CI 错误</li> 
 <li>修正了文档中对 GitHub 的引用</li> 
</ul> 
<h3>ARM64</h3> 
<ul> 
 <li>为 ARM64 移植准备了解决方案和属性文件</li> 
 <li>将未处理的异常处理程序移植到 ARM64</li> 
 <li>将 Setting 项目移植到 ARM64</li> 
 <li>将大部分的 PowerToys 移植到 ARM64</li> 
 <li>将调试工具移植到 ARM64</li> 
</ul> 
<h3>Always on Top</h3> 
<ul> 
 <li>修复了某些应用程序的窗口最顶端状态的重置问题</li> 
</ul> 
<h3>ColorPicker</h3> 
<ul> 
 <li>CIEXYZ 格式现在可以正确显示为大写</li> 
</ul> 
<h3>安装程序</h3> 
<ul> 
 <li>在 .exe 安装程序引导程序中分发一个已签名的 .msi</li> 
 <li>删除了安装程序中的 .NET Core 依赖</li> 
 <li>部分支持 ARM64 安装程序</li> 
 <li>将 .NET 更新至 6.0.4。</li> 
 <li>在重新安装/更新时强制更新所有文件，以尝试修复安装问题</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FPowerToys%2Freleases%2Ftag%2Fv0.58.0" target="_blank">https://github.com/microsoft/PowerToys/releases/tag/v0.58.0</a></p>
                                        </div>
                                      
</div>
            