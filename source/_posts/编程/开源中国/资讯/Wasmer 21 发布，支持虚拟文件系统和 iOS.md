
---
title: 'Wasmer 2.1 发布，支持虚拟文件系统和 iOS'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5585'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5585'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wasmer 2.1 已正式发布。Wasmer 是支持 WASI 和 Emscripten 的通用 WebAssembly 运行时，提供基于 WebAssembly 的超轻量级容器，专注于支持在任何平台上运行 WASM 代码：从桌面端到云端、以及 IoT 设备，并且能嵌入在任何编程语言中。</p> 
<p>半年前发布的 <a href="https://www.oschina.net/news/146635/wasmer-2-0-released" target="_blank">Wasmer 2.0<span> </span></a>是开源 WASM 实现的一个重大进步，<span style="background-color:#ffffff; color:#121212">Wasmer 2.1 则是新的主要迭代版本。</span></p> 
<p><span style="background-color:#ffffff; color:#121212">更新亮点：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>引入 Wasmer JS</li> 
 <li>引入虚拟文件系统</li> 
 <li>支持 iOS</li> 
 <li>在 Windows 中提供 Singlepass 支持</li> 
 <li>支持 LLVM ARM64 & LLVM 13</li> 
 <li>更快的 Singlepass 编译</li> 
 <li>可重现和确定性的构建</li> 
 <li>集成新语言：Lisp 和 Crystal</li> 
</ul> 
<p>Wasmer 2.1 引入了一个虚拟文件系统，在基于 JavaScript 的环境且提供有限的原生文件系统支持的情况下，该特性尤其有用。Wasmer 2.1 的另一个显著特点是，其 Singlepass 编译器现在的代码编译速度提高了 10 倍。Wasmer 2.1 的编译器基础架构也已从 LLVM 11 迁移到 LLVM 13，并且现在还支持 LLVM AArch64。</p> 
<p>Wasmer 2.1 还通过将 WASM 文件预编译到 Dylib，并在运行时使用 Dylib 引擎加载来添加对 iOS 的支持，以绕过 Apple App Store 对 JIT 编译器的审核要求。同样在平台方面，Wasmer 的 Singlepass 编译器现在支持 Windows。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmer.io%2Fposts%2Fwasmer-2.1" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            