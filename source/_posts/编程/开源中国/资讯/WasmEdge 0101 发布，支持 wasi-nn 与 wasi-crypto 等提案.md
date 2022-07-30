
---
title: 'WasmEdge 0.10.1 发布，支持 wasi-nn 与 wasi-crypto 等提案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4275'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 14:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4275'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2F" target="_blank">WasmEdge</a> 0.10.1 发布，本版本增加了 wasi-nn 与 wasi-crypto 等 WebAssembly 提案，优化了 C API 与 macOS 开发者的开发体验。</p> 
<p>新增 feature:</p> 
<ul> 
 <li>以 plugin 的方式在 Ubuntu 20.04 x86_64 上支持带有 OpenVINO 后端的 WASI-NN 提案。 
  <ul> 
   <li>用户可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fintro%2Fstandard.html" target="_blank">标准扩展状态</a>获取信息。</li> 
   <li>对于使用 OpenVINO 后端启用 WASI-NN 的构建，请在 <code>cmake</code> 中添加 <code>-DWASMEDGE_PLUGIN_WASI_NN_BACKEND="OpenVINO"</code>。</li> 
  </ul> </li> 
 <li>以 plugin 的方式在 Ubuntu 20.04 x86_64、manylinux2014 x86_64 和 manylinux2014 aarch64 上支持 WASI-crypto 提案。 
  <ul> 
   <li>用户可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwasmedge.org%2Fbook%2Fen%2Fintro%2Fstandard.html" target="_blank">标准扩展状态</a>获取信息。</li> 
   <li>对于使用 OpenSSL 1.1 启用 WASI-crypto 的构建，请在 <code>cmake</code> 中添加<code>-DWASMEDGE_PLUGIN_WASI_CRYPTO=ON</code>。</li> 
  </ul> </li> 
 <li>添加了静态工具构建选项。 
  <ul> 
   <li>默认情况下，WasmEdge 工具将依赖于 WasmEdge 共享库。</li> 
   <li>开发者可以添加 <code>-DWASMEDGE_BUILD_STATIC_LIB=On</code> 和 <code>-DWASMEDGE_BUILD_STATIC_TOOLS=On</code> 来构建独立的 WasmEdge CLI 工具。</li> 
  </ul> </li> 
 <li>在 WasmEdge C API 中导出了 <code>WasmEdge_VMContext</code> 的组件。 
  <ul> 
   <li>添加了 <code>WasmEdge_VMGetLoaderContext</code> API，用于在 VM 中检索 <code>WasmEdge_LoaderContext</code> 。</li> 
   <li>添加了 <code>WasmEdge_VMGetValidatorContext</code> API，用于在 VM 中检索 <code>WasmEdge_ValidatorContext</code> 。</li> 
   <li>添加了 <code>WasmEdge_VMGetExecutorContext</code> API，用于在 VM 中检索 <code>WasmEdge_ExecutorContext</code>。</li> 
  </ul> </li> 
 <li>添加了 CLI 工具的 API。 
  <ul> 
   <li>开发者可以使用 <code>WasmEdge_Driver_Compiler</code> API 来触发 WasmEdge AOT 编译工具。</li> 
   <li>开发者可以使用 <code>WasmEdge_Driver_Tool</code> API 来触发 WasmEdge runtime 工具。</li> 
  </ul> </li> 
 <li>支持 WASM <code>threads</code> 提案。 
  <ul> 
   <li>为 WasmEdge C API 中的配置添加了 <code>WasmEdge_Proposal_Threads</code>。</li> 
   <li>用户可以使用 <code>--enable-threads</code> 在 <code>wasmedge</code> 和 <code>wasmedgec</code> 工具中启用提案。</li> 
  </ul> </li> 
 <li>在 MacOS 上支持 LLVM 14。 
  <ul> 
   <li>在 LLVM-14 环境中的 lld 中使用了新的 <code>macho</code>。</li> 
   <li>将 IWYU 提升到 0.18 以与 MacOS 上的 LLVM 14 兼容。</li> 
  </ul> </li> 
 <li>提升 MacOS x86_64 build到 MacOS 11。</li> 
</ul> 
<p>已修复的问题</p> 
<ul> 
 <li>修复了通用 WASM 格式在 MacOS 平台上失败的问题。 
  <ul> 
   <li>开发者可以在MacOS上指定扩展名<code>.wasm</code>作为AOT编译器的通用 WASM 格式输出来开启AOT模式。</li> 
  </ul> </li> 
 <li>修复了带有 LLVM 14 的 MacOS 上的 WasmEdge C API 静态库。 
  <ul> 
   <li>WasmEdge C API 静态库处于实验阶段，不能确保可用。推荐使用共享库。</li> 
  </ul> </li> 
 <li>减少实例化 AOT 编译的 WASM 时的分支缺失。</li> 
</ul> 
<p>更多详情请点击 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWasmEdge%2FWasmEdge%2Freleases%2Ftag%2F0.10.1" target="_blank">WasmEdge 0.10.1 changelog</a></p>
                                        </div>
                                      
</div>
            