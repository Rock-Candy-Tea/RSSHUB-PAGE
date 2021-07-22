
---
title: 'GraalVM 21.2 社区版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cd3325de448efaf7ea4e381bfd0bb63a86a.png'
author: 开源中国
comments: false
date: Thu, 22 Jul 2021 07:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cd3325de448efaf7ea4e381bfd0bb63a86a.png'
---

<div>   
<div class="content">
                                                                                            <p>GraalVM 21.2 稳定版已发布。GraalVM 是 Oracle 打造的高性能跨语言虚拟机，支持运行 JavaScript、Python 3、Ruby、R、基于 JVM 的语言（如 Java、Scala 和 Kotlin），以及基于 LLVM 的语言，如 C 和 C++。</p> 
<p>此外，GraalVM 在编程语言之间具有高效的互操作性，并可提前将 Java 应用程序编译为本地可执行文件，以加快启动时间，降低内存开销。</p> 
<p>GraalVM 社区发行版包括：</p> 
<ul> 
 <li>带有 GraalVM 编译器的 Java runtime</li> 
 <li>带有 GraalVM JavaScript 解释器的 Node.js runtime</li> 
 <li>LLVM runtime</li> 
 <li>开发者监控和调试工具</li> 
</ul> 
<p>GraalVM 环境可以通过 GraalVM Updater 工具使用可选的可用组件进行扩展，例如 Native Image、Ruby、R、Python、LLVM 工具链、WebAssembly 和 Espresso。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cd3325de448efaf7ea4e381bfd0bb63a86a.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fgraalvm%2Fgraalvm-21-2-ee2cce3b57aa" target="_blank">GraalVM 21.2</a> 的主要变化包括改进原生镜像的可用性、更新编译器、针对 JavaScript、Python 和 Ruby 等语言的改进，以及在 GitHub 仓库提供 GraalVM 文档等。</p> 
<ul> 
 <li>为原生镜像(Native Image)发布了新的官方 Gradle 和 Maven 插件，并提供了初步的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjunit.org%2Fjunit5%2F" target="_blank">JUnit 5</a> 测试支持。这些插件将使构建、测试和运行 Java 应用程序作为原生可执行文件变得更加容易，并且原生的 JUnit 支持允许 JVM 库通过 GraalVM 原生映像运行其测试套件。</li> 
 <li>改进了 Graal 编译器以允许使用超过 64 个循环的 AOT 方法。</li> 
 <li>添加了一种尝试将写入移出循环的优化，称为“Write Sinking”。Write Sinking 是一项默认禁用的实验性功能。可通过<code>-Dgraal.OptWriteMotion=true</code>启用它。</li> 
 <li>新增适用于 AArch64 CPU 架构的 GraalVM 发行版，并启用了更多功能，例如 Ruby runtime 和 Java on Truffle (Espresso)。</li> 
</ul> 
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.graalvm.org%2Frelease-notes%2F21_2%2F" target="_blank">release note</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fgraalvm-ce-builds%2Freleases%2Ftag%2Fvm-21.2.0" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            