
---
title: '.NET 7 Preview 4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0512/071600_uCkc_5430600.png'
author: 开源中国
comments: false
date: Thu, 12 May 2022 07:16:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0512/071600_uCkc_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">.NET 7 发布了第 4 个预览版。</span></p> 
<p><br> <img alt height="338" src="https://static.oschina.net/uploads/space/2022/0512/071600_uCkc_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">重要变化一览</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增强 OpenTelemetry 的 .NET 实现的可观测性</li> 
 <li>为日期和时间结构体增加微秒和纳秒属性</li> 
 <li>为缓存扩展(caching extensions)引入新指标</li> 
 <li>提升“On Stack Replacement”性能</li> 
 <li>增加新的 tar API</li> 
 <li>优化 .NET 7 中正则表达式的性能、增加功能</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>为 </strong><span style="color:#333333"><strong>TimeStamp、DateTime、DateTimeOffset 和 TimeOnly</strong></span><strong> 添加微秒和纳秒属性</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在 Preview 4 之前，各种日期和时间结构体中，可用的最小时间增量是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fapi%2Fsystem.datetime.ticks" target="_blank">Ticks</a> 属性中可用的“tick”。在 .NET 中，一个 tick 是 100ns。此前开发者必须对"tick"值执行计算以确定微秒和纳秒值。现在，Preview 4 通过在日期和时间实现中引入微秒和毫秒来解决这个问题。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>增加新的 tar API</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本添加了新的程序集，包含可读取、写入、归档和提取 tar 存档的跨平台 API。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">使用示例</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">// Generates a tar archive where all the entry names are prefixed by the root directory 'SourceDirectory'
TarFile.CreateFromDirectory(sourceDirectoryName: "/home/dotnet/SourceDirectory/", destinationFileName: "/home/dotnet/destination.tar", includeBaseDirectory: true);

// Extracts the contents of a tar archive into the specified directory, but avoids overwriting anything found inside
TarFile.ExtractToDirectory(sourceFileName: "/home/dotnet/destination.tar", destinationDirectoryName: "/home/dotnet/DestinationDirectory/", overwriteFiles: false);</pre> 
<pre style="margin-left:0; margin-right:0; text-align:start">// Generates a tar archive where all the entry names are prefixed by the root directory 'SourceDirectory'
using MemoryStream archiveStream = new();
TarFile.CreateFromDirectory(sourceDirectoryName: @"D:SourceDirectory", destination: archiveStream, includeBaseDirectory: true);

// Extracts the contents of a stream tar archive into the specified directory, and avoids overwriting anything found inside
TarFile.ExtractToDirectory(source: archiveStream, destinationDirectoryName: @"D:DestinationDirectory", overwriteFiles: false);</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>为缓存扩展 (caching extensions) 引入新指标</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本为<code>IMemoryCache</code>添加了指标支持，主要的 API 包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>MemoryCacheStatistics</code> 用于记录命中/未命中/估算缓存大小的数据，以及针对<code>IMemoryCache</code>的计数</li> 
 <li><code>GetCurrentStatistics</code>：返回<code>MemoryCacheStatistics</code>实例，当<code>TrackStatistics</code> flag 未启用则返回 null。该库内置了可用于<code>MemoryCache</code>的实现</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-4%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            