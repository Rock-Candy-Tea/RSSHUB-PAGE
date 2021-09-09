
---
title: 'WasmEdge 0.8.2 发布，增加 Networking 支持、Rust SDK、兼容性优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-970716397fab1c5757a986a79c0790e0dbf.jpg'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 05:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-970716397fab1c5757a986a79c0790e0dbf.jpg'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.8.2" target="_blank">WasmEdge 0.8.2 版本</a>发布啦！</p> 
<ul> 
 <li>更好的跨平台兼容性。在 Mac OS X（Intel 和 M1）、Windows 10 以及配备 ARM 32 位芯片的 IoT 设备上运行 WasmEdge 应用程序。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fwasmedge_wasi_socket" target="_blank">Networking 支持</a>。可以从 WasmEdge 应用程序发出网络请求并运行 HTTP 服务器。</li> 
 <li>新的和改进的 API。在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Fblob%2Fmaster%2Fdocs%2Fc_api_quick_start.md" target="_blank">C</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Ftree%2Fmaster%2Fbindings%2Frust" target="_blank">Rust</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.secondstate.io%2Farticles%2Fextend-golang-app-with-webassembly-rust%2F" target="_blank">Golang</a> 应用程序中嵌入 WasmEdge 函数。</li> 
 <li>WasmEdge 的 AoT 编译器的通用二进制输出。在云原生平台可以利用 AOT 增进性能。</li> 
 <li>支持 proxy-wasm 规范，WasmEdge 为服务网格带来了高性能 API 路由。</li> 
</ul> 
<p><img alt="WasmEdge 0.8.2 版本发布" src="https://oscimg.oschina.net/oscnet/up-970716397fab1c5757a986a79c0790e0dbf.jpg" referrerpolicy="no-referrer"></p> 
<h2>跨平台兼容性</h2> 
<p>借助 <code>manylinux1</code> 发布目标，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge" target="_blank">WasmEdge Runtime</a> ，包括其 AOT 编译器和本机扩展，可以在老旧至 2007 年的 Linux 版本上运行。现在，WasmEdge 也可以在基于ARM 32 位 CPU 老的设备和 SoC 板上运行，它们常常用于物联网应用程序。</p> 
<p>除了 Linux，WasmEdge 还支持 Mac OS X，包括基于 Intel 和 M1 的 Mac 以及 Windows。这些设备得到了开发者和边缘应用程序的广泛使用。你可以在自己的笔记本电脑上尝试一下！</p> 
<p>之后，团队正致力于在即将发布的 WasmEdge 版本中支持如 seL4 等实时操作系统。</p> 
<h2>Networking 支持</h2> 
<p>云原生应用通常需要建立网络连接。但是，标准 WebAssembly 规范不支持 networking。 WASI-socket 规范旨在将基于 socket 的网络支持添加到 WebAssembly 中，但社区仍然就此争论不休。</p> 
<p>WasmEdge 团队决定在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fwasmedge_wasi_socket" target="_blank">WasmEdge 0.8.2 中实现 socket 支持</a>。 WasmEdge 网络 socket 支持以当前的 WASI socket 提案为蓝本，并为开发者提供了一个 Rust crate 来编写具有网络功能的 WebAssembly 应用程序。</p> 
<p>WasmEdge 的网络 socket API 支持 <code>TcpStream</code>、 <code>TcpListener</code>、<code>UdpSocket</code> 和 <code>Shutdown</code>。此版本包括用于 WebAssembly 的 HTTP 客户端和服务器端实现的 Rust demo 应用程序。</p> 
<p>请注意，目前 WasmEdge socket API 仅适用于 Linux。</p> 
<p>更多细节请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fwasmedge_wasi_socket" target="_blank">wasmedge_wasi_socket repo</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fwasmedge_wasi_socket" target="_blank">https://github.com/second-state/wasmedge_wasi_socket</a></p> 
<h2>API 提升</h2> 
<p>WasmEdge 的一个关键应用场景是将其作为 serverless 函数 runtime 嵌入到云原生环境中。这要求开发者通过 API 从主机应用程序启动 WasmEdge。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Fblob%2Fmaster%2Fdocs%2Fc_api.md" target="_blank">WasmEdge C API</a> 是从主机应用程序访问 WasmEdge 运行时的接口。它也是 WasmEdge 其他语言 API 的基础，例如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2FWasmEdge-go" target="_blank">WasmEdge Go API</a>。此版本为 WasmEdge C API 添加了一些功能点。</p> 
<ul> 
 <li>添加了静态库 <code>libwasmedge_c.a</code>。</li> 
 <li>将 <code>ErrCode</code> 添加到 C 声明中。</li> 
 <li>增加了 <code>WasmEdge_String</code> 转换为C 字符串的 API。</li> 
 <li>添加了从 <code>WasmEdge_MemoryInstanceContext</code> 获取数据指针的 API。</li> 
</ul> 
<p>此外，WasmEdge 0.8.2 还包含两个 用于 Rust API 的 Rust crate， <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Ftree%2Fmaster%2Fbindings%2Frust%2Fwasmedge-sys" target="_blank"><code>wasmedge-sys</code></a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Ftree%2Fmaster%2Fbindings%2Frust%2Fwasmedge-rs" target="_blank"><code>wasmege-rs</code></a>。 <code>wasmedge-sys crate</code> 是从 WasmEdge C API 生成的低级 API。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Ftree%2Fmaster%2Fbindings%2Frust%2Fwasmedge-rs" target="_blank"><code>wasmedge-rs</code></a> 是一个惯用的 Rust API，封装了低级 wasmedge-sys ，使其更安全，对开发者更友好。完整的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Ftree%2Fmaster%2Fbindings%2Frust%2Fwasmedge-rs" target="_blank"><code>wasmedge-rs</code></a> crate 仍在积极开发中。欢迎任何反馈和贡献。</p> 
<p>如果你想查看一个 API 的例子，请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fdapr-wasm" target="_blank">dapr-wasm repo</a>。它使用 WasmEdge Golang 和 Rust API 在云原生 service mesh 中实现 sidecar 应用程序。</p> 
<h2>WasmEdge的 AoT 编译器的通用二进制码</h2> 
<p>WasmEdge 0.8.2 添加了一个新的 AOT 编译器 flag <code>--generic-binary</code>。此标志用于生成通用二进制文件并禁用 CPU 特定优化。</p> 
<p>因此，通用二进制文件可能会损失大约 20% 的原始性能，但在整个 CPU 类别中实现了更好的兼容性（例如，生成适用于所有 x86 CPU 的二进制文件）。</p> 
<p><code>--generic-binary</code> 的应用场景包括在 serverless 平台（例如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Faws-lambda-wasm-runtime" target="_blank">AWS Lambda</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Ftencent-scf-wasm-runtime" target="_blank">腾讯云</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fvercel-wasm-runtime" target="_blank">Vercel</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsecond-state%2Fnetlify-wasm-runtime" target="_blank">Netlify</a>）上运行 WasmEdge。为了将这些平台上的启动时间缩短至毫秒级，我们将 WasmEdge 配置为在部署环境预先（AOT）编译其应用程序。我们无法在 runtime (运行环境)预先确定 CPU 的确切代号和型号。通用二进制码选项平衡了 AOT 的性能和 WebAssembly 应用程序的可移植性。</p> 
<h2>支持 Proxy-wasm</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fproxy-wasm%2Fspec" target="_blank">Proxy-wasm</a> 是一种在 API 代理中嵌入 WebAssembly Runtime 的规范。 它允许 WebAssembly 函数以编程方式发送服务网格网络中的 API 流量。 proxy-wasm 标准由 Envoy、Istio Proxy 和 MOSN 支持。 在 WasmEdge 0.8.2 中，提供了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fproxy-wasm%2Fproxy-wasm-cpp-host%2Fpull%2F193" target="_blank">proxy-wasm 的主机实现</a>。 WasmEdge 现在可以用作 Envoy 和 MOSN 的高性能扩展。</p> 
<p>要想了解有关 WasmEdge 0.8.2 版本的更多信息，请查看我们的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.8.2" target="_blank">changelog</a>！ WasmEdge 0.8.2 是朝着云原生 WebAssembly 生态迈出的重要一步。加入我们这场大变革！</p> 
<p>最后，我们感谢来自社区的贡献 @actly、 @alabulei1、@CaptainVincent、@chenyukang、@hydai、@ibmibmibm @juntao、@kenvifire、@L-jasmine、@MaazKhan711635、 @MileyFu、@nhynes、 @q82419、@robnanarivo、 @yanganto 和 @Yonama。（排名不分先后，按照首字母进行排序）</p> 
<p>最后的最后，WasmEdge 参加了今年秋季的 CNCF LFX Mentorship 项目。我们要感谢来自世界各地的 100多名我们项目的开发者，期待他们的贡献。</p>
                                        </div>
                                      
</div>
            