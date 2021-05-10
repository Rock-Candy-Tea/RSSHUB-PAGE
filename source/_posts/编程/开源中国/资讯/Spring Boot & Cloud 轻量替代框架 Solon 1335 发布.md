
---
title: 'Spring Boot & Cloud 轻量替代框架 Solon 1.3.35 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4953'
author: 开源中国
comments: false
date: Mon, 10 May 2021 12:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4953'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个微型的Java开发框架。强调，克制 + 简洁 + 开放的原则；力求，更小、更快、更自由的体验。支持：RPC、REST API、MVC、Micro service、WebSocket、Socket 等多种开发模式。</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范。是 Solon 的微服务模式开发套件方案。</p> 
<h4 style="text-align:start">替代？还能说些什么异同之处吗？</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单与快速概览》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的架构笔记》</a></p> 
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
<h3 style="text-align:start">1、为REST api增加更友好注解支持（@Get @Post @Delete @Put @Patch 等...）</h3> 
<p style="text-align:start">普通 HTTP api</p> 
<pre style="text-align:start"><code class="language-java"><em>//经典写法</em>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"demo00"</span>)
<span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo00</span>(String name) &#123;
    <span style="color:#a626a4">return</span> name;
&#125;
</code></pre> 
<p style="text-align:start">REST api（或强调http method的）</p> 
<pre style="text-align:start"><code class="language-java"><em>//经典写法</em>
<span style="color:#4078f2">@Mapping</span>(value = <span style="color:#50a14f">"demo10"</span>, method = MethodType.PUT)
<span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo10</span>(String name) &#123;
    <span style="color:#a626a4">return</span> name;
&#125;

<em>//新增method注解写法（比经典写法，简洁不少）</em>
<span style="color:#4078f2">@Put</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"demo11"</span>)
<span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo11</span>(String name) &#123;
    <span style="color:#a626a4">return</span> name;
&#125;

<em>//经典写法</em>
<span style="color:#4078f2">@Mapping</span>(value = <span style="color:#50a14f">"demo20"</span>, method = &#123;MethodType.POST, MethodType.GET&#125;)
<span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo20</span>(String name) &#123;
    <span style="color:#a626a4">return</span> name;
&#125;

<em>//新增method注解写法（比经典写法，简洁不少）</em>
<span style="color:#4078f2">@Post</span>
<span style="color:#4078f2">@Get</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"demo21"</span>)
<span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo21</span>(String name) &#123;
    <span style="color:#a626a4">return</span> name;
&#125;
</code></pre> 
<h3 style="text-align:start">2、注解 @Inject 增加 required 属性</h3> 
<h3 style="text-align:start">3、sureness-solon-plugin 权限认证组件（对 sureness 的适配）</h3> 
<h3 style="text-align:start">4、Solon cloud event 增加 kafka-solon-plugin 适配组件</h3> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            