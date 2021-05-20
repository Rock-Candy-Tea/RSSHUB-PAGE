
---
title: 'Service Worker 使用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07129a89209d4d73bdc4341337f06768~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 19:33:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07129a89209d4d73bdc4341337f06768~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>service worker一般用的可能不多，但在很多时候却有着不可替代的作用，现在很多文章都只是对其简要介绍，很多细节部分都没有说明，所以就打算写这篇文章较为全面地聊一聊service worker能做什么，怎么做。</p>
<h3 data-id="heading-0">兼容性</h3>
<p>就目前来说，service worker有着不错的兼容性，除了IE以外的大部分新浏览器都可以较好支持。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07129a89209d4d73bdc4341337f06768~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">如何使用service worker</h3>
<h4 data-id="heading-2">一个基本的service worker脚本</h4>
<p>service worker脚本与普通js脚本的区别主要是因为他们的运行容器不同，在普通页面脚本中，有许多宿主对象可以使用，如与dom相关的<code>window</code>, <code>document</code>等，这些是service worker无法使用的，由于没有<code>window</code>对象，worker中的全局对象变成了<code>self</code>。其次，service worker被设计成完全异步的，所以需要尽量避免在其中使用需要长时间计算的同步逻辑。</p>
<p>service worker具有自己的生命周期状态，在不同的生命周期中可以做不同事情，主要有以下几个：</p>
<ol>
<li>install：准备好缓存等内容</li>
<li>waiting：如果有一个旧版本的service worker在运行，那么会进入waiting状态，等待页面关闭后再打开才会更新service worker版本</li>
<li>activate：表示service worker取得了当前页面的控制权，可以监听fetch和返回缓存等了</li>
</ol>
<p>（在官方的表述中，有installing，installed，activating，activated，redundant几种，但由于它们没有相应的监听事件，所以不使用这种表述）</p>
<p><em>注：service worker 在不用时会被中止，并在下次有需要时重启</em></p>
<p>下面来写一个基本的service worker：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-comment">// Perform install steps</span>
  event.waitUntil(
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">1000</span>);
    &#125;)
  );
&#125;);

self.addEventListener(<span class="hljs-string">'activate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'activate'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>install和activate是service worker中的两个生命周期钩子，这两个生命周期里面要做些什么主要取决于需要通过service worker实现的功能，这些会在下面的【service worker能做什么】部分介绍。</p>
<p>在两个事件中都可以使用<code>event.waitUntil</code>接受一个promise，来告诉浏览器目前还在<code>install</code>或者<code>activate</code>过程中，不要关闭worker，否则worker是有可能在任何时候被关闭的，如上面所示，就表示<code>install</code>过程会持续至少1s。</p>
<h4 data-id="heading-3">注册service worker</h4>
<p>service worker一般通过<code>navigator.serviceWorker.register()</code>来注册，它的用例如下：</p>
<p><em>注：如果你不是在localhost上开发，那么需要https才能使用service worker</em></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">regist</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> registration = <span class="hljs-keyword">await</span> navigator.serviceWorker.register(<span class="hljs-string">'service-worker.js'</span>, &#123;<span class="hljs-attr">scope</span>: <span class="hljs-string">'./'</span>&#125;);
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.error(e);
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>register的第一个参数是脚本文件的路径，第二个参数中的scope（暂时只有这个属性）是这个脚本影响的作用域范围，如果像上面这样写，那么在当前路径/子路径下的页面都会受到影响。如果需要判断一个页面是否受service worker控制，可以检测<code>navigator.serviceWorker.controller</code>这个属性是否为null或者一个service worker实例。</p>
<p>用过web worker的话可能知道对web worker来说，脚本文件不一定是一个真实的文件路径地址，也可以是通过blob url来创建，就像下面这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> content = <span class="hljs-string">"console.log('worker is runningggg!')"</span>;
<span class="hljs-keyword">let</span> url = URL.createObjectURL(<span class="hljs-keyword">new</span> Blob([content], &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">"text/javascript"</span>&#125;));
<span class="hljs-keyword">let</span> worker = <span class="hljs-keyword">new</span> Worker(url);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是service worker不能用这种方式来创建，否则会报错：</p>
<pre><code class="copyable">TypeError: Failed to register a ServiceWorker: The URL protocol of the script ('blob:xxxx') is not supported.
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">更新service worker</h4>
<p>是否更新service worker是首先是由浏览器来决定的，只有当前后两个service worker文件在内容上不同的时候浏览器才会启动新的service worker的install事件。</p>
<p>有几种情况下，页面不会立即通过注册的service worker进行请求：</p>
<ol>
<li>第一次注册service worker时，即使service worker已经activate，页面的请求也不会通过worker，只有在刷新页面后才会通过service worker代理请求</li>
<li>当页面存在旧版本的service worker，那么install过后会进入waiting状态，新的service worker会在重新打开页面后（注意不是刷新页面）生效</li>
<li>同一个scope中已打开的其它页面，在刷新之前不会受控于service worker</li>
</ol>
<p>在第二种情况下，可以通过<code>self.skipWaiting()</code>来跳过waiting，这样的话每次更新service worker文件浏览器都会第一时间激活新的worker，无论有没有重新打开页面，<code>self.skipWaiting()</code>可以放在任何地方，不过一般会把它放在install事件里面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  self.skipWaiting();
  event.waitUntil(
    <span class="hljs-comment">// do something</span>
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，以上只是激活了service worker，激活不等于能够使用，如果不刷新页面还是不能使用的，如果不想刷新页面（第一、三种情况），可以在service worker中使用clients.claim()替换这种默认行为，如果像下面这样写，那么service worker在activate之后立即生效：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.addEventListener(<span class="hljs-string">'activate'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  event.waitUntil(clients.claim());
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这些页面中没有显式调用register，如果需要在这些页面中知道新的service worker被激活，那么可以监听<code>controllerchange</code>事件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">navigator.serviceWorker.addEventListener(<span class="hljs-string">'controllerchange'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(e))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">service worker工作流程</h4>
<p>将注册和更新过程整合就可以得到完整的service worker工作流程，因为一直没有找到比较详细的service worker整体流程图，所以自己画了一个，有错误还请指出。</p>
<p>有一点需要注意，对于service worker脚本文件，它的http缓存规则与普通文件有所不同，如果设置了强缓存，并且max-age设置小于24小时，那么与普通http缓存无异，但是如果max-age大于24小时，那么service worker文件会在24小时之后强制更新。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ab4291f92f8460d95462d492bf203b7~tplv-k3u1fbpfcp-watermark.image" alt="service worker流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">与页面间的通信</h4>
<p>由于service worker挂载在<code>navigator.serviceWorker.controller</code>上，所以可以通过它与service worker进行通讯，方法是与web worker相同的postMessage，而在service worker中则是使用self.clients获取受控的页面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">navigator.serviceWorker.controller.postMessage(<span class="hljs-string">'hello'</span>);
navigator.serviceWorker.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(e.data);
&#125;)

<span class="hljs-comment">// sw.js</span>
self.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(e);
  <span class="hljs-comment">// 向特定窗口返回消息</span>
  e.source.postMessage(<span class="hljs-string">'response from service worker'</span>)
&#125;);

<span class="hljs-comment">// 向全部窗口发送消息</span>
(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> cls = <span class="hljs-keyword">await</span> self.clients.matchAll();
  cls.forEach(<span class="hljs-function"><span class="hljs-params">cl</span> =></span> cl.postMessage(<span class="hljs-string">'message from service worker'</span>));
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与其它地方的postMessage类似，也可以通过MessageChannel进行通讯：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> MessageChannel();
navigator.serviceWorker.controller.postMessage(<span class="hljs-string">'hello'</span>, [channel.port1]);
channel.port2.onmessge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(e.data); &#125;

<span class="hljs-comment">// sw.js</span>
self.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
  e.ports[<span class="hljs-number">0</span>].postMessage(<span class="hljs-string">'message from service worker'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">service worker能做什么：缓存</h3>
<p>service worker强大的缓存功能主要来自于它能够拦截全局的fetch事件，以及能在后台运行的能力等。</p>
<p>既然能够拦截fetch事件，那很容易想到的就是可以把关于浏览器请求的处理都放在一处，也就很大程度上方便了缓存管理，并且由于service worker可以离线使用，使得它成为了PWA的基础。</p>
<p>下面介绍一下如何使用service worker管理缓存</p>
<h4 data-id="heading-8">管理缓存</h4>
<p>service worker的缓存能力主要与<code>self.caches</code>对象有关，这是一个CacheStorage对象，在普通页面中也可以使用，但是一般用在service worker中，同样的，CacheStorage只能用在https环境中。</p>
<p>如果预先知道需要缓存什么内容，可以使用<code>caches.addAll()</code>来预先缓存内容，如果像下面这样写，那么会在service worker安装的时候缓存<code>test.jpg</code>这个文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.addEventListener(<span class="hljs-string">'install'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  event.waitUntil(
    caches.open(<span class="hljs-string">'v1'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">cache</span>) </span>&#123;
      <span class="hljs-keyword">return</span> cache.addAll([
        <span class="hljs-string">'/test.jpg'</span>,
      ]);
    &#125;)
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后便可以通过拦截<code>fetch</code>事件来使用缓存了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  event.respondWith(
    caches.match(event.request).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
      <span class="hljs-keyword">return</span> response || fetch(event.request);
    &#125;)
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面这种情况下，<code>test.jpg</code>会从缓存中返回，而其它文件则会从网络下载，但在一些情况下我们不能预知需要缓存的内容，第一次请求之后进行缓存，与<code>caches.addAll()</code>不同，<code>caches.put()</code>可以手动将内容放入缓存中，需要注意的是，由于fetch所获得的response内容的读取是一次性的，而实际上我们把response返回给了页面，还把它放入了缓存中，所以要使用<code>response.clone()</code>创建两个相同的response：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.addEventListener(<span class="hljs-string">'fetch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  event.respondWith(
    caches.match(event.request).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resp</span>) </span>&#123;
      <span class="hljs-keyword">return</span> resp || fetch(event.request).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
        <span class="hljs-keyword">return</span> caches.open(<span class="hljs-string">'v1'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">cache</span>) </span>&#123;
          cache.put(event.request, response.clone());
          <span class="hljs-keyword">return</span> response;
        &#125;);
      &#125;);
    &#125;)
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">缓存的更新</h4>
<p>由于caches是可以分版本的，所以在更新了新的缓存列表后可以将旧的删除，这一是为了避免缓存混乱，二是为了减少缓存空间占用，每个浏览器都有自己的磁盘空间限制，在容量超出的时候，为了内容的一致性，浏览器一般会删除域下面的所有数据。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> currentCacheVersion = <span class="hljs-string">'v2'</span>;

self.addEventListener(<span class="hljs-string">'activate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  event.waitUntil(
    caches.keys().then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">keyList</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(keyList.map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">key</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (key !== currentCacheVersion) &#123;
          <span class="hljs-keyword">return</span> caches.delete(key);
        &#125;
      &#125;));
    &#125;)
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">手动构建Response</h4>
<p>上面所示的response都是通过fetch获的，实际上也可以手动构建Response，这给开发者带来了很大的灵活性，例如在返回缓存时修改header信息等，这里不详细介绍，可以参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Response" target="_blank" rel="nofollow noopener noreferrer">MDN</a>。</p>
<h3 data-id="heading-11">service worker能做什么：后台同步</h3>
<p>这个功能移动端可能应用场景会更多，并且对大部分应用场景来说这或许是一个锦上添花的功能，并且兼容性不是很好：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c94de344e3b40eb83e6a0c2e0689f90~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到只有chromium系的浏览器支持后台同步</p>
<h4 data-id="heading-12">后台同步(Background Sync)能做什么</h4>
<p>后台同步主要为了将网络请求与页面分离，在用户关闭页面后也可以继续请求，比方说一个请求了很长列表的页面，当列表还未加载完的时候用户就关闭了页面，那么下次打开的时候又需要重新加载，这时就可以使用后台同步。</p>
<p>后台同步分为几个部分</p>
<ol>
<li>service worker中监听<code>sync</code>事件</li>
<li>页面向service worker发送<code>sync</code>请求</li>
<li>在service worker中触发<code>sync</code>事件回调函数，然后进行请求</li>
</ol>
<p>下面是一个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">navigator.serviceWorker.register(<span class="hljs-string">'/sw.js'</span>);

navigator.serviceWorker.ready.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">swRegistration</span>) </span>&#123;
  <span class="hljs-keyword">return</span> swRegistration.sync.register(<span class="hljs-string">'sync-user-list'</span>);
&#125;);

<span class="hljs-comment">// sw.js</span>
self.addEventListener(<span class="hljs-string">'sync'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (event.tag == <span class="hljs-string">'sync-user-list'</span>) &#123;
    event.waitUntil(fetch(<span class="hljs-string">'./sync?type=userlist'</span>));
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意要将返回Promise放入<code>event.waitUntil</code>中，好让浏览器知道什么时候请求完成。</p>
<h4 data-id="heading-13">同步的数据如何使用</h4>
<p>同步后的数据可以通过多种途径来使用，例如：</p>
<ol>
<li>通过postMessage发送回页面</li>
<li>通过Notification给用户发送通知</li>
<li>通过一些变量/indexDB存储同步回来的结果(service worker无法使用localStorage等同步存储方式)</li>
</ol>
<p>以第一种为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">navigator.serviceWorker.register(<span class="hljs-string">'/sw.js'</span>);

navigator.serviceWorker.ready.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">swRegistration</span>) </span>&#123;
  <span class="hljs-keyword">return</span> swRegistration.sync.register(<span class="hljs-string">'sync-user-list'</span>);
&#125;);

navigator.serviceWorker.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
  <span class="hljs-keyword">const</span> content = e.data;
&#125;)

<span class="hljs-comment">// sw.js</span>
self.addEventListener(<span class="hljs-string">'sync'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (event.tag == <span class="hljs-string">'sync-user-list'</span>) &#123;
    event.waitUntil(fetch(<span class="hljs-string">'./sync?type=userlist'</span>).then(<span class="hljs-keyword">async</span> res => &#123;
      <span class="hljs-keyword">const</span> content = <span class="hljs-keyword">await</span> res.text();
      <span class="hljs-keyword">return</span> clients.matchAll().then(<span class="hljs-function"><span class="hljs-params">cls</span> =></span> cls[<span class="hljs-number">0</span>].postMessage(content));
    &#125;));
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以第二种为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">navigator.serviceWorker.register(<span class="hljs-string">'/sw.js'</span>);

navigator.serviceWorker.ready.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">swRegistration</span>) </span>&#123;
  <span class="hljs-keyword">return</span> swRegistration.sync.register(<span class="hljs-string">'sync-user-list'</span>);
&#125;);

<span class="hljs-comment">// sw.js</span>
self.addEventListener(<span class="hljs-string">'sync'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (event.tag == <span class="hljs-string">'sync-user-list'</span>) &#123;
    event.waitUntil(fetch(<span class="hljs-string">'./sync?type=userlist'</span>).then(<span class="hljs-keyword">async</span> res => &#123;
      <span class="hljs-keyword">const</span> content = <span class="hljs-keyword">await</span> res.text();
      self.registration.showNotification(content);
    &#125;));
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">service worker能做什么：Web Push</h3>
<p>web push是一种浏览器后台推送通知的方法，它可以实现在关闭页面后继续推送通知的功能原理是通过浏览器的推送服务器向用户推送消息，看看它的兼容性怎么样：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b97af6cc225f4884848065ef99d4e9a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里特意把一些国内的手机浏览器也放了进来，可以看到，safari是不支持的，但是几个国内的移动端浏览器都支持，需要注意的是，如果使用的是Chrome，那么推送服务使用的是Google的<a href="https://firebase.google.cn/" target="_blank" rel="nofollow noopener noreferrer">FCM</a>，这个服务国内应该是无法使用的。</p>
<p>这一部分不详细介绍了，在Google Developers上有<a href="https://developers.google.com/web/fundamentals/push-notifications" target="_blank" rel="nofollow noopener noreferrer">一篇</a>比较详细的介绍，如果有空的话我可能也会写一篇相关的文章。</p>
<h3 data-id="heading-15">DevTools</h3>
<p>由于service worker的特性，相比于页面脚本它不是那么好开发调试，下面介绍两个开发的小方法。</p>
<h4 data-id="heading-16">调试</h4>
<p>如果使用chrome，可以在chrome://inspect/#service-workers 中点击相应service worker的inspect，即可调试</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c8768eea08f401fb0845b625eb17545~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">service worker自动更新</h4>
<p>上面说到，在service worker文件更新了之后要关闭页面重新打开才能生效，为了避免这个麻烦，可以在开发代码中加入<code>skipWaitinig()</code>和<code>clients.claim()</code>，或者在DevTools的Applcation标签页选上<code>Update on reload</code>，这样每次刷新页面就会自动激活新的service worker。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/792768c189184f42879da429e2d898b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">工程化</h3>
<p>由于目前的前端工程几乎都用打包工具进行构建，而service worker一般都要作为一个单独的文件来引入，所以可以在构建工具中做一些配置：</p>
<p>例如使用webpack构建：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
<span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-string">'app'</span>: <span class="hljs-string">"./src/index.js"</span>,
    <span class="hljs-string">'service-worker'</span>: <span class="hljs-string">"./src/service-worker.ts"</span>,
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外也有一些工具与service worker相关：</p>
<p><a href="https://github.com/NekR/offline-plugin" target="_blank" rel="nofollow noopener noreferrer">offline-plugin</a></p>
<p><a href="https://github.com/oliviertassinari/serviceworker-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">serviceworker-webpack-plugin</a> 已Archived</p>
<p>由于这些工具我没怎么用过，所以就不介绍了。</p></div>  
</div>
            