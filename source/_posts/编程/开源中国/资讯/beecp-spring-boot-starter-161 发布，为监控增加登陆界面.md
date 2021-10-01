
---
title: 'beecp-spring-boot-starter-1.6.1 发布，为监控增加登陆界面'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9690'
author: 开源中国
comments: false
date: Thu, 30 Sep 2021 17:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9690'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span> </span>BeeCP-Starter是BeeCP在Springboot上的数据源管理工具：以标签+配置的方式简化数据源管理，并提供监控界面。</p> 
<p><strong>1：版本下载</strong></p> 
<pre><code class="language-xml"><dependency>
   <groupId>com.github.chris2018998</groupId>
   <artifactId>beecp-spring-boot-starter</artifactId>
   <version>1.6.1</version>
</dependency></code></pre> 
<p><strong>2：更新内容</strong></p> 
<p><span style="color:#2980b9"><strong><em> 1：为监控界面增加登陆功能</em></strong></span><br>    spring.datasource.monitorUserId=登陆名<br>    spring.datasource.monitorPassword=登陆口令</p> 
<p><em>   *配置文件增加上述两项后，初次使用则会出现登陆界面*</em></p> 
<p><span style="color:#2980b9"><strong><em> 2：调整监控界面地址</em></strong></span></p> 
<p>   <a href="http://IP:port/项目部署名/beecp">http://IP:port/项目部署名/beecp</a></p> 
<p><span style="color:#2980b9"><strong><em> 3：更改配置项名</em></strong></span></p> 
<p>   dsIds <strong>更改为 </strong>dsId（非多源模式下的单一数据源若不配置此项，默认值为beeDs）</p> 
<p><span style="color:#2980b9"><strong><em> 4：移除部分数据源的支持</em></strong></span></p> 
<p>    移除Druid, Tomcat-Jdbc, HikariCP的支持</p> 
<p><strong>3：项目地址</strong></p> 
<p>  地址1： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChris2018998%2FBeeCP-Starter">https://github.com/Chris2018998/BeeCP</a></p> 
<p>  地址2： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChris2018998%2FBeeCP-Starter">https://github.com/Chris2018998/BeeCP-Starter</a></p>
                                        </div>
                                      
</div>
            