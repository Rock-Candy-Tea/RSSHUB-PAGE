
---
title: 'Spring Boot 2.5.1 && Spring 2.4.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://minio.pigx.vip/oss/1623374636.png'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 10:33:00 GMT
thumbnail: 'https://minio.pigx.vip/oss/1623374636.png'
---

<div>   
<div class="content">
                                                                    
                                                        <hr> 
<p>Spring Boot 2.5.1 、2.4.7 已经发布。现在可从 repo.spring.io 和 Maven Central 获得。</p> 
<pre><code><span style="color:#aa0d91"><<span style="color:#aa0d91">parent</span>></span>
  <span style="color:#aa0d91"><<span style="color:#aa0d91">groupId</span>></span>org.springframework.boot<span style="color:#aa0d91"></<span style="color:#aa0d91">groupId</span>></span>
  <span style="color:#aa0d91"><<span style="color:#aa0d91">artifactId</span>></span>spring-boot-starter-parent<span style="color:#aa0d91"></<span style="color:#aa0d91">artifactId</span>></span>
  <span style="color:#aa0d91"><<span style="color:#aa0d91">version</span>></span>2.5.1<span style="color:#aa0d91"></<span style="color:#aa0d91">version</span>></span>
  <span style="color:#aa0d91"><<span style="color:#aa0d91">relativePath</span>/></span>
<span style="color:#aa0d91"></<span style="color:#aa0d91">parent</span>></span>
</code></pre> 
<p>这是一个提前发布的 <strong>BUG FIX 版本</strong>，由于官方在 发布 SpringBoot 2.5.0 后收到大量的 BUG 反馈。 <strong>如果你还没有开始使用 spring boot 2.5.0， 请直接使用 2.5.1 向下兼容。</strong></p> 
<p><img alt="官方声明" src="https://minio.pigx.vip/oss/1623374636.png" referrerpolicy="no-referrer"></p> 
<p>官方声明</p> 
<h2>🐞 Bug Fixes</h2> 
<ul> 
 <li> <p>升级 2.5.0 会导致 Jackson 发出关于 Kotlin 的启动警告</p> </li> 
 <li> <p>在 JDK11 环境下 开启 SecurityManager 无法运行</p> </li> 
 <li> <p>RandomValuePropertySource 存在分母为零的问题</p> </li> 
 <li> <p>目录配置存在两个'.'时，新的配置文件加载机制失效，导致无序</p> </li> 
 <li> <p>RestTemplateBuilder 无法同时配置 MetricsRestTemplateCustomizer 和 LocalHostUriTemplateHandler 属性</p> </li> 
 <li> <p>当镜像名包含特殊字符时，新的镜像构建器无法快速失败，会一直保持运行</p> </li> 
 <li> <p>spring data 的部分端点指标丢失</p> </li> 
 <li> <p>无法设置 H2 的 driverClassName ，抛出 UnsupportedDataSourcePropertyException</p> </li> 
 <li> <p>无法设置 SQL Server 的 jdbc-url ，抛出 UnsupportedDataSourcePropertyException</p> </li> 
 <li> <p>Flyway 和 Liquibase 自定义数据源没有 url 导致 java.lang.ClassCastException</p> </li> 
 <li> <p>DataSourceInitializationConfiguration 自定义用户名/密码属性无效</p> </li> 
 <li> <p>spring.datasource.password 的空值会导致 NullPointerException</p> </li> 
</ul> 
<h2>详情</h2> 
<p>其他 BUG 修复、文档更新和依赖项升级，详情查看：</p> 
<ul> 
 <li> <p>https://spring.io/blog/2021/06/10/spring-boot-2-5-1-is-now-available</p> </li> 
 <li> <p>https://github.com/spring-projects/spring-boot/releases/tag/v2.5.1</p> </li> 
</ul>
                                        </div>
                                      
</div>
            