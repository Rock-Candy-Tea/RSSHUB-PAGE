
---
title: '.NET 7 Preview 7 发布，下一版本进入 RC 阶段'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6466'
author: 开源中国
comments: false
date: Fri, 12 Aug 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6466'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <p>.NET 7 发布了最后一个预览版 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-7%2F" target="_blank">Preview 7</a>，在此之后将会进入 RC 阶段。</p> 
 <p>此版本主要变化包括对 System.LINQ、Unix 文件权限、底层结构、p/Invoke 源代码生成、代码生成和 websocket 的改进。</p> 
 <h3>优化<code>System.LINQ</code></h3> 
 <p><code>System.Linq</code>现在包含<code>Order</code>和<code>OrderDescending</code>方法，它们可以根据<code>T</code>对<code>IEnumerable</code>进行排序。<code>IQueryable</code>现在也同样提供对此的支持。</p> 
 <p><strong>用法</strong></p> 
 <p>此前需要通过引用自身的值来调用<code><span>OrderBy</span></code><span style="background-color:#ffffff; color:#333333">/</span><code><span>OrderByDescending</span></code><span style="background-color:#ffffff; color:#333333"><span> </span></span></p> 
 <pre><code class="language-cpp">var data = new[] &#123; 2, 1, 3 &#125;;
var sorted = data.OrderBy(static e => e);
var sortedDesc = data.OrderByDescending(static e => e);</code></pre> 
 <p>现在支持直接写成：</p> 
 <pre><code class="language-cpp">var data = new[] &#123; 2, 1, 3 &#125;;
var sorted = data.Order();
var sortedDesc = data.OrderByDescending();</code></pre> 
 <h3 style="text-align:left">支持 Unix 文件模式</h3> 
 <p>此前 .NET 没有内置支持获取和设置 Unix 文件权限，这些权限用于控制哪些用户可以读取、写入和执行文件以及目录。而且 P/Invoking 手动调用 syscalls 并不容易，因为有些 syscalls 在不同的发行版上有不同的公开方式。例如，在 Ubuntu 上，你可能要对<code>__xstat</code>进行 Pinvoke，在 Red Hat 上对<code>stat</code>进行 Pinvoke，诸如此类。为此，Preview 7 引入了一个新的枚举：</p> 
 <pre><code class="language-cpp">public enum UnixFileMode
&#123;
    None,
    OtherExecute, OtherWrite, OtherRead,
    GroupExecute, GroupWrite, GroupRead,
    UserExecute, UserWrite, UserRead,
     ...
&#125;</code></pre> 
 <p><strong>用法</strong></p> 
 <pre><code class="language-cpp">// Create a new directory with specific permissions
Directory.CreateDirectory("myDirectory", UnixFileMode.UserRead | UnixFileMode.UserWrite | UnixFileMode.UserExecute);

// Create a new file with specific permissions
FileStreamOptions options = new()
&#123;
    Access = FileAccess.Write,
    Mode = FileMode.Create,
    UnixCreateMode =  UnixFileMode.UserRead | UnixFileMode.UserWrite,
&#125;;
using FileStream myFile = new FileStream("myFile", options);

// Get the mode of an existing file
UnixFileMode mode = File.GetUnixFileMode("myFile");

// Set the mode of an existing file
File.SetUnixFileMode("myFile", UnixFileMode.UserRead | UnixFileMode.UserWrite | UnixFileMode.UserExecute);</code></pre> 
 <h3 style="text-align:left">优化底层<code><span>struct</span></code><span>：支持</span><code><span>ref</span></code><span> </span>字段</h3> 
 <p>.NET 7 运行时环境现在完全支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fapi%2Fsystem.type.isbyreflike" target="_blank">ByRefLike</a> 类型中的<code>ref</code>字段（即<code>ref struct</code>）。此功能背后包含大量的语言设计，例如<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcsharplang%2Fblob%2Fmain%2Fproposals%2Flow-level-struct-improvements.md" target="_blank">改进底层结构</a>。借助此功能，以前需要在运行时环境中进行专门处理的类型（例如<code>Span<T></code>和<code>ReadOnlySpan<T></code>），现在可以在 C# 中完全实现。</p> 
</div> 
<div style="text-align:start">
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-7%2F" target="_blank">详情查看发布公告</a>。
</div>
                                        </div>
                                      
</div>
            