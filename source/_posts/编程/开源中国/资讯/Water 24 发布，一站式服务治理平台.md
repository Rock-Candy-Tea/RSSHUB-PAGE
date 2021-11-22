
---
title: 'Water 2.4 发布，一站式服务治理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5781'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 15:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5781'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">Water（水孕育万物...）</h3> 
<p style="color:#24292e; text-align:start">Water 为项目开发、服务治理，提供一站式解决方案（可以理解为微服务架构支持套件）。基于 Solon 框架开发，并支持完整的 Solon Cloud 规范；已在生产环境跑了4年。</p> 
<p style="color:#24292e; text-align:start">功能约等于：consul + rabbitmq + elk + prometheus + openFaas + quartz 等一些别的功能，并有机结合在一起。</p> 
<h3 style="text-align:start">本次更新</h3> 
<ul> 
 <li>服务 watersev，子级服务增加各自的签到。从而形成子级服务的集群 
  <ul> 
   <li>服务 watersev-pln，可自由集群，并让每个任务分布到集群中运行</li> 
   <li>服务 watersev-mot，可自由集群，并让每个任务分布到集群中运行</li> 
   <li>服务 watersev-msgexg，可自由集群，并分解borker到不同节点上</li> 
   <li>服务 watersev-msgdis，可自由集群，并分解borker到不同节点上</li> 
   <li>服务 watersev-sevchk，取消启动时需要 reset 的逻辑</li> 
  </ul> </li> 
 <li>服务 waterapi 
  <ul> 
   <li>镜像端口改为：9371</li> 
   <li>优化日志记录格式，强调输出输出概念和上下文随带</li> 
  </ul> </li> 
 <li>服务 waterraas 
  <ul> 
   <li>端口改为：9375 （之前为：9376）</li> 
  </ul> </li> 
 <li>服务 waterpaas 
  <ul> 
   <li>更名为：waterfaas</li> 
  </ul> </li> 
 <li>服务 PaaS 将包函：FaaS + RaaS 
  <ul> 
   <li>FaaS 调整： 
    <ul> 
     <li>数据表 paas_file 更名：luffy_file。强调FaaS自身的代号</li> 
     <li>数据表 paas_etl 更名：luffy_etl</li> 
     <li>管理后台 /paas/ 开头的路径，改为 /luffy/开头</li> 
     <li>配置 paas_uri 更名为：faas_uri</li> 
    </ul> </li> 
  </ul> </li> 
 <li>安全名单，增加 token 的模式支持</li> 
</ul> 
<h3 style="text-align:start">快速入门</h3> 
<h4 style="text-align:start">了解开发框架与镜像</h4> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292e; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:960px; word-spacing:0px"> 
 <thead> 
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
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/waterapi</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 主接口服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/watersev</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 后台服务（健康检测；数据监视；消息派发；定时任务等...）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/wateradmin</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 管理控制台（支持LDAP登录）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/waterfaas</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 即时接口服务，提供轻量级FaaS接口服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">noearorg/waterraas</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">镜像：Water 规则计算服务，提供轻量级规则计算服务</td> 
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
  <span style="color:#986801">name:</span> <span style="color:#50a14f">"wateradmin"</span>
  <span style="color:#986801">group:</span> <span style="color:#50a14f">"water"</span>

<span style="color:#986801">solon.cloud.water:</span>
  <span style="color:#986801">server:</span> <span style="color:#50a14f">"waterapi:9371"</span>           <em>#WATER服务地址</em>
  <span style="color:#986801">config:</span>
    <span style="color:#986801">load:</span> <span style="color:#50a14f">"test.properties"</span>         <em>#默认加载的配置</em>
  <span style="color:#986801">log:</span>
    <span style="color:#986801">default:</span> <span style="color:#50a14f">"water_log_admin"</span>      <em>#默认日志记录器</em>
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
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">boolean</span> <span style="color:#4078f2">handler</span><span>(Event event)</span> <span style="color:#a626a4">throws</span> Exception </span>&#123;
        <em>//处理消息...</em>
        log.info(<span style="color:#50a14f">"我收到消息："</span> + event.content());
        <span style="color:#a626a4">return</span> <span style="color:#a626a4">true</span>;
    &#125;
&#125;


<em>//配置订阅：关注配置的实时更新</em>
<span style="color:#4078f2">@CloudConfig</span>(<span style="color:#50a14f">"demoDb"</span>)
<span style="color:#a626a4">public</span> <span><span style="color:#a626a4">class</span> <span style="color:#c18401">TestConfigHandler</span> <span style="color:#a626a4">implements</span> <span style="color:#c18401">CloudConfigHandler</span> </span>&#123;
    <span style="color:#4078f2">@Override</span>
    <span><span style="color:#a626a4">public</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">handler</span><span>(Config config)</span> </span>&#123;

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
&#125;
</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            