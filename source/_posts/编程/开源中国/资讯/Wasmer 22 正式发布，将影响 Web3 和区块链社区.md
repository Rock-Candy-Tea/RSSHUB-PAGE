
---
title: 'Wasmer 2.2 正式发布，将影响 Web3 和区块链社区'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0302/154401_IrdS_2720166.png'
author: 开源中国
comments: false
date: Thu, 03 Mar 2022 07:25:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0302/154401_IrdS_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Wasmer 2.2 已正式发布。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmer.io%2Fposts%2Fwasmer-2.2" target="_blank">公告称</a>，此版本改进巨大，并将会在很大程度上影响 Web3 和区块链社区。</p> 
<blockquote> 
 <p>Wasmer 是支持 WASI 和 Emscripten 的通用 WebAssembly 运行时，提供基于 WebAssembly 的超轻量级容器，专注于支持在任何平台上运行 WASM 代码：从桌面端到云端、以及 IoT 设备，并且能嵌入在任何编程语言中。</p> 
 <p>Wasmer 凭借其多样化的支持和专注于从通用桌面应用程序到“便携式 ML/AI 应用程序”的领域，目前仍然是领先的 WASM 运行时之一。</p> 
</blockquote> 
<p><strong>Wasmer 2.2 主要新特性</strong></p> 
<p>Wasmer 的 Singlepass 编译器现已支持在 64 位 Arm (AArch64) 上的 Linux 和 macOS 操作系统运行。</p> 
<p>Wasmer 正在为其 Singlepass 编译器提供对 Aarch64 架构的兼容。通过新改版的 Singlepass，Web3 和区块链开发者可以在 Windows、Linux 和 macOS 上<strong>使用 Singepass 高效运行 Wasmer Runtime</strong>。</p> 
<p>Singlepass 是使用 Cranelift 或 LLVM 编译器路径的 Wasmer 编译器替代方案。Singlepass 编译代码的速度十分快，编译性能比 Cranelift 或 LLVM“快几个数量级”，且运行时的性能开销很低。</p> 
<p><strong>Linux x86_64 Benchmarks</strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0302/154401_IrdS_2720166.png" referrerpolicy="no-referrer"></p> 
<p><strong>Linux ARM64 Benchmarks</strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0302/154429_6lZD_2720166.png" referrerpolicy="no-referrer"></p> 
<p><strong>macOS M1 Benchmarks</strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0302/154744_yCYT_2720166.png" referrerpolicy="no-referrer"></p> 
<p>详细性能基准测试结果：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmer.io%2Fposts%2Fwasmer-2.2" target="_blank">https://wasmer.io/posts/wasmer-2.2</a></p> 
<p>Singlepass 的另一个优点是可以避免 JIT “炸弹”。对于使用较旧 Intel/AMD CPU 的用户，Wasmer 2.2 中的 Singlepass 编译器还添加了 SSE 4.2 支持作为其 AVX 路径的替代方案。</p> 
<p>除了 AArch64 的 Singlepass 之外，Wasmer 2.2 的另一个 64 位 Arm 新增功能现在正式支持 Apple 的 M1 处理器。在 AArch64 空间之外，Wasmer 2.2 中有许多错误修复。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Freleases%2Ftag%2F2.2.0" target="_blank">通过GitHub和</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmer.io%2Fposts%2Fwasmer-2.2" target="_blank">Wasmer.io</a>的项目站点。</p> 
<p>除了针对 AArch64 架构的 Singlepass，Wasmer 2.2 另一项和 64 位 ARM 架构相关的新功能是<strong>正式支持 Apple 的 M1 处理器</strong>。此外还包括许多错误修复。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Freleases%2Ftag%2F2.2.0" target="_blank">https://github.com/wasmerio/wasmer/releases/tag/2.2.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            