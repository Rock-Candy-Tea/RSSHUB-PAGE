
---
title: 'Axios 如何实现请求重试？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/599860c469cd47129a8bae4336eed107~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 16:36:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/599860c469cd47129a8bae4336eed107~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 <a href="https://mp.weixin.qq.com/s/By-iXlONjSZLKFG2Xd7rpg" target="_blank" rel="nofollow noopener noreferrer">Axios 如何取消重复请求？</a> 这篇文章中，阿宝哥介绍了在 <a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Axios</a> 中如何取消重复请求及 <code>CancelToken</code> 的工作原理。而本文将介绍在 Axios 中如何通过 <strong>拦截器或适配器</strong> 来实现请求重试的功能。那么为什么要进行请求重试呢？这是因为在某些情况下，比如请求超时的时候，我们希望能自动重新发起请求进行重试操作，从而完成对应的操作。</p>
<p>下面阿宝哥将介绍如何使用 <a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Axios</a> 提供的拦截器或适配器来实现请求重试的功能，如果你对 Axios 的拦截器和适配器还不熟悉的话，建议先阅读 <a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a> 这篇文章。接下来，我们先来介绍如何使用拦截器实现请求重试的方案。</p>
<h3 data-id="heading-0">一、拦截器实现请求重试的方案</h3>
<p><a href="https://github.com/axios/axios" target="_blank" rel="nofollow noopener noreferrer">Axios</a> 是一个基于 Promise 的 HTTP 客户端，而 HTTP 协议是基于请求和响应：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/599860c469cd47129a8bae4336eed107~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以 Axios 提供了 <strong>请求拦截器和响应拦截器</strong> 来分别处理请求和响应，它们的作用如下：</p>
<ul>
<li>请求拦截器：该类拦截器的作用是在请求发送前统一执行某些操作，比如在请求头中添加 token 字段。</li>
<li>响应拦截器：该类拦截器的作用是在接收到服务器响应后统一执行某些操作，比如发现响应状态码为 401 时，自动跳转到登录页。</li>
</ul>
<p>在 Axios 中设置拦截器很简单，通过 <code>axios.interceptors.request</code> 和 <code>axios.interceptors.response</code> 对象提供的 <code>use</code> 方法，就可以分别设置请求拦截器和响应拦截器：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> AxiosInstance &#123;
  <span class="hljs-attr">interceptors</span>: &#123;
    <span class="hljs-attr">request</span>: AxiosInterceptorManager<AxiosRequestConfig>;
    response: AxiosInterceptorManager<AxiosResponse>;
  &#125;;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> AxiosInterceptorManager<V> &#123;
  use(onFulfilled?: <span class="hljs-function">(<span class="hljs-params">value: V</span>) =></span> V | <span class="hljs-built_in">Promise</span><V>, 
    onRejected?: <span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>): <span class="hljs-built_in">number</span>;
  eject(id: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">void</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于请求重试的功能来说，我们希望让用户不仅能够设置重试次数，而且可以设置重试延时时间。当请求失败的时候，若该请求的配置对象配置了重试次数，而 Axios 就会重新发起请求进行重试操作。为了能够全局进行请求重试，接下来我们在响应拦截器上来实现请求重试功能，具体代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.interceptors.response.use(<span class="hljs-literal">null</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> config = err.config;
  <span class="hljs-keyword">if</span> (!config || !config.retryTimes) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err);
  <span class="hljs-keyword">const</span> &#123; __retryCount = <span class="hljs-number">0</span>, retryDelay = <span class="hljs-number">300</span>, retryTimes &#125; = config;
  <span class="hljs-comment">// 在请求对象上设置重试次数</span>
  config.__retryCount = __retryCount;
  <span class="hljs-comment">// 判断是否超过了重试次数</span>
  <span class="hljs-keyword">if</span> (__retryCount >= retryTimes) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err);
  &#125;
  <span class="hljs-comment">// 增加重试次数</span>
  config.__retryCount++;
  <span class="hljs-comment">// 延时处理</span>
  <span class="hljs-keyword">const</span> delay = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve();
    &#125;, retryDelay);
  &#125;);
  <span class="hljs-comment">// 重新发起请求</span>
  <span class="hljs-keyword">return</span> delay.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> axios(config);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的代码并不会复杂，对应的处理流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d248bd368fd145a0b4e0a8bee7c66541~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>介绍完如何使用拦截器实现请求重试的功能之后，下面阿宝哥来介绍适配器实现请求重试的方案。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 50 几篇 TS 系列教程。</p>
</blockquote>
<h3 data-id="heading-1">二、适配器实现请求重试的方案</h3>
<p>Axios 引入了适配器，使得它可以同时支持浏览器和 Node.js 环境。对于浏览器环境来说，它通过封装 <code>XMLHttpRequest</code> API 来发送 HTTP 请求，而对于 Node.js 环境来说，它通过封装 Node.js 内置的 <code>http</code> 和 <code>https</code> 模块来发送 HTTP 请求。</p>
<p>在 <a href="https://mp.weixin.qq.com/s/NfyxtWUzjHh6ucXvBF9B4Q" target="_blank" rel="nofollow noopener noreferrer">Axios 如何缓存请求数据？</a> 这篇文章中，阿宝哥介绍了如何通过增强默认的 Axios 适配器，来实现缓存请求数据的功能。同样，采用类似的思路，我们也可以通过增强默认的  Axios 适配器来实现请求重试的功能。</p>
<p>在介绍如何增强默认适配器之前，我们先来看一下 Axios 内置的 <code>xhrAdapter</code> 适配器，它被定义在 <code>lib/adapters/xhr.js</code> 文件中：</p>
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
<p>很明显 <code>xhrAdapter</code> 适配器是一个函数对象，它接收一个 <code>config</code> 参数并返回一个 <code>Promise</code> 对象。而在 <code>xhrAdapter</code> 适配器内部，最终会使用 <code>XMLHttpRequest</code> API 来发送 HTTP 请求。为了实现请求重试的功能，我们就可以考虑通过高阶函数来增强 <code>xhrAdapter</code> 适配器的功能。</p>
<h4 data-id="heading-2">2.1 定义 retryAdapterEnhancer 函数</h4>
<p>为了让用户能够更灵活地控制请求重试的功能，我们定义了一个 <code>retryAdapterEnhancer</code> 函数，该函数支持两个参数：</p>
<ul>
<li>adapter：预增强的 Axios 适配器对象；</li>
<li>options：缓存配置对象，该对象支持  2 个属性，分别用于配置不同的功能：
<ul>
<li>times：全局设置请求重试的次数；</li>
<li>delay：全局设置请求延迟的时间，单位是 ms。</li>
</ul>
</li>
</ul>
<p>了解完 <code>retryAdapterEnhancer</code> 函数的参数之后，我们来看一下该函数的具体实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">retryAdapterEnhancer</span>(<span class="hljs-params">adapter, options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; times = <span class="hljs-number">0</span>, delay = <span class="hljs-number">300</span> &#125; = options;

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">async</span> (config) => &#123;
    <span class="hljs-keyword">const</span> &#123; retryTimes = times, retryDelay = delay &#125; = config;
    <span class="hljs-keyword">let</span> __retryCount = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">const</span> request = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> adapter(config);
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-comment">// 判断是否进行重试</span>
        <span class="hljs-keyword">if</span> (!retryTimes || __retryCount >= retryTimes) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err);
        &#125;
        __retryCount++; <span class="hljs-comment">// 增加重试次数</span>
        <span class="hljs-comment">// 延时处理</span>
        <span class="hljs-keyword">const</span> delay = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            resolve();
          &#125;, retryDelay);
         &#125;);
         <span class="hljs-comment">// 重新发起请求</span>
         <span class="hljs-keyword">return</span> delay.then(<span class="hljs-function">() =></span> &#123;
           <span class="hljs-keyword">return</span> request();
         &#125;);
        &#125;
      &#125;;
   <span class="hljs-keyword">return</span> request();
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的代码并不会复杂，核心的处理逻辑如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7b2d97dde104c01ac025525f65ad6bb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">2.2 使用 retryAdapterEnhancer 函数</h4>
<h5 data-id="heading-4">2.2.1 创建 Axios 对象并配置 adapter 选项</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> http = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">"http://localhost:3000/"</span>,
  <span class="hljs-attr">adapter</span>: retryAdapterEnhancer(axios.defaults.adapter, &#123;
    <span class="hljs-attr">retryDelay</span>: <span class="hljs-number">1000</span>,
  &#125;),
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2.2.2 使用 http 对象发送请求</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 请求失败不重试</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestWithoutRetry</span>(<span class="hljs-params"></span>) </span>&#123;
  http.get(<span class="hljs-string">"/users"</span>);
&#125;

<span class="hljs-comment">// 请求失败重试</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestWithRetry</span>(<span class="hljs-params"></span>) </span>&#123;
  http.get(<span class="hljs-string">"/users"</span>, &#123; <span class="hljs-attr">retryTimes</span>: <span class="hljs-number">2</span> &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，如何通过增强 <code>xhrAdapter</code> 适配器来实现 Axios 请求重试的功能已经介绍完了。由于完整的示例代码内容比较多，阿宝哥就不放具体的代码了。感兴趣的小伙伴，可以访问以下地址浏览示例代码。</p>
<blockquote>
<p>完整的示例代码：<a href="https://gist.github.com/semlinker/979ebc659abacea7aa6c0c44af070afe" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/semlinker/9…</a></p>
</blockquote>
<p>这里我们来看一下 Axios 实现请求重试示例的运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/742c5f1808d343a292bd21af1115385c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">三、总结</h3>
<p>本文介绍了在 Axios 中如何实现请求重试，基于文中定义的 <code>retryAdapterEnhancer</code> 函数或响应拦截器，你可以轻松地扩展请求重试的功能。Axios 是一个很优秀的开源项目，里面有很多值得我们学习与借鉴的地方。如果你对 Axios 内部 HTTP 拦截器的设计与实现、HTTP 适配器的设计与实现及如何防御 CSRF 攻击感兴趣的话，可以阅读 <a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a> 这篇文章。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-7">四、参考资源</h3>
<ul>
<li><a href="https://github.com/kuitos/axios-extensions" target="_blank" rel="nofollow noopener noreferrer">Github - axios-extensions</a></li>
<li><a href="https://mp.weixin.qq.com/s/By-iXlONjSZLKFG2Xd7rpg" target="_blank" rel="nofollow noopener noreferrer">Axios 如何取消重复请求？</a></li>
<li><a href="https://mp.weixin.qq.com/s/NfyxtWUzjHh6ucXvBF9B4Q" target="_blank" rel="nofollow noopener noreferrer">Axios 如何缓存请求数据？</a></li>
<li><a href="https://mp.weixin.qq.com/s/gqr-CpLEIAEymbdLX3NrpQ" target="_blank" rel="nofollow noopener noreferrer">77.9K 的 Axios 项目有哪些值得借鉴的地方</a></li>
</ul></div>  
</div>
            