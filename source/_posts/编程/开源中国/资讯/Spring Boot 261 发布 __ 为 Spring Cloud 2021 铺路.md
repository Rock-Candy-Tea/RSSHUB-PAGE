
---
title: 'Spring Boot 2.6.1 发布 __ 为 Spring Cloud 2021 铺路'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://minio.pigx.vip/oss/1638256190.png'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 15:10:00 GMT
thumbnail: 'https://minio.pigx.vip/oss/1638256190.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><span>发布说明</span></h2> 
<p style="color:#595959; margin-left:0; margin-right:0">11 月 29 日 Spring Boot 2.6.1 正式发布，主要是为了支持本周发布的 Spring Cloud 2021.0</p> 
<p style="color:#595959; margin-left:0; margin-right:0"><img alt="1638256190" src="https://minio.pigx.vip/oss/1638256190.png" referrerpolicy="no-referrer"></p> 
<p style="color:#595959; margin-left:0; margin-right:0">此版本包括 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Freleases%2Ftag%2Fv2.6.1" target="_blank">11 个错误修复和文档改进</a>。</p> 
<h2><span>🐞 修复</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>模式分析 PatternParseException 的操作消息中的 matching-strategy 属性的名称不正确<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28839" target="_blank">#28839</a></p> </li> 
 <li> <p>修复 ErrorPageSecurityFilter 部署到 Servlet 3.1 的兼容问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28790" target="_blank">#28790</a></p> </li> 
 <li> <p>QuartzDataSourceScriptDatabaseInitiializer 不提供 MariaDB <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F28779" target="_blank">#28779</a>的映射</p> </li> 
 <li> <p>"test" 和 "Inlined Test Properties" 属性源顺序不正确 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28776" target="_blank">#28776</a></p> </li> 
 <li> <p>在没有 spring-security-web 的 Servlet 应用程序中使用 Spring Security 时出现 ArrayStoreException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28774" target="_blank">#28774</a></p> </li> 
 <li> <p>DefaultClientResources 在将 Lettuce 与 Actuator 一起使用时未正确关闭是发出警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fpull%2F28767" target="_blank">#28767</a></p> </li> 
 <li> <p>具有 permitAll 的页面无法再通过自动配置的 MockMvc <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28759" target="_blank">#28759</a></p> </li> 
 <li> <p>依赖管理 org.elasticsearch.distribution.integ-test-zip:elasticsearch 应将其类型声明为 zip <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28746" target="_blank">#28746</a></p> </li> 
</ul> 
<h2><span>📔 文档</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>修复文档 "External Application Properties" 部分中的拼写错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28834" target="_blank">#28834</a></p> </li> 
 <li> <p>修复参考文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28833" target="_blank">#28833</a> 中 "spring --version" 的输出。</p> </li> 
 <li> <p>org.springframework.boot.actuate.metrics.data  包添加描述 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fissues%2F28761" target="_blank">#28761</a>。</p> </li> 
</ul>
                                        </div>
                                      
</div>
            