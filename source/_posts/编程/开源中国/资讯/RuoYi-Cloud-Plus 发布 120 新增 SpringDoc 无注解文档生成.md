
---
title: 'RuoYi-Cloud-Plus 发布 1.2.0 新增 SpringDoc 无注解文档生成'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-972235bcbe3518dedd351ff0e2ee7d1031c.png'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 09:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-972235bcbe3518dedd351ff0e2ee7d1031c.png'
---

<div>   
<div class="content">
                                                                                            <h1><span>更新日志</span></h1> 
<h3><span>重大更新</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>[重大更新] 新增 ruoyi-common-elasticsearch 模块 集成 easy-es 傻瓜式操作搜索引擎</p> </li> 
 <li> <p>[重大更新] 新增 ruoyi-common-doc 整合 springdoc 基于 javadoc 实现无注解零入侵生成接口文档</p> </li> 
 <li> <p>[不兼容更新] 移除 swagger 所属 ruoyi-doc ruoyi-common-swagger 两个模块 建议使用 ruoyi-common-doc 模块</p> </li> 
</ul> 
<h3><span>依赖升级</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>update springboot 2.6.9 => 2.7.2 重构使用最新自动配置方式</p> </li> 
 <li> <p>update springboot-admin 2.6.7 => 2.7.3</p> </li> 
 <li> <p>update dubbo 3.0.9 => 3.0.10</p> </li> 
 <li> <p>update redisson 3.17.4 => 3.17.5</p> </li> 
 <li> <p>update hutool 5.8.3 => 5.8.5</p> </li> 
 <li> <p>update okhttp 4.9.1 => 4.10.0</p> </li> 
 <li> <p>update aws-java-sdk-s3 1.12.248 => 1.12.264 修复依赖安全漏洞</p> </li> 
 <li> <p>update aliyun.sms 2.0.9 => 2.0.16</p> </li> 
 <li> <p>update tencent.sms 3.1.537 => 3.1.555</p> </li> 
 <li> <p>update guava 30.0-jre => 31.1-jre</p> </li> 
</ul> 
<h3><span>功能更新</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>update 修改 资源服务 不提供默认短信 sdk 依赖</p> </li> 
 <li> <p>update 优化表格上右侧工具条（搜索按钮显隐&右侧样式凸出）</p> </li> 
 <li> <p>update 优化 前后端多环境部署保持一致 删除无用环境文件</p> </li> 
 <li> <p>update 优化 错误登录锁定与新增解锁功能</p> </li> 
 <li> <p>update 优化字典数据使用store存取</p> </li> 
 <li> <p>update 优化布局设置使用el-drawer抽屉显示</p> </li> 
 <li> <p>update 更新框架文档 专栏与视频 链接地址</p> </li> 
 <li> <p>update 优化 对象上传 主动设置文件公共读 解决天翼云OSS文件私有问题</p> </li> 
 <li> <p>update 优化 网关验证码过滤器 路径匹配改为严格匹配</p> </li> 
 <li> <p>update 优化 数据导致权限生成 SQL 重复问题</p> </li> 
</ul> 
<h3><span>新功能</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>add 增加 全局跨域过滤器 处理跨域请求 适配移动端访问</p> </li> 
 <li> <p>add 增加 搜索引擎 crud 演示案例</p> </li> 
</ul> 
<h3><span>问题修复</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>fix 防止date-picker组件报错，降级element-ui版本</p> </li> 
 <li> <p>fix 修复 RedisUtils 并发 set ttl 错误问题</p> </li> 
 <li> <p>fix 防止vue3主键字段名与row或ids一致导致报错的问题</p> </li> 
 <li> <p>fix 修复 幂等组件 逻辑问题导致线程变量未清除</p> </li> 
 <li> <p>fix 修复 图片回显查询 路径错误问题</p> </li> 
 <li> <p>fix 修复 脱敏没有实现类导致返回数据异常问题</p> </li> 
 <li> <p>fix 修复 xxljob 错误导入配置文件引发的问题</p> </li> 
 <li> <p>fix 修复 gateway模块 dockerfile 端口编写错误</p> </li> 
 <li> <p>fix 修复用户导出字典使用错误</p> </li> 
 <li> <p>fix 修复 demo 模块 远程调用失败问题</p> </li> 
 <li> <p>fix 修复 sentinel 控制台未适配 springboot 2.6 新路由策略导致无法登录问题</p> </li> 
</ul> 
<h2><span>Vue版本发布 4.3.0-beta1 公测版</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">详细地址: https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/releases/tag/v4.3.0-beta1</p> 
<h2><span>平台简介</span></h2> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">RuoYi-Cloud-Plus <code>微服务通用权限管理系统</code> 重写 RuoYi-Cloud 全方位升级(不兼容原框架)</p> 
</blockquote> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">项目代码、文档 均开源免费可商用 遵循开源协议在项目中保留开源协议文件即可<br> 活到老写到老 为兴趣而开源 为学习而开源 为让大家真正可以学到技术而开源</p> 
</blockquote> 
<table style="display:table; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">功能介绍</th> 
   <th style="background-color:#f0f0f0; text-align:left">使用技术</th> 
   <th style="background-color:#f0f0f0; text-align:left">特性注意事项</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">微服务权限管理系统</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Cloud-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">重写 RuoYi-Cloud 全方位升级(不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式集群分支</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Vue-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">重写 RuoYi-Vue (不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">前端开发框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Vue、Element UI</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">后端开发框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringBoot</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">微服务开发框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringCloud</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">微服务开发框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringCloudAlibaba</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">容器框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Undertow</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">基于 XNIO 的高性能容器</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">权限认证框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Sa-Token、Jwt</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">强解耦、强扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">MySQL</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 8.X 最低 5.7</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库(未完成)</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Oracle</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 12c</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库(未完成)</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">PostgreSQL</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 14</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库(未完成)</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SQLServer</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 2019</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">缓存数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redis</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 6.X 最低 5.X</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式注册中心</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba Nacos</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">采用2.X 基于GRPC通信高性能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式配置中心</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba Nacos</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">采用2.X 基于GRPC通信高性能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">服务网关</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringCloud Gateway</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">响应式高性能网关</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">负载均衡</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringCloud Loadbalancer</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">负载均衡处理</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RPC远程调用</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Apache Dubbo</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">原生态使用体验、高性能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式限流熔断</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba Sentinel</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">无侵入、高扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式事务</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba Seata</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">无侵入、高扩展 支持 四种模式</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式消息队列</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringCloud Stream</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">门面框架兼容各种MQ集成</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式消息队列</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Apache Kafka</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">高性能高速度</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式消息队列</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Apache RocketMQ</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">高可用功能多样</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式消息队列</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RabbitMQ</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">支持各种扩展插件功能多样性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式搜索引擎</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">ElasticSearch、Easy-Es</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">以 Mybatis-Plus 方式操作 ElasticSearch</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式数据同步(未完成)</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba Canal</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">采集数据同步各种数据库 ES Redis Mysql</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式链路追踪(未完成)</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Apache SkyWalking</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">链路追踪、网格分析、度量聚合、可视化</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式日志中心</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">ELK</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">ELK业界成熟解决方案</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式锁</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Lock4j</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">注解锁、工具锁 多种多样</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式幂等</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redisson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">拦截重复提交</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式任务调度</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Xxl-Job</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">高性能 高可靠 易扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式文件存储</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Minio</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">本地存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式云存储</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">七牛、阿里、腾讯</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">云存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">短信模块</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">阿里、腾讯</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">短信发送</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式监控(未完成)</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Prometheus、Grafana</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">全方位性能监控</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">服务监控</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringBoot-Admin</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">全方位服务监控</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">数据库框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Mybatis-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">快速 CRUD 增加开发效率</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">数据库框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">P6spy</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">更强劲的 SQL 分析</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">多数据源框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Dynamic-Datasource</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">支持主从与多种类数据库异构</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">序列化框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Jackson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">统一使用 jackson 高效可靠</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redis客户端</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redisson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">支持单机、集群配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">校验框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Validation</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">增强接口安全性、严谨性 支持国际化</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Excel框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba EasyExcel</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">性能优异 扩展性强</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">文档框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringDoc、javadoc</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">无注解零入侵基于java注释</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">工具类框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Hutool、Lombok</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">减少代码冗余 增加安全性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">代码生成器</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配MP、Knife4j规范化代码</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">一键生成前后端代码</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">部署方式</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Docker</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">容器编排 一键部署业务集群</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">国际化</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringMessage</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring标准国际化方案</td> 
  </tr> 
 </tbody> 
</table> 
<h2><span>业务功能</span></h2> 
<table style="display:table; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">功能</th> 
   <th style="background-color:#f0f0f0; text-align:left">介绍</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">用户管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">用户是系统操作者，该功能主要完成系统用户配置。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">部门管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">岗位管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">配置系统用户所属担任职务。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">菜单管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">配置系统菜单，操作权限，按钮权限标识等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">角色管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">角色菜单权限分配、设置角色按机构进行数据范围权限划分。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">字典管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">对系统中经常使用的一些较为固定的数据进行维护。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">参数管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">对系统动态配置常用参数。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">通知公告</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统通知公告信息发布维护。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">操作日志</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统正常操作日志记录和查询；系统异常信息日志记录和查询。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">登录日志</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统登录日志记录查询包含登录异常。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">文件管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统文件上传、下载等管理。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">定时任务</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">在线（添加、修改、删除)任务调度包含执行结果日志。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">代码生成</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">前后端代码的生成（java、html、xml、sql）支持CRUD下载 。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统接口</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">根据业务代码自动生成相关的api接口文档。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">服务监控</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">监视集群系统CPU、内存、磁盘、堆栈、在线日志、Spring相关配置等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">缓存监控</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">对系统的缓存信息查询，命令统计等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">在线构建器</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">拖动表单元素生成相应的HTML代码。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">连接池监视</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">使用案例</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统的一些功能案例</td> 
  </tr> 
 </tbody> 
</table> 
<h2><span>演示图例</span></h2> 
<table border="1" cellpadding="1" cellspacing="1" style="display:table; text-align:left; width:500px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-972235bcbe3518dedd351ff0e2ee7d1031c.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-5e0097702fa91e2e36391de8127676a7fa1.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> <p style="color:black; margin-left:0; margin-right:0"><img src="https://oscimg.oschina.net/oscnet/up-e56e3828f48cd9886d88731766f06d5f3c1.png" width="1920" referrerpolicy="no-referrer"></p> </td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-0715990ea1a9f254ec2138fcd063c1f556a.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-eaf5417ccf921bb64abb959e3d8e290467f.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-fc285cf33095ebf8318de6999af0f473861.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-60c83fd8bd61c29df6dbf47c88355e9c272.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-7f731948c8b73c7d90f67f9e1c7a534d5c3.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-e4de89b5e2d20c52d3c3a47f9eb88eb8526.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-8791d823a508eb90e67c604f36f57491a67.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-4589afd99982ead331785299b894174feb6.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-8ea177cdacaea20995daf2f596b15232561.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-32d1d04c55c11f74c9129fbbc58399728c4.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-04fa118f7631b7ae6fd72299ca0a1430a63.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-fe7e85b65827802bfaadf3acd42568b58c7.png" width="1920" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-eff2b02a54f8188022d8498cfe6af6fcc06.png" width="1920" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            