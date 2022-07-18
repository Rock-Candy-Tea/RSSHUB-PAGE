
---
title: 'RuoYi-Cloud-Plus 发布 1.1.0 新增 ELK 与三大 MQ 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0520/152809_0edbfaf1_1766278.png'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 09:56:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0520/152809_0edbfaf1_1766278.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0; margin-right:0; text-align:left">升级说明</h1> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">重大更新</h3> 
<ul> 
 <li>[重大更新] 新增 ELK 分布式日志中心整合</li> 
 <li>[重大更新] 新增 ruoyi-stream-mq 演示模块 完成 RabbitMQ RocketMQ Kafka 整合</li> 
 <li>[重大更新] 优化 docker 部署方式 使用 host 模式简化部署流程 降低使用成本</li> 
 <li>[重大更新] 调整 dubbo 服务注册命名空间与 cloud 服务保持一致 通过注册组区分访问服务</li> 
 <li>[安全性] 优化 nginx 限制外网访问内网 actuator 相关路径 建议升级</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">依赖升级</h3> 
<ul> 
 <li>update springboot 2.6.8 => 2.6.9</li> 
 <li>update easyexcel 3.1.0 => 3.1.1</li> 
 <li>update hutool 5.8.2 => 5.8.3</li> 
 <li>update redisson 3.17.2 => 3.17.4</li> 
 <li>update aws-java-sdk-s3 1.12.215 => 1.12.248</li> 
 <li>update tencentcloud-sdk-java 3.1.500 => 3.1.537</li> 
 <li>update dubbo 3.0.8 => 3.0.9</li> 
 <li>update seata 1.5.1 => 1.5.2</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">功能更新</h3> 
<ul> 
 <li>update 增加 redisson key 前缀配置</li> 
 <li>update 优化 DateColumn 支持单模板多key场景</li> 
 <li>update 优化部署脚本 增加 elk kafka rabbitmq rocketmq 等配置</li> 
 <li>update 修改 oss 客户端自定义域名 统一使用https开关控制协议头</li> 
 <li>update 优化 使用 StreamUtils 简化业务流操纵</li> 
 <li>update 优化 ruoyi-demo 模块 去除用不上的 seata 依赖</li> 
 <li>update 优化 接口文档 接口地址与服务地址不匹配问题</li> 
 <li>update 优化字典数据回显样式下拉框显示值</li> 
 <li>update 默认不启用压缩文件缓存防止node_modules过大</li> 
 <li>update 优化登出方法</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新功能</h3> 
<ul> 
 <li>add 增加 rocketmq docker编排</li> 
 <li>add 新增 rabbitmq docker编排 包含延迟插件</li> 
 <li>add 新增 kafka docker编排</li> 
 <li>add 增加 es ik 分词器插件集成</li> 
 <li>add 增加 StreamUtils 流工具 简化 stream 流操纵</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">问题修复</h3> 
<ul> 
 <li>fix 修复 获取 SensitiveService 空问题 增加空兼容</li> 
 <li>fix 修复 演示页面导出路径错误</li> 
 <li>fix 修复 minio 上传自定义域名回显路径错误问题</li> 
 <li>fix 修复 hutool 工具返回不可操纵类型 导致报错问题</li> 
 <li>fix 修复 远程调用短信功能返回实体 SysSms 序列化报错问题</li> 
 <li>fix 修复 复制过程错误 导致演示excel文件损坏问题</li> 
 <li>fix 修复 dubbo 注册组不生效问题 通过覆盖源码方式</li> 
 <li>fix 修复代码生成首字母大写问题</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">平台简介</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">RuoYi-Cloud-Plus 是一个微服务通用权限管理系统，重写 RuoYi-Cloud 并进行全方位升级 (不兼容原框架)。</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
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
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">微服务权限管理系统</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">RuoYi-Cloud-Plus</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/JavaLionLi/RuoYi-Cloud-Plus">RuoYi-Cloud-Plus 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">重写 RuoYi-Cloud 全方位升级 (不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式集群分支</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">RuoYi-Vue-Plus</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus">RuoYi-Vue-Plus 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">重写 RuoYi-Vue (不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">前端开发框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Vue、Element UI</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN" target="_blank">Element UI 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">后端开发框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringBoot</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot%2F%23learn" target="_blank">SpringBoot 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">微服务开发框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringCloud</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud" target="_blank">SpringCloud 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">微服务开发框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringCloudAlibaba</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud-alibaba" target="_blank">SpringCloudAlibaba 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">容器框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Undertow</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fundertow.io%2F" target="_blank">Undertow 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">基于 XNIO 的高性能容器</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">权限认证框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Sa-Token、Jwt</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsa-token.dev33.cn%2F" target="_blank">Sa-Token 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">强解耦、强扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">关系数据库</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">MySQL</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.mysql.com%2F" target="_blank">MySQL 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">适配 8.X 最低 5.7</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">关系数据库</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Oracle</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.oracle.com%2Fcn%2Fdatabase%2F" target="_blank">Oracle 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">适配 12c</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">关系数据库</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">PostgreSQL</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2F" target="_blank">PostgreSQL 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">适配 14</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">关系数据库</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SQLServer</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fsql%2Fsql-server" target="_blank">SQLServer 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">适配 2019</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">缓存数据库</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Redis</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2F" target="_blank">Redis 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">适配 6.X 最低 5.X</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式注册中心</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Alibaba Nacos</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2Fquick-start.html" target="_blank">Alibaba Nacos 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 2.X 基于 GRPC 通信高性能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式配置中心</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Alibaba Nacos</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2Fquick-start.html" target="_blank">Alibaba Nacos 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 2.X 基于 GRPC 通信高性能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">服务网关</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringCloud Gateway</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud-gateway" target="_blank">SpringCloud Gateway 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">响应式高性能网关</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">负载均衡</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringCloud Loadbalancer</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fguides%2Fgs%2Fspring-cloud-loadbalancer%2F" target="_blank">SpringCloud Loadbalancer 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">负载均衡处理</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">RPC 远程调用</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Apache Dubbo</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdubbo.apache.org%2Fzh%2F" target="_blank">Apache Dubbo 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">原生态使用体验、高性能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式限流熔断</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Alibaba Sentinel</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsentinelguard.io%2Fzh-cn%2F" target="_blank">Alibaba Sentinel 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">无侵入、高扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式事务</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Alibaba Seata</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fseata.io%2Fzh-cn%2F" target="_blank">Alibaba Seata 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">无侵入、高扩展 支持 四种模式</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式消息队列</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringCloud Stream</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-cloud-stream" target="_blank">SpringCloud Stream 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">门面框架兼容各种 MQ 集成</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式消息队列</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Apache Kafka</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkafka.apache.org%2F" target="_blank">Apache Kafka 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">高性能高速度</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式消息队列</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Apache RocketMQ</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Frocketmq.apache.org%2F" target="_blank">Apache RocketMQ 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">高可用功能多样</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式消息队列</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">RabbitMQ</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2F" target="_blank">RabbitMQ 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">支持各种扩展插件功能多样性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式搜索引擎</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ElasticSearch</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Felasticsearch%2F" target="_blank">ElasticSearch 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">业界知名</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式数据同步</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Alibaba Canal</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fcanal%2Fwiki" target="_blank">Alibaba Canal 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采集数据同步各种数据库 ES Redis Mysql</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式链路追踪</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Apache SkyWalking</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fskywalking.apache.org%2Fdocs%2F" target="_blank">Apache SkyWalking 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">链路追踪、网格分析、度量聚合、可视化</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式日志中心</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ELK</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Felasticsearch%2F" target="_blank">ElasticSearch 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">ELK 业界成熟解决方案</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式锁</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Lock4j</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/baomidou/lock4j">Lock4j 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">注解锁、工具锁 多种多样</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式幂等</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Redisson</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/baomidou/lock4j">Lock4j 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">拦截重复提交</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式任务调度</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Xxl-Job</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.xuxueli.com%2Fxxl-job%2F" target="_blank">Xxl-Job 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">高性能 高可靠 易扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式文件存储</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Minio</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.min.io%2F" target="_blank">Minio 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">本地存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式云存储</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">七牛、阿里、腾讯</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4359146&doc_id=1469725">OSS 使用文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">云存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分布式监控</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Prometheus、Grafana</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprometheus.io%2Fdocs%2Fintroduction%2Foverview%2F" target="_blank">Prometheus 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">全方位性能监控</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">服务监控</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringBoot-Admin</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodecentric.github.io%2Fspring-boot-admin%2Fcurrent%2F" target="_blank">SpringBoot-Admin 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">全方位服务监控</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">数据库框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Mybatis-Plus</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2Fguide%2F" target="_blank">Mybatis-Plus 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">快速 CRUD 增加开发效率</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">数据库框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">P6spy</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp6spy.readthedocs.io%2F" target="_blank">p6spy 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">更强劲的 SQL 分析</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">多数据源框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Dynamic-Datasource</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Ftracy5546%2Fdynamic-datasource%2Fcontent" target="_blank">dynamic-ds 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">支持主从与多种类数据库异构</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">序列化框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Jackson</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFasterXML%2Fjackson" target="_blank">Jackson 官网</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">统一使用 jackson 高效可靠</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Redis 客户端</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Redisson</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Fwiki%2F%25E7%259B%25AE%25E5%25BD%2595" target="_blank">Redisson 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">支持单机、集群配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">校验框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Validation</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jboss.org%2Fhibernate%2Fstable%2Fvalidator%2Freference%2Fen-US%2Fhtml_single%2F" target="_blank">Validation 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">增强接口安全性、严谨性 支持国际化</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Excel 框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Alibaba EasyExcel</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feasyexcel%2Fdoc%2Feasyexcel" target="_blank">EasyExcel 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">性能优异 扩展性强</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">文档框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Knife4j</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.xiaominfo.com%2Fknife4j%2Fdocumentation%2F" target="_blank">Knife4j 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">美化接口文档</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">工具类框架</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Hutool、Lombok</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hutool.cn%2Fdocs%2F" target="_blank">Hutool 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">减少代码冗余 增加安全性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">代码生成器</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">适配 MP、Knife4j 规范化代码</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hutool.cn%2Fdocs%2F" target="_blank">Hutool 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">一键生成前后端代码</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">部署方式</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Docker</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2F" target="_blank">Docker 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">容器编排 一键部署业务集群</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">国际化</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">SpringMessage</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-framework%2Fdocs%2Fcurrent%2Freference%2Fhtml%2Fweb.html%23mvc" target="_blank">SpringMVC 文档</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Spring 标准国际化方案</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">软件架构图</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://images.gitee.com/uploads/images/2022/0520/152809_0edbfaf1_1766278.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">贡献代码</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎各路英雄豪杰<span> </span><code>PR</code><span> </span>代码 请提交到<span> </span><code>dev</code><span> </span>开发分支 统一测试发版</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">业务功能</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>功能</th> 
   <th>介绍</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">用户管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">用户是系统操作者，该功能主要完成系统用户配置。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">部门管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">岗位管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置系统用户所属担任职务。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">菜单管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">配置系统菜单，操作权限，按钮权限标识等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">角色管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">角色菜单权限分配、设置角色按机构进行数据范围权限划分。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">字典管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">对系统中经常使用的一些较为固定的数据进行维护。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">参数管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">对系统动态配置常用参数。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">通知公告</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">系统通知公告信息发布维护。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">操作日志</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">系统正常操作日志记录和查询；系统异常信息日志记录和查询。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">登录日志</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">系统登录日志记录查询包含登录异常。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">文件管理</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">系统文件上传、下载等管理。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">定时任务</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">在线（添加、修改、删除) 任务调度包含执行结果日志。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">代码生成</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">前后端代码的生成（java、html、xml、sql）支持 CRUD 下载 。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">系统接口</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据业务代码自动生成相关的 api 接口文档。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">服务监控</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">监视集群系统 CPU、内存、磁盘、堆栈、在线日志、Spring 相关配置等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">缓存监控</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">对系统的缓存信息查询，命令统计等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">在线构建器</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">拖动表单元素生成相应的 HTML 代码。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">连接池监视</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">监视当前系统数据库连接池状态，可进行分析 SQL 找出系统性能瓶颈。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">使用案例</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">系统的一些功能案例</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">演示图例</h2> 
<table cellpadding="1" cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:700px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-972235bcbe3518dedd351ff0e2ee7d1031c.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-5e0097702fa91e2e36391de8127676a7fa1.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> <p style="margin-left:0; margin-right:0"><img src="https://oscimg.oschina.net/oscnet/up-e56e3828f48cd9886d88731766f06d5f3c1.png" width="1920" referrerpolicy="no-referrer"></p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-0715990ea1a9f254ec2138fcd063c1f556a.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-eaf5417ccf921bb64abb959e3d8e290467f.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-fc285cf33095ebf8318de6999af0f473861.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-60c83fd8bd61c29df6dbf47c88355e9c272.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7f731948c8b73c7d90f67f9e1c7a534d5c3.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-e4de89b5e2d20c52d3c3a47f9eb88eb8526.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-8791d823a508eb90e67c604f36f57491a67.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-4589afd99982ead331785299b894174feb6.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-8ea177cdacaea20995daf2f596b15232561.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img align="left" src="https://oscimg.oschina.net/oscnet/up-32d1d04c55c11f74c9129fbbc58399728c4.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-04fa118f7631b7ae6fd72299ca0a1430a63.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-fe7e85b65827802bfaadf3acd42568b58c7.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-eff2b02a54f8188022d8498cfe6af6fcc06.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            