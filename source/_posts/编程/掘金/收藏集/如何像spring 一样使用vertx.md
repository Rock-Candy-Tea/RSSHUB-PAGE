
---
title: '如何像spring 一样使用vertx'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c3a8d2d8eda~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 25 Apr 2020 06:37:54 GMT
thumbnail: 'https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c3a8d2d8eda~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache html"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">如何像spring 一样使用vertx</h1>
<h2 data-id="heading-1">什么是vertx</h2>
<p>EclipseVert.x是事件驱动和非阻塞的。这意味着您的应用程序可以使用少量的内核线程处理大量并发。Vert.x让你的应用程序可以用最少的硬件扩展,Vert.x与多种语言一起使用，包括Java、Kotlin、JavaScript、Groovy、Ruby和Scala。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c3a8d2d8eda~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c3c5af49169~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
技术无好坏,只有适合不适合.<p></p>
<p>Vertx，是一个基于JVM、轻量级、高性能的应用平台，非常适用于移动端后台、互联网、企业应用架构。</p>
<p>Vertx，基于Netty全异步通信，并扩展出了很多有用的特性。</p>
<p>Vertx，是基于事件总线设计的高性能架构，保证应用中不同部分以一种非堵塞的线程安全方式通讯。</p>
<p>Vertx，是借鉴Erlang和Akka架构设计，能充分利用多核处理器性能并实现高并发编程需求的框架。</p>
<p><strong>Vertx特点</strong>：</p>
<ul>
<li>
<p><strong>支持多种编程语言</strong></p>
<p>目前支持Java、JavaScript、Ruby、Python、Groovy、Clojure、Ceylon等，并提供友好的API接口。以上技术栈的工程师可以非常容易的学习和使用Vert.x 架构。</p>
</li>
<li>
<p><strong>异步无锁编程</strong></p>
<p>经典的多线程编程模型能满足很多Web开发场景，但随着移动互联网并发连接数的猛增，多线程并发控制模型性能难以扩展，同时要想控制好并发锁需要较高的技巧，目前Reactor异步编程模型开始跑马圈地，而Vert.x就是这种异步无锁编程的一个首选。</p>
</li>
<li>
<p><strong>对各种IO的丰富支持</strong></p>
<p>目前Vert.x的异步模型已支持TCP、UDP、FileSystem、DNS、EventBus、Sockjs等，基本满足绝大多数系统架构需求。</p>
</li>
<li>
<p><strong>分布式消息传输</strong></p>
<p>Vert.x基于分布式Bus消息机制实现其Actor模型，我们的业务逻辑如果依赖其他Actor则通过Bus简单的将消息发送出去就可以了。EventBus事件总线，可以轻松编写分布式解耦的程序，具有很好的扩展性。</p>
<p>EventBus也是Vert.x架构的灵魂所在。</p>
</li>
<li>
<p><strong>生态体系日趋成熟</strong></p>
<p>Vertx归入Eclipse基金会门下，异步驱动已经支持了Postgres、MySQL、MongoDB、Redis等常用组件，并且有若干Vertx在生产环境中的应用案例。</p>
</li>
</ul>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c44076db37b~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<ul>
<li>
<p><strong>Vertx是轻量级的</strong></p>
<p>vertx的核心代码包只有650kB左右，同时提供丰富的扩展插件，满足各类需求。</p>
</li>
<li>
<p><strong>模块化</strong></p>
<p>Vertx本身内置强大的模块管理机制,当你写完一个Vert.x业务逻辑的时候,你可以将其打包成module,然后部署到基于Maven的仓库里,与现有主流的开发过程无缝结合。</p>
</li>
<li>
<p><strong>支持WebSocket</strong></p>
<p>支持WebSocket协议兼容SockJS ， 可以非常方便的实现web前端和服务后端长连接通信，是轻量级web聊天室应用首选解决方案。</p>
</li>
<li>
<p><strong>使用简单</strong></p>
<p>这里的简单意味着你编写的代码是完全基于异步事件的,类似Node.JS,与此同时.你不需要关注线程上的同步,与锁之类的概念,所有的程序都是异步执行并且通信是无阻塞的。</p>
</li>
<li>
<p><strong>良好的扩展性</strong></p>
<p>因为基于Actor模型,所以你的程序都是一个点一个点的单独在跑,一群点可以组成一个服务,某个点都是可以水平扩展,动态替换,这样你的程序,基本就可以达到无限制的水平扩展。</p>
</li>
<li>
<p><strong>高并发性</strong></p>
<p>vert.x是一个事件驱动非阻塞的异步编程框架，你可以在极少的核心线程里占用最小限度的硬件资源处理大量的高并发请求。</p>
</li>
<li>
<p><strong>基本概念</strong></p>
<p>handler: 事件处理器
event loop:事件循环(线程)(同netty)
verticle: Vert.x 基本组件,模块。
worker: 工作线程
event bus: 事件总线</p>
</li>
</ul>
<p>我们看下vertx 的java开发流程</p>
<pre><code lang="scala" class="hljs language-scala copyable">
<span class="hljs-keyword">import</span> io.vertx.core.<span class="hljs-type">AbstractVerticle</span>;
public <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Server</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbstractVerticle</span> </span>&#123;
  public void start() &#123;
    vertx.createHttpServer().requestHandler(req -> &#123;
      req.response()
        .putHeader(<span class="hljs-string">"content-type"</span>, <span class="hljs-string">"text/plain"</span>)
        .end(<span class="hljs-string">"Hello from Vert.x!"</span>);
    &#125;).listen(<span class="hljs-number">8080</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c46a13224db~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>但同时vertx也有他的缺点,就拿vertx-web相比springmvc来说,vertx更加灵活,但同时也需要开发人员weba原生开发有更深刻的了解,包括各种请求返回头的添加,以及各种拦截器,自定义消息转换等的处理,都需要开发人员自行配置,这显然是大部分开发人员所不愿意的,所以导致了vertx目前并不怎么流行,但这些并不影响一个框架本身的魅力.当然还有很多轻量级的web开发框架,jfinal,play等等小众框架.</p>
<h2 data-id="heading-2">什么是vertx-web-springmvc?</h2>
<p>vertx-web-springmvc  是基于vertx -web 类似springmvc的开发风格的web框架,方便原spring开发人员无缝迁移</p>
<ul>
<li>springmvc 风格开发</li>
<li>统一异常处理</li>
<li>拦截器</li>
<li>统一结果处理</li>
<li>springmvc 风格模板渲染</li>
<li>静态资源</li>
<li>支持spring容器</li>
<li>跨域支持</li>
</ul>
<p><strong>springmvc 风格注解介绍</strong></p>
<table>
<thead>
<tr>
<th>注解</th>
<th>用法</th>
</tr>
</thead>
<tbody>
<tr>
<td>TemplateBody</td>
<td>类似springmvc的@ ResponseBody标记模板渲染 阻塞执行,配合 VertxTemplateEngine标记</td>
</tr>
<tr>
<td>ResponseBody</td>
<td>类似springmvc的 @ResponseBody 标记消息转换 (依赖 MessageConverter)阻塞执行,配合 VertxMessageConverter标记</td>
</tr>
<tr>
<td>RouteHandler</td>
<td>类似springmvc的 @Controller</td>
</tr>
<tr>
<td>RouteMapping</td>
<td>类似springmvc的 @RequestMapping</td>
</tr>
<tr>
<td>Interceptor</td>
<td>vertx 拦截器标记</td>
</tr>
<tr>
<td>RouterAdvice</td>
<td>类似springmvc的 @ControllerAdvice</td>
</tr>
<tr>
<td>ExceptionHandler</td>
<td>类似springmvc的 @ExceptionHandler 异常处理</td>
</tr>
</tbody>
</table>
<h2 data-id="heading-3">vertx-web-springmvc 开发示例</h2>
<ul>
<li>json,模板渲染,vertx-web 原生开发示例</li>
</ul>
<pre><code lang="typescript" class="hljs language-typescript copyable">package com.<span class="hljs-property">taoyuanx</span>.<span class="hljs-property">vertxdemo</span>.<span class="hljs-property">withspring</span>.<span class="hljs-property">web</span>;

<span class="hljs-keyword">import</span> com.<span class="hljs-property">taoyuanx</span>.<span class="hljs-property">springmvc</span>.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">anno</span>.<span class="hljs-property">route</span>.<span class="hljs-property">ResponseBody</span>;
<span class="hljs-keyword">import</span> com.<span class="hljs-property">taoyuanx</span>.<span class="hljs-property">springmvc</span>.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">anno</span>.<span class="hljs-property">route</span>.<span class="hljs-property">RouteHandler</span>;
<span class="hljs-keyword">import</span> com.<span class="hljs-property">taoyuanx</span>.<span class="hljs-property">springmvc</span>.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">anno</span>.<span class="hljs-property">route</span>.<span class="hljs-property">RouteMapping</span>;
<span class="hljs-keyword">import</span> com.<span class="hljs-property">taoyuanx</span>.<span class="hljs-property">springmvc</span>.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">core</span>.<span class="hljs-property">template</span>.<span class="hljs-property">TemplateBody</span>;
<span class="hljs-keyword">import</span> io.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">Handler</span>;
<span class="hljs-keyword">import</span> io.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">http</span>.<span class="hljs-property">HttpMethod</span>;
<span class="hljs-keyword">import</span> io.<span class="hljs-property">vertx</span>.<span class="hljs-property">core</span>.<span class="hljs-property">json</span>.<span class="hljs-property">JsonObject</span>;
<span class="hljs-keyword">import</span> io.<span class="hljs-property">vertx</span>.<span class="hljs-property">ext</span>.<span class="hljs-property">web</span>.<span class="hljs-property">RoutingContext</span>;
<span class="hljs-keyword">import</span> org.<span class="hljs-property">springframework</span>.<span class="hljs-property">stereotype</span>.<span class="hljs-property">Component</span>;

<span class="hljs-keyword">import</span> java.<span class="hljs-property">util</span>.<span class="hljs-property">concurrent</span>.<span class="hljs-property">TimeUnit</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@author</span> <span class="hljs-variable">dushitaoyuan</span>
 * <span class="hljs-doctag">@date</span> 2020/4/21
 */</span>
<span class="hljs-meta">@RouteHandler</span>(value = <span class="hljs-string">"api"</span>)

<span class="hljs-meta">@Component</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">RouteHandlerDemo</span> &#123;
    <span class="hljs-meta">@RouteMapping</span>(value = <span class="hljs-string">"demo"</span>, method = <span class="hljs-title class_">HttpMethod</span>.<span class="hljs-property">GET</span>)
    <span class="hljs-keyword">public</span> <span class="hljs-title class_">Handler</span><<span class="hljs-title class_">RoutingContext</span>> <span class="hljs-title function_">handle</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> ctx -> &#123;
            ctx.<span class="hljs-title function_">response</span>().<span class="hljs-title function_">end</span>(<span class="hljs-string">"demo"</span>);
            <span class="hljs-title class_">System</span>.<span class="hljs-property">out</span>.<span class="hljs-title function_">println</span>(<span class="hljs-string">"demo"</span>);
        &#125;;
    &#125;

    <span class="hljs-meta">@RouteMapping</span>(value = <span class="hljs-string">"blockDemo"</span>, method = <span class="hljs-title class_">HttpMethod</span>.<span class="hljs-property">GET</span>, blocked = <span class="hljs-literal">true</span>)
    <span class="hljs-keyword">public</span> <span class="hljs-title class_">Handler</span><<span class="hljs-title class_">RoutingContext</span>> <span class="hljs-title function_">blockHande</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> ctx -> &#123;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-title class_">TimeUnit</span>.<span class="hljs-property">SECONDS</span>.<span class="hljs-title function_">sleep</span>(<span class="hljs-number">3</span>);
                <span class="hljs-title class_">System</span>.<span class="hljs-property">out</span>.<span class="hljs-title function_">println</span>(<span class="hljs-string">"blockDemo"</span>);
                ctx.<span class="hljs-title function_">response</span>().<span class="hljs-title function_">end</span>(<span class="hljs-string">"blockDemo"</span>);
            &#125; <span class="hljs-keyword">catch</span> (<span class="hljs-title class_">InterruptedException</span> e) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">RuntimeException</span>(e);
            &#125;

        &#125;;
    &#125;
  
    <span class="hljs-meta">@RouteMapping</span>(value = <span class="hljs-string">"jsonMessage"</span>, method = <span class="hljs-title class_">HttpMethod</span>.<span class="hljs-property">GET</span>)
    <span class="hljs-meta">@ResponseBody</span>
    <span class="hljs-keyword">public</span> <span class="hljs-title class_">JsonObject</span> <span class="hljs-title function_">jsonMessage</span>(<span class="hljs-params">RoutingContext ctx</span>) &#123;
        <span class="hljs-title class_">JsonObject</span> jsonObject=<span class="hljs-keyword">new</span> <span class="hljs-title class_">JsonObject</span>();
        jsonObject.<span class="hljs-title function_">put</span>(<span class="hljs-string">"spring json"</span>,<span class="hljs-string">"json"</span>);
        <span class="hljs-keyword">return</span> jsonObject;
    &#125;

    <span class="hljs-meta">@RouteMapping</span>(value = <span class="hljs-string">"template"</span>, method = <span class="hljs-title class_">HttpMethod</span>.<span class="hljs-property">GET</span>)
    <span class="hljs-meta">@TemplateBody</span>
    <span class="hljs-keyword">public</span> <span class="hljs-title class_">String</span> <span class="hljs-title function_">template</span>(<span class="hljs-params">RoutingContext ctx,JsonObject dataModel</span>)
    &#123;
        dataModel.<span class="hljs-title function_">put</span>(<span class="hljs-string">"hello"</span>,<span class="hljs-string">"dushitaoyuan say hi to you! thymeleaf"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-string">"index.html"</span>;
    &#125;

    <span class="hljs-meta">@RouteMapping</span>(value = <span class="hljs-string">"template2"</span>, method = <span class="hljs-title class_">HttpMethod</span>.<span class="hljs-property">GET</span>)
    <span class="hljs-meta">@TemplateBody</span>
    <span class="hljs-keyword">public</span> <span class="hljs-title class_">String</span> <span class="hljs-title function_">template2</span>(<span class="hljs-params">RoutingContext ctx,JsonObject dataModel</span>)
    &#123;
        dataModel.<span class="hljs-title function_">put</span>(<span class="hljs-string">"hello"</span>,<span class="hljs-string">"dushitaoyuan say hi to you! freemarker"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-string">"index.ftl"</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>
<p>异常处理</p>
<pre><code lang="less" class="hljs language-less copyable"><span class="hljs-variable">@RouterAdvice</span>
<span class="hljs-variable">@Component</span>
public class RouteAdviceDemo &#123;
    <span class="hljs-variable">@ExceptionHandler</span>(value = MyException.class)
    public Handler<RoutingContext> handle() &#123;
        <span class="hljs-selector-tag">return</span> <span class="hljs-selector-tag">ctx</span> <span class="hljs-selector-tag">-</span>> &#123;
            <span class="hljs-selector-tag">MyException</span> <span class="hljs-selector-tag">failure</span> = (MyException) <span class="hljs-selector-tag">ctx</span><span class="hljs-selector-class">.failure</span>();
            <span class="hljs-selector-tag">ResponseUtil</span><span class="hljs-selector-class">.responseJson</span>(ctx, <span class="hljs-number">500</span>, new JsonObject().put(<span class="hljs-string">"errorMsg"</span>,failure.getMessage()));
        &#125;;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></li>
<li>
<p>自定义模板引擎</p>
</li>
</ul>
<pre><code lang="ini" class="hljs language-ini copyable">    ThymeleafTemplateEngine <span class="hljs-attr">thymeleafTemplateEngine</span> = ThymeleafTemplateEngine.create(serverConfig.getVertx())<span class="hljs-comment">;</span>
            FreeMarkerTemplateEngine <span class="hljs-attr">freeMarkerTemplateEngine</span> = FreeMarkerTemplateEngine.create(serverConfig.getVertx())<span class="hljs-comment">;</span>
            springMvcRouterHandler.registVertxTemplateEngine("myTemplate", "templates/", "html", thymeleafTemplateEngine)<span class="hljs-comment">;</span>
            springMvcRouterHandler.registVertxTemplateEngine("myTemplate2", "templates/", "ftl", freeMarkerTemplateEngine)<span class="hljs-comment">;</span>
           
<span class="copy-code-btn">复制代码</span></code></pre><ul>
<li>
<p>自定义拦截器</p>
<pre><code lang="typescript" class="hljs language-typescript copyable"><span class="hljs-meta">@Interceptor</span>(value = <span class="hljs-string">"/api/*"</span>)
<span class="hljs-meta">@Component</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">RouteInterceptorDemo</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">IRequestInterceptor</span>, <span class="hljs-title class_">Order</span> &#123;


    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">boolean</span> <span class="hljs-title function_">pre</span>(<span class="hljs-params">RoutingContext routingContext</span>) &#123;
        <span class="hljs-title class_">System</span>.<span class="hljs-property">out</span>.<span class="hljs-title function_">println</span>(<span class="hljs-string">"pre1"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">boolean</span> <span class="hljs-title function_">after</span>(<span class="hljs-params">RoutingContext routingContext</span>) &#123;
        <span class="hljs-comment">/**
         * end 后 不执行
         */</span>
        <span class="hljs-title class_">System</span>.<span class="hljs-property">out</span>.<span class="hljs-title function_">println</span>(<span class="hljs-string">"after1"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> int <span class="hljs-title function_">order</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">100</span>;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></li>
<li>
<p>自定义json解析(默认内置)</p>
<pre><code lang="typescript" class="hljs language-typescript copyable"><span class="hljs-meta">@VertxMessageConverter</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">JsonMessageConverter</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">MessageConverter</span> &#123;


    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-built_in">boolean</span> <span class="hljs-title function_">support</span>(<span class="hljs-params"><span class="hljs-built_in">Object</span> source</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-title class_">Handler</span><<span class="hljs-title class_">RoutingContext</span>> <span class="hljs-title function_">convertTo</span>(<span class="hljs-params"><span class="hljs-built_in">Object</span> source</span>) &#123;
        <span class="hljs-keyword">return</span> ctx -> &#123;
            <span class="hljs-keyword">if</span> (source <span class="hljs-keyword">instanceof</span> <span class="hljs-title class_">JsonObject</span>) &#123;
                <span class="hljs-title class_">ResponseUtil</span>.<span class="hljs-title function_">responseJson</span>(ctx, <span class="hljs-title class_">HttpResponseStatus</span>.<span class="hljs-property">OK</span>.<span class="hljs-title function_">code</span>(), ((<span class="hljs-title class_">JsonObject</span>) source).<span class="hljs-title function_">encode</span>());
                <span class="hljs-keyword">return</span>;
            &#125;
            <span class="hljs-title class_">ResponseUtil</span>.<span class="hljs-title function_">responseJson</span>(ctx, <span class="hljs-title class_">HttpResponseStatus</span>.<span class="hljs-property">OK</span>.<span class="hljs-title function_">code</span>(), <span class="hljs-title class_">JSON</span>Util.<span class="hljs-title function_">toJsonString</span>(source));
        &#125;;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></li>
</ul>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/25/171b1c4a028b61c9~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp" loading="lazy" referrerpolicy="no-referrer"><figcaption></figcaption></figure><p></p>
<p>代码仓库地址:<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdushitaoyuan%2Fvertx-web-springmvc" title="https://github.com/dushitaoyuan/vertx-web-springmvc" ref="nofollow noopener noreferrer">github.com/dushitaoyua…</a></p>
<p>官方例子仓库:<a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvert-x3%2Fvertx-examples" title="https://github.com/vert-x3/vertx-examples" ref="nofollow noopener noreferrer">github.com/vert-x3/ver…</a></p>
</div>  
</div>
            