
---
title: 'Solon 1.7 重要发布，更现代感的应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3772'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 09:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3772'
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
 <li>新增 hasordb-solon-plugin 插件</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Service</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span></span>&#123;
    <span style="color:#4078f2">@Db</span>(<span style="color:#50a14f">"db1"</span>)
    JdbcTemplate jdbcTemplate;
    
    <span style="color:#4078f2">@Db</span>(<span style="color:#50a14f">"db1"</span>)
    LambdaTemplate lambdaTemplate;
    
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>()</span></span>&#123;
        <span style="color:#a626a4">var</span> dtoList = jdbcTemplate.queryForList(<span style="color:#50a14f">"select * from test_user"</span>, TestUser<span>.<span style="color:#a626a4">class</span>)</span>;
        <span style="color:#a626a4">var</span> dtoList2 = lambdaTemplate.lambdaQuery(TestUser<span>.<span style="color:#a626a4">class</span>).<span style="color:#c18401">queryForList</span>()</span>;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>新增 solon.cache.redisson 插件</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><em>#完整配置示例</em>
<span style="color:#986801">demo.cache1:</span>
  <span style="color:#986801">driverType:</span> <span style="color:#50a14f">"redisson"</span> <em>#缓存驱动类型</em>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"localhost:6379"</span>
  <span style="color:#986801">password:</span> <span style="color:#50a14f">"1234"</span>
  <span style="color:#986801">db:</span> <span style="color:#986801">0</span> <em>#默认为 0，可不配置</em>
  <span style="color:#986801">defSeconds:</span> <span style="color:#986801">30</span> <em>#默认为 30秒，可不配置</em>
</code></pre> 
<pre style="text-align:start"><code class="language-java"><em>//配置缓存服务</em>
<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">Config</span> </span>&#123;
    <em>//通过 CacheServiceSupplier ，可根据 driverType 自动构建缓存服务</em>
    <span style="color:#4078f2">@Bean</span>(name = <span style="color:#50a14f">"cache2s"</span>)
    <span><span style="color:#a626a4">public</span> CacheService <span style="color:#4078f2">cache2</span><span>(@Inject(<span style="color:#50a14f">"$&#123;demo.cache2&#125;"</span>)</span> CacheServiceSupplier supplier)</span>&#123;
        <span style="color:#a626a4">return</span> supplier.get();
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>新增 solon.sessionstate.redisson 插件</li> 
 <li>新增 solon.sessionstate.jedis 插件（替代旧的 solon.extend.sessionstate.redis）</li> 
 <li>新增 solon.sessionstate.local 插件（替代旧的 solon.extend.sessionstate.local）</li> 
 <li>插件 httputils-solon-plugin 增加对服务上游和地址的检测</li> 
 <li>插件 beetlsql-solon-plugin 升级 beetlsql 为 3.14.0</li> 
 <li>插件 water-solon-plugin 升级 water 为：2.6.2 添加 ak/sk 和 多语言包 适配</li> 
 <li>插件 mybatis-plus-solon-plugin 增加对 globalConfig 的配置支持</li> 
 <li>插件 weed3-solon-plugin 升级 weed3 为：3.4.25</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Service</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoService</span></span>&#123;
    <span style="color:#4078f2">@Db</span>(<span style="color:#50a14f">"db1"</span>)
    DbContext db1;
    
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>()</span></span>&#123;
        <span style="color:#a626a4">var</span> dtoList = db1.table(<span style="color:#50a14f">"test_user"</span>).limit(<span style="color:#986801">10</span>).selectList(<span style="color:#50a14f">"*"</span>, TestUser<span>.<span style="color:#a626a4">class</span>)</span>;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>插件 sqltoy-solon-plugin 升级 sqltoy 为：5.1.31</li> 
 <li>添加 配置注入支持 字符串值 按需转换为 object(bean)</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">mybatis.db1:</span>
    <span style="color:#986801">typeAliases:</span>    
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"demo4031.model"</span>
    <span style="color:#986801">mappers:</span>        
        <span style="color:#4078f2">-</span> <span style="color:#50a14f">"demo4031.dso.mapper"</span>
    <span style="color:#986801">configuration:</span>
        <span style="color:#986801">cacheEnabled:</span> <span style="color:#0184bb">false</span>
        <span style="color:#986801">logImpl:</span> <span style="color:#50a14f">"org.apache.ibatis.logging.nologging.NoLoggingImpl"</span>
    <span style="color:#986801">globalConfig:</span>
        <span style="color:#986801">metaObjectHandler:</span> <span style="color:#50a14f">"demo4031.dso.MetaObjectHandlerImpl"</span> <em>#新增的支持</em>
        <span style="color:#986801">dbConfig:</span>
            <span style="color:#986801">logicDeleteField:</span> <span style="color:#50a14f">"deleted"</span>
</code></pre> 
<ul> 
 <li>添加 Solon Cloud 国际化接口规范</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span> </span>&#123;
    <span style="color:#4078f2">@Bean</span>
    <span><span style="color:#a626a4">public</span> I18nBundleFactory <span style="color:#4078f2">i18nBundleFactory</span><span>()</span></span>&#123;
        <em>//将国际化服务，切换为云端接口</em>
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> CloudI18nBundleFactory();
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>添加 SessionStateBase 提供会话状护的基础能力支持</li> 
 <li>添加 CloudBreakerService /root 配置支持(可支持动态创建)</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.cloud.local:</span>
  <span style="color:#986801">breaker:</span>
    <span style="color:#986801">root:</span> <span style="color:#986801">100</span> <em>#默认100 (Qps100 或 信号量为100；视插件而定)</em>
    <span style="color:#986801">main:</span> <span style="color:#986801">150</span> 
    
<em>#此配置可以放到配置中心，例：</em>
<em>#solon.cloud.water:</em>
<em>#    server: "waterapi:9371"</em>
<em>#    config.load: "breaker.yml"</em>
</code></pre> 
<ul> 
 <li>添加 MethodWrap::getArounds() 接口</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>, <span style="color:#c18401">app</span> -> </span>&#123;
            <em>//调试模式下，增加请求包围拦截器的打印</em>
            <span style="color:#a626a4">if</span> (Solon.cfg().isDebugMode()) &#123;
                app.after(ctx -> &#123;
                    Action action = ctx.action();
                    <span style="color:#a626a4">if</span> (action != <span style="color:#a626a4">null</span> && action.method().getArounds().size() > <span style="color:#986801">0</span>) &#123;
                        StringBuilder buf = <span style="color:#a626a4">new</span> StringBuilder();
                        
                        buf.append(<span style="color:#50a14f">"path: "</span>).append(ctx.path()).append(<span style="color:#50a14f">": "</span>);
                        <span style="color:#a626a4">for</span> (InterceptorEntity ie : action.method().getArounds()) &#123;
                            buf.append(ie.getReal().getClass().getName()).append(<span style="color:#50a14f">","</span>);
                        &#125;
                        buf.setLength(buf.length() - <span style="color:#986801">1</span>);
                        
                        System.out.println(buf);
                    &#125;
                &#125;);
            &#125;
        &#125;);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>添加 NamiBuilder::timeout 接口</li> 
</ul> 
<pre style="text-align:start"><code class="language-java">HelloService rpc = Nami.builder().url(<span style="color:#50a14f">"tcp://localhost:28080/demoe/rpc"</span>)
                                   .encoder(SnackTypeEncoder.instance)
                                   .timeout(<span style="color:#986801">60</span> * <span style="color:#986801">60</span>) <em>//单位：秒</em>
                                   .create(HelloService<span>.<span style="color:#a626a4">class</span>)</span>;
</code></pre> 
<ul> 
 <li>调整 session-id-key 可配置 "server.session.cookieName"</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><em>#设定会话超时秒数（单位：秒）</em>
<span style="color:#986801">server.session.timeout:</span> <span style="color:#986801">3600</span> 
<em>#设定会话id的cookieName</em>
<span style="color:#986801">server.session.cookieName:</span> <span style="color:#50a14f">"E52Ou8sV"</span>
</code></pre> 
<ul> 
 <li>调整 Action::bean() 更名为 controller()</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>)</span>;

        <em>//打印所有路由记录里的控制器名</em>
        Collection<Routing<Handler>> routings = Solon.global().router().getAll(Endpoint.main);
        <span style="color:#a626a4">for</span>(Routing<Handler> routing : routings)&#123;
            <span style="color:#a626a4">if</span>(routing.target() <span style="color:#a626a4">instanceof</span> Action)&#123;
                Action action = (Action) routing.target();
                System.out.println(action.controller().name());
            &#125;
        &#125;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>调整 Gateway 内部路由改为 RoutingTable 接口，支持 method（之前为 Map）</li> 
 <li>调整 属性注入的异常透传机制</li> 
 <li>调整 CloudConfigHandler:handler 更名为：handle</li> 
 <li>调整 CloudDiscoveryHandler:handler 更名为：handle</li> 
 <li>调整 CloudEventHandler:handler 更名为：handle</li> 
 <li>调整 CloudEventInterceptor:doInterceptor 更名为：doIntercept</li> 
 <li>调整 CloudJobInterceptor:doInterceptor 更名为：doIntercept</li> 
 <li>snack3 升级为：3.2.21</li> 
 <li>redisx 升级为：1.4.3</li> 
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
            