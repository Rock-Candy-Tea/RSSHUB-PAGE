
---
title: 'Wasmer 3.0 Alpha 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d9f522ac99c682156ac3b2cec0634146254.png'
author: 开源中国
comments: false
date: Tue, 02 Aug 2022 07:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d9f522ac99c682156ac3b2cec0634146254.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Wasmer 3.0<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Freleases%2Ftag%2F3.0.0-alpha" target="_blank">发布</a><span style="background-color:#ffffff; color:#000000">了首个 Alpha 版本。</span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Wasmer 是支持 WASI 和 Emscripten 的通用 WebAssembly 运行时，提供基于 WebAssembly 的超轻量级容器，专注于支持在任何平台上运行 WASM 代码：从桌面端到云端、以及 IoT 设备，并且能嵌入在任何编程语言中。</p> 
 <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-d9f522ac99c682156ac3b2cec0634146254.png" referrerpolicy="no-referrer"></p> 
 <p>Wasmer 凭借其多样化的支持和专注于从通用桌面应用程序到 “便携式 ML/AI 应用程序” 的领域，目前仍然是领先的 WASM 运行时之一。</p> 
</blockquote> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Wasmer 3.0 Alpha 新增了一个 WASIX 实现，其包含完整的网络支持，还提供了用于 WebAssembly 应用程序之间 RPC 的虚拟总线接口。除了上述变化，Wasmer 3.0 还对大量代码进行了重构，引入新的上下文 API，修复 Singlepass 编译器和其他错误，以及其他的 API 变化和增加。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">主要变化</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fpull%2F3035" target="_blank">#3035</a> 新增简易的 "divide by zero" wast 测试，因为现在可以在 singlepass 上正确跟踪 trap 信息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fpull%2F3021" target="_blank">#3021</a> 添加缺失的 Aarch64 重定位（llvm 编译器需要）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fpull%2F3008" target="_blank">#3008</a> 添加一个新的 cargo public-api CI 检查</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fpull%2F2941" target="_blank">#2941</a> 新增 WASIX 实现和针对 WebAssembly 的完整网络支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fpull%2F2952" target="_blank">#2952</a> CI: 添加 make build-wasmer-wasm 测试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fpull%2F2982" target="_blank">#2982</a> 将 rustfmt.toml 文件添加到仓库</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwasmerio%2Fwasmer%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">详情查看 Changelog</a>。</p>
                                        </div>
                                      
</div>
            