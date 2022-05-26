
---
title: 'Solon 1.8.0 发布，云原生微服务开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-61f087bb2c62d2a018005990c43b4e2dfe6.png'
author: 开源中国
comments: false
date: Thu, 26 May 2022 00:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-61f087bb2c62d2a018005990c43b4e2dfe6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目</h3> 
<ul> 
 <li>启动快 5 ～ 10 倍</li> 
 <li>qps 高 2～ 3 倍</li> 
 <li>运行时内存节省 1/3 ~ 1/2</li> 
 <li>打包可以缩小到 1/2 ~ 1/10（比如，90Mb 的变成了 9Mb）</li> 
 <li>基于 app.name 进行注册发现 与 k8s svc 相互对应</li> 
 <li>支持 Service Mesh 架构部署方案</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个更现代感的应用开发框架，轻量、开放生态型的。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放 + 生态的原则</strong></li> 
 <li>力求，<strong>更小、更少、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前有近<strong>130</strong>个生态插件，含盖了日常开发的各种需求：</p> 
<p style="color:#24292e; text-align:start"><img alt height="591" src="https://oscimg.oschina.net/oscnet/up-61f087bb2c62d2a018005990c43b4e2dfe6.png" width="717" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">本次主要更新内容</h3> 
<ul> 
 <li>新增 solon.extend.hotplug 插件（提供业务插件 '热插拨' 和 '热管理' 支持）</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> &#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> &#123;
        Solon.start(App.class, args, app -> &#123;
            <em>//添加待管理的插件</em>
            PluginManager.add(<span style="color:#50a14f">"add1"</span>, <span style="color:#50a14f">"/x/x/x.jar"</span>);
            PluginManager.add(<span style="color:#50a14f">"add2"</span>, <span style="color:#50a14f">"/x/x/x2.jar"</span>);
     
            app.get(<span style="color:#50a14f">"start"</span>, ctx -> &#123;
                <em>//启动插件</em>
                PluginManager.start(<span style="color:#50a14f">"add1"</span>);
                ctx.output(<span style="color:#50a14f">"OK"</span>);
            &#125;);
            
            app.get(<span style="color:#50a14f">"stop"</span>, ctx -> &#123;
                <em>//停止插件</em>
                PluginManager.stop(<span style="color:#50a14f">"add1"</span>);
                ctx.output(<span style="color:#50a14f">"OK"</span>);
            &#125;);
        &#125;);
    &#125;
&#125;
</code></pre> 
<p style="color:#24292e; text-align:start">更多介绍看官网的：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2Farticle%2F262" target="_blank">solon.extend.hotplug</a></p> 
<ul> 
 <li>调整 AopContext ，更具隔离性</li> 
 <li>调整 AopContext::beanOnloaded 参数由 Runnable 改为：Consumer</li> 
 <li>调整 Plugin::start 参数由 SolonApp 改为：AopContext</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Plugin1Impl</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Plugin</span> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">start</span><span>(AopContext context)</span> &#123;
        <em>//通过当前上下文扫描，具有隔离性</em>
        context.beanScan(Plugin1Impl.class);
        
        context.beanOnloaded(ctx->&#123;
            <em>//回调有上下文信息，方便做多插件可复用的设计</em>
        &#125;);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 @Cache 在函数里有逗号时无法删除缓存的问题</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span> &#123;
    <em>/**
     * 执行结果缓存10秒，使用 key=test_$&#123;label&#125; 并添加 test 标签
     * */</em>
    <span style="color:#4078f2">@Cache(key="test_$&#123;label&#125;", tags = "test" , seconds = 10)</span>
    <span style="color:#4078f2">@Mapping("/cache/")</span>
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">test</span><span>(<span style="color:#986801">int</span> label)</span> &#123;
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> <span style="color:#c18401">Date</span>();
    &#125;

    <em>/**
     * 执行后，清除 标签为 test  的所有缓存
     * */</em>
    <span style="color:#4078f2">@CacheRemove(tags = "test")</span>
    <span style="color:#4078f2">@Mapping("/cache/clear")</span>
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">clear</span><span>()</span> &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"清除成功(其实无效)-"</span> + <span style="color:#a626a4">new</span> <span style="color:#c18401">Date</span>();
    &#125;

    <em>/**
     * 执行后，更新 key=test_$&#123;label&#125;  的缓存
     * */</em>
    <span style="color:#4078f2">@CachePut(key = "test_$&#123;label&#125;")</span>
    <span style="color:#4078f2">@Mapping("/cache/clear2")</span>
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">clear2</span><span>(<span style="color:#986801">int</span> label)</span> &#123;
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> <span style="color:#c18401">Date</span>();
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 Gateway 对默认接口识别失效的问题</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Mapping("/api/v3/app/**")</span>
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">ApiGatewayV3</span> <span style="color:#a626a4">extends</span> <span style="color:#c18401">UapiGateway</span> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">protected</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">register</span><span>()</span> &#123;
        filter(<span style="color:#a626a4">new</span> <span style="color:#c18401">BreakerFilter</span>()); <em>//融断</em>

        before(<span style="color:#a626a4">new</span> <span style="color:#c18401">StartHandler</span>()); <em>//开始计时</em>
        before(<span style="color:#a626a4">new</span> <span style="color:#c18401">ParamsParseHandler</span>()); <em>//参数解析</em>
        before(<span style="color:#a626a4">new</span> <span style="color:#c18401">ParamsSignCheckHandler</span>(<span style="color:#a626a4">new</span> <span style="color:#c18401">Md5Encoder</span>())); <em>//参数签名较验</em>
        before(<span style="color:#a626a4">new</span> <span style="color:#c18401">ParamsRebuildHandler</span>(<span style="color:#a626a4">new</span> <span style="color:#c18401">AesDecoder</span>())); <em>//参数重构</em>

        after(<span style="color:#a626a4">new</span> <span style="color:#c18401">OutputBuildHandler</span>(<span style="color:#a626a4">new</span> <span style="color:#c18401">AesEncoder</span>())); <em>//输出构建</em>
        after(<span style="color:#a626a4">new</span> <span style="color:#c18401">OutputSignHandler</span>(<span style="color:#a626a4">new</span> <span style="color:#c18401">Md5Encoder</span>())); <em>//输出签名</em>
        after(<span style="color:#a626a4">new</span> <span style="color:#c18401">OutputHandler</span>()); <em>//输出</em>
        after(<span style="color:#a626a4">new</span> <span style="color:#c18401">EndBeforeLogHandler</span>()); <em>//日志</em>
        after(<span style="color:#a626a4">new</span> <span style="color:#c18401">EndHandler</span>(<span style="color:#50a14f">"v3.api.app"</span>)); <em>//结束计时</em>

        <em>//添加一批具体的接口处理Bean</em>
        addBeans(bw -> <span style="color:#50a14f">"api"</span>.equals(bw.tag()));
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 rocketmq-solon-plugin ，消费异常时仍返回成功的问题</li> 
 <li>优化 rabbitmq-solon-plugin ，消费异常时的处理</li> 
</ul> 
<h3 style="text-align:start">进一步了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul> 
<h3 style="text-align:start">项目地址</h3> 
<ul> 
 <li>gitee：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fsolon" target="_blank">https://github.com/noear/solon</a></li> 
 <li>website:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a></li> 
</ul>
                                        </div>
                                      
</div>
            