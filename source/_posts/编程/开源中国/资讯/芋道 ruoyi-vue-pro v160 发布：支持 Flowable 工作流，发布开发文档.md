
---
title: '芋道 ruoyi-vue-pro v1.6.0 发布：支持 Flowable 工作流，发布开发文档'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1426'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 13:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1426'
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
<ul> 
 <li>基于 Flowable 实现工作流，可见<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fblob%2Fmaster%2Fyudao-module-bpm%2Fyudao-module-bpm-impl-flowable%2F" target="_blank"><code>yudao-module-bpm-impl-flowable</code></a><span> </span>模块。</li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">友情提示：原本 Activiti 实现的工作流，在<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fblob%2Fmaster%2Fyudao-module-bpm%2Fyudao-module-bpm-impl-activiti%2F" target="_blank"><code>yudao-module-bpm-impl-activiti</code></a><span> </span>模块，保持同步更新。</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:start">📈 Statistic</h3> 
<ul> 
 <li>总代码行数：75008</li> 
 <li>源码代码行数：46416</li> 
 <li>注释行数：17132</li> 
 <li>单元测试用例数：341</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">⭐ New Features</h3> 
<ul> 
 <li>【新增】<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FYunaiV%2Fruoyi-vue-pro%2Fblob%2Fmaster%2Fyudao-module-bpm%2Fyudao-module-bpm-impl-flowable%2F" target="_blank"><code>yudao-module-bpm-impl-flowable</code></a><span> </span>模块，实现 Flowable 工作流<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/issues/I3QDUV">#88:构建报错Cannot resolve plugin org.springframework.boot:spring-boot-maven-plugin:<unknown></a></li> 
 <li>【新增】《开发文档》的简介、功能列表、快速启动、技术选型、项目结构、新建模块、SaaS 多租户等小节完成，可访问<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fdoc.iocoder.cn" target="_blank">https://doc.iocoder.cn</a><span> </span>地址</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐞 Bug Fixes</h3> 
<ul> 
 <li>【修复】正常租户登陆后退出，切换到过期租户时造成的<span> </span><code>tenant.ignore-urls</code><span> </span>配置失效的问题，比如无法获取验证码图片造成无法登录<span> </span><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro/pulls/91" target="_blank">#91</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🔨 Dependency Upgrades</h3> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">暂无，计划升级 Spring Boot 2.6.X</p>
                                        </div>
                                      
</div>
            