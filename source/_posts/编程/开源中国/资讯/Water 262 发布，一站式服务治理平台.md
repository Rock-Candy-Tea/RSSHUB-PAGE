
---
title: 'Water 2.6.2 发布，一站式服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=21'
author: 开源中国
comments: false
date: Sun, 24 Apr 2022 13:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=21'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">Water（水孕育万物...）</h3> 
<p style="color:#24292e; text-align:start">Water 为项目开发、服务治理，提供一站式解决方案（可以理解为微服务架构支持套件）。基于 Solon 框架开发，并支持完整的 Solon Cloud 规范；已在生产环境奔跑了4年。</p> 
<p style="color:#24292e; text-align:start">功能相当于：consul + rabbitmq + elk + prometheus + openFaas + quartz + 等等，并有机结合在一起。 或者约等于：nacos + rocketmq + PlumeLog + prometheus + magic-api + xxl-job + 等。</p> 
<p style="color:#24292e; text-align:start"><strong>对 k8s 友好，支持 ip 漂移、支持 k8s service 映射。</strong></p> 
<h3 style="text-align:start">本次更新</h3> 
<ul> 
 <li>设置增加菜单资源管理能力</li> 
 <li>网关配置，更名为：上游配置</li> 
 <li>网关监控，更名为：上游监控</li> 
 <li>调整列表工具栏样式</li> 
 <li>多语言包增加批量删除功能</li> 
 <li>消息持久转移调整为log_date为条件</li> 
 <li>控制台登录界面增加版本显示</li> 
 <li>控制台UI优化</li> 
 <li>solon 升级为：1.7.3（项目地址：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a>）</li> 
 <li>grit 升级为：1.1.4（项目地址：<a href="https://gitee.com/noear/grit">https://gitee.com/noear/grit</a>）</li> 
 <li>weed3 升级为：3.4.25</li> 
 <li>redisx 升级为：1.4.2（项目地址：<a href="https://gitee.com/noear/redisx">https://gitee.com/noear/redisx</a>）</li> 
 <li>snack3 升级为：3.2.21（项目地址：<a href="https://gitee.com/noear/snack3">https://gitee.com/noear/snack3</a>）</li> 
</ul> 
<h3 style="text-align:start">快速入门</h3> 
<h4 style="text-align:start">了解开发框架与镜像</h4> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292e; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:960px; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>组件</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">开发框架</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">org.noear:water.client</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">框架：Water 客户端</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">org.noear:water-solon-plugin</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">框架：Water 客户端 for solon（也可用于 Spring Boot 项目）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/waterapi:2.6.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 主接口服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/watersev:2.6.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 后台服务（健康检测；数据监视；消息派发；定时任务等...）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/wateradmin:2.6.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 管理控制台（支持LDAP登录）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/waterfaas:2.6.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 即时接口服务，提供轻量级FaaS接口服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/xwater:2.6.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">构建：Water 助理工具</td> 
  </tr> 
 </tbody> 
</table> 
<h4 style="text-align:start">控制台演示站</h4> 
<p style="color:#24292e; text-align:start">地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwater.noear.org%2F" target="_blank">http://water.noear.org</a><span> </span>（账号：demo ；密码：demo ）</p> 
<p style="color:#24292e; text-align:start">关键持久化说明：</p> 
<ul> 
 <li>日志持久化，支持：MySql、PostgreSQL、MongoDb、ElasticSearch、ClickHouse</li> 
 <li>消息持久化，支持：MySql、PostgreSQL、MongoDb</li> 
</ul> 
<h4 style="text-align:start">项目地址</h4> 
<ul> 
 <li>https://gitee.com/noear/water</li> 
 <li>https://github.com/noear/water</li> 
</ul> 
<h4 style="text-align:start">代码演示</h4> 
<p>(1) 配置</p> 
<ul> 
 <li>pom.xml / mevan 配置</li> 
</ul> 
<pre style="text-align:start"><code class="language-xml"><em><!-- 客户端版本 --></em>
<span><<span style="color:#e45649">dependency</span>></span>
    <span><<span style="color:#e45649">groupId</span>></span>org.noear<span></<span style="color:#e45649">groupId</span>></span>
    <span><<span style="color:#e45649">artifactId</span>></span>water.client<span></<span style="color:#e45649">artifactId</span>></span>
    <span><<span style="color:#e45649">version</span>></span>$&#123;water.ver&#125;<span></<span style="color:#e45649">version</span>></span>
<span></<span style="color:#e45649">dependency</span>></span>

<em><!-- solon cloud 集成版本 （也可用于 Spring Boot 项目） --></em>
<span><<span style="color:#e45649">dependency</span>></span>
    <span><<span style="color:#e45649">groupId</span>></span>org.noear<span></<span style="color:#e45649">groupId</span>></span>
    <span><<span style="color:#e45649">artifactId</span>></span>water-solon-plugin<span></<span style="color:#e45649">artifactId</span>></span>
    <span><<span style="color:#e45649">version</span>></span>$&#123;solon.ver&#125;<span></<span style="color:#e45649">version</span>></span>
<span></<span style="color:#e45649">dependency</span>></span>
</code></pre> 
<ul> 
 <li>application.yml / 配置说明</li> 
</ul> 
<pre style="text-align:start"><code class="language-yml"><span style="color:#986801">solon.app:</span>
  <span style="color:#986801">name:</span> <span style="color:#50a14f">"demo-api"</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">"demo"</span>

<span style="color:#986801">solon.cloud.water:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"waterapi:9371"</span>    <em>#WATER服务地址</em>
  <span style="color:#986801">config:</span>
    <span style="color:#986801">load:</span> <span style="color:#50a14f">"demo.yml"</span>         <em>#默认加载的配置</em>
</code></pre> 
<p>(2) 代码</p> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoApp</span> </span>&#123;
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span> </span>&#123;
        SolonApp app = Solon.start(DemoApp<span>.<span style="color:#a626a4">class</span>, <span style="color:#c18401">args</span>)</span>;

        <em>//监控服务：之：添加接口性能记录（一般这个过滤器写成独立类）</em>
        Logger log = LoggerFactory.getLogger(DemoApp<span>.<span style="color:#a626a4">class</span>)</span>;
        app.filter((ctx, chain) -> &#123;
            <em>//1.开始计时（用于计算响应时长）</em>
            <span style="color:#a626a4">long</span> start = System.currentTimeMillis();

            <span style="color:#a626a4">try</span> &#123;
                chain.doFilter(ctx);
            &#125; <span style="color:#a626a4">catch</span> (Throwable e) &#123;
                <em>//2.顺带记录个异常</em>
                log.error(<span style="color:#50a14f">"&#123;&#125;"</span>,e);
            &#125; <span style="color:#a626a4">finally</span> &#123;
                <em>//3.获得接口响应时长</em>
                <span style="color:#a626a4">long</span> milliseconds = System.currentTimeMillis() - start;
                CloudClient.metric().addMeter(Solon.cfg().appName(), <span style="color:#50a14f">"path"</span>, ctx.pathNew(), milliseconds);
            &#125;
        &#125;);
    &#125;
&#125;

<span style="color:#4078f2">@Configuration</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoConfig</span> </span>&#123;

    <span style="color:#4078f2">@Bean</span>
    <span><span style="color:#a626a4">public</span> DataSource <span style="color:#4078f2">db1</span><span>(@CloudConfig(<span style="color:#50a14f">"demoDb"</span>)</span> HikariDataSource ds) </span>&#123;
        <em>//配置一个数据源</em>
        <span style="color:#a626a4">return</span> ds;
    &#125;
    
    <span style="color:#4078f2">@Bean</span>
    <span><span style="color:#a626a4">public</span> I18nBundleFactory <span style="color:#4078f2">i18nBundleFactory</span><span>()</span></span>&#123;
        <em>//将国际化服务，切换为云端接口</em>
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">new</span> CloudI18nBundleFactory();
    &#125;
&#125;

<span style="color:#4078f2">@Slf</span>4j
<span style="color:#4078f2">@Controller</span>
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">DemoController</span></span>&#123;
    <span style="color:#4078f2">@CloudConfig</span>(name = <span style="color:#50a14f">"demoDb"</span>, autoRefreshed = <span style="color:#a626a4">true</span>)  <em>//配置服务的功能（注解模式）</em>
    DbContext demoDb;

    <span style="color:#4078f2">@NamiClient</span>            <em>//RPC服务发现的功能（注解模式）</em>
    RockService rockService;
   
    <span style="color:#4078f2">@Mapping</span>(<span style="color:#50a14f">"/"</span>)
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">test</span><span>()</span></span>&#123;
        <em>//日志服务：写个日志</em>
        log.info(<span style="color:#50a14f">"你好，日志服务"</span>); <em>//(content)</em>
        TagsMDC.tag0(<span style="color:#50a14f">"demo"</span>);
        log.error(<span style="color:#50a14f">"&#123;&#125;\r\n&#123;&#125;"</span>,<span style="color:#50a14f">"test"</span>,<span style="color:#50a14f">"你好，日志服务"</span>); <em>//(tag,summary,content)</em>
        
        <em>//配置服务：使用配置的数据库上下文进行查询</em>
        Map map = demoDb.table(<span style="color:#50a14f">"water_reg_service"</span>).limit(<span style="color:#986801">1</span>).selectMap(<span style="color:#50a14f">"*"</span>);

        <em>//消息服务：发送消息</em>
        CloudClient.event().publish(<span style="color:#a626a4">new</span> Event(<span style="color:#50a14f">"demo.test"</span>, <span style="color:#50a14f">"&#123;\"order_id\":1&#125;"</span>)); <em>//（非注解模式）</em>

        <em>//Rpc发现服务：调用Rpc接口</em>
        AppModel app = rockService.getAppById(<span style="color:#986801">12</span>);
    &#125;
&#125;

<em>//消息订阅：订阅消息并处理（根据：topic 进行订阅）</em>
<span style="color:#4078f2">@Slf</span>4j
<span style="color:#4078f2">@CloudEvent</span>(<span style="color:#50a14f">"demo.test"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">Event_demo_test</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudEventHandler</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">handle</span><span>(Event event)</span> <span style="color:#a626a4">throws</span> Exception </span>&#123;
        <em>//处理消息...</em>
        log.info(<span style="color:#50a14f">"我收到消息："</span> + event.content());
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;


<em>//配置订阅：关注配置的实时更新</em>
<span style="color:#4078f2">@CloudConfig</span>(<span style="color:#50a14f">"demoDb"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">TestConfigHandler</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudConfigHandler</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">handle</span><span>(Config config)</span> </span>&#123;

    &#125;
&#125;

<em>//分布式任务</em>
<span style="color:#4078f2">@CloudJob</span>(name = <span style="color:#50a14f">"demo_test"</span>, cron7x = <span style="color:#50a14f">"0 1 * * * ?"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">Job_test</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudJobHandler</span> </span>&#123;

    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">handle</span><span>(Context ctx)</span> <span style="color:#a626a4">throws</span> Throwable </span>&#123;
        <em>//处理任务...</em>
        log.info(<span style="color:#50a14f">"我被调度了"</span>);
    &#125;
&#125;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            