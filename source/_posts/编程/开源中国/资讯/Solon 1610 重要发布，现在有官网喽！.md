
---
title: 'Solon 1.6.10 重要发布，现在有官网喽！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2713'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 13:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2713'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">关于官网</h3> 
<p style="color:#24292e; text-align:start">千呼万唤始出来：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a><span> </span>。整了一个月多了，总体样子有了。。。还得不断接着整！</p> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量级应用开发框架。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。短小而精悍！</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放的原则</strong></li> 
 <li>力求，<strong>更小、更快、更自由的体验</strong></li> 
</ul> 
<h3 style="text-align:start">关于 Solon Cloud</h3> 
<p style="color:#24292e; text-align:start">Solon Cloud 定义了一系列分布式开发的接口标准和配置规范，相当于DDD模式里的防腐层概念。是 Solon 的微服务架构模式开发解决方案。</p> 
<h3 style="text-align:start">关于本次更新</h3> 
<h4 style="text-align:start">1、增加了第三方日志框架的适配。以往是直接使用日志框架，亲合度差了一些</h4> 
<ul> 
 <li>新增 log4j2-solon-plugin 插件</li> 
 <li>新增 logback-solon-plugin 插件</li> 
</ul> 
<p style="color:#24292e; text-align:start">之前只适配了分布式日志服务。现在也有本地的了。且，统一的配置方式（默认可以0配置）：</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">demoapp</span>

<em># 以下为默认值，可以都不加，或者想改哪行加哪行(支持"云端配置服务"进行配置，支持写到"云端日志服务")</em>
<span style="color:#986801">solon.logging.appender:</span>
  <span style="color:#986801">console:</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">TRACE</span>
    <span style="color:#986801">pattern:</span> <span style="color:#50a14f">"%highlight(%-5level %d&#123;yyyy-MM-dd HH🇲🇲ss.SSS&#125; [-%t][*%X&#123;traceId&#125;]%tags[%logger&#123;20&#125;]:) %n%msg%n"</span>
  <span style="color:#986801">file:</span>
    <span style="color:#986801">name:</span> <span style="color:#50a14f">"logs/$&#123;solon.app.name&#125;"</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">INFO</span>
    <span style="color:#986801">pattern:</span> <span style="color:#50a14f">"%-5level %d&#123;yyyy-MM-dd HH🇲🇲ss.SSS&#125; [-%t][*%X&#123;traceId&#125;]%tags[%logger&#123;20&#125;]: %n%msg%n"</span>
  <span style="color:#986801">cloud:</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">INFO</span>
    
<em># 记录器级别的配置示例</em>
<span style="color:#986801">solon.logging.logger:</span>
  <span style="color:#50a14f">"features.*"</span><span style="color:#50a14f">:</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">WARN</span>
  <span style="color:#50a14f">"org.jetty.demo.*"</span><span style="color:#50a14f">:</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">WARN</span>    
</code></pre> 
<p style="color:#24292e; text-align:start">并以 slf4j 做为统一的记录界面</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Slf</span>4j
<span style="color:#4078f2">@Service</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">hello</span><span>()</span></span>&#123;
        log.info(<span style="color:#50a14f">"Hello world!"</span>);
    &#125;
&#125;
</code></pre> 
<h4 style="text-align:start">2、增加了一些便利接口和使用方式</h4> 
<ul> 
 <li>增加 Context::sessionAsInt, Context::sessionAsLong, Context::sessionAsDouble 接口</li> 
 <li>增加 Context::sessionRemove 接口</li> 
 <li>修复 solon.extend.stop 用户ip获取错误</li> 
 <li>增加 mybatisplus-solon-plugin 为 globalConfig 注入内容的入口</li> 
 <li>集成包 solon-api 默认添加 solon.extend.cors 插件</li> 
 <li>增加 主体流注入支持（@Body InputStream body）</li> 
 <li>取消 solon.cache 插件，由 solon.data 插件集成相关功能，并提供工厂扩展机制</li> 
 <li>增加 上下文特性，自动做为模板变量</li> 
 <li>增加 JsonRenderFactory 的事件扩展支持</li> 
 <li>增加 模板引擎配置 事件扩展机制</li> 
</ul> 
<p style="color:#24292e; text-align:start">综合一些特性，做个简单的组合演示</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span>-></span>&#123;
            <em>//增加默认的跨域支持（支持它的插件，现在默认集成到了 solon-api 集成包里）</em>
            app.before(<span style="color:#a626a4">new</span> CrossHandler().exposedHeaders(<span style="color:#50a14f">"sign,token"</span>));
        
            <em>//定制渲染工厂（现在，不管哪个Json 框架都可基于 JsonRenderFactory 进行统一的定制）</em>
            app.onEvent(JsonRenderFactory<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">f</span>-></span>&#123;
                <em>//json渲染时，将 long 型统一转为 string</em>
                f.addConvertor(Long<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">v</span>-> <span style="color:#c18401">String</span>.<span style="color:#c18401">valueOf</span>(<span style="color:#c18401">v</span>))</span>;
            &#125;);
            
            <em>//定制ftl模板配置</em>
            app.onEvent(freemarker.template.Configuration<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">c</span> -> </span>&#123;
                <em>//增加经典模式支持</em>
                c.setSetting(<span style="color:#50a14f">"classic_compatible"</span>, <span style="color:#50a14f">"true"</span>);
                c.setSetting(<span style="color:#50a14f">"number_format"</span>, <span style="color:#50a14f">"0.##"</span>);
            &#125;);
        &#125;);
    &#125;
&#125;

<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span> </span>&#123;
    <em>//通过供应商模式，自动构建不同的缓存服务类型（从原来的 solon.cache 转移到 solon.data 插件）</em>
    <span style="color:#4078f2">@Bean</span>
    <span><span style="color:#a626a4">public</span> CacheService <span style="color:#4078f2">cache1</span><span>(@Inject(<span style="color:#50a14f">"cache1"</span>)</span> CacheServiceSupplier supplier) </span>&#123;
        <span style="color:#a626a4">return</span> supplier.get();
    &#125;
&#125;

<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/login"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">login</span><span>(Context ctx)</span></span>&#123;
        <em>//到登录页时，把 user_id 删掉；确保用户重新登录</em>
        ctx.sessionRemove(<span style="color:#50a14f">"user_id"</span>);
    &#125;
    
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/admin"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">admin</span><span>(Context ctx)</span></span>&#123;
        <span style="color:#a626a4">long</span> userId = ctx.sessionAsLong(<span style="color:#50a14f">"user_id"</span>);
        <span style="color:#a626a4">if</span>(userId == <span style="color:#986801">0</span>)&#123;
            <em>//如果用户id为0，则302跳转到登录面</em>
            ctx.redirect(<span style="color:#50a14f">"/login"</span>);
        &#125;
    &#125;
    
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/admin/group/edit.save"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">admin_group_edit_save</span><span>(<span style="color:#a626a4">long</span> groupId, String name, @Body String meta)</span></span>&#123;
        <em>//groupId, name 通过 queryString 传入；meta 是通过 body 传入的纯文本</em>
    &#125;
&#125;

<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoFilter</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Filter</span></span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">doFilter</span><span>(Context ctx, FilterChain chain)</span> <span style="color:#a626a4">throws</span> Throwable </span>&#123;
        <em>//给所有模板增加全局变量（或公共变量）</em>
        ctx.attrSet(<span style="color:#50a14f">"js"</span>, <span style="color:#50a14f">"/_static/js"</span>);
        ctx.attrSet(<span style="color:#50a14f">"css"</span>, <span style="color:#50a14f">"/_static/css"</span>);
        
        chain.doFilter(ctx);
    &#125;
&#125;
</code></pre> 
<h4 style="text-align:start">3、能力或兼容性增强</h4> 
<ul> 
 <li>增加 @Init 私有函数支持</li> 
 <li>增加 @Bean 私有函数支持</li> 
 <li>增加 @Inject("$&#123;xxx:&#125;")，默认值为空的支持</li> 
 <li>增加 StringSerializerRender 对 renderAndReturn 的支持</li> 
 <li>增加 Context::renderAndReturn 支持非视图数据</li> 
 <li>调整 EventListener 充许 onEvent 抛出异常</li> 
 <li>调整 初始化失败时，自动停掉所有插件并结束进程</li> 
 <li>增加 上下文特性，自动做为模板变量</li> 
 <li>优化 配置注入"$&#123;xxx:def&#125;"的兼容性，def有":"符也没关系了</li> 
 <li>增加 Mvc 数组参数注入时，自动以,号分离为数组</li> 
 <li>增加 @Init::index 属性</li> 
 <li>增加 容器扫描去重去处</li> 
 <li>取消 @Param::format 属性（自动处理增加17种格式）</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span> </span>&#123;
    <em>//以前必须要用 public</em>
    <span style="color:#4078f2">@Bean</span>
    <span><span style="color:#a626a4">private</span> CacheService <span style="color:#4078f2">cache1</span><span>(@Inject(<span style="color:#50a14f">"cache1"</span>)</span> CacheServiceSupplier supplier) </span>&#123;
        <span style="color:#a626a4">return</span> supplier.get();
    &#125;
    
    <span style="color:#4078f2">@Init</span>
    <span><span style="color:#a626a4">private</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">init</span><span>()</span></span>&#123;
        <em>//...</em>
    &#125;
&#125;

<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;

    <em>//以前是不能在默认值里出现:号的</em>
    <span style="color:#4078f2">@Inject</span>(<span style="color:#50a14f">"$&#123;user.name:noear:org&#125;"</span>)
    String userName;
    
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">test</span><span>(Context ctx)</span></span>&#123;
        UserModel user = userService.get(<span style="color:#986801">1</span>);
        
        <em>//现在可以借助上下文的渲染函数进行序列化（默认是json，也可指定渲染器）</em>
        ctx.attrSet(<span style="color:#50a14f">"@render"</span>,<span style="color:#50a14f">"@json"</span>);
        String json = ctx.renderAndReturn(user);
        
        <span style="color:#a626a4">return</span> Base64Utils.encode(json);
    &#125;
&#125;
</code></pre> 
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
</code>
</pre> 
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
<p style="color:#24292e; text-align:start">更多系统的学习内容，建议参考官网</p> 
<p> </p>
                                        </div>
                                      
</div>
            