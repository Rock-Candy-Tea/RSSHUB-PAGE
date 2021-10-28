
---
title: 'Solon & Solon Cloud 1.5.53 发布，轻量级 Java 基础开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5008'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 10:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5008'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:start">Solon 已有 120 个生态扩展插件，此次更新主要为细节打磨：</h4> 
<p>1、插件 mybatis-solon-plugin 增加 mappers、typeAliases 单行配置支持</p> 
<p style="color:#24292e; text-align:start">之前的多行模式：</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">mybatis.db1:</span>
    <span style="color:#986801">typeAliases:</span>    <em>#支持包名 或 类名（.class 结尾）</em>
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"webapp.model"</span>
    <span style="color:#986801">mappers:</span>        <em>#支持包名 或 类名（.class 结尾）或 xml（.xml结尾）</em>
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"webapp.dso.mapper"</span>
</code></pre> 
<p style="color:#24292e; text-align:start">新增加的单行模式支持：</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">mybatis.db1.typeAliases:</span>  <span style="color:#50a14f">"webapp.model"</span> <em>#如有多项逗号隔开</em>
<span style="color:#986801">mybatis.db1.mappers:</span> <span style="color:#50a14f">"webapp.dso.mapper"</span>
</code></pre> 
<p>2、添加 DownloadedFile 类，用于下载文件输出</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DownController</span> </span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"down1"</span>)
    <span><span style="color:#a626a4">public</span> DownloadedFile <span style="color:#4078f2">down</span><span>()</span> </span>&#123;
        InputStream stream = <span style="color:#a626a4">new</span> ByteArrayInputStream(<span style="color:#50a14f">"&#123;code:1&#125;"</span>.getBytes(StandardCharsets.UTF_8));

        <em>//之前复用了上传用的 UploadedFile 类，类名感觉不太对路</em>
        DownloadedFile file = <span style="color:#a626a4">new</span> DownloadedFile(<span style="color:#50a14f">"text/json"</span>, stream, <span style="color:#50a14f">"test.json"</span>); 

        <span style="color:#a626a4">return</span> file;
    &#125;

    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"down2"</span>)
    <span><span style="color:#a626a4">public</span> File <span style="color:#4078f2">down2</span><span>()</span> </span>&#123;
        String filePath = Utils.getResource(<span style="color:#50a14f">"static/debug.htm"</span>).getFile();

        File file = <span style="color:#a626a4">new</span> File(filePath); <em>//也可能用File直接输出</em>

        <span style="color:#a626a4">return</span> file;
    &#125;
&#125;
</code></pre> 
<p>3、将不确定的插件移到_hatch下，之后会有孵化插件的概念</p> 
<p>4、重新调整内核的异常处理链，进行让 Filter 可以统一获取异常处理</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">TestApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        Solon.start(TestApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span> -> </span>&#123;
            app.filter((ctx, chain) -> &#123;
                <em>//1.开始计时（用于计算响应时长）</em>
                <span style="color:#a626a4">long</span> start = System.currentTimeMillis();
                <span style="color:#a626a4">try</span> &#123;
                    chain.doFilter(ctx);

                    <em>//2.状态404与未处理</em>
                    <span style="color:#a626a4">if</span> (ctx.status() == <span style="color:#986801">404</span> || ctx.getHandled() == <span style="color:#a626a4">false</span>) &#123;
                        ctx.setHandled(<span style="color:#a626a4">true</span>);
                        ctx.output(<span style="color:#50a14f">"没有：（"</span>);
                    &#125;
                &#125; <span style="color:#a626a4">catch</span> (Throwable e) &#123;
                    <em>//3.异常捕促与控制</em>
                    e.printStackTrace();

                    ctx.output(<span style="color:#50a14f">"出错了：（"</span>);
                &#125;

                <em>//4.获得接口响应时长</em>
                <span style="color:#a626a4">long</span> times = System.currentTimeMillis() - start;
                System.out.println(<span style="color:#50a14f">"用时："</span>+ times);
            &#125;);
        &#125;);
    &#125;
&#125;

<em>//此处调整，解决控制器异常无法被过滤器获取的问题。</em>
</code></pre> 
<p>5、调整 solon.extend.cors 插件的 CrossHandler 接口，并增加 exposedHeaders(..)</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">TestApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span> -> </span>&#123;
            <em>//添加全局跨域控制</em>
            app.before(<span style="color:#a626a4">new</span> CrossHandler()
                    .allowCredentials(<span style="color:#a626a4">true</span>)
                    .allowedMethods(<span style="color:#50a14f">"*"</span>)
                    .allowedHeaders(<span style="color:#50a14f">"*"</span>)
                    .allowedOrigins(<span style="color:#50a14f">"*"</span>)
                    .exposedHeaders(<span style="color:#50a14f">"sign,token"</span>));
        &#125;);
    &#125;
&#125;
</code></pre> 
<p>6、插件 sa-token-solon-plugin，升级 sa-token 到 1.27.0</p> 
<p>7、插件 beetlsql-solon-plugin，升级 beetlsql 到 3.11.0-RELEASE</p> 
<p>8、增加自动打印异常的全局控制 enableErrorAutoprint</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Slf</span>4j
<span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span></span>&#123;
    <span><span style="color:#a626a4">public</span> statis <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Lo LoggerFactory.getLogger(DemoApp<span>.<span style="color:#a626a4">class</span>)</span>;
        
        Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span>-></span>&#123;
            <em>//默认是true，转到日志框架后，关掉</em>
            app.enableErrorAutoprint(<span style="color:#a626a4">false</span>);  <em>//控制进入EventBus的异常打印</em>
           
            <em>//订阅进入EventBus的异常</em>
            app.onError(e->&#123;
                Context ctx = Context.current();
                
                <span style="color:#a626a4">if</span>(ctx)&#123;
                    <em>//经常有人会疑问：为什么框架不把异常直接转到日志框架？</em>
                    <em>//下面就是好处：可以定制它，比如记录异常时的上下文参数，你排查时方便</em>
                    MDC.put(<span style="color:#50a14f">"tag0"</span>, ctx.path());
                    log.error(<span style="color:#50a14f">">Params: &#123;&#125;\r\nError: &#123;&#125;"</span>, ctx.paramMap(), e);
                &#125;<span style="color:#a626a4">else</span>&#123;
                    log.error(e);
                &#125;
            &#125;);
        &#125;);
    &#125;
&#125;
</code></pre> 
<p style="color:#24292e; text-align:start">Solon 内核的原则是“零外部依赖”，未处理的异常是发送到EventBus的。需要用户订阅处理，例：app.onError(e->...)。现在，默认就能看到异常打印了。</p> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<h3 style="text-align:start">关于 Solon Cloud</h3> 
<p style="color:#24292e; text-align:start">Solon Cloud 是一系列的接口标准和配置规范，相当于DDD模式里的防腐层概念。是 Solon 的微服务架构模式开发解决方案。</p> 
<h3 style="text-align:start">快速了解 Solon 的材料：</h3> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
<h4 style="text-align:start">所谓更小：</h4> 
<p style="color:#24292e; text-align:start">内核0.1m，最小的接口开发单位0.2m（相较于 Dubbo、Springboot 的依赖包，小到可以乎略不计）</p> 
<h4 style="text-align:start">所谓更快：</h4> 
<p style="color:#24292e; text-align:start">本机http helloworld测试，Qps可达12万之多。可参考：《<a href="https://gitee.com/noear/helloworld_wrk_test">helloworld_wrk_test</a>》</p> 
<h4 style="text-align:start">所谓更自由：(代码操控自由)</h4> 
<pre style="text-align:start"><code class="language-java"><em>// 除了注解模式之外，还可以按需手动</em>
<em>//</em>
<em>//手动获取配置（Props 为 Properties 增强版）</em>
Props db = Solon.cfg().getProp(<span style="color:#50a14f">"db"</span>);

<em>//手动获取容器里的Bean</em>
UserService userService = Aop.get(UserService<span>.<span style="color:#a626a4">class</span>)</span>;

<em>//手动监听http post请求</em>
Solon.global().post(<span style="color:#50a14f">"/user/update"</span>, x-> userService.updateById(x.paramMap()));

<em>//手动添加个RPC服务</em>
Solon.global().add(<span style="color:#50a14f">"/rpc/"</span>, HelloService<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">true</span>)</span>;

<em>//手动获取一个RPC服务消费端</em>
HelloService helloService = Nami.builder().create(HelloService<span>.<span style="color:#a626a4">class</span>)</span>;

<em>//手动为容器添加组件</em>
Aop.wrapAndPut(DemoService<span>.<span style="color:#a626a4">class</span>)</span>;
</code></pre> 
<h3 style="text-align:start">Hello world：</h3> 
<pre style="text-align:start"><code class="language-java"><em>//Handler 模式：</em>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        SolonApp app = Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
        
        app.get(<span style="color:#50a14f">"/"</span>,(c)->c.output(<span style="color:#50a14f">"Hello world!"</span>));
    &#125;
&#125;

<em>//Controller 模式：(mvc or rest-api)</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
    &#125;
  
    <em>//限定 put & post 方法类型</em>
    <span style="color:#4078f2">@Put</span>
    <span style="color:#4078f2">@Post</span>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>(String name)</span></span>&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello "</span> + name;
    &#125;
&#125;

<em>//Remoting 模式：(rpc)</em>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
<span style="color:#4078f2">@Remoting</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">HelloService</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
    &#125;

    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>()</span></span>&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello world!"</span>;
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start"> </h3> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Api 入门教程示例：<a href="https://gitee.com/noear/solon_api_demo">https://gitee.com/noear/solon_api_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Auth 入门教程示例：<a href="https://gitee.com/noear/solon_auth_demo">https://gitee.com/noear/solon_auth_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon Socketd 入门教程示例：<a href="https://gitee.com/noear/solon_socketd_demo">https://gitee.com/noear/solon_socketd_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            