
---
title: '.NET 6 Preview 6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cfabffec60c94b51e21f6b6faed3337c56c.png'
author: 开源中国
comments: false
date: Sat, 17 Jul 2021 07:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cfabffec60c94b51e21f6b6faed3337c56c.png'
---

<div>   
<div class="content">
                                                                                            <p>.NET 6 Preview 6 现已发布，此版本是进入 RC 时期之前的倒数第二个预览版，RC 版本将会有两个 。官方表示，Preview 6 本身相对较小，Preview 7 将会更大。在那之后，团队将进行质量修复，直至 11 月的最终版本发布。</p> 
<h4>x64 仿真更新</h4> 
<p>开发团队已经完成了对 macOS 的 Apple Silicon 和 Windows 的 Arm64 的支持。剩下的就是在 macOS Apple Silicon 和 Windows Arm64 上支持 x64 仿真。其需要做两件事来实现这一点：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fdesigns%2Fpull%2F217" target="_blank">Side-by-side capable installers</a></li> 
 <li>以 .NET CLI 为目标的一流架构（主要）支持在所有场景中使用本机架构 SDK。</li> 
</ul> 
<p>在可以使用 side-by-side capable installers  之前（稍后在 .NET 6 中），用户需要安装所有 x64 版本或所有 Arm64 版本。如果要切换，需要卸载/删除 Arm64 机器上的所有 .NET 版本。</p> 
<h4>Tools：.NET SDK 可选工作负载改进</h4> 
<p>添加了三个新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fdesigns%2Fblob%2Fmain%2Faccepted%2F2020%2Fworkloads%2Fworkloads.md" target="_blank">工作负载</a>命令，可实现更好的发现和管理。</p> 
<ul> 
 <li><code>dotnet workload search</code> — 列出可安装的工作负载。</li> 
 <li><code>dotnet workload uninstall</code>— 如果不再需要工作负载，请删除指定的工作负载。也是节省空间的好选择。</li> 
 <li><code>dotnet workload repair</code> — 重新安装你之前安装的所有工作负载。 
  <ul> 
   <li>如果你的安装因互联网连接断开而在中间失败，这将非常有用。</li> 
   <li>可选工作负载由多个工作负载包组成，你可能已经进入这样一种状态，即其中一些安装成功，而另一些安装失败。</li> 
  </ul> </li> 
</ul> 
<p>在之前的预览中，开发团队添加了以下命令：</p> 
<ul> 
 <li><code>dotnet workload install</code> — 安装工作负载。</li> 
 <li><code>dotnet workload list</code> — 列出已安装的工作负载。</li> 
 <li><code>dotnet workload update</code> — 更新已安装的工作负载。</li> 
</ul> 
<h4>Libraries：TLS support for <code>System.DirectoryServices.Protocols</code></h4> 
<p>Linux 和 macOS 的 System.DirectoryServices.Protocols 已经启用了 TLS 支持。.NET 用户现在可以享受与 LDAP 服务器的安全通信。</p> 
<h4>Tools: Crossgen2 替换 crossgen</h4> 
<p>Crossgen2 已被用于所有现有的 crossgen 方案，官方已从 SDK 中删除了（旧的）crossgen。</p> 
<p>Crossgen（1 和 2）能够将 IL 预编译为本地代码作为 publishing step。预编译主要有利于提高启动率。博客内容指出，Crossgen2 是一个从零开始的实现，已经被证明是一个卓越的代码生成创新平台。例如，与 crossgen1 相比，crossgen2 可以为更多的 IL 模式生成代码。</p> 
<p>以下 MSBuild 属性演示了如何用 crossgen2 启用预编译：</p> 
<pre><code>   <!-- Enable pre-compiling native code (in ready-to-run format) with crossgen2 -->
      <PublishReadyToRun>true</PublishReadyToRun> 
      <!-- Enable generating a composite R2R image -->
      <PublishReadyToRunComposite>true</PublishReadyToRunComposite></code></pre> 
<h4>Libraries：改进了 sync-over-async 的性能</h4> 
<p>当 sync-over-async 是线程池工作线程上发生的唯一阻塞工作类型时，此更改默认提高了线程注入的速度。有一些新的 AppContext 配置值，可以用来配置响应 sync-over-async 的线程注入率。</p> 
<h4>Runtime：W^X memory policy</h4> 
<p>官方正在启用对 W^X memory protection 的支持，这是 Apple Silicon machines 的一项要求，也是其他操作系统上的一项有用的安全措施。 W^X 在 .NET 6 的所有其他环境中是可选的，并且可能是 .NET 7 的所有环境中的默认模式。</p> 
<h4>CodeGen changelog</h4> 
<p><strong>Dynamic PGO</strong></p> 
<ul> 
 <li>添加选项以随机选择受保护的 devirt 类</li> 
 <li>pgo/devirt 诊断改进</li> 
</ul> 
<p><strong>LSRA</strong></p> 
<ul> 
 <li>重构 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fblob%2Fmain%2Fdocs%2Fdesign%2Fcoreclr%2Fjit%2Flsra-detail.md" target="_blank">LSRA</a> heuristics selection 
  <ul> 
   <li>现在，DEBUG 模式包含一个 COMPlus 变量，LsraOrdering 将让用户设置启发式排序。</li> 
   <li>调整寄存器的启发式以选择最佳的寄存器候选溢出。</li> 
  </ul> </li> 
</ul> 
<p><img alt height="180" src="https://oscimg.oschina.net/oscnet/up-cfabffec60c94b51e21f6b6faed3337c56c.png" width="480" referrerpolicy="no-referrer"></p> 
<p><img alt height="209" src="https://oscimg.oschina.net/oscnet/up-24baa5beaa1479897659a06dc2056f9b4ee.png" width="480" referrerpolicy="no-referrer"></p> 
<p><img alt height="194" src="https://oscimg.oschina.net/oscnet/up-42464c7e687d22d62c8307229355508202a.png" width="480" referrerpolicy="no-referrer"></p> 
<p><strong>Code quality</strong></p> 
<ul> 
 <li>消除多余的"test"指令。</li> 
</ul> 
<p>完整更新说明可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6-preview-6%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            