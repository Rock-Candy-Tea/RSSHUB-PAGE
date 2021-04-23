
---
title: 'GraalVM 21.1 社区版发布：实验性支持 Java 16'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0423/073225_laFo_4252687.png'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 23:33:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0423/073225_laFo_4252687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GraalVM 21.1 稳定版已发布。GraalVM 是 Oracle 打造的高性能跨语言虚拟机，支持运行 JavaScript、Python 3、Ruby、R、基于 JVM 的语言（如 Java、Scala 和 Kotlin），以及基于 LLVM 的语言，如 C 和 C++。</p> 
<p><img height="277" src="https://static.oschina.net/uploads/space/2021/0423/073225_laFo_4252687.png" width="700" referrerpolicy="no-referrer"></p> 
<p>新版本增加了许多新功能，以及优化性能，主要更新内容包括：</p> 
<ul> 
 <li>实验性支持 Java 16</li> 
 <li>继续进行对 Linux AArch64 的支持，目前处于实验性阶段。GraalVM 的 LLVM Runtime 也增加了实验性的 Linux AArch64 支持</li> 
 <li>Polyglot run-time 默认启用多层编译 (multi-tier compilation) 策略，因为 Oracle 工程师发现多层编译改进了大多数语言的 warmup 效率</li> 
 <li>改进 Java Debug Wire Protocol，包括提供更好的性能。在启用调试功能的情况下，Truffle 上的 Java 性能提升 200 倍</li> 
 <li>对 Ruby 2.7 的更完整支持，以及默认启用多层编译策略，此外还包括性能改进</li> 
 <li>GraalVM for Python 新增 SSL 支持、完全原生支持 POSIX API 后端、支持使用 GIL 的多线程，以及对 HPy Python C API 的支持以提升性能</li> 
 <li>GraalVM for WebAssembly "GraalWASM" 代码运行速度有所提升，并且 WASM 解释器的总体峰值性能提升了 10 倍 。除此之外，还针对 GraalWasm 启动器进行了优化，以及许多其他的改进</li> 
</ul> 
<p>详细更新说明和下载地址访问<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fgraalvm-ce-builds%2Freleases%2Ftag%2Fvm-21.1.0" target="_blank"> release note</a>。</p>
                                        </div>
                                      
</div>
            