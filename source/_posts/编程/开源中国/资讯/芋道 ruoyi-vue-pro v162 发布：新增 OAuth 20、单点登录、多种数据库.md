
---
title: '芋道 ruoyi-vue-pro v1.6.2 发布：新增 OAuth 2.0、单点登录、多种数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3663'
author: 开源中国
comments: false
date: Fri, 10 Jun 2022 09:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3663'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目地址</span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>严肃声明：现在、未来都不会有商业版本，所有功能全部开源！</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>拒绝虚假开源，售卖商业版，程序员不骗程序员！！</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>「我喜欢写代码，乐此不疲」</strong><br> <strong>「我喜欢做开源，以此为乐」</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">🐯<span style="color:#e74c3c"><span style="background-color:#ffffff">项目介绍</span></span></h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>芋道</strong>，一套<strong>全部开源</strong>的<strong>企业级</strong>的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有任何问题，或者想要的功能，可以在<span> </span><em>Issues</em><span> </span>中提给艿艿。</p> 
</blockquote> 
<ul> 
 <li>前端采用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin">vue-element-admin</a><span> </span>，正在支持 Vue 3 + ElementUI Plus 最新方案。</li> 
 <li>后端采用 Spring Boot、MySQL + MyBatis Plus、Redis + Redisson。</li> 
 <li>数据库可使用 MySQL、Oracle、PostgreSQL、SQL Server、MariaDB、国产达梦 DM、TiDB 等</li> 
 <li>权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统。</li> 
 <li>支持加载动态权限菜单，按钮级别权限控制，本地缓存提升性能。</li> 
 <li>支持 SaaS 多租户系统，可自定义每个租户的权限，提供透明化的多租户底层封装。</li> 
 <li>工作流使用 Activiti + Flowable，支持动态表单、在线设计流程、多种任务分配方式。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码 + 单元测试 + Swagger 接口文档 + Validator 参数校验。</li> 
 <li>集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款。</li> 
 <li>集成阿里云、腾讯云、云片等短信渠道，集成 MinIO、阿里云、腾讯云、七牛云等云存储服务。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🐶在线体验</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdashboard.yudao.iocoder.cn">http://dashboard.yudao.iocoder.cn</a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>账号密码：admin/admin123</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">更新说明</span></span></h1> 
<h3 style="text-align:start">📈<span> </span>Statistic</h3> 
<ul> 
 <li>总代码行数：84846</li> 
 <li>源码代码行数：52792</li> 
 <li>注释行数：19234</li> 
 <li>单元测试用例数：671</li> 
</ul> 
<h3 style="text-align:start">⭐<span> </span>New Features</h3> 
<ul> 
 <li>【新增】对 PostgreSQL 数据库的支持<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/151">#151</a><span> </span>感谢这个过程中怪物的帮助！</li> 
 <li>【新增】对 Oracle 数据库的支持<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/152">#152</a><span> </span>感谢这个过程中<span> </span><a href="https://gitee.com/anzhen-tech">安贞</a>、品霖的帮助！</li> 
 <li>【新增】对 SQL Server 数据库的支持<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/153">#153</a><span> </span>感谢这个过程中 Simon、蜉蝣无垠、牛希尧的帮助！</li> 
 <li>【新增】《开发指南 —— 后端手册》的接口文档、三方登录、异常处理（错误码）、参数校验、分页实现、系统日志、数据库 MyBatis、多数据源、缓存 Redis、本地缓存、定时任务、消息队列、配置中心、单元测试、分布式锁、幂等性、限流熔断、数据库文档、短信配置、开发环境...</li> 
 <li>【新增】《开发指南 —— 运维手册》的开发环境、Linux 部署、Docker 部署、Jenkins 部署、HTTPS 证书、服务监控...</li> 
 <li>【新增】《开发指南 —— 前端手册》的开发规范、菜单路由、Icon 图标、字典数据、系统组件、通用方法、配置读取...</li> 
 <li>【新增】手机验证码登录，美化登录界面，由<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/155">#155</a><span> </span>贡献</li> 
 <li>【新增】一键改包的程序，快速将项目的 Maven、包名等信息替换成你的<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/110">#110</a></li> 
 <li>【新增】菜单新增是否缓存、是否隐藏的字段<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/133">#133</a><span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/172">#172</a></li> 
 <li>【新增】Spring Cache 声明式缓存，使用 Redis 存储<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fcommit%2F49b906bbfe27b31ce52bfe7403740ff5b335462e" target="_blank">code</a></li> 
 <li>【新增】腾讯云短信，由<span> </span><a href="https://gitee.com/swpthebest">swpthebest</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/118">#118</a></li> 
 <li>【新增】敏感词，由<span> </span><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ajxndtb689684aver" target="_blank">dachuan</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/121">#121</a></li> 
 <li>【新增】数据源配置，为多租户、代码生成支持动态数据源做准备<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/138">#138</a></li> 
 <li>【新增】用户 Token 采用 OAuth2.0 的 Access Token + Refresh Token，提升安全性<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/166">#166</a></li> 
 <li>【新增】基于 OAuth2.0 实现 SSO 单点登录<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/176">#176</a></li> 
 <li>【新增】用户与岗位的关联表，由<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/113">anzhen-tech</a><span> </span>贡献<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/113">#113</a></li> 
 <li>【新增】MyBatis 字段的加解密功能<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/0ae9af04927fa3a161789e58037915537f8d2f5e">code</a></li> 
 <li>【新增】集成微信 Native、小程序的支付能力，支持 v2 和 v3 的回调数据处理<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/142">#142</a></li> 
 <li>【优化】yudao-module-xx-impl 调整成 yudao-module-xx-biz，更加符合定位<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/09103f310b6f3a0cdc8ab61f62d765cb4777f0ea">code</a></li> 
 <li>【优化】简化三方登录的实现，降低理解成本<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/137">#137</a></li> 
 <li>【优化】去除<span> </span><code>yudao-module-system</code>、<code>yudao-module-infra</code><span> </span>对<span> </span><code>yudao-module-member</code><span> </span>的依赖<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/122">#122</a></li> 
 <li>【优化】<code>yudao-framework-test</code><span> </span>测试组件的封装，内置 Redis、DB 等多种快速测试的基类<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fcommit%2Fd60be0bb53431856ed2574379f3cf1162d2bf4a5" target="_blank">code</a></li> 
 <li>【优化】配置指定默认的 npm 镜像源<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/170/files">#170</a></li> 
 <li>【优化】字典管理、通知管理、岗位管理、角色管理、错误码管理的排序显示<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/174">#174</a></li> 
 <li>【优化】前端 Token、账号、密码等信息，统一使用 LocalStorage 替代 Cookie 存储<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/d322e781998efb424ede22d31793b56ba264a0dd">code</a></li> 
 <li>【优化】上传文件的类型识别，增加基于 filename 的读取<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/86bb6f0b802c6596a5fb3ead8548e55309175a45">code</a></li> 
</ul> 
<h3 style="text-align:start">🐞<span> </span>Bug Fixes</h3> 
<ul> 
 <li>【修复】角色菜单集合复选框回显不正确<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/107">#107</a></li> 
 <li>【修复】工作流 BPMN 图的 canvas 自适应，解决展示补全的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/104">#104</a></li> 
 <li>【修复】API 访问日志不记录的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fcommit%2F0547671c9e6d406ecf211845cd38df75824f407c" target="_blank">code</a></li> 
 <li>【修复】修复忽略租户的 URL，未带租户会报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/9b687ff6c9eb945f29c2728704841e9443a01108">code</a></li> 
 <li>【修复】菜单无法使用外链的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/6e404697353ccc4c2c7e797e4da7d41098d59c96">code</a></li> 
 <li>【修复】代码生成器的 vue 模板中，导出 Excel 文件时，文件名未格式化的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fpull%2F133" target="_blank">#133</a></li> 
 <li>【修复】代码生成时，对话框的日期选择器，在编辑情况下不能回显<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/135/files">#135</a></li> 
 <li>【修复】在 Windows 下 ftp 上传和下载存在报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/156/files">#156</a></li> 
 <li>【修复】图片上传组件 ImageUpload 上传报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/63e632ceb7c9df92b406017b16039a83ee3e9218">code</a></li> 
 <li>【修复】文件上传组件 FileUpload 上传报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/1f36af8e6a3c8a3b5f274df7180b075bb268254f">code</a></li> 
 <li>【修复】form generator 组件上传文件、图片报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/c410240ed545374375c6073e3f74ddf39ad41878">code</a></li> 
 <li>【修复】富文本编辑器的 Editor 的图片上传报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/b6cb6469f1fefb083e3c0134c0217ea14dcd7495">code</a></li> 
 <li>【修复】DO 生成模板，当主键是 String 类型，模板有误<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/167">#167</a></li> 
 <li>【修复】创建用户不分配角色的情况会存在空指针<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/171">#171</a></li> 
 <li>【修复】yudao-ui-admin 启动告警<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/173">#173</a></li> 
 <li>【修复】新建的用户未分配角色时，操作自己信息回报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/30fbfb61432e254305d447802cc5e85d9c63c861">code</a></li> 
 <li>【修复】工作流的编辑无法撤回、crtl 选中的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/325a8d0a6e55b33189685f5e8cdbc960d8d86994">code</a></li> 
 <li>【修复】支付宝通知回调 BUG 修复<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/142">#142</a></li> 
</ul> 
<h3 style="text-align:start">🔨<span> </span>Dependency Upgrades</h3> 
<ul> 
 <li>【升级】spring-boot from 2.5.10 to 2.6.8 ：修复 RCE 漏洞，并且 2.5.X 结束声明周期</li> 
 <li>【升级】redisson from 3.16.6 to 3.17.3 ：提升 Redisson 客户端的稳定性</li> 
 <li>【升级】mysql-connector-java from 5.1.46 to 8.0.28 ：提升 MySQL 客户端的性能</li> 
 <li>【升级】Knife4j from from 3.0.2 to 3.0.3</li> 
 <li>【升级】swagger-annotations from 1.5.22 to 1.6.6</li> 
 <li>【升级】spring-boot-admin from 2.6.2 to 2.6.7</li> 
 <li>【升级】fastjson from 1.2.73 to 2.0.5</li> 
 <li>【升级】resilience4j from 1.7.0 to 1.7.1</li> 
 <li>【升级】jackson from 2.12.6 to 2.13.3</li> 
 <li>【升级】spring-mvc from 5.3.16 to 5.3.20</li> 
 <li>【升级】spring-security from 5.5.5 to 5.6.5</li> 
 <li>【升级】hibernate-validator from 6.2.2 to 6.2.3</li> 
 <li>【升级】junit from 5.7.2 to 5.8.2</li> 
 <li>【升级】mockito from 3.9.0 to 4.0.0</li> 
 <li>【升级】mybatis-plus from 3.4.3.4 to 3.5.2</li> 
</ul>
                                        </div>
                                      
</div>
            