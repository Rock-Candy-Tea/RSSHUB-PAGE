
---
title: 'Spring Boot 轻量替代框架 Solon 1.3.18 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7593'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 13:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7593'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个微型的Java开发框架。项目从2018年启动以来，参考过大量前人作品；历时两年，4000多次的commit；内核保持0.1m的身材，超高的跑分，良好的使用体验。支持：RPC、REST API、MVC、WebSocket、Socket 等多种开发模式。</p> 
<p style="text-align:start">Solon 强调：克制 + 简洁 + 开放的原则；力求：更小、更快、更自由的体验。</p> 
<h4 style="text-align:start">替代？那有什么异同之处？</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的架构笔记》</a></p> 
<h4 style="text-align:start">所谓更小：</h4> 
<p style="text-align:start">内核0.1m，最小开发单位0.2m（相比Dubbo、Springboot项目包，小到可以乎略不计）</p> 
<h4 style="text-align:start">所谓更快：</h4> 
<p style="text-align:start">本机helloworld测试，Qps可达12万之多。可参考：《<a href="https://gitee.com/noear/helloworld_wrk_test">helloworld_wrk_test</a>》</p> 
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
</code></pre> 
<h4 style="text-align:start">本次版本主要变化：</h4> 
<h3 style="text-align:start">1、增加 luffy-solon-plugin 组件，实现与动态语言混合执行能力</h3> 
<pre style="text-align:start"><code class="language-javascript"><em>//</em>
<em>// file: resources/luffy/hello.js</em>
<em>//</em>
<span style="color:#a626a4">let</span> name = ctx.param(<span style="color:#50a14f">"name"</span>);

<span style="color:#a626a4">if</span>(!name)&#123;
    name = <span style="color:#50a14f">"world"</span>;
&#125;

<span style="color:#a626a4">return</span> <span style="color:#50a14f">`Hello <span style="color:#e45649">$&#123;name&#125;</span>!`</span>;

<em>// 浏览器打开： http://localhost:8080/hello.js</em>
<em>// Java调用：CallUtil.callFile("/hello.js", null);</em>
</code></pre> 
<p style="text-align:start"><strong>目前已适配的动态语言</strong></p> 
<ul> 
 <li>python</li> 
 <li>ruby</li> 
 <li>javascript</li> 
 <li>groovy</li> 
 <li>lua</li> 
 <li>graaljs</li> 
</ul> 
<h3 style="text-align:start">2、Solon cloud 增加云端黑白名单接口 CloudListService</h3> 
<pre style="text-align:start"><code class="language-java"><em>//手动应用</em>
<em>//</em>
<span style="color:#a626a4">if</span>(CloudClient.list().inList(<span style="color:#50a14f">"blacklist"</span>,<span style="color:#50a14f">"ip"</span>,<span style="color:#50a14f">"127.0.0.1"</span>))&#123;
    <em>//提示</em>
&#125;

<em>//注解应用</em>
<span style="color:#4078f2">@NotBlanklist</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"demo1"</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">demo1</span>()&#123;
   <em>//业务处理</em>
&#125;

<span style="color:#4078f2">@Withelist</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"demo2"</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">demo2</span>()&#123;
  <em>//业务处理</em>
&#125;
</code></pre> 
<h3 style="text-align:start">3、增加 solon.logging 的异常格式化支持</h3> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Slf</span>4j
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span>&#123;
  <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">demo</span>()&#123;
    <span style="color:#a626a4">try</span>&#123;
        <em>//业务处理</em>
    &#125;<span style="color:#a626a4">catch</span>(Exception ex)&#123;
        log.error(<span style="color:#50a14f">"&#123;&#125;\r\n&#123;&#125;"</span>, <span style="color:#50a14f">"error:"</span>, ex);
    &#125;
  &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">4、增加 solon.extend.sessionstate.jwt 组件通过 header 传输的支持</h3> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>项目地址：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>RPC入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            