
---
title: 'SpringBoot之程序性能监控'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/16753854-01f58707856a7da1.jpg'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/16753854-01f58707856a7da1.jpg'
---

<div>   
<h4>经典名言--无监控不调优</h4>
<ul>
<li>要想进行SpringBoot项目调优，首选需要监控项目运行时情况。<br>
当下SpringBoot项目逐渐替代早期的Spring项目，随着用户量的增加，Spring Boot框架也提供了actuator模块。该模块很方便的对你的Spring Boot程序做监控。在SpringBoot中加入监控的方法只需要把相应的监控依赖actuator引入即可。</li>
<li>pom文件中引入actuator依赖<br>
首先需要在pom.xml文件中引入以下依赖：</li>
</ul>
<pre><code><dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
</code></pre>
<ul>
<li>为了保证actuator接口的敏感性，需要在配置文件中开放安全属性配置<br>
配置参数如下：</li>
</ul>
<pre><code>management.security.enabled=false
</code></pre>
<p>配置后就可以允许你查看Spring Boot进程的actuator信息了</p>
<ul>
<li>
<p>启动日志查看</p>
<ul>
<li>
<p>启动SpringBoot程序，控制台日志里可以看到actuator接口信息</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="433"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-01f58707856a7da1.jpg" data-original-width="1080" data-original-height="433" data-original-format="image/jpeg" data-original-filesize="128609" src="https://upload-images.jianshu.io/upload_images/16753854-01f58707856a7da1.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<br>
<p>通过上图打印信息，我们可以实时的获取应用的各项监控指标，用于后期的问题排查和调优。</p>
</li>
</ul>
</li>
<li><p>actuator的接口分为原生接口和用户自定义接口<br>
原生接口主要有如下几个：</p></li>
</ul>
<table>
<thead>
<tr>
<th>路径</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>health</td>
<td>展示了进程的健康状态</td>
</tr>
<tr>
<td>beans</td>
<td>程序创建的Bean</td>
</tr>
<tr>
<td>configprops</td>
<td>配置信息，属性值</td>
</tr>
<tr>
<td>env</td>
<td>环境属性</td>
</tr>
<tr>
<td>info</td>
<td>info开头的程序属性信息</td>
</tr>
<tr>
<td>metrics</td>
<td>度量指标，比如JVM和HTTP请求等</td>
</tr>
<tr>
<td>trace</td>
<td>HTTP的详细请求信息</td>
</tr>
<tr>
<td>mappings</td>
<td>所有的URL路径映射关系</td>
</tr>
<tr>
<td>dump</td>
<td>线程快照信息</td>
</tr>
<tr>
<td>heapdump</td>
<td>内存快照信息</td>
</tr>
</tbody>
</table>
<p>如果你想关闭某个接口，比如关闭health接口，可以通过设置来实现：</p>
<pre><code>endpoints.health.enabled=false
</code></pre>
<ul>
<li>
<p>监控展示器-JConsole<br>
JConsole说明：是一个内置Java性能分析器，如果你本机已经配置了jdk的话，可直接命令行输入jconsole，打开后的页面如下图所示：</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="532" data-height="551"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-e34ba9fe330e8729.png" data-original-width="532" data-original-height="551" data-original-format="image/png" data-original-filesize="189228" src="https://upload-images.jianshu.io/upload_images/16753854-e34ba9fe330e8729.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<br>
<p>选择你要监控的进程，点击连接即可进入该Java进程的监控首页，如下图所示（类似jdk自带的jvisualvm）：</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1063" data-height="784"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-3d8f1ca2bfedacf3.png" data-original-width="1063" data-original-height="784" data-original-format="image/png" data-original-filesize="299073" src="https://upload-images.jianshu.io/upload_images/16753854-3d8f1ca2bfedacf3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<br>
jvisualvm监控图对比<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1188" data-height="650"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-6a1679508bb95b6b.png" data-original-width="1188" data-original-height="650" data-original-format="image/png" data-original-filesize="56171" src="https://upload-images.jianshu.io/upload_images/16753854-6a1679508bb95b6b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
<li><p>Spring Boot Admin是一款开源软件<br>
Spring Boot Admin是一款监控和管理Spring Boot应用程序的开源软件。Spring Boot Admin读取actuator的接口数据，并通过Spring Boot Admin UI将实时数据展示在前端。</p></li>
<li><p>实现步骤<br>
首先创建一个Spring Boot Admin Server，首先需要创建一个基本的Spring Boot应用程序，这个就不做赘述了，并加入以下依赖：</p></li>
</ul>
<pre><code><dependency>
  <groupId>de.codecentric</groupId>
  <artifactId>spring-boot-admin-server</artifactId>
  <version>1.5.7</version>
</dependency>

<dependency>
  <groupId>de.codecentric</groupId>
  <artifactId>spring-boot-admin-server-ui</artifactId>
  <version>1.5.7</version>
</dependency>
</code></pre>
<p>随后把server.port端口设置为8090，并注册到你的eureka服务上</p>
<ul>
<li>启动类中使用注解开启服务</li>
</ul>
<pre><code>@SpringBootApplication
@EnableDiscoveryClient
@EnableAdminServer
@EnableTurbine
public class HtsApplication &#123;

  public static void main(String[] args) &#123;
    SpringApplication.run(HtsApplication.class, args);
  &#125;
&#125;
</code></pre>
<p>在浏览器输入url：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A8090" target="_blank">http://localhost:8090</a><br>
就可以看到Spring Boot Admin Server的页面信息<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="199"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-725b797149c391eb.jpg" data-original-width="1080" data-original-height="199" data-original-format="image/jpeg" data-original-filesize="19570" src="https://upload-images.jianshu.io/upload_images/16753854-725b797149c391eb.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<ul>
<li>在任意需要被监控的Spring Boot应用程序上添加依赖</li>
</ul>
<pre><code><dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-client</artifactId>
    <version>1.5.7</version>
</dependency>
</code></pre>
<ul>
<li>最后启动客户端，其中Spring Boot Admin Server从Eureka上拿到注册信息后完成认证<br>
在浏览器中输入url：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A8090" target="_blank">http://localhost:8090</a> 就可以看到应用程序的监控信息了。<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="385"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-bf8fd93406b12144.jpg" data-original-width="1080" data-original-height="385" data-original-format="image/jpeg" data-original-filesize="35374" src="https://upload-images.jianshu.io/upload_images/16753854-bf8fd93406b12144.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
</ul>
<hr>
  
</div>
            