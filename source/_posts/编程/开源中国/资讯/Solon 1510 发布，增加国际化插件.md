
---
title: 'Solon 1.5.10 发布，增加国际化插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2273'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 09:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2273'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个轻量的Java基础开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Job、Micro service、WebSocket、Socket 等多种开发模式。短小而精悍！</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h3 style="text-align:start">快速了解Solon的材料：</h3> 
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
<h4 style="text-align:start">本次版本主要变化：</h4> 
<h3 style="text-align:start">1、增加 solon.i18n 插件</h3> 
<ul> 
 <li>使用国际化工具，获取默认消息</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> &#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/demo/"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">demo</span>(Context ctx) &#123;
        <span style="color:#a626a4">return</span> I18nUtil.getMessage(ctx, <span style="color:#50a14f">"login.title"</span>);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>使用注解，为视图模板提供支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@I</span>18n(<span style="color:#50a14f">"i18n.login"</span>)
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">LoginController</span> &#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/login/"</span>)
    <span style="color:#a626a4">public</span> ModelAndView <span style="color:#4078f2">login</span>() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> ModelAndView(<span style="color:#50a14f">"login.ftl"</span>);
    &#125;
&#125;
</code></pre> 
<p style="text-align:start">在各种模板里的使用方式：</p> 
<p style="text-align:start">beetl::</p> 
<pre style="text-align:start"><code class="language-html">i18n::$&#123;i18n["login.title"]&#125;
i18n::$&#123;@i18n.get("login.title")&#125;
i18n::$&#123;@i18n.getAndFormat("login.title",12,"a")&#125;
</code></pre> 
<p style="text-align:start">enjoy::</p> 
<pre style="text-align:start"><code class="language-html">i18n::#(i18n.get("login.title"))
i18n::#(i18n.getAndFormat("login.title",12,"a"))
</code></pre> 
<p style="text-align:start">freemarker::</p> 
<pre style="text-align:start"><code class="language-html">i18n::$&#123;i18n["login.title"]&#125;
i18n::$&#123;i18n.get("login.title")&#125;
i18n::$&#123;i18n.getAndFormat("login.title",12,"a")&#125;
</code></pre> 
<p style="text-align:start">thymeleaf::</p> 
<pre style="text-align:start"><code class="language-html">i18n::<<span style="color:#e45649">span</span> <span style="color:#986801">th:text</span>=<span style="color:#50a14f">'$&#123;i18n.get("login.title")&#125;'</span>></<span style="color:#e45649">span</span>>
i18n::<<span style="color:#e45649">span</span> <span style="color:#986801">th:text</span>=<span style="color:#50a14f">'$&#123;i18n.getAndFormat("login.title",12,"a")&#125;'</span>></<span style="color:#e45649">span</span>>
</code></pre> 
<p style="text-align:start">velocity::</p> 
<pre style="text-align:start"><code class="language-html">i18n::$&#123;i18n["login.title"]&#125;
i18n::$&#123;i18n.get("login.title")&#125;
i18n::$&#123;i18n.getAndFormat("login.title",12,"a")&#125;
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
                                        </div>
                                      
</div>
            