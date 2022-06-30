
---
title: 'PowerShell v7.3 Preview 5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9542'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9542'
---

<div>   
<div class="content">
                                                                                            <p>PowerShell Core 是一个跨平台（Windows、Linux 和 macOS）的自动化和配置工具/框架，可以很好地与你现有的工具配合，并为处理结构化数据（如 JSON、CSV、XML 等）、REST API 和对象模型而优化。它包括一个命令行 Shell、一种相关的脚本语言和一个处理 cmdlets 的框架。</p> 
<p>PowerShell v7.3 Preview 5 发布，更新内容如下：</p> 
<h3>引擎更新和修复</h3> 
<ul> 
 <li>改进类型推理和补全（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16963" target="_blank">#16963</a>）</li> 
 <li>使<code>Out-String</code>和<code>Out-File</code>保持字符串输入不变 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17455" target="_blank">#17455</a>)</li> 
 <li>使<code>AnsiRegex</code>能够捕获 Hyperlink ANSI 序列 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17442" target="_blank">#17442</a>)</li> 
 <li>为<code>pwsh</code>增加<code>ConfigurationFile</code>命令行参数，以支持本地会话配置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17447" target="_blank">#17447</a>)</li> 
 <li>修复<code>osx-arm64</code>的本地库加载 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17365" target="_blank">#17365</a>)</li> 
 <li>当表头或列表标签的样式为空字符串时，修复格式化，使其适当地发挥作用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17463" target="_blank">#17463</a>)</li> 
</ul> 
<h3>常规 Cmdlet 更新和修复</h3> 
<ul> 
 <li>修复<code>param</code>块内的各种补全问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17489" target="_blank">#17489</a>)</li> 
 <li>改进运算符的补全 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17486" target="_blank">#17486</a>)</li> 
 <li>改进命令参数的数组元素补全 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17078" target="_blank">#17078</a>)</li> 
 <li>使用 AST 范围来补全<code>PSScriptRoot</code>路径(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17376" target="_blank">#17376</a>)</li> 
 <li>为带有类型参数的通用方法添加类型推理支持(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16951" target="_blank">#16951</a>)</li> 
 <li>只在<code>stdout</code>没有被重定向的情况下写出 OSC 指标(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17419" target="_blank">#17419</a>)</li> 
 <li>删除断言，并使用相对较大的容量，以涵盖可能增加的 .NET 参考程序集(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17423" target="_blank">#17423</a>)</li> 
 <li>增加参考程序集数量到 161 个(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17420" target="_blank">#17420</a>)</li> 
</ul> 
<h3>工具</h3> 
<ul> 
 <li>更新脚本，使之与 .NET 7 Preview 5 保持一致 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17448" target="_blank">#17448</a>)</li> 
 <li>Start-PSPester：<code>Path</code>的参数完成器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17334" target="_blank">#17334</a>)</li> 
 <li>增加提醒工作流程 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17387" target="_blank">#17387</a>)</li> 
 <li>更新文档问题模板 URL（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17410" target="_blank">#17410</a>）</li> 
 <li>更新脚本以自动获取新的 Preview 预发布版本(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F17375" target="_blank">#17375</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases" target="_blank">https://github.com/PowerShell/PowerShell/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            