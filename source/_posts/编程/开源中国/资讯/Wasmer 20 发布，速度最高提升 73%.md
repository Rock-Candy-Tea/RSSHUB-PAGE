
---
title: 'Wasmer 2.0 发布，速度最高提升 73%'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8015'
author: 开源中国
comments: false
date: Sat, 19 Jun 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8015'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wasmer 是支持 WASI 和 Emscripten 的 WebAssembly 运行时，提供基于 WebAssembly 的超轻量级容器，其可以在任何地方运行：从桌面端到云端、以及 IoT 设备，并且能嵌入在任何编程语言中。</p> 
<p>Wasmer 2.0 的新内容：</p> 
<p>SIMD</p> 
<ul> 
 <li>SIMD 是指单指令、多数据（single instruction, multiple data）。简而言之，SIMD 使一条指令可以同时对许多数据进行操作。在 Wasmer 2.0 中引入 SIMD，为许多不同的用例提供了更高性能的数据级并行性。创建机器学习、视频（转码、编码、解码......等）、图像处理、3D 物理或图形应用的用户应该能看到性能的大幅提升。</li> 
</ul> 
<p>引用类型</p> 
<ul> 
 <li> <p>Wasmer 2.0 的另一个突出特点是包含了引用类型。对于不熟悉的人来说，引用类型允许 Wasm 模块与主机环境或多个 Wasm 模块之间引用和共享特定类型的信息。</p> <p>这允许使用更简单的代码与来自主机的 Wasm 模块进行交互，并且是启用接口类型等未来提案的关键功能。</p> </li> 
</ul> 
<p>性能的改进</p> 
<ul> 
 <li>当使用浮点数操作时，LLVM 的运行速度提高了约 56%；</li> 
 <li>函数调用现在快得多，尽可能避免内核交互；</li> 
 <li>由于新的后端架构，Cranelift 的运行速度提高了 48%；</li> 
 <li>反序列化速度提升 73%；</li> 
</ul> 
<p>这些引擎有了新的名字：</p> 
<ul> 
 <li>JIT → Universal (默认)；</li> 
 <li>Native → Dylib（Dynamic Library 的首字母缩写）；</li> 
 <li>Object File → StaticLib（Static Library 的首字母缩写）；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Freleases%2Ftag%2F2.0.0" target="_blank">https://github.com/wasmerio/wasmer/releases/tag/2.0.0</a></p>
                                        </div>
                                      
</div>
            