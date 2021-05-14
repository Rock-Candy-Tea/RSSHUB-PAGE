
---
title: '请立刻停止使用 JWT 进行会话管理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d74925f9cbab4427b248792659c55546~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 17:36:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d74925f9cbab4427b248792659c55546~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">引言</h1>
<p><strong>近来发现，不少 WEB 应用系统使用 JWT 进行会话管理，缘由竟然是为了避免服务端存储会话，或者追求可自主控制，实不知使用 JWT 进行会话管理有巨大的安全隐患！</strong></p>
<h1 data-id="heading-1">HTTP 会话管理</h1>
<p>先说说 HTPP 协议，众所周知， HTTP 协议的特点就是一问一答（一次请求一次响应）。那么基于 HTTP 协议，做个购物网站，要实现用户登录，添加商品到购物车，最终买单的功能。为了实现以上功能，识别出一系列操作都是同一个用户，最为简单的方式就是每次操作浏览器都发送账户和密码，这样服务端知道是哪个用户添加商品到购物车和最终买单。这样看起来很简陋，而且在每次请求中携带账户和密码将大大增加泄露风险。
​</p>
<p>为了减少账户密码在请求中携带的次数，我们引入一个 session-id 的东西。在你携带账户密码登录购物网站（第一次请求），服务端验证通过后返回一个 session-id 。此后你添加商品到购物车也好，最终下单也好，反正后续的每次请求都携带好这个 session-id 即可。为什么携带 session-id 就可以识别出这是哪个客户的操作呢？因为服务端将客户的账户信息和本次会话发送给客户端的 session-id 关联了起来，那么这个session-id 和账户的关联信息就是 session-data。
​</p>
<p>在以上例子里，session-data 是存储在服务端的。其实，session-data 也可以存储到客户端。那么根据 session-data 存储的位置不同，分为 Server Side Session 和 Client Side Session 两种模式。</p>
<h2 data-id="heading-2">Server Side Session</h2>
<p>Server Side Session 模式是最为常见的，如前面购物网站的例子。在此模式中，客户端（浏览器）将 session-id 存储到 本地 cookies 中。其典型实现如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d74925f9cbab4427b248792659c55546~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
上图中 User A 是个已经建立会话的老用户，他的 Cookies 中存储了 Session_id，值为“AA01”，在请求中携带这个 Session_id，服务端收到后通过 Session_id 查询到 Session Database 中对应的数据，并在程序中使用。New User是个刚开始会话的新用户，他的 Cookies 中还没有 Session_id，于是服务端生成一个新的 session_id 返回给他，并在返回中使用401状态码，告知他重定向到登录页，进行登录。后续如果这个 New User 登录成功，服务端将会把他的身份信息存储到 Session Table中，并与会话初生成的 session_id 关联，这样后续的请求就如同 User A 这个老用户。</p>
<h2 data-id="heading-3">Client Side Session</h2>
<p>Client Side Session 模式大家可能觉得有点陌生，其实用的很多。如大部分使用 JWT 进行会话管理的WEB系统，就是 Client Side Session 模式。所谓 Client Side Session 模式就是把用户的 session-data 数据存储在客户端，这样服务端就非常清闲。其交互流程大致如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbf25fe8ee05430890c653794fe32d39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
上图中左侧 User A 是个已经建立会话的老用户，他的 Cookies 中存储了 Session_data，值为当前用户的基本信息，在请求中携带着 Session_data 数据，服务端收到请求后解析出 Session_data 信息，便知道是哪个用户的请求。右侧的 New User 用户正在登录建立会话，服务端验证成功后，将生成 session_data 信息，返回给客户端。由于 session_data 数据是存储在客户端，为了防止篡改，服务端会对生成的 session_data 数据进行签名，甚至加密。</p>
<h2 data-id="heading-4">Server Side VS Client Side</h2>
<p>前文介绍了 Server Side Session 和 Client Side Session 两种模式各自的原理，那么这两种模式孰优孰劣呢？在对比之前，先定一个基准，就是仅限<strong>功能性</strong>和<strong>安全性</strong>，而不是对比两种模式的原始实现性。</p>
<h3 data-id="heading-5">Server Side Session</h3>
<p>优点：</p>
<ol>
<li>会话数据存储在服务端，不暴露相关信息，安全性高；</li>
<li>每次请求只需传递 session-id，减少流量开销；</li>
<li>服务端可方便吊销会话，控制同账户会话并发数等全面的会话策略管理；</li>
</ol>
<p>缺点：</p>
<ol>
<li>服务端分布式部署时，需增加处理 Session-data 共享。</li>
</ol>
<h3 data-id="heading-6">Client Side Session</h3>
<p>优点：</p>
<ol>
<li>分散存储；</li>
</ol>
<p>缺点：</p>
<ol>
<li>会话数据存储在客户端，且在每次请求中携带，增加泄露风险；</li>
<li>每次请求需传递更多数据，增加流量开销；</li>
<li>服务端不方便吊销会话，实现各种会话策略管理；</li>
</ol>
<p>从以上对比可以看出，两种模式在<strong>功能性</strong>和<strong>安全性</strong>上的特点刚好相反。Server Side Session 模式优点突出，但为什么还存在Client Side Session 模式呢？所谓存在即合理，因为 Client Side Session 模式<strong>原始实现简单</strong>！Client Side Session 模式服务端无需集中存储 session-data 数据，自然也无需处理 session-data 的查找，而且分散存储在客户端，服务端无需考虑分布式下的 session-data 共享。
但是 Client Side Session 模式原始实现简单对于使用者来说并不重要，因为使用者只使用现成的库和框架，只要支持度好就行。所以，Server Side Session 比 Client Side Session 模式更为普遍。</p>
<h1 data-id="heading-7">什么是 JWT ？</h1>
<p><strong>首先说明 JWT（JWE、JWS）标准只是设计了一个防篡改令牌，并非是为会话管理而设计。</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23f89f4516a740e19dc4fd941d323394~tplv-k3u1fbpfcp-zoom-1.image" alt="17E29B58-487F-48bd-AD39-06FCEA348A9E.png" loading="lazy" referrerpolicy="no-referrer">
JSON Web Token(JWT)是一个基于 RFC 7519 的开放数据标准，它定义了一种宽松且紧凑的数据组合方式，使用 JSON  对象在各应用之间传输信息（信息加密即 jwe，签名即 jws）。该 JSON 对象可以通过数字签名进行鉴签和校验，一般地，JWT 可以采用 HMAC 算法，RSA 或者 ECDSA 的公钥/私钥对数据进行签名操作。一个 JWT 通常有 HEADER (头)，PAYLOAD (有效载荷)和 SIGNATURE (签名)三个部分组成，三者之间使用“.”链接，格式如上图所示。</p>
<h2 data-id="heading-8">JWT 的缺陷</h2>
<p>JWT 标准设计看起来很不错，实际上包藏祸心，因为其设计，隐藏诸多安全问题，详细如下：</p>
<h3 data-id="heading-9">重置空加密算法缺陷</h3>
<p>JWT 支持将算法设定为“None”，如果你使用JWT库时未设置关闭该功能，那么任何Token都是有效的。具体做法是将JWT第一部分 header 中 alg 字段设置为 None ，再将第三部分 signature 设置为空（即不添加signature字段）， 此token 可顺利通过验证。</p>
<h3 data-id="heading-10">密钥混淆攻击</h3>
<p>JWT 最常用的两种算法是 HMAC 和 RSA。HMAC（对称加密算法）用同一个密钥对 token 进行签名和认证。而RSA（非对称加密算法）需要两个密钥，先用私钥加密生成 JWT ，然后使用其对应的公钥来解密验证。如果公钥泄露（很多人觉得公钥可以分发），那么将算法 RS256 修改为 HS256 ，即非对称加密向下降级为对称加密。再使用这个泄露的公钥对 token 进行签名，后端收到后根据头中指定的算法，将使用公钥对 token 验证，如此便认证通过。</p>
<h3 data-id="heading-11">密钥暴力破解</h3>
<p>如果 JWT 使用对称加密算法（如 HS256）， 这意味着对令牌进行签名的密钥也用于对其进行验证。由于签名验证是一个自包含的过程，因此可以测试 token 本身的有效密钥，而不必将其发送回应用程序进行验证。如果密钥设置过于简单，如常用词汇、生日年份等，结合已知的泄露密码列表，将很快破解出密钥，如此便可伪造出任意token 。</p>
<h3 data-id="heading-12">kid 指定攻击</h3>
<p>kid 即为 key ID ，存在于 jwt header 中，是一个可选的字段，用来指定加密算法的密钥。如在头部注入新的 kid 字段，并指定 HS256 算法的 key 为 123456，生成新的token,服务端收到将使用指定的密钥123456来验证token。</p>
<h2 data-id="heading-13">如何避免 JWT 的缺陷</h2>
<p>以上列举的问题中，除了密钥暴力破解，其余皆为 jwt 标准设计引发的缺陷。如果你选择使用 jwt 标准，那么请找一个靠谱的实现库，并进行安全测试。请避免使用对称加密算法，并正确配置安全项，如开启验证 jwt 头部，禁止 alg 设置为 none，禁止密钥降级等安全措施。不过最好的避免方式就是不用 jwt ，改用 paseto ，一个替代 jwt 的新标准。</p>
<h1 data-id="heading-14">JWT 进行会话管理的“优点”</h1>
<p>首先，如前文所述，JWT 标准并非是为会话管理而设计，当然 paseto 标准（ JWT 标准的替代者）也不是。现如今大多数使用 JWT 进行会话管理实际上是 Client Side Session 模式。前文讲到 Client Side Session 模式将会话数据存储到客户端，那么为了防止数据篡改或者泄露，一般对存储在客户端的数据进行签名或加密。很多人就利用 JWT 实现库将会话数据放在 PAYLOAD 区域，然后生成一个token，发送给客户端。客户端如果是网页浏览器，甚至通过 js 将收到的 token 放置在 localStorage 中。以上操作让开发者感觉一切尽在掌握之中，殊不知集万千漏洞于一身。</p>
<p>使用 JWT 进行会话管理的人声称优点如下：</p>
<ol>
<li>天然支持分布式验证；</li>
<li>高并发下降低服务器压力；</li>
<li>灵活易用；</li>
<li>更安全，可防止CSRF；</li>
<li>在移动设备上效果更好；</li>
<li>适用于阻止 cookie 的用户。</li>
</ol>
<p>​</p>
<p>以上声称的优点实际上是 Client Side Session 模式和自主控制 token 带来的。但是我要告诉各位，对于使用者来说，以上优点全部是伪命题。</p>
<h2 data-id="heading-15">天然支持分布式验证</h2>
<p>这个特点是真的，然而现实情况是几乎没有人真正需要这个特点。因为 session 共享技术很成熟，现有软件框架都提供了良好的支持方案。</p>
<h2 data-id="heading-16">高并发下降低服务器压力</h2>
<p>看上去高并发下，Client Side Session 模式没有服务端存储和查询，可降低服务器压力。然而，如果真的是高并发，更应该考虑业务处理对服务器带来的压力，而不是会话存储和查询，因为这根本就是九牛一毛。</p>
<h2 data-id="heading-17">灵活易用</h2>
<p>这完全是个错误，自定义使用 JWT 进行会话管理，需要更多的代码配置来处理，何来灵活易用？</p>
<h2 data-id="heading-18">更安全，可防止CSRF</h2>
<p>前文介绍 JWT 标准，已说明 JWT 存在很多设计问题，更不必说 Client Side Session 模式带来信息泄露的风险。而对于可以防止CSRF，除非你把 token 放在 cookies 以外区域，如 localStorage 中，使用JS来操作，然而这将带来更大的风险。</p>
<h2 data-id="heading-19">在移动设备上效果更好</h2>
<p>很久以前，部分移动浏览器存在不支持cookie的情况，但这已经是过去式了。现在但凡是个靠谱的 HTTP 库，移动开发框架都支持 cookie，所以这根本不是个问题。</p>
<h2 data-id="heading-20">适用于阻止 cookie 的用户</h2>
<p>确实有用户会阻止 cookie 的使用，为了避免被跟踪。但建立会话就是要求登录验证身份信息，所以，选择阻止 cookie 使用的用户明白，为什么我登录不了。对于真心想避免跟踪的用户，不仅仅会阻止cookie，而是会阻止一切客户端存储。这样，Client Side Session 模式下，会话信息也是无处可存。</p>
<p>如果你偏爱 Client Side Session 模式，而且确实觉得 Client Side Session 模式可以满足你的需求，那仅需使用服务端框架支持的 Client Side Session 模式实现即可，而不必去使用 JWT 。</p>
<h1 data-id="heading-21">HTTP 会话管理的正确之道</h1>
<p>对于安全会话，首先是需要使用 HTTPS，用于保证传输通道的安全。然后使用 Server Side Session 模式的实现，如网页浏览器中的 cookie 存储随机标识符，即 session-id，该 session-id 与服务端存储的 session-data 配对。如果你需要保持更久的会话，可加入一个长期的 remember me id 来实现，而不是随意延长 session-id 的有效期。
​</p>
<p>有朋友说，JWT 会话管理可通过扩展避免 Client Side Session 模式下的缺点。如吊销会话，服务端可加入黑名单机制，或者服务端记录签发出去的 token，并设置有效期，然后每次请求进行比对。那么问题来了，这样还是 Client Side Session 模式吗？
​</p>
<h1 data-id="heading-22">补充</h1>
<p>有朋友说 JWT 非常简单的实现了单点登录，一问究竟，我竟无言以对。原来他是指多个系统配置一样的密钥进行token验证，即可实现系统间无缝身份验证。没错，这其实就是 Client Side Session 模式的优点，在特定场景下可实现“单点登录”的效果。但现实大多数场景下是不可能达成的，因为首先需要各个不同公司开发的软件系统都采用 JWT 进行会话管理，接着互相信任共享同一个密钥（这是极其不安全的）。现在主流解决单点登录的协议是OIDC 或者是 OAuth2，再古老些也是 SAML 或 CAS。
​</p>
<p>有朋友问，既然 JWT 并不是为会话管理设计的，那 JWT 应该用来做什么？JWT 适用于一次性令牌，即短有效性，一次性使用。如用于密码找回邮件中的短效一次性链接，或者是文件下载。</p>
<h1 data-id="heading-23">参考文献</h1>
<p>[1] [EB/OL].<a href="http://cryto.net/~joepie91/blog/2016/06/13/stop-using-jwt-for-sessions/" target="_blank" rel="nofollow noopener noreferrer">cryto.net/~joepie91/b…</a>.2021-05-04<br>
[2] paseto [EB/OL].<a href="https://github.com/paragonie/paseto" target="_blank" rel="nofollow noopener noreferrer">github.com/paragonie/p…</a>/.2021-05-04<br>
[3] [EB/OL].<a href="https://paragonie.com/blog/2017/03/jwt-json-web-tokens-is-bad-standard-that-everyone-should-avoid" target="_blank" rel="nofollow noopener noreferrer">paragonie.com/blog/2017/0…</a>.2021-05-04<br>
[4] [EB/OL].<a href="https://geekkeen.github.io/http-cookie-session.html" target="_blank" rel="nofollow noopener noreferrer">geekkeen.github.io/http-cookie…</a>.2021-05-04<br>
[5] [EB/OL].<a href="https://blog.by24.cn/archives/about-session.html" target="_blank" rel="nofollow noopener noreferrer">blog.by24.cn/archives/ab…</a>.2021-05-04</p></div>  
</div>
            