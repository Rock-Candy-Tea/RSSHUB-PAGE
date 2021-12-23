
---
title: 'WasmEdge 0.9.0 发布，提升性能、稳定性与互操作性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1387'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 11:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1387'
---

<div>   
<div class="content">
                                                                                            <p>WasmEdge 0.9.0 发布啦。新版的 WasmEdge 迎着新年的脚步走来了！是时候为大家揭晓 WasmEdge 的新特性了，一起解锁 2022年的新技能吧！</p> 
<p>此版本的 WasmEdge 专注于云原生基础架构的性能、稳定性以及与互操作性。 具体来说，WasmEdge 现在支持：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Fblob%2Fmaster%2Fdocs%2Fsimd.md" target="_blank">SIMD 标准和其他几个 WebAssembly 提案(默认情况下)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs.html" target="_blank">更多 JavaScript 标准，例如 ES6、CJS 和 NPM 模块</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2Fssr.html" target="_blank">性能提升，特别是对于 JavaScript 应用程序</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fembed%2Fc.html" target="_blank">优化且符合标准的 C API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fframeworks%2Fapp%2Freactr.html" target="_blank">增强的 Go API 和 Reactr 集成</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fframeworks%2Fmesh%2Fdapr.html" target="_blank">Dapr 集成</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fstart%2Funiversal.html" target="_blank">一种新的通用 Wasm 二进制文件格式，用于 AOT 编译的高性能应用</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fkubernetes.html" target="_blank">容器和 Kubernetes 生态</a></li> 
</ul> 
<h2>SIMD 和其它 WebAssembly 提案</h2> 
<p>WasmEdge 从 0.7.0 版本开始支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Fblob%2Fmaster%2Fdocs%2Fsimd.md" target="_blank">WebAssembly SIMD（单指令多数据）提案。</a> 从 WasmEdge 0.9.0开始，它默认启用 SIMD。</p> 
<blockquote> 
 <p>对于具有多个 CPU 内核的现代设备，SIMD 允许数据处理程序充分利用 CPU。 SIMD 可以大大提高数据应用程序的性能。</p> 
</blockquote> 
<p>除了 SIMD 规范之外，WasmEdge 0.9.0 还增加了对 W3C 目前正在考虑的许多 WebAssembly 提案的支持，包括Import/Export mutable globals 提案、Non-trapping float-to-int conversions 提案、Sign-extension operators 提案和Multi-value提案。 这些提案在 WasmEdge 中是默认启用的。</p> 
<p>如果你想禁用其中一些特性，你可以在 <code>wasmedge</code> 和 <code>wasmedgec</code>中使用<code>--disable-proposal-name</code>。</p> 
<h2>增强的 JavaScript 支持</h2> 
<p>在 WebAssembly runtime 中运行 JavaScript 程序有着非常明显的好处。 WasmEdge 可以充当与 Linux 应用程序容器并行运行的安全应用程序容器，但只消耗一小部分资源并提供更好的可移植性和安全性。</p> 
<p>WasmEdge 不仅支持 JavaScript 应用程序，还支持将 JavaScript 与 Rust 等高性能语言混合使用。在 WasmEdge 0.9.0 版本中，我们增强了对 JavaScript 生态系统的支持。 WasmEdge 现在支持重用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2Fes6.html" target="_blank">ES6 模块</a> 、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2F%2520cjs.html" target="_blank">CommonJS (CJS) 模块</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2Fnpm.html" target="_blank">NPM 模块</a>。我们还有一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fdev%2Fjs%2Fssr.html" target="_blank">运行 React SSR JavaScript 函数</a>的示例 。</p> 
<p>随着 WasmEdge networking socket API 及其 JavaScript runtime 的持续优化，我们的目标是在不久的将来支持复杂的应用场景，例如 React SSR Streaming。</p> 
<h2>性能提升</h2> 
<p>虽然 WasmEdge 已经是性能很好的 WebAssembly runtime 之一，但我们也知道在某些特殊情况下，WasmEdge 可能表现不佳。 其中一种情况是在 WasmEdge 中运行 JavaScript 解释器。 但现在这种情况发生改变了！ WasmEdge 0.9.0 是 QuickJS 解释器引擎测试中花费时间最少的 WasmEdge 版本。</p> 
<p>另一个与性能相关的更改是我们在 WasmEdge 0.9.0 中将 runtime <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fstart%2Fcli.html" target="_blank">统计指标收集和报告设为可选</a>。 如果你确实想在 runtime 查看 WasmEdge 的性能统计信息，可以使用以下命令行选项。</p> 
<ul> 
 <li>使用 <code>--enable-time-measuring</code> 展示执行时间。</li> 
 <li>使用 <code>--enable-gas-measuring</code> 来显示使用的 gas 量。</li> 
 <li>使用 <code>--enable-instruction-count</code> 来展示执行的命令数量。</li> 
 <li>或者使用 <code>--enable-all-statistics</code> 来启动所有的数据选择。</li> 
</ul> 
<h2>改进的 C API</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fembed%2Fc%2Fref.html" target="_blank">C API</a> 在 WasmEdge 0.9.0 有很多改变和提升。 我们更新了与 host 函数相关的 API、Wasm 类型上下文和实例创建 API。 我们重命名了 Interpreter API 并简化了 WASI 创建和初始化。 我们还广泛重构了 C API 的内部实现以提高性能。</p> 
<p>C API 中也有一些新特性。一个新的 WasmEdge C API 用于列出来自 AST 模块上下文的导入和导出。 开发者可以查询WASI 和 AOT 编译器相关配置。</p> 
<p>有关 C API 更改内容的详细说明，请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.9.0" target="_blank">changelog</a>。</p> 
<h2>Universal wasm binary</h2> 
<p>WasmEdge 的大部分原始性能来自其高度优化的 AOT 编译器。 开发者可以使用 <code>wasmedec XYZ.wasm XYZ.so</code> 命令或使用 SDK 从 AOT 编译器创建 Linux 原生 <code>.so</code> 文件。 然而，虽然 <code>.so</code> 文件的性能要高得多，但它不可移植。 从 0.9.0 开始，WasmEdge AOT 编译器工具将原生二进制文件包装到原始 wasm 文件中的自定义部分。 它允许 Wasm 应用程序在不受支持的操作系统或平台上从 AOT 编译优雅地降级到解释器执行。</p> 
<p>开发者可以使用 <code>wasmedgec XYZ.wasm XYZ.wasm</code> 来创建<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fstart%2Funiversal.html" target="_blank">通用的 wasm 二进制文件</a> 。</p> 
<p>有了此特性，你可以在其它 wasm runtime 像运行常规 wasm 文件一样运行由 WasmEdge AOT 编译器生成的 wasm 文件。 但是如果你使用 WasmEdge 来运行 wasm 文件，WasmEdge 将从自定义部分中提取原生二进制文件并执行它。</p> 
<h2>容器和 k8s 工具</h2> 
<p>云原生 WebAssembly 应用程序可以由容器工具管理，并在 k8s 集群中与 Linux 容器应用并行运行。 作为最受欢迎的 OCI runtime 项目之一，crun 增加了内置的 WasmEdge 0.9.0 支持，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fkubernetes.html" target="_blank">云原生 WebAssembly 愿景</a>终于成为现实。</p> 
<p>要了解如何利用 Kubernetes、Docker、containerd 和 CRI-O 等容器工具来编排、管理和运行轻量级 WebAssembly 应用程序，请参阅文章-<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.secondstate.io%2Farticles%2Fmanage-webassembly-apps-in-wasmedge-using-docker-tools%2F" target="_blank">使用容器和 Kubernetes 工具管理 WebAssembly 应用程序</a>。</p> 
<p>了解更多有关 WasmEdge 0.9.0 的相关信息，请查看我们的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.9.0" target="_blank">changelog</a>。</p> 
<p>最后，我们要感谢社区成员的贡献，包括 @q82419, @ibmibmibm, @hydai, @SAtacker, @juntao, @LFsWang, @yanganto, @apekuss, @alabulei1, @dm4, @0yi0, @nhynes, @eee4017, @LuiHsu, @avinal, @MileyFu, @O3OI, @vss96, @kenvifire, @ZhangHanDong, @CaptainVincent, @slidoooor, @robnanarivo, @Peter-Chang, @PsiACE, @spider0061, @Jayita10, @actly, @William-Mou, @L-jasmine, @chenyukang, @Yoname, @MaaKhan711635, @tpmccallum。</p>
                                        </div>
                                      
</div>
            