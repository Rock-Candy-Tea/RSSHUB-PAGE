
---
title: 'IntelliJ IDEA 2022.2 发布首个 Beta 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-619149a6f56f48380911ae827cb73346f09.png'
author: 开源中国
comments: false
date: Sat, 09 Jul 2022 07:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-619149a6f56f48380911ae827cb73346f09.png'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.2 首个公开测试版已发布。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-619149a6f56f48380911ae827cb73346f09.png" referrerpolicy="no-referrer"></p> 
<p><strong>主要变化</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F06%2Fintellij-idea-2022-2-eap-7%2F" target="_blank">增强远程开发</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F06%2Fintellij-idea-2022-2-eap-7%2F" target="_blank">体验</a></strong></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">远程开发功能将 IDE 拆分为本地和远程组件，IDE 本身作为后端服务安装在远程服务器上用于加载项目。同时瘦客户端（thin client）在本地运行并提供完整的工作 UI。这两个组件通过 SSH 连接，在远程服务器进行繁重任务的处理，进而提供流畅的本地体验。 关于远程开发的更多内容可查看 JetBrains 中国的</span><a href="https://my.oschina.net/u/5494143/blog/5332935">博客<span> </span></a><span style="background-color:#ffffff; color:#333333">。</span></p> 
<p><img src="https://oscimg.oschina.net/oscnet/b6f155b5-73d4-402f-9111-f916984dc312.png" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>支持 Spring 6 和 Spring Boot 3 的特性</strong></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#27282c">IntelliJ IDEA 2022.2 完全支持 Spring 6 和 Spring Boot 3 的新特性，包括新的<span> </span></span><em>@AutoConfiguration </em><span style="background-color:#ffffff; color:#27282c">类和<span> </span></span><em>@ConfigurationProperties </em><span style="background-color:#ffffff; color:#27282c">类。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-88f3d8db55184a034f4d3ff537f869599f3.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-2cce3aeb3847621fa0916953647e14288ed.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>支持使用快捷键全局更改字体大小</strong></li> 
</ul> 
<p>新版本<span style="background-color:#ffffff; color:#333333">版本引入了可更改所有编辑器字体大小的键盘快捷键， 要放大字体，按 ⌃⇧. /Alt+Shift+</span><strong style="color:#333333">.<span> </span></strong><span style="background-color:#ffffff; color:#333333">；要缩小字体，按 ⌃⇧,/Alt+Shift+Comma。</span></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-c64a7e1b432983d9c81d1636b9afbf36afb.gif" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>支持在 JSON、YAML 和 .properties 字符串值中启用可点击的 URL</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>JSON、YAML 和 .properties 文件现在具有在以 http:// 和 https:// 开头的值内自动插入 Web 引用的功能。 用户</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可以轻松地在 Web 浏览器中一键打开这些链接，也可以在 HTTP 客户端中从 Context Actions 菜单（Alt + Enter / Option + ⏎）生成请求。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bad4d94bb081369da23afc9562052028fd7.gif" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>新增用于 Java 的实验性 GraalVM 原生调试器</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>IntelliJ IDEA 2022.2 支持调试原生 GraalVM 镜像二进制文件，可以将调试器附加到任何基于 GraalVM 的可执行文件，或使用附加的调试器启动应用程序。它将为 Maven/Gradle 项目自动创建相应的运行配置。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>请注意，这是实验性功能，需要安装 GraalVM 的开发版本和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplugins.jetbrains.com%2Fplugin%2F19237-graalvm-native-debugger" target="_blank">插件</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-c641c1c750f91f63e32c94276ae678abe32.png" width="700" referrerpolicy="no-referrer"></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5ad395a86ceb6dfd2ca93ed8826ecfffde9.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-33db071e7e06c223a62ef2778499fdf516d.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>改进对 bean 验证注解的支持</strong></li> 
</ul> 
<p>IntelliJ IDEA 2022.2 现在为 Java 和 Kotlin 的 Bean Validation 注释中的消息属性提供 references 并支持 folding。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-1dd53662e39f679f24ee581aa1976657472.png" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>支持 Groovy 集成查询 </strong></li> 
 <li><strong>升级内置的 Kubernetes 和 Docker 版本</strong></li> 
 <li><strong><em>运行当前文件 </em>功能支持运行和调试单个文件，而无需专门的运行配置</strong></li> 
 <li><strong>支持导入受信任的 SSL 证书</strong></li> 
 <li><strong>改进 HTTP 客户端</strong></li> 
 <li><strong>从 JBR11 切换到 JBR17</strong></li> 
 <li><strong>改进 Java 的代码检查和代码补全功能</strong></li> 
 <li><strong>增强的 IntelliJ IDEA 配置文件</strong></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F07%2Fintellij-idea-2022-2-beta%2F" target="_blank">详细更新说明查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            