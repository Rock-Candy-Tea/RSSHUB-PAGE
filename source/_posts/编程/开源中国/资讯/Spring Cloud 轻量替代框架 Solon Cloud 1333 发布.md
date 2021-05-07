
---
title: 'Spring Cloud 轻量替代框架 Solon Cloud 1.3.33 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8736'
author: 开源中国
comments: false
date: Fri, 07 May 2021 13:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8736'
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
<h3 style="text-align:start">1、Solon logging 增加记录器级别控制</h3> 
<p style="text-align:start">例</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.logging.logger:</span>
  <span style="color:#50a14f">"org.aaa.*"</span><span style="color:#50a14f">:</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">INFO</span>
  <span style="color:#986801">"org.xxx.xxx.yyy":</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">INFO</span>
</code></pre> 
<h3 style="text-align:start">2、Solon cloud 增加 zookeeper-solon-plugin 组件，提供配置与注册服务</h3> 
<p style="text-align:start">配置好后，使用标准的 Solon cloud 注解与接口即可使用。配置示例：</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.cloud.zookeeper:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"localhost:2181"</span>
  <span style="color:#986801">config:</span>
    <span style="color:#986801">load:</span> <span style="color:#50a14f">"test.properties"</span>

<em>#zk日志太猛了，限制一下</em>
<span style="color:#986801">solon.logging.logger:</span>
  <span style="color:#50a14f">"org.apache.zookeeper.*"</span><span style="color:#50a14f">:</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">"WARN"</span>
</code></pre> 
<p style="text-align:start">代码使用：</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> &#123;
    <span style="color:#4078f2">@Bean</span>
    <span style="color:#a626a4">public</span> DataSource <span style="color:#4078f2">ds</span>(@CloudConfig(<span style="color:#50a14f">"$&#123;demo.db1&#125;"</span>) HikariDataSource ds)&#123;
        System.out.println(ds.getUsername() + <span style="color:#50a14f">":"</span> + ds.getJdbcUrl());
        <span style="color:#a626a4">return</span> ds;
    &#125;
&#125;

<em>//手动获取配置：Config cfg = CloudClient.config().pull(Solon.cfg().appGroup(), "demo.db1");</em>
</code></pre> 
<h3 style="text-align:start">3、Solon cloud 增加 snowflake-id-solon-plugin 组件，提供雪花算法ID生成服务</h3> 
<p style="text-align:start">此组件使用应用信息做为 dataId，使用ip:port做为workId。引入包后，可直接通过接口使用</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">long</span> logId = CloudClient.id().generate();
</code></pre> 
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
            