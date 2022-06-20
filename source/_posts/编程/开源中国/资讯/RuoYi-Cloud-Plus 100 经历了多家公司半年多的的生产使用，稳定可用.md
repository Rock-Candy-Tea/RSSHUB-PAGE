
---
title: 'RuoYi-Cloud-Plus 1.0.0 经历了多家公司半年多的的生产使用，稳定可用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0520/152809_0edbfaf1_1766278.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 10:16:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0520/152809_0edbfaf1_1766278.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>升级说明</h1> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">新增/优化 工程模块</h3> 
<ul> 
 <li>add 新增 ruoyi-common-alibaba-bom 工程管理 alibaba 相关依赖</li> 
 <li>add 新增 ruoyi-common-bom 工程管理 ruoyi-common 相关依赖</li> 
 <li>add 新增 ruoyi-api-bom 工程管理 ruoyi-api 依赖项</li> 
 <li>add 新增 ruoyi-api-resource 模块 规范用法 移除 ruoyi-file 模块</li> 
 <li>add 新增 ruoyi-common-web 模块 使用 undertow 替换 tomcat</li> 
 <li>add 新增 ruoyi-common-dubbo 整合 dubbo 3.X 实现高性能 rpc 远程调用 替换 feign</li> 
 <li>add 新增 ruoyi-common-dict 实现字典多服务调用</li> 
 <li>add 新增 ruoyi-common-loadbalancer 自定义负载均衡模块 用于多团队开发</li> 
 <li>add 新增 ruoyi-common-excel 模块 集成 Alibaba EasyExcel 替换 自带excel实现</li> 
 <li>add 新增 ruoyi-common-oss 模块 支持 AWS S3 协议 分布式文件存储</li> 
 <li>add 新增 ruoyi-common-mail 邮件模块</li> 
 <li>add 新增 ruoyi-common-sms 短信模块 整合 阿里云、腾讯云 短信功能</li> 
 <li>add 新增 ruoyi-common-idempotent 分布式幂等模块</li> 
 <li>add 新增 ruoyi-common-satoken 整合 sa-token 重写所有权限</li> 
 <li>add 新增 ruoyi-xxl-job-admin 整合 xxljob 替换 quartz 支持分布式任务调度</li> 
 <li>add 新增 ruoyi-job 模块 统一远程处理任务 规范用法</li> 
 <li>add 新增 ruoyi-doc 模块 集成 Knife4j 替换 swagger</li> 
 <li>add 新增 ruoyi-seata-server 源码集成 Seata 1.5.X 服务端</li> 
 <li>add 新增 ruoyi-sentinel-dashboard 模块 源码集成 sentinel 控制台</li> 
 <li>update 抽取所有公用配置到 maven profile 管理</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">代码依赖改动</h3> 
<ul> 
 <li>update SpringCloud 2021.0.3</li> 
 <li>update 适配 SpringCloudAlibaba 2021.0.1.0 全新配置方式</li> 
 <li>update poi 4.1.2 => 5.2.2 性能大幅提升</li> 
 <li>update 重构 整合 jackson 替换 fastjson</li> 
 <li>update 重构 整合 redisson 客户端</li> 
 <li>update 重构 整合 mybatis-plus</li> 
 <li>update 重写 数据权限实现 基于 mybatis-plus</li> 
 <li>add 增加 lombok 优化原生代码</li> 
 <li>add 整合 hutool 优化相关代码</li> 
 <li>add 新增 国际化 功能</li> 
 <li>add 新增 lock4j 分布式锁</li> 
 <li>add 增加监控中心 在线日志监控 优化日志文件格式</li> 
 <li>add 适配 docker 部署方式</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后续/进行中计划</h3> 
<ul> 
 <li>增加 Vue3 前端工程</li> 
 <li>应用模块 适配 Oracle、PostgreSQL、SQLServer</li> 
 <li>增加 SpringCloud Stream 支持</li> 
 <li>适配 Apache Kafka、Apache RocketMQ、RabbitMQ</li> 
 <li>适配 ElasticSearch 分布式搜索引擎</li> 
 <li>适配 Alibaba Canal 分布式数据同步中心</li> 
 <li>适配 Apache SkyWalking 分布式链路追踪监控中心</li> 
 <li>适配 ELK 分布式日志中心</li> 
 <li>适配 Prometheus、Grafana 分布式全方位数据大屏监控</li> 
</ul> 
<h1>平台简介</h1> 
<p>RuoYi-Cloud-Plus 是一个微服务通用权限管理系统，重写 RuoYi-Cloud 并进行全方位升级(不兼容原框架)。</p> 
<table> 
 <thead> 
  <tr> 
   <th>功能介绍</th> 
   <th>使用技术</th> 
   <th>文档地址</th> 
   <th>特性注意事项</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>微服务权限管理系统</td> 
   <td>RuoYi-Cloud-Plus</td> 
   <td><a href="https://gitee.com/JavaLionLi/RuoYi-Cloud-Plus">RuoYi-Cloud-Plus官网</a></td> 
   <td>重写 RuoYi-Cloud 全方位升级(不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td>分布式集群分支</td> 
   <td>RuoYi-Vue-Plus</td> 
   <td><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus">RuoYi-Vue-Plus官网</a></td> 
   <td>重写 RuoYi-Vue (不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td>前端开发框架</td> 
   <td>Vue、Element UI</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN" target="_blank">Element UI官网</a></td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>后端开发框架</td> 
   <td>SpringBoot</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot%2F%23learn" target="_blank">SpringBoot官网</a></td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>微服务开发框架</td> 
   <td>SpringCloud</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud" target="_blank">SpringCloud官网</a></td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>微服务开发框架</td> 
   <td>SpringCloudAlibaba</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud-alibaba" target="_blank">SpringCloudAlibaba官网</a></td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>容器框架</td> 
   <td>Undertow</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fundertow.io%2F" target="_blank">Undertow官网</a></td> 
   <td>基于 XNIO 的高性能容器</td> 
  </tr> 
  <tr> 
   <td>权限认证框架</td> 
   <td>Sa-Token、Jwt</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsa-token.dev33.cn%2F" target="_blank">Sa-Token官网</a></td> 
   <td>强解耦、强扩展</td> 
  </tr> 
  <tr> 
   <td>关系数据库</td> 
   <td>MySQL</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.mysql.com%2F" target="_blank">MySQL官网</a></td> 
   <td>适配 8.X 最低 5.7</td> 
  </tr> 
  <tr> 
   <td>关系数据库</td> 
   <td>Oracle</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.oracle.com%2Fcn%2Fdatabase%2F" target="_blank">Oracle官网</a></td> 
   <td>适配 12c</td> 
  </tr> 
  <tr> 
   <td>关系数据库</td> 
   <td>PostgreSQL</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2F" target="_blank">PostgreSQL官网</a></td> 
   <td>适配 14</td> 
  </tr> 
  <tr> 
   <td>关系数据库</td> 
   <td>SQLServer</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fsql%2Fsql-server" target="_blank">SQLServer官网</a></td> 
   <td>适配 2019</td> 
  </tr> 
  <tr> 
   <td>缓存数据库</td> 
   <td>Redis</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2F" target="_blank">Redis官网</a></td> 
   <td>适配 6.X 最低 5.X</td> 
  </tr> 
  <tr> 
   <td>分布式注册中心</td> 
   <td>Alibaba Nacos</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2Fquick-start.html" target="_blank">Alibaba Nacos文档</a></td> 
   <td>采用2.X 基于GRPC通信高性能</td> 
  </tr> 
  <tr> 
   <td>分布式配置中心</td> 
   <td>Alibaba Nacos</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2Fquick-start.html" target="_blank">Alibaba Nacos文档</a></td> 
   <td>采用2.X 基于GRPC通信高性能</td> 
  </tr> 
  <tr> 
   <td>服务网关</td> 
   <td>SpringCloud Gateway</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud-gateway" target="_blank">SpringCloud Gateway文档</a></td> 
   <td>响应式高性能网关</td> 
  </tr> 
  <tr> 
   <td>负载均衡</td> 
   <td>SpringCloud Loadbalancer</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fguides%2Fgs%2Fspring-cloud-loadbalancer%2F" target="_blank">SpringCloud Loadbalancer文档</a></td> 
   <td>负载均衡处理</td> 
  </tr> 
  <tr> 
   <td>RPC远程调用</td> 
   <td>Apache Dubbo</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdubbo.apache.org%2Fzh%2F" target="_blank">Apache Dubbo官网</a></td> 
   <td>原生态使用体验、高性能</td> 
  </tr> 
  <tr> 
   <td>分布式限流熔断</td> 
   <td>Alibaba Sentinel</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsentinelguard.io%2Fzh-cn%2F" target="_blank">Alibaba Sentinel文档</a></td> 
   <td>无侵入、高扩展</td> 
  </tr> 
  <tr> 
   <td>分布式事务</td> 
   <td>Alibaba Seata</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseata.io%2Fzh-cn%2F" target="_blank">Alibaba Seata文档</a></td> 
   <td>无侵入、高扩展 支持 四种模式</td> 
  </tr> 
  <tr> 
   <td>分布式消息队列</td> 
   <td>SpringCloud Stream</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud-stream" target="_blank">SpringCloud Stream文档</a></td> 
   <td>门面框架兼容各种MQ集成</td> 
  </tr> 
  <tr> 
   <td>分布式消息队列</td> 
   <td>Apache Kafka</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkafka.apache.org%2F" target="_blank">Apache Kafka文档</a></td> 
   <td>高性能高速度</td> 
  </tr> 
  <tr> 
   <td>分布式消息队列</td> 
   <td>Apache RocketMQ</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Frocketmq.apache.org%2F" target="_blank">Apache RocketMQ文档</a></td> 
   <td>高可用功能多样</td> 
  </tr> 
  <tr> 
   <td>分布式消息队列</td> 
   <td>RabbitMQ</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2F" target="_blank">RabbitMQ文档</a></td> 
   <td>支持各种扩展插件功能多样性</td> 
  </tr> 
  <tr> 
   <td>分布式搜索引擎</td> 
   <td>ElasticSearch</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Felasticsearch%2F" target="_blank">ElasticSearch官网</a></td> 
   <td>业界知名</td> 
  </tr> 
  <tr> 
   <td>分布式数据同步</td> 
   <td>Alibaba Canal</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fcanal%2Fwiki" target="_blank">Alibaba Canal官网</a></td> 
   <td>采集数据同步各种数据库 ES Redis Mysql</td> 
  </tr> 
  <tr> 
   <td>分布式链路追踪</td> 
   <td>Apache SkyWalking</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fskywalking.apache.org%2Fdocs%2F" target="_blank">Apache SkyWalking文档</a></td> 
   <td>链路追踪、网格分析、度量聚合、可视化</td> 
  </tr> 
  <tr> 
   <td>分布式日志中心</td> 
   <td>ELK</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Felasticsearch%2F" target="_blank">ElasticSearch官网</a></td> 
   <td>ELK业界成熟解决方案</td> 
  </tr> 
  <tr> 
   <td>分布式锁</td> 
   <td>Lock4j</td> 
   <td><a href="https://gitee.com/baomidou/lock4j">Lock4j官网</a></td> 
   <td>注解锁、工具锁 多种多样</td> 
  </tr> 
  <tr> 
   <td>分布式幂等</td> 
   <td>Redisson</td> 
   <td><a href="https://gitee.com/baomidou/lock4j">Lock4j文档</a></td> 
   <td>拦截重复提交</td> 
  </tr> 
  <tr> 
   <td>分布式任务调度</td> 
   <td>Xxl-Job</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.xuxueli.com%2Fxxl-job%2F" target="_blank">Xxl-Job官网</a></td> 
   <td>高性能 高可靠 易扩展</td> 
  </tr> 
  <tr> 
   <td>分布式文件存储</td> 
   <td>Minio</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.min.io%2F" target="_blank">Minio文档</a></td> 
   <td>本地存储</td> 
  </tr> 
  <tr> 
   <td>分布式云存储</td> 
   <td>七牛、阿里、腾讯</td> 
   <td><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4359146&doc_id=1469725">OSS使用文档</a></td> 
   <td>云存储</td> 
  </tr> 
  <tr> 
   <td>分布式监控</td> 
   <td>Prometheus、Grafana</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprometheus.io%2Fdocs%2Fintroduction%2Foverview%2F" target="_blank">Prometheus文档</a></td> 
   <td>全方位性能监控</td> 
  </tr> 
  <tr> 
   <td>服务监控</td> 
   <td>SpringBoot-Admin</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodecentric.github.io%2Fspring-boot-admin%2Fcurrent%2F" target="_blank">SpringBoot-Admin文档</a></td> 
   <td>全方位服务监控</td> 
  </tr> 
  <tr> 
   <td>数据库框架</td> 
   <td>Mybatis-Plus</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2Fguide%2F" target="_blank">Mybatis-Plus文档</a></td> 
   <td>快速 CRUD 增加开发效率</td> 
  </tr> 
  <tr> 
   <td>数据库框架</td> 
   <td>P6spy</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp6spy.readthedocs.io%2F" target="_blank">p6spy官网</a></td> 
   <td>更强劲的 SQL 分析</td> 
  </tr> 
  <tr> 
   <td>多数据源框架</td> 
   <td>Dynamic-Datasource</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Ftracy5546%2Fdynamic-datasource%2Fcontent" target="_blank">dynamic-ds文档</a></td> 
   <td>支持主从与多种类数据库异构</td> 
  </tr> 
  <tr> 
   <td>序列化框架</td> 
   <td>Jackson</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFasterXML%2Fjackson" target="_blank">Jackson官网</a></td> 
   <td>统一使用 jackson 高效可靠</td> 
  </tr> 
  <tr> 
   <td>Redis客户端</td> 
   <td>Redisson</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Fwiki%2F%25E7%259B%25AE%25E5%25BD%2595" target="_blank">Redisson文档</a></td> 
   <td>支持单机、集群配置</td> 
  </tr> 
  <tr> 
   <td>校验框架</td> 
   <td>Validation</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jboss.org%2Fhibernate%2Fstable%2Fvalidator%2Freference%2Fen-US%2Fhtml_single%2F" target="_blank">Validation文档</a></td> 
   <td>增强接口安全性、严谨性 支持国际化</td> 
  </tr> 
  <tr> 
   <td>Excel框架</td> 
   <td>Alibaba EasyExcel</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feasyexcel%2Fdoc%2Feasyexcel" target="_blank">EasyExcel文档</a></td> 
   <td>性能优异 扩展性强</td> 
  </tr> 
  <tr> 
   <td>文档框架</td> 
   <td>Knife4j</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.xiaominfo.com%2Fknife4j%2Fdocumentation%2F" target="_blank">Knife4j文档</a></td> 
   <td>美化接口文档</td> 
  </tr> 
  <tr> 
   <td>工具类框架</td> 
   <td>Hutool、Lombok</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hutool.cn%2Fdocs%2F" target="_blank">Hutool文档</a></td> 
   <td>减少代码冗余 增加安全性</td> 
  </tr> 
  <tr> 
   <td>代码生成器</td> 
   <td>适配MP、Knife4j规范化代码</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hutool.cn%2Fdocs%2F" target="_blank">Hutool文档</a></td> 
   <td>一键生成前后端代码</td> 
  </tr> 
  <tr> 
   <td>部署方式</td> 
   <td>Docker</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2F" target="_blank">Docker文档</a></td> 
   <td>容器编排 一键部署业务集群</td> 
  </tr> 
  <tr> 
   <td>国际化</td> 
   <td>SpringMessage</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-framework%2Fdocs%2Fcurrent%2Freference%2Fhtml%2Fweb.html%23mvc" target="_blank">SpringMVC文档</a></td> 
   <td>Spring标准国际化方案</td> 
  </tr> 
 </tbody> 
</table> 
<h2>软件架构图</h2> 
<p><img src="https://images.gitee.com/uploads/images/2022/0520/152809_0edbfaf1_1766278.png" referrerpolicy="no-referrer"></p> 
<h2>贡献代码</h2> 
<p>欢迎各路英雄豪杰 <code>PR</code> 代码 请提交到 <code>dev</code> 开发分支 统一测试发版</p> 
<h2>业务功能</h2> 
<table> 
 <thead> 
  <tr> 
   <th>功能</th> 
   <th>介绍</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>用户管理</td> 
   <td>用户是系统操作者，该功能主要完成系统用户配置。</td> 
  </tr> 
  <tr> 
   <td>部门管理</td> 
   <td>配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</td> 
  </tr> 
  <tr> 
   <td>岗位管理</td> 
   <td>配置系统用户所属担任职务。</td> 
  </tr> 
  <tr> 
   <td>菜单管理</td> 
   <td>配置系统菜单，操作权限，按钮权限标识等。</td> 
  </tr> 
  <tr> 
   <td>角色管理</td> 
   <td>角色菜单权限分配、设置角色按机构进行数据范围权限划分。</td> 
  </tr> 
  <tr> 
   <td>字典管理</td> 
   <td>对系统中经常使用的一些较为固定的数据进行维护。</td> 
  </tr> 
  <tr> 
   <td>参数管理</td> 
   <td>对系统动态配置常用参数。</td> 
  </tr> 
  <tr> 
   <td>通知公告</td> 
   <td>系统通知公告信息发布维护。</td> 
  </tr> 
  <tr> 
   <td>操作日志</td> 
   <td>系统正常操作日志记录和查询；系统异常信息日志记录和查询。</td> 
  </tr> 
  <tr> 
   <td>登录日志</td> 
   <td>系统登录日志记录查询包含登录异常。</td> 
  </tr> 
  <tr> 
   <td>文件管理</td> 
   <td>系统文件上传、下载等管理。</td> 
  </tr> 
  <tr> 
   <td>定时任务</td> 
   <td>在线（添加、修改、删除)任务调度包含执行结果日志。</td> 
  </tr> 
  <tr> 
   <td>代码生成</td> 
   <td>前后端代码的生成（java、html、xml、sql）支持CRUD下载 。</td> 
  </tr> 
  <tr> 
   <td>系统接口</td> 
   <td>根据业务代码自动生成相关的api接口文档。</td> 
  </tr> 
  <tr> 
   <td>服务监控</td> 
   <td>监视集群系统CPU、内存、磁盘、堆栈、在线日志、Spring相关配置等。</td> 
  </tr> 
  <tr> 
   <td>缓存监控</td> 
   <td>对系统的缓存信息查询，命令统计等。</td> 
  </tr> 
  <tr> 
   <td>在线构建器</td> 
   <td>拖动表单元素生成相应的HTML代码。</td> 
  </tr> 
  <tr> 
   <td>连接池监视</td> 
   <td>监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</td> 
  </tr> 
  <tr> 
   <td>使用案例</td> 
   <td>系统的一些功能案例</td> 
  </tr> 
 </tbody> 
</table> 
<h2>演示图例</h2> 
<table cellpadding="1" cellspacing="1" style="width:700px"> 
 <tbody> 
  <tr> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-972235bcbe3518dedd351ff0e2ee7d1031c.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-5e0097702fa91e2e36391de8127676a7fa1.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td> <p><img src="https://oscimg.oschina.net/oscnet/up-e56e3828f48cd9886d88731766f06d5f3c1.png" width="1920" referrerpolicy="no-referrer"></p> </td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-0715990ea1a9f254ec2138fcd063c1f556a.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-eaf5417ccf921bb64abb959e3d8e290467f.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-fc285cf33095ebf8318de6999af0f473861.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-60c83fd8bd61c29df6dbf47c88355e9c272.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-7f731948c8b73c7d90f67f9e1c7a534d5c3.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-e4de89b5e2d20c52d3c3a47f9eb88eb8526.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-8791d823a508eb90e67c604f36f57491a67.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-4589afd99982ead331785299b894174feb6.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-8ea177cdacaea20995daf2f596b15232561.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img align="left" src="https://oscimg.oschina.net/oscnet/up-32d1d04c55c11f74c9129fbbc58399728c4.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-04fa118f7631b7ae6fd72299ca0a1430a63.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-fe7e85b65827802bfaadf3acd42568b58c7.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td><img src="https://oscimg.oschina.net/oscnet/up-eff2b02a54f8188022d8498cfe6af6fcc06.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            