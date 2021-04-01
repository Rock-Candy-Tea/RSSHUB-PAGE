
---
title: '微前端 之 icestark 源码阅读'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1bb8f3d72c4f5f8dc8a0ade9abeccf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 17:01:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1bb8f3d72c4f5f8dc8a0ade9abeccf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、前言</h3>
<p>在之前<a href="https://juejin.cn/post/6869531594818846733" target="_blank">《微前端探索》</a>文章中，我们分析了微前端框架 single-spa 和 qiankun 的一些源码、原理等，本文再对社区另外一个微前端框架 icestark 做一个简单整理分析，帮助各位想探索微前端的同学有个感性的认识。</p>
<h3 data-id="heading-1">二、 源码目录</h3>
<p>icestark 源码的主要目录结构如下所示，主要包括 packages 和 src 两个目录，相关总结整理如下，我们不会一行一行去讲解代码，如果你对某一块很感兴趣，可以自己去 github 上面 clone 代码库，源码还是非常简单易懂的。</p>
<p><img alt="123.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1bb8f3d72c4f5f8dc8a0ade9abeccf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">三、重要代码整理</h3>
<h4 data-id="heading-3">1、子应用状态管理</h4>
<p>我们学习 single-spa 的时候总结到 single-spa 是一个状态机，负责管理各个子应用的状态。所以 icestark 必然存在这个子应用的状态管理，相关的实现在 src/apps.ts 文件中，其包括以下几个主要过程/方法：</p>
<ul>
<li>registerMicroApp：注册子应用的方法，将子应用添加到全局 microApps 数组变量中；</li>
<li>createMicroApp：创建子应用的方法，包括加载子应用的资源等；</li>
<li>mountMicroApp：挂载子应用的方法，将子应用挂载到容器中；</li>
<li>unmountMicroApp：卸载子应用的方法，将子应用从容器中卸载；</li>
<li>unloadMicroApp：unload 子应用的方法，包括移除子应用的资源等；</li>
<li>removeMicroApp：移除子应用的方法，将子应用从全局 microApps 数组中移除；</li>
</ul>
<p>以上方法实现的思路还是比较简单的，定义个全局 microApps 数组变量来保存子应用，然后每个子应用分别有个对应的 status 变量来表示该子应用的状态是怎样的，然后进行下一步操作时会根据当前的状态进行对应的下一步操作，以下我们挑选个最“复杂”的方法 createMicroApp 来看下，我们对代码进行了相关注释，还是比较简单的，就不再赘述了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createMicroApp</span>(<span class="hljs-params">app: string | AppConfig, appLifecyle?: AppLifecylceOptions</span>) </span>&#123;
  <span class="hljs-keyword">const</span> appConfig = getAppConfigForLoad(app, appLifecyle);
  <span class="hljs-keyword">const</span> appName = appConfig && appConfig.name;

  <span class="hljs-keyword">if</span> (appConfig && appName) &#123;
    <span class="hljs-keyword">if</span> (appConfig.status === NOT_LOADED || appConfig.status === LOAD_ERROR ) &#123;
      <span class="hljs-comment">// 如果该子应用的当前状态是未加载或加载失败，执行以下逻辑</span>
      <span class="hljs-keyword">if</span> (appConfig.title) <span class="hljs-built_in">document</span>.title = appConfig.title;
      <span class="hljs-comment">// 更新子应用的状态</span>
      updateAppConfig(appName, &#123; <span class="hljs-attr">status</span>: LOADING_ASSETS &#125;);
      <span class="hljs-keyword">let</span> lifeCycle: ModuleLifeCycle = &#123;&#125;;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 加载子应用资源</span>
        lifeCycle = <span class="hljs-keyword">await</span> loadAppModule(appConfig);
        <span class="hljs-comment">// in case of app status modified by unload event</span>
        <span class="hljs-keyword">if</span> (getAppStatus(appName) === LOADING_ASSETS) &#123;
          <span class="hljs-comment">// 更新子应用配置</span>
          updateAppConfig(appName, &#123; ...lifeCycle, <span class="hljs-attr">status</span>: NOT_MOUNTED &#125;);
        &#125;
      &#125; <span class="hljs-keyword">catch</span> (err)&#123;
        <span class="hljs-comment">// 出错，更新子应用配置</span>
        updateAppConfig(appName, &#123; <span class="hljs-attr">status</span>: LOAD_ERROR &#125;);
      &#125;
      <span class="hljs-keyword">if</span> (lifeCycle.mount) &#123;
        <span class="hljs-comment">// 进行子应用挂载</span>
        <span class="hljs-keyword">await</span> mountMicroApp(appConfig.name);
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (appConfig.status === UNMOUNTED) &#123;
      <span class="hljs-comment">// 如果当前的子应用是卸载状态执行以下逻辑</span>
      <span class="hljs-keyword">if</span> (!appConfig.cached) &#123;
        <span class="hljs-comment">// 加载 js/css 资源</span>
        <span class="hljs-keyword">await</span> loadAndAppendCssAssets(appConfig.appAssets || &#123; <span class="hljs-attr">cssList</span>: [], <span class="hljs-attr">jsList</span>: []&#125;);
      &#125;
      <span class="hljs-comment">// 进行挂载</span>
      <span class="hljs-keyword">await</span> mountMicroApp(appConfig.name);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (appConfig.status === NOT_MOUNTED) &#123;
      <span class="hljs-comment">// 如果当前的子应用是没有挂载状态，则进行挂载</span>
      <span class="hljs-keyword">await</span> mountMicroApp(appConfig.name);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.info(<span class="hljs-string">`[icestark] current status of app <span class="hljs-subst">$&#123;appName&#125;</span> is <span class="hljs-subst">$&#123;appConfig.status&#125;</span>`</span>);
    &#125;
    <span class="hljs-comment">// 返回创建的子应用的信息</span>
    <span class="hljs-keyword">return</span> getAppConfig(appName);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[icestark] fail to get app config of <span class="hljs-subst">$&#123;appName&#125;</span>`</span>);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2、路由劫持</h4>
<p>我们都知道 react、vue、angular 等单应用路由劫持的实现都是：history 路由通过监听 popstate 事件、hash 路由通过监听 hashchange 路由来实现的，那么 icestark 的路由劫持是怎么做的呢，嗯哼，他们也没有变出花来，也是一样的实现原理，代码位置在 src/start.js 文件中，相关源码如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> hijackHistory = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-comment">// 监听对应的路由事件，urlChange 为事件回调函数</span>
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, urlChange, <span class="hljs-literal">false</span>);
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, urlChange, <span class="hljs-literal">false</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"></h4>
<h4 data-id="heading-6">3、沙箱隔离</h4>
<p>在微前端容器中，存在多个子应用共有一个 window 对象的情况，如果不进行隔离，可能多个子应用之间会存在互相影响的情况。icestark 基于 Proxy 为每个子应用启用了一个沙箱环境，代码位置在 packages/icestark-sandbox/src/index.js 文件中，相关代码实现如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">createProxySandbox</span>(<span class="hljs-params">injection?: object</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; propertyAdded, originalValues, multiMode &#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">const</span> proxyWindow = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>) <span class="hljs-keyword">as</span> Window;
    <span class="hljs-keyword">const</span> originalWindow = <span class="hljs-built_in">window</span>;
    <span class="hljs-keyword">const</span> originalAddEventListener = <span class="hljs-built_in">window</span>.addEventListener;
    <span class="hljs-keyword">const</span> originalRemoveEventListener = <span class="hljs-built_in">window</span>.removeEventListener;
    <span class="hljs-keyword">const</span> originalSetInerval = <span class="hljs-built_in">window</span>.setInterval;
    <span class="hljs-keyword">const</span> originalSetTimeout = <span class="hljs-built_in">window</span>.setTimeout;

    <span class="hljs-comment">// hijack addEventListener</span>
    proxyWindow.addEventListener = <span class="hljs-function">(<span class="hljs-params">eventName, fn, ...rest</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> listeners = <span class="hljs-built_in">this</span>.eventListeners[eventName] || [];
      listeners.push(fn);
      <span class="hljs-keyword">return</span> originalAddEventListener.apply(originalWindow, [eventName, fn, ...rest]);
    &#125;;
    <span class="hljs-comment">// hijack removeEventListener</span>
    proxyWindow.removeEventListener = <span class="hljs-function">(<span class="hljs-params">eventName, fn, ...rest</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> listeners = <span class="hljs-built_in">this</span>.eventListeners[eventName] || [];
      <span class="hljs-keyword">if</span> (listeners.includes(fn)) &#123;
        listeners.splice(listeners.indexOf(fn), <span class="hljs-number">1</span>);
      &#125;
      <span class="hljs-keyword">return</span> originalRemoveEventListener.apply(originalWindow, [eventName, fn, ...rest]);
    &#125;;
    <span class="hljs-comment">// hijack setTimeout</span>
    proxyWindow.setTimeout = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> timerId = originalSetTimeout(...args);
      <span class="hljs-built_in">this</span>.timeoutIds.push(timerId);
      <span class="hljs-keyword">return</span> timerId;
    &#125;;
    <span class="hljs-comment">// hijack setInterval</span>
    proxyWindow.setInterval = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> intervalId = originalSetInerval(...args);
      <span class="hljs-built_in">this</span>.intervalIds.push(intervalId);
      <span class="hljs-keyword">return</span> intervalId;
    &#125;;

    <span class="hljs-keyword">const</span> sandbox = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(proxyWindow, &#123;
      set(target: Window, <span class="hljs-attr">p</span>: PropertyKey, <span class="hljs-attr">value</span>: any): boolean &#123;
        target[p] = value;
      &#125;,
      get(target: Window, <span class="hljs-attr">p</span>: PropertyKey): any &#123;
        <span class="hljs-keyword">const</span> targetValue = target[p];
        <span class="hljs-keyword">if</span> (targetValue) &#123;
          <span class="hljs-comment">// case of addEventListener, removeEventListener, setTimeout, setInterval setted in sandbox</span>
          <span class="hljs-keyword">return</span> targetValue;
        &#125;
      &#125;,
      has(target: Window, <span class="hljs-attr">p</span>: PropertyKey): boolean &#123;
        <span class="hljs-keyword">return</span> p <span class="hljs-keyword">in</span> target || p <span class="hljs-keyword">in</span> originalWindow;
      &#125;,
    &#125;);
    <span class="hljs-built_in">this</span>.sandbox = sandbox;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">4、通信</h4>
<p>icestark 提供了 event/store 通信，其无非是实现了个简单的 EventEmit 实例，代码位置在 packages/icestark-data/src/event.js 文件中，相关源代码实现逻辑如下，我们进行了些代码注释，就不再赘述。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Event</span> <span class="hljs-title">implements</span> <span class="hljs-title">Hooks</span> </span>&#123;
  <span class="hljs-attr">eventEmitter</span>: object;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.eventEmitter = &#123;&#125;;
  &#125;

  <span class="hljs-comment">// 事件触发</span>
  <span class="hljs-function"><span class="hljs-title">emit</span>(<span class="hljs-params">key: string, ...args</span>)</span> &#123;
    <span class="hljs-keyword">const</span> keyEmitter = <span class="hljs-built_in">this</span>.eventEmitter[key];
    <span class="hljs-comment">// 执行事件注册的回调方法</span>
    keyEmitter.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> &#123;
      cb(...args);
    &#125;);
  &#125;

  <span class="hljs-comment">// 事件监听</span>
  <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">key: string, callback: (value: any) => <span class="hljs-keyword">void</span></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.eventEmitter[key]) &#123;
      <span class="hljs-built_in">this</span>.eventEmitter[key] = [];
    &#125;
    <span class="hljs-comment">// 将事件回调方法放入数组中</span>
    <span class="hljs-built_in">this</span>.eventEmitter[key].push(callback);
  &#125;
  <span class="hljs-comment">// 取消注册</span>
  <span class="hljs-function"><span class="hljs-title">off</span>(<span class="hljs-params">key: string, callback?: (value: any) => <span class="hljs-keyword">void</span></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (callback === <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-built_in">this</span>.eventEmitter[key] = <span class="hljs-literal">undefined</span>;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-built_in">this</span>.eventEmitter[key] = <span class="hljs-built_in">this</span>.eventEmitter[key].filter(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb !== callback);
  &#125;

  <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">key: string</span>)</span> &#123;
    <span class="hljs-keyword">const</span> keyEmitter = <span class="hljs-built_in">this</span>.eventEmitter[key];
    <span class="hljs-keyword">return</span> isArray(keyEmitter) && keyEmitter.length > <span class="hljs-number">0</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">四、总结</h3>
<p>经过以上代码整理分析，我们可以看到，其实 icestark 跟 single-spa、qiankun 这些微前端框架做的事情/原理<strong>大同小异</strong>，icestark 自己去实现了子应用的状态管理，然后也去实现了沙箱、通信等这些辅助功能。</p>
<p>辛苦整理良久，还望手动点赞鼓励~
博客 github地址为：<a href="https://github.com/fengshi123/blog" target="_blank" rel="nofollow noopener noreferrer">github.com/fengshi123/…</a> ，汇总了作者的所有博客，欢迎关注及 star ~</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            