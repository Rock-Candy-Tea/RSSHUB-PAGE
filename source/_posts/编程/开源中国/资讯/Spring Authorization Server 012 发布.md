
---
title: 'Spring Authorization Server 0.1.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3800'
author: 开源中国
comments: false
date: Sat, 10 Jul 2021 06:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3800'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Authorization Server 0.1.2 已经发布，Spring Authorization Server 是 Spring Security 团队领导的社区驱动项目，致力于解决 Spring 社区的 OAuth 2.0 Authorization Server 支持问题。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>新特性 
  <ul> 
   <li>提供定制授权端点的能力</li> 
   <li>更新授权服务器示例以使用 jdbc</li> 
   <li>提供基于 JDBC 的示例</li> 
   <li>在令牌请求中包含 WebAuthenticationDetails</li> 
   <li>提供自定义令牌端点的能力</li> 
   <li>刷新令牌授予可以发出 ID 令牌</li> 
   <li>提供 OAuth2AuthorizationConsentService 的 JDBC 实现</li> 
   <li>提供 RegisteredClientRepository 的 JDBC 实现 </li> 
   <li>为自定义授权同意页提供配置</li> 
   <li>记住用户同意并使同意页可配置</li> 
   <li>引入样本 oauth 服务器的集成测试</li> 
  </ul> </li> 
 <li>Bug 修复 
  <ul> 
   <li>为授权服务器添加 jackson 模块</li> 
   <li>授权表的属性栏太小</li> 
   <li>修复 NPE 保存公共客户端 </li> 
   <li>JdbcRegisteredClientRepository 在保存公共客户端时抛出 NPE</li> 
   <li>OAuth2AuthorizationCodeAuthenticationProvider 没有正确反序列化 OAuth2Authorization 对象属性</li> 
   <li>临时修复访问令牌响应的 expires_in</li> 
   <li>修复授权码过期检查</li> 
   <li>OAuth2AuthorizationCodeAuthenticationProvider 应检查代码是否已过期</li> 
   <li>Oauth2 客户端期望 “expires_in” 是一个数字</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F09%2Fspring-authorization-server-0-1-2-available-now" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            