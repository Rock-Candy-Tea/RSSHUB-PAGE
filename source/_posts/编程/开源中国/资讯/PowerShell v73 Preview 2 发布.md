
---
title: 'PowerShell v7.3 Preview 2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1518'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1518'
---

<div>   
<div class="content">
                                                                                            <p>PowerShell Core 是一个跨平台（Windows、Linux 和 macOS）的自动化和配置工具/框架，可以很好地与你现有的工具配合，并为处理结构化数据（如 JSON、CSV、XML 等）、REST API 和对象模型而优化。它包括一个命令行 Shell、一种相关的脚本语言和一个处理 cmdlets 的框架。</p> 
<p>PowerShell v7.3 Preview 2 发布，更新内容如下：</p> 
<h3>引擎更新和修复</h3> 
<ul> 
 <li>修复了生成代理函数的 <code>clean</code> 块</li> 
 <li>增加支持，允许用通用类型的参数调用方法</li> 
 <li>当 PowerShell 内置模块丢失时报告错误</li> 
</ul> 
<h3>常规 Cmdlet 的更新和修复</h3> 
<ul> 
 <li>如果要完成的单词是一个单破折号，则防止命令补全</li> 
 <li>使用 <code>FindFirstFileW</code> 而不是 <code>FindFirstFileExW</code> 来正确处理 FAT32 上的 Unicode 文件名</li> 
 <li>在 Break/Continue 后添加循环标签补全</li> 
 <li>为 <code>File-System</code> 项目添加 <code>.ResolvedTarget</code> 属性，以反映符号链接的目标为 <code>FileSystemInfo</code></li> 
 <li>使用 <code>NotifyEndApplication</code> 来重新启用 VT 模式</li> 
 <li>增加新参数到 <code>Start-Sleep</code>: <code>[-Duration] <timespan></code></li> 
 <li>让 <code>Measure-Object</code> 忽略丢失的属性，除非在严格模式下运行</li> 
 <li>为 <code>Invoke-Command</code> 添加 <code>-StrictMode</code>，允许在本地调用命令时指定严格模式</li> 
 <li>修正 <code>$PSNativeCommandArgPassing</code> = <code>Windows</code>，以正确处理空参数</li> 
 <li>添加 <code>exec</code> cmdlet 以兼容 bash</li> 
 <li>为 7.3 版本更新 <code>HelpInfoUri</code></li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases" target="_blank">https://github.com/PowerShell/PowerShell/releases</a></p>
                                        </div>
                                      
</div>
            