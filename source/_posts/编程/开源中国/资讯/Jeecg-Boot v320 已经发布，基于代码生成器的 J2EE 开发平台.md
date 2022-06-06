
---
title: 'Jeecg-Boot v3.2.0 已经发布，基于代码生成器的 J2EE 开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
author: 开源中国
comments: false
date: Sat, 04 Jun 2022 22:33:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jeecg-Boot v3.2.0 已经发布，基于代码生成器的 J2EE 开发平台</p> 
<p>此版本更新内容包括：</p> 
<h3>项目介绍</h3> 
<blockquote> 
 <p>JeecgBoot是一款企业级的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p><strong>当前版本</strong>：v3.2.0 | 2022-04-25</p> 
<h3>源码下载</h3> 
<ul> 
 <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot" target="_blank">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3>技术文档</h3> 
<ul> 
 <li>官方网站： <a href="https://gitee.com/link?target=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>技术文档： <a href="https://gitee.com/link?target=http%3A%2F%2Fdoc.jeecg.com" target="_blank">http://doc.jeecg.com</a></li> 
 <li>在线演示： <a href="https://gitee.com/link?target=http%3A%2F%2Fboot.jeecg.com" target="_blank">http://boot.jeecg.com</a></li> 
 <li>新手入门： <a href="https://gitee.com/link?target=http%3A%2F%2Fjeecg.com%2Fdoc%2Fquickstart" target="_blank">http://jeecg.com/doc/quickstart</a></li> 
</ul> 
<h3>升级日志</h3> 
<blockquote> 
 <p>此版本重构很大，重点升级了SpringBoot、SpringCloudAlibaba、MybatisPlus到最新版、重构了微服务模块，同时针对代码做了规范优化。</p> 
</blockquote> 
<h4>重点升级</h4> 
<ul> 
 <li>升级springboot 2.6.6</li> 
 <li>升级spring-cloud-alibaba 2021.1</li> 
 <li>升级mybatisplus 3.5.1</li> 
 <li>重构sentinel模块，支持持久化到nacos</li> 
 <li>重构gateway模块，熔断限流降级切换为sentinel</li> 
 <li>代码规范大重构</li> 
 <li>解决代码生成器不支持路径含中文或空格问题</li> 
</ul> 
<h4>解决微服务bug</h4> 
<ul> 
 <li>gateway，在网关路由页面如何设置路由条件Header <a href="https://gitee.com/jeecg/jeecg-boot/issues/I52J6R" target="_blank">issues/I52J6R</a></li> 
 <li>网关刷新问题<a href="https://gitee.com/jeecg/jeecg-boot/issues/I442RS" target="_blank">#I442RS</a></li> 
 <li>微服务下Knife4j每次重新部署jar时，都要重启gateway服务才能显示成功<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3185" target="_blank">#3185</a></li> 
 <li>微服务版，定时任务中，通过openfeign调用其他服务，报错tocken失效<a href="https://gitee.com/jeecg/jeecg-boot/issues/I523YP" target="_blank">#I523YP</a></li> 
 <li>微服务之间的feign调用，如何免登录，同时又不会被暴露网关<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4Z69G" target="_blank">#I4Z69G</a></li> 
 <li>微服务框架下的定时任务和字典项查询无权限<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2662" target="_blank">#2662</a></li> 
 <li>异步线程中调用openFeign访问远程服务，子线程的header中偶尔出现取不到token的情况<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4Q7FY" target="_blank">#I4Q7FY</a></li> 
 <li>微服务都是在内网环境中，只有网关会暴露公网,服务调用不鉴权<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2539" target="_blank">#2539</a></li> 
 <li>切换微服后,被调用服务要求鉴权怎么办<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2171" target="_blank">#2171</a></li> 
 <li>微服务 springcloud版本漏洞<a href="https://gitee.com/jeecg/jeecg-boot/issues/I52U2F" target="_blank">#I52U2F</a></li> 
</ul> 
<h4>Issues处理</h4> 
<ul> 
 <li>代码生成列表页面的图片支持点击放大预览功能</li> 
 <li>【安全机制加强】字典接口、online报表等敏感接口加字段限制 AbstractQueryBlackListHandler</li> 
 <li>敏感操作加操作日志，便于追踪</li> 
 <li>swagger接口返回值，显示的是object问题代码调整</li> 
 <li>poi导入问题<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4PU45" target="_blank">#I4PU45</a></li> 
 <li>查询条件的值为等号= bug<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3443" target="_blank">#3443</a></li> 
 <li>当搜索框里只输入 * 时，后台索引越界<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3382" target="_blank">#3382</a></li> 
 <li>分子字典树前端代码生成错误<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4SKUS" target="_blank">#I4SKUS</a></li> 
 <li>java 增强导入类异常<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3479" target="_blank">#3479</a></li> 
 <li>订单流水号<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4W3XN" target="_blank">#I4W3XN</a></li> 
 <li>代码生成app页面没有此js<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4WFGF" target="_blank">#I4WFGF</a></li> 
 <li>3.1版本 online表单Datetime通过日期查询报错<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3489" target="_blank">#3489</a></li> 
 <li>Shiro安全漏洞提示<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3498" target="_blank">#3498</a></li> 
 <li>浏览器显示乱码问题<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4YH95" target="_blank">#I4YH95</a></li> 
 <li>/sys/user/list接口使用部门departId查询用户时没有权限报错<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4XTYB" target="_blank">#I4XTYB</a></li> 
 <li>模板管理发送消息出现NullPointerException错误<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3512" target="_blank">#3512</a></li> 
 <li>刷新页面redis中原有token未过期时会创建一个新token存放至redis中<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4YY7I" target="_blank">#I4YY7I</a></li> 
 <li>国产数据库适配异常<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3543" target="_blank">#3543</a></li> 
 <li>启动项目在bean初始化之前,报了警告多个PropertySourcesPlaceholderConfigurer重复注入<a href="https://gitee.com/jeecg/jeecg-boot/issues/I50IJ6" target="_blank">#I50IJ6</a></li> 
 <li>service调用service，代码逻辑缺陷<a href="https://gitee.com/jeecg/jeecg-boot/issues/I52JSM" target="_blank">#I52JSM</a></li> 
 <li>Nacos 1.4.1 依然存在权限绕过的漏洞<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3507" target="_blank">#3507</a></li> 
 <li>启动报错：Cannot resolve com.sun:tools:1.8.0<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3596" target="_blank">#3596</a></li> 
 <li>升级springboot2.6后不支持达梦数据库<a href="https://gitee.com/jeecg/jeecg-boot/issues/I52KAU" target="_blank">#I52KAU</a></li> 
 <li>微信扫码登录，绑定未验证手机验证码，存在安全隐患<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3555" target="_blank">#3555</a></li> 
 <li>vue2代码生成的vue3代码中，data.ts文件里，componentProps后面少一个逗号<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I4ZRF3" target="_blank">#I4ZRF3</a></li> 
</ul> 
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
<h3>系统功能模块</h3> 
<div> 
 <pre><code>├─系统管理
│  ├─用户管理
│  ├─角色管理
│  ├─菜单管理
│  ├─权限设置（支持按钮权限、数据权限）
│  ├─表单权限（控制字段禁用、隐藏）
│  ├─部门管理
│  ├─我的部门（二级管理员）
│  └─字典管理
│  └─分类字典
│  └─系统公告
│  └─职务管理
│  └─通讯录
│  └─多租户管理
├─Online在线开发(低代码)
│  ├─Online在线表单 - 功能已开放
│  ├─Online代码生成器 - 功能已开放
│  ├─Online在线报表 - 功能已开放
│  ├─Online在线图表(暂不开源)
│  ├─Online图表模板配置(暂不开源)
│  ├─Online布局设计(暂不开源)
│  ├─多数据源管理 - 功能已开放
├─积木报表设计器(低代码)
│  ├─打印设计器 - 功能已开放
│  ├─数据报表设计 - 功能已开放
│  ├─图形报表设计(支持Echart) - 功能已开放
│  ├─大屏设计器(暂不开源)
├─消息中心
│  ├─消息管理
│  ├─模板管理
├─代码生成器(低代码)
│  ├─代码生成器功能（一键生成前后端代码，生成后无需修改直接用，绝对是后端开发福音）
│  ├─代码生成器模板（提供4套模板，分别支持单表和一对多模型，不同风格选择）
│  ├─代码生成器模板（生成代码，自带excel导入导出）
│  ├─查询过滤器（查询逻辑无需编码，系统根据页面配置自动生成）
│  ├─高级查询器（弹窗自动组合查询条件）
│  ├─Excel导入导出工具集成（支持单表，一对多 导入导出）
│  ├─平台移动自适应支持
├─系统监控
│  ├─Gateway路由网关
│  ├─性能扫描监控
│  │  ├─监控 Redis
│  │  ├─Tomcat
│  │  ├─jvm
│  │  ├─服务器信息
│  │  ├─请求追踪
│  │  ├─磁盘监控
│  ├─定时任务
│  ├─系统日志
│  ├─消息中心（支持短信、邮件、微信推送等等）
│  ├─数据日志（记录数据快照，可对比快照，查看数据变更情况）
│  ├─系统通知
│  ├─SQL监控
│  ├─swagger-ui(在线接口文档)
│─报表示例
│  ├─曲线图
│  └─饼状图
│  └─柱状图
│  └─折线图
│  └─面积图
│  └─雷达图
│  └─仪表图
│  └─进度条
│  └─排名列表
│  └─等等
│─大屏模板
│  ├─作战指挥中心大屏
│  └─物流服务中心大屏
│─常用示例
│  ├─自定义组件
│  ├─对象存储(对接阿里云)
│  ├─JVXETable示例（各种复杂ERP布局示例）
│  ├─单表模型例子
│  └─一对多模型例子
│  └─打印例子
│  └─一对多TAB例子
│  └─内嵌table例子
│  └─常用选择组件
│  └─异步树table
│  └─接口模拟测试
│  └─表格合计示例
│  └─异步树列表示例
│  └─一对多JEditable
│  └─JEditable组件示例
│  └─图片拖拽排序
│  └─图片翻页
│  └─图片预览
│  └─PDF预览
│  └─分屏功能
│─封装通用组件
│  ├─行编辑表格JEditableTable
│  └─省略显示组件
│  └─时间控件
│  └─高级查询
│  └─用户选择组件
│  └─报表组件封装
│  └─字典组件
│  └─下拉多选组件
│  └─选人组件
│  └─选部门组件
│  └─通过部门选人组件
│  └─封装曲线、柱状图、饼状图、折线图等等报表的组件（经过封装，使用简单）
│  └─在线code编辑器
│  └─上传文件组件
│  └─验证码组件
│  └─树列表组件
│  └─表单禁用组件
│  └─等等
│─更多页面模板
│  ├─各种高级表单
│  ├─各种列表效果
│  └─结果页面
│  └─异常页面
│  └─个人页面
├─高级功能
│  ├─系统编码规则
│  ├─提供单点登录CAS集成方案
│  ├─提供APP发布方案
│  ├─集成Websocket消息通知机制
│─流程模块功能 (暂不开源)
│  ├─流程设计器
│  ├─在线表单设计
│  └─我的任务
│  └─历史流程
│  └─历史流程
│  └─流程实例管理
│  └─流程监听管理
│  └─流程表达式
│  └─我发起的流程
│  └─我的抄送
│  └─流程委派、抄送、跳转
│  └─。。。
└─其他模块
   └─更多功能开发中。。
</code></pre> 
 <div>
   
 </div> 
</div> 
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
<p>详情查看：<a href="https://gitee.com/jeecg/jeecg-boot/releases/v3.2.0">https://gitee.com/jeecg/jeecg-boot/releases/v3.2.0</a></p>
                                        </div>
                                      
</div>
            