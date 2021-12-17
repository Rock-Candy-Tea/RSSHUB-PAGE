
---
title: 'Spring Cloud 2020.0.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=612'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 02:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=612'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0">Spring Cloud 2020.0.5 正式发布，这是错误修正版本。兼容 Spring Boot 2.4.x and 2.5.x, 不支持 2.6.x (请使用 Spring Cloud 2021)</p> 
<p style="color:#333333; margin-left:0; margin-right:0">目前已经可以从中央仓库获取，坐标如下：</p> 
<pre style="margin-left:0; margin-right:0"><code><span style="color:#000080"><<span style="color:#000080">dependencyManagement</span>></span>
    <span style="color:#000080"><<span style="color:#000080">dependencies</span>></span>
        <span style="color:#000080"><<span style="color:#000080">dependency</span>></span>
            <span style="color:#000080"><<span style="color:#000080">groupId</span>></span>org.springframework.cloud<span style="color:#000080"></<span style="color:#000080">groupId</span>></span>
            <span style="color:#000080"><<span style="color:#000080">artifactId</span>></span>spring-cloud-dependencies<span style="color:#000080"></<span style="color:#000080">artifactId</span>></span>
            <span style="color:#000080"><<span style="color:#000080">version</span>></span>2020.0.5<span style="color:#000080"></<span style="color:#000080">version</span>></span>
            <span style="color:#000080"><<span style="color:#000080">type</span>></span>pom<span style="color:#000080"></<span style="color:#000080">type</span>></span>
            <span style="color:#000080"><<span style="color:#000080">scope</span>></span>import<span style="color:#000080"></<span style="color:#000080">scope</span>></span>
        <span style="color:#000080"></<span style="color:#000080">dependency</span>></span>
    <span style="color:#000080"></<span style="color:#000080">dependencies</span>></span>
<span style="color:#000080"></<span style="color:#000080">dependencyManagement</span>></span>
<span style="color:#000080"><<span style="color:#000080">dependencies</span>></span>
    <span style="color:#000080"><<span style="color:#000080">dependency</span>></span>
        <span style="color:#000080"><<span style="color:#000080">groupId</span>></span>org.springframework.cloud<span style="color:#000080"></<span style="color:#000080">groupId</span>></span>
        <span style="color:#000080"><<span style="color:#000080">artifactId</span>></span>spring-cloud-starter-config<span style="color:#000080"></<span style="color:#000080">artifactId</span>></span>
    <span style="color:#000080"></<span style="color:#000080">dependency</span>></span>
    <span style="color:#000080"><<span style="color:#000080">dependency</span>></span>
        <span style="color:#000080"><<span style="color:#000080">groupId</span>></span>org.springframework.cloud<span style="color:#000080"></<span style="color:#000080">groupId</span>></span>
        <span style="color:#000080"><<span style="color:#000080">artifactId</span>></span>spring-cloud-starter-netflix-eureka-client<span style="color:#000080"></<span style="color:#000080">artifactId</span>></span>
    <span style="color:#000080"></<span style="color:#000080">dependency</span>></span>
    ...
<span style="color:#000080"></<span style="color:#000080">dependencies</span>></span>
</code></pre> 
<h2 style="margin-left:0; margin-right:0"><span>更新日志</span></h2> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Netflix</span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0">更新至 Netflix/Eureka to 1.10.17</p> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Config</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">Git 存储配置文件支持 https 代理</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">新增 AWS 、 Redis 、CredHub 的存储支持 Support ordering AWS, Redis, and CredHub Repositories (1980)</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Gateway</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>新增监控指标: netty 连接数，路径标签、路由定义的数量</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Kubernetes</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>Kubernetes API Client 可以设置代理</p> </li> 
 <li> <p>允许不设置 activeProfile 参数</p> </li> 
 <li> <p>升级 Kubernetes Java Client 11.0.3</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Openfeign</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>PageJacksonModule 序列化模块 支持 size = 0 的分页设置</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Sleuth</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>新增缓存执行器包装器</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span>Spring Cloud Vault</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">token 支持从 <code>~/.vault_token</code> 获取</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">新增 <code>spring.cloud.vault.reactive.enabled</code> 属性</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">支持多个数据库密钥的生成</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><span>组件版本</span></h2> 
<table style="display:table; line-height:1.6 !important; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">组件</th> 
   <th style="background-color:#f0f0f0; text-align:left">版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Netflix</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Config</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.6</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Sleuth</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Gateway</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.6</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Cloudfoundry</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Contract</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Kubernetes</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Zookeeper</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Cli</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.4</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Task</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2.3.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Starter Build</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">2020.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Openfeign</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.6</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Vault</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.5</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Cloud Commons</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">3.0.5</td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            