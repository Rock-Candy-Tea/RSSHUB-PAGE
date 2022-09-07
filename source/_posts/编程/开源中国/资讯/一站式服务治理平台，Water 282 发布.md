
---
title: '一站式服务治理平台，Water 2.8.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4442'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 14:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4442'
---

<div>   
<div class="content">
                                                                                            <h3>Water（水孕育万物...）</h3> 
<p>Water 为项目开发、服务治理，提供一站式解决方案（可以理解为微服务架构支持套件）。基于 Solon 框架开发，并支持完整的 Solon Cloud 规范；已在生产环境奔跑了4年。</p> 
<p>功能相当于：consul + rabbitmq + elk + prometheus + openFaas + quartz + 等等，并有机结合在一起。 或者约等于：nacos + rocketmq + PlumeLog + prometheus + magic-api + xxl-job + 等。</p> 
<p><strong>对 k8s 友好，支持 ip 漂移、支持 k8s service 映射。</strong></p> 
<h3>本次更新</h3> 
<ul> 
 <li>新增 "指标关注" 记录接口和显示</li> 
 <li>新增 "证书监视" 管理界面</li> 
 <li>添加 "应用监视" 批量禁用启用支持</li> 
 <li>添加 "数据监视" 批量禁用启用支持</li> 
 <li>solon 升级为：1.10.2（项目地址：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a>）</li> 
 <li>snack3 升级为：3.2.35（项目地址：<a href="https://gitee.com/noear/snack3">https://gitee.com/noear/snack3</a>）</li> 
</ul> 
<h3>快速入门</h3> 
<h4>了解开发框架与镜像</h4> 
<table> 
 <thead> 
  <tr> 
   <th>组件</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>开发框架</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>org.noear:water.client</td> 
   <td>框架：Water 客户端</td> 
  </tr> 
  <tr> 
   <td>org.noear:water-solon-plugin</td> 
   <td>框架：Water 客户端 for solon（也可用于 Spring Boot 项目）</td> 
  </tr> 
  <tr> 
   <td>镜像</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>noearorg/waterapi:2.8.2</td> 
   <td>镜像：Water 主接口服务</td> 
  </tr> 
  <tr> 
   <td>noearorg/watersev:2.8.2</td> 
   <td>镜像：Water 后台服务（健康检测；数据监视；消息派发；定时任务等...）</td> 
  </tr> 
  <tr> 
   <td>noearorg/wateradmin:2.8.2</td> 
   <td>镜像：Water 管理控制台（支持LDAP登录）</td> 
  </tr> 
  <tr> 
   <td>noearorg/waterfaas:2.8.2</td> 
   <td>镜像：Water 即时接口服务，提供轻量级FaaS接口服务</td> 
  </tr> 
  <tr> 
   <td> </td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>noearorg/xwater:2.8.2</td> 
   <td>构建：Water 助理工具</td> 
  </tr> 
 </tbody> 
</table> 
<h4>控制台演示站</h4> 
<p>地址： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwater.noear.org" target="_blank">http://water.noear.org</a> （账号：demo ；密码：demo ）</p> 
<p>关键持久化说明：</p> 
<ul> 
 <li>日志持久化，支持：MySql、PostgreSQL、MongoDb、ElasticSearch、ClickHouse</li> 
 <li>消息持久化，支持：MySql、PostgreSQL、MongoDb</li> 
</ul> 
<h4>项目地址</h4> 
<ul> 
 <li><a href="https://gitee.com/noear/water">https://gitee.com/noear/water</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fwater" target="_blank">https://github.com/noear/water</a></li> 
</ul> 
<h4>代码演示</h4> 
<p>(1) 配置</p> 
<ul> 
 <li>pom.xml / mevan 配置</li> 
</ul> 
<pre><code class="language-xml"><!-- 客户端版本 -->
<dependency>
    <groupId>org.noear</groupId>
    <artifactId>water.client</artifactId>
    <version>$&#123;water.ver&#125;</version>
</dependency>

<!-- solon cloud 集成版本 （也可用于 Spring Boot 项目） -->
<dependency>
    <groupId>org.noear</groupId>
    <artifactId>water-solon-plugin</artifactId>
    <version>$&#123;solon.ver&#125;</version>
</dependency>
</code></pre> 
<ul> 
 <li>app.yml / 配置说明</li> 
</ul> 
<pre><code class="language-yml">solon.app:
  name: "demo-api"
  group: "demo"

solon.cloud.water:
  server: "waterapi:9371"    #WATER服务地址
  config:
    load: "demo.yml"         #默认加载的配置
</code></pre> 
<p>(2) 代码</p> 
<pre><code class="language-java">public class DemoApp &#123;
    public void main(String[] args) &#123;
        SolonApp app = Solon.start(DemoApp.class, args);

        //监控服务：之：添加接口性能记录（一般这个过滤器写成独立类）
        Logger log = LoggerFactory.getLogger(DemoApp.class);
        app.filter((ctx, chain) -> &#123;
            //1.开始计时（用于计算响应时长）
            long start = System.currentTimeMillis();

            try &#123;
                chain.doFilter(ctx);
            &#125; catch (Throwable e) &#123;
                //2.顺带记录个异常
                log.error("&#123;&#125;",e);
            &#125; finally &#123;
                //3.获得接口响应时长
                long milliseconds = System.currentTimeMillis() - start;
                CloudClient.metric().addMeter(Solon.cfg().appName(), "path", ctx.pathNew(), milliseconds);
            &#125;
        &#125;);
    &#125;
&#125;

@Configuration
public class DemoConfig &#123;

    @Bean
    public DataSource db1(@CloudConfig("demoDb") HikariDataSource ds) &#123;
        //配置一个数据源
        return ds;
    &#125;
    
    @Bean
    public I18nBundleFactory i18nBundleFactory()&#123;
        //将国际化服务，切换为云端接口
        return new CloudI18nBundleFactory();
    &#125;
&#125;

@Slf4j
@Controller
public class DemoController&#123;
    @CloudConfig(name = "demoDb", autoRefreshed = true)  //配置服务的功能（注解模式）
    DbContext demoDb;

    @NamiClient            //RPC服务发现的功能（注解模式）
    RockService rockService;
   
    @Mapping("/")
    public void test()&#123;
        //日志服务：写个日志
        log.info("你好，日志服务"); //(content)
        TagsMDC.tag0("demo");
        log.error("&#123;&#125;\\r\\n&#123;&#125;","test","你好，日志服务"); //(tag,summary,content)
        
        //配置服务：使用配置的数据库上下文进行查询
        Map map = demoDb.table("water_reg_service").limit(1).selectMap("*");

        //消息服务：发送消息
        CloudClient.event().publish(new Event("demo.test", "&#123;\\"order_id\\":1&#125;")); //（非注解模式）

        //Rpc发现服务：调用Rpc接口
        AppModel app = rockService.getAppById(12);
    &#125;
&#125;

//消息订阅：订阅消息并处理（根据：topic 进行订阅）
@Slf4j
@CloudEvent("demo.test")
public class Event_demo_test implements CloudEventHandler &#123;
    @Override
    public boolean handle(Event event) throws Exception &#123;
        //处理消息...
        log.info("我收到消息：" + event.content());
        return true;
    &#125;
&#125;


//配置订阅：关注配置的实时更新
@CloudConfig("demoDb")
public class TestConfigHandler implements CloudConfigHandler &#123;
    @Override
    public void handle(Config config) &#123;

    &#125;
&#125;

//分布式任务
@CloudJob(name = "demo_test", cron7x = "0 1 * * * ?")
public class Job_test implements CloudJobHandler &#123;

    @Override
    public void handle(Context ctx) throws Throwable &#123;
        //处理任务...
        log.info("我被调度了");
    &#125;
&#125;
</code></pre>
                                        </div>
                                      
</div>
            