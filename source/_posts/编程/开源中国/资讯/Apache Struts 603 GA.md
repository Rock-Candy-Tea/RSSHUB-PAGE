
---
title: 'Apache Struts 6.0.3 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6696'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6696'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#17233b">Apache Struts 小组<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstruts.apache.org%2Fannounce-2022%23a20220915" target="_blank">宣布</a>，Apache Struts 6.0.3 版现已作为“General Availability”版本提供。具体更新内容包括：</span></p> 
<ul> 
 <li>将 async 和速度插件添加到 bom <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F568" target="_blank">#568</a></li> 
 <li>[WW-5191] 修复了 <s:textarea/> 标签中 maxLength 和 minLength 属性的位置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F572" target="_blank">#572</a></li> 
 <li>[WW-5185] 重新引入 Tiles 资源的正确实现，以支持 Tiles definitions 的通配符匹配 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F566" target="_blank">#566</a></li> 
 <li>[WW-5188] 从 2.6 开始替换为 6.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F569" target="_blank">#569</a></li> 
 <li>WW-5197 添加对 java.sql.Date 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F574" target="_blank">#574</a></li> 
 <li>[WW-5201] 将 log4j2 升级到版本 2.18.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F575" target="_blank">#575</a></li> 
 <li>[WW-5193] 使用正确的 org.hibernate.validator groupId 并升级到版本 6.1.3.Final <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F576" target="_blank">#576</a></li> 
 <li>WW-5202 将 jasperreports 更新到 6.19.1 并从 jasperreports 中排除可选的 itext <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F578" target="_blank">#578</a></li> 
 <li>[WW-5190] 修复调度请求时的 StackOverflowException <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F571" target="_blank">#571</a></li> 
 <li>[WW-5192] 修复了与枚举一起使用时损坏的 radio tag <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F577" target="_blank">#577</a></li> 
 <li>[WW-5204] 将 OGNL 升级到版本 3.3.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F579" target="_blank">#579</a></li> 
 <li>将 maven wrapper 更新到 3.8.6 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F582" target="_blank">#582</a></li> 
 <li>WW-5208 将 hibernate-validator 更新到 6.2.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F583" target="_blank">#583</a></li> 
 <li>[WW-5205] - 恢复内部 bean 的注入重构 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F580" target="_blank">#580</a></li> 
 <li>添加 openjdk17 以构建，删除 oraclejdk9 (EOL) 并从 oraclejdk 切换到 openjdk 以修复 Travis CI 构建 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F584" target="_blank">#584</a></li> 
 <li>将 maven-surefire-plugin 更新为 3.0.0-M7 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F587" target="_blank">#587</a></li> 
 <li>[WW-5207] 默认使用 ASM 9 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F586" target="_blank">#586</a></li> 
 <li>[WW-5203] 在每次调用时重新构建策略字符串 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F588" target="_blank">#588</a></li> 
 <li>[WW-5173] - 尝试修复自定义缓存工厂的 DI 行为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F573" target="_blank">#573</a></li> 
 <li>将 maven-enforcer-plugin 更新为 3.1.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F591" target="_blank">#591</a></li> 
 <li>[WW-5215] 在应用 CSP 设置之前检查是否已创建会话 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F590" target="_blank">#590</a></li> 
 <li>[WW-5212] 升级到 Spring 5.3.22 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F592" target="_blank">#592</a></li> 
 <li>[WW-5218] 允许禁用与 CSP 相关的拦截器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Fpull%2F593" target="_blank">#593</a></li> 
</ul> 
<p>详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fstruts%2Freleases%2Ftag%2FSTRUTS_6_0_3" target="_blank">https://github.com/apache/struts/releases/tag/STRUTS_6_0_3</a></p>
                                        </div>
                                      
</div>
            