
---
title: '对标 Spring Boot & Cloud ，轻量框架 Solon 1.4.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8891'
author: 开源中国
comments: false
date: Tue, 01 Jun 2021 05:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8891'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。</p> 
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
<h3 style="text-align:start">1、增加 sa-token-solon-plugin 插件，适配 sa-token 认证框架</h3> 
<p style="text-align:start">应用样例</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test/"</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">TestController</span> &#123;
    <span style="color:#4078f2">@SaCheckLogin</span>
    <span style="color:#4078f2">@SaCheckRole</span>(<span style="color:#50a14f">"super-admin"</span>)
    <span style="color:#4078f2">@SaCheckPermission</span>(<span style="color:#50a14f">"user-add"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"atCheck"</span>)
    <span style="color:#a626a4">public</span> AjaxJson <span style="color:#4078f2">atCheck</span>() &#123;
        System.out.println(<span style="color:#50a14f">"只有通过注解鉴权，才能进入此方法"</span>);
        <span style="color:#a626a4">return</span> AjaxJson.getSuccess();
    &#125;

    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"atJurOr"</span>)
    <span style="color:#4078f2">@SaCheckPermission</span>(value = &#123;<span style="color:#50a14f">"user-add"</span>, <span style="color:#50a14f">"user-all"</span>, <span style="color:#50a14f">"user-delete"</span>&#125;, mode = SaMode.OR)
    <span style="color:#a626a4">public</span> AjaxJson <span style="color:#4078f2">atJurOr</span>() &#123;
        <span style="color:#a626a4">return</span> AjaxJson.getSuccessData(<span style="color:#50a14f">"用户信息"</span>);
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">2、增加 solon.extend.auth 插件，Solon 自扩展的认证框架</h3> 
<p style="text-align:start">适配样例</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> &#123;
    <span style="color:#4078f2">@Bean</span>
     <span style="color:#a626a4">public</span> AuthAdapter <span style="color:#4078f2">init</span>() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> AuthAdapter()
            .loginUrl(<span style="color:#50a14f">"/login"</span>)
            .authPathMatchers(<span style="color:#a626a4">new</span> AuthPathMatchersImpl())
            .authInterceptor(<span style="color:#a626a4">new</span> AuthInterceptorImpl())
            .authProcessor(<span style="color:#a626a4">new</span> AuthProcessorImpl())
            .authOnFailure((ctx, rst) -> &#123;
                ctx.render(Result.failure(<span style="color:#986801">403</span>,<span style="color:#50a14f">"没有权限:("</span>));
            &#125;);
    &#125;
&#125;
</code></pre> 
<p style="text-align:start">应用样例</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test/"</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">TestController</span> &#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/hello/"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span>() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"hello world!"</span>;
    &#125;
    
    <span style="color:#4078f2">@AuthRoles</span>(<span style="color:#50a14f">"admin"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/admin/"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">admin</span>() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"hello admin!"</span>;
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">3、增加 solon-enjoy-web 快速开发套件（支持 enjob + activerecord 体验）</h3> 
<p style="text-align:start">jFinal 系列技术的爱好者，可以有不同的玩具了。solon-enjoy-web，支持 solon 完整的事务能力及缓存能力</p> 
<pre style="text-align:start"><code class="language-java"><em>//配置默认数据源</em>
<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> &#123;
    <span style="color:#4078f2">@Bean</span>
    <span style="color:#a626a4">public</span> DataSource <span style="color:#4078f2">db1</span>(@Inject(<span style="color:#50a14f">"$&#123;test.db1&#125;"</span>) HikariDataSource dataSource) &#123;
        <span style="color:#a626a4">return</span> dataSource;
    &#125;
&#125;

<em>//应用示列</em>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demo/"</span>)
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> &#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">""</span>)
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">test</span>()&#123;
        <span style="color:#a626a4">return</span> Db.template(<span style="color:#50a14f">"appx_get"</span>).findFirst();
    &#125;

    <span style="color:#4078f2">@Cache</span>(tags = <span style="color:#50a14f">"test2"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test2"</span>)
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">test2</span>()&#123;
        AppxModel dao = <span style="color:#a626a4">new</span> AppxModel().dao();

        <span style="color:#a626a4">return</span> dao.findById(<span style="color:#986801">4</span>);
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">4、增加 异常订阅转换为正常输出的能力</h3> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">GlobalException</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">EventListener</span><<span style="color:#c18401">Throwable</span>> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">onEvent</span>(Throwable e) &#123;
        Context c = Context.current();

        <span style="color:#a626a4">if</span> (c != <span style="color:#a626a4">null</span>) &#123;
            AjaxJson aj = <span style="color:#a626a4">null</span>;
            <span style="color:#a626a4">if</span> (e <span style="color:#a626a4">instanceof</span> SaTokenException) &#123;    
                NotLoginException ee = (NotLoginException) e;
                aj = AjaxJson.getNotLogin().setMsg(ee.getMessage());
            &#125; <span style="color:#a626a4">else</span> <span style="color:#a626a4">if</span> (e <span style="color:#a626a4">instanceof</span> NotRoleException) &#123;     
                NotRoleException ee = (NotRoleException) e;
                aj = AjaxJson.getNotJur(<span style="color:#50a14f">"无此角色："</span> + ee.getRole());
            &#125; <span style="color:#a626a4">else</span> <span style="color:#a626a4">if</span> (e <span style="color:#a626a4">instanceof</span> NotPermissionException) &#123;  
                NotPermissionException ee = (NotPermissionException) e;
                aj = AjaxJson.getNotJur(<span style="color:#50a14f">"无此权限："</span> + ee.getCode());
            &#125; <span style="color:#a626a4">else</span> <span style="color:#a626a4">if</span> (e <span style="color:#a626a4">instanceof</span> DisableLoginException) &#123; 
                DisableLoginException ee = (DisableLoginException) e;
                aj = AjaxJson.getNotJur(<span style="color:#50a14f">"账号被封禁："</span> + ee.getDisableTime() + <span style="color:#50a14f">"秒后解封"</span>);
            &#125; <span style="color:#a626a4">else</span> &#123;
                aj = AjaxJson.getError(e.getMessage());
            &#125;

            c.result = aj;
        &#125;
    &#125;
&#125;
</code>
</pre> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            