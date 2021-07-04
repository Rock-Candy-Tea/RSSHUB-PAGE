
---
title: '小 Tips：Chrome 91 版本 Cookie Same-Site 前端本地开发解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-images.githubusercontent.com/28448589/124253943-1eca1880-db5b-11eb-86c7-063a888bc36e.png'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 01:44:40 GMT
thumbnail: 'https://user-images.githubusercontent.com/28448589/124253943-1eca1880-db5b-11eb-86c7-063a888bc36e.png'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近在本地开发环境测试公司系统时，遇到了跨域问题，导致无法登录获取用户权限。原本只要是本地浏览器存储了目标服务器的cookie 信息就可以发送跨域请求，但奇怪的是，已经通过开启 CORS 同源请求的方式获取到了 cookie，在本地开发环境启动的系统依然出现了跨域情况，检查发现请求根本没有自动携带 cookie。为什么开启了 CORS，还是会出现跨域的问题呢？</p>
<p>文章大纲</p>
<ul>
<li>
<p>分析问题</p>
<ul>
<li>为什么会有跨域问题</li>
<li>如何解决跨域问题</li>
<li>为什么开启 CORS，还会出现跨域</li>
</ul>
</li>
<li>
<p>解决问题</p>
<ul>
<li>
<p>浏览器关闭 Same-Site</p>
</li>
<li>
<p>使用第三方代理</p>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">分析问题</h2>
<h3 data-id="heading-2">为什么会有跨域问题</h3>
<p>跨域本质上是 浏览器实现**同源策略（Same Origin Policy）**的一种安全手段。对于同源的定义，<code>url 协议</code>（protocol）、<code>端口</code>（port）、<code>主机</code>（host 域名）完全相同称为同源站点。同源策略限制了两个不同源站点的资源访问，比如前端想通过 XMLHttpRequest 将站点数据发送给不同源站点，就会产生跨域问题。</p>
<p>比如 A 源为：<code>http://store.company.com/dir/page.html</code>，下列与 B 源 的对比。引用自 MDN <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#definition_of_an_origin" target="_blank" rel="nofollow noopener noreferrer">Definition of an origin</a></p>



































<table><thead><tr><th align="left">URL</th><th align="left">Outcome</th><th align="left">Reason</th></tr></thead><tbody><tr><td align="left"><code>http://store.company.com/dir2/other.html</code></td><td align="left">Same origin</td><td align="left">Only the path differs</td></tr><tr><td align="left"><code>http://store.company.com/dir/inner/another.html</code></td><td align="left">Same origin</td><td align="left">Only the path differs</td></tr><tr><td align="left"><code>https://store.company.com/page.html</code></td><td align="left">Failure</td><td align="left">Different protocol</td></tr><tr><td align="left"><code>http://store.company.com:81/dir/page.html</code></td><td align="left">Failure</td><td align="left">Different port (<code>http://</code> is port 80 by default)</td></tr><tr><td align="left"><code>http://news.company.com/dir/page.html</code></td><td align="left">Failure</td><td align="left">Different host</td></tr></tbody></table>
<p>而本地前端服务<code> http://localhost:9096</code> 与服务端 <code>http://api.backend.com</code> 是不同源的，存在跨域资源访问限制问题。</p>
<h3 data-id="heading-3">如何解决跨域问题</h3>
<p>解决跨域问题，有很多种方式，比如使用 <code>JSONP</code>、<code>CORS</code>、<code>Proxy</code> 等方案。在公司的项目中，使用了 CORS 方案。</p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Glossary/CORS" target="_blank" rel="nofollow noopener noreferrer">CORS</a> 跨域资源共享是为了解决同源策略的网络层面限制而引入的，它是一种基于 <a href="https://developer.mozilla.org/zh-CN/docs/Glossary/HTTP" target="_blank" rel="nofollow noopener noreferrer">HTTP</a> 头的机制，该机制通过允许服务器标示除了它自己以外的其他 <a href="https://developer.mozilla.org/zh-CN/docs/Glossary/%E6%BA%90" target="_blank" rel="nofollow noopener noreferrer">origin</a>（域，协议和端口），这样会浏览器可以访问加载这些资源。</p>
<p>如何开启呢，比如一个登录 <code>login</code> 接口简单请求，浏览器发出的请求信息会添加 <code>origin</code> 字段，<code>Origin</code>字段用来说明，本次请求来自哪个源（协议 + 域名 + 端口）。服务器根据这个值，决定是否同意这次请求。</p>
<pre><code class="copyable">  GET /cors HTTP/1.1
+ Origin: http://api.backend.com
  Host: localhost:9096
  Accept-Language: zh-CN,zh
  Connection: keep-alive
  User-Agent: Mozilla/5.0...
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>Origin</code>指定的域名在许可范围内，服务器会设置响应头 <code>Access-Control-Allow-Origin</code> ，浏览器会检查这个字段，从而让 <code>XMLHttpRequest</code> 正常获得结果，否则，就会抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js">+ Access-Control-Allow-Origin: http:<span class="hljs-comment">//localhost:9096</span>
<span class="hljs-built_in">Set</span>-cookie: token=xxxx; Path=xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，服务器会通过 <code>Session-Cookie</code> 机制维护用户的登录状态，从而使用 <code>Set-Cookie</code> 告诉浏览器中写入 <code>Cookie</code>。</p>
<p>登录成功后，客户端再次发送一个 <code>getUser</code> 接口用于获取用户权限信息，要携带之前的 <code>Cookie</code> 发送给服务端。</p>
<p>由于  CORS 请求默认不发送 Cookie 和 HTTP 认证信息。所以要把 Cookie 发送到服务器，需要 <code>ajax</code> 请求中开发 <code>withCredentials</code> 属性 为 <code>true</code>，并且服务端要指定 <code>Access-Control-Allow-Credentials</code> 字段：</p>
<pre><code class="hljs language-sh copyable" lang="sh">+ Access-Control-Allow-Credentials: <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且<code>Access-Control-Allow-Origin</code>就不能设为星号，必须指定明确的、与请求网页一致的域名。这样，就可以实现携带 Cookie 正常访问不同源的服务端资源了。</p>
<h3 data-id="heading-4">为什么开启 CORS，还会出现跨域</h3>
<p>通过查看浏览器的 Chrome Network 发现，登录成功后，getUser 接口发送的浏览器请求没有正常携带 Cookie 字段。关于 cookie 无法被携带问题，有不少排查的方向，</p>
<ul>
<li>浏览器是可以禁用 Cookie 的  <code>chrome://settings/cookies?search=cookie</code></li>
<li>浏览器的插件导致，可以考虑使用无痕模式测试</li>
<li>是否开启了某些工具模拟请求，网络设置问题</li>
<li>是否是 Cookie 的属性设置问题，比如 domain、path、失效时间等。</li>
<li>...</li>
</ul>
<p>经过仔细排查后发现这是因为浏览器设置的 Cookie 的 Same-Site 属性问题，导致 Cookie 无法被正常携带。</p>
<p><img src="https://user-images.githubusercontent.com/28448589/124253943-1eca1880-db5b-11eb-86c7-063a888bc36e.png" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Cookie</code> 的 <code>Same-Site</code> 属性是为了防止（CSRF-Cross-Site-Request-Forgery）<code>跨站请求伪造攻击</code>，CSRF 是指在受害者访问一个网站时，其 Cookie 还没有过期的情况下，攻击者伪造一个链接地址发送受害者并欺骗让其点击，从而获取用户信息。</p>
<p><code>Same-Site</code> 名为同站，那它跟跨站、跨域有什么区别呢，理解它们的区别有利于我们更好的理解 <code>Cookie</code> 的 <code>Same-Site</code> 属性。</p>
<h4 data-id="heading-5">同站（Same-Site）、跨站（Cross-Site）与跨域（Cross-Origin）的区别</h4>
<p><strong>跨域</strong></p>
<p>本质上是 浏览器实现**同源策略（Same Origin Policy）**的一种安全手段。对于同源的定义，url 协议（protocol）、端口（port）、主机（host 域名）完全相同称为同源站点。</p>
<p><strong>同站与跨站</strong></p>
<p>只要两个 URL 的<code>eTLD+1</code> 相同即是同站，否则为跨站，不需要考虑协议和端口。</p>
<p><strong>eTLD</strong>: (effective top-level domain) 有效顶级域名，注册于 Mozilla 维护的公共后缀列表（Public Suffix List）中,如 <code>.com</code>、<code>.org</code> 、<code>.com</code> 等</p>
<p><strong>eTLD+1</strong>: 有效顶级域名 + 二级域名，如 <code>taobao.com</code>，<code>baidu.com</code>，<code>sugarat.top</code></p>
<blockquote>
<p>参考MDN <a href="https://developer.mozilla.org/en-US/docs/Glossary/TLD" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></p>
</blockquote>
<h4 data-id="heading-6">Cookie 的 Same-Site</h4>
<p>大部分网站使用了 Cookie 来存储登录状态，保护 Cookie 不被三方站点利用尤为重要，我们可以合理设置 <code>Cookie</code> 的 <code>Samesite</code> 属性值防御 <code>CSRF</code> 攻击。</p>
<ul>
<li><code>strict</code>：严格校验，严格校验站点是否为同源</li>
<li><code>lax</code>：较宽松校验，在跨站点的情况下，从第三方网站打开链接，get 方式提交表单都会携带 cookie，
但如果在第三方站点中使用了 post 方法，或者通过 img，iframe 等标签加载的 url，会禁止 cookie 发送</li>
<li><code>none</code>：不校验第三方站点是否为同源或同一站点，任何情况下都会发送 cookie</li>
</ul>
<h2 data-id="heading-7">解决问题</h2>
<h3 data-id="heading-8">浏览器关闭 Cookie 的 Same-Site</h3>
<p>我们可以通过手动关闭 Cookie 的 Same-Site，这样就正常携带 Cookie 给服务端了。在 Chrome 浏览器中可以输入 <code>chrome://flags/</code></p>
<p>把 <code>SameSite by default Cookie</code> 和 <code>Cookies without SameSite must be secure</code> 禁用掉。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccaac866011740b7a46123ce5d9b1d68~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>SameSite by default Cookie</code> 禁用或开启 SameSite Cookie 的规则</li>
<li><code>Cookies without SameSite must be secure</code> ：当没有设置 <code>SameSite</code> 属性或者设为 <code>None</code> 的时候，开启这个规则就要求跨站的前后端数据通信必须是 https 协议。</li>
</ul>
<p>在 91 版本以前，是可以这样做的。仔细发现浏览器 Chrome 自动升级到了 91 版本，91 版本不再给手动关闭了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c3ffc210cd24fa3874fd6d07d067cfe~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果想让后端设置响应头关闭，通过设置 <code>Set-Cookie</code> 时设置  <code>Same-Site</code> 属性为 <code>none </code>，但是这种做法要 https 协议才支持，必须设置 <code>Secure</code> 属性。</p>
<pre><code class="hljs language-bash copyable" lang="bash">Set-Cookie: widget_session=abc123; SameSite=None; Secure
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然不能手动设置了，还有其他的方案吗？</p>
<p>方案一：本地开发暂时不升级到 91 版本了。</p>
<p>方案二：通过反向代理解决这个问题。</p>
<p>接下来具体说说方案二。</p>
<h3 data-id="heading-9">使用第三方代理</h3>
<p>在使用代理解决 Cookie 携带问题前，先要搞懂什么是正向代理和反向代理。</p>
<p>正向代理与反向代理的区别是他们提供的服务对象不同，</p>
<ul>
<li>正向就是对服务获取方服务的，表现为在客户端的出口位置，主要解决客户端的问题（比如科学上外网）</li>
<li>反向就是对服务提供方服务的，表现为在服务端的网络入口位置，主要解决服务端的问题（负载均衡）</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11e565e8ca3948d4a504b0d36c2d117b~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>来自知乎某图 <a href="https://www.zhihu.com/question/24723688" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com/question/24…</a></p>
<h4 data-id="heading-10">正向代理</h4>
<p>举个例子，没有代理的情况下，日常 git clone 仓库常常 443 错误，这是 https 开放的默认端口。</p>
<pre><code class="hljs language-js copyable" lang="js">git clone https:<span class="hljs-comment">//github.com/alexjoverm/typescript-library-starter.git ts-axios</span>
Cloning into <span class="hljs-string">'ts-axios'</span>...
<span class="hljs-attr">fatal</span>: unable to access <span class="hljs-string">'https://github.com/alexjoverm/typescript-library-starter.git/'</span>: LibreSSL SSL_connect: SSL_ERROR_SYSCALL <span class="hljs-keyword">in</span> connection to github.com:<span class="hljs-number">443</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67062f660a904c06916a6d405f23de9d~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 使用socks5协议</span>
HTTP_PROXY="socks5://127.0.0.1:1086" HTTPS_PROXY="socks5://127.0.0.1:1086" git clone https://github.com/alexjoverm/typescript-library-starter.git ts-axios
<span class="hljs-meta">
#</span><span class="bash"> 使用http协议</span>
HTTP_PROXY="http://127.0.0.1:1087" HTTPS_PROXY="http://127.0.0.1:1087" git clone https://github.com/alexjoverm/typescript-library-starter.git ts-axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正向代理：客户端 --- 代理服务器 --- 目标服务器。这样就可以正常下载仓库了。</p>
<h4 data-id="heading-11">反向代理</h4>
<p>除了使用反向代理作负载均衡外，还可以使用反向代理解决跨站携带 Cookie 的问题，核心思路就是在前端本地使用代理服务器，整个数据的传递方式是 <code>目标服务器---代理服务器---浏览器</code>，而本地代理服务器与本地浏览器是属于同站，不存在跨站问题，而服务器与服务器之间传递数据没有同源策略的限制，并不会存在跨域行为，代理服务器与目标服务器之间能正常转发 Cookie， 浏览器就能正常携带 Cookie 给目标服务器了。</p>
<p>如果你是 Vue 项目的话，一般是通过 <code>Vue-Cli</code> 脚手架搭建，要使用实现代理服务，可以直接在 <code>vue.config.js</code> 文件对应 <code>webpack</code> 的 w配置增加 <code>devServer.proxy</code> 配置，值为要被代理的目标地址，</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">9000</span>
    <span class="hljs-attr">proxy</span>: <span class="hljs-string">'http://backend.com:4000'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前端根据 <code>devServer.port</code> 修改资源请求的地址为对应的  <code>localhost + port</code> 的形式即可，也就是说前端直接请求代理服务器地址即可，<code>http://localhost:9000</code>，这样前端发送请求，由于与代理服务器是同站，浏览器就会携带上 Cookie，Cookie 经过代理服务器进行转发给目标服务器，这样就可以正常维持登录状态了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ca242c4d63449c2a1b560432f6149b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了上面的方式外，你也可以使用 node 构建一个简单的代理服务器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">"http"</span>);
<span class="hljs-keyword">const</span> httpProxy = <span class="hljs-built_in">require</span>(<span class="hljs-string">"http-proxy"</span>); <span class="hljs-comment">// 通过 http-proxy 实现代理功能</span>

<span class="hljs-keyword">const</span> proxy = httpProxy.createProxyServer();

proxy.on(<span class="hljs-string">"error"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, req, res</span>) </span>&#123;
  res.end();
&#125;);

<span class="hljs-keyword">const</span> proxy_server = http.createServer(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res</span>) </span>&#123;
  proxy.web(req, res, &#123;
    <span class="hljs-attr">target</span>: <span class="hljs-string">"http://backend.com:18080"</span> <span class="hljs-comment">// 目标服务器</span>
  &#125;);
&#125;);

proxy_server.listen(<span class="hljs-number">8080</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 代理服务器监听的端口</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"proxy server is running"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在生产环境上，前端应用与后端应用不在同一个服务器上，还可以使用 nginx 进行代理转发。</p>
<ol>
<li>把访问 <code>http://代理服务器地址:9001/edu</code> 的请求转发到 <code>http://目标服务器1:8080</code></li>
<li>把访问 <code>http://代理服务器地址:9001/vod</code> 的请求转发到 <code>http://目标服务器2:8081</code></li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">server &#123;
  listen 9001; // 代理服务器端口
  server_name xxx.xxx // 代理服务器域
  ;

  location ~ /edu/ &#123;
    proxy_pass http://目标服务器域1:8080;
  &#125;
  
  location ~ /vod/ &#123;
    proxy_pass http://目标服务器域2:8081;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">小结</h2>
<p>对于 Cookie Same-Site 的处理，本质上还是解决跨域的问题，离不开业界的方案，比如 CORS、设置代理，还可以通过 token 认证方式绕过这种处理，前端拿到服务端的 token 保存到本地，每次请求时都写到请求头里，这也是一种方案。</p>
<h2 data-id="heading-13">参考资料</h2>
<ul>
<li>
<p><a href="http://www.ruanyifeng.com/blog/2016/04/cors.html" target="_blank" rel="nofollow noopener noreferrer">跨域资源共享 CORS 详解</a> 阮一峰大佬，详细讲解了 CORS 机制对简单请求和非简单请求的两种不同处理，以及客户端和服务端的配置区别。</p>
</li>
<li>
<p><a href="https://juejin.cn/post/6844904095271288840" target="_blank">当 CORS 遇到 SameSite</a></p>
</li>
<li>
<p><a href="https://github.com/mqyqingfeng/Blog/issues/157" target="_blank" rel="nofollow noopener noreferrer">浏览器系列之 Cookie 和 SameSite 属性</a></p>
</li>
<li>
<p><a href="https://github.com/shadowsocks/shadowsocks-windows/issues/407" target="_blank" rel="nofollow noopener noreferrer">git 设置代理</a></p>
</li>
<li>
<p><a href="https://www.cnblogs.com/anker/p/6056540.html" target="_blank" rel="nofollow noopener noreferrer">正向代理与反向代理</a></p>
</li>
</ul></div>  
</div>
            