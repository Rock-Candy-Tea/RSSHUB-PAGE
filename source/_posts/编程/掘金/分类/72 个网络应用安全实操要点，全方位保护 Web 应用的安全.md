
---
title: '72 个网络应用安全实操要点，全方位保护 Web 应用的安全'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e40f31c75594037b4a0a488505f7d65~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 17:05:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e40f31c75594037b4a0a488505f7d65~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 4 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>原文地址：<a href="https://www.appsecmonkey.com/blog/web-application-security-checklist/" target="_blank" rel="nofollow noopener noreferrer">Web Application Security Checklist</a></p>
<p>原文作者：Teo Selenius（已授权）</p>
<p>译者 & 校正：HelloGitHub-小熊熊 & 卤蛋</p>
</blockquote>
<p>对于开发者而言，网络安全的重要性不言而喻。任何一处代码错误、一个依赖项漏洞或是数据库的端口暴露到公网，都会有可能直接送你上热搜。</p>
<p>那么，哪里可以找到详细的避雷指引呢？<a href="https://owasp.org/www-project-top-ten/" target="_blank" rel="nofollow noopener noreferrer">OWASP's top 10</a> 清单太短了，而且它更关注的是漏洞罗列，而非对预防。相比之下，<a href="https://owasp.org/www-project-application-security-verification-standard/" target="_blank" rel="nofollow noopener noreferrer">ASVS </a>是个很好的列表，但还是满足不了实际需求。</p>
<p>本文这份清单将介绍 72 个实操要点，让你全方位保护你的 Web 应用程序。各位看官，准备入坑啦！</p>
<h2 data-id="heading-0">一、浏览器端的威胁防御</h2>
<h3 data-id="heading-1">1、用且仅用 HTTPS，防范网络攻击</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e40f31c75594037b4a0a488505f7d65~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>众所周知，一个安全的应用需要对浏览器和 Web 服务器之间的所有连接进行加密。此外，建议禁用一些旧的密码套件和协议。
使用 HTTPS 时，仅加密网站的“敏感”部分是不够的。如非这样，攻击者可以截获某个未加密的 HTTP 请求，然后伪造来自服务器的响应，返回恶意内容。
幸运的是，HTTPS 目前是很容易做到的。我们可以通过 <a href="https://letsencrypt.org/" target="_blank" rel="nofollow noopener noreferrer">Let's Encrypt</a> 免费获得证书，加上 <a href="https://certbot.eff.org/" target="_blank" rel="nofollow noopener noreferrer">CertBot</a> 免费续期。</p>
<p>继续我们的清单，下一个是 HSTS 它与 HTTPS 密切相关。</p>
<h3 data-id="heading-2">2、使用 HSTS 和预加载来保护用户免受 SSL 剥离攻击</h3>
<p>服务器可以用 HSTS 或 Strict Transport Security header 来强制进行加密连接。它表示需要一直使用 HTTPS 连接访问网站。</p>
<p>HSTS 可以防止 SSL 剥离攻击。所谓的 SSL 剥离攻击也就是：网络上的攻击者截获浏览器发出的第一个 HTTP 请求（通常是未加密的），并立即伪造对该请求的回复，假装是服务器并将连接降级为明文 HTTP。</p>
<p>值得注意的是，HSTS 仅在用户至少成功访问了一次应用程序的情况下才能生效。为了克服这个限制，可以把我们的网站提交到 <a href="https://hstspreload.org/" target="_blank" rel="nofollow noopener noreferrer">hstspreload.org</a> ，这样，各浏览器便可以将我们的域名通过硬编码写入到 HSTS 列表中。</p>
<p>如下：</p>
<pre><code class="hljs language-html copyable" lang="html">Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>警告：</p>
<p>在实施 HSTS 时，将会强制进出该网站的所有网络请求均被加密，如果网站请求中仍然有纯文本，可能无法访问。所以，先设置一个小的 max-age 参数进行调试，如果一切正常工作，再加大这个值。调试成功后再加上预加载 (preload) ，把开启预加载保留在最后一步，因为关闭它是件很麻烦和痛苦的事情。</p>
</blockquote>
<h3 data-id="heading-3">3、设置安全 Cookie，保护用户免受网络攻击</h3>
<p>给 Cookie 加上 Secure 属性。此属性将防止 Cookie 在（意外或强制的）未加密的连接中泄漏。</p>
<pre><code class="copyable">Set-Cookie: foo=bar; ...other options... Secure
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4、安全生成 HTML 以避免 XSS 漏洞</h3>
<p>要避免 XSS（跨站点脚本）漏洞，可以采用下面两种方法：</p>
<ol>
<li>完全静态的网站（例如 JavaScript SPA + 后端API）。避免生成 HTML 问题的最有效方法是根本不生成HTML，如前述方法，当然，也可以试试很酷的 NexJS。</li>
<li>模板引擎。针对传统的 Web 应用程序，其中的 HTML 大多是在后端服务器上根据提供参数动态生成的。这种情况下，不要通过字符串连接来创建 HTML 。推荐的做法是使用模板引擎，比如 PHP 语言的 Twig、Java 语言的 Thymeleaf、Python 语言的 Jinja2 等等。</li>
</ol>
<p>此外，务必要正确配置模板引擎，从而可以自动对参数进行编码，并且不要使用任何可以绕过这种编码的“不安全”函数。不要把 HTML 放在回调函数、属性（不带引号）或 href/src 等诸如此类的地方。</p>
<h3 data-id="heading-5">5、安全使用 JavaScript 以避免 XSS 漏洞</h3>
<p>要避免 JavaScript 端的 XSS（跨站点脚本）漏洞，切忌将不受信任的数据传递到可执行代码的函数或属性中。这类常见的函数或属性包括：</p>
<ul>
<li>eval、setTimeout、setInterval 等。</li>
<li>innerHTML，React's dangerouslySetInnerHTML 等。</li>
<li>onClick、onMouseEnter、onError 等。</li>
<li>href、src 等。</li>
<li>location, location.href 等。</li>
</ul>
<h3 data-id="heading-6">6、沙箱处理不可信内容，避免 XSS 漏洞</h3>
<p>最好是能避免不可信的内容，但往往又不能完全避免：例如需要从远程获取 HTML 进行展示，或者需要允许用户用所见即所得的编辑器写文章，等等。</p>
<p>要避免这些场景中的 XSS（跨站点脚本）漏洞，请首先使用 DOMPurify 清理内容，然后在沙箱中进行内容呈现。</p>
<p>即使所见即所得的编辑库声称从 HTML 中移除了恶意内容，仍然可以通过重新净化和沙箱来处理，进一步确保安全。</p>
<p>还有一种常见的情况是，我们想在网页展示广告等内容。这种情况下简单采用 IFrame 是不够的，因为 same-origin 策略会允许跨域的 frame 将父级 frame （也就是我们的网站）的 URL 修改为一个钓鱼网站。因此，要记住使用 IFrame 的沙箱属性来避免此种情况的发生。</p>
<h3 data-id="heading-7">7、采用内容安全策略，避免 XSS 漏洞</h3>
<p>内容安全策略（CSP）可以很好地防御 XSS（跨站点脚本）攻击、点击劫持攻击等。所以，一定要用它！默认情况下，CSP 会阻止几乎所有的危险操作，所以额外的配置越少越好。如下：</p>
<pre><code class="copyable">Content-Security-Policy: default-src 'self'; form-action 'self'; object-src 'none'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它允许从 Web 应用程序的源代码加载脚本、样式、图像、字体等，但不允许加载其他内容。最值得注意的是，它将阻止内联脚本（）的运行，从而更好地预防 XSS 漏洞。</p>
<p>此外，form-action:'self' 指令可防止在网站上创建恶意 HTML 表单（比如“您的会话已过期，请在此处输入密码”类似的表单），并将其提交到攻击者的服务器。</p>
<p>无论如何，都不要指定 script-src: unsafe inline ，一旦这样做，CSP 将形同虚设。</p>
<p>最后，如果你担心 CSP 会影响生产环境，可以先以 Report-Only 模式进行部署：</p>
<pre><code class="copyable">Content-Security-Policy-Report-Only: default-src 'self'; form-action 'self'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">8、设置 HttpOnly 的 Cookie，保护用户免受 XSS 攻击</h3>
<p>为 Cookie 设置 HttpOnly 属性，可以防止 Cookie 被 JavaScript 代码访问。 一旦跨脚本攻击发生，该设置也会让黑客更难窃取到 Cookie 信息。当然，有些需要被 JavaScript 代码访问的 Cookie，就不能做这个设置了。</p>
<pre><code class="copyable">Set-Cookie: foo=bar; ...other options... HttpOnly
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">9、针对下载功能，合理设置避免 XSS 漏洞</h3>
<p>向用户提供下载功能时，在 header 中设置 Content-Disposition: attachment，从而避免 XSS 漏洞。该设置将禁止在用户浏览器直接渲染文件，从而避免 HTML 或 SVG 格式的下载文件可能引发的漏洞。如下：</p>
<pre><code class="copyable">Content-Disposition: attachment; filename="document.pdf"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如我们想允许特定的文件（如 pdf）能在浏览器端打开，并且也确定这样是安全的，那么，可以针对该类型文件，将 header 省略掉或是将 attachment 换为 inline。</p>
<h3 data-id="heading-10">10、针对 API 响应，合理设置避免 XSS 漏洞</h3>
<p>反射型文件下载（RFD）攻击往往通过构建一个 URL 从 API 下载一个恶意文件来实现。针对该类漏洞，可采用在 API HTTP 响应中返回带有安全文件名的 Content-Disposition header来防御。</p>
<h3 data-id="heading-11">11、利用现有平台的反跨站请求伪造（CSRF）机制，避免 CSRF 漏洞</h3>
<p>为避免反跨站请求伪造漏洞，务必确保我们所采用的平台开启了反跨站请求伪造功能，并确保该配置发挥了应有的作用。</p>
<h3 data-id="heading-12">12、验证 OAuth 身份认证的 state 参数，避免 CSRF 漏洞</h3>
<p>有一类与 OAuth 身份认证相关的跨站请求伪造漏洞是黑客让用户不经意间采用其账户进行登录。因此，如果有使用 OAuth 身份认证，务必确保对状态（state）参数的验证。</p>
<h3 data-id="heading-13">13、正确使用 HTTP 协议，避免 CSRF 漏洞</h3>
<p>除了 POST、PUT、PATCH、DELETE 以外，不要使用其它 HTTP 方法进行数据更改。GET 请求一般是不包含在反跨站请求伪造机制中的。</p>
<h3 data-id="heading-14">14、为 Cookie 设置同源属性，避免 CSRF、XS-leak、XSS 漏洞</h3>
<p>为 Cookie 设置 SameSite 属性。SameSite 能防止大多数的跨站点请求伪造攻击，而且还可以防止许多跨站点泄漏的漏洞。</p>
<p>SameSite 属性有两种模式：宽松（lax）和严格（strict）。</p>
<p>宽松模式可以防止大多数跨站点计时和跨站点请求伪造攻击，但对基于 Get 请求的跨站点请求伪造漏洞无效。如下：</p>
<pre><code class="hljs language-html copyable" lang="html">Set-Cookie: foo=bar; ...other options... SameSite=Lax
<span class="copy-code-btn">复制代码</span></code></pre>
<p>严格模式则可以防止该类基于 Get 请求的漏洞，以及反射型的跨站点脚本漏洞。然而，严格模式不适合常规的应用程序，因为它会中断身份验证链接。如果用户已登录某个网站，现在要在新的页面打开指向该应用程序的链接，则打开的新页面将不会为该用户自动登录。由于严格模式的限制，会话 Cookie 也不会随请求一起发送。严格模式设置如下：</p>
<pre><code class="copyable">Set-Cookie: foo=bar; ...other options... SameSite=Strict
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">15、每次登录创建一个新的会话 ID，防止会话固定攻击</h3>
<p>会话固定攻击一般是在以下情形发生：</p>
<ol>
<li>
<p>攻击者将 Cookie（例如 JSESSIONID=ABC123）注入到用户的浏览器中。不用担心，攻击者有很多方法可以做到这一点。</p>
</li>
<li>
<p>用户使用其凭据登录，并在登录请求中提交攻击者设置的 JSESSIONID=ABC123 。</p>
</li>
<li>
<p>应用程序对 Cookie 和用户进行身份验证。</p>
</li>
<li>
<p>与此同时，拥有该 Cookie 的攻击者也就可以通过该用户的身份进行登录了。</p>
</li>
</ol>
<p>为了防止出现这种情况，程序中需要在身份验证通过后，创建一个新的会话 ID 返回给用户，而不是验证可能被动了手脚的 Cookie。</p>
<h3 data-id="heading-16">16、合理命名 Cookie，防止会话固定攻击</h3>
<p>难道 Cookie 命名也能影响到网络应用程序的安全性？确实如此！将 Cookie 采用 __Host-** 的形式来命名，浏览器将：</p>
<ul>
<li>不能通过非加密的链接访问该项 Cookie， 从而避免会话固定攻击以及其它涉及到 Cookie 读取与写入的攻击；</li>
<li>不允许子域名重写该项 Cookie，从而避免来自子域名网站（抑或是被攻陷，抑或本身就是恶意的）的攻击。</li>
</ul>
<p>该项设置示例如下：</p>
<pre><code class="copyable">Set-Cookie: __Host-foo=bar ...other options...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">17、设置 Cache-Control header，防止用户信息被窃取</h3>
<p>缓存是将访问过的网站、下载过的文件全部存储在硬盘的某个位置，直到有人手动删除它们。默认情况下，浏览器会对页面的一切内容进行缓存，从而加快访问速度、节约网络带宽。</p>
<p>要在公共网络环境保证信息安全，我们需要将所有 HTTP 响应设置一个合适的 Cache-Control header，特别是针对非公开的和动态的内容。</p>
<p>该项设置示例如下：</p>
<pre><code class="hljs language-html copyable" lang="html">Cache-Control: no-store, max-age=0
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">18、设置 Clear-Site-Data header，防止用户信息被窃取</h3>
<p>另外一个可以有效保证用户退出后记录即被清除的 header 是 Clear-Site-Data 。当用户退出登录时，可以在 HTTP 请求中携带该 header。浏览器会清除该域名下的缓存、Cookie、存储以及执行上下文。大部分浏览器都支持该 header。</p>
<p>该项设置示例如下：</p>
<pre><code class="hljs language-html copyable" lang="html">Clear-Site-Data: "*"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">19、妥当地处理“退出”，防止用户信息被窃取</h3>
<p>用户退出登录后，务必要对访问令牌和会话识别码进行失效处理。这样，即使攻击者从访问历史/缓存/内存等地方获取到这些信息，它们也不再有效。</p>
<p>此外，如果有单点登录，切记要调用单点登录的退出端口。否则，因为单点登录会话仍处于活跃状态，此时的退出将会无效，只要用户再次点击“登录”，即可自动登录。</p>
<p>最后，清理掉你可能用到过的 Cookie、HTML5 存储等。上面提到的 Clear-Site-Data 还未被某些浏览器支持，所以最好还是手工清除一下。</p>
<h3 data-id="heading-20">20、针对 JavaScript 密码采用 SessionStorage，防止用户信息被后来者窃取</h3>
<p>SessionStorage 类似于 LocalStorage，但对每个标签页都是独有的，而且在浏览器/标签页关闭以后将自动清除。</p>
<blockquote>
<p>注意：如果要在系统内打开的多个标签页之间同步用户的授权信息，那就需要用事件来同步 sessionStorage 信息。</p>
</blockquote>
<h3 data-id="heading-21">21、不要通过 URL 传输敏感信息</h3>
<p>URL 设计的初衷就不是为了传输敏感信息。它会被显示在屏幕上，存储到浏览器历史记录，也容易随 referrer header 而泄漏，被记录在服务器日志等。所以，切忌在 URL 中传递敏感信息。</p>
<h3 data-id="heading-22">22、采用 Referrer 策略，防止 URL 地址泄露</h3>
<p>默认情况下，当从系统中链接到一个外部网站时，浏览器会设置一个 Referrer 的 header 来告诉该网站此次访问的来源。这个 header 包含了整个 URL 地址，这可能就涉及到一点隐私。</p>
<p>可以在 HTTP 响应中设置一个 Referrer-Policy 的 header 来禁止该默认行为：</p>
<pre><code class="hljs language-html copyable" lang="html">Referrer-Policy: no-referrer
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">23、为应用设置独立域名，防止同源应用相互干扰</h3>
<p>如果我们这样设置应用域名：<a href="https://www.example.com/app1/" target="_blank" rel="nofollow noopener noreferrer">www.example.com/app1/</a> 和 <a href="https://www.example.com/app2/%EF%BC%8C%E6%98%AF%E9%9D%9E%E5%B8%B8%E5%8D%B1%E9%99%A9%E7%9A%84%E3%80%82%E5%9B%A0%E4%B8%BA%E6%B5%8F%E8%A7%88%E5%99%A8%E4%BC%9A%E8%AE%A4%E4%B8%BA%E5%AE%83%E4%BB%AC%E6%98%AF%E5%90%8C%E6%BA%90%E5%BA%94%E7%94%A8%EF%BC%8C%E4%B9%9F%E5%B0%B1%E6%98%AF%E5%90%8C%E6%A0%B7%E7%9A%84%E6%9C%8D%E5%8A%A1%E4%B8%BB%E6%9C%BA%E3%80%81%E7%AB%AF%E5%8F%A3%E5%92%8C%E6%A8%A1%E5%BC%8F%E3%80%82%E6%AD%A3%E5%9B%A0%E4%B8%BA%E6%98%AF%E5%90%8C%E6%BA%90%E5%BA%94%E7%94%A8%EF%BC%8C%E5%AE%83%E4%BB%AC%E5%B0%86%E5%AF%B9%E5%BD%BC%E6%AD%A4%E6%9C%89%E5%AE%8C%E5%85%A8%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%E3%80%82%E4%BB%BB%E4%BD%95%E5%BD%B1%E5%93%8D%E5%85%B6%E4%B8%AD%E4%B8%80%E4%B8%AA%E7%9A%84%E6%BC%8F%E6%B4%9E%E9%83%BD%E4%BC%9A%E5%90%8C%E6%A0%B7%E5%BD%B1%E5%93%8D%E5%88%B0%E5%8F%A6%E5%A4%96%E4%B8%80%E4%B8%AA%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">www.example.com/app2/，是非常危险…</a></p>
<p>因此，我们需要给每个应用一个独立的域名。所以，这种情况下应该设置为：<code>https://app1.example.com/</code> 和 <code>https://app2.example.com/</code></p>
<p>注意：位于同一个域名下的子域名是可以为整个域名设置 Cookie 的。例如 app1.example.com 可以为 example.com 设置 Cookie，而这个 Cookie 也将适用于 app2.example.com。允许为一个站点设置 Cookie 有时会给会话固定等类型的漏洞以可乘之机。公共后缀列表可以用来应对该问题。此外，也可以通过将 Cookie 命名为 <code>__Host-</code> 来防止其被子域名所覆盖。</p>
<h3 data-id="heading-24">24、谨慎采用 CORS（跨域资源共享）</h3>
<p>浏览器的安全模型大部分是依赖于同源策略，它可以防止应用的跨域读取。而 CORS（跨域资源共享）则是一种允许网站进行跨域资源访问的手段。所以，决定使用它之前，最好先搞清楚自己是否真的需要。</p>
<h3 data-id="heading-25">25、限制请求来源</h3>
<p>如果你在 <code>api.example.com</code> 的服务需要被来自 <code>www.example.com</code> 的 GET 请求访问，那么可以在 <code>api.example.com</code> 服务上指定如下header:</p>
<pre><code class="hljs language-html copyable" lang="html">Access-Control-Allow-Origin: https://www.example.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你有个公开的服务接口（比如说一个提供给互联网上 JavaScript 客户端使用的计算器服务），那么你可以指定一个随机的来源：</p>
<pre><code class="hljs language-html copyable" lang="html">Access-Control-Allow-Origin: *
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你只想让有限的几个域名访问它，那么可以在程序中读取请求的 Origin header，进行比对后处理。不过，建议使用现成的库来操作，不要徒手撸，很容易出错。</p>
<h3 data-id="heading-26">26、谨慎使用 allow credentials 选项</h3>
<p>默认情况下，跨域资源共享是不带用户凭证的。但如果在 Web 服务器端指定如下 header，则将允许携带：</p>
<pre><code class="hljs language-html copyable" lang="html">Access-Control-Allow-Origin: https://www.example.com
Access-Control-Allow-Credentials: true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这对 header 组合相当危险。因为它会使跨域访问具备已登录用户的权限，并使用该权限来访问网站资源。所以，如果你不得不使用它，务必小心为上。</p>
<h3 data-id="heading-27">27、对 HTTP method 进行验证</h3>
<p>仅允许所需要的 HTTP 方法，从而最小化攻击面。</p>
<pre><code class="hljs language-html copyable" lang="html">Access-Control-Allow-Methods: GET
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">28、合理使用 WebSockets， 避免反跨站请求伪造等漏洞</h3>
<p>WebSockets 迄今还是比较新的技术，技术文档较少使用它难免会有些风险。所以，采用时务必要做到以下几点：</p>
<ul>
<li>
<p>对连接进行加密</p>
<p>就像我们应该用 https:// 而非 http:// 采用 WebSockets 时也要使用 wss:// 而非 ws://</p>
</li>
</ul>
<blockquote>
<p>HSTS 也会影响 WebSockets ，它会自动将非加密的 WebSocket 连接升级到 wss://</p>
</blockquote>
<ul>
<li>
<p>对连接进行鉴权</p>
<p>如果使用的是基于 Cookie 的鉴权机制，且 WebSocket 服务器与应用服务器在同一个域名下，那就可以在 WebSocket 中继续使用已有的会话。不过切记要对请求源进行验证！</p>
<p>如果不是基于 Cookie ，可以在系统中创建一个单次使用、有时间限制并与用户 IP 绑定的授权令牌，用该令牌对 WebSocket 进行授权。</p>
</li>
<li>
<p>对连接源进行确认</p>
<p>理解 WebSockets 的一个关键点在于要知道同源策略对其是无效的。任何一个能与你的系统建立 WebSocket 连接的网站，在使用 Cookie 鉴权的时候，都是可以直接获得用户信息的。因此，在 WebSocket 握手时，必须要确认连接源。可以通过验证请求头中的 Origin 参数来确认。</p>
</li>
</ul>
<blockquote>
<p>如果想要做到双重保险，可以采用反跨站请求伪造令牌作为 URL 参数。但针对每个任务则需要创建一次性的独立令牌，而不要直接使用反跨站请求伪造令牌，因为后者主要是用来为应用的其它部分提供安全保障的。</p>
</blockquote>
<h3 data-id="heading-29">29、采用 U2F 令牌或客户端证书，保护系统关键用户免受钓鱼攻击</h3>
<p>如果系统可能会面临钓鱼攻击的威胁，说人话也就是，“如果存在这样的可能性：攻击者创建一个假的网站，骗取管理员/CEO 或其它用户的信任，从而盗取其用户名、密码和验证码”，那么就应该使用 U2F 令牌或客户端证书来防止这种攻击，这样的话即使攻击者有了用户名、密码和验证码也无法得逞。</p>
<blockquote>
<p>备注： 强调钓鱼防护对于一般用户而言往往会带来不必要的麻烦。然而，提供多一种可选项对终端用户而言也非坏事。此外，向用户提前告知钓鱼攻击的危险也是非常必要的。</p>
</blockquote>
<h3 data-id="heading-30">30、针对跨站点泄露进行保护</h3>
<p>跨站点泄露是一系列浏览器边信道攻击。这种攻击使恶意网站可以从其它 Web 应用程序的用户中推测出信息。</p>
<p>这种攻击存在已有时日，但是浏览器端却是最近才开始添加针对性的预防机制。可以在 <a href="https://www.appsecmonkey.com/blog/xs-leaks/" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a> 中了解关于该类攻击的更多细节以及应该采取的安全控制措施。</p>
<h2 data-id="heading-31">二、服务器端的威胁防御</h2>
<p>其次，是服务器端的威胁防御，这里从应用系统、基础设施、应用架构、应用监控、事件响应等不同侧面，归纳了如下建议：</p>
<h3 data-id="heading-32">2.1 应用系统</h3>
<h3 data-id="heading-33">31、对用户输入进行合法性验证</h3>
<p>该类别的措施中最关键的一点就是尽可能严格地对所有用户输入进行合法性验证。适当的验证会使系统漏洞更难被发现和利用。对不合法的用户输入直接拒绝，而不要尝试去清洗。验证方面包括如下：</p>
<ul>
<li>采用严格的数据类型。针对日期采用 DataTime 类型，数字采用 Integer 类型等等。针对有固定可选项的情况采用枚举类型。尽量避免采用字符串类型。</li>
<li>如果必须采用字符串，至少给一个长度限制。</li>
<li>如果必须采用字符串，将可输入的字符集尽可能地减少。</li>
<li>如果要处理 JSON，使用 JSON 模式进行验证。</li>
<li>如果要处理 XML，使用 XML 模式进行验证。</li>
</ul>
<h3 data-id="heading-34">32、异常处理优雅化，避免技术细节泄露</h3>
<p>对终端用户不要显示堆栈记录或类似的调试信息。采用全局的异常处理器对异常进行处理，展现给浏览器端简单的错误信息。这样会使攻击者更难发现和利用系统中的漏洞。</p>
<h3 data-id="heading-35">33、不要自己做鉴权</h3>
<p>对用户进行鉴权时可能会出现各种各样的问题：要抵御密码猜想攻击、用户枚举攻击，要管理密码重置、存储用户凭证，样样都不容易。就像密码处理一样复杂，我们普通人还是不要尝试了。</p>
<p>直接使用 <a href="https://auth0.com/" target="_blank" rel="nofollow noopener noreferrer">auth0</a> 等类似的工具来进行身份验证，采用一些广泛使用的、安全的软件模块来实现通信协议（常见的为 <a href="https://openid.net/connect/" target="_blank" rel="nofollow noopener noreferrer">OpenID connect</a>）。如果不想用 auth0 这类第三方的身份提供商，也可以自己搭建一个类似 <a href="https://www.keycloak.org/" target="_blank" rel="nofollow noopener noreferrer">KeyCloak</a> 的服务来代替。</p>
<h3 data-id="heading-36">34、对一切都进行鉴权，减少攻击面</h3>
<p>应用系统要默认对一切都进行鉴权，除非是一些静态资源、异常页面或登出页面。</p>
<h3 data-id="heading-37">35、采用多重身份认证</h3>
<p>万一有人破解了身份认证服务呢？如果存在这种担忧，直接上多重身份认证（说人话也就是：除了密码以外，还需要手机验证码）。这样就算身份认证服务被黑、攻击者可以冒充到任何人，还是无法知道手机收到的验证码。</p>
<h3 data-id="heading-38">36、通过严格的权限控制，避免对数据或功能的未授权访问</h3>
<p>权限控制虽不是件容易事，但也有妥善处理的方法：只要时刻记住不要在控制器方法中忘了对用户权限进行验证，从而带来用户越权的漏洞，包括：</p>
<ul>
<li>不要默认对所有控制器方法开通访问权限。</li>
<li>根据用户角色划分每个控制器的访问权限。</li>
<li>采用方法级别的安全控制，限制对服务方法的访问权限。</li>
<li>采用集中化的权限管理工具，防止对每条记录的非授权访问。</li>
<li>采用前端 Web 应用和后台 API 结合的架构，对每个 App 和 API 均采取权限控制，而不仅是对与互联网连接的部分进行控制。</li>
</ul>
<p>为了进一步澄清权限管理工具，这里总结了一些要点：</p>
<ul>
<li>数据记录要有可以进行权限控制的字段，比如 <code>int ownerId</code>。</li>
<li>被授权的用户要有一个 ID。</li>
<li>要有一个类可用来进行权限评估，在数据记录的 ownerId 与 用户的 ID 相匹配时，能判断出用户具有对应的访问权限。</li>
<li>在以上基础上，可以将权限评估类集成到应用平台的权限控制系统中，比如 Spring Security 产品的 PreAuthorize、PostAuthorize 等等。</li>
<li>如果需要更复杂的权限控制，也可以搭建一个完善的 ACL 系统。</li>
</ul>
<h3 data-id="heading-39">37、采用合适的工具和技术，避免注入漏洞</h3>
<p>注入类的漏洞有很多，而且都很相似，包括 SQL 注入、HTML 注入、XML 注入、XPath 注入、命令注入、SMTP 注入、响应 header 注入等等。名称不同但本质相同，相应地解决方法也类似：</p>
<ul>
<li>问题原因： 使用字符串拼接，来构建特定协议下的参数化消息。</li>
<li>解决方案：采用合适的、安全的、现成的工具来实现这项任务。</li>
</ul>
<p>这里不会深入太多细节，只要记住：不管你是什么协议，都谨记上面这点。后面会列举一些常见的注入类漏洞。</p>
<h3 data-id="heading-40">38、创建安全的数据库查询语句，避免 SQL 注入漏洞</h3>
<p>如果要避免 SQL 注入漏洞，那就记住绝不要自己用字符串拼接 SQL 查询语句。采用一个对象关系映射框架（ORM）来实现，可以让开发更高效、应用更安全。</p>
<p>如果想要构建更细粒度的查询，可以使用更底层一点的 ORM。</p>
<p>如果不能使用 ORM，那就尝试预处理语句，但也要小心这类语句会比 ORM 更容易出现错误。</p>
<blockquote>
<p>警告：</p>
<p>ORM 框架也不是万能的，体现在两方面：一是，它对原生的 SQL 查询还是支持的，最好不要使用这类查询；二是，像其它任何软件一样，ORM 框架也会时不时被曝出漏洞。所以，还是遵循我们一而再再而三强调的策略：对所有输入进行验证，采用网络应用程序防火墙（WAF），并保持软件包的更新，这样基本就可以放心了。</p>
</blockquote>
<h3 data-id="heading-41">39、谨慎使用操作系统的命令行，防止命令注入的相关漏洞</h3>
<p>如果可以避免，最好不要执行操作系统命令。如果不能避免，那最好遵循以下准则：</p>
<ul>
<li>
<p>采用合适的库/方法来构建命令及其参数。参数必须是 list 类型。不要用单独字符串来创建命令。</p>
</li>
<li>
<p>不用使用 shell 来调用命令。</p>
</li>
<li>
<p>预定义好命令参数。比如 curl，如果允许用户通过 -o 来指定参数，那么攻击者就有机会写入到本地文件系统。</p>
</li>
<li>
<p>了解程序如何执行，并相应地对参数进行验证。再比如 curl，你可能只是想让用户可以拉取某个网站的内容，但如果他拉取了 file:///etc/passwd，那就危险了。</p>
</li>
<li>
<p>想清楚再行动。在上面的例子中，就算验证了访问地址是以 http:// 或 https:// 开头，攻击者也可以发起以这两类协议开头的攻击，如：<a href="http://192.168.0.1/internal_sensitive_service/admin%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">http://192.168.0.1/internal_sensitive_service/admin。</a></p>
</li>
<li>
<p>再强调一遍：真得要想清楚了再行动。就算你对 DNS 进行验证，确保命令中不含敏感内网地址，你有去禁止将特定 DNS 记录映射到 192.168.0.1 吗？如果答案是否，那就危险了。</p>
</li>
</ul>
<h3 data-id="heading-42">40、合理配置 XML 解析器，避免 XML 漏洞</h3>
<p>作为一种标记语言，XML 的危险性体现在它可以访问系统资源。XSLT 的一些实现甚至支持嵌入代码。因此，在处理时必须非常谨慎。</p>
<ul>
<li>
<p>如果可以，避免接受来自不受信任源的 XML/XSLT。</p>
</li>
<li>
<p>如果要向 XML、XSLT 或 XPath 传参，记住要使用安全的软件组件，而不要使用字符串连接/格式化的方式。</p>
</li>
<li>
<p>使用主流、安全的软件组件来解析 XML/XSLT。不要使用错误的库或代码来处理 XML。此外，在任何情况下，都不要试图去徒手撸一个解析器（比如 SAML），非常容易出错。</p>
</li>
<li>
<p>正确配置解析器：禁用 XSLT 文档、禁用 xinclude、禁用文档类型定义、禁用外部实体，启用 DOS 保护。具体配置在实现时会有所不同，但务必对所选择的解析器进行深入的研究。</p>
</li>
</ul>
<h3 data-id="heading-43">41、采用合适的类构建URL，避免 URL 注入漏洞</h3>
<p>URL 注入经常会在以下情况发生：</p>
<pre><code class="hljs language-java copyable" lang="java">flavour = request.getParam(<span class="hljs-string">"flavour"</span>);
url = <span class="hljs-string">"https:/api.local/pizzas/"</span> + flavour + <span class="hljs-string">"/"</span>;
<span class="hljs-keyword">return</span> get(url).json();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 flavour 被设置为：</p>
<pre><code class="copyable">../admin/all-the-sensitive-things/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这个 API 请求将会变为 <code>https://api.local/admin/all-the-sensitive-things/</code>，是不是很凶险？</p>
<p>解决方案依然是采用合适的 URL 构建库来为 URL 传参，从而能正确地对参数进行编码。</p>
<h3 data-id="heading-44">42、采用合适的类构建路径，避免路径遍历漏洞</h3>
<p>就像 URL 地址一样，如果攻击者设法在路径中的某个地方偷偷地插入 <code>../../../</code> ，文件路径可能最终指向意料之外的位置。要避免这种情况，请创建一个类，采用这个类安全地构造路径，并验证最终路径是否在预期目录中。避免在文件路径中使用不受信任的数据，或者更好的是，完全避免使用文件系统，直接采用云存储。</p>
<h3 data-id="heading-45">43、谨慎采用文件系统，接收不受信任的内容</h3>
<p>如果允许用户写入服务器的文件系统，可能会出现各种各样的问题。改用云存储，或者在数据库中使用二进制 blob。</p>
<p>如果您必须访问磁盘，则应遵循以下指导原则：</p>
<ul>
<li>
<p>不要让不受信任的数据影响内部文件路径。</p>
</li>
<li>
<p>将文件保存在远离 webroot 的隔离目录中。</p>
</li>
<li>
<p>在写入磁盘之前，请验证文件内容是否与预期格式匹配。</p>
</li>
<li>
<p>正确设置文件系统权限以防止写入不需要的位置。</p>
</li>
<li>
<p>不要提取压缩包（例如 ZIP），因为它们可以包含任何文件，包括指向系统任意地方的链接和路径。</p>
</li>
</ul>
<h3 data-id="heading-46">44、不要动态执行代码，避免远程代码执行漏洞</h3>
<p>不要使用 eval 或等效函数。找到一种其它的方法来实现代码执行。否则，不受信任的数据将有可能进行函数调用，从而在有机会在服务器上执行恶意代码。</p>
<h3 data-id="heading-47">45、合理采用序列化，避免反序列化漏洞</h3>
<p>对不受信任的数据进行反序列化是很危险的，很容易导致远程代码执行。</p>
<ul>
<li>
<p>如果可以避免，不要使用序列化。</p>
</li>
<li>
<p>如果可以在服务器端序列化对象，则对其进行数字签名。当需要再次反序列化它们时，请在继续反序列化之前验证签名。</p>
</li>
<li>
<p>使用一些主流的软件组件，并保持更新。许多反序列化库会一直被发现漏洞。<a href="https://github.com/google/gson" target="_blank" rel="nofollow noopener noreferrer">GSon</a> 是个不错的选择。</p>
</li>
<li>
<p>使用简单的文本格式，如 JSON，而不是二进制格式。此外，应该避免像XML这样有问题的格式，因为这样除了反序列化之外，还需要担心 XML 漏洞。</p>
</li>
<li>
<p>在处理序列化对象之前验证它。例如：对于 JSON，在继续反序列化之前，根据严格的 JSON 模式验证 JSON 文档。</p>
</li>
</ul>
<h3 data-id="heading-48">2.2 基础设施</h3>
<h3 data-id="heading-49">46、采用网络应用程序防火墙（WAF）</h3>
<p>安装防火墙，会减少很多风险。<a href="https://modsecurity.org/rules.html" target="_blank" rel="nofollow noopener noreferrer">ModSecurity</a> 就是一个很好的开源选择。</p>
<h3 data-id="heading-50">47、配置 Web 服务器，避免 HTTP desync 攻击</h3>
<p>HTTP desync，也称 HTTP 请求走私攻击，是指攻击者劫持随机用户向系统发出的 HTTP 请求。这类攻击一般在以下情况下发生：</p>
<ul>
<li>
<p>前端服务器，比如负载均衡器或反向代理服务器，接受携带有 Content-length、Transfer-Encoding 等头部参数的请求时，将请求未经处理随即传递到后台；</p>
</li>
<li>
<p>后台接受该请求的服务器（通常是应用服务器），采用（或被欺骗采用）一个不同于前端服务器的机制来确定 HTTP 请求从何处开始、何处结束，比如前端服务器使用 Content-Length，而应用服务器采用 Transfer-Encoding；</p>
</li>
<li>
<p>前端服务器重复利用与后端服务器的连接；</p>
</li>
<li>
<p>前端服务器在与后台服务器连接时采用 HTTP/1（而非 HTTP/2）。</p>
</li>
</ul>
<p>那么该如何进行防范呢？一般是根据所采用的产品：</p>
<ul>
<li>
<p>咨询所采用的反向代理产品供应商，确保该产品具备主动防范攻击的能力；</p>
</li>
<li>
<p>配置前端服务器，在与后台连接时采用 HTTP/2;</p>
</li>
<li>
<p>配置前端服务器，防止利用同一个连接发送多个客户端的 HTTP 请求；</p>
</li>
<li>
<p>采用网络应用程序防火墙（WAF），并确保其具备防止请求走私的模块。</p>
</li>
</ul>
<h3 data-id="heading-51">48、采用容器</h3>
<p>让目标应用隔离其他应用来运行。这样，即使发生了攻击事件，攻击者也不会有权限去访问未经许可的文件、系统或网络资源。因此，最好使用 Kubernetes 或一个云端环境来部署你的应用。如果因为某种原因必须使用一台服务器，那么可以手动采用 Docker 来约束应用。</p>
<h3 data-id="heading-52">49、使用 SELinux/AppArmor</h3>
<p>即使通过容器来运行应用，也还是需要进一步采用 SELinux 或 AppArmor 策略来进一步地对应用做出约束，从而减少容器漏洞引发的威胁。</p>
<h3 data-id="heading-53">50、采用最少权限的服务账户</h3>
<p>这种方法带来的好处是即使发生了被攻击事件，也能减少被攻击造成的损失。再次重申，列出所有的情形是不可能的，这里仅列举一些例子帮助大家理解：</p>
<ul>
<li>即使使用了 Docker，甚至是使用了 SELinux/AppArmor，不要用 root 账户来运行你的应用。为你的应用单独创建一个具备尽可能少的权限的账户，从而降低攻击者利用容器或内核漏洞等进行攻击的可能性；</li>
<li>如果有使用数据库，确保应用程序中的数据库用户在访问数据库时具备尽可能少的权限；</li>
<li>如果应用中集成了 API，确保应用访问 API 时具备尽可能少的权限。</li>
</ul>
<h3 data-id="heading-54">51、限制外部网络连接</h3>
<p>攻击者通常需要建立一定的反向通信渠道来建立操控渠道或窃取数据。此外，一些漏洞也是需要外部网络连接才会被发现、被利用。</p>
<p>因此，不能让应用随便访问外部网络，包括 DNS。试下在服务器运行命令 <code>nslookup www.example.com</code>，如果运行成功，则说明你没有对外部网络连接做出适当的限制。如何处理此类问题，一般则取决于基础设施。</p>
<p>针对外部的 TCP/UDP/ICMP 连接，一般可以通过以下方式禁用：</p>
<ul>
<li>网关防火墙，如果有的话；</li>
<li>如果是老式服务器，可以采用本地的防火墙（例如 iptables 或 Windows 防火墙）；</li>
<li>如果服务器端采用 Docker，可以使用 iptables；</li>
<li>如果使用了 Kubernetes，可采用网络策略定义。</li>
</ul>
<p>DNS 处理起来稍微麻烦一点，我们通常需要允许对一些 hosts 的访问。</p>
<ul>
<li>如果有本地的 hosts 文件，那就很简单，可以采取上面的任何一种方式来将 DNS 彻底禁用；</li>
<li>如果没有，那么你需要在你上游的 DNS 中配置一个私有的区域，在网络层限制仅能访问该指定的 DNS 服务器。这个私有区域内只允许对一些预先指定的 hosts 的访问。</li>
</ul>
<h3 data-id="heading-55">52、跟踪 DNS 记录，防止子域名劫持</h3>
<p>子域名劫持发生场景举例如下：</p>
<ol>
<li>
<p>假如我们拥有一个域名 example.com；</p>
</li>
<li>
<p>针对一次促销活动，我们买了另一个域名 <a href="http://www.my-cool-campaign.com/" target="_blank" rel="nofollow noopener noreferrer">www.my-cool-campaign.com</a> ，然后创建了一个别名从 campaign.example.com 映射到 <a href="http://www.my-cool-campaign.com;/" target="_blank" rel="nofollow noopener noreferrer">www.my-cool-campaign.com；</a></p>
</li>
<li>
<p>这次促销活动结束后，<a href="http://www.my-cool-campaign.com/" target="_blank" rel="nofollow noopener noreferrer">www.my-cool-campaign.com</a> 域名也到期了；</p>
</li>
<li>
<p>但是，从 campaign.example.com 到 <a href="http://www.my-cool-campaign.com/" target="_blank" rel="nofollow noopener noreferrer">www.my-cool-campaign.com</a> 的别名映射仍存在；</p>
</li>
<li>
<p>如果有人购买了这个到期的域名，那么 campaign.example.com 便可以直接指向该域名；</p>
</li>
<li>
<p>如果攻击者在 <a href="http://www.my-cool-campaign.com/" target="_blank" rel="nofollow noopener noreferrer">www.my-cool-campaign.com</a> 域名下提供一些恶意内容，那么便可以通过 <a href="https://campaign.example.com/" target="_blank" rel="nofollow noopener noreferrer">campaign.example.com</a> 域名直接访问到；</p>
</li>
</ol>
<p>因此，需要随时留意你的 DNS 记录。如果需要处理的类似情况较多，强烈建议你做一个自动监控方案。</p>
<h3 data-id="heading-56">2.3 架构</h3>
<h3 data-id="heading-57">53、创建内部 API 用来访问数据源</h3>
<p>对连接互联网的网络应用程序不应该太过于信任。例如，不应允许它进行数据库直连。否则，当有人攻破应用程序时，整个数据库都将面临威胁。</p>
<p>相反，我们应该搭建多组件组成的架构，例如：</p>
<ul>
<li>
<p>我们域名为 <a href="http://www.example.com/" target="_blank" rel="nofollow noopener noreferrer">www.example.com</a> 的应用程序使用 auth0 进行鉴权。</p>
</li>
<li>
<p>该应用程序访问内部 API 服务 api.example.local 时，携带被授权用户的 token，放在请求头部的 Authorization 中。</p>
</li>
<li>
<p>位于 api.example.local 的 API 服务根据用户的 token 进行访问限制，进而根据被授予的权限读写数据库。</p>
</li>
</ul>
<p>假如现在有黑客想要攻破我们的应用程序，即使成功，他也没有权限访问整个数据库，而只是利用某个用户的 token，进而访问该 token 所允许访问的那部分数据。</p>
<h3 data-id="heading-58">54、内部连接也需加密和验证</h3>
<p>不要盲目相信内网的安全性，有很多方法可以攻破它。对于系统间的访问，全部采用 TLS（也就是 HTTPS）进行加密，最好在网络和系统两个层次对连接进行鉴权。</p>
<h3 data-id="heading-59">55、对敏感信息集中管理</h3>
<p>如果没有采用合适的敏感信息管理方案，就很难保持授权的短期性化、可审计性和秘密性。因此，建议采用 HashiCorp Vault 一类的工具来集中管理密码、加密 key 等类似信息。</p>
<h3 data-id="heading-60">2.4 监控</h3>
<h3 data-id="heading-61">56、收集，分析，报警</h3>
<p>集中收集日志到一个独立系统，比如 SIEM（安全信息和事件监控系统）。在这个系统中，可以在一些表征脆弱性、攻击的事件发生时进行报警。当严重威胁发生时，可以立即通知相关人员。</p>
<h3 data-id="heading-62">57、收集系统安全事件</h3>
<p>最重要的日志来源可能就是系统自身了。当有可疑行为发生时，系统应能引发异常，记录事件，可能的话，甚至可以自动封锁可能带来问题的用户或IP地址。常见可疑行为包括：</p>
<ul>
<li>输入值的合法性验证错误（例如，试图输入 UI 中不可能提供的值）</li>
<li>访问控制错误 (例如，尝试访问一条在 UI 中不可能出现的记录)</li>
<li>数据库语法错误表示某个人发现了一处 SQL 注入的脆弱性，这时候可要动作快点采取行动了</li>
<li>XML 错误表示某个人发现了一处 XML 注入的脆弱性，或者正尝试利用 XXE（XML 外部实体）脆弱性进行攻击</li>
<li>错误请求表示用户可能发送了被应用拒绝的请求。Spring 框架的 RequstRejectedException 就是一个例子</li>
<li>反跨站请求伪造令牌验证错误一般表示有人正尝试寻找系统中存在的脆弱性</li>
</ul>
<h3 data-id="heading-63">58、收集运行时安全日志</h3>
<p>使用运行时安全监控工具如 Falco 来对异常系统访问进行检测。如果采用了 Kubernetes，那么 Falco 就特别有用。远程也可以对日志进行收集和监控。</p>
<h3 data-id="heading-64">59、收集 SELinux/AppArmor 日志</h3>
<p>假如我们制定了 SELinux 策略防止向外部的连接，但系统忽然向外部某个网站（例如 burpcollaborator.net）发起 HTTP 请求，那就需要立刻引起关注。又或者你的系统尝试访问 /etc/passwd。这两种情况都表示有人已经发现了我们系统中的漏洞。</p>
<h3 data-id="heading-65">60、收集 Web 服务器事件</h3>
<p>对 Web 服务器软件，至少要对访问日志和错误日志进行收集，收集后发送到集中式的日志服务器。在突发事件响应时，这将辅助我们快速理清时间线。</p>
<h3 data-id="heading-66">61、收集网络应用程序防火墙（WAF）日志</h3>
<p>如果你像上文推荐使用了网络应用程序防火墙（WAF），那么也对这个日志进行收集。但不用针对这个日志设置报警，因为它基本上会收到来自互联网各种各样的问题，而且不部分是你不用担心的。</p>
<h3 data-id="heading-67">2.5 事件响应</h3>
<h3 data-id="heading-68">62、制定应对计划</h3>
<p>一旦对我们的系统进行了监控和加固，攻击者将难以快速定位系统漏洞，即使最终发现，我们也能快速了解情况。</p>
<p>但仅了解情况是不够的，还需要做出如下准备：</p>
<ul>
<li>快速分析系统日志，了解当前状况和需采取的对应措施</li>
<li>在应用防火墙等产品中，快速对个别 url 地址和参数做出限制</li>
<li>如有需要，快速关停系统</li>
</ul>
<p><strong>六、开发管理</strong></p>
<h3 data-id="heading-69">63、威胁模型</h3>
<p>系统地考虑一下“可能会出现哪些问题”并据此做出调整。设计一个新的系统时，越早开始这一步越好。当对系统发生改变时，再重新梳理一遍这个过程。</p>
<p>例如：</p>
<blockquote>
<p>小王：如果攻击者攻破了我们连接了互联网的服务器，怎么办？</p>
<p>小陈：那可就完蛋了！</p>
<p>小王：好吧！这就说明我们在这里存在着一个信任关系，我们认为连接了互联网的服务器是不会被攻破的。我们可以信任这一点吗？</p>
<p>小陈：未必吧！有一百种可能导致我们的服务器被黑掉，例如我们代码中存在的脆弱性，或者依赖中存在的脆弱性，或者是我们 Web 服务器所安装软件的脆弱性。</p>
<p>小王：好吧！那就让我们打破这层信任关系。接下来该做些什么呢？</p>
<p>小陈：我们这样来分解一下系统：创建一些内部的接口用来实际访问数据库，由此以来，前端的 Web 服务器就不能直接访问后台的所有东西。</p>
<p>小王：这是个好办法！除此以外，还有其它什么可能出问题呢？</p>
<p>小陈：嗯，如果黑客攻破了我们的内网呢？</p>
<p>小王：那所有东西都要丢失了，因为内网里服务器之间的连接都是未加密的。</p>
<p>小陈：……</p>
</blockquote>
<p>这就是威胁模型，它不需要多么复杂。使用这种方式，来找出系统中可能存在的威胁。</p>
<h3 data-id="heading-70">64、源代码强制审查</h3>
<p>通过技术控制手段，防止代码未经他人审核便提交入库。这是构建安全开发环境的基础，因为它可以做到：</p>
<ol>
<li>
<p>如果攻击者攻陷了一个开发人员的电脑，或者是开发人员自身企图发起攻击，将不能直接将恶意代码迁入代码库；</p>
</li>
<li>
<p>如果开发人员的错误导致引入了有漏洞的代码，很可能在被其他人检查时及时发现。</p>
</li>
</ol>
<h3 data-id="heading-71">65、自动化持续集成管道，仅允许简单访问</h3>
<p>开发人员应该有权限触发 Jenkins 构建，且 Jenkins 权限配置也仅该如此，不要再允许其它权限。单个开发人员应该不能在构建阶段引入任意代码。当然，如果像上文推荐的强制性地采用了代码审查，Jenkinsfile 也可以保存在版本管理工具中。</p>
<h3 data-id="heading-72">66、对 artifacts 进行签名</h3>
<p>如果是构建容器镜像，可以把对镜像签名作为构建的一步。将签名密钥存储在安全的地方。构建阶段需要访问密钥，但是杜绝将密钥与 Jenkinsfile 一起存储在版本管理工具中。更好的方式是将密钥存储在 HashiCorp Vault 之类的地方，然后在构建时再进行拉取。</p>
<h3 data-id="heading-73">67、持续集成管道中加入静态应用程序扫描器</h3>
<p>在持续集成管道中使用 <a href="https://spotbugs.github.io/" target="_blank" rel="nofollow noopener noreferrer">SpotBugs</a> 和 <a href="https://find-sec-bugs.github.io/" target="_blank" rel="nofollow noopener noreferrer">Find-Sec-Bugs</a>（或者根据你所采用的技术栈进行选择）之类的工具。它们可以帮你在部署代码之前发现已知的漏洞。</p>
<p>此外，也可以作为 IDE 的插件安装在开发人员的电脑上，在代码迁入之前就运行这些工具进行检查。</p>
<h3 data-id="heading-74">68、构建时对依赖进行检查，保证最小的依赖集</h3>
<p>应用程序中依赖的每个软件包都是一个风险来源。通过依赖，我们拉取了第三人的代码并在我们的应用服务器上执行，所以，必须要搞清楚我们依赖的这个软件包是什么，为什么会依赖它？</p>
<ol>
<li>
<p>保持最小的依赖集；</p>
</li>
<li>
<p>仅使用我们所信任的依赖。它们必须是广泛使用和广为人知的；</p>
</li>
<li>
<p>采用构建框架，对依赖进行确认。</p>
</li>
</ol>
<p>此外，严格控制应用服务器的对外连接，从而避免后门的存在。</p>
<h3 data-id="heading-75">69、对依赖进行安全扫描</h3>
<p>使用 OWASP 依赖检查工具对依赖中常见的安全问题进行扫描。除了在持续集成管道中，也可以在开发人员的开发环境运行这些工具。</p>
<h3 data-id="heading-76">70、持续集成管道对镜像进行安全扫描</h3>
<p>如果采用了容器化技术，可以使用 <a href="https://github.com/aquasecurity/trivy" target="_blank" rel="nofollow noopener noreferrer">Trivy</a> 等工具对容器镜像进行一些常规漏洞的扫描。</p>
<h3 data-id="heading-77">71、自动化部署和签名验证</h3>
<p>开发人员可以有权限到生产环境中部署，但是权限范围应该控制在前阶段已经构建和签名过的特定镜像，而不是直接访问生产服务器。如果是使用 Kubernetes，可以通过 Notary 或开放策略代理来验证待部署镜像的签名。</p>
<h3 data-id="heading-78">72、设置一个安全人员</h3>
<p>一个人的精力是有限的。我们不能期望每个开发人员都精通渗透测试或是安全工程师。正如你不能期望所有的安全专家都是优秀的开发人员一样。因此，可以在团队中设置一个专门关注安全的人员，主要与开发人员、架构师进行交流，帮助保护我们的应用程序并在团队中传播安全意识。</p>
<h2 data-id="heading-79">三、结论</h2>
<p>保证应用程序的安全性，光靠避免漏洞时不够的，必须全面通盘考虑，主动进行防御。这里对一些主要方法进行了总结：</p>
<ul>
<li>
<p>使用最新版本的的软件组件来执行危险的操作，如身份验证、访问控制、加密、访问数据库或解析 XML，并确保正确配置了这些组件，例如 XML 解析时禁用外部实体。</p>
</li>
<li>
<p>使用平台提供的安全控制，例如反跨站请求伪造保护。</p>
</li>
<li>
<p>使用 Web 浏览器提供的安全控件，如 HSTS、SameSite Cookie 和内容安全策略。</p>
</li>
<li>
<p>对安全控制进行集中化处理，特别是身份验证和访问控制，从而避免一些遗漏，如在某些控制器方法上忘记对安全进行控制。</p>
</li>
<li>
<p>使用 Web 应用程序防火墙，防止应用程序漏洞被发现和被利用。</p>
</li>
<li>
<p>通过限制对文件、网络和系统资源的访问来对应用程序进行限制。</p>
</li>
<li>
<p>利用威胁模型发现架构中的威胁，并相应进行处理。既包括在源代码层面对每个开发人员的源代码进行安全控制，也包括在架构层面对前端 Web 服务器的安全控制。</p>
</li>
<li>
<p>对系统进行监控，制定异常处理预案。</p>
</li>
<li>
<p>在开发环境和持续集成环境中使用漏洞扫描程序对代码、镜像、依赖进行扫描。</p>
</li>
<li>
<p>对开发人员、架构师等开展安全培训，并在团队中配备一名安全人员。</p>
</li>
</ul>
<hr>
<p>如果你看到最后一定是收获颇丰，这里还有一个收获更多知识的方法，但比读完这篇文章要难得多，<a href="https://mp.weixin.qq.com/s/9FUQ2i0HbemwfIj9sa1p0A" target="_blank" rel="nofollow noopener noreferrer">加入我们</a>一起变强！</p>
<blockquote>
<p>变强之路充满荆棘，所以强者才受人尊敬</p>
</blockquote></div>  
</div>
            