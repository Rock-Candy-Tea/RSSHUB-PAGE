
---
title: '年末巨献 __ Spring Cloud 2021 （朱比利） 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://minio.pigx.vip/oss/1638510332.png'
author: 开源中国
comments: false
date: Fri, 03 Dec 2021 06:03:00 GMT
thumbnail: 'https://minio.pigx.vip/oss/1638510332.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://minio.pigx.vip/oss/1638510332.png" referrerpolicy="no-referrer"></p> 
<h2><span>Spring Cloud 2021 （朱比利） 发布</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">Spring Cloud 2021 （Jubilee）正式发布 ,此版本 <strong style="color:#47c1a8">基于 Spring Boot 2.6.x 构建</strong>，不兼容 SpringBoot 2.5.x 或者低版本。</p> </li> 
 <li> <p style="color:#595959; margin-left:0; margin-right:0">现在已经可以从中央仓库下载</p> </li> 
</ul> 
<pre><code>   <span><<span style="color:#e45649">dependency</span>></span>
    <span><<span style="color:#e45649">groupId</span>></span>org.springframework.cloud<span></<span style="color:#e45649">groupId</span>></span>
    <span><<span style="color:#e45649">artifactId</span>></span>spring-cloud-dependencies<span></<span style="color:#e45649">artifactId</span>></span>
    <span><<span style="color:#e45649">version</span>></span>2021.0.0<span></<span style="color:#e45649">version</span>></span>
    <span><<span style="color:#e45649">type</span>></span>pom<span></<span style="color:#e45649">type</span>></span>
    <span><<span style="color:#e45649">scope</span>></span>import<span></<span style="color:#e45649">scope</span>></span>
   <span></<span style="color:#e45649">dependency</span>></span>
</code></pre> 
<h2><span>核心组件依赖</span></h2> 
<table style="display:table; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">组件</th> 
   <th style="background-color:#f0f0f0; text-align:left">版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Vault</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Bus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Cli</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Zookeeper</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Circuitbreaker</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Commons</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Kubernetes</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Openfeign</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Task</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2.4.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Sleuth</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Contract</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Consul</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Gateway</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Config</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Cloudfoundry</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Starter Build</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2021.0.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Netflix</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.1.0</td> 
  </tr> 
 </tbody> 
</table> 
<h2><span>特性说明</span></h2> 
<h3><span>Spring Cloud Commons</span></h3> 
<p style="color:#595959; margin-left:0; margin-right:0">添加负载均衡器配置属性，支持和 spring cloud gateway 和 openfeign 整合配置</p> 
<h3><span>Spring Cloud Config</span></h3> 
<p style="color:#595959; margin-left:0; margin-right:0">配置中心支持 与 AWS 密钥管理器、AWS 参数存储和 GCP 密钥管理器集成。</p> 
<h3><span>Spring Cloud Gateway</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>redis 路由信息存储支持，扩展动态路由更加简单</p> </li> 
 <li> <p>支持 http2</p> </li> 
 <li> <p>支持 grpc</p> </li> 
</ul> 
<h3><span>Spring Cloud Kubernetes</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>配置服务发现控制器</p> </li> 
</ul> 
<h3><span>Spring Cloud Openfeign</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>支持 Spring Cache @Cachable 注解</p> </li> 
</ul> 
<h3><span>Spring Cloud Sleuth</span></h3> 
<p style="color:#595959; margin-left:0; margin-right:0">提供 Tomcat, Spring Vault, R2DBC, JDBC, Spring Cloud Deployer, Spring Cloud Skipper, Reactor Kafka, Spring TX, Spring Batch, RSocket, Spring Cloud Task, Spring Cloud Config, Kotlin Coroutines 等组件的监控能力.</p> 
<h2><span>特别说明</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>仅支持于 SpringBoot 2.6 整合使用，无法兼容低版本 SpringBoot</p> </li> 
 <li> <p>Spring Cloud Alibaba 2021 无法与之兼容，需要等待 SCA 官方发布新版本适配</p> </li> 
</ul>
                                        </div>
                                      
</div>
            