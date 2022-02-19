
---
title: '.NET 7 预览版 1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=496'
author: 开源中国
comments: false
date: Sat, 19 Feb 2022 07:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=496'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">伴随着<span> </span><a href="https://www.oschina.net/news/182806/20th-anniversary-net">.NET 诞生 20 周年</a>。.NET 7 第一个预览版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Ftree%2Fmain%2Frelease-notes%2F7.0%23releases" target="_blank"><span> </span>.NET 7 Preview 1 正式发布</a>。.NET 7 Preview 1 包括对 API 的可空注释、持续的 JIT 编译器优化、新的 API 以及对更多热重载方案的支持。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 .NET 7 Preview 1 已通过<span> </span><a href="https://www.oschina.net/news/182799/visual-studio-2022-17-2-pre-1-released">Visual Studio 17.2 预览版 1</a><span> </span>进行测试，在此可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F7.0" target="_blank">下载<span> </span></a>，适用于 Windows、macOS 和 Linux 。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Microsoft.Extensions 的可空（nullable）注释</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET  在注释 Microsoft.Extensions.* 库，以实现可空性(nullability)方面取得了进展。在 .NET 7 Preview 1 中，以下库已针对可空性进行了注释：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Microsoft.Extensions.DependencyInjection.Abstractions</li> 
 <li>Microsoft.Extensions.Logging.Abstractions</li> 
 <li>Microsoft.Extensions.Primitives</li> 
 <li>Microsoft.Extensions.FileSystemGlobbing</li> 
 <li>Microsoft.Extensions.DependencyModel</li> 
 <li>Microsoft.Extensions.Configuration.Abstractions</li> 
 <li>Microsoft.Extensions.FileProviders.Abstractions</li> 
 <li>Microsoft.Extensions.FileProviders.Physical</li> 
 <li>Microsoft.Extensions.Configuration</li> 
 <li>Microsoft.Extensions.Configuration.Binder</li> 
 <li>Microsoft.Extensions.Configuration.CommandLine</li> 
 <li>Microsoft.Extensions.Configuration.EnvironmentVariables</li> 
 <li>Microsoft.Extensions.Configuration.FileExtensions</li> 
 <li>Microsoft.Extensions.Configuration.Ini</li> 
 <li>Microsoft.Extensions.Configuration.Json</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">到 .NET 7 正式发布时，计划为所有 Microsoft.Extensions.* 库添加可空性注释。可以在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F43605" target="_blank">dotnet/runtime#43605</a><span> </span>处关注进度。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">可观察性（继续改进跟踪 API）</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">继续改进跟踪 API：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加<span> </span><code>ActivityContext.TryParse</code><span> </span>重载，以允许解析和创建<span> </span><code>ActivityContext</code><span> </span>对象，包括是否从远程父级传播活动上下文(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F42575" target="_blank">相关 issue</a>)。</li> 
 <li>添加<span> </span><code>Activity.IsStopped()</code><span> </span>方法， 指示<span> </span><code>Activity</code><span> </span>对象是否停止（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F63353" target="_blank">相关 issue</a>）。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">代码生成</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将一些旧式内部函数转换为 NamedIntrinsic 。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F62271" target="_blank"><span> </span>#62271</a></li> 
 <li>将额外的二进制操作添加到 RangeCheck 分析中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61662" target="_blank">#61662</a></li> 
 <li>[JIT] [61620] 针对 *x = dblCns 优化 ARM64；<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61847" target="_blank"><span> </span>#61847</a></li> 
 <li>CoreRT 支持 ARM64&Unix 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F41023" target="_blank"><span> </span>#41023</a></li> 
 <li>基于覆盖的 FMA codegen 优化<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F58196" target="_blank">#58196</a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">动态 PGO</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F62831" target="_blank"><u>对 Arm64 的 OSR 支持</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61712" target="_blank"><u>JIT：支持同步方法的 OSR</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F62263" target="_blank"><u>JIT：处理 OSR、PGO 和尾部调用的交互</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F60939" target="_blank"><u>添加 2009 年 Jit 架构计划（节选）</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61023" target="_blank"><u>JIT：一些 relops 的有限版本的前向替换</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F63420" target="_blank"><u>JIT：为后期去虚拟化保存泛型上下文</u></a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">Arm64</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F62895" target="_blank"><u>Arm64：内存屏障改进</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61030" target="_blank"><u>在 InitBlkUnroll/CopyBlkUnroll 中使用 SIMD 操作并将展开限制增加到 128 字节</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F63422" target="_blank"><u>[Arm64] 继续展开 InitBlock 和 CopyBlock 最多 128 字节</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F62933" target="_blank"><u>'cmeq' 和 'fcmeq' Vector64.Zero/Vector128.Zero ARM64 包含优化</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F62399" target="_blank"><u>[arm64] JIT: X % 2 == 0 -> X & 1 == 0</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61549" target="_blank"><u>[arm64] JIT：添加符号/零扩展</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61293" target="_blank"><u>[arm64] JIT：为“arrayBase + elementOffset”启用 CSE/提升</u></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61037" target="_blank"><u>[arm64] JIT：将“A * B + C”折叠为 MADD/MSUB</u></a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">互操作：p/Invoke 代码生成</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET 7 将在 .NET 6 中原型化的 p/invoke 源生成器集成到 dotnet/runtime 中，并且一直在转换运行时库以使用它。这意味着转换后的 p/invokes 与 AOT 兼容，不再需要在运行时生成 IL 存根。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">未来打算让 p/invoke 源生成器在运行时之外可用，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F60595" target="_blank"><u>可以在dotnet/runtime#60595</u></a><u><span> </span></u>中关注剩余的工作。</p> 
<h3>System.Text.Json 中的新 API</h3> 
<p>System.Text.Json 附带了一些小的增强功能：</p> 
<ul> 
 <li>开发人员现在可以访问 <code>JsonSerializerOptions</code> ：由 System.Text.Json 内部使用的默认单例（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61434" target="_blank">相关问题</a>）。</li> 
 <li>添加一个 <code>JsonWriterOptions.MaxDepth</code> 属性，并确保此值来自序列化的等效 <code>JsonSerializerOptions.MaxDepth</code> 属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fpull%2F61608" target="_blank">相关问题</a>）。</li> 
 <li>将<code>Patch</code>方法添加到 <code>System.Net.Http.Json</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F60531" target="_blank">相关问题</a>）。</li> 
</ul> 
<h3 style="text-align:left">热重载改进</h3> 
<p>下列更改适用于  <span style="background-color:#ffffff; color:#333333">Blazor WebAssembly 和 .NET 的</span> <span style="background-color:#ffffff; color:#333333">C# 热重载</span></p> 
<ul> 
 <li>向现有方法添加静态 lambda</li> 
 <li>将捕获这个的 lambda 添加到已经有至少一个捕获这个的 lambda 的现有方法中</li> 
 <li>向现有类添加新的静态或非虚拟实例方法</li> 
 <li>向现有类添加新的静态字段</li> 
 <li>添加新类</li> 
</ul> 
<p style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>已知的问题：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>不支持新增类中的实例字段</li> 
 <li>现有或新类中新添加的方法和字段对反射不可见</li> 
</ul> 
<p>可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F57365" target="_blank">dotnet/runtime#57365 </a>中关注进度</p> 
<p> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-7-preview-1%2F" target="_blank">https://devblogs.microsoft.com/dotnet/announcing-net-7-preview-1/</a></p>
                                        </div>
                                      
</div>
            