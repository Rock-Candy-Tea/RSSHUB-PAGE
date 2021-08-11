
---
title: '在 Spring Boot 中使用 HikariCP 连接池'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-48b123710538f67b.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-48b123710538f67b.png'
---

<div>   
<p>上次帮小王解决了如何在 Spring Boot 中使用 JDBC 连接 MySQL 后，我就一直在等，等他问我第三个问题，比如说如何在 Spring Boot 中使用 HikariCP 连接池。但我等了四天也没有等到任何音讯，似乎他从我的世界里消失了，而我却仍然沉醉在他拍我马屁的美妙感觉里。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="240" data-height="240"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-48b123710538f67b.png" data-original-width="240" data-original-height="240" data-original-format="image/png" data-original-filesize="57974" src="https://upload-images.jianshu.io/upload_images/1179389-48b123710538f67b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>突然感觉，没有小王的日子里，好空虚。怎么办呢？想来想去还是写文章度日吧，积极创作的过程中，也许能够摆脱对小王的苦苦思念。写什么好呢？</p>
<p>想来想去，就写如何在 Spring Boot 中使用 HikariCP 连接池吧。毕竟实战项目当中，肯定不能使用 JDBC，连接池是必须的。而 HikariCP 据说非常的快，快到 Spring Boot 2 默认的数据库连接池也从 Tomcat 切换到了 HikariCP（喜新厌旧的臭毛病能不能改改）。</p>
<p>HikariCP 的 GitHub 地址如下：</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fbrettwooldridge%2FHikariCP" target="_blank">https://github.com/brettwooldridge/HikariCP</a></p>
<p>目前星标 12K，被使用次数更是达到了 43.1K。再来看看它的自我介绍。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1373" data-height="466"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-5659eb095812061e.png" data-original-width="1373" data-original-height="466" data-original-format="image/png" data-original-filesize="81916" src="https://upload-images.jianshu.io/upload_images/1179389-5659eb095812061e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>牛逼的不能行啊，原来 Hikari 来源于日语，“光”的意思，这意味着快得像光速一样吗？讲真，看简介的感觉就好像在和我的女神“汤唯”握手一样刺激和震撼。</p>
<p>既然 Spring Boot 2 已经默认使用了 HikariCP，那么使用起来也相当的轻松惬意，只需要简单几个步骤。</p>
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
<div class="image-view" data-width="696" data-height="530"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-b3c540d815151a03.png" data-original-width="696" data-original-height="530" data-original-format="image/png" data-original-filesize="60182" src="https://upload-images.jianshu.io/upload_images/1179389-b3c540d815151a03.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>勾选 Web、JDBC、MySQL Driver 等三个依赖。</p>
<p>1）Web 表明该项目是一个 Web 项目，便于我们直接通过 URL 来实操。</p>
<p>3）MySQL Driver：连接 MySQL 服务器的驱动器。</p>
<p>5）JDBC：Spring Boot 2 默认使用了 HikariCP，所以 HikariCP 会默认在 spring-boot-starter-jdbc 中附加依赖，因此不需要主动添加 HikariCP 的依赖。</p>
<p>PS：怎么证明这一点呢？项目导入成功后，在 pom.xml 文件中，按住鼠标左键 + Ctrl 键访问 spring-boot-starter-jdbc 依赖节点，可在 spring-boot-starter-jdbc.pom 文件中查看到 HikariCP 的依赖信息。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="407" data-height="181"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-f6df51a5687426e1.png" data-original-width="407" data-original-height="181" data-original-format="image/png" data-original-filesize="13512" src="https://upload-images.jianshu.io/upload_images/1179389-f6df51a5687426e1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>选项选择完后，就可以点击【Generate】按钮生成一个初始化的 Spring Boot 项目了。生成的是一个压缩包，导入到 IDE 的时候需要先解压。</p>
<h3>03、编辑 application.properties 文件</h3>
<p>项目导入成功后，等待 Maven 下载依赖，完成后编辑 application.properties 文件，配置 MySQL 数据源信息。</p>
<pre><code>spring.datasource.url=jdbc:mysql://127.0.0.1:3306/springbootdemo?useUnicode=true&characterEncoding=UTF-8&serverTimezone=UTC
spring.datasource.username=root
spring.datasource.password=123456
</code></pre>
<p>是不是有一种似曾相识的感觉（和<a href="https://www.jianshu.com/p/826accd69217" target="_blank">上一篇</a>中的数据源配置一模一样）？为什么呢？答案已经告诉过大家了——默认、默认、默认，重要的事情说三遍，Spring Boot 2 默认使用了 HikariCP 连接池。</p>
<h3>04、编辑 Spring Boot 项目</h3>
<p>为了便于我们查看 HikariCP 的连接信息，我们对 SpringBootMysqlApplication 类进行编辑，增加以下内容。</p>
<pre><code class="java">@SpringBootApplication
public class HikariCpDemoApplication implements CommandLineRunner &#123;
    @Autowired
    private DataSource dataSource;

    public static void main(String[] args) &#123;
        SpringApplication.run(HikariCpDemoApplication.class, args);
    &#125;

    @Override
    public void run(String... args) throws Exception &#123;
        Connection conn = dataSource.getConnection();
        conn.close();
    &#125;
&#125;
</code></pre>
<p>HikariCpDemoApplication 实现了 CommandLineRunner 接口，该接口允许我们在项目启动的时候加载一些数据或者做一些事情，比如说我们尝试通过 DataSource 对象与数据源建立连接，这样就可以在日志信息中看到 HikariCP 的连接信息。CommandLineRunner 接口有一个方法需要实现，就是我们看到的 <code>run()</code> 方法。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1164" data-height="387"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-73517fb73ae45744.png" data-original-width="1164" data-original-height="387" data-original-format="image/png" data-original-filesize="54170" src="https://upload-images.jianshu.io/upload_images/1179389-73517fb73ae45744.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>通过 debug 的方式，我们可以看到，在项目运行的过程中，dataSource 这个 Bean 的类型为 HikariDataSource。</p>
<h3>05、运行 Spring Boot 项目</h3>
<p>接下来，我们直接运行 <code>HikariCpDemoApplication</code> 类，这样一个 Spring Boot 项目就启动成功了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="830" data-height="71"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-c11071af357f8e92.png" data-original-width="830" data-original-height="71" data-original-format="image/png" data-original-filesize="7170" src="https://upload-images.jianshu.io/upload_images/1179389-c11071af357f8e92.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>HikariDataSource 对象的连接信息会被打印出来。也就是说，HikariCP 连接池的配置启用了。快给自己点个赞。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="255" data-height="256"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-c3e24c85cbcb28f0.png" data-original-width="255" data-original-height="256" data-original-format="image/png" data-original-filesize="83519" src="https://upload-images.jianshu.io/upload_images/1179389-c3e24c85cbcb28f0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>06、为什么 Spring Boot 2.0 选择 HikariCP 作为默认数据库连接池</h3>
<p>有几种基准测试结果可用来比较HikariCP和其他连接池框架（例如<em><a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.mchange.com%2Fprojects%2Fc3p0%2F" target="_blank">c3p0</a></em>，<em><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcommons.apache.org%2Fproper%2Fcommons-dbcp%2F" target="_blank">dbcp2</a></em>，<em><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fpeople.apache.org%2F%7Efhanik%2Fjdbc-pool%2Fjdbc-pool.html" target="_blank">tomcat</a></em>和<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.vibur.org%2F" target="_blank"><em>vibur）的性能</em></a>。例如，HikariCP团队发布了以下基准（可<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fbrettwooldridge%2FHikariCP-benchmark" target="_blank">在此处</a>获得原始结果）：</p>
<p>HikariCP 团队为了证明自己性能最佳，特意找了几个背景对比了下。不幸充当背景的有 c3p0、dbcp2、tomcat 等传统的连接池。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1295" data-height="581"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-c04bd15efd464b2d.png" data-original-width="1295" data-original-height="581" data-original-format="image/png" data-original-filesize="180266" src="https://upload-images.jianshu.io/upload_images/1179389-c04bd15efd464b2d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>从上图中，我们能感受出背景的尴尬，HikariCP 鹤立鸡群了。HikariCP 制作以如此优秀，原因大致有下面这些：</p>
<p>1）字节码级别上的优化：要求编译后的字节码最少，这样 CPU 缓存就可以加载更多的程序代码。</p>
<p>HikariCP 优化前的代码片段：</p>
<pre><code class="java">public final PreparedStatement prepareStatement(String sql, String[] columnNames) throws SQLException
&#123;
    return PROXY_FACTORY.getProxyPreparedStatement(this, delegate.prepareStatement(sql, columnNames));
&#125;
</code></pre>
<p>HikariCP 优化后的代码片段：</p>
<pre><code class="java">public final PreparedStatement prepareStatement(String sql, String[] columnNames) throws SQLException
&#123;
    return ProxyFactory.getProxyPreparedStatement(this, delegate.prepareStatement(sql, columnNames));
&#125;
</code></pre>
<p>以上两段代码的差别只有一处，就是 ProxyFactory 替代了 PROXY_FACTORY，这个改动后的字节码比优化前减少了 3 行指令。具体的分析参照 HikariCP 的 Wiki <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fbrettwooldridge%2FHikariCP%2Fwiki%2FDown-the-Rabbit-Hole" target="_blank">文档</a>。</p>
<p>2）使用自定义的列表（FastStatementList）代替 ArrayList，可以避免 <code>get()</code> 的时候进行范围检查，<code>remove()</code> 的时候从头到尾的扫描。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1078" data-height="519"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-24662e1d059f0014.png" data-original-width="1078" data-original-height="519" data-original-format="image/png" data-original-filesize="144989" src="https://upload-images.jianshu.io/upload_images/1179389-24662e1d059f0014.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>07、鸣谢</h3>
<p>好了，各位读者朋友们，答应小王的文章终于写完了。<strong>能看到这里的都是最优秀的程序员，升职加薪就是你了</strong>👍。如果觉得不过瘾，还想看到更多，可以 star 二哥的 GitHub【<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2Fitwanger.github.io" target="_blank">itwanger.github.io</a>】，本文已收录。</p>
<p>PS：本文配套的源码已上传至 GitHub 【<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2FSpringBootDemo" target="_blank">SpringBootDemo.SpringBootMysql</a>】。</p>
<p>原创不易，如果觉得有点用的话，请不要吝啬你手中<strong>点赞</strong>的权力；如果想要第一时间看到二哥更新的文章，请扫描下方的二维码，关注沉默王二公众号。我们下篇文章见！</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="900" data-height="500"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-1d346c25dfc2b58f.jpeg" data-original-width="900" data-original-height="500" data-original-format="image/jpeg" data-original-filesize="103638" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
  
</div>
            