
---
title: 'WasmEdge 0.9.1 发布！ 更好的 networking 支持与开发者体验、安卓支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6154'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 17:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6154'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge" target="_blank">WasmEdge </a>0.9.1 发布了！此版本集成了高性能 networking、JavaScript 流式 SSR 和 Fetch API 支持、新的 bindgen 框架、安卓和 OpenHarmony 操作系统支持、扩展的 Kubernetes 支持以及改进的内存管理。</p> 
<ul> 
 <li>WebAssembly 扩展</li> 
 <li>流式服务端渲染（SSR）函数</li> 
 <li>安卓和 OpenHarmony</li> 
 <li>Kubernetes</li> 
 <li>漏洞修复和性能提升</li> 
</ul> 
<h2>WebAssembly 扩展</h2> 
<p>WasmEdge 目标是支持所有标准和可选的标准 WebAssembly 扩展提案。WasmEdge 也支持对云原生使用场景的非标准和试验性扩展，例如 networking 和数据传递。</p> 
<h3>Rust 和 JavaScript 的高性能 networking</h3> 
<p>WasmEdge 从 0.8.2 版本开始就原生支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fwasmedge_wasi_socket" target="_blank">Networking socket</a> 。但是，使用同步 networking sockets，应用程序一次只能处理一个连接。因此高性能的 CPU 大部分时间处于空闲状态，等待数据从 network 缓慢流入。</p> 
<p>在 0.9.1 中，WasmEdge 通过在 Rust 和 JavaScript 应用程序中支持非阻塞 I/O ，从而显著提高了 networking 性能。通过非阻塞 I/O，WasmEdge 程序可以一次打开多个连接，并在接收到数据时异步处理来自这些连接的数据。 同时，WasmEdge 为非阻塞 network I/O 提供了 Rust API 和 JavaScript API。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Frust%2Fnetworking-nonblocking.html" target="_blank">Rust 的异步 HTTP 客户端和服务器示例。</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2Fnetworking.html" target="_blank">JavaScript 的异步 HTTP 客户端和服务器示例。</a></li> 
</ul> 
<p>通过 JavaScript 中的非阻塞 network I/O，我们现在可以在 WasmEdge 中运行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2Fssr.html" target="_blank">流式 SSR 函数</a>并使用 JavaScript Fetch API。 流式 SSR 和 Fetch 通常用于边缘 serverless 函数。</p> 
<h3>WasmEdge-Bindgen</h3> 
<p>标准的 WebAssembly 规范仅支持一些开箱即用的简单数据类型。它甚至不支持常见的数据类型，如字符串和数组。要将丰富的数据类型从 Host 应用程序传递给 WebAssembly 函数，我们需要 bindgen 解决方案来将复杂类型转换为简单类型。例如，一个 bindgen 解决方案可以将一个字符串转换为两个整数：一个内存指针和一个长度。</p> 
<p>在浏览器世界中，emscripten 工具链处理 JavaScript 调用基于 C 的 WebAssembly 函数；wasm-bindgen 工具链处理 JavaScript 调用基于 Rust 的 WebAssembly 函数。然而，它们都不能很好地在云原生环境中的 WASI 应用程序工作。</p> 
<p>因此，WasmEdge 团队创建了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fwasmedge-bindgen" target="_blank">wasmedge-bindgen</a> 框架来支持 WASI 环境中的复杂参数。目前支持 Go host app 调用 Rust 编译的 WebAssembly 函数。具体请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fembed%2Fgo%2Ffunction.html" target="_blank">教程</a>。</p> 
<p>同时，我们也在开发 wasmedge-bindgen 对 Rust、C、JavaScript / Node.JS 和 Python host app 的支持。</p> 
<h3>Multi-memories 提案</h3> 
<p>WasmEdge 0.9.1 支持 multi-memories <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWebAssembly%2Fmulti-memory%2Fblob%2Fmain%2Fproposals%2Fmulti-memory%2FOverview.md" target="_blank">提案</a>。此扩展通过在单个 WebAssembly 模块中启用多个内存，使 WebAssembly 执行更快（即更快地复制值）、更安全，且隔离更佳。</p> 
<p>如果要启用 multi-memories 提案，请在 <code>wasmedgec</code> 和 <code>wasmedge</code> 工具中使用 <code>--enable-multi-memory</code> 命令行。</p> 
<h2>支持更多操作系统和设备</h2> 
<p>除了基于 seL4 的嵌入式和实时设备，WasmEdge 现在已被移植到更多的边缘设备平台。 最大的边缘设备平台是安卓，现在安卓已经完全支持 WasmEdge 0.9.1。</p> 
<ul> 
 <li>在安卓平台编译和构建 WasmEdge 。 👉 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fextend%2Fbuild_for_android.html" target="_blank">https://wasmedge.org/book/en/extend/build_for_android.html</a></li> 
 <li>在安卓上使用 Rust + WebAssembly 用于高性能 AI 推理 (mobilenet 图片识别) 👉 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fos%2Fandroid%2Fcli.html" target="_blank">https://wasmedge.org/book/en/os/android/cli.html</a></li> 
 <li>在安卓 NDK shell 中封装一个 WebAssembly 应用。 这与第二个是相同的 TensorFlow TFLite 图片识别/推理 Wasm 应用程序，但包在你自己的应用中。 👉 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fos%2Fandroid%2Fndk.html" target="_blank">https://wasmedge.org/book/en/os/android/ndk.html</a></li> 
 <li>创建一个带有嵌入式 WasmEdge Runtime 的安卓 APK 应用。WebAssembly 函数将你的应用变为一个面向其他开发者的平台。 👉 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fos%2Fandroid%2Fapk.html" target="_blank">https://wasmedge.org/book/en/os/android/apk.html</a></li> 
</ul> 
<p>WasmEdge 和其 TensorFlow 扩展已经在 ARM64 硬件设备上的 Linux 和 Android 操作系统都得到完全支持。</p> 
<p>此外，在 OpenHarmony 操作系统上增加对 WasmEdge 的支持的开发工作已启动。OpenHarmnoy 是新的手机和物联网设备操作系统。</p> 
<p>最后，WasmEdge 0.9.1 已经被 Windows 用户的 windows 包管理器收录。 使用以下命令行就可以在 Windows 上安装 WasmEdge。</p> 
<pre><code>winget install wasmedge
</code></pre> 
<h2>Kubernetes</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fkubernetes.html" target="_blank">WasmEdge 完全符合 OCI 标准。</a>这意味着 WasmEdge 应用可以由标准容器工具存储、管理和执行。 WasmEdge 本身是一个安全的沙箱容器。</p> 
<p>在 Kubernetes 集群中，容器化的 WasmEdge 应用程序可以在同一个集群中与 Linux 容器（例如 Docker 容器应用程序）并行管理和编排。 在 0.9.1 版本中，WasmEdge 得到边缘优化的 Kubernetes 框架的正式支持，如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fkubernetes%2Fkubernetes%2Fopenyurt.html" target="_blank">OpenYurt</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge%2Fblob%2Fmain%2Fexamples%2Fwasmedge%2Fwasmedge.md" target="_blank">SuperEdge</a>。</p> 
<h2>漏洞修复和性能提升</h2> 
<p>WasmEdge 每次版本发布都有长串的漏洞修复和性能提升清单。这次 0.9.1 版本也不例外。</p> 
<ul> 
 <li>通过在生产环境的应用程序中大量使用，已发现并修复了大量内存泄漏问题。</li> 
 <li>减少指令类的内存使用量，这进一步减少了 WasmEdge 在边缘设备上的占用空间。</li> 
 <li>WasmEdge 执行现在可以被外部信号中断和恢复。 此功能支持更加规范的嵌入式函数。</li> 
 <li>对 WasmEdge CLI 帮助信息进行了美化。</li> 
</ul> 
<p>虽然 WasmEdge 0.9.1 是一个小的版本更新，但是有着对开发者而言非常重要的特性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.9.1" target="_blank">快来查看吧</a>！</p> 
<p>感谢 WasmEdge 的所有贡献者！L-jasmine, yanganto, AvengerMoJo, HangedFish, harytary, KernelErr, juntao, MileyFu, O3OI, Saksham Sharma, Shen-Ta Hsieh(BestSteve), SAtacker, Sonofmagic, srenatus, 0xE282B0, vdice, apepkuss, 0yi0, q82419, chenyukang, st9549898, sakhshm26, dreammyboy, zephoon, megrax, alabulei1, alittlehorse, baiyutang, hydai, javadoors, jaredliw, Vinson-Ben, majinghe, meoww-bot, wangbyby, pasicopan, peterbi, villanel, DarumaDocker, wangyuan249, wby, wolfishLamb, sunnywa.</p>
                                        </div>
                                      
</div>
            