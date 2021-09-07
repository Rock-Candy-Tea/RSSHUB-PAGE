
---
title: 'Solon 1.5.29 发布，轻量级 Java 基础开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9144'
author: 开源中国
comments: false
date: Tue, 07 Sep 2021 13:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9144'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">本次版本主要变化：</h3> 
<ul> 
 <li>增加 captcha-solon-plugin 插件（提供滑块验证与选文字验证能力）</li> 
 <li>插件 sa-token-solon-plugin，升级 sa-token 为 1.26.0</li> 
 <li>插件 water-solon-plugin，升级 water.client 为 2.2.8</li> 
 <li>插件 beetlsql-solon-plugin 升级 beetlsql 为 3.8.0</li> 
 <li>插件 weed3-solon-plugin，升级 weed3 为 3.3.22</li> 
 <li>修复 当profile为空内容时会出错的问题</li> 
 <li>修复 solon.auth 插件的 @Auth 注解在控制器上无效的问题</li> 
 <li>修复 Servelt 的 session 不能清空的问题</li> 
 <li>修复 solon.exnted.cors 在某些情况下会404的问题</li> 
 <li>增加 会话状态接口重置的能力</li> 
 <li>增强 配置转实体的枚举支持不计大小写</li> 
 <li>调整 验证器 Date ，空为通过（是否充许为空由@NotEmpty处理，以便控制充许空的应用场景）</li> 
 <li>调整 验证器 Email ，空为通过（是否充许为空由@NotEmpty处理）</li> 
 <li>调整 验证器 Pattern ，空为通过（是否充许为空由@NotEmpty处理）</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h3 style="text-align:start">快速了解 Solon 的材料：</h3> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
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
<h3 style="text-align:start">Hello world：</h3> 
<pre style="text-align:start"><code class="language-java"><em>//Handler 模式：</em>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">App</span>&#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span>(String[] args)&#123;
        SolonApp app = Solon.start(App.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>);
        
        app.get(<span style="color:#50a14f">"/"</span>,(c)->c.output(<span style="color:#50a14f">"Hello world!"</span>));
    &#125;
&#125;

<em>//Controller 模式：(mvc or rest-api)</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">App</span>&#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span>(String[] args)&#123;
        Solon.start(App.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>);
    &#125;
  
    <em>//限定 put 方法类型</em>
    <span style="color:#4078f2">@Put</span>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span>(String name)&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello "</span> + name;
    &#125;
&#125;

<em>//Remoting 模式：(rpc)</em>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
<span style="color:#4078f2">@Remoting</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">App</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">HelloService</span>&#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span>(String[] args)&#123;
        Solon.start(App.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>);
    &#125;

    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span>()&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello world!"</span>;
    &#125;
&#125;
</code>
</pre> 
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
            