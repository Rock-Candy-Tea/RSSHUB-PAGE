
---
title: 'Gradle 7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-da6afa34782554f8072a083e0c1dadb45ce.png'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 07:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-da6afa34782554f8072a083e0c1dadb45ce.png'
---

<div>   
<div class="content">
                                                                                            <p>Gradle 7.0 现已发布。Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</p> 
<p>该版本默认启用文件系统监视功能，使你的增量构建速度更快；扩展了对使用 Java 16 构建项目的支持；并增加了对在使用 Apple Silicon 处理器（如 M1）的 Mac 上构建的支持。</p> 
<p>同时，此版本还引入了 centralized dependency versions 的功能预览，启用构建验证错误，使你的构建更加可靠，并使其更容易为设置文件创建 convention plugins。且许多孵化中的功能已经晋升为稳定版。具体更新内容如下：</p> 
<h4>性能提升</h4> 
<p><strong>更快的增量构建</strong></p> 
<p>文件系统监视是 Gradle 6.5 中的一项可选功能，在 Gradle 6.7 中被标记为生产就绪。 当启用时，Gradle 会在两次构建之间将它所了解到的文件系统保存在内存中，并在每次构建时跳过从文件系统中读取。这大大减少了确定自上一次构建以来发生了什么变化所需的磁盘 I/O 量。</p> 
<p>现在，在所有支持的平台上，包括最新版本的 Windows、Linux 和 MacOS，都默认启用了这项优化。有关更多详细信息，可参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.0%2Fuserguide%2Fgradle_daemon.html%23sec%3Adaemon_watch_fs" target="_blank">文档</a>。</p> 
<p><strong>Android 项目中更快的增量更改</strong></p> 
<p>此版本包含了对 Android 项目中增量更改的性能改进，特别是那些使用 Jettifier 的项目。例如，与 Gradle 6.8 相比，Santa Tracker Android 项目中的 non-ABI 更改的 assembleDebug 提高了 12%：</p> 
<p><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-da6afa34782554f8072a083e0c1dadb45ce.png" width="462" referrerpolicy="no-referrer"></p> 
<p><strong>忽略空 buildSrc 项目</strong></p> 
<p>Gradle 现在将忽略一个空的 buildSrc 目录，只有在检测到构建文件和/或源文件时才会生成一个 buildSrc.jar。当检测到一个空的 buildSrc 目录时，有两个好处：</p> 
<ul> 
 <li>:buildSrc:* 任务将不会被不必要地执行。</li> 
 <li>空的 buildSrc.jar 不会被添加到 buildcript class path 中，避免了可能造成的 cache misses。</li> 
</ul> 
<h4>新功能和可用性改进</h4> 
<ul> 
 <li>对 Apple Silicon 的原生支持</li> 
 <li>支持 Java 16</li> 
 <li>Centralized dependency versions</li> 
 <li>类型安全的 project accessors</li> 
 <li>Groovy 3 升级</li> 
 <li>Dependency locking 改进</li> 
 <li>在 plugins block 中使用 dynamic 版本</li> 
</ul> 
<p>更多详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.0%2Frelease-notes.html" target="_blank">https://docs.gradle.org/7.0/release-notes.html</a></p>
                                        </div>
                                      
</div>
            