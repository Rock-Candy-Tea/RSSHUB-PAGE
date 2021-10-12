
---
title: 'Sa-Token v1.27.0 更新，轻量级权限认证框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 01:38:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Sa-Token 是一个轻量级 Java 权限认证框架，主要解决：登录认证、权限认证、分布式 Session 会话、单点登录、OAuth2.0 等一系列权限相关问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过 Sa-Token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Sa-Token v1.27.0  版本更新包括以下内容：</strong></p> 
<ul> 
 <li>升级：增强 SaRouter 链式匹配能力<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>新增：新增插件 Thymeleaf 标签方言<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>新增：@SaCheckPermission 增加 orRole 字段，用于权限角色“双重or”匹配<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>升级：Cookie 模式增加<span> </span><code>secure</code>、<code>httpOnly</code>、<code>sameSite</code>等属性的配置<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>重构：重构 SSO 三种模式，抽离出统一的认证中心<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>新增：新增 SaStrategy 策略类，方便内部逻辑按需重写<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>新增：临时认证模块新增 deleteToken 方法用于回收 Token</li> 
 <li>新增：新增 kickout、replaced 等注销会话的方法，更灵活的控制会话周期<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>新增：权限认证增加 API：<code>StpUtil.hasPermissionAnd</code>、<code>StpUtil.hasPermissionOr</code></li> 
 <li>新增：角色认证增加 API：<code>StpUtil.hasRoleAnd</code>、<code>StpUtil.hasRoleOr</code></li> 
 <li>新增：新增<span> </span><code>StpUtil.getRoleList()</code><span> </span>和<span> </span><code>StpUtil.getPermissionList()</code><span> </span>方法</li> 
 <li>新增：新增 StpLogic 自动注入特性，可快速方便的扩展 StpLogic 对象</li> 
 <li>优化：优化同端互斥登录逻辑，如果登录时没有指定设备标识，则默认顶替所有设备下线</li> 
 <li>优化：在未登录时调用 hasRole 和 hasPermission 不再抛出异常，而是返回false</li> 
 <li>升级：升级注解鉴权算法，并提供更简单的重写方式</li> 
 <li>文档：新增常见报错排查，方便快速排查异常报错</li> 
 <li>文档：文档新增 SSO 单点登录与 OAuth2 技术选型对比</li> 
 <li>破坏式更新： 
  <ul> 
   <li>[向下兼容] 废弃 SaTokenAction 接口，替代方案： SaStrategy</li> 
   <li>[向下兼容] 移除<span> </span><code>StpUtil.logoutByLoginId()</code><span> </span>更换为<span> </span><code>StpUtil.kickout()</code>;</li> 
   <li>[不向下兼容] 侦听器 doLogoutByLoginId 与 doReplaced 方法移除 device 参数</li> 
   <li>[不向下兼容] 侦听器 doLogoutByLoginId 方法重命名为 doKickout</li> 
  </ul> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>框架功能结构图</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="274" src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png" width="500" referrerpolicy="no-referrer"></strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            