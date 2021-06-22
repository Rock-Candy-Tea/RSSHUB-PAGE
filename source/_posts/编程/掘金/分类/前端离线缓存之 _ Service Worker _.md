
---
title: '前端离线缓存之 _ Service Worker _'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/566c11b5108c4b709603c86bdaba52f7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 01:50:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/566c11b5108c4b709603c86bdaba52f7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">定义</h5>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Service_Worker_API" target="_blank" rel="nofollow noopener noreferrer">Service workers</a> 本质上充当 Web 应用程序、浏览器与网络（可用时）之间的<code>代理服务器</code>。这个 API 旨在创建有效的<code>离线</code>体验，它会拦截网络请求并根据网络是否可用采取来适当的动作、更新来自服务器的的资源。它还提供入口以推送通知和访问后台同步 API。</p>
<h5 data-id="heading-1">特性</h5>
<ol>
<li>一个独立的<code>worker</code>线程，独立于当前网页进程，有自己独立的workercontext。</li>
<li>一旦被<code>install</code>，就永远存在，除非被手动<code>unregister</code></li>
<li>用到的时候可以直接<code>唤醒</code>，不用的时候<code>自动睡眠</code></li>
<li>可编程拦截代理请求和返回，缓存文件，缓存的文件可以被网页进程取到（包括网络离线状态）</li>
<li>离线内容开发者可控</li>
<li>能向客户端<code>推送</code>消息</li>
<li>不能直接操作<code>DOM</code></li>
<li>必须在<code>HTTPS</code>或者<code>localhost</code>环境下才能工作</li>
<li>异步实现，内部大都是通过<code>Promise</code>实现</li>
</ol>
<h5 data-id="heading-2">生命周期</h5>
<h6 data-id="heading-3">定义：简单来说，分为三个阶段：“注册（<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/ServiceWorkerContainer/register" target="_blank" rel="nofollow noopener noreferrer">register</a>）”、“安装（<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/InstallEvent" target="_blank" rel="nofollow noopener noreferrer">Install</a>）”、“激活（activate）”, 还有最重要的一个拦截事件 "<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/FetchEvent" target="_blank" rel="nofollow noopener noreferrer">fetch</a>"</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/566c11b5108c4b709603c86bdaba52f7~tplv-k3u1fbpfcp-watermark.image" alt="service_worker_lifecycle.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-comment">/**
 * 特别说明
 * <span class="hljs-doctag">@scope </span>表示定义service worker注册范围的URL ；service worker可以控制的URL 范围
 */</span>
<span class="hljs-keyword">if</span> (<span class="hljs-string">'serviceWorker'</span> <span class="hljs-keyword">in</span> navigator) &#123;
  navigator.serviceWorker.register(<span class="hljs-string">'sw.js'</span>, &#123;<span class="hljs-attr">scope</span>: <span class="hljs-string">'./'</span>&#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">registration</span>) </span>&#123;
    <span class="hljs-comment">// do something</span>
  &#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">// do something</span>
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// sw.js 文件</span>
self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">// do something</span>
&#125;);
self.addEventListener(<span class="hljs-string">'activate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">// do something</span>
&#125;)


<span class="hljs-comment">/*
     * The most important
 */</span>
self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">/**
    1. 主要通过 CacheStorage 、Cache 等 API 操作"离线数据"和"实时数据"
    2. 返回给客户端的数据主要分为：
       1. Network First：网络优先策略
       2. Cache First：缓存优先策略
       3. Network Only：仅通过发送正常的网络请求获取资源，并将请求响应结果直接返回。
       4. Cache Only：仅从缓存中读取资源。
  
  */</span>
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">工作流程</h5>
<h6 data-id="heading-5">注意事项</h6>
<ul>
<li>Service Worker 文件只在首次注册的时候执行了一次</li>
<li><code>安装</code>、<code>激活</code>流程也只是在<code>首次</code>执行 Service Worker 文件的时候进行了一次。</li>
<li><code>fetch</code> 事件
<ul>
<li>首次注册成功的 Service Worker 没能拦截当前页面的请求。</li>
<li>非首次注册的 Service Worker 可以控制当前的页面并能拦截请求。</li>
<li>原因：为什么首次没有拦截到网络请求呢？主要是因为在 Service Worker 的注册是一个<code>异步</code>的过程，在激活完成后当前页面的请求都<code>已经发送完成</code>，因为<code>时机太晚</code>，此时是拦截不到任何请求的，只能等待<code>下次</code>访问再进行</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e336b2890d4df2bf52cf77f427661c~tplv-k3u1fbpfcp-watermark.image" alt="service_worker_process.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">Service Worker 更新原理</h5>
<h6 data-id="heading-7">skipWaiting</h6>
<ul>
<li>Service Worker 一旦更新，需要等所有的终端都<code>关闭</code>之后，再重新打开页面才能激活新的 Service Worker，这个过程太复杂了。通常情况下，开发者希望当 Service Worker 一检测到更新就直接激活新的 Service Worker。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/933a9be2090f4f06a38be854e85e1219~tplv-k3u1fbpfcp-watermark.image" alt="service_worker_update_process.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-8"><a href="https://lavas-project.github.io/pwa-book/chapter04/4-service-worker-debug.html" target="_blank" rel="nofollow noopener noreferrer">Service Worker 调试</a></h5>
<h5 data-id="heading-9">本地数据储存</h5>
<blockquote>
<p>经过以上的铺垫，现在可愉快操作<code>离线数据</code>和<code>实时数据</code>了,先看一段代码，后补充！</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CACHE_NAME = <span class="hljs-string">'fed-cache'</span>
<span class="hljs-keyword">const</span> Self = globalThis

Self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  Self.skipWaiting()
  Self.caches.open(CACHE_NAME)
&#125;)
Self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">/*
   * 是否含有网络
   * 是：进行网络请求，且更新cache数据（保持数据比较新）
   * 否：进行离线缓存
   */</span>
  <span class="hljs-keyword">if</span> (Self.navigator.onLine) &#123;
    util.fetchPut(event.request.clone())
  &#125; <span class="hljs-keyword">else</span> &#123;
    event.respondWith(
      caches.match(event.request).then(<span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> response
      &#125;)
    )
  &#125;
&#125;)

<span class="hljs-keyword">let</span> util = &#123;
  <span class="hljs-attr">fetchPut</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">request</span>) </span>&#123;
    <span class="hljs-keyword">return</span> fetch(request).then(<span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> responseClone = response.clone()
      <span class="hljs-keyword">if</span> (util.noCache(response)) &#123;
        <span class="hljs-keyword">return</span> response
      &#125;
      <span class="hljs-keyword">if</span> (request.method === <span class="hljs-string">'GET'</span>) &#123;
        Self.caches.open(CACHE_NAME).then(<span class="hljs-function">(<span class="hljs-params">cache</span>) =></span> &#123;
          cache.put(request, responseClone)
        &#125;)
      &#125;
      <span class="hljs-keyword">return</span> response
    &#125;)
  &#125;,
  <span class="hljs-attr">noCache</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (
      !response ||
      response.status !== <span class="hljs-number">200</span> ||
      response.type !== <span class="hljs-string">'basic'</span> ||
      !response.url.includes(<span class="hljs-string">'http'</span>) ||
      response.url.includes(<span class="hljs-string">'vite'</span>)
    ) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>下面将介绍操作缓存的API，我自个理解一个概念，<code>Cache</code> 类似<code>IndexedDB</code>都为数据库
<code>CacheStorage API</code> 主要操作 <code>数据库</code>
<code>Cache API</code> 主要操作 <code>数据表</code></p>
</blockquote>
<h5 data-id="heading-10"><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/CacheStorage" target="_blank" rel="nofollow noopener noreferrer">CacheStorage API</a></h5>
<ol>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/CacheStorage/open" target="_blank" rel="nofollow noopener noreferrer">CacheStorage.open()</a>  创建/打开数据库</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/CacheStorage/match" target="_blank" rel="nofollow noopener noreferrer">CacheStorage.match()</a> 在<code>所有数据库</code>中，检索符合条件的返回<code>Response</code> 对象</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/CacheStorage/has" target="_blank" rel="nofollow noopener noreferrer">CacheStorage.has()</a>   是否含有某个数据库</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/CacheStorage/delete" target="_blank" rel="nofollow noopener noreferrer">CacheStorage.delete()</a> 删除某个数据库</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/CacheStorage/keys" target="_blank" rel="nofollow noopener noreferrer">CacheStorage.keys()</a>  遍历所有的数据库，返回数组（包含数据库名字）</li>
</ol>
<h5 data-id="heading-11"><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache" target="_blank" rel="nofollow noopener noreferrer">Cache API</a></h5>
<ol>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/match" target="_blank" rel="nofollow noopener noreferrer">Cache.match(request, options)</a> 查询单条数据</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/matchAll" target="_blank" rel="nofollow noopener noreferrer">Cache.matchAll(request, options)</a> 查询多条数据</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/add" target="_blank" rel="nofollow noopener noreferrer">Cache.add(request)</a> 添加一条数据</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/addAll" target="_blank" rel="nofollow noopener noreferrer">Cache.addAll(requests)</a> 添加多条数据</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/put" target="_blank" rel="nofollow noopener noreferrer">Cache.put(request, response)</a> 添加一条数据</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/delete" target="_blank" rel="nofollow noopener noreferrer">Cache.delete(request, options)</a> 删除一条数据</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Cache/keys" target="_blank" rel="nofollow noopener noreferrer">Cache.keys(request, options)</a> 遍历数据表</li>
</ol>
<h5 data-id="heading-12">缓存空间的使用情况</h5>
<blockquote>
<p>主要用于管理空间内存，达到限制要定时处理。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 查询当前缓存空间的使用情况
 * 缓存资源的过期失效和清理工作，尽量避免被动触发浏览器的资源清理
 */</span>
navigator.storage.estimate().then(<span class="hljs-function">(<span class="hljs-params">estimate</span>) =></span> &#123;
  <span class="hljs-comment">// 设备为当前域名所分配的存储空间总大小</span>
  <span class="hljs-built_in">console</span>.log(estimate.quota)
  <span class="hljs-comment">// 当前域名已经使用的存储空间大小</span>
  <span class="hljs-built_in">console</span>.log(estimate.usage)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13"><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/FetchEvent" target="_blank" rel="nofollow noopener noreferrer">FetchEvent</a></h5>
<ol>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/FetchEvent/respondWith" target="_blank" rel="nofollow noopener noreferrer">FetchEvent.respondWith()</a> 主要防止异步操作， 和 <code>async await</code> 感觉一样，扩展延长 <code>fetch</code> 事件生命周期的作用</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 错误用法</span>
self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-comment">// 因fetch属于异步，存在fetch 代码已执行完毕，而setTimeout 未触发的可能性</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      event.respondWith(<span class="hljs-keyword">new</span> Response(<span class="hljs-string">'Hello World!'</span>))
    &#125;, <span class="hljs-number">1000</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 正确用法</span>

<span class="hljs-comment">// 等待 1 秒钟之后异步返回 Response 对象</span>
event.respondWith(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-keyword">new</span> Response(<span class="hljs-string">'Hello World!'</span>))
  &#125;, <span class="hljs-number">1000</span>)
&#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/ExtendableEvent/waitUntil" target="_blank" rel="nofollow noopener noreferrer">ExtendableEvent.waitUntil()</a> 方法告诉事件分发器该事件仍在进行。这个方法也可以用于检测进行的任务是否成功。在服务工作线程中，这个方法告诉浏览器事件一直进行，直至 promise 解决，浏览器不应该在事件中的异步操作完成之前终止服务工作线程。 一句话 <code>延长生命周期</code>, 可用于<code>install</code>、<code>fetch</code> 事件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">const</span> preCache = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> cache = <span class="hljs-keyword">await</span> caches.open(<span class="hljs-string">'static-v1'</span>);
    <span class="hljs-keyword">return</span> cache.addAll([
      <span class="hljs-string">'/'</span>,
      <span class="hljs-string">'/about/'</span>,
      <span class="hljs-string">'/static/styles.css'</span>
    ]);
  &#125;;
  event.waitUntil(preCache());
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">通信 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Clients" target="_blank" rel="nofollow noopener noreferrer">Clients</a> 、<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Client" target="_blank" rel="nofollow noopener noreferrer">Client</a></h5>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// main.js (主线程)</span>
 navigator.serviceWorker.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`message: <span class="hljs-subst">$&#123;event.data&#125;</span>`</span>)
 &#125;)
 
 <span class="hljs-comment">// sw.js  文件</span>
  self.clients.matchAll().then(<span class="hljs-function"><span class="hljs-params">allClients</span>=></span>&#123;
    allClients.forEach(<span class="hljs-function"><span class="hljs-params">client</span> =></span> &#123;
      client.postMessage(<span class="hljs-string">'I am Rainy'</span>)
    &#125;);
  &#125;)
  
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">最后注意的点</h5>
<ol>
<li><code>Cache.put</code>, <code>Cache.add</code>和<code>Cache.addAll</code>只能在GET请求下使用。</li>
<li>ServiceWorker, 只能<code>fetch</code>进行拦截，<code>axios</code>不行</li>
</ol>
<h5 data-id="heading-16">参考文章</h5>
<ol>
<li><a href="https://lavas-project.github.io/pwa-book/chapter04.html" target="_blank" rel="nofollow noopener noreferrer">Service Worker</a></li>
</ol></div>  
</div>
            