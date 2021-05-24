
---
title: 'JAP 1.0.2 正式发布，jap-ids 支持多租户、适配前后端分离、自定义授权流程等新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://img1.sycdn.imooc.com/60ab05a5000104e212190881.jpg'
author: 开源中国
comments: false
date: Mon, 24 May 2021 09:56:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img1.sycdn.imooc.com/60ab05a5000104e212190881.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <h1>JAP 1.0.2 正式发布</h1> 
</div> 
<div style="text-align:start"> 
 <h2>概要</h2> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <ol> 
   <li><code>jap-ids</code> 1.0.2 支持多租户场景、支持动态 <code>issuer</code>、支持前后端分离的业务场景；</li> 
   <li><code>jap-social</code> 对外提供 <code>refreshToken</code>、<code>revokeToken</code> 和 <code>getUserInfo</code> 方法；</li> 
   <li>新增 <code>Pipeline</code> 模式，支持自定义部分业务场景的流程，同时引入 <code>SPI</code> 机制；</li> 
   <li>基于 Github Action，JAP 正式启用快照版，比如：<code>1.0.2-SNAPSHOT</code>。（快照版实时更新，但不可用于生产环境）</li> 
   <li>使用 <code>jap-bom</code> 管理项目版本依赖，使用 <code>flatten-maven-plugin</code> 简化 pom 版本</li> 
   <li>JustAuth 和 JAP 项目已经加入 “<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjustauth.wiki%2Fresource%2Fsummer2021.html" target="_blank">开源软件供应链点亮计划 - 暑期2021</a>”，欢迎各位在校学生踊跃参与！</li> 
  </ol> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <h1>JAP 1.0.2 版本更新内容</h1> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <p>本次更新涉及到字段、方法返回类型的修改，请升级的时候注意。可以参照本文下方的更新说明进行修改、调整。</p> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <h2>新功能/特性</h2> 
</div> 
<div style="text-align:start"> 
 <h3><strong>jap-ids</strong> 模块</h3> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>在<code>IdsConfig</code>中添加 <code>enableDynamicIssuer</code> 属性，<code>boolean</code> 类型。当 <code>enableDynamicIssuer=true</code> 时，开发者不再需要单独设置 <code>issuer</code>，<code>jap-ids</code> 将从当前请求的域名中自动提取 <code>issuer</code>。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <p>此功能针对客户端支持<code>自定义域名</code>的业务场景。可以通过域名的标识（比如二级域名<code>jap.justauth.plus</code> 中的标识就是 <code>jap</code>）确定用户所属的客户端（也可以对应到租户）。</p> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>在<code>IdsConfig</code> 中添加 <code>loginPageUrl</code> 属性，<code>loginPageUrl</code> 与 <code>loginUrl</code> 的区别：</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <ul> 
   <li><code>loginPageUrl</code>：登录表单页面 URL，关键字：<strong>页面</strong>。</li> 
   <li><code>loginUrl</code>：登录的api URL，关键字：<strong>API</strong>。</li> 
  </ul> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>在<code>IdsConfig</code>中添加 <code>externalLoginPageUrl</code> 属性，<code>boolean</code> 类型。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <p>如果授权服务未提供登录页面（登录页面由其他服务托管，比如登录页面在单独的静态服务中部署），则需要启用此配置。</p> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>在<code>IdsConfig</code>中添加 <code>externalConfirmPageUrl</code> 属性，<code>boolean</code> 类型。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <p>如果授权服务未提供授权确认页面（授权确认页面由其他服务托管，比如授权确认页面在单独的静态服务中部署），则需要启用此配置。</p> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>在<code>IdsConfig</code>中添加 <code>authorizeAutoApproveUrl</code> 属性。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <p>当授权 URL 中包含 <code>autoapprove=true</code> 时，授权服务器在用户登录完成后，不会跳转到 <code>confirmPageUrl</code>，而是直接跳转到 <code>authorizeAutoApproveUrl</code>。</p> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>添加 <code>IdsUserStoreService</code> 接口类，以支持登录后对用户数据的自定义操作，默认为 <code>Session</code> 存储用户信息。<strong>感谢微信用户（antscqy）的建议</strong>。</li> 
  <li>添加 <code>IdsPipeline</code> 接口，开发人员可以自定义流程，目前仅支持自定义 <code>IdsxxFilter</code>（过滤器）和 <code>LoginEndpoint</code> 的流程。</li> 
  <li>添加 <code>spi</code> 插件机制，<code>jap-ids</code> 对外提供的接口，都可以以 <code>spi</code> 的形式实现。</li> 
  <li>添加以下内置 scope：<code>profile</code>, <code>address</code>, <code>read</code> and <code>write</code>。</li> 
  <li>在 <code>OauthUtil#createAuthorizeUrl(String, IdsRequestParam)</code> 中添加 <code>uid</code> 参数（可选的参数）。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <h3><strong>jap-social</strong> 模块</h3> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li><code>SocialStrategy</code> 对外提供 <code>refreshToken</code>、<code>revokeToken</code> 和 <code>getUserInfo</code> 方法。感谢群友的反馈。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <h2>修改</h2> 
</div> 
<div style="text-align:start"> 
 <h3>POM 依赖</h3> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>将 <code>javax.servlet-api</code> 依赖替换为 <code>jakarta.servlet-api</code>。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <h3><strong>jap-ids</strong> 模块</h3> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>将 <code>IdsConfig.confirmUrl</code> 参数名称修改为 <code>confirmPageUrl</code>。</li> 
  <li>将 <code>ApprovalEndpoint#getAuthClientInfo(HttpServletRequest)</code> 的返回类型修改为<code>IdsResponse<String, Map<String, Object>></code>。</li> 
  <li>将 <code>Ap provalEndpoint#authorize(HttpServletRequest)</code> 的返回类型修改为 <code>IdsResponse<String, String></code>。</li> 
  <li>将 <code>AuthorizationEndpoint#agree(HttpServletRequest)</code> 的返回类型修改为 <code>IdsResponse<String, String></code>。</li> 
  <li>将 <code>LoginEndpoint#signin(HttpServletRequest)</code> 的返回类型修改为 <code>IdsResponse<String, String></code>。</li> 
  <li>将 <code>LogoutEndpoint#logout(HttpServletRequest)</code> 的返回类型修改为 <code>IdsResponse<String, String></code>。</li> 
  <li>修改 <code>ClientDetail</code> 类的注释。</li> 
  <li>将 <code>IdsResponse#getData()</code> 方法的返回类型修改为<strong>泛型</strong>。</li> 
  <li>删除 <code>IdsScopeProvider#initScopes(List<IdsScope>)</code> 方法，不再允许重置系统内置的 scope，新版 <code>jap-ids</code> 支持添加新的 <code>scope</code> 以及 修改内置的 <code>scope</code> 描述。</li> 
  <li>当<code>response_type=id_token</code>时，<code>id_token</code> 中将返回用户的基本信息（依据 <code>scope</code> 授权范围）。</li> 
  <li>优化 <code>UserInfoEndpoint#getCurrentUserInfo(HttpServletRequest)</code> 方法的业务流程，对于用户的特定属性，比如手机号、邮箱等，按照提供的 <code>scope</code> 决定是否返回。</li> 
  <li>修改 <code>IdsUserService</code> 接口的<code>loginByUsernameAndPassword</code> 和 <code>getByName</code> 方法，分别新增了 <code>clientId</code> 入参。</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <blockquote> 
  <p>针对多租户场景下，同一个用户可能存在多个租户主体下，单纯依靠用户账密已经<strong>无法唯一确定一个用户</strong>，这种情况下业务系统可以根据 <code>clientId</code> 获取具体的租户下的用户信息。</p> 
 </blockquote> 
</div> 
<div style="text-align:start"> 
 <h3>PR</h3> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>合并 Gitee PR <a href="https://gitee.com/fujieid/jap/pulls/11">#11</a> by <a href="https://gitee.com/dreamlu">@dreamlu</a>。使用 <code>flatten-maven-plugin</code> 简化 pom 版本</li> 
  <li>合并 Gitee PR <a href="https://gitee.com/fujieid/jap/pulls/12">#12</a> by <a href="https://gitee.com/sywd">@sywd</a>。添加 <code>jap-bom</code> 管理项目版本依赖</li> 
  <li>合并 Gitee PR <a href="https://gitee.com/fujieid/jap/pulls/13">#13</a> by <a href="https://gitee.com/dreamlu">@dreamlu</a>。代码优化，方便作为 Spring bean 初始化</li> 
  <li>合并 Gitee PR <a href="https://gitee.com/fujieid/jap/pulls/14">#14</a> by <a href="https://gitee.com/dreamlu">@dreamlu</a>。优化 pom 配置，修复 <code>jap-bom</code> 导入问题</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <h1>关于 JAP</h1> 
</div> 
<div style="text-align:start"> 
 <h2>JAP 是什么？</h2> 
</div> 
<div style="text-align:start"> 
 <p>JAP 是一款开源的登录认证中间件，基于模块化设计，为所有需要登录认证的 WEB 应用提供一套标准的技术解决方案，开发者可以基于 JAP 适配绝大多数的 WEB 系统（自有系统、联邦协议）。</p> 
</div> 
<div style="text-align:start"> 
 <h2>JAP 有哪些功能？</h2> 
</div> 
<div style="text-align:start"> 
 <p><img alt="JAP 开源的统一登录认证标准组件 - 包含的功能" src="https://cors.zfour.workers.dev/?http://img1.sycdn.imooc.com/60ab05a5000104e212190881.jpg" referrerpolicy="no-referrer"></p> 
</div> 
<div style="text-align:start"> 
 <h2>JAP 有什么优势？</h2> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li><strong>易用性</strong>：JAP 的 API 沿袭 JustAuth 的简单性，做到了开箱即用的程度。JAP 高度抽象各种登录场景，提供了多套简单使用的 API，极大程度的降低了开发者的学习成本和使用成本</li> 
  <li><strong>全面性</strong>：JAP 全量适配 JustAuth 支持的第三方平台，实现第三方登录。同时也支持所有基于标准OAuth2.0 协议或者 OIDC 协议或者 SAML 协议的应用、系统，同时 JAP 还提供不同语言版本的项目 SDK，适配多种研发场景</li> 
  <li><strong>模块化</strong>：JAP 基于模块化设计开发，针对每一种登录场景，比如账号密码、OAuth、OIDC等，都单独提供了独有的模块化解决方案</li> 
  <li><strong>标准化</strong>：JAP 和业务完全解耦，将登录认证相关的逻辑抽象出一套标准的技术解决方案，针对每一种业务场景，比如用户登录、验证密码、创建并绑定第三方系统的账号等，都提供了一套标准的策略或者接口，开发者可以基于 JAP，灵活并方便的完成相关业务逻辑的开发和适配</li> 
  <li><strong>通用性</strong>：JAP 不仅可以用到第三方登录、OAuth授权、OIDC认证等业务场景，还能适配开发者现有的业务系统的普通账号密码的登录场景，基本将所有登录相关的业务场景都已经涵盖。针对 WEB 应用，JAP 将提供满足各种不同登录场景的解决方案（和开发语言无关）</li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <h2>JAP 适用于哪些场景？</h2> 
</div> 
<div style="text-align:start"> 
 <p>JAP 适用于所有需要登录认证功能的场景。比如：</p> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li> <p><strong>要求规范</strong>：新项目立项，你们需要研发一套包含登录、认证的系统，并且从长远方面考虑，你们需要一套标准的、灵活的、功能全面的登录认证功能。</p> </li> 
  <li> <p><strong>需求灵活</strong>：现有登录模块为自研，但是新一轮的技术规划中，你们想将登录认证模块重构，以更加灵活的架构适应后面的新需求，比如：集成 MFA 登录、集成 OAuth 登录、SAML登录等。</p> </li> 
  <li> <p><strong>力求省事</strong>：你们的项目太多（或者是开发语言较多，比如：Java、Python、Node 等），每个项目都需要登录认证模块，想解决这种重复劳动的问题，使研发人员有更多的时间和精力投入到业务开发中，提高研发产能和研发效率。</p> <p>关于 JAP 的更多内容，可以参考《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjustauth.plus%2Fpaper%2FJAP-paper-V1.0.0.pdf" target="_blank">JAP 产品技术白皮书</a>》</p> </li> 
 </ul> 
</div> 
<div style="text-align:start"> 
 <h2>相关链接</h2> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li><strong>Gitee</strong>：<a href="https://gitee.com/fujieid/jap">https://gitee.com/fujieid/jap</a></li> 
  <li><strong>Github</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffujieid%2Fjap" target="_blank">https://github.com/fujieid/jap</a></li> 
  <li><strong>CodeChina</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodechina.csdn.net%2Ffujieid%2Fjap" target="_blank">https://codechina.csdn.net/fujieid/jap</a></li> 
  <li><strong>开发者文档</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjustauth.plus%2F" target="_blank">https://justauth.plus</a></li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            