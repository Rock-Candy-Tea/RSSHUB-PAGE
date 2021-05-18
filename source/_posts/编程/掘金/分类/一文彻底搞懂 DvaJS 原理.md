
---
title: '一文彻底搞懂 DvaJS 原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe4d06c6f1bd4e21b2bb413feb2d200c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 19:28:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe4d06c6f1bd4e21b2bb413feb2d200c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Dva 是什么</h2>
<p>dva 首先是一个基于<a href="https://github.com/reduxjs/redux" target="_blank" rel="nofollow noopener noreferrer">redux</a>和<a href="https://github.com/redux-saga/redux-saga" target="_blank" rel="nofollow noopener noreferrer">redux-saga</a>的数据流方案，然后为了简化开发体验，dva 还额外内置了<a href="https://github.com/ReactTraining/react-router" target="_blank" rel="nofollow noopener noreferrer">react-router</a>和<a href="https://github.com/github/fetch" target="_blank" rel="nofollow noopener noreferrer">fetch</a>，所以也可以理解为一个轻量级的应用框架。</p>
<h2 data-id="heading-1">Dva 解决的问题</h2>
<blockquote>
<p>经过一段时间的自学或培训，大家应该都能理解 redux 的概念，并认可这种数据流的控制可以让应用更可控，以及让逻辑更清晰。但随之而来通常会有这样的疑问：概念太多，并且 reducer, saga, action 都是分离的（分文件）。</p>
</blockquote>
<ul>
<li>文件切换问题。redux 的项目通常要分 reducer, action, saga, component 等等，他们的分目录存放造成的文件切换成本较大。</li>
<li>不便于组织业务模型 (或者叫 domain model) 。比如我们写了一个 userlist 之后，要写一个 productlist，需要复制很多文件。</li>
<li>saga 创建麻烦，每监听一个 action 都需要走 fork -> watcher -> worker 的流程</li>
<li>entry 创建麻烦。可以看下这个<a href="https://github.com/ant-design/antd-init/blob/master/boilerplates/redux/src/entries/index.js" target="_blank" rel="nofollow noopener noreferrer">redux entry</a>的例子，除了 redux store 的创建，中间件的配置，路由的初始化，Provider 的 store 的绑定，saga 的初始化，还要处理 reducer, component, saga 的 HMR 。这就是真实的项目应用 redux 的例子，看起来比较复杂。</li>
</ul>
<h2 data-id="heading-2">Dva 的优势</h2>
<ul>
<li><strong>易学易用</strong>，仅有 6 个 api，对 redux 用户尤其友好，<a href="https://umijs.org/guide/with-dva.html" target="_blank" rel="nofollow noopener noreferrer">配合 umi 使用</a>后更是降低为 0 API</li>
<li><strong>elm 概念</strong>，通过 reducers, effects 和 subscriptions 组织 model</li>
<li><strong>插件机制</strong>，比如<a href="https://github.com/dvajs/dva/tree/master/packages/dva-loading" target="_blank" rel="nofollow noopener noreferrer">dva-loading</a>可以自动处理 loading 状态，不用一遍遍地写 showLoading 和 hideLoading</li>
<li><strong>支持 HMR</strong>，基于<a href="https://github.com/dvajs/babel-plugin-dva-hmr" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-dva-hmr</a>实现 components、routes 和 models 的 HMR</li>
</ul>
<h2 data-id="heading-3">Dva 的劣势</h2>
<ul>
<li><strong>未来不确定性高。</strong><a href="https://github.com/dvajs/dva/issues/2208" target="_blank" rel="nofollow noopener noreferrer">dva@3 前年提出计划后，官方几乎不再维护</a>。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe4d06c6f1bd4e21b2bb413feb2d200c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>对于绝大多数不是特别复杂的场景来说，<strong>目前可以被 Hooks 取代</strong></li>
</ul>
<h2 data-id="heading-4">Dva 的适用场景</h2>
<ul>
<li>业务场景：组件间通信多，业务复杂，需要引入状态管理的项目</li>
<li>技术场景：使用 React Class Component 写的项目</li>
</ul>
<h2 data-id="heading-5">Dva 核心概念</h2>
<ul>
<li><strong>基于 Redux 理念的数据流向</strong>。 用户的交互或浏览器行为通过 dispatch 发起一个 action，如果是同步行为会直接通过 Reducers 改变 State，如果是异步行为（可以称为副作用）会先触发 Effects 然后流向 Reducers 最终改变 State。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bad128e488c4843991d5d90de2b0691~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>基于 Redux 的基本概念</strong>。包括：</p>
<ul>
<li>State 数据，通常为一个 JavaScript 对象，操作的时候每次都要当作不可变数据（immutable data）来对待，保证每次都是全新对象，没有引用关系，这样才能保证 State 的独立性，便于测试和追踪变化。</li>
<li>Action 行为，一个普通 JavaScript 对象，它是改变 State 的唯一途径。</li>
<li>dispatch，一个用于触发 action 改变 State 的函数。</li>
<li>Reducer 描述如何改变数据的纯函数，接受两个参数：已有结果和 action 传入的数据，通过运算得到新的 state。</li>
<li>Effects（Side Effects） 副作用，常见的表现为异步操作。dva 为了控制副作用的操作，底层引入了<a href="http://superraytin.github.io/redux-saga-in-chinese" target="_blank" rel="nofollow noopener noreferrer">redux-sagas</a>做异步流程控制，由于采用了<a href="http://www.ruanyifeng.com/blog/2015/04/generator.html" target="_blank" rel="nofollow noopener noreferrer">generator 的相关概念</a>，所以将异步转成同步写法，从而将 effects 转为纯函数。</li>
<li>Connect 一个函数，绑定 State 到 View</li>
</ul>
</li>
<li>
<p><strong>其他概念</strong></p>
<ul>
<li>Subscription，订阅，从<strong>源头</strong>获取数据，然后根据条件 dispatch 需要的 action，概念来源于<a href="https://elm-lang.org/news/farewell-to-frp" target="_blank" rel="nofollow noopener noreferrer">elm</a>。数据源可以是当前的时间、服务器的 websocket 连接、keyboard 输入、geolocation 变化、history 路由变化等等。</li>
<li>Router，前端路由，dva 实例提供了 router 方法来控制路由，使用的是<a href="https://github.com/reactjs/react-router" target="_blank" rel="nofollow noopener noreferrer">react-router</a>。</li>
<li>Route Components，跟数据逻辑无关的组件。通常需要 connect Model 的组件都是 Route Components，组织在/routes/目录下，而/components/目录下则是纯组件（Presentational Components，详见<a href="https://github.com/dvajs/dva-docs/blob/master/v1/zh-cn/tutorial/04-%E7%BB%84%E4%BB%B6%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%B3%95.md" target="_blank" rel="nofollow noopener noreferrer">组件设计方法</a>）</li>
</ul>
</li>
</ul>
<h2 data-id="heading-6">Dva 应用最简结构</h2>
<h4 data-id="heading-7">不带 Model</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> dva <span class="hljs-keyword">from</span> <span class="hljs-string">'dva'</span>;
<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Hello dva<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
<span class="hljs-comment">// 创建应用</span>
<span class="hljs-keyword">const</span> app = dva();
<span class="hljs-comment">// 注册视图</span>
app.router(<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>);
<span class="hljs-comment">// 启动应用</span>
app.start(<span class="hljs-string">'#root'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">带 Model</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建应用</span>
<span class="hljs-keyword">const</span> app = dva();
app.use(createLoading()) <span class="hljs-comment">// 使用插件</span>
<span class="hljs-comment">// 注册 Model</span>
app.model(&#123;
  <span class="hljs-attr">namespace</span>: <span class="hljs-string">'count'</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span> &#123; <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span> &#125;,
  &#125;,
  <span class="hljs-attr">effects</span>: &#123;
    *<span class="hljs-function"><span class="hljs-title">addAfter1Second</span>(<span class="hljs-params">action, &#123; call, put &#125;</span>)</span> &#123;
      <span class="hljs-keyword">yield</span> call(delay, <span class="hljs-number">1000</span>);
      <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'add'</span> &#125;);
    &#125;,
  &#125;,
&#125;);
<span class="hljs-comment">// 注册视图</span>
app.router(<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ConnectedApp</span> /></span></span>);
<span class="hljs-comment">// 启动应用</span>
app.start(<span class="hljs-string">'#root'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Dva底层原理和部分关键实现</h2>
<h4 data-id="heading-10">背景介绍</h4>
<ol>
<li>整个 dva 项目使用 lerna 管理的，在每个 package 的 package.json 中找到模块对应的入口文件，然后查看对应源码。</li>
<li>dva 是个函数，返回一了个 app 的对象。</li>
<li>目前 dva 的源码核心部分包含两部分，dva 和 dva-core。前者用高阶组件 React-redux 实现了 view 层，后者是用 redux-saga 解决了 model 层。</li>
</ol>
<h4 data-id="heading-11"><a href="https://github.com/dvajs/dva/blob/master/packages/dva/src/index.js" target="_blank" rel="nofollow noopener noreferrer">dva</a></h4>
<p>dva 做了三件比较重要的事情：</p>
<ol>
<li>代理 router 和 start 方法，实例化 app 对象</li>
<li>调用 dva-core 的 start 方法，同时渲染视图</li>
<li>使用 react-redux 完成了 react 到 redux 的连接。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dva/src/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">opts = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-comment">// 1. 使用 connect-react-router 和 history 初始化 router 和 history</span>
  <span class="hljs-comment">// 通过添加 redux 的中间件 react-redux-router，强化了 history 对象的功能</span>
 <span class="hljs-keyword">const</span> history = opts.history || createHashHistory();
  <span class="hljs-keyword">const</span> createOpts = &#123;
    <span class="hljs-attr">initialReducer</span>: &#123;
      <span class="hljs-attr">router</span>: connectRouter(history),
    &#125;,
    <span class="hljs-function"><span class="hljs-title">setupMiddlewares</span>(<span class="hljs-params">middlewares</span>)</span> &#123;
      <span class="hljs-keyword">return</span> [routerMiddleware(history), ...middlewares];
    &#125;,
    <span class="hljs-function"><span class="hljs-title">setupApp</span>(<span class="hljs-params">app</span>)</span> &#123;
      app._history = patchHistory(history);
    &#125;,
  &#125;;
  <span class="hljs-comment">// 2. 调用 dva-core 里的 create 方法 ，函数内实例化一个 app 对象。</span>
 <span class="hljs-keyword">const</span> app = create(opts, createOpts);
  <span class="hljs-keyword">const</span> oldAppStart = app.start;
  <span class="hljs-comment">// 3. 用自定义的 router 和 start 方法代理</span>
 app.router = router;
  app.start = start;
  <span class="hljs-keyword">return</span> app;
  <span class="hljs-comment">// 3.1 绑定用户传递的 router 到 app._router</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">router</span>(<span class="hljs-params">router</span>) </span>&#123;
    invariant(
      isFunction(router),
      <span class="hljs-string">`[app.router] router should be function, but got <span class="hljs-subst">$&#123;<span class="hljs-keyword">typeof</span> router&#125;</span>`</span>,
    );
    app._router = router;
  &#125;
  <span class="hljs-comment">// 3.2 调用 dva-core 的 start 方法，并渲染视图</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params">container</span>) </span>&#123;
    <span class="hljs-comment">// 对 container 做一系列检查，并根据 container 找到对应的DOM节点</span>
    <span class="hljs-keyword">if</span> (!app._store) &#123;
      oldAppStart.call(app);
    &#125;
    <span class="hljs-keyword">const</span> store = app._store;
    <span class="hljs-comment">// 为HMR暴露_getProvider接口</span>
 <span class="hljs-comment">// ref: https://github.com/dvajs/dva/issues/469</span>
 app._getProvider = getProvider.bind(<span class="hljs-literal">null</span>, store, app);
    <span class="hljs-comment">// 渲染视图</span>
 <span class="hljs-keyword">if</span> (container) &#123;
      render(container, store, app, app._router);
      app._plugin.apply(<span class="hljs-string">'onHmr'</span>)(render.bind(<span class="hljs-literal">null</span>, container, store, app));
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> getProvider(store, <span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>._router);
    &#125;
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getProvider</span>(<span class="hljs-params">store, app, router</span>) </span>&#123;
  <span class="hljs-keyword">const</span> DvaRoot = <span class="hljs-function"><span class="hljs-params">extraProps</span> =></span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>&#123;router(&#123; app, history: app._history, ...extraProps &#125;)&#125;<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
  );
  <span class="hljs-keyword">return</span> DvaRoot;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">container, store, app, router</span>) </span>&#123;
  <span class="hljs-keyword">const</span> ReactDOM = <span class="hljs-built_in">require</span>(<span class="hljs-string">'react-dom'</span>); <span class="hljs-comment">// eslint-disable-line</span>
 ReactDOM.render(React.createElement(getProvider(store, app, router)), container);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们同时可以发现 app 是通过 create(opts, createOpts)进行初始化的，其中 opts 是暴露给使用者的配置，createOpts 是暴露给开发者的配置，真实的 create 方法在 dva-core 中实现</p>
<h4 data-id="heading-12"><a href="https://github.com/dvajs/dva/blob/master/packages/dva-core/src/index.js" target="_blank" rel="nofollow noopener noreferrer">dva-core</a></h4>
<p>dva-core 则完成了核心功能：</p>
<ol>
<li>
<p>通过 create 方法完成 app 实例的构造，并暴露 use、model 和 start 三个接口</p>
</li>
<li>
<p>通过 start 方法完成</p>
</li>
</ol>
<ul>
<li>
<pre><code class="copyable">store 的初始化
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">models 和 effects 的封装，收集并运行 sagas
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">运行所有的 model.subscriptions
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">暴露 app.model、app.unmodel、app.replaceModel 三个接口
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>dva-core create</p>
<p><strong>作用：</strong> 完成 app 实例的构造，并暴露 use、model 和 start 三个接口</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dva-core/src/index.js</span>
<span class="hljs-keyword">const</span> dvaModel = &#123;
  <span class="hljs-attr">namespace</span>: <span class="hljs-string">'@@dva'</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">UPDATE</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>;
    &#125;,
  &#125;,
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">hooksAndOpts = &#123;&#125;, createOpts = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; initialReducer, setupApp = noop &#125; = createOpts; <span class="hljs-comment">// 在dva/index.js中构造了createOpts对象</span>
  <span class="hljs-keyword">const</span> plugin = <span class="hljs-keyword">new</span> Plugin(); <span class="hljs-comment">// dva-core中的插件机制，每个实例化的dva对象都包含一个plugin对象</span>
  plugin.use(filterHooks(hooksAndOpts)); <span class="hljs-comment">// 将dva(opts)构造参数opts上与hooks相关的属性转换成一个插件</span>
  <span class="hljs-keyword">const</span> app = &#123;
    <span class="hljs-attr">_models</span>: [prefixNamespace(&#123; ...dvaModel &#125;)],
    <span class="hljs-attr">_store</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">_plugin</span>: plugin,
    <span class="hljs-attr">use</span>: plugin.use.bind(plugin), <span class="hljs-comment">// 暴露的use方法，方便编写自定义插件</span>
    model, <span class="hljs-comment">// 暴露的model方法，用于注册model</span>
    start, <span class="hljs-comment">// 原本的start方法，在应用渲染到DOM节点时通过oldStart调用</span>
  &#125;;
  <span class="hljs-keyword">return</span> app;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>dva-core start</p>
<p><strong>作用：</strong></p>
<ol>
<li>封装models 和 effects ，收集并运行 sagas</li>
<li>完成store 的初始化</li>
<li>运行所有的model.subscriptions</li>
<li>暴露app.model、app.unmodel、app.replaceModel三个接口</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> sagaMiddleware = createSagaMiddleware();
  <span class="hljs-keyword">const</span> promiseMiddleware = createPromiseMiddleware(app);
  app._getSaga = getSaga.bind(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">const</span> sagas = [];
  <span class="hljs-keyword">const</span> reducers = &#123; ...initialReducer &#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> m <span class="hljs-keyword">of</span> app._models) &#123;
    <span class="hljs-comment">// 把每个 model 合并为一个reducer，key 是 namespace 的值，value 是 reducer 函数</span>
    reducers[m.namespace] = getReducer(m.reducers, m.state, plugin._handleActions);
    <span class="hljs-keyword">if</span> (m.effects) &#123;
      <span class="hljs-comment">// 收集每个 effects 到 sagas 数组</span>
      sagas.push(app._getSaga(m.effects, m, onError, plugin.get(<span class="hljs-string">'onEffect'</span>), hooksAndOpts));
    &#125;
  &#125;
  <span class="hljs-comment">// 初始化 Store</span>
  app._store = createStore(&#123;
    <span class="hljs-attr">reducers</span>: createReducer(),
    <span class="hljs-attr">initialState</span>: hooksAndOpts.initialState || &#123;&#125;,
    plugin,
    createOpts,
    sagaMiddleware,
    promiseMiddleware,
  &#125;);
  <span class="hljs-keyword">const</span> store = app._store;
  <span class="hljs-comment">// Extend store</span>
  store.runSaga = sagaMiddleware.run;
  store.asyncReducers = &#123;&#125;;
  <span class="hljs-comment">// Execute listeners when state is changed</span>
  <span class="hljs-keyword">const</span> listeners = plugin.get(<span class="hljs-string">'onStateChange'</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> listener <span class="hljs-keyword">of</span> listeners) &#123;
    store.subscribe(<span class="hljs-function">() =></span> &#123;
      listener(store.getState());
    &#125;);
  &#125;
  <span class="hljs-comment">// Run sagas, 调用 Redux-Saga 的 createSagaMiddleware 创建 saga中间件，调用中间件的 run 方法所有收集起来的异步方法</span>
  <span class="hljs-comment">// run方法监听每一个副作用action，当action发生的时候，执行对应的 saga</span>
  sagas.forEach(sagaMiddleware.run);
  <span class="hljs-comment">// Setup app</span>
  setupApp(app);
  <span class="hljs-comment">// 运行 subscriptions</span>
  <span class="hljs-keyword">const</span> unlisteners = &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> model <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>._models) &#123;
    <span class="hljs-keyword">if</span> (model.subscriptions) &#123;
      unlisteners[model.namespace] = runSubscription(model.subscriptions, model, app, onError);
    &#125;
  &#125;
  <span class="hljs-comment">// 暴露三个 Model 相关的接口，Setup app.model and app.unmodel</span>
  app.model = injectModel.bind(app, createReducer, onError, unlisteners);
  app.unmodel = unmodel.bind(app, createReducer, reducers, unlisteners);
  app.replaceModel = replaceModel.bind(app, createReducer, reducers, unlisteners, onError);
  <span class="hljs-comment">/**
   * Create global reducer for redux.
   *
   * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Object&#125;</span></span>
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReducer</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> reducerEnhancer(
      combineReducers(&#123;
        ...reducers,
        ...extraReducers,
        ...(app._store ? app._store.asyncReducers : &#123;&#125;),
      &#125;),
    );
  &#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">路由</h4>
<p>在前面的 dva.start 方法中我们看到了 createOpts，并了解到在 dva-core 的 start 中的不同时机调用了对应方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> routerRedux <span class="hljs-keyword">from</span> <span class="hljs-string">'connected-react-router'</span>;
<span class="hljs-keyword">const</span> &#123; connectRouter, routerMiddleware &#125; = routerRedux;
<span class="hljs-keyword">const</span> createOpts = &#123;
  <span class="hljs-attr">initialReducer</span>: &#123;
    <span class="hljs-attr">router</span>: connectRouter(history),
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setupMiddlewares</span>(<span class="hljs-params">middlewares</span>)</span> &#123;
    <span class="hljs-keyword">return</span> [routerMiddleware(history), ...middlewares];
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setupApp</span>(<span class="hljs-params">app</span>)</span> &#123;
    app._history = patchHistory(history);
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 initialReducer 和 setupMiddlewares 在初始化 store 时调用，然后才调用 setupApp</p>
<p>可以看见针对 router 相关的 reducer 和中间件配置，其中 connectRouter 和 routerMiddleware 均使用了 connected-react-router 这个库，其主要思路是：把路由跳转也当做了一种特殊的 action。</p>
<h2 data-id="heading-14">Dva 与 React、React-Redux、Redux-Saga 之间的差异</h2>
<h4 data-id="heading-15">原生 React</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db028baefc7a4fbd89d651cb3061cd65~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">按照 React 官方指导意见, 如果多个 Component 之间要发生交互, 那么状态(即: 数据)就维护在这些 Component 的最小公约父节点上,
也即是</p>
<p>以及 本身不维持任何 state, 完全由父节点 传入 props 以决定其展现, 是一个纯函数的存在形式, 即: Pure Component</p>
<h4 data-id="heading-16">React-Redux</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef148947d84841c5961da2a29c7b5562~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">与上图相比, 几个明显的改进点:</p>
<ol>
<li>状态及页面逻辑从 里面抽取出来, 成为独立的 store, 页面逻辑就是 reducer</li>
<li>及都是 Pure Component, 通过 connect 方法可以很方便地给它俩加一层 wrapper 从而建立起与 store 的联系: 可以通过 dispatch 向 store 注入 action, 促使 store 的状态进行变化, 同时又订阅了 store 的状态变化, 一旦状态变化, 被 connect 的组件也随之刷新</li>
<li>使用 dispatch 往 store 发送 action 的这个过程是可以被拦截的, 自然而然地就可以在这里增加各种 Middleware, 实现各种自定义功能, eg: logging</li>
</ol>
<p>这样一来, 各个部分各司其职, 耦合度更低, 复用度更高, 扩展性更好。</p>
<h4 data-id="heading-17">Redux-Saga</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d87820f560274d4cb2b3e4732e7c369d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">因为我们可以使用 Middleware 拦截 action, 这样一来异步的网络操作也就很方便了, 做成一个 Middleware 就行了, 这里使用 redux-saga 这个类库, 举个栗子:</p>
<ol>
<li>点击创建 Todo 的按钮, 发起一个 type == addTodo 的 action</li>
<li>saga 拦截这个 action, 发起 http 请求, 如果请求成功, 则继续向 reducer 发一个 type == addTodoSucc 的 action, 提示创建成功, 反之则发送 type == addTodoFail 的 action 即可</li>
</ol>
<h4 data-id="heading-18">Dva</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7cceb8c26ee4aeab8aeb662e71acb85~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">有了前面三步的铺垫, Dva 的出现也就水到渠成了, 正如 Dva 官网所言, Dva 是基于 React + Redux + Saga 的最佳实践, 对于提升编码体验有三点贡献：</p>
<ol>
<li>把 store 及 saga 统一为一个 model 的概念, 写在一个 js 文件里面</li>
<li>增加了一个 Subscriptions, 用于收集其他来源的 action, 比如键盘操作等</li>
<li>model 写法很简约, 类似于 DSL（领域特定语言），可以提升编程的沉浸感，进而提升效率</li>
</ol>
<p><strong>约定大于配置</strong></p>
<pre><code class="hljs language-js copyable" lang="js">app.model(&#123;
  <span class="hljs-attr">namespace</span>: <span class="hljs-string">'count'</span>,
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">record</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">current</span>: <span class="hljs-number">0</span>,
  &#125;,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">const</span> newCurrent = state.current + <span class="hljs-number">1</span>;
      <span class="hljs-keyword">return</span> &#123; ...state,
        <span class="hljs-attr">record</span>: newCurrent > state.record ? newCurrent : state.record,
        <span class="hljs-attr">current</span>: newCurrent,
      &#125;;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">minus</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123; ...state, <span class="hljs-attr">current</span>: state.current - <span class="hljs-number">1</span>&#125;;
    &#125;,
  &#125;,
  <span class="hljs-attr">effects</span>: &#123;
    *<span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">action, &#123; call, put &#125;</span>)</span> &#123;
      <span class="hljs-keyword">yield</span> call(delay, <span class="hljs-number">1000</span>);
      <span class="hljs-keyword">yield</span> put(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'minus'</span> &#125;);
    &#125;,
  &#125;,
  <span class="hljs-attr">subscriptions</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">keyboardWatcher</span>(<span class="hljs-params">&#123; dispatch &#125;</span>)</span> &#123;
      key(<span class="hljs-string">'⌘+up, ctrl+up'</span>, <span class="hljs-function">() =></span> &#123; dispatch(&#123;<span class="hljs-attr">type</span>:<span class="hljs-string">'add'</span>&#125;) &#125;);
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">Dva 背后值得学习的思想</h2>
<blockquote>
<p>Dva 的 api 参考了<a href="https://github.com/choojs/choo" target="_blank" rel="nofollow noopener noreferrer">choo</a>，概念来自于 elm。</p>
</blockquote>
<ol>
<li>Choo 的理念：编程应该是有趣且轻松的，API 要看上去简单易用。</li>
</ol>
<blockquote>
<p>We believe programming should be fun and light, not stern and stressful. It's cool to be cute; using serious words without explaining them doesn't make for better results - if anything it scares people off. We don't want to be scary, we want to be nice and fun, and then<em>casually_be the best choice around._Real casually.</em></p>
</blockquote>
<blockquote>
<p>We believe frameworks should be disposable, and components recyclable. We don't want a web where walled gardens jealously compete with one another. By making the DOM the lowest common denominator, switching from one framework to another becomes frictionless. Choo is modest in its design; we don't believe it will be top of the class forever, so we've made it as easy to toss out as it is to pick up.</p>
</blockquote>
<blockquote>
<p>We don't believe that bigger is better. Big APIs, large complexities, long files - we see them as omens of impending userland complexity. We want everyone on a team, no matter the size, to fully understand how an application is laid out. And once an application is built, we want it to be small, performant and easy to reason about. All of which makes for easy to debug code, better results and super smiley faces.</p>
</blockquote>
<ol start="2">
<li>来自 Elm 的概念：</li>
</ol>
<ul>
<li>Subscription，订阅，从<strong>源头</strong>获取数据，数据源可以是当前的时间、服务器的 websocket 连接、keyboard 输入、geolocation 变化、history 路由变化等等。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19a78b52270a4f5e899b03a16365cc85~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">附录</h2>
<p><a href="https://github.com/dvajs/dva/issues/1" target="_blank" rel="nofollow noopener noreferrer">Why dva and what's dva</a></p>
<p><a href="https://www.github.com/sorrycc/blog/issues/6" target="_blank" rel="nofollow noopener noreferrer">支付宝前端应用架构的发展和选择</a></p>
<p><a href="https://github.com/sorrycc/blog/issues/1" target="_blank" rel="nofollow noopener noreferrer">React + Redux 最佳实践</a></p>
<p><a href="https://dvajs.com/guide/concepts.html#%E6%95%B0%E6%8D%AE%E6%B5%81%E5%90%91" target="_blank" rel="nofollow noopener noreferrer">Dva 概念</a></p>
<p><a href="https://dvajs.com/guide/introduce-class.html#react-%E6%B2%A1%E6%9C%89%E8%A7%A3%E5%86%B3%E7%9A%84%E9%97%AE%E9%A2%98" target="_blank" rel="nofollow noopener noreferrer">Dva 入门课</a></p>
<p><a href="https://dvajs.com/guide/source-code-explore.html#%E9%9A%90%E8%97%8F%E5%9C%A8-package-json-%E9%87%8C%E7%9A%84%E7%A7%98%E5%AF%86" target="_blank" rel="nofollow noopener noreferrer">Dva 源码解析</a></p>
<p><a href="https://www.yuque.com/lulongwen/react/ixolgo" target="_blank" rel="nofollow noopener noreferrer">Dva 源码实现</a></p>
<p><a href="https://www.shymean.com/article/dva%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90" target="_blank" rel="nofollow noopener noreferrer">Dva 源码分析</a></p>
<hr>
<p>欢迎关注「 字节前端 ByteFE 」
简历投递联系邮箱「<a href="mailto:tech@bytedance.com">tech@bytedance.com</a>」</p></div>  
</div>
            