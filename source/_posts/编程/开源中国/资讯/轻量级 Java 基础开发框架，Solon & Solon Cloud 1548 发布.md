
---
title: '轻量级 Java 基础开发框架，Solon & Solon Cloud 1.5.48 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3105'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 16:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3105'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="text-align:start">Solon 已有120个生态扩展插件，此次更新主要为细节打磨：</h4> 
<ul> 
 <li>增加 solon.serialization，做为序列化的基础插件</li> 
 <li> <p>优化 所有Json序列化插件，使之可方便定制类型序列化</p> <pre><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
      Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span>-></span>&#123;
          initMvcJsonCustom();
      &#125;);
  &#125;

  <em>/**
   * 初始化json定制（需要在插件运行前定制）
   */</em>
  <span><span style="color:#a626a4">private</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">initMvcJsonCustom</span><span>()</span> </span>&#123;
      <em>//通过转换器，做简单类型的定制</em>
      SnackRenderFactory.global
              .addConvertor(Date<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">s</span> -> <span style="color:#c18401">s</span>.<span style="color:#c18401">getTime</span>())</span>;

      SnackRenderFactory.global
              .addConvertor(LocalDate<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">s</span> -> <span style="color:#c18401">s</span>.<span style="color:#c18401">format</span>(<span style="color:#c18401">DateTimeFormatter</span>.<span style="color:#c18401">ofPattern</span>("<span style="color:#c18401">yyyy</span>-<span style="color:#c18401">MM</span>-<span style="color:#c18401">dd</span>")))</span>;

      SnackRenderFactory.global
              .addConvertor(LocalDateTime<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">s</span> -> <span style="color:#c18401">s</span>.<span style="color:#c18401">format</span>(<span style="color:#c18401">DateTimeFormatter</span>.<span style="color:#c18401">ofPattern</span>("<span style="color:#c18401">yyyy</span>-<span style="color:#c18401">MM</span>-<span style="color:#c18401">dd</span> <span style="color:#c18401">HH</span>:<span style="color:#c18401">mm</span>")))</span>;

     <em>//复杂的，可用原生编码接口</em>
     <em>//SnackRenderFactory.global.addEncoder(...)</em>
  &#125;
&#125;  

<em>//每个适配插件都会有自己定制渲染工厂</em>
<em>//solon.serialization.snack3:: SnackRenderFactory</em>
<em>//solon.serialization.jackson:: JacksonRenderFactory</em>
<em>//solon.serialization.gson:: GsonRenderFactory</em>
<em>//solon.serialization.fastjson:: FastjsonRenderFactory</em>
</code></pre> </li> 
 <li> <p>调整 CloudLockService，lock 更名为 tryLock</p> <pre><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span></span>&#123;
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">demo</span><span>(<span style="color:#a626a4">long</span> userId, ...)</span></span>&#123;
      <span style="color:#a626a4">if</span>(CloudCleint.lock().tryLock(<span style="color:#50a14f">"user_id"</span> + userId))&#123;
          <em>//获取分布式锁成功</em>
          <em>//..做业务</em>
      &#125;<span style="color:#a626a4">else</span>&#123;
          <em>//提示...</em>
      &#125;
  &#125;
&#125;
</code></pre> </li> 
 <li> <p>引入 redisx 框架做为 solon.cache.redis 和 solon.extend.sessionstate.redis 的客户端</p> </li> 
 <li> <p>插件 aws-s3-solon-plugin，改为基于 rest api 适配</p> <pre><code class="language-java"><em>//大小从7MB 变成了 2KB：）</em>

CloudClient.file().put(<span style="color:#50a14f">"user_1"</span>, <span style="color:#a626a4">new</span> Media(<span style="color:#50a14f">"&#123;name:'noear'&#125;"</span>));
</code></pre> </li> 
 <li> <p>插件 weed3-solon-plugin，weed3 升级为 3.4.1</p> </li> 
 <li> <p>插件 mybatis-solon-plugin 增加 SqlSessionFactoryBuilder 可定制的能力</p> <pre><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
      <span style="color:#a626a4">new</span> SolonBuilder()
              .onPluginLoadEnd(e -> &#123;
                  <em>//重新定义 SqlSessionFactoryBuilder（没有需要，最好别动它...）</em>
                  Aop.wrapAndPut(SqlSessionFactoryBuilder<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">new</span> <span style="color:#c18401">SqlSessionFactoryBuilderImpl</span>())</span>;
              &#125;)
              .start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>)</span>;
  &#125;
&#125;  
</code></pre> </li> 
</ul> 
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
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Api 入门教程示例：<a href="https://gitee.com/noear/solon_api_demo">https://gitee.com/noear/solon_api_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Auth 入门教程示例：<a href="https://gitee.com/noear/solon_auth_demo">https://gitee.com/noear/solon_auth_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            