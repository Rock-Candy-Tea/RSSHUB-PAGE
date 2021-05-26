
---
title: 'Java 轻量开发框架 Solon 1.4.4 发布 ，完善分布式任务规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9718'
author: 开源中国
comments: false
date: Wed, 26 May 2021 11:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9718'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。</p> 
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
<h4 style="text-align:start">本次版本主要变化：</h4> 
<h3 style="text-align:start">1、增加 xxl-job-solon-plugin 插件，并适配CloudJob规范</h3> 
<p style="text-align:start">配置示例</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">demojob</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">demo</span>
  
<span style="color:#986801">solon.cloud.xxljob:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"http://localhost:8093/xxl-job-admin"</span>
</code></pre> 
<p style="text-align:start">应用示例</p> 
<pre style="text-align:start"><code class="language-java"><em>//1.注解模式</em>
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">JobBeanDemo2</span> &#123;
    <em>//Solon cloud job 注解</em>
    <span style="color:#4078f2">@CloudJob</span>(<span style="color:#50a14f">"JobBeanDemo2-1"</span>)
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span>()&#123;
        System.out.println(<span style="color:#50a14f">"JobBeanDemo2-1"</span>);
    &#125;

    <em>//原生注解</em>
    <span style="color:#4078f2">@XxlJob</span>(<span style="color:#50a14f">"JobBeanDemo2-2"</span>)
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test2</span>()&#123;
        System.out.println(<span style="color:#50a14f">"JobBeanDemo2-2"</span>);
    &#125;
&#125;

<em>//2.手动模式</em>
CloudClient.job().register(<span style="color:#50a14f">"test2"</span>, c -> &#123;
    System.out.println(<span style="color:#50a14f">"Hello test2"</span>);
&#125;);
</code></pre> 
<h3 style="text-align:start">2、为 water-solon-plugin 插件，增加CloudJob规范适配</h3> 
<p style="text-align:start">配置示例</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">demojob</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">demo</span>
  
<span style="color:#986801">solon.cloud.water:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">water</span>
</code></pre> 
<p style="text-align:start">应用示例</p> 
<pre style="text-align:start"><code class="language-java"><em>//1.注解模式</em>
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">JobBeanDemo2</span> &#123;
    <span style="color:#4078f2">@CloudJob</span>(<span style="color:#50a14f">"JobBeanDemo2-1"</span>)
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span>()&#123;
        System.out.println(<span style="color:#50a14f">"JobBeanDemo2-1"</span>);
    &#125;
&#125;

<em>//2.手动模式</em>
CloudClient.job().register(<span style="color:#50a14f">"test2"</span>, c -> &#123;
    System.out.println(<span style="color:#50a14f">"Hello test2"</span>);
&#125;);
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
            