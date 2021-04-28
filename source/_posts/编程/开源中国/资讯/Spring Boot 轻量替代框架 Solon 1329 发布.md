
---
title: 'Spring Boot 轻量替代框架 Solon 1.3.29 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6327'
author: 开源中国
comments: false
date: Wed, 28 Apr 2021 12:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6327'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个微型的Java开发框架。项目2018年启动，参考过大量前人作品；内核0.1m的身材，超高的跑分，以及良好的使用体验。支持：RPC、REST API、MVC、WebSocket、Socket 等多种开发模式。</p> 
<p style="text-align:start">Solon 强调：克制 + 简洁 + 开放的原则；力求：更小、更快、更自由的体验。</p> 
<h4 style="text-align:start">替代？那有什么异同之处？</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
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
<h3 style="text-align:start">1、Solon cloud event 增加通道概念，以支持不同消息队列产品共用</h3> 
<p style="text-align:start">例如一个IoT项目的应用场景：业务消息用RabbitMQ，设备消息用 MQTT。</p> 
<p style="text-align:start"><strong>配置</strong></p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">demo</span>       <em>#配置服务使用的默认组</em>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">helloproducer</span>    <em>#发现服务使用的应用名</em>

<span style="color:#986801">solon.cloud.mqtt:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"tcp://localhost:41883"</span>   <em>#mqtt服务地址（默认通道不用命名）</em>

<span style="color:#986801">solon.cloud.rabbitmq:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">localhost:5672</span>   <em>#rabbitmq 服务地址</em>
  <span style="color:#986801">username:</span> <span style="color:#50a14f">root</span>           <em>#rabbitmq 链接账号</em>
  <span style="color:#986801">password:</span> <span style="color:#986801">123456</span>         <em>#rabbitmq 链接密码</em>
  <span style="color:#986801">event:</span>
    <span style="color:#986801">channel:</span> <span style="color:#50a14f">"biz"</span>      <em>#对事件服务进行通道命名</em>

</code></pre> 
<p style="text-align:start"><strong>生产端代码</strong></p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">TestController</span> &#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">test</span>(String msg) &#123;
        <em>//发送默认通道</em>
        <span style="color:#a626a4">return</span> CloudClient.event().publish(<span style="color:#a626a4">new</span> Event(<span style="color:#50a14f">"hello.demo"</span>, msg).qos(<span style="color:#986801">1</span>).retained(<span style="color:#a626a4">true</span>));
    &#125;

    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test2"</span>)
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">test2</span>(String msg) &#123;
        <em>//发送到biz通道（发送时，增加 channel 信息即可）</em>
        <span style="color:#a626a4">return</span> CloudClient.event().publish(<span style="color:#a626a4">new</span> Event(<span style="color:#50a14f">"hello.demo2"</span>, msg).channel(<span style="color:#50a14f">"biz"</span>));
    &#125;
&#125;
</code></pre> 
<p style="text-align:start"><strong>消费端代码</strong></p> 
<pre style="text-align:start"><code class="language-java"><em>//订阅并消费默认通道的事件（为了演示把mqtt的消息订阅过来了）</em>
<span style="color:#4078f2">@CloudEvent</span>(<span style="color:#50a14f">"hello.demo"</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">EVENT_hello_demo</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudEventHandler</span> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">handler</span>(Event event) <span style="color:#a626a4">throws</span> Throwable &#123;
        System.out.println(LocalDateTime.now() + ONode.stringify(event));
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;

<em>//订阅并消费biz通道的事件</em>
<span style="color:#4078f2">@CloudEvent</span>(value = <span style="color:#50a14f">"hello.demo2"</span>, channel = <span style="color:#50a14f">"biz"</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">EVENT_hello_demo2</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudEventHandler</span> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">handler</span>(Event event) <span style="color:#a626a4">throws</span> Throwable &#123;
        System.out.println(LocalDateTime.now() + ONode.stringify(event));
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">2、Solon cloud breaker 断路器增加动态配置支持</h3> 
<p style="text-align:start"><strong>配置</strong></p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.cloud.local:</span>
  <span style="color:#986801">breaker:</span>
    <span style="color:#986801">hello:</span> <span style="color:#986801">1</span>   <em>#断路器名称与阀值</em>
</code></pre> 
<p style="text-align:start"><strong>演示代码</strong></p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> &#123;

    <em>//此处安排了个断路器（即限流器），如果断路时，会返回HTTP 403状态</em>
    <span style="color:#4078f2">@CloudBreaker</span>(<span style="color:#50a14f">"hello"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/hello"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span>() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"hello"</span>;
    &#125;


    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/reset"</span>)
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">reset</span>() &#123;
        <em>//重新设置断路器的阀值（此配置，也可能过配置服务管理；动态更新）</em>
        Solon.cfg().setProperty(<span style="color:#50a14f">"solon.cloud.local.breaker.hello"</span>, <span style="color:#50a14f">"10"</span>);
    &#125;
&#125;

</code></pre> 
<h3 style="text-align:start">3、Solon logging 增加支持有格式化或无格式化的异常打印</h3> 
<p style="text-align:start">Solon logging 是基于 slf4j 的个实现方案，内部对接 Solon cloud log service 接口，从而将日志写到分布式日志服务。</p> 
<pre style="text-align:start"><code class="language-java">
<em>//无格式化场景</em>
log.error(<span style="color:#50a14f">"Error: "</span>, e);

<em>//格式化场景</em>
log.error(<span style="color:#50a14f">"Error: &#123;&#125;"</span>, e);

</code></pre> 
<h3 style="text-align:start">4、增加路由组件切换支持</h3> 
<pre style="text-align:start"><code class="language-java">
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Demo10App</span> &#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span>(String[] args) &#123;
        Solon.start(Demo10App.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span> -> &#123;
            Router router = <span style="color:#a626a4">new</span> RouterCustom();

            <em>//替换路由器</em>
            app.routerSet(router);
        &#125;);
    &#125;
&#125;

</code></pre> 
<h3 style="text-align:start">5、@Init 增加延时处理机制，并默认为 true</h3> 
<pre style="text-align:start"><code class="language-java">
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Demo</span> &#123;
    <span style="color:#4078f2">@Init</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">init</span>()&#123;
    &#125;
&#125;

</code></pre> 
<h3 style="text-align:start">6、优化session.jwt组件内部机制</h3> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>项目地址：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            