
---
title: 'ballcat v0.6.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2361'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 10:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2361'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start">[0.6.0] 2021-01-20</h2> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ballcat.cn%2Fguide%2FCHANGELOG.html%23warning" target="_blank">#</a>⚠️ Warning</h3> 
<ul> 
 <li>Swagger2 相关注解迁移到 OpenAPI3，由于使用了 springdoc-openapi，且该项目当前版本的一些问题，如果没有在 服务中引入<span> </span><strong>springdoc-openapi-ui</strong><span> </span>的依赖，或者配置中添加<span> </span><code>springdoc.api-docs.enabled=false</code><span> </span>的配置，则会导致启动报错</li> 
 <li>删除了 knife4j-ui 的版本管理，对于 OpenAPI3，请使用 knife4j 的 3.x 版本</li> 
 <li>springfox 组件未适配 springboot 2.6.2 版本，如需继续使用 springfox，请添加<span> </span><code>spring.mvc.pathmatch.matching-strategy=ant-path-matcher</code><span> </span>配置，以及注册<span> </span><code>SpringfoxHandlerProviderBeanPostProcessor</code><span> </span>到 spring 容器中</li> 
 <li>springboot 2.6.x 默认禁止循环依赖，如有循环依赖启动将会报错，请注意修改代码，或者添加配置<span> </span><code>spring.main.allow-circular-references = true<span> </span></code>(不建议)</li> 
 <li><code>IPageArgumentResolver</code><span> </span>移除，如果直接使用 mybatisPlus 的 IPage 做为查询入参会有 SQL 注入风险，请注意修改！！！</li> 
 <li><code>IPageArgumentResolver</code><span> </span>移除，如果直接使用 mybatisPlus 的 IPage 做为查询入参会有 SQL 注入风险，请注意修改！！！</li> 
 <li><code>IPageArgumentResolver</code><span> </span>移除，如果直接使用 mybatisPlus 的 IPage 做为查询入参会有 SQL 注入风险，请注意修改！！！</li> 
</ul> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ballcat.cn%2Fguide%2FCHANGELOG.html%23%25E2%25AD%2590-new-features" target="_blank">#</a>⭐ New Features</h3> 
<ul> 
 <li>【修改】修改 jackson 脱敏支持的模块添加方式，使用为注册<span> </span><code>JsonDesensitizeModule</code><span> </span>的形式，以便复用 spring-boot 默认的 module 注册。</li> 
 <li>【修改】调整<span> </span><code>CustomJavaTimeModule</code><span> </span>的注册方式，防止被 JSR310 的<span> </span><code>JavaTimeModule</code><span> </span>覆盖</li> 
 <li>【删除】移除过时已久的<span> </span><code>IPageArgumentResolver</code>，让 starter-web 和 mybatis-plus 模块解耦。</li> 
 <li>【删除】移除过时的 Lov 相关代码。</li> 
 <li>【修改】Swagger2 相关注解迁移到 OpenAPI3</li> 
 <li>【修改】文档底层支持从 springfox 迁移到 springdoc-openapi</li> 
 <li>【添加】对于 GET 请求的入参封装类，如 xxQO，添加<span> </span><code>@ParameterObject</code><span> </span>注解，以便在文档上正确展示查询入参</li> 
 <li>【修改】由于 springfox 长久不更新，弃用基于该框架的<span> </span><strong>ballcat-spring-boot-starter-swagger</strong><span> </span>组件</li> 
 <li>【新增】添加<span> </span><strong>ballcat-extend-openapi</strong>，模块，基于 springdoc-openapi 做了部分扩展，参看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ballcat.cn%2Fguide%2Ffeature%2Fopenapi.html" target="_blank">文档<span><span>open in new window</span></span></a></li> 
 <li>【删除】删除 knife4j-ui 的版本管理</li> 
 <li>【修改】代码优化，显示指定部分参数或返回值的泛型</li> 
 <li>【修改】Sonarlint 部分代码警告处理</li> 
 <li>【删除】移除 dependencies pom 中无用的 pluginManagement 部分</li> 
 <li>【修改】hutool 依赖管理改为使用 hutool 官方提供的 bom</li> 
 <li>【新增】添加<span> </span><strong>ballcat-extend-tesseract</strong><span> </span>扩展模块，用于 OCR 文字识别工具的调用封装</li> 
 <li>【修改】字典相关逻辑调整 
  <ul> 
   <li>去除字典只读/可写的属性控制</li> 
   <li>字典项增加启用/禁用的状态属性</li> 
   <li>字典现在在有字典项的情况下不允许删除（之前会自动级联删除）</li> 
  </ul> </li> 
 <li>【修改】同步 mybtais-plus 升级 3.5.x 后，AbstractMethod 的方法名获取做的调整</li> 
 <li>【修改】<strong>ballcat-spring-boot-starter-oss</strong><span> </span>更新 oss 相关方法与变量. 由 path 变为 key. 符合 oss 规范，原 rootPath 属性标记为过期，修改为 objectKeyPrefix</li> 
 <li>【添加】<strong>ballcat-spring-boot-starter-oss</strong><span> </span>新增根据<span> </span><code>File</code><span> </span>直接上传的方法</li> 
 <li>【修改】<code>StreamUtils</code><span> </span>克隆流方法优化. 使用 FileOutStream 保证不会因为文件过大而内存溢出</li> 
 <li>【修改】<code>OssDisabledException</code><span> </span>父类由<span> </span><code>Exception</code><span> </span>修改为<span> </span><code>RuntimeException</code></li> 
 <li>【修改】<strong>ballcat-common-idempotent</strong><span> </span>幂等组件微调 
  <ul> 
   <li><code>RedisIdempotentKeyStore</code><span> </span>的 stringRedisTemplate 属性，改为构造器注入</li> 
   <li>取消<span> </span><code>IdempotentAspect</code><span> </span>切面的 @Component 注解，防止误注册</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ballcat.cn%2Fguide%2FCHANGELOG.html%23%25F0%259F%2590%259E-bug-fixes" target="_blank">#</a>🐞 Bug Fixes</h3> 
<ul> 
 <li>【修复】修复删除字典项时没有将变动通知到前端的问题</li> 
 <li>【修复】修复<span> </span><code>FileUtils#updateTmpDir</code><span> </span>方法中文件夹创建异常的问题</li> 
</ul> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ballcat.cn%2Fguide%2FCHANGELOG.html%23%25F0%259F%2594%25A8-dependency-upgrades" target="_blank">#</a>🔨 Dependency Upgrades</h3> 
<ul> 
 <li>【升级】spring-boot from 2.5.6 to 2.6.2</li> 
 <li>【升级】lombok from 1.18.20 to 1.18.22</li> 
 <li>【升级】spring-javaformat from 0.0.28 to 0.0.29</li> 
 <li>【升级】hutool from 5.7.12 to 5.7.19</li> 
 <li>【升级】dynamic-datasource from 3.4.1 to 3.5.0</li> 
 <li>【升级】jasypt from 3.0.3 to 3.0.4</li> 
 <li>【升级】jsoup from 1.14.2 to 1.14.3</li> 
 <li>【升级】mybatis-plus from 3.4.3.4 to 3.5.0</li> 
 <li>【升级】mybatis from 3.5.7 to 3.5.9</li> 
 <li>【升级】jsqlparse from 4.2 to 4.3</li> 
 <li>【升级】fastjson from 1.2.76 to 1.2.79</li> 
 <li>【升级】spring-boot-admin from 2.5.4 to 2.6.0</li> 
</ul>
                                        </div>
                                      
</div>
            