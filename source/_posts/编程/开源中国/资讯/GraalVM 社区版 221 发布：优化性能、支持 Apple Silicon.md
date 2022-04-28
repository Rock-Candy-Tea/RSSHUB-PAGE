
---
title: 'GraalVM 社区版 22.1 发布：优化性能、支持 Apple Silicon'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0eb8c023df7e26e654379008b13586adbc2.png'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 07:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0eb8c023df7e26e654379008b13586adbc2.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#121212">GraalVM 社区版 22.1 已发布。</span></p> 
<blockquote> 
 <p>GraalVM 是一个高性能的 JDK 发行版。它旨在加速用 Java 和其他 JVM 语言编写的应用程序的执行，同时还为 JavaScript、Python、基于 LLVM 的语言（如 C 和 C++）以及许多其他流行编程语言提供运行时。此外，GraalVM 为编程语言之间提供了高效互操作性，并将 Java 应用程序提前编译为本机可执行文件，从而加快启动时间并降低内存开销。</p> 
</blockquote> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0eb8c023df7e26e654379008b13586adbc2.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="background-color:#ffffff; color:#121212">主要更新内容</span></strong></p> 
<ul> 
 <li>通过 darwin-aarch64 target 对基于 Arm 的 Apple Silicon 提供支持，目前处于试验性阶段。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-121a78625f14ec48d59baa02eebe717c9fd.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>优化代码库体积，以减少本地可执行文件(native executables)的大小。 同时还优化了 native-image 生成器的性能，以及减少内存占用。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-da05af1dc32a21f160134d34c253e0a1098.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bbfbcd0c9d0256ce31e4f5035be640cdc74.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>GraalVM 的 JavaScript 支持已经实现了 Intl.NumberFormat v3、Array Grouping、Temporal 和其他特性的提案。</li> 
 <li>GraalVM 的 Ruby 支持已经实现了 Ruby 3 关键字参数语义、减少了 C 语言扩展的内存占用，以及其他改进。</li> 
 <li>GraalVM 的 Python 支持现在可以处理模块冻结 ()，从而使 Python REPL 的启动速度提高 30%，内存减少 40%。</li> 
 <li>GraalVM 的 LLVM 运行时支持增加了对 C/C++ 线程本地存储的支持、新的互操作 API (interop API)，以及其他改进。</li> 
 <li>Truffle 上的 Java 在单线程模式下实现了显式引用处理，因此可以在更多情况下使用以防止资源泄漏</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fgraalvm-ce-builds%2Freleases%2Ftag%2Fvm-22.1.0" target="_blank">下载地址</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fgraalvm%2Fgraalvm-22-1-developer-experience-improvements-apple-silicon-builds-and-more-b7ac9a0f6066" target="_blank">发布公告</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            