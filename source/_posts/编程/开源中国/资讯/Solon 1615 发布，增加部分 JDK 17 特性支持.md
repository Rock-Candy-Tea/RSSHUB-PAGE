
---
title: 'Solon 1.6.15 发布，增加部分 JDK 17 特性支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6299'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 12:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6299'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">关于官网</h3> 
<p style="color:#24292e; text-align:start">千呼万唤始出来：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a><span> </span>。整了一个月多了。。。还得不断接着整！</p> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量级应用开发框架。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。短小而精悍！</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放的原则</strong></li> 
 <li>力求，<strong>更小、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前已有近130个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">关于 Solon Cloud</h3> 
<p style="color:#24292e; text-align:start">Solon Cloud 定义了一系列分布式开发的接口标准和配置规范，相当于DDD模式里的防腐层概念。是 Solon 的微服务架构模式开发解决方案。</p> 
<h3 style="text-align:start">本次主要更新</h3> 
<ul> 
 <li>增加对 kotlin data class 和 jdk14+ record 的序列化、反序列化及注入支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span><span style="color:#a626a4">public</span> record <span style="color:#4078f2">User</span><span>(String username, Integer age)</span> </span>&#123; &#125;

<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>(User user)</span></span>&#123;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>@Service 增加 name, typed 属性</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//通过 name 指定 bean name；通过 typed 注册类型 bean，即 DemoService 的默认实现</em>
<span style="color:#4078f2">@Service</span>(name=<span style="color:#50a14f">"DemoService-CN"</span>, typed=<span style="color:#a626a4">true</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoServiceCnImpl</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">DemoService</span></span>&#123;

&#125;

<em>//上面这种方式需要“编译时”确定默认bean（注：当没有name时，都是默认bean）</em>
<em>//</em>
<em>//基于Solon的特性，还有一种“运行时”确定的方案</em>
<em>//</em>
<span style="color:#4078f2">@Service</span>(name=<span style="color:#50a14f">"DemoService-CN"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoServiceCnImpl</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">DemoService</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#4078f2">DemoServiceCnImpl</span><span>()</span></span>&#123;
        <span style="color:#a626a4">if</span>(<span style="color:#50a14f">"CN"</span>.equals(Solon.cfg().get(<span style="color:#50a14f">"datacenter.region"</span>, <span style="color:#50a14f">"CN"</span>)))&#123;
            Aop.wrapAndPut(DemoService<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">this</span>)</span>;
        &#125;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>优化 sqltoy-solon-plugin 插件，增加便利的多数据源控制和切换</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Service</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span></span>&#123;
    <span style="color:#4078f2">@Db</span>
    SqlToyLazyDao dao1;
    
    <span style="color:#4078f2">@Db</span>(<span style="color:#50a14f">"db2"</span>)
    SqlToyLazyDao dao2;
&#125;
</code></pre> 
<ul> 
 <li>新增 solon.extend.async 插件</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Service</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">AsyncTask</span> </span>&#123;
    <em>//会被异步运行（提交到异步执行器运行）//不要有返回值（返回也拿不到）</em>
    <span style="color:#4078f2">@Async</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>(String hint)</span></span>&#123;
        System.out.println(Thread.currentThread().getName());
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 当主应用配置有变量时，应用环境配置无法替换的问题</li> 
 <li>优化 Aop.beanForeach ，进行去重处理</li> 
 <li>增加 三种日期格式自动解析</li> 
</ul> 
<h3 style="text-align:start">快速了解 Solon</h3> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></p>
                                        </div>
                                      
</div>
            