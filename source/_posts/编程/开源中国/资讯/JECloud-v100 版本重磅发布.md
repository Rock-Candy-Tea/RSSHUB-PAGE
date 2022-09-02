
---
title: 'JECloud-v1.0.0 版本重磅发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://doc.jepaas.com/uploads/je-doc-jecloud-help/images/m_2f8c97bc8d1584edaa533c6cde416b18_r.png'
author: 开源中国
comments: false
date: Fri, 02 Sep 2022 09:55:00 GMT
thumbnail: 'https://doc.jepaas.com/uploads/je-doc-jecloud-help/images/m_2f8c97bc8d1584edaa533c6cde416b18_r.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">平台简介</h2> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">JECloud 是基于微服务架构的低代码平台，是新一代企业级 APaaS 平台，为企业数字化业务提供了按需使用、持续运行的业务中台能力。快速满足企业多变的需求，允许个性化定制，提供支撑企业业务的完美解决方案，为企业业务的快速创新提供了重要支撑，加速企业数字化转型。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">基础架构</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="JECloud基础架构" src="https://doc.jepaas.com/uploads/je-doc-jecloud-help/images/m_2f8c97bc8d1584edaa533c6cde416b18_r.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">JECloud 核心服务<br>  </h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">网关服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台接口统⼀开放服务，用户可以自定义路由规则，同时默认实现三种路由方式：URL 路由、Header 路由、参数路由。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">元数据服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台统⼀元数据管理服务。其功能主要包括：资源表元数据管理、功能元数据管理、数据字典元数据管理、图报表元数据管理、系统设置管理。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">RBAC 服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台统⼀组织，用户，机构、账号、角色权限等管理服务。其主要功能主要包括： 组织管理、三方机构管理、员工管理、账号管理、角色管理、权限管理、授权管理、菜单管理等。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">工作流服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台统⼀流程服务，功能主要包括：流程在线设计、流程流转、流程历史及待办。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">消息服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台统⼀消息服务，功能主要包括：邮件消息发送、短信消息发送、微邮管理、冒泡管理、推送消息发送、钉钉消息发送、微信消息发送、飞书消息发送。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文档服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台统一文档存储服务，功能主要包括：阿里云对象存储、腾讯云对象存储、本地存储、NFS 存储、外部存储扩展。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">链接器服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台统一的 WebSocket 链接管理服务。用于统一管理 WebSocket 链接，实现平台级页面消息推送。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Operator 服务</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:left">平台自动化流水线工具，基于 Go 语言构建，用于可基于架构管理，快速发布服务至目标服务器。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Features</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>完成菜单管理模块。</li> 
 <li>完成元数据资源表引擎。</li> 
 <li>完成元数据应用中心管理。</li> 
 <li>完成元数据数据字典引擎。</li> 
 <li>完成基于 Activiti7 的流程引擎。</li> 
 <li>完成微应用插件与管理。</li> 
 <li>完成顶部菜单模块。</li> 
 <li>完成平台级设置模块。</li> 
 <li>完成系统级设置模块。</li> 
 <li>完成统一机构管理，支持内部组织，外部组织机构的统一映射管理。</li> 
 <li>完成基于 RBAC 权限模型的重构。</li> 
 <li>完成人员多部门管理功能。</li> 
 <li>完成升级引擎，方便用户相关配置数据的打包和升级。</li> 
 <li>完成统一编号功能，为全局业务提供业务编号支持。</li> 
 <li>完成架构管理 - 微服务产品管理功能。</li> 
 <li>完成架构管理 - 运维管理功能。</li> 
 <li>完成平台统一缓存可视化功能。</li> 
 <li>完成微服务项目骨架项目，为业务快速创建微服务项目提供支持。</li> 
 <li>完成微应用项目骨架项目，为业务快速创建微应用项目提供支持。</li> 
 <li>完成基于 Go 的微服务流水线项目，方便用户一键发布微服务至目标服务器。</li> 
 <li>完成基于 Go 的微服务初始化项目，方便用户初始化基础环境。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">NextStep</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>增加表单高保真在线设计器。</li> 
 <li>工作流增加随机节点。</li> 
 <li>工作流增加跳跃、加签、催办、预警延期、传阅等。</li> 
 <li>增加多附件组件。</li> 
 <li>数据权限增加字段和字典级权限。</li> 
 <li>增加图表引擎。</li> 
 <li>增加数据源引擎。</li> 
 <li>增加门户引擎。</li> 
 <li>完成 SaaS 相关中间件，SaaS 体系及 SaaS 运营管理。</li> 
 <li>增加移动端 APP、H5、小程序在线设计与发布。</li> 
 <li>完善平台帮助手册与相关教程。</li> 
</ul> 
<div style="text-align:left"> 
 <div>
  体验地址：
  <span> </span>
  <span style="color:#6425d0">https://jecloud.net/experience</span>
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            