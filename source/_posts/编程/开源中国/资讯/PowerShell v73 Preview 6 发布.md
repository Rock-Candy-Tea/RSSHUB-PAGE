
---
title: 'PowerShell v7.3 Preview 6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4761'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4761'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PowerShell Core 是一个跨平台（Windows、Linux 和 macOS）的自动化和配置工具/框架，可以很好地与你现有的工具配合，并为处理结构化数据（如 JSON、CSV、XML 等）、REST API 和对象模型而优化。它包括一个命令行 Shell、一种相关的脚本语言和一个处理 cmdlets 的框架。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PowerShell v7.3 Preview 6 发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">常规 Cmdlet 更新和修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>Export-PSSession</code><span> </span>在为<span> </span><code>-OutputModule</code><span> </span>指定有根的路径时不抛出错误</li> 
 <li>改变<span> </span><code>ConvertFrom-Json -AsHashtable</code>，以使用有序的哈希表</li> 
 <li>在<span> </span><code>Out-GridView</code><span> </span>中使用前，删除字符串中潜在的 ANSI 转义序列</li> 
 <li>为<span> </span><code>New-TimeSpan</code><span> </span>添加<span> </span><code>-Milliseconds</code><span> </span>参数</li> 
 <li>更新<span> </span><code>Set-AuthenticodeSignature</code>，使用<span> </span><code>SHA256</code><span> </span>作为默认值</li> 
 <li>修复补全<span> </span><code>ValidateSet</code><span> </span>值时的标签补全回归问题</li> 
 <li>在显示方法定义和重载时显示可选参数</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">测试</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为发布版本修复 SDK 测试</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">构建和包的改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新了 .NET SDK 至<span> </span><code>7.0.100-preview.6.22352.1</code></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases%2Ftag%2Fv7.3.0-preview.6" target="_blank">https://github.com/PowerShell/PowerShell/releases/tag/v7.3.0-preview.6</a></p>
                                        </div>
                                      
</div>
            