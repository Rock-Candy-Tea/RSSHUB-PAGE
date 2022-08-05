
---
title: 'novel v3.3.0 发布，Spring Boot 3 + Vue 3 学习型项目'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://s3.ax1x.com/2020/12/27/r5400A.png'
author: 开源中国
comments: false
date: Fri, 05 Aug 2022 08:19:00 GMT
thumbnail: 'https://s3.ax1x.com/2020/12/27/r5400A.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">novel v3.3.0 发布，主要改变如下：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong>[架构]</strong></span><span style="color:#222222"> </span><span>集成</span> Spring Boot Admin<span>，实现应用管理和监控功能</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong>[架构]</strong></span><span style="color:#222222"> </span><span>集成</span> Springdoc <span>自动生成</span> Swagger <span>接口文档</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#222222"><strong style="color:#ce7f2d">[架构]</strong> </span><span>集成</span> Redisson + Spring AOP <span>实现分布式锁</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span style="color:#ce7f2d"><strong>[优化]</strong></span><span style="color:#222222"> </span>使用</span> Java <span>和</span> Spring Boot <span>的新特性重构部分功能</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong><strong style="color:#ce7f2d">[优化]</strong></strong></span><span style="color:#222222"> </span><span>遵循</span> Google Java Style Guide <span>和阿里巴巴规范格式化代码</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong><strong style="color:#ce7f2d">[优化]</strong></strong></span><span style="color:#222222"> </span>优化数据库脚本管理</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong>[文档] </strong></span><span>更新文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.xxyopen.com%2Fcourse%2Fnovel%2F6.html" target="_blank">项目部署</a></span><span>部分</span></p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">演示站点</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F47.106.243.172%3A8888%2F" target="_blank">点击前往</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify">项目介绍</h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">novel 是一套基于时下最新 Java 技术栈 Spring Boot 3 + Vue 3 开发的前后端分离学习型小说项目，配备详细的项目开发文档手把手教你从零开始开发上线一个生产级别的 Java 系统。由小说门户系统、作家后台管理系统、平台后台管理系统等多个子系统构成。包括小说推荐、作品检索、小说排行榜、小说阅读、小说评论、会员中心、作家专区、充值订阅、新闻发布等功能。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">开发环境</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>MySQL 8.0</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Redis 7.0</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Elasticsearch 8.2.0（可选）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>RabbitMQ 3.10.2（可选）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>XXL-JOB 2.3.1（可选）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>JDK 17</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Maven 3.8</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>IntelliJ IDEA 2021.3（可选）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Node 16.14</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong>注：Elasticsearch、RabbitMQ 和 XXL-JOB 默认关闭，可通过 application.yml 配置文件中相应的</strong><strong><code>enable</code><span> </span>配置属性开启。</strong></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">后端技术选型</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>技术</th> 
   <th>版本</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Boot</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.0.0-SNAPSHOT</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">容器 + MVC 框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">MyBatis</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.5.9</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">ORM 框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">MyBatis-Plus</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.5.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">MyBatis 增强工具</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">JJWT</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.11.5</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">JWT 登录支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Lombok</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.18.24</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">简化对象封装工具</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Caffeine</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.1.0</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">本地缓存支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Redis</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">7.0</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">分布式缓存支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Redisson</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.17.4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">分布式锁实现</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">MySQL</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">8.0</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">数据库服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">ShardingSphere-JDBC</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">5.1.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">数据库分库分表支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Elasticsearch</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">8.2.0</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">搜索引擎服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">RabbitMQ</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.10.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">开源消息中间件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">XXL-JOB</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.3.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">分布式任务调度平台</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Sentinel</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.8.4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">流量控制组件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Springdoc-openapi</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.0.0-M4-SNAPSHOT</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Swagger 3 接口文档自动生成</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Boot Admin</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.0.0-M1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">应用管理和监控</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Undertow</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.2.17.Final</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Java 开发的高性能 Web 服务器</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Sonarqube</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">代码质量控制</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>注：更多热门新技术待集成。</strong></p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">前端技术选型</h2> 
<table cellspacing="0" style="--darkreader-inline-color:#d3cfc9; --darkreader-inline-outline:currentcolor; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box !important; caret-color:#222222; color:#222222; display:table; font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:normal; letter-spacing:0.544px; line-height:27px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:currentcolor none 0px; overflow-wrap:break-word !important; overflow:auto; padding:0px; text-align:justify; text-decoration:none; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:677px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th style="text-align:center">技术</th> 
   <th style="text-align:center">版本</th> 
   <th style="text-align:center">说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">Vue.js</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">3.2.13</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">渐进式 JavaScript 框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">Vue Router</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">4.0.15</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">Vue.js 的官方路由</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">axios</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">0.27.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">基于 promise 的网络请求库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">element-plus</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">2.2.0</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:center">基于 Vue 3，面向设计师和开发者的组件库</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">部分截图</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>首页</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="img" src="https://s3.ax1x.com/2020/12/27/r5400A.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2. 分类索引页</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-d0b2e03129bfae47b8bb96a491b73d383c5.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3. 排行榜</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-78d5a68586cd92a86c669311f414508f922.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4. 详情页</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-8be2495a2869f93626b0c9c1df6f329747a.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">5. 阅读页</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-517c84148d2db8e11717a8bbecc57fa1be7.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">代码仓库</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F201206030%2Fnovel" target="_blank">https://github.com/201206030/novel</a></p>
                                        </div>
                                      
</div>
            