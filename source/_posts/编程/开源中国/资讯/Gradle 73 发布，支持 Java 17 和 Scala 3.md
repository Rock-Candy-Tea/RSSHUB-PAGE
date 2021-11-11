
---
title: 'Gradle 7.3 发布，支持 Java 17 和 Scala 3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5199'
author: 开源中国
comments: false
date: Thu, 11 Nov 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5199'
---

<div>   
<div class="content">
                                                                                            <p>Gradle 7.3 版本为 JVM 项目引入了声明性测试套件 API，添加了对使用 Java 17 构建项目的支持，并更新了 Scala 插件以支持 Scala 3。</p> 
<p>Gradle 7.3 具体更新内容如下：</p> 
<h3>升级说明</h3> 
<p>通过更新你的 Wrapper，将你的构建转换为使用 Gradle 7.3。</p> 
<p><code>./gradlew wrapper --gradle-version=7.3</code></p> 
<h3>新功能和可用性改进</h3> 
<ul> 
 <li> <p>支持 Java 17</p> <p>Gradle 现在支持在 Java 17 上运行和构建。在以前的 Gradle 版本中，在 Java 17 上运行 Gradle 会导致一个错误。从 Gradle 7.3 开始，运行 Gradle 本身和用 Java 17 构建 JVM 项目都被完全支持。</p> </li> 
 <li> <p>JVM 项目中的声明性测试套件</p> <p>在测试 Java 和 JVM 项目时，开发者经常需要将测试类分组，将它们组织成可管理的块，这样就可以以不同的频率或在构建管道的不同点上运行它们。</p> <p>以前，正确的测试分组需要彻底了解如何修改和连接 Gradle 中的各种领域对象，如 SourceSets、配置和任务。如果你想把测试分成不同的组，你需要了解这些独立的部分如何相互作用。</p> <p>在 Gradle 7.3 中，JVM Test Suite Plugin 简化了这种测试组的创建。</p> </li> 
 <li> <p>支持 Scala 3</p> <p>Scala 插件允许用户使用 Gradle 和 Zinc 增量编译器来编译他们的 Scala 代码。Scala 插件现在可以编译 Scala 3 的代码了。所有现有的配置选项在最新的语言版本下仍然可以使用。</p> <p>最新版本的 Scala 3 在保持与大部分现有 Scala 2 代码兼容的同时，也带来了众多功能。</p> </li> 
 <li> <p>探索 <code>gradle init</code> 的新行为</p> <p>当你使用 <code>gradle init</code> 初始化一个新的 Gradle 项目时，Gradle 现在会询问你是否想在构建中尝试新的但不稳定的功能。开发者可以在生成新项目时，通过运行 <code>gradle init --incubating</code> 来询问这一行为。</p> <p>目前，用这个选项生成的构建只启用 Test Suites，但其他新的 API 或行为可能会在它们引入时被添加。</p> </li> 
 <li> <p>取消了对别名（alias）的限制</p> <p>在以前的 Gradle 版本中，不可能用后缀 <code>plugin</code>、 <code>version</code>和其他受限制的关键字来声明别名。在这个 7.3 版本中，这些限制现在被取消了。</p> </li> 
</ul> 
<h3>可靠性改进</h3> 
<ul> 
 <li> <p>更强大的文件系统观察</p> <p>当运行增量构建时，Gradle 需要了解自上一次构建以来文件系统上有什么变化。为了做到这一点，它尽可能地依赖操作系统的文件系统事件。</p> <p>在一些罕见的环境中，这些事件可能不够可靠，并且会导致 Gradle 忽略一些变化。为了防止这种情况，Gradle 现在在启用基于文件系统事件的优化之前，会验证文件系统事件是否及时交付。</p> </li> 
 <li> <p>允许将单个文件复制到包含不可读文件的目录中</p> <p>现在可以在 <code>Copy</code>任务上使用 <code>Task.doNotTrackState()</code>方法，强制 Gradle 忽略目标目录中的内容。</p> </li> 
 <li> <p>配置缓存中的输入规范化支持</p> <p>输入规范化现在能被实验性配置缓存正确跟踪。当配置缓存启用时，任务的最新检查现在会考虑规范化规则，从而产生更快的构建。</p> </li> 
 <li> <p>插件开发改进</p> <p>使用 Build Init 插件初始化新的插件项目也可以从 <code>--incubating</code>选项中受益。</p> </li> 
</ul> 
<h3>Tooling <strong>改进</strong></h3> 
<ul> 
 <li> <p>文件下载进度事件</p> <p>当构建下载许多文件或非常大的文件时（例如在解决依赖关系时），由于缺乏任何日志或控制台输出，Gradle 可能会被认为出现了无响应。</p> <p>7.3 版本增加了新的事件，在文件被下载时通知 IDE。这允许 IDE 在 Gradle 运行时和 IDE 导入/同步时显示更好的进度信息。</p> </li> 
 <li> <p>安全性改进</p> <p><code>ant</code> 和 <code>common-compress</code> 捆绑库都已更新，以解决报告的漏洞。</p> </li> 
</ul> 
<h3><strong>修复的问题</strong></h3> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18632" target="_blank">#18632</a>] - Test Suite 无法添加版本目录项目</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18622" target="_blank">#18622</a>] - KMP 中找不到名称为 'test' 的 SourceSet</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18598" target="_blank">#18598</a>] - 修复小的 JvmTestSuitePlugin 文档格式问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F9095" target="_blank">#9095</a>] - 为任务完全禁用缓存和最新检查</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18324" target="_blank">#18324</a>] - gradle 依赖于一个不安全的第三方 JAR 包，其中包含 CVE 漏洞</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18239" target="_blank">#18239</a>] - 支持 TestNG 和 Spock 作为测试框架选项</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.3%2Frelease-notes.html" target="_blank">https://docs.gradle.org/7.3/release-notes.html</a></p>
                                        </div>
                                      
</div>
            