
---
title: 'Solon 1.7.6 发布，更现代感的应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6899'
author: 开源中国
comments: false
date: Mon, 09 May 2022 09:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6899'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目</h3> 
<ul> 
 <li>启动快 5 ～ 10 倍</li> 
 <li>qps 高 2～ 3 倍</li> 
 <li>运行时内存节省 1/3 ~ 1/2</li> 
 <li>打包可以缩小到 1/2 ~ 1/10（比如，90Mb 的变成了 9Mb）</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个更现代感的应用开发框架，轻量、开放生态型的。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放 + 生态的原则</strong></li> 
 <li>力求，<strong>更小、更少、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前有近<strong>130</strong>个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">本次主要更新内容</h3> 
<ul> 
 <li>添加 jaeger-solon-plugin 插件。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2F255" target="_blank">插件使用说明</a></li> 
 <li>添加 solon.cloud.tracing 插件，做为 jaeger-solon-plugin 和 opentracing-solon-plugin 的公共能力支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//通过基类，为业务处理自动增加‘链路跟踪’的埋点</em>
<span style="color:#4078f2">@Tracing</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">BaseService</span></span>&#123;
    
&#125;

<span style="color:#4078f2">@Service</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">UserService</span> <span style="color:#c18401">extend</span> <span style="color:#c18401">BaseService</span></span>&#123;
    <span><span style="color:#a626a4">public</span> UserDo <span style="color:#4078f2">getUser</span><span>(<span style="color:#a626a4">long</span> userId)</span></span>&#123;
        <span style="color:#a626a4">return</span> ...;
    &#125;
    
    <em>//或者注解到函数上，为操作命名</em>
    <span style="color:#4078f2">@Tracing</span>(<span style="color:#50a14f">"更新用户"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">updateUser</span><span>(<span style="color:#a626a4">long</span> userId, UserDo user)</span></span>&#123;
        <em>//...</em>
    &#125;
&#125;

<em>//注：控制器已由过滤器适配埋点，不需要再埋点</em>
</code></pre> 
<ul> 
 <li>插件 opentracing-solon-plugin 调整为，基于 solon.cloud.tracing 二次构建</li> 
 <li>插件 sa-token-solon-plugin 支持 SaTokenConfig 注入</li> 
 <li>插件 solon-test 调整 HttpUtils。支持超时</li> 
 <li>增加 bodyNew 的应用范围</li> 
 <li>增加 method 拦截器的去重处理</li> 
 <li>取消 window 下彩色打印符输出。window 不支持</li> 
 <li>snack3 升级为：3.2.22。支持 yaml 对象数组注入</li> 
</ul> 
<h3 style="text-align:start">进一步了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            