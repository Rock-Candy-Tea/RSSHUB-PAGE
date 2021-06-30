
---
title: '如何开始阅读VUE源码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d032d26c1114eaf8b1a22c33116478c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 05:20:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d032d26c1114eaf8b1a22c33116478c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>关于vue响应式的文章其实已经挺多了，不过大多都在浅尝辄止，基本就是简单介绍一下<code>Object.defineProperty</code>，覆盖一下<code>setter</code>做个小<code>demo</code>就算解决，好一点的会帮你引入<code>observe、watcher、dep</code>的概念，以及加入对<code>Array</code>的特殊处理，所以本篇除了上述以外，更多的重心将放在<code>setter</code>引发<code>render</code>的机制与流程上，然后结合这个这个响应式机制解析<code>vue</code>中的<code>watch</code>和<code>computed</code>语法实现</p>
<p>文章分为两部分，第一部分会简单介绍vue实例构建流程，第二部分则深入探究响应式实现。</p>
<blockquote>
<p>建议对照源码阅读文章，因为很多本文很多地方会直接指出文件路径，同时将省略部分代码而直述功能</p>
</blockquote>
<p>版本信息：</p>
<ul>
<li>vue: 2.6.12</li>
</ul>
<h2 data-id="heading-1">一、寻找vue</h2>
<blockquote>
<p>直入主题</p>
</blockquote>
<p>真正的<code>vue</code>实例在<code>core/instance/index</code>中可以找到</p>
<pre><code class="copyable">function Vue (options) &#123;
  ....
  this._init(options) // 这个方法在initMixin中定义
&#125;

initMixin(Vue)  // 挂载_init()
stateMixin(Vue)  // 挂载状态处理方法(挂载data,methods等)
eventsMixin(Vue)  // 挂载 事件 的方法($on,$off等)
lifecycleMixin(Vue) // 挂载 生命周期方法(update,destory)
renderMixin(Vue)  // 挂载与渲染有关的方法($nextTick,_render) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个方法可以按照代码逻辑来看，实现对应功能，这里拿<code>initMixin</code>举例</p>
<blockquote>
<p>篇幅有限，所有此处仅解释initMixin逻辑，剩余几个方法大家可以自己探索哦</p>
</blockquote>
<h3 data-id="heading-2">initMixin</h3>
<p><code>initMixin</code>中仅仅挂载了<code>_init()</code>方法，在<code>_init</code>中，初始化了整个<code>vue</code>的状态:</p>
<pre><code class="copyable">function _init(option) &#123;
  ...
  vm._uid = uid++ // 即component id
  ...
  initLifecycle(vm)
  initEvents(vm)
  initRender(vm)
  callHook(vm, 'beforeCreate')
  initInjections(vm) // resolve injections before data/props
  initState(vm)
  initProvide(vm)
  callHook(vm, 'created')
  ...
  if (vm.$options.el) &#123;
    vm.$mount(vm.$options.el) // 开始挂载
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们可以看到几个<code>beforeCreate</code>,<code>created</code>和<code>Mount</code>关键字，大概就能够猜到<code>vu</code>e实例的部分生命周期方法就是在这里进行了挂载，再结合 <a href="https://cn.vuejs.org/v2/guide/instance.html#%E5%AE%9E%E4%BE%8B%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90" target="_blank" rel="nofollow noopener noreferrer">vue官方文档的图示</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d032d26c1114eaf8b1a22c33116478c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于初始化整个<code>vue</code>的状态，可以举例来说，例如<code>initLifecycle</code>中就赋值了<code>parent,children</code>,以及一些<code>isMounted,isDestroy</code>的标识符。<code>initRender</code>中就将<code>attrs,listeners</code>响应化，等等，诸如此类。</p>
<p>从<code>initMixin=>initState=>initData</code>,便可以看到挂载<code>props,methods,data,computed,watch</code>了，</p>
<blockquote>
<p>可以看到，此处先挂载了<code>props,methods</code>,然后是<code>data</code>的顺序，其实再往下探究逻辑就可以知道，如果存在变量重名，优先级是<code>props>methods>data</code>的，这也就解释了为什么初始化的顺序是这样安排的</p>
</blockquote>
<p>在<code>initData</code>中，先是获取了<code>data</code>数据,判断<code>props,methods</code>变量重名问题，然后是走了一个代理，将变量名代理到<code>vue</code>实例上，这样的话你的<code>vue</code>实例中，使用<code>this.x</code>指向就可以访问到<code>this.data.x,</code>这类代理也用在了<code>props</code>和<code>methods</code>中</p>
<blockquote>
<p>在<code>initData</code>获取数据中可以看到一个判断<code>typeof data === 'function' ? getData(data, vm) : data || &#123;&#125;</code>, 支持两种方式获取，实际上如果是自己写这样一个逻辑是会藏有隐患的，如果你的data是直接使用对象，而js的复杂数据类型是地址引用，这意味着，你实例化了两个<code>vue</code>对象，实际上他们的data引用地址是同一个地址，对其中一个<code>vue data</code>的修改会触发另一个vue数据的变动，带来的问题是巨大的</p>
</blockquote>
<pre><code class="copyable">export function proxy (target: Object, sourceKey: string, key: string) &#123;
  sharedPropertyDefinition.get = function proxyGetter () &#123;
    return this[sourceKey][key]
  &#125;
  sharedPropertyDefinition.set = function proxySetter (val) &#123;
    this[sourceKey][key] = val
  &#125;
  Object.defineProperty(target, key, sharedPropertyDefinition)
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个逻辑处理的设计也是非常巧妙，他覆盖了实例中对该key的访问，使用<code>setter</code>和<code>getter</code>将实际访问指向了<code>this.data[key]</code>。</p>
<blockquote>
<p>这里可以说一下computed的逻辑，实际上也是取巧使用了原本用于data的响应式逻辑，其实看到上面贴出来的proxy代码，大概就能猜到，既然proxy能够改变一个变量读取的指向，那么他也能创造一个虚假变量的指向，这个创造出来的这个变量实际上就是computed所使用的变量，将每次computed函数赋给getter，再加上响应式处理，就完全实现了computed，</p>
</blockquote>
<p>走到最后，就是<code>observe(data)</code>,也就是开始处理vue数据的双向绑定</p>
<h2 data-id="heading-3">二、双向绑定</h2>
<p>不同于<code>react</code>的单向数据流，<code>vue</code>使用的双向绑定，单向数据流可以理解为当源头的数据发生变动则触发行为，当然这个变动是主动的，即你需要<code>setState</code>才能触发，而双向绑定则可以抽象为，每一个数据旁边都有一个监护人(一种处理逻辑)，当数据发生变化，这个监护人就会响应行为，这个流程是被动发生的，只要该数据发生变动，就会通过监护人触发行为。</p>
<p>如果你之前有过了解，大概就会知道，js每个数据的变动都是通过<code>Object</code>原型链中的<code>setter</code>去改变值，而如果你在他改变值之前，去通知监护人，就能够实现上述的逻辑，这一点很多博客文章都写的非常清楚了。</p>
<p>接着第一部分的<code>initData</code>知道最后<code>observe(data)</code>，这里开始正式处理响应式。</p>
<h3 data-id="heading-4">2.1 前置条件</h3>
<p>前面一直提到，通过<code>Object</code>的原型链改变对象的默认行为：<code>getter</code>和<code>setter</code>，首先我们需要知道，在<code>js</code>中，读取一个对象的值并不是直接读取，而是通过Object的原型链上的默认行为getter拿到对应的值，而改变这种行为实际上是通过<code>Object.defineProperty</code>,来重新定义一个对象的<code>getter</code>和<code>setter</code>，在<code>/src/core/observer/index.js</code>中我们可以看一个<code>defineReactive</code>方法，他就是<code>vue</code>用来实现这种行为的方法，也是这个响应式的核心</p>
<pre><code class="copyable">function defineReactive(obj, key, val, ... ) &#123;
  // 此处需要保留getter、setter是因为，开发者可能自己基于defineProperty已经做过一层覆盖，
  // 而响应式又会覆盖一次，所以为了保留开发者自己的行为，此处需要兼容原有的getter、setter
  const getter = property && property.get // 拿到默认的getter、setter行为
  const setter = property && property.set
  Object.defineProperty(obj, key, &#123;
    enumerable: true, // 是否可以被枚举出来(例如Object.keys()，for in)
    configurable: true, // 是否可以被配置，是否可以被删除
    get: function() &#123;
      const value = getter ? getter.call(obj) : val
      ...
      return value
    &#125;
    set: function(newVal) &#123;
      ...
      setter.call(obj, newVal)
  &#125; 
  &#125;)
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. 2响应式</h3>
<p>首先，我们猜想一下，双向绑定的行为，数据能够响应行为的变化，而行为又能够操作数据的改变，虽然有部分教程会让你站在数据的角度去理解这种行为，实际上，我们站在行为的角度上去理解是更加方便的。</p>
<p>我们将一种行为定义为一个<code>Watcher</code>，他有可能是一个<code>vue</code>文件的<code>template</code>中的<code>dom</code>节点渲染行为，也有可能是<code>computed</code>的计算值行为，总之，我们从行为的角度出发，一个行为的发生，会伴随着对变量的读取（回想一下我们在<code>vue</code>文件中的<code>template</code>写<code>html</code>标签时，总是会使用<code>&#123;&#123;obj.xxx&#125;&#125;</code>来读取某个变量并渲染），我们想要实现，<strong>变量的改变也会带动这个行为的重新渲染</strong>，是不是我们只需要在首次行为发生的周期内，在读取某个变量时，在这个变量内记录这个<code>Watcher</code>，这样的话，下次变量的改变时，我只要触发我之前记录过的<code>Watcher</code>就行了。所以，我们只需要在一个<code>Watcher</code>发生时，将其挂载到一个公共变量上，这样在读取一个值的时候，记录这个公共变量，就能够实现上述操作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80e208a101b3499381c7a40ad2e0b7ab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里先不解释Dep的作用，可以将其抽象理解为一个被挂载在数据上的数组，每次这个数据被一个watch读取时，就会将这个watch记录下来</p>
</blockquote>
<h4 data-id="heading-6">2.2.1 Watcher</h4>
<p>既然说到将一种行为定义为一个<code>watcher</code>，那么可以在<code>/src/core/observer/watcher.js</code>中看到<code>Watcher</code>的实体类，而我们之前一直所说的“行为”，实际上就是构造器的第二个参数<code>expOrFn</code>，可以有表达式或者函数读取的两种模式</p>
<pre><code class="copyable">class Watcher &#123;
 constructor ( vm: Component, // vue实例
    expOrFn: string | Function, // 行为
    cb: Function, // 为watch服务
    options?: ?Object,
    isRenderWatcher?: boolean // 判断是否为渲染watcher， )
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着来看一种最典型的watcher行为，在<code>/src/core/instance/lifecycle.js</code>中的<code>moundComponent</code>方法中，可以看到一个实例化<code>watcher</code>的方法</p>
<pre><code class="copyable">new Watcher(vm, updateComponent, noop, &#123;
    before () &#123;
      if (vm._isMounted && !vm._isDestroyed) &#123;
        callHook(vm, 'beforeUpdate')
      &#125;
    &#125;
  &#125;, true /* isRenderWatcher */) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，他将<code>updateComponent</code>(可以抽象为渲染行为)传给<code>Watcher</code>，而在<code>Watcher</code>的实例化中，将会执行此方法，当然在执行之前，<code>pushTarget(this)</code>,将这个watcher挂载到公共变量上而后开始执行渲染行为，</p>
<pre><code class="copyable">class Watch &#123;
  constructor(...) &#123;
    ....
    if (typeof expOrFn === 'function') &#123;
      this.getter = expOrFn
    &#125;
    this.get();
  &#125;
  get() &#123;
    pushTarget(this) // 挂载行为至公共Target
    value = this.getter.call(vm, vm) // 开始执行行为，之所以会有返回值是为了computed服务
    popTarget() // 取消挂载，避免下次读取变量时又会绑定此行为
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aadc58256dd46018a9c2708ad8dd9be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，如果此行为读取了某个响应式变量，那么该变量的<code>getter</code>将会存储公共变量<code>target</code>，当行为完成后就会取消行为的挂载，这个时候我们再回过头来看前面的<code>defineReactive</code>的逻辑</p>
<pre><code class="copyable">function defineReactive(obj, key) &#123;
  const dep = new Dep(); // 每个数据都有一个自己的存储列表
  const getter = property && property.get
  const setter = property && property.set
  Object.defineProperty(obj, key, &#123;
    enumerable: true,
    configurable: true,
    get: function reactiveGetter () &#123;
      const value = getter ? getter.call(obj) : val
      if (Dep.target) &#123; // 判断公共变量中是否挂载了行为(watcher)
        dep.depend() // 将行为(watcher)加入dep(即此变量的存储行为列表)
        ...
      &#125;
      return value
    &#125;,
    set: function reactiveSetter(newVal) &#123;
      const value = getter ? getter.call(obj) : val
      if (newVal === value || (newVal !== newVal && value !== value)) &#123;
        return // 判断变量没有变化，则直接返回(后两者判断则是因为NaN!==NaN的特性)
      &#125;
      if (setter) &#123;
        setter.call(obj, newVal) // 开始
      &#125; else &#123;
        val = newVal
      &#125;
      dep.notify() // 通知自己这个数据的存储列表，数据发生改变，需要重新执行行为(watcher)
    &#125;
   &#125;);
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候就很清晰明了了，这就是很多博客文章所说的<strong>依赖收集</strong>，变量在get时通过公共变量<code>Target</code>收集依赖(也就是本文所说的行为),在<code>set</code>时，即变量数据发生改变时，触发更新<code>notify</code>;</p>
<h4 data-id="heading-7">2.2.2 Computed</h4>
<p>前文有大致介绍<code>computed</code>的实现，实际上在介绍完Wacher之后就可以来详细介绍了，计算属性<code>computed</code>并没有实际的变量，他通过原型链覆盖创造了一个变量指向(<code>src/core/instance/state.js</code>的<code>initComputed</code>),回忆一下computed的两种写法</p>
<pre><code class="copyable">'fullName': function() &#123;
  return this.firstName + this.secondeName;
&#125;
'fullName': &#123;
  get: function () &#123;...&#125;,
  set: function() &#123;...&#125;,
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再来看一下<code>initComputed</code></p>
<pre><code class="copyable">function initComputed (vm: Component, computed: Object) &#123;
 const watchers = vm._computedWatchers = Object.create(null)
 for (const key in computed) &#123;
   const userDef = computed[key]
   // 对照着computed的两种写法，就能理解为什么这里有这样的判断，
   const getter = typeof userDef === 'function' ? userDef : userDef.get
   watchers[key] = new Watcher(
    vm,
    getter || noop,
    noop,
    &#123; lazy: true &#125;
  )
   defineComputed(vm, key, userDef) // 通过defineProperty来创造一个挂载在vm上key(fullName)的指向
 &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，他将<code>computed</code>的<code>getter</code>方法，作为<code>Watcher</code>的行为传递了进去，这样在执行<code>getter</code>时，可以将此行为绑定至过程中所读取到的变量(<code>firstName</code>),如此，再下次firstName发生改变时，就会触发此<code>Watcher</code>，重新运行getter方法，得到一个新的<code>fullName</code>的值（还记得前文<code>class Watch</code>中的<code>value = this.getter.call(vm, vm)</code>吗？这个返回值就是<code>computed</code>的返回值），这样就实现了<code>computed</code>的逻辑</p>
<h4 data-id="heading-8">2.2.3 Watch</h4>
<p><code>watch</code>的用法，是监听某个变量，当该变量发生变化时，执行特定的逻辑，</p>
<p>上文提到的两种<code>Watcher</code>行为都是函数行为，但是<code>Watcher</code>的行为是支持函数或者表达式的(<code>expOrFn</code>)，所以此处的<code>exp(expression)</code>这里就是可以提现到的，我们只需要在变量发生变化时，执行<code>watch</code>定义的逻辑即可，</p>
<p>还记得前文代码<code>defineReactive</code>中 <code>set</code>方法通知依赖更新(<code>dep.notify()</code>),虽然前文一直为了方便理解，将Dep描述为一种抽象的列表结构，仅用于依赖收集，但实际上他是一个单独的数据结构，</p>
<pre><code class="copyable">let uid = 0；
class Dep &#123;
  constructor() &#123;
    this.id = uid ++; 
    this.subs = []; // 真正用于收集依赖的数据
  &#125;
  depend () &#123; // 依赖收集
    if (Dep.target) &#123;
      Dep.target.addDep(this)
    &#125;
  &#125;
  addSub (sub: Watcher) &#123;
    this.subs.push(sub)
  &#125;
  notify() &#123; // 变量值发生变化，通知更新
    // 遍历所有收集的依赖，注意触发更新，
    for (let i = 0, l = subs.length; i < l; i++) &#123;
      subs[i].update()
    &#125;
  &#125;
  ...
&#125;
Dep.target = null; // 这就是一直说的，用于挂载Watcher行为的公共变量
function pushTarget(target)&#123; Dep.target = target &#125;;
function popTarget() &#123; Dep.target = null &#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>实际上这里的静态变量<code>target</code>以及<code>pushTarget、popTarget</code>是经过简化的，因为渲染并不是一个单一的行为，他是层层嵌套的行为，所以在绑定响应式时，也是需要区分该变量到底是要绑定至哪个行为(否则每个变量都绑定最顶层的行为，一个变量的变化，将会引发整个页面的<code>update</code>)，因此真正的target是还有一个<code>stack</code>栈结构，用于挂载多个嵌套的行为</p>
</blockquote>
<p>可以看到，每次变量更新，都会触发<code>watcher.update</code>，那么对于<code>watch</code>监听的回调，就可以放到在<code>update</code>中调用</p>
<pre><code class="copyable">class Watch &#123;
  constructor(vm, expOrFn, cb, ...) &#123;
    this.cb = cb // 这个cb就是watch监听的回调
  &#125;
  update() &#123;
    this.run()
  &#125;
  run() &#123;
    ...
    this.cb.call(this.vm, ...)
&#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，关于<code>watch</code>监听的实现逻辑大致就是如此</p>
<blockquote>
<p>关于依赖收集，实际上并不是在get变量时，直接将<code>watcher</code>绑定至<code>Dep</code>中，可以看到<code>Dep.depend()</code>,他先通知行为（<code>watcher</code>），叫他先绑定自己，然后watcher绑定完dep之后，才会回过头，告知<code>Dep</code>要<code>addSub()</code>,这里的逻辑像是一个圈</p>
</blockquote>
<p>所以现在我们回过头来看，前文说了，每个数据都有一个“监护人”，来记录此数据所绑定的行为，那么这个“监护人”到底在哪里呢？ 可以看到<code>/src/core/observer/index.js</code>的<code>class Observer</code>中，</p>
<pre><code class="copyable">class Observer &#123;
  constructor(val) &#123;
    ...
    def(value, '__ob__', this) // 对value定义__ob__属性，挂载此object
    ...
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce112afc6f314723bb8fed8f5bccb785~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"> 对于每一份需要响应式处理的数据，都会挂载一个<code>Observer</code>实例，其内subs就是用于记录绑定此数据的<code>Watcher</code>，同时也可以看到，这份数据的<code>get、set</code>方法已经是被重写过了，也就是前文的<code>defineReactive</code>中的覆盖行为。</p>
<h4 data-id="heading-9">2.2.4 其他</h4>
<p>其实对于<code>Array</code>的响应式是需要特殊处理的，因为他除了<code>set、get</code>之外，还会对数组进行增减操作(<code>splice</code>等)，而这些操作是set无法捕捉的，所以覆盖<code>get、set</code>显然无法实现数组的响应式，而<code>vue</code>中采用的是直接覆盖数组的原型链中会对数据本身改变的方法(<code>push、shift、splice</code>等)，<code>/src/core/observer/array.js</code>整个文件就是对数据的特殊处理 最新的<code>vue3</code>中，使用了<code>ES6</code>的<code>proxy</code>特性来替代这种覆盖<code>set、get</code>实现响应式行为，这种模式同时也能够处理<code>Array</code>。</p>
<h2 data-id="heading-10">三、结尾</h2>
<p><code>vue</code>的源码当然没有如此简单，很多东西文章都没有涉及到，譬如说，通过上面的逻辑其实你可以发现，<code>dep</code>和<code>watcher</code>其实是互相引用的，而<code>js</code>的垃圾回收是检测变量引用的机制，所以如果是简单的复制上文的逻辑，最终的这部分的内存其实是无法被回收的，需要你手动清除，当然<code>vue</code>中也做了这样的处理(每个<code>vm</code>下其实有一个<code>watcherList</code>,用于记录这个示例中所有使用到的<code>watcher</code>，再<code>vm.destroy</code>时，通过遍历<code>watcherList</code>，再销毁每一个<code>watcher</code>，而<code>watcher</code>中又会自己销毁<code>Dep</code>)，但是限于篇幅原因无法详细介绍了。</p>
<h1 data-id="heading-11">最后</h1>
<p>为了帮助大家更好温习重点知识、更高效的准备面试，特别整理了**《95页前端学习笔记》**电子稿文件。</p>
<blockquote>
<p>主要内容包括html，css，html5，css3，JavaScript，正则表达式，函数，BOM，DOM，jQuery，AJAX，vue 等等。</p>
</blockquote>
<h3 data-id="heading-12">👉<a href="https://jq.qq.com/?_wv=1027&k=VIWqVeW1" target="_blank" rel="nofollow noopener noreferrer">点击这里免费获取</a>👈</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2bb2a92a60e43caa0a52561f6037168~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">html5/css3</h3>
<ul>
<li>
<p>HTML5 的优势</p>
</li>
<li>
<p>HTML5 废弃元素</p>
</li>
<li>
<p>HTML5 新增元素</p>
</li>
<li>
<p>HTML5 表单相关元素和属性</p>
</li>
<li>
<p>CSS3 新增选择器</p>
</li>
<li>
<p>CSS3 新增属性</p>
</li>
<li>
<p>新增变形动画属性</p>
</li>
<li>
<p>3D变形属性</p>
</li>
<li>
<p>CSS3 的过渡属性</p>
</li>
<li>
<p>CSS3 的动画属性</p>
</li>
<li>
<p>CSS3 新增多列属性</p>
</li>
<li>
<p>CSS3新增单位</p>
</li>
<li>
<p>弹性盒模型</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cab1446e4224106aaf37b865a85c861~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-14">JavaScript</h3>
<ul>
<li>
<p>JavaScript基础</p>
</li>
<li>
<p>JavaScript数据类型</p>
</li>
<li>
<p>算术运算</p>
</li>
<li>
<p>强制转换</p>
</li>
<li>
<p>赋值运算</p>
</li>
<li>
<p>关系运算</p>
</li>
<li>
<p>逻辑运算</p>
</li>
<li>
<p>三元运算</p>
</li>
<li>
<p>分支循环</p>
</li>
<li>
<p>switch</p>
</li>
<li>
<p>while</p>
</li>
<li>
<p>do-while</p>
</li>
<li>
<p>for</p>
</li>
<li>
<p>break和continue</p>
</li>
<li>
<p>数组</p>
</li>
<li>
<p>数组方法</p>
</li>
<li>
<p>二维数组</p>
</li>
<li>
<p>字符串</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a81487a9a743abaddfc64d1710048c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-15">正则表达式</h3>
<ul>
<li>
<p>创建正则表达式</p>
</li>
<li>
<p>元字符</p>
</li>
<li>
<p>模式修饰符</p>
</li>
<li>
<p>正则方法</p>
</li>
<li>
<p>支持正则的 String方法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a676b628a17044c6826fbf143203e6b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-16">js对象</h3>
<ul>
<li>
<p>定义对象</p>
</li>
<li>
<p>对象的数据访问</p>
</li>
<li>
<p>JSON</p>
</li>
<li>
<p>内置对象</p>
</li>
<li>
<p>Math 方法</p>
</li>
<li>
<p>Date 方法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/067a02c89fa14977852dea5c4a1be32e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-17">面向对象是一种编程思想</h3>
<ul>
<li>定义对象</li>
<li>原型和原型链</li>
<li>原型链</li>
<li>原型</li>
</ul>
<h3 data-id="heading-18">常用的JavaScript设计模式</h3>
<ul>
<li>
<p>单体模式</p>
</li>
<li>
<p>工厂模式</p>
</li>
<li>
<p>例模式</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f765c5eae974e5381d40427c0081f45~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-19">函数</h3>
<ul>
<li>
<p>函数的定义</p>
</li>
<li>
<p>局部变量和全局变量</p>
</li>
<li>
<p>返回值</p>
</li>
<li>
<p>匿名函数</p>
</li>
<li>
<p>自运行函数</p>
</li>
<li>
<p>闭包</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/220c36652e6842abaf876dcde9b06a60~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-20">BOM</h3>
<ul>
<li>
<p>BOM概述</p>
</li>
<li>
<p>window方法</p>
</li>
<li>
<p>frames [ ] 框架集</p>
</li>
<li>
<p>history 历史记录</p>
</li>
<li>
<p>location 定位</p>
</li>
<li>
<p>navigator 导航</p>
</li>
<li>
<p>screen 屏幕</p>
</li>
<li>
<p>document 文档</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e62038814a4ba5a0602e8ea0a2b9b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-21">DOM</h3>
<ul>
<li>DOM对象方法</li>
<li>操作DOM间的关系</li>
<li>DOM节点属性</li>
</ul>
<h3 data-id="heading-22">事件</h3>
<ul>
<li>
<p>事件分类</p>
</li>
<li>
<p>事件对象</p>
</li>
<li>
<p>事件流</p>
</li>
<li>
<p>事件目标</p>
</li>
<li>
<p>事件委派(delegate)</p>
</li>
<li>
<p>事件监听</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d51a6b0da17f4ee1b75ef626d00ee85c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-23">jQuery</h3>
<ul>
<li>
<p>jQuery 选择器</p>
</li>
<li>
<p>属性选择器</p>
</li>
<li>
<p>位置选择器</p>
</li>
<li>
<p>后代选择器</p>
</li>
<li>
<p>子代选择器</p>
</li>
<li>
<p>选择器对象</p>
</li>
<li>
<p>子元素</p>
</li>
<li>
<p>DOM操作</p>
</li>
<li>
<p>JQuery 事件</p>
</li>
<li>
<p>容器适应</p>
</li>
<li>
<p>标签样式操作</p>
</li>
<li>
<p>滑动</p>
</li>
<li>
<p>自定义动画</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9818cba91b24a24aa52d07ff6aa260d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-24">AJAX</h3>
<ul>
<li>工作原理</li>
<li>XMLHttpRequest对象</li>
<li>XML和HTML的区别</li>
<li>get() 和post()</li>
</ul>
<h3 data-id="heading-25">HTTP</h3>
<ul>
<li>
<p>HTTP消息结构</p>
</li>
<li>
<p>url请求过程</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd1a07c160e14a61ae1f7c796a583d47~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-26">性能优化</h3>
<ul>
<li>JavaScript代码优化</li>
<li>提升文件加载速度</li>
</ul>
<h3 data-id="heading-27">webpack</h3>
<ul>
<li>
<p>webpack的特点</p>
</li>
<li>
<p>webpack的缺点</p>
</li>
<li>
<p>安装</p>
</li>
<li>
<p>webpack基本应用</p>
</li>
<li>
<p>配置文件入门</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6144ee2ba6ec403296efce116de2edb2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-28">vue</h3>
<ul>
<li>
<p>MVC模式</p>
</li>
<li>
<p>MVVM模式</p>
</li>
<li>
<p>基础语法</p>
</li>
<li>
<p>实例属性/方法</p>
</li>
<li>
<p>生命周期</p>
</li>
<li>
<p>计算属性</p>
</li>
<li>
<p>数组的更新检查</p>
</li>
<li>
<p>事件对象</p>
</li>
<li>
<p>Vue组件</p>
</li>
<li>
<p>路由使用</p>
</li>
<li>
<p>路由导航</p>
</li>
<li>
<p>嵌套路由</p>
</li>
<li>
<p>命名视图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d294d4b731f41ba8aca134cb4a31157~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-29">👉<a href="https://jq.qq.com/?_wv=1027&k=VIWqVeW1" target="_blank" rel="nofollow noopener noreferrer">点击这里免费获取</a>👈</h3></div>  
</div>
            