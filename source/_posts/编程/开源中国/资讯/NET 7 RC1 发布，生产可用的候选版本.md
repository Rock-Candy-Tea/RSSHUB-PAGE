
---
title: '.NET 7 RC1 发布，生产可用的候选版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1011'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1011'
---

<div>   
<div class="content">
                                                                    
                                                        <p>.NET 7 RC 1 发布了， .NET 7 将有两个支持生产的候选版本 (RC)， 这是第一个。</p> 
<p>下载 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F7.0" target="_blank">.NET 7 Release Candidate 1</a></p> 
<p><strong>.NET 7 RC 1 中的新增功能：</strong></p> 
<h2><strong>支持在 Windows Server 2019 上默认使用 ICU 库</strong></h2> 
<p>Windows Server 2019 缺乏 ICU 支持。在 Windows Server 2019 上运行的想要使用 ICU 的服务和应用程序需要部署 ICU 并启用一些配置才能使用它，如<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdotnet%2Fcore%2Fextensions%2Fglobalization-icu%23app-local-icu" target="_blank">文档</a>中所述。</p> 
<p>在 .NET 7.0 rc1 中，Windows Server 2019 将默认支持 ICU。</p> 
<p>参考： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F62329" target="_blank">dotnet/runtime#62329</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F72656" target="_blank">dotnet/runtime#72656</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fdocs%2Fissues%2F30319" target="_blank">dotnet/docs#30319</a>。</p> 
<h2><strong>提高 DateTime 和 DateTimeOffset 中 Add 方法的计算精度</strong></h2> 
<p>改进了 DateTime 和 DateTimeOffset 方法： AddDays、AddHours、AddMinutes、AddSeconds、AddMilliseconds 和 AddMicroseconds 的计算精度，以产生更好的结果。</p> 
<p>参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F66815" target="_blank">dotnet/runtime#66815</a><span style="color:#24292f"> 和 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F73198" target="_blank">dotnet/runtime#73198</a></p> 
<h2><strong>可以从 app.config 文件初始化 System.Diagnostics.TraceSource </strong></h2> 
<p>为了更容易从 .NET Framework 迁移，添加了对从应用程序配置文件初始化 TraceSource 和相关类型（包括 Switch 和 TraceListener）的支持。请注意，必须进行显式调用才能通过 System.Diagnostics.TraceConfiguration.Register() 启用此功能。</p> 
<p>参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F23937" target="_blank">dotnet/runtime#23937</a><span style="color:#24292f"> 和 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F73087" target="_blank">dotnet/runtime#73087</a> </p> 
<h2><strong>支持 XmlSchema 导入/导出</strong></h2> 
<p>.NET 7 RC1 在 DataContractSerializer 空间中带来了导入和导出 XmlSchema 的回归。 该 API 尽可能类似于 .NET Framework  4.8 API，以便从 .NET Framework 轻松移植代码。 </p> 
<p>该导出功能是与 .NET 7.0 SDK 中的 DataContractSerializer 一起内置的功能，在名为 System.Runtime.Serialization.Schema 的附加包中可用。 （这个包不是 7.0 SDK 的一部分，因为它依赖于 System.CodeDom，也作为一个单独的包提供。）</p> 
<p>参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F72243" target="_blank">dotnet/runtime#72243</a> 和 4.8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdotnet%2Fapi%2Fsystem.runtime.serialization.xsddatacontractexporter%3Fview%3Dnetframework-4.8" target="_blank">导出</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fdotnet%2Fapi%2Fsystem.runtime.serialization.xsddatacontractimporter%3Fview%3Dnetframework-4.8" target="_blank">导入</a> API 文档 。</p> 
<h2><strong>检测 HTTP/2 和 HTTP/3 协议错误</strong></h2> 
<p>使用带有默认 SocketsHttpHandler 的 HttpClient 时，现在可以检测 HTTP/2 和 HTTP/3 协议错误代码。 此功能对于 gRPC 等高级应用程序很有用。</p> 
<p><strong>用法</strong></p> 
<p>调用 HttpClient 方法时：</p> 
<pre><code>using var client = new HttpClient();

try
&#123;
    var response = await client.GetStringAsync("https://myservice");
&#125;
catch (HttpRequestException ex) when (ex.InnerException is HttpProtocolException protocolException)
&#123;
    Console.WriteLine("HTTP2/3 protocol error code: " + protocolException.ErrorCode);
&#125;</code></pre> 
<p>调用响应流方法时</p> 
<pre><code>using var client = new HttpClient();
using var response = awaitclient.GetAsync("https://myservice", HttpCompletionOption.ResponseHeadersRead);
using var responseStream = await response.Content.ReadAsStreamAsync();
using var memoryStream = new MemoryStream();

try
&#123;
    await responseStream.CopyToAsync(memoryStream);
&#125;
catch (HttpProtocolException protocolException)
&#123;
    Console.WriteLine("HTTP2/3 protocol error code: " + protocolException.ErrorCode);
&#125;</code></pre> 
<p>参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F70684" target="_blank">dotnet/runtime#70684</a> 。</p> 
<p> </p> 
<p>有关该候选版本的其他功能可以查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F7716" target="_blank">Issue #7716</a> ，或查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-rc-1%2F" target="_blank">更新博客</a>。</p>
                                        </div>
                                      
</div>
            