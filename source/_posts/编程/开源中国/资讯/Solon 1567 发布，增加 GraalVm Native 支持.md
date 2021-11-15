
---
title: 'Solon 1.5.67 发布，增加 GraalVm Native 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3605'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 17:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3605'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="text-align:start">Solon 已有120个生态扩展插件，此次更新主要为细节打磨：</h4> 
<ul> 
 <li>添加 solon.extend.graalvm 插件，用于适配 graalvm native image 模式</li> 
</ul> 
<pre style="text-align:start"><code class="language-java">从此，solon 进入 graalvm <span style="color:#a626a4">native</span> image 的世界。

感谢开发者：@馒头虫/瓢虫，近<span style="color:#986801">1</span>个月时间的实验和适配。
</code></pre> 
<ul> 
 <li>添加 detector-solon-plugin 插件，用于为健康检测，增加一批预设的探测器（可选：cpu,disk,jvm,memory,os,qps）</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><em>#提供了一批健康探测器（多个以,隔开）
#solon.health.detector: "cpu,os,qps"</em>
<span style="color:#986801">solon.health.detector:</span> <span style="color:#50a14f">"cpu"</span>
</code></pre> 
<p style="color:#24292e; text-align:start">输出示例：</p> 
<pre style="text-align:start"><code class="language-json">#curl http:<em>//localhost:8080/healthz</em>
&#123;
  <span style="color:#986801">"status"</span>: <span style="color:#50a14f">"UP"</span>,
  <span style="color:#986801">"details"</span>: &#123;
    <span style="color:#986801">"cpu"</span>: &#123;
      <span style="color:#986801">"status"</span>: <span style="color:#50a14f">"UP"</span>,
      <span style="color:#986801">"details"</span>: &#123;
        <span style="color:#986801">"ratio"</span>: <span style="color:#986801">53.8</span>
      &#125;
    &#125;
  &#125;
&#125;
</code></pre> 
<ul> 
 <li>添加 solon.extend.hotdev 插件</li> 
</ul> 
<pre style="text-align:start"><code>为开发过程，修改java代自动重新加载，进行尝试。
</code></pre> 
<ul> 
 <li>插件 solon.data 的缓存注解 tags 值，支持返回数据做为模板参数</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">UserService</span></span>&#123;
    <em>/**
     * 获取用户信息
     */</em>
    <span style="color:#4078f2">@Cache</span>(tags = <span style="color:#50a14f">"user_$&#123;userId&#125;,company_bind_$&#123;.company_id&#125;"</span>) <em>//使用返回结果的字段：company_id</em>
    <span><span style="color:#a626a4">public</span> UserDo <span style="color:#4078f2">getUser</span><span>(Long userId)</span> <span style="color:#a626a4">throws</span> SQLException </span>&#123;
        <span style="color:#a626a4">return</span> userMapper.getUser(userId);
    &#125;
    
    <em>/**
     * 根据companyId批量解绑，同时清除与个企业相关的用户缓存
     * <span style="color:#a626a4">@return</span>
     * <span style="color:#a626a4">@throws</span> SQLException
     */</em>
    <span style="color:#4078f2">@CacheRemove</span>(tags = <span style="color:#50a14f">"company_bind_$&#123;companyId&#125;"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">int</span> <span style="color:#4078f2">batchUnbindCompany</span><span>(Long companyId)</span> <span style="color:#a626a4">throws</span> SQLException </span>&#123;
        <span style="color:#a626a4">return</span> userMapper.batchUnbindByCompanyId(companyId);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>插件 solon.i18n 国际化配置支持 key 级别的 默认配置（之前基于文件）</li> 
</ul> 
<pre style="text-align:start"><code>例：一个 key 在 message_cn_ZH 找不到配置，会到 message_cn 找，再没有 到 message 打
</code></pre> 
<ul> 
 <li>插件 solon.i18n 增加过滤器，自动为上下文解析地区</li> 
 <li>插件 water-solon-plugin 升级 water 2.3.2</li> 
 <li>内核 @Bean 增加 index；@Component 增加 index。为特定类型增加位置支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//例：为应用过滤器增加位置</em>
<em>//</em>
<span style="color:#4078f2">@Component</span>(index = <span style="color:#986801">1</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">AppFilterImpl</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Filter</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">doFilter</span><span>(Context ctx, FilterChain chain)</span> <span style="color:#a626a4">throws</span> Throwable </span>&#123;
        chain.doFilter(ctx);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>内核 增加 solon.locale 配置，为系统提供默认地区配置</li> 
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
<h3 style="text-align:start"> </h3> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Api 入门教程示例：<a href="https://gitee.com/noear/solon_api_demo">https://gitee.com/noear/solon_api_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Auth 入门教程示例：<a href="https://gitee.com/noear/solon_auth_demo">https://gitee.com/noear/solon_auth_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon Socketd 入门教程示例：<a href="https://gitee.com/noear/solon_socketd_demo">https://gitee.com/noear/solon_socketd_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            