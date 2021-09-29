
---
title: 'Rider 2021.3 EAP 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-09d6a25cb4961f017296fd54629d3b249e7.png'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-09d6a25cb4961f017296fd54629d3b249e7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Rider 2021.3 EAP 现已发布，以下是其更新亮点。</p> 
<p><img alt height="800" src="https://oscimg.oschina.net/oscnet/up-09d6a25cb4961f017296fd54629d3b249e7.png" width="1600" referrerpolicy="no-referrer"></p> 
<h4>问题视图</h4> 
<p>问题视图（Rider UI 中的 "问题" 选项卡）是一个工具窗口，它汇总了解决方案中存在的所有潜在问题，例如项目加载错误、失败的 NuGet 还原过程、来自打开文件的检查以及所有 SWEA 错误。</p> 
<p><img alt height="700" src="https://oscimg.oschina.net/oscnet/up-7b6baae84ca8ebf93f57b9de55ac312354b.png" width="1600" referrerpolicy="no-referrer"></p> 
<h4>.NET 6 SDK 支持</h4> 
<p>从这个 EAP 开始，Rider 正式提供了对 .NET 6 SDK 的初步支持，包括项目模板、目标框架以及针对新 SDK 的创建/运行/调试项目，不过，目前尚不支持 .NET 6 的热重载功能和 Blazor 调试。</p> 
<h4>调试选项卡的新 UI</h4> 
<p>"调试" 选项卡现在具有新的 UI。默认情况下，有三个选项卡：线程和变量、控制台和调试输出。其他选项卡如内存和并行堆栈是隐藏的，但用户可以通过选项菜单（螺母图标）显示它们。</p> 
<p><img alt height="450" src="https://oscimg.oschina.net/oscnet/up-515b79264683aae1b89960db57516e26ea8.png" width="1600" referrerpolicy="no-referrer"></p> 
<p>该版本完全删除了左侧工具栏，并将图标移至顶部工具栏或上下文菜单。并在 "更多" 下拉菜单中添加了一个新的设置子菜单，包括调试器相关的最常见设置的候选列表，而无需转到设置/首选项对话框。</p> 
<p><img alt height="742" src="https://oscimg.oschina.net/oscnet/up-ded517bd03785f35f9839881d6e78c1dc69.png" width="1600" referrerpolicy="no-referrer"></p> 
<h4>调试器更新</h4> 
<p>UWP 开发者现在可以立即在调试器下启动 UWP 项目，而不再需要先运行项目，然后手动将调试器附加到正在运行的进程。此外，现在可以在本地 Windows Docker 容器中调试 .NET (Core) 和 .NET Framework 应用程序。</p> 
<h4>语言支持</h4> 
<p>C# 10 即将发布，该版本添加了其对文件范围命名空间和全局使用的支持。此外，还添加了一个新的语法样式选项。当用户选择样式时，Rider 将同时显示必须更改以遵循样式的代码检查，并提供适当的快速修复。开发者可以一键修复项目甚至整个解决方案。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4728c33c5804705a42142c59511ba00700d.gif" referrerpolicy="no-referrer"></p> 
<h4>代码分析</h4> 
<p>由于可空引用类型在 C# 中可用，一些代码示例已经包含 NRT 语法。为了帮助用户在将此类代码粘贴到项目后摆脱这种语法，Rider 提供了两个新的快速修复：替换为 JetBrains.Annotations 属性和删除没有 "#nullable" 上下文的可空注释。</p> 
<p><img alt height="400" src="https://oscimg.oschina.net/oscnet/up-0ed3ff0d2e42eceddec1f586c5b22fb7671.png" width="1600" referrerpolicy="no-referrer"></p> 
<h4>更好地支持 SQL 注入</h4> 
<p>该版本改进了对 SQL 注入的支持，包括正确解析 string.Format 方法、字符串插值和简单字符串连接的 SQL 查询字符串，以及使用 Microsoft SQL Server 方言或 Dapper 库时，SQL 查询字符串中参数的 SQLParameter 变量不再出现错误。</p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fdotnet%2F2021%2F09%2F28%2Frider-2021-3-eap%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            