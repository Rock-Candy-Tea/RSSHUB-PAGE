
---
title: 'Axios 如何缓存请求数据？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fa55bc3d4f04ca5b8216aa1b08b8286~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 15:17:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fa55bc3d4f04ca5b8216aa1b08b8286~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文是 Axios 四部曲的最后一篇文章，这篇文章将介绍在 Axios 中如何通过 <strong>增强默认适配器</strong> 来缓存请求数据。那么为什么要缓存请求数据呢？这是因为在缓存未失效时，我们可以直接使用已缓存的数据，而不需发起请求从服务端获取数据，这样不仅可以减少 HTTP 请求而且还能减少等待时间从而提高用户体验。</p>
<p>因为本文将使用 <a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Axios</a> 提供的默认适配器来实现缓存请求数据的功能，所以如果你对 Axios 适配器还不熟悉的话，建议先阅读 <a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a> 这篇文章。为了让大家能够更好地理解后续的内容，我们先来看一下整体的流程图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fa55bc3d4f04ca5b8216aa1b08b8286~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中蓝色部分的工作流程，就是本文的重点。接下来，阿宝哥将从如何设计缓存开始，带大家一起来开发缓存请求数据的功能。</p>
<h3 data-id="heading-0">一、如何设计缓存</h3>
<p>在计算中，缓存是一个高速数据存储层，其中存储了数据子集，且通常是 <strong>短暂性</strong> 存储，这样日后再次请求该数据时，速度要比访问数据的主存储位置快。通过缓存，你可以高效地重用之前检索或计算的数据。了解完缓存的作用之后，我们来设计缓存的 API：</p>
<ul>
<li>get(key)：从缓存中获取指定 <code>key</code> 对应的值；</li>
<li>delete(key)：从缓存中删除指定 <code>key</code> 对应的值；</li>
<li>clear()：清空已缓存的数据；</li>
<li>set(key, value, maxAge)：保存键值对，同时支持设置缓存的最大时间，即 <code>maxAge</code> 单位为毫秒。</li>
</ul>
<p>基于上述的缓存 API，我们可以实现一个简单的缓存功能，具体代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MemoryCache = &#123;
  <span class="hljs-attr">data</span>: &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">key, value, maxAge</span>)</span> &#123; <span class="hljs-comment">// 保存数据</span>
    <span class="hljs-built_in">this</span>.data[key] = &#123;
      <span class="hljs-attr">maxAge</span>: maxAge || <span class="hljs-number">0</span>,
      value,
      <span class="hljs-attr">now</span>: <span class="hljs-built_in">Date</span>.now(),
     &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">key</span>)</span> &#123; <span class="hljs-comment">// 从缓存中获取指定 key 对应的值。</span>
    <span class="hljs-keyword">const</span> cachedItem = <span class="hljs-built_in">this</span>.data[key];
    <span class="hljs-keyword">if</span> (!cachedItem) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">const</span> isExpired = <span class="hljs-built_in">Date</span>.now() - cachedItem.now > cachedItem.maxAge;
    isExpired && <span class="hljs-built_in">this</span>.delete(key);
    <span class="hljs-keyword">return</span> isExpired ? <span class="hljs-literal">null</span> : cachedItem.value;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">key</span>)</span> &#123; <span class="hljs-comment">// 从缓存中删除指定 key 对应的值。</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.data[key];
  &#125;,
  <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 清空已缓存的数据。</span>
    <span class="hljs-built_in">this</span>.data = &#123;&#125;;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实除了自定义缓存对象之外，你也可以使用成熟的第三方库，比如 <a href="https://www.npmjs.com/package/lru-cache" target="_blank" rel="nofollow noopener noreferrer">lru-cache</a>。</p>
<blockquote>
<p>LRU 缓存淘汰算法就是一种常用策略。LRU 的全称是 Least Recently Used，也就是说我们认为最近使用过的数据应该是是「有用的」，很久都没用过的数据应该是无用的，内存满了就优先删那些很久没用过的数据。</p>
</blockquote>
<h3 data-id="heading-1">二、如何增强默认适配器</h3>
<p>Axios 引入了适配器，使得它可以同时支持浏览器和 Node.js 环境。对于浏览器环境来说，它通过封装 <code>XMLHttpRequest</code> API 来发送 HTTP 请求，而对于 Node.js 环境来说，它通过封装 Node.js 内置的 <code>http</code> 和 <code>https</code> 模块来发送 HTTP 请求。</p>
<p>在介绍如何增强默认适配器之前，我们先来回顾一下 Axios 完整请求的流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83387b95f4f24494b65b67458052f520~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解完 Axios 完整请求的流程之后，我们再来看一下 Axios 内置的 <code>xhrAdapter</code> 适配器，它被定义在 <code>lib/adapters/xhr.js</code> 文件中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// lib/adapters/xhr.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">xhrAdapter</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dispatchXhrRequest</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">var</span> requestData = config.data;
    <span class="hljs-keyword">var</span> requestHeaders = config.headers;

    <span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest();
    <span class="hljs-comment">// 省略大部分代码</span>
    <span class="hljs-keyword">var</span> fullPath = buildFullPath(config.baseURL, config.url);
    request.open(config.method.toUpperCase(), buildURL(fullPath, config.params, config.paramsSerializer), <span class="hljs-literal">true</span>);
    <span class="hljs-comment">// Set the request timeout in MS</span>
    request.timeout = config.timeout;

    <span class="hljs-comment">// Listen for ready state</span>
    request.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleLoad</span>(<span class="hljs-params"></span>) </span>&#123; ... &#125;

    <span class="hljs-comment">// Send the request</span>
    request.send(requestData);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显 <code>xhrAdapter</code> 适配器是一个函数对象，它接收一个 <code>config</code> 参数并返回一个 <code>Promise</code> 对象。而在 <code>xhrAdapter</code> 适配器内部，最终会使用 XMLHttpRequest API 来发送 HTTP 请求。为了实现缓存请求数据的功能，我们就可以考虑通过高阶函数来增强 <code>xhrAdapter</code> 适配器的功能。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 50 几篇 TS 系列教程。</p>
</blockquote>
<h4 data-id="heading-2">2.1 定义辅助函数</h4>
<h5 data-id="heading-3">2.1.1 定义 generateReqKey 函数</h5>
<p>在增强 <code>xhrAdapter</code> 适配器之前，我们先来定义一个 <code>generateReqKey</code> 函数，该函数用于根据当前请求的信息，生成请求 Key；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateReqKey</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; method, url, params, data &#125; = config;
  <span class="hljs-keyword">return</span> [method, url, Qs.stringify(params), Qs.stringify(data)].join(<span class="hljs-string">"&"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>generateReqKey</code> 函数生成的请求 key，将作为缓存项的 key，而对应的 value 就是默认 <code>xhrAdapter</code> 适配器返回的 Promise 对象。</p>
<h5 data-id="heading-4">2.1.2 定义 isCacheLike 函数</h5>
<p><code>isCacheLike</code> 函数用于判断传入的 cache 参数是否实现了前面定义的 Cache API，利用该函数，我们允许用户为每个请求自定义 Cache 对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isCacheLike</span>(<span class="hljs-params">cache</span>) </span>&#123;
<span class="hljs-keyword">return</span> !!(cache.set && cache.get && cache.delete && cache.clear  
&& <span class="hljs-keyword">typeof</span> cache.get === <span class="hljs-string">'function'</span> && <span class="hljs-keyword">typeof</span> cache.set === <span class="hljs-string">'function'</span> 
    && <span class="hljs-keyword">typeof</span> cache.delete === <span class="hljs-string">'function'</span> && <span class="hljs-keyword">typeof</span> cache.clear === <span class="hljs-string">'function'</span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2.2 定义 cacheAdapterEnhancer 函数</h4>
<p>为了让用户能够更灵活地控制数据缓存的功能，我们定义了一个 <code>cacheAdapterEnhancer</code> 函数，该函数支持两个参数：</p>
<ul>
<li>adapter：预增强的 Axios 适配器对象；</li>
<li>options：缓存配置对象，该对象支持 4 个属性，分别用于配置不同的功能：
<ul>
<li>maxAge：全局设置缓存的最大时间；</li>
<li>enabledByDefault：是否启用缓存，默认为 true；</li>
<li>cacheFlag：缓存标志，用于配置请求 config 对象上的缓存属性；</li>
<li>defaultCache：用于设置使用的缓存对象。</li>
</ul>
</li>
</ul>
<p>了解完 <code>cacheAdapterEnhancer</code> 函数的参数之后，我们来看一下该函数的具体实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cacheAdapterEnhancer</span>(<span class="hljs-params">adapter, options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; maxAge, enabledByDefault = <span class="hljs-literal">true</span>,
    cacheFlag = <span class="hljs-string">"cache"</span>, defaultCache = MemoryCache,
  &#125; = options;
  
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; url, method, params, forceUpdate &#125; = config;
    <span class="hljs-keyword">let</span> useCache = config[cacheFlag] !== <span class="hljs-literal">undefined</span> && config[cacheFlag] !== <span class="hljs-literal">null</span>
        ? config[cacheFlag]
        : enabledByDefault;
      <span class="hljs-keyword">if</span> (method === <span class="hljs-string">"get"</span> && useCache) &#123;
        <span class="hljs-keyword">const</span> cache = isCacheLike(useCache) ? useCache : defaultCache;
        <span class="hljs-keyword">let</span> requestKey = generateReqKey(config);  <span class="hljs-comment">// 生成请求Key</span>
        <span class="hljs-keyword">let</span> responsePromise = cache.get(requestKey); <span class="hljs-comment">// 从缓存中获取请求key对应的响应对象</span>
        <span class="hljs-keyword">if</span> (!responsePromise || forceUpdate) &#123; <span class="hljs-comment">// 缓存未命中/失效或强制更新时，则重新请求数据</span>
           responsePromise = (<span class="hljs-keyword">async</span> () => &#123;
             <span class="hljs-keyword">try</span> &#123;
               <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> adapter(config);  <span class="hljs-comment">// 使用默认的xhrAdapter发送请求</span>
             &#125; <span class="hljs-keyword">catch</span> (reason) &#123;
                 cache.delete(requestKey);
                 <span class="hljs-keyword">throw</span> reason;
                &#125;
           &#125;)();
           cache.set(requestKey, responsePromise, maxAge);  <span class="hljs-comment">// 保存请求返回的响应对象</span>
           <span class="hljs-keyword">return</span> responsePromise; <span class="hljs-comment">// 返回已保存的响应对象</span>
       &#125;
       <span class="hljs-keyword">return</span> responsePromise;
     &#125;
     <span class="hljs-keyword">return</span> adapter(config); <span class="hljs-comment">// 使用默认的xhrAdapter发送请求</span>
   &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的代码并不会复杂，核心的处理逻辑如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a53b4a88d64906ad7726c84c4c701a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">2.3 使用 cacheAdapterEnhancer 函数</h4>
<h5 data-id="heading-7">2.3.1 创建 Axios 对象并配置 adapter 选项</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> http = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">"https://jsonplaceholder.typicode.com"</span>,
  <span class="hljs-attr">adapter</span>: cacheAdapterEnhancer(axios.defaults.adapter, &#123;
    <span class="hljs-attr">enabledByDefault</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 默认禁用缓存</span>
    <span class="hljs-attr">maxAge</span>: <span class="hljs-number">5000</span>, <span class="hljs-comment">// 缓存时间为5s</span>
  &#125;),
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">2.3.2 使用 http 对象发送请求</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用缓存</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestWithCache</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> http.get(<span class="hljs-string">"/todos/1"</span>, &#123; <span class="hljs-attr">cache</span>: <span class="hljs-literal">true</span> &#125;);
  <span class="hljs-built_in">console</span>.dir(response);
&#125;

<span class="hljs-comment">// 不使用缓存</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestWithoutCache</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> http.get(<span class="hljs-string">"/todos/1"</span>, &#123; <span class="hljs-attr">cache</span>: <span class="hljs-literal">false</span> &#125;);
  <span class="hljs-built_in">console</span>.dir(response);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 cache 属性除了支持布尔值之外，我们可以配置实现 Cache API 的缓存对象，具体的使用示例如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> customCache = &#123; <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;<span class="hljs-comment">/*...*/</span>&#125;, <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params"></span>)</span> &#123;<span class="hljs-comment">/*...*/</span>&#125;, <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params"></span>)</span> &#123;<span class="hljs-comment">/*...*/</span>&#125;, <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span> &#123;<span class="hljs-comment">/*...*/</span>&#125;&#125;;
      
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestForceUpdate</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> http.get(<span class="hljs-string">"/todos/1"</span>, &#123;
    <span class="hljs-attr">cache</span>: customCache,
    <span class="hljs-attr">forceUpdate</span>: <span class="hljs-literal">true</span>,
  &#125;);
  <span class="hljs-built_in">console</span>.dir(response);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，如何通过增强 <code>xhrAdapter</code> 适配器来实现 Axios 缓存请求数据的功能已经介绍完了。由于完整的示例代码内容比较多，阿宝哥就不放具体的代码了。感兴趣的小伙伴，可以访问以下地址浏览示例代码。</p>
<blockquote>
<p>完整的示例代码：<a href="https://gist.github.com/semlinker/b8a7bd5a0a16c2d04011c2c4a8167fbd" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/semlinker/b…</a></p>
</blockquote>
<h3 data-id="heading-9">三、总结</h3>
<p>本文介绍了在 Axios 中如何缓存请求数据及如何设计缓存对象，基于文中定义的 <code>cacheAdapterEnhancer</code> 函数，你可以轻松地扩展缓存的功能。至此 Axios 四部曲已经全部更新完成了，以下是其他文章的链接，感兴趣的小伙伴可以了解一下。写得不好的地方，请多多包涵。</p>
<ul>
<li><a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a></li>
<li><a href="https://mp.weixin.qq.com/s/By-iXlONjSZLKFG2Xd7rpg" target="_blank" rel="nofollow noopener noreferrer">Axios 如何取消重复请求？</a></li>
<li><a href="https://mp.weixin.qq.com/s/8RJSBwCDTvwX3Oql31ckkg" target="_blank" rel="nofollow noopener noreferrer">Axios 如何实现请求重试？</a></li>
</ul>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-10">四、参考资源</h3>
<ul>
<li><a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a></li>
<li><a href="https://mp.weixin.qq.com/s/By-iXlONjSZLKFG2Xd7rpg" target="_blank" rel="nofollow noopener noreferrer">Axios 如何取消重复请求？</a></li>
<li><a href="https://github.com/kuitos/axios-extensions" target="_blank" rel="nofollow noopener noreferrer">Github - axios-extensions</a></li>
</ul></div>  
</div>
            