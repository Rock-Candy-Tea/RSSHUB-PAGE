
---
title: 'Spring Authorization Server 0.2.2 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=356'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 16:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=356'
---

<div>   
<div class="content">
                                                                                            <p style="color:#34495e; margin-left:0.8em; margin-right:0.8em"><span><strong><span>Spring Authorization Server 0.2.2</span></strong></span><span>版本发布，这个版本主要是优化和bug修复，比较重要的新特性是</span><span><strong><span>客户端身份验证支持JWT断言</span></strong></span><span>。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>变更一览</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>新特性</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>JdbcOAuth2AuthorizationService</code></span><span>现在支持大数据库字段。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>废弃</span><span><code>OAuth2TokenIntrospectionClaimAccessor</code></span><span>，将使用Spring Security 5.6的实现。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>废弃</span><span><code>JwtEncoder</code></span><span>相关的类，使用Spring Security jose库实现。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>JdbcOAuth2AuthorizationService</code></span><span>中的token字段现在支持</span><span><code>clob</code></span><span> 和</span><span><code>text</code></span><span>数据类型。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Token撤销逻辑现在可以自定义了。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>userinfo_endpoint</code></span><span>端点现在被加入授权服务器元数据信息中了。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持从当前请求中解析 Token的</span><span><code>issuer</code></span><span>。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>客户端身份验证（Client authentication）现在支持JWT断言（JWT assertion）。</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>Bug修复</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>初始请求中缺少</span><span><code>state</code></span><span>和拒绝同意会导致异常。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>使用 PKCE #581请求无效令牌时会抛出 </span><span><code>invalid_grant</code></span><span>。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>默认的配置超出了Mysql行限制。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>OAuth2ClientAuthenticationToken</code></span><span> 不应跨请求保存。</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>依赖升级</span></h3> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到Jackson 2.12.6 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fissues%2F609" target="_blank"><span>#609</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到 Spring Boot 2.5.9 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fissues%2F608" target="_blank"><span>#608</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到 Reactor 2020.0.15 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fissues%2F607" target="_blank"><span>#607</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到 Spring Security 5.5.4 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fissues%2F606" target="_blank"><span>#606</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到 Spring Framework 5.3.15 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fissues%2F605" target="_blank"><span>#605</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到 </span><span><code>io.spring.ge.conventions</code></span><span> 0.0.9 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fissues%2F578" target="_blank"><span>#578</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级到 gradle enterprise 3.8 以规避log4j漏洞 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fadvisories%2FGHSA-p6xc-xr62-6r2g" target="_blank"><span>CVE-2021-45105</span></a></span><span>. </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Fpull%2F547" target="_blank"><span>#547</span></a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            