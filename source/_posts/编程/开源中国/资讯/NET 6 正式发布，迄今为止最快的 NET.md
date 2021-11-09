
---
title: '.NET 6 正式发布，迄今为止最快的 .NET'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1109/070818_2GKj_2720166.png'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 07:57:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1109/070818_2GKj_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>微软宣布 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6%2F" target="_blank">.NET 6</a> 已正式推出，并称其为迄今为止最快的 .NET 版本。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1109/070818_2GKj_2720166.png" referrerpolicy="no-referrer"></p> 
<p>发布公告提到，.NET 6 是首个原生支持 Apple Silicon (Arm64) 的版本，并且还针对 Windows Arm64 进行了改进。.NET 团队<span style="background-color:#ffffff; color:#333333">构建了一个新的动态配置文件引导优化 (PGO) 系统，该系统可提供仅在运行时才会进行的深度优化。其他变化包括使用 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fwhats-new-in-dotnet-monitor%2F" target="_blank">dotnet monitor</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fopentelemetry-net-reaches-v1-0%2F" target="_blank">OpenTelemetry</a> 改进云诊断、提供更强大和更高效的 WebAssembly 支持，以及添加用于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fhttp-3-support-in-dotnet-6%2F" target="_blank">HTTP/3</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Ftry-the-new-system-text-json-source-generator%2F" target="_blank">JSON 处理</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fpreview-features-in-net-6-generic-math%2F" target="_blank">数学</a>和直接操作内存的新 API。</p> 
<p>作为 LTS 长期支持版本，.NET 6 将会获得 3 年的技术支持。</p> 
<p>在 .NET 6 开发周期内，总共包含大约一万个 commit，下面简要介绍新版本的亮点变化。</p> 
<h3>.NET 6 亮点</h3> 
<ul> 
 <li>使用 Microsoft 服务、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Fnycdotnet%2Fstatus%2F1438970921302347778" target="_blank">其他公司运行的云应用程序</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjellyfin%2Fjellyfin%2Fpull%2F6806" target="_blank">开源项目</a>进行了生产压力测试。</li> 
 <li>作为最新的长期支持 (LTS) 版本提供三年的技术支持</li> 
 <li>跨<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Faspnetcore%2Ftree%2Fmain%2Fsrc%2FComponents" target="_blank">浏览器</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Faspnetcore" target="_blank">云</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fwinforms" target="_blank">桌面</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fiot%2F" target="_blank">IoT</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fmaui" target="_blank">移动应用程序的</a>统一平台，全部使用相同的 .NET 库，可便捷地共享代码。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fperformance-improvements-in-net-6%2F" target="_blank">性能全面提升</a>，尤其是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Ffile-io-improvements-in-dotnet-6%2F" target="_blank">文件 I/O 的性能</a>，减少了执行时间、等待时间和内存使用。</li> 
 <li>C# 10 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fwelcome-to-csharp-10%2F" target="_blank">带来了语言改进，</a>例如记录结构 (<span style="background-color:#ffffff; color:#333333">record structs</span>)、隐式使用和新的 lambda 功能，同时编译器添加了增量源代码生成器。 F# 6 新特性包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Ffsharp-6-release" target="_blank">基于 task 的异步、管道调试和多项性能改进</a>。</li> 
 <li>Visual Basic 在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fwhats-new-for-visual-basic-in-visual-studio-2022" target="_blank">Visual Studio 体验和 Windows Forms 项目打开体验方面进行了改进</a>。</li> 
 <li>热重载 (Hot Reload) 支持跳过重新构建和重新启动以查看新更改（当应用程序正处于运行状态），此特性支持在 Visual Studio 2022 中使用，并通过 .NET CLI 为 C# 和 Visual Basic 提供了支持。</li> 
 <li>云诊断已通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fopentelemetry-net-reaches-v1-0%2F" target="_blank">OpenTelemetry</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fwhats-new-in-dotnet-monitor%2F" target="_blank">dotnet monitor</a> 进行改进，现在在生产环境中得到支持，并且可用于 Azure 应用服务。</li> 
 <li>JSON API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Ftry-the-new-system-text-json-source-generator%2F" target="_blank">更强大</a>，并提供源代码生成器器用于串行更高的性能。</li> 
 <li>ASP.NET Core 引入了最少的 API，以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hanselman.com%2Fblog%2Fexploring-a-minimal-web-api-with-aspnet-core-6" target="_blank">简化入门体验</a>并提升 HTTP 服务的性能。</li> 
 <li>Blazor <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Faspnet%2Fcore%2Fblazor%2Fcomponents%2F%3Fview%3Daspnetcore-6.0%23render-razor-components-from-javascript" target="_blank">组件现在可以从 JavaScript 渲染</a>并与现有的基于 JavaScript 的应用程序集成。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Faspnet%2Fcore%2Fblazor%2Fhost-and-deploy%2Fwebassembly%3Fview%3Daspnetcore-6.0%23ahead-of-time-aot-compilation" target="_blank">用于 Blazor WebAssembly (Wasm) 应用程序的</a> WebAssembly AOT <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Faspnet%2Fcore%2Fblazor%2Fhost-and-deploy%2Fwebassembly%3Fview%3Daspnetcore-6.0%23ahead-of-time-aot-compilation" target="_blank">编译</a>，以及对运行时重新链接和本机依赖项的支持。</li> 
 <li>使用 ASP.NET Core 构建的单页应用程序现在使用了更灵活的模式，可以与 Angular、React 和其他流行的前端 JavaScript 框架一起使用。</li> 
 <li>添加了 HTTP/3 以便 ASP.NET Core、HttpClient 和 gRPC 都可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fhttp-3-support-in-dotnet-6%2F" target="_blank">与 HTTP/3 客户端和服务器交互</a>。</li> 
 <li>文件 IO 现在支持符号链接，并通过从头开始重新编写<code><span>FileStream</span></code>大幅提升了性能。</li> 
 <li>通过支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fblog%2Fblog%2F2021%2F09%2F07%2FOpenSSL3.Final%2F" target="_blank">OpenSSL 3</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcryptopp.com%2Fwiki%2FChaCha20Poly1305" target="_blank">ChaCha20Poly1305 加密方案</a>和运行时纵深防御缓解措施（特别是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fdesigns%2Fblob%2Fmain%2Faccepted%2F2021%2Fruntime-security-mitigations.md%23wx" target="_blank">W^X</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fdesigns%2Fblob%2Fmain%2Faccepted%2F2021%2Fruntime-security-mitigations.md%23intel-control-flow-enforcement-technology-cet" target="_blank">CET）</a>，安全性得到了提升。</li> 
 <li>支持为 Linux、macOS 和 Windows（以前仅适用于 Linux）发布单文件应用程序。</li> 
 <li>IL 修剪现在更加强大和有效，提供了新的警告和分析器，可确保正确的最终结果。</li> 
 <li>添加了源代码生成器和分析器，可帮助生成更好、更安全和更高性能的代码。</li> 
 <li>源代码构建使 Red Hat 等组织能够从源代码构建 .NET，并向其用户提供自己的构建版本。</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6%2F" target="_blank">详情查看发布公告</a>。</p> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F6.0" target="_blank">下载 .NET 6.0</a></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F6.0" target="_blank">Installers and binaries</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2F_%2Fmicrosoft-dotnet" target="_blank">Container images</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fblob%2Fmain%2Frelease-notes%2F6.0%2Finstall-linux.md" target="_blank">Linux packages</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fblob%2Fmain%2Frelease-notes%2F6.0%2FREADME.md" target="_blank">Release notes</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fblob%2Fmain%2Frelease-notes%2F6.0%2Fpreview%2Fapi-diff%2Frc1%2FREADME.md" target="_blank">API diff</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fblob%2Fmain%2Frelease-notes%2F6.0%2Fknown-issues.md" target="_blank">Known issues</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F6881" target="_blank">GitHub issue tracker</a></li> 
</ul>
                                        </div>
                                      
</div>
            