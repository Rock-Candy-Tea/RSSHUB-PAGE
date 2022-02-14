
---
title: 'springCloud -- 中级篇(2)'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11531502-743ca269f0f7d450.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11531502-743ca269f0f7d450.png'
---

<div>   
<p>本系列笔记涉及到的代码在GitHub上，地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fzsllsz%2Fcloud" target="_blank">https://github.com/zsllsz/cloud</a></p>
<p>本文涉及知识点：</p>
<ul>
<li><p>服务配置中心之config；</p></li>
<li><p>服务消息总线之bus(会用到rabbitmq)；</p></li>
</ul>
<hr>
<p>欢迎大家关注我的公众号 <strong>javawebkf</strong>，目前正在慢慢地将简书文章搬到公众号，以后简书和公众号文章将同步更新，且简书上的付费文章在公众号上将免费。</p>
<hr>
<h1>一、服务配置中心之springCloud Config</h1>
<p><strong>1、是什么？</strong><br>
springCloud学到现在，已经新建了十四五个module，每个module都有yml，不方便管理，所以配置中心就应运而生了。我们可以把微服务相同的配置抽到配置中心里面去，比如数据源的配置。假如某一天需要换数据源，只需要修改配置中心的配置即可，而不用每个微服务的yml都去改。没错，以前学的zookeeper也有这功能。spring config 分为服务端和客户端两部分，服务端也称分布式配置中心，是一个独立的微服务应用；客户端则是通过指定的配置中心来管理应用资源以及业务相关的配置内容，并在启动的时候从配置中心加载配置信息。</p>
<p><strong>2、能干嘛？</strong></p>
<ul>
<li>集中管理配置文件</li>
<li>不同环境不同配置，动态化的配置更新，分环境部署</li>
<li>运行期间动态调整配置</li>
<li>配置发生变化时不需要重启即可使用新的配置</li>
<li>将配置信息以rest接口形式暴露</li>
</ul>
<p><strong>3、config服务端配置与测试：</strong></p>
<ul>
<li>首先在github上新建一个仓库，然后新建一个config-dev.yml文件，内容随意，如下图：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="983" data-height="449"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-743ca269f0f7d450.png" data-original-width="983" data-original-height="449" data-original-format="image/png" data-original-filesize="56522" src="https://upload-images.jianshu.io/upload_images/11531502-743ca269f0f7d450.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">github仓库</div>
</div>
<ul>
<li>新建名为cloud-config-center-3344的module；</li>
<li>pom.xml：</li>
</ul>
<pre><code><dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator </artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<!-- eureka client -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-config-server</artifactId>
</dependency>
</code></pre>
<ul>
<li>yml：</li>
</ul>
<pre><code>server:
  port: 3344
  
spring:
  application:
    name: cloud-config-center
  cloud:
    config:
      server:
        git:
          uri: git@github.com:zsllsz/springcloud-config.git # github仓库地址
          search-paths:
          - springcloud-config # 搜索目录
      label: master # 读取的分支
eureka:
  client:
    service-url:
      defaultZone: http://eureka7001.com:7001/eureka
</code></pre>
<ul>
<li>主启动：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableConfigServer
public class ConfigMain3344 &#123;

    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(ConfigMain3344.class, args);
    &#125;
&#125;
</code></pre>
<p>启动后7001注册中心，然后启动3344，访问<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A3344%2Fmaster%2Fconfig-dev.yml" target="_blank">http://localhost:3344/master/config-dev.yml</a>，看看能否读取到config-dev.yml中的内容：<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="571" data-height="201"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-846f815b6c003379.png" data-original-width="571" data-original-height="201" data-original-format="image/png" data-original-filesize="8564" src="https://upload-images.jianshu.io/upload_images/11531502-846f815b6c003379.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">读取配置成功</div>
</div><p></p>
<p>如果读取的是master，那么<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A3344%2Fmaster%2Fconfig-dev.yml" target="_blank">http://localhost:3344/master/config-dev.yml</a>中的master可以省略，因为默认就是读master；如果读其他分支，比如dev，那就在配置中写成dev，然后访问的url将master换成dev即可。url还可以是这样：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A3344%2Fconfig%2Fdev%2Fmaster" target="_blank">http://localhost:3344/config/dev/master</a>，这里表示读取config-dev文件，分支为master。如果用lable表示分支，application表示文件名，profiles表示环境，那么url形式有如下几种：</p>
<ul>
<li>/lable/application-profile.yml</li>
<li>/application-profile.yml（只能读master）</li>
<li>/application/profile/lable</li>
</ul>
<p><strong>4、config客户端配置与测试：</strong></p>
<ul>
<li>修改github上的config-dev.yml，将内容改成符合yml文件格式的内容，比如这样：</li>
<li>新建名为cloud-config-client-3355的module；</li>
<li>pom.xml：</li>
</ul>
<pre><code><dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator </artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<!-- eureka client -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-config</artifactId>
</dependency>
</code></pre>
<ul>
<li>bootstrap.yml：注意，以前的yml是application.yml，它是用户级的资源配置，现在要新建一个bootstrap.yml，这个是系统级的，优先级更高。</li>
</ul>
<pre><code>server:
  port: 3355
  
spring:
  application:
    name: config-client
  # config 配置
  cloud:
    config:
      label: master # 分支
      name: config # 文件名
      profile: dev # 环境
      # 以上三个组合起来就是表示读取master上的config-dev.yml
      uri:
      - http://localhost:3344 # 配置中心地址
      
eureka:
  client:
    service-url:
      defaultZone: http://eureka7001.com:7001/eureka
</code></pre>
<ul>
<li>主启动：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableEurekaClient
public class ConfigClientMain3355 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(ConfigClientMain3355.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>controller：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/config")
public class ConfigController &#123;

    @Value("$&#123;config.info&#125;")
    private String configInfo;
    
    @GetMapping("/info")
    public String getInfo() &#123;
        return configInfo;
    &#125;
&#125;
</code></pre>
<p>我们在bootstrap.yml中配置了配置中心3344的访问路径，3344又会去github上找config-dev.yml，这个文件上又有<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fconfig.info" target="_blank">config.info</a>，所以在这个controller直接用@Value注解可以获取。最后访问这个controller，就可以在浏览器输出config-dev.yml中<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fconfig.info" target="_blank">config.info</a>的信息，如下：<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="488" data-height="162"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-40ee3d5497ab7901.png" data-original-width="488" data-original-height="162" data-original-format="image/png" data-original-filesize="7371" src="https://upload-images.jianshu.io/upload_images/11531502-40ee3d5497ab7901.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">成功获取配置信息</div>
</div><p></p>
<p><strong>5、动态刷新问题：</strong><br>
加入github上的config-dev.yml内容修改了，3344因为是直接连接github去获取配置信息的，所以可以获取最新信息；但是3355就必须重启才能获取最新内容，这不方便。接下来配置动态刷新，即不用重启也可以获取最新配置：</p>
<ul>
<li>修改bootstrap.yml，加上如下配置：</li>
</ul>
<pre><code># 暴露监控端口
management:
  endpoints:
    web:
      exposure:
        include:
        - "*"
</code></pre>
<ul>
<li>在controller中加上@RefreshScope注解，如下：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/config")
@RefreshScope
public class ConfigController &#123;

    @Value("$&#123;config.info&#125;")
    private String configInfo;
    
    @GetMapping("/info")
    public String getInfo() &#123;
        return configInfo;
    &#125;
&#125;
</code></pre>
<p>这样就搞定了，可以修改github上文件测试一下。经实测访问3355时还是没有获取到最新的配置内容，其实还需要发送一个post请求刷新3355。执行如下命令或者用postman请求都可：</p>
<pre><code>curl -X POST "http://localhost:3355/actuator/refresh"
</code></pre>
<p><br></p>
<h1>二、服务消息总线之springcloud bus</h1>
<p>上面的config还有点麻烦的就是每次修改了github上的配置文件，想要客户端也能立即读取到最新的，需要发送一个post请求去刷新，总归还是不方便。springcloud bus就是对springcloud config的增强，配合config使用，可以实现完全自动刷新，不需要再发post请求。</p>
<p><strong>1、是什么？</strong><br>
搭配消息中间件使用，可以实现全局广播通知。支持的消息中间件有RabbitMQ和Kafka。这个消息总线就像一个微信公众号，一个个的微服务应用就是订阅了这个公众号的人。微信公众号发了推文，每个订阅了的人都可以收到消息。这个springcloud bus就是这个公众号，它会让所有的服务都连接上来，配置文件有变化它会通知所有的服务。</p>
<p><strong>2、RabbitMQ安装与配置：</strong></p>
<ul>
<li>由于RabbitMQ是Erlang语言开发的，所以要安装Erlang，在centos上依次执行以下命令即可安装erlang：</li>
</ul>
<pre><code>yum install -y epel-release

wget https://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm

rpm -Uvh erlang-solutions-1.0-1.noarch.rpm

yum install -y erlang

erl -version
</code></pre>
<ul>
<li>rabbitmq的安装：首先下载rpm包，地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Fdownload%2Fv3.8.3%2Frabbitmq-server-3.8.3-1.el7.noarch.rpm" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.3/rabbitmq-server-3.8.3-1.el7.noarch.rpm</a>，然后执行如下命令：</li>
</ul>
<pre><code># 导入密钥
rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
# 安装
yum install rabbitmq-server-3.8.3-1.el7.noarch.rpm
# 启动
systemctl start rabbitmq-server
# 开启图形界面
rabbitmq-plugins enable rabbitmq_management
</code></pre>
<p>访问ip:15672，即可访问图形界面。默认用户名和密码都为guest，但是这个只允许用localhost访问，所以可以通过以下步骤新建用户：</p>
<pre><code># 新建admin用户，密码也为admin
rabbitmqctl add_user admin admin
# 设置权限
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
# 将admin设置为管理员用户
rabbitmqctl set_user_tags admin administrator
# 重启rabbitmq
systemctl restart rabbitmq-server
</code></pre>
<p>再次访问ip:15672，用admin就可以登陆进去了。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="994" data-height="480"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-7b363304c1f379f4.png" data-original-width="994" data-original-height="480" data-original-format="image/png" data-original-filesize="44640" src="https://upload-images.jianshu.io/upload_images/11531502-7b363304c1f379f4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">rabbitmq启动成功</div>
</div>
<p><strong>3、springcloud bus的使用：</strong></p>
<ul>
<li>新建名为cloud-config-client-3366的module；</li>
<li>pom.xml：</li>
</ul>
<pre><code><dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator </artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<!-- eureka client -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-config</artifactId>
</dependency>
</code></pre>
<ul>
<li>bootstrap.yml：</li>
</ul>
<pre><code>server:
  port: 3366
  
spring:
  application:
    name: config-client
  # config 配置
  cloud:
    config:
      label: master # 分支
      name: config # 文件名
      profile: dev # 环境
      # 以上三个组合起来就是表示读取master上的config-dev.yml
      uri:
      - http://localhost:3344 # 配置中心地址
      
eureka:
  client:
    service-url:
      defaultZone: http://eureka7001.com:7001/eureka
  
# 暴露监控端点    
management:
  endpoints:
    web:
      exposure:
        include:
        - "*"
</code></pre>
<ul>
<li>主启动类：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableEurekaClient
public class ConfigClientMain3366 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(ConfigClientMain3366.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>controller：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/config")
@RefreshScope
public class ConfigClientController &#123;
    @Value("$&#123;config.info&#125;")
    private String configInfo;

    @GetMapping("/info")
    public String getInfo() &#123;
        return configInfo;
    &#125;
&#125;
</code></pre>
<p>上面还没用到bus。bus的通知思想有两种，一种是广播通知一个客户端，进而通知到所有的客户端；另一种是bus广播通知服务端，服务端再通知所有的客户端。一般情况使用第二种方式，即通知服务端，通知这个带头大哥即可。</p>
<p><strong>下面开始使用springcloud bus</strong></p>
<ul>
<li>修改<strong>3344</strong>的pom，新增如下依赖：</li>
</ul>
<pre><code><!-- rabbitmq的支持 -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-bus-amqp</artifactId>
</dependency>
</code></pre>
<ul>
<li>修改<strong>3344</strong>的yml，添加rabbitmq和bus相关配置，如下：</li>
</ul>
<pre><code>  # mq相关配置
  rabbitmq:
    host: 192.168.0.106
    port: 5672
    username: admin
    password: admin
# bus配置
management:
  endpoints:
    web:
      exposure:
        include:
        - 'bus-refresh'
</code></pre>
<ul>
<li>修改3355的pom，添加如下依赖：</li>
</ul>
<pre><code><!-- rabbitmq的支持 -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-bus-amqp</artifactId>
</dependency>
</code></pre>
<ul>
<li>修改3355的yml，添加如下配置：</li>
</ul>
<pre><code>  # mq相关配置
  rabbitmq:
    host: 192.168.0.106
    port: 5672
    username: admin
    password: admin
</code></pre>
<ul>
<li>
<strong>3366</strong>和3355做一样的修改。</li>
<li>依次启动7001，3344，3355，3366</li>
<li>3344、3355和3366先访问一次配置文件</li>
<li>然后修改github上config-dev.yml的内容</li>
<li>3344此时可以访问到修改后的内容，因为它是带头大哥，直连github的，但是3355和3366此时还没有获取到最新的，因为RabbitMQ还没进行广播通知；</li>
<li>执行如下命令：</li>
</ul>
<pre><code>curl -X POST http://localhost:3344/actuator/bus-refresh
</code></pre>
<ul>
<li>刷新了带头大哥3344，叫它去通知3355和3366，再次去访问3355和3366，发现也能获取到最新的配置了。这就是bus和rabbitmq的功劳。如下图，在rabbitmq上有一个topic叫springCloudBus，3344、3355和3366都订阅了这个topic。当github上的配置发生改变时，我们就发一个post请求去通知3344，然后所有订阅了该topic的服务都会收到通知去更新配置。</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="967" data-height="704"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-00b92ba203b7b0be.png" data-original-width="967" data-original-height="704" data-original-format="image/png" data-original-filesize="85306" src="https://upload-images.jianshu.io/upload_images/11531502-00b92ba203b7b0be.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">rabbitmq</div>
</div>
<p><strong>4、定点通知：</strong><br>
上面演示的是通知所有订阅了该topic的服务，即3355和3366都通知到了。如果我想只通知3355，又当如何？发送post请求的时候指定发给谁就行了，公式就是：</p>
<pre><code>curl -X POST http://localhost:3344/actuator/bus-refresh/客户端的服务名:服务端口
</code></pre>
<p>服务名就是config客户端的微服务名字，即3344和3355的spring.application.name，比如只通知3355，那么执行如下命令即可：</p>
<pre><code>curl -X POST http://localhost:3344/actuator/bus-refresh/config-client:3355
</code></pre>
  
</div>
            