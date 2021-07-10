
---
title: '统一认证授权平台keycloak太牛了，我要搞一搞'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09b5093239084838adb3b27e5bfc73d5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 17:10:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09b5093239084838adb3b27e5bfc73d5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09b5093239084838adb3b27e5bfc73d5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最近想要打通几个应用程序的用户关系，搞一个集中式的用户管理系统来统一管理应用的用户体系。经过一番调研选中了红帽开源的<strong>Keycloak</strong>，这是一款非常强大的统一认证授权管理平台。之所以选中了<strong>Keycloak</strong>是基于以下几个原因。</p>
<h2 data-id="heading-0">易用性</h2>
<p><strong>Keycloak</strong>为Web应用和Restful服务提供了一站式的单点登录解决方案。它的目标就是让应用的安全管理变得简单，让开发人员可以轻松地保护他们的应用程序和服务。并且Keycloak为登录、注册、用户管理提供了可视化管理界面，你可以借助于该界面来配置符合你需要的安全策略和进行用户管理。 而且还可以</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67bb2eebe4c74c8b896343ba3536e1fe~tplv-k3u1fbpfcp-zoom-1.image" alt="登录界面" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f24879a36ec479c9a2d431a939baa68~tplv-k3u1fbpfcp-zoom-1.image" alt="可配置的GUI管理" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">功能强大</h2>
<p><strong>Keycloak</strong>实现了业内常见的认证授权协议和通用的安全技术，主要有：</p>
<ul>
<li>浏览器应用程序的单点登录（SSO）。</li>
<li>OIDC认证授权。</li>
<li>OAuth 2.0。</li>
<li>SAML。</li>
<li>多租户支持。</li>
<li>身份代理 - 使用外部 OpenID Connect 或 SAML 身份提供商进行身份验证。</li>
<li>第三方登录。</li>
<li>用户联盟 - 从 LDAP 和 Active Directory 服务器同步用户。</li>
<li>Kerberos 网桥 - 自动验证登录到 Kerberos 服务器的用户。</li>
<li>用于集中管理用户、角色、角色映射、客户端和配置的管理控制台。</li>
<li>用户账户集中管理的管理控制台。</li>
<li>自定义主题。</li>
<li>两段身份认证。</li>
<li>完整登录流程 - 可选的用户自注册、恢复密码、验证电子邮件、要求密码更新等。</li>
<li>会话管理 - 管理员和用户自己可以查看和管理用户会话。</li>
<li>令牌映射 - 将用户属性、角色等映射到令牌和语句中。</li>
<li>安全策略恢复功能。</li>
<li>CORS 支持 - 客户端适配器具有对 CORS 的内置支持。</li>
<li>自定义SPI接口扩展。</li>
<li>JavaScript 应用程序、WildFly、JBoss EAP、Fuse、Tomcat、Jetty、Spring 等客户端适配器。</li>
<li>支持任何具有 OpenID Connect Relying Party 库或 SAML 2.0 Service Provider 库的平台/语言。</li>
</ul>
<blockquote>
<p>而且有专门的Spring Boot Starter，非常容易集成到Spring Boot中。</p>
</blockquote>
<h2 data-id="heading-2">基于实践的开源</h2>
<p>红帽出品，必属精品。红帽良好的口碑决定了<strong>Keycloak</strong>的可靠性。它遵循<strong>Apache 2.0</strong>开源协议进行开源，经过八年的持续开源，代码质量很高，非常适合做定制化开发。红帽的商业付费认证授权产品<strong>Red Hat SSO</strong>就是基于<strong>Keycloak</strong>。为企业提供了动态单点登录的解决方案，间接证明了<strong>Keycloak</strong>的可靠性。</p>
<h2 data-id="heading-3">适配Spring Security</h2>
<p>这个框架对<strong>Spring Security</strong>和<strong>Spring Boot</strong>做了适配，非常适合使用了这两种体系的迁移扩展。这也是我选择它的重要原因之一。</p>
<h2 data-id="heading-4">缺点</h2>
<p>虽然优点非常多，但是缺点也很明显。功能强大就意味着架构比较复杂，概念比较多，学习成本比较高。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1d667ab034b498a9fb717198b1aca61~tplv-k3u1fbpfcp-zoom-1.image" alt="KeyClock的核心概念" loading="lazy" referrerpolicy="no-referrer"></p>
<p>学习成本比较高的另一个原因是中文资料比较少，需要自己去啃官方的文档。对于业务需要的认证方式可能会需要自行实现一些接口，同样考验着个人的编码能力。</p>
<h2 data-id="heading-5">最后</h2>
<p>胖哥对这个东西关注了很久却没有下手，第一是因为它确实有挑战性，第二没有实际的开发场景，现在机会来了，今天对这个框架进行一个简单的介绍，让不了解它的同学先简单了解一下。如果你对<strong>Keycloak</strong>进行了详细的研究和实践，基本上能够搞定一些大中型的应用安全体系构建，既有诱惑也有挑战。另外这个程序适合做统一认证授权门户构建，不太适合一些小应用，相对比较重，不过微服务用这个应该非常棒。在目前新的Spring认证服务器还没有达到生产可用时是一个不错的选择。所以后续会和大家一起研究学习这个东西，感兴趣的朋友可以多多关注：码农小胖哥。</p>
<p><code>关注公众号：Felordcn获取更多资讯</code></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ffelord.cn" target="_blank" rel="nofollow noopener noreferrer" title="https://felord.cn" ref="nofollow noopener noreferrer">个人博客：https://felord.cn</a></p></div>  
</div>
            