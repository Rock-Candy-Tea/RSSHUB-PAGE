
---
title: 'Sa-Token v1.20.0 发布，轻量级权限认证框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 09:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">Sa-Token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、分布式Session会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p style="text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过sa-token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="text-align:left">Sa-Token v1.20.0  版本更新包括以下内容：</p> 
<ul> 
 <li>新增：新增Solon适配插件，感谢大佬 <code>@刘西东</code> 提供的pr <strong>[重要]</strong></li> 
 <li>新增：新增<code>SaRouter.stop()</code>函数，用于一次性跳出匹配链功能 <strong>[重要]</strong></li> 
 <li>新增：新增单元测试 <strong>[重要]</strong></li> 
 <li>新增：新增临时令牌验证模块 <strong>[重要]</strong></li> 
 <li>新增：新增<code>sa-token-temp-jwt</code>模块整合jwt临时令牌鉴权 <strong>[重要]</strong></li> 
 <li>新增：会话 <code>SaSession.get()</code> 增加缓存API，简化代码</li> 
 <li>新增：新增框架调查问卷</li> 
 <li>修复：修复同时引入 <code>Spring Cloud Bus</code> 与 <code>Sa-Token</code> 冲突的问题 <strong>[重要]</strong></li> 
 <li>修复：修复<code>SaServletFilter</code>异常函数中无法自定义<code>Content-Type</code>的问题</li> 
 <li>文档：新增微服务依赖引入说明</li> 
 <li>文档：新增认证流程图</li> 
 <li>不兼容更新重构： 
  <ul> 
   <li>方法：<code>StpUtil.setLoginId(id)</code> -> <code>StpUtil.login(id)</code></li> 
   <li>方法：<code>StpUtil.getLoginKey()</code> -> <code>StpUtil.getLoginType()</code> (注意其它所有地方的<code>LoginKey</code>均已更改为<code>loginType</code>)</li> 
   <li>工具类：<code>SaRouterUtil</code> -> <code>SaRouter</code></li> 
   <li>配置类：<code>allowConcurrentLogin</code> -> <code>isConcurrent</code></li> 
   <li>配置类：<code>isV</code> -> <code>isPrint</code></li> 
   <li>为保证平滑更新，旧API仍旧保留，但已增加<code>@Deprecated</code>注解，请尽快更新至新API</li> 
  </ul> </li> 
</ul> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">更多详细信息请关注官方文档</span></p>
                                        </div>
                                      
</div>
            