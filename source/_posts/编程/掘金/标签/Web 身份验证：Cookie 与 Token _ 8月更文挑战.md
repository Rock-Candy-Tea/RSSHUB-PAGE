
---
title: 'Web 身份验证：Cookie 与 Token _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc69f011d47442f592b45820476360d2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 18:40:33 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc69f011d47442f592b45820476360d2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>应用开发一般都少不了身份验证，而身份验证机制的稳定性对所有应用程序都变得至关重要。具体选择何种方式进行身份验证可以根据项目及团队情况来衡量，在决定之前需要先理解WEB身份验证常见的两种方式：基于 <code>Cookie</code> 的身份验证和基于令牌（<code>Token</code>）的身份验证。</p>
<h3 data-id="heading-0">基于 Cookie 的身份验证</h3>
<p>身份验证是将用户凭据交换为唯一身份标识的过程。</p>
<blockquote>
<p>在基于 <code>Cookie</code> 的身份验证中，此唯一标识符 (<code>Cookie</code>) 在服务器端创建并发送给浏览器。</p>
</blockquote>
<p>当登录 Web 应用程序时，浏览器将从其应用程序的服务器接收一个 <code>Cookie</code>，浏览器将存储它并将该 <code>Cookie</code> 与每个后续请求一起发送，以验证请求来自同一用户。</p>
<p>为了更好地理解 <code>Cookie</code> 的工作原理，下面将这个过程分解为 5 个部分。</p>
<h4 data-id="heading-1">Cookie 工作流程</h4>
<h5 data-id="heading-2">1. 使用凭据登录到应用程序</h5>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc69f011d47442f592b45820476360d2~tplv-k3u1fbpfcp-watermark.image" alt="cookie1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">2. 服务器验证凭据并在创建 session</h5>
<p>服务器验证凭证成功后，创建 <code>session</code> ，可以存储在内存或数据库中，为了更好的扩展建议将其存储在数据库中。如果是存储在内存中，在使用负载均衡或多服务器部署的场景下会出现 <code>session</code>  问题。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23e2cf4dd8cd455cbf0f1678e44be2d8~tplv-k3u1fbpfcp-watermark.image" alt="cookie2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">3. 服务器通过将cookie包含在Set-Cookie 标头中来响应浏览器</h5>
<p>这个 <code>cookie</code> 通过名称值对发送，它包含一个唯一的 <code>id</code> 来标识用户。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d8249823224f209355c334f306c375~tplv-k3u1fbpfcp-watermark.image" alt="cookie3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除此之外，<code>Cookie</code> 还可以包含到期日期、作用域和有效时间等详细信息。具有多个 <code>Set-Cookie </code>标头的示例响应如下所示：</p>
<pre><code class="copyable">HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: <cookie-name>=<cookie-value>
Set-Cookie: <cookie-name>=<cookie-value>; Expires=<date>
Set-Cookie: <cookie-name>=<cookie-value>; Max-Age=<number>
Set-Cookie: <cookie-name>=<cookie-value>; Domain=<domain>
Set-Cookie: <cookie-name>=<cookie-value>; Path=<path>
Set-Cookie: <cookie-name>=<cookie-value>; Secure
Set-Cookie: <cookie-name>=<cookie-value>; HttpOnly

[page content]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">4. 浏览器将 Cookie 存储在存储中并与后续请求一起发送</h5>
<p>当服务器收到带有 <code>Cookie</code> 的请求时，它会将 <code>Cookie</code> 中的 <code>session ID</code> 与数据库中的 <code>session</code> 进行比较以验证用户的有效性。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84d2d31c45fc48a9b6d7172501fd4ffe~tplv-k3u1fbpfcp-watermark.image" alt="cookie4.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以使用浏览器开发工具在应用程序部分下的 <code>Cookie</code> 存储中找到浏览器中保存的所有 Cookie。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fd830d6e4d54a55ace178112c6e39b4~tplv-k3u1fbpfcp-watermark.image" alt="cookie5.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">5. 当用户注销时，服务器将从数据库中删除 session</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/066bbfa623564455b4593f7c559a710b~tplv-k3u1fbpfcp-watermark.image" alt="cookie6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一旦用户注销，服务器将通过清除数据库 <code>session</code> 并使 <code>Cookie</code> 过期，浏览器也会从 <code>Cookie</code> 存储中删除它。</p>
<h4 data-id="heading-7">Cookie 特征与优缺点</h4>
<p>上面简单介绍了一下 <code>Cookie</code> 的工作流程，下面来看看其特征与优缺点。</p>
<h5 data-id="heading-8">这是一个完全自动化的过程</h5>
<p>如果使用 <code>Cookie</code> 进行身份验证，则无需明确开发任何内容来向请求添加 <code>Cookie</code>。</p>
<blockquote>
<p>浏览器会负责 Cookie 的处理，它会自动为所有请求添加 Cookie。</p>
</blockquote>
<p>尽管这种自动化过程使开发变得更容易，但也有一些缺点。例如，有些请求不需要任何身份验证，但是使用这种方法，<code>Cookie</code> 也将在每个请求中被发送。</p>
<blockquote>
<p>此外，CSRF 攻击者可以利用这种机制来欺骗浏览器向虚假网站发送带有 Cookie 的请求。</p>
</blockquote>
<h4 data-id="heading-9">安全措施</h4>
<p>默认情况下，基于 <code>Cookie</code> 的身份验证对攻击没有有效的保护，它们主要容易受到跨站脚本（<code>XSS</code>）和跨站请求伪造（<code>CSRF</code>）攻击。</p>
<blockquote>
<p>但是，可以显式地修改 Cookie标头来保护它们免受此类攻击。</p>
</blockquote>
<p>例如，在设置 <code>Cookie</code> 头时使用 <code>HttpOnly</code> 属性可以很容易地保护 <code>Cookie</code> 免受 <code>XSS</code> 攻击。</p>
<pre><code class="copyable">Set-Cookie: <cookie-name>=<cookie-value>; Secure
Set-Cookie: <cookie-name>=<cookie-value>; HttpOnly
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，可以在 <code>Cookie</code> 标头中使用 <code>SameSite</code> 属性来有效地防止 <code>CSRF</code> 攻击。</p>
<pre><code class="copyable">Set-Cookie: <cookie-name>=<cookie-value>; SameSite=Lax
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>SameSite</code> 属性有 3 个值可用：</p>
<ul>
<li><code> SameSite=Lex</code>：将确保浏览器不会在跨站点请求时发送 <code>Cookie</code>（如果没有定义 SameSite 属性，这是 Cookie 的默认行为）。</li>
<li><code>SameSite=Strict</code> ： 将确保浏览器仅针对同站点请求发送 <code>Cookie</code>。</li>
<li><code>SameSite=Note</code> 将允许通过跨站点和同站点请求发送 <code>Cookie</code></li>
</ul>
<h4 data-id="heading-10">通常适用于单个域名</h4>
<p>除非特别配置，否则 <code>Cookie</code> 仅适用于单个域名。尽管从表面上这似乎是一种限制，但它是默认情况下强制执行单一来源的最强大功能之一。但是，如果前端和后端 (API) 来自不同的域名或子域名，则需要在 <code>Cookie</code> 中将其明确列入白名单。否则，浏览器不会随请求一起发送 <code>Cookie</code>。</p>
<h4 data-id="heading-11">不适合开放API</h4>
<p>如果正在构建一个API来向客户端公开服务，那么 <code>Cookie</code> 可能不是最佳的选择。除非客户端只是浏览器，否则它会使客户端变得复杂。</p>
<p>例如，开发的是一款手机应用，与令牌 <code>Token</code> 相比，拥有 <code>Cookie</code> 将使移动应用程序 <code>Cookie</code> 管理变得复杂。</p>
<h4 data-id="heading-12">可能存在可扩展性问题</h4>
<p>如前所述，服务器负责 <code>Cookie</code> 设置，需要在数据库中为每个用户存储 <code>session</code> 。</p>
<p>尽管有成熟的方法来处理可扩展性（例如，使用像 <code>Redis</code> 这样的内存数据库作为 <code>session</code> 的存储），但它仍然增加了更多的复杂性。</p>
<p>但是，随着用户数量的增加，在扩展和管理这些 <code>session</code> 时可能会出现问题。</p>
<h4 data-id="heading-13">最适合存储额外的数据</h4>
<p>由于这种方法为每个用户维护单独的 <code>session</code>，所以可以存储额外的数据到 <code>session</code> 中。</p>
<p>通过 <code>Cookie</code> 和 <code>session</code>，可以存储特定的数据，如用户个性化、访问控制和 <code>session</code>。然后，它允许将其用于后续请求。</p>
<p>然而，也可以用 <code>Token</code> 来实现这一点。例如，使用 <code>JWT</code> 令牌，可以存储 <code>Claims</code> 数据。然而，由于它将增加 <code>Token</code> 的大小，保留更多 <code>Token</code> 将影响更高的网络利用率。</p>
<h4 data-id="heading-14">可以限制浏览器对 Cookie 的访问</h4>
<p>由于 <code>Cookie</code> 提供了 <code>HTTP-Only</code> 选项，可以限制 JavaScript 对它的访问。此外，它将阻止任何访问Cookie与跨站点脚本攻击。</p>
<h3 data-id="heading-15">基于令牌Token的认证</h3>
<p>引入基于令牌的身份验证是为了解决基于 <code>Cookie</code> 方法的不足。</p>
<blockquote>
<p>与Cookie不同，基于Token的方法需要自己实现，Token保存在客户端。</p>
</blockquote>
<p>当登录到web应用程序时，服务器将验证凭据并向浏览器发送加密 <code>Token</code>。然后浏览器将存储这个Token，并可以添加到后续请求的授权头中。</p>
<p>然而，基于 <code>Token</code> 方法的标准实现要比上面描述的流程复杂得多。例如，<code>OpenID Connect</code> 引入了多个身份验证流来处理不同类型的用例。</p>
<p>为了更好地理解 <code>Token</code> 的工作方式，下面将这个过程分解为4个部分，并以使用最广泛的 <code>Token</code> 标准 <code>JWT</code> 作为实例。</p>
<blockquote>
<p>JSON Web Token (JWT) 是基于令牌的身份验证中最常用的开放标准。</p>
</blockquote>
<h4 data-id="heading-16">Token的认证工作流程</h4>
<h5 data-id="heading-17">1. 使用凭据登录到应用程序</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09688139d793468fba8d31ff332ebc7b~tplv-k3u1fbpfcp-watermark.image" alt="cookie1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-18">2. 服务器验证凭据，生成令牌并使用密钥对其进行签名，然后将其发送回浏览器</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5289aa0df0741778c90ae7ec3221636~tplv-k3u1fbpfcp-watermark.image" alt="token2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通常，需要在传输时使用加密（如 SSL）来保护通道。</p>
<p>在服务器端，可以使用像 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjsonwebtoken" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/jsonwebtoken" ref="nofollow noopener noreferrer">jsonwebtoken</a> 这样的 NPM 库来生成这些令牌。</p>
<pre><code class="copyable">npm install jsonwebtoken
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const jwt = require("jsonwebtoken");
const privateKey =
    "eyJkYXRhIjp7InVzZXJuYW1lIjoiZGV2cG9pbnQifSwiaWF0IjoxNjI3Njk3ODQ2fQ";
const token = jwt.sign(
    &#123;
        data: &#123;
            username: "devpoint",
        &#125;,
    &#125;,
    privateKey,
    &#123; algorithm: "HS256" &#125;,
    &#123; expiresIn: Math.floor(Date.now() / 1000) + 60 * 60 &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjsonwebtoken" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/jsonwebtoken" ref="nofollow noopener noreferrer">jsonwebtoken</a> 生成的 <code>Token</code> 如下所示：</p>
<pre><code class="copyable">eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZXJuYW1lIjoiZGV2cG9pbnQifSwiaWF0IjoxNjI3Njk3OTA2fQ.9v0S-74SH5UQwTAqgvNL43fAxQqW3_cajoDsum3TZEo
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">3. 将 Token 存储在浏览器存储中，并使用JavaScript添加到后续请求中</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88069a6d8fd04337bb32c079b8c4b7bb~tplv-k3u1fbpfcp-watermark.image" alt="token3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器可以将此 <code>Token</code> 存储在本地存储、<code>Session storage</code> 或 <code>Cookie</code> 中。然后这个 <code>Token</code> 将被添加到必要请求的授权头中，并发送到服务器端进行请求验证。因此，需要使用 JavaScript 来实现向标头添加Token。</p>
<pre><code class="copyable">Authorization: Bearer <token>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjsonwebtoken" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/jsonwebtoken" ref="nofollow noopener noreferrer">jsonwebtoken</a> 库中的 <code>jwt.decode()</code> 函数来解码此 <code>Token</code> 并在应用程序中使用有效负载数据。</p>
<h5 data-id="heading-20">4. 当用户注销时，需要手动从其存储中删除Token</h5>
<p>一旦用户退出系统，需要手动清除存储在存储中的 <code>Token</code>，使其无法用于进一步的请求。</p>
<h4 data-id="heading-21">Token的认证特征及优缺点</h4>
<h5 data-id="heading-22">一种无状态机制</h5>
<p>与 <code>Cookie</code> 不同，基于令牌的方法是无状态的。这意味着它不会在数据库或服务器中保存有关用户的任何信息。</p>
<blockquote>
<p>服务器只负责创建、验证令牌，这允许构建比基于 Cookie 的方法更具可扩展性的解决方案。</p>
</blockquote>
<h5 data-id="heading-23">安全问题</h5>
<p>尽管令牌试图解决 <code>Cookie</code> 中的安全问题，但它也并不完全安全。</p>
<blockquote>
<p>如果应用程序允许将外部 JavaScript 嵌入到应用程序中，则保存在浏览器中的令牌可能容易受到 XSS 攻击。</p>
</blockquote>
<p>此外，由于令牌是无状态的，如果暴露在外面，在它到期之前没有办法撤销它。因此，尽可能少地保留令牌至关重要。大部分身份验证服务将 <code>JWT</code> 令牌的有效期设置在 <code>5</code> 分钟以内。</p>
<h3 data-id="heading-24">总结</h3>
<p>基于令牌和基于 <code>Cookie</code> 的方法是 Web 应用程序最常用的两种身份验证机制。在本文中，讨论了它们的工作原理、特性、优缺点。</p>
<p>正如所看到的，这些方法都不是 100% 完美的，它们各有优缺点。因此，在选择身份验证方法时，建议根据项目要求选择一种，而不是追求完美的方法。</p></div>  
</div>
            