
---
title: '最易懂的Vue源码解析-响应式原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9c8240f641b4285996e069656985f5c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 20:53:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9c8240f641b4285996e069656985f5c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近看了下vue的源码(2.0版)，决定就核心部分-响应式原理做一个沉淀，欢迎感兴趣的小伙伴阅读</p>
<h1 data-id="heading-1">源码解析</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9c8240f641b4285996e069656985f5c~tplv-k3u1fbpfcp-watermark.image" alt="Trigger.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是官方给的流程图，为了方便理解，我将从以下顺序进行分析</p>
<ol>
<li>Data部分，Vue对data做了什么</li>
<li>为什么要进行依赖收集，又是怎么收集的</li>
<li>Watcher是什么，在其中起了什么作用</li>
<li>组件的re-render是在什么时候怎么触发的</li>
</ol>
<h2 data-id="heading-2">1.双向绑定</h2>
<p>在看源码之前我们就知道，Vue是<strong>MVVM</strong>的框架，能将数据做到<strong>双向绑定</strong>，它对<code>data</code>的每个属性都用<code>Object.defineProperty</code>定义了<code>getter</code>和<code>setter</code>，但人家肯定不是这一句话就写完的，具体是怎么<strong>实现</strong>的呢？</p>
<h3 data-id="heading-3">data初始化</h3>
<p>让我们打开Vue的<strong>源码</strong>，翻到<code>vue/src/core/instance</code>，选择这个目录是因为里面的代码基本都是一些<strong>初始化</strong>的操作，里面一定会有对<code>data</code>的初始化</p>
<p>根据程序员的<strong>直觉</strong>，我们先看看<code>index.js</code>，可以看到里面主要执行了几个方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
initMixin(Vue)
stateMixin(Vue)
eventsMixin(Vue)
lifecycleMixin(Vue)
renderMixin(Vue)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们看下<strong>第一个</strong>函数<code>initMixin</code>，根据引入目录，我们在<code>init.js</code>中找到了这个<strong>函数</strong>，看到在里面又执行了几个<strong>方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// init.js</span>
initLifecycle(vm) <span class="hljs-comment">// 初始化生命周期</span>
initEvents(vm) <span class="hljs-comment">// 初始化时间</span>
initRender(vm) <span class="hljs-comment">// 初始化render</span>
callHook(vm, <span class="hljs-string">'beforeCreate'</span>) <span class="hljs-comment">// 触发beforeCreate</span>
initInjections(vm) <span class="hljs-comment">// resolve injections before data/props</span>
initState(vm) <span class="hljs-comment">// 上面是before，下面是after，中间是什么？</span>
initProvide(vm) <span class="hljs-comment">// resolve provide after data/props</span>
callHook(vm, <span class="hljs-string">'created'</span>) <span class="hljs-comment">// 触发created</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据<strong>命名和注释</strong>，我猜<code>data</code>的<strong>初始化</strong>应该是在<code>initState</code>函数中</p>
<p>果然！在<code>state.js</code>里的<code>initState</code>中幸运的找到了<code>initData</code>函数！不亏是大框架层级真深。。。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6656110ca632456aab3ae6a9b7b3127d~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// state.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  vm._watchers = []
  <span class="hljs-keyword">const</span> opts = vm.$options
  <span class="hljs-keyword">if</span> (opts.props) initProps(vm, opts.props)
  <span class="hljs-keyword">if</span> (opts.methods) initMethods(vm, opts.methods)
  <span class="hljs-keyword">if</span> (opts.data) &#123;
    initData(vm) <span class="hljs-comment">// here~</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    observe(vm._data = &#123;&#125;, <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>)
  &#125;
  <span class="hljs-keyword">if</span> (opts.computed) initComputed(vm, opts.computed)
  <span class="hljs-keyword">if</span> (opts.watch && opts.watch !== nativeWatch) &#123;
    initWatch(vm, opts.watch)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了<strong>初始化</strong><code>data</code>，这个函数里还<strong>处理</strong>了<code>props</code>、<code>methods</code>、<code>computed</code>和<code>watch</code>，这里不多解释，感兴趣的可以自己去看看</p>
<p>这次我们重点看<code>initData</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// state.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-keyword">let</span> data = vm.$options.data
  data = vm._data = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span>
    ? getData(data, vm)
    : data || &#123;&#125;
  <span class="hljs-keyword">if</span> (!isPlainObject(data)) &#123;
    data = &#123;&#125;
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
      <span class="hljs-string">'data functions should return an object:\n'</span> +
      <span class="hljs-string">'https://vuejs.org/v2/guide/components.html#data-Must-Be-a-Function'</span>,
      vm
    )
  &#125;
  <span class="hljs-comment">// 上面代码的意思是要求data必须返回一个函数 至于为什么可以进上面链接看官方解释</span>
  
  <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(data)
  <span class="hljs-keyword">const</span> props = vm.$options.props
  <span class="hljs-keyword">const</span> methods = vm.$options.methods
  <span class="hljs-keyword">let</span> i = keys.length
  <span class="hljs-keyword">while</span> (i--) &#123;
    <span class="hljs-keyword">const</span> key = keys[i]
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-keyword">if</span> (methods && hasOwn(methods, key)) &#123;
        warn(
          <span class="hljs-string">`Method "<span class="hljs-subst">$&#123;key&#125;</span>" has already been defined as a data property.`</span>,
          vm
        )
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (props && hasOwn(props, key)) &#123;
      process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
        <span class="hljs-string">`The data property "<span class="hljs-subst">$&#123;key&#125;</span>" is already declared as a prop. `</span> +
        <span class="hljs-string">`Use prop default value instead.`</span>,
        vm
      )
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!isReserved(key)) &#123;
      proxy(vm, <span class="hljs-string">`_data`</span>, key)
    &#125;
  &#125;
  <span class="hljs-comment">// 上面代码意思method、data、props里字段命名不能冲突</span>

  observe(data, <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，其实<strong>重点的操作</strong>在最后的<code>observe</code>函数</p>
<h3 data-id="heading-4">observer</h3>
<p>顺着<code>observe</code>的<strong>引入目录</strong>我们来到<code>vue/src/core/observer</code>，在<code>index.js</code>中找到了这个<strong>函数本体</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-comment">/**
 * Attempt to create an observer instance for a value,
 * returns the new observer if successfully observed,
 * or the existing observer if the value already has one.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span> (<span class="hljs-params">value: any, asRootData: ?boolean</span>): <span class="hljs-title">Observer</span> | <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">if</span> (!isObject(value) || value <span class="hljs-keyword">instanceof</span> VNode) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-keyword">let</span> ob: Observer | <span class="hljs-keyword">void</span>
  <span class="hljs-keyword">if</span> (hasOwn(value, <span class="hljs-string">'__ob__'</span>) && value.__ob__ <span class="hljs-keyword">instanceof</span> Observer) &#123;
    ob = value.__ob__
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
    shouldObserve &&
    !isServerRendering() &&
    (<span class="hljs-built_in">Array</span>.isArray(value) || isPlainObject(value)) &&
    <span class="hljs-built_in">Object</span>.isExtensible(value) &&
    !value._isVue
  ) &#123;
    ob = <span class="hljs-keyword">new</span> Observer(value) 
  &#125;
  <span class="hljs-keyword">if</span> (asRootData && ob) &#123;
    ob.vmCount++
  &#125;
  <span class="hljs-keyword">return</span> ob
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合<strong>注释和代码</strong>我们大概了解这段代码其实就做了一件事情：<strong>返回一个新的<code>Observer</code>或者返回已存在的<code>Observer</code></strong></p>
<p><code>Observer</code>是啥？又干了什么事？不着急，慢慢往下看</p>
<p>刚说到<code>new</code>了下<code>Observer</code>，所以我们直接看<code>Observer</code>类的<strong>构造函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-title">constructor</span> (<span class="hljs-params">value: any</span>) &#123;
  <span class="hljs-built_in">this</span>.value = value
  <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
  <span class="hljs-built_in">this</span>.vmCount = <span class="hljs-number">0</span>
  def(value, <span class="hljs-string">'__ob__'</span>, <span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
    <span class="hljs-keyword">if</span> (hasProto) &#123;
      protoAugment(value, arrayMethods)
    &#125; <span class="hljs-keyword">else</span> &#123;
      copyAugment(value, arrayMethods, arrayKeys)
    &#125;
    <span class="hljs-built_in">this</span>.observeArray(value)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">this</span>.walk(value)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，我们的<code>data</code>通过<code>observe</code>改名为<code>value</code>然后传到<code>constructor</code>最终被做了这样的<strong>处理</strong>：<strong>数组</strong>的话执行<code>observerArray</code>函数，<strong>不是数组</strong>则执行<code>walk</code>函数，而这两个函数<strong>源码</strong>就放在了构造函数<strong>下面</strong>很容易就找到了！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-comment">/**
 * Walk through all properties and convert them into
 * getter/setters. This method should only be called when
 * value type is Object.
 */</span>
walk (obj: <span class="hljs-built_in">Object</span>) &#123;
  <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(obj)
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < keys.length; i++) &#123;
    <span class="hljs-comment">// 把data每一项都definRective</span>
    defineReactive(obj, keys[i])
  &#125;
&#125;

<span class="hljs-comment">/**
 * Observe a list of Array items.
 */</span>
observeArray (items: <span class="hljs-built_in">Array</span><any>) &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = items.length; i < l; i++) &#123;
    <span class="hljs-comment">// 将数组遍历，把每一项再observe，最终还是相当于每一项都definRective</span>
    observe(items[i])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以最终都会到达<code>defineReactive</code>函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-comment">/**
 * Define a reactive property on an Object.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span> (<span class="hljs-params">
  obj: <span class="hljs-built_in">Object</span>,
  key: string,
  val: any,
  customSetter?: ?<span class="hljs-built_in">Function</span>,
  shallow?: boolean
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()

  <span class="hljs-keyword">const</span> property = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj, key)
  <span class="hljs-keyword">if</span> (property && property.configurable === <span class="hljs-literal">false</span>) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// cater for pre-defined getter/setters</span>
  <span class="hljs-keyword">const</span> getter = property && property.get
  <span class="hljs-keyword">const</span> setter = property && property.set
  <span class="hljs-keyword">if</span> ((!getter || setter) && <span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">2</span>) &#123;
    val = obj[key]
  &#125;

  <span class="hljs-keyword">let</span> childOb = !shallow && observe(val)
  
  <span class="hljs-comment">// 定义getter和setter</span>
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveGetter</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">const</span> value = getter ? getter.call(obj) : val
      <span class="hljs-keyword">if</span> (Dep.target) &#123;
        dep.depend()
        <span class="hljs-keyword">if</span> (childOb) &#123;
          childOb.dep.depend()
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
            dependArray(value)
          &#125;
        &#125;
      &#125;
      <span class="hljs-keyword">return</span> value
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveSetter</span> (<span class="hljs-params">newVal</span>) </span>&#123;
      <span class="hljs-keyword">const</span> value = getter ? getter.call(obj) : val
      <span class="hljs-comment">/* eslint-disable no-self-compare */</span>
      <span class="hljs-keyword">if</span> (newVal === value || (newVal !== newVal && value !== value)) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">/* eslint-enable no-self-compare */</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && customSetter) &#123;
        customSetter()
      &#125;
      <span class="hljs-comment">// #7981: for accessor properties without setter</span>
      <span class="hljs-keyword">if</span> (getter && !setter) <span class="hljs-keyword">return</span>
      <span class="hljs-keyword">if</span> (setter) &#123;
        setter.call(obj, newVal)
      &#125; <span class="hljs-keyword">else</span> &#123;
        val = newVal
      &#125;
      childOb = !shallow && observe(newVal)
      dep.notify()
    &#125;
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">getter和setter</h3>
<p>这个函数看起来很长，其实可以<strong>归纳</strong>如下：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 1.创建了个dep</span>
 <span class="hljs-keyword">const</span> dep=<span class="hljs-keyword">new</span> Dep()

 <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveGetter</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 2.判断target存在，就执行depend()，这里就是收集依赖</span>
    <span class="hljs-keyword">if</span> (Dep.target) &#123;
          dep.depend()
        &#125;
      <span class="hljs-keyword">return</span> value
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveSetter</span> (<span class="hljs-params">newVal</span>) </span>&#123;
    val = newVal

        <span class="hljs-comment">// 3.通知依赖更新</span>
        dep.notify()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样是不是就简单多啦，所以可以看出<code>Vue</code>的<code>data</code>就是在这里被<strong>定义</strong><code>getter</code>和<code>setter</code>的</p>
<p>当我们对<code>data</code>执行<code>get</code>操作时就会<strong>触发</strong><code>getter</code>，执行<code>set</code>操作时就会<strong>触发</strong><code>setter</code></p>
<blockquote>
<p>思考1：如果我动态往data里新加一个属性a，操作a是否会触发getter和setter？<br> 答案：不会 <a href="https://cn.vuejs.org/v2/api/#Vue-set" target="_blank" rel="nofollow noopener noreferrer">cn.vuejs.org/v2/api/#Vue…</a></p>
</blockquote>
<blockquote>
<p>思考2：在Vue中我们用push方法向data的某个数组变量中增加一个属性，会触发setter吗？结论是会的，Vue对数组方法做了特殊处理，想知道时怎么处理的话就去源码(observer/array.js)中寻找答案吧~</p>
</blockquote>
<h2 data-id="heading-6">2.观察者模式</h2>
<h3 data-id="heading-7">Dep</h3>
<p>我们注意到<code>getter</code>和<code>setter</code>中有个<strong>出现频率很高</strong>的词——<code>dep</code>。那么<code>dep</code>是什么，又是怎么通过它进行<strong>依赖收集</strong>呢？</p>
<p>顺着<strong>引入路径</strong>，我们来到<code>observer/dep.js</code>，<code>defineReactive</code>归纳后我标注的<strong>1、2、3</strong>三个步骤的操作分别对应如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dep.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-keyword">static</span> target: ?Watcher;
  id: number;
  subs: <span class="hljs-built_in">Array</span><Watcher>;
  
  <span class="hljs-comment">// 1.new Dep()时创建了空的subs，这是用来存依赖的数组</span>
  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-built_in">this</span>.id = uid++
    <span class="hljs-built_in">this</span>.subs = []
  &#125;
  
  <span class="hljs-comment">// 2.dep.depend() 执行了target的addDep()</span>
  depend () &#123;
    <span class="hljs-keyword">if</span> (Dep.target) &#123;
      Dep.target.addDep(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;
  
  <span class="hljs-comment">// 3.dep.notify()对subs数组里每个项执行了update，也就是通知每个依赖更新</span>
  notify () &#123;
    <span class="hljs-comment">// stabilize the subscriber list first</span>
    <span class="hljs-keyword">const</span> subs = <span class="hljs-built_in">this</span>.subs.slice()
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && !config.async) &#123;
      <span class="hljs-comment">// subs aren't sorted in scheduler if not running async</span>
      <span class="hljs-comment">// we need to sort them now to make sure they fire in correct</span>
      <span class="hljs-comment">// order</span>
      subs.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a.id - b.id)
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = subs.length; i < l; i++) &#123;
      subs[i].update()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么一看，好像没有向<strong>依赖数组<code>subs</code>存入内容</strong>的操作，因为<code>depend</code>函数也并没有对<code>subs</code>做类似<code>push</code>的行为，<code>收集依赖</code>的步骤在哪呢？</p>
<p>好奇的小伙伴肯定注意到了<code>target</code>，这又是啥，从哪来的，是做啥的？</p>
<p>其实这是理解<strong>依赖收集</strong>的关键，通过在<code>dep.js</code>中<strong>搜索</strong>'target'我们在上面代码第一行看到关于<code>target</code><strong>类型</strong>的定义是一个<code>Watcher</code>类，然后在最下面<strong>搜到</strong>这样的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dep.js</span>

<span class="hljs-comment">// The current target watcher being evaluated.</span>
<span class="hljs-comment">// This is globally unique because only one watcher</span>
<span class="hljs-comment">// can be evaluated at a time.</span>
Dep.target = <span class="hljs-literal">null</span>
<span class="hljs-keyword">const</span> targetStack = []

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushTarget</span> (<span class="hljs-params">target: ?Watcher</span>) </span>&#123;
  targetStack.push(target)
  Dep.target = target
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">popTarget</span> (<span class="hljs-params"></span>) </span>&#123;
  targetStack.pop()
  Dep.target = targetStack[targetStack.length - <span class="hljs-number">1</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>target</code>应该就是在这里被<strong>注入灵魂</strong>的，注释上说<code>Dep.target</code>必须保持全局<strong>有且只有一个</strong>，这也解释了这段代码的功能，也是为什么在<strong>依赖收集</strong>时可以直接判断<code>Dep.target</code></p>
<p>那这俩函数<code>pushTarget</code>和<code>popTarget</code>在哪<strong>调用</strong>的呢？而<code>Watcher</code>，根据命名和平时的使用，我们猜测，<code>Watcher</code>应该是个能观察到<strong>数据变化</strong>的工具，先去<code>Watcher</code>里看看吧</p>
<h3 data-id="heading-8">Watcher--观察者</h3>
<p>带着疑惑我们打开了<code>observer/watcher.js</code>，果然在里面找到了<code>pushTarget</code>和<code>popTarget</code>的调用！它在一个名叫<code>get</code>的函数里</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher.js</span>

  <span class="hljs-comment">/**
   * Evaluate the getter, and re-collect dependencies.
   */</span>
  get () &#123;
    <span class="hljs-comment">// 1.赋值target Dep.target = this</span>
    pushTarget(<span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">let</span> value
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>.vm
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 2.执行this.getter</span>
      value = <span class="hljs-built_in">this</span>.getter.call(vm, vm)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
        handleError(e, vm, <span class="hljs-string">`getter for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> e
      &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// 3.收集完成后删掉target</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.deep) &#123;
        traverse(value)
      &#125;
      popTarget()
      <span class="hljs-built_in">this</span>.cleanupDeps()
    &#125;
    <span class="hljs-keyword">return</span> value
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，<code>target</code>被<strong>赋值</strong>了<code>this</code>，也就是当前的<code>Watcher</code></p>
<p>那<code>this.getter</code>是什么呢，我们在<code>Watcher</code>的<strong>构造函数</strong>中找到了他</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher.js</span>

<span class="hljs-comment">// expOrFn是创建Watcher时传进来的，要观察的表达式，这里把表达式转成了getter函数</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> expOrFn === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-built_in">this</span>.getter = expOrFn
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.getter = parsePath(expOrFn)
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.getter) &#123;
        <span class="hljs-built_in">this</span>.getter = noop
        process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
          <span class="hljs-string">`Failed watching path: "<span class="hljs-subst">$&#123;expOrFn&#125;</span>" `</span> +
          <span class="hljs-string">'Watcher only accepts simple dot-delimited paths. '</span> +
          <span class="hljs-string">'For full control, use a function instead.'</span>,
          vm
        )
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以<code>this.getter</code>相当于是<strong>观察内容的的赋值逻辑</strong>，怎么理解呢：</p>
<p>举例我创建了一个<code>Watcher</code>观察一个属性<code>a</code>，而<code>a</code>的<strong>赋值逻辑</strong>为<code>data.b + data.c</code>，那么<code>this.getter</code>就相当于<strong>执行</strong>了<code>data.b + data.c</code></p>
<p>接着在<strong>构造函数</strong>中我们也幸运的找到了上面提到的<code>get</code>函数的<strong>调用位置</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher.js</span>

<span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.lazy
      ? <span class="hljs-literal">undefined</span>
      : <span class="hljs-built_in">this</span>.get()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">依赖收集</h3>
<p>现在我们已经解开了大部分<strong>谜题</strong>，为了方便<strong>理解</strong>，我们模拟一下<strong>整个流程</strong>，还是刚才的例子，我们有一个变量<code>a</code>，而<code>a</code>的<strong>赋值逻辑</strong>涉及了<code>data.b</code>和<code>data.c</code></p>
<p>现在我们<code>new Watcher()</code>把它传入，然后走到了<strong>构造函数</strong>，执行<code>this.get()</code>，<code>get()</code>会创建<code>target=Watcher</code>并执行<code>this.getter()</code>，而<code>this.getter()</code>就相当于执行<code>a</code>的<strong>赋值逻辑</strong>，就会 <strong>“触碰”</strong> 到<code>data.b</code>和<code>data.c</code>，因为<code>data</code>所有属性都在<strong>初始化</strong>的时候被定义了<code>getter</code>和<code>setter</code>，当被 <strong>“触碰”</strong> 就会触发<code>data.b</code>和<code>data.c</code>的<code>getter</code></p>
<p><strong>前方高能</strong></p>
<p>也就是执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// observe.js</span>

<span class="hljs-comment">// 创建Watcher与data的桥梁dep（记住是data.b或data.c的dep，跟a无关）</span>
<span class="hljs-keyword">const</span> dep=<span class="hljs-keyword">new</span> Dep()

<span class="hljs-comment">// getter：</span>
<span class="hljs-keyword">if</span> (Dep.target) &#123;
    <span class="hljs-comment">// target有吗？有的，刚才get()里创建了，值为当前Watcher</span>
    dep.depend()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// observe.js</span>

dep.depend()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等于</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dep.js</span>

Dep.target.addDep(<span class="hljs-built_in">this</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是执行<code>Watcher</code>里的<code>addDep</code>:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher.js</span>

addDep (dep: Dep) &#123;
    <span class="hljs-keyword">const</span> id = dep.id
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.newDepIds.has(id)) &#123;
      <span class="hljs-built_in">this</span>.newDepIds.add(id)
      <span class="hljs-built_in">this</span>.newDeps.push(dep)
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.depIds.has(id)) &#123;
        <span class="hljs-comment">// 上面代码是一些判重处理 对本期主题不重要</span>
        dep.addSub(<span class="hljs-built_in">this</span>)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等于</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher.js</span>

dep.addSub(<span class="hljs-built_in">this</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等于</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dep.js</span>

addSub (sub: Watcher) &#123;
  <span class="hljs-built_in">this</span>.subs.push(sub)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是这样，兜兜转转，最终<code>data.b</code>和<code>data.c</code>的<code>subs</code>里成功放入了<code>a</code>的<code>Watcher</code>，也就完成了<strong>依赖收集</strong>的步骤！</p>
<h3 data-id="heading-10">依赖更新</h3>
<p><strong>依赖收集</strong>完了，<strong>Watcher</strong>存好了，怎么更新的呢？</p>
<p>假设现在<code>data.b</code>或<code>data.c</code>被<code>set</code>了新的值，那么就会<strong>触发</strong>他们的<code>setter</code>：</p>
<p><strong>继续高能</strong></p>
<p>也就是执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// observe.js</span>

<span class="hljs-comment">// setter:</span>
dep.notify()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// dep.js</span>

 notify () &#123;
    <span class="hljs-comment">// stabilize the subscriber list first</span>
    <span class="hljs-keyword">const</span> subs = <span class="hljs-built_in">this</span>.subs.slice()
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && !config.async) &#123;
      <span class="hljs-comment">// subs are not sorted in scheduler if not running async</span>
      <span class="hljs-comment">// we need to sort them now to make sure they fire in correct</span>
      <span class="hljs-comment">// order</span>

      subs.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a.id - b.id)
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = subs.length; i < l; i++) &#123;
      <span class="hljs-comment">// here~ 这里subs里只有一个，就是a的Watcher</span>
      subs[i].update()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher.js</span>

update () &#123;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.lazy) &#123;
      <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
      <span class="hljs-built_in">this</span>.run()
    &#125; <span class="hljs-keyword">else</span> &#123;
      queueWatcher(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认会走到<code>this.run()</code>，其他两种模式这次就先不做解释啦</p>
<pre><code class="hljs language-js copyable" lang="js">run () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.active) &#123;
      <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.get()
      
      <span class="hljs-comment">// 下面是一些value变化后回调逻辑</span>
      <span class="hljs-keyword">if</span> (
        value !== <span class="hljs-built_in">this</span>.value ||
        <span class="hljs-comment">// Deep watchers and watchers on Object/Arrays should fire even</span>
        <span class="hljs-comment">// when the value is the same, because the value may</span>
        <span class="hljs-comment">// have mutated.</span>
        isObject(value) ||
        <span class="hljs-built_in">this</span>.deep
      ) &#123;
        <span class="hljs-comment">// set new value</span>
        <span class="hljs-keyword">const</span> oldValue = <span class="hljs-built_in">this</span>.value
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            handleError(e, <span class="hljs-built_in">this</span>.vm, <span class="hljs-string">`callback for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
        &#125;
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>约等于</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.value=<span class="hljs-built_in">this</span>.get()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>get</code>函数刚刚有解释哦，里面会执行<code>a</code>的<strong>赋值逻辑</strong>，<code>a</code>就顺利被<strong>更新</strong>了！</p>
<p>至此，整条<strong>响应式链路</strong>就理清楚了！</p>
<h3 data-id="heading-11">组件的响应式</h3>
<p>当然a、b、c都是我的<strong>举例</strong>，实际<strong>组件的响应式</strong>和例子也很相似。</p>
<p>首先每一个<strong>组件</strong>就相当于例子中的<strong>a</strong>，都会配一个<code>Watcher</code>，只不过而组件的<strong>赋值逻辑</strong>有一个<strong>专属函数</strong>，也就是<strong>渲染函数</strong><code>render</code></p>
<p><code>render</code>执行过程中就会生成<code>DOM</code>，而<code>DOM</code>中所需要的<code>data</code>就相当于例子中的<code>b、c</code>一样会被 <strong>“触碰”</strong> ，然后就像<strong>例子</strong>中一样，往所有<code>data</code>的<strong>依赖</strong>中放入<strong>组件</strong>的<code>Watcher</code></p>
<p>当<code>data</code>变化时就会<strong>触发</strong><code>Watcher</code>的执行<strong>赋值逻辑</strong><code>re-render</code>，然后<strong>组件</strong>就成功被<strong>更新</strong>啦~</p>
<blockquote>
<p>思考：这部分源码在哪里呢？试着找到然后研究下？</p>
</blockquote>
<h1 data-id="heading-12">总结</h1>
<ul>
<li><strong>Watcher</strong>的作用印证了我们的猜想，它就是一个观察者，可以观察一个数据变化</li>
<li><strong>Dep</strong>则是一个订阅者，主要的作用就是收集依赖也就是收集观察者Watcher和通知观察者更新</li>
<li><strong>Observer</strong>的主要作用是使用<code>Object.defineProperty</code>方法对<code>Data</code>的每一个子属性定义<code>getter</code>和<code>setter</code>，然后劫持他们的<code>get</code>和<code>set</code>操作</li>
</ul>
<p>——————————————end——————————————</p>
<p>才疏学浅，大佬轻喷~</p></div>  
</div>
            