
---
title: '芋道 ruoyi-vue-pro v1.4.0 发布：重构成多 Maven Module 的代码结构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2965'
author: 开源中国
comments: false
date: Mon, 07 Feb 2022 09:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2965'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目地址</span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目介绍</span></span></h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>芋道</strong>，一套<strong>全部开源</strong>的<strong>企业级</strong>的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有任何问题，或者想要的功能，可以在<span> </span><em>Issues</em><span> </span>中提给艿艿。</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端采用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin">vue-element-admin</a><span> </span>，正在支持 Vue 3 + ElementUI Plus 最新方案。</li> 
 <li>后端采用 Spring Boot、MySQL + MyBatis Plus、Redis + Redisson。</li> 
 <li>权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统。</li> 
 <li>支持加载动态权限菜单，按钮级别权限控制，本地缓存提升性能。</li> 
 <li>工作流使用 Activiti ，支持动态表单、在线设计流程、多种任务分配方式。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码 + 单元测试 + Swagger 接口文档 + Validator 参数校验。</li> 
 <li>集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款。</li> 
 <li>集成阿里云、腾讯云、云片等短信渠道，集成阿里云、腾讯云、七牛云等云存储服务。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">在线体验</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdashboard.yudao.iocoder.cn">http://dashboard.yudao.iocoder.cn</a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>账号密码：admin/admin123</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">更新说明</span></span></h1> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">⚠️ Warning</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">大版本重构，基于 Maven Module 的方式拆分多模块，希望大家多多提点建议！</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">嘿嘿，为接入 Flowable 工作流、支持 Spring Cloud 微服务版本做准备~</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">📈 Statistic</h3> 
<ul> 
 <li>总代码行数：69118</li> 
 <li>源码代码行数：42571</li> 
 <li>注释行数：15847</li> 
 <li>单元测试用例数：278</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">⭐ New Features</h3> 
<ul> 
 <li>【重构】大模块按照多 Maven Module 的方式拆分，提升可维护性，为后续重构 onemall 提供基础</li> 
 <li>【移除】将<span> </span><code>yudao-core-service</code><span> </span>模块移除，替换成每个 Maven Module 暴露对应的<span> </span><code>yudao-module-***-api</code><span> </span>模块</li> 
 <li>【新增】Spring Security 支持读取多种用户类型，从不同的数据库表，从而实现单项目提供管理后台、用户 APP 的不同 RESTful API 接口</li> 
 <li>【新增】Spring Security 新增 AuthorizeRequestsCustomizer 抽象类， 自定义每个 Maven Module 的 URL 的安全配置</li> 
 <li>【新增】代码生成器支持多 Maven Module 的方式生成代码，支持管理后台、用户 APP 两种场景的 RESTful API 的生成，支持 H2 SQL 脚本的生成</li> 
 <li>【新增】每次发布大版本时，将 yudao-ui-admin 编译后，放到 yudao-server 项目中，可以快速体验，无需搭建前端开发环境</li> 
 <li>【重构】将数据库文档调整到 tool 模块，更加明确</li> 
 <li>【优化】代码生成器的前端展示效果，例如说 Java 包路径合并</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐞 Bug Fixes</h3> 
<ul> 
 <li>【修复】用户无权限访问 指定 API 时，未返回 FORBIDDEN 结果码</li> 
 <li>【修复】定时任务刷新本地缓存时，无租户上线文，导致查询报错</li> 
 <li>【修复】配置中心只加载了删除的配置</li> 
 <li>【修复】管理后台 UI 超时登录后，返回登陆界面时，由于未登陆加载不到信息，导致报错的问题</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🔨 Dependency Upgrades</h3> 
<ul> 
 <li>【升级】spring-boot from 2.4.12 to 2.5.9，最新的 Spring Boot 2.6.X 在等更流行一些，稳定第一</li> 
 <li>【升级】Spring Boot Admin from 2.3.2 to 2.6.2，提供更好的监控能力</li> 
 <li>【移除】Apache FreeMarker 依赖，修改 Screw 使用 Velocity 作为模板引擎</li> 
 <li>【升级】redisson from 3.16.6 to 3.16.8</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">未来计划</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.4.1 计划：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于 uniapp 实现跨端的用户前台</li> 
 <li>基于 flowable 实现工作流</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.5.0 计划：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>三方支付：https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/pay_extension</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.6.0 计划：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>简易商城，支持商品、交易、支付、营销等基本功能</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            