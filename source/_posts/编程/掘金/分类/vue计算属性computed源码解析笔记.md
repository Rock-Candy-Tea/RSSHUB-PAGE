
---
title: 'vue计算属性computed源码解析笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4914'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 00:45:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=4914'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>学习笔记，持续补充</strong></p>
<h4 data-id="heading-0">1. 使用示例 (<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23computed" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#computed" ref="nofollow noopener noreferrer">官网</a>)</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-comment">// 计算属性的 getter</span>
    <span class="hljs-comment">// 仅读取</span>
    <span class="hljs-attr">aDouble</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// `this` 指向 vm 实例</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a * <span class="hljs-number">2</span>
    &#125;,
    <span class="hljs-comment">// 读取和设置</span>
    <span class="hljs-attr">aPlus</span>: &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a + <span class="hljs-number">1</span>
      &#125;,
      <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">v</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.a = v - <span class="hljs-number">1</span>
      &#125;
    &#125;
  &#125;
&#125;)
vm.aPlus   <span class="hljs-comment">// => 2</span>
vm.aPlus = <span class="hljs-number">3</span>
vm.a       <span class="hljs-comment">// => 2</span>
vm.aDouble <span class="hljs-comment">// => 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>计算属性的结果会被缓存，除非依赖的响应式 property 变化才会重新计算。注意，如果某个依赖 (比如非响应式 property) 在该实例范畴之外，则计算属性是<strong>不会</strong>被更新的。</p>
<p>这是官网给的有关计算属性的说明，至于计算属性到底是个什么，为什么会被缓存呢？我们继续往下看</p>
<h4 data-id="heading-1">2. 源码解析（2.5.17beta版，多计算，少渲染）</h4>
<p>这里结合一个场景例子，直观的分析一下计算属性的实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">firstName</span>: <span class="hljs-string">'Foo'</span>,
    <span class="hljs-attr">lastName</span>: <span class="hljs-string">'Bar'</span>
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-attr">fullName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">' '</span> + <span class="hljs-built_in">this</span>.lastName
    &#125;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">1. initComputed（）</h5>
<p>首先，在vue初始化过程中，在 initState ( ) 中会对computed计算属性进行初始化处理，判断如果定义了计算属性，会执行</p>
<p>initComputed（）方法，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (opts.computed) initComputed(vm, opts.computed)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下这个  initComputed（）方法，主要分为四步</p>
<ul>
<li>创建一个空对象，用来保存watcher</li>
<li>对computed计算属性遍历，拿到定义的每一个计算属性</li>
<li>为每一个计算属性创建一个watcher</li>
<li>对遍历出的每一个计算属性做判断，如果不是vm上的属性，执行defineComputed ( )方法，如果是vm上的属性，判断当前计算属性名是不是已经在data和props定义了</li>
</ul>
<p>可以看一下下面代码及相关注释</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> computedWatcherOptions = &#123; <span class="hljs-attr">computed</span>: <span class="hljs-literal">true</span> &#125; <span class="hljs-comment">// 实例化Watcher时的配置项</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initComputed</span> (<span class="hljs-params">vm: Component, computed: <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-comment">// 第一步. 创建空对象 watchers，vm._computedWatchers</span>
  <span class="hljs-keyword">const</span> watchers = vm._computedWatchers = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  <span class="hljs-comment">// 判断是否是服务端渲染(SSR),这里我们分析的是浏览器环境</span>
  <span class="hljs-keyword">const</span> isSSR = isServerRendering()
  <span class="hljs-comment">// 第二步. 对computed计算属性遍历</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> computed) &#123;
    <span class="hljs-keyword">const</span> userDef = computed[key] <span class="hljs-comment">// 拿到定义的每一个计算属性的value</span>
    <span class="hljs-comment">// 判断上边拿到的计算属的value，是否是function，如果是function，直接赋值给getter，不是的话将计算属性的get赋值给getter（看下官网计算属性定义的方式，---->示例）</span>
    <span class="hljs-keyword">const</span> getter = <span class="hljs-keyword">typeof</span> userDef === <span class="hljs-string">'function'</span> ? userDef : userDef.get
    <span class="hljs-comment">// 如果计算属性没定义getter，给出警告</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && getter == <span class="hljs-literal">null</span>) &#123;
      warn(
        <span class="hljs-string">`Getter is missing for computed property "<span class="hljs-subst">$&#123;key&#125;</span>".`</span>,
        vm
      )
    &#125;

    <span class="hljs-keyword">if</span> (!isSSR) &#123;
      <span class="hljs-comment">// 第三步. 为每一个getter创建一个watcher（可以称为computed watcher，在下面对实例化computed watcher进行了分析）</span>
      watchers[key] = <span class="hljs-keyword">new</span> Watcher(
        vm,
        getter || noop,
        noop,
        computedWatcherOptions
      )
    &#125;

    <span class="hljs-comment">// component-defined computed properties are already defined on the</span>
    <span class="hljs-comment">// component prototype. We only need to define computed properties defined</span>
    <span class="hljs-comment">// at instantiation here. 组件定义的计算属性已经在组件原型上定义了</span>
    
    <span class="hljs-comment">// 第四步. 判断key，如果不是vm的属性，执行defineComputed（ ）做响应式处理</span>
    <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> vm)) &#123;
      defineComputed(vm, key, userDef)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">// 如果key已经在data，或者props中定义了，给出警告</span>
      <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> vm.$data) &#123;
        warn(<span class="hljs-string">`The computed property "<span class="hljs-subst">$&#123;key&#125;</span>" is already defined in data.`</span>, vm)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (vm.$options.props && key <span class="hljs-keyword">in</span> vm.$options.props) &#123;
        warn(<span class="hljs-string">`The computed property "<span class="hljs-subst">$&#123;key&#125;</span>" is already defined as a prop.`</span>, vm)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>下面我们分析一下以上四步中所做的一些处理</strong></p>
<h5 data-id="heading-3">2. defineComputed（）</h5>
<p>这个方法，他的目的就是利用Object.defineProperty（）给每一个计算属性添加getter和setter，使之响应式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 定义一个对象，当作Object.defineProperty（）的参数</span>
<span class="hljs-keyword">const</span> sharedPropertyDefinition = &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">get</span>: noop, <span class="hljs-comment">// 空函数</span>
  <span class="hljs-attr">set</span>: noop
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineComputed</span> (<span class="hljs-params">
  target: any,
  key: string, <span class="hljs-comment">// 定义的计算属性名</span>
  userDef: <span class="hljs-built_in">Object</span> | <span class="hljs-built_in">Function</span> <span class="hljs-comment">// 计算属性所做的处理</span>
</span>) </span>&#123;
  <span class="hljs-comment">// 下面的操作就是给定义的这个 sharedPropertyDefinition 对象添加get和set处理函数</span>
  <span class="hljs-keyword">const</span> shouldCache = !isServerRendering() <span class="hljs-comment">// 非服务器端渲染</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> userDef === <span class="hljs-string">'function'</span>) &#123; <span class="hljs-comment">// 是函数</span>
    sharedPropertyDefinition.get = shouldCache
      ? createComputedGetter(key)
      : userDef
    sharedPropertyDefinition.set = noop
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 是对象</span>
    sharedPropertyDefinition.get = userDef.get
      ? shouldCache && userDef.cache !== <span class="hljs-literal">false</span>
        ? createComputedGetter(key)
        : userDef.get
      : noop
    sharedPropertyDefinition.set = userDef.set
      ? userDef.set
      : noop
  &#125; 
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
      sharedPropertyDefinition.set === noop) &#123;
    sharedPropertyDefinition.set = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      warn(
        <span class="hljs-string">`Computed property "<span class="hljs-subst">$&#123;key&#125;</span>" was assigned to but it has no setter.`</span>,
        <span class="hljs-built_in">this</span>
      )
    &#125;
  &#125;
  <span class="hljs-comment">// 最后，调用Object.defineProperty对计算属性进行处理</span>
  <span class="hljs-built_in">Object</span>.defineProperty(target, key, sharedPropertyDefinition)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这里我们先忽略计算属性对set函数的处理，在平时的开发场景中，计算属性有 setter 的情况比较少，主要分析一下getter, 上面对于get函数的定义，在我们平常使用的浏览器环境中会进入createComputedGetter （ ），我们来看一下这个函数做了什么，继续往下</strong></p>
<h5 data-id="heading-4">3. createComputedGetter（）</h5>
<p>最终getter对应的是createComputedGetter（）的返回值，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComputedGetter</span> (<span class="hljs-params">key</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computedGetter</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 这里会去获取this._computedWatchers，这个是上面在initComputed中定义在vm 上的对象，可以通过this访问到，这个对象保存的是每一个计算属性的watcher，下面定义的这个 watcher，就是取到的每个计算属性的watcher</span>
    <span class="hljs-keyword">const</span> watcher = <span class="hljs-built_in">this</span>._computedWatchers && <span class="hljs-built_in">this</span>._computedWatchers[key]
    <span class="hljs-keyword">if</span> (watcher) &#123;
      <span class="hljs-comment">// 调用watcher.depend()，返回watcher.evaluate()，这是什么？？看下面 4</span>
      watcher.depend()
      <span class="hljs-keyword">return</span> watcher.evaluate()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对于返回的这个函数，如果会调用depend ( )和evaluate ( )方法，这俩方法定义在Watcher这个类中，如下</strong></p>
<h5 data-id="heading-5">4. 计算属性的new Watcher（）</h5>
<p>Watcher是定义的一个类，下面我直接把定义Watcher的代码拿了过来，有点多，大家可以看下，和计算属性相关的，我会随后拿出来分析</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* @flow */</span>

<span class="hljs-keyword">import</span> &#123;
  warn,
  remove,
  isObject,
  parsePath,
  _Set <span class="hljs-keyword">as</span> <span class="hljs-built_in">Set</span>,
  handleError
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util/index'</span>

<span class="hljs-keyword">import</span> &#123; traverse &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./traverse'</span>
<span class="hljs-keyword">import</span> &#123; queueWatcher &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./scheduler'</span>
<span class="hljs-keyword">import</span> Dep, &#123; pushTarget, popTarget &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./dep'</span>

<span class="hljs-keyword">import</span> type &#123; SimpleSet &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util/index'</span>

<span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>

<span class="hljs-comment">/**
 * A watcher parses an expression, collects dependencies,
 * and fires callback when the expression value changes.
 * This is used for both the $watch() api and directives.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-attr">vm</span>: Component;
  expression: string;
  cb: <span class="hljs-built_in">Function</span>;
  id: number;
  deep: boolean;
  user: boolean;
  computed: boolean;
  sync: boolean;
  dirty: boolean;
  active: boolean;
  dep: Dep;
  deps: <span class="hljs-built_in">Array</span><Dep>;
  newDeps: <span class="hljs-built_in">Array</span><Dep>;
  depIds: SimpleSet;
  newDepIds: SimpleSet;
  before: ?<span class="hljs-built_in">Function</span>;
  getter: <span class="hljs-built_in">Function</span>;
  value: any;

  <span class="hljs-title">constructor</span> (<span class="hljs-params">
    vm: Component,
    expOrFn: string | <span class="hljs-built_in">Function</span>,
    cb: <span class="hljs-built_in">Function</span>,
    options?: ?<span class="hljs-built_in">Object</span>,
    isRenderWatcher?: boolean
  </span>) &#123;
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-keyword">if</span> (isRenderWatcher) &#123;
      vm._watcher = <span class="hljs-built_in">this</span>
    &#125;
    vm._watchers.push(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// options</span>
    <span class="hljs-keyword">if</span> (options) &#123;
      <span class="hljs-built_in">this</span>.deep = !!options.deep
      <span class="hljs-built_in">this</span>.user = !!options.user
      <span class="hljs-built_in">this</span>.computed = !!options.computed
      <span class="hljs-built_in">this</span>.sync = !!options.sync
      <span class="hljs-built_in">this</span>.before = options.before
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.deep = <span class="hljs-built_in">this</span>.user = <span class="hljs-built_in">this</span>.computed = <span class="hljs-built_in">this</span>.sync = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-built_in">this</span>.cb = cb
    <span class="hljs-built_in">this</span>.id = ++uid <span class="hljs-comment">// uid for batching</span>
    <span class="hljs-built_in">this</span>.active = <span class="hljs-literal">true</span>
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-built_in">this</span>.computed <span class="hljs-comment">// for computed watchers</span>
    <span class="hljs-built_in">this</span>.deps = []
    <span class="hljs-built_in">this</span>.newDeps = []
    <span class="hljs-built_in">this</span>.depIds = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
    <span class="hljs-built_in">this</span>.newDepIds = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
    <span class="hljs-built_in">this</span>.expression = process.env.NODE_ENV !== <span class="hljs-string">'production'</span>
      ? expOrFn.toString()
      : <span class="hljs-string">''</span>
    <span class="hljs-comment">// parse expression for getter</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> expOrFn === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-built_in">this</span>.getter = expOrFn
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.getter = parsePath(expOrFn)
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.getter) &#123;
        <span class="hljs-built_in">this</span>.getter = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
        process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
          <span class="hljs-string">`Failed watching path: "<span class="hljs-subst">$&#123;expOrFn&#125;</span>" `</span> +
          <span class="hljs-string">'Watcher only accepts simple dot-delimited paths. '</span> +
          <span class="hljs-string">'For full control, use a function instead.'</span>,
          vm
        )
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.computed) &#123;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>
      <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get()
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Evaluate the getter, and re-collect dependencies.
   */</span>
  get () &#123;
    pushTarget(<span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">let</span> value
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>.vm
    <span class="hljs-keyword">try</span> &#123;
      value = <span class="hljs-built_in">this</span>.getter.call(vm, vm)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
        handleError(e, vm, <span class="hljs-string">`getter for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> e
      &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// "touch" every property so they are all tracked as</span>
      <span class="hljs-comment">// dependencies for deep watching</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.deep) &#123;
        traverse(value)
      &#125;
      popTarget()
      <span class="hljs-built_in">this</span>.cleanupDeps()
    &#125;
    <span class="hljs-keyword">return</span> value
  &#125;

  <span class="hljs-comment">/**
   * Add a dependency to this directive.
   */</span>
  addDep (dep: Dep) &#123;
    <span class="hljs-keyword">const</span> id = dep.id
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.newDepIds.has(id)) &#123;
      <span class="hljs-built_in">this</span>.newDepIds.add(id)
      <span class="hljs-built_in">this</span>.newDeps.push(dep)
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.depIds.has(id)) &#123;
        dep.addSub(<span class="hljs-built_in">this</span>)
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Clean up for dependency collection.
   */</span>
  cleanupDeps () &#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.deps.length
    <span class="hljs-keyword">while</span> (i--) &#123;
      <span class="hljs-keyword">const</span> dep = <span class="hljs-built_in">this</span>.deps[i]
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.newDepIds.has(dep.id)) &#123;
        dep.removeSub(<span class="hljs-built_in">this</span>)
      &#125;
    &#125;
    <span class="hljs-keyword">let</span> tmp = <span class="hljs-built_in">this</span>.depIds
    <span class="hljs-built_in">this</span>.depIds = <span class="hljs-built_in">this</span>.newDepIds
    <span class="hljs-built_in">this</span>.newDepIds = tmp
    <span class="hljs-built_in">this</span>.newDepIds.clear()
    tmp = <span class="hljs-built_in">this</span>.deps
    <span class="hljs-built_in">this</span>.deps = <span class="hljs-built_in">this</span>.newDeps
    <span class="hljs-built_in">this</span>.newDeps = tmp
    <span class="hljs-built_in">this</span>.newDeps.length = <span class="hljs-number">0</span>
  &#125;

  <span class="hljs-comment">/**
   * Subscriber interface.
   * Will be called when a dependency changes.
   */</span>
  update () &#123;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.computed) &#123;
      <span class="hljs-comment">// A computed property watcher has two modes: lazy and activated.</span>
      <span class="hljs-comment">// It initializes as lazy by default, and only becomes activated when</span>
      <span class="hljs-comment">// it is depended on by at least one subscriber, which is typically</span>
      <span class="hljs-comment">// another computed property or a component's render function.</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dep.subs.length === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// In lazy mode, we don't want to perform computations until necessary,</span>
        <span class="hljs-comment">// so we simply mark the watcher as dirty. The actual computation is</span>
        <span class="hljs-comment">// performed just-in-time in this.evaluate() when the computed property</span>
        <span class="hljs-comment">// is accessed.</span>
        <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// In activated mode, we want to proactively perform the computation</span>
        <span class="hljs-comment">// but only notify our subscribers when the value has indeed changed.</span>
        <span class="hljs-built_in">this</span>.getAndInvoke(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">this</span>.dep.notify()
        &#125;)
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
      <span class="hljs-built_in">this</span>.run()
    &#125; <span class="hljs-keyword">else</span> &#123;
      queueWatcher(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Scheduler job interface.
   * Will be called by the scheduler.
   */</span>
  run () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.active) &#123;
      <span class="hljs-built_in">this</span>.getAndInvoke(<span class="hljs-built_in">this</span>.cb)
    &#125;
  &#125;

  getAndInvoke (cb: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.get()
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
      <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
        <span class="hljs-keyword">try</span> &#123;
          cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          handleError(e, <span class="hljs-built_in">this</span>.vm, <span class="hljs-string">`callback for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Evaluate and return the value of the watcher.
   * This only gets called for computed property watchers.
   */</span>
  evaluate () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dirty) &#123;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get()
      <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value
  &#125;

  <span class="hljs-comment">/**
   * Depend on this watcher. Only for computed property watchers.
   */</span>
  depend () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dep && Dep.target) &#123;
      <span class="hljs-built_in">this</span>.dep.depend()
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Remove self from all dependencies' subscriber list.
   */</span>
  teardown () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.active) &#123;
      <span class="hljs-comment">// remove self from vm's watcher list</span>
      <span class="hljs-comment">// this is a somewhat expensive operation so we skip it</span>
      <span class="hljs-comment">// if the vm is being destroyed.</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.vm._isBeingDestroyed) &#123;
        remove(<span class="hljs-built_in">this</span>.vm._watchers, <span class="hljs-built_in">this</span>)
      &#125;
      <span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.deps.length
      <span class="hljs-keyword">while</span> (i--) &#123;
        <span class="hljs-built_in">this</span>.deps[i].removeSub(<span class="hljs-built_in">this</span>)
      &#125;
      <span class="hljs-built_in">this</span>.active = <span class="hljs-literal">false</span>
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面执行initComputed（ ）的时候，在我们所说的第三步中，遍历实例化创建了计算属性的watcher （computed watcher)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  watchers[key] = <span class="hljs-keyword">new</span> Watcher(
        vm,
        getter || noop,
        noop,
        computedWatcherOptions  <span class="hljs-comment">// const computedWatcherOptions = &#123; computed: true &#125;</span>
      )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简化一下new Watcher，我们看一下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title">constructor</span> (<span class="hljs-params">
  vm: Component,
  expOrFn: string | <span class="hljs-built_in">Function</span>,
  cb: <span class="hljs-built_in">Function</span>,
  options?: ?<span class="hljs-built_in">Object</span>,
  isRenderWatcher?: boolean
</span>) &#123;
  
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.computed) &#123; <span class="hljs-comment">// 判断this.computed</span>
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep()
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get() <span class="hljs-comment">// 调用get()求值</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看到，计算属性的watcher并不会立即求值，而是判断了this.computed，同时实例化了一个dep实例。</p>
<p><strong>在vue渲染数据到页面这一过程中</strong>，如果访问到定义的计算属性时，就会触发计算属性的getter（ getter对应的是 上边所说的createComputedGetter（ ）函数的返回值 ），拿到计算属性对应的watcher，然后执行Watcher中的depend 方法，并且返回evaluate方法处理后的值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">if</span> (watcher) &#123;
      watcher.depend()
      <span class="hljs-keyword">return</span> watcher.evaluate()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>depend 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
  * Depend on this watcher. Only for computed property watchers.
  */</span>
depend () &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dep && Dep.target) &#123;
    <span class="hljs-built_in">this</span>.dep.depend()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，这时候的 Dep.target 是渲染 watcher ，所以 this.dep.depend( ) 相当于渲染 watcher 订阅了这个 computed watcher  的变化。</p>
<p>然后再执行watcher.evaluate ( ) 求值</p>
<p>evaluate（ ）这个函数 首先判断this.dirty，如果为true，会调用get ( ) 求值，get ( )也定义在Watcher这个类中，他的核心就是</p>
<p>value = this.getter.call(vm, vm) ，<strong>实际上就是调用计算属性中定义的getter函数，求值</strong>，   并把this.dirty设置为false，最后返回所求的值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
  * Evaluate and return the value of the watcher.
  * This only gets called for computed property watchers.
  */</span>
evaluate () &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dirty) &#123;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get()
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要特别注意的是，由于 <code>this.firstName</code> 和 <code>this.lastName</code> 都是响应式对象，这里会触发它们的 getter，根据我们之前的分析，它们会把自身持有的 <code>dep</code> 添加到当前正在计算的 <code>watcher</code> 中，这个时候 <code>Dep.target</code> 就是这个 <code>computed watcher</code>。</p>
<h5 data-id="heading-6">5. 修改计算属性所依赖的数据</h5>
<p>一旦我们对计算属性所依赖的数据进行修改, 会触发setter过程，通知所有订阅他变化的watcher更新（ dep.notify ( )  ）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> notify () &#123;
    <span class="hljs-comment">// stabilize the subscriber list first</span>
    <span class="hljs-keyword">const</span> subs = <span class="hljs-built_in">this</span>.subs.slice()
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = subs.length; i < l; i++) &#123;
      subs[i].update()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，遍历循环，并执行watcher的update ( )方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> update () &#123;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.computed) &#123;
      <span class="hljs-comment">// A computed property watcher has two modes: lazy and activated.</span>
      <span class="hljs-comment">// It initializes as lazy by default, and only becomes activated when</span>
      <span class="hljs-comment">// it is depended on by at least one subscriber, which is typically</span>
      <span class="hljs-comment">// another computed property or a component's render function.</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dep.subs.length === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// In lazy mode, we don't want to perform computations until necessary,</span>
        <span class="hljs-comment">// so we simply mark the watcher as dirty. The actual computation is</span>
        <span class="hljs-comment">// performed just-in-time in this.evaluate() when the computed property</span>
        <span class="hljs-comment">// is accessed.</span>
        <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// In activated mode, we want to proactively perform the computation</span>
        <span class="hljs-comment">// but only notify our subscribers when the value has indeed changed.</span>
        <span class="hljs-built_in">this</span>.getAndInvoke(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">this</span>.dep.notify()
        &#125;)
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
      <span class="hljs-built_in">this</span>.run()
    &#125; <span class="hljs-keyword">else</span> &#123;
      queueWatcher(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于计算属性的watcher，他实际上有两种模式，lazy和active，如果this.dep.subs.length === 0说明没有人去订阅这个计算属性watcher的变化，把this.dirty设为true，使只有当下次再访问这个计算属性的时候才会重新求值。</p>
<p>在我们所举例的场景下，渲染 watcher 订阅了这个 computed watcher  的变化，那么它会执行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-built_in">this</span>.getAndInvoke(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.dep.notify()
   &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">getAndInvoke (cb: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> value = <span class="hljs-built_in">this</span>.get() <span class="hljs-comment">// 会重新计算</span>
    <span class="hljs-comment">// 新旧值会进行比较，如果变化了 ，才会执行传入的回调函数</span>
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
      <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
        <span class="hljs-keyword">try</span> &#123;
          cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          handleError(e, <span class="hljs-built_in">this</span>.vm, <span class="hljs-string">`callback for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getAndInvoke 函数会重新计算，然后对比新旧值，如果变化了则执行回调函数，那么这里这个回调函数是 this.dep.notify()，在我们这个场景下就是触发了渲染 watcher重新渲染</p>
<p><strong>这里对计算属性的新旧值会进行比较，这样保证了，当计算属性依赖的值发生变化时，他会被重新计算，但不一定会重新渲染，只有计算出来的新值相对于旧值改变了，才会触发渲染watcher重新渲染，本质上这是vue的一种优化，多计算，少更新</strong></p>
<h4 data-id="heading-7">3. 源码解析（2.6.13版本，多渲染，少计算）</h4>
<p>在watch的update方法中，没有getAndInvoke这一方法，不会比较计算属性计算出的新旧值，不管相等否，都会触发updateComponent去update更新渲染</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Watcher.prototype.update = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">/* istanbul ignore else */</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.lazy) &#123;
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
    <span class="hljs-built_in">this</span>.run();
  &#125; <span class="hljs-keyword">else</span> &#123;
    queueWatcher(<span class="hljs-built_in">this</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看之前版本（2.5.17beta)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Watcher.prototype.update = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> this$<span class="hljs-number">1</span> = <span class="hljs-built_in">this</span>;

  <span class="hljs-comment">/* istanbul ignore else */</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.computed) &#123;
    <span class="hljs-comment">// A computed property watcher has two modes: lazy and activated.</span>
    <span class="hljs-comment">// It initializes as lazy by default, and only becomes activated when</span>
    <span class="hljs-comment">// it is depended on by at least one subscriber, which is typically</span>
    <span class="hljs-comment">// another computed property or a component's render function.</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.dep.subs.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// In lazy mode, we don't want to perform computations until necessary,</span>
      <span class="hljs-comment">// so we simply mark the watcher as dirty. The actual computation is</span>
      <span class="hljs-comment">// performed just-in-time in this.evaluate() when the computed property</span>
      <span class="hljs-comment">// is accessed.</span>
      <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// In activated mode, we want to proactively perform the computation</span>
      <span class="hljs-comment">// but only notify our subscribers when the value has indeed changed.</span>
      <span class="hljs-built_in">this</span>.getAndInvoke(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        this$<span class="hljs-number">1.</span>dep.notify();
      &#125;);
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123;
    <span class="hljs-built_in">this</span>.run();
  &#125; <span class="hljs-keyword">else</span> &#123;
    queueWatcher(<span class="hljs-built_in">this</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下getAndInvoke ( )方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Watcher.prototype.getAndInvoke = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getAndInvoke</span> (<span class="hljs-params">cb</span>) </span>&#123;
  <span class="hljs-keyword">var</span> value = <span class="hljs-built_in">this</span>.get();
  <span class="hljs-comment">// 做了判断，如果计算出的新值和旧值不一样 的话，才会继续执行，如果一样，就不会继续，，不会再次渲染</span>
  <span class="hljs-keyword">if</span> ( 
    value !== <span class="hljs-built_in">this</span>.value ||   
    <span class="hljs-comment">// Deep watchers and watchers on Object/Arrays should fire even</span>
    <span class="hljs-comment">// when the value is the same, because the value may</span>
    <span class="hljs-comment">// have mutated.</span>
    isObject(value) ||
    <span class="hljs-built_in">this</span>.deep
  ) &#123;
    <span class="hljs-comment">// set new value</span>
    <span class="hljs-keyword">var</span> oldValue = <span class="hljs-built_in">this</span>.value;
    <span class="hljs-built_in">this</span>.value = value;
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
      <span class="hljs-keyword">try</span> &#123;
        cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        handleError(e, <span class="hljs-built_in">this</span>.vm, (<span class="hljs-string">"callback for watcher \""</span> + (<span class="hljs-built_in">this</span>.expression) + <span class="hljs-string">"\""</span>));
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            