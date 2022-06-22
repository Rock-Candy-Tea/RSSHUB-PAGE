
---
title: 'WasmEdge 0.10.0 发布！新的插件扩展机制、网络 Socket 增强、LLVM 14支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-48706cadad7c4f92f9d1dd859a93a1dd9cc.png'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 09:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-48706cadad7c4f92f9d1dd859a93a1dd9cc.png'
---

<div>   
<div class="content">
                                                                                            <p>在 0.10.0 版本中，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge" target="_blank">WasmEdge</a> 提供了全新的插件（plug-in）机制，使本地扩展更易于开发和安装，提高了与 LLVM 14 的兼容性，并支持新的 WebAssembly 规范、提案和特性。</p> 
<ul> 
 <li>本地 host 函数的新插件系统</li> 
 <li>对 WasmEdge socket API 的增强（例如，WasmEdge 中的微服务和 Web 服务客户端）</li> 
 <li>支持新的 WebAssembly 提案和规范</li> 
 <li>WasmEdge C API 增强</li> 
 <li>其他特性以及漏洞修复</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-48706cadad7c4f92f9d1dd859a93a1dd9cc.png" referrerpolicy="no-referrer"></p> 
<h2>本地 host 函数的新插件系统</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.secondstate.io%2Farticles%2Fextend-webassembly%2F" target="_blank">host 函数</a>是允许 WebAssembly 程序访问本地库提供的功能和特性的桥梁。 这是我们使用更多特性和函数扩展 WebAssembly runtime 的方式。 例如，WASI 标准本身就是通过 host 函数让 WebAssembly 应用可以使用 <code>libc</code> 进行系统调用。</p> 
<p>WasmEdge 的 TensorFlow、NN、Socket 和图像处理扩展都是通过 host 函数实现的。 让开发者容易使用 host 函数，对 WebAssembly runtime 至关重要。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-361b5ab090ec281ca861fb53a1c6e29eca8.png" referrerpolicy="no-referrer"></p> 
<p>新的 WasmEdge 插件系统旨在简化 host 函数开发和管理。 插件系统可以让开发者可以使用统一的 host 函数接口轻松创建新的 WasmEdge 扩展。 查看 WasmEdge Book 中的指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fextend%2Fplugin%2Floadable.html" target="_blank">如何使用 WasmEdge 的插件系统添加 host 函数</a> ，来试试吧。</p> 
<blockquote> 
 <p>目前只支持使用 C++ 编写 WasmEdge 插件。 在不久的将来，我们将增加对 Rust 和 C 的支持。</p> 
</blockquote> 
<p>WasmEdge 的用户现在可以通过在 WasmEdge 文件夹中添加或删除包含 host 函数的文件来启用或禁用 WasmEdge 扩展。 插件系统让用户在未来可以轻松、安全地管理大量开发者贡献的 WasmEdge 扩展。</p> 
<p>例如， WasmEdge 团队实现了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Ftree%2Fmaster%2Fplugins" target="_blank"><code>wasmedge_process</code></a> 扩展作为插件。<code>wasmedge_process</code> 允许 WebAssembly 程序调用操作系统命令。接下来的几周，我们会把 WasmEdge 的现有扩展移植到新的插件格式。 同时，也欢迎你为 WasmEdge 贡献基于 host 函数的扩展。</p> 
<h2>Wasi-socket 提升</h2> 
<p>WasmEdge networking sockets 是 non-blocking 和高性能的。 WasmEdge 是目前唯一可以运行 Web 服务应用程序的 WebAssembly runtime。 许多开发者尝试创建和部署基于 WasmEdge 的 Web 服务或客户端。 在此版本中，我们继续改进了 WasmEdge socket API。</p> 
<ul> 
 <li>IPV4 和 IPV6 模式</li> 
 <li>UDP 函数：<code>send_to</code> 和 <code>resv_from</code></li> 
 <li>DNS 名称查找</li> 
 <li>检查 socket 选项枚举的有效值</li> 
 <li>修正：MacOS 上的 wasi-socket</li> 
 <li>修正：用同一个 fd 调用 <code>poll_oneoff</code> 两次和在 socket 上调用 <code>fd_close</code> 时出错。</li> 
 <li><code>::getaddrinfo</code> 的以零结尾的字符串。</li> 
</ul> 
<blockquote> 
 <p>展望未来，我们将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Fissues%2F1430" target="_blank">提供兼容 wasm 的 Rust TLS 实现</a> ，从而支持 <code>HTTPS</code> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Fissues%2F1429" target="_blank">在 WasmEdge 中创建 Tokio 异步 runtime</a>。</p> 
</blockquote> 
<h2>C API 提升</h2> 
<p>C API 是 WasmEdge 其他语言 API 的基础，例如 WasmEdge Rust API 和 WasmEdge Go API。 此版本改进了 WasmEdge C API。</p> 
<ul> 
 <li>将 <code>WasmEdge_ImportObjectContext</code> 合并到 <code>WasmEdge_ModuleInstanceContext</code> 中。</li> 
 <li>使用指向 <code>WasmEdge_FunctionInstanceContext</code> 的指针而不是 <code>FuncRef</code> 值类型中的索引。</li> 
 <li>将 <code>WasmEdge_StoreContext</code> 的函数移至 <code>WasmEdge_ModuleInstanceContext</code>。</li> 
 <li>更新了 <code>WasmEdge_VMContext</code> API。</li> 
</ul> 
<p>此新版本也带来新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fembed%2Fc%2Fref.html" target="_blank">C API</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fembed%2Fc%2Fref.html" target="_blank">Go API</a> 文档。 对于想使用更新的 C 和 Go API 的开发者来说，请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fembed%2Fc%2F0.9.1%2Fupgrade_to_0.10.0.html" target="_blank">WasmEdge Book</a>。</p> 
<h2>标准 Wasm 扩展</h2> 
<p>WasmEdge 发展势头迅猛，完全符合了 WebAssembly 标准，并支持所有强制性和可选的 WebAssembly 规范。 从 0.10.0 版开始，WasmEdge 支持<code>Tail Call</code> 和 <code>extended-const</code>提案。</p> 
<h2>其他特性及漏洞修复</h2> 
<p>除了上述特性外，还有一些特性需要注意。</p> 
<ul> 
 <li>兼容 LLVM 14，提高了性能。</li> 
 <li><code>WasmEdge_VMContext</code>、<code>WasmEdge_ConfigureContext</code>、<code>WasmEdge_ModuleInstanceContext</code> 和 <code>WasmEdge_StoreContext APIs</code> 中的线程安全。</li> 
 <li>AOT 模式下的 gas 限制，允许在 WasmEdge 中精确计量应用程序。</li> 
 <li>新的单元测试。</li> 
</ul> 
<p>要了解有关 WasmEdge 0.10.0 版本的更多信息，请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.10.0" target="_blank">changelog</a>! 加入我们吧！</p> 
<p>最后，感谢我们的贡献者！</p> 
<p>apepkuss, dm4, q82419, cyw3, SAtacker, ibmibmibm, hydai, gusy1234, hangedfish, 0yi0, tpmccallum, MediosZ, hantmc, LFsWang, eat4toast, eee4017, situ2001, meoww-bot, juntao, mfordjody, joyaaa, sunnywa, DarumaDocker, spacewander, luckyJ-nj, mydreamer4134, malc0lm,kgpp34, wenchajun, laingke, cold-Elite, border1px, zhuyaguang, bbcfive, JooKS-me, KerneIErr, zswaaa, zhannicholas, O3OI, KcjinChen, FlyingOnion, swartz-k, Bevisy, deyuhua, zephoon, abhinandanudupa, chinzhiweiblank.</p>
                                        </div>
                                      
</div>
            