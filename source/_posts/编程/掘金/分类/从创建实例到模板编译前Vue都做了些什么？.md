
---
title: '从创建实例到模板编译前Vue都做了些什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4466'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 02:32:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=4466'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">写在前面</h1>
<p><a href="https://juejin.cn/post/6987425001532031013" target="_blank" title="https://juejin.cn/post/6987425001532031013">Vue构造函数的创建过程</a> 一文中介绍了 Vue构造函数 的创建过程，其中第一个对 Vue构造函数 进行成员添加的就是 initMixin(Vue)，该调用内创建了 _init 方法。可以说，Vue实例 的大门就是 _init 方法，因此，我们从这个方法入手，一步一步剖析 vm 是如何生成的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
<div id="app">
  <div>
    <h1>&#123;&#123;msg&#125;&#125;</h1>
    <div id="extendUse"></div>
    <child-component :msg="msg" />
  </div>
</div>
*/</span>
<span class="hljs-comment">// Vue.extend 手动挂载组件</span>
<span class="hljs-keyword">const</span> ExtendUse = Vue.extend(&#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'msg'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<h2>ExtendUse said: &#123;&#123;msg&#125;&#125;</h2>`</span>,
&#125;)
<span class="hljs-keyword">const</span> ChildExtend = <span class="hljs-keyword">new</span> ExtendUse(&#123;
  <span class="hljs-attr">propsData</span>: &#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'hello Extend'</span>
  &#125;
&#125;).$mount(<span class="hljs-string">'#extendUse'</span>)
<span class="hljs-comment">// Vue.component 自动挂载组件</span>
<span class="hljs-keyword">const</span> ChildComponent = Vue.extend(&#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'msg'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<h2>child's father said: &#123;&#123;msg&#125;&#125;</h2>`</span>,
&#125;)
Vue.component(<span class="hljs-string">'child-component'</span>, ChildComponent)
<span class="hljs-comment">// Vue 实例</span>
<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'hello Vue'</span>,
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照惯例，我先将 _init 的源码简写一下，并且划分一下步骤:</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-comment">// 步骤 - 1</span>
  <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>
  vm._uid = uid++
  vm._isVue = <span class="hljs-literal">true</span>
  <span class="hljs-comment">// 步骤 - 2</span>
  <span class="hljs-keyword">if</span> (options && options._isComponent) &#123;
    initInternalComponent(vm, options)
  &#125; <span class="hljs-keyword">else</span> &#123;
    vm.$options = mergeOptions(
      resolveConstructorOptions(vm.constructor),
      options || &#123;&#125;,
      vm
    )
  &#125;
  <span class="hljs-comment">// 步骤 - 3</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    initProxy(vm)
  &#125; <span class="hljs-keyword">else</span> &#123;
    vm._renderProxy = vm
  &#125;
  vm._self = vm
  <span class="hljs-comment">// 步骤 - 4</span>
  initLifecycle(vm)
  initEvents(vm)
  initRender(vm)
  callHook(vm, <span class="hljs-string">'beforeCreate'</span>)
  initInjections(vm)
  initState(vm)
  initProvide(vm)
  callHook(vm, <span class="hljs-string">'created'</span>)
  <span class="hljs-comment">// 步骤 - 5</span>
  <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
    vm.$mount(vm.$options.el)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">步骤 - 1</h1>
<p><strong>在这段代码中，我们首要了解的是 vm 指向了谁？</strong>
从它的调用 <code>function Vue(options) &#123; this._init(options) &#125;</code> 中我们可以了解到，Vue 是一个构造函数，而 _init 方法又不是该构造函数的静态方法，因此 this 指向了实例，所以 <code>const vm = this</code> 这一步其实就是将实例本身赋值给了 vm。<br>
再具体点？<code>const app = new Vue(options)</code> 这里的 app 就是 vm 的值。<br>
接着，在实例身上添加上 _uid 和 _isVue 的标识，记录当前实例是第 (_uid + 1) 个 Vue 实例对象。</p>
<h1 data-id="heading-2">步骤 - 2</h1>
<p>这段代码是一个条件判断，判断的是是否是一个组件。那怎样的存在算是一个组件呢？Vue.extend 手动挂载上去的算不算一个组件呢？<br>
我就先兜个底，只有存在于 vm.options.components 中的才算组件，且能进入 if 判断之中。这就意味着，要么 <code>Vue.component(id, definition)</code> 定义的对象，要么 <code>new Vue(&#123; components: &#123; id: definition &#125; &#125;)</code> 定义的对象，其他方式都不具备 _isComponent 属性。因此，即使是 Vue.component 方法内同样也调用了的 Vue.extend 方法，在手动挂载时也不算作组件，不具备 _isComponent 属性。<br>
那这段代码的意义是什么呢？简而言之，就是将 Vue构造函数 中的成员变量 options 和我们传入的 options 合并然后挂载到实例的 $options 属性上。</p>
<h2 data-id="heading-3">initInternalComponent</h2>
<p>不知道大家想没想过，组件为什么会进到 _init 中来，哪儿定义了它也可以进来进行初始化操作？<br>
如果你没有忘记 <a href="https://juejin.cn/post/6988086842000146440" target="_blank" title="https://juejin.cn/post/6988086842000146440">Vue.component和Vue.extend都做了些什么？</a> 一文中讲过，Vue.component 中会调用一次 Vue.extend，将生成的实例存入 vm.options.components 之中。而在 Vue.extend 中我们曾定义过一个 VueComponent构造函数，这个构造函数继承了 Vue构造函数，因此也有 _init 方法，在 VueComponent构造函数 的 constructor 中又恰好调用了 <code>this._init(options)</code>，所以套了一层又一层，剥丝抽茧后你应该就能明白为什么组件可以进来了吧。<br>
那么，这个方法内做了些什么？当你进入函数题你会发现，options 中哪来的这么多属性？？？我丢，见都没见过啊，一脸懵逼逐渐变成N脸懵逼。所以我们先按下不表，因为其中涉及到模板编译部分，扯得太远回不来就麻烦了。</p>
<h2 data-id="heading-4">resolveConstructorOptions</h2>
<p>既然不讲组件的 options 合并，那总得讲讲 <code>new (Vue.extend(extendOptions))(options) / new Vue(options)</code> 的 options 合并啊，讲讲讲，这不就来了么。先声明一下，以下 vm 指的是 Vue构造函数 的实例，componentVM 指的是 Vue.extend 返回的构造函数的实例。<br>
这个方法本质上是为了得到 Vue构造函数 身上的 options。<br>
如果传入的 constructor 没有 super 属性，则说明当前实例是 vm，直接返回 vm.constructor.options。<br>
如果传入的 constructor 拥有 super 属性，则说明当前实例是 componentVM，那么当前的 vm.constructor.options 就是 VueComponent.options。如果 VueComponent.superOptions 和 VueComponent.super.options 不相等时会将 VueComponent.superOptions 更新，得到最新的 VueComponent.options 然后返回，否则直接返回 VueComponent.options。</p>
<h3 data-id="heading-5">mergeOptions</h3>
<p>首先，我们需要了解这个方法做了什么。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeOptions</span> (<span class="hljs-params">parent, child, vm</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    checkComponents(child)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> child === <span class="hljs-string">'function'</span>) &#123;
    child = child.options
  &#125;
  normalizeProps(child, vm)
  normalizeInject(child, vm)
  normalizeDirectives(child)
  <span class="hljs-keyword">const</span> extendsFrom = child.extends
  <span class="hljs-keyword">if</span> (extendsFrom) &#123;
    parent = mergeOptions(parent, extendsFrom, vm)
  &#125;
  <span class="hljs-keyword">if</span> (child.mixins) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = child.mixins.length; i < l; i++) &#123;
      parent = mergeOptions(parent, child.mixins[i], vm)
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> options = &#123;&#125;
  <span class="hljs-keyword">let</span> key
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
  <span class="hljs-keyword">return</span> options
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">checkComponents</h4>
<p>判断 (vm | componentVM).options.components: &#123; id: definition &#125; 的 id 是否等于 slot / component 或其他原生 HTML 标签，如果是则报错。</p>
<h4 data-id="heading-7">normalizeProps</h4>
<p>当 (vm | componentVM) 中传入的 options 中存在 props 时激活该方法，目的是为了格式化 props 中的属性。<br>
如果 options.props 是一个数组，则将 options.props 的值统一成 &#123; item: &#123; type: null &#125; &#125;。<br>
如果 options.props 是一个对象，则将 options.props 的值统一成 &#123; key: &#123; type: value &#125; &#125;。<br>
当 key 是以短横线命名法( name-space )命名时将其转换成驼峰命名法( nameSpace )</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 如果 options.props 是一个数组</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'msg'</span>, <span class="hljs-string">'aeo-rus'</span>]
&#125;)
<span class="hljs-comment">/*
props: &#123;
  msg: &#123;
    type: null
  &#125;,
  aeoRus: &#123;
    type: null
  &#125;
&#125;
*/</span>
<span class="hljs-comment">// 如果 options.props 是一个对象</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">msg</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'hello Vue'</span>
    &#125;,
    <span class="hljs-string">'aeo-rus'</span>: &#123;
      <span class="hljs-attr">default</span>: <span class="hljs-string">'aeorus'</span>
    &#125;,
  &#125;
&#125;)
<span class="hljs-comment">/*
props: &#123;
  msg: &#123;
    type: String,
    default: 'hello Vue'
  &#125;,
  aeoRus: &#123;
    default: 'aeorus'
  &#125;
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">normalizeInject</h4>
<p>当 (vm | componentVM) 中传入的 options 中存在 inject 时激活该方法，目的是为了格式化 inject 中的属性。<br>
如果 options.inject 是一个数组，则将 options.inject 的值统一成 &#123; item: &#123; from: item &#125; &#125;。<br>
如果 options.inject 是一个对象，则将 options.inject 的值统一成 &#123; key: &#123; from: value &#125; &#125; ( 当 value 也是对象时则统一成 &#123; from: key, value.k: value.v &#125; )。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">inject</span>: [<span class="hljs-string">'onload'</span>, <span class="hljs-string">'reload'</span>]
&#125;)
<span class="hljs-comment">/*
inject: &#123;
  onload: &#123;
    from: 'onload'
  &#125;,
  reload: &#123;
    from: 'reload'
  &#125;
&#125;
*/</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">inject</span>: &#123;
    <span class="hljs-attr">onload</span>: &#123;
      <span class="hljs-attr">from</span>: <span class="hljs-string">'onlaunch'</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'onload'</span>
    &#125;,
    <span class="hljs-attr">reload</span>: <span class="hljs-string">'reload'</span>
  &#125;
&#125;)
<span class="hljs-comment">/*
inject: &#123;
  onload: &#123;
    from: 'onlaunch',
    default: 'onload'
  &#125;,
  reload: &#123;
    from: 'reload'
  &#125;
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">normalizeDirectives</h4>
<p>当 (vm | componentVM) 中传入的 options 中存在 directives 时激活该方法，目的是为了格式化 directives 中的指令。<br>
将 options.directives 的值统一成 &#123; key: &#123; bind: value, update: value &#125; &#125; ( 有可能 value 是一个方法 ) 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">directives</span>: &#123;
    <span class="hljs-attr">focus</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el</span>)</span> &#123;
        el.focus()
      &#125;
    &#125;
  &#125;
&#125;)
<span class="hljs-comment">/*
directives: &#123;
  focus: &#123;
    inserted: el => &#123;
      el.focus()
    &#125;
  &#125;
&#125;
*/</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">directives</span>: &#123;
    <span class="hljs-attr">focus</span>: <span class="hljs-function"><span class="hljs-params">el</span> =></span> &#123;
      el.focus()
    &#125;
  &#125;
&#125;)
<span class="hljs-comment">/*
directives: &#123;
  focus: &#123;
    bind: el => &#123;
      el.focus()
    &#125;,
    update: el => &#123;
      el.focus()
    &#125;
  &#125;
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">extends / mixins</h4>
<p>当 (vm | componentVM) 中传入的 options 中存在 extends / mixins 时进入条件判断，递归 mergeOptions 方法，将 extends / mixins 的对象 ( 实质上就是 options ) 与 (vm | componentVM) 进行合并。</p>
<h4 data-id="heading-11">mergeField</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> options = &#123;&#125;
<span class="hljs-keyword">let</span> key
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
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法极其复杂，本质上就是合并了构造函数身上的属性和 options 上的属性。根据 key 的不同判断是返回 options 上的属性抑或以构造函数身上的属性的值为原型创造的新的拥有 options 上的属性的值的对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 比如当 key 为 components 时返回</span>
options = &#123;
  <span class="hljs-attr">components</span>: &#123;
    ChildComponent,
    <span class="hljs-attr">__proto__</span>: &#123;
      <span class="hljs-attr">components</span>: &#123;
        KeepAlive,
        Transition,
        TransitionGroup,
      &#125;,
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">步骤 - 3</h1>
<p>我们可以看到在这段代码中多了一个新的属性 _renderProxy，从字面意义上来看应该称之为<strong>渲染代理对象</strong>，事实上它确实参与了渲染流程，在调用 render 方法获取 vnode 时会将 render 方法的内部指针指向它。<br>
但随之而来产生了两个问题: 1.为什么要有渲染代理对象？2.为什么开发环境和生产环境要用不同的渲染代理对象？<br>
其实并不复杂，我们通过以下代码来进行解答:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
目录: core/instance/render.js
vnode = render.call(vm._renderProxy, vm.$createElement)
*/</span>
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
  h(<span class="hljs-string">'div'</span>, <span class="hljs-string">'hello vue'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过以上代码可以发现，h函数 其实就是 vm.$createElement，但是因为调用的时候是直接使用 <code>h()</code> 来调用的，因此它内部的指针应该指向 window 而不是当前实例，所以我们需要通过 call 的方式将内部指针指向当前实例，如此就可以使用 this 获取到该实例身上 options 中其他的属性了。<br>
那么开发环境和生产环境为什么要用不同的渲染代理对象呢？我们可以发现在开发环境中其实是调用了 initProxy 方法创建的渲染代理对象，其中判断了是否存在 Proxy 对象，通过 Proxy 对象拦截 <code>this.xxx</code> 中的 xxx 是否是一个非法的属性，有利于我们开发时的操作不谨慎。但是生产环境时就没必要了，毕竟我们不会将错误保留到线上。</p>
<h1 data-id="heading-13">步骤 - 4</h1>
<p>这又是一连串的调用，像极了 <strong>core/global-api/index.js</strong> 中的操作，但是请不要忽略入参，<strong>core/global-api/index.js</strong> 中传入的是 Vue，而这里传入的是 vm。这意味着，<strong>core/global-api/index.js</strong> 中是对 Vue构造函数 进行成员的添加，而这里是对 vm 进行属性的添加。<br></p>
<h2 data-id="heading-14">initLifecycle</h2>
<p>初始化一系列属性，如果当前实例是组件则将 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">parent / </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord">/</span></span></span></span></span>root 绑定上组件所归属的 vm。</p>
<pre><code class="hljs language-js copyable" lang="js">vm = &#123;
  <span class="hljs-attr">__proto__</span>: &#123;
    ...Vue,
  &#125;,
  _uid,
  _isVue,
  $options,
  _renderProxy,
  _self,
  <span class="hljs-comment">/* new add start */</span>
  $parent,
  $root,
  <span class="hljs-attr">$children</span>: [],
  <span class="hljs-attr">$refs</span>: &#123;&#125;,
  <span class="hljs-attr">_watcher</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_inactive</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_directInactive</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isMounted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isBeingDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">/* new add end */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">initEvents</h2>
<p>初始化事件中心，如果当前实例是组件则会对父组件的事件监听进行重新绑定。</p>
<pre><code class="hljs language-js copyable" lang="js">vm = &#123;
  <span class="hljs-attr">__proto__</span>: &#123;
    ...Vue,
  &#125;,
  _uid,
  _isVue,
  $options,
  _renderProxy,
  _self,
  $parent,
  $root,
  <span class="hljs-attr">$children</span>: [],
  <span class="hljs-attr">$refs</span>: &#123;&#125;,
  <span class="hljs-attr">_watcher</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_inactive</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_directInactive</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isMounted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isBeingDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">/* new add start */</span>
  <span class="hljs-attr">_events</span>: &#123;&#125;,
  <span class="hljs-attr">_hasHookEvent</span>: &#123;&#125;,
  <span class="hljs-comment">/* new add end */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">initRender</h2>
<p>初始化存放和生成 虚拟DOM 的属性和方法。<br>
如果当前实例不是组件，则将 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">attrs / </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord">/</span></span></span></span></span>listeners 设置为空对象添加到实例上。<br>
如果当前实例是组件，则会将父组件 虚拟DOM 上的 attrs 添加响应式后放到自身实例的 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>属性上；再将父组件的事件监听添加响应式后放到自身实例的</mtext></mrow><annotation encoding="application/x-tex">attrs 属性上；再将父组件的事件监听添加响应式后放到自身实例的 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">属</span><span class="mord cjk_fallback">性</span><span class="mord cjk_fallback">上</span><span class="mord cjk_fallback">；</span><span class="mord cjk_fallback">再</span><span class="mord cjk_fallback">将</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">监</span><span class="mord cjk_fallback">听</span><span class="mord cjk_fallback">添</span><span class="mord cjk_fallback">加</span><span class="mord cjk_fallback">响</span><span class="mord cjk_fallback">应</span><span class="mord cjk_fallback">式</span><span class="mord cjk_fallback">后</span><span class="mord cjk_fallback">放</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">自</span><span class="mord cjk_fallback">身</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">的</span></span></span></span></span>listeners 属性上。</p>
<pre><code class="hljs language-js copyable" lang="js">vm = &#123;
  <span class="hljs-attr">__proto__</span>: &#123;
    ...Vue,
  &#125;,
  _uid,
  _isVue,
  $options,
  _renderProxy,
  _self,
  $parent,
  $root,
  <span class="hljs-attr">$children</span>: [],
  <span class="hljs-attr">$refs</span>: &#123;&#125;,
  <span class="hljs-attr">_watcher</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_inactive</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_directInactive</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isMounted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isBeingDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_events</span>: &#123;&#125;,
  <span class="hljs-attr">_hasHookEvent</span>: &#123;&#125;,
  <span class="hljs-comment">/* new add start */</span>
  <span class="hljs-attr">$vnode</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_vnode</span>: <span class="hljs-literal">null</span>,
  $slots,
  $scopedSlots,
  <span class="hljs-function"><span class="hljs-title">_c</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  $createElement() &#123;&#125;,
  $attrs,
  $listeners,
  <span class="hljs-comment">/* new add end */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">beforeCreate</h2>
<p>调用 beforeCreate 生命周期。</p>
<h2 data-id="heading-18">initInjections</h2>
<p>由于 <strong>步骤 - 2 -> resolveConstructorOptions -> mergeOptions -> normalizeInject</strong> 这一过程中在实例的 $options 中挂载了 inject 这个属性的缘故，这个方法中就不需要再进行添加，只是单纯地为 inject 中的对象添加了响应式。</p>
<pre><code class="hljs language-js copyable" lang="js">vm = &#123;
  <span class="hljs-attr">__proto__</span>: &#123;
    ...Vue,
  &#125;,
  _uid,
  _isVue,
  <span class="hljs-attr">$options</span>: &#123;
    <span class="hljs-comment">/* update start */</span>
    <span class="hljs-attr">inject</span>: &#123;&#125;
    <span class="hljs-comment">/* update end */</span>
  &#125;,
  _renderProxy,
  _self,
  $parent,
  $root,
  <span class="hljs-attr">$children</span>: [],
  <span class="hljs-attr">$refs</span>: &#123;&#125;,
  <span class="hljs-attr">_watcher</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_inactive</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_directInactive</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isMounted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isBeingDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_events</span>: &#123;&#125;,
  <span class="hljs-attr">_hasHookEvent</span>: &#123;&#125;,
  <span class="hljs-attr">$vnode</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_vnode</span>: <span class="hljs-literal">null</span>,
  $slots,
  $scopedSlots,
  <span class="hljs-function"><span class="hljs-title">_c</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  $createElement() &#123;&#125;,
  $attrs,
  $listeners,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">initState</h2>
<p>这一步大家肯定熟，只要在网上看过 Vue 源码解析啊响应式原理啊之类视频的应该都了解，这里就是网传的 Vue 的 constructor 中的内容。<br>
即初始化 props / methods / data / computed / watch。</p>
<pre><code class="hljs language-js copyable" lang="js">vm = &#123;
  <span class="hljs-attr">__proto__</span>: &#123;
    ...Vue,
  &#125;,
  _uid,
  _isVue,
  <span class="hljs-attr">$options</span>: &#123;
    <span class="hljs-attr">inject</span>: &#123;&#125;
  &#125;,
  _renderProxy,
  _self,
  $parent,
  $root,
  <span class="hljs-attr">$children</span>: [],
  <span class="hljs-attr">$refs</span>: &#123;&#125;,
  <span class="hljs-attr">_watcher</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_inactive</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_directInactive</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isMounted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isBeingDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_events</span>: &#123;&#125;,
  <span class="hljs-attr">_hasHookEvent</span>: &#123;&#125;,
  <span class="hljs-attr">$vnode</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_vnode</span>: <span class="hljs-literal">null</span>,
  $slots,
  $scopedSlots,
  <span class="hljs-function"><span class="hljs-title">_c</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  $createElement() &#123;&#125;,
  $attrs,
  $listeners,
  <span class="hljs-comment">/* new add start */</span>
  _watchers,
  _props, <span class="hljs-comment">// 如果 options 上有 props</span>
  ...options.methods, <span class="hljs-comment">// 如果 options 上有 methods</span>
  ...options.data, <span class="hljs-comment">// 如果 options 上有 data</span>
  <span class="hljs-attr">_data</span>: &#123;
    ...options.data
  &#125;, <span class="hljs-comment">// 如果 options 上有 data</span>
  ...options.computed, <span class="hljs-comment">// 如果 options 上有 computed</span>
  <span class="hljs-comment">/* new add end */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">initProvide</h2>
<pre><code class="hljs language-js copyable" lang="js">vm = &#123;
  <span class="hljs-attr">__proto__</span>: &#123;
    ...Vue,
  &#125;,
  _uid,
  _isVue,
  <span class="hljs-attr">$options</span>: &#123;
    <span class="hljs-attr">inject</span>: &#123;&#125;
  &#125;,
  _renderProxy,
  _self,
  $parent,
  $root,
  <span class="hljs-attr">$children</span>: [],
  <span class="hljs-attr">$refs</span>: &#123;&#125;,
  <span class="hljs-attr">_watcher</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_inactive</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_directInactive</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isMounted</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_isBeingDestroyed</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">_events</span>: &#123;&#125;,
  <span class="hljs-attr">_hasHookEvent</span>: &#123;&#125;,
  <span class="hljs-attr">$vnode</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_vnode</span>: <span class="hljs-literal">null</span>,
  $slots,
  $scopedSlots,
  <span class="hljs-function"><span class="hljs-title">_c</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  $createElement() &#123;&#125;,
  $attrs,
  $listeners,
  <span class="hljs-attr">_watchers</span>: [], <span class="hljs-comment">// 如果 options 上有 watch 则会存在 Watcher 的实例</span>
  _props, <span class="hljs-comment">// 如果 options 上有 props</span>
  ...options.methods, <span class="hljs-comment">// 如果 options 上有 methods</span>
  ...options.data, <span class="hljs-comment">// 如果 options 上有 data</span>
  <span class="hljs-attr">_data</span>: &#123;
    ...options.data
  &#125;, <span class="hljs-comment">// 如果 options 上有 data</span>
  ...options.computed, <span class="hljs-comment">// 如果 options 上有 computed</span>
  <span class="hljs-comment">/* new add start */</span>
  _provided, <span class="hljs-comment">// 如果 options 上有 provide</span>
  <span class="hljs-comment">/* new add end */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">created</h2>
<p>调用 created 生命周期。</p>
<h1 data-id="heading-22">步骤 - 5</h1>
<p>到目前为止，我们都只是初始化的工作，大部分都是挂载某某属性，要说真的做了什么业务相关的事情，那大概就是 initState 这部分了，其中为数据添加了响应式，当有计算属性和侦听器时还顺便做了依赖收集。<br>
但是，我们是否还没看到对于 DOM 的处理？对了，这就是为什么在 beforeCreate 和 created 生命周期里无法获取 <code>this.$refs</code> 的原因，我们还没有进入模板编译，那么 DOM 自然就还没有生成，没有生成的东西怎么可能在这些钩子里被获取呢？<br>
自此，_init 就告一段落了，接下来我们即将进入下一个流程 ———— 模板编译 -> ゲットスタート ( get start )。</p></div>  
</div>
            