
---
title: 'JAP 1.0.1 以及 《JAP产品技术白皮书》正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4293b3dd863516ed591ba3610da15bb90be.JPEG'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 13:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4293b3dd863516ed591ba3610da15bb90be.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>JAP 1.0.1 以及 《JAP产品技术白皮书》正式发布</h1> 
<h2>快讯</h2> 
<blockquote> 
 <ol> 
  <li style="text-align:left"><span style="color:#3f3f3f">JAP 1.0.1 正式发布</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">《JAP产品技术白皮书》正式发布。立即获取：<span style="color:#576b95">白皮书[1]</span></span></li> 
 </ol> 
</blockquote> 
<h1>JAP 1.0.1 版本内容</h1> 
<h2>新增功能/支持</h2> 
<ul> 
 <li style="text-align:left"><span style="color:#3f3f3f">添加 <code>com.fujieid.jap.core.util.RequestUtil</code></span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f">完成<code>jap-ids</code>模块</span></li> 
</ul> 
<blockquote> 
 <p style="text-align:left"><code>jap-ids</code> 是基于 <span style="color:#576b95">RFC6749[2]</span>、<span style="color:#576b95">RFC7636[3]</span>、<span style="color:#576b95">RFC7033[4]</span>等标准协议和 <span style="color:#576b95">OpenID Connect Core 1.0[5]</span> 认证协议，实现的一款轻量级、业务解耦、开箱即用的新一代国产授权认证框架。</p> 
</blockquote> 
<blockquote> 
 <p style="text-align:left"><strong>jap-ids 目前已支持以下功能：</strong></p> 
 <ul> 
  <li style="text-align:left"><span style="color:#3f3f3f">授权码模式（Authorization Code Grant）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">授权码-PKCE模式（Proof Key for Code Exchange）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">隐式授权模式（Implicit Grant）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">密码授权模式（Resource Owner Password Credentials Grant）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">客户端授权模式（Client Credentials Grant）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">刷新 access_token</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">回收 access_token</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">获取当前授权用户的基本信息</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">校验登录状态</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">异常响应</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">退出登录</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">服务发现（OpenID Connect Discovery）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">JWK 端点（JWKS）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">JWK 令牌颁发</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">自定义 JWT 加解密证书</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">全场景 response type 支持（<code>code</code>、<code>token</code>、<code>id_token</code>、<code>id_token token</code>、<code>code id_token</code>、<code>code token</code>、<code>code id_token token</code>）</span></li> 
  <li style="text-align:left"><span style="color:#3f3f3f">等</span></li> 
 </ul> 
</blockquote> 
<p style="text-align:left">关于 <code>jap-ids</code> 的更多使用详情，请参考示例项目：<span style="color:#576b95">jap-ids-demo[6]</span>，或者查阅文档：<span style="color:#576b95">IDS OAuth 2.0 服务端[7]</span></p> 
<h2>代码修改/优化</h2> 
<ul> 
 <li style="text-align:left"><span style="color:#3f3f3f">[jap-oidc] 优化 <code>OidcStrategy#authenticate</code> 方法，缓存 <code>OidcDiscoveryDto</code>，减少不必要的 http 请求</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f">[jap-oidc] 优化 <code>OidcUtil</code> 工具类的代码，解决一些已知问题</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f">[jap-social] 解决一些已知问题</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f">重构 <code>com.fujieid.jap.core.cache.JapLocalCache</code>，实现定时器，定期清理本地缓存</span></li> 
</ul> 
<h2>合并 PR</h2> 
<p style="text-align:left"><span style="color:#3f3f3f">合并 Gitee PR <span style="color:#576b95">#9[8]</span> by <span style="color:#576b95">@dreamlu[9]</span></span></p> 
<h2>Issue</h2> 
<p style="text-align:left"><span style="color:#3f3f3f">解决 Gitee Issue <span style="color:#576b95">#I3DC7N[10]</span></span></p> 
<h1>JAP 产品技术白皮书</h1> 
<p style="text-align:left">经过两个月的整理、修改、迭代，我们 JAP 的技术白皮书，终于完成了！</p> 
<p style="text-align:left"><img alt height="213" src="https://oscimg.oschina.net/oscnet/up-4293b3dd863516ed591ba3610da15bb90be.JPEG" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">在 “JAP 社区交流群”中，不少朋友都期待着《<span style="color:#576b95">JAP 产品技术白皮书[11]</span>》的发布。</p> 
<p style="text-align:left">前期我们也做过一些调研，大部分开发者/用户的述求基本上是：JAP 文档中有太多专有技术名词，理解起来比较困难。针对此，我们在白皮书中对于 JAP 相关领域的概念、名词做了专门解释，能够帮助开发者/用户更深入的了解、使用相关技术。</p> 
<p style="text-align:left">同时，在此份白皮书中，我们对 JAP 的功能、特点、架构、流程等都做了全面的、详细的解释，部分内容如下：</p> 
<p style="text-align:left"><img height="929" src="https://oscimg.oschina.net/oscnet/up-6fb3621dbd1bf24719fffd225748f3af246.png" width="698" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="928" src="https://oscimg.oschina.net/oscnet/up-00cf4a7956cf3ce723a59868854a0b354a0.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">希望这份白皮书，能够帮助到各位开发者/用户。</p> 
<h1>关于 JAP</h1> 
<h2>JAP 是什么？</h2> 
<p style="text-align:left">JAP 是一款开源的登录认证中间件，基于模块化设计，为所有需要登录认证的 WEB 应用提供一套标准的技术解决方案，开发者可以基于 JAP 适配绝大多数的 WEB 系统（自有系统、联邦协议）。</p> 
<h2>JAP 有哪些功能？</h2> 
<p style="text-align:left"><img src="https://gitee.com/fujieid/jap/raw/master/docs/media/01c3231f.png" referrerpolicy="no-referrer"></p> 
<h2>JAP 有什么优势？</h2> 
<ul> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>易用性</strong>：JAP 的 API 沿袭 JustAuth 的简单性，做到了开箱即用的程度。JAP 高度抽象各种登录场景，提供了多套简单使用的 API，极大程度的降低了开发者的学习成本和使用成本</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>全面性</strong>：JAP 全量适配 JustAuth 支持的第三方平台，实现第三方登录。同时也支持所有基于标准OAuth2.0 协议或者 OIDC 协议或者 SAML 协议的应用、系统，同时 JAP 还提供不同语言版本的项目 SDK，适配多种研发场景</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>模块化</strong>：JAP 基于模块化设计开发，针对每一种登录场景，比如账号密码、OAuth、OIDC等，都单独提供了独有的模块化解决方案</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>标准化</strong>：JAP 和业务完全解耦，将登录认证相关的逻辑抽象出一套标准的技术解决方案，针对每一种业务场景，比如用户登录、验证密码、创建并绑定第三方系统的账号等，都提供了一套标准的策略或者接口，开发者可以基于 JAP，灵活并方便的完成相关业务逻辑的开发和适配</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>通用性</strong>：JAP 不仅可以用到第三方登录、OAuth授权、OIDC认证等业务场景，还能适配开发者现有的业务系统的普通账号密码的登录场景，基本将所有登录相关的业务场景都已经涵盖。针对 WEB 应用，JAP 将提供满足各种不同登录场景的解决方案（和开发语言无关）</span></li> 
</ul> 
<h2>JAP 适用于哪些场景？</h2> 
<p style="text-align:left">JAP 适用于所有需要登录认证功能的场景。比如：</p> 
<ul> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>要求规范</strong>：新项目立项，你们需要研发一套包含登录、认证的系统，并且从长远方面考虑，你们需要一套标准的、灵活的、功能全面的登录认证功能。</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>需求灵活</strong>：现有登录模块为自研，但是新一轮的技术规划中，你们想将登录认证模块重构，以更加灵活的架构适应后面的新需求，比如：集成 MFA 登录、集成 OAuth 登录、SAML登录等。</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>力求省事</strong>：你们的项目太多（或者是开发语言较多，比如：Java、Python、Node 等），每个项目都需要登录认证模块，想解决这种重复劳动的问题，使研发人员有更多的时间和精力投入到业务开发中，提高研发产能和研发效率。</span></li> 
</ul> 
<p style="text-align:left">关于 JAP 的更多内容，可以参考《<span style="color:#576b95">JAP 产品技术白皮书[12]</span>》</p> 
<h2>相关链接</h2> 
<ul> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>Gitee</strong>：https://gitee.com/fujieid/jap</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>Github</strong>：https://github.com/fujieid/jap</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>CodeChina</strong>：https://codechina.csdn.net/fujieid/jap</span></li> 
 <li style="text-align:left"><span style="color:#3f3f3f"><strong>开发者文档</strong>：https://justauth.plus</span></li> 
</ul> 
<h4 style="text-align:left">引用链接</h4> 
<p style="text-align:left"><code>[1]</code> 白皮书: <em>https://justauth.plus/paper/JAP-paper-V1.0.0.pdf</em><br> <code>[2]</code> RFC6749: <em>https://tools.ietf.org/html/rfc6749</em><br> <code>[3]</code> RFC7636: <em>https://tools.ietf.org/html/rfc7636</em><br> <code>[4]</code> RFC7033: <em>https://tools.ietf.org/html/rfc7033</em><br> <code>[5]</code> OpenID Connect Core 1.0: <em>https://openid.net/specs/openid-connect-core-1_0.html</em><br> <code>[6]</code> jap-ids-demo: <em>https://gitee.com/fujieid/jap-ids-demo</em><br> <code>[7]</code> IDS OAuth 2.0 服务端: <em>https://justauth.plus/ids/</em><br> <code>[8]</code> #9: <em>https://gitee.com/fujieid/jap/pulls/9</em><br> <code>[9]</code> @dreamlu: <em>https://gitee.com/dreamlu</em><br> <code>[10]</code> #I3DC7N: <em>https://gitee.com/fujieid/jap/issues/I3DC7N</em><br> <code>[11]</code> JAP 产品技术白皮书: <em>https://justauth.plus/paper/JAP-paper-V1.0.0.pdf</em><br> <code>[12]</code> JAP 产品技术白皮书: <em>https://justauth.plus/paper/JAP-paper-V1.0.0.pdf</em></p>
                                        </div>
                                      
</div>
            