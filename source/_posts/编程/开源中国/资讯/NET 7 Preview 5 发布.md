
---
title: '.NET 7 Preview 5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6662'
author: 开源中国
comments: false
date: Thu, 16 Jun 2022 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6662'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">.NET 7 发布了第 5 个预览版。</span></p> 
<p><strong>主要变化包括：</strong></p> 
<ul> 
 <li>改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-7-generic-math%2F" target="_blank">Generic Math</a>，方便 API 作者的使用</li> 
 <li>为 <span style="background-color:#ffffff; color:#333333">ML.NET </span>引入新的 <span style="background-color:#ffffff; color:#333333">Text Classification API，</span>增加了最先进的深度学习技术对于自然语言处理</li> 
 <li>对源代码生成器的多项改进</li> 
 <li>用于 RegexGenerator 的新 Roslyn 分析器和修复器，以及在 CodeGen、可观察性、JSON 序列化/反序列化和使用流方面的多项性能改进</li> 
</ul> 
<hr> 
<p style="text-align:left"><strong>对源代码生成器的多项改进</strong></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了对</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><code><span>IAsyncEnumerable</span><span><</span><span>T</span><span>></span></code><span style="background-color:#ffffff; color:#333333"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F59268" target="_blank">#59268</a><span style="background-color:#ffffff; color:#333333">),<span> </span></span><code><span>JsonDocument</span></code><span style="background-color:#ffffff; color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F59954" target="_blank">#59954</a><span style="background-color:#ffffff; color:#333333">),</span><code><span>DateOnly</span></code><span style="background-color:#ffffff; color:#333333">/</span><code><span>TimeOnly</span></code><span style="background-color:#ffffff; color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F53539" target="_blank">#53539</a><span style="background-color:#ffffff; color:#333333">)<span> </span></span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff">类型的源代码生成支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>。例如：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code class="language-cpp">[JsonSerializable(typeof(typeof(MyPoco))]
public class MyContext : JsonSerializerContext &#123;&#125;

public class MyPoco
&#123;
    // Use of IAsyncEnumerable that previously resulted 
    // in JsonSerializer.Serialize() throwing NotSupportedException 
    public IAsyncEnumerable<int> Data &#123; get; set; &#125; 
&#125;

// It now works and no longer throws NotSupportedException
JsonSerializer.Serialize(new MyPoco &#123; Data = ... &#125;, MyContext.MyPoco); </code></pre> 
<p><strong>改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-7-generic-math%2F" target="_blank">Generic Math</a></strong></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>.NET 6 发布了预览版的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fpreview-features-in-net-6-generic-math%2F" target="_blank">Generic Math</a>，此特性允许 .NET 开发者在通用代码中利用静态 API，包括运算符。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Generic Math 极大地方便了 API 作者<span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>，因为他们使用的 API 将开始支持更多类型，而不需要每个数字类型都获得显式支持。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 .NET 7 中，开发团队对实现进行了改进并响应了社区的反馈。有关更改和可用 API 的更多信息，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-7-generic-math%2F" target="_blank">点此查看</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-5%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            