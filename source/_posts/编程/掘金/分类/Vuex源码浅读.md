
---
title: 'Vuex源码浅读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4263'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 22:55:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=4263'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">vuex是什么？</h2>
<p>Vuex 是一个专为 Vue.js 应用程序开发的<strong>状态管理模式</strong>。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 也集成到 Vue 的官方调试工具 <code>devtools extension</code>，提供了诸如零配置的 time-travel 调试、状态快照导入导出等高级调试功能。（<a href="https://vuex.vuejs.org/zh/" target="_blank" rel="nofollow noopener noreferrer">Vuex官网</a>）</p>
<h2 data-id="heading-1">提示</h2>
<ul>
<li>本文只分析主要代码(主流程代码)</li>
<li>阅读本文的前提是至少使用过<code>vuex</code></li>
<li><a href="https://github.com/vuejs/vuex" target="_blank" rel="nofollow noopener noreferrer">源码</a> 版本是 3.x 版本 (截止到2021/04/23)</li>
<li>本文的主要目的是记录一下自己的学习过程</li>
</ul>
<h2 data-id="heading-2">目标</h2>
<ul>
<li>了解Vuex的安装过程</li>
<li>了解Store的实例化过程</li>
</ul>
<p>先看一个简单的 <code>vuex</code> 是初始化的过程</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)
<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">1</span>
  &#125;,
  <span class="hljs-attr">getter</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">state</span>)</span> &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">context</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          context.commit(<span class="hljs-string">'increment'</span>)
          resolve(context.state)
        &#125;, <span class="hljs-number">1000</span>)
      &#125;)
    &#125;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
    <span class="hljs-attr">a</span>: &#123;
      <span class="hljs-attr">state</span>: &#123;
        <span class="hljs-attr">aCount</span>: <span class="hljs-number">1</span>
      &#125;      
    &#125;,
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">state</span>: &#123;
        <span class="hljs-attr">bCount</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;
  &#125;
&#125;)
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#root'</span>,
  router,
  store, 
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Vuex的安装过程</h2>
<p>首先 <code>vuex</code> 的安装方法(install)在 <strong>src/store.js</strong> 中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/store.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">_Vue</span>) </span>&#123;
  Vue = _Vue
  applyMixin(Vue)
&#125;

<span class="hljs-comment">// src/mixin.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMixin</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-keyword">const</span> version = <span class="hljs-built_in">Number</span>(Vue.version.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>])
  <span class="hljs-keyword">if</span> (version >= <span class="hljs-number">2</span>) &#123;
    Vue.mixin(&#123; <span class="hljs-attr">beforeCreate</span>: vuexInit &#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    ...
<span class="hljs-comment">//这里是 vuex1.x版本的代码，可以忽视</span>
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vuexInit</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> options = <span class="hljs-built_in">this</span>.$options
    <span class="hljs-keyword">if</span> (options.store) &#123;
      <span class="hljs-built_in">this</span>.$store = <span class="hljs-keyword">typeof</span> options.store === <span class="hljs-string">'function'</span>
        ? options.store()
        : options.store
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (options.parent && options.parent.$store) &#123;
      <span class="hljs-built_in">this</span>.$store = options.parent.$store
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 <code>vuex</code> 的安装过程还是比较简单的 暴露一个 <code>install</code> 方法，在调用 <code>Vue.use(Vuex)</code> 的时候会调用 <code>install</code> 方法。install方法就是在Vue中mixin一个beforeCreate钩子函数，beforeCreate中干的事就是把通过 <code>new Vuex.Store()</code> 生成的实例绑定到 Vue的每一个实例上 的<code>this.$sotre</code>，这样我们在组件中就可以通过 <code>this.$store</code> 访问 vuex 的实例。</p>
<h2 data-id="heading-4">Store的实例化过程</h2>
<p><code>store</code>就是一个数据仓库,为了更方便的管理仓库, 我们把一个大的 <code>store</code>拆成一些 <code>modules</code>,整 个 <code>modules</code> 是一个树型结构。每个 <code>module</code> 又分別定义了 <code>state</code>, <code>getters</code>, <code>mutations</code>、 <code>actions</code> 我们也通过递归遍历模块的方式都完成了它们的初始化。</p>
<p>还是在 <strong>src/store.js</strong> 中，<code>vuex</code>暴露了一个 <code>Store</code> 的构造函数。先看 <code>constructor()</code>，原型方法在执行到的时候再看。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">options = &#123;&#125;</span>) &#123;
<span class="hljs-comment">//...</span>
    <span class="hljs-keyword">const</span> &#123;
      plugins = [],
      strict = <span class="hljs-literal">false</span>
    &#125; = options

    <span class="hljs-built_in">this</span>._committing = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>._actions = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">this</span>._actionSubscribers = []
    <span class="hljs-built_in">this</span>._mutations = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">this</span>._wrappedGetters = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">this</span>._modules = <span class="hljs-keyword">new</span> ModuleCollection(options)
    <span class="hljs-built_in">this</span>._modulesNamespaceMap = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">this</span>._subscribers = []
    <span class="hljs-built_in">this</span>._watcherVM = <span class="hljs-keyword">new</span> Vue()
    <span class="hljs-built_in">this</span>._makeLocalGettersCache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)

    <span class="hljs-keyword">const</span> store = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> &#123; dispatch, commit &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-built_in">this</span>.dispatch = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">boundDispatch</span> (<span class="hljs-params">type, payload</span>) </span>&#123;
      <span class="hljs-keyword">return</span> dispatch.call(store, type, payload)
    &#125;
    <span class="hljs-built_in">this</span>.commit = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">boundCommit</span> (<span class="hljs-params">type, payload, options</span>) </span>&#123;
      <span class="hljs-keyword">return</span> commit.call(store, type, payload, options)
    &#125;

    <span class="hljs-built_in">this</span>.strict = strict
    <span class="hljs-keyword">const</span> state = <span class="hljs-built_in">this</span>._modules.root.state

    installModule(<span class="hljs-built_in">this</span>, state, [], <span class="hljs-built_in">this</span>._modules.root)

    resetStoreVM(<span class="hljs-built_in">this</span>, state)

    plugins.forEach(<span class="hljs-function"><span class="hljs-params">plugin</span> =></span> plugin(<span class="hljs-built_in">this</span>))

    <span class="hljs-keyword">const</span> useDevtools = options.devtools !== <span class="hljs-literal">undefined</span> ? options.devtools : Vue.config.devtools
    <span class="hljs-keyword">if</span> (useDevtools) &#123;
      devtoolPlugin(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 下面是原型方法</span>
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先是定义了一大堆初始化变量，大多数我们可以先不看，等到用到的时候再回头看，先看执行代码(干了事的代码)。</p>
<p>分析执行的代码我们可以得到在 <code>constructor()</code> 中主要执行了下面几个方法，其实也就是整个<code>Store</code> 整个初始化的过程中几个主要的过程。</p>
<ul>
<li><code>new ModuleCollection(options)</code></li>
<li><code>installModule(this, state, [], this._modules.root)</code></li>
<li><code>resetStoreVM(this, state)</code></li>
</ul>
<p>下面我们分别进入这几个方法具体分析一下。</p>
<h3 data-id="heading-5">new ModuleCollection</h3>
<p>代码位置 <strong>src/module/module-collection.js</strong></p>
<p>根据构造函数名我们大致可以得出这是初始化<code>store</code>中<code>modules</code>的构造函数，带着这个思路我们还是先看 <code>constructor()</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ModuleCollection</span> </span>&#123;
  <span class="hljs-comment">// rawRootModule 就是我们初始化时传入 new Vuex.Store(optionss) 的 options</span>
  <span class="hljs-title">constructor</span> (<span class="hljs-params">rawRootModule</span>) &#123;
    <span class="hljs-built_in">this</span>.register([], rawRootModule, <span class="hljs-literal">false</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>constructor()</code> 很简单，就执行了一个 <strong>this.register([], rawRootModule, false)</strong>。接着看 <code>register</code> 方法。</p>
<p><code>rawModule</code> 就是我们传入的 options 或者 options下的 <code>module</code>，也就是用于生成 <code>module</code> 的原始数据。</p>
<pre><code class="hljs language-js copyable" lang="js">  register (path, rawModule, runtime = <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-comment">// 初始化 module</span>
    <span class="hljs-keyword">const</span> newModule = <span class="hljs-keyword">new</span> Module(rawModule, runtime)
    <span class="hljs-comment">// 第一次进来 path为空 register 中第一个参数为 []</span>
    <span class="hljs-keyword">if</span> (path.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 将通过第一次传入的 options 生成的 modeule 作为 root 绑定到 this 上，方便取 root module</span>
      <span class="hljs-built_in">this</span>.root = newModule
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 之后再进来 path 就有值了 取出来 root module，再次生成的 module 都会绑定到 root module 中</span>
      <span class="hljs-keyword">const</span> parent = <span class="hljs-built_in">this</span>.get(path.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>))
      parent.addChild(path[path.length - <span class="hljs-number">1</span>], newModule)
    &#125;
<span class="hljs-comment">// 如果 我们初始化的数据中有 modules 就继续递归执行 register</span>
    <span class="hljs-keyword">if</span> (rawModule.modules) &#123;
      forEachValue(rawModule.modules, <span class="hljs-function">(<span class="hljs-params">rawChildModule, key</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.register(path.concat(key), rawChildModule, runtime)
      &#125;)
    &#125;
  &#125;

<span class="hljs-comment">// 代码位置 src/module/module.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Module</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">rawModule, runtime</span>) &#123;
    <span class="hljs-built_in">this</span>.runtime = runtime
    <span class="hljs-comment">// 初始化子 module，当前 module 下的子 rawModule 都添加到 _children 中</span>
    <span class="hljs-built_in">this</span>._children = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">this</span>._rawModule = rawModule
    <span class="hljs-keyword">const</span> rawState = rawModule.state
<span class="hljs-comment">// 将moudle中的 state 绑定到 this 上</span>
    <span class="hljs-built_in">this</span>.state = (<span class="hljs-keyword">typeof</span> rawState === <span class="hljs-string">'function'</span> ? rawState() : rawState) || &#123;&#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就能生成一个 <code>modules</code> 的树状数据，并把数据放到 <strong>this._modules</strong> 中。</p>
<p><code>modules</code> 大概是这个样子，可以看到 <code>modules</code> 目前只是生成了一个树状结构和初始化了每个<code>module</code>的<code>state</code>，接下来我们继续看代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// rowModule 就是该module的原始数据</span>
&#123;
  <span class="hljs-attr">root</span>: &#123;
    <span class="hljs-attr">state</span>: &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">1</span> &#125;,
    <span class="hljs-attr">_children</span>: &#123;
      <span class="hljs-attr">a</span>: &#123;
        <span class="hljs-attr">state</span>: &#123; <span class="hljs-attr">aCount</span>: <span class="hljs-number">1</span>&#125;,
        <span class="hljs-attr">_children</span>: &#123;&#125;
        <span class="hljs-attr">_rawModule</span>: rowModule
      &#125;,
      <span class="hljs-attr">b</span>: &#123;
        <span class="hljs-attr">state</span>: &#123; <span class="hljs-attr">bCount</span>: <span class="hljs-number">1</span>&#125;,
        <span class="hljs-attr">_children</span>: &#123;&#125;
        <span class="hljs-attr">_rawModule</span>: rowModule
      &#125;
    &#125;,
    <span class="hljs-attr">_rawModule</span>: rowModule
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">installModule</h3>
<p><strong>installModule</strong> 是初始化 <code>module</code> 中 <code>getter</code> <code>mutations</code> <code>actions</code> 。</p>
<p>直接看代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">installModule</span> (<span class="hljs-params">store, rootState, path, <span class="hljs-built_in">module</span>, hot</span>) </span>&#123;
  <span class="hljs-keyword">const</span> isRoot = !path.length
  <span class="hljs-comment">// 获取当前module 的 namespace，root module的namespace为 ""。</span>
  <span class="hljs-keyword">const</span> namespace = store._modules.getNamespace(path)

  <span class="hljs-comment">// register in namespace map</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.namespaced) &#123;
    <span class="hljs-keyword">if</span> (store._modulesNamespaceMap[namespace] && __DEV__) &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[vuex] duplicate namespace <span class="hljs-subst">$&#123;namespace&#125;</span> for the namespaced module <span class="hljs-subst">$&#123;path.join(<span class="hljs-string">'/'</span>)&#125;</span>`</span>)
    &#125;
    <span class="hljs-comment">// 记录namespace和 module 的对应关系</span>
    <span class="hljs-comment">// &#123;</span>
    <span class="hljs-comment">//   'a/': aModule,</span>
    <span class="hljs-comment">//   'b/': bModule</span>
    <span class="hljs-comment">// &#125;</span>
    store._modulesNamespaceMap[namespace] = <span class="hljs-built_in">module</span>
  &#125;
  
<span class="hljs-comment">// 这里可以先不看，和响应式数据有关的</span>
  <span class="hljs-keyword">if</span> (!isRoot && !hot) &#123;
    <span class="hljs-keyword">const</span> parentState = getNestedState(rootState, path.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>))
    <span class="hljs-keyword">const</span> moduleName = path[path.length - <span class="hljs-number">1</span>]
    store._withCommit(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (__DEV__) &#123;
        <span class="hljs-keyword">if</span> (moduleName <span class="hljs-keyword">in</span> parentState) &#123;
          <span class="hljs-built_in">console</span>.warn(
            <span class="hljs-string">`[vuex] state field "<span class="hljs-subst">$&#123;moduleName&#125;</span>" was overridden by a module with the same name at "<span class="hljs-subst">$&#123;path.join(<span class="hljs-string">'.'</span>)&#125;</span>"`</span>
          )
        &#125;
      &#125;
      Vue.set(parentState, moduleName, <span class="hljs-built_in">module</span>.state)
    &#125;)
  &#125;

  <span class="hljs-keyword">const</span> local = <span class="hljs-built_in">module</span>.context = makeLocalContext(store, namespace, path)

  <span class="hljs-comment">// 将 mutation 循环绑定到当前module上</span>
  <span class="hljs-built_in">module</span>.forEachMutation(<span class="hljs-function">(<span class="hljs-params">mutation, key</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> namespacedType = namespace + key
    registerMutation(store, namespacedType, mutation, local)
  &#125;)
  <span class="hljs-comment">// 将 action 循环绑定到当前module上</span>
  <span class="hljs-built_in">module</span>.forEachAction(<span class="hljs-function">(<span class="hljs-params">action, key</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> type = action.root ? key : namespace + key
    <span class="hljs-keyword">const</span> handler = action.handler || action
    registerAction(store, type, handler, local)
  &#125;)
  <span class="hljs-comment">// 将 getter 循环绑定到当前module上</span>
  <span class="hljs-built_in">module</span>.forEachGetter(<span class="hljs-function">(<span class="hljs-params">getter, key</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> namespacedType = namespace + key
    registerGetter(store, namespacedType, getter, local)
  &#125;)
  <span class="hljs-comment">// 如果改 module 下有子module 递归继续执行 installModule</span>
  <span class="hljs-built_in">module</span>.forEachChild(<span class="hljs-function">(<span class="hljs-params">child, key</span>) =></span> &#123;
    installModule(store, rootState, path.concat(key), child, hot)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的核心代码：</p>
<ul>
<li>
<p><strong>const local = module.context = makeLocalContext(store, namespace, path)</strong></p>
</li>
<li>
<p><strong>registerMutation(store, namespacedType, mutation, local)</strong></p>
</li>
<li>
<p><strong>registerAction(store, type, handler, local)</strong></p>
</li>
<li>
<p><strong>registerGetter(store, namespacedType, getter, local)</strong></p>
</li>
</ul>
<h4 data-id="heading-7">makeLocalContext</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我直接把非关键代码直接删除了</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeLocalContext</span> (<span class="hljs-params">store, namespace, path</span>) </span>&#123;
  <span class="hljs-keyword">const</span> noNamespace = namespace === <span class="hljs-string">''</span>
  <span class="hljs-keyword">const</span> local = &#123;
    <span class="hljs-comment">// unifyObjectStyle 是统一参数的方法，这个方法让 dispatch 和 commit 可以采用两种不同的入参方式</span>
    <span class="hljs-comment">// commit('increment', 1) | commit(&#123;type: 'increment', payload: 1&#125;)</span>
    
    <span class="hljs-comment">// 这里的dispatch</span>
    <span class="hljs-attr">dispatch</span>: noNamespace ? store.dispatch : <span class="hljs-function">(<span class="hljs-params">_type, _payload, _options</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> args = unifyObjectStyle(_type, _payload, _options)
      <span class="hljs-keyword">const</span> &#123; payload, options &#125; = args
      <span class="hljs-keyword">let</span> &#123; type &#125; = args
      <span class="hljs-keyword">return</span> store.dispatch(type, payload)
    &#125;,

    <span class="hljs-attr">commit</span>: noNamespace ? store.commit : <span class="hljs-function">(<span class="hljs-params">_type, _payload, _options</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> args = unifyObjectStyle(_type, _payload, _options)
      <span class="hljs-keyword">const</span> &#123; payload, options &#125; = args
      <span class="hljs-keyword">let</span> &#123; type &#125; = args
      store.commit(type, payload, options)
    &#125;
  &#125;
  <span class="hljs-built_in">Object</span>.defineProperties(local, &#123;
    <span class="hljs-attr">getters</span>: &#123;
      <span class="hljs-attr">get</span>: noNamespace
        ? <span class="hljs-function">() =></span> store.getters
        : <span class="hljs-function">() =></span> makeLocalGetters(store, namespace)
    &#125;,
    <span class="hljs-attr">state</span>: &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> getNestedState(store.state, path)
    &#125;
  &#125;)

  <span class="hljs-keyword">return</span> local
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 <strong>makeLocalContext</strong> 返回了一个 local对象，local对象的目的是为该<code>module</code>设置局部的 <code>dispatch</code>、<code>commit</code>方法以及<code>getters</code>和<code>state</code>（由于<code>namespace</code>的存在需要做兼容处理）</p>
<p>定义local环境后，循环注册该<code>module</code>下的 <code>mutations</code> <code>actions</code> <code>getter</code></p>
<h4 data-id="heading-8">registerMutation</h4>
<p>注册 mutation</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.forEachMutation(<span class="hljs-function">(<span class="hljs-params">mutation, key</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> namespacedType = namespace + key
  registerMutation(store, namespacedType, mutation, local)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerMutation</span> (<span class="hljs-params">store, type, handler, local</span>) </span>&#123;
  <span class="hljs-comment">// 通过 namespace 找到当前模块的 mutations</span>
  <span class="hljs-keyword">const</span> entry = store._mutations[type] || (store._mutations[type] = [])
  <span class="hljs-comment">// 循环注册mutations</span>
  entry.push(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrappedMutationHandler</span> (<span class="hljs-params">payload</span>) </span>&#123;
    <span class="hljs-comment">// 将 store 绑定到每一个 mutation 的 this 上 然后把 local.state 作为第一个参数传入到每一个mutation中，这也是为什么我们在使用commit的时候第一个参数为当前 module 的 state</span>
    <span class="hljs-comment">// commit实际调用的不是我们传入的handler，而是经过封装的</span>
    handler.call(store, local.state, payload)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">registerAction</h4>
<p>注册 <code>action</code> 的过程和 注册 <code>mutation</code> 的过程差不多，需要注意的是 <code>action</code> 被重新封装后 会返回一个 <code>Promise</code> 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.forEachAction(<span class="hljs-function">(<span class="hljs-params">action, key</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> type = action.root ? key : namespace + key
  <span class="hljs-comment">// 兼容写法</span>
  <span class="hljs-keyword">const</span> handler = action.handler || action
  registerAction(store, type, handler, local)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerAction</span> (<span class="hljs-params">store, type, handler, local</span>) </span>&#123;
  <span class="hljs-keyword">const</span> entry = store._actions[type] || (store._actions[type] = [])
  entry.push(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrappedActionHandler</span> (<span class="hljs-params">payload</span>) </span>&#123;
    <span class="hljs-comment">// 传入 dispatch commit 等参数供我们调用 action 时作为第一个参数使用</span>
    <span class="hljs-keyword">let</span> res = handler.call(store, &#123;
      <span class="hljs-attr">dispatch</span>: local.dispatch,
      <span class="hljs-attr">commit</span>: local.commit,
      <span class="hljs-attr">getters</span>: local.getters,
      <span class="hljs-attr">state</span>: local.state,
      <span class="hljs-attr">rootGetters</span>: store.getters,
      <span class="hljs-attr">rootState</span>: store.state
    &#125;, payload)
    <span class="hljs-comment">// 使用 action 需要 浏览器支持 Promise</span>
    <span class="hljs-keyword">if</span> (!isPromise(res)) &#123;
      res = <span class="hljs-built_in">Promise</span>.resolve(res)
    &#125;
    <span class="hljs-keyword">if</span> (store._devtoolHook) &#123;
      <span class="hljs-keyword">return</span> res.catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        store._devtoolHook.emit(<span class="hljs-string">'vuex:error'</span>, err)
        <span class="hljs-keyword">throw</span> err
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> res
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">registerGetter</h4>
<p><code>getters</code> 处理同理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.forEachGetter(<span class="hljs-function">(<span class="hljs-params">getter, key</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> namespacedType = namespace + key
  registerGetter(store, namespacedType, getter, local)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerGetter</span> (<span class="hljs-params">store, type, rawGetter, local</span>) </span>&#123;
  <span class="hljs-comment">// getters只允许存在一个处理函数，getter重复需要报错</span>
  <span class="hljs-keyword">if</span> (store._wrappedGetters[type]) &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[vuex] duplicate getter key: <span class="hljs-subst">$&#123;type&#125;</span>`</span>)
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 存储封装后的getters处理函数</span>
  store._wrappedGetters[type] = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrappedGetter</span> (<span class="hljs-params">store</span>) </span>&#123;
    <span class="hljs-comment">//  传入 state getters 等参数供我们调用 getters 时作为第一个参数使用</span>
    <span class="hljs-keyword">return</span> rawGetter(
      local.state, <span class="hljs-comment">// local state</span>
      local.getters, <span class="hljs-comment">// local getters</span>
      store.state, <span class="hljs-comment">// root state</span>
      store.getters <span class="hljs-comment">// root getters</span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这样我们就给 store 注册了 actions mutations getters</p>
</blockquote>
<h3 data-id="heading-11">resetStoreVM</h3>
<p>这一步主要就是让 <code>store</code> 中的 <code>state</code> 和 <code>getter</code> 实现响应的一步，把 <code>state</code> 和 <code>getter</code> 都绑定到一个 <code>Vue</code> 的实例上实现数据的响应式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resetStoreVM</span> (<span class="hljs-params">store, state, hot</span>) </span>&#123;
  <span class="hljs-comment">// 缓存之前的 vue 实例</span>
  <span class="hljs-keyword">const</span> oldVm = store._vm

  store.getters = &#123;&#125;
 
  store._makeLocalGettersCache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  <span class="hljs-keyword">const</span> wrappedGetters = store._wrappedGetters
  <span class="hljs-keyword">const</span> computed = &#123;&#125;
  forEachValue(wrappedGetters, <span class="hljs-function">(<span class="hljs-params">fn, key</span>) =></span> &#123;

    computed[key] = partial(fn, store)
    <span class="hljs-comment">// 通过Object.defineProperty为每一个getter方法设置get方法，比如获取this.$store.getters.test的时候获取的是store._vm.test，也就是Vue对象的computed属性</span>
    <span class="hljs-built_in">Object</span>.defineProperty(store.getters, key, &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> store._vm[key],
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// for local getters</span>
    &#125;)
  &#125;)


  <span class="hljs-keyword">const</span> silent = Vue.config.silent
  Vue.config.silent = <span class="hljs-literal">true</span>
  <span class="hljs-comment">// 这里 new Vue() 并把 state 和 getter 绑定到实例上 实现响应式</span>
  store._vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">$$state</span>: state
    &#125;,
    computed
  &#125;)
  Vue.config.silent = silent

  <span class="hljs-keyword">if</span> (store.strict) &#123;
    enableStrictMode(store)
  &#125;

  <span class="hljs-keyword">if</span> (oldVm) &#123;
    <span class="hljs-comment">// 解除旧的vue实例对state的引用，并销毁旧的Vue对象</span>
    <span class="hljs-keyword">if</span> (hot) &#123;
      store._withCommit(<span class="hljs-function">() =></span> &#123;
        oldVm._data.$$state = <span class="hljs-literal">null</span>
      &#125;)
    &#125;
    Vue.nextTick(<span class="hljs-function">() =></span> oldVm.$destroy())
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单来说就是通过 <code>new Vue()</code> 把 <code>state</code> 和 <code>getter</code> 绑定到 <code>Vue</code> 的实例上 实现响应式，然后吧 <code>Vue</code> 的实例绑定到 <code>store</code> 的 <code>_vm</code> 属性上。</p>
<p>到这里 <code>Store</code>的实例化过程的主流程就分析完毕了。</p>
<p>最后来看看我们最常用到的 <code>commit</code> 和 <code>dispatch</code> 方法</p>
<h3 data-id="heading-12">commit</h3>
<pre><code class="hljs language-js copyable" lang="js">  commit (_type, _payload, _options) &#123;
    <span class="hljs-comment">// 处理不同的传参方式</span>
    <span class="hljs-keyword">const</span> &#123;
      type,
      payload,
      options
    &#125; = unifyObjectStyle(_type, _payload, _options)

    <span class="hljs-keyword">const</span> mutation = &#123; type, payload &#125;
    <span class="hljs-comment">// 找到对应的 mutation 方法</span>
    <span class="hljs-keyword">const</span> entry = <span class="hljs-built_in">this</span>._mutations[type]
    <span class="hljs-keyword">if</span> (!entry) &#123;
      <span class="hljs-keyword">if</span> (__DEV__) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[vuex] unknown mutation type: <span class="hljs-subst">$&#123;type&#125;</span>`</span>)
      &#125;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 通过 _withCommit 来执行 mutation</span>
    <span class="hljs-built_in">this</span>._withCommit(<span class="hljs-function">() =></span> &#123;
      entry.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitIterator</span> (<span class="hljs-params">handler</span>) </span>&#123;
        handler(payload)
      &#125;)
    &#125;)
  <span class="hljs-comment">// 订阅者函数遍历执行，传入当前的mutation对象和当前的state</span>
    <span class="hljs-built_in">this</span>._subscribers
      .slice() <span class="hljs-comment">// shallow copy to prevent iterator invalidation if subscriber synchronously calls unsubscribe</span>
      .forEach(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub(mutation, <span class="hljs-built_in">this</span>.state))

    <span class="hljs-keyword">if</span> (
      __DEV__ &&
      options && options.silent
    ) &#123;
      <span class="hljs-built_in">console</span>.warn(
        <span class="hljs-string">`[vuex] mutation type: <span class="hljs-subst">$&#123;type&#125;</span>. Silent option has been removed. `</span> +
        <span class="hljs-string">'Use the filter functionality in the vue-devtools'</span>
      )
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>_withCommit</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js">_withCommit (fn) &#123;
  <span class="hljs-keyword">const</span> committing = <span class="hljs-built_in">this</span>._committing
  <span class="hljs-comment">// 只有通过 _withCommit 执行 mutation '_committing' 才为 true</span>
  <span class="hljs-built_in">this</span>._committing = <span class="hljs-literal">true</span>
  fn()
  <span class="hljs-comment">// 执行完毕 _committing 重新置为 false</span>
  <span class="hljs-comment">// 这也是为什么 mutation 必须为 同步函数的原因，只有为同步函数才能正确的等待 mutatuion执行完毕后修改 _committing 的值</span>
  <span class="hljs-built_in">this</span>._committing = committing
&#125;

<span class="hljs-comment">// 监听对state的修改，若 _committing 不为 true 则抛出警告</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enableStrictMode</span> (<span class="hljs-params">store</span>) </span>&#123;
  <span class="hljs-comment">// this._data.$$state 指向 store 的 state</span>
  store._vm.$watch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._data.$$state &#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      assert(store._committing, <span class="hljs-string">`do not mutate vuex store state outside mutation handlers.`</span>)
    &#125;
  &#125;, &#123; <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">sync</span>: <span class="hljs-literal">true</span> &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">dispatch</h3>
<pre><code class="hljs language-js copyable" lang="js">dispatch (_type, _payload) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>, <span class="hljs-string">'this'</span>)
    <span class="hljs-comment">// check object-style dispatch</span>
    <span class="hljs-keyword">const</span> &#123;
      type,
      payload
    &#125; = unifyObjectStyle(_type, _payload)

    <span class="hljs-keyword">const</span> action = &#123; type, payload &#125;
    <span class="hljs-comment">// 找到对应的 action 方法</span>
    <span class="hljs-keyword">const</span> entry = <span class="hljs-built_in">this</span>._actions[type]
    <span class="hljs-keyword">if</span> (!entry) &#123;
      <span class="hljs-keyword">if</span> (__DEV__) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[vuex] unknown action type: <span class="hljs-subst">$&#123;type&#125;</span>`</span>)
      &#125;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-built_in">this</span>._actionSubscribers
        .slice() <span class="hljs-comment">// shallow copy to prevent iterator invalidation if subscriber synchronously calls unsubscribe</span>
        .filter(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub.before)
        .forEach(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub.before(action, <span class="hljs-built_in">this</span>.state))
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (__DEV__) &#123;
        <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`[vuex] error in before action subscribers: `</span>)
        <span class="hljs-built_in">console</span>.error(e)
      &#125;
    &#125;

    <span class="hljs-comment">// 执行 action 并返回一个 Promise</span>
    <span class="hljs-keyword">const</span> result = entry.length > <span class="hljs-number">1</span>
      ? <span class="hljs-built_in">Promise</span>.all(entry.map(<span class="hljs-function"><span class="hljs-params">handler</span> =></span> handler(payload)))
      : entry[<span class="hljs-number">0</span>](payload)
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      result.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-built_in">this</span>._actionSubscribers
            .filter(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub.after)
            .forEach(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub.after(action, <span class="hljs-built_in">this</span>.state))
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          <span class="hljs-keyword">if</span> (__DEV__) &#123;
            <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`[vuex] error in after action subscribers: `</span>)
            <span class="hljs-built_in">console</span>.error(e)
          &#125;
        &#125;
        resolve(res)
      &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-built_in">this</span>._actionSubscribers
            .filter(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub.error)
            .forEach(<span class="hljs-function"><span class="hljs-params">sub</span> =></span> sub.error(action, <span class="hljs-built_in">this</span>.state, error))
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          <span class="hljs-keyword">if</span> (__DEV__) &#123;
            <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`[vuex] error in error action subscribers: `</span>)
            <span class="hljs-built_in">console</span>.error(e)
          &#125;
        &#125;
        reject(error)
      &#125;)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">最后</h2>
<p>文章只介绍了 vuex 的主流程代码，源码中还有一些辅助函数、工具函数类似<code>mapState</code>、<code>mapGetters</code>、<code>mapActions</code>、<code>mapMutations</code>等等，有兴趣的可以打开源码看看。</p>
<p>第一次写文章，如果大家发现有错误或者疑问，再或者哪里没写明白的地方，欢迎评论指出。</p></div>  
</div>
            