
---
title: 'Spring Boot & Cloud 轻量替代框架 Solon 1.4.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0519/142041_60At_2720166.png'
author: 开源中国
comments: false
date: Wed, 19 May 2021 13:49:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0519/142041_60At_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个微型的Java开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Micro service、WebSocket、Socket 等多种开发模式。</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h4 style="text-align:start">快速了解Solon的材料：</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5053423">《Solon 生态插件清单》</a></p> 
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
<p>本次版本主要变化：</p> 
<h4 style="text-align:start">1、发布新的家簇成员表</h4> 
<p><img src="https://static.oschina.net/uploads/space/2021/0519/142041_60At_2720166.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:start">2、强化 Solon Remoting 概念 [ 增加 @Remoting 注解，替代旧的 @Component(remoting=true) ]</h4> 
<pre style="text-align:start"><code class="language-java"><em>//服务端代码1 - 使用tpc通信</em>
<span style="color:#4078f2">@Socket</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demo/socket"</span>)
<span style="color:#4078f2">@Remoting</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoRemoting1</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">HelloService</span>&#123;
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span>(String name)&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello "</span> + name;
    &#125;
&#125;

<em>//服务端代码2 - 使用http通信</em>
<span style="color:#4078f2">@Http</span>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demo/http"</span>)
<span style="color:#4078f2">@Remoting</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoRemoting2</span>  <span style="color:#a626a4">implements</span> <span style="color:#c18401">HelloService</span>&#123;
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span>(String name)&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello "</span> + name;
    &#125;
&#125;

<em>//客户端代码1</em>
<span style="color:#4078f2">@NamiClient</span>(name=<span style="color:#50a14f">"demo"</span>, path=<span style="color:#50a14f">"/demo/socket"</span>)
HelloService helloService;

String tmp = helloService.hello(<span style="color:#50a14f">"noear"</span>);
</code></pre> 
<h4 style="text-align:start">3、增加 @ClientEndpoint autoReconnect 属性</h4> 
<pre style="text-align:start"><code class="language-java"><em>//autoReconnect 默认为 true</em>
<span style="color:#4078f2">@ClientEndpoint</span>(uri = <span style="color:#50a14f">"tcp://localhost:28080"</span>, heartbeatRate = <span style="color:#986801">5</span>, autoReconnect = <span style="color:#a626a4">false</span>)
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">ClientListener</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Listener</span> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">onMessage</span>(Session session, Message message) <span style="color:#a626a4">throws</span> IOException &#123;
        System.out.println(message.bodyAsString());
    &#125;
&#125;
</code></pre> 
<p style="text-align:start">相关资料可百度：solon socketd</p> 
<h4 style="text-align:start">4、增强 solon-springboot-starter，可将 solon 注入器应用到 springboot bean</h4> 
<p style="text-align:start">当 spring boot 项目迁移到 solon 时，过渡期可以使用这个组件进行混合开发，示例：</p> 
<pre style="text-align:start"><code class="language-java"><em>//Spring bean</em>
<span style="color:#4078f2">@RestController</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span>&#123;
    <em>//Solon inject</em>
    <span style="color:#4078f2">@CloudConfig</span>(<span style="color:#50a14f">"user.name"</span>)
    String userName;
    
    <em>//Solon inject</em>
    <span style="color:#4078f2">@NamiClient</span>
    HelloService helloService;
&#125;
</code></pre> 
<h4 style="text-align:start">5、取消 nami-springboot-starter 组件</h4> 
<p style="text-align:start">因 solon-springboot-starter 的增强，这个组件没必要了。</p> 
<h4 style="text-align:start">6、取消 <code>@EnabelNamiClients</code>、<code>@EnableSolonCloud</code>、<code>@EnableSolon</code> 注解</h4> 
<p style="text-align:start">因 solon-springboot-starter 的增强，这三个注解也没怵要了；所有 Solon 相关的能力，直接可用。</p> 
<h4 style="text-align:start">7、取消 @Component remoting 属性</h4> 
<p style="text-align:start">由新 <code>@Remoting</code> 替代</p> 
<h3 style="text-align:start">附：项目地址</h3> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fsolon" target="_blank">https://github.com/noear/solon</a></li> 
</ul> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            