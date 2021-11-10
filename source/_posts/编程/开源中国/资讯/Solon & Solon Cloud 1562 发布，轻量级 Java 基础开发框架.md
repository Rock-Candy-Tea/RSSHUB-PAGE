
---
title: 'Solon & Solon Cloud 1.5.62 发布，轻量级 Java 基础开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6349'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 16:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6349'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:start">Solon 已有120个生态扩展插件，此次更新主要为细节打磨，且对k8s和docker-compose更友好：</h4> 
<p>1、插件 solon.coud ，事件总线增加支持本地同主题多订阅模式（以支持同服务内，领域隔离的需求）</p> 
<pre style="text-align:start"><code class="language-java"><em>//</em>
<em>// 同一个事件主题，支持多个本地订阅。可以做不同业务的领域隔离</em>
<em>//</em>

<span style="color:#4078f2">@CloudEvent</span>(<span style="color:#50a14f">"demo.user.created"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">EventHandlerDemo1</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudEventHandler</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">handler</span><span>(Event event)</span> <span style="color:#a626a4">throws</span> Throwable </span>&#123;
        <em>//送2块金币</em>
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;

<span style="color:#4078f2">@CloudEvent</span>(<span style="color:#50a14f">"demo.user.created"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">EventHandlerDemo2</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudEventHandler</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">handler</span><span>(Event event)</span> <span style="color:#a626a4">throws</span> Throwable </span>&#123;
        <em>//与移动合作，送100块充值卡</em>
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;
</code></pre> 
<p>2、插件 solon.view.beetl，升级 beetl 到 3.8</p> 
<p>3、插件 solon.boot.smarthttp 升级 smart-http 为 1.1.9</p> 
<p>4、插件 weed3-solon-puglin 升级 weed 3.4.8</p> 
<p>5、修复 solon.extend.staticfiles 增加本地绝对位置时无效的问题</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">InitPluginDemo</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">Plugin</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">start</span><span>(SolonApp app)</span> </span>&#123;
        <em>//添加静态目录印射</em>

        <em>//1.添加扩展目录：$&#123;solon.extend&#125;/static/</em>
        StaticMappings.add(<span style="color:#50a14f">"/"</span>, <span style="color:#a626a4">new</span> ExtendStaticRepository());
        <em>//2.添加本地绝对目录</em>
        StaticMappings.add(<span style="color:#50a14f">"/"</span>, <span style="color:#a626a4">new</span> FileStaticRepository(<span style="color:#50a14f">"/data/sss/water/water_ext/"</span>));
        <em>//3.添加资源路径</em>
        StaticMappings.add(<span style="color:#50a14f">"/"</span>, <span style="color:#a626a4">new</span> ClassPathStaticRepository(<span style="color:#50a14f">"user"</span>));
    &#125;
&#125;
</code></pre> 
<p>6、增加 app.before(index, handler) 接口</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span>-></span>&#123;
            app.before(<span style="color:#986801">2</span>, c->&#123;
                <em>//...</em>
            &#125;);
        &#125;);
    &#125;
&#125; 
</code></pre> 
<p>7、增加 app.cfg().isAloneMode() 接口（独立运行模式）</p> 
<p>8、简化接口 Utils::getResourceAsString(name)</p> 
<pre style="text-align:start"><code class="language-java"><em>//</em>
<em>//读取资源文件更简便</em>
<em>//</em>
String json = Utils.getResourceAsString(<span style="color:#50a14f">"water_init/user.json"</span>);
</code></pre> 
<p>9、插件 water-solon-plugin 增加基于服务名的消息订阅</p> 
<p>10、增加 solon.cache 插件，主要增加 CacheServiceProxy 类，可根据配置自动适配缓存服务</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">cache1:</span>
  <span style="color:#986801">driverType:</span> <span style="color:#50a14f">"redis"</span> <em>#通过类型配置，自动切换缓存服务</em>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"localhost:6379"</span>
  <span style="color:#986801">password:</span> <span style="color:#50a14f">"123456"</span>
  <span style="color:#986801">db:</span> <span style="color:#986801">9</span>
</code></pre> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> CacheService <span style="color:#4078f2">cache</span><span>(@Inject(<span style="color:#50a14f">"$&#123;cache1&#125;"</span>)</span>CacheServiceProxy cache)</span>&#123;
        <em>//根据driverType配置，会自动切换不同的缓存服务实现</em>
        <span style="color:#a626a4">return</span> cache;
    &#125;
&#125;
</code></pre> 
<p>11、增加 cloudevent-plus-solon-plugin 插件。增加基于实体的事件处理模式</p> 
<pre style="text-align:start"><code class="language-java"><em>//定义事件实体</em>
<span style="color:#4078f2">@CloudEvent</span>(<span style="color:#50a14f">"user.create.event"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">UserCreatedEvent</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudEventEntity</span> </span>&#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">long</span> userId;
&#125;

<em>//类函数模式订阅事件实体</em>
<span style="color:#4078f2">@Component</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">EventSubscriber</span></span>&#123;
    <span style="color:#4078f2">@CloudEventSubscribe</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">onUserCreatedEvent</span><span>(UserCreatedEvent event)</span></span>&#123;
        <em>//处理业务</em>
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;
<em>//发送事件</em>
<span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">publishDemo</span><span>()</span></span>&#123;
    UserCreatedEvent event = <span style="color:#a626a4">new</span> UserCreatedEvent();
    event.userId = <span style="color:#986801">1212</span>;
    event.publish();
&#125;
</code></pre> 
<p>12、增加 sqltoy-solon-plugin 插件（由 @夜の孤城 同学完成适配）</p> 
<p>13、内核 loadEnv 将同步到 System.setProperty 和 Solon.cfg().setProperty</p> 
<pre style="text-align:start"><code class="language-java"><em>//加载water的环境变量，并同步到 System.setProperty 和 Solon.cfg().setProperty</em>
<em>//</em>
Solon.cfg().loadEnv(<span style="color:#50a14f">"water."</span>);
</code></pre> 
<p>14、增加新环境变量：solon.start.ping。可以控制服务启动依赖，进而控制不同的服务启动顺序</p> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">version:</span> <span style="color:#50a14f">'3'</span>

<span style="color:#986801">services:</span>
  <span style="color:#986801">waterapi:</span>
    <span style="color:#986801">image:</span> <span style="color:#50a14f">noearorg/waterapi:latest</span>
    <span style="color:#986801">container_name:</span> <span style="color:#50a14f">waterapi</span>
    <span style="color:#986801">environment:</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">water.ds.schema=&#123;water&#125;</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">water.ds.server=&#123;water.mysql.io:3306&#125;</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">water.ds.username=&#123;demo&#125;</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">water.ds.password=&#123;1234&#125;</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">TZ=Asia/Shanghai</span>
    <span style="color:#986801">ports:</span>
      <span style="color:#4078f2">-</span> <span style="color:#986801">9371</span><span style="color:#50a14f">:8080</span>
  <span style="color:#986801">watersev:</span>
    <span style="color:#986801">image:</span> <span style="color:#50a14f">noearorg/watersev:latest</span>
    <span style="color:#986801">container_name:</span> <span style="color:#50a14f">watersev</span>
    <span style="color:#986801">environment:</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">solon.cloud.water.server=waterapi:8080</span>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">solon.start.ping=waterapi:8080</span> <em>#只在ping通 waterapi:8080 后，才启动服务</em>
      <span style="color:#4078f2">-</span> <span style="color:#50a14f">TZ=Asia/Shanghai</span>
    <span style="color:#986801">depends_on:</span>
      <span style="color:#4078f2">-</span>  <span style="color:#50a14f">waterapi</span>
    <span style="color:#986801">ports:</span>
      <span style="color:#4078f2">-</span> <span style="color:#986801">9372</span><span style="color:#50a14f">:8080</span>
</code></pre> 
<p>15、调整 water-solon-plugin 内部的白名单机制</p> 
<p>16、优化 序列化插件关于 JsonActionExecutor 对数组数据的泛型处理</p> 
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
<h3 style="text-align:start">Hello world：</h3> 
<pre style="text-align:start"><code class="language-java"><em>//Handler 模式：</em>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        SolonApp app = Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
        
        app.get(<span style="color:#50a14f">"/"</span>,(c)->c.output(<span style="color:#50a14f">"Hello world!"</span>));
    &#125;
&#125;

<em>//Controller 模式：(mvc or rest-api)</em>
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
    &#125;
  
    <em>//限定 put & post 方法类型</em>
    <span style="color:#4078f2">@Put</span>
    <span style="color:#4078f2">@Post</span>
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>(String name)</span></span>&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello "</span> + name;
    &#125;
&#125;

<em>//Remoting 模式：(rpc)</em>
<span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
<span style="color:#4078f2">@Remoting</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">App</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">HelloService</span></span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span></span>&#123;
        Solon.start(App<span>.<span style="color:#a626a4">class</span>,<span style="color:#c18401">args</span>)</span>;
    &#125;

    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> String <span style="color:#4078f2">hello</span><span>()</span></span>&#123;
        <span style="color:#a626a4">return</span> <span style="color:#50a14f">"Hello world!"</span>;
    &#125;
&#125;
</code></pre> 
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
            