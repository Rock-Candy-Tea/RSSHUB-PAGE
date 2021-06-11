
---
title: 'Vuex 原理解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3632'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 16:55:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=3632'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>Vue 本身具备响应式的状态，组件间也可以通过 props/emit 等方式进行通信，但是，当页面达到一定的复杂程度，多个视图共享同一状态，且当多个视图发出的行为需要变更状态时，单向数据流的简洁性就变得容易被破坏，难以维护。</p>
<p>Vuex 是专门为 Vue 应用程序开发的状态管理模式，是 Flux 架构的一种实现，将状态抽离出来作为 Store 层，当 View 层发起修改，会要求 Store 进行变更，变更之后再通知 View 更新视图，这样组件就可以从繁琐的组件通信解脱出来，只需关注视图层的逻辑。</p>
<h2 data-id="heading-1">工作原理</h2>
<p>为什么 vuex 只能用于 vue，因为 vuex 本质是一个 vue 插件，依赖于 vue 的响应式系统，使用 vuex 的第一步是通过 <code>Vue.use(Vuex)</code> 应用 vuex，查看源码，有对外暴露 <code>install</code> 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">_Vue</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (Vue && _Vue === Vue) <span class="hljs-keyword">return</span>
  Vue = _Vue
  applyMixin(Vue)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当应用 vuex 时，会调用 <code>applyMixin</code> 方法，下面是核心代码，通过 <code>Vue.mixin</code> 注册一个全局 mixin，在所有组件的 <code>beforeCreate</code> 阶段，都会调用 <code>vuexInit</code>，向组件实例注入 store</p>
<p><code>new Vue</code> 需要传入 store 实例，根实例执行 vuexInit 时，可以从 options 获取到 store，然后保存在 <code>$store</code> 属性，由于父组件先于子组件执行 <code>beforeCreate</code>，因此子组件执行 vuexInit 时总能够获取到父组件的 <code>$store</code>，然后保存起来，这也是为什么我们可以在任意组件直接通过 <code>this.$store</code> 获取到 store 实例。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.mixin(&#123; <span class="hljs-attr">beforeCreate</span>: vuexInit &#125;)

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vuexInit</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> options = <span class="hljs-built_in">this</span>.$options
    <span class="hljs-comment">// store injection</span>
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
<h2 data-id="heading-2">核心原理</h2>
<p>store 实例通过 <code>new Vuex.Store</code> 创建，由此可见 vuex 对外暴露一个 Store 类，下面来看核心模块的实现原理</p>
<h3 data-id="heading-3">State</h3>
<p>在 vue 中，我们通过 <code>store.state</code> 获取 state，从下面代码可知，<code>store.state</code> 实际上是 <code>this._vm._data.$$state</code> 的代理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">options = &#123;&#125;</span>) &#123;
    <span class="hljs-built_in">this</span>._modules = <span class="hljs-keyword">new</span> ModuleCollection(options)
    <span class="hljs-keyword">const</span> state = <span class="hljs-built_in">this</span>._modules.root.state
    resetStoreVM(<span class="hljs-built_in">this</span>, state)
  &#125;
  get state () &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._vm._data.$$state
  &#125;
  set state (v) &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      assert(<span class="hljs-literal">false</span>, <span class="hljs-string">`use store.replaceState() to explicit replace store state.`</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建 Store 实例会调用 <code>resetStoreVM(this, state)</code>，下面是核心代码，可以看到 store 内部创建了一个 vue 实例，<strong>由此可见，store 内部新建了一个没有 template 的 vue 实例，而 state 就是该实例的响应式属性 <code>$state</code></strong>，对 state 的修改，实际上就跟在普通组件中修改状态没有区别。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resetStoreVM</span> (<span class="hljs-params">store, state, hot</span>) </span>&#123;
  store.getters = &#123;&#125;
  <span class="hljs-keyword">const</span> wrappedGetters = store._wrappedGetters
  <span class="hljs-keyword">const</span> computed = &#123;&#125;
  forEachValue(wrappedGetters, <span class="hljs-function">(<span class="hljs-params">fn, key</span>) =></span> &#123;
    computed[key] = partial(fn, store)
    <span class="hljs-built_in">Object</span>.defineProperty(store.getters, key, &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> store._vm[key],
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// for local getters</span>
    &#125;)
  &#125;)
  store._vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">$$state</span>: state
    &#125;,
    computed
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Getters</h3>
<p>由上面代码可知，getters 实际上是 <code>computed</code></p>
<h2 data-id="heading-5">小结</h2>
<p>Vuex 是一个 vue 插件，非常轻量，这得益于 vue 的响应式系统，Store 内部维护了一个 Vue 实例对象，state/getters 本质是 Vue 实例的 data 和 computed，</p></div>  
</div>
            