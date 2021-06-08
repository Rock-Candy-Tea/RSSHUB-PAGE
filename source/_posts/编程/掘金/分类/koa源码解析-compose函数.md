
---
title: 'koa源码解析-compose函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6d786b6f83442e0b6d830ee7e6fc0d6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 08:58:43 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6d786b6f83442e0b6d830ee7e6fc0d6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>孤阴不生，独阳不长，负阴而抱阳，充气以为和。</p>
<h2 data-id="heading-0">前言</h2>
<p>本文主要介绍的是koa框架是如何优雅的处理中间件。</p>
<p><em>基于koa v2.13.1、koa-compose v4.2.0</em></p>
<h2 data-id="heading-1">使用示例</h2>
<p>先看一段我们很熟悉的node项目中入口文件代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();

<span class="hljs-comment">// logger</span>

app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
  <span class="hljs-keyword">await</span> next();
  <span class="hljs-keyword">const</span> rt = ctx.response.get(<span class="hljs-string">'X-Response-Time'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;ctx.method&#125;</span> <span class="hljs-subst">$&#123;ctx.url&#125;</span> - <span class="hljs-subst">$&#123;rt&#125;</span>`</span>);
&#125;);

<span class="hljs-comment">// x-response-time</span>

app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
  <span class="hljs-keyword">const</span> start = <span class="hljs-built_in">Date</span>.now();
  <span class="hljs-keyword">await</span> next();
  <span class="hljs-keyword">const</span> ms = <span class="hljs-built_in">Date</span>.now() - start;
  ctx.set(<span class="hljs-string">'X-Response-Time'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;ms&#125;</span>ms`</span>);
&#125;);

<span class="hljs-comment">// response</span>

app.use(<span class="hljs-keyword">async</span> ctx => &#123;
  ctx.body = <span class="hljs-string">'Hello World'</span>;
&#125;);

app.listen(<span class="hljs-number">3000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码很简单，主要就是三个步骤：</p>
<ol>
<li>创建一个koa对象的实例app</li>
<li>再调用app的use方法。以app.use(XX).use(XX)插入中间件函数。</li>
<li>最后调用启动方法，并监听3000端口</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6d786b6f83442e0b6d830ee7e6fc0d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">中间件方法的保存，与触发</h2>
<h3 data-id="heading-3">1. 保存中间件</h3>
<p>首先我们来看看是如何以<code>app.use(fn).use(fn).use(fn)</code>保存中间件的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//lib/application.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Emitter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">fn</span>)</span> &#123;
    <span class="hljs-comment">//校验fn格式</span>
    <span class="hljs-built_in">this</span>.middleware.push(fn);
    <span class="hljs-comment">//返回this，可以一直app.use()重复调用</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;  
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>app.use(fn)</code>做的事情很简单：就是在<code>http</code>服务启动前，将我们项目预设的中间件保存在<code>middleware</code>数组中，等待<code>http</code>服务发起回调触发这些中间件。</p>
<p>那下面我们看看一个http请求过来，保存在<code>middleware</code>中的中间件是如何触发的。</p>
<h3 data-id="heading-4">2. 触发中间件</h3>
<p>创建一个<code>http</code>的服务<code>server</code>，并以<code>callback()</code>作为回调。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">listen</span>(<span class="hljs-params">...args</span>)</span> &#123;
    <span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-built_in">this</span>.callback());
    <span class="hljs-keyword">return</span> server.listen(...args);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>callbakc()</code>方法中，以<code>compose</code>来组织中间件，放返回回调方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">callback</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//以某种方式组织这些中间件</span>
    <span class="hljs-keyword">const</span> fn = compose(<span class="hljs-built_in">this</span>.middleware);

    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.listenerCount(<span class="hljs-string">'error'</span>)) <span class="hljs-built_in">this</span>.on(<span class="hljs-string">'error'</span>, <span class="hljs-built_in">this</span>.onerror);

    <span class="hljs-comment">//获取到http请求中的req，res，保存在ctx上下文中</span>
    <span class="hljs-keyword">const</span> handleRequest = <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> ctx = <span class="hljs-built_in">this</span>.createContext(req, res);
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handleRequest(ctx, fn);
    &#125;;
    <span class="hljs-comment">//返回经过compose处理后的中间件方法</span>
    <span class="hljs-keyword">return</span> handleRequest;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在接受的<code>http</code>请求时，作为回调函数执行经过compose处理过的中间件方法，修改上下文<code>ctx</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">handleRequest</span>(<span class="hljs-params">ctx, fnMiddleware</span>)</span> &#123;
    <span class="hljs-keyword">const</span> res = ctx.res;
    <span class="hljs-keyword">const</span> onerror = <span class="hljs-function"><span class="hljs-params">err</span> =></span> ctx.onerror(err);
    <span class="hljs-keyword">const</span> handleResponse = <span class="hljs-function">() =></span> respond(ctx);
    <span class="hljs-comment">//将上下文作为入参传入中间件。</span>
    <span class="hljs-keyword">return</span> fnMiddleware(ctx).then(handleResponse).catch(onerror);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">compose函数的实现</h2>
<p>下面就来介绍我们的核心方法。
就是因为这个compose方法，我们才得以在中间件中以<code>await next()</code>的形式将控制权转交给下一个中间件，并在最后一个中间件将控制权依次向上传递。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span> (<span class="hljs-params">middleware</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(middleware)) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Middleware stack must be an array!'</span>)
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> fn <span class="hljs-keyword">of</span> middleware) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> fn !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Middleware must be composed of functions!'</span>)
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context, next</span>) </span>&#123;
    <span class="hljs-comment">// last called middleware #</span>
    <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>
    <span class="hljs-keyword">return</span> dispatch(<span class="hljs-number">0</span>)
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatch</span> (<span class="hljs-params">i</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (i <= index) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'next() called multiple times'</span>))
      index = i
      <span class="hljs-keyword">let</span> fn = middleware[i]
      <span class="hljs-keyword">if</span> (i === middleware.length) fn = next
      <span class="hljs-keyword">if</span> (!fn) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(fn(context, dispatch.bind(<span class="hljs-literal">null</span>, i + <span class="hljs-number">1</span>)));
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>compose的源码来源<code>koa-compose</code>，代码也比较简单。我们来简单分析一下：</p>
<ol>
<li>做一个入参（中间件）的类型校验</li>
<li>并马上返回一个译名函数。做一个柯里化，分步传入参数。对应源码：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//compose化中间件</span>
<span class="hljs-keyword">const</span> fn = compose(<span class="hljs-built_in">this</span>.middleware); 
...
<span class="hljs-comment">//返回请求的回调函数-即compose之后的中间件函数</span>
<span class="hljs-keyword">return</span> fnMiddleware(ctx).then(handleResponse).catch(onerror);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在佚名函数中马上返回了一个函数调用。做了一个尾递归的优化，防止栈溢出。一句话解释：在A函数内部返回B函数的执行结果，B函数的内存空间就能马上释放</li>
<li>而最关键的就是<code>dispatch</code>函数，主要逻辑：
<ol>
<li>先做了一个边界情况<code> if (!fn) return Promise.resolve()</code>，没有下一个中间件了，就<code>Promise.resolve()</code>，回溯到上一个中间件的<code>await next()</code>之后的逻辑；</li>
<li>然后就是返回第一个中间件的调用结果，这样就是一个尾递归优化。</li>
<li>关键的是<code>fn</code>的第二个参数，是下一个中间件函数，能够让上一个中间件优雅的调用。</li>
</ol>
</li>
</ol>
<p><strong>小结：</strong></p>
<ol>
<li>js控制权从第一个中间件开始，依次往下传递。向下传递的关键在于执行<code>await next()</code>，手动触发执行。</li>
<li>而<code>await next()</code>方法也为后面的控制权向上回溯做了铺垫。每一个<code>await next()</code>都嵌套了下一个中间件的方法，直到最后一个没有<code>await next()</code>的中间件执行完毕</li>
<li>最后一个中间件执行完毕，开始向上回溯，执行上一个中间件的<code>await next()</code>后的方法</li>
</ol>
<h2 data-id="heading-6">总结</h2>
<ol>
<li><code>compose</code>函数利用了尾递归进行了内存栈的优化</li>
<li>将下一个中间件的作为当前执行中间件的入参，来手动控制进入下一个中间件的时机。</li>
<li>利用<code>async/await</code>来处理异步的中间件来向上回溯</li>
</ol></div>  
</div>
            