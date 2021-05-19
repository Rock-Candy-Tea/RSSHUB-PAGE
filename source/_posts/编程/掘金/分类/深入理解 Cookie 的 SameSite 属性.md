
---
title: '深入理解 Cookie 的 SameSite 属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c0cad0cdb5f476881eb9a2c2f9b48ac~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 06:15:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c0cad0cdb5f476881eb9a2c2f9b48ac~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Cookie 简介</h3>
<p>HTTP 协议是<strong>无状态</strong>的，但可以通过 Cookie 来维持客户端与服务端之间的“会话状态”。</p>
<p>简单来说就是：服务端通过 <strong>Set-Cookie</strong> 响应头设置 Cookie 到客户端，而客户端在下次向服务器发送请求时添加名为 <strong>Cookie</strong> 的请求头，以携带服务端之前“埋下”的内容，从而使得服务端可以识别客户端的身份。</p>
<p>举个简单的🌰：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 服务端</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">"http"</span>);

http
  .createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
      res.end(<span class="hljs-string">"hello world"</span>);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/favicon.ico"</span>) &#123;
      res.statusCode = <span class="hljs-number">204</span>;
      res.end();
    &#125; <span class="hljs-keyword">else</span> &#123;
      res.writeHead(<span class="hljs-number">200</span>, [
        [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421"</span>], <span class="hljs-comment">// 设置 cookie</span>
      ]);
      res.end(<span class="hljs-string">"some data"</span>);
    &#125;
  &#125;)
  .listen(<span class="hljs-number">80</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 客户端</span>
<span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">"/someapi"</span>);
xhr.send();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c0cad0cdb5f476881eb9a2c2f9b48ac~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当客户端再次发起请求时就会自动携带上之前“埋下”的 Cookie：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/774e5734b5054b0fb91efb7d986d18c3~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单的介绍完 Cookie 后，我们来看一下它的 <code>SameSite</code> 属性。</p>
<h3 data-id="heading-1">SameSite 属性</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44da76741b50490aac2a303f4468f50b~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>SameSite</code> 有三个可选值：</p>
<ul>
<li><code>Strict</code></li>
<li><code>Lax</code></li>
<li><code>None</code>。</li>
</ul>
<p>从 Chrome 80 开始，如果不指定 SameSite 就等效于设置为 <code>Lax</code>。你可以通过 chrome://flags/#same-site-by-default-cookies 禁用这个行为，禁用后不指定 SameSite 就等效于设置为 <code>None</code>。关于他们的区别我们稍后结合具体的场景来介绍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cac5d83dae04114b0df71ea20b5be18~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先来看看上图中出现的 <code>third-party</code> 这个概念，对 Cookie 来说什么是<strong>第三方</strong> 呢，"SameSite 同站" 又是什么意思呢？</p>
<p>举个例子：假设我们的网站是 bar.com ，当我们引入 foo.com 的图片时，图片服务如果设置了 cookie，我们就称之为”<strong>第三方 cookie</strong>“。</p>
<p>是否是 “第三方” 不是根据同源策略（协议，主机，端口）来判断，而是 <a href="https://en.wikipedia.org/wiki/Public_Suffix_List" target="_blank" rel="nofollow noopener noreferrer">PSL</a>（公共后缀列表），比如 'bar.com' 和 'a.bar.com' 就不是 “第三方” 的关系，而是“同站”。检测两个域名是否是同站的方法也很简单，比如你在 'a.bar.com' 网站，设置 <code>document.domain = 'bar.com'</code> 并不会报错，但如何设置 <code>document.domain = 'foo.com'</code> 就会报错，那么 'foo.com' 相对于 'a.bar.com' 来说就是第三方。</p>
<blockquote>
<p>更权威的解释可以参考这里<a href="https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-03#section-5.2" target="_blank" rel="nofollow noopener noreferrer">"Same-site" and "cross-site" Requests</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60abcc2e0a60439bb79717c3cc859e0c~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6bcffebbc894ff2bfa4152f19f72cc9~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当端口不同时，比如我们的网站是 bar.com:8080 ，我们引入 bar.com:9000 的图片时不会判定为第三方的</p>
<p>但是协议不同默认会判定为第三方。比如我们的网站是 <a href="http://bar.com/" target="_blank" rel="nofollow noopener noreferrer">bar.com</a> ，我们引入 <a href="https://bar.com/" target="_blank" rel="nofollow noopener noreferrer">bar.com</a> 的图片时会判定为第三方。不过在 Chrome 中你可以通过 chrome://flags/#schemeful-same-site 来忽略协议的限制。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f9126e337cf4254b5422470ecbb60ac~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了图片这种场景，向第三方网站发起 AJAX/fetch 请求、嵌入第三方网站的 iframe、表单提交到第三方网站、链接跳转到第三方网站等都可能涉及到“第三方 cookie”。针对这些可能出现 “第三方cookie”  的场景，SameSite 设置为不同的值又会有哪些不同的效果呢？让我们来一一探究（多图警告😀）：</p>
<h3 data-id="heading-2">1. AJAX 请求</h3>
<p>当我们跨域发送 AJAX 请求时，由于浏览器同源策略的限制，我们的请求是无法发送的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a9d9f6910c24268acf465e817c2c523~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过我们可以使用 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS" target="_blank" rel="nofollow noopener noreferrer">CORS</a> 的方式来解决跨域的问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">"http"</span>);

http
  .createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
      res.end(<span class="hljs-string">"hello world"</span>);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/favicon.ico"</span>) &#123;
      res.statusCode = <span class="hljs-number">204</span>;
      res.end();
    &#125; <span class="hljs-keyword">else</span> &#123;
      res.writeHead(<span class="hljs-number">200</span>, [
        [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421"</span>], <span class="hljs-comment">// 设置 cookie</span>
        [<span class="hljs-string">"Access-Control-Allow-Origin"</span>, <span class="hljs-string">"*"</span>], <span class="hljs-comment">// 允许跨域请求</span>
      ]);
      res.end(<span class="hljs-string">"some data"</span>);
    &#125;
  &#125;)
  .listen(<span class="hljs-number">80</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/716fa62c6d034129813add6675fd0756~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是当我们再次发起请求时，虽然这个跨域请求的响应头中有设置 Cookie，却发现下次请求时并不会携带之前服务器设置的 Cookie。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26f823ef0ee8484fa27e46b51de9f165~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这就带来一个问题，我们失去了利用 Cookie 来维持服务端与客户端“会话状态”的能力</strong>。那么如何在向第三方网站请求的时候携带 Cookie 呢？需要满足如下条件：</p>
<ol>
<li>网站开启 https 并将 Cookie 的 Secure 属性设置为 true</li>
<li>Access-Control-Allow-Origin 设置为具体的 origin，而不是 *</li>
<li>Access-Control-Allow-Credentials 设置为 true</li>
<li>SameSite 属性设置为 None</li>
</ol>
<blockquote>
<p>想在本地测试这段代码的同学需要注意一下，<a href="http://www.foo.com/" target="_blank" rel="nofollow noopener noreferrer">www.foo.com</a> 和 <a href="http://www.bar.com/" target="_blank" rel="nofollow noopener noreferrer">www.bar.com</a> 的请求都会打到这个服务上，通过修改电脑的 hosts 文件很容易做到这一点，https 的证书是采用 mkcert 生成的自签名证书。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        res.end(<span class="hljs-string">"hellow world"</span>);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/favicon.ico"</span>) &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.writeHead(<span class="hljs-number">200</span>, [
          [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421; Secure; SameSite=None"</span>],
          ...(req.headers.origin <span class="hljs-comment">// 跨域请求时请求头中会包含 origin，也就是请求发出的网站</span>
            ? [
                [<span class="hljs-string">"Access-Control-Allow-Origin"</span>, req.headers.origin], <span class="hljs-comment">// 不可以使用 *，必须指定</span>
                [<span class="hljs-string">"Access-Control-Allow-Credentials"</span>, <span class="hljs-string">"true"</span>], <span class="hljs-comment">// 设置允许跨域请求携带 Cookie</span>
              ]
            : []),
        ]);
        res.end(<span class="hljs-string">"some data"</span>);
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>满足上面的条件之后，跨域请求就可以携带 Cookie 了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.withCredentials = <span class="hljs-literal">true</span>;
xhr.open(<span class="hljs-string">'GET'</span>, <span class="hljs-string">"https://www.bar.com/someapi"</span>);
xhr.send();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/348d51adf1f944f8acf451087f301cfc~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这四个条件缺一不可：</strong></p>
<p>当不开启 https 的时候：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1cbe833712445c798c97d5bc4372ac8~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当不设置 Secure 属性：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99eeefaf9a8a4054857ee5587c6466d2~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当 Access-Control-Allow-Origin 设置为 * 时</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e23bf21b7a74a37a2823902b247eeb1~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当 Access-Control-Allow-Credentials 的值不为 true 时</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e251772a7254b7abb734f43381534bd~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当 SameSite 属性设置为 Strict 或 Lax 时</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/393d5a88637040c1bdcb3ed25ee73008~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/049d6f1d487245b182ab7aa96736908e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于使用浏览器的 fetch API 发送请求也是一样的，使用 fetch 发起跨域请求时如果想携带 cookie，需要设置 "credentials" 为 "include"：</p>
<pre><code class="hljs language-js copyable" lang="js">fetch(<span class="hljs-string">"https://www.bar.com/somedata"</span>, &#123;
  <span class="hljs-string">"method"</span>: <span class="hljs-string">"GET"</span>,
  <span class="hljs-string">"credentials"</span>: <span class="hljs-string">"include"</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. 嵌套第三方 iframe</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(req.headers.host);
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        <span class="hljs-keyword">if</span> (req.headers.host === <span class="hljs-string">"www.foo.com"</span>) &#123;
          res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>);
          res.end(<span class="hljs-string">`<div>这是父页面</div>
<iframe src="https://www.bar.com/"></iframe>`</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
          res.writeHead(<span class="hljs-number">200</span>, [
            [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421; Secure; SameSite=None"</span>],
            [<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>],
          ]);
          res.end(<span class="hljs-string">`<div>这是子页面</div>`</span>);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果设置了SameSite 为 Strict:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0cb7fecced448de932173f38b200547~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
如果设置了SameSite 为 Lax:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f17c946dd3ac4b3991d53c28ea495ba7~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
如果不指定 SameSite:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ab9e8db712448de8339a0fef0162c12~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
如果设置了 SameSite 为 None:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a9e065ac3b64cb0a288fea9c91e3b8e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这说明只有明确的指定了 SameSite 为 None 时，跨域 iframe 页面被引入时 Cookie 才能生效。</p>
<p>举例说明一下：假设我们希望在自己的网站内嵌 bilibili 的视频播放器，直接通过 iframe 把 B 站播放器引入到我们自己的网站是无法使用 1080p 画质的。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">iframe</span>
  <span class="hljs-attr">src</span>=<span class="hljs-string">"//player.bilibili.com/player.html?bvid=BV1Vv41157uK&high_quality=1"</span>
  <span class="hljs-attr">allowfullscreen</span>=<span class="hljs-string">"allowfullscreen"</span>
  <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span>
  <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span>
  <span class="hljs-attr">scrolling</span>=<span class="hljs-string">"no"</span>
  <span class="hljs-attr">frameborder</span>=<span class="hljs-string">"0"</span>
></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05d287e8dbe5496ca38230e0920eeccb~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是由于 B 站 Cookie 的 SameSite 属性并没有设置为 None，内嵌在其他第三方网站时 B 站播放器无法传递 Cookie 到服务器，服务器也就拿不到用户的登录态，对于未登录的用户 B 站是不提供 1080p 播放的。</p>
<p>不过在 Chrome 中我们可以通过禁用 chrome://flags/#same-site-by-default-cookies 来让”第三方 cookie“默认为 None，当我们关闭这个选项并重启浏览器之后，就可以在内嵌 iframe 中播放 1080p 的 B站视频了（前提是在 B 站已经登录过）。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7bbf474da434837ae2e1be7e21b6667~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">3. 加载第三方图片或脚本等</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(req.headers.host, req.url);
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        <span class="hljs-keyword">if</span> (req.headers.host === <span class="hljs-string">"www.foo.com"</span>) &#123;
          res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>);
          res.end(<span class="hljs-string">`<div>这是父页面</div>
<img src="https://www.bar.com/"></img>`</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
          res.writeHead(<span class="hljs-number">200</span>, [
            [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421; Secure; SameSite=Strict"</span>],
            [<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"image/png"</span>],
          ]);
          fs.createReadStream(<span class="hljs-string">"logo.png"</span>).pipe(res);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3850f7bdb67b4cc3841f164e6adbd046~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9f440e0aa9d45bc9b39cb9d464bb409~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a6a07fe47284b8ba33245dc11605558~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6451147a5ca4cfe8d8cbc7d5e96945e~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这和引入第三方的 iframe 是一样的，只有 SameSite 属性为 None，Cookie 才能生效。</p>
<p>举个应用的例子：下图是一个添加了谷歌广告的网站，可以看到谷歌广告相关的 Cookie 会把 SameSite 属性设置为 None。这样当足够多的网站引入了谷歌的广告脚本等资源时，他就可以构建出用户在各个网站的浏览轨迹以及访问偏好了，从而精准的推送广告。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab8f5ea72d034918adff3e7b5a751f13~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">4. 提交表单到第三方网站</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        <span class="hljs-keyword">if</span> (req.headers.host === <span class="hljs-string">"www.foo.com"</span>) &#123;
          res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>);
          res.end(<span class="hljs-string">`<form action="https://www.bar.com/" method="post" enctype="multipart/form-data">
<input type="text" name="name" />
<input type="number" name="age" />
<button type="submit">提交</button>
</form>`</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(req.headers.host, req.url, req.method, req.headers.cookie);
          res.writeHead(<span class="hljs-number">200</span>, [
            [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421; Secure; SameSite=Strict"</span>],
          ]);
          res.end(<span class="hljs-string">"ok"</span>);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ceecb25609346238e2a2370e29038be~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/464dff85bb1d45f8b13a7fb248b67f1c~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a82bad21dd3e4742920b2caa0ce21b1b~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的测试中可以看出将 SameSite 设置为 None 是一种危险的行为，它会使得针对你的网站发起 <a href="https://en.wikipedia.org/wiki/Cross-site_request_forgery" target="_blank" rel="nofollow noopener noreferrer">CSRF</a> (Cross-site request forgery) 攻击变得非常容易，因为从一个第三方恶意网站向你的网站发起的请求也会携带 Cookie，这使得伪造的请求会被识别为一次普通用户发起的请求。下面具体演示一下，我们假设 <a href="http://www.foo.com/" target="_blank" rel="nofollow noopener noreferrer">www.foo.com</a> 是一个恶意网站，<a href="http://www.bar.com/" target="_blank" rel="nofollow noopener noreferrer">www.bar.com</a> 是我们自己的网站：</p>
<blockquote>
<p>这部分的示例只是为了说明问题，只展示一些关键步骤，具体的细节，比如登录和登陆态校验的实现会被简化</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这是我们自己正常的网站</span>
<span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        <span class="hljs-comment">// 我们网站首页有一个转账的表单</span>
        res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>);
        res.end(<span class="hljs-string">`<form action="/transfer" method="post">
<input type="number" name="money" />
<button type="submit">提交</button>
</form>`</span>);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/login"</span>) &#123;
        <span class="hljs-comment">// 登录后，客户端会存储用户的 Cookie 信息</span>
        res.setHeader(<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421; Secure; SameSite=None"</span>);
        res.end(<span class="hljs-string">"login success"</span>);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/transfer"</span>) &#123;
        <span class="hljs-comment">// 登录后的用户可以转账，未登录的不能转账</span>
        res.end(req.headers.cookie ? <span class="hljs-string">"ok"</span> : <span class="hljs-string">"fail"</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用户直接访问 <a href="http://www.bar.com/" target="_blank" rel="nofollow noopener noreferrer">www.bar.com</a> 提交表单转账，由于没有登录（没有 Cookie）会提示失败，所以用户会先进入 <a href="http://www.bar.com/login" target="_blank" rel="nofollow noopener noreferrer">www.bar.com/login</a> 登录，登录后客户端会有 Cookie，当用户回到首页再次提交转账表单时，就会转账成功，这模拟了一个简单的基于 Cookie 鉴权的网站。</p>
<p>接下来我们一起来看看攻击者是如何突破 <a href="http://www.bar.com/" target="_blank" rel="nofollow noopener noreferrer">www.bar.com</a> 的鉴权滴。当攻击者知道了你网站有转账的功能，那么他就可以诱导用户进入准备好的恶意网站，在这个恶意网站中向你的网站发起转账请求，如果进入恶意网站的用户之前登录过你的网站并且登录态没有过期，那么这次伪造的请求就会成功把用户的钱转走。下面是恶意网站的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这是一个要伪造请求的恶意网站</span>
<span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>);
        res.end(<span class="hljs-string">`<div>这是一个恶意网站</div>
<form
id="fake-form"
action="https://www.bar.com/transfer"
method="post"
target="submit-target"
>
    <input type="hidden" name="money" value="1000" />
</form>
<iframe name="submit-target"></iframe>
<script>document.getElementById("fake-form").submit();</script>`</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3983eac70147e9ba71691a7c82c164~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，用户被诱导进入恶意网站后，恶意网站自动像你的服务器发起了伪造的转账请求，由于你 Cookie 中的 SameSite 属性设置为 None，这就导致这次伪造的请求也会携带用户的 Cookie，单纯基于 Cookie 做的接口鉴权就被攻破了，用户的资金面临安全风险。这也是为什么最新版的浏览器都会把 SameSite 的默认值从 None 调整为 Lax 的一个重要原因。</p>
<h3 data-id="heading-6">5. 链接跳转第三方网站</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> https = <span class="hljs-built_in">require</span>(<span class="hljs-string">"https"</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

https
  .createServer(
    &#123;
      <span class="hljs-attr">key</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/key.pem"</span>),
      <span class="hljs-attr">cert</span>: fs.readFileSync(__dirname + <span class="hljs-string">"/cert.pem"</span>),
    &#125;,
    <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (req.url == <span class="hljs-string">"/"</span>) &#123;
        <span class="hljs-keyword">if</span> (req.headers.host === <span class="hljs-string">"www.foo.com"</span>) &#123;
          res.setHeader(<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>);
          res.end(<span class="hljs-string">`<div>foo page</div>
<a href="https://www.bar.com/">www.bar.com</a>`</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(req.headers.host, req.url, req.headers.cookie);
          res.writeHead(<span class="hljs-number">200</span>, [
            [<span class="hljs-string">"Set-Cookie"</span>, <span class="hljs-string">"name=haochuan9421; Secure; SameSite=None"</span>],
            [<span class="hljs-string">"Content-Type"</span>, <span class="hljs-string">"text/html;charset=utf-8"</span>],
          ]);
          res.end(<span class="hljs-string">"bar page"</span>);
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.statusCode = <span class="hljs-number">204</span>;
        res.end();
      &#125;
    &#125;
  )
  .listen(<span class="hljs-number">443</span>, <span class="hljs-string">"0.0.0.0"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d35f9d3a9ac64030b2f32cbd95fee088~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5172d5de78734f928f3b2454f15298db~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19917b24ce2b4611b2c6ec1f622b6ecf~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Strict </code> 这个规则过于严格，可能造成非常不好的用户体验。比如，当前网页有一个 GitHub 链接，用户点击跳转就不会带有 GitHub 的 Cookie，跳转过去总是未登陆状态。</p>
<h3 data-id="heading-7">总结</h3>
<p>现代浏览器针对 Cookie 的 <code>SameSite</code> 属性的默认值已经很合理了，作为网站所有者通常不需要手动设置这个属性，一般只有当我们的服务需要和“第三方”对接时才考虑怎么设置更合理。</p>
<p><code>Strict</code> 最为严格，表示完全禁止“第三方 Cookie”，只有当前网页的 URL 与请求目标一致时，才会带上 Cookie，一般用于保证系统的封闭性和安全性。</p>
<p><code>Lax</code> 是目前大多数现代浏览器的默认值，他在保证安全性的前提下，也可以避免一些不好的用户体验，比如从别的网站跳转过时会没有登录态。</p>
<p><code>None</code> 是最为宽松的一种设定，通常用于开放我们的服务给不同的第三方接入，同时又需要追踪用户的场景，比如广告，设置为 <code>None</code> 时需要考虑开放的安全性。</p></div>  
</div>
            