
---
title: 'Sa-Token v1.25.0 更新，最全单点登录框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 09:04:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">Sa-Token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、分布式Session会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p style="text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过sa-token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="text-align:left">Sa-Token v1.25.0  版本更新包括以下内容：</p> 
<ul> 
 <li>新增：<code>SaRequest</code>新增<code>getHeader(name, defaultValue)</code>方法，用于获取header默认值</li> 
 <li>新增：<code>SaRequest</code> 添加 <code>forward</code> 转发方法</li> 
 <li>新增：Readme新增源码模块介绍、友情链接、正在使用Sa-Token的项目</li> 
 <li>重构：重构SSO单点登录模块源码，增加可读性</li> 
 <li>新增：SSO配置表新增所属端说明</li> 
 <li>新增：SSO模式三新增账号资料同步示例 <strong>[重要]</strong></li> 
 <li>新增：前后端分离模式下接入SSO的示例 <strong>[重要]</strong></li> 
 <li>优化：优化SSO单点注销重定向逻辑</li> 
 <li>重构：重构SSO单点登录模块部分API</li> 
 <li>优化：优化SaQuickBean中过滤器处理逻辑</li> 
 <li>文档：优化文档样式，增加示例</li> 
 <li>文档：代码鉴权、注解鉴权、路由拦截鉴权，选择指南</li> 
 <li>文档：文档新增 SSO旧有系统改造指南</li> 
 <li>文档：SSO集成文档里添加API列表</li> 
 <li>文档：新增 <code>Sa-Token-Study</code> 链接，讲解 Sa-Token 源码涉及到的技术点</li> 
 <li>不兼容更新重构： 
  <ul> 
   <li>重构：修复 <code>SaReactorHolder.getContent()</code> 拼写错误：<code>content</code> -> <code>context</code></li> 
  </ul> </li> 
</ul> 
<h4 style="text-align:left"><strong>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></strong></h4> 
<p>框架功能架构图</p> 
<p><img alt src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            