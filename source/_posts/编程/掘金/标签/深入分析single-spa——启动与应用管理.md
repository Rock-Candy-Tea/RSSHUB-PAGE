
---
title: '深入分析single-spa——启动与应用管理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9f72ae312924db18d1b761aa9078666~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 04:56:04 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9f72ae312924db18d1b761aa9078666~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Application是single-spa中重要的部分，single-spa在运行时，会涉及到应用的注册/取消注册和卸载。本文将对single-spa自身的启动以及其中对应用的管理进行深入分析。</p>
</blockquote>
<h2 data-id="heading-0">single-spa的启动</h2>
<p>首先我们先来看一下single-spa的一段<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsingle-spa.js.org%2Fdocs%2Fconfiguration" target="_blank" rel="nofollow noopener noreferrer" title="https://single-spa.js.org/docs/configuration" ref="nofollow noopener noreferrer">示例代码</a>:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// single-spa-config.js</span>
<span class="hljs-keyword">import</span> &#123; registerApplication, start &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'single-spa'</span>;

<span class="hljs-comment">// Simple usage</span>
registerApplication(
  <span class="hljs-string">'app2'</span>,
  <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'src/app2/main.js'</span>),
  <span class="hljs-function">(<span class="hljs-params">location</span>) =></span> location.pathname.startsWith(<span class="hljs-string">'/app2'</span>),
  &#123; <span class="hljs-attr">some</span>: <span class="hljs-string">'value'</span> &#125;
);

<span class="hljs-comment">// Config with more expressive API</span>
registerApplication(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'app1'</span>,
  <span class="hljs-attr">app</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'src/app1/main.js'</span>),
  <span class="hljs-attr">activeWhen</span>: <span class="hljs-string">'/app1'</span>,
  <span class="hljs-attr">customProps</span>: &#123;
    <span class="hljs-attr">some</span>: <span class="hljs-string">'value'</span>,
  &#125;
&#125;);

start();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，我们可以看到：</p>
<ul>
<li>
<p>single-spa导出了<code>registerApplication</code>和<code>start</code>两个方法</p>
</li>
<li>
<p>start用来启动single-spa应用；在此之前，我们还可以通过registerApplication注册微前端应用，</p>
</li>
<li>
<p>registerApplication用来在single-spa中注册微前端应用，这样single-spa就可以知道应该在何时/如何去初始化、加载、卸载应用</p>
</li>
</ul>
<h3 data-id="heading-1">start</h3>
<p>single-spa的start部分的代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params">opts</span>) </span>&#123;
  started = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">if</span> (opts && opts.urlRerouteOnly) &#123;
    setUrlRerouteOnly(opts.urlRerouteOnly);
  &#125;
  <span class="hljs-keyword">if</span> (isInBrowser) &#123;
    reroute();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里我们可以看到：</p>
<ul>
<li><code>start</code>接受一个opts对象作为参数，其中唯一的配置项为urlReouteOnly；如果设置urlReouteOnly为true，那么<code>history.pushState()</code> 和<code>history.replaceState()</code>将不会触发<code>reroute</code></li>
<li>如果在浏览器环境中，调用<code>start</code>将会触发<code>reroute</code>的执行</li>
</ul>
<h2 data-id="heading-2">应用管理</h2>
<p>single-spa中对于微前端应用的管理，主要涉及到：</p>
<ul>
<li>注册应用，会配置应用名称、激活时机等信息</li>
<li>取消注册应用，在取消注册的时候会卸载对应应用</li>
</ul>
<h3 data-id="heading-3">应用注册——registerApplication</h3>
<h5 data-id="heading-4">执行流程</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9f72ae312924db18d1b761aa9078666~tplv-k3u1fbpfcp-watermark.image" alt="registerApplication.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于registerApplication的使用，我们可以直接去看代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerApplication</span>(<span class="hljs-params">
  appNameOrConfig,
  appOrLoadApp,
  activeWhen,
  customProps
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> registration = sanitizeArguments(
    appNameOrConfig,
    appOrLoadApp,
    activeWhen,
    customProps
  );

  <span class="hljs-keyword">if</span> (getAppNames().indexOf(registration.name) !== -<span class="hljs-number">1</span>)
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(
      formatErrorMessage(
        <span class="hljs-number">21</span>,
        __DEV__ &&
          <span class="hljs-string">`There is already an app registered with name <span class="hljs-subst">$&#123;registration.name&#125;</span>`</span>,
        registration.name
      )
    );

  apps.push(
    assign(
      &#123;
        <span class="hljs-attr">loadErrorTime</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">status</span>: NOT_LOADED,
        <span class="hljs-attr">parcels</span>: &#123;&#125;,
        <span class="hljs-attr">devtools</span>: &#123;
          <span class="hljs-attr">overlays</span>: &#123;
            <span class="hljs-attr">options</span>: &#123;&#125;,
            <span class="hljs-attr">selectors</span>: [],
          &#125;,
        &#125;,
      &#125;,
      registration
    )
  );

  <span class="hljs-keyword">if</span> (isInBrowser) &#123;
    ensureJQuerySupport();
    reroute();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>registerApplication函数接受4个参数：</p>
<ul>
<li><code>appNameOrConfig</code>：应用名称，需要保证全局唯一；如果重复注册相同名称的应用，则会抛出错误</li>
<li><code>appOrLoadApp</code>：应用的定义，用来加载应用，可以是包含single-spa生命周期的对象/加载应用的方法</li>
<li><code>activeWhen</code>：用来匹配应用的函数——activity function或者需要匹配的路径，用来判断应用是否应当被激活</li>
<li><code>customProps</code>：传递给应用的自定义属性</li>
</ul>
<h3 data-id="heading-5">应用取消注册——unregisterApplication</h3>
<p>unregisterApplication是与registerApplication相对的方法，但相对来说简单很多：</p>
<ul>
<li>判断应用是否已经注册过；如果没有注册过，抛出错误</li>
<li>如果已注册过，则调用unloadApplication，并将应用从apps列表中移出</li>
</ul>
<h5 data-id="heading-6">执行流程：</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09ea09a72b554de884edabea1195327f~tplv-k3u1fbpfcp-watermark.image" alt="unregisterApplication.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">代码如下：</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unregisterApplication</span>(<span class="hljs-params">appName</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (apps.filter(<span class="hljs-function">(<span class="hljs-params">app</span>) =></span> toName(app) === appName).length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(
      formatErrorMessage(
        <span class="hljs-number">25</span>,
        __DEV__ &&
          <span class="hljs-string">`Cannot unregister application '<span class="hljs-subst">$&#123;appName&#125;</span>' because no such application has been registered`</span>,
        appName
      )
    );
  &#125;
  <span class="hljs-keyword">return</span> unloadApplication(appName).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> appIndex = apps.map(toName).indexOf(appName);
    apps.splice(appIndex, <span class="hljs-number">1</span>);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">卸载应用——unloadApplication</h3>
<p>在unregisterApplication的最终，将调用unloadApplication。卸载完成的应用，将恢复到NOT_LOADED的状态，下次激活时需要重新加载。</p>
<h4 data-id="heading-9">执行流程</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6bc613f4fbb480ab781e1436d5187e4~tplv-k3u1fbpfcp-watermark.image" alt="unloadApplication.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">源码</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unloadApplication</span>(<span class="hljs-params">appName, opts = &#123; waitForUnmount: <span class="hljs-literal">false</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> appName !== <span class="hljs-string">"string"</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(
      formatErrorMessage(
        <span class="hljs-number">26</span>,
        __DEV__ && <span class="hljs-string">`unloadApplication requires a string 'appName'`</span>
      )
    );
  &#125;
  <span class="hljs-keyword">const</span> app = find(apps, <span class="hljs-function">(<span class="hljs-params">App</span>) =></span> toName(App) === appName);
  <span class="hljs-keyword">if</span> (!app) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(
      formatErrorMessage(
        <span class="hljs-number">27</span>,
        __DEV__ &&
          <span class="hljs-string">`Could not unload application '<span class="hljs-subst">$&#123;appName&#125;</span>' because no such application has been registered`</span>,
        appName
      )
    );
  &#125;

  <span class="hljs-keyword">const</span> appUnloadInfo = getAppUnloadInfo(toName(app));
  <span class="hljs-keyword">if</span> (opts && opts.waitForUnmount) &#123;
    <span class="hljs-comment">// We need to wait for unmount before unloading the app</span>

    <span class="hljs-keyword">if</span> (appUnloadInfo) &#123;
      <span class="hljs-comment">// Someone else is already waiting for this, too</span>
      <span class="hljs-keyword">return</span> appUnloadInfo.promise;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// We're the first ones wanting the app to be resolved.</span>
      <span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        addAppToUnload(app, <span class="hljs-function">() =></span> promise, resolve, reject);
      &#125;);
      <span class="hljs-keyword">return</span> promise;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">/* We should unmount the app, unload it, and remount it immediately.
     */</span>

    <span class="hljs-keyword">let</span> resultPromise;

    <span class="hljs-keyword">if</span> (appUnloadInfo) &#123;
      <span class="hljs-comment">// Someone else is already waiting for this app to unload</span>
      resultPromise = appUnloadInfo.promise;
      immediatelyUnloadApp(app, appUnloadInfo.resolve, appUnloadInfo.reject);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// We're the first ones wanting the app to be resolved.</span>
      resultPromise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        addAppToUnload(app, <span class="hljs-function">() =></span> resultPromise, resolve, reject);
        immediatelyUnloadApp(app, resolve, reject);
      &#125;);
    &#125;

    <span class="hljs-keyword">return</span> resultPromise;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在卸载应用的过程中，我们可以看到如下两个函数的调用：</p>
<ul>
<li><code>addAppToUnload</code>：通过将应用加入到<code>appToUnload</code>中，等待后续处理</li>
<li><code>immediatelyUnloadApp</code>：立即调用生命周期方法中与<code>unmount</code>和<code>unload</code>有关的方法，来卸载应用</li>
</ul>
<h4 data-id="heading-11">addAppToUnload</h4>
<p>通过将需要<code>unload</code>的应用，加入到<code>appToUnload</code>中，等待稍后处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addAppToUnload</span>(<span class="hljs-params">app, promiseGetter, resolve, reject</span>) </span>&#123;
  appsToUnload[toName(app)] = &#123; app, resolve, reject &#125;;
  <span class="hljs-built_in">Object</span>.defineProperty(appsToUnload[toName(app)], <span class="hljs-string">"promise"</span>, &#123;
    <span class="hljs-attr">get</span>: promiseGetter,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">immediatelyUnloadApp</h4>
<p>链式调用<code>toUnmountPromise</code>和<code>toUnloadPromise</code>，来进行应用的卸载</p>
<h5 data-id="heading-13">执行流程</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f224a113d92748318733ff0217f3afed~tplv-k3u1fbpfcp-watermark.image" alt="immediatelyUnloadApp.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">immediatelyUnloadApp</span>(<span class="hljs-params">app, resolve, reject</span>) </span>&#123;
  toUnmountPromise(app)
    .then(toUnloadPromise)
    .then(<span class="hljs-function">() =></span> &#123;
      resolve();
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// reroute, but the unload promise is done</span>
        reroute();
      &#125;);
    &#125;)
    .catch(reject);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">参考资料</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsingle-spa.js.org%2Fdocs%2Fconfiguration%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://single-spa.js.org/docs/configuration/" ref="nofollow noopener noreferrer">Configuration</a></p></div>  
</div>
            