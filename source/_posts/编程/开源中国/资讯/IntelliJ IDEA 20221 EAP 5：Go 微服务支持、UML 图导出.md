
---
title: 'IntelliJ IDEA 2022.1 EAP 5：Go 微服务支持、UML 图导出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7ec5afdc693dadf20d0da35e732d4663887.gif'
author: 开源中国
comments: false
date: Wed, 16 Mar 2022 07:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7ec5afdc693dadf20d0da35e732d4663887.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#27282c">IntelliJ IDEA 2022.1 EAP 5 现已推出，该版本包括对 Go 微服务和 .proto 文件的支持、导出 UML 图的能力、增强的文件选择器对话框、可访问性改进等等.</span></p> 
<h3>Go 微服务支持</h3> 
<ul> 
 <li>添加了对 Go 微服务的支持，提供 URL 路径引用、端点、Search Everywhere 和装订线图标等功能。</li> 
 <li>使用这些功能需要在 IntelliJ IDEA Ultimate 中安装 Go 插件，目前仅适用于标准库函数。</li> 
 <li>IntelliJ IDEA Ultimate 现在为 Go 文件中的 HTTP 方法和标头提供补全，每个端点旁边都会出现一个地球图标，如果单击它，IntelliJ IDEA Ultimate 将建议几个选项。</li> 
</ul> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-7ec5afdc693dadf20d0da35e732d4663887.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>还可以使用 <em>Search Everywhere </em>功能在代码中查找端点并导航到它们：请单击<em>导航</em>，然后单击 <em>URL 映射，</em>或使用快捷键<em>⇧ ⌘ \ (Ctrl+Shift+\)，</em>然后输入端点地址以触发代码完成。 </p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-d7ed457b3143a817ab1e6dfa920b59e9c6e.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">还可以在 HTTP 客户端中生成请求——只需单击端点附近的地球图标即可。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e22a6ea4306dd7d458267e844c2dfccde0f.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><em>此外，</em>可以在 <em>Endpoints </em>工具窗口中查看 Go 文件的端点，</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可以从 Endpoints 工具窗口使用 Jump to Source，也可以单击每个单独的端点并直接从 HTTP 客户端选项卡运行请求。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt src="https://oscimg.oschina.net/oscnet/up-cf9ac669427ba5fb3413a4fae5bdd8a3211.gif" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2022%2F02%2F17%2Fgoland-2022-1-eap-3-is-out-with-new-features-for-working-with-microservices%2F" target="_blank">在此博客文章</a>中了解有关 Go 微服务支持的更多信息。</p> 
<h3>Spring Data Mongo 的代码洞察改进</h3> 
<p>引入了许多更新来改善使用 Spring Data MongoDB 的用户体验。IntelliJ IDEA 现在突出显示 JSON 查询，完成运算符和文档字段，并提供从映射实体到 <strong><em>数据库 </em></strong>工具窗口的导航。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-47057e9fe6edb70aff55aaf559022dae81c.png" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-56f7ce377726cd92feb689113162e3cdd52.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3>更好地支持 .proto 文件</h3> 
<p>为 .proto 文件引入了一个新的意图操作：为未解析的消息引用添加了缺失的导入语句，添加缺少的导入语句后， IDE 将提供消息引用的补全建议。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-b2d7b578fae22fcfb07323876cc867581c0.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>gRPC 反射支持</h3> 
<ul> 
 <li>当项目中存在描述 gRPC 服务的 .proto 文件时，IntelliJ IDEA Ultimate 现在为服务名称、方法名称和请求正文选项提供代码补全。更重要的是，现在可以通过装订线图标运行请求。</li> 
 <li>如果项目没有 .proto 文件，但服务器支持 gRPC 反射，你将能够运行请求，并完成服务器运行实例的服务和方法名称。</li> 
</ul> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-946868d703da4ab3f086f42f5134c0eb019.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3>更快的 URL 完成、导航和 Search Everywhere</h3> 
<ul> 
 <li><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改进了处理 Spring 项目时 URL 搜索和完成的性能，现在 IDE 会在进行搜索时显示 URL。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><em>Endpoints 工具窗口中 Speed search </em>的性能也得到了改进，现在 IDE 在搜索端点时可以更快地提供第一批结果。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h3>将 UML 图导出为其他格式</h3> 
<p><span style="background-color:#ffffff; color:#27282c">现在可以将 UML 图导出为 yEd .graphml、JGraph .drawio、Graphviz .dot、带位置的 Graphviz .dot、Mermaid .md、Plantuml 和 IntelliJ IDEA .uml 文件，使得它们与第三方工具兼容。</span></p> 
<p><span style="background-color:#ffffff; color:#27282c"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-2355050f1bbe4c0e796a0802ba7406c8adc.png" width="700" referrerpolicy="no-referrer"></span></p> 
<h2>用户体验<span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span> </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3>更新文件选择器对话框</h3> 
<p style="margin-left:0; margin-right:0; text-align:start">该版本从文件选择器对话框中删除了树，意味着 IDE 在打开时不再计算所有中间目录节点。</p> 
<p style="margin-left:0; margin-right:0; text-align:start">此更改通过防止死胡同路径计算导致的持续挂起，以提高 IDE 的整体性能。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-4187ef884b9776c13439814fdbae3f839ca.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>构建工具</h2> 
<h3>更新 Gradle 的进度条</h3> 
<p style="margin-left:0; margin-right:0; text-align:start">为 Gradle 进程实现了一个确定的进度条，例如下载依赖项和导入工件，允许跟踪文件发生的情况并估计该过程何时完成。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-ba1b5cb9169658e832bd0e15b4d29d90f87.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2>可访问性改进</h2> 
<ul> 
 <li><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为 IntelliJ IDEA 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Faccessibility.html" target="_blank">辅助功能</a>引入了更新和修复，以更好地满足用户的需求。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为了便于在“<em>日志</em>”选项卡中导航，屏幕阅读器现在可以读取分支树的名称和描述，并提供语音提示以使用 <em>Cmd+L </em>浏览其他日志过滤器。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改进了对 macOS 用户的辅助功能支持。此 EAP 版本解决了导致列表元素多次不必要重复的 VoiceOver 问题。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此外，VoiceOver 现在可以读取组合框列表，且修复了在外部显示器上工作时 VoiceOver 光标的错误定位。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h2>插件</h2> 
<ul> 
 <li>该版本从 IDE 中解散了以下插件：Spring Batch、Spring Web Services、Grails、JAX-WS、JSF、Java EE：Batch、WebLogic、WebSphere 和 Jetty。</li> 
 <li>所有版本的 IDE 仍然支持这些插件，唯一的区别是它们需要从 JetBrains Marketplace 安装。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start">以上是该版本的亮点内容，完整的更新列表可可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-104%2FIntelliJ-IDEA-2022.1-EAP-5-%28221.4994.44-build%29-Release-Notes" target="_blank">发行说明</a>中查看。</p>
                                        </div>
                                      
</div>
            