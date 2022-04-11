
---
title: 'Solon 1.6.36 发布，更现代感的应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9946'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 08:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9946'
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
<h3 style="text-align:start">本次主要更新</h3> 
<ul> 
 <li>添加 SocketContext::SessionState 接口支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java">
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@Socket</span>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/hello"</span>)
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>(Context ctx)</span></span>&#123;
        <span style="color:#a626a4">if</span>(ctx.session(<span style="color:#50a14f">"user"</span>) == <span style="color:#a626a4">null</span>)&#123;
            ctx.sessionSet(<span style="color:#50a14f">"user"</span>, <span style="color:#50a14f">"noear"</span>);
        &#125;
        
        <span style="color:#a626a4">return</span> ctx.session(<span style="color:#50a14f">"user"</span>);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>添加 Session::pathNew() 接口支持</li> 
 <li>添加 SolonApp::listenBefore, SolonApp::listenAfter 接口，以提供 Listener 过滤的支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span> -> </span>&#123;
            app.listenBefore(<span style="color:#a626a4">new</span> ListenerEmpty() &#123;
                <span style="color:#4078f2">@Override</span>
                <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">onOpen</span><span>(Session session)</span> </span>&#123;
                    <em>//修改ws的监听路径</em>
                    <span style="color:#a626a4">if</span> (session.path().startsWith(<span style="color:#50a14f">"/xx/"</span>)) &#123;
                        session.pathNew(session.path().substring(<span style="color:#986801">4</span>));
                    &#125;
                &#125;
            &#125;);
        &#125;);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>添加 sa-token-solon-plugin 插件对 dao 适配[实验方案] 
  <ul> 
   <li>SaTokenDaoOfRedis</li> 
   <li>SaTokenDaoOfSession</li> 
  </ul> </li> 
 <li>新增 mybatis-plus-extension-solon-plugin 插件</li> 
 <li>插件 solon.extend.sessionstate.jwt 呼略 ServiceConfigurationError 抛出</li> 
 <li>添加 CloudJobInterceptor，提供 job 的拦截机制</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Slf</span>4j
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">CloudJobInterceptorImpl</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudJobInterceptor</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">doIntercept</span><span>(Job job, CloudJobHandler handler)</span> <span style="color:#a626a4">throws</span> Throwable </span>&#123;
        <span style="color:#a626a4">long</span> start = System.currentTimeMillis();
        <span style="color:#a626a4">try</span> &#123;
            handler.handle(job.getContext());
        &#125; <span style="color:#a626a4">catch</span> (Throwable e) &#123;
            <em>//记录带标签的日志</em>
            TagsMDC.tag0(<span style="color:#50a14f">"job"</span>);
            TagsMDC.tag1(job.getName());
            log.error(<span style="color:#50a14f">"&#123;&#125;"</span>, e);
            
            <span style="color:#a626a4">throw</span> e; <em>//别吃掉</em>
        &#125; <span style="color:#a626a4">finally</span> &#123;
            <em>//记录一个内部处理的花费时间</em>
            <span style="color:#a626a4">long</span> timespan = System.currentTimeMillis() - start;
            CloudClient.metric().addMeter(Solon.cfg().appName(), <span style="color:#50a14f">"job"</span>, timespan);
        &#125;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>添加 CloudEventInterceptor，提供 event 的拦截机制</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//CloudEventInterceptor 与 CloudJobInterceptor 起到类型的作用</em>
</code></pre> 
<ul> 
 <li>调整 Gateway 的缺省处理设定方式</li> 
 <li>调整 CloudJobHandler 为 job 的强制接口，之前 Handler 即可</li> 
 <li>调整 HttpUtils 增加短处理和长处理的切换支持</li> 
</ul> 
<h3 style="text-align:start">进一步了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul>
                                        </div>
                                      
</div>
            