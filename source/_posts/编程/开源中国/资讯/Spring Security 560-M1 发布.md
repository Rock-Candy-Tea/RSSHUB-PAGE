
---
title: 'Spring Security 5.6.0-M1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1448'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 06:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1448'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Security 5.6.0-M1 现已发布，该版本除了除了依赖项升级，还包含很多错误修复和优化。</p> 
<p>主要更新内容</p> 
<ul> 
 <li>设置 servlet 上下文路径时，CookieClearingLogoutHandler 无法删除 cookie</li> 
 <li>访问令牌响应支持任何数据类型</li> 
 <li>将 AuthenticationDetailsS​​ource 添加到表单登录 Kotlin DSL</li> 
 <li>将 AuthenticationDetailsS​​ource 添加到 OAuth2 登录 Kotlin DSL</li> 
 <li>将 Kotlin 示例添加到参考文档中</li> 
 <li>添加 InvalidSessionStrategy 的 RequestedUrlRedirectInvalidSessionStrategy 实现</li> 
 <li>在访问令牌响应中添加对任何数据类型的支持</li> 
 <li>允许在 saml2Login Kotlin DSL 中配置 AuthenticationManager</li> 
 <li>允许在一个方法上添加多个安全注释（将评估结果与 AND 运算符组合）</li> 
 <li>DigestAuthenticationFilter 只解码一次随机数</li> 
 <li>HttpSecurity DSL 应该接受一个 AuthenticationManager</li> 
 <li>HttpSecurityConfigurer 应该有一个用于 authorizeHttpRequests 的无参数方法</li> 
 <li>改进 InMemoryUserDetailsManager 中无效属性的错误消息</li> 
 <li>在 DNS SRV 类型查找中包含端口</li> 
 <li>引入 samplesBranch 属性</li> 
 <li>当对象被签名时，将 KeyInfo 作为签名对象的一部分提供</li> 
 <li>删除 DependencySetPlugin</li> 
 <li>删除 PowerMock 依赖</li> 
 <li>在 Javadoc 中用 &lt 和 &gt 替换 < 和 ></li> 
 <li>默认在 WebSessionOAuth2ServerAuthorizationRequestRepository 中存储一个请求</li> 
 <li>支持 RsaKeyConverters 中的 X509 证书</li> 
 <li>直接使用 GPG_PRIVATE_KEY</li> 
 <li>在文档的链接中使用新的 springFrameworkVersion 属性</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F19%2Fspring-security-5-6-0-m1-released" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            