
---
title: '.NET 6 RC1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6698'
author: 开源中国
comments: false
date: Fri, 17 Sep 2021 06:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6698'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET 6 Release Candidate 1 现已发布，这是两个 RC 版本中的第一个版本。微软方面表示，在过去的一个月左右，团队一直专注于质量改进，解决新功能中的功能或性能问题或现有功能的回归问题。具体更新内容如下：</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>源码构建</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">公告指出，“源码构建是一个场景，也是我们与 Red Hat 公司合作的基础设施，自 .NET Core 1.0 发布之前就一直在进行。几年后，我们已经非常接近于提供一个完全自动化的版本。对于 RHEL 的.NET用户来说，此功能非常重要”。Red Hat 方面表示，.NET 已经发展成为他们生态系统中的一个重要的开发者平台。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET 6 中的最大改进是：“source tarball 现在是我们构建的产品”。过去，它需要大量的人工来制作，从而导致向 Red Hat 提供 source tarball 会出现巨大的延迟；导致双方对此都不满意。双方已经在这个项目上合作了五年之久，如今终于取得了成功。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET 团队项目经理 Richard Lander 认为，源码构建是向可重复构建迈出的一大步；.NET SDK 和 C# 编译器具有显著的可重复构建能力。不过要想实现完全的可重复性，仍有一些具体的技术问题需要解决。其中，一个主要的遗留问题则是对汇编中的压缩内容使用稳定的压缩算法。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>配置文件引导优化 (PGO)</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Profile Guided Optimization (PGO) 是大多数开发者平台的一项重要功能。它是基于这样的假设：作为启动的一部分执行的代码通常是统一的，通过利用这一点可以提供更高级别的性能。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET 已经以各种形式使用 PGO 二十年了。在 .NET 6 中，开发团队决定从头开始重建 PGO 系统，专注于实现更好的体验。在这个版本中，运行时库被编译成随时可以运行的格式，并以（新形式的）PGO 数据进行了优化。而这在很大程度上是由 crossgen2 作为新的使能技术所推动的。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，该团队还没有让其他任何人使用 PGO 来优化应用程序。并表示，这是接下来将会在 .NET 7 中出现的内容。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>动态 PGO</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">动态 PGO 是以上描述的静态 PGO 系统的镜像。静态 PGO 与 crossgen2 集成，动态 PGO 与 RyuJIT 集成。静态 PGO 需要单独的训练活动并使用特殊工具，而动态 PGO 是自动的，并使用运行中的应用程序来收集相关数据。在静态 PGO 数据被持久化的情况下，动态 PGO 数据在每次应用程序运行后都会丢失。动态 PGO 类似于跟踪 JIT。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">动态 PGO 目前是 opt-in，并设置了以下环境变量。</p> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>DOTNET_TieredPGO=1</li> 
  <li>DOTNET_TC_QuickJitForLoops=1</li> 
 </ul> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Crossgen2</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Richard Lander 称，Crossgen2 是平台 ahead-of-time 或 pre-compilation 的一个重要步骤，可能是该版本中最有前途的基础性功能。Crossgen2 已被用于所有现有的 Crossgen 方案，官方已从 SDK 中删除了（旧的）Crossgen。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">最重要的方面是，Crossgen2 的设计目标是成为一个独立的编译器。作为一个独立的编译器，它可以用任何语言编写。“当然，我们选择了 C#，但它也可以用 Rust 或 JavaScript 编写”。它只需要能够将给定的 RyuJIT 构建作为插件加载并使用规定的协议与其通信。同样，独立的特性使其能够 cross-targeting。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>安全缓解措施</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">开发团队为此版本添加了对两个关键安全缓解措施的预览支持：CET 和 W^X；并打算在 .NET 7 中默认启用它们。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>CET</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Intel 的 Control-flow Enforcement Technology (CET) 是一些较新的 Intel 和 AMD 处理器中提供的安全功能。它为硬件增加了一些功能，可以防止一些涉及控制流劫持的常见类型的攻击。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>W^X</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">W^X 是最基本的缓解措施之一，它通过禁止内存页同时可写和可执行来阻止最简单的攻击路径。微软方面没有考虑更高级的缓解措施，并表示将添加其他补充缓解措施，如 CET。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">作为 Apple Silicon 过渡的一部分，Apple 已将 W^X 强制用于未来版本的 macOS 桌面操作系统。W^X 适用于所有装有 .NET 6 的操作系统，但仅在 Apple Silicon 上默认启用。对于 .NET 7，它将在所有操作系统上启用。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>HTTP/3</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">HTTP/3 是一个新的 HTTP 版本。作为在 .NET 6 预览版中提出的正式草案，HTTP/3 通过使用称为 QUIC 的新底层连接协议解决了过去 HTTP 版本的现有功能和性能挑战。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，HTTP/3 的 RFC 尚未最终确定，因此仍有可能发生变化。.NET 6 中已包含了 HTTP/3，用户可以尝试使用；这是一项预览功能，因此不受支持。可能存在一些问题，需要与其他服务器和客户端进行更广泛的测试以确保兼容性。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">.NET 6 不包括对 MacOS 上的 HTTP/3 的支持，主要是因为缺乏与 QUIC 兼容的 TLS API。.NET 在 MacOS 上使用 SecureTransport 来实现其 TLS 实现，它还不包括支持 QUIC handshake 的 TLS APIs。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>SDK 工作负载</strong></p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这是一项新功能，使 Microsoft 能够在不增加 SDK 大小的情况下为新应用程序类型添加支持。在未来的版本中，开发团队打算删除更多组件并使它们成为可选组件，包括 ASP.NET 和 Windows 桌面。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">“最后，我们可以想象 SDK 仅包含 MSBuild、NuGet、语言编译器和工作负载获取功能。我们非常希望结合广泛的.NET 生态系统，并提供完成特定工作所需的软件。你可以看到此模型如何更好地用于 CI 场景，使 dotnet 工具能够为正在构建的特定代码获取一组定制组件。”</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">完整更新说明可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6-release-candidate-1%2F" target="_blank">发布公告</a>。</p> 
</div>
                                        </div>
                                      
</div>
            