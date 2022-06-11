
---
title: 'springCloud --- 高级篇(1)'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11531502-b226295de96913b5.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11531502-b226295de96913b5.png'
---

<div>   
<p>本系列笔记涉及到的代码在GitHub上，地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fzsllsz%2Fcloud" target="_blank">https://github.com/zsllsz/cloud</a></p>
<p>本文涉及知识点：</p>
<ul>
<li><p>springCloud Alibaba介绍；</p></li>
<li><p>nacos做注册中心；</p></li>
<li><p>nacos做配置中心；</p></li>
<li><p>sentinel流控；</p></li>
</ul>
<hr>
<p>欢迎大家关注我的公众号 <strong>javawebkf</strong>，目前正在慢慢地将简书文章搬到公众号，以后简书和公众号文章将同步更新，且简书上的付费文章在公众号上将免费。</p>
<hr>
<h1>一、springCloud Alibaba简介</h1>
<p><strong>1、为什么会诞生springCloud Alibaba？</strong><br>
通过springCloud初级篇和中级篇的学习，我们知道springCloud很多技术现在都停更了，Netflix也说明了不再维护了。一开始阿里搞出了一个Dubbo，但是后面停更了几年，spring就联合Netflix搞出了一个springCloud生态，Netflix主要技术有5个，eureka、ribbon、feign、zuul和config。但是呢Netflix内部神仙打架，意见不一，然后导致这些技术大部分停更了。这时，阿里又杀出来了，搞出了一套springCloud Alibaba，spring官方看它还不错，阿里也想推广自己，所以在2018年四月份spring又把springCloud Alibaba给收编了。所以对于我们使用者而言，无非就是从 springCloud Netflix 换成 springCloud Alibaba而已。</p>
<p><strong>2、springCloud Alibaba能干嘛？</strong></p>
<ul>
<li>服务的注册与发现</li>
<li>服务的降级与限流</li>
<li>分布式配置管理</li>
<li>消息驱动能力</li>
<li>分布式任务调度</li>
<li>阿里云对象存储</li>
<li>阿里云短信服务</li>
</ul>
<p>可以发现，springCloud能干的它几乎都能干，还多了一些springCloud不能干的。springCloud Alibaba相关网址如下，可以查阅相关文档：<br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fblob%2Fmaster%2FREADME-zh.md" target="_blank">https://github.com/alibaba/spring-cloud-alibaba/blob/master/README-zh.md</a><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fspring-cloud-alibaba-group.github.io%2Fgithub-pages%2Fgreenwich%2Fspring-cloud-alibaba.html" target="_blank">https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html</a><br>
一般我们要学怎么使用查第二个文档就好了。</p>
<h1>二、springCloud Alibaba Nacos 代替eureka做服务注册中心</h1>
<p>之前springCloud的服务注册可以用eureka、consul和zookeeper，配置中心用config和bus，现在springCloud Alibaba用Nacos搞定这些，简言之就是注册中心加配置中心。<br>
<strong>1、下载安装：</strong></p>
<ul>
<li>入口网站：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fnacos.io%2Fzh-cn%2Findex.html" target="_blank">https://nacos.io/zh-cn/index.html</a>
</li>
<li>下载地址(本次下载1.1.4的linux版)：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Falibaba%2Fnacos%2Ftags" target="_blank">https://github.com/alibaba/nacos/tags</a>
</li>
<li>安装运行：前提要有maven和jdk1.8及以上的环境。下载完解压，然后直接进入bin目录下执行以下命令启动单机版nacos：</li>
</ul>
<pre><code>bash startup.sh -m standalone
</code></pre>
<ul>
<li>
<p>测试：访问 ip:8848/nacos，看到如下画面就启动成功了，默认账号密码都是nacos。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="999" data-height="662"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-b226295de96913b5.png" data-original-width="999" data-original-height="662" data-original-format="image/png" data-original-filesize="50744" src="https://upload-images.jianshu.io/upload_images/11531502-b226295de96913b5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">nacos</div>
</div>
</li>
</ul>
<p><strong>2、基于nacos的服务提供者：</strong></p>
<ul>
<li>新建名为cloudalibaba-provider-payment9001的module</li>
<li>父pom.xml中添加springCloud Alibaba依赖(一开始就添加过了)</li>
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
<!-- nacos -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
</code></pre>
<ul>
<li>application.yml：</li>
</ul>
<pre><code>server:
  port: 9001
spring:
  application:
    name: nacos-payment-provider
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
# 端点启动和暴露(这时actuator的功能，学springcloud config时也配置过)
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
@EnableDiscoveryClient
public class NacosMainPayment9001 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(NacosMainPayment9001.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>业务类：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/provider")
public class PaymentController &#123;
    
    @GetMapping("/payment/&#123;id&#125;")
    public String payment(@PathVariable("id") Integer id) &#123;
        return "success" + id;
    &#125;
&#125;
</code></pre>
<ul>
<li>
<p>最后启动该项目，并访问测试一下，然后看看nacos控制台。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1009" data-height="548"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-0a93895011a5cd53.png" data-original-width="1009" data-original-height="548" data-original-format="image/png" data-original-filesize="54810" src="https://upload-images.jianshu.io/upload_images/11531502-0a93895011a5cd53.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">服务成功注册进nacos</div>
</div>
</li>
<li><p>为了等下演示nacos的负载均衡，新建9002，内容几乎和9001一样。</p></li>
</ul>
<p><strong>3、基于nacos的服务消费者：</strong></p>
<ul>
<li>新建名为cloudalibaba-consumer-nacos-order80的module</li>
<li>pom.xml：和9001的一样</li>
<li>application.yml：</li>
</ul>
<pre><code>server:
  port: 80
spring:
  application:
    name: nacos-order-consumer
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
# 消费者将要去访问的微服务名称
service-url:
  nacos-user-service: http://nacos-payment-provider
</code></pre>
<ul>
<li>主启动类：和9001的一样，也是那两个注解</li>
<li>配置RestTemplate：</li>
</ul>
<pre><code>@Configuration
public class RestTemplateConfig &#123;
    @Bean
    @LoadBalanced
    public RestTemplate getRestTemplate() &#123;
        return new RestTemplate();
    &#125;
&#125;
</code></pre>
<ul>
<li>controller：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/consumer")
public class OrderController &#123;

    @Autowired
    private RestTemplate restTemplate;
    
    @Value("$&#123;service-url.nacos-user-service&#125;")
    private String serverUrl;
    
    @GetMapping("/order/&#123;id&#125;")
    public String getPayment(@PathVariable("id") Integer id) &#123;
        return restTemplate.getForObject(serverUrl + "/provider/payment/" + id, String.class);
    &#125;
&#125;
</code></pre>
<p>访问这个controller，就会发现一次是调用9001，一次是调用9002。因为nacos也集成了ribbon，所以自带负载均衡。</p>
<p><strong>4、nacos的CAP模型：</strong><br>
nacos支持CP和AP，可以自由切换。这样一来，nacos可以代替所有的注册中心。如果要代替eureka，用AP，如果要代替consul或者zookeeper，用CP。</p>
<h1>三、springCloud Alibaba Nacos 代替config做服务配置中心</h1>
<p><strong>1、新建名为cloudalibaba-config-nacos-client3377的module：</strong></p>
<ul>
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
<!-- nacos -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
<!-- nacos config -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>
</code></pre>
<ul>
<li>yml：和config一样，要先搞一个bootstrap.yml从配置中心拉取配置，其他自己专有的再用application.yml。先有共性再有个性。<br>
<em>bootstrap.yml：</em>
</li>
</ul>
<pre><code>server:
  port: 3377
spring:
  application:
    name: nacos-config-client
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
      config:
        server-addr: 192.168.0.106:8848
        file-extension: yaml #指定yaml格式的配置，就是对应以前用config时GitHub上的配置文件
</code></pre>
<p><em>application.yml:</em></p>
<pre><code>spring:
  profiles:
    active:
    - dev #激活开发环境
</code></pre>
<ul>
<li>主启动类：</li>
</ul>
<pre><code>@SpringBootApplication
@EnableDiscoveryClient
public class NacosConfigMain3377 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(NacosConfigMain3377.class, args);
    &#125;
&#125;
</code></pre>
<ul>
<li>controller：用@Value注解尝试读取nacos中的配置文件</li>
</ul>
<pre><code>@RestController
@RequestMapping("/config")
@RefreshScope // 动态刷新
public class NacosConfigController &#123;
    @Value("$&#123;config.info&#125;")
    private String info;
    
    @GetMapping("/info")
    public String info() &#123;
        return info;
    &#125;
&#125;
</code></pre>
<p>至此工程新建完毕，接下来就要去nacos中新建配置文件。</p>
<p><strong>2、在nacos上新建配置文件：</strong></p>
<ul>
<li>先看一下nacos配置管理的界面：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1139" data-height="383"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-59fc23dc6aeccba0.png" data-original-width="1139" data-original-height="383" data-original-format="image/png" data-original-filesize="38586" src="https://upload-images.jianshu.io/upload_images/11531502-59fc23dc6aeccba0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">nacos配置管理</div>
</div>
<p>可以看到有一个Data Id，一个Group。<br>
<strong>Data Id的格式：</strong></p>
<pre><code>$&#123;prefix&#125;-$&#123;spring.profile.active&#125;.$&#123;file-extension&#125;
</code></pre>
<ul>
<li>
<code>prefix</code> 默认为 <code>spring.application.name</code> 的值，也可以通过配置项 <code>spring.cloud.nacos.config.prefix</code>来配置。</li>
<li>
<code>spring.profile.active</code> 即为当前环境对应的 profile，注意：当 <code>spring.profile.active</code> 为空时，对应的连接符 <code>-</code> 也将不存在，dataId 的拼接格式变成 <code>$&#123;prefix&#125;.$&#123;file-extension&#125;</code>。在使用的时候，还是不要让它为空，免得出现奇奇怪怪的问题。</li>
<li>
<code>file-exetension</code> 为配置内容的数据格式，可以通过配置项 <code>spring.cloud.nacos.config.file-extension</code> 来配置。目前只支持 <code>properties</code> 和 <code>yaml</code> 类型。</li>
<li>通过 Spring Cloud 原生注解 @RefreshScope 实现配置自动更新，这就是刚才controller中加这个注解的原因。<br>
按照上面的格式，那3377这个项目的data Id就是：<code>nacos-config-client-dev.yaml</code><br>
然后在nacos上新建如下配置：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1120" data-height="646"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-33d0b6ef3a558fc3.png" data-original-width="1120" data-original-height="646" data-original-format="image/png" data-original-filesize="56438" src="https://upload-images.jianshu.io/upload_images/11531502-33d0b6ef3a558fc3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">新建配置</div>
</div>
<p>这个配置一定要注意每个冒号后面要加一个空格！</p>
<ul>
<li>然后访问3377的controller，就可以成功获取到配置了：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="543" data-height="179"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-b33297d8cc2b0237.png" data-original-width="543" data-original-height="179" data-original-format="image/png" data-original-filesize="8795" src="https://upload-images.jianshu.io/upload_images/11531502-b33297d8cc2b0237.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">成功读取到配置</div>
</div>
<ul>
<li>动态刷新：现在修改nacos上的配置文件，然后再次访问3377的controller，会发现可以获取到最新的内容。(如果没有获取到最新的，那就是浏览器缓存的原因)</li>
</ul>
<p><strong>3、nacos配置管理的命名空间、data id和group的关系：</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1140" data-height="618"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-5fae9728f4b53e00.png" data-original-width="1140" data-original-height="618" data-original-format="image/png" data-original-filesize="76862" src="https://upload-images.jianshu.io/upload_images/11531502-5fae9728f4b53e00.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">nacos</div>
</div>
<ul>
<li>命名空间：有一个默认的public，相当于对group进行分组管理</li>
<li>分组group：有一个默认的DEFAULT_GROUP，对data Id进行分组管理</li>
<li>data Id：理解为配置文件的id</li>
</ul>
<p>所以三者关系就是：<code>namespace + group + data Id</code>可以确认一个唯一的配置文件。</p>
<p>这样设计的好处就是可以方便地区分不同的环境。比如现在有开发、测试和生产三个环境，那我们就新建三个不同的namespace。</p>
<p><strong>使用默认命名空间默认分组读取不同data id的配置文件：</strong></p>
<ul>
<li>在nacos上新建nacos-config-client-test.yaml，当作测试环境的配置文件，目前都是public命名空间默认分组下；</li>
<li>将3377的application.yml中的dev改成test，就可以读测试环境配置文件了；</li>
</ul>
<p><strong>使用默认命名空间不同分组读取配置配置文件：</strong></p>
<ul>
<li>在nacos上新建两个配置文件,名字都叫nacos-config-client-info.yaml，分组分别为DEV_GROUP和TEST_GROUP；</li>
<li>然后bootstrap.yml和application.yml分别改成这样：</li>
</ul>
<pre><code>server:
  port: 3377
spring:
  application:
    name: nacos-config-client
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
      config:
        server-addr: 192.168.0.106:8848
        file-extension: yaml #指定yaml格式的配置，就是对应以前用config时GitHub上的配置文件
        group: DEV_GROUP
</code></pre>
<pre><code>spring:
  profiles:
    active:
    #- dev #激活开发环境
    - info
</code></pre>
<p>这样就搞定了，这样读取的就是dev_group分组下的info配置文件。</p>
<p><strong>使用不同的命名空间读取不同的配置文件：</strong></p>
<ul>
<li>新建DEV和TEST命名空间；</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1144" data-height="424"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-9946e054512c06f0.png" data-original-width="1144" data-original-height="424" data-original-format="image/png" data-original-filesize="49606" src="https://upload-images.jianshu.io/upload_images/11531502-9946e054512c06f0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">命名空间</div>
</div>
<p>bootstrap.yml再加一行配置，如下：</p>
<pre><code>server:
  port: 3377
spring:
  application:
    name: nacos-config-client
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
      config:
        server-addr: 192.168.0.106:8848
        file-extension: yaml #指定yaml格式的配置，就是对应以前用config时GitHub上的配置文件
        namespace: 4d4b4c98-2746-4ff7-8ce9-eb2837db456c
        group: DEV_GROUP
</code></pre>
<p>这样就可以指定命名空间指定分组读取指定后缀文件了。</p>
<h1>四、nacos集群和持久化</h1>
<p>官网的集群架构图：VIP的意思是虚拟IP，我们可以认为vip就是nginx的集群。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1098" data-height="476"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-f0272bdafd7d4f54.png" data-original-width="1098" data-original-height="476" data-original-format="image/png" data-original-filesize="40240" src="https://upload-images.jianshu.io/upload_images/11531502-f0272bdafd7d4f54.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">nacos集群架构图</div>
</div>
<p>nacos默认自带了一个数据库(derby)用来做持久化，当nacos集群的时候，每一台服务器上的nacos都以自己自带的数据库来搞持久化，会存在数据一致性的问题。所以干脆都别用自带的数据库了，都用MySQL。</p>
<p><strong>1、用MySQL做持久化：</strong></p>
<ul>
<li>在nacos/conf目录下有一个nacos-mysql.sql的脚本，在MySQL中新建一个名为nacos_config的数据库，在此数据库中执行这个脚本即可；</li>
<li>在nacos/conf目录下有一个application.properties文件，打开修改它将官网的这段配置粘贴到其中，并将MySQL连接地址改成自己的就可以了：</li>
</ul>
<pre><code>spring.datasource.platform=mysql
db.num=1
db.url.0=jdbc:mysql://192.168.0.106:3306/nacos_config?characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true
db.user=root
db.password=你的MySQL密码
</code></pre>
<ul>
<li>修改完重启nacos,重启之后立即访问可能会访问不了，毕竟人家启动也要时间嘛。启动完登陆进去，发现之前的配置都没了。然后自己新增配置，再去数据库查看，发现nacos_config数据库的config_info表中就有数据了，说明切换到MySQL成功了。</li>
</ul>
<p><strong>2、nacos集群：</strong><br>
需要的环境：</p>
<ul>
<li>2个nginx(此处为了简单就只启动了一个nginx，想了解nginx集群可以参考我nginx相关文章)</li>
<li>3个nacos</li>
<li>1个mysql</li>
</ul>
<p><strong>nginx集群和mysql已经安装好了，nacos集群通过如下步骤搞定：</strong></p>
<ul>
<li>nacos的application.properties中加上MySQL配置(之前已经加过)；</li>
<li>拷贝cluster.conf.example改名为cluster.conf，然后修改其内容：</li>
</ul>
<pre><code>192.168.2.43:8848
192.168.2.43:8849
192.168.2.43:8850
</code></pre>
<p>由于这里是在一台虚拟机上启动3份nacos，所以后面要加上端口。如果有3台不同的机器，那么这里直接写那3台机器的ip就好了。并且要注意，这个ip不能填写127.0.0.1，执行<code>hostname -i</code>，填写ens33后面跟着的那个IP。</p>
<ul>
<li>修改nacos的startup.sh，使其能够指定端口启动：<br>
修改有两处，第一处，增加端口启动，如下图，左边是修改前，右边是修改后：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="844" data-height="257"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-43330b49ec96408d.png" data-original-width="844" data-original-height="257" data-original-format="image/png" data-original-filesize="35611" src="https://upload-images.jianshu.io/upload_images/11531502-43330b49ec96408d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">增加端口启动</div>
</div>
<p>第二次启动，启动日志增加端口打印，如下图，上面是修改前，下面是修改后：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="911" data-height="136"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-0749ee2821b8591d.png" data-original-width="911" data-original-height="136" data-original-format="image/png" data-original-filesize="29623" src="https://upload-images.jianshu.io/upload_images/11531502-0749ee2821b8591d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">增加端口打印</div>
</div>
<p>这样就改完了。</p>
<ul>
<li>修改nginx的conf配置文件：</li>
</ul>
<pre><code> upstream cluster &#123;
      server  192.168.2.43:8848;
      server  192.168.2.43:8849;
      server  192.168.2.43:8850;
  &#125;

  server &#123;
      listen       80;
      server_name  192.168.2.43;
      location / &#123;
      proxy_pass  http://cluster;
  &#125;
</code></pre>
<p>这样所有配置都整完了，接下来依次启动nginx和nacos.</p>
<ul>
<li>启动nginx；</li>
<li>启动nacos集群：</li>
</ul>
<pre><code>./startup.sh -p 8848
./startup.sh -p 8849
./startup.sh -p 8850
</code></pre>
<p>启动成功后，访问：<code>192.168.2.43/nacos</code>，登录后可以看到如下效果：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="799" data-height="534"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-b6b18a3b11e15f6d.png" data-original-width="799" data-original-height="534" data-original-format="image/png" data-original-filesize="36297" src="https://upload-images.jianshu.io/upload_images/11531502-b6b18a3b11e15f6d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">集群节点</div>
</div>
<p><strong>可能遇到的坑：</strong></p>
<ul>
<li>异常1：</li>
</ul>
<pre><code>unable to find local peer: 192.168.2.43:0, all peers: [192.168.2.43:8850, 192.168.2.43:8849, 192.168.2.43:8848]
</code></pre>
<p>解决办法：在<code>nacos/config/application.properties</code>中加上如下配置：</p>
<pre><code>nacos.inetutils.ip-address=192.168.2.43
</code></pre>
<ul>
<li>异常2：一直启动中，nacos is starting……，可能是虚拟机内存不够，将启动命令中为jvm分配的内存设置小一点即可，如下：</li>
</ul>
<pre><code>JAVA_OPT="$&#123;JAVA_OPT&#125; -server -Xms256m -Xmx256m -Xmn128m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=320m"
</code></pre>
<p><br></p>
<h1>五、springCloud Alibaba Sentinel介绍和基本使用</h1>
<p><strong>1、sentinel介绍：</strong><br>
之前我们用hystrix豪猪哥来实现服务降级熔断，sentinel也是干这事的，并且更加强大和好用。</p>
<ul>
<li>官网：<code>https://github.com/alibaba/Sentinel/wiki/%E4%BB%8B%E7%BB%8D</code>
</li>
</ul>
<p>sentinel能够解决的问题：</p>
<ul>
<li>服务雪崩</li>
<li>服务降级</li>
<li>服务熔断</li>
<li>服务限流</li>
</ul>
<p><strong>2、优点：</strong></p>
<ul>
<li>丰富的应用场景：秒杀、消息削峰填谷，集群流量控制，实时熔断等</li>
<li>完备的实时监控：精确到秒的实时监控</li>
<li>广泛的开原生态：可以快速的与springCloud、dubbo等框架整合</li>
<li>完善的SPI扩展点：提供了完善的SPI扩展接口，可以通过实现扩展接口来定制逻辑</li>
</ul>
<p><strong>3、下载安装：</strong></p>
<ul>
<li><p>下载地址：<code>https://github.com/alibaba/Sentinel/releases</code>，选择对应版本点击进入，下载dashboard即可，比如我下载的是<code>sentinel-dashboard-1.7.0.jar</code></p></li>
<li><p>使用文档：<code>https://spring-cloud-alibaba-group.github.io/github-pages/greenwich/spring-cloud-alibaba.html#_spring_cloud_alibaba_sentinel</code></p></li>
<li><p>sentinel运行：控制台由两部分构成，前台和后台。前台(即web界面)的端口是8080，所以8080端口不能被占用，并且要jdk8及以上。下载完成后直接<code>java -jar</code>运行jar包即可。然后访问8080，出现如下界面即启动成功，默认用户名和密码都是sentinel。</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1118" data-height="633"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-8625c97ab7b85d6c.png" data-original-width="1118" data-original-height="633" data-original-format="image/png" data-original-filesize="42917" src="https://upload-images.jianshu.io/upload_images/11531502-8625c97ab7b85d6c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel</div>
</div>
<p>相比豪猪哥，简单了很多，豪猪哥需要我们引入依赖后自己启动一个微服务当成dashboard，而sentinel不需要自己写，直接运行jar包就可以了。</p>
<p><strong>4、初用sentinel：</strong></p>
<ul>
<li>启动8848的nacos(为了简单，就启动了单机版而不是集群版)</li>
<li>新建名为cloudalibaba-sentinel-service8401的module：<br>
<strong><em>pom.xml：</em></strong>
</li>
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
<!-- nacos -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
<!-- 做持久化的时候会用到的 -->
<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-datasource-nacos</artifactId>
</dependency>
<!-- sentinel -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>
<!-- openfeign -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
</code></pre>
<p><strong><em>application.yml：</em></strong></p>
<pre><code>server:
  port: 8401
spring:
  application:
    name: cloudalibaba-sentinel-service
  cloud:
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
    sentinel:
      transport:
        dashboard: 192.168.0.106:8080
        port: 8719 # 默认8719，如果被占用会依次加1，直至找到没有被占用的端口
# actuator图形化配置
management:
  endpoints:
    web:
      exposure:
        include:
        - "*"
</code></pre>
<p><strong><em>主启动类：</em></strong></p>
<pre><code>@SpringBootApplication
@EnableDiscoveryClient
public class SentinalMain8401 &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(SentinalMain8401.class, args);
    &#125;
&#125;
</code></pre>
<p><strong><em>controller：</em></strong></p>
<pre><code>@RestController
@RequestMapping("/sentinel")
public class FlowLimitController &#123;

    @GetMapping("/testA")
    public String testA() &#123;
        return "=========== testA ==========";
    &#125;
    
    @GetMapping("/testB")
    public String testB() &#123;
        return "=========== testB ==========";
    &#125;
&#125;
</code></pre>
<ul>
<li>启动8080的sentinel</li>
<li>启动8401的微服务</li>
<li>访问8401微服务，然后看sentinel控制台是否有相关信息</li>
</ul>
<p>8080控制台并没有任何8401的相关信息，不要方，这是因为sentinel使用懒加载机制，没调用的不会出现在dashboard中。访问一下8401，然后再看dashboard中就有了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1124" data-height="686"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-417263910922ba7a.png" data-original-width="1124" data-original-height="686" data-original-format="image/png" data-original-filesize="73232" src="https://upload-images.jianshu.io/upload_images/11531502-417263910922ba7a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel正在监控8401</div>
</div>
<p>然后访问几次8401，实时监控中就会有相关信息了，如下图：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1130" data-height="641"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-ba8a88c2bc56b6af.png" data-original-width="1130" data-original-height="641" data-original-format="image/png" data-original-filesize="80614" src="https://upload-images.jianshu.io/upload_images/11531502-ba8a88c2bc56b6af.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">testA的调用信息</div>
</div>
<p><strong><em>可能遇到的坑：</em></strong>不管怎么访问8401，实时监控中都没有调用信息，可能的原因有：</p>
<ul>
<li>如果你的sentinel运行在虚拟机上，8401运行在自己电脑上，那么可能原因是虚拟机时间和本机时间不一致导致。解决办法就是更新虚拟机时间，命令如下：</li>
</ul>
<pre><code>yum -y install ntp ntpdate
ntpdate cn.pool.ntp.org
</code></pre>
<ul>
<li>如果sentinel运行在虚拟机上，8401在本机，访问8401后，sentinel没有监控到，并且sentinel运行日志报了如下的错误：</li>
</ul>
<pre><code>java.util.concurrent.ExecutionException: java.net.NoRouteToHostException: 没有到主机的路由
</code></pre>
<p>解决办法就是在8401的application.yml中加上如下配置：</p>
<pre><code>sentinel:
      transport:
        dashboard: 192.168.0.106:8080
        client-ip: 192.168.0.104 # 这一行是新加的
        port: 8719 # 默认8719，如果被占用会依次加1，直至找到没有被占用的端口
</code></pre>
<p>就是加上client-ip，值就是8401项目，即你要sentinel监控的项目所运行的机器的IP。</p>
<h1>六、sentinel流控规则</h1>
<p><strong>1、基本介绍：</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="837" data-height="627"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-d014d608f20d14ef.png" data-original-width="837" data-original-height="627" data-original-format="image/png" data-original-filesize="51203" src="https://upload-images.jianshu.io/upload_images/11531502-d014d608f20d14ef.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel流控规则</div>
</div>
<p>在sentinel的dashboard中有一个流控规则，如上图，下面对这些名词进行解释。</p>
<ul>
<li>资源名：唯一名称，默认请求路径</li>
<li>针对来源：sentinel可以针对调用者进行限流，填写微服务名称，默认default，表示不区分来源</li>
<li>阈值类型：QPS（每秒钟的请求数）：当调用该API的QPS达到阈值时，进行限流；线程数：当调用该API的线程数达到阈值时进行限流</li>
<li>是否集群：不需要集群</li>
<li>流控模式：直接：达到限流条件时直接限流；关联：关联的资源达到阈值时限流自己（当与A关联的资源B达到阈值时，就限流A自己。应用场景：支付服务达到阈值的时候，就限流下订单的服务）；链路：只记录指定链路上的流量（指定资源从入口资源进来的流量，如果达到阈值，就进行限流，API级别的针对来源）</li>
<li>流控效果：快速失败：直接失败，抛异常；warm up：根据codeFactor（冷加载因子，默认是3）的值，从阈值/codeFactor，经过预热时长，才达到设置的QPS阈值</li>
<li>排队等待：匀速排队，让请求以匀速通过，阈值类型必须设置为QPS，否则无效</li>
</ul>
<p><strong>2、流控模式：</strong></p>
<p><strong><em>流控模式之直接：</em></strong></p>
<p><em>QPS直接快速失败：</em></p>
<ul>
<li>添加流控规则：在簇点链路那里添加流控即可，比如我添加的如下：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="843" data-height="592"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-a580497bae57c513.png" data-original-width="843" data-original-height="592" data-original-format="image/png" data-original-filesize="52372" src="https://upload-images.jianshu.io/upload_images/11531502-a580497bae57c513.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel QPS直接快速失败</div>
</div>
<p>这里设置的意思就是，访问testB，一秒钟超过一次，就是直接快速报错。我现在对testB连点两下，就会返回如下信息：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="712" data-height="254"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-e241ab38417ea5ac.png" data-original-width="712" data-original-height="254" data-original-format="image/png" data-original-filesize="10508" src="https://upload-images.jianshu.io/upload_images/11531502-e241ab38417ea5ac.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel对testB进行流控</div>
</div>
<ul>
<li>存在的问题：超过QPS阈值的时候，返回的是默认信息<code>Blocked by Sentinel (flow limiting)</code>，如何自定义呢？应该有hystrix一样的兜底方法（后续再说其用法）。</li>
</ul>
<p><em>线程数直接失败：</em></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="833" data-height="521"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-dbef78d2a931fd2f.png" data-original-width="833" data-original-height="521" data-original-format="image/png" data-original-filesize="41812" src="https://upload-images.jianshu.io/upload_images/11531502-dbef78d2a931fd2f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel线程数直接失败</div>
</div>
<p>我们再访问testB，发现不管点多快，都没有被流控给拦住。因为我们在一个浏览器中访问，始终是一个线程。这样配置的意思就是并发线程数超过阈值1时，就会返回失败信息。可以用jmeter模拟并发访问的情况。</p>
<p><strong><em>流控模式之关联：</em></strong></p>
<p>配置如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="822" data-height="640"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-8671ac9ce9a72609.png" data-original-width="822" data-original-height="640" data-original-format="image/png" data-original-filesize="55380" src="https://upload-images.jianshu.io/upload_images/11531502-8671ac9ce9a72609.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel流控之关联</div>
</div>
<p>这里的意思就是testA的QPS数超过1，就会导致testB不能用。测试方法：用jmeter对testA进行并发访问，然后我们在浏览器访问testB。就会发现也会返回<code>Blocked by Sentinel (flow limiting)</code>。</p>
<p><strong><em>流控模式之链路：</em></strong><br>
多个请求调用了同一个微服务超过了QPS阈值就会快速失败，配置如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="819" data-height="647"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-f74a04c6240c2e7a.png" data-original-width="819" data-original-height="647" data-original-format="image/png" data-original-filesize="56067" src="https://upload-images.jianshu.io/upload_images/11531502-f74a04c6240c2e7a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel流控之链路</div>
</div>
<p>注意入口资源的名字就是sentinel簇点链路中显示的名字。然后快速访问A，只要QPS超过1，就会返回<code>Blocked by Sentinel (flow limiting)</code>。</p>
<p><strong>3、流控效果：</strong><br>
上面用的流控效果都是快速失败，现在来认识一下这些流控效果。</p>
<ul>
<li>快速失败：上面的案例都是直接失败，就是超过阈值就返回<code>Blocked by Sentinel (flow limiting)</code>
</li>
<li>预热（ Warm Up）：请求的QPS从 <code>阈值 / 冷加载因子(默认是3)</code>开始，经过 <code>预热时长</code>，最后达到阈值。比如下图的配置意思是：初始阈值为 <code>10 / 3 = 3</code>，经过10秒钟的时间，阈值慢慢升到10。现在快速访问testA，因为一开始QPS阈值为3，所以你点快一点可能就失败了，但是慢慢地，你点很快都不会失败了，因为最后阈值升为10，正常情况下没有人手速能达到1秒钟点11次吧。</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="843" data-height="645"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-617cec250e23ac40.png" data-original-width="843" data-original-height="645" data-original-format="image/png" data-original-filesize="55191" src="https://upload-images.jianshu.io/upload_images/11531502-617cec250e23ac40.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel流控效果之预热</div>
</div>
<ul>
<li>排队等待：就是不管同时有多少个请求过来，我每秒钟只处理阈值数的请求，其他老老实实排队等待去。如下图配置意思就是每秒钟只处理一个，其他的排队等着，每隔1000毫秒才放下一个请求进来。</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="820" data-height="621"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-2a2a6da19777037c.png" data-original-width="820" data-original-height="621" data-original-format="image/png" data-original-filesize="53878" src="https://upload-images.jianshu.io/upload_images/11531502-2a2a6da19777037c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">sentinel流控效果之排队等待</div>
</div>
  
</div>
            