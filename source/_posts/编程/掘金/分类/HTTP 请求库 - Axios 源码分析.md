
---
title: 'HTTP 请求库 - Axios 源码分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e801a19e5a484b80a295f5c51d4b4c51~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 22:31:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e801a19e5a484b80a295f5c51d4b4c51~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>说到 JS HTTP 请求，就不得不提 Axios，作为前端网络请求库领域中的霸主，被广泛应用于众多的 web 项目中。</p>
<blockquote>
<p>几款热门 HTTP 请求库在 GitHub 上的受欢迎程度</p>
</blockquote>



































<table><thead><tr><th>热门 JS HTTP 请求库</th><th>特性简介</th><th>Star</th><th>Fork</th></tr></thead><tbody><tr><td>Axios</td><td>基于 Promise，支持浏览器和 node</td><td>85.4k</td><td>8.3k</td></tr><tr><td>Request</td><td>不基于 Promise，简化版的 HTTP</td><td>25.2k</td><td>3.1k</td></tr><tr><td>Fetch</td><td>基于 Promise，不支持 node 调用</td><td>24.8k</td><td>3k</td></tr><tr><td>Superagent</td><td></td><td>15.7k</td><td>1.3k</td></tr></tbody></table>
<p>虽然大家都是对 XMLHttpRequest 的封装，但是纵观 Axios 的热度，一骑绝尘啊！由此可见，Axios 真的是一个很优秀的开源项目。然而惭愧的是日常开发中总是拿来就用，一直没有静下心来好好拜读一番 Axios 的源码，会不会有很多人跟我一样呢？这里先列举一下 axios 项目的核心目录结构：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">lib

└─ adapters

   ├─ http.js <span class="hljs-comment">// node 环境下利用 http 模块发起请求</span>

   ├─ xhr.js <span class="hljs-comment">// 浏览器环境下利用 xhr 发起请求</span>

└─ cancel

   ├─ Cancel.js

   ├─ CancelToken.js

   ├─ isCancel.js

└─ core

    ├─ Axios.js <span class="hljs-comment">// 生成 Axios 实例</span>

    ├─ InterceptorManager.js <span class="hljs-comment">// 拦截器</span>

    ├─ dispatchRequest.js  <span class="hljs-comment">// 调用适配器发起请求</span>

    ...

└─ helpers

    ├─ mergeConfig.js <span class="hljs-comment">// 合并配置</span>

    ├─ ...

├─ axios.js  <span class="hljs-comment">// 入口文件</span>

├─ defaults.js  <span class="hljs-comment">// axios 默认配置项</span>

├─ utils.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">简介</h2>
<p>Axios 是一个基于 Promise 网络请求库，作用于 node.js 和浏览器中。在服务端它使用原生 node.js<code>http</code>模块, 而在客户端 (浏览端) 则使用 XMLHttpRequests。特性：</p>
<ul>
<li>从浏览器创建<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest" ref="nofollow noopener noreferrer">XMLHttpRequests</a></li>
</ul>
<ul>
<li>
<p>从 node.js 创建<a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.org%2Fapi%2Fhttp.html" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.org/api/http.html" ref="nofollow noopener noreferrer">http</a>请求</p>
</li>
<li>
<p>支持<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise" ref="nofollow noopener noreferrer">Promise</a>API</p>
</li>
<li>
<p>拦截请求和响应</p>
</li>
<li>
<p>转换请求和响应数据</p>
</li>
<li>
<p>取消请求</p>
</li>
<li>
<p>自动转换 JSON 数据</p>
</li>
<li>
<p>客户端支持防御<a href="https://link.juejin.cn/?target=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCross-site_request_forgery" target="_blank" rel="nofollow noopener noreferrer" title="http://en.wikipedia.org/wiki/Cross-site_request_forgery" ref="nofollow noopener noreferrer">XSRF</a></p>
</li>
</ul>
<h2 data-id="heading-2">Axios 内部运作流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e801a19e5a484b80a295f5c51d4b4c51~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
接下来我们结合 axios 的运作流程一起来剖析以下几个模块：</p>
<ul>
<li>Axios 构造函数</li>
<li>请求 / 响应拦截器</li>
<li>dispatchRequest 派发请求</li>
<li>转换请求 / 响应数据</li>
<li>适配器处理 HTTP 请求</li>
</ul>
<h2 data-id="heading-3">Axios 如何支持不同的使用方式?</h2>
<h3 data-id="heading-4">使用 axios 发起请求</h3>
<p>我们先来回忆一下平时是如何使用 axios 的：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// 方式 1  axios(config)</span>

axios(&#123;

    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,

    <span class="hljs-attr">url</span>: <span class="hljs-string">'xxx'</span>,

    <span class="hljs-attr">data</span>: &#123;&#125;

&#125;);



<span class="hljs-comment">// 方式 2  axios(url[, config]),默认 get 请求</span>

axios(<span class="hljs-string">'http://xxx'</span>);



<span class="hljs-comment">// 方式 3 使用别名进行请求</span>

axios.request(config)

axios.get(url[, config])

axios.post(url[, data[, config]])

axios.put(url[, data[, config]])

...



<span class="hljs-comment">// 方式 4 创建 axios 实例，自定义配置</span>

<span class="hljs-keyword">const</span> instance = axios.create(&#123;

  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'https://some-domain.com/api/'</span>,

  <span class="hljs-attr">timeout</span>: <span class="hljs-number">1000</span>,

  <span class="hljs-attr">headers</span>: &#123;<span class="hljs-string">'X-Custom-Header'</span>: <span class="hljs-string">'foobar'</span>&#125;

&#125;);



axios#request(config)

axios#get(url[, config])

axios#post(url[, data[, config]])

axios#put(url[, data[, config]])

...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">源码分析</h3>
<p>首先来看 axios 的入口文件， lib 目录下的<code>axios.js</code>:</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// /lib/axios.js</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params">defaultConfig</span>) </span>&#123;

  <span class="hljs-comment">// 创建 axios 实例</span>

  <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Axios(defaultConfig);

  <span class="hljs-comment">// 把 instance 指向 Axios.prototype.request 方法</span>

  <span class="hljs-keyword">var</span> instance = bind(Axios.prototype.request, context);

  <span class="hljs-comment">// 把 Axios.prototype 上的方法扩展到 instance 上，指定上下文是 context</span>

  utils.extend(instance, Axios.prototype, context);

  <span class="hljs-comment">// 把 context 上的方法扩展到 instance 上</span>

  utils.extend(instance, context);

  <span class="hljs-comment">// 导出 instance 对象</span>

  <span class="hljs-keyword">return</span> instance;

&#125;

<span class="hljs-keyword">var</span> axios = createInstance(defaults);

<span class="hljs-comment">// 添加 create 方法，返回 createInstance 函数，参数为自定义配置 + 默认配置</span>

axios.create = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;

  <span class="hljs-keyword">return</span> createInstance(mergeConfig(axios.defaults, instanceConfig));

&#125;;



...



<span class="hljs-built_in">module</span>.exports = axios;

<span class="hljs-comment">// Allow use of default import syntax in TypeScript</span>

<span class="hljs-built_in">module</span>.exports.default = axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，当我们调用<code>axios()</code>时，实际上是执行了<code>createInstance</code>返回的一个指向<code>Axios.prototype.request</code>的函数；通过添加<code>create</code>方法支持用户自定义配置创建，并且最终也是执行了<code>Axios.prototype.request</code>方法；接下来我们看看<code>Axios.prototype.request</code>的源码是怎么写的：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// /lib/core/Axios.js</span>

<span class="hljs-comment">// 创建一个 Axios 实例</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Axios</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;

  ...

&#125;

Axios.prototype.request = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">config</span>) </span>&#123;

  <span class="hljs-comment">// 判断 config 类型并赋值</span>

  <span class="hljs-comment">// 方式二：axios('https://xxxx') ，判断参数字符串，则赋值给 config.url</span>

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'string'</span>) &#123;

    config = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] || &#123;&#125;;

    config.url = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];

  &#125; <span class="hljs-keyword">else</span> &#123;

  <span class="hljs-comment">// 方式一：axios(&#123;&#125;) ,参数为对象，则直接赋值给 config</span>

    config = config || &#123;&#125;;

  &#125;

  ...

&#125;

...

<span class="hljs-comment">// 方式三 & 方式四</span>

<span class="hljs-comment">// 遍历为请求设置别名</span>

utils.forEach([<span class="hljs-string">'delete'</span>, <span class="hljs-string">'get'</span>, <span class="hljs-string">'head'</span>, <span class="hljs-string">'options'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachMethodNoData</span>(<span class="hljs-params">method</span>) </span>&#123;

  <span class="hljs-comment">/*eslint func-names:0*/</span>

  Axios.prototype[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url, config</span>) </span>&#123;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(mergeConfig(config || &#123;&#125;, &#123;

      <span class="hljs-attr">method</span>: method,

      <span class="hljs-attr">url</span>: url,

      <span class="hljs-attr">data</span>: (config || &#123;&#125;).data

    &#125;));

  &#125;;

&#125;);

<span class="hljs-comment">// 遍历为请求设置别名</span>

utils.forEach([<span class="hljs-string">'post'</span>, <span class="hljs-string">'put'</span>, <span class="hljs-string">'patch'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEachMethodWithData</span>(<span class="hljs-params">method</span>) </span>&#123;

  <span class="hljs-comment">/*eslint func-names:0*/</span>

  Axios.prototype[method] = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url, data, config</span>) </span>&#123;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.request(mergeConfig(config || &#123;&#125;, &#123;

      <span class="hljs-attr">method</span>: method,

      <span class="hljs-attr">url</span>: url,

      <span class="hljs-attr">data</span>: data

    &#125;));

  &#125;;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，axios 支持了 4 中不同的使用方式，无论哪种使用方式，最后都是执行 Axios 实例上的核心方法：<code>request</code>。</p>
<h2 data-id="heading-6">请求 / 响应拦截器是如何生效的？</h2>
<h3 data-id="heading-7">设置拦截器</h3>
<p>对于大多数 spa 的项目来说，通常会使用 token 进行用户的身份认证，这就要求每个请求都携带认证信息；接收到服务器信息之后，如果发现用户未登录，需要统一跳转登录页；遇到这种场景，就需要用到 axios 提供的拦截器，以下是拦截器的设置：</p>
<pre><code class="copyable"> // 添加请求拦截器

axios.interceptors.request.use(function (config) &#123;

  config.headers.token = 'xxx';

  return config;

&#125;);



 // 添加响应拦截器

axios.interceptors.response.use(function (response) &#123;

    if(response.code === 401) &#123;

        login()

    &#125;

    return response;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">源码分析</h3>
<p>通过拦截器的使用，可以知道实例 Axios 上添加了<code>interceptors</code>方法，接下来我们看看源码的实现：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// /lib/core/Axios.js</span>

<span class="hljs-comment">// 每个 Axios 实例上都有 interceptors 属性，该属性上有 request、response 属性，</span>

<span class="hljs-comment">// 分别都是一个 InterceptorManager 实例，而 InterceptorManager 构造函数就是</span>

<span class="hljs-comment">// 用来管理拦截器</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Axios</span>(<span class="hljs-params">instanceConfig</span>) </span>&#123;

  <span class="hljs-built_in">this</span>.defaults = instanceConfig;

  <span class="hljs-built_in">this</span>.interceptors = &#123;

    <span class="hljs-attr">request</span>: <span class="hljs-keyword">new</span> InterceptorManager(),

    <span class="hljs-attr">response</span>: <span class="hljs-keyword">new</span> InterceptorManager()

  &#125;;

&#125;



<span class="hljs-comment">// /lib/core/InterceptorManager.js</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">InterceptorManager</span>(<span class="hljs-params"></span>) </span>&#123;

  <span class="hljs-built_in">this</span>.handlers = []; <span class="hljs-comment">// 拦截器</span>

&#125;

<span class="hljs-comment">// 往拦截器里 push 拦截方法</span>

InterceptorManager.prototype.use = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">use</span>(<span class="hljs-params">fulfilled, rejected, options</span>) </span>&#123;

  <span class="hljs-built_in">this</span>.handlers.push(&#123;

    <span class="hljs-attr">fulfilled</span>: fulfilled,

    <span class="hljs-attr">rejected</span>: rejected,

    ...

  &#125;);

  <span class="hljs-comment">// 返回当前索引，用于注销指定拦截器</span>

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handlers.length - <span class="hljs-number">1</span>;

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Axios 与<code>InterceptorManager</code>的关系如图示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a119afef07d64a7ea1d57ee1d898c3b6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
现在我们已经有了拦截器，那么 axios 是如何保证发起请求的顺序执行呢？</p>
<ul>
<li>请求拦截器 => http 请求 => 响应拦截器</li>
</ul>
<p>上源码：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// /lib/core/Axios.js</span>

<span class="hljs-comment">// request 方法中</span>

<span class="hljs-comment">// 省略部分代码</span>

<span class="hljs-comment">// 生成请求拦截队列</span>

<span class="hljs-keyword">var</span> requestInterceptorChain = [];

<span class="hljs-built_in">this</span>.interceptors.request.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unshiftRequestInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;

    requestInterceptorChain.unshift(interceptor.fulfilled, interceptor.rejected);

&#125;);

<span class="hljs-comment">// 生成响应拦截队列</span>

<span class="hljs-keyword">var</span> responseInterceptorChain = [];

<span class="hljs-built_in">this</span>.interceptors.response.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushResponseInterceptors</span>(<span class="hljs-params">interceptor</span>) </span>&#123;

    responseInterceptorChain.push(interceptor.fulfilled, interceptor.rejected);

&#125;);



<span class="hljs-comment">// 编排整个请求的任务队列</span>

<span class="hljs-keyword">var</span> chain = [dispatchRequest, <span class="hljs-literal">undefined</span>];

<span class="hljs-built_in">Array</span>.prototype.unshift.apply(chain, requestInterceptorChain);

chain.concat(responseInterceptorChain);



promise = <span class="hljs-built_in">Promise</span>.resolve(config);

<span class="hljs-comment">// 循环 chain ，不断从 chain 中取出设置的任务，通过 Promise 调用链执行</span>

<span class="hljs-keyword">while</span> (chain.length) &#123;

  promise = promise.then(chain.shift(), chain.shift());

&#125;



<span class="hljs-keyword">return</span> promise;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用图示表示一下拦截器过程更清晰：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/940f196b786f419db298a32391af690b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
生成任务队列后，再通过<code>promise.then(chain.shift(), chain.shift())</code>调用 Promise 链去处理设置的任务。这里需要注意一点，请求拦截队列在生成时，是通过<code>Array.unshift(fulfilled, rejected)</code>设置的，也就是说在执行请求拦截时，先设置的拦截方法后执行，后设置的拦截方法先执行。</p>
<h2 data-id="heading-9">派发请求 dispatchRequest</h2>
<h3 data-id="heading-10">源码分析</h3>
<p>处理完请求拦截之后，总算开始步入整个请求链路的正轨，也就是上图中任务队列的中间步骤：<code>dispatchRequest</code>派发请求。</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// /lib/core/dispatchRequest.js</span>

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchRequest</span>(<span class="hljs-params">config</span>) </span>&#123;

  <span class="hljs-comment">// 转换请求数据</span>

  config.data = transformData.call(

    config,

    config.data,

    config.headers,

    config.transformRequest

  );

  ...

  <span class="hljs-comment">// 适配器 可以自定义适配器，没有自定义，执行axios默认适配器</span>

  <span class="hljs-keyword">var</span> adapter = config.adapter || defaults.adapter;

  <span class="hljs-comment">// 通过适配器处理 config 配置，返回服务端响应数据 response</span>

  <span class="hljs-keyword">return</span> adapter(config).then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onAdapterResolution</span>(<span class="hljs-params">response</span>) </span>&#123;

    ...

    <span class="hljs-comment">// 转换响应数据</span>

    response.data = transformData.call(

      config,

      response.data,

      response.headers,

      config.transformResponse

    );

    ...

    <span class="hljs-keyword">return</span> response;

  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onAdapterRejection</span>(<span class="hljs-params">reason</span>) </span>&#123;

    ...

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(reason);

  &#125;）

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dispatchRequest</code>中主要做了两件事，先通过<code>transformData</code>对请求数据进行处理，然后定义适配器<code>adapter</code>并执行，通过 .then 方法 对<code>adapter</code>（适配器） resolve 出的响应数据进行处理（<code>transformData</code>）并返回 response，失败返回一个状态为<code>rejected`</code>的 Promise 对象。到此也就明白，当用户调用 axios()时，为什么可以链式调用 Promise 的 .then() 和 .catch() 来处理业务逻辑了。接下来我们从<code>transformData</code>入手，看看 axios 是如何转换请求和响应数据的。</p>
<h2 data-id="heading-11">转换请求 / 响应数据</h2>
<h3 data-id="heading-12">源码分析</h3>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// /lib/core/dispatchRequest.js</span>

config.data = transformData.call(

    config,

    config.data,

    config.headers,

    config.transformRequest

);



<span class="hljs-comment">// /lib/core/transformData.js</span>

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformData</span>(<span class="hljs-params">data, headers, fns</span>) </span>&#123;

    utils.forEach(fns, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transform</span>(<span class="hljs-params">fn</span>) </span>&#123;

    data = fn(data, headers);

    &#125;);



    <span class="hljs-keyword">return</span> data;

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述代码可以发现<code>transformData</code>方法主要是遍历<code>config.transformRequest</code>数组中的方法，<code>config.data</code>和<code>config.headers</code>作为参数。来看一下<code>transformRequest</code>和<code>tranformResponse</code>的定义:</p>
<pre><code class="copyable">// /lib/default.js

var default = &#123;

  ...

  // 转换请求数据

  transformRequest: [function transformRequest(data, headers) &#123;

    // 判断 data 类型

    if (utils.isFormData(data) ||

      utils.isArrayBuffer(data) ||

      utils.isBuffer(data) ||

      utils.isStream(data) ||

      utils.isFile(data) ||

      utils.isBlob(data)

    ) &#123;

      return data;

    &#125;

    if (utils.isArrayBufferView(data)) &#123;

      return data.buffer;

    &#125;

    if (utils.isURLSearchParams(data)) &#123;

      setContentTypeIfUnset(headers, 'application/x-www-form-urlencoded;charset=utf-8');

      return data.toString();

    &#125;

    // 如果 data 是对象，或 Content-Type 设置为 application/json

    if (utils.isObject(data) || (headers && headers['Content-Type'] === 'application/json')) &#123;

      // 设置 Content-Type 为 application/json

      setContentTypeIfUnset(headers, 'application/json');

      // 将 data 转换为 json 字符串返回

      return JSON.stringify(data);

    &#125;

    return data;

  &#125;],

  // 转换响应数据

  transformResponse: [function transformResponse(data) &#123;

    ...

    if (strictJSONParsing || (forcedJSONParsing && utils.isString(data) && data.length)) &#123;

      try &#123;

        // 将 data 转换为 json 对象并返回

        return JSON.parse(data);

      &#125; catch (e) &#123;

        ...

      &#125;

    &#125;

    return data;

  &#125;],

  ...

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，请求数据和响应数据的转换过程已经结束了，顺便提一下，官方文档介绍的特性之一：**自动转换 JSON 数据，**应该就是转换过程中的<code>JSON.stringify(data)</code>与<code>JSON.parse(data)</code>了;</p>
<h3 data-id="heading-13">重写 / 新增转换方法</h3>
<p>发现<code>transformRequest</code>方法是<code>default</code>对象上的一个属性，那么我们是不是可以通过自定义配置来改写转换的过程呢？</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;

<span class="hljs-comment">// 重写转换请求数据的过程</span>

axios.default.transformRequest = [<span class="hljs-function">(<span class="hljs-params">data, headers</span>) =></span> &#123;

    ...

    <span class="hljs-keyword">return</span> data

&#125;];

<span class="hljs-comment">// 增加对请求数据的处理</span>

axios.default.transformRequest.push(

<span class="hljs-function">(<span class="hljs-params">data, headers</span>) =></span> &#123;

    ...

    <span class="hljs-keyword">return</span> data

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">适配器（adapter）处理请求</h2>
<p><code>dispatchRequest</code>方法做的第二件事：定义<code>adapter</code>，并执行。接下来，我们来揭开<code>adapter</code>的面纱，看看它具体是怎么处理 HTTP 请求的~</p>
<h3 data-id="heading-15">源码分析</h3>
<p>下面的代码可以看出，适配器是可以自定义的，如果没有自定义，则执行 axios 提供的默认适配器。</p>
<pre><code class="copyable">// /lib/core/dispatchRequest.js (51行)

var adapter = config.adapter || defaults.adapter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来分析默认适配器，在<code>default.js</code>中：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDefaultAdapter</span>(<span class="hljs-params"></span>) </span>&#123;

    <span class="hljs-keyword">var</span> adapter;

    <span class="hljs-comment">// 判断当前环境</span>

    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> XMLHttpRequest !== <span class="hljs-string">'undefined'</span>) &#123;

    <span class="hljs-comment">// 浏览器环境，使用 xhr 请求</span>

    adapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./adapters/xhr'</span>);

    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> process !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Object</span>.prototype.toString.call(process) === <span class="hljs-string">'[object process]'</span>) &#123;

    <span class="hljs-comment">// node 环境，使用 http 模块</span>

    adapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./adapters/http'</span>);

    &#125;

    <span class="hljs-keyword">return</span> adapter;

&#125;

<span class="hljs-keyword">var</span> defaults = &#123;

    ...

    <span class="hljs-comment">// 定义 adapter 属性</span>

    <span class="hljs-attr">adapter</span>: getDefaultAdapter(),

    ...

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，axios 之所以支持浏览器环境和 node 环境，就是<code>getDefaultAdapter</code>方法进行了环境判断，分别使用<strong>xhr 处理浏览器请求</strong>和**http 模块处理 node 请求。**官方称之为<code>isomorphic</code>（同构）能力。这里定义了<code>defaults</code>对象，该对象定义了 axios 的一系列默认配置，还记得它是在哪被注入到 axios 中的吗？当然是在入口文件<code>axios.js</code>里了。</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// /lib/axios.js</span>

...

<span class="hljs-keyword">var</span> defaults = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./defaults'</span>);

...

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createInstance</span>(<span class="hljs-params">defaultConfig</span>) </span>&#123;

  ...

  <span class="hljs-comment">// 创建 axios 实例</span>

  <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Axios(defaultConfig);

  ...

&#125;

<span class="hljs-keyword">var</span> axios = createInstance(defaults);

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哎呦，串起来了有没有~好的，重新说回到 xhr 请求，本文只分析浏览器环境中 axios 的运行机制，因此接下来，让我们打开<code>./adapters/xhr</code>文件来看一下：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhrAdapter</span>(<span class="hljs-params">config</span>) </span>&#123;

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchXhrRequest</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;

    ...

    <span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest();

    <span class="hljs-comment">// 设置完整请求路径</span>

    <span class="hljs-keyword">var</span> fullPath = buildFullPath(config.baseURL, config.url);

    request.open(config.method.toUpperCase(), buildURL(fullPath, config.params, config.paramsSerializer), <span class="hljs-literal">true</span>) ;

    <span class="hljs-comment">// 请求超时</span>

    request.timeout = config.timeout;

    request.ontimeout = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleTimeout</span>(<span class="hljs-params"></span>) </span>&#123;...&#125;

    <span class="hljs-comment">// 请求中断</span>

    request.onabort = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleAbort</span>(<span class="hljs-params"></span>) </span>&#123;...&#125;

    ...

    request.send(requestData);

  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 config 中的请求配置进行赋值处理，正式发起<code>XMLHttpRequest</code>****请求。</p>
<h3 data-id="heading-16">自定义 adapter</h3>
<p>通过上面对 adapter 的分析，可以发现如果自定义 adapter 的话，是可以接管 axios 的请求和响应数据的，因此可以自定义 adapter 实现 mock；</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">const</span> mockUrl = &#123;

    <span class="hljs-string">'/mock'</span>: &#123;<span class="hljs-attr">data</span>: xxx&#125;

&#125;;

<span class="hljs-keyword">const</span> instance = Axios.create(&#123;

    <span class="hljs-attr">adapter</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;

        <span class="hljs-keyword">if</span> (!mockUrl[config.url]) &#123;

            <span class="hljs-comment">// 调用默认的适配器处理需要删除自定义适配器，否则会死循环</span>

            <span class="hljs-keyword">delete</span> config.adapter

            <span class="hljs-keyword">return</span> Axios(config)

        &#125;

        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;

            resolve(&#123;

                <span class="hljs-attr">data</span>: mockUrl[config.url],

                <span class="hljs-attr">status</span>: <span class="hljs-number">200</span>,

            &#125;)

        &#125;)

    &#125;

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">结语</h2>
<p>篇幅限制，本文只分析了 axios 中的部分源码，诸如 客户端支持防御 XSRF 攻击、取消请求 等模块没有提及，感兴趣的同学可以打开 GitHub 去读一读，相信一定会获益匪浅。</p>
<p>参考资料：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Faxios-http.com%2Fzh%2Fdocs%2Fintro" target="_blank" rel="nofollow noopener noreferrer" title="https://axios-http.com/zh/docs/intro" ref="nofollow noopener noreferrer">起步 | Axios Docs</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faxios%2Faxios%2Fblob%2Fmaster%2Flib%2Faxios.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/axios/axios/blob/master/lib/axios.js" ref="nofollow noopener noreferrer">github.com/axios/axios…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/966de52590c04a91a3b75934aae58fef~tplv-k3u1fbpfcp-watermark.image" alt="默认标题_公众号封面首图_2021-08-30+14_19_33.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            