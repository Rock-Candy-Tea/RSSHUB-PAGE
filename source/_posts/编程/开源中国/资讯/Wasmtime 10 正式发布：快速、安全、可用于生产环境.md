
---
title: 'Wasmtime 1.0 正式发布：快速、安全、可用于生产环境'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9a7e6caaa5bfd612ea215a9516795f71f5d.png'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 08:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9a7e6caaa5bfd612ea215a9516795f71f5d.png'
---

<div>   
<div class="content">
                                                                                            <p>历经三年开发，Bytecode Alliance（字节码联盟）宣布 WebAssembly runtime —— Wasmtime 1.0 正式发布，并可用于生产环境。</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/news/111316/announcing-the-bytecode-alliance">Bytecode Alliance（字节码联盟）</a>由 Mozilla、Fastly、Intel 与 Red Hat 联合成立，是一个推动 WebAssembly 标准化的组织，该联盟旨在通过协作实施标准和提出新标准，以完善 WebAssembly 在浏览器之外的生态。目前正在积极推动 WASI (WebAssembly System Interface)，使 WebAssembly 能够安全地访问文件、网络和内存等系统资源。</p> 
</blockquote> 
<p>Wasmtime 是 Bytecode Alliance 开发的 WebAssembly runtime，采用 Rust 编写，构建于编译器 Cranelift 之上。Wasmtime 完全开源，符合 WASI 标准，还支持与 C/C++、Python、.NET、Go 和其他编程语言<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbytecodealliance.org%2Farticles%2F1-year-update" target="_blank">集成</a>，可运行在 Windows/Linux/macOS 等平台。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9a7e6caaa5bfd612ea215a9516795f71f5d.png" referrerpolicy="no-referrer"></p> 
<p>Bytecode Alliance <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbytecodealliance.org%2Farticles%2Fwasmtime-1-0-fast-safe-and-production-ready" target="_blank">在 1.0 发布公告称</a>此版本“<strong>快速、安全且可用于生产环境</strong>”。此外开发团队还表示，一年前他们就已将 Wasmtime 视作可用于生产环境，但他们不想只是随便发布一个 WebAssembly 引擎，而是希望提供一个在速度和安全性方面有高水准的 WebAssembly 引擎 —— 为了有足够的自信推荐别人使用 Wasmtime。</p> 
<p>因此，在过去的一年里，Bytecode Alliance 部分成员已经在生产环境运行 Wasmtime。Wasmtime 也不负众望，在这些生产环境中表现出色，提供了稳定的平台，同时带来了安全和速度上的优势。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c0b868ac76ab4b280f667211b7ae5534f17.png" referrerpolicy="no-referrer"></p> 
<p>据介绍，Shopify 已经在他们的生产环境使用 Wasmtime 长达 14 个月。Shopify 于 2021 年 7 月从另一个 WebAssembly 引擎切换到 Wasmtime。切换后，Shopify 的平均执行性能提升了大约 50%。Fastly 于 2022 年 3 月从另一个 WebAssembly 引擎切换到 Wasmtime。切换后，Fastly 的执行时间优化了大约 50%。此外，Fastly 每秒请求数的增加幅度从 72% 到 163% 不等。Fastly 还使用 Wasmtime 处理了数万亿个请求。</p> 
<p>Bytecode Alliance 在发布公告提到了提升 Wasmtime 速度的思路。他们表示在优化性能时，主要是关注实例化和 Runtime 的性能。比如针对实例化，他们使用了两种不同的优化手段：虚拟内存和延迟初始化。而对于 Runtime，他们也通过多项更改提升了 runtime 性能，不过主要的提升还是来自于对编译器 Cranelift 所做的更改，它采用 WebAssembly 代码并将其转换为机器代码。</p> 
<p>Bytecode Alliance 最后谈到了未来发布计划，他们会保持频繁且可预测的稳定版本周期，每个月都会发布一个新版本的 Wasmtime。详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.wasmtime.dev%2Fstability-release.html" target="_blank">Release Process</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbytecodealliance.org%2Farticles%2Fwasmtime-1-0-fast-safe-and-production-ready" target="_blank">更多内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            