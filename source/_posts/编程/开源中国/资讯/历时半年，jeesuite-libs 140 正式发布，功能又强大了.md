
---
title: '历时半年，jeesuite-libs 1.4.0 正式发布，功能又强大了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5654'
author: 开源中国
comments: false
date: Sun, 22 May 2022 23:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5654'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292e; text-align:start">  从上次获得海纳奖后差不多半年过去了，由于功能比较多，这半年一直反复测试验证，jeesuite-libs终于迎来了1.4.0-release版本发布。本次更新包括以下几个重大更新：</p> 
<ul> 
 <li>升级Spring Boot版本到2.6.6，Spring Cloud版本到2021.0.1</li> 
 <li>新增网关模块jeesuite-gateway-adapter，支持认证授权、审计日志、openAPI、响应重写、动态路由等</li> 
 <li>新增消息中间件适配模块jeesuite-amqp-adapter，支持rocketMQ、kafka、redis、阿里云MNS、腾讯云CMQ等</li> 
 <li>新增文件存储适配模块jeesuite-cos-adapter，支持阿里云、腾讯云、华为云、七牛、AWS、minIO</li> 
 <li>新增日志模块jeesuite-logging，支持日志配置自动刷新、日志处理以及一些日志工具类等</li> 
</ul> 
<h2 style="text-align:start">jeesuite-common</h2> 
<ul> 
 <li>重写httpUtils自适应支持JDK、okhttp3、apache httpclient模式，兼容Springcloud负载均衡</li> 
 <li>新增重试异步线程池</li> 
 <li>优化ResourceUtils无缝兼容Apollo、Nacos集成</li> 
 <li>新增GlobalRuntimeContext和CurrentRuntimeContext统一管理运行时上下文</li> 
 <li>新增带时间标识全局ID生成工具TimestampGUIDGenarator</li> 
 <li>优化BeanUtils支持嵌套对象复制</li> 
 <li>修复Kryo序列化工具类线程安全问题</li> 
</ul> 
<h2 style="text-align:start">jeesuite-common2</h2> 
<ul> 
 <li>新增全局节点ID生成器ZkWorkIdGenerator</li> 
 <li>新增简单定时任务工具GlobalInternalScheduleService</li> 
 <li>优化分布式锁</li> 
</ul> 
<h2 style="text-align:start">jeesuite-mybatis</h2> 
<ul> 
 <li>全新重写MultiRouteDataSource，更加灵活支持多组、多租户、读写分离等场景</li> 
 <li>新增自动字段填充处理，支持升级字段、租户字段、ID等字段写入</li> 
 <li>新增SQL重写组件，统一处理租户隔离、数据权限、软删除过滤等</li> 
 <li>重构自动缓存组件、兼容多租户、数据权限等场景</li> 
 <li>BaseMapper支持乐观锁更新方法</li> 
 <li>修复某些复杂SQL分页统计查询失败</li> 
</ul> 
<h2 style="text-align:start">jeesuite-cache</h2> 
<ul> 
 <li>新增CacheAdapter、CacheUtils，自动适配本地缓存和redis缓存实现</li> 
 <li>新增RedisTemplateGroups，灵活管理多组redis实例</li> 
</ul> 
<h2 style="text-align:start">jeesuite-scheduler</h2> 
<ul> 
 <li>新增Redis分布式协调器</li> 
 <li>新增http API管理接口</li> 
 <li>简化ScheduleConf注解部分属性</li> 
</ul> 
<h2 style="text-align:start">jeesuite-security</h2> 
<ul> 
 <li>新增兼容webflux反应式编程模式</li> 
 <li>重构API权限检查逻辑</li> 
</ul> 
<h2 style="text-align:start">jeesuite-springweb</h2> 
<ul> 
 <li>新增本地mock登录机制</li> 
 <li>新增请求/响应增强模块，默认实现响应重写等</li> 
 <li>优化AppMetadata生成逻辑</li> 
</ul> 
<h2 style="text-align:start">jeesuite-springboot-starter</h2> 
<ul> 
 <li>移除原定义的JeesuiteXxxEnabled注解改成基于Condition自动加载</li> 
 <li>新增自定义JDBC及Mybatis starter</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#40485b">作者微信号：x3b4f07082，欢迎随时交流</span></p>
                                        </div>
                                      
</div>
            