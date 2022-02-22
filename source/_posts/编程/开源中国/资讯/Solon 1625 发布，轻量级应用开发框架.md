
---
title: 'Solon 1.6.25 发布，轻量级应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6481'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 18:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6481'
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
 <li>插件 solon.boot.smarthttp，升级 smart-http 到 1.1.11</li> 
 <li>插件 solon.socketd.client.smartsocket，升级 smart-socket 到 1.5.15</li> 
 <li>添加 SolonApp::pluginPop 接口</li> 
</ul> 
<p style="color:#24292e; text-align:start">示例</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        SolonApp app = Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>)</span>;

        <em>//动态插入插件</em>
        app.plug(<span style="color:#a626a4">new</span> PluginImpl()); 

        <em>//动态拨出插件</em>
        PluginEntity tmp = app.pluginPop(PluginImpl<span>.<span style="color:#a626a4">class</span>)</span>;
        <span style="color:#a626a4">if</span>(tmp != <span style="color:#a626a4">null</span>) &#123;
            <em>//停掉插件</em>
            tmp.prestop();
            tmp.stop();
        &#125;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>调整 solon.schedule 调度策略</li> 
 <li>调整 water job 的 name 处理</li> 
 <li>调整 @CacheRemove key 为 keys</li> 
 <li>调整 @Param 的作用范围，只能作用于参数</li> 
 <li>新增 @Header 以支持头变量注入</li> 
</ul> 
<p style="color:#24292e; text-align:start">示例</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"hello"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">hello</span><span>(@Header(<span style="color:#50a14f">"Token"</span>)</span> String token)</span>&#123;
    
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>新增 @PathVar 以方便文档框架识别</li> 
 <li>新增 配置对复杂结构类的支持</li> 
</ul> 
<p style="color:#24292e; text-align:start">配置</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">jap:</span>
  <span style="color:#986801">issuer:</span> <span style="color:#50a14f">test</span>
  <span style="color:#986801">japConfig:</span>
    <span style="color:#986801">sso:</span> <span style="color:#0184bb">true</span>
    <span style="color:#986801">ssoConfig:</span>
      <span style="color:#986801">cookieDomain:</span> <span style="color:#50a14f">https://lab.test.cn</span>
  <span style="color:#986801">simpleConfig:</span>
    <span style="color:#986801">credentialEncryptSalt:</span> <span style="color:#50a14f">xxxxx</span>
  <span style="color:#986801">credentials:</span>
    <span style="color:#986801">gitee:</span>
      <span style="color:#986801">clientId:</span> <span style="color:#50a14f">aaaaaaaaaa</span>
      <span style="color:#986801">clientSecret:</span> <span style="color:#50a14f">bbbbbbbbbb</span>
      <span style="color:#986801">redirectUri:</span> <span style="color:#50a14f">http://127.0.0.1:8443/social/login/gitee</span>
  <span style="color:#986801">callbacks:</span>
    <span style="color:#4078f2">-</span> <span style="color:#50a14f">/</span>
</code></pre> 
<p style="color:#24292e; text-align:start">注入到复杂结构</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Inject</span>(<span style="color:#50a14f">"$&#123;jap&#125;"</span>)
<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span></span>&#123;
    <span style="color:#a626a4">public</span> String issuer;
    <span style="color:#a626a4">public</span> JapConfig japConfig;
    <span style="color:#a626a4">public</span> List<String> callbacks;
&#125;
</code></pre> 
<h3 style="text-align:start">快速了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul>
                                        </div>
                                      
</div>
            