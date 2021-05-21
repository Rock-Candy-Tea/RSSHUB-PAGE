
---
title: 'Envoy on Windows GA 了！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0521/141054_PVep_4252687.png'
author: 开源中国
comments: false
date: Fri, 21 May 2021 14:12:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0521/141054_PVep_4252687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><em>作者：Sotiris Nanopoulos</em></p> 
<p>Envoy 项目一直努力使网络对所有运行的应用程序“透明”，而不管编程语言、平台架构和操作系统。今天，我们很兴奋地宣布 Envoy 现在可以在 Windows 平台上使用了！从版本 1.18.3 开始，你可以在 Windows 上使用 Envoy 用于生产工作负载。</p> 
<p><img height="221" src="https://static.oschina.net/uploads/space/2021/0521/141054_PVep_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p>自 2016 年以来，在 Windows 上移植 Envoy 一直是社区的目标。从那以后，Envoy-Windows-Development 小组取得了很大的进展。该团队主要由来自 VMware 和微软的开发者组成，在过去的一年中，该团队合作使 Envoy 从 2020 年 10 月的 alpha 版本到今天的稳定生产就绪状态。</p> 
<p>你现在可以在 Windows 上使用 Envoy 来构建原生云应用程序，改善遗留应用程序的可观察性，甚至可以将 Envoy 部署为边缘代理与 Windows 应用程序一起。</p> 
<p>在我们深入研究我们为改善 Windows 体验而构建的面向公众的特性之前，我们要感谢 Envoy 开发者社区和维护者们的指导、支持和耐心。</p> 
<h2>新增特性</h2> 
<p>自从 Envoy Windows Alpha 版本发布以来，我们增加了更多的功能，支持持续集成，并提高了 Envoy 在 Windows 上的性能和可靠性。</p> 
<h3>使用合成边缘事件改进轮询机制</h3> 
<p>Envoy 在 Linux 解决了C10K[1]问题，方法是为每个线程提供多个客户端服务，并使用非阻塞 I/O 和边缘触发就绪更改通知（edge-triggered readiness change notification）。然而，Windows Server 2019 并不支持边缘触发就绪更改通知，这导致 Envoy 在 Windows 上空转和消耗 CPU 资源。</p> 
<p>为了解决这个问题，我们设计了类似于边缘事件的合成边缘事件。合成边缘事件是由 Envoy 管理的级别事件，其行为与边缘事件类似。我们通过在新事件到达时手动禁用事件注册，并仅在需要时再次启用它们来实现这一点。</p> 
<p>我们在综合测试中观察到，通过切换到合成边缘事件，Envoy 截获的事件减少了 3 个数量级。这是一个显著的改进，允许 Windows 上的 Envoy 扩展到多个并发连接。我们计划进一步完善事件机制。新版本的 Windows 提供了一个原生边缘事件 API，我们计划将其集成到 Envoy 中。</p> 
<h3>Windows 容器镜像</h3> 
<p>我们希望操作人员和开发人员能够以最小的摩擦在 Windows 上开始使用 Envoy。自 2020 年 10 月下旬以来，我们一直在docker hub[2]上发布开发者镜像。这些镜像包含各种 SDK 和工具，对于希望扩展或试验 Envoy 的开发人员特别有用。在版本 1.18 中，我们还发布了更精简的镜像，envoy-windows[3]，这更适合于生产环境。</p> 
<h3>改进的诊断</h3> 
<p>我们希望操作人员能够在相同配置的不同平台上运行 Envoy。新的流访问日志记录器[4]允许操作人员将侦听器和管理门户产生的访问日志重定向到流程的标准输出。Envoy 使用正确的本地 API 写入标准输出/错误，这取决于它运行的平台。</p> 
<h3>添加对 Clang 编译器的支持</h3> 
<p>Envoy 用户利用 Envoy 的通用扩展模型为他们的用例构建自定义过滤器和特性。通用扩展模型的一部分是对 Linux 上不同架构（arm）和编译器工具链（Clang 和 GCC）的支持。遵循社区的精神，我们在 Windows 上增加了对 Clang 的支持。自 1 月份以来，CI 在每个提交上都构建了 envoy.exe，通过包括 MSVC 和 Clang 编译器。</p> 
<h3>改进流程管理</h3> 
<p>Alpha 版本关注的是功能而不是可用性。从那时起，我们为开发者和 Windows 原生操作人员添加了一些功能，以便轻松管理 Envoy 进程的生命周期。现在，当 Ctrl + C 和 Ctrl + Break 事件发送到控制台时，Envoy 优雅地结束了，跟它处理 SIGINT 和 SIGTERM 的方式是一样的。此外，我们还增加了对 Envoy 作为Windows 服务[5]运行的实验性支持。</p> 
<h2>贡献的统计数据</h2> 
<p>虽然这些统计数字本身并不能说明很多问题，但我们想回过头来看看我们在过去一年中所取得的成就：</p> 
<ol> 
 <li> <p>Windows 开发小组已经为 Envoy 仓库贡献了 189 个补丁。</p> </li> 
 <li> <p>435 个 Envoy 的测试中有 416 个在每次提交时都在 Windows 上运行。由于缺乏平台对特定功能的支持，16 个测试没有在 Windows 上编译，其余 3 个测试在新添加的 QUIC 支持中失败。</p> </li> 
 <li> <p>我们支持两个编译器（MSVC 和 Clang），三个运行时（win32 原生、SCM 和容器），以及多个版本的 Windows 操作系统（客户端和服务器版本 1809 及以上）。</p> </li> 
</ol> 
<h2>Envoy Windows 的下一步是？</h2> 
<p>我们还有很多工作要做，让 Windows 上的 Envoy 与 Linux 平起平坐。我们期待：</p> 
<ol> 
 <li> <p>添加更多演示不同用例的示例沙箱。</p> </li> 
 <li> <p>改进二进制文件的发布。</p> </li> 
 <li> <p>测试和改进性能。</p> </li> 
 <li> <p>在即将发布的Windows Server 2022[6]版本中集成服务网格解决方案，如OSM[7]。</p> </li> 
</ol> 
<h2>我如何提供反馈并参与其中？</h2> 
<p>我们期待你的反馈和意见。有多种方法可以接触到我们，所有的方法都是同等有效的，所以你可以选择一个你喜欢的。</p> 
<p>你可以在Envoy slack 工作空间[8]#envoy-windows-dev 频道中与致力于 Envoy on Windows 的贡献者联系，提出问题或提供反馈。此外，我们跟踪和分类所有Github 问题[9]。我们也会关注envoy-dev[10]和envoy-announce[11]谷歌群，并回答问题。我们还在文档网站上维护一个FAQ[12]。</p> 
<p><em>重要的一点是，如果你遇到了导致 Envoy 崩溃的 bug，请联系 envoy-security@googlegroups.com。你可能无意中发现了一个不应该在我们修补它之前公开的安全漏洞。</em></p> 
<p>像每个 CNCF 项目一样，我们每两周举办一次会议，你可以在Envoy CNCF 日历[13]上找到。这些会议是一个开始参与 Envoy on Windows 路线图并为之做出贡献的好地方。</p> 
<p><em>Envoy Windows 开发小组，</em></p> 
<p><em>Sunjay Bhatia、Bill Rowe（VMware）</em></p> 
<p><em>Praveen Balasubramanian、Nick Grifka、Randy Miller、Sotiris Nanopoulos、David Schott（微软）</em></p> 
<h3>参考资料</h3> 
<p>[1] C10K: <em>http://www.kegel.com/c10k.html</em></p> 
<p>[2] docker hub: <em>https://hub.docker.com/r/envoyproxy/envoy-windows-dev</em></p> 
<p>[3] envoy-windows: <em>https://hub.docker.com/r/envoyproxy/envoy-windows</em></p> 
<p>[4] 新的流访问日志记录器: <em>https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/access_loggers/stream/v3/stream.proto#standard-streams-access-loggers</em></p> 
<p>[5] Windows 服务: <em>https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/run-envoy#run-envoy-with-the-demo-configuration</em></p> 
<p>[6] Windows Server 2022: <em>https://cloudblogs.microsoft.com/windowsserver/2021/03/02/announcing-windows-server-2022-now-in-preview/</em></p> 
<p>[7] OSM: <em>https://openservicemesh.io/</em></p> 
<p>[8] Envoy slack 工作空间: <em>https://envoyslack.cncf.io/</em></p> 
<p>[9] Github 问题: <em>https://github.com/envoyproxy/envoy/issues</em></p> 
<p>[10] envoy-dev: <em>https://groups.google.com/g/envoy-dev</em></p> 
<p>[11] envoy-announce: <em>https://groups.google.com/g/envoy-announce</em></p> 
<p>[12] FAQ: <em>https://www.envoyproxy.io/docs/envoy/latest/faq/overview#windows</em></p> 
<p>[13] Envoy CNCF 日历: <em>https://goo.gl/PkDijT</em></p>
                                        </div>
                                      
</div>
            