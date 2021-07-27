
---
title: '深入分析single-spa——事件机制'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79e1d2b7add14fd7b4f723e17d0cc4a7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 06:12:53 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79e1d2b7add14fd7b4f723e17d0cc4a7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">single-spa中的事件</h2>
<blockquote>
<p>在之前关于<a href="https://juejin.cn/post/6988825809830035487" target="_blank" title="https://juejin.cn/post/6988825809830035487">navigation-events和reroute</a>的分享中，其实有很多的事件触发，在这里就single-spa中的事件作进一步的展开介绍。在路由导航的不同阶段以及应用的不同状态处理中，single-spa会派发不同的事件；通过对这些事件的理解和处理，我们可以增加一些自定义的功能。</p>
</blockquote>
<p>在single-spa中，事件大致分为如下两类：</p>
<h3 data-id="heading-1">原生事件</h3>
<p>在navigation-events中，single-spa实现了对于浏览器的路由导航事件的监听：</p>
<ul>
<li>popstate</li>
<li>hashchange</li>
<li>pushstate</li>
<li>replacestate</li>
</ul>
<h3 data-id="heading-2">自定义的popstate事件</h3>
<p>single-spa对于原生的<code>popstate</code>事件增加了一些自定义的属性：</p>
<ul>
<li>singleSpa：标示该popstate事件由single-spa触发</li>
<li>singleSpaTrigger：标示该popstate事件触发的原始方法名</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPopStateEvent</span>(<span class="hljs-params">state, originalMethodName</span>) </span>&#123;
  <span class="hljs-keyword">let</span> evt;
  <span class="hljs-keyword">try</span> &#123;
    evt = <span class="hljs-keyword">new</span> PopStateEvent(<span class="hljs-string">"popstate"</span>, &#123; state &#125;);
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    evt = <span class="hljs-built_in">document</span>.createEvent(<span class="hljs-string">"PopStateEvent"</span>);
    evt.initPopStateEvent(<span class="hljs-string">"popstate"</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">false</span>, state);
  &#125;
  <span class="hljs-comment">// 给原生popstate事件增加singleSpa和singleSpaTrigger属性</span>
  evt.singleSpa = <span class="hljs-literal">true</span>;
  evt.singleSpaTrigger = originalMethodName;
  <span class="hljs-keyword">return</span> evt;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">触发时机</h3>
<p>该方法会在如下方法调用的时候被触发：</p>
<ul>
<li>history.pushState</li>
<li>history.replaceState</li>
<li>triggerAppChange等可能触发callCapturedEventListeners的single-spa自定义方法</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79e1d2b7add14fd7b4f723e17d0cc4a7~tplv-k3u1fbpfcp-watermark.image" alt="popstate触发流程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以监听<code>popstate</code>事件，来判断该事件是否由single-spa触发：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这是官方文档中的一段代码</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function"><span class="hljs-params">evt</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (evt.singleSpa) &#123;
    <span class="hljs-built_in">console</span>.log(
      <span class="hljs-string">'This event was fired by single-spa to forcibly trigger a re-render'</span>,
    );
    <span class="hljs-built_in">console</span>.log(evt.singleSpaTrigger); <span class="hljs-comment">// pushState | replaceState</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'This event was fired by native browser behavior'</span>);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">自定义事件(Custom Events)</h3>
<p>在核心方法——reroute的执行中，single-spa会触发一系列的自定义事件，其固定的事件名称格式为：<code>single-spa:event-name</code>。对于这些自定义事件的入参，single-spa通过getCustomEventDetail方法进行封装，提供了统一的事件接口。</p>
<ul>
<li>事件封装与派发</li>
</ul>
<p>single-spa对于自定义事件的封装，是基于一个名为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebmodules%2Fcustom-event" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webmodules/custom-event" ref="nofollow noopener noreferrer">custom-event</a>的库实现的，这个库实现了跨浏览器的自定义事件支持；创建的事件，则通过<code>window.dispatchEvent</code>来进行派发，类似：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.dispatchEvent(<span class="hljs-string">'single-spa:event-name'</span>, <span class="hljs-keyword">new</span> CustomEvent(<span class="hljs-comment">/* */</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于Custom-Event的更多信息，可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCustomEvent" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent" ref="nofollow noopener noreferrer">MDN CustomEvent</a>.</p>
<ul>
<li>事件监听</li>
</ul>
<p>这些事件，我们都可以当做浏览器的原生事件，通过事件监听的方式进行处理：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'single-spa:event-name'</span>, <span class="hljs-comment">/* 回调函数，入参即为custom event detail */</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">事件列表</h4>













































<table><thead><tr><th>事件顺序</th><th>事件名称</th><th>触发时机</th></tr></thead><tbody><tr><td>1</td><td><code>single-spa:before-app-change</code> / <code>single-spa:before-no-app-change</code></td><td>进入reroute方法时，根据发生改变的应用数量触发；与事件顺序6对应</td></tr><tr><td>2</td><td><code>single-spa:before-routing-event</code></td><td>每次 reroute 开始一定会发生，与事件7对应</td></tr><tr><td>3</td><td><code>single-spa:before-mount-routing-event</code></td><td>url 发行改变后，旧的应用卸载完毕后，触发该事件，表示后续要开始加载应用</td></tr><tr><td>4</td><td><code>single-spa:before-first-mount</code></td><td>在某个应用第一次 mount 应用之前触发该事件；<strong>该事件只会触发一次，定义在<code>mount.js</code>中</strong></td></tr><tr><td>5</td><td><code>single-spa:first-mount</code></td><td>在某个应用第一次 mount 应用之后触发该事件；<strong>该事件只会触发一次，该定义在<code>mount.js</code>中</strong></td></tr><tr><td>6</td><td><code>single-spa:app-change</code> / <code>single-spa:no-app-change</code></td><td>与事件顺序1对应</td></tr><tr><td>7</td><td><code>single-spa:routing-event</code></td><td>与事件 2 对应，发生在 reroute 结束</td></tr></tbody></table>
<h4 data-id="heading-6">自定义事件触发流程</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a10786ca00d243c69bab9d45c56611dd~tplv-k3u1fbpfcp-watermark.image" alt="Custom Events流程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">获取事件详情——getCustomEventDetail</h4>
<p>single-spa中，通过该方法实现了对于Custom Events的事件详情的统一封装，具体实现如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCustomEventDetail</span>(<span class="hljs-params">isBeforeChanges = <span class="hljs-literal">false</span>, extraProperties</span>) </span>&#123;
    <span class="hljs-keyword">const</span> newAppStatuses = &#123;&#125;;
    <span class="hljs-keyword">const</span> appsByNewStatus = &#123;
      <span class="hljs-comment">// for apps that were mounted</span>
      [MOUNTED]: [],
      <span class="hljs-comment">// for apps that were unmounted</span>
      [NOT_MOUNTED]: [],
      <span class="hljs-comment">// apps that were forcibly unloaded</span>
      [NOT_LOADED]: [],
      <span class="hljs-comment">// apps that attempted to do something but are broken now</span>
      [SKIP_BECAUSE_BROKEN]: [],
    &#125;;

    <span class="hljs-keyword">if</span> (isBeforeChanges) &#123;
      appsToLoad.concat(appsToMount).forEach(<span class="hljs-function">(<span class="hljs-params">app, index</span>) =></span> &#123;
        addApp(app, MOUNTED);
      &#125;);
      appsToUnload.forEach(<span class="hljs-function">(<span class="hljs-params">app</span>) =></span> &#123;
        addApp(app, NOT_LOADED);
      &#125;);
      appsToUnmount.forEach(<span class="hljs-function">(<span class="hljs-params">app</span>) =></span> &#123;
        addApp(app, NOT_MOUNTED);
      &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
      appsThatChanged.forEach(<span class="hljs-function">(<span class="hljs-params">app</span>) =></span> &#123;
        addApp(app);
      &#125;);
    &#125;

    <span class="hljs-keyword">const</span> result = &#123;
      <span class="hljs-attr">detail</span>: &#123;
        <span class="hljs-comment">// 应用状态哈希，key为应用名称，value为应用状态  </span>
        newAppStatuses,
        <span class="hljs-comment">// 各状态对应的应用哈希，key为应用状态，value为对应状态的应用列表</span>
        appsByNewStatus,
        <span class="hljs-comment">// 状态改变的应用列表数量</span>
        <span class="hljs-attr">totalAppChanges</span>: appsThatChanged.length,
        <span class="hljs-comment">// 初始事件信息</span>
        <span class="hljs-attr">originalEvent</span>: eventArguments?.[<span class="hljs-number">0</span>],
        <span class="hljs-comment">// 原本的url地址</span>
        oldUrl,
        <span class="hljs-comment">// 导航到的url地址</span>
        newUrl,
        <span class="hljs-comment">// 导航是否已取消</span>
        navigationIsCanceled,
      &#125;,
    &#125;;

    <span class="hljs-keyword">if</span> (extraProperties) &#123;
      assign(result.detail, extraProperties);
    &#125;

    <span class="hljs-keyword">return</span> result;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addApp</span>(<span class="hljs-params">app, status</span>) </span>&#123;
      <span class="hljs-keyword">const</span> appName = toName(app);
      status = status || getAppStatus(appName);
      newAppStatuses[appName] = status;
      <span class="hljs-keyword">const</span> statusArr = (appsByNewStatus[status] =
        appsByNewStatus[status] || []);
      statusArr.push(appName);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">自定义事件的使用</h4>
<h4 data-id="heading-9">实例场景</h4>
<ul>
<li>取消导航</li>
</ul>
<p>在<code>single-spa:before-routing-event</code>中，传递了<code>cancelNavigation</code>方法作为该事件的入参，调用该方法即可取消该次routing:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// route.js</span>
<span class="hljs-built_in">window</span>.dispatchEvent(
  <span class="hljs-keyword">new</span> CustomEvent(
    <span class="hljs-string">"single-spa:before-routing-event"</span>,
      getCustomEventDetail(<span class="hljs-literal">true</span>, &#123; cancelNavigation &#125;)
  )
);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancelNavigation</span>(<span class="hljs-params"></span>) </span>&#123;
  navigationIsCanceled = <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这是官方文档中的一段代码；如果监听该事件，并且调用了cancelNavigation，就可以取消这次导航</span>
<span class="hljs-built_in">window</span>.addEventListener(
  <span class="hljs-string">'single-spa:before-routing-event'</span>,
  <span class="hljs-function">(<span class="hljs-params">&#123; detail: &#123; oldUrl, newUrl, cancelNavigation &#125; &#125;</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (
      <span class="hljs-keyword">new</span> URL(oldUrl).pathname === <span class="hljs-string">'/route1'</span> &&
      <span class="hljs-keyword">new</span> URL(newUrl).pathname === <span class="hljs-string">'/route2'</span>
    ) &#123;
      cancelNavigation();
    &#125;
  &#125;,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 调用cancelNavigation会设置navigationIsCanceled = false，从而结束这次routing, 并导航回到之前的url</span>
<span class="hljs-keyword">if</span> (navigationIsCanceled) &#123;
  <span class="hljs-built_in">window</span>.dispatchEvent(
    <span class="hljs-keyword">new</span> CustomEvent(
      <span class="hljs-string">"single-spa:before-mount-routing-event"</span>,
        getCustomEventDetail(<span class="hljs-literal">true</span>)
    )
  );
  finishUpAndReturn();
  navigateToUrl(oldUrl);
  <span class="hljs-keyword">return</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在基于single-spa封装的知名微前端框架——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Fqiankun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/qiankun" ref="nofollow noopener noreferrer">qiankun</a>中，也基于一些事件做了自定义的处理：</p>
<ul>
<li>设置默认mount的微前端应用</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 参考https://qiankun.umijs.org/zh/api#setdefaultmountappapplink</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setDefaultMountApp</span>(<span class="hljs-params">defaultAppLink: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'single-spa:no-app-change'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listener</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> mountedApps = getMountedApps();
    <span class="hljs-keyword">if</span> (!mountedApps.length) &#123;
      navigateToUrl(defaultAppLink);
    &#125;

    <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'single-spa:no-app-change'</span>, listener);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果要在微前端应用加载后做监测/埋点，或者需要对微前端实行prefetch</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 参考https://qiankun.umijs.org/zh/api#runafterfirstmountedeffect</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runAfterFirstMounted</span>(<span class="hljs-params">effect: () => <span class="hljs-keyword">void</span></span>) </span>&#123;
  <span class="hljs-comment">// can not use addEventListener once option for ie support</span>
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'single-spa:first-mount'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listener</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'development'</span>) &#123;
      <span class="hljs-built_in">console</span>.timeEnd(firstMountLogLabel);
    &#125;
    effect();
    <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'single-spa:first-mount'</span>, listener);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 如果在start的参数中配置了prefetch, 或者手动调用prefetchApps等方法，则会触发prefetchAfterFirstMounted</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prefetchAfterFirstMounted</span>(<span class="hljs-params">apps: AppMetadata[], opts?: ImportEntryOpts</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'single-spa:first-mount'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">listener</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> notLoadedApps = apps.filter(<span class="hljs-function">(<span class="hljs-params">app</span>) =></span> getAppStatus(app.name) === NOT_LOADED);
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'development'</span>) &#123;
      <span class="hljs-keyword">const</span> mountedApps = getMountedApps();
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[qiankun] prefetch starting after <span class="hljs-subst">$&#123;mountedApps&#125;</span> mounted...`</span>, notLoadedApps);
    &#125;
    notLoadedApps.forEach(<span class="hljs-function">(<span class="hljs-params">&#123; entry &#125;</span>) =></span> prefetch(entry, opts));
    <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'single-spa:first-mount'</span>, listener);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">参考资料</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsingle-spa.js.org%2Fdocs%2Fapi%2F%23events" target="_blank" rel="nofollow noopener noreferrer" title="https://single-spa.js.org/docs/api/#events" ref="nofollow noopener noreferrer">Events</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebmodules%2Fcustom-event" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webmodules/custom-event" ref="nofollow noopener noreferrer">custom-event</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Fqiankun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/qiankun" ref="nofollow noopener noreferrer">qiankun</a></p></div>  
</div>
            