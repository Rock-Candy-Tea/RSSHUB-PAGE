
---
title: 'Solon 1.6.6 发布，细节打磨'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4539'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 18:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4539'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="text-align:start">Solon 已有120个生态扩展插件，此次更新主要为细节打磨：</h4> 
<ul> 
 <li>增加 @Inject("ds1") BeanWrap bw 模式注入</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span></span>&#123;
    <span style="color:#4078f2">@Bean</span>(value = <span style="color:#50a14f">"db1"</span>, typed = <span style="color:#a626a4">true</span>)
    <span><span style="color:#a626a4">public</span> DataSource <span style="color:#4078f2">db1</span><span>(@Inject(<span style="color:#50a14f">"$&#123;test.db1&#125;"</span>)</span> HikariDataSource ds) </span>&#123;
        <span style="color:#a626a4">return</span> ds;
    &#125;
    
    <span style="color:#4078f2">@Bean</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">bw1</span><span>(@Inject(<span style="color:#50a14f">"db1"</span>)</span> BeanWrap bw)</span>&#123;
        <em>//这是新支持的，可获取Bean的包装器</em>
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>优化 mybatis-solon-plugin 的适配方案</li> 
 <li>优化 water-solon-plugin 任务调试的安全机制</li> 
 <li>升级 sa-token-solon-plugin ，sa-token 到 1.28</li> 
 <li>升级 beetlsql-solon-plugin ，beetlsql 到 3.12</li> 
 <li>升级 solon.boot.smarthttp， smart-http 到 1.1.10</li> 
 <li>升级 weed3-solon-plugin， weed 到 3.4.10</li> 
 <li>升级 water-solon-plugin， water 到 2.5.1。原 /run/,/msg/ 升级为 /_run/</li> 
 <li>Mvc 注入，支持 1 转为 true 的支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>(bool isOk)</span></span>&#123;
    &#125;
&#125;

<em>//curl http://localhost:8080/test?isOk=1</em>
</code></pre> 
<ul> 
 <li>AuthProcessorBase 增加 list = null 的预检</li> 
 <li>去掉 Scan completed 打印</li> 
 <li>Nami 增加 interface 默认函数的支持</li> 
 <li>允许 Size，Length 注解的数据为Null。交由 NotNull 负责</li> 
 <li>修复 water-solon-plugin ，不能处理缓存更新通知的问题（之前的版改出了问题）</li> 
 <li>关闭 water-solon-plugin 的默认日志打印</li> 
 <li>插件 solon.serialization.fastjson 增加泛型参数支持</li> 
 <li>插件 solon.serialization.snack3 增加泛型参数支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Post</span>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>(Map<String,User> userMap, List<Order> orderAry)</span></span>&#123;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>插件 beetlsql-solon-plugin，升级 beetlsql 到 3.12.2-RELEASE</li> 
 <li>增加 @Body 注解，注入 body string 支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>(@Body String bodyStr)</span></span>&#123;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>增加 @Validated List<?> 验证模式支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Valid</span>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>(@Validated List<User> users)</span></span>&#123;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 Nami 构造器设定的 Headers，没有下传的问题</li> 
 <li>修复 solon.boot.socketd.websocket，去掉 session.path() 多余内容</li> 
 <li>修复 sockted sessionBase::paramMap()，当 query=null 时会出错的问题</li> 
 <li>依赖 snack3 升级为 3.2.1</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon ，轻量级应用开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
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
<p> </p>
                                        </div>
                                      
</div>
            