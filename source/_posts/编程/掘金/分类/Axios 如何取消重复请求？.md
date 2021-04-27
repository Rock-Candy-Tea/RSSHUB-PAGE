
---
title: 'Axios 如何取消重复请求？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/008895016b2442f3945f542d30c3c3ef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 15:24:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/008895016b2442f3945f542d30c3c3ef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 Web 项目开发过程中，我们经常会遇到重复请求的场景，如果系统不对重复的请求进行处理，则可能会导致系统出现各种问题。比如重复的 <code>post</code> 请求可能会导致服务端产生两笔记录。那么重复请求是如何产生的呢？这里我们举 2 个常见的场景：</p>
<ul>
<li>假设页面中有一个按钮，用户点击按钮后会发起一个 AJAX 请求。如果未对该按钮进行控制，当用户快速点击按钮时，则会发出重复请求。</li>
<li>假设在考试结果查询页面中，用户可以根据 <strong>“已通过”、“未通过” 和 “全部”</strong> 3 种查询条件来查询考试结果。如果请求的响应比较慢，当用户在不同的查询条件之前快速切换时，就会产生重复请求。</li>
</ul>
<p>既然已经知道重复请求是如何产生的，也知道了它会带来一些问题。接下来，阿宝哥将以 <a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Axios</a> 为例，带大家来一起解决重复请求的问题。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。</p>
</blockquote>
<h3 data-id="heading-0">一、如何取消请求</h3>
<p><a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Axios</a> 是一个基于 Promise 的 HTTP 客户端，同时支持浏览器和 Node.js 环境。它是一个优秀的 HTTP 客户端，被广泛地应用在大量的 Web 项目中。对于浏览器环境来说，Axios 底层是利用 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer">XMLHttpRequest</a> 对象来发起 HTTP 请求。如果要取消请求的话，我们可以通过调用 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer">XMLHttpRequest</a> 对象上的 <code>abort</code> 方法来取消请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.open(<span class="hljs-string">"GET"</span>, <span class="hljs-string">"https://developer.mozilla.org/"</span>, <span class="hljs-literal">true</span>);
xhr.send();
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> xhr.abort(), <span class="hljs-number">300</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而对于 Axios 来说，我们可以通过 Axios 内部提供的 <code>CancelToken</code> 来取消请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">const</span> source = CancelToken.source();

axios.post(<span class="hljs-string">'/user/12345'</span>, &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'semlinker'</span>
&#125;, &#123;
  <span class="hljs-attr">cancelToken</span>: source.token
&#125;)

source.cancel(<span class="hljs-string">'Operation canceled by the user.'</span>); <span class="hljs-comment">// 取消请求，参数是可选的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，你也可以通过调用 <code>CancelToken</code> 的构造函数来创建 <code>CancelToken</code>，具体如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
<span class="hljs-keyword">let</span> cancel;

axios.get(<span class="hljs-string">'/user/12345'</span>, &#123;
  <span class="hljs-attr">cancelToken</span>: <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">c</span>) </span>&#123;
    cancel = c;
  &#125;)
&#125;);

cancel(); <span class="hljs-comment">// 取消请求</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经知道在 Axios 中如何使用 <code>CancelToken</code> 来取消请求了，那么 <code>CancelToken</code> 内部是如何工作的呢？这里我们先记住这个问题，后面阿宝哥将为你们揭开 <code>CancelToken</code> 背后的秘密。接下来，我们来分析一下如何判断重复请求。</p>
<h3 data-id="heading-1">二、如何判断重复请求</h3>
<p>当请求方式、请求 URL 地址和请求参数都一样时，我们就可以认为请求是一样的。因此在每次发起请求时，我们就可以根据当前请求的请求方式、请求 URL 地址和请求参数来生成一个唯一的 key，同时为每个请求创建一个专属的 CancelToken，然后把 key 和 cancel 函数以键值对的形式保存到 Map 对象中，使用 Map 的好处是可以快速的判断是否有重复的请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>

<span class="hljs-keyword">const</span> pendingRequest = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-comment">// GET -> params；POST -> data</span>
<span class="hljs-keyword">const</span> requestKey = [method, url, qs.stringify(params), qs.stringify(data)].join(<span class="hljs-string">'&'</span>); 
<span class="hljs-keyword">const</span> cancelToken = <span class="hljs-keyword">new</span> CancelToken(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">executor</span>(<span class="hljs-params">cancel</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(!pendingRequest.has(requestKey))&#123;
    pendingRequest.set(requestKey, cancel);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当出现重复请求的时候，我们就可以使用 cancel 函数来取消前面已经发出的请求，在取消请求之后，我们还需要把取消的请求从 <code>pendingRequest</code> 中移除。现在我们已经知道如何取消请求和如何判断重复请求，下面我们来介绍如何取消重复请求。</p>
<h3 data-id="heading-2">三、如何取消重复请求</h3>
<p>因为我们需要对所有的请求都进行处理，所以我们可以考虑使用 Axios 的拦截器机制来实现取消重复请求的功能。Axios 为开发者提供了请求拦截器和响应拦截器，它们的作用如下：</p>
<ul>
<li>请求拦截器：该类拦截器的作用是在请求发送前统一执行某些操作，比如在请求头中添加 token 字段。</li>
<li>响应拦截器：该类拦截器的作用是在接收到服务器响应后统一执行某些操作，比如发现响应状态码为 401 时，自动跳转到登录页。</li>
</ul>
<h4 data-id="heading-3">3.1 定义辅助函数</h4>
<p>在配置请求拦截器和响应拦截器前，阿宝哥先来定义 3 个辅助函数：</p>
<ul>
<li><code>generateReqKey</code>：用于根据当前请求的信息，生成请求 Key；</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateReqKey</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; method, url, params, data &#125; = config;
  <span class="hljs-keyword">return</span> [method, url, Qs.stringify(params), Qs.stringify(data)].join(<span class="hljs-string">"&"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>addPendingRequest</code>：用于把当前请求信息添加到pendingRequest对象中；</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> pendingRequest = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addPendingRequest</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">const</span> requestKey = generateReqKey(config);
  config.cancelToken = config.cancelToken || <span class="hljs-keyword">new</span> axios.CancelToken(<span class="hljs-function">(<span class="hljs-params">cancel</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!pendingRequest.has(requestKey)) &#123;
       pendingRequest.set(requestKey, cancel);
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>removePendingRequest</code>：检查是否存在重复请求，若存在则取消已发的请求。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removePendingRequest</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">const</span> requestKey = generateReqKey(config);
  <span class="hljs-keyword">if</span> (pendingRequest.has(requestKey)) &#123;
     <span class="hljs-keyword">const</span> cancelToken = pendingRequest.get(requestKey);
     cancelToken(requestKey);
     pendingRequest.delete(requestKey);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建好 <code>generateReqKey</code>、<code>addPendingRequest</code> 和 <code>removePendingRequest</code> 函数之后，我们就可以设置请求拦截器和响应拦截器了。</p>
<h4 data-id="heading-4">3.2 设置请求拦截器</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.interceptors.request.use(
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
    removePendingRequest(config); <span class="hljs-comment">// 检查是否存在重复请求，若存在则取消已发的请求</span>
    addPendingRequest(config); <span class="hljs-comment">// 把当前请求信息添加到pendingRequest对象中</span>
    <span class="hljs-keyword">return</span> config;
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3.3 设置响应拦截器</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.interceptors.response.use(
  <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
     removePendingRequest(response.config); <span class="hljs-comment">// 从pendingRequest对象中移除请求</span>
     <span class="hljs-keyword">return</span> response;
   &#125;,
   <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
      removePendingRequest(error.config || &#123;&#125;); <span class="hljs-comment">// 从pendingRequest对象中移除请求</span>
      <span class="hljs-keyword">if</span> (axios.isCancel(error)) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"已取消的重复请求："</span> + error.message);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 添加异常处理</span>
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
   &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于完整的示例代码内容比较多，阿宝哥就不放具体的代码了。感兴趣的小伙伴，可以访问以下地址浏览示例代码。</p>
<blockquote>
<p>完整的示例代码：<a href="https://gist.github.com/semlinker/e426780664f0186db434882f1e27ac3a" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/semlinker/e…</a></p>
</blockquote>
<p>这里我们来看一下 Axios 取消重复请求示例的运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/008895016b2442f3945f542d30c3c3ef~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可知，当出现重复请求时，之前已发送且未完成的请求会被取消掉。下面我们用一张流程图来总结一下取消重复请求的处理流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74708ddbcba1457ba22c51936c7cacb2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，我们来回答前面留下的问题，即 <code>CancelToken</code> 内部是如何工作的？</p>
<h3 data-id="heading-6">四、CancelToken 的工作原理</h3>
<p>在前面的示例中，我们是通过调用 <code>CancelToken</code> 构造函数来创建 <code>CancelToken</code> 对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> axios.CancelToken(<span class="hljs-function">(<span class="hljs-params">cancel</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!pendingRequest.has(requestKey)) &#123;
    pendingRequest.set(requestKey, cancel);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以接下来，我们来分析 <code>CancelToken</code> 构造函数，该函数被定义在 <code>lib/cancel/CancelToken.js</code> 文件中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// lib/cancel/CancelToken.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CancelToken</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> executor !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'executor must be a function.'</span>);
  &#125;

  <span class="hljs-keyword">var</span> resolvePromise;
  <span class="hljs-built_in">this</span>.promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseExecutor</span>(<span class="hljs-params">resolve</span>) </span>&#123;
    resolvePromise = resolve;
  &#125;);

  <span class="hljs-keyword">var</span> token = <span class="hljs-built_in">this</span>;
  executor(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancel</span>(<span class="hljs-params">message</span>) </span>&#123; <span class="hljs-comment">// 设置cancel对象</span>
    <span class="hljs-keyword">if</span> (token.reason) &#123;
      <span class="hljs-keyword">return</span>; <span class="hljs-comment">// Cancellation has already been requested</span>
    &#125;
    token.reason = <span class="hljs-keyword">new</span> Cancel(message);
    resolvePromise(token.reason);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，<code>cancel</code> 对象是一个函数，当我们调用该函数后，会创建 <code>Cancel</code> 对象并调用 <code>resolvePromise</code> 方法。该方法执行后，<code>CancelToken</code> 对象上 <code>promise</code> 属性所指向的 <code>promise</code> 对象的状态将变为 <code>resolved</code>。那么这样做的目的是什么呢？这里我们从 <code>lib/adapters/xhr.js</code> 文件中找到了答案：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// lib/adapters/xhr.js </span>
<span class="hljs-keyword">if</span> (config.cancelToken) &#123;
  config.cancelToken.promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onCanceled</span>(<span class="hljs-params">cancel</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!request) &#123; <span class="hljs-keyword">return</span>; &#125;
    request.abort(); <span class="hljs-comment">// 取消请求</span>
    reject(cancel);
    request = <span class="hljs-literal">null</span>;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完上述的内容，可能有的小伙伴还不是很能理解 <code>CancelToken</code> 的工作原理，所以阿宝哥又画了一张图来帮助大家理解 <code>CancelToken</code> 的工作原理：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55c3847567ff4dcf974c4e0462220aff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">五、总结</h3>
<p>本文介绍了在 Axios 中如何取消重复请求及 CancelToken 的工作原理，<strong>需要注意的是已取消的请求可能已经达到服务端，针对这种情形，服务端的对应接口需要进行幂等控制</strong>。在后续的文章中，阿宝哥将会介绍在 Axios 中如何设置数据缓存，感兴趣的小伙伴不要错过哟。 如果你想了解 Axios 中 HTTP 拦截器及 HTTP 适配器的设计与实现，可以阅读 <a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a> 这篇文章。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-8">六、参考资源</h3>
<ul>
<li><a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Github - Axios</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer">MDN - XMLHttpRequest</a></li>
<li><a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a></li>
</ul></div>  
</div>
            