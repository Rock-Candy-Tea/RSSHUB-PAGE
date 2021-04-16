
---
title: 'Spring Boot 2.4.5 & 2.3.10 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4112'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 06:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4112'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Boot 2.4.5 & 2.3.10 现已发布。本次更新是错误修复版本，分别包含 57 个与 78 个错误修复。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.4.5" target="_blank">2.4.5</a> 
  <ul> 
   <li>当 spring.main.cloud-platform 被设置为NONE时，CloudPlatform.isActive 可以返回 true</li> 
   <li>Elasticsearch 自动配置没有配置默认的转换器</li> 
   <li>Gradle bootBuildImage 不会保留资源的文件权限</li> 
   <li>Keystore.load 调用不会关闭 InputStream</li> 
   <li>带有 Reactory Netty 的 TCP 的密码配置被忽略</li> 
   <li>修复使用 Cassandra 关闭 Spring Boot 应用程序时出现 java.util.concurrent.RejectedExecutionException 的问题</li> 
   <li>修复 spring-boot:build-image 在配置中指定分类器时挂起的问题</li> 
   <li>修复 AbstractWebMvcEndpointHandlerMapping 不链接 InvalidEndpointRequestExceptions 的问题</li> 
   <li>修复当 JVM 退出时，未打包的 jar 不会被删除的问题</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F04%2F15%2Fspring-boot-2-3-10-is-now-available" target="_blank">2.3.10</a> 
  <ul> 
   <li>修复使用上下文层次结构运行时，PrimaryDefaultValidatorPostProcessor 引起 NoSuchBeanDefinitionException 的问题</li> 
   <li>修复 TldPatterns 与 Tomcat 不对齐的问题</li> 
   <li>修复 http.client.requests 的 URI 标签忽略 REST 模板的根 URI的问题</li> 
   <li>修复当配置了多个架构或数据脚本位置并且在某个位置找不到任何资源时，用户无法确定哪个位置有故障的问题</li> 
   <li>EmbeddedDatabaseConnection＃h2 不应指定主机名</li> 
   <li>修复 spring-web 不存在时，RSocket 的 EmbeddedServerAutoConfiguration 不会关闭的问题</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            