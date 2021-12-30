
---
title: 'Solon 1.6.11 发布，类似 Spring 的生态体系'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1747'
author: 开源中国
comments: false
date: Thu, 30 Dec 2021 11:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1747'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">关于官网</h3> 
<p style="color:#24292e; text-align:start">千呼万唤始出来：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a><span> </span>。整了一个月多了，总体样子有了。。。还得不断接着整！</p> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量级应用开发框架。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。短小而精悍！</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放的原则</strong></li> 
 <li>力求，<strong>更小、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前已有近130个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">关于 Solon Cloud</h3> 
<p style="color:#24292e; text-align:start">Solon Cloud 定义了一系列分布式开发的接口标准和配置规范，相当于DDD模式里的防腐层概念。是 Solon 的微服务架构模式开发解决方案。</p> 
<h3 style="text-align:start">关于本次更新</h3> 
<ul> 
 <li>增加 ModelAndView 注入支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/hello"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">hello</span><span>(ModelAndView mv)</span></span>&#123;
        <span style="color:#a626a4">return</span> mv.view(<span style="color:#50a14f">"hello.ftl"</span>);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>新增 solon.schedule 插件，为 Spring 迁移用户提供一些便利（目前已有4个本地定时任务插件，2个分布式定时任务插件）</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>// 启用 Scheduled 注解的任务</em>
<span style="color:#4078f2">@EnableScheduling</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">JobApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        Solon.start(JobApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>)</span>;
    &#125;
&#125;

<em>// 基于 Runnable 接口的模式</em>
<span style="color:#4078f2">@Scheduled</span>(fixedRate = <span style="color:#986801">1000</span> * <span style="color:#986801">3</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">Job1</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Runnable</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">run</span><span>()</span> </span>&#123;
        System.out.println(<span style="color:#50a14f">"我是 Job1 （3s）"</span>);
    &#125;
&#125;

<em>// 基于 Method 的模式</em>
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">JobBean</span> </span>&#123;
    <span style="color:#4078f2">@Scheduled</span>(fixedRate = <span style="color:#986801">1000</span> * <span style="color:#986801">3</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">job11</span><span>()</span></span>&#123;
        System.out.println(<span style="color:#50a14f">"我是 job11 （3s）"</span>);
    &#125;

    <span style="color:#4078f2">@Scheduled</span>(cron = <span style="color:#50a14f">"0/10 * * * * ? *"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">job12</span><span>()</span></span>&#123;
        System.out.println(<span style="color:#50a14f">"我是 job12 （0/10 * * * * ? *）"</span>);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 solon.boot.jlhttp 插件上传的文件名可能会乱码的问题</li> 
 <li>升级 beetlsql 到 3.12.5</li> 
 <li>升级 weed3 到 3.4.12</li> 
 <li>升级 snack3 到 3.2.6</li> 
 <li>插件 quartz-solon-plugin 排除关于 quartz 对线程池的依赖</li> 
</ul> 
<h3 style="text-align:start">快速了解 Solon</h3> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></p>
                                        </div>
                                      
</div>
            