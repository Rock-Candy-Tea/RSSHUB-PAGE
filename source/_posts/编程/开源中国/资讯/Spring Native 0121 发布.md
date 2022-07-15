
---
title: 'Spring Native 0.12.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7696'
author: 开源中国
comments: false
date: Fri, 15 Jul 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7696'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Native 0.12.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F07%2F13%2Fspring-native-0-12-1-available-now" target="_blank">已发布</a>，这是一个常规更新版本，主要是修复错误、升级依赖，以及增加部分特性。</p> 
<p><strong>新特性</strong></p> 
<ul> 
 <li>为 Sleuth R2dbcTransactionManager 检测工具添加提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1663" target="_blank">#1663</a></li> 
</ul> 
<p><strong>优化兼容性</strong></p> 
<ul> 
 <li>支持 R2DBC PostgreSQL <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1626" target="_blank">#1626</a></li> 
 <li>支持 EntityGraph <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1619" target="_blank">#1619</a></li> 
 <li>为 com.zaxxer.hikari.HikariDataSource 添加 reflection entries <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1599" target="_blank">#1599</a></li> 
</ul> 
<p><strong>升级依赖项</strong></p> 
<ul> 
 <li>Native Build Tools 0.9.13 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1638" target="_blank">#1638</a></li> 
 <li>Spring Boot 2.7.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1637" target="_blank">#1637</a></li> 
</ul> 
<p><strong>Bug Fixes</strong></p> 
<ul> 
 <li>修复无法识别类在构建时初始化的 InitializationHint <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1660" target="_blank">#1660</a></li> 
 <li>修复 (Simple)ClientHttpRequestFactory 中关于 Nativehints 的回归错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1636" target="_blank">#1636</a></li> 
 <li>修复没有在 NativeListener 中设置原生图像系统属性的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1625" target="_blank">#1625</a></li> 
 <li>修复 jdbc-tx 测试在 GraalVM 22.1 中没有生效的问题  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1584" target="_blank">#1584</a></li> 
 <li>修复 AOP 不支持在包含 execution pointcut designator 的 class field 上使用 '*' <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1580" target="_blank">#1580</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.12.1" target="_blank">详情查看 release note</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            