
---
title: '在 Next.js 中使用 connect 中间件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1250'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 18:34:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=1250'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文节选自 <a href="http://nextjs-in-action-cn.taonan.lu/" target="_blank" rel="nofollow noopener noreferrer">Next.js 应用开发实践</a></p>
</blockquote>
<p>Next.js 没有中间件机制。首先让我简单解释一下什么是中间件，为什么我们需要中间件。</p>
<p>在 Express/Koa, 我们可以用中间件进入一个请求的生命周期，一个典型的中间件是一个函数，它接受 <code>req</code>, <code>res</code> 和 <code>next</code> 参数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">exampleMiddleware</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-comment">/** ...*/</span>) &#123;
    req.foo = <span class="hljs-string">'bar'</span>
  next()
  &#125; <span class="hljs-keyword">else</span> &#123;
    res.statusCode = <span class="hljs-number">403</span>
    res.send(<span class="hljs-string">'forbiddon'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这个中间件的模式起源于一个 Node.js Web 框架 <a href="https://github.com/senchalabs/connect" target="_blank" rel="nofollow noopener noreferrer">connect</a>, 早期的 Express 也基于 Connect 开发，于是很多框架也兼容了这种模式，所以这种中间件模式我们通常称为 connect 中间件。</p>
</blockquote>
<p>在中间件里，我们可以：</p>
<ul>
<li>在 <code>req</code> 对象注入一些属性，这些属性可以被下一个中间件或者 controller 获取到。</li>
<li>可以通过不执行 <code>next()</code> 来中止请求，同时修改 <code>res</code> 的属性从而改变 response 的状态。</li>
</ul>
<p>这使得中间件可以很好地使代码在不同的路由之间重用。假设我们需要在一个路由跟据 cookies 获取用户信息，我们可以把这个获取用户信息的方法写成中间件，然后把用户信息注入到 <code>req.user</code>，这样所以使用了这个中间件的路由可以通过 <code>req.user</code> 取得用户信息。而且在中间件中，如果判断用户没有登录，可以中止这个请求，并返回 403.</p>
<p>下面是 Express 编写和使用中间件的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">authMiddleware</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
  <span class="hljs-comment">// 假设 cookies 中用 `token` 保存用户信息</span>
  <span class="hljs-keyword">if</span> (req.cookies.token) &#123;
    <span class="hljs-keyword">const</span> user = getUserByToken(req.cookies.token)
    req.user = user
    next()
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// cookies.token 不存在，中止请求并返回 403</span>
    res.statusCode = <span class="hljs-number">403</span>
    res.send(<span class="hljs-string">'please sign in first'</span>)
  &#125;
&#125;

<span class="hljs-comment">// 不使用这个中间件的路由</span>
app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.send(<span class="hljs-string">'hello world'</span>)
&#125;)

<span class="hljs-comment">// 使用这个中间件的路由</span>
app.get(<span class="hljs-string">'/profile'</span>, authMiddleware, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  <span class="hljs-comment">// 可以通过 `req.user` 取得用户信息</span>
  res.send(<span class="hljs-string">`welcome! <span class="hljs-subst">$&#123;req.user.name&#125;</span>`</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在 Next.js 要做同样的事，我们会这么做：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// pages/api/example.ts</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">auth</span>(<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (req.cookies.token) &#123;
    <span class="hljs-keyword">const</span> user = getUserByToken(req.cookies.token)
    <span class="hljs-keyword">return</span> user
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 用户未登录</span>
    res.status(<span class="hljs-number">403</span>)
    res.send(<span class="hljs-string">'please sign in first'</span>)
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (req, res) => &#123;
  <span class="hljs-keyword">if</span> (req.method === <span class="hljs-string">'GET'</span>) &#123;
    res.send(<span class="hljs-string">'hello'</span>)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (req.method === <span class="hljs-string">'POST'</span>) &#123;
    <span class="hljs-keyword">const</span> user = auth(req, res)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'do other things'</span>)
  res.send(<span class="hljs-string">`welcome! <span class="hljs-subst">$&#123;user.name&#125;</span>`</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但在 Next.js, 我们没有任何办法中止请求。理论上 <code>console.log('do other things')</code> 在用户未登录时不应该被执行。</p>
<h3 data-id="heading-0">使用 <code>next-connect</code></h3>
<p>要在 Next.js 中像 Express/Koa 这样使用 connect 中间件，我们可以使用  <a href="https://github.com/hoangvvo/next-connect" target="_blank" rel="nofollow noopener noreferrer">next-connect</a> 这个库。</p>
<blockquote>
<p>安装 <code>next-connect</code>:</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add next-connect
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>现在，让我们用 <code>next-connect</code> 重写上面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// pages/api/example.ts</span>

<span class="hljs-keyword">import</span> nc <span class="hljs-keyword">from</span> <span class="hljs-string">'next-connect'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">authMiddleware</span>(<span class="hljs-params">req, res, next</span>) </span>&#123;
  res.status(<span class="hljs-number">403</span>)
  res.send(<span class="hljs-string">'please sign in first'</span>)
&#125;

<span class="hljs-comment">// 用 `nc()` 创建一个 api handler</span>
<span class="hljs-keyword">const</span> handler = nc()
  .get(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    res.send(<span class="hljs-string">'hello'</span>)
  &#125;)
  .post(authMiddleware, <span class="hljs-function">(<span class="hljs-params">req,res</span>) =></span> &#123;
    res.send(<span class="hljs-string">'hello'</span>)
  &#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> handler
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，现在我们在 Next.js 的API route 可以像在 Express 一样使用中间件。</p>
<p>在 <code>authMiddleware</code>中，我们返回了一个 403，并且没有执行 <code>next()</code>, 模拟了用户未登录的情况。由于 <code>next()</code> 没有执行，这个 POST 请求不会执行这个 POST handler 的代码。</p>
<p>用 <code>next-connect</code> 的另一个好处是，我们可以用<code>.get()</code>, <code>.post()</code>, <code>put()</code> 这样的 helper 来创建对应的 handler, 而不需要用 <code>if (req.method === XXX)</code> 这样的判断。让代码更好读。</p>
<p>因为 <code>next-connect</code> 兼容 connect 中间件，所以我们可以直接用社区上成熟的 connect 中间件，例如用于修改跨域设置的中间件 <code>cors</code>:</p>
<blockquote>
<p>安装 <code>cors</code>:</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add cors
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<pre><code class="hljs language-diff copyable" lang="diff">// pages/api/example.ts

import nc from 'next-connect'
<span class="hljs-addition">+ import * as cors from 'cors'</span>

const corsOptions = &#123;
  origin: 'http://example.com',
  optionsSuccessStatus: 200
&#125;

const handler = nc()
<span class="hljs-addition">+.use(cors(corsOptions))</span>
  .get((req, res) => &#123;
    res.send('hello')
  &#125;)
  .post(authMiddleware, (req,res) => &#123;
    res.send('hello')
  &#125;)

export default handler
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            