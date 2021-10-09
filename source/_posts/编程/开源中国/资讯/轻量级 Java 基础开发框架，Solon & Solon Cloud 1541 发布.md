
---
title: '轻量级 Java 基础开发框架，Solon & Solon Cloud 1.5.41 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8851'
author: 开源中国
comments: false
date: Sat, 09 Oct 2021 04:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8851'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="text-align:start">Solon 已有120个生态扩展插件，此次更新主要涉及 Solon Cloud 细节打磨：</h4> 
<ul> 
 <li> <p>调整 本地服务发现配置，与云端发现并存，并优于云端发现</p> <pre><code class="language-yml"><em># 这个特性，在k8s下会更方便。比如，dubbo 需要用注册服务，但 某 服务可直接通过 service name 调用</em>
<em>#</em>
<span style="color:#986801">solon.cloud.nacos:</span> 
  <span style="color:#986801">server:</span> <span style="color:#50a14f">xxx.xxx.xxx</span>

<span style="color:#986801">solon.cloud.local:</span>
  <span style="color:#986801">discovery:</span>
    <span style="color:#986801">service:</span>
      <span style="color:#986801">userapi:</span>
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"http://userapi"</span>
</code></pre> </li> 
 <li> <p>增加 CloudLoadBalanceFactory::register 接口（用于本地注册）</p> <pre><code class="language-java"><em>// 这个特性，算是"本地服务发现配置"的手动代码模式</em>
<em>//</em>
CloudLoadBalanceFactory.instance
    .register(<span style="color:#50a14f">""</span>,<span style="color:#50a14f">"userapi"</span>,()-> <span style="color:#50a14f">"http://userapi"</span>);

<em>//solon 一直崇尚代码的自动。</em>
</code></pre> </li> 
 <li> <p>优化 CloudFileService 接口设计:get,put,delete+Media</p> <pre><code class="language-java"><em>//上传</em>
CloudClient.file().put(<span style="color:#50a14f">"user_1"</span>, <span style="color:#a626a4">new</span> Media(<span style="color:#50a14f">"&#123;\"name\":\"noear\"&#125;"</span>)); <em>//上传文件</em>
CloudClient.file().put(<span style="color:#50a14f">"user_1_logo"</span>, <span style="color:#a626a4">new</span> Media(inputStream, <span style="color:#50a14f">"image/jpg"</span>)); <em>//上传图片</em>

<em>//获取</em>
String userJson =  CloudClient.file().get(<span style="color:#50a14f">"user_1"</span>).bodyAsString();
InputStream userLogo = CloudClient.file().get(<span style="color:#50a14f">"user_1_logo"</span>).body();

<em>//删除</em>
CloudClient.file().delete(<span style="color:#50a14f">"user_1"</span>).
</code></pre> </li> 
 <li>添加 minio-solon-plugin 插件 <pre><code><em># solon cloud 已适配了：aliyun oss、aws S3、七牛云存储、mino 的对象存储适配插件（即 CloudFileService 接口）</em>
</code></pre> </li> 
 <li>添加 solon.extend.health 插件 <pre><code class="language-java"><em>//提供一个 "/healthz" 的检测地址，并可增加检测点</em>
<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> </span>&#123;
  <span style="color:#4078f2">@Bean</span>
  <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">healthInit</span><span>()</span></span>&#123;
      HealthChecker.addPoint(<span style="color:#50a14f">"preflight"</span>, Result::succeed);
      HealthChecker.addPoint(<span style="color:#50a14f">"test"</span>, Result::failure);
      HealthChecker.addPoint(<span style="color:#50a14f">"boom"</span>, () -> &#123;
          <span style="color:#a626a4">throw</span> <span style="color:#a626a4">new</span> IllegalStateException();
      &#125;);
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
  
    <em>//限定 put 方法类型</em>
    <span style="color:#4078f2">@Put</span>
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
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            