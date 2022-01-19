
---
title: '被缠上了，小王问我怎么在 Spring Boot 中使用 JDBC 连接 MySQL'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-452a8ff7ffae502b.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-452a8ff7ffae502b.png'
---

<div>   
<p>上次帮小王<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FRa9zotaUTsm3z-UMimB5pg" target="_blank">入了 Spring Boot 的门</a>后，他觉得我这个人和蔼可亲、平易近人，于是隔天小王又微信我说：“二哥，快教教我，怎么在 Spring Boot  项目中使用 JDBC 连接 MySQL 啊？”</p>
<p>收到问题的时候，我有点头大，难道以后就要被小王缠上了？</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="255" data-height="255"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-452a8ff7ffae502b.png" data-original-width="255" data-original-height="255" data-original-format="image/png" data-original-filesize="145616" src="https://upload-images.jianshu.io/upload_images/1179389-452a8ff7ffae502b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>没等我发牢骚，小王就紧接着说：“二哥，你先别生气，上次你帮了我的忙后，我在心里感激了你一晚上，想着第一次遇到这么亲切的大佬，一定要抱紧大腿。。。。。”</p>
<p>马屁拍到这份上，我的气自然也就消了。随后，我花了五分钟的时间帮他解决了苦恼，没成想，他又发给我了一个小红包，表示对我的感谢。并建议我再写一篇文章出来，因为他觉得像他这样的小白还有很多。没办法，我关上门，开了灯，开始了今天这篇文章的创作。</p>
<h3>01、初始化 MySQL 数据库</h3>
<p>既然要连接 MySQL，那么就需要先在电脑上安装 MySQL 服务（本文暂且跳过），并且创建数据库和表。</p>
<pre><code class="sql">CREATE DATABASE `springbootdemo`;
DROP TABLE IF EXISTS `mysql_datasource`;
CREATE TABLE `mysql_datasource` (
  `id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
</code></pre>
<h3>02、使用 Spring Initlallzr 创建 Spring Boot 项目</h3>
<p>创建一个 Spring Boot 项目非常简单，通过 Spring Initlallzr（<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fstart.spring.io%2F" target="_blank">https://start.spring.io/</a>）就可以了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="720" data-height="955"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-ddf6ce81b536bd0e.png" data-original-width="720" data-original-height="955" data-original-format="image/png" data-original-filesize="104789" src="https://upload-images.jianshu.io/upload_images/1179389-ddf6ce81b536bd0e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>勾选 Lombok、Web、MySQL Driver、Actuator、JDBC 等五个依赖。</p>
<p>1）Lombok 是一种 Java 实用工具，可用来帮助开发人员消除 Java 的一些冗余代码，比如说可以通过注解生成 getter/setter。使用之前需要先在 IDE 中安装插件。</p>
<p>2）Web 表明该项目是一个 Web 项目，便于我们直接通过 URL 来实操。</p>
<p>3）MySQL Driver：连接 MySQL 服务器的驱动器。</p>
<p>4）Actuator 是 Spring Boot 提供的对应用系统的自省和监控的集成功能，可以查看应用配置的详细信息，例如自动化配置信息、创建的 Spring beans 以及一些环境属性等。</p>
<p>5）JDBC：本篇文章我们通过 JDBC 来连接和操作数据库。</p>
<p>选项选择完后，就可以点击【Generate】按钮生成一个初始化的 Spring Boot 项目了。生成的是一个压缩包，导入到 IDE 的时候需要先解压。</p>
<h3>03、编辑 application.properties 文件</h3>
<p>项目导入成功后，等待 Maven 下载依赖，完成后编辑 application.properties 文件，配置 MySQL 数据源信息。</p>
<pre><code>spring.datasource.url=jdbc:mysql://127.0.0.1:3306/springbootdemo
spring.datasource.username=root
spring.datasource.password=123456
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
</code></pre>
<p>1）<code>spring.datasource.</code> 为固定格式。</p>
<p>2）URL 为 MySQL 的连接地址。</p>
<p>3）username 为数据库的访问用户名。</p>
<p>4）password 为数据库的访问密码。</p>
<p>5）driver-class-name 用来指定数据库的驱动器。也可以不指定，Spring Boot 会根据 URL（有 mysql 关键字） 自动匹配驱动器。</p>
<h3>04、编辑 Spring Boot 项目</h3>
<p>为了便于我们操作，我们对 SpringBootMysqlApplication 类进行编辑，增加以下内容。</p>
<pre><code class="java">@SpringBootApplication
@RestController
public class SpringBootMysqlApplication &#123;
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @RequestMapping("insert")
    public String insert() &#123;
        String id = UUID.randomUUID().toString();
        String sql = "insert into mysql_datasource (id,name) values ('"+id+"','沉默王二')";
        jdbcTemplate.execute(sql);
        return "插入完毕";
    &#125;

&#125;
</code></pre>
<p>1）@SpringBootApplication、@RestController、@RequestMapping 注解在<a href="https://www.jianshu.com/p/c06c324ea255" target="_blank">之前的文章</a>中已经介绍过了，这里不再赘述。</p>
<p>2）@Autowired：顾名思义，用于自动装配 Java Bean。</p>
<p>3）JdbcTemplate：Spring 对数据库的操作在 jdbc 上做了深层次的封装，利用 Spring 的注入功能可以把 DataSource 注册到 JdbcTemplate 之中。JdbcTemplate 提供了四个常用的方法。</p>
<p>①、execute() 方法：用于执行任何 SQL 语句。</p>
<p>②、update() 方法：用于执行新增、修改、删除等 SQL 语句。</p>
<p>③、query() 方法：用于执行查询相关 SQL 语句。</p>
<p>④、call() 方法：用于执行存储过程、函数相关 SQL 语句。</p>
<p>本例中我们使用 execute() 方法向 mysql_datasource 表中插入一行数据 <code>&#123;id:uuid, name:'沉默王二'&#125;</code>。</p>
<h3>05、运行 Spring Boot 项目</h3>
<p>接下来，我们直接运行 <code>SpringBootMysqlApplication</code> 类，这样一个 Spring Boot 项目就启动成功了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1800" data-height="172"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-ea7987e76c205e60.png" data-original-width="1800" data-original-height="172" data-original-format="image/png" data-original-filesize="51127" src="https://upload-images.jianshu.io/upload_images/1179389-ea7987e76c205e60.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这时候，我们可以直接浏览器的 URL 中键入 <code>http://localhost:8080/insert</code> 测试 MySQL 的插入语句是否执行成功。很遗憾，竟然出错了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1052" data-height="411"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-889bbf157e24b33b.png" data-original-width="1052" data-original-height="411" data-original-format="image/png" data-original-filesize="99080" src="https://upload-images.jianshu.io/upload_images/1179389-889bbf157e24b33b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>该怎么办呢？这需要我们在连接字符串中显式指定时区，修改 spring.datasource.url 为以下内容。</p>
<pre><code>spring.datasource.url=jdbc:mysql://127.0.0.1:3306/springbootdemo?serverTimezone=UTC
</code></pre>
<p>重新运行该项目后再次访问，发现数据插入成功了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="482" data-height="109"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-f064cb967e75bb37.png" data-original-width="482" data-original-height="109" data-original-format="image/png" data-original-filesize="9010" src="https://upload-images.jianshu.io/upload_images/1179389-f064cb967e75bb37.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>为了确保数据是否真的插入成功了，我们通过 Navicat（一款强大的数据库管理和设计工具）来查看一下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="538" data-height="150"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-10b4c575499daf18.png" data-original-width="538" data-original-height="150" data-original-format="image/png" data-original-filesize="15779" src="https://upload-images.jianshu.io/upload_images/1179389-10b4c575499daf18.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>情况不妙，中文乱码了。该怎么办呢？需要我们在连接字符串中显式指定字符集，修改 spring.datasource.url 为以下内容。</p>
<pre><code>spring.datasource.url=jdbc:mysql://127.0.0.1:3306/springbootdemo?useUnicode=true&characterEncoding=utf-8&serverTimezone=UTC
</code></pre>
<p>重新运行该项目后再次访问，发现中文不再乱码了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="543" data-height="191"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-c880526a301fd38e.png" data-original-width="543" data-original-height="191" data-original-format="image/png" data-original-filesize="17132" src="https://upload-images.jianshu.io/upload_images/1179389-c880526a301fd38e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>快给自己点个赞。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="240" data-height="240"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-124546f7d9bef7a5.gif" data-original-width="240" data-original-height="240" data-original-format="image/gif" data-original-filesize="274532" src="https://upload-images.jianshu.io/upload_images/1179389-124546f7d9bef7a5.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>06、鸣谢</h3>
<p>我是沉默王二，一枚有趣的程序员。如果觉得文章对你有点帮助，请微信搜索「 <strong>沉默王二</strong> 」第一时间阅读，回复【<strong>666</strong>】更有我为你精心准备的 500G 高清教学视频（已分门别类）。</p>
<blockquote>
<p>本文 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2Fitwanger.github.io" target="_blank">GitHub</a> 已经收录，有大厂面试完整考点，欢迎 Star。</p>
</blockquote>
<p><strong>原创不易，莫要白票，请你为本文点个赞吧</strong>，这将是我写作更多优质文章的最强动力。</p>
  
</div>
            