
---
title: 'Vue2 源码总结梳理 -「大大的源码」'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c493a1b890d94794abdacfc26b6839c2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 00:49:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c493a1b890d94794abdacfc26b6839c2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>这段时间利用课余时间夹杂了很多很多事把 Vue2 源码学习了一遍，但很多都是跟着视频大概过了一遍，也都画了自己的思维导图。但还是对详情的感念模糊不清，<strong>故这段时间对源码进行了总结梳理。</strong></p>
<blockquote>
<p>本篇文章更合适于<strong>已看过 Vue2 源码</strong>，进一步总结加深概念的人群。若还未读过源码或<strong>零碎一知半解</strong>的小伙伴，也可以挑选阶段进行总结梳理，<strong>个人还是强烈认为需要过一遍源码</strong>。</p>
</blockquote>
<h1 data-id="heading-1">目录结构</h1>
<pre><code class="copyable">├── benchmarks                  性能、基准测试
├── dist                        构建打包的输出目录
├── examples                    案例目录
├── flow                        flow 语法的类型声明
├── packages                    一些额外的包，比如：负责服务端渲染的包 vue-server-renderer、配合 vue-loader 使用的的 vue-template-compiler，还有 weex 相关的
│   ├── vue-server-renderer
│   ├── vue-template-compiler
│   ├── weex-template-compiler
│   └── weex-vue-framework
├── scripts                     所有的配置文件的存放位置，比如 rollup 的配置文件
├── src                         vue 源码目录
│   ├── compiler                编译器
│   ├── core                    运行时的核心包
│   │   ├── components          全局组件，比如 keep-alive
│   │   ├── config.js           一些默认配置项
│   │   ├── global-api          全局 API，比如熟悉的：Vue.use()、Vue.component() 等
│   │   ├── instance            Vue 实例相关的，比如 Vue 构造函数就在这个目录下
│   │   ├── observer            响应式原理
│   │   ├── util                工具方法
│   │   └── vdom                虚拟 DOM 相关，比如熟悉的 patch 算法就在这儿
│   ├── platforms               平台相关的编译器代码
│   │   ├── web
│   │   └── weex
│   ├── server                  服务端渲染相关
├── test                        测试目录
├── types                       TS 类型声明

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>来自 <a href="https://juejin.cn/post/6949370458793836580#heading-16" target="_blank">juejin.cn/post/694937…</a></p>
</blockquote>
<h1 data-id="heading-2">Vue 初始化</h1>
<blockquote>
<p>位置：<code>/src/core/instance/index.js</code></p>
</blockquote>
<h2 data-id="heading-3">入口</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Vue 的构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
    !(<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> Vue)
  ) &#123;
    warn(<span class="hljs-string">'Vue is a constructor and should be called with the `new` keyword'</span>)
  &#125;
  <span class="hljs-comment">// 在 /src/core/instance/init.js，</span>
  <span class="hljs-comment">// 1.初始化组件实例关系属性</span>
  <span class="hljs-comment">// 2.自定义事件的监听</span>
  <span class="hljs-comment">// 3.插槽和渲染函数</span>
  <span class="hljs-comment">// 4.触发 beforeCreate 钩子函数</span>
  <span class="hljs-comment">// 5.初始化 inject 配置项</span>
  <span class="hljs-comment">// 6.初始化响应式数据，如 props, methods, data, computed, watch</span>
  <span class="hljs-comment">// 7.初始化解析 provide</span>
  <span class="hljs-comment">// 8.触发 created 钩子函数</span>
  <span class="hljs-built_in">this</span>._init(options)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">核心代码</h2>
<p><em>源码核心代码顺序以深度遍历形式</em></p>
<h3 data-id="heading-5">initMixin</h3>
<blockquote>
<p>位置：<code>/src/core/instance/init.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span> (<span class="hljs-params">Vue: Class<Component></span>) </span>&#123;
  <span class="hljs-comment">// 负责 Vue 的初始化过程</span>
  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options?: <span class="hljs-built_in">Object</span></span>) </span>&#123;
    vm._self = vm<span class="hljs-comment">// 将 vm 挂载到实例 _self 上</span>

    <span class="hljs-comment">// 初始化组件实例关系属性，比如 $parent、$children、$root、$refs...</span>
    initLifecycle(vm)

    <span class="hljs-comment">// 自定义事件的监听：谁注册，谁监听</span>
    initEvents(vm)

    <span class="hljs-comment">// 插槽信息：vm.$slot</span>
    <span class="hljs-comment">// 渲染函数：vm.$createElement（创建元素）</span>
    initRender(vm)

    <span class="hljs-comment">// beforeCreate 钩子函数</span>
    callHook(vm, <span class="hljs-string">'beforeCreate'</span>)

    <span class="hljs-comment">// 初始化组件的 inject 配置项</span>
    initInjections(vm)

    <span class="hljs-comment">// 数据响应式：props、methods、data、computed、watch</span>
    initState(vm)

    <span class="hljs-comment">// 解析实例 vm.$options.provide 对象，挂载到 vm._provided 上，和 inject 对应。</span>
    initProvide(vm)

    <span class="hljs-comment">// 调用 created 钩子函数</span>
    callHook(vm, <span class="hljs-string">'created'</span>)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">致命五问</h2>
<blockquote>
<p>Vue 源码「初始化」致命五问。</p>
<ol>
<li><code>beforeCreate</code> 钩子函数前完成了什么？</li>
<li>父子组件中，子组件调用执行本身注册的自定义事件 A()，那么父子组件中，谁监听事件 A() 的执行调用？</li>
<li><code>created</code> 钩子函数前完成了什么？</li>
<li><code>initInjections(vm)</code>、<code>initState(vm)</code>、<code>initProvide(vm)</code> 三者的执行顺序可否变化？</li>
<li>Vue 的初始化过程？</li>
</ol>
<p><em>思考问题后，答案在下方，根据自己阅读整理源码，对自己提出有意义的问题并自我回答。不确保是面试热点题噢（切勿入题太深）</em></p>
</blockquote>
<h2 data-id="heading-7">致命五答</h2>
<h3 data-id="heading-8">一答</h3>
<blockquote>
<p>问：beforeCreate 钩子函数前完成了什么？</p>
</blockquote>
<blockquote>
<p>答：beforeCreate 之前，主要是在处理 vm 实例上的各种属性配置和自定义事件属性，也就是<strong>将 Vue 的壳初始化完成</strong>。<br>
首先合并了组件的配置项挂载到全局 vm.$options 上。初始化组件实例关系属性，如：$parent、$children、$root、$refs 等等，然后初始化自定义的事件监听，最后初始化组件的插槽 slot 和作用域插槽scopedSlots，createElement（即 render 函数，同时定义了组件 attrs 和 $listeners属性。）</p>
</blockquote>
<h3 data-id="heading-9">二答</h3>
<blockquote>
<p>问：父子组件中，子组件调用执行本身注册的自定义事件 A()，那么父子组件中，谁监听事件 A() 的执行调用？</p>
</blockquote>
<blockquote>
<p>答：谁注册了自定义事件，则谁监听自定义事件。故是子组件监听事件。</p>
</blockquote>
<h3 data-id="heading-10">三答</h3>
<blockquote>
<p>问：created 钩子函数前完成了什么？</p>
</blockquote>
<blockquote>
<p>答：<strong>created 钩子函数是在 Vue 壳构建完成后，开始初始化实例的响应式数据和方法。</strong><br>
首先初始化好 inject 配置项，再初始化各种响应式数据和方法如：props、methods、data、computed、watch，最后初始化 vm._provided 属性。</p>
</blockquote>
<h3 data-id="heading-11">四答</h3>
<blockquote>
<p>问：initInjections(vm)、initState(vm)、initProvide(vm) 三者的执行顺序可否变化？</p>
</blockquote>
<blockquote>
<p>答：不可以，源码中有官方注释。<br>
inject 配置项是注入数据，在后续的 computed 和 data 中均可以或需要使用注入数据，故解析 injections 需要在 data/props 前。<br>
解析 provide 实际上只是将 vm.$options.provide 挂载到 vm._providedinject 上，需要等响应式数据和方法初始化完毕后再执行。inject 和 provide 是成对出现的，一个注入，一个接收。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    initInjections(vm) <span class="hljs-comment">// resolve injections before data/props</span>
    initState(vm)
    initProvide(vm) <span class="hljs-comment">// resolve provide after data/props</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">五答</h3>
<blockquote>
<p>问：Vue 的初始化过程？</p>
</blockquote>
<blockquote>
<p>答：Vue 初始化过程其实就是 beforeCreate 钩子函数和 created 钩子函数前执行的内容。</p>
<ul>
<li>在 beforeCreate 前，主要先初始化搭建了 Vue 实例的壳，如组件的 options 配置项，组件实例的关系属性，处理了自定义事件。</li>
<li>在 created 前，主要是初始化实例的响应式数据和方法，首先初始化 inject 配置项，再初始化数据响应式和方法，最后解析组件配置项上的 provide 对象。总结来说构建初始化 Vue 实例对象 vm。</li>
</ul>
</blockquote>
<h1 data-id="heading-13">响应式原理</h1>
<blockquote>
<p>位置：<code>/src/core/instance/index.js</code></p>
</blockquote>
<h2 data-id="heading-14">入口</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始化数据响应式：props、methods、data、computed、watch</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span> (<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-comment">// 初始化当前实例的 watchers 数组</span>
  vm._watchers = []
  <span class="hljs-comment">// 拿到上边初始化合并后的 options 配置项</span>
  <span class="hljs-keyword">const</span> opts = vm.$options
  
  <span class="hljs-comment">// props 响应式，挂载到 vm</span>
  <span class="hljs-keyword">if</span> (opts.props) initProps(vm, opts.props)
  
  <span class="hljs-comment">// 1. 判断 methods 是否为函数</span>
  <span class="hljs-comment">// 2. 方法名与 props 判重</span>
  <span class="hljs-comment">// 3. 挂载到 vm</span>
  <span class="hljs-keyword">if</span> (opts.methods) initMethods(vm, opts.methods)
  
  <span class="hljs-keyword">if</span> (opts.data) &#123;
    <span class="hljs-comment">// 初始化 data 并挂载到 vm</span>
    initData(vm)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 响应式 data 上的数据</span>
    observe(vm._data = &#123;&#125;, <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>)
  &#125;
  
<span class="hljs-comment">// 1. 创建 watcher 实例，默认是懒执行，并挂载到 vm 上</span>
  <span class="hljs-comment">// 2. computed 与上列 props、methods、data 判重</span>
  <span class="hljs-keyword">if</span> (opts.computed) initComputed(vm, opts.computed)
  
  <span class="hljs-comment">// 1. 处理 watch 对象与 watcher 实例的关系（一对一、一对多）</span>
  <span class="hljs-comment">// 2. watch 的格式化和配置项</span>
  <span class="hljs-keyword">if</span> (opts.watch && opts.watch !== nativeWatch) &#123;
    initWatch(vm, opts.watch)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">核心代码</h2>
<p><em>源码核心代码顺序以深度遍历形式</em></p>
<h3 data-id="heading-16">observe</h3>
<blockquote>
<p>位置：<code>/src/core/observer/index.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为对象创建观察者 Observe</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span> (<span class="hljs-params">value: any, asRootData: ?boolean</span>): <span class="hljs-title">Observer</span> | <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-comment">// 非对象和 VNode 实例不做响应式处理</span>
  <span class="hljs-keyword">if</span> (!isObject(value) || value <span class="hljs-keyword">instanceof</span> VNode) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-keyword">let</span> ob: Observer | <span class="hljs-keyword">void</span>
  <span class="hljs-comment">// 若 value 对象上存在 __ob__ 属性并且实例是 Observer 则表示已经做过观察了，直接返回 __ob__ 属性。</span>
  <span class="hljs-keyword">if</span> (hasOwn(value, <span class="hljs-string">'__ob__'</span>) && value.__ob__ <span class="hljs-keyword">instanceof</span> Observer) &#123;
    ob = value.__ob__
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
    <span class="hljs-comment">// 一堆判断对象的条件</span>
    shouldObserve &&
    !isServerRendering() &&
    (<span class="hljs-built_in">Array</span>.isArray(value) || isPlainObject(value)) &&
    <span class="hljs-built_in">Object</span>.isExtensible(value) &&
    !value._isVue
  ) &#123;
    <span class="hljs-comment">// 创建观察者实例</span>
    ob = <span class="hljs-keyword">new</span> Observer(value)
  &#125;
<span class="hljs-comment">// </span>
  <span class="hljs-keyword">if</span> (asRootData && ob) &#123;
    ob.vmCount++
  &#125;
  <span class="hljs-keyword">return</span> ob
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">Observer</h3>
<blockquote>
<p>位置：<code>/src/core/observer/index.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 监听器类</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-comment">// ... 配置</span>
  <span class="hljs-title">constructor</span> (<span class="hljs-params">value: any</span>) &#123;
    <span class="hljs-built_in">this</span>.value = value
    <span class="hljs-comment">// 实例化一个发布者 Dep</span>
    <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
    <span class="hljs-built_in">this</span>.vmCount = <span class="hljs-number">0</span>
    def(value, <span class="hljs-string">'__ob__'</span>, <span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
      <span class="hljs-comment">// ...处理数组</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// value 为对象，为对象的每个属性设置响应式</span>
      <span class="hljs-comment">// 也就是为啥响应式对象属性的对象也是响应式</span>
      <span class="hljs-built_in">this</span>.walk(value)
    &#125;
  &#125;

<span class="hljs-comment">// 值为对象时</span>
  walk (obj: <span class="hljs-built_in">Object</span>) &#123;
    <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(obj)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < keys.length; i++) &#123;
      <span class="hljs-comment">// 设置响应式对象</span>
      defineReactive(obj, keys[i])
    &#125;
  &#125;

<span class="hljs-comment">// 值为数组时</span>
  observeArray (items: <span class="hljs-built_in">Array</span><any>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = items.length; i < l; i++) &#123;
      <span class="hljs-comment">// 判断，优化，创建观察者实例</span>
      observe(items[i])
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">Dep</h3>
<blockquote>
<p>位置：<code>/src/core/observer/dep.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 订阅器类</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 该 dep 发布者的 id</span>
    <span class="hljs-built_in">this</span>.id = uid++
    <span class="hljs-comment">// 存放订阅者</span>
    <span class="hljs-built_in">this</span>.subs = []
  &#125;

  <span class="hljs-comment">// 添加订阅者</span>
  addSub (sub: Watcher) &#123;
    <span class="hljs-built_in">this</span>.subs.push(sub)
  &#125;

  <span class="hljs-comment">// 添加订阅者</span>
  removeSub (sub: Watcher) &#123;
    remove(<span class="hljs-built_in">this</span>.subs, sub)
  &#125;

  <span class="hljs-comment">// 向订阅者中添加当前 dep</span>
  <span class="hljs-comment">// 在 Watcher 中也有这个操作，实现双向绑定</span>
  depend () &#123;
    <span class="hljs-keyword">if</span> (Dep.target) &#123;
      Dep.target.addDep(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;

  <span class="hljs-comment">// 通知 dep 中的所有 watcher，执行 watcher.update() 方法</span>
  notify () &#123;
    <span class="hljs-comment">// ...省略代码</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">Watcher</h3>
<blockquote>
<p>位置：<code>/src/core/observer/watcher.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 订阅者类，一个组件一个 watcher，订阅的数据改变时执行相应的回调函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  ...代码省略：<span class="hljs-title">constructor</span>(<span class="hljs-params"></span>) 构造配置一个 <span class="hljs-title">watcher</span>

  <span class="hljs-title">get</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 打开 Dep.target，Dep.target = this</span>
    pushTarget(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// value 为回调函数执行的结果</span>
    <span class="hljs-keyword">let</span> value
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>.vm
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 这里执行 updateComponent，进入 patch 阶段更新视图。</span>
      value = <span class="hljs-built_in">this</span>.getter.call(vm, vm)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-comment">// ...捕获异常</span>
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// "touch" every property so they are all tracked as</span>
      <span class="hljs-comment">// dependencies for deep watching</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.deep) &#123;
        traverse(value)
      &#125;
      <span class="hljs-comment">// 最后清除 watcher 实例的各种依赖收集</span>
      popTarget()
      <span class="hljs-built_in">this</span>.cleanupDeps()
    &#125;
    <span class="hljs-keyword">return</span> value
  &#125;

  addDep (dep: Dep) &#123;
    <span class="hljs-keyword">const</span> id = dep.id
    <span class="hljs-comment">// watcher 订阅着 dep 发布者并进行缓存判重</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.newDepIds.has(id)) &#123;
      <span class="hljs-comment">// 缓存 dep 发布者</span>
      <span class="hljs-built_in">this</span>.newDepIds.add(id)
      <span class="hljs-built_in">this</span>.newDeps.push(dep)
      
      <span class="hljs-comment">// 发布者收集订阅者 watcher</span>
      <span class="hljs-comment">// 在 dep 中也有这个操作，实现双向绑定</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.depIds.has(id)) &#123;
        dep.addSub(<span class="hljs-built_in">this</span>)
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Clean up for dependency collection.
   */</span>
  cleanupDeps () &#123;
    <span class="hljs-comment">// ...代码省略</span>
    <span class="hljs-comment">// 清除 dep 发布者的依赖收集</span>
  &#125;

<span class="hljs-comment">// 订阅者 update() 更新</span>
  update () &#123;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-comment">// // 懒执行如 computed</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.lazy) &#123;
      <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
      
    <span class="hljs-comment">// 同步执行，watcher 实例的一个配置项</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
      <span class="hljs-comment">// 同步执行，在使用 vm.$watch 或者 watch 选项时可以传一个 sync 选项，</span>
      <span class="hljs-built_in">this</span>.run()
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 大部分 watcher 更新进入 watcher 的队列</span>
      queueWatcher(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;

<span class="hljs-comment">// 1. 同步执行时会调用</span>
<span class="hljs-comment">// 2. 浏览器异步队列刷新 flushSchedulerQueue() 会调用</span>
  run () &#123;
    <span class="hljs-comment">// ...代码省略，active = false 直接返回</span>
    <span class="hljs-comment">// 使用 this.get() 获取新值来更新旧值</span>
    <span class="hljs-comment">// 并且执行 cb 回调函数，将新值和旧值返回。</span>
  &#125;

<span class="hljs-comment">// 订阅者 watcher 懒执行</span>
  evaluate () &#123;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get()
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-comment">/**
   * Depend on all deps collected by this watcher.
   */</span>
  depend () &#123;
    <span class="hljs-comment">// 调用当前 watcher 依赖的所有 dep 发布者的 depend()</span>
    <span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.deps.length
    <span class="hljs-keyword">while</span> (i--) &#123;
      <span class="hljs-built_in">this</span>.deps[i].depend()
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Remove self from all dependencies' subscriber list.
   */</span>
  teardown () &#123;
    <span class="hljs-comment">// ...销毁该 watcher 实例</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">defineReactive</h3>
<blockquote>
<p>位置：<code>/src/core/observer/index.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 设置响应式对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span> (<span class="hljs-params">
  obj: <span class="hljs-built_in">Object</span>,
  key: string,
  val: any,
  customSetter?: ?<span class="hljs-built_in">Function</span>,
  shallow?: boolean
</span>) </span>&#123;
...省略
  <span class="hljs-comment">// 响应式核心</span>
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    
    <span class="hljs-comment">// get 拦截对象的读取操作</span>
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveGetter</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">const</span> value = getter ? getter.call(obj) : val
      <span class="hljs-keyword">if</span> (Dep.target) &#123;
        
        <span class="hljs-comment">// 依赖收集并通知实现发布者 dep 和订阅者 watcher 的双向绑定</span>
        dep.depend()
        
        <span class="hljs-comment">// 依赖收集对象属性中的对象</span>
        <span class="hljs-keyword">if</span> (childOb) &#123;
          childOb.dep.depend()
          <span class="hljs-comment">// 数组情况</span>
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
            <span class="hljs-comment">// 为数组项为对象的项添加依赖</span>
            dependArray(value)
          &#125;
        &#125;
      &#125;
      <span class="hljs-keyword">return</span> value
    &#125;,
    
    <span class="hljs-comment">// set 拦截对对象的设置操作</span>
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveSetter</span> (<span class="hljs-params">newVal</span>) </span>&#123;
      <span class="hljs-keyword">const</span> value = getter ? getter.call(obj) : val
      <span class="hljs-comment">// 无新值，不用更新则直接 return</span>
      <span class="hljs-keyword">if</span> (newVal === value || (newVal !== newVal && value !== value)) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">// 没有 setter，只读属性，则直接 return</span>
      <span class="hljs-keyword">if</span> (getter && !setter) <span class="hljs-keyword">return</span>
      
      <span class="hljs-comment">// 设置新值</span>
      <span class="hljs-keyword">if</span> (setter) &#123;
        setter.call(obj, newVal)
      &#125; <span class="hljs-keyword">else</span> &#123;
        val = newVal
      &#125;
      <span class="hljs-comment">// 将新值进行响应式</span>
      childOb = !shallow && observe(newVal)
      <span class="hljs-comment">// dep 发布者通知更新</span>
      dep.notify()
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">proxy</h3>
<blockquote>
<p>位置：<code>/src/core/instance/state.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sharedPropertyDefinition = &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">get</span>: noop,
  <span class="hljs-attr">set</span>: noop
&#125;

<span class="hljs-comment">// 为每个属性设置拦截代理，并且挂载到 vm 上（target）</span>
<span class="hljs-comment">// 如 proxy(vm, `_props`, key)、proxy(vm, `_data`, key)</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span> (<span class="hljs-params">target: <span class="hljs-built_in">Object</span>, sourceKey: string, key: string</span>) </span>&#123;
  sharedPropertyDefinition.get = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxyGetter</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[sourceKey][key]
  &#125;
  sharedPropertyDefinition.set = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxySetter</span> (<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-built_in">this</span>[sourceKey][key] = val
  &#125;
  <span class="hljs-built_in">Object</span>.defineProperty(target, key, sharedPropertyDefinition)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">致命五问</h2>
<blockquote>
<p>Vue 源码「响应式原理」致命五问。</p>
<ol>
<li>什么是 MVVM 模式？</li>
<li>Vue 的双向绑定原理？</li>
<li>Vue 如何处理响应式数据？</li>
<li>computed 和 watch 的特性区别？</li>
<li>computed 和 watch 的使用场景区别？</li>
</ol>
<p><em>思考问题后，答案在下方，根据自己阅读整理源码，对自己提出有意义的问题并自我回答。不确保是面试热点题噢（切勿入题太深）</em></p>
</blockquote>
<h2 data-id="heading-23">致命五答</h2>
<h3 data-id="heading-24">一答</h3>
<blockquote>
<p>问：什么是 MVVM 模式？</p>
</blockquote>
<blockquote>
<p>答：MVVM（Model–View–ViewModel ） 是一个软件架构设计模式。其进了前端开发与后端业务逻辑的分离，极大地提高了前端开发效率，MVVM 分为以下三层</p>
<ul>
<li>1.View 视图层，也就是构建出来的用户页面。</li>
<li>2.Model 数据层，就是存放数据状态。</li>
<li>3.ViewModel 视图数据层，是 MVVM 模式的核心层，作为其余两层的中间枢纽，更新视图层且操作改变数据层的状态。</li>
</ul>
</blockquote>
<h3 data-id="heading-25">二答</h3>
<blockquote>
<p>问：Vue 的双向绑定原理？</p>
</blockquote>
<blockquote>
<p>答：Vue 双向绑定采用的是 MVVM 模式。监听器 <code>Observer</code> 、订阅器 <code>Dep</code>、订阅者 <code>Watcher</code>、解析器 <code>Compile</code>。</p>
<ul>
<li>Compile 解析器：扫描和解析每个节点的相关指令，并根据初始化模板数据以及初始化相应的订阅器。</li>
<li>Observer 监听器：调用 defineReactive 劫持并监听所有属性，getter 向 Dep 依赖。</li>
<li>Dep 订阅器：收集观察者 Watcher 和通知观察者目标更新。每个属性拥有自己的消息订阅器dep，用于存放所有订阅了该属性的观察者对象，当数据发生改变时，通知所有的 watch 执行自己的update逻辑。</li>
<li>Watcher 订阅者：观察属性提供回调函数以及收集依赖（如计算属性computed，vue会把该属性所依赖数据的dep添加到自身的deps中），当被观察的值发生变化时，会接收到来自dep的通知，从而触发回调函数。
<ul>
<li>Watcher类的实现比较复杂，因为他的实例分为渲染 watcher（render-watcher）、计算属性 watcher（computed-watcher）、侦听器 watcher（normal-watcher）三种。
<ul>
<li>computed-watcher：我们在组件钩子函数computed中定义，这类 watcher 有个特点：当计算属性依赖于其他数据时，属性并不会立即重新计算，只有之后其他地方需要读取属性的时候，它才会真正计算，即具备 lazy（懒计算）特性。</li>
<li>normal-watcher：我们在组件钩子函数watch 中定义，即只要监听的属性改变了，都会触发定义好的回调函数。</li>
<li>render-watcher：每一个组件都会有一个 render-watcher，当 data/computed 中的属性改变的时候，会调用该 render-watcher 来更新组件的视图。</li>
<li>这三种 watcher 也有固定的<strong>执行顺序</strong>，分别是：<code>computed-render -> normal-watcher -> render-watcher</code>。尽可能的保证，在更新组件视图的时候，computed 属性已经是最新值了，如果 render-watcher 排在 computed-render 前面，就会导致页面更新的时候 computed 值为旧数据。</li>
</ul>
</li>
</ul>
</li>
<li>而 Dep 订阅器和 Watcher 订阅者又是一种<strong>观察者模式</strong>。Watcher 用来订阅属性的变化通，从而更新视图。Dep 用来收集 Watcher 的依赖，当 Observer 更新时，通过 dep.notify() 统一派发给 Watcher，实现了双向绑定。</li>
<li>综上：简单来说通过数据劫持+发布订阅模式，通过以下初始化和更新的过程来实现双向绑定，也就是响应式原理。</li>
<li>初始化：
<ul>
<li>1.Observer 对数据进行响应式绑定</li>
<li>2.Compiler 编译解析模块指令，初始化渲染页面，并将每个指令的节点绑上更新函数，实例化监听监听数据的订阅者 Watcher。</li>
<li>3.数据 getter 时，执行对应数据的 dep 收集所有 watcher 依赖</li>
</ul>
</li>
<li>更新：
<ul>
<li>1.更新时触发 dep.notify()，派发通知所有订阅者 watcher</li>
<li>2.订阅者 watcher 执行 update() 回调函数</li>
<li>3.调用对应 Compiler 编译解析模块，重新更新视图</li>
</ul>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c493a1b890d94794abdacfc26b6839c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-26">三答</h3>
<blockquote>
<p>问：Vue 如何处理响应式数据？</p>
</blockquote>
<blockquote>
<p>答：响应式的数据主要分为两类：Object 和 Array</p>
<ul>
<li>Object 对象则利用 defineReactive()，来循环遍历整个对象，通过 Object.defineProperty 设置 getter 和 setter 的拦截，再通过观察者模式双向绑定来实现对象响应式原理</li>
<li>Array 数组则利用 <code>Array.split()</code> 重写数组的那 7 个可以更改自身的原型方法来实现响应式。</li>
</ul>
</blockquote>
<h3 data-id="heading-27">四答</h3>
<blockquote>
<p>问：computed 和 watch 的特性区别？</p>
</blockquote>
<blockquote>
<p>答：通过源码阅读 computed 和 watch 在本质是没有区别的，都是通过 Watcher 的实例去实现的响应式，主要有以下特性区别。</p>
<ol>
<li>computed 默认为懒执行，dirty 为 true。watch 有 immediate 配置，可以实现立即执行一次 cb。</li>
<li>computed 支持缓存，依赖数据发生改变，才会重新进行计算。watch 不支持缓存，立即响应式变化。</li>
<li>computed 不支持异步。watch 支持异步。</li>
<li>computed 的 cb 函数默认走 get 方法。watch 的 cb 函数第一个参数是新值，第二个参数是旧值。</li>
</ol>
</blockquote>
<h3 data-id="heading-28">五答</h3>
<blockquote>
<p>问：computed 和 watch 的使用场景区别？</p>
</blockquote>
<blockquote>
<p>答：computed 和 watch 使用场景的区别根本原因是因它们的特性不同，大致有以下的场景区别。</p>
<ul>
<li>选择 computed
<ol>
<li>当数据需要缓存时</li>
<li>当数据依赖其他数据计算得到时</li>
<li>逻辑较为简单并无需异步操作时（watch 消耗较大）</li>
</ol>
</li>
<li>选择 watch
<ol>
<li>当执行异步操作时</li>
<li>即时监听数据完成较为复杂的回调函数时</li>
</ol>
</li>
</ul>
</blockquote>
<h1 data-id="heading-29">异步更新</h1>
<p>Vue 源码的异步更新也就是响应式原理的进一步深入，下面引用以下官方对于异步更新的介绍来进一步了解这个概念。</p>
<blockquote>
<p>可能你还没有注意到，Vue 在更新 DOM 时是<strong>异步</strong>执行的。只要侦听到数据变化，Vue 将开启一个队列，并缓冲在同一事件循环中发生的所有数据变更。如果同一个 watcher 被多次触发，只会被推入到队列中一次。这种在缓冲时去除重复数据对于避免不必要的计算和 DOM 操作是非常重要的。然后，在下一个的事件循环“tick”中，Vue 刷新队列并执行实际 (已去重的) 工作。Vue 在内部对异步队列尝试使用原生的 <code>Promise.then</code>、<code>MutationObserver</code> 和 <code>setImmediate</code>，如果执行环境不支持，则会采用 <code>setTimeout(fn, 0)</code> 代替。</p>
<p>例如，当你设置 <code>vm.someData = 'new value'</code>，该组件不会立即重新渲染。当刷新队列时，组件会在下一个事件循环“tick”中更新。多数情况我们不需要关心这个过程，但是如果你想基于更新后的 DOM 状态来做点什么，这就可能会有些棘手。虽然 Vue.js 通常鼓励开发人员使用“数据驱动”的方式思考，避免直接接触 DOM，但是有时我们必须要这么做。为了在数据变化之后等待 Vue 完成更新 DOM，可以在数据变化之后立即使用 <code>Vue.nextTick(callback)</code>。这样回调函数将在 DOM 更新完成后被调用。</p>
</blockquote>
<h2 data-id="heading-30">入口</h2>
<blockquote>
<p>异步更新发生在响应式原理更新 dep.notify() 派发通知给 watcher 调用 update() 更新回调方法。</p>
<p>位置：<code>/src/core/observer/watcher.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// watcher 异步更新入口</span>
update () &#123;
  <span class="hljs-comment">// computed 懒加载走这</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.lazy) &#123;
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
    <span class="hljs-comment">// 当给 watcher 实例设置同步选项，也就是不走异步更新队列，直接执行 this.run() 调用更新</span>
    <span class="hljs-comment">// 这个属性在官方文档中没有出现</span>
    <span class="hljs-built_in">this</span>.run()
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 大部分都走 queueWatcher() 异步更新队列</span>
    queueWatcher(<span class="hljs-built_in">this</span>)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">核心代码</h2>
<p><em>源码核心代码顺序以深度遍历形式</em></p>
<h3 data-id="heading-32">queueWatcher</h3>
<blockquote>
<p>位置：<code>/src/core/observer/scheduler.js</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 将当前 watcher 放入 watcher 的异步更新队列 </span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queueWatcher</span> (<span class="hljs-params">watcher: Watcher</span>) </span>&#123;
  <span class="hljs-keyword">const</span> id = watcher.id
<span class="hljs-comment">// 避免重复添加相同 watcher 进异步更新队列</span>
  <span class="hljs-keyword">if</span> (has[id] == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// 缓存标记</span>
    has[id] = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// flushing 正在刷新队列</span>
    <span class="hljs-keyword">if</span> (!flushing) &#123;
      <span class="hljs-comment">// 直接入队</span>
      queue.push(watcher)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 正在刷新队列</span>
      <span class="hljs-comment">// 将 watcher 按 id 递增顺序放入更新队列中。</span>
      <span class="hljs-keyword">let</span> i = queue.length - <span class="hljs-number">1</span>
      <span class="hljs-keyword">while</span> (i > index && queue[i].id > watcher.id) &#123;
        i--
      &#125;
      <span class="hljs-comment">// 用数组切割方法</span>
      queue.splice(i + <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, watcher)
    &#125;
    <span class="hljs-comment">// queue the flush</span>
    <span class="hljs-comment">// 正在刷新队列</span>
    <span class="hljs-keyword">if</span> (!waiting) &#123;
      <span class="hljs-comment">// 设置标记，确保只有一条异步更新队列</span>
      waiting = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && !config.async) &#123;
        <span class="hljs-comment">// 直接刷新队列：</span>
        <span class="hljs-comment">// 1.异步更新队列 queue 升序排序，确保按 id 顺序执行</span>
        <span class="hljs-comment">// 2.遍历队列调用每个 watcher 的 before()、run() 方法并清除当前 watcher 缓存（也就是 id 置为空）</span>
        <span class="hljs-comment">// 3.调用 resetSchedulerState()，重置异步更新队列，等待下一次更新。（也就是清除缓存，初始化下标，俩标志设为 false）</span>
        flushSchedulerQueue()
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-comment">// 也就是 vm.$nextTick、Vue.nextTick</span>
      <span class="hljs-comment">// 做了两件事：</span>
      <span class="hljs-comment">// 1.将回调函数（flushSchedulerQueue） 放入 callbacks 数组。</span>
      <span class="hljs-comment">// 2.向浏览器任务队列中添加 flushCallbacks 函数，达到下次 DOM 渲染更新后立即调用</span>
      nextTick(flushSchedulerQueue)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">run</h3>
<blockquote>
<p>位置：<code>/src/core/observer/watcher.js</code></p>
<p>调用：flushSchedulerQueue() 遍历调用每个 watcher 的 run()</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 由 刷新队列函数 flushSchedulerQueue 调用，如果是同步 watch，则由 this.update 直接调用，完成如下几件事：
 *   1、执行实例化 watcher 传递的第二个参数，updateComponent 或者 获取 this.xx 的一个函数(parsePath 返回的函数)
 *   2、更新旧值为新值
 *   3、执行实例化 watcher 时传递的第三个参数，比如用户 watcher 的回调函数
 */</span>
run () &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.active) &#123;
    <span class="hljs-comment">// 调用 watcher.get() 获取当前 watcher 的值。</span>
    <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.get()
    <span class="hljs-keyword">if</span> (
      value !== <span class="hljs-built_in">this</span>.value ||
      <span class="hljs-comment">// Deep watchers and watchers on Object/Arrays should fire even</span>
      <span class="hljs-comment">// when the value is the same, because the value may</span>
      <span class="hljs-comment">// have mutated.</span>
      isObject(value) ||
      <span class="hljs-built_in">this</span>.deep
    ) &#123;
      <span class="hljs-comment">// 更新值</span>
      <span class="hljs-keyword">const</span> oldValue = <span class="hljs-built_in">this</span>.value
      <span class="hljs-built_in">this</span>.value = value
<span class="hljs-comment">// 若果是用户定义的 watcher，执行用户 cb 函数，传递新值和旧值。</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          handleError(e, <span class="hljs-built_in">this</span>.vm, <span class="hljs-string">`callback for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 其余走渲染 watcher，this.cb 默认为 noop（空函数）</span>
        <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">nextTick</h3>
<blockquote>
<p>位置：<code>/src/core/util/next-tick.js</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> callbacks = [] 
<span class="hljs-keyword">let</span> pending = <span class="hljs-literal">false</span>

<span class="hljs-comment">// cb 函数是 flushSchedulerQueue 异步函数队列</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextTick</span> (<span class="hljs-params">cb?: <span class="hljs-built_in">Function</span>, ctx?: <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> _resolve
  <span class="hljs-comment">// callbacks 数组推进 try/catch 封装的 cb（避免异步队列中某个 watcher 回调函数发生错误无法排查）</span>
  callbacks.push(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (cb) &#123;
      <span class="hljs-keyword">try</span> &#123;
        cb.call(ctx)
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        handleError(e, ctx, <span class="hljs-string">'nextTick'</span>)
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (_resolve) &#123;
      _resolve(ctx)
    &#125;
  &#125;)
  <span class="hljs-comment">// 执行了 flushCallbacks() 函数，表示当前浏览器异步任务队列无 flushCallbacks 函数</span>
  <span class="hljs-keyword">if</span> (!pending) &#123;
    pending = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// nextTick() 的重点！</span>
    <span class="hljs-comment">// 执行 timerFunc，重新在浏览器的异步任务队列中放入 flushCallbacks 函数</span>
    timerFunc()
  &#125;
  <span class="hljs-comment">// 做 Promise 异常处理</span>
  <span class="hljs-comment">// $flow-disable-line</span>
  <span class="hljs-keyword">if</span> (!cb && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Promise</span> !== <span class="hljs-string">'undefined'</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      _resolve = resolve
    &#125;)
  &#125;
&#125;


<span class="hljs-comment">// timerFunc 将 flushCallbacks 函数放入浏览器的异步任务队列中。</span>
<span class="hljs-comment">// 关键在于放入浏览器异步任务队列的优先级！</span>
<span class="hljs-comment">// 1.Promise.resolve().then(flushCallbacks)</span>
<span class="hljs-comment">// 2.new MutationObserver(flushCallbacks)</span>
<span class="hljs-comment">// 3.setImmediate(flushCallbacks)</span>
<span class="hljs-comment">// 4.setTimeout(flushCallbacks, 0)</span>
<span class="hljs-keyword">let</span> timerFunc
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Promise</span> !== <span class="hljs-string">'undefined'</span> && isNative(<span class="hljs-built_in">Promise</span>)) &#123;
  <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve()
  timerFunc = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 第一选 Promise.resolve().then() 放入 flushCallbacks</span>
    p.then(flushCallbacks)
    <span class="hljs-comment">// 若挂掉了，采用添加空计时器来“强制”刷新微任务队列。</span>
    <span class="hljs-keyword">if</span> (isIOS) <span class="hljs-built_in">setTimeout</span>(noop)
  &#125;
  isUsingMicroTask = <span class="hljs-literal">true</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!isIE && <span class="hljs-keyword">typeof</span> MutationObserver !== <span class="hljs-string">'undefined'</span> && (
  isNative(MutationObserver) ||
  <span class="hljs-comment">// PhantomJS and iOS 7.x</span>
  MutationObserver.toString() === <span class="hljs-string">'[object MutationObserverConstructor]'</span>
)) &#123;
  <span class="hljs-comment">// Use MutationObserver where native Promise is not available,</span>
  <span class="hljs-comment">// e.g. PhantomJS, iOS7, Android 4.4</span>
  <span class="hljs-comment">// (#6466 MutationObserver is unreliable in IE11)</span>
  <span class="hljs-keyword">let</span> counter = <span class="hljs-number">1</span>
  
  <span class="hljs-comment">// 第二选 new MutationObserver(flushCallbacks)</span>
  <span class="hljs-comment">// 创建并返回一个新的 MutationObserver 它会在指定的DOM发生变化时被调用。</span>
  <span class="hljs-comment">// [MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver)</span>
  <span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> MutationObserver(flushCallbacks)
  <span class="hljs-keyword">const</span> textNode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-built_in">String</span>(counter))
  observer.observe(textNode, &#123;
    <span class="hljs-attr">characterData</span>: <span class="hljs-literal">true</span>
  &#125;)
  timerFunc = <span class="hljs-function">() =></span> &#123;
    counter = (counter + <span class="hljs-number">1</span>) % <span class="hljs-number">2</span>
    textNode.data = <span class="hljs-built_in">String</span>(counter)
  &#125;
  isUsingMicroTask = <span class="hljs-literal">true</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> setImmediate !== <span class="hljs-string">'undefined'</span> && isNative(setImmediate)) &#123;
  <span class="hljs-comment">// 第三选 setImmediate()</span>
  timerFunc = <span class="hljs-function">() =></span> &#123;
    setImmediate(flushCallbacks)
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 第四选 setTimeout() 定时器</span>
  timerFunc = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(flushCallbacks, <span class="hljs-number">0</span>)
  &#125;
&#125;


<span class="hljs-comment">// 最终一条浏览器异步队列执行 callbacks 数组中的方法来达到 nextTick() 异步更新调用方法。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushCallbacks</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 设置标记，开启下一次浏览器异步队列更新</span>
  pending = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">const</span> copies = callbacks.slice(<span class="hljs-number">0</span>)
  <span class="hljs-comment">// 清空 callbacks 数组</span>
  callbacks.length = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 执行异步更新队列其中存储的每个 flushSchedulerQueue 函数</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < copies.length; i++) &#123;
    copies[i]()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-35">致命五问</h2>
<blockquote>
<p>Vue 源码「异步更新」致命五问。</p>
<ol>
<li>Vue 响应式原理中的异步更新是如何实现？</li>
<li>Vue 默认更新是同步的还是异步的？</li>
<li>Vue 是如何避免重复执行同一次异步更新？</li>
<li>Vue 的 nextTick 全局 API 是如何实现的？</li>
<li>Vue 是如何将刷新 callbacks 数组的函数放入浏览器任务队列进行异步更新的？</li>
</ol>
<p><em>思考问题后，答案在下方，根据自己阅读整理源码，对自己提出有意义的问题并自我回答。不确保是面试热点题噢（切勿入题太深）</em></p>
</blockquote>
<h2 data-id="heading-36">致命五答</h2>
<h3 data-id="heading-37">一答</h3>
<blockquote>
<p>问：Vue 响应式原理中的异步更新是如何实现？</p>
</blockquote>
<blockquote>
<p>答：Dep 订阅器派发通知给每个 watcher 订阅器，执行 <code>update()</code> 方法开始异步更新。<br>
异步更新原理总体来说是：<code>将 每个 watcher 放入 queue 全局队列中</code> => <code>调用 nextTick() 方法将刷新 watcher 队列的方法 flushSchedulerQueue 放入 callbacks 数组中</code> => <code>将刷新 callbacks 数组的函数 flushCallbacks 通过 timerFunc() 方法放进浏览器的异步任务队列中</code> => <code>最后浏览器遍历执行 callbacks 数组中的刷新 watcher 队列方法 flushSchedulerQueue</code> => <code>刷新 watcher 队列方法遍历执行 queue 队列的每个 watcher.before() 和 watcher.run() 方法</code> => <code>继续下一次异步更新</code>。<br>
以下是 update() 方法详情：</p>
<ol>
<li>首先判断两个特殊标记
<ul>
<li>是否为 lazy 懒更新，则设置 dirty 为 true，以标记当前 watcher 为懒更新</li>
<li>再判断是否有 sync 同步更新标记，直接执行 <code>watcher.run()</code>，Vue 官方不推荐使用，文档没有该属性。</li>
</ul>
</li>
<li>然后将 watcher 放入 queue 队列中，放入队列有两种方式，以 flushing 标志判断
<ul>
<li>若无在刷新队列中，直接 push 进 queue 队列</li>
<li>若正在刷新队列中，按 watcher.id 进行升序排序，确保更新的顺序</li>
</ul>
</li>
<li>然后调用 nextTick()，将 flushSchedulerQueue（刷新当前 watcher 队列的方法）放入 callbacks 数组中。若浏览器的任务队列中无 flushCallbacks 函数，则执行 timerFunc()。（用 pending 来判断控制）</li>
<li>timerFunc() 将 flushCallbacks 函数（执行第 3 点中 callbacks 数组中的所有 flushSchedulerQueue 方法）放入浏览器的异步任务队列中</li>
<li>等待浏览器异步任务队列执行 callbacks 数组中的 flushSchedulerQueue 方法。</li>
<li>每个 flushSchedulerQueue 方法中先将 queue 队列排序，再遍历 queue 执行 watcher.before() 和 watcher.run() 方法，而后再初始化异步更新队列，自此异步更新完成。</li>
</ol>
</blockquote>
<h3 data-id="heading-38">二答</h3>
<blockquote>
<p>问：Vue 默认更新是同步的还是异步的？</p>
</blockquote>
<blockquote>
<p>答：Vue 默认异步更新，通过 <code>watcher.async</code>。Vue 源码还设置了开启同步更新的操作，可以通过设置 <code>watcher.sync</code> 的属性，在 watcher.update() 方法时并直接执行 watcher.run() 方法进行更新操作。<strong>但 Vue 官方不推荐使用该属性，因同步更新机制将阻塞后续任务的执行，整个组件更新将大打折扣。</strong></p>
</blockquote>
<h3 data-id="heading-39">三答</h3>
<blockquote>
<p>问：Vue 是如何避免重复执行同一次异步更新？</p>
</blockquote>
<blockquote>
<p>答：通过三个标识符的操作来进行避免重复执行同一次的异步更新。</p>
</blockquote>
<blockquote>
<ol>
<li>在将 watcher 放入 watcher 队列时，进行了 id 的缓存，避免重复 watcher 添加到 queue 数组。</li>
<li>通过 waiting 判断是否正在刷新 queue 队列，避免重复执行刷新 queue 队列。</li>
<li>通过 pending 判断浏览器的异步任务队列中是否有刷新 callbacks（放的是刷新 queue 队列的任务） 数组的任务，避免浏览器异步任务队列重复执行刷新 callbacks 数组的任务。</li>
</ol>
</blockquote>
<h3 data-id="heading-40">四答</h3>
<blockquote>
<p>问：Vue 的 nextTick 全局 API 是如何实现的？</p>
</blockquote>
<blockquote>
<p>答：Vue.nextTick 将传递的刷新 watcher 队列的回调函数 用 <code>try catch</code> 包裹然后放入 callbacks 数组。<br>
在浏览器异步任务队列无其他刷新 callbacks 数组的方法时，执行 timerFunc 函数，放入当前刷新 callbacks 数组的方法。<br>
进而达到<strong>在下次 DOM 更新循环结束之后执行延迟回调。在修改数据之后立即使用这个方法，获取更新后的 DOM。</strong> 的功能</p>
</blockquote>
<h3 data-id="heading-41">五答</h3>
<blockquote>
<p>问：Vue 是如何将刷新 callbacks 数组的函数放入浏览器任务队列进行异步更新的？</p>
</blockquote>
<blockquote>
<p>答：根据浏览器任务队列异步执行的效率来选择放入方法的优先级，分别为：</p>
<ol>
<li>Promise.resolve().then(flushCallbacks)</li>
<li>new MutationObserver(flushCallbacks)
<ul>
<li>提供了监视对DOM树所做更改的能力（HTML5 中的新特性）</li>
</ul>
</li>
<li>setImmediate(flushCallbacks)</li>
<li>setTimeout(flushCallbacks, 0)</li>
</ol>
</blockquote>
<h1 data-id="heading-42">Vue 全局 API</h1>
<blockquote>
<p>位置：<code>/src/core/global-api/index.js</code></p>
<p>调用: <code>/src/core/index.js</code></p>
</blockquote>
<h2 data-id="heading-43">入口</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始化全局配置和 API</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initGlobalAPI</span> (<span class="hljs-params">Vue: GlobalAPI</span>) </span>&#123;
  <span class="hljs-comment">// 全局配置 config</span>
  <span class="hljs-keyword">const</span> configDef = &#123;&#125;
  configDef.get = <span class="hljs-function">() =></span> config
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    configDef.set = <span class="hljs-function">() =></span> &#123;
      warn(
        <span class="hljs-string">'Do not replace the Vue.config object, set individual fields instead.'</span>
      )
    &#125;
  &#125;
  <span class="hljs-comment">// 给 Vue 挂载全局配置，并拦截。</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue, <span class="hljs-string">'config'</span>, configDef)

  <span class="hljs-comment">// Vue 的全局工具方法: Vue.util.xx</span>
  Vue.util = &#123;
    <span class="hljs-comment">// 警告</span>
    warn,
    <span class="hljs-comment">// 选项扩展</span>
    extend,
    <span class="hljs-comment">// 选项合并</span>
    mergeOptions,
    <span class="hljs-comment">// 设置响应式</span>
    defineReactive
  &#125;

  <span class="hljs-comment">// Vue.set()</span>
  Vue.set = set
  
  <span class="hljs-comment">// Vue.delete()</span>
  <span class="hljs-comment">// 处理操作与下列 set() 基本一致。</span>
  <span class="hljs-comment">// target 为对象时，采用运算符 delete</span>
  Vue.delete = del
  
  <span class="hljs-comment">// Vue.nextTick()</span>
  <span class="hljs-comment">// 不多 BB 就是上节 异步更新原理中的 nextTick</span>
<span class="hljs-comment">// 1.将回调函数（flushSchedulerQueue） 放入 callbacks 数组。</span>
<span class="hljs-comment">// 2.向浏览器任务队列中添加 flushCallbacks 函数，达到下次 DOM 渲染更新后立即调用</span>
  Vue.nextTick = nextTick

  <span class="hljs-comment">// Vue.observable() 响应式方法</span>
  <span class="hljs-comment">// 也不多 BB 就是上上节 响应式原理中的 observe</span>
  <span class="hljs-comment">// 为对象创建一个 Oberver 监听器实例，并监听</span>
  Vue.observable = <T>(obj: T): <span class="hljs-function"><span class="hljs-params">T</span> =></span> &#123;
    observe(obj)
    <span class="hljs-keyword">return</span> obj
  &#125;

  Vue.options = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  <span class="hljs-comment">// ASSET_TYPES = ['component', 'directive', 'filter']</span>
  ASSET_TYPES.forEach(<span class="hljs-function"><span class="hljs-params">type</span> =></span> &#123;
    <span class="hljs-comment">// 初始化挂载 Vue.options.xx 实例对象</span>
    Vue.options[type + <span class="hljs-string">'s'</span>] = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  &#125;)

  <span class="hljs-comment">// Vue.options._base 挂载 Vue 的构造函数</span>
  Vue.options._base = Vue

  <span class="hljs-comment">// 在 Vue.options.components 中扩展内置组件，比如 keep-alive</span>
  <span class="hljs-comment">// 在 /src/shared/utils.js：（for in 挂载）</span>
  extend(Vue.options.components, builtInComponents)

  <span class="hljs-comment">// Vue.use 全局 API：安装 plugin 插件</span>
  <span class="hljs-comment">// 1.installedPlugins 缓存判断当前 plugin 是否已安装</span>
  <span class="hljs-comment">// 2.调用 plugin 的安装并缓存</span>
  initUse(Vue)
  
  <span class="hljs-comment">// Vue.mixin 全局 API：混合配置</span>
  <span class="hljs-comment">// this.options = mergeOptions(this.options, mixin)</span>
  <span class="hljs-comment">// 出现相同配置项时，子选项会覆盖父选项的配置：options[key] = strat(parent[key], child[key], vm, key)</span>
  initMixin(Vue)
  
  <span class="hljs-comment">// Vue.extend 全局 API：扩展一些公共配置或方法</span>
  initExtend(Vue)
  
  <span class="hljs-comment">// Vue.component/directive/filter 全局 API：创造组件实例注册方法</span>
  initAssetRegisters(Vue)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-44">核心代码</h2>
<p><em>源码核心代码顺序以深度遍历形式</em></p>
<h3 data-id="heading-45">set()</h3>
<blockquote>
<p>位置：<code>/src/core/observer/index.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 通过 vm.$set() 方法给对象或数组设置响应式</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span> (<span class="hljs-params">target: <span class="hljs-built_in">Array</span><any> | <span class="hljs-built_in">Object</span>, key: any, val: any</span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-comment">// ...省略代码：警告</span>
  
  <span class="hljs-comment">// 更新数组通过 splice 方法实现响应式更新：vm.$set(array, idx, val)</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(target) && isValidArrayIndex(key)) &#123;
    target.length = <span class="hljs-built_in">Math</span>.max(target.length, key)
    target.splice(key, <span class="hljs-number">1</span>, val)
    <span class="hljs-keyword">return</span> val
  &#125;
  
  <span class="hljs-comment">// 更新已有属性，直接更新最新值：vm.$set(obj, key, val)</span>
  <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> target && !(key <span class="hljs-keyword">in</span> <span class="hljs-built_in">Object</span>.prototype)) &#123;
    target[key] = val
    <span class="hljs-keyword">return</span> val
  &#125;
  
  <span class="hljs-comment">// 设置未定义的对象值</span>
  <span class="hljs-comment">// 获取当前 target 对象的 __ob__，判断是否已被 observer 设置为响应式对象。</span>
  <span class="hljs-keyword">const</span> ob = (target: any).__ob__
  <span class="hljs-comment">// ...省略代码：不能向 _isVue 和 ob.vmCount = 1 的根组件添加新值</span>
  
  <span class="hljs-comment">// 若 target 不是响应式对象，直接往 target 设置静态属性</span>
  <span class="hljs-keyword">if</span> (!ob) &#123;
    target[key] = val
    <span class="hljs-keyword">return</span> val
  &#125;
  <span class="hljs-comment">// 若 target 是响应式对象</span>
  <span class="hljs-comment">// defineReactive() 添加上响应式属性</span>
  <span class="hljs-comment">// 立即调用对象上的订阅器 dep 派发更新</span>
  defineReactive(ob.value, key, val)
  ob.dep.notify()
  <span class="hljs-keyword">return</span> val
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">initExtend</h3>
<blockquote>
<p>位置：/src/core/global-api/extend.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initExtend</span> (<span class="hljs-params">Vue: GlobalAPI</span>) </span>&#123;
 <span class="hljs-comment">// 每个实例构造函数（包括Vue）都有一个唯一的 cid。这使我们能够创建包装的“子对象”，用于原型继承和缓存它们的构造函数。</span>
  Vue.cid = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> cid = <span class="hljs-number">1</span>

  <span class="hljs-comment">// Vue 去扩展子类</span>
  Vue.extend = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">extendOptions: <span class="hljs-built_in">Object</span></span>): <span class="hljs-title">Function</span> </span>&#123;
    extendOptions = extendOptions || &#123;&#125;
    <span class="hljs-keyword">const</span> Super = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> SuperId = Super.cid

    <span class="hljs-comment">// 缓存多次 Vue.extend 使用同一个配置项时</span>
    <span class="hljs-keyword">const</span> cachedCtors = extendOptions._Ctor || (extendOptions._Ctor = &#123;&#125;)
    <span class="hljs-keyword">if</span> (cachedCtors[SuperId]) &#123;
      <span class="hljs-keyword">return</span> cachedCtors[SuperId]
    &#125;

    <span class="hljs-comment">// 是否为有效的配置项名，避免重复</span>
    <span class="hljs-keyword">const</span> name = extendOptions.name || Super.options.name
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && name) &#123;
      validateComponentName(name)
    &#125;

    <span class="hljs-comment">// 定义 Sub 构造函数，准备合并</span>
    <span class="hljs-keyword">const</span> Sub = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">VueComponent</span>(<span class="hljs-params">options</span>) </span>&#123;
      <span class="hljs-comment">// 就是 Vue 实例初始化的 init() 方法</span>
      <span class="hljs-built_in">this</span>._init(options)
    &#125;
    <span class="hljs-comment">// 通过原型继承的方式继承 Vue</span>
    Sub.prototype = <span class="hljs-built_in">Object</span>.create(Super.prototype)
    Sub.prototype.constructor = Sub
    <span class="hljs-comment">// 唯一标识</span>
    Sub.cid = cid++
    <span class="hljs-comment">// 选项合并</span>
    Sub.options = mergeOptions(
      Super.options,
      extendOptions
    )
    <span class="hljs-comment">// 挂载自己的父类</span>
    Sub[<span class="hljs-string">'super'</span>] = Super

    <span class="hljs-comment">// 将上边合并的配置项初始化配置代理到 Sub.prototype._props/_computed 对象上</span>
    <span class="hljs-comment">// 方法在下边</span>
    <span class="hljs-keyword">if</span> (Sub.options.props) &#123;
      initProps(Sub)
    &#125;
    <span class="hljs-keyword">if</span> (Sub.options.computed) &#123;
      initComputed(Sub)
    &#125;

    <span class="hljs-comment">// 实现多态方法</span>
    Sub.extend = Super.extend
    Sub.mixin = Super.mixin
    Sub.use = Super.use

    <span class="hljs-comment">// 实现 component、filter、directive 三个静态方法</span>
    ASSET_TYPES.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type</span>) </span>&#123;
      Sub[type] = Super[type]
    &#125;)

    <span class="hljs-comment">// 递归组件的原理并注册</span>
    <span class="hljs-keyword">if</span> (name) &#123;
      Sub.options.components[name] = Sub
    &#125;

    <span class="hljs-comment">// 在扩展时保留对基类选项的引用，可以检查 Super 的选项是否是最新。</span>
    Sub.superOptions = Super.options
    Sub.extendOptions = extendOptions
    Sub.sealedOptions = extend(&#123;&#125;, Sub.options)

    <span class="hljs-comment">// 缓存</span>
    cachedCtors[SuperId] = Sub
    <span class="hljs-keyword">return</span> Sub
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initProps</span> (<span class="hljs-params">Comp</span>) </span>&#123;
  <span class="hljs-keyword">const</span> props = Comp.options.props
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> props) &#123;
    proxy(Comp.prototype, <span class="hljs-string">`_props`</span>, key)
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initComputed</span> (<span class="hljs-params">Comp</span>) </span>&#123;
  <span class="hljs-keyword">const</span> computed = Comp.options.computed
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> computed) &#123;
    defineComputed(Comp.prototype, key, computed[key])
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">initAssetRegisters</h3>
<blockquote>
<p>位置：/src/core/global-api/assets.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initAssetRegisters</span> (<span class="hljs-params">Vue: GlobalAPI</span>) </span>&#123;
  <span class="hljs-comment">// ASSET_TYPES = ['component', 'directive', 'filter']</span>
  ASSET_TYPES.forEach(<span class="hljs-function"><span class="hljs-params">type</span> =></span> &#123;
    <span class="hljs-comment">// 每个 Vue 上挂载实例注册方法</span>
    Vue[type] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
      id: string,
      definition: <span class="hljs-built_in">Function</span> | <span class="hljs-built_in">Object</span>
    </span>): <span class="hljs-title">Function</span> | <span class="hljs-title">Object</span> | <span class="hljs-title">void</span> </span>&#123;
      <span class="hljs-comment">// 无方法</span>
      <span class="hljs-keyword">if</span> (!definition) &#123;
        <span class="hljs-comment">// 返回空</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.options[type + <span class="hljs-string">'s'</span>][id]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (type === <span class="hljs-string">'component'</span> && isPlainObject(definition)) &#123;
          <span class="hljs-comment">// 组件若为 name，默认为 id</span>
          definition.name = definition.name || id
          <span class="hljs-comment">// 调用 Vue.extend，将该组件进行扩展，也就是可以实例化该组件</span>
          definition = <span class="hljs-built_in">this</span>.options._base.extend(definition)
        &#125;
    <span class="hljs-comment">// bind 绑定和 update 更新指令均调用该 defintion 方法</span>
        <span class="hljs-keyword">if</span> (type === <span class="hljs-string">'directive'</span> && <span class="hljs-keyword">typeof</span> definition === <span class="hljs-string">'function'</span>) &#123;
          definition = &#123; <span class="hljs-attr">bind</span>: definition, <span class="hljs-attr">update</span>: definition &#125;
        &#125;
        <span class="hljs-comment">// this.options.components[id] = definition || this.options.directives[id] = definition || this.options.filter[id] = definition</span>
        <span class="hljs-built_in">this</span>.options[type + <span class="hljs-string">'s'</span>][id] = definition
        <span class="hljs-keyword">return</span> definition
      &#125;
    &#125;
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">致命六问</h2>
<blockquote>
<p>Vue 源码「全局 API」致命六问。</p>
<ol>
<li>Vue 初始化全局 API 时，做了什么？</li>
<li>Vue 全局 API 有什么作用？</li>
<li>Vue 中当父子组件配置选项发生冲突时，是如何处理？</li>
<li>初始化后，自定义往 Vue 实例上的响应式对象添加属性，添加的属性是否具有响应式？</li>
<li>如何自定义数据实现响应式？</li>
<li>vm.$set() 和 vm.$delete() 方法，分别如何操作对象和数组？</li>
</ol>
<p><em>思考问题后，答案在下方，根据自己阅读整理源码，对自己提出有意义的问题并自我回答。不确保是面试热点题噢（切勿入题太深）</em></p>
</blockquote>
<h2 data-id="heading-49">致命六答</h2>
<h3 data-id="heading-50">一答</h3>
<blockquote>
<p>问：Vue 初始化全局 API 时，做了什么？</p>
</blockquote>
<pre><code class="copyable">答：
1.Vue 初始化了全局的 config 配置并设为响应式。
2.暴露一些工具方法，如日志、选项扩展、选项合并、设置对象响应式
3.暴露全局初始化方法，如 Vue.set、Vue.delete、Vue.nextTick、Vue.observable
4.暴露组件配置注册方法，如  Vue.options.components、Vue.options.directives、Vue.options.filters、Vue.options._base
5.暴露全局方法，如 Vue.use、Vue.mixin、Vue.extend、Vue.initAssetRegisters()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">二答</h3>
<blockquote>
<p>问：Vue 全局 API 有什么作用？</p>
</blockquote>
<blockquote>
<p>答：</p>
<ul>
<li>Vue.use()： 用来安装 plugin 插件，对插件进行缓存优化，并执行 install() 安装。</li>
<li>Vue.mixin()：用来在 Vue 的全局配置上合并 options 配置。并且每个组件生成 vnode 时会合并全局配置和组件配置，因此可以作为抽离公共的业务逻辑，实现公共的业务逻辑，也就是类的继承。</li>
<li>Vue.extend()：用来在 Vue 实例扩展子类，可以用于一些公共组件化配置上。与 Vue.mixin() 区别，我认为 extend 更多的是公众的组件化，也就是类的多态，外观模式。</li>
<li>Vue.initAssetRegisters()：用来将实例上的 component、directive、filter 对象配置到全局的 Vue.options 上。</li>
</ul>
</blockquote>
<h3 data-id="heading-52">三答</h3>
<blockquote>
<p>问：Vue 中当父子组件配置选项发生冲突时，是如何处理？</p>
</blockquote>
<blockquote>
<p>答：Vue 混合父子组件配置选项时，采用配置项的 key 值作为标识，<strong>若 key 值相等冲突，则子组件的配置选项将覆盖父组件的配置选项</strong>。</p>
</blockquote>
<h3 data-id="heading-53">四答</h3>
<blockquote>
<p>问：初始化后，自定义往 Vue 实例上的响应式对象添加属性，添加的属性是否具有响应式？</p>
</blockquote>
<blockquote>
<p>答：Vue 响应式是在初始化过程进行双向绑定和发布订阅模式实现的，若在<strong>后续自定义手动添加属性，无论是原始数据类型还是复杂数据类型都是不具备响应式的</strong>。</p>
</blockquote>
<h3 data-id="heading-54">五答</h3>
<blockquote>
<p>问：如何自定义数据实现响应式？</p>
</blockquote>
<blockquote>
<p>答：首先要保证挂载的对象是响应式的，也就是有 <code>target.\_\_ob__</code> 的标识符才能实现响应式，否则只能一种普通对象的静态挂载。<br>
我们可以使用 <code>vm.$set()</code> 来实现自定义数据的响应式，如对象：vm.$set(obj, key, val)，数组：vm.$set(array, idx, val)。</p>
</blockquote>
<h3 data-id="heading-55">六答</h3>
<blockquote>
<p>问：<code>vm.$set()</code> 和 <code>vm.$delete()</code> 方法，分别如何操作对象和数组？</p>
</blockquote>
<blockquote>
<p>答：</p>
<ul>
<li><code>vm.$set()</code>
<ul>
<li>操作对象使用的是 defineReactive(ob.value, key, val) 方法，原理是 Object.definePrototype() 来拦截，并调用 ob.dep.notify() 通知该对象已完成操作。</li>
<li>操作数组使用的是遍历数组，对指定下标使用 target.splice(key, 1, val)，实现响应式。</li>
</ul>
</li>
<li><code>vm.$delete()</code>
<ul>
<li>操作对象使用操作符 delete，并调用 ob.dep.notify() 通知该对象已完成操作。</li>
<li>操作数组的方法与 <code>vm.$set()</code> 一致，指定下标使用 target.splice(key, 1, val) 截取删除。</li>
</ul>
</li>
</ul>
</blockquote>
<h1 data-id="heading-56">Vue patch 渲染更新</h1>
<blockquote>
<p>位置：<code>/src/core/instance/lifecycle.js</code></p>
<p>我根据打断点，来明确一下初始化/更新时 patch 调用的顺序逻辑</p>
<p>初始化调用：<code>this._init(options)</code> => <code>vm.$mount(vm.$options.el)</code> => <code>mountComponent(this, el, hydrating)</code> => <code>new Watcher()</code> => <code>watcher.get()</code> => <code>updateComponent()</code> => <code>vm._update(vm._render(), hydrating)</code> => <code>vm.__patch__(vm.$el, vnode, hydrating, false)</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40c9f7c7495a4c3fa07ac9cf159d91bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更新时调用：<code>observe.set()</code> => <code>dep.notify()</code> => <code>watcher.update()</code> => <code>nextTick()</code> => <code>watcher.run()</code> => <code>watcher.get()</code> => <code>updateComponent()</code> => <code>vm._update(vm._render(), hydrating)</code> => <code>vm.__patch__(prevVnode, vnode)</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cac60d8f6084cdf85a17882f3cadc7f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-57">入口</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// patch 渲染更新的入口</span>
Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode: VNode, hydrating?: boolean</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">const</span> prevEl = vm.$el
  
  <span class="hljs-comment">// vm._vnode 由 vm._render() 生成</span>
  <span class="hljs-comment">// 老虚拟节点</span>
  <span class="hljs-keyword">const</span> prevVnode = vm._vnode
  <span class="hljs-keyword">const</span> restoreActiveInstance = setActiveInstance(vm)
  <span class="hljs-comment">// 新虚拟节点</span>
  vm._vnode = vnode
  <span class="hljs-comment">// Vue.prototype.__patch__ is injected in entry points</span>
  <span class="hljs-comment">// based on the rendering backend used.</span>
  
  <span class="hljs-keyword">if</span> (!prevVnode) &#123;
    <span class="hljs-comment">// 只有新虚拟节点，即为首次渲染，初始化页面时走这里</span>
    vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 有新老节点，即为更新数据渲染，更新页面时走这里</span>
    vm.$el = vm.__patch__(prevVnode, vnode)
  &#125;
  
  <span class="hljs-comment">// 缓存虚拟节点</span>
  restoreActiveInstance()
  
  <span class="hljs-comment">// update __vue__ reference</span>
  <span class="hljs-keyword">if</span> (prevEl) &#123;
    prevEl.__vue__ = <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> (vm.$el) &#123;
    vm.$el.__vue__ = vm
  &#125;
  <span class="hljs-comment">// if parent is an HOC, update its $el as well</span>
  <span class="hljs-comment">// 当父子节点的虚拟节点一致，也更新父节点的 $el</span>
  <span class="hljs-keyword">if</span> (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) &#123;
    vm.$parent.$el = vm.$el
  &#125;
  <span class="hljs-comment">// updated hook is called by the scheduler to ensure that children are</span>
  <span class="hljs-comment">// updated in a parent's updated hook.</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-58">核心代码</h2>
<p><em>源码核心代码顺序以深度遍历形式</em></p>
<h3 data-id="heading-59">patch()</h3>
<blockquote>
<p>位置：<code>/src/core/observer/index.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// patch 方法，hydrating 是否服务端渲染，removeOnly 是否使用了 <transition group> 过渡组</span>
<span class="hljs-comment">// 1.vnode 不存在，则摧毁 oldVnode</span>
<span class="hljs-comment">// 2.vnode 存在且 oldVnode 不存在，表示组件初次渲染，添加标示且创建根节点</span>
<span class="hljs-comment">// 3.vnode 和 oldVnode 都存在时</span>
<span class="hljs-comment">// 3.1.oldVnode 不是真实节点表示更新阶段（都是虚拟节点），执行 patchVnode，生成 vnode</span>
<span class="hljs-comment">// 3.2.oldVnode 是真实元素，表示初始化渲染，执行 createElm 基于 vnode 创建整棵 DOM 树并插入到 body 元素下，递归更新父占位符节点元素，完成更新后移除 oldnode。</span>
<span class="hljs-comment">// 4.最后 vnode 插入队列并生成返回 vnode</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode, hydrating, removeOnly</span>) </span>&#123;
  <span class="hljs-comment">// vnode 不存在，表示删除节点，则摧毁 oldVnode</span>
  <span class="hljs-keyword">if</span> (isUndef(vnode)) &#123;
    <span class="hljs-comment">// 执行 oldVnode 也就是未更新组件生命周期 destroy 钩子</span>
    <span class="hljs-comment">// 执行 oldVnode 各个模块(style、class、directive 等）的 destroy 方法</span>
<span class="hljs-comment">// 如果有 children 递归调用 invokeDestroyHook</span>
    <span class="hljs-keyword">if</span> (isDef(oldVnode)) invokeDestroyHook(oldVnode)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">let</span> isInitialPatch = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">const</span> insertedVnodeQueue = []

  <span class="hljs-comment">// vnode 存在且 oldVnode 不存在</span>
  <span class="hljs-keyword">if</span> (isUndef(oldVnode)) &#123;
    <span class="hljs-comment">// empty mount (likely as component), create new root element</span>
    <span class="hljs-comment">// 组件初次渲染，创建根节点</span>
    isInitialPatch = <span class="hljs-literal">true</span>
    createElm(vnode, insertedVnodeQueue)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 判断 oldVnode 是否为真实元素</span>
    <span class="hljs-keyword">const</span> isRealElement = isDef(oldVnode.nodeType)
    <span class="hljs-comment">// 不是真实元素且 oldVnode 和 vnode 是同一个节点，执行 patchVnode 直接更新节点</span>
    <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
      patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
      
    <span class="hljs-comment">// 真实元素或者新老节点不相同</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (isRealElement) &#123;
        <span class="hljs-comment">// mounting to a real element</span>
        <span class="hljs-comment">// check if this is server-rendered content and if we can perform</span>
        <span class="hljs-comment">// a successful hydration.</span>
        <span class="hljs-comment">// oldVnode 是元素节点且有服务器渲染的属性</span>
        <span class="hljs-keyword">if</span> (oldVnode.nodeType === <span class="hljs-number">1</span> && oldVnode.hasAttribute(SSR_ATTR)) &#123;
          oldVnode.removeAttribute(SSR_ATTR)
          hydrating = <span class="hljs-literal">true</span>
        &#125;
        <span class="hljs-comment">// ...省略代码，服务端渲染执行 invokeInsertHook(vnode, insertedVnodeQueue, true)</span>
        
        <span class="hljs-comment">// either not server-rendered, or hydration failed.</span>
        <span class="hljs-comment">// create an empty node and replace it</span>
        
        <span class="hljs-comment">// 不是服务端渲染，或 hydration 失败，创建一个空的 vnode 节点</span>
        oldVnode = emptyNodeAt(oldVnode)
      &#125;

      <span class="hljs-comment">// 拿到 oldVnode /父 oldVnode 的真实元素</span>
      <span class="hljs-keyword">const</span> oldElm = oldVnode.elm
      <span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)

      <span class="hljs-comment">// 基于 vnode 创建整棵 DOM 树并插入到 body 元素下</span>
      createElm(
        vnode,
        insertedVnodeQueue,
        <span class="hljs-comment">// extremely rare edge case: do not insert if old element is in a</span>
        <span class="hljs-comment">// leaving transition. Only happens when combining transition +</span>
        <span class="hljs-comment">// keep-alive + HOCs. (#4590)</span>
        oldElm._leaveCb ? <span class="hljs-literal">null</span> : parentElm,
        nodeOps.nextSibling(oldElm)
      )

      <span class="hljs-comment">// 递归更新父占位符节点元素</span>
      <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
        <span class="hljs-keyword">let</span> ancestor = vnode.parent
        <span class="hljs-keyword">const</span> patchable = isPatchable(vnode)
        <span class="hljs-keyword">while</span> (ancestor) &#123;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) &#123;
            cbs.destroy[i](ancestor)
          &#125;
          ancestor.elm = vnode.elm
          <span class="hljs-keyword">if</span> (patchable) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
              cbs.create[i](emptyNode, ancestor)
            &#125;
            <span class="hljs-comment">// #6513</span>
            <span class="hljs-comment">// invoke insert hooks that may have been merged by create hooks.</span>
            <span class="hljs-comment">// e.g. for directives that uses the "inserted" hook.</span>
            <span class="hljs-keyword">const</span> insert = ancestor.data.hook.insert
            <span class="hljs-keyword">if</span> (insert.merged) &#123;
              <span class="hljs-comment">// start at index 1 to avoid re-invoking component mounted hook</span>
              <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < insert.fns.length; i++) &#123;
                insert.fns[i]()
              &#125;
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            registerRef(ancestor)
          &#125;
          ancestor = ancestor.parent
        &#125;
      &#125;

      <span class="hljs-comment">// 完成更新，移除 oldVnode</span>
      <span class="hljs-comment">// 当有父节点时，指定范围删除自己</span>
      <span class="hljs-keyword">if</span> (isDef(parentElm)) &#123;
        removeVnodes([oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
        
      <span class="hljs-comment">// 没有父节点时</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.tag)) &#123;
        invokeDestroyHook(oldVnode)
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">// 将虚拟节点插入队列中</span>
  invokeInsertHook(vnode, insertedVnodeQueue, isInitialPatch)
  <span class="hljs-keyword">return</span> vnode.elm
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-60">createElm</h3>
<blockquote>
<p>位置：<code>src/core/vdom/patch.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 基于 vnode 创建真实 DOM 树</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">
  vnode,
  insertedVnodeQueue,
  parentElm,
  refElm,
  nested,
  ownerArray,
  index
</span>) </span>&#123;
  <span class="hljs-comment">// 直接复制缓存的 vnode</span>
  <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
    vnode = ownerArray[index] = cloneVNode(vnode)
  &#125;
  vnode.isRootInsert = !nested <span class="hljs-comment">// for transition enter check</span>

  <span class="hljs-comment">// 创建 vnode 组件</span>
  <span class="hljs-keyword">if</span> (createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// 获取 data 对象</span>
  <span class="hljs-keyword">const</span> data = vnode.data
  <span class="hljs-comment">// 所有的孩子节点</span>
  <span class="hljs-keyword">const</span> children = vnode.children
  <span class="hljs-keyword">const</span> tag = vnode.tag
  <span class="hljs-keyword">if</span> (isDef(tag)) &#123;
    <span class="hljs-comment">// ...省略代码：当标签未知时发出警告</span>

    <span class="hljs-comment">// 创建新节点</span>
    vnode.elm = vnode.ns
      ? nodeOps.createElementNS(vnode.ns, tag)
      : nodeOps.createElement(tag, vnode)
    setScope(vnode)

    <span class="hljs-comment">// 递归创建所有子节点（普通元素、组件）</span>
    createChildren(vnode, children, insertedVnodeQueue)
    <span class="hljs-keyword">if</span> (isDef(data)) &#123;
      invokeCreateHooks(vnode, insertedVnodeQueue)
    &#125;
    
    <span class="hljs-comment">// 将节点插入父节点</span>
    insert(parentElm, vnode.elm, refElm)

    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && data && data.pre) &#123;
      creatingElmInVPre--
    &#125;
    <span class="hljs-comment">// 处理注释节点并插入父节点</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isTrue(vnode.isComment)) &#123;
    vnode.elm = nodeOps.createComment(vnode.text)
    insert(parentElm, vnode.elm, refElm)
    <span class="hljs-comment">// 处理文本节点并插入父节点</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    vnode.elm = nodeOps.createTextNode(vnode.text)
    insert(parentElm, vnode.elm, refElm)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-61">patchVnode</h3>
<blockquote>
<p>位置：<code>/src/core/vdom/patch.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 更新节点</span>
<span class="hljs-comment">// 1.新老节点相同，直接返回</span>
<span class="hljs-comment">// 2.静态节点，克隆复用</span>
<span class="hljs-comment">// 3.全部遍历更新 vnode.data 上的属性</span>
<span class="hljs-comment">// 4.若是文本节点，直接更新文本</span>
<span class="hljs-comment">// 5.若不是文本节点</span>
<span class="hljs-comment">// 5.1 都有孩子，则递归执行 updateChildren 方法（diff 算法更新）</span>
<span class="hljs-comment">// 5.2 ch 有 oldCh 没有，则表明新增节点 addVnodes</span>
<span class="hljs-comment">// 5.3 ch 没有 oldCh 有，则表明删除节点 removeVnodes</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">
  oldVnode,
  vnode,
  insertedVnodeQueue,
  ownerArray,
  index,
  removeOnly
</span>) </span>&#123;
  <span class="hljs-comment">// 老节点和新节点相同，直接返回</span>
  <span class="hljs-keyword">if</span> (oldVnode === vnode) &#123;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// 缓存过的 vnode，直接克隆 vnode</span>
  <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
    <span class="hljs-comment">// clone reused vnode</span>
    vnode = ownerArray[index] = cloneVNode(vnode)
  &#125;

  <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm

  <span class="hljs-comment">// 异步占位符节点</span>
  <span class="hljs-keyword">if</span> (isTrue(oldVnode.isAsyncPlaceholder)) &#123;
    <span class="hljs-keyword">if</span> (isDef(vnode.asyncFactory.resolved)) &#123;
      hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode.isAsyncPlaceholder = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// reuse element for static trees.</span>
  <span class="hljs-comment">// note we only do this if the vnode is cloned -</span>
  <span class="hljs-comment">// if the new node is not cloned it means the render functions have been</span>
  <span class="hljs-comment">// reset by the hot-reload-api and we need to do a proper re-render.</span>
  <span class="hljs-keyword">if</span> (isTrue(vnode.isStatic) &&
    isTrue(oldVnode.isStatic) &&
    vnode.key === oldVnode.key &&
    (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
  ) &#123;
    <span class="hljs-comment">// 新旧节点都是静态的而且两个节点的 key 一样，并且新节点被克隆了或者新节点有 v-once 指令，则用 oldVnode 的组件节点，且跳出，不进行 diff 更新</span>
    vnode.componentInstance = oldVnode.componentInstance
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// 执行组件的 prepatch 钩子</span>
  <span class="hljs-keyword">let</span> i
  <span class="hljs-keyword">const</span> data = vnode.data
  <span class="hljs-keyword">if</span> (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) &#123;
    i(oldVnode, vnode)
  &#125;

  <span class="hljs-comment">// 孩子</span>
  <span class="hljs-keyword">const</span> oldCh = oldVnode.children
  <span class="hljs-keyword">const</span> ch = vnode.children
  
  <span class="hljs-comment">// 更新 vnode 上的属性</span>
  <span class="hljs-keyword">if</span> (isDef(data) && isPatchable(vnode)) &#123;
    <span class="hljs-comment">// 全部遍历更新（Vue3 做了大量优化）</span>
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
    <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.update)) i(oldVnode, vnode)
  &#125;
  <span class="hljs-comment">// 新节点不是文本节点</span>
  <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
    <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
      <span class="hljs-comment">// 如果 oldCh 和 ch 不同，开始更新子节点（也就是 diff 算法）</span>
      <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly)
      
    <span class="hljs-comment">// 只有 ch</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
        <span class="hljs-comment">// 检查是否有重复 key 值，给予警告</span>
        checkDuplicateKeys(ch)
      &#125;
      <span class="hljs-comment">// oldVnode 中有文本信息，创建文本节点并添加</span>
      <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) nodeOps.setTextContent(elm, <span class="hljs-string">''</span>)
      addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue)
      
    <span class="hljs-comment">// 只有 oldCh</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
      <span class="hljs-comment">// 删除节点的操作</span>
      removeVnodes(oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
      <span class="hljs-comment">// oldVnode 上有文本</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
      <span class="hljs-comment">// 置空文本</span>
      nodeOps.setTextContent(elm, <span class="hljs-string">''</span>)
    &#125;
  
  <span class="hljs-comment">// vnode 是文本，若 oldVnode 和 vnode 文本不相同</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
    <span class="hljs-comment">// 更新文本节点</span>
    nodeOps.setTextContent(elm, vnode.text)
  &#125;
    
  <span class="hljs-comment">// 还有 data 数据，执行组件的 prepatch 钩子</span>
  <span class="hljs-keyword">if</span> (isDef(data)) &#123;
    <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.postpatch)) 
      i(oldVnode, vnode)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">removeVnodes</h3>
<blockquote>
<p>位置：<code>/src/core/vdom/patch.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除 vnode 节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeVnodes</span>(<span class="hljs-params">vnodes, startIdx, endIdx</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (; startIdx <= endIdx; ++startIdx) &#123;
    <span class="hljs-keyword">const</span> ch = vnodes[startIdx]
    <span class="hljs-comment">// 有子节点</span>
    <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
      <span class="hljs-comment">// 不是文本节点</span>
      <span class="hljs-keyword">if</span> (isDef(ch.tag)) &#123;
        <span class="hljs-comment">// patch() 方法中有说明</span>
        removeAndInvokeRemoveHook(ch)
        invokeDestroyHook(ch)
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// Text node</span>
        <span class="hljs-comment">// 直接移除该元素</span>
        removeNode(ch.elm)
      &#125;
    &#125;
  &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-63">updateChildren</h3>
<blockquote>
<p>src/core/vdom/patch.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 更新子节点采用了 diff 算法</span>
<span class="hljs-comment">// 做了四种假设，假设新老节点开头结尾有相同节点的情况，一旦命中假设，就避免了一次循环，以提高执行效率</span>
<span class="hljs-comment">// 如果不幸没有命中假设，则执行遍历，从老节点中找到新开始节点</span>
<span class="hljs-comment">// 找到相同节点，则执行 patchVnode，然后将老节点移动到正确的位置</span>
<span class="hljs-comment">// 如果老节点先于新节点遍历结束，则剩余的新节点执行新增节点操作</span>
<span class="hljs-comment">// 如果新节点先于老节点遍历结束，则剩余的老节点执行删除操作，移除这些老节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm, oldCh, newCh, insertedVnodeQueue, removeOnly</span>) </span>&#123;
  <span class="hljs-comment">// 为 diff 算法假设做初始化：新老子节点的头尾下标和对应值</span>
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]
  <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]
  <span class="hljs-keyword">let</span> oldKeyToIdx, idxInOld, vnodeToMove, refElm

  <span class="hljs-comment">// <transition-group> 的标识符</span>
  <span class="hljs-keyword">const</span> canMove = !removeOnly

  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    <span class="hljs-comment">// 若重复 key 则发出警告</span>
    checkDuplicateKeys(newCh)
  &#125;

  <span class="hljs-comment">// 遍历新老节点数组，直到一方取完值</span>
  <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    
    <span class="hljs-comment">// 老开始节点无值，表示更新过，向右移动下标（往后看）</span>
    <span class="hljs-keyword">if</span> (isUndef(oldStartVnode)) &#123;
      oldStartVnode = oldCh[++oldStartIdx] <span class="hljs-comment">// Vnode has been moved left</span>
    <span class="hljs-comment">// 老结束节点无值，表示更新过，向左移动下标（往后看）</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isUndef(oldEndVnode)) &#123;
      oldEndVnode = oldCh[--oldEndIdx]
      
    <span class="hljs-comment">// 新老的开始/结束节点是相同节点，返回 patchVnode 阶段，不更新比较</span>
    <span class="hljs-comment">// 因为两个都不比较，同时移动下标</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
      patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
      oldStartVnode = oldCh[++oldStartIdx]
      newStartVnode = newCh[++newStartIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
      patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      oldEndVnode = oldCh[--oldEndIdx]
      newEndVnode = newCh[--newEndIdx]
      
    <span class="hljs-comment">// 新尾和老头/新头和老尾相等</span>
    <span class="hljs-comment">// 一样需要移动下标，进行 ch 数组下个节点的判断</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123; <span class="hljs-comment">// Vnode moved right</span>
      patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
      <span class="hljs-comment">// <transtion-group> 包裹的组件时使用，如轮播图情况。</span>
      canMove && nodeOps.insertBefore(parentElm, oldStartVnode.elm, nodeOps.nextSibling(oldEndVnode.elm))
      oldStartVnode = oldCh[++oldStartIdx]
      newEndVnode = newCh[--newEndIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; <span class="hljs-comment">// Vnode moved left</span>
      patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
      canMove && nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm)
      oldEndVnode = oldCh[--oldEndIdx]
      newStartVnode = newCh[++newStartIdx]
      
    <span class="hljs-comment">// 四种常规 web 操作假设都不成立，则不能优化，开始遍历更新</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 当老节点的 key 对应不上 idx 时</span>
      <span class="hljs-comment">// 在指定 idx 的范围内，找到 key 在老节点中的下标位置</span>
      <span class="hljs-comment">// 形成 map = &#123; key1: id1, key2: id2, ...&#125;</span>
      <span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx)) oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
      
      <span class="hljs-comment">// 若新开始节点有 key 值，在老节点的 key 和 id 映射表 map 中找到返回对应的 id 下标值</span>
      <span class="hljs-comment">// 若新开始节点没有 key 值，则找到老节点数组中新开始节点的值，返回 id 下标</span>
      idxInOld = isDef(newStartVnode.key)
        ? oldKeyToIdx[newStartVnode.key]
        : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
      
      <span class="hljs-comment">// 若新开始节点不存在老节点中，那就是新建元素</span>
      <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// New element</span>
        createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
        
      <span class="hljs-comment">// 新开始节点存在老节点中，开始判断情况更新</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        vnodeToMove = oldCh[idxInOld]
        
        <span class="hljs-comment">// 如果两个节点不但 key 相同，节点也是相同，则直接返回 patchVnode</span>
        <span class="hljs-keyword">if</span> (sameVnode(vnodeToMove, newStartVnode)) &#123;
          patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
          <span class="hljs-comment">// 将该老节点置为 空，避免新节点反复找到同一个节点</span>
          oldCh[idxInOld] = <span class="hljs-literal">undefined</span>
          <span class="hljs-comment">// 还是判断 <transition-group> 标签的情况</span>
          canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 两个节点虽然 key 相等，但节点不相等，看作新元素，创建节点</span>
          createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
        &#125;
      &#125;
      <span class="hljs-comment">// 老节点向后移动一个</span>
      newStartVnode = newCh[++newStartIdx]
    &#125;
  &#125;
  
  <span class="hljs-comment">// 新老节点某个数组被遍历完了</span>
  <span class="hljs-comment">// 新的有多余，那就是新增</span>
  <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
    refElm = isUndef(newCh[newEndIdx + <span class="hljs-number">1</span>]) ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
    addVnodes(parentElm, refElm, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
 <span class="hljs-comment">// 老的有多余，那就是删除</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartIdx > newEndIdx) &#123;
    removeVnodes(oldCh, oldStartIdx, oldEndIdx)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-64">致命七问</h2>
<blockquote>
<p>Vue 源码「patch」致命七问。</p>
<ol>
<li>Vue 初始化阶段和更新阶段，是如何进入 patch 阶段。（或 Vue 初始化和更新阶段分别发生什么等相关问题）</li>
<li>Vue patch 阶段做了什么？</li>
<li>你知道 patch 方法有几个参数？最后两个参数分别有什么作用？</li>
<li>diff 算法是什么？起到什么作用？</li>
<li>若节点 key 值相等且节点不同，新节点会覆盖旧节点吗？</li>
<li>vnode 是什么？有什么用？</li>
<li>Vue 如何处理 Vnode 上的属性？</li>
</ol>
<p><em>思考问题后，答案在下方，根据自己阅读整理源码，对自己提出有意义的问题并自我回答。不确保是面试热点题噢（切勿入题太深）</em></p>
</blockquote>
<h2 data-id="heading-65">致命七答</h2>
<h3 data-id="heading-66">一答</h3>
<blockquote>
<p>问：Vue 初始化阶段和更新阶段，是如何进入 patch 阶段。（或 Vue 初始化和更新阶段分别发生什么等相关问题）</p>
</blockquote>
<blockquote>
<p>答：</p>
<ul>
<li>Vue 初始化分为以下几个阶段
<ol>
<li>初始化时执行 Vue._init()，初始化组件的各种属性和事件并触发 beforeCreate 钩子函数，之后初始化响应式数据并最后触发 created 钩子函数</li>
<li>执行 vm.$mount()，调用 mountComponent()，初始化 render 函数和组件的框架调用 beforeMount 钩子函数，初始化 dep.target。</li>
<li>创建当前组件的 Watcher 实例，执行 watcher.get() 方法获取当前 watcher 上的数据。</li>
<li>执行 updateComponent() 回调来执行 vm.update() 方法，因初始化渲染，故直接调用 vm.__patch__ 创建空元素。生成 vnode 虚拟节点。</li>
<li>执行 proxy 对数据进行响应式处理，执行 dep.depend() 收集对应响应式数据上所有 watcher 的依赖，watcher 也收集 dep 的依赖实现双向绑定。</li>
<li>开始调用 render 渲染函数（关键是 _createElement()）根据 vnode 递归遍历实现整个真实页面。</li>
</ol>
</li>
<li>Vue 更新分为以下几个阶段
<ol>
<li>当数据更新时，进入数据对应的监听者 observe.set() 方法中调用 dep.notify() 发布通知所有 watcher 执行 update() 方法。</li>
<li>接下来就是异步更新内容，封装各种 watcher 队列和刷新函数队列，进入 nextTick() 中执行 timerFunc() 利用浏览器异步任务队列来实现异步更新。</li>
<li>等到浏览器异步任务队列开始执行 flushCallbacks()，便调用 callbacks 中每个 flushSchedulerQueue() 执行回调  watcher.run()</li>
<li>watcher 通过 get() 调用 updateComponent() 中的 vm.__patch__(prevVnode, vnode) 开始进入递归遍历节点的 patch 阶段。</li>
<li>patch 阶段通过判断新老子节点的情况，调用 updateChildren() 开始 diff 算法假设和优化，最终形成 vnode 虚拟节点。</li>
<li>开始调用 render 渲染函数，根据 vnode 递归遍历实现整个真实页面。</li>
</ol>
</li>
</ul>
</blockquote>
<h3 data-id="heading-67">二答</h3>
<blockquote>
<p>问：Vue patch 阶段做了什么？</p>
</blockquote>
<blockquote>
<p>答：patch 阶段主要进行了四点内容。</p>
<ol>
<li>vnode 不存在，则摧毁 oldVnode</li>
<li>vnode 存在且 oldVnode 不存在，表示组件初次渲染，添加标示且创建根节点</li>
<li>vnode 和 oldVnode 都存在时
<ol>
<li>oldVnode 不是真实节点表示更新阶段（都是虚拟节点），执行 patchVnode，生成 vnode</li>
<li>oldVnode 是真实元素，表示初始化渲染，执行 createElm 基于 vnode 创建整棵 DOM 树并插入到 body 元素下，递归更新父占位符节点元素，完成更新后移除 oldnode。</li>
</ol>
</li>
<li>最后 vnode 插入队列并生成返回 vnode。</li>
</ol>
</blockquote>
<h3 data-id="heading-68">三答</h3>
<blockquote>
<p>问：你知道 patch 方法有几个参数？最后两个参数分别有什么作用？</p>
</blockquote>
<blockquote>
<p>答：<code>patch(oldVnode, vnode, hydrating, removeOnly)</code>，patch 方法共有四个参数，最后两个参数为 <code>hydrating</code> 和 <code>removeOnly</code>。它们的作用分别为：</p>
<ol>
<li>hydrating 判断是否服务器渲染执行。在 patch 阶段时，oldVnode 是真实元素，初始化渲染时，若 oldVnode 是元素节点且有服务器渲染的属性，则设置 hydrating 为 true，表示服务端渲染。</li>
<li>removeOnly 判断节点是否被 <code><transition-group> </code> 包裹着。在 updateChildren 中判断插入执行 nodeOps.insertBefore()，如轮播图等案例。</li>
</ol>
</blockquote>
<h3 data-id="heading-69">四答</h3>
<blockquote>
<p>问：diff 算法是什么？起到什么作用？</p>
</blockquote>
<blockquote>
<p>答：diff 算法是在 patch 阶段，遍历比较更新子节点时，利用 web 常规操作的思维做的四种假设，一旦命中假设，就<strong>避免了循环，以提高执行效率，起到绝大部分更新情况的优化效果</strong>。</p>
<ul>
<li>四种假设分别为：
<ol>
<li>老开始和新开始节点相同</li>
<li>老结束和新结束节点相同</li>
<li>老开始和新结束节点相同</li>
<li>老结束和新开始节点相同</li>
</ol>
</li>
</ul>
<p>当 diff 算法阶段都未命中假设时，则利用 <code>key</code> 值映射 oldVnode 的下标值生成 map 对象，以此来利用 key 值快速找到新节点在旧节点中的下标位置，进行判断比对，若<code>没有 key 值</code>，则只能利用新节点的值暴力遍历比较旧节点的值进行判断更新。<br>
最后新老数组中某一数组遍历完成，则进行添加或删除节点操作。</p>
</blockquote>
<h3 data-id="heading-70">五答</h3>
<blockquote>
<p>问：若节点 key 值相等且节点不同，新节点会覆盖旧节点吗？</p>
</blockquote>
<blockquote>
<p>答：在 diff 算法阶段，当新节点找到在老节点相同 key 且节点不同时，会看作是创建新节点执行 <code>createElm()</code></p>
</blockquote>
<h3 data-id="heading-71">六答</h3>
<blockquote>
<p>问：vnode 是什么？有什么用？</p>
</blockquote>
<blockquote>
<p>答：vnode 是利用 JS 对象模拟真实 DOM 树，抽象了渲染的过程，形成一个 JS 对象。作用如下：</p>
<ol>
<li>减少对真实DOM的操作，大大减轻了浏览器的负担。</li>
<li>因 JavaScript 本质是弱语言跨平台的性质，故虚拟 DOM 可以跨平台使用。</li>
<li>虚拟 DOM 可以快速对比两次状态的差异以便更新真实 DOM。</li>
</ol>
</blockquote>
<h3 data-id="heading-72">七答</h3>
<blockquote>
<p>问：Vue 如何处理 vnode 上的属性？</p>
</blockquote>
<blockquote>
<p>答：在 patchVnode 方法中，<strong>直接遍历更新 vnode 上的全部属性</strong>。Vue3 将进行大量优化更新。</p>
</blockquote>
<h3 data-id="heading-73">最后</h3>
<blockquote>
<p>最后放一个 Vnode 的类，位置：<code>/src/core/vdom/vnode.js</code></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-attr">tag</span>: string | <span class="hljs-keyword">void</span>;
  data: VNodeData | <span class="hljs-keyword">void</span>;
  children: ?<span class="hljs-built_in">Array</span><VNode>;
  text: string | <span class="hljs-keyword">void</span>;
  elm: Node | <span class="hljs-keyword">void</span>;
  ns: string | <span class="hljs-keyword">void</span>;
  context: Component | <span class="hljs-keyword">void</span>; <span class="hljs-comment">// rendered in this component's scope</span>
  key: string | number | <span class="hljs-keyword">void</span>;
  componentOptions: VNodeComponentOptions | <span class="hljs-keyword">void</span>;
  componentInstance: Component | <span class="hljs-keyword">void</span>; <span class="hljs-comment">// component instance</span>
  parent: VNode | <span class="hljs-keyword">void</span>; <span class="hljs-comment">// component placeholder node</span>

  <span class="hljs-comment">// strictly internal</span>
  raw: boolean; <span class="hljs-comment">// contains raw HTML? (server only)</span>
  isStatic: boolean; <span class="hljs-comment">// hoisted static node</span>
  isRootInsert: boolean; <span class="hljs-comment">// necessary for enter transition check</span>
  isComment: boolean; <span class="hljs-comment">// empty comment placeholder?</span>
  isCloned: boolean; <span class="hljs-comment">// is a cloned node?</span>
  isOnce: boolean; <span class="hljs-comment">// is a v-once node?</span>
  asyncFactory: <span class="hljs-built_in">Function</span> | <span class="hljs-keyword">void</span>; <span class="hljs-comment">// async component factory function</span>
  asyncMeta: <span class="hljs-built_in">Object</span> | <span class="hljs-keyword">void</span>;
  isAsyncPlaceholder: boolean;
  ssrContext: <span class="hljs-built_in">Object</span> | <span class="hljs-keyword">void</span>;
  fnContext: Component | <span class="hljs-keyword">void</span>; <span class="hljs-comment">// real context vm for functional nodes</span>
  fnOptions: ?ComponentOptions; <span class="hljs-comment">// for SSR caching</span>
  devtoolsMeta: ?<span class="hljs-built_in">Object</span>; <span class="hljs-comment">// used to store functional render context for devtools</span>
  fnScopeId: ?string; <span class="hljs-comment">// functional scope id support</span>

  <span class="hljs-title">constructor</span> (<span class="hljs-params">
    tag?: string,
    data?: VNodeData,
    children?: ?<span class="hljs-built_in">Array</span><VNode>,
    text?: string,
    elm?: Node,
    context?: Component,
    componentOptions?: VNodeComponentOptions,
    asyncFactory?: <span class="hljs-built_in">Function</span>
  </span>) &#123;
    <span class="hljs-built_in">this</span>.tag = tag
    <span class="hljs-built_in">this</span>.data = data
    <span class="hljs-built_in">this</span>.children = children
    <span class="hljs-built_in">this</span>.text = text
    <span class="hljs-built_in">this</span>.elm = elm
    <span class="hljs-built_in">this</span>.ns = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.context = context
    <span class="hljs-built_in">this</span>.fnContext = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.fnOptions = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.fnScopeId = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.key = data && data.key
    <span class="hljs-built_in">this</span>.componentOptions = componentOptions
    <span class="hljs-built_in">this</span>.componentInstance = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.parent = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.raw = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>.isStatic = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>.isRootInsert = <span class="hljs-literal">true</span>
    <span class="hljs-built_in">this</span>.isComment = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>.isCloned = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>.isOnce = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>.asyncFactory = asyncFactory
    <span class="hljs-built_in">this</span>.asyncMeta = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.isAsyncPlaceholder = <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-comment">// DEPRECATED: alias for componentInstance for backwards compat.</span>
  <span class="hljs-comment">/* istanbul ignore next */</span>
  get child (): Component | <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.componentInstance
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-74">思维导图</h1>
<blockquote>
<p>记录我学习源码过程（结尾有我学习源码的链接）做的思维导图</p>
</blockquote>
<ul>
<li>Vue源码(1) - 前言</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2793bd6230546c8bcba482263ca66ee~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(1) - 前言.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(2)-初始化</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6234fddea83b48919f8a791abf08955a~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(2)-Vue初始化过程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(3)-响应式原理</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc74bde5335a4e72816515051ba1f5d9~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(3)-响应式原理.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(4)-异步更新</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3c1d0263d84797a9575ceaaf1e427c~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(4)-异步更新.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(5)-全局API</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf11f6a68224494695c9b870bc06e4d9~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(5)-全局API.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(6)-实例方法</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec23c3ac956c4aae9208ba2cdc6fb286~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(6)-实例方法.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(7)-Hook Event</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86a7354b661f494693d57ad59b1dab01~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(7)-Hook Event.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(8)-编译器（解析）</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f0dcaa86373484dadc86eaa5342c01c~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(8)-编译器（解析）.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(9)-编译器之优化</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d1147bae5a546e4944a12278673b097~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(9)-编译器之优化.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(10)—编译器之生成渲染函数</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5ebac2eb62040c9b77c55a286457d20~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(10)—编译器之生成渲染函数.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(11)-render helper</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/027c0c6593eb4d5db55d313388013b5b~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(11)-render helper.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Vue源码(12)-patch</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26d3c59817214d41b4b1f0fb9d9507cb~tplv-k3u1fbpfcp-watermark.image" alt="Vue源码(12)-patch.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-75">结尾</h1>
<blockquote>
<p>感谢下列参考文章，以及我学习源码系列教程<br>
参考文章：<br>
<a href="https://www.jianshu.com/p/624c17c0e3fd" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/624c17c0e…</a></p>
<p><a href="https://juejin.cn/post/6844903903822086151" target="_blank">juejin.cn/post/684490…</a></p>
<p><a href="https://juejin.cn/post/6844903918753808398" target="_blank">juejin.cn/post/684490…</a></p>
<p>学习源码：</p>
<p><a href="https://juejin.cn/column/6960553066101735461" target="_blank">juejin.cn/column/6960…</a></p>
<p><a href="https://space.bilibili.com/359669053/channel/detail?cid=178493" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/359669053/c…</a></p>
</blockquote>
<p>最后希望这篇源码总结对小伙伴们有所帮助噢！若有纰漏或瑕疵，麻烦指教一二！</p>
<p>🌟 <em>点赞关注(暗示)</em></p></div>  
</div>
            