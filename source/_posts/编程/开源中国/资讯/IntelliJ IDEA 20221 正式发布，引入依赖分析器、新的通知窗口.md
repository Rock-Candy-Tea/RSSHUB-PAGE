
---
title: 'IntelliJ IDEA 2022.1 正式发布，引入依赖分析器、新的通知窗口'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0321/074211_uC5c_5430600.png'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 08:02:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0321/074211_uC5c_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.1 正式发布了，该版本的重点功能是：引入了 <em>Dependency Analyzer </em>以促进依赖关系管理和冲突解决，一个更新的 <em>New Project </em>向导来优化新项目的启动过程，以及 <em>Notifications </em>通知工具窗口，它提供了一种新的、简化的方式来接收来自 IDE 的通知。2022.1 版本还包括许多其他值得注意的改进，下面摘录部分新功能作介绍。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">关键更新</h2> 
<ul> 
 <li> <h4 style="margin-left:0; margin-right:0; text-align:left"><em>依赖分析器 （Dependency Analyzer）</em></h4> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为了促进依赖管理和冲突解决，IntelliJ IDEA 实现了<em>依赖分析器</em>，它提供项目和子项目中使用的所有依赖项（包括传递性依赖项）的广泛信息。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这个新功能允许轻松检测冲突的依赖关系并解决问题，比如可以过滤掉相同的依赖项，并查看它们在不同库中的存在，还可以快速浏览依赖项，以正确构建配置。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074211_uC5c_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>增强的 <em>新项目 </em>向导</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">重新设计了<em>新项目 </em>向导界面，以简化创建新项目的过程。可以快速启动一个空项目；使用 Java、Kotlin、Groovy 和 JavaScript 的预配置选项；或者有更复杂的项目，请使用<em>生成器。</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-8979d97d5e9cb2b30cdb0c01531d7a126eb.gif" width="700" referrerpolicy="no-referrer"></em></p> 
<ul> 
 <li> <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的<em>通知 </em>工具窗口</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> </li> 
</ul> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span><span><span style="color:rgba(25, 25, 28, 0.7)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span>事件<em>日志</em>实例已替换为新的 <em>通知 </em>工具窗口，更清楚地突出重要和有用的建议和通知，并将它们组织在专用工具窗口中。有关更多详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F01%2Fintellij-idea-2022-1-eap-1%2F%23New_Notifications_tool_window" target="_blank">博客文章</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <p style="margin-left:0; margin-right:0"><span><span><span><span><span><span><span><span style="color:rgba(25, 25, 28, 0.7)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-5a032ea1c9fd1a07752c732f4cc751bdcfa.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:start">用户体验</h2> 
<ul> 
 <li> <h3 style="margin-left:0px; margin-right:0px; text-align:left">新建项目向导中的 Maven Archetype 优化</h3> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">作为新建项目向导的 UI 改造的一部分，IntelliJ IDEA 重新设计了 Maven Archetype 项目生成器，2022.1 版本在浏览原型时引入了“键入时搜索”功能，以及在模块创建期间管理原型目录的能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-420b6f0066a16eccf25377cd223407dbf79.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#27282c">此外，还可以按原型输入所需的属性：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#27282c"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-b1426130c021697657318452915797cf939.png" width="700" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li> <h3 style="margin-left:0; margin-right:0; text-align:left">均匀拆分选项卡</h3> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">IntelliJ IDEA 2022.1 <span style="color:#27282c">可以在编辑器选项卡之间平均分配工作空间，使它们具有相同的宽度。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074257_C9x6_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3 style="margin-left:0; margin-right:0; text-align:left">将 UML 图导出为其他格式</h3> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#27282c">现在可以将 UML 图导出为 yEd .graphml、JGraph .drawio、Graphviz .dot、带位置的 Graphviz .dot、Mermaid .md、Plantuml 和 IntelliJ IDEA .uml 文件，使得它们与第三方工具兼容。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#27282c"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-2355050f1bbe4c0e796a0802ba7406c8adc.png" width="700" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li> <h3 style="margin-left:0; margin-right:0; text-align:left">更新了<span> </span><em>结构搜索和替换<span> </span></em>对话框</h3> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">重新设计了<em>结构搜索和替换</em>对话框，提供所有模板的列表，以便更轻松地在它们之间导航。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074220_S9cT_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>安全</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li> <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span>包检查器插件</span></span></span></span></h3> </li> 
</ul> 
<p>ntelliJ IDEA 2022.1 现在可以通过检查 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcheckmarx.com%2F" target="_blank">Checkmarx SCA 数据库</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2F" target="_blank">国家漏洞数据库</a>，来检测项目中使用的 Maven 和 Gradle 依赖项中的漏洞。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-ae99c607345c0f68a2d8eb03e20f5f78580.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>Java 支持</h2> 
<ul> 
 <li> <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>支持 Java 18 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> </li> 
</ul> 
<div style="margin-left:0px; margin-right:0px; text-align:start"> 
 <p style="margin-left:0; margin-right:0">IntelliJ IDEA 2022.1 支持 2022 年 3 月发布的 Java 18 的新功能。IDE 现在支持代码片段、开关表达式的模式匹配更改等功能。有关详细信息，请参阅此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F03%2Fjava-18-features-support%2F%3F_gl%3D1*6wf1f9*_ga*MjA4MTU3MzE1OC4xNjM0ODU3MzQ1*_ga_V0XZL7QHEB*MTY0OTgwNTQ3NS40LjEuMTY0OTgwNjMwMy4yMw..%26_ga%3D2.58852333.1145425053.1649805475-2081573158.1634857345" target="_blank">博客文章</a>。</p> 
 <p style="margin-left:0; margin-right:0"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-6b0d34ae78b26b6ad0ae8172d3bf2c57674.png" width="700" referrerpolicy="no-referrer"></p> 
 <ul> 
  <li> <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Java反编译器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> </li> 
 </ul> 
 <div style="margin-left:0px; margin-right:0px; text-align:start"> 
  <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:rgba(25, 25, 28, 0.7)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span>Java 反编译器现在与 Java 17 版本更兼容。它支持现代语言构造函数，例如密封类型和模式匹配，具有更好的字符串反编译切换功能，提供类型注释并检测公共常量。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
  <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:rgba(25, 25, 28, 0.7)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-22e15a0bae707bcd5fc631f7f011656c905.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
  <p style="margin-left:0; margin-right:0"> </p> 
  <ul> 
   <li> <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更好的 JUnit 5 支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> </li> 
  </ul> 
  <div style="margin-left:0px; margin-right:0px; text-align:start"> 
   <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:rgba(25, 25, 28, 0.7)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span>添加了对 JUnit 5.7 中引入的新功能的支持，包括对<code>@EnabledIf/DisabledIf</code>、<code>@NullSource/EmptySource</code>和<code>@TempDir</code>注释的支持。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
   <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:rgba(25, 25, 28, 0.7)"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-badd32c0ba4110a396b990166bcd7b1c9cb.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
   <h3 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><em>使用 try/catch </em>模板更新 Surround</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
   <p>更新后的<em>带有 try/catch</em>模板的 Surround 现在重新抛出包装到 RuntimeException 中的异常，而不是吞下它。</p> 
   <p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-3bd2ac97427c6e72126a7818288ff1f551f.gif" width="700" referrerpolicy="no-referrer"></p> 
   <h2>Kotlin 支持</h2> 
   <p>IntelliJ IDEA 2022.1 支持 Kotlin 1.6.20，因此最新的 Kotlin 语言功能，例如支持并行编译、上下文接收器原型以及跨所有 Kotlin 目标的更好的代码共享，现在都可以在 IDE 中使用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2022%2F04%2Fkotlin-1-6-20-released%2F" target="_blank">在此博客文章</a>中了解有关新 Kotlin 更新的更多 信息。</p> 
   <ul> 
    <li> <h3 style="margin-left:0; margin-right:0; text-align:left">改进了 Kotlin 的 IDE 性能</h3> </li> 
   </ul> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">优化了包索引，大大提高了 IDE 在执行代码完成、突出显示和与参考搜索等相关操作时的速度，在代码更改后发生的重新索引案例的数量和范围也有所减少。</p> 
  </div> 
 </div> 
</div> 
<h2><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>框架和技术</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Go 微服务支持</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>添加了对 Go 微服务的支持，提供 URL 路径引用、端点、Search Everywhere 和装订线图标等功能。使用这些功能需要在 IntelliJ IDEA Ultimate 中安装 Go 插件，目前仅适用于标准库函数。</li> 
 <li>IntelliJ IDEA Ultimate 现在为 Go 文件中的 HTTP 方法和标头提供补全，每个端点旁边都会出现一个地球图标，如果单击它，IntelliJ IDEA Ultimate 将建议几个选项。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-7ec5afdc693dadf20d0da35e732d4663887.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Spring Data Mongo 的代码洞察改进</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">引入了许多更新来改善使用 Spring Data MongoDB 的用户体验。IntelliJ IDEA 现在突出显示 JSON 查询，完成运算符和文档字段，并提供从映射实体到 <strong><em>数据库 </em></strong>工具窗口的导航。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-47057e9fe6edb70aff55aaf559022dae81c.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-56f7ce377726cd92feb689113162e3cdd52.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">更好地支持 .proto 文件</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为 .proto 文件引入了一个新的意图操作：为未解析的消息引用添加了缺失的导入语句，添加缺少的导入语句后， IDE 将提供消息引用的补全建议。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-b2d7b578fae22fcfb07323876cc867581c0.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">gRPC 反射支持</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>当项目中存在描述 gRPC 服务的 .proto 文件时，IntelliJ IDEA Ultimate 现在为服务名称、方法名称和请求正文选项提供代码补全。更重要的是，现在可以通过装订线图标运行请求。</li> 
 <li>如果项目没有 .proto 文件，但服务器支持 gRPC 反射，你将能够运行请求，并完成服务器运行实例的服务和方法名称。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-946868d703da4ab3f086f42f5134c0eb019.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:var(--rs-typography-color-hard,#19191c)"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Kubernetes 支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Kubernetes</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">编辑集群上的资源</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">现在可以从编辑器选项卡中修改从集群加载的资源。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-575e05287021b8d88deac8f265c976afe4a.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">kubectl 的自定义路径</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果 kubectl 不在标准位置，现在可以手动配置路径。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-8fcc6ca200a51ea83e64afd2d4dfaef73e5.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">转发端口 </h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">该版本为 pod 添加了端口转发功能。要转发端口，可以使用工具栏上的图标或选择上下文菜单项。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-bbd237f5630441cbcf2a6de552d58980f60.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">服务视图中的 <em>描述资源操作</em></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em>“服务</em>”视图中的所有资源都有一个新的“<em>描述资源”操作，</em>可以从上下文菜单中调用它或使用工具栏按钮。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-0a75c4a75d5a00d67d655e25f90d6393a68.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持集群中的<em>事件</em></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">集群事件现在显示在<span> </span><em>服务<span> </span></em>视图的单独节点中，提供有关系统中最近事件的数据。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-41e69659009f2eece845952339e8dec11aa.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">要查看特定 pod 的事件，请在其上面调用<span> </span><em>Describe Resource<span> </span></em>并在操作结果中 查找<span> </span><em>Events 部分</em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-48af28fd3bb2bbdbf8782eb3548e1455352.png" width="700" referrerpolicy="no-referrer"></em></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为 werf.yaml 和相关 Helm 模板文件 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwerf.io%2F" target="_blank">https://werf.io</a><span> </span>) 引入了有限的编辑器支持，包括代码补全功能、检查和快速修复建议、重构/重命名 .<span> </span><em>Values.werf.image.*</em>，以及一些字段的验证，如<span> </span><em>boolean<span> </span></em>和<span> </span><em>int</em>。  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-f061e9f7be0e12ea28c82f1c3c5e1c8a4e1.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-cbdea67533f0cd278c902bb42f160452ab9.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">对 Helm 的导入子值支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持通过<span> </span><em>import-values<span> </span></em>设置导入子值，这些设置影响模板中内置对象的完成/导航。尚未提供对 import-values 字段的增强编辑器支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-20829152d1418cb227b345e3bc4855f5c45.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#27282c">请注意，Kubernetes 功能仅适用于 IntelliJ IDEA Ultimate，并且需要安装插件。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">构建工具</h2> 
<ul> 
 <li> <h3 style="margin-left:0; margin-right:0; text-align:left">更新 Gradle 的进度条</h3> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">为 Gradle 进程实现了一个确定的进度条，例如下载依赖项和导入工件，允许跟踪文件发生的情况并估计该过程何时完成。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-ba1b5cb9169658e832bd0e15b4d29d90f87.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">此版本还包含大量更新项，详情可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fidea%2Fwhatsnew%2F%23web-development" target="_blank">更新公告</a>中细阅。</p>
                                        </div>
                                      
</div>
            