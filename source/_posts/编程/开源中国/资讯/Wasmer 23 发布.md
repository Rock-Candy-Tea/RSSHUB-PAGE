
---
title: 'Wasmer 2.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5964'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5964'
---

<div>   
<div class="content">
                                                                                            <p>Wasmer 官方宣布在推出下一个大版本 Wasmer 3.0 之前先发布了一个 2.3 版本。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Wasmer 是支持 WASI 和 Emscripten 的通用 WebAssembly 运行时，提供基于 WebAssembly 的超轻量级容器，专注于支持在任何平台上运行 WASM 代码：从桌面端到云端、以及 IoT 设备，并且能嵌入在任何编程语言中。</p> 
 <p style="margin-left:0; margin-right:0">Wasmer 凭借其多样化的支持和专注于从通用桌面应用程序到 “便携式 ML/AI 应用程序” 的领域，目前仍然是领先的 WASM 运行时之一。</p> 
</blockquote> 
<p><span><span><span><span style="color:#231044"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Wasmer 2.3 版本包括的一些更新内容有：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>一个新的 stack switcher（corosensei），用于处理从 Host language 到 Wasm world 的 crossing</li> 
 <li>在 Singlepass 编译器中添加了对 EH frame 生成的支持以帮助调试</li> 
 <li>通过 Singlepass 支持 Dylib 引擎</li> 
 <li>Wasmer 编译为 Wasm/WASI</li> 
 <li>将 Cranelift 升级到 0.82</li> 
</ul> 
<p><strong>新的 Stack switcher - Corosensei </strong></p> 
<p>受 Rust 1.59 及其对内联汇编的原生支持的启发，<span><span><span><span style="color:#231044"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Wasmer 开发团队</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>意识到他们可以利用这个新特性来支持新的 stack switcher 的实现。从而开发了一个新的库：corosensei，其测试结果表明：在最新的苹果 M1 芯片中，Switching stack 的中位数仅为约 3.8ns。而在 AMD Ryzen 中，只用了约 4.2ns。“这可能是你在 Rust 中能找到的最快的 stack switcher 的实现了 (甚至可能是在 C 语言中）。”</p> 
<p>它甚至支持 linked backtraces 和 panic propagation。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span style="color:#1a202c"><span><span><span><span><span><span><span><span><span><span><span><span><span>在 Singlepass 中更好地支持 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>native backtraces <span><span><span><span style="color:#1a202c"><span><span><span><span><span><span><span><span><span><span><span><span><span>和 dylib 执行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#231044">在 Wasmer 2.3 中改进了对 Singlepass 的 unwinding 支持，以提供更好的回溯，并使 Singlepass 与 Dylib 引擎一起运行成为可能。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Wasmer 编译为 Wasm/WASI</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">此举旨在为了使 WebAssembly 的编译完全在 WebAssembly 中完成，以便在未来的产品中进行应用。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>将 Cranelift 升级到 0.82</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">更新了 Wasmer 以使用最新版本的 Cranelift。因此，Wasmer 2.3 完全支持 SIMD 指令，并使用 ISLE 使用新的实验性编译策略。ISLE 是由 Cranelift 团队创建的用于指令选择和机器代码降低的新领域特定语言 (DSL)。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmer.io%2Fposts%2Fwasmer-2.3" target="_blank">查看官方公告</a>。</p>
                                        </div>
                                      
</div>
            