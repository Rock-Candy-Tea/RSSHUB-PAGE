
---
title: '芋道 ruoyi-vue-pro v1.5.1 发布：优化多租户功能，新增租户套餐，增强多租户封装'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=213'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 08:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=213'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目地址</span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:left"><strong>严肃声明：现在、未来都不会有商业版本，所有功能全部开源！</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>拒绝虚假开源，售卖商业版，程序员不骗程序员！！</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>「我喜欢写代码，乐此不疲」</strong><br> <strong>「我喜欢做开源，以此为乐」</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">🐯<span style="color:#e74c3c"><span style="background-color:#ffffff">项目介绍</span></span></h1> 
<p> </p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>芋道</strong>，一套<strong>全部开源</strong>的<strong>企业级</strong>的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有任何问题，或者想要的功能，可以在<span> </span><em>Issues</em><span> </span>中提给艿艿。</p> 
</blockquote> 
<ul> 
 <li>前端采用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin">vue-element-admin</a><span> </span>，正在支持 Vue 3 + ElementUI Plus 最新方案。</li> 
 <li>后端采用 Spring Boot、MySQL + MyBatis Plus、Redis + Redisson。</li> 
 <li>权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统。</li> 
 <li>支持加载动态权限菜单，按钮级别权限控制，本地缓存提升性能。</li> 
 <li>支持 SaaS 多租户系统，可自定义每个租户的权限，提供透明化的多租户底层封装。</li> 
 <li>工作流使用 Activiti ，支持动态表单、在线设计流程、多种任务分配方式。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码 + 单元测试 + Swagger 接口文档 + Validator 参数校验。</li> 
 <li>集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款。</li> 
 <li>集成阿里云、腾讯云、云片等短信渠道，集成阿里云、腾讯云、七牛云等云存储服务。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🐶在线体验</h2> 
<p>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdashboard.yudao.iocoder.cn">http://dashboard.yudao.iocoder.cn</a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>账号密码：admin/admin123</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">更新说明</span></span></h1> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">⚠️ Warning</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">暂无，主要优化多租户功能：</p> 
<ul> 
 <li>创建租户时，自动创建用户、角色等信息</li> 
 <li>支持租户套餐，自定义每个租户的菜单、操作、按钮等权限信息</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">📈 Statistic</h3> 
<ul> 
 <li>总代码行数：71249</li> 
 <li>源码代码行数：43921</li> 
 <li>注释行数：16341</li> 
 <li>单元测试用例数：341</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">⭐ New Features</h3> 
<ul> 
 <li>【新增】后端<span> </span><code>yudao.tenant.enable</code><span> </span>配置项，前端<span> </span><code>VUE_APP_TENANT_ENABLE</code><span> </span>配置项，用于开关租户功能。<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/79311ecc71f0c6beabe0e5f84e1423ce745a5f09" target="_blank">commit</a></li> 
 <li>【优化】调整默认所有表开启多租户的特性，可通过<span> </span><code>yudao.tenant.ignore-tables</code><span> </span>配置项进行忽略，替代原本默认不开启的策略<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/79311ecc71f0c6beabe0e5f84e1423ce745a5f09" target="_blank">commit</a></li> 
 <li>【新增】通过<span> </span><code>yudao.tenant.ignore-urls</code><span> </span>配置忽略多租户的请求，例如说 ，例如说短信回调、支付回调等 Open API<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/79311ecc71f0c6beabe0e5f84e1423ce745a5f09" target="_blank">commit</a></li> 
 <li>【新增】新增<span> </span><code>@TenantIgnore</code><span> </span>注解，标记指定方法，忽略多租户的自动过滤，适合实现跨租户的逻辑<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/4d53944771c66b563da1e3d68d3ba43405af8a06" target="_blank">commit</a></li> 
 <li>【新增】租户套餐的管理，可配置每个租户的可使用的功能权限<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/6b6d676a6baa2dad16ae9bf03d5002209064c8cc" target="_blank">commit</a></li> 
 <li>【优化】新建租户时，自动创建对应的管理员账号、角色等基础信息<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/2598c033a95d4b61d5f5ab3da5f1414f25c510d6" target="_blank">commit</a></li> 
 <li>【优化】Redis 最低版本 5.0.0 检测，解决搭建环境过程中无法理解 XREADGROUP 指令的报错<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/c64bb81caeee2721e0c373eee014e3977d88cb37" target="_blank">commit</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐞 Bug Fixes</h3> 
<ul> 
 <li>【修复】修复不支持根部门的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/fa62ace6af5ecc2f3030fa86d2ce222a1392f1a6" target="_blank">commit</a></li> 
 <li>【修复】错误码存在重复的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/10ba70e1079d9a068c054ee677a7accc0b1209fe" target="_blank">commit</a></li> 
 <li>【修复】角色的数据范围为仅本人时，登陆后获取权限列表报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/c61811a622a6829802e233e303bab091cc308f3a" target="_blank">commit</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🔨 Dependency Upgrades</h3> 
<ul> 
 <li>【升级】spring-boot from 2.5.9 to 2.5.10</li> 
 <li>【升级】mybatis-plus from 3.4.3.4 to 3.5.1</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">未来计划</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.6.0 计划：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于 flowable 实现工作流（今天合并到 master 分支）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.6.1 计划：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>功能优化：https://gitee.com/zhijiantianya/ruoyi-vue-pro/issues/I4VFYB</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            