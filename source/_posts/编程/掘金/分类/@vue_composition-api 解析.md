
---
title: '@vue_composition-api 解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/298a9664d1224956ae37e4d55caae916~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 18:13:11 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/298a9664d1224956ae37e4d55caae916~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：周超</p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fguide%2Fcomposition-api-introduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/guide/composition-api-introduction.html" ref="nofollow noopener noreferrer">组合式 API</a> 是 vue3 提出的一个新的开发方式，而在 vue2 中我们可以使用新的组合式 API 进行组件开发。本篇通过一个例子，来分析这个插件是如何提供功能。</p>
<p>关于该插件的安装、使用，可以直接阅读文档。</p>
<h3 data-id="heading-1">安装</h3>
<p>我们从最开始安装分析，一探究竟。</p>
<h4 data-id="heading-2">vue.use</h4>
<p>按照文档所提到的，我们必须通过 Vue.use() 进行安装：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.use 安装</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueCompositionAPI <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>
Vue.use(VueCompositionAPI)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fcomposition-api%2Fblob%2Fmaster%2Fsrc%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/composition-api/blob/master/src/index.ts" ref="nofollow noopener noreferrer">入口文件</a>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> type Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Data, SetupFunction &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./component'</span>
<span class="hljs-keyword">import</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./install'</span>
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Plugin
 
<span class="hljs-comment">// auto install when using CDN</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">window</span>.Vue) &#123;
  <span class="hljs-built_in">window</span>.Vue.use(Plugin)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以知道我们 Vue.use 时，传入的就是 install 文件中的 Plugin 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// install.ts 折叠源码</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue: VueConstructor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isVueRegistered(Vue)) &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      warn(
        <span class="hljs-string">'[vue-composition-api] already installed. Vue.use(VueCompositionAPI) should be called only once.'</span>
      )
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;
 
  <span class="hljs-keyword">if</span> (__DEV__) &#123;
    <span class="hljs-keyword">if</span> (Vue.version) &#123;
      <span class="hljs-keyword">if</span> (Vue.version[<span class="hljs-number">0</span>] !== <span class="hljs-string">'2'</span> || Vue.version[<span class="hljs-number">1</span>] !== <span class="hljs-string">'.'</span>) &#123;
        warn(
          <span class="hljs-string">`[vue-composition-api] only works with Vue 2, v<span class="hljs-subst">$&#123;Vue.version&#125;</span> found.`</span>
        )
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      warn(<span class="hljs-string">'[vue-composition-api] no Vue version found'</span>)
    &#125;
  &#125;
 
  Vue.config.optionMergeStrategies.setup = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
    parent: <span class="hljs-built_in">Function</span>,
    child: <span class="hljs-built_in">Function</span>
  </span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergedSetupFn</span>(<span class="hljs-params">props: any, context: any</span>) </span>&#123;
      <span class="hljs-keyword">return</span> mergeData(
        <span class="hljs-keyword">typeof</span> parent === <span class="hljs-string">'function'</span> ? parent(props, context) || &#123;&#125; : <span class="hljs-literal">undefined</span>,
        <span class="hljs-keyword">typeof</span> child === <span class="hljs-string">'function'</span> ? child(props, context) || &#123;&#125; : <span class="hljs-literal">undefined</span>
      )
    &#125;
  &#125;
 
  setVueConstructor(Vue)
  mixin(Vue)
&#125;
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Plugin = &#123;
  <span class="hljs-attr">install</span>: <span class="hljs-function">(<span class="hljs-params">Vue: VueConstructor</span>) =></span> install(Vue),
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">install</h4>
<p>通过上面的代码和 Vue.use 可知，我们安装时其实就是调用了 install 方法，先分析一波 install。根据代码块及功能可以分成三个部分：</p>
<ol>
<li>前两个大 if 的开发 check 部分</li>
<li>关于 setup 合并策略</li>
<li>通过 mixin 混入插件关于 组合式 API 的处理逻辑</li>
</ol>
<p><strong>第一部分</strong>中的第一个 if 是为了确保该 install 方法只被调用一次，避免浪费性能；第二个 if 则是确保vue版本为2.x。不过这里有个关于第一个if的小问题：多次注册插件时，Vue.use 自己本身会进行重复处理——安装过的插件再次注册时，不会调用 install 方法（Vue.use代码见下）。那么这个 if 的目的是啥？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Vue.use 部分源码</span>
Vue.use = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">plugin: <span class="hljs-built_in">Function</span> | <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> installedPlugins = (<span class="hljs-built_in">this</span>._installedPlugins || (<span class="hljs-built_in">this</span>._installedPlugins = []))
  <span class="hljs-keyword">if</span> (installedPlugins.indexOf(plugin) > -<span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;
 
  <span class="hljs-comment">// additional parameters</span>
  <span class="hljs-keyword">const</span> args = toArray(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)
  args.unshift(<span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin.install === <span class="hljs-string">'function'</span>) &#123;
    plugin.install.apply(plugin, args)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin === <span class="hljs-string">'function'</span>) &#123;
    plugin.apply(<span class="hljs-literal">null</span>, args)
  &#125;
  installedPlugins.push(plugin)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上面代码可知 Vue.use 实际上还是传入 vue 并调用插件的 install 方法，那么如果有大神（或者是奇葩？）绕过 Vue.use 直接调用，那么这个 if 的判断就生效了。如下方代码，此时第二个 install 会判断重复后，抛出错误</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 直接调用 install</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueCompositionAPI <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
 
Vue.config.productionTip = <span class="hljs-literal">false</span>
 
VueCompositionAPI.install(Vue)
VueCompositionAPI.install(Vue)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/298a9664d1224956ae37e4d55caae916~tplv-k3u1fbpfcp-watermark.image" alt="image2021-6-23_16-38-4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第二部分</strong>的合并策略是“Vue.config.optionMergeStrategies”这个代码块。Vue 提供的这个能力很生僻，我们日常的开发中几乎不会主动接触到。先上<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23optionMergeStrategies" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#optionMergeStrategies" ref="nofollow noopener noreferrer">文档</a>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b315c438494746688191d6d884451d6d~tplv-k3u1fbpfcp-watermark.image" alt="image2021-6-23_16-50-30.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是用来定义属性的合并行为。比如例子中的 extend 在调用时，会执行 mergeOptions。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Vue.extend</span>
Vue.extend = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">extendOptions</span>) </span>&#123;
    <span class="hljs-keyword">const</span> Super = <span class="hljs-built_in">this</span>
    extendOptions = extendOptions || &#123;&#125;
    Sub.options = mergeOptions(
      Super.options,
      extendOptions
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 mergeOptions 里关于 _my_option的相关如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> strats = config.optionMergeStrategies
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeOptions</span> (<span class="hljs-params">parent, child, vm</span>)</span>&#123;
  <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> parent) &#123;
    mergeField(key)
  &#125;
  <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> child) &#123;
    <span class="hljs-keyword">if</span> (!hasOwn(parent, key)) &#123;
      mergeField(key)
    &#125;
  &#125;
 
 
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeField</span> (<span class="hljs-params">key</span>) </span>&#123;
    <span class="hljs-keyword">const</span> strat = strats[key] || defaultStrat
    options[key] = strat(parent[key], child[key], vm, key)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 parent 就是 Super.options 也就是 Vue.options，而 child 就是 extendOptions 也就是我们传入的 &#123; _my_option: 1 &#125;。在这里使用了两个 for 循环，确保父子元素种所有的 key 都会执行到 mergeField，而第二个 for 循环中的 if 判断确保不会执行两次，保证了正确性及性能。而 mergeField 则是最终执行策略的地方。从 strats 中获取到我们定义的方法，把对应参数传入并执行，在这里就是：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// demo执行</span>
strat(<span class="hljs-literal">undefined</span>, <span class="hljs-number">1</span>, vm, <span class="hljs-string">'_my_option'</span>) <span class="hljs-comment">// return 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顺便一提，Vue.mixin 的实现就是 mergeOptions，也就是说当我们使用了 mixin 且里面具有 setup 属性时，会执行到上述合并策略。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.mixin = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">mixin</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.options = mergeOptions(<span class="hljs-built_in">this</span>.options, mixin)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而我们插件中相关的策略也很简单，获取好定义的父子 setup，然后合并成一个新的，在调用时会分别执行父子 setup，并通过 mergeData 方法合并返回：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// optionMergeStrategies.setup</span>
Vue.config.optionMergeStrategies.setup = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
  parent: <span class="hljs-built_in">Function</span>,
  child: <span class="hljs-built_in">Function</span>
</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergedSetupFn</span>(<span class="hljs-params">props: any, context: any</span>) </span>&#123;
    <span class="hljs-keyword">return</span> mergeData(
      <span class="hljs-keyword">typeof</span> parent === <span class="hljs-string">'function'</span> ? parent(props, context) || &#123;&#125; : <span class="hljs-literal">undefined</span>,
      <span class="hljs-keyword">typeof</span> child === <span class="hljs-string">'function'</span> ? child(props, context) || &#123;&#125; : <span class="hljs-literal">undefined</span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第三部分</strong>则是通过调用 mixin 方法向 vue 中混入一些事件，下面是 mixin 的定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.mixin(&#123;
    <span class="hljs-attr">beforeCreate</span>: functionApiInit,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: ComponentInstance</span>)</span> &#123;
      updateTemplateRef(<span class="hljs-built_in">this</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: ComponentInstance</span>)</span> &#123;
      updateTemplateRef(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;)
   
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functionApiInit</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initSetup</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  <span class="hljs-comment">// 省略...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 mixin 内部调用了 Vue.mixin 来想 beforeCreate、mounted、updated 等生命周期混入事件。这样就完成 install 的执行， Vue.use(VueCompositionAPI) 也到此结束。</p>
<h3 data-id="heading-4">初始化 — functionApiInit</h3>
<h4 data-id="heading-5">functionApiInit 执行</h4>
<p>我们知道在new Vue 时，会执行组件的 beforeCreate 生命周期。此时刚才通过 Vue.mixin 注入的函数 “functionApiInit”开始执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-built_in">this</span>._init(options)
&#125;
Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  initLifecycle(vm)
  initEvents(vm)
  initRender(vm)
  callHook(vm, <span class="hljs-string">'beforeCreate'</span>) <span class="hljs-comment">// 触发 beforeCreate 生命周期，执行 functionApiInit</span>
  initInjections(vm) <span class="hljs-comment">// resolve injections before data/props</span>
  initState(vm)
  initProvide(vm) <span class="hljs-comment">// resolve provide after data/props</span>
  callHook(vm, <span class="hljs-string">'created'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法也很清晰，分别暂存了组件最开始的 render方法和 data方法（我们平常写的 data 是一个函数），然后在这基础上又扩展了一下这两个方法，达到类似钩子的目的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functionApiInit</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: ComponentInstance</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">const</span> $options = vm.$options
  <span class="hljs-keyword">const</span> &#123; setup, render &#125; = $options
 
  <span class="hljs-keyword">if</span> (render) &#123;
    <span class="hljs-comment">// keep currentInstance accessible for createElement</span>
    $options.render = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args: any</span>): <span class="hljs-title">any</span> </span>&#123;
      <span class="hljs-keyword">return</span> activateCurrentInstance(vm, <span class="hljs-function">() =></span> render.apply(<span class="hljs-built_in">this</span>, args))
    &#125;
  &#125;
 
  <span class="hljs-keyword">if</span> (!setup) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> setup !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">if</span> (__DEV__) &#123;
      warn(
        <span class="hljs-string">'The "setup" option should be a function that returns a object in component definitions.'</span>,
        vm
      )
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;
 
  <span class="hljs-keyword">const</span> &#123; data &#125; = $options
  <span class="hljs-comment">// wrapper the data option, so we can invoke setup before data get resolved</span>
  $options.data = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrappedData</span>(<span class="hljs-params"></span>) </span>&#123;
    initSetup(vm, vm.$props)
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span>
      ? (data <span class="hljs-keyword">as</span> (
          <span class="hljs-built_in">this</span>: ComponentInstance,
          <span class="hljs-attr">x</span>: ComponentInstance
        ) => object).call(vm, vm)
      : data || &#123;&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然是先扩展的 render，但在 new Vue 的实际执行中会优先执行下方扩展的方法 “wrappedData”。因为 data 的执行是在 new Vue 时发生，而 render 的执行在 $mount 中。所以我们这里就按照执行顺序来看看如何扩展我们的 wrappedData。</p>
<p>wrappedData 这里只是简单执行了 initSetup 方法，对原先的 data 做了判断。这里是因为 Vue 执行时拿到的 data 已经是 wrappedData 这个函数而不是用户编写的 data，所以关于原 data 的处理移交在了 wrappedData 中。可以说 99%的逻辑都在 initSetup 中。我们接下来看这个方法。</p>
<h4 data-id="heading-6">setup 调用及处理</h4>
<p>这块是通过 initSetup  函数实现的，代码很长且仅有几行是这里不用关心的（可自行研究），整体上可以跟着注释走一遍。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initSetup</span>(<span class="hljs-params">vm: ComponentInstance, props: Record<any, any> = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-comment">// 获取定义好的 setup</span>
  <span class="hljs-keyword">const</span> setup = vm.$options.setup!
  <span class="hljs-comment">// 创建 setup 方法接收的第二个参数 context，主流程中使用不上，先忽略</span>
  <span class="hljs-keyword">const</span> ctx = createSetupContext(vm)
 
  <span class="hljs-comment">// fake reactive for `toRefs(props)`</span>
  <span class="hljs-comment">// porps 相关，主流成可先忽略（毕竟可以不写 props...）</span>
  def(props, <span class="hljs-string">'__ob__'</span>, createObserver())
 
  <span class="hljs-comment">// resolve scopedSlots and slots to functions</span>
  <span class="hljs-comment">// slots 相关，同 props 先忽略</span>
  <span class="hljs-comment">// @ts-expect-error</span>
  resolveScopedSlots(vm, ctx.slots)
 
  <span class="hljs-keyword">let</span> binding: ReturnType<SetupFunction<Data, Data>> | <span class="hljs-literal">undefined</span> | <span class="hljs-literal">null</span>
  <span class="hljs-comment">// 执行 setup</span>
  activateCurrentInstance(vm, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// make props to be fake reactive, this is for `toRefs(props)`</span>
    binding = setup(props, ctx)
  &#125;)
 
  <span class="hljs-comment">// 以下都是根据 setup 返回值，进行的一些处理</span>
  <span class="hljs-keyword">if</span> (!binding) <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">if</span> (isFunction(binding)) &#123;  <span class="hljs-comment">// setup 可以返回一个渲染函数（render）</span>
    <span class="hljs-comment">// keep typescript happy with the binding type.</span>
    <span class="hljs-keyword">const</span> bindingFunc = binding
    <span class="hljs-comment">// keep currentInstance accessible for createElement</span>
    <span class="hljs-comment">// 获取到渲染函数后，手动添加再 vue 实例上</span>
    vm.$options.render = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// @ts-expect-error</span>
      resolveScopedSlots(vm, ctx.slots)
      <span class="hljs-keyword">return</span> activateCurrentInstance(vm, <span class="hljs-function">() =></span> bindingFunc())
    &#125;
    <span class="hljs-keyword">return</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isPlainObject(binding)) &#123; <span class="hljs-comment">// setup 返回的是一个普通对象</span>
    <span class="hljs-keyword">if</span> (isReactive(binding)) &#123; <span class="hljs-comment">// 如果返回的是通过 reactive 方法定义的对象，需要通过 toRefs 结构</span>
      binding = toRefs(binding) <span class="hljs-keyword">as</span> Data
    &#125;
     
    <span class="hljs-comment">// 用于 slots 及 $refs ，先忽略</span>
    vmStateManager.set(vm, <span class="hljs-string">'rawBindings'</span>, binding)
    <span class="hljs-keyword">const</span> bindingObj = binding
 
    <span class="hljs-comment">// 遍历返回值，做一些处理</span>
    <span class="hljs-built_in">Object</span>.keys(bindingObj).forEach(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> bindingValue: any = bindingObj[name]
 
      <span class="hljs-keyword">if</span> (!isRef(bindingValue)) &#123;
        <span class="hljs-keyword">if</span> (!isReactive(bindingValue)) &#123;
          <span class="hljs-keyword">if</span> (isFunction(bindingValue)) &#123;
            bindingValue = bindingValue.bind(vm)
          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!isObject(bindingValue)) &#123;
            bindingValue = ref(bindingValue)
          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasReactiveArrayChild(bindingValue)) &#123;
            <span class="hljs-comment">// creates a custom reactive properties without make the object explicitly reactive</span>
            <span class="hljs-comment">// NOTE we should try to avoid this, better implementation needed</span>
            customReactive(bindingValue)
          &#125;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isArray(bindingValue)) &#123;
          bindingValue = ref(bindingValue)
        &#125;
      &#125;
      asVmProperty(vm, name, bindingValue)
    &#125;)
 
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 不是对象和方法时，在开发环境下抛错</span>
  <span class="hljs-keyword">if</span> (__DEV__) &#123;
    assert(
      <span class="hljs-literal">false</span>,
      <span class="hljs-string">`"setup" must return a "Object" or a "Function", got "<span class="hljs-subst">$&#123;<span class="hljs-built_in">Object</span>.prototype.toString
        .call(binding)
        .slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>)&#125;</span>"`</span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先聚焦到 setup 的执行。setup 包裹在  activateCurrentInstance 方法中，activateCurrentInstance 目的是为了设置当前的实例。类似我们平常写的交换a、b变量的值。setup 在调用前，会先获取 currentInstance 变量并赋值给 preVm，最开始时currentInstance 为 null。接着再把 currentInstance 设置成当前的 vue 实例，于是我们变可以在 setup 通过 插件提供的 getCurrentInstance 方法获取到当前实例。在执行完毕后，又通过 setCurrentInstance(preVm) 把 currentInstance 重置为null。所以印证了文档中所说的，只能在 setup 及生命周期（不在本篇重点）中使用 getCurrentInstance  方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// setup执行</span>
activateCurrentInstance(vm, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// make props to be fake reactive, this is for `toRefs(props)`</span>
  binding = setup(props, ctx)
&#125;)
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activateCurrentInstance</span>(<span class="hljs-params">vm, fn, onError</span>) </span>&#123;
  <span class="hljs-keyword">let</span> preVm = getCurrentVue2Instance()
  setCurrentInstance(vm)
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> fn(vm)
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-keyword">if</span> (onError) &#123;
      onError(err)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> err
    &#125;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    setCurrentInstance(preVm)
  &#125;
&#125;
 
 
<span class="hljs-keyword">let</span> currentInstance = <span class="hljs-literal">null</span>
 
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setCurrentInstance</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-comment">// currentInstance?.$scopedSlots</span>
  currentInstance = vm
&#125;
 
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCurrentVue2Instance</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> currentInstance
&#125;
 
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCurrentInstance</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (currentInstance) &#123;
    <span class="hljs-keyword">return</span> toVue3ComponentInstance(currentInstance)
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个思考，为什么需要在最后把 currentInstance 设置为 null？我们写了一个点击事件，并在相关的事件代码里调用了getCurrentInstance 。如果在 setup 调用重置为 null ，那么在该事件里就可能导致获取到错误的 currentInstance。于是就置为null 用来避免这个问题。（个人想法，期待指正）。</p>
<p>setup 内部可能会执行的东西有很多，比如通过 ref 定义一个响应式变量，这块放在后续单独说。</p>
<p>当获取完 setup 的返回值 binding 后，会根据其类型来做处理。如果返回函数，则说明这个 setup 返回的是一个渲染函数，便把放回值赋值给 vm.$options.render 供挂载时调用。如果返回的是一个对象，则会做一些相应式处理，这块内容和响应式相关，我们后续和响应式一块看。</p>
<pre><code class="copyable">// setup 返回对象

if (isReactive(binding)) &#123;
  binding = toRefs(binding) as Data
&#125;
 
vmStateManager.set(vm, 'rawBindings', binding)
const bindingObj = binding
 
Object.keys(bindingObj).forEach((name) => &#123;
  let bindingValue: any = bindingObj[name]
 
  if (!isRef(bindingValue)) &#123;
    if (!isReactive(bindingValue)) &#123;
      if (isFunction(bindingValue)) &#123;
        bindingValue = bindingValue.bind(vm)
      &#125; else if (!isObject(bindingValue)) &#123;
        bindingValue = ref(bindingValue)
      &#125; else if (hasReactiveArrayChild(bindingValue)) &#123;
        // creates a custom reactive properties without make the object explicitly reactive
        // NOTE we should try to avoid this, better implementation needed
        customReactive(bindingValue)
      &#125;
    &#125; else if (isArray(bindingValue)) &#123;
      bindingValue = ref(bindingValue)
    &#125;
  &#125;
  asVmProperty(vm, name, bindingValue)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这里只看重点函数 “asVmProperty”。我们知道 setup 返回的是一个对象 (赋值给了 binding / bindingObj)，且里面的所有属性都能在 vue 的其他选项中使用。那么这块是如何实现的呢？</p>
<h4 data-id="heading-7">访问 setup 返回值 — asVmProperty 实现</h4>
<p>这个函数执行后，我们就可以在 template 模版及 vue 选项中访问到 setup 的返回值，的下面是“asVmProperty” 这个函数的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asVmProperty</span>(<span class="hljs-params">vm, propName, propValue</span>) </span>&#123;
  <span class="hljs-keyword">const</span> props = vm.$options.props
  <span class="hljs-keyword">if</span> (!(propName <span class="hljs-keyword">in</span> vm) && !(props && hasOwn(props, propName))) &#123;
    <span class="hljs-keyword">if</span> (isRef(propValue)) &#123;
      proxy(vm, propName, &#123;
        <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> propValue.value,
        <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">val: unknown</span>) =></span> &#123;
          propValue.value = val
        &#125;,
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      proxy(vm, propName, &#123;
        <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">if</span> (isReactive(propValue)) &#123;
            ;(propValue <span class="hljs-keyword">as</span> any).__ob__.dep.depend()
          &#125;
          <span class="hljs-keyword">return</span> propValue
        &#125;,
        <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">val: any</span>) =></span> &#123;
          propValue = val
        &#125;,
      &#125;)
    &#125;
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">target, key, &#123; get, set &#125;</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.defineProperty(target, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">get</span>: get || noopFn,
    <span class="hljs-attr">set</span>: set || noopFn,
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数很短，这里有3个处理逻辑：</p>
<ol>
<li>普通属性的 get 和 set 正常返回</li>
<li>如果是 ref 类型的属性（通过 ref 创建），通过 vm.xxx 访问/修改时，访问/修改 ref 的 value 属性</li>
<li>代理 reactive 类型的属性 （通过 reactive 创建），reactive 返回的是一个响应式对象。当访问这个对象时， 需要调用 响应式对象种的 depend 收集watcher（观察者），以便数据更新时通知 watcher 进行更新。</li>
</ol>
<p>总之 asVmProperty 是拿到 setup 返回值中的一个键值对后，再通过 Object.defineProperty 劫持了 this（是vm，也就是组件实例）中访问改键值对的 get 和 set，这样我们便可以通过 this.xxx 访问到 setup 中return 出去的属性。</p>
<p>而模版访问也同理，因为 template 编译成 render 后，上面的变量都实际会编译成 _vm.xxx，而 _vm 就是 this ，也就是组件实例。</p></div>  
</div>
            