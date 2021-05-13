
---
title: 'Spring Boot & Cloud 轻量替代框架 Solon 1.3.37 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4755'
author: 开源中国
comments: false
date: Thu, 13 May 2021 12:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4755'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Solon 是一个微型的Java开发框架。强调，<strong>克制 + 简洁 + 开放的原则</strong>；力求，<strong>更小、更快、更自由的体验</strong>。支持：RPC、REST API、MVC、Micro service、WebSocket、Socket 等多种开发模式。</p> 
<p style="text-align:start">Solon Cloud 是一系列的接口标准和配置规范，算是 Solon 的分布式开发套件方案。</p> 
<h4 style="text-align:start">快速了解Solon的材料：</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《Solon Cloud 分布式服务开发套件清单，感觉受与 Spring Cloud 的不同》</a></p> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《Solon 的想法与架构笔记》</a></p> 
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
<h3 style="text-align:start">1、增加 solon.extend.jsr303 组件，支持 jsr303 bean验证能力</h3> 
<p style="text-align:start">Solon 原有的验证体系是基于 Context 的，基于方法或参数的验证。现在算是补齐了 Bean 或 Model 的验证能力。</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Valid</span>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">ValidController</span> &#123;
    <em>//这是基于 context 的验证体系（可以批量验证参数）</em>
    <span style="color:#4078f2">@NotZero</span>(&#123;<span style="color:#50a14f">"val1"</span>, <span style="color:#50a14f">"val2"</span>&#125;)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"nzero"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">nzero</span>(<span style="color:#a626a4">int</span> val1, <span style="color:#a626a4">int</span> val2) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;

    <em>//这也是基于 context 的验证体系</em>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"size"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">size</span>(@Length(min = <span style="color:#986801">2</span>, max = <span style="color:#986801">5</span>, message = <span style="color:#50a14f">"测试"</span>) String val1,
                       @<span style="color:#4078f2">Length</span>(min = <span style="color:#986801">2</span>, max = <span style="color:#986801">5</span>, message = <span style="color:#50a14f">"测试"</span>) String val2) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;

    <em>//这是基于 bean 的验证体系（@Validated，这个注解加上代表要验证这个模型参数）</em>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"bean"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">bean</span>(@Validated ValidModel model) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"OK"</span>;
    &#125;
&#125;

<em>//申明可验证的模型</em>
<span style="color:#4078f2">@Data</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">ValidModel</span> &#123;
    <span style="color:#4078f2">@NotBlank</span>(message = <span style="color:#50a14f">"手机号不能为空"</span>)
    <span style="color:#a626a4">private</span> String mobile;

    <span style="color:#4078f2">@NotBlank</span>(message = <span style="color:#50a14f">"密码不能为空"</span>)
    <span style="color:#a626a4">private</span> String password;
&#125;
</code></pre> 
<h3 style="text-align:start">2、增加 solon.cache.spymemcached 分布式缓存组件，提供 solon cache 的实现支持</h3> 
<p style="text-align:start">配置：（Solon 的缓存注解，默认是不需要配置缓存服务的。默认会提供本地缓存服务）</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">demoapp</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">demo</span>
  
<span style="color:#986801">cache1:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">memcached.water.io:11211</span>  <em>#具体需要哪些配置，可以看下 MemCacheService 的类实现</em>
  <span style="color:#986801">user:</span> <span style="color:#50a14f">memcached</span>
</code></pre> 
<p style="text-align:start">代码：</p> 
<pre style="text-align:start"><code class="language-java"><em>//组件配置</em>
<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> &#123;
    <span style="color:#4078f2">@Bean</span>
    <span style="color:#a626a4">public</span> CacheService <span style="color:#4078f2">cache</span>(@Inject(<span style="color:#50a14f">"$&#123;cache1&#125;"</span>) MemCacheService cache)&#123;
        <span style="color:#a626a4">return</span> cache;
    &#125;
&#125;

<em>//使用</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">CacheController</span> &#123;
    <em>/**
     * 执行结果缓存10秒，并添加 test_$&#123;label&#125; 和 test1 标签
     * */</em>
    <span style="color:#4078f2">@Cache</span>(tags = <span style="color:#50a14f">"test_$&#123;label&#125;,test1"</span> , seconds = <span style="color:#986801">60</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/cache/"</span>)
    <span style="color:#a626a4">public</span> Date <span style="color:#4078f2">test</span>(<span style="color:#a626a4">int</span> label) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> Date();
    &#125;

    <em>/**
     * 执行后，清除 标签为 test  的缓存（不过，目前没有 test 的示签...）
     * */</em>
    <span style="color:#4078f2">@CachePut</span>(tags = <span style="color:#50a14f">"test1"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/cache/update"</span>)
    <span style="color:#a626a4">public</span> Date <span style="color:#4078f2">update</span>() &#123;
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> Date();
    &#125;

    <em>/**
     * 执行后，清除 标签为 test_$&#123;label&#125;  的缓存
     * */</em>
    <span style="color:#4078f2">@CacheRemove</span>(tags = <span style="color:#50a14f">"test_$&#123;label&#125;"</span>)
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/cache/remove"</span>)
    <span style="color:#a626a4">public</span> String <span style="color:#4078f2">remove</span>(<span style="color:#a626a4">int</span> label) &#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"清除成功-"</span> + <span style="color:#a626a4">new</span> Date();
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">3、增加 solon.cache.jedis 分布式缓存组件</h3> 
<p style="text-align:start">使用同上</p> 
<h3 style="text-align:start">4、优化 solon.logging 内部结构，扩展更自由</h3> 
<p style="text-align:start">例，配置一个新的日志添加器，指定类名，指定级别：</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.logging.appender:</span>
  <span style="color:#986801">test:</span>
    <span style="color:#986801">class:</span> <span style="color:#50a14f">demo.TestAppender</span>
    <span style="color:#986801">level:</span> <span style="color:#50a14f">TRACE</span>
</code></pre> 
<p style="text-align:start">定义日志添加器：</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">TestAppender</span> <span style="color:#a626a4">extends</span> <span style="color:#c18401">AppenderBase</span> &#123;
    <span style="color:#4078f2">@Override</span>
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">append</span>(LogEvent logEvent) &#123;
        System.out.println(<span style="color:#50a14f">"[Test] "</span> + logEvent.getContent());
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">附：生态组件清单</h3> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>Nami 插件（Solon rpc client）</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">nami插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">nami.coder.fastjson</td> 
   <td style="border-color:#dfe2e5">对<code>fastjson</code>的编解码适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">nami.coder.hessian</td> 
   <td style="border-color:#dfe2e5">对<code>hessian</code>的编解码适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">nami.coder.snack3</td> 
   <td style="border-color:#dfe2e5">对<code>snack3</code>的编解码适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">nami.channel.http.okhttp</td> 
   <td style="border-color:#dfe2e5">对<code>okhttp</code>的通道适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">nami.channel.socketd</td> 
   <td style="border-color:#dfe2e5">对<code>socketd</code>的通道适配（适配后，可使用org.noear:solon.sockted.client.* 做为客户端）</td> 
  </tr> 
 </tbody> 
</table> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>Solon 插件</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">boot插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.jlhttp*</td> 
   <td style="border-color:#dfe2e5">boot插件,对<code>jlhttp</code>适配,提供<code>http</code>服务（不自带session state）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.jetty*</td> 
   <td style="border-color:#dfe2e5">boot插件,对<code>jetty</code>适配,提供<code>http</code>服务（网友@khb提供）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.jetty.jsp</td> 
   <td style="border-color:#dfe2e5">扩展插件,为<code>jetty</code>添加<code>jsp</code>支持（不建议使用jsp）（网友@khb提供）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.undertow*</td> 
   <td style="border-color:#dfe2e5">boot插件,对<code>undertow</code>适配,提供<code>http</code>服务（网友@tyk提供）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.websocket</td> 
   <td style="border-color:#dfe2e5">boot插件,对<code>java-websocket</code>适配，提供<code>websocket</code>服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.undertow.jsp</td> 
   <td style="border-color:#dfe2e5">扩展插件,为<code>undertow</code>添加<code>jsp</code>支持（不建议使用jsp）（网友@tyk提供）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">静态文件支持插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.staticfiles</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加静态文件支持（监视 resources/static 文件夹）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">切面支持插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.aspect</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加Dao、Service注解支持；进而支持事务和缓存注解</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">数据操作支持插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.data</td> 
   <td style="border-color:#dfe2e5">扩展插件,实现事务和缓存的注解支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">验证支持插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.validation</td> 
   <td style="border-color:#dfe2e5">扩展插件,实现验证的注解支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Yaml配置支持插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.properties.yaml</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加yml配置文件支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Data插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.data</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加事件（@Tran）、缓存（@Cache）支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Cloud插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.cloud</td> 
   <td style="border-color:#dfe2e5">扩展插件, 添加Solon Cloud 的接口定义及配置规范</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Validation插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.validation</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加验证（@Valid）支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Cache插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.cache.spymemcached</td> 
   <td style="border-color:#dfe2e5">扩展插件,完成memcached的缓存服务适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.solon.cache.jedis</td> 
   <td style="border-color:#dfe2e5">扩展插件,完成redis的缓存服务适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">jsr插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.jsr303</td> 
   <td style="border-color:#dfe2e5">扩展插件,完成jsr303 bean 验证支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.jsr330</td> 
   <td style="border-color:#dfe2e5">扩展插件,完成jsr330 组件与注入支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">跨域插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.cors</td> 
   <td style="border-color:#dfe2e5">扩展插件,完成web跨域注解支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Session插件::</td> 
   <td style="border-color:#dfe2e5">说明（可将boot插件的session state服务，自动换掉）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.sessionstate.jwt</td> 
   <td style="border-color:#dfe2e5">扩展插件,分布式<code>session</code>（基于<code>jwt</code>构建）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.sessionstate.local</td> 
   <td style="border-color:#dfe2e5">扩展插件,本地<code>session</code></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.extend.sessionstate.redis</td> 
   <td style="border-color:#dfe2e5">扩展插件,分布式<code>session</code>（其于<code>redis</code>构建）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">日志插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.logging</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加日志支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.logging.impl</td> 
   <td style="border-color:#dfe2e5">扩展插件,添加Slf4j日志支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">序列化插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.serialization.fastjson*</td> 
   <td style="border-color:#dfe2e5">序列化插件，对 <code>fastjson</code> 适配，提供<code>json</code>视图输出 或 序列化输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.serialization.snack3*</td> 
   <td style="border-color:#dfe2e5">序列化插件，对 <code>snack3</code> 适配，提供<code>json</code>视图输出 或 序列化输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.serialization.hession*</td> 
   <td style="border-color:#dfe2e5">序列化插件，对 <code>hession</code> 适配，提供 <code>hession</code> 序列化输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.serialization.jackson</td> 
   <td style="border-color:#dfe2e5">序列化插件，对 <code>jackson</code> 适配，提供<code>json</code>视图输出 或 序列化输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.serialization.protostuff</td> 
   <td style="border-color:#dfe2e5">序列化插件，对 <code>protostuff</code> 适配，提供<code>protostuff</code>视图输出 或 序列化输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">视图插件::</td> 
   <td style="border-color:#dfe2e5">说明（可置多个视图插件）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.view.freemarker*</td> 
   <td style="border-color:#dfe2e5">视图插件，对 <code>freemarker</code> 适配，提供<code>html</code>视图输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.view.jsp</td> 
   <td style="border-color:#dfe2e5">视图插件，对 <code>jsp</code> 适配，提供<code>html</code>视图输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.view.velocity</td> 
   <td style="border-color:#dfe2e5">视图插件，对 <code>velocity</code> 适配，提供<code>html</code>视图输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.view.thymeleaf</td> 
   <td style="border-color:#dfe2e5">视图插件，对 <code>thymeleaf</code> 适配，提供<code>html</code>视图输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.view.beetl</td> 
   <td style="border-color:#dfe2e5">视图插件，对 <code>beetl</code> 适配，提供<code>html</code>视图输出</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.view.enjoy</td> 
   <td style="border-color:#dfe2e5">视图插件，对 <code>enjoy</code> 适配，提供<code>html</code>视图输出</td> 
  </tr> 
 </tbody> 
</table> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>Solon SocketD 插件</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">SocketD boot插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.socketd.jdksocket</td> 
   <td style="border-color:#dfe2e5">sockted boot插件,对<code>jdksocket</code>适配，提供<code>socketd</code>服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.socketd.netty</td> 
   <td style="border-color:#dfe2e5">sockted boot插件,对<code>netty</code>适配，提供<code>socketd</code>服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.socketd.rsocket</td> 
   <td style="border-color:#dfe2e5">sockted boot插件,对<code>rsocket</code>适配，提供<code>socketd</code>服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.socketd.smartsocket</td> 
   <td style="border-color:#dfe2e5">sockted boot插件,对<code>smart-socket</code>适配，提供<code>socketd</code>服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.boot.socketd.websocket</td> 
   <td style="border-color:#dfe2e5">sockted boot插件,对<code>websocket</code>适配，提供<code>socketd</code>服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">SocketD client 插件::</td> 
   <td style="border-color:#dfe2e5">说明</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.sockted</td> 
   <td style="border-color:#dfe2e5">扩展插件,sockted 协议的编解码、会话等基础支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.sockted.client.jdksocket</td> 
   <td style="border-color:#dfe2e5">扩展插件,sockted 协议的 jdksocket 客户端适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.sockted.client.netty</td> 
   <td style="border-color:#dfe2e5">扩展插件,sockted 协议的 netty 客户端适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.sockted.smartsocket</td> 
   <td style="border-color:#dfe2e5">扩展插件,sockted 协议的 smartsocket 客户端适配</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon.sockted.websocket</td> 
   <td style="border-color:#dfe2e5">扩展插件,sockted 协议的 websocket 客户端适配</td> 
  </tr> 
 </tbody> 
</table> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>其它扩展插件</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:beetlsql-solon-plugin</td> 
   <td style="border-color:#dfe2e5">beetlsql 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:mybatis-solon-plugin</td> 
   <td style="border-color:#dfe2e5">mybatis 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:mybatis-sqlhelper-solon-plugin</td> 
   <td style="border-color:#dfe2e5">mybatis-sqlhelper 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:weed3-solon-plugin</td> 
   <td style="border-color:#dfe2e5">weed3 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:cron4j-solon-plugin</td> 
   <td style="border-color:#dfe2e5">cron4j 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:quartz-solon-plugin</td> 
   <td style="border-color:#dfe2e5">quartz 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:dubbo-solon-plugin</td> 
   <td style="border-color:#dfe2e5">dubbo 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:feign-solon-plugin</td> 
   <td style="border-color:#dfe2e5">feign 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:hasor-solon-plugin</td> 
   <td style="border-color:#dfe2e5">hasor 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:luffy-solon-plugin</td> 
   <td style="border-color:#dfe2e5">luffy 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:sureness-solon-plugin</td> 
   <td style="border-color:#dfe2e5">sureness 适配插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:solon-springboot-starter</td> 
   <td style="border-color:#dfe2e5">springboot 适配插件</td> 
  </tr> 
 </tbody> 
</table> 
<table cellspacing="0" style="width:960px"> 
 <thead> 
  <tr> 
   <th>Solon Cloud 插件</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:consul-solon-plugin</td> 
   <td style="border-color:#dfe2e5">consul 适配插件（支持Solon cloud 配置服务、注册与发现服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:nacos-solon-plugin</td> 
   <td style="border-color:#dfe2e5">nacos 适配插件（支持Solon cloud 配置服务、注册与发现服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:zookeeper-solon-plugin</td> 
   <td style="border-color:#dfe2e5">zookeeper 适配插件（支持Solon cloud 配置服务、注册与发现服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:water-solon-plugin</td> 
   <td style="border-color:#dfe2e5">water 适配插件（支持Solon cloud 配置、注册与发现、事件、日志、跟踪、等服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:rabbitmq-solon-plugin</td> 
   <td style="border-color:#dfe2e5">rabbitmq 适配插件（支持Solon cloud 事件总线服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:rocketmq-solon-plugin</td> 
   <td style="border-color:#dfe2e5">rocketmq 适配插件（支持Solon cloud 事件总线服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:mqtt-solon-plugin</td> 
   <td style="border-color:#dfe2e5">mqtt 适配插件（支持Solon cloud 事件总线服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:kafka-solon-plugin</td> 
   <td style="border-color:#dfe2e5">kafka 适配插件（支持Solon cloud 事件总线服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:guava-solon-plugin</td> 
   <td style="border-color:#dfe2e5">guava 适配插件（支持Solon cloud 融断服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:sentinel-solon-plugin</td> 
   <td style="border-color:#dfe2e5">sentinel 适配插件（支持Solon cloud 融断服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:semaphore-solon-plugin</td> 
   <td style="border-color:#dfe2e5">semaphore 适配插件（支持Solon cloud 融断服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:aliyun-oss-solon-plugin</td> 
   <td style="border-color:#dfe2e5">aliyun-oss 适配插件（支持Solon cloud 分布式文件服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:aws-s3-solon-plugin</td> 
   <td style="border-color:#dfe2e5">aws-s3 适配插件（支持Solon cloud 分布式文件服务）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"> </td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">org.noear:snowflake-id-solon-plugin</td> 
   <td style="border-color:#dfe2e5">snowflake 算法适配插件（支持Solon cloud 分布式ID服务）</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>Solon 入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>Solon Rpc 入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>Solon Cloud 入门教程示例：<a href="https://gitee.com/noear/solon_cloud_demo">https://gitee.com/noear/solon_cloud_demo</a></li> 
 <li>Solon 进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            