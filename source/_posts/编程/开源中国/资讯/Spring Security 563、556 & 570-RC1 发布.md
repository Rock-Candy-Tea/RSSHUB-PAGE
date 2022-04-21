
---
title: 'Spring Security 5.6.3、5.5.6 & 5.7.0-RC1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1561'
author: 开源中国
comments: false
date: Thu, 21 Apr 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1561'
---

<div>   
<div class="content">
                                                                                            <p>Spring Security 的三个分支发布了更新：5.6.3、5.5.6 和 5.7.0-RC1。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F04%2F18%2Fspring-security-5-7-0-rc1-released" target="_blank"><strong>5.7.0-RC1 主要变化</strong></a></p> 
<ul> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">引入<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-security%2Freference%2F5.7%2Fservlet%2Fauthentication%2Fpersistence.html%23securitycontextholderfilter" target="_blank">SecurityContextHolderFilter</a><span> </span>- 用于显式保存 SecurityContext</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">为<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-security%2Freference%2F5.7%2Fservlet%2Fexploits%2Fheaders.html%23servlet-headers-cross-origin-policies" target="_blank">Cross Origin Policies headers</a> 添加 DSL 支持</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">支持为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Fissues%2F6548" target="_blank">加密客户端</a>配置 PKCE</p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">添加对 SAML 2.0 Login & Single Logout XML 的支持</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Freleases%2Ftag%2F5.7.0-RC1" target="_blank">详情查看 release note</a>。</p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F04%2F18%2Fspring-security-5-6-3-and-5-5-6-available-now" target="_blank">5.6.3 & 5.5.6</a></strong></p> 
<ul> 
 <li>当 AuthorizationManager 弃用授权时，AuthorizationManagerWebInvocationPrivilegeEvaluator 会授予访问权<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Fissues%2F10951" target="_blank">#10951</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">将 HashSet 更改为 LinkedHashSet 以获取 RelyingPartyRegistration 凭据</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Fissues%2F10916" target="_blank">#10916</a></li> 
 <li>修复 saml2 authentication-requests 文档<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Fissues%2F11047" target="_blank">#11047</a></li> 
 <li>从文档删除 "Hi servlet/authentication/architecture there"<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Fissues%2F10963" target="_blank">#10963</a></li> 
</ul> 
<p>此外还升级了依赖项。</p> 
<p>详情查看 release note（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Freleases%2Ftag%2F5.6.3" target="_blank">5.6.3</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-security%2Freleases%2Ftag%2F5.5.6" target="_blank">5.5.6</a>）。</p> 
<p>Spring Security 是一个能够为基于 Spring 的企业应用系统提供声明式的安全访问控制解决方案的安全框架。它提供了一组可以在 Spring 应用上下文中配置的 Bean，充分利用了 Spring IoC，DI（控制反转Inversion of Control ,DI:Dependency Injection 依赖注入）和 AOP（面向切面编程）功能，为应用系统提供声明式的安全访问控制功能，减少了为企业系统安全控制编写大量重复代码的工作。</p>
                                        </div>
                                      
</div>
            