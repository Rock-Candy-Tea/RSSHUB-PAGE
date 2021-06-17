
---
title: 'Sa-Token v1.20.0 发布，轻量级权限认证框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 01:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">Sa-Token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、分布式Session会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p style="text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过sa-token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="text-align:left">Sa-Token v1.20.0  版本更新包括以下内容：</p> 
<p style="text-align:left">- 新增：新增Solon适配插件，感谢大佬 `@刘西东` 提供的pr **[重要]** <br> - 新增：新增`SaRouter.stop()`函数，用于一次性跳出匹配链功能 **[重要]** <br> - 新增：新增单元测试   **[重要]** <br> - 新增：新增临时令牌验证模块   **[重要]**  <br> - 新增：新增`sa-token-temp-jwt`模块整合jwt临时令牌鉴权    **[重要]**  <br> - 新增：会话 `SaSession.get()` 增加缓存API，简化代码 <br> - 新增：新增框架调查问卷 <br> - 修复：修复同时引入 `Spring Cloud Bus` 与 `Sa-Token` 冲突的问题   **[重要]** <br> - 修复：修复`SaServletFilter`异常函数中无法自定义`Content-Type`的问题 <br> - 文档：新增微服务依赖引入说明 <br> - 文档：新增认证流程图 <br> - 不兼容更新重构：<br>     - 方法：`StpUtil.setLoginId(id)` -> `StpUtil.login(id)` <br>     - 方法：`StpUtil.getLoginKey()` -> `StpUtil.getLoginType()` (注意其它所有地方的`LoginKey`均已更改为`loginType`)<br>     - 工具类：`SaRouterUtil` -> `SaRouter` <br>     - 配置类：`allowConcurrentLogin` -> `isConcurrent` <br>     - 配置类：`isV` -> `isPrint` <br>     - 为保证平滑更新，旧API仍旧保留，但已增加`@Deprecated`注解，请尽快更新至新API  </p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">更多详细信息请关注官方文档</span></p> 
<p style="text-align:left"> </p>
                                        </div>
                                      
</div>
            