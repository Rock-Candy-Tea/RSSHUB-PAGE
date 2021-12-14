
---
title: 'Safari 15.2 引入新的 WebKit 改进，支持 Wasm 和广色域'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8020'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 08:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8020'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px"><span style="color:#333333">WebKit 的最新更新为 Safari 15.2 带来了许多改进，重点是支持创意应用程序和利用当今硬件的强大功能。</span>互联网一直关于交流和协作，它始于由文本组成的异步消息。随着它的成熟，互联网变得实时互联，添加了图像，然后是视频。现在网站变成了一种发布、广播、经营、聚集社区和创造新技术的手段。</p> 
<h3 style="margin-left:0px">WebAssembly 增强功能</h3> 
<p style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWebAssembly" target="_blank">WebAssembly (Wasm)</a>是一种低级汇编语言，允许编译多种编程语言，如 C/C++、C#、Objective-C、Swift、Python、Java 甚至 Cobol，以接近本机的速度在 Web 上运行，而无需用户安装任何特殊的组件。</p> 
<p style="margin-left:0px">Wasm 旨在与 JavaScript 一起工作，允许网站同时使用两者，提供了将强大的软件应用程序引入网络所需的工具。</p> 
<p style="margin-left:0px">在 Safari 15.2 中，Wasm 的可寻址内存已扩展到 4GB，为更大、更强大的应用程序开辟了可能性。添加零成本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWebAssembly%2Fexception-handling%2Fblob%2Fmaster%2Fproposals%2Fexception-handling%2FExceptions.md" target="_blank">异常处理</a>还为 Wasm 提供了潜在的性能提升。</p> 
<h3 style="margin-left:0px">COOP/COEP HTTP 标头</h3> 
<p style="margin-left:0px">共享内存为原生应用程序提供了强大的功能，不过在 Web 上，这种功能必须与强大的安全保护相平衡。 Safari 10.1-11 的 WebKit 曾支持 <code>SharedArrayBuffer</code>，但由于其存在用于推测执行攻击（比如如 Spectre）的风险而被禁用。</p> 
<p style="margin-left:0px">Safari 15.2 添加了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FCross-Origin-Opener-Policy" target="_blank"><code>Cross-Origin-Opener-Policy</code>(COOP)</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FCross-Origin-Embedder-Policy" target="_blank"><code>Cross-Origin-Embedder-Policy</code>(COEP)</a> HTTP 响应标头的支持。站点可以采用这些标头来选择进程隔离并得到更好的保护。如果站点同时提供<code>Cross-Origin-Opener-Policy: same-origin</code> 和 <code>Cross-Origin-Embedder-Policy: require-corp</code>，它们现在<strong>可以再次使用 SharedArrayBuffer 和 Wasm 线程。</strong></p> 
<h3 style="margin-left:0px">对 Canvas 的广色域支持</h3> 
<p style="margin-left:0px">现代创意依赖于相机和华丽的显示器，然而，当今 Web 上的大多数颜色都是 sRGB 颜色，跟 1990 年代后期计算机显示器的有限的颜色功能相匹配。但其实人类视觉系统可以感知更广泛的颜色，比如现代的显示器再现了 Display P3 色域的颜色，饱和度明显高于 sRGB。</p> 
<p style="margin-left:0px">自 2016 年以来，WebKit 已支持广色域图像和视频，广色域颜色支持的一个显着要点是在 HTML <code>canvas</code> 元素中。</p> 
<p style="margin-left:0px">如今，在 Safari 15.2 中，WebKit 添加了广泛的色域支持——包括 Display P3——用于HTML5的 <code>canvas</code> 标准，此功能通过<em> <strong>Wide Gamut 2D Graphics</strong>  </em>功能实现<em>，</em>将在 Safari 15.2 的发布公告中详细介绍此功能。</p> 
<p style="margin-left:0px"> </p> 
<p style="margin-left:0px">有关 Safari 15.2 中的更多信息，包括错误修复，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fsafari-release-notes%2F" target="_blank">Safari 15.2 发行说明（即将推出）。</a><span style="color:#333333">Safari 15.2 在 macOS Monterey 上可用，也可用于 iOS 和 iPadOS 15.2，很快就会在 macOS Big Sur 和 macOS Catalina 上可用。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            