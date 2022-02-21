
---
title: 'Spring Cloud 2021.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=410'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 14:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=410'
---

<div>   
<div class="content">
                                                                                            <p>Spring Cloud 2021.0.1 正式发布，这是 Spring Cloud 2021 的第一个错误修正版本。</p> 
<p><strong>支持 2021.0.0 平稳升级</strong></p> 
<p>目前已经可以从中央仓库获取，坐标如下：</p> 
<pre><code class="language-xml">dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>2021.0.1</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
    ...
</dependencies>
</code></pre> 
<h2>更新日志</h2> 
<h3>Spring Cloud Gateway</h3> 
<ul> 
 <li> <p>新增路由谓词，用于检查 X-Forwarded-for 请求值的合法性，类似于 RemoteAddr 谓词</p> </li> 
 <li> <p>允许设置网关 HandlerMapping 的顺序。默认情况下 GatewyHandlerMapping 优先级最高</p> </li> 
</ul> 
<h3>Spring Cloud Openfeign</h3> 
<ul> 
 <li>更新至 OpenFeign 11.8</li> 
 <li>支持 OkHttpClient 的 readTimeout 属性</li> 
 <li>OAuth2FeignRequestInterceptor 配置 AccessTokenProvider 连接器自动负载均衡</li> 
</ul> 
<h3>Spring Cloud Config</h3> 
<ul> 
 <li>修复文件匹配器 在 JSON 、YAML、properties 格式处理 BUG</li> 
</ul> 
<h3>Spring Cloud Sleuth</h3> 
<ul> 
 <li> <p>修复 springboot 2.6.x 应用启动失败</p> </li> 
 <li> <p>TraceId 在线程池之间传递，污染上下文</p> </li> 
 <li> <p>添加对非 Brave Kafka 消息容器的支持</p> </li> 
</ul> 
<h2>依赖升级</h2> 
<p>以下模块升级至 2021.0.1</p> 
<table> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Spring Cloud Config</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Zookeeper</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Circuitbreaker</td> 
   <td>2.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Kubernetes</td> 
   <td>2.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Commons</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Sleuth</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Contract</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Task</td> 
   <td>2.4.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Gateway</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Openfeign</td> 
   <td>3.1.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Starter Build</td> 
   <td>2021.0.1</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Netflix</td> 
   <td>3.1.1</td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            