
---
title: '聊聊单点登录(SSO)中的CAS认证'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c967cd85751e4e739cd8455286c86302~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 15 Sep 2022 03:30:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c967cd85751e4e739cd8455286c86302~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">SSO介绍</h2>
<h3 data-id="heading-1">背景</h3>
<ul>
<li>随着企业的发展，一个大型系统里可能包含 n 多子系统,  用户在操作不同的系统时，需要多次登录，很麻烦，我们需要一种<strong>全新的登录方式来实现多系统应用群的登录，这就是单点登录</strong>。</li>
<li>web 系统 由单系统发展成<strong>多系统组成的应用群</strong>，复杂性应该由<strong>系统内部</strong>承担，而不是用户。无论 web 系统内部多么复杂，对用户而言，都是一个统一的整体，也就是说，用户访问 web 系统的整个应用群与访问单个系统一样，登录/注销 只要1次就够了</li>
</ul>
<p align="center"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c967cd85751e4e739cd8455286c86302~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">SSO 定义</h3>
<ul>
<li><strong>SSO（Single sign-on）</strong> 即单点登录，一种对于许多相互关联，但是又是各自独立的软件系统，提供访问控制的方法</li>
<li><strong>SSO（Single sign-on）</strong> 是比较流行的企业业务整合的解决方案之一。<strong>SSO（Single sign-on）</strong> 定义是在多个应用系统中，<strong>用户只需要登录一次就可以访问所有相互信任的应用系统</strong></li>
</ul>
<blockquote>
<p>以游乐场的通票为例：</p>
</blockquote>
<p>我们只要买一次通票，就可以玩所有游乐场内的设施，而不需要在过山车或者摩天轮那里重新买一次票。在这里，买票就相当于登录认证，游乐场就相当于使用一套 SSO 的公司，各种游乐设施就相当于公司的各个产品。</p>
<p align="center"><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31a65f636e2c4c03af8a740fc85e3474~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
> **类比到各个子系统认证，如图**
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cb8ecbdf48f4bf48fe5349638d40d20~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">SSO 三种类型</h2>
<ul>
<li>
<p><strong>各子系统在同一个站点下</strong></p>
</li>
<li>
<p><strong>各子系统在相同的顶级域名下</strong></p>
<p>同一个站点和相同顶级域下的单点登录是利用了 <strong>Cookie</strong> 顶域共享的特性。目前数栈都是只需要在 <strong>UIC</strong> 的登录页面进行一次登录就可以在各个子应用之间进行跳转，这种操作源于根据设置 <strong>Cookie</strong> 中的 <strong>domain</strong> 为顶级域名。</p>
</li>
<li>
<p><strong>各子系统属于不同的顶级域</strong></p>
<p>如果属于不同的域，不同域之间的 <strong>Cookie</strong> 是不共享的。怎么办？接下来就要说一说 <strong>CAS (Central Authentication Service)</strong> 流程了，这个流程是<strong>单点登录</strong>的标准流程</p>
</li>
</ul>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fapereo.github.io%2Fcas%2F6.5.x%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://apereo.github.io/cas/6.5.x/index.html" ref="nofollow noopener noreferrer">CAS (Central Authentication Service)</a></h2>
<h3 data-id="heading-5">CAS 是什么</h3>
<p>  <strong>Central Authentication Service</strong> ——— 中央认证服务，是 <strong>Yale</strong> 大学发起的一个企业级的、开源的项目，旨在为 <strong>Web 应用</strong>系统提供一种可靠的 <strong>SSO</strong> 解决方案。只是 <strong>SSO</strong> 解决方案的一种，它的流程其实跟 <strong>Cookie-session</strong> 模式是一样的，单点登录等于说是每个子系统都拥有一套完整的 <strong>Cookie-session</strong> 模式，再加上一套 <strong>Cookie-session</strong> 模式的 <strong>SSO 系统</strong>。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b356c1025e59418c88153cdce2c4413d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第一次访问 APP1:</strong></p>
<ol>
<li>用户访问 <strong>APP1</strong>，需要登录的时候会重定向到 <strong>CAS Server</strong></li>
<li>在 <strong>CAS Server</strong> 进行账号密码认证，<strong>CAS Server</strong> 会保存 <strong>session</strong>，并生成 <strong>sessionId</strong> 返回给 <strong>SSO Client，SSO Client</strong> 写入当前域的 <strong>Cookie</strong>，同时根据 <strong>TGT</strong> 签发1个 <strong>ST</strong> 传入 <strong>APP1</strong></li>
<li><strong>APP1</strong> 携带  <strong>ST</strong> 向 <strong>CAS Server 请求校验</strong></li>
<li><strong>CAS Server</strong> 校验成功后，返回 登录态给 <strong>APPI</strong> 服务端</li>
<li><strong>APPI</strong> 服务端 将 登陆态写入 <strong>session</strong> 并生成 <strong>sessionId</strong> 返回给 <strong>APPI Client</strong></li>
<li>之后再做登录认证，就是同域下的认证了</li>
</ol>
<p><strong>第一次访问 APP2:</strong></p>
<ol>
<li>用户访问系统 <strong>APP2</strong>，当跳到 <strong>SSO</strong> 里准备登录的时候发现 <strong>SSO</strong> 已经登录了，那 <strong>SSO</strong> 生成一个 <strong>ST</strong>，携带该 <strong>ST</strong> 传入 <strong>APP2</strong></li>
<li><strong>APP2</strong> 携带 <strong>ST</strong> 向 <strong>CAS Server</strong> 请求校验</li>
<li><strong>CAS Server</strong> 校验成功后，返回 登录态给 <strong>APP2</strong> 服务端</li>
<li><strong>APP2</strong> 服务端 将 登陆态写入 <strong>session</strong> 并生成 <strong>sessionId</strong> 返回给 <strong>APPI Client</strong></li>
<li>在这个流程里，<strong>APP2</strong> 就不用走登录流程了</li>
</ol>
<h3 data-id="heading-6">CAS 票据</h3>
<p><strong>TGT</strong></p>
<p> <strong>CAS Server <strong>创建</strong>TGT</strong>，存在 <strong>CAS Server</strong> 的 <strong>Session</strong> 里面，根据用户信息签发的</p>
<p><strong>TGC</strong></p>
<p> 创建 <strong>TGT</strong> 的同时，生成 <strong>TGC</strong>。通过 <strong>CAS Server</strong> 的 <strong>response header</strong> 的 set-cookie 字段设置 <strong>TGC</strong>，唯一标识用户身份（<strong>sessionId</strong>) <strong>ST</strong></p>
<p><strong>ST</strong></p>
<p> 根据 <strong>TGT</strong> 签发的 <strong>ST</strong>，是 <strong>CAS</strong> 为用户签发的访问某一 <strong>service</strong> 的票据</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80fa9fac4f174585a4cd634504fb7332~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">CAS 单点登录(SSO) &  单点登出(SLO)</h3>
<h4 data-id="heading-8">单点登录(SSO)</h4>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e8d855819894c3fa1f8ba85ead37cb2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第一次访问 APP1:</strong></p>
<ol>
<li>访问 <strong>APP1</strong> 服务地址，<strong>APP1</strong> 请求未通过认证，重定向至 <strong>CAS Server</strong> 地址。</li>
<li>访问 <strong>CAS Server</strong> 地址，发送认证请求，带上 <strong>Cookie</strong>。</li>
<li><strong>CAS Server</strong> 识别出用户没有 <strong>Cookie</strong> 信息，没有登录，返回 <strong>CAS</strong> 登陆页地址。</li>
<li>用户输入正确的账户密码，<strong>CAS Server</strong> 用户认证通过，创建 <strong>SSO Session</strong>。</li>
<li>重定向回 <strong>APP1</strong> 的服务地址，并在 <strong>cookie</strong> 中创建了 <strong>CASTGC</strong>，<strong>TGC</strong> 中包含了 <strong>Ticket（TGT）</strong>，<strong>TGT</strong> 就是 <strong>SSO Session</strong> 的 <strong>key</strong>。</li>
<li>访问 <strong>APP1</strong> 的服务地址，并带上 <strong>ST</strong>，客户端拿到 <strong>ST</strong> 向<strong>CAS Server</strong>进行认证。</li>
<li><strong>CAS Server</strong> 认证成功，返回响应信息给 <strong>APPI</strong></li>
<li><strong>APPI</strong> 拿到成功的响应后，设置 <strong>Session</strong>，并重定向回 <strong>APP1</strong> 的地址，并设置 <strong>Cookie JSESSIONID</strong>。</li>
<li><strong>APPI</strong> 发起请求，带上 <strong>Cookie</strong> 中的信息，其中 <strong>JSESSIONID</strong> 用来确定当前用户所对应的 <strong>session</strong> 信息，发送给客户端进行校验。</li>
<li>客户端使用 <strong>JSESSIONID</strong> 与 <strong>Session</strong> 中存储的数据进行校验。</li>
<li>校验通过，返回正确的内容，展示 <strong>APP1</strong></li>
</ol>
<p><strong>第二次访问 APP1:</strong></p>
<ol>
<li><strong>APPI</strong> 发起请求，并带上 <strong>Cookie</strong> 中的 <strong>JSESSIONID</strong> 给 <strong>APPI 服务端。</strong></li>
<li><strong>APPI 服务端</strong> 使用 <strong>JSESSIONID</strong> 与 <strong>Session</strong> 中存储的数据进行校验。</li>
<li>校验通过，返回正确的内容，展示 <strong>APP1</strong> 。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3264e5b6f18444cb700616d6904fcf8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>在 APP1 登陆成功的情况下，第一次访问 APP2:</strong></p>
<ol>
<li>访问 <strong>APP2</strong> 服务地址，<strong>APP2</strong> 请求未通过认证，重定向至 <strong>CAS Server</strong> 地址。</li>
<li>访问 <strong>CAS Server</strong> 地址，发送认证请求，带上 <strong>TGT</strong> 信息。</li>
<li><strong>CAS Server</strong> 通过 <strong>TGT</strong> 去查找 <strong>SSO</strong> 的信息进行认证。</li>
<li>认证通过，生成票据 <strong>ST</strong> 重定向至 <strong>APP2</strong> 的服务地址。</li>
<li><strong>APP2 服务</strong> 携带 <strong>ST</strong> 向 <strong>CAS Server</strong> 进行认证。</li>
<li><strong>CAS Server</strong> 认证成功，返回客户端通过的响应。</li>
<li>客户端拿到成功的响应后，设置 <strong>Session</strong>，并重定向至 <strong>APP2</strong> 的地址，并设置 <strong>Cookie</strong> <strong>MOD_AUTH_CAS_S</strong>。</li>
<li><strong>APP2</strong> 发起请求，带上 <strong>Cookie</strong> 中的 <strong>MOD_AUTH_CAS_S</strong> ，发送给客户端进行校验。</li>
<li>客户端使用 <strong>MOD_AUTH_CAS_S</strong> 与 <strong>Session</strong> 中存储的数据进行校验。</li>
<li>校验通过，返回正确的内容，展示 <strong>APP2</strong>。</li>
</ol>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fapereo%2Fcas%2Fblob%2Fmaster%2Fdocs%2Fcas-server-documentation%2Fimages%2Fcas_flow_diagram.png" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/apereo/cas/blob/master/docs/cas-server-documentation/images/cas_flow_diagram.png" ref="nofollow noopener noreferrer"><strong>官方时序图</strong></a></p>
<h4 data-id="heading-9"> 单点登出(SLO)</h4>
<ol>
<li>在 <strong>APP1</strong> 平台 请求退出登录后,  先在 <strong>query</strong> 中 携带 <strong>service 字段</strong> 重定向 <strong>CAS</strong> 登出地址</li>
<li>用户携带 <strong>service query</strong> 字段和 <strong>CASTGC</strong> 请求到 <strong>CAS Server</strong></li>
<li><strong>CAS Server</strong> 根据 <strong>CASTGC</strong> 找到 <strong>TGT</strong>的信息，删除 <strong>TGT</strong> 完成 <strong>CAS</strong> 的注销</li>
<li><strong>CAS Server</strong> 可以在 <strong>TGT</strong> 中拿到关联的所有 <strong>ST</strong>,  根据 <strong>ST</strong> 找到对应的应用注册信息，调用其中的 <strong>logoutUrl</strong>，把 <strong>ST</strong> 包装到 <strong>logoutRequest</strong> 发送给 <strong>APP1</strong></li>
<li><strong>APP1</strong> 根据 <strong>logoutRequest</strong> 找到 <strong>ST</strong> ，查找 <strong>Session</strong> 中以 <strong>ST</strong> 为键的值删除，清除登陆状态</li>
<li><strong>APP1</strong> 登出成功</li>
<li><strong>APP2</strong> 根据 <strong>logoutRequest</strong> 找到 <strong>ST</strong> ，查找 <strong>Session</strong> 中以 <strong>ST</strong> 为键的值删除，清除登陆状态</li>
<li><strong>APP2</strong> 登出成功</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a616807e5bd34deb985c72a201826695~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            