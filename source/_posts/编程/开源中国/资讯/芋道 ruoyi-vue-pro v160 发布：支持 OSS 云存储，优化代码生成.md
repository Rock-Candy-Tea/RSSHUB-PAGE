
---
title: '芋道 ruoyi-vue-pro v1.6.0 发布：支持 OSS 云存储，优化代码生成'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5539'
author: 开源中国
comments: false
date: Mon, 21 Mar 2022 02:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5539'
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
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdashboard.yudao.iocoder.cn">http://dashboard.yudao.iocoder.cn</a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>账号密码：admin/admin123</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">更新说明</span></span></h1> 
<h3 style="text-align:start">📈<span> </span>Statistic</h3> 
<ul> 
 <li>总代码行数：77279</li> 
 <li>源码代码行数：47812</li> 
 <li>注释行数：17676</li> 
 <li>单元测试用例数：537</li> 
</ul> 
<h3 style="text-align:start">⭐<span> </span>New Features</h3> 
<ul> 
 <li>【优化】文件存储的功能，支持将文件存储到 S3（MinIO、阿里云、腾讯云、七牛云）、本地、FTP、FTP、数据库等<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/98">#98</a></li> 
 <li>【新增】《开发文档》的代码生成（新增功能）、功能权限、上传下载等小节完成，可访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.iocoder.cn%2F" target="_blank">https://doc.iocoder.cn</a><span> </span>地址</li> 
 <li>【新增】开发环境下，管理后台每个菜单展示对应的《开发文档》的说明<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/efe4200181785dc5425259622b8007e44163750f">code</a></li> 
 <li>【新增】《开发文档》的工作流、代码生成（新增功能）、功能权限、数据权限等小节完成，可访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.iocoder.cn%2F" target="_blank">https://doc.iocoder.cn</a><span> </span>地址</li> 
 <li>【优化】将<span> </span><code>yudao-module-tool</code><span> </span>合并到<span> </span><code>yudao-module-infra</code><span> </span>模块，统一基础设施<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/94">#94</a></li> 
 <li>【优化】代码生成时，额外生成 MyBatis Mapper XML 文件<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/96">#96</a></li> 
 <li>【新增】开启 TopNav 时，没有子菜单的情况下，隐藏侧边栏<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/1a2c03bc7e67eb73de50da426fee23030b1a3115">code</a></li> 
</ul> 
<h3 style="text-align:start">🐞<span> </span>Bug Fixes</h3> 
<ul> 
 <li>【修复】仅本人数据权限时，个人中心会报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/97">#97</a></li> 
 <li>【修复】修改租户套餐的权限时，本地缓存刷新错误的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/99">#99</a></li> 
 <li>【修复】删除菜单、角色时，本地缓存未刷新的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/9209e8da1c54ca0b09645a47086ee15479c83113">code</a></li> 
 <li>【修复】登录界面输入不存在的租户时，导致后续请求报错的问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/db06292ea35d239c71af7e45f64cae0018d2f0bd">code</a></li> 
 <li>【修复】登录超时刷新页面时，跳转登录页面还提示重新登录问题<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/commit/fb1648ecbaed13d8553e6e5c302613670f1f15d1">code</a></li> 
</ul> 
<h3 style="text-align:start">🔨<span> </span>Dependency Upgrades</h3> 
<ul> 
 <li>【升级】apollo-client from 1.7.0 to 1.9.2</li> 
 <li>【升级】guide from 4.1.0 to 5.1.0 ：解决 Apollo 在 JDK 17 无法启动的问题</li> 
</ul>
                                        </div>
                                      
</div>
            