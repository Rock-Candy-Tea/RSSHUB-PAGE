
---
title: 'Spring Boot 轻量替代框架 Solon 1.3.20 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2215'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 09:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2215'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">Solon 是一个微型的Java开发框架。项目2018年启动，参考过大量前人作品；内核0.1m的身材，超高的跑分，以及良好的使用体验。支持：RPC、REST API、MVC、WebSocket、Socket 等多种开发模式。</p> 
<p style="text-align:start">Solon 强调：克制 + 简洁 + 开放的原则；力求：更小、更快、更自由的体验。</p> 
<h4 style="text-align:start">替代？那有什么异同之处？</h4> 
<p style="text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《Solon 特性简集，相较于 Springboot 有什么区别？》</a></p> 
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
</code></pre> 
<h4 style="text-align:start">本次版本主要变化：</h4> 
<h3 style="text-align:start">1、Solon Cloud 增加分布式文件服务定义： CloudFileService</h3> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">interface</span> <span style="color:#c18401">CloudFileService</span> &#123;
    InputStream <span style="color:#4078f2">getStream</span>(String bucket, String key) <span style="color:#a626a4">throws</span> CloudFileException;
    Result <span style="color:#4078f2">putStream</span>(String bucket, String key, InputStream stream, String streamMime) <span style="color:#a626a4">throws</span> CloudFileException;
    
    InputStream <span style="color:#4078f2">getText</span>(String bucket, String key) <span style="color:#a626a4">throws</span> CloudFileException;
    Result <span style="color:#4078f2">putText</span>(String bucket, String key, String text) <span style="color:#a626a4">throws</span> CloudFileException;
    ...
&#125;
</code></pre> 
<h3 style="text-align:start">2、Solon Cloud 增加适配组件：aliyun-oss-solon-plugin、aws-s3-solon-plugin（适配 CloudFileService）</h3> 
<p style="text-align:start">以 aliyun-oss-solon-plugin 使用为例：</p> 
<ul> 
 <li>配置：</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.cloud.aliyun.oss:</span>  <em># 亚马逊则为：solon.cloud.aws.s3</em>
  <span style="color:#986801">file:</span>
    <span style="color:#986801">bucket:</span> <span style="color:#50a14f">aaa</span>
    <span style="color:#986801">endpoint:</span> <span style="color:#50a14f">bbb.xxx.xxx</span>
    <span style="color:#986801">accessKey:</span> <span style="color:#50a14f">ccc</span>
    <span style="color:#986801">secretKey:</span> <span style="color:#50a14f">ddd</span>
    
<em>#可以通过配置服务动态加载，以灵活切换不同的配置    </em>
<em>#solon.cloud.water:</em>
<em>#  server: water</em>
<em>#  config:</em>
<em>#    load: xxx_hdfs_cfg</em>
</code></pre> 
<ul> 
 <li>代码：</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span> &#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span>() &#123;
        String key = <span style="color:#50a14f">"test/"</span> + Utils.guid();
        String val = <span style="color:#50a14f">"Hello world!"</span>;
        
        <em>//写入数据</em>
        Result result = CloudClient.file().putText(key, val);
        System.out.println(ONode.stringify(result));
        <span style="color:#a626a4">assert</span> result.getCode() == Result.SUCCEED_CODE;

        <em>//读取数据</em>
        String tmp = CloudClient.file().getText(key);
        <span style="color:#a626a4">assert</span> val.equals(tmp);
    &#125;
&#125;    
</code></pre> 
<h3 style="text-align:start">3、Solon Cloud 增加适配组件：mqtt-solon-plugin（适配 CloudEventService）</h3> 
<p style="text-align:start">配置示例：</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">demo</span>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">consumer</span>
  
<span style="color:#986801">solon.cloud.mqtt:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"tcp://localhost:41883"</span>   <em>#mqtt服务地址</em>
</code></pre> 
<p style="text-align:start">代码示例：</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">TestController</span> &#123;
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/test"</span>)
    <span style="color:#a626a4">public</span> Object <span style="color:#4078f2">test</span>(String msg) &#123;
        <span style="color:#a626a4">if</span>(Utils.isEmpty(msg))&#123;
            msg = <span style="color:#50a14f">"demo2"</span>;
        &#125;

        Event event = <span style="color:#a626a4">new</span> Event(<span style="color:#50a14f">"hello.demo"</span>, msg).qos(<span style="color:#986801">1</span>).retained(<span style="color:#a626a4">true</span>);
        <span style="color:#a626a4">return</span> CloudClient.event().publish(event);
    &#125;
&#125;
</code></pre> 
<h3 style="text-align:start">4、增加应用启动事件：AppInitEndEvent</h3> 
<p style="text-align:start">Solon 启动处理顺序：</p> 
<ul> 
 <li>1.实例化 Solon.global() 并加载配置</li> 
 <li>2.加载扩展文件夹</li> 
 <li>3.扫描插件并排序</li> 
 <li>4.运行 initialize 函数</li> 
 <li>5.推送 AppInitEndEvent 事件（新增）</li> 
 <li>6.运行插件</li> 
 <li>7.推送 PluginLoadEndEvent 事件</li> 
 <li>8.导入java bean(@Import)</li> 
 <li>9.扫描并加载java bean</li> 
 <li>a.推送 BeanLoadEndEvent 事件</li> 
 <li>b.加载渲染印映关系</li> 
 <li>c.执行bean加完成事件</li> 
 <li>d.推送 AppLoadEndEvent 事件</li> 
 <li>e.结束</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//订阅示例（通过Solon事件总线提前订阅）</em>
EventBus.subscribe(AppInitEndEvent.<span style="color:#a626a4">class</span>, <span style="color:#c18401">event</span>->&#123;
    System.out.println(<span style="color:#50a14f">"app init end..."</span>);
&#125;);

Solon.start(App.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>);
</code></pre> 
<h3 style="text-align:start">5、取消 HandlerLink 类，增加 HandlerPipeline 类</h3> 
<ul> 
 <li>此例代码摘自组件 solon.extend.staticfiles ：</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><em>//切换处理（让静态文件优先）</em>
HandlerPipeline pipeline = <span style="color:#a626a4">new</span> HandlerPipeline();
pipeline.next(<span style="color:#a626a4">new</span> StaticResourceHandler()).next(app.handlerGet());

app.handlerSet(pipeline);
</code></pre> 
<ul> 
 <li>此例代码摘自组件 srww.base</li> 
</ul> 
<pre style="text-align:start"><code class="language-java">SolonServletFilter.onFilterEnd = <span style="color:#a626a4">new</span> HandlerPipeline().next(<span style="color:#a626a4">new</span> BaseLogHandler()).next(<span style="color:#a626a4">new</span> BaseEndHandler());
</code></pre> 
<h3 style="text-align:start">附：入门示例</h3> 
<ul> 
 <li>项目地址：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>入门教程示例：<a href="https://gitee.com/noear/solon_demo">https://gitee.com/noear/solon_demo</a></li> 
 <li>RPC入门教程示例：<a href="https://gitee.com/noear/solon_rpc_demo">https://gitee.com/noear/solon_rpc_demo</a></li> 
 <li>进阶教程示例：<a href="https://gitee.com/noear/solon_advance_demo">https://gitee.com/noear/solon_advance_demo</a></li> 
</ul>
                                        </div>
                                      
</div>
            