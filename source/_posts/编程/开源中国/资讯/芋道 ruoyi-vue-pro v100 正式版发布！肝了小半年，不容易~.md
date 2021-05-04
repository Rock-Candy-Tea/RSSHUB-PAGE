
---
title: '芋道 ruoyi-vue-pro v1.0.0 正式版发布！肝了小半年，不容易~'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3739'
author: 开源中国
comments: false
date: Tue, 04 May 2021 00:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3739'
---

<div>   
<div class="content">
                                                                                            <p>项目地址：<a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<p>更新说明：</p> 
<p style="text-align:start">第一个版本，基于 <a href="https://gitee.com/y_project/RuoYi-Vue" target="_blank">RuoYi-Vue</a> 重构，主要是三个方面：</p> 
<ul> 
 <li>代码的重构</li> 
 <li>技术选型的调整</li> 
 <li>后台功能的新增</li> 
</ul> 
<p style="text-align:start">因此，<code>v1.0.0</code> 的更新日志，分成这三方面来写。</p> 
<h3 style="text-align:start">代码的重构</h3> 
<ul> 
 <li>调整整体代码结构，将多个 Maven Module 合并为单个，使用 Java package 进行拆分隔离，如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstatic.iocoder.cn%2Fruoyi-vue-pro-modules.jpg" target="_blank">图</a> 所示。原因是：随着业务逻辑的逐步复杂，多个 Maven Module 的依赖关系的管理，会是一个很大的问题。</li> 
 <li>拆分 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework" target="_blank">framework</a> 为多个 Maven Module，按照 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework/yudao-spring-boot-starter-web" target="_blank">Web</a>、<a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework/yudao-spring-boot-starter-security" target="_blank">Security</a>、<a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework/yudao-spring-boot-starter-mybatis" target="_blank">MyBatis</a>、<a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework/yudao-spring-boot-starter-redis" target="_blank">Redis</a> 等不同组件，进行封装与拓展。</li> 
 <li>基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjunit.org%2Fjunit5%2F" target="_blank">JUnit5</a> 与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmockito%2Fmockito" target="_blank">Mockito</a>，实现单元测试，保证功能的正确性，与代码的可维护性。一直自动化，一直爽！</li> 
 <li>增加 SpringBoot 多环境的配置文件，提供完善的 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/bin/deploy.sh" target="_blank">deploy.sh</a> 部署脚本，以及 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F6942098287533129765" target="_blank">Jenkins 部署教程</a>。</li> 
 <li>优化 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework/yudao-spring-boot-starter-security" target="_blank">Spring Security</a> 实现权限的代码，提升可读性和维护性。</li> 
 <li>增加本地缓存（菜单、角色、数据字典等等），提升性能。通过 Redis 订阅发布，实现缓存的实时刷新。</li> 
 <li>增加 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/system/controller/auth/vo" target="_blank">VO</a> 类，作为 API 接口的响应对象，避免数据库实体与前端的直接耦合。</li> 
 <li>优化 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/src/main/java/cn/iocoder/dashboard/framework/logger/operatelog" target="_blank">操作日志</a>，支持读取 Swagger 作为日志的内容。</li> 
 <li>优化 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/src/main/java/cn/iocoder/dashboard/framework/quartz" target="_blank">定时任务</a>，支持执行失败的重试，更完善的执行日志。</li> 
 <li>优化 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/tool/service/codegen" target="_blank">codegen</a> 代码生成器，在原先生成 Controller、Service、Mapper、数据库实体、Vue 代码的基础上，额外生成 VO、单元测试的代码。</li> 
 <li>调整文件改用 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/infra/dal/dataobject/file/InfFileDO.java" target="_blank">数据库</a> 存储，而不是文件系统。原因是，项目在部署多个服务节点时，文件需要做同步。未来，会增加 aliyun、七牛云等存储云服务。</li> 
 <li>去除原有数据库的连表查询、递归查询，改为单表操作的方式，多次读取 + 内存拼接。</li> 
 <li>优化 Java 代码的格式，解决 IDEA 代码告警的问题。</li> 
</ul> 
<h3 style="text-align:start">后台功能的新增</h3> 
<ul> 
 <li>增加 API <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/infra/dal/dataobject/logger/InfApiAccessLogDO.java" target="_blank">访问</a>与<a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/infra/dal/dataobject/logger/InfApiErrorLogDO.java" target="_blank">异常</a>日志，方便排查线上 API 的问题。</li> 
 <li>增加 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/system/dal/dataobject/errorcode/SysErrorCodeDO.java" target="_blank">全局错误码</a>，统一业务异常的管理。管理后台会支持错误码的管理，支持提示文案的可配置化。</li> 
 <li>增加 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-admin-server/src/main/java/cn/iocoder/yudao/adminserver/modules/system/service/sms" target="_blank">短信模块</a>，提供短信渠道、短息模板、短信日志的管理，对接 aliyun、云片等主流短信平台。</li> 
 <li>增加 Redis <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/yudao-framework/yudao-spring-boot-starter-redis/src/main/java/cn/iocoder/yudao/framework/redis/core/RedisKeyDefine.java" target="_blank">Key</a> 的管理，知道项目中使用到的 Redis Key 的格式、数据类型、过期时间、描述等等信息。</li> 
</ul> 
<h3 style="text-align:start">技术选型的调整</h3> 
<ul> 
 <li>将 Spring Boot 版本，从 2.1.3 升级到 2.4.5 最新。</li> 
 <li>增加 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/yudao-dependencies/pom.xml" target="_blank">bom</a> 文件，统一 Maven 的依赖管理。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2F" target="_blank">MyBatis Plus</a> 组件，简化 MyBatis 使用，提升开发效率。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson" target="_blank">Redisson</a> 组件，作为 Redis 的客户端，提供更强大的 Redis 操作。</li> 
 <li>基于 Redis 实现分布式消息队列的功能。接入 Redis <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Fpubsub" target="_blank">Pub/Sub</a> 实现广播消费，接入 Redis <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Fstreams-intro" target="_blank">Stream</a> 实现集群消费。</li> 
 <li>去除 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson" target="_blank">fastjson</a>，统一使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jackson.com%2F" target="_blank">Jackson</a> 作为 JSON 库，老爆安全漏洞的悲伤。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmapstruct.org%2F" target="_blank">MapStruct</a> 组件，实现数据库实体与 VO 类之间的转换。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprojectlombok.org%2F" target="_blank">Lombok</a> 组件，生成 setter、getter 等常用方法，去除冗余代码。</li> 
 <li>引入 Spring <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.iocoder.cn%2FSpring-Boot%2FAsync-Job%2F%3Foschina" target="_blank">Async</a> 功能，实现异步任务。例如说，异步记录 API 访问日志、管理员操作日志等等。</li> 
 <li>魔改 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fctripcorp%2Fapollo" target="_blank">Apollo</a> 组件，接入本地数据库，实现内嵌的配置中心。通俗的说，我们可以将原本添加到 <code>application.yaml</code> 的配置项，改为添加到数据库中，项目启动会进行读取。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhutool" target="_blank">Hutool</a> 组件，去除大量重复的工具类，也避免原本 Util 存在一些 bug 的问题。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpingfangushi%2Fscrew" target="_blank">Screw</a> 组件，实现数据库文档的生成，虽然好像现在用途较少。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Feasyexcel" target="_blank">EasyExcel</a>，提供 Excel 的导入与导出的功能。</li> 
 <li>实现 <a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-framework/yudao-spring-boot-starter-protection/src/main/java/cn/iocoder/yudao/framework/idempotent" target="_blank">Idempotent</a> 组件，实现幂等的功能，可以用来解决 HTTP 重复请求的问题。</li> 
 <li>引入 <a href="https://gitee.com/baomidou/lock4j" target="_blank">Lock4J</a>，实现声明式的分布式锁的功能。虽然 Redisson 内置了分布式锁的功能，但是通过注解声明一个 <code>@Lock4j</code> 注解的使用方式，更加便利，且满足绝大多数场景。</li> 
 <li>去除原有的服务监控，使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcodecentric%2Fspring-boot-admin" target="_blank">SpringBoot Admin</a> 替代，提供更完整的监控能力。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fskywalking" target="_blank">SkyWalking</a> 组件，实现链路追踪和日志服务的功能。通过链路追踪，我们可以看到一个 API 请求涉及到的 MySQL、Redis 等操作；通过日志服务，我们可以方便的看到每个服务实例的日志。</li> 
 <li>引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fquartz-scheduler" target="_blank">Resilience4j</a> 组件，实现限流、熔断等功能，保证服务的稳定性。</li> 
 <li>引入 <a href="https://gitee.com/xiaoym/knife4j" target="_blank">Knife4j</a>，美化接口文档。原本所有 API 接口文档是缺失的，已经全部补全，可见 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fapi-dashboard.yudao.iocoder.cn%2Fdoc.html" target="_blank">http://api-dashboard.yudao.iocoder.cn/doc.html</a> 地址。</li> 
</ul>
                                        </div>
                                      
</div>
            