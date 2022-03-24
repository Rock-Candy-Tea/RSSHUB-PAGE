
---
title: 'PowerShell v7.3 Preview 3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1287'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1287'
---

<div>   
<div class="content">
                                                                                            <p>PowerShell Core 是一个跨平台（Windows、Linux 和 macOS）的自动化和配置工具/框架，可以很好地与你现有的工具配合，并为处理结构化数据（如 JSON、CSV、XML 等）、REST API 和对象模型而优化。它包括一个命令行 Shell、一种相关的脚本语言和一个处理 cmdlets 的框架。</p> 
<p>PowerShell v7.3 Preview 3 发布，更新内容如下：</p> 
<h3>引擎更新和修复</h3> 
<ul> 
 <li>修复了 .NET 方法泛型参数的解析代码 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16937" target="_blank">#16937</a>)</li> 
 <li>允许 <code>PSGetMemberBinder</code> 获取 <code>ByRef</code> 属性的值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16956" target="_blank">#16956</a>)</li> 
 <li>允许包含 <code>Automation.Null</code> 元素的集合被输送到管道 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16957" target="_blank">#16957</a>)</li> 
</ul> 
<h3>常规 Cmdlet 的更新和修复</h3> 
<ul> 
 <li>将 <code>CompatPowerShellGet</code> 模块添加到遥测模块的允许列表中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16935" target="_blank">#16935</a>)</li> 
 <li>通过处理已经退出的进程，修复 <code>Enter-PSHostProcess</code> 和 <code>Get-PSHostProcessInfo</code> cmdlets (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16946" target="_blank">#16946</a>)</li> 
 <li>改进多种情况下的 Hashtable 补全 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16498" target="_blank">#16498</a>)</li> 
</ul> 
<h3>代码清理</h3> 
<ul> 
 <li>修复 <code>CommandHelpProvider.cs</code> 中的一个拼写错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16949" target="_blank">#16949</a>)</li> 
</ul> 
<h3>测试</h3> 
<ul> 
 <li>更新一些测试，使其在 CI 中更加稳定 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16944" target="_blank">#16944</a>)</li> 
 <li>将测试中使用的 Windows 镜像回滚至 Windows Server 2019 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Fpull%2F16958" target="_blank">#16958</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases" target="_blank">https://github.com/PowerShell/PowerShell/releases</a></p>
                                        </div>
                                      
</div>
            