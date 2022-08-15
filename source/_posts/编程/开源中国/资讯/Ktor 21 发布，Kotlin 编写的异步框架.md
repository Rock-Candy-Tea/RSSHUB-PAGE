
---
title: 'Ktor 2.1 发布，Kotlin 编写的异步框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0815/070525_CODP_4937141.png'
author: 开源中国
comments: false
date: Mon, 15 Aug 2022 07:06:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0815/070525_CODP_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Ktor 是一个异步框架，用于创建微服务、Web 应用等。从头到尾都是用 Kotlin 编写的。</p> 
<p>Ktor 2.1.0 近日正式发布，除了新的功能和错误修复之外，还特别发布了三个新工具的测试版。让我们逐一看看这些工具。</p> 
<h2>本地命令行工具</h2> 
<p>Ktor 提供了两种方法来简化创建新的应用程序模板 —— IntelliJ IDEA 或 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fstart.ktor.io" target="_blank">start.ktor.io</a>。</p> 
<p>我们现在通过提供一个在 Kotlin/Native 中构建的命令行工具来扩展它。除了为你生成一个 Ktor 服务器应用程序外，如果你的系统没有安装 JDK，它还负责下载一个 JDK。</p> 
<p>要创建一个新的项目，只需输入 :</p> 
<p><code>ktor generate &#123;projectName&#125;</code></p> 
<p><img alt height="194" src="https://static.oschina.net/uploads/space/2022/0815/070525_CODP_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>一旦完成（如果需要的话，还包括下载 JDK/Gradle），它就会构建这个项目</p> 
<p><img alt height="131" src="https://static.oschina.net/uploads/space/2022/0815/070537_4qOS_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>剩下的就是运行它了</p> 
<p><img alt height="126" src="https://static.oschina.net/uploads/space/2022/0815/070547_Y40e_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>该工具目前可用于 macOS 和 Linux，将在之后提供 Windows 的支持。</p> 
<h2>Yeoman 生成器</h2> 
<p>与命令行客户端类似，Ktor 也添加了 Yeoman 支持。如果你不熟悉 Yeoman，它是一个命令行工具，允许你为各种项目轻松生成脚手架。</p> 
<p>如果你没有安装 Yeoman，请确保你首先安装 node/npm（与 14.0.0 以上版本兼容）。一旦你有了这个，你可以运行。</p> 
<p><code>npm install -g yo</code></p> 
<p>This installs yeoman globally on your system. Next step is to install the Ktor generators:</p> 
<p>这将在你的系统上全局安装 Yeoman。下一步是安装 Ktor 生成器。</p> 
<p><code>npm install -g generator-ktor</code></p> 
<p>一旦安装完毕，你可以简单地创建一个新的项目目录，并使用以下命令运行生成器</p> 
<p><code>yo ktor</code></p> 
<h2><strong>Gradle Deployment</strong> 插件</h2> 
<p>Ktor 的目标之一是使整个开发尽可能地顺利和愉快。当然，人们很少会开发一个应用程序而不去部署它。</p> 
<p>为此，最近发布了一个新的 Gradle 部署插件的测试版（注意，使用向导新创建的项目将默认添加这个插件）。现在你可以在 Gradle 文件中定义你希望你的 Ktor 应用程序如何被部署。</p> 
<p>虽然它目前只适用于 Gradle，但计划也提供 Maven 支持。</p> 
<h2><strong>YAML Configuration</strong> 支持</h2> 
<p>除了使用代码或 HOCON 配置 Ktor 应用程序外，你现在还可以使用 YAML，它也可用于 Ktor 本地服务器应用程序。以下面的 HOCON 配置为例：</p> 
<pre><code>ktor &#123;
    deployment &#123;
        port = 8080
    &#125;
    application &#123;
        modules = [ com.example.ApplicationKt.module ]
    &#125;
&#125;
</code></pre> 
<p>在 YAML 中，相当于：</p> 
<pre><code>ktor:
    deployment:
        port: 8080
    application:
        modules:
            - com.example.ApplicationKt.module
</code></pre> 
<h2>其他</h2> 
<ul> 
 <li>将 Kotlin 更新到 1.7.0</li> 
 <li>Darwin：允许设置自定义 NSURLSession</li> 
 <li>支持在调用时设置缓存选项</li> 
 <li>Java 引擎：允许配置 HTTP 版本</li> 
 <li>将 jteVersion 从 2.0.3 升级到 2.1.2</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fktor%2F2022%2F08%2F12%2Fktor-2-1-0-released-and-it-comes-with-goodies%2F" target="_blank">https://blog.jetbrains.com/ktor/2022/08/12/ktor-2-1-0-released-and-it-comes-with-goodies/</a></p>
                                        </div>
                                      
</div>
            