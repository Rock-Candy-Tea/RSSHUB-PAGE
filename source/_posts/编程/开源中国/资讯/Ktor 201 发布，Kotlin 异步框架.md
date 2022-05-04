
---
title: 'Ktor 2.0.1 发布，Kotlin 异步框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-09fc9cdaa692b6ae7b3a03221d561f6a34f.png'
author: 开源中国
comments: false
date: Wed, 04 May 2022 08:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-09fc9cdaa692b6ae7b3a03221d561f6a34f.png'
---

<div>   
<div class="content">
                                                                                            <p>Ktor 是使用 Kotlin 构建异步服务器和客户端的 Web 框架，上个月发布了重要的新版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fktor%2F2022%2F04%2F11%2Fktor-2-0-released%2F" target="_blank"> 2.0</a>，并于近日发布了首个补丁更新 2.0.1。</p> 
<p><span style="background-color:#ffffff; color:#27282c">Ktor 2.0 引入了许多新功能，以及破坏性变化，官方称这让他们有机会执行一些维护工作并摆脱遗留决策。尽管存在重大变更，但官方表示已尽可能降低其影响，并提供了有助于自动迁移的实用工具。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-09fc9cdaa692b6ae7b3a03221d561f6a34f.png" referrerpolicy="no-referrer"></p> 
<p><strong>Ktor 2.0 新特性</strong></p> 
<h3>Ktor 服务器</h3> 
<p><strong>简化的可扩展性</strong></p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">Ktor 提供的所有功能均以插件架构构建，“功能”也因此更名为“插件”。对于某些人来说，架构模型会难以理解。2.0 大幅简化了可扩展性 API，使插件更易创建。</p> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">看看下面 1.x 的 API 代码</p> 
<pre><code>companion object Feature : ApplicationFeature<ApplicationCallPipeline, CustomHeader.Configuration, CustomHeader> &#123;
    override val key = AttributeKey<CustomHeader>("CustomPlugin")
    override fun install(pipeline: ApplicationCallPipeline, configure: Configuration.() -> Unit): CustomHeader &#123;
       val configuration = Configuration().apply(configure)

       val feature = CustomHeader(configuration)

       pipeline.intercept(ApplicationCallPipeline.Call) &#123;

            feature.intercept(this)
        &#125;

       return feature
    &#125;
&#125;</code></pre> 
<p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">到了 2.0 中</p> 
<div style="margin-left:0; margin-right:0; text-align:left"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <pre><code>val myCustomPlugin = createApplicationPlugin("CustomPlugin") &#123;
    onCall &#123;

    &#125;

    onCallReceive &#123;

    &#125;

    onCallRespond &#123;

    &#125;
&#125;</code></pre> 
   <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">大多数现有插件都已转换为使用新 API，并已覆盖大多数情景。 有关详情，请参见 `CustomHeader` 插件从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fktorio%2Fktor-documentation%2Fblob%2F2.0.0%2FcodeSnippets%2Fsnippets%2Fcustom-plugin-base-api%2Fsrc%2Fmain%2Fkotlin%2Fcom%2Fexample%2Fplugins%2FCustomHeader.kt" target="_blank">旧</a> API 到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fktorio%2Fktor-documentation%2Fblob%2F2.0.0%2FcodeSnippets%2Fsnippets%2Fcustom-plugin%2Fsrc%2Fmain%2Fkotlin%2Fcom%2Fexample%2Fplugins%2FCustomHeaderPlugin.kt" target="_blank">新</a> API 的转换，以及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fktor.io%2Fdocs%2Fcustom-plugins.html" target="_blank">插件开发文档</a>。</p> 
   <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">据官方介绍，他们在可扩展性方面还有更多计划，包括用于从市场轻松发布和使用插件的工具！</p> 
   <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Native 支持</strong></p> 
   <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">在服务器端，除了 GraalVM（从 1.6 开始就已支持）之外，现在还支持 Kotlin/Native，这意味着独立服务器应用程序上有了两种选择。</p> 
   <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">关于 Kotin/Native 支持，目前仅限于使用 CIO 作为引擎，开发团队将继续在性能领域推进工作。建议使用新的 Kotlin/Native 内存模型。</p> 
   <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>其他服务器改进</strong></p> 
   <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">对 Ktor 服务器进行了一系列较小的改进，包括随机端口支持</p> 
   <pre><code>fun main() &#123;
    embeddedServer(Netty, port = 0) &#123;
        configureRouting()
    &#125;.start(wait = true)
&#125;</code></pre> 
   <div style="margin-left:0; margin-right:0; text-align:left"> 
    <div style="margin-left:0; margin-right:0"> 
     <div style="margin-left:0; margin-right:0"> 
      <div> 
       <p>以及改进的测试 API、类型安全路由、XML 序列化、插件的子路由以及 60 多个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissues%2FKTOR%3Fq%3D%2523Server%2520Target%2520release%3A%25202.0.0%2520%2523Resolved%2520" target="_blank">错误修正和其他功能</a>。</p> 
       <h3>Ktor 客户端</h3> 
       <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>简化的 API</strong></p> 
       <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">API 得到进一步简化。在 Ktor 客户端中，引入了新的 API 来处理常见 HTTP 请求</p> 
       <pre><code>val result = client.post("http://127.0.0.1:$port/") &#123;

&#125;
result.bodyAsText()</code></pre> 
       <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">新版本已经摆脱了通用的 <em>post<T>, get<T></em> 方法。 现在，所有内容都返回一个 `HttpResponse`，可供访问正文（使用 `bodyAsText`、`bodyAsChannel`）以及标题。</p> 
       <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>重试</strong></p> 
       <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">增加了对重试的内置支持，包括重试之间的时间调整</p> 
       <pre><code>val client = HttpClient(CIO) &#123;
    install(HttpRequestRetry) &#123;
        maxRetries = 5
        retryIf &#123; request, response ->
            !response.status.isSuccess()
        &#125;
        retryOnExceptionIf &#123; _, cause ->
            cause is NetworkError
        &#125;
        delayMillis &#123; retry ->
            retry * 3000L
        &#125; // retries in 3, 6, 9, etc. seconds
    &#125;
&#125;</code></pre> 
       <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>内容协商</strong></p> 
       <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">如果您一直在服务器中使用内容协商，您应该已经很熟悉这一功能了。 本质上，它就是客户端与服务器协商可以请求和提供的不同类型内容的能力。 在此之前，它的协商方面仅适用于服务器。 现在，客户端也提供了此功能。</p> 
       <div style="margin-left:0; margin-right:0; text-align:left"> 
        <div style="margin-left:0; margin-right:0"> 
         <div style="margin-left:0; margin-right:0"> 
          <div> 
           <pre><code>val client = HttpClient(CIO) &#123;
    install(ContentNegotiation) &#123;
    &#125;
&#125;</code></pre> 
           <p>这个插件有效取代了 `JsonFeature`。</p> 
          </div> 
         </div> 
        </div> 
       </div> 
       <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>其他客户端改进</strong></p> 
       <p style="color:#27282c; margin-left:0; margin-right:0; text-align:start">除了上述内容外，客户端还包括用于身份验证的快捷 API（例如 `basic()` 和 `bearer()` 辅助函数）、请求级别的侦听器、新的指标插件、XML 序列化，以及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissues%2FKTOR%3Fq%3D%2523Client%2520%2520Target%2520release%3A%25202.0.0%2520%2523Resolved%2520" target="_blank">许多错误修正和其他功能</a>。</p> 
       <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fktor.io%2Fchangelog%2F2.0%2F" target="_blank">更多内容查看 Changelog</a>。</p> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            