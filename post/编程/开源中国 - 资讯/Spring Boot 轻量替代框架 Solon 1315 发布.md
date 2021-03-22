
---
title: 'Spring Boot 轻量替代框架 Solon 1.3.15 发布'
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Mon, 22 Mar 2021 12:01:00 GMT
thumbnail: ''
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
<h3 style="text-align:start">1、增加 Solon Cloud Breaker 接口规范（限流）</h3> 
<ul> 
 <li>使用断路器进行限流</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//1.通过注解，添加断路器实现限流</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">BreakerDemo</span> &#123;
    <em>//添加断路器，以实现限流。demo 为断路器 name</em>
    <span style="color:#4078f2">@CloudBreaker</span>(<span style="color:#50a14f">"demo"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demox/test"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">test</span>() <span style="color:#a626a4">throws</span> Exception&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;
&#125;

<em>//2.通过过滤器添加断路器实现限流</em>
Solon.global().filter((ctx, chain) -> &#123;
    <span style="color:#a626a4">if</span>(<span style="color:#50a14f">"/demox/test"</span>.equals(ctx.path())) &#123;
        <span style="color:#a626a4">try</span> (AutoCloseable entry = CloudClient.breaker().entry(<span style="color:#50a14f">"demo"</span>)) &#123;
            chain.doFilter(ctx);
        &#125;<span style="color:#a626a4">catch</span> (BreakerException ex)&#123;
            ctx.statusSet(<span style="color:#986801">403</span>);
        &#125;
    &#125;
&#125;);
</code></pre> 
<ul> 
 <li>本地配置支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-yaml"><span style="color:#986801">solon.cloud.local:</span>
  <span style="color:#986801">breaker:</span>     
    <span style="color:#986801">demo:</span> <span style="color:#986801">1</span>    <em>#qps</em>
</code></pre> 
<p style="text-align:start">附：目前为止Solon Cloud 组件已规范并定义以下接口</p> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>接口定义</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudBreakerService</td> 
   <td style="border-color:#dfe2e5">分布式断路器服务接口（实现组件有：guava-solon-plugin、sentinel-solon-plugin）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudConfigService</td> 
   <td style="border-color:#dfe2e5">分布式配置服务接口</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudDiscoveryService</td> 
   <td style="border-color:#dfe2e5">分布式注册也发现服务接口</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudEventService</td> 
   <td style="border-color:#dfe2e5">分布式事件服务接口</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudLockService</td> 
   <td style="border-color:#dfe2e5">分布式锁接口</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudLogService</td> 
   <td style="border-color:#dfe2e5">分布式日志服务接口</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">CloudTraceService</td> 
   <td style="border-color:#dfe2e5">分布式链路跟踪服务接口</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">2、增加Solon Sloud Discovery本地配置支持，便于本地调试</h3> 
<pre style="text-align:start"><code class="language-yaml">
<span style="color:#986801">solon.cloud.nacos:</span>
  <span style="color:#986801">discovery:</span>
    <span style="color:#986801">enable:</span> <span style="color:#0184bb">false</span>   <em>#禁用云端发现服务（本地的发现服务才会生效）</em>

<span style="color:#986801">solon.cloud.local:</span>
  <span style="color:#986801">discovery:</span>
    <span style="color:#986801">service:</span>
      <span style="color:#986801">demo1:</span>
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"http://localhost:8080"</span>
      <span style="color:#986801">demo2:</span>
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"http://localhost:8081"</span>
      <span style="color:#986801">demo3:</span>
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"tcp://localhost:28080"</span>
</code></pre> 
<pre style="text-align:start"><code class="language-java"><em>//RPC 客户端注入，自动发现demo1的服务节点</em>
<span style="color:#4078f2">@NamiClient</span>(name=<span style="color:#50a14f">"demo1"</span>)
Demo1Service service;
</code></pre> 
<h3 style="text-align:start">3、加强静态文件组件可配性和调试便利</h3> 
<ul> 
 <li>增加缓存控制的max-age配置，例：</li> 
</ul> 
<pre style="text-align:start"><code class="language-yaml"><span style="color:#986801">solon.staticfiles:</span>
  <span style="color:#986801">maxAge:</span> <span style="color:#986801">6000</span> <em>#10分钟检测一次</em>
</code></pre> 
<ul> 
 <li>调试模式下自动取消304缓存</li> 
</ul> 
<pre style="text-align:start"><code>方便调试时，即时刷新静态资源
</code></pre> 
<h3 style="text-align:start">4、Solon Data组件之缓存管理增加key模式（之前仅有tags模式）</h3> 
<ol> 
 <li>tags 模式：用于批量管控。（例如：多次分页查询的结果，可通过 tags 批量删除）</li> 
 <li>key 模式：用于精准管控，使用时要注意 key 冲突。</li> 
</ol> 
<pre style="text-align:start"><code><em>//</em>
<em>// 混合使用示例：</em>
<em>//</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> &#123;
    <em>/**
     * 执行结果缓存10秒，设定 key=test3_$&#123;label&#125; ，并添加 tag=test3 标签（可以批量删除）
     */</em>
    <span style="color:#4078f2">@Cache(key = <span style="color:#50a14f">"test3_<span style="color:#e45649">$&#123;label&#125;</span>"</span>, tags = <span style="color:#50a14f">"test3"</span>, seconds = 10)</span>
    <span style="color:#4078f2">@Mapping(<span style="color:#50a14f">"/cache3/"</span>)</span>
    <span style="color:#a626a4">public</span> String cache(int label) &#123;
        <span style="color:#a626a4">return</span> LocalDateTime.now().toString();
    &#125;
    <em>/**
     * 执行后，清除 tag=test3 的所有缓存，并更新 key=test3_$&#123;label&#125; 的缓存数据
     */</em>
    <span style="color:#4078f2">@CachePut(key = <span style="color:#50a14f">"test3_<span style="color:#e45649">$&#123;label&#125;</span>"</span>)</span>
    <span style="color:#4078f2">@CacheRemove(tags = <span style="color:#50a14f">"test3"</span>)</span>
    <span style="color:#4078f2">@Mapping(<span style="color:#50a14f">"/cache3/update"</span>)</span>
    <span style="color:#a626a4">public</span> String remove(int label) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"清除成功-"</span> + new Date();
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">5、安全停止，升级为二段式暂停</h3> 
<pre style="text-align:start"><code class="language-java"><em>//启动时，通过lumda函数，开启安全停止即可</em>
<em>//</em>
Solon.start(TestApp.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">x</span> -> <span style="color:#c18401">x</span>.<span style="color:#c18401">enableSafeStop</span>(<span style="color:#c18401">true</span>));

</code></pre> 
<h3 style="text-align:start">6、验证组件，增加自定义状态码支持</h3> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoValidator</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Validator</span><<span style="color:#c18401">Demo</span>> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> Result <span style="color:#4078f2">validate</span>(Context ctx, Demo anno, String name, StringBuilder tmp) &#123;
        <em>//</em>
        <em>// 旧版本，最终输出只返回 400 状态</em>
        <em>//</em>
        <span style="color:#a626a4">return</span> Result.failure(<span style="color:#986801">401</span>);
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>项目地址：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>RPC入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            