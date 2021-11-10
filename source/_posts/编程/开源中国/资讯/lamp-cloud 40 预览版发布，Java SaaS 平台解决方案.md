
---
title: 'lamp-cloud 4.0 预览版发布，Java SaaS 平台解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-efe2e1b81fc35dab6f6bea8082cd6503f57.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 09:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-efe2e1b81fc35dab6f6bea8082cd6503f57.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">4.0 预览版 更新详情:</a></h1> 
<h2>build: 依赖升级</h2> 
<pre><code>spring.boot.version>2.5.6
spring.cloud.version>2020.0.4
spring-boot-admin.version>2.5.3
mybatisplus.version>3.4.3.4
mysql.version>8.0.27
hutool.version>5.7.16</code></pre> 
<h2>feat</h2> 
<ol> 
 <li>4.x 版本命名为 pro</li> 
 <li>authority服务更名为base服务</li> 
 <li>重新设计多租户体系、多应用体系、多部门体系、多员工体系</li> 
 <li>支持切换租户（身份）、切换应用</li> 
 <li>调整租户初始化流程，由租户服务负责创建表结构、表数据，其余服务仅仅链接数据源。</li> 
 <li>全新的菜单、资源配置方案：支持菜单、视图（隐藏菜单）、功能（按钮）、字段、API等类型的资源配置。</li> 
 <li>废弃注解方式控制API权限,新增在资源管理界面配置系统各类权限。</li> 
 <li>去除 非DataSource模式 代码使项目更加简单易懂</li> 
 <li>修改 updateTime 和 createTime 字段为 updatedTime 和 createdTime</li> 
 <li>新增 BaseLogAspect、LampLogAspect 通过AOP打印指定方法入参和出参</li> 
 <li>重构缓存的key，命名规则为：  `[前缀:][租户编码:][服务模块名:]业务类型[:业务字段][:value类型][:业务值]`</li> 
 <li>查询方法的返回值调整为 ResultVO， 不推荐将Entity返回</li> 
 <li>废弃DTO，改为VO。</li> 
 <li>参考阿里规范，新增biz层和manager层，调用顺序为：controller->biz(可选)->service->manager->mapper</li> 
 <li>集成seata1.4.2保证分布式事务有效性</li> 
 <li>重构SuperController、SuperService，新增SuperManager。 SuperService编写单数据源业务逻辑代码；Manager层，聚焦通用小业务（如第三方封装、service能力下沉、缓存、多个Dao组合）</li> 
 <li>新增lamp-scan-start模块，用于扫描服务的在线接口</li> 
 <li>调整token中封装的信息</li> 
 <li>请求头中tenant调整为TenantId， 新增ApplicationId，token调整为Token</li> 
</ol> 
<p>更多功能，等你来体验：    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftangyh.top%2F" target="_blank">https://tangyh.top/</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">《灯灯》中后台快速开发平台</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">lamp 项目组成</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1） 工具集 （ lamp-util 项目必备，其他2个可选）</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>gitee</th> 
   <th>github</th> 
   <th>备注</th> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">工具集</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-util">lamp-util</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-util" target="_blank">lamp-util</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">业务无关的工具集，cloud和boot 项目都依赖它</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">代码生成器</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-util">lamp-generator</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-util" target="_blank">lamp-generator</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">给开发人员使用</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">定时调度器</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-job">lamp-job</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-job" target="_blank">lamp-job</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">尚未开发</td> 
  </tr> 
 </thead> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2） 后端 （下面2个项目功能一致，任选其一即可）</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>gitee</th> 
   <th>github</th> 
   <th>备注</th> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">微服务版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-cloud">lamp-cloud</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">l<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-cloud" target="_blank">amp-cloud</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringCloud 版</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">单体版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-boot">lamp-boot</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-boot" target="_blank">lamp-boot</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringBoot 版(和lamp-cloud功能基本一致)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">示例项目</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-samples" target="_blank">lamp-samples</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-samples" target="_blank">lamp-samples</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">微服务版的示例功能</td> 
  </tr> 
 </thead> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3） 前端 （下面3个项目功能一致，任选其一即可）</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>gitee</th> 
   <th>github</th> 
   <th>备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">租户后台</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-web">lamp-web</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-web" target="_blank">lamp-web</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">基于vue-admin-element开发 （vue2.x）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">租户后台 （强烈推荐！👏👏👏）</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/zuihou111/lamp-web-plus">lamp-web-plus</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-web-plus" target="_blank">lamp-web-plus</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">基于vue-vben-admin开发 （vue3.x）</td> 
  </tr> 
 </tbody> 
</table> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如果你非要说 lamp 是 Linux+Apache+MySQL+PHP，那就算是吧，毕竟 PHP 是世界上最好的语言，我也希望此项目成为世界上最好的后台框架！😈😈😈</p> 
</blockquote> 
<h1 style="margin-left:0; margin-right:0; text-align:left">lamp-cloud 简介</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>lamp-cloud</code><span> </span>基于 jdk11/jdk8 +<span> </span><code>SpringCloud</code><span> </span>+ SpringCloudAlibaba+<span> </span><code>SpringBoot</code><span> </span>的微服务快速开发平台，其中的可配置的 SaaS 功能尤其闪耀， 具备 RBAC 功能、网关统一鉴权、Xss 防跨站攻击、自动代码生成、多种存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">核心技术采用 Spring Cloud Alibaba、SpringBoot、Mybatis、Seata、Sentinel、RabbitMQ、FastDFS/MinIO、SkyWalking 等主要框架和中间件。 希望能努力打造一套从<span> </span><code>JavaWeb基础框架</code><span> </span>-<span> </span><code>分布式微服务架构</code><span> </span>-<span> </span><code>持续集成</code><span> </span>-<span> </span><code>系统监测</code><span> </span>的解决方案。<code>本项目旨在实现基础能力，不涉及具体业务。</code></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">lamp 租户模式介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本项目可以通过配置，轻松切换项目的<span> </span><strong>多租户实现方式</strong>。</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>租户模式</th> 
   <th>描述</th> 
   <th>优点</th> 
   <th>缺点</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">NONE (非租户模式)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">没有租户</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">简单、适合独立系统</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">缺少租户系统的优点</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">COLUMN (字段模式)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">租户共用一个数据库，在业务表中增加字段来区分</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">简单、不复杂、开发无感知</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">数据隔离性差、安全性差、数据备份和恢复困难、</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SCHEMA (独立数据库)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">每个租户独立一个 数据库(schema)，执行 sql 时，动态在表名前增加 schema</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">简单、开发无感知、数据隔离性好</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置文件中必须配置数据库的 root 账号、不支持复杂 sql 和 sql 嵌套自定义函数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">DATASOURCE (独立数据源)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">每个租户独立一个数据源，执行代码时，动态切换数据源</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">可独立部署数据库，数据隔离性好、扩展性高、故障影响小</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">相对复杂、开发需要注意切换数据源时的事务问题、需要较多的数据库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SCHEMA_COLUMN (独立数据库+字段模式)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">每个租户独立一个 数据库，执行代码时，先动态切换数据源，在动态拼接 子租户id进行二次隔离</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">简单、开发无感知、数据隔离性好、支持大租户小门店形式</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置文件中必须配置数据库的 root 账号、不支持复杂 sql 和 sql 嵌套自定义函数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">DATASOURCE_COLUMN (独立数据源+字段模式)</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">每个租户独立一个 数据库(数据源)，执行代码时，动态切换数据源，在动态拼接 子租户id 二次隔离</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">可独立部署数据库，数据隔离性好、扩展性高、故障影响小、支持大租户小门店形式</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">相对复杂、开发需要注意切换数据源时的事务问题、需要较多的数据库</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left"> </h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">lamp-cloud 技术栈/版本介绍：</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>所涉及的相关的技术有： 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>JSON序列化：Jackson</li> 
   <li>消息队列：RabbitMQ</li> 
   <li>缓存：Redis</li> 
   <li>数据库： MySQL 5.7 或者 MySQL 8</li> 
   <li>定时器：采用 xxl-jobs 项目进行二次改造</li> 
   <li>前端：vue + element-ui</li> 
   <li>持久层框架： Mybatis-plus</li> 
   <li>代码生成器：基于 Mybatis-plus-generator 自定义</li> 
   <li>API网关：Gateway/zuul</li> 
   <li>服务注册&发现和配置中心: Nacos</li> 
   <li>服务消费：OpenFeign</li> 
   <li>负载均衡：Ribbon</li> 
   <li>服务熔断：Sentinel</li> 
   <li>项目构建：Maven</li> 
   <li>分布式事务： seata</li> 
   <li>分布式系统的流量防卫兵： Sentinel</li> 
   <li>监控： spring-boot-admin</li> 
   <li>链路调用跟踪： zipkin/SkyWalking</li> 
   <li>文件服务器：FastDFS 5.0.5 / 阿里云OSS / 本地存储/MinIO</li> 
   <li>Nginx</li> 
  </ul> </li> 
 <li>部署方面： 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>服务器：CentOS</li> 
   <li>Jenkins</li> 
   <li>Docker</li> 
   <li>Kubernetes</li> 
  </ul> </li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">项目截图：</h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>预览</th> 
   <th>预览</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt src="https://oscimg.oschina.net/oscnet/up-efe2e1b81fc35dab6f6bea8082cd6503f57.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/99e21a50fe4cd8e644bc2a2c693b9b86.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/315afa0201968de0b20c1af42fb981c5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cdb488d0ed1c35613025613df6a36f96.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/c8d8936b144fe568ef394289ddbf0268.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/4d3c5d0ab011266821fe02482db33c38.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/58ae227c8b3e98129091dc86efb219c8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/7e34b4c35c24445f72898c95fb2d6347.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/2f1bcc485ca1ff3ee22995b6b276cc6f.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cbcafbcff1e2404f2fb466ab257de6de.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/45111269e0acd9173e480e31505b04f3.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/67e0575c0c9acb0e787e17194e5fba0d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            