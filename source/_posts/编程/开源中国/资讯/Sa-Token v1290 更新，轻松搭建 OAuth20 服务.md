
---
title: 'Sa-Token v1.29.0 更新，轻松搭建 OAuth2.0 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js4.png'
author: 开源中国
comments: false
date: Thu, 10 Feb 2022 09:08:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js4.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Sa-Token 是一个轻量级 Java 权限认证框架，主要解决：登录认证、权限认证、分布式 Session 会话、单点登录、OAuth2.0 等一系列权限相关问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过 Sa-Token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Sa-Token v1.29.0  版本更新包括以下内容：</p> 
<ul> 
 <li>升级：sa-token-jwt插件可在登录时添加额外数据。</li> 
 <li>重构：优化Dubbo调用时向下传递Token的规则，可避免在项目启动时由于Context无效引发的bug。</li> 
 <li>重构：OAuth2 授权模式开放由全局配置和Client单独配置共同设定。</li> 
 <li>重构：OAuth2 模块部分属性支持每个 Client 单独配置。</li> 
 <li>重构：OAuth2 模块部分方法名修复单词拼写错误：converXxx -> convertXxx。</li> 
 <li>重构：修复 OAuth2 模块<span> </span><code>deleteAccessTokenIndex</code><span> </span>回收 token 不彻底的bug。</li> 
 <li>新增：OAuth2 模块新增<span> </span><code>pastClientTokenTimeout</code>，用于指定 PastClientToken 默认有效期。</li> 
 <li>文档：常见报错章节增加目录树，方便查阅。</li> 
 <li>文档：优化文档样式。</li> 
 <li>新增：新增 BCrypt 加密。</li> 
 <li>修复：修复StpUtil.getLoginIdByToken(token) 在部分场景下返回出错的bug。</li> 
 <li>重构：优化OAuth2模块密码式校验步骤。</li> 
 <li>新增：新增Jackson定制版Session，避免timeout属性的序列化。</li> 
 <li>新增：SaLoginModel新增setToken方法，用于预定本次登录产生的Token。</li> 
 <li>新增：新增 StpUtil.createLoginSession() 方法，用于无Token注入的方式创建登录会话。</li> 
 <li>新增：OAuth2 与 StpUtil 登录会话数据互通。</li> 
 <li>新增：新增<span> </span><code>StpUtil.renewTimeout(100);</code><span> </span>方法，用于 Token 的 Timeout 值续期。</li> 
 <li>修复：修复默认dao实现类中<span> </span><code>updateObject</code><span> </span>无效的bug</li> 
 <li>完善：完善单元测试。</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>框架功能结构图</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="274" src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js4.png" width="500" referrerpolicy="no-referrer"></strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            