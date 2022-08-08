
---
title: 'JeecgBoot 3.4.0 版本发布，微服务重构版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeecgos.oss-cn-beijing.aliyuncs.com/files/jeecgboot_springcloud2022.png'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 11:16:00 GMT
thumbnail: 'https://jeecgos.oss-cn-beijing.aliyuncs.com/files/jeecgboot_springcloud2022.png'
---

<div>   
<div class="content">
                                                                                            <h3>项目介绍</h3> 
<blockquote> 
 <p>JeecgBoot是一款企业级的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p><strong>当前版本</strong>：v3.4.0 | 2022-08-06</p> 
<h3>源码下载</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3>升级日志</h3> 
<blockquote> 
 <p>微服务重构专项升级，简化优化微服务架构，让微服务使用更加方便。</p> 
</blockquote> 
<h4>微服务重构内容</h4> 
<ul> 
 <li>升级<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fspring-cloud-alibaba%2Fblob%2F2021.x%2Fspring-cloud-alibaba-docs%2Fsrc%2Fmain%2Fasciidoc-zh%2Fsca-upgrade-guide.adoc" target="_blank">Spring Cloud Alibaba 2021.0.1.0</a>，使用 spring.config.import 方式引入nacos配置</li> 
 <li>拆分jeecg-boot-starter出来，使用独立项目维护 <a href="https://gitee.com/jeecg/jeecg-boot-starter">jeecg-boot-starter项目新地址</a></li> 
 <li>升级微服务3.4+版本对应文档</li> 
 <li>本次只升级后台版本号，暂时未更新前端</li> 
</ul> 
<h4>微服务文档更新</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F3040735" target="_blank">单体升级成微服务</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F3040736" target="_blank">使用archetype生成微服务模块</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F3040737" target="_blank">Docker镜像启动微服务项目</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F3041089" target="_blank">Gateway网关高级配置</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F2595023" target="_blank">分库分表ShardingSphere用法</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F3040798" target="_blank">微服务模块配置独立的数据源和Nacos配置</a></li> 
</ul> 
<h3>微服务技术栈</h3> 
<ul> 
 <li> <p>基础框架：Spring Boot 2.6.6</p> </li> 
 <li> <p>微服务框架： Spring Cloud Alibaba 2021.0.1.0</p> </li> 
 <li> <p>持久层框架：MybatisPlus 3.5.1</p> </li> 
 <li> <p>报表工具： JimuReport 1.5.2</p> </li> 
 <li> <p>安全框架：Apache Shiro 1.8.0，Jwt 3.11.0</p> </li> 
 <li> <p>微服务技术栈：Spring Cloud Alibaba、Nacos、Gateway、Sentinel、Skywalking</p> </li> 
 <li> <p>数据库连接池：阿里巴巴Druid 1.1.22</p> </li> 
 <li> <p>日志打印：logback</p> </li> 
 <li> <p>其他：autopoi, fastjson，poi，Swagger-ui，quartz, lombok（简化代码）等。</p> </li> 
</ul> 
<h3>微服务解决方案</h3> 
<p>1、服务注册和发现 Nacos</p> 
<p>2、统一配置中心 Nacos</p> 
<p>3、路由网关 gateway(三种加载方式)</p> 
<p>4、分布式 http feign</p> 
<p>5、熔断降级限流 Sentinel</p> 
<p>6、分布式文件 Minio、阿里OSS</p> 
<p>7、统一权限控制 JWT + Shiro</p> 
<p>8、服务监控 SpringBootAdmin</p> 
<p>9、链路跟踪 Skywalking <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzhangdaiscott%2Fjeecgcloud%2F1771670" target="_blank">参考文档</a></p> 
<p>10、消息中间件 RabbitMQ</p> 
<p>11、分布式任务 xxl-job</p> 
<p>12、分布式事务 Seata</p> 
<p>13、分布式日志 elk + kafka</p> 
<p>14、支持 docker-compose、k8s、jenkins</p> 
<p>15、CAS 单点登录</p> 
<p>16、路由限流</p> 
<h4>微服务架构图</h4> 
<p><img alt="微服务架构图" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/jeecgboot_springcloud2022.png" referrerpolicy="no-referrer"></p> 
<h3>Jeecg Boot 产品功能蓝图</h3> 
<p><img alt="功能蓝图" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/upload/test/Jeecg-Boot-lantu202005_1590912449914.jpg" referrerpolicy="no-referrer"></p> 
<h3>为什么选择 JeecgBoot?</h3> 
<blockquote> 
 <p>开源界“小普元”超越传统商业平台。引领低代码开发模式(OnlineCoding-> 代码生成器 -> 手工MERGE)，低代码开发同时又支持灵活编码， 可以帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高开发效率，节省成本，同时又不失灵活性。</p> 
</blockquote> 
<ul> 
 <li>采用最新主流前后分离框架（SpringBoot+Mybatis-plus+Ant-Design+Vue），容易上手; 代码生成器依赖性低,灵活的扩展能力，可灵活实现二次开发;</li> 
 <li>开发效率很高,采用代码生成器，单表数据模型和一对多(父子表)、树列表等数据模型，增删改查功能自动生成，菜单配置直接使用（前端代码和后端代码都一键生成）；</li> 
 <li>代码生成器提供强大模板机制，支持自定义模板风格。目前提供四套风格模板（单表两套、一对多两套）</li> 
 <li>封装完善的用户、角色、菜单、组织机构、数据字典、在线定时任务等基础功能。强大的权限机制，支持访问授权、按钮权限、数据权限、表单权限等</li> 
 <li>零代码在线开发能力，在线配置表单、在线配置报表、在线配置图表、在线设计表单</li> 
 <li>常用共通封装，各种工具类(定时任务,短信接口,邮件发送,Excel导入导出等),基本满足80%项目需求</li> 
 <li>简易Excel导入导出，支持单表导出和一对多表模式导出，生成的代码自带导入导出功能</li> 
 <li>集成简易报表工具，图像报表和数据导出非常方便，可极其方便的生成图形报表、pdf、excel、word等报表；</li> 
 <li>采用前后分离技术，页面UI精美，针对常用组件做了封装：时间、行表格控件、截取显示控件、报表组件，编辑器等等</li> 
 <li>查询过滤器：查询功能自动生成，后台动态拼SQL追加查询条件；支持多种匹配方式（全匹配/模糊查询/包含查询/不匹配查询）；</li> 
 <li>数据权限（精细化数据权限控制，控制到行级，列表级，表单字段级，实现不同人看不同数据，不同人对同一个页面操作不同字段</li> 
 <li>在线配置报表（无需编码，通过在线配置方式，实现曲线图，柱状图，数据等报表）</li> 
 <li>页面校验自动生成(必须输入、数字校验、金额校验、时间空间等);</li> 
 <li>提供单点登录CAS集成方案，项目中已经提供完善的对接代码</li> 
 <li>表单设计器，支持用户自定义表单布局，支持单表，一对多表单、支持select、radio、checkbox、textarea、date、popup、列表、宏等控件</li> 
 <li>专业接口对接机制，统一采用restful接口方式，集成swagger-ui在线接口文档，Jwt token安全验证，方便客户端对接</li> 
 <li>接口安全机制，可细化控制接口授权，非常简便实现不同客户端只看自己数据等控制</li> 
 <li>高级组合查询功能，在线配置支持主子表关联查询，可保存查询历史</li> 
 <li>提供各种系统监控，实时跟踪系统运行情况（监控 Redis、Tomcat、jvm、服务器信息、请求追踪、SQL监控）</li> 
 <li>消息中心（支持短信、邮件、微信推送等等）</li> 
 <li>集成Websocket消息通知机制</li> 
 <li>提供APP发布方案：</li> 
 <li>支持多语言，提供国际化方案；</li> 
 <li>数据变更记录日志，可记录数据每次变更内容，通过版本对比功能查看历史变化</li> 
 <li>平台UI强大，实现了移动自适应</li> 
 <li>平台首页风格，提供多种组合模式，支持自定义风格</li> 
 <li>提供简单易用的打印插件，支持谷歌、IE浏览器等各种浏览器</li> 
 <li>示例代码丰富，提供很多学习案例参考</li> 
 <li>采用maven分模块开发方式</li> 
 <li>支持菜单动态路由</li> 
 <li>权限控制采用 RBAC（Role-Based Access Control，基于角色的访问控制）</li> 
</ul> 
<h3>系统截图</h3> 
<p>PC端</p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/5a396adc1ff8f074082fa002b88b5915.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/69de4ca50e51c70b6e2f48a530be6eb3.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/df82289dcc7326cdf7adc073d4feab3a.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/b91d1ae6ff0177c728434150bc82a72a.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/5091f504924e235ca0d49196a686c643.png" referrerpolicy="no-referrer"></p> 
<p>手机端</p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/320e78580453295b47c97f1c31d0c050.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/0f607ab82712c1f240aa14827091e94e.png" referrerpolicy="no-referrer"></p> 
<p>PAD端</p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/0eba9d8fa3a4847599cfe940ff6a80d3.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/7debc83021006b8fdae7f65378fd6492.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/2cc9e7b01a99248033bd5da69802842f.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/62f5720f2fd20b43bdccfaeb469d4460.png" referrerpolicy="no-referrer"></p> 
<p>报表效果</p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/55d6dc8d7baef718d3032d6b6d1265ab.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/366b4070ca053dcbd267e0eaa2971950.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/f343d6821db09a2448baef238948a6ca.gif" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/4f5ffd3b8357185a0226b9c317bc2c55.png" referrerpolicy="no-referrer"></p> 
<p>大屏效果</p> 
<p><img alt src="https://img-blog.csdnimg.cn/img_convert/60ae64fe29fd6ec26d75a225389b53dd.png" referrerpolicy="no-referrer"></p> 
<p>欢迎吐槽，欢迎star~</p>
                                        </div>
                                      
</div>
            