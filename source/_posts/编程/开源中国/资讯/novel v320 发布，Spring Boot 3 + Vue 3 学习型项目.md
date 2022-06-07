
---
title: 'novel v3.2.0 发布，Spring Boot 3 + Vue 3 学习型项目'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://s3.ax1x.com/2020/12/27/r5400A.png'
author: 开源中国
comments: false
date: Tue, 07 Jun 2022 00:13:00 GMT
thumbnail: 'https://s3.ax1x.com/2020/12/27/r5400A.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff">novel v3.2.0 发布，主要改变如下：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong>[架构]</strong></span><span style="color:#222222"> 集成分布式任务调度 XXL-JOB， 优化 Elasticsearch 数据同步任务。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong>[架构]</strong></span><span style="color:#222222"> 集成 Sentinel 实现接口防刷和限流。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#222222"><strong style="color:#ce7f2d">[架构]</strong> 集成 ShardingSphere-JDBC，优化小说内容存储。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span style="color:#ce7f2d"><strong>[功能]</strong></span><span style="color:#222222"> </span></span><span style="color:#222222">新增作家专区作家注册功能。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong><strong style="color:#ce7f2d">[功能]</strong></strong></span><span style="color:#222222"> 新增作家专区小说发布功能。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong><strong style="color:#ce7f2d">[功能]</strong></strong></span><span style="color:#222222"> 新增作家专区章节发布功能。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#ce7f2d"><strong>[BUG] </strong></span><span style="color:#222222">同类推荐过滤无章节小说。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#222222"><strong style="color:#ce7f2d">[BUG]</strong> 修复小说详情页封面错误图显示。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#222222"><strong style="color:#ce7f2d">[优化]</strong> 部分页面样式优化。</span></p> </li> 
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
<p style="margin-left:0; margin-right:0"><span><strong>注：Elasticsearch、RabbitMQ 和 XXL-JOB 默认关闭，可通过 application.yml 配置文件中相应的</strong><strong><code>enable</code>配置属性开启。</strong></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify">后端技术选型</h2> 
<table cellspacing="0" style="-webkit-text-size-adjust:auto; -webkit-text-stroke-width:0px; border-collapse:collapse; box-sizing:border-box !important; caret-color:#222222; color:#222222; display:table; font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-weight:normal; letter-spacing:0.5440000295639038px; line-height:27px; margin:0px 0px 10px; max-width:100%; orphans:auto; outline:0px; padding:0px; text-align:justify; text-decoration:none; text-indent:0px; text-transform:none; white-space:normal; widows:auto; width:677px; word-spacing:0px; word-wrap:break-word !important"> 
 <thead> 
  <tr> 
   <th style="background-color:#f7f7f7; text-align:left">技术</th> 
   <th style="background-color:#f7f7f7; text-align:center">版本</th> 
   <th style="background-color:#f7f7f7; text-align:-webkit-match-parent">说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring Boot</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">3.0.0-SNAPSHOT</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">容器 + MVC 框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">MyBatis</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">3.5.9</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">ORM 框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">MyBatis-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">3.5.1</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">MyBatis 增强工具</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">JJWT</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">0.11.5</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">JWT 登录支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Lombok</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">1.18.24</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">简化对象封装工具</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Caffeine</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">3.1.0</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">本地缓存支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redis</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">7.0</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">分布式缓存支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">MySQL</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">8.0</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">数据库服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">ShardingSphere-JDBC</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">5.1.1</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">数据库分库分表支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Elasticsearch</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">8.2.0</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">搜索引擎服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RabbitMQ</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">3.10.2</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">开源消息中间件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">XXL-JOB</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">2.3.1</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">分布式任务调度平台</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Sentinel</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">1.8.4</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">流量控制组件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Undertow</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">2.2.17.Final</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">Java 开发的高性能 Web 服务器</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Docker</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">-</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">应用容器引擎</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Jenkins</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">-</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">自动化部署工具</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Sonarqube</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:center">-</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px">代码质量控制</td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0px; margin-right:0px; text-align:justify"><strong>注：更多热门新技术待集成。</strong></p> 
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
            