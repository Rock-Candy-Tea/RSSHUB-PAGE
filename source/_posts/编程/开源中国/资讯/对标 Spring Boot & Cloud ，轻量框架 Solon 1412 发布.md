
---
title: '对标 Spring Boot & Cloud ，轻量框架 Solon 1.4.12 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1360'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 08:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1360'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h4 style="text-align:start">快速了解Solon的材料：</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5053423">《Solon 生态插件清单》</a>，目前已有100多个生态插件</p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4784513">《Solon 框架入门》</a></p> 
<h4 style="text-align:start">所谓更小：</h4> 
<p style="text-align:start">内核0.1m，最小的接口开发单位0.2m（相较于 Dubbo、Springboot 的依赖包，小到可以乎略不计）</p> 
<h4 style="text-align:start">所谓更快：</h4> 
<p style="text-align:start">本机http helloworld测试，Qps可达12万之多。可参考：《<a href="https://gitee.com/noear/helloworld_wrk_test">helloworld_wrk_test</a>》</p> 
<h4 style="text-align:start">所谓更自由：(代码操控自由)</h4> 
<pre style="text-align:start"><code class="language-java"><em>// 除了注解模式之外，还可以按需手动</em>
<em>//</em>
<em>//手动获取配置（Props 为 Properties 增强版）</em>
Props db = Solon.cfg().getProp(<span style="color:#50a14f">"db"</span>);

<em>//手动获取容器里的Bean</em>
UserService userService = Aop.get(UserService.<span style="color:#a626a4">class</span>);

<em>//手动监听http post请求</em>
Solon.global().post(<span style="color:#50a14f">"/user/update"</span>, x-> userService.updateById(x.paramMap()));

<em>//手动添加个RPC服务</em>
Solon.global().add(<span style="color:#50a14f">"/rpc/"</span>, HelloService.<span style="color:#a626a4">class</span>, <span style="color:#c18401">true</span>);

<em>//手动获取一个RPC服务消费端</em>
HelloService helloService = Nami.builder().create(HelloService.<span style="color:#a626a4">class</span>);

<em>//手动为容器添加组件</em>
Aop.wrapAndPut(DemoService.<span style="color:#a626a4">class</span>);
</code></pre> 
<h4 style="text-align:start">本次版本主要变化：</h4> 
<h3 style="text-align:start">1、增加新的插件适配</h3> 
<ul> 
 <li>添加 opentracing-solon-plugin 插件。可快速对接所有支持 opentracing 的链路跟踪产品。下面以 Jaeger 对接为例：</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> &#123;
    <span style="color:#4078f2">@Bean</span>
    <span style="color:#a626a4">public</span> Tracer <span style="color:#4078f2">tracer</span>() <span style="color:#a626a4">throws</span> TTransportException &#123;
        Reporter reporter = <span style="color:#a626a4">new</span> RemoteReporter.Builder()
                .withSender(<span style="color:#a626a4">new</span> UdpSender(AGENT_HOST, AGENT_PORT, <span style="color:#986801">0</span>))
                .withFlushInterval(<span style="color:#986801">10</span>)
                .build();

        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> JaegerTracer.Builder(Solon.cfg().appName())
                .withReporter(reporter)
                .withExpandExceptionLogs()
                .withSampler(<span style="color:#a626a4">new</span> ConstSampler(<span style="color:#a626a4">true</span>)).build();
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">2、优化 Nami 内部结构（不影响外部调用）</h3> 
<ul> 
 <li>优化 Nami Filter；改为链式过滤；并添加 Invocation 做为配套</li> 
 <li>拆分 Nami.Builder 为独立的 NamiBuilder 类</li> 
 <li>取消 Decoder, Encoder, Channel 对 Filter 的继承；改为更明确的 pretreatment 预处理接口</li> 
 <li>移动 Result 到 nami 一级包目录</li> 
 <li>简化 Naimi 的附件模式。改由 NamiAttachment 直接操控</li> 
</ul> 
<p style="text-align:start">总体来说，是简化和增强了 Nami 的过滤及附件能力。例：</p> 
<pre style="text-align:start"><code class="language-java"><em>//过滤能力</em>
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">NamiFilterAdapter</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Filter</span> &#123;    <em>//这是Nami的过滤器接口</em>
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> Result <span style="color:#4078f2">doFilter</span>(Invocation inv) <span style="color:#a626a4">throws</span> Throwable &#123;
        inv.headers.put(<span style="color:#50a14f">"token"</span>,<span style="color:#50a14f">"1"</span>);
        System.out.println(<span style="color:#50a14f">"我给 Nami 加了个头信息!"</span>);
        <span style="color:#a626a4">return</span> inv.invoke();
    &#125;
&#125;

<em>//附件能力</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Demo</span> &#123;
    <span style="color:#4078f2">@NamiClient</span>
    HelloService helloService;

    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span>() &#123;
        <em>//添加附件：token=aaa （最终会做为 header 传给 server）</em>
        NamiAttachment.put(<span style="color:#50a14f">"Token"</span>,<span style="color:#50a14f">"5643c10c-87c3-4b7e-bd26-30cf2456aad8"</span>);
        
        <em>//helloService 的 remoting server ，需要有 token 认证</em>
        helloService.hello(<span style="color:#50a14f">"noear"</span>);
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">3、增强部分接口及相关配置能力</h3> 
<ul> 
 <li>增加 Solon Filter 序号位支持</li> 
 <li>增加 Solon Props::getByParse 接口，可应对组合配置需要。例：<code>Hello $&#123;user.name&#125;</code> 这样的配置需求</li> 
 <li>增加 CloudJobHandler 接口，让 Job Handler 更清晰些</li> 
 <li>增加 Solon Auth 新注解：<code>@AuthIp</code>, <code>@AuthPath</code> 支持</li> 
 <li>增加 CloudConfig 的注解内容，支持 $&#123;xx&#125;yyy 风格配置</li> 
 <li>增加 CloudEvent 的注解内容，支持 $&#123;xx&#125;yyy 风格配置</li> 
 <li>增加 CloudJob 的注解内容，支持 $&#123;xx&#125;yyy 风格配置</li> 
 <li>增加 CloudBreaker 的注解内容，支持 $&#123;xx&#125;yyy 风格配置</li> 
 <li>增加 @Component 单例组件通过 EventBus 扩展的机制</li> 
 <li>增加 env 启动参数切换配置文件；例：java -jar xxx.jar -env=test</li> 
 <li>标注 Utils::throwableWrap 函数为弃用，并调整内部异常包装处理</li> 
 <li>限制 DataThrowable 被最终渲染</li> 
 <li>取消 WarnThrowable</li> 
</ul> 
<h3 style="text-align:start">4、日志对接进一步增加</h3> 
<p style="text-align:start">Solon 的日志体系，除自有 slf4j 实现之后；还适配有 Logback 的添加器；现增加 Log4j 添加器的适配。</p> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            