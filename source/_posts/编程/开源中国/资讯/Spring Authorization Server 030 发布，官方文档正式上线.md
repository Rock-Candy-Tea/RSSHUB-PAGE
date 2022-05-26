
---
title: 'Spring Authorization Server 0.3.0 发布，官方文档正式上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://asset.felord.cn/blog/20220526093507.png'
author: 开源中国
comments: false
date: Thu, 26 May 2022 10:36:00 GMT
thumbnail: 'https://asset.felord.cn/blog/20220526093507.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span>基于</span><span><strong><span>OAuth2.1</span></strong></span><span>的授权服务器</span><span><strong><span>Spring Authorization Server 0.3.0</span></strong></span><span>今天正式发布，在本次更新中有几大亮点。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>文档正式上线</span></h2> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>Spring Authorization Server 的文档随着本次更新正式发布了，目前已经可以在Spring官网访问。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>地址是：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-authorization-server" target="_blank"><span>https://spring.io/projects/spring-authorization-server</span></a></span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><img src="https://asset.felord.cn/blog/20220526093507.png" referrerpolicy="no-referrer"></span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><img src="https://asset.felord.cn/blog/20220526094331.png" referrerpolicy="no-referrer"></span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>该文档目前包含了以下几个重要的模块：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>项目概述：简介和功能列表。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>获得帮助：示例、常见问题和</span><span><strong><span>issues</span></strong></span><span>。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>入门： 系统要求、依赖和引导你开发第一个应用。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>配置模型： 默认配置和自定义配置。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>核心模型/组件： 核心的领域模型和组件接口介绍。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>协议端点： </span><span><strong><span>OAuth2</span></strong></span><span> 和</span><span><strong><span>OIDC 1.0</span></strong></span><span>协议端点的实现。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>使用指南： </span><span><strong><span>Spring Authorization Server</span></strong></span><span> 的指南。</span></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>0.3.0的重大变化</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>将仅包含常量的接口更改为最终类。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>将 </span><span><code>OAuth2TokenCustomizer</code></span><span> 移动到令牌包下。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>删除标记为</span><span><code>@Deprecation</code></span><span>的弃用功能代码。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>移除 </span><span><code>JwtEncoder</code></span><span> 和相关的类。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>删除 令牌上下文构建器中的</span><span><code>OAuth2TokenClaimsContext.Builder.claims()</code></span><span> 。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>删除令牌自省中的</span><span><strong><span>claim</span></strong></span><span>访问器 </span><span><code>OAuth2TokenIntrospectionClaimAccessor</code></span><span>。 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>删除对OAuth2中对</span><span><strong><span>PKCE</span></strong></span><span><code>plain</code></span><span>类型的</span><span><code>code_challenge_method</code></span><span>的支持。</span></p> </li> 
</ul> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>更多的新特性请参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-authorization-server%2Freleases%2Ftag%2F0.3.0" target="_blank"><span>0.3.0 changelog</span></a></span><span>。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>依赖升级</span></h2> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>本版本支持刚刚发布的Spring Boot 2.7.0和</span><span><strong><span>Spring Security 5.7.1</span></strong></span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to com.squareup.okhttp3:4.9.3</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to jackson-bom:2.13.3 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to mockito-core:4.5.1 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to nimbus-jose-jwt:9.22 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to Spring Boot 2.7.0 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to Spring Framework 5.3.20 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Update to Spring Security 5.7.1 </span></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>新的贡献者</span></h2> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>在本次版本中又增加了两名新的贡献者（</span><span><strong><span>Contributor</span></strong></span><span>）：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappchemist" target="_blank"><span>@appchemist</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403" target="_blank"><span>@NotFound403</span></a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            