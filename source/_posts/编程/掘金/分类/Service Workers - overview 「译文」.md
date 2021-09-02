
---
title: 'Service Workers - overview 「译文」'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b72668ba49bc48d98aa275a3ffd39eb1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 23:14:05 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b72668ba49bc48d98aa275a3ffd39eb1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ffundamentals%2Fprimers%2Fservice-workers" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/fundamentals/primers/service-workers" ref="nofollow noopener noreferrer">developers.google.com/web/fundame…</a></h4>
<p>丰富的离线体验、定期后台同步、推送通知——这些通常是手机APP的功能——但是现在web端也可以拥有。Service Worker 提供了这些功能所依赖的技术基础。</p>
<h2 data-id="heading-1">什么是 service worker ？</h2>
<p>Service Worker 是浏览器在后台运行的脚本，与网页分开，为不需要网页或用户交互的功能打开大门。 今天，它们已经包含推送通知和后台同步等功能。 将来，Service Worker 可能会支持其他功能，例如定期同步或地理围栏。 本教程中讨论的核心功能是拦截和处理网络请求的能力，包括以编程方式管理响应缓存。</p>
<p>它还有一个令人兴奋的 API ，就是支持离线体验，让开发人员完全控制体验。</p>
<p>在 Service Worker 之前，还有一个 API 可以为用户提供网络离线体验，称为 AppCache。Service Worker 避免了 AppCache API 的许多问题。</p>
<p>Service Worker 的注意事项：</p>
<ul>
<li>它是一个 JavaScript Worker，所以不能直接访问 DOM。但是，Service Worker 可以通过回应 postMessage 接口发送的消息与其控制的页面进行通信，这些页面可以根据需要操作 DOM。</li>
<li>Service Worker 是一个可编程的网络代理，你可以控制如何处理来自页面的网络请求。</li>
<li>它在不使用时终止，并在下一次需要时重新启动，因此不能依赖 Service Worker 的 <code>onfetch</code> 和 <code>onmessage</code> 处理程序中的全局状态。如果需要在重启后保留和重用某些信息，Service Worker 可以访问 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIndexedDB_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API" ref="nofollow noopener noreferrer">IndexedDB API</a>。</li>
<li>Service Worker 广泛使用了 Promise，所以如果你还不太了解 Promise ，请先学习它。</li>
</ul>
<h2 data-id="heading-2">Service Worker 生命周期</h2>
<p>Service Worker 的生命周期与你的网页完全分开。</p>
<p>安装 Service Worker，您需要在页面的 JavaScript 中注册它。</p>
<p>通常在安装步骤中，你需要缓存一些静态资源。如果所有文件都被成功缓存，那么证明 Service Worker 已经安装成功。如果任何文件无法下载和缓存，则安装步骤将失败并且 Service Worker 不会被激活（即不会被安装）。如果发生这种情况，请不要担心，它下次会再试一次。</p>
<p>安装后，将执行激活步骤，在这时处理旧缓存管理，我们将在 Service Worker 更新部分进行介绍。</p>
<p>激活后，Service Worker 将控制其范围内的所有页面，除了第一次注册 Service Worker 的页面在再次加载之前不会受到控制。一旦 Service Worker 处于控制状态，它将处于两种状态之一：被终止以节省内存，或者它会处理从页面发出的网络请求或消息时的 <code>fetch</code> 和 <code>message</code> 事件。</p>
<p>下面是首次安装时 Service Worker 生命周期的过度简化版本。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b72668ba49bc48d98aa275a3ffd39eb1~tplv-k3u1fbpfcp-watermark.image" alt="sw-lifecycle.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">先决条件</h2>
<h3 data-id="heading-4">浏览器支持</h3>
<p>浏览器选项正在增加。 Chrome、Firefox 和 Opera 支持 Service Worker。 Microsoft Edge 现在显示公众支持。 甚至 Safari 也暗示了未来的发展。 您可以在 Jake Archibald 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjakearchibald.github.io%2Fisserviceworkerready%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jakearchibald.github.io/isserviceworkerready/" ref="nofollow noopener noreferrer">is Serviceworker ready</a> 网站上关注所有浏览器的进度。</p>
<h3 data-id="heading-5">HTTPS</h3>
<p>在开发过程中，可以通过 localhost 使用 Service Worker，但要将其部署在站点上，需要在服务器上设置 HTTPS。</p>
<p>使用 Service Worker，可以劫持连接、制造和过滤响应。权利很大。虽然你会永远拥有这些权力，但中间人可能不会。为避免这种情况，你只能在通过 HTTPS 提供服务的页面上注册 Service Worker，这样我们可以知道浏览器接收的 Service Worker 有没有被篡改。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpages.github.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pages.github.com/" ref="nofollow noopener noreferrer">GitHub Pages</a> 是一个通过 HTTPS 提供服务的 demo，可以参阅一下。</p>
<p>如果你想将 HTTPS 添加到服务器，那么你需要获取 TLS 证书并在服务器里设置它。请查看服务器的文档，然后查看 Mozilla 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fssl-config.mozilla.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ssl-config.mozilla.org/" ref="nofollow noopener noreferrer">SSL 配置生成器</a> 进行操作。</p>
<h2 data-id="heading-6">注册 Service Worker</h2>
<p>安装 Service Worker，需要通过在你的页面中注册它。这样浏览器就可以知道你的 Service Worker 在 JavaScript 文件的位置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-string">'serviceWorker'</span> <span class="hljs-keyword">in</span> navigator) &#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        navigator.serviceWorker.register(<span class="hljs-string">'/sw.js'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">registration</span>) </span>&#123;
            <span class="hljs-comment">// Registration was successful</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ServiceWorker registration successful with scope: '</span>, registration.scope);
        &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
            <span class="hljs-comment">// registration failed :(</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ServiceWorker registration failed: '</span>, err);
        &#125;);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码检查 Service Worker API 是否可用，如果可用，则在页面加载后注册 <code>/sw.js</code> 中的 Service Worker 。</p>
<p>你可以在每次页面加载时调用 <code>register()</code> 而不用担心；浏览器会判断 service worker 是否已经注册并相应地处理它。</p>
<p><code>register()</code> 方法的一个微妙之处是 service worker 文件的位置。在这种情况下，你会注意到 service worker 文件位于域的根目录。这意味着 service worker 的范围将是整个源。换句话说，这个 Service Worker 将接收该域上所有内容的 <code>fetch</code> 事件。如果我们在 <code>/example/sw.js</code> 中注册 Service Worker ，那么 Service Worker 只会看到 URL 以 <code>/example/</code> 开头的页面（即 /example/page1/、/example/page2/）的 <code>fetch</code> 事件。</p>
<p>现在，您可以跳转到 chrome://inspect/#service-workers 并在你的站点里查看 Service Worker 是否已启用。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e80256bea21f46b4ab86692db7623fe8~tplv-k3u1fbpfcp-watermark.image" alt="sw-chrome-inspect.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首次实现 Service Worker 时，可以通过 <a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">chrome://serviceworker-internals</a> 查看你的 Service Worker 详细信息。如果仅仅是了解 Service Worker 的生命周期，这个网址还是有用的，以后它可以被 <a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">chrome://inspect/#service-workers</a> 取代。</p>
<p>你可能会发现在隐身窗口中测试 Service Worker 很有用，可以关闭并重新打开窗口，之前的 Service Worker 不会影响新窗口。一旦该窗口关闭，从隐身窗口中创建的任何注册和缓存都将被清除。</p>
<h2 data-id="heading-7">安装 service worker</h2>
<p>在受控页面启动注册过程后，service worker 脚本开始处理安装事件。</p>
<p>最基本的示例：你需要为 <code>install</code> 事件定义回调并决定要缓存哪些文件。</p>
<pre><code class="hljs language-js copyable" lang="js">self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">// Perform install steps</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>install</code> 回调中，需要执行以下步骤：</p>
<ol>
<li>打开缓存，</li>
<li>缓存我们的文件，</li>
<li>确认是否缓存了所有必需的资源。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> CACHE_NAME = <span class="hljs-string">'my-site-cache-v1'</span>;
<span class="hljs-keyword">var</span> urlsToCache = [
  <span class="hljs-string">'/'</span>,
  <span class="hljs-string">'/styles/main.css'</span>,
  <span class="hljs-string">'/script/main.js'</span>
];

self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">// Perform install steps</span>
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">cache</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Opened cache'</span>);
        <span class="hljs-keyword">return</span> cache.addAll(urlsToCache);
      &#125;)
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，<code>caches.open()</code> 传入了我们的缓存名称，之后调用 <code>cache.addAll()</code> 并传入我们的文件数组。这是一个 <code>promise</code> 链（<code>caches.open()</code> 和 <code>cache.addAll()</code>）。<code>event.waitUntil()</code> 方法接受这个 <code>promise</code> 并使用它来知道安装需要多长时间，以及它是否成功。</p>
<p>如果所有文件都缓存成功，则 Service Worker 安装成功。如果其中的某个文件下载失败，则安装步骤失败。所以请谨慎确定在安装步骤中缓存的文件列表。定义一长串文件会增加一个文件无法缓存的可能性，从而导致 Service Worker 无法安装。</p>
<p>这只是一个demo，你可以在安装事件中执行其他任务或完全避免设置安装事件侦听器。</p>
<h2 data-id="heading-8">缓存和返回请求</h2>
<p>现在我们已经安装了 Service Worker，接下来我们要 <code>return</code> 其中某个缓存的 <code>responses</code>。</p>
<p>安装 Service Worker 并且用户打开新页面或刷新当前页面后，Service Worker 将开始接收 <code>fetch</code> 事件，示例如下。</p>
<pre><code class="hljs language-js copyable" lang="js">self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  event.respondWith(
    caches.match(event.request)
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
        <span class="hljs-comment">// Cache hit - return response</span>
        <span class="hljs-keyword">if</span> (response) &#123;
          <span class="hljs-keyword">return</span> response;
        &#125;
        <span class="hljs-keyword">return</span> fetch(event.request);
      &#125;
    )
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们定义了 fetch 事件，在 event.respondWith() 中，我们从 caches.match() 中传入了一个 promise。这个方法会查看请求并从 Service Worker 创建的缓存中查找缓存结果。</p>
<p>如果我们有匹配的响应，会返回缓存的值，否则返回调用 fetch 的结果；</p>
<p>如果我们想累积缓存新请求，可以通过处理 fetch 请求的响应然后将其添加到缓存中来实现，如下所示。</p>
<pre><code class="hljs language-js copyable" lang="js">self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  event.respondWith(
    caches.match(event.request)
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
        <span class="hljs-comment">// Cache hit - return response</span>
        <span class="hljs-keyword">if</span> (response) &#123;
          <span class="hljs-keyword">return</span> response;
        &#125;

        <span class="hljs-keyword">return</span> fetch(event.request).then(
          <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
            <span class="hljs-comment">// Check if we received a valid response</span>
            <span class="hljs-keyword">if</span>(!response || response.status !== <span class="hljs-number">200</span> || response.type !== <span class="hljs-string">'basic'</span>) &#123;
              <span class="hljs-keyword">return</span> response;
            &#125;

            <span class="hljs-comment">// IMPORTANT: Clone the response. A response is a stream</span>
            <span class="hljs-comment">// and because we want the browser to consume the response</span>
            <span class="hljs-comment">// as well as the cache consuming the response, we need</span>
            <span class="hljs-comment">// to clone it so we have two streams.</span>
            <span class="hljs-keyword">var</span> responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">cache</span>) </span>&#123;
                cache.put(event.request, responseToCache);
              &#125;);

            <span class="hljs-keyword">return</span> response;
          &#125;
        );
      &#125;)
    );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码做的事情如下：</p>
<ol>
<li>在 <code>fetch</code> 请求上给 <code>.then()</code> 添加回调。</li>
<li>收到响应后，我们会执行以下检查：
<ul>
<li>确保响应有效。</li>
<li>检查响应中的状态为 200。</li>
<li>确保响应类型是 <strong>basic</strong> ，这证明它是来自我们源的请求，意味着第三方资源的请求不会被缓存。</li>
</ul>
</li>
<li>如果通过了检查，克隆响应。这样做的原因是因为响应是一个 <strong>Stream</strong>，所以 <code>body</code> 只能被使用一次。由于我们想要返回响应供浏览器使用，并将其传递给缓存使用，因此我们需要克隆它，以便我们可以将一个发送到浏览器，一个发送到缓存。</li>
</ol>
<h2 data-id="heading-9">更新 Service Worker</h2>
<p>你的 Service Worker 将在某个时间点需要更新。这个时候，您需要执行以下步骤：</p>
<ol>
<li>更新 Service Worker 的 js 文件。当用户打开你的网站时，浏览器会尝试重新下载在后台定义 Service Worker 的脚本文件。如果 Service Worker 文件与当前文件相比只要有一个字节的差异，它就会认为它是新的。</li>
<li>新 Service Worker 将启动并触发 <code>install</code> 事件。</li>
<li>此时旧的 Service Worker 仍在控制当前页面，因此新的 Service Worker 将进入等待状态。</li>
<li>当网站当前打开的页面关闭时，旧的 Service Worker 将被杀死，新的 Service Worker 将接管。</li>
<li>一旦新 service worker 获得控制权，它的 <code>activate</code> 事件就会被触发。</li>
</ol>
<p>activate 回调中会做缓存管理。为何要在 <code>activate</code> 回调中执行此操作？如果在安装步骤中清除任何旧缓存，则控制所有当前页面的任何旧的 Service Worker 将突然停止从该缓存中提供文件。</p>
<p>假设我们有一个名为<code>“my-site-cache-v1”</code>的缓存，我们希望将其拆分为一个页面缓存和一个博客文章缓存。这意味着在安装步骤中，我们将创建两个缓存，<code>“pages-cache-v1”</code>和<code>“blog-posts-cache-v1”</code>，在激活步骤中，我们要删除旧的<code>“my-site-cache-v1“</code>。</p>
<p>以下代码将通过循环访问 Service Worker 中的所有缓存并删除未在缓存许可名单中定义的缓存来执行此操作。</p>
<pre><code class="hljs language-js copyable" lang="js">self.addEventListener(<span class="hljs-string">'activate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;

  <span class="hljs-keyword">var</span> cacheAllowlist = [<span class="hljs-string">'pages-cache-v1'</span>, <span class="hljs-string">'blog-posts-cache-v1'</span>];

  event.waitUntil(
    caches.keys().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">cacheNames</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(
        cacheNames.map(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">cacheName</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (cacheAllowlist.indexOf(cacheName) === -<span class="hljs-number">1</span>) &#123;
            <span class="hljs-keyword">return</span> caches.delete(cacheName);
          &#125;
        &#125;)
      );
    &#125;)
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">常踩的坑</h2>
<h3 data-id="heading-11">如果安装失败，没有提示</h3>
<p>如果 <code>worker</code> 注册了，但没有出现在 <code>chrome://inspect/#service-workers</code> 或 <code>chrome://serviceworker-internals</code> 中，则很可能是因为抛出错误或者将 <code>rejected promise</code> 传递给<code>event.waitUntil()</code> 导致无法安装。</p>
<p>要解决此问题，请转到 <code>chrome://serviceworker-internals</code> 并选中 <strong>“Open DevTools window and pause JavaScript execution on service worker startup for debugging”</strong> ，然后在 <code>install</code> 事件的开始处打断点 <code>debugger</code>，定位问题。</p>
<h3 data-id="heading-12">fetch() 的默认值</h3>
<h4 data-id="heading-13">默认情况下没有凭据</h4>
<p>使用 fetch 时，默认情况下，请求不包含诸如 cookie 之类的凭据。如果需要凭据，请这样调用：</p>
<pre><code class="hljs language-js copyable" lang="js">fetch(url, &#123;
  <span class="hljs-attr">credentials</span>: <span class="hljs-string">'include'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Fetch</code> 的行为更像其他 CORS 请求，例如 <code><img crossorigin></code>，它从不发送 <code>cookie</code>，除非你选择使用 <code><img crossorigin="use-credentials"></code>。</p>
<h4 data-id="heading-14">没有 CORS 默认失败</h4>
<p>默认情况下，如果不支持 CORS，从第三方 URL 获取资源将会失败。可以在请求中添加 <code>no-CORS</code> 选项来解决这个问题，这会导致“不透明”响应，也就是说无法判断响应是否成功。</p>
<pre><code class="hljs language-js copyable" lang="js">cache.addAll(urlsToPrefetch.map(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">urlToPrefetch</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Request(urlToPrefetch, &#123; <span class="hljs-attr">mode</span>: <span class="hljs-string">'no-cors'</span> &#125;);
&#125;)).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'All resources have been fetched and cached.'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">处理响应式图像</h3>
<p><code>srcset</code> 属性或 <code><picture></code> 元素在运行时会选择合适的 <code>image</code> 资源并发送网络请求。</p>
<p>对于 Service Worker，如果你想在 <code>install</code> 步骤中缓存图像，下面有几个选择：</p>
<ol>
<li>安装 <code><picture></code> 元素和 <code>srcset</code> 属性将请求的所有图像；</li>
<li>安装图像的单个低分辨率版本；</li>
<li>安装图像的单个高分辨率版本。</li>
</ol>
<p>实际上，应该选择选项 2 或 3，但下载所有图像会浪费存储空间。</p>
<p>假设在安装时选择低分辨率版本，在页面加载时尝试从网络检索高分辨率图像，如果高分辨率图像失败，则回退到低分辨率版本。这很好，但有一个问题：</p>
<p>如果我们有以下两张图片：</p>




















<table><thead><tr><th>屏幕密度</th><th>Width</th><th>Height</th></tr></thead><tbody><tr><td>1x</td><td>400</td><td>400</td></tr><tr><td>2x</td><td>800</td><td>800</td></tr></tbody></table>
<p>在 <code>srcset</code> 图像中，我们会有一些像这样的标记：</p>
<pre><code class="hljs language-js copyable" lang="js"><img src=<span class="hljs-string">"image-src.png"</span> srcset=<span class="hljs-string">"image-src.png 1x, image-2x.png 2x"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在 2x 显示器上，浏览器将选择下载 image-2x.png，离线的时候如果图片被缓存了，可以在 <code>.catch()</code> 中发送请求并返回 <code>image-src.png</code> ，但是浏览器会考虑到 2x 屏幕上的额外像素的图像，因此图像将显示为 200x200 CSS 像素而不是 400x400 CSS 像素。解决此问题的唯一方法是在图像上设置固定的高度和宽度：</p>
<pre><code class="hljs language-js copyable" lang="js"><img
  src=<span class="hljs-string">"image-src.png"</span>
  srcset=<span class="hljs-string">"image-src.png 1x, image-2x.png 2x"</span>
  style=<span class="hljs-string">"width:400px; height: 400px;"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>ok，当你看到这行文字的时候，证明本篇文章你已阅读完，给你点个赞。如有翻译不周的地方，请指出。</p>
</blockquote></div>  
</div>
            