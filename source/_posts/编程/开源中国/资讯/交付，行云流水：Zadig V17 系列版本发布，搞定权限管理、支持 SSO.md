
---
title: '交付，行云流水：Zadig V1.7 系列版本发布，搞定权限管理、支持 SSO'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8c23d3d068b44b4274444c21a7bbc4d9ec1.png'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 14:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8c23d3d068b44b4274444c21a7bbc4d9ec1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img alt src="https://oscimg.oschina.net/oscnet/up-8c23d3d068b44b4274444c21a7bbc4d9ec1.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><strong>“交付，行云流水”</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">经过二个月的研发迭代</p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">Zadig V1.7 版本终于发布了<br>  </p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">V1.7.0 支持权限管理、统一用户接入功能</p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">并针对 Zadig 系统架构进行了的优化<br>  </p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">V1.7.1 更在 V1.7.0 之上</p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">大幅度降低 Zadig 安装难度<br>  </p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">至此，Zadig 已经极其适用于企业级的研发场景</p> 
<p style="margin-left:0px; margin-right:0px; text-align:center">让大团队高复杂度的软件交付，行云流水</p> 
<hr> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#464545"><strong>“权限灵活配置，协作一气呵成”</strong></span></h3> 
<p style="margin-left:0; margin-right:0"><strong><span>支持项目权限管理：系统管理员及项目管理员，可以对项目角色及权限进行配置和管理</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在项目的<strong><span> </span>角色管理<span> </span></strong>中按需添加角色</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0ce96f684ce5dbed699af7dc176afabda12.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在项目的<strong><span> </span>成员管理<span> </span></strong>中，为用户绑定角色，赋予权限，实现对项目资源的权限管理</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e40826bdde354e2832fbc83d234963cf812.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#464545"><strong>“登录一键认证，接入一步到位”</strong></span></h3> 
<p style="margin-left:0; margin-right:0"><strong><span>支持统一用户接入 LDAP（Microsoft Active Directory、OpenLDAP）、OAuth 2.0、GitHub 等</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">通过<span> </span><strong>第三方集成 </strong>-><span> </span><strong>用户账户集成<span> </span></strong>按需接入</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3912379976d632f429b2966684a7cec8b53.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#464545"><strong>“高效简洁架构，云原生拉满”</strong></span></h3> 
<p style="margin-left:0; margin-right:0"><strong><span>优化系统架构 ～ Zadig 新系统架构引入了云原生组件</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">API 网关 Gloo Edge 组件、认证和授权组件 OPA、身份认证组件 Dex 等，并在 GitHub 上发布了系统架构图及详细的组件介绍，提供了中英文档说明</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5b3f2882ed64312f46d5a3876d633300f37.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#464545"><strong>“工具箱统一整合，访问快捷”</strong></span></h3> 
<p style="margin-left:0; margin-right:0"><strong><span>支持外部系统常用链接管理</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在系统配置中添加常用外部链接，方便用户整合其他系统入口，实现快捷访问，降低开发者心智负担</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3364f346ccc59029eadbab0b1914ad2ddcb.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#464545"><strong>“资源规格，你说了算”</strong></span></h3> 
<p style="margin-left:0; margin-right:0"><strong><span>构建配置支持自定义资源规格</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在构建配置中，资源规格可以自定义，按需使用</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7f7b51409f16ec110f348a5cac52844dc25.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#464545"><strong>新增功能详情列表</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>Zadig V1.7.0</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持用户管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持项目权限管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持外部系统常用链接管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>托管项目支持 Webhook 自动触发</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span><strong>Zadig V1.7.1</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>认证支持标准化 OAuth2 扩展开发</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>构建配置支持自定义资源规格</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>权限管理模块的若干问题修复</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>认证和账号模块的若干问题修复</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><span style="color:#464545"><strong>Release Note</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>Zadig V1.7.0</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">User management</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Authorization system</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Frequently used link</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Webhooks for loaded project</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong><span>Zadig V1.7.1</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">Support OAuth2 authentication extension development</p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">Build configuration support for customized resource specifications</p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">Bugfix for User management/Authorization system</p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:center"><strong><span>关于Zadig</span></strong></h3> 
<p style="margin-left:0; margin-right:0">Zadig 是基于 Kubernetes 设计、研发的开源分布式持续交付 (Continuous Delivery) 产品，为开发者提供云原生运行环境，支持开发者本地联调、微服务并行构建和部署、集成测试等。Zadig 内置了面向 Kubernetes、Helm、云主机、大体量微服务等复杂业务场景的最佳实践，为工程师一键生成自动化工作流 。</p>
                                        </div>
                                      
</div>
            