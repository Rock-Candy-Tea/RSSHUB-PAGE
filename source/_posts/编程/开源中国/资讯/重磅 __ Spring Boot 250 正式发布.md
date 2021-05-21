
---
title: '重磅 __ Spring Boot 2.5.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://minio.pigx.vip/oss/1621559309.png'
author: 开源中国
comments: false
date: Fri, 21 May 2021 03:41:00 GMT
thumbnail: 'https://minio.pigx.vip/oss/1621559309.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://minio.pigx.vip/oss/1621559309.png" referrerpolicy="no-referrer"></p> 
<p>spring boot 2.5.0、2.4.6、2.3.11 正式发布。</p> 
<pre><code><parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-parent</artifactId>
  <version><span style="color:#1c00cf">2.5</span><span style="color:#1c00cf">.0</span></version>
</parent>
</code></pre> 
<h2>新特性</h2> 
<ul> 
 <li> <p>支持 Java16</p> </li> 
 <li> <p>支持 Gradle7</p> </li> 
 <li> <p>增强 Docker 镜像构建工具</p> </li> 
 <li> <p>全新的数据源加载机制</p> </li> 
</ul> 
<p>spring boot 2.5 的详细新特性说明可以参考 本公众号（JAVA 架构日记）之前推文。</p> 
<h2>暗黑模式</h2> 
<p><img alt src="https://minio.pigx.vip/oss/1621559685.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p>外观新颖，字体更清晰。</p> </li> 
 <li> <p>上下方向箭头展开/折叠示例代码以显示导入和详细信息。</p> </li> 
 <li> <p>代码片段剪贴板按钮</p> </li> 
 <li> <p>文档支持暗黑模式</p> </li> 
</ul> 
<p><img alt src="https://minio.pigx.vip/oss/1621559796.png" referrerpolicy="no-referrer"></p> 
<h2>重要变更说明</h2> 
<ul> 
 <li>数据源相关变更 
  <ul> 
   <li> <p><code>spring.datasource.*</code> 已被 <code>spring.sql.init.*</code> 属性替代。</p> </li> 
   <li> <p>Flyway 和 Liquibase 需要指定单独的 username / password,不再从 datasource 继承。</p> </li> 
  </ul> </li> 
 <li>不再维护 spring data solr , 从此版本开始 已经开始从源码中移除。</li> 
 <li>断点 /info 不再通过 web 暴露，如果类中包含 spring security，需要安全验证。</li> 
 <li>EL 语法实现由 tomcat-embed-el 替代为 jakrta-el。</li> 
 <li>Error View 异常页面中不会包含 具体的错误信息，如果需要则可以通过 <code>server.error.include-message</code>开启。</li> 
 <li>通过 <code>logging.register-shutdown-hook</code> 属性可以在 jvm 退出时释放日志资源。</li> 
</ul>
                                        </div>
                                      
</div>
            