
---
title: 'Vue3 源码解析（六）：响应式原理与 reactive'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96baaca981084a4ba6ed4014bd84a26b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 03:32:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96baaca981084a4ba6ed4014bd84a26b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天这篇文章是笔者会带着大家一起深入剖析 Vue3 的响应式原理实现，以及在响应式基础 API 中的 reactive 是如何实现的。对于 Vue 框架来说，其非侵入的响应式系统是最独特的特性之一了，所以不论任何一个版本的 Vue，在熟悉其基础用法后，响应式原理都是笔者最想优先了解的部分，也是阅读源码时必细细研究的部分。毕竟知己知彼百战不殆，当你使用 Vue 时，掌握了响应式原理一定会让你的 coding 过程更加游刃有余的。</p>
<h2 data-id="heading-0">Vue2 的响应式原理</h2>
<p>在开始介绍 Vue3 的响应式原理前，我们先一起回顾一下 Vue2 的响应式原理。</p>
<p>当我们把一个普通选项传入 Vue 实例的 data 选项中，Vue 将遍历此对象所有的 property，并使用 Object.defineProperty 把这些 property 全部转为 getter/setter。而 Vue2 在处理数组时，也会通过原型链劫持会改变数组内元素的方法，并在原型链观察新增的元素，以及派发更新通知。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96baaca981084a4ba6ed4014bd84a26b~tplv-k3u1fbpfcp-zoom-1.image" alt="vue2-observer" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里放上一张 Vue2 文档中介绍响应式的图片。对于文档中有的描述笔者就不再赘述，而从 Vue2 的源码角度来对照图片说一说。在 Vue2 的源码中的 src/core 路径下有一个 observer 模块，它就是 Vue2 中处理响应式的地方了。在这个模块下 observer 负责将对象、数组转换成响应式的，即图中的紫色部分，处理 Data 的 getter 及 setter。当 data 中的选项被访问时，会触发 getter，此时 observer 目录下的 wather.js  模块就会开始工作，它的任务就是收集依赖，我们收集到的依赖是一个个 Dep 类的实例化对象。而 data 中的选项变更时，会触发 setter 的调用，而在 setter 的过程中，触发 dep 的 notify 函数，派发更新事件，由此实现数据的响应监听。</p>
<h2 data-id="heading-1">Vue3 的响应式变化</h2>
<p>在简单回顾了 Vue2 的响应式原理后，我们会有一个疑惑，Vue3 的响应式原理与 Vue2 相比有什么不同呢？</p>
<p>在 Vue3 中响应式系统最大的区别就是，数据模型是被代理的 JavaScript 对象了。不论是我们在组件的 data 选项中返回一个普通的JavaScript 对象，还是使用 composition api 创建一个 reactive 对象，Vue3 都会将该对象包裹在一个带有 get 和 set 处理程序的 Proxy 中。</p>
<p>Proxy 对象用于创建一个对象的代理，从而实现基本操作的拦截和自定义（如属性查找、赋值等）。</p>
<p>其基础语法类似于:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Proxy 相比较于 Object.defineProperty 究竟有什么优势呢？这个问题让我们先从 Object.defineProperty 的弊端说起。</p>
<p>从 Object 的角度来说，由于 Object.defineProperty 是对指定的 key 生成 getter/setter 以进行变化追踪，那么如果这个 key 一开始不存在我们定义的对象上，响应式系统就无能为力了，所以在 Vue2 中无法检测对象的 property 的添加或移除。而对于这个缺陷，Vue2 提供了 <code>vm.$set</code> 和全局的 <code>Vue.set</code> API 让我们能够向对象添加响应式的 property。</p>
<p>从数组的角度来说，当我们直接利用索引设置一个数组项时，或者当我们修改数组长度时，Vue2 的响应式系统都不能监听到变化，解决的方法也如上，使用上面提及的 2 个 api。</p>
<p>而这些问题在 ES6 的新特性 Proxy 面前通通都是不存在的，Proxy 对象能够利用 handler 陷阱在 get、set 时捕获到任何变动，也能监听对数组索引的改动以及 数组 length 的改动。</p>
<p>而依赖收集和派发更新的方式在 Vue3 中也变得不同，在这里我先快速的整体描述一下：在 Vue3 中，通过 track 的处理器函数来收集依赖，通过 trigger 的处理器函数来派发更新，每个依赖的使用都会被包裹到一个副作用（effect）函数中，而派发更新后就会执行副作用函数，这样依赖处的值就被更新了。</p>
<h2 data-id="heading-2">响应式基础 reactive 的实现</h2>
<p>既然这是一个源码分析的文章，咱们还是从源码的角度来分析响应式究竟是如何实现的。所以笔者会先分析响应式基础的 API —— reactive ，相信通过讲解 reactive 的实现，大家会对 Proxy 有更深刻的认识。</p>
<h3 data-id="heading-3">reactive</h3>
<p>二话不说，直接看源码。下面是 reactive API 的函数，函数的参数接受一个对象，通过 <code>createReactiveObject</code> 函数处理后，直接返回一个 proxy 对象。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>>(<span class="hljs-params">target: T</span>): <span class="hljs-title">UnwrapNestedRefs</span><<span class="hljs-title">T</span>>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">target: <span class="hljs-built_in">object</span></span>) </span>&#123;
  // 如果试图去观察一个只读的代理对象，会直接返回只读版本
  <span class="hljs-title">if</span> (<span class="hljs-params">target && (target <span class="hljs-keyword">as</span> Target)[ReactiveFlags.IS_READONLY]</span>) </span>&#123;
    <span class="hljs-keyword">return</span> target
  &#125;
  <span class="hljs-comment">// 创建一个代理对象并返回</span>
  <span class="hljs-keyword">return</span> createReactiveObject(
    target,
    <span class="hljs-literal">false</span>,
    mutableHandlers,
    mutableCollectionHandlers,
    reactiveMap
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在第三行能看到通过判断 target 中是否有 ReactiveFlags 中的 IS_READONLY key 确定对象是否为只读对象。ReactiveFlags 枚举会在源码中不断的与我们见面，所以有必要提前介绍一下 ReactiveFlags：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-built_in">enum</span> ReactiveFlags &#123;
  SKIP = <span class="hljs-string">'__v_skip'</span>, <span class="hljs-comment">// 是否跳过响应式 返回原始对象</span>
  IS_REACTIVE = <span class="hljs-string">'__v_isReactive'</span>, <span class="hljs-comment">// 标记一个响应式对象</span>
  IS_READONLY = <span class="hljs-string">'__v_isReadonly'</span>, <span class="hljs-comment">// 标记一个只读对象</span>
  RAW = <span class="hljs-string">'__v_raw'</span> <span class="hljs-comment">// 标记获取原始值</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ReactiveFlags 枚举中有 4 个枚举值，这四个枚举值的含义都在注释里。对于 ReactiveFlags 的使用是代理对象对 handler 中的 trap 陷阱非常好的应用，对象中并不存在这些 key，而通过 get 访问这些 key 时，返回值都是通过 get 陷阱的函数内处理的。介绍完 ReactiveFlags 后我们继续往下看。</p>
<h3 data-id="heading-4">createReactiveObject</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveObject</span>(<span class="hljs-params">
  target: Target,
  isReadonly: <span class="hljs-built_in">boolean</span>,
  baseHandlers: ProxyHandler<<span class="hljs-built_in">any</span>>,
  collectionHandlers: ProxyHandler<<span class="hljs-built_in">any</span>>,
  proxyMap: <span class="hljs-built_in">WeakMap</span><Target, <span class="hljs-built_in">any</span>>
</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>先看 createReactiveObject 函数的签名，该函数接受 5 个参数:</p>
<ul>
<li>target：目标对象，想要生成响应式的原始对象。</li>
<li>isReadonly：生成的代理对象是否只读。</li>
<li>baseHandlers：生成代理对象的 handler 参数。当 target 类型是 Array 或 Object 时使用该 handler。</li>
<li>collectionHandlers：当 target 类型是 Map、Set、WeakMap、WeakSet 时使用该 handler。</li>
<li>proxyMap：存储生成代理对象后的 Map 对象。</li>
</ul>
<p>这里需要注意的是 baseHandlers 和 collectionHandlers 的区别，这两个参数会根据 target 的类型进行判断，最终选择将哪个参数传入 Proxy 的构造函数，当做 handler 参数使用。</p>
<p>接着我们开始看 createReactiveObject 的逻辑部分：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveObject</span>(<span class="hljs-params">
  target: Target,
  isReadonly: <span class="hljs-built_in">boolean</span>,
  baseHandlers: ProxyHandler<<span class="hljs-built_in">any</span>>,
  collectionHandlers: ProxyHandler<<span class="hljs-built_in">any</span>>,
  proxyMap: <span class="hljs-built_in">WeakMap</span><Target, <span class="hljs-built_in">any</span>>
</span>) </span>&#123;
  <span class="hljs-comment">// 如果目标不是对象，直接返回原始值</span>
  <span class="hljs-keyword">if</span> (!isObject(target)) &#123;
    <span class="hljs-keyword">return</span> target
  &#125;
  <span class="hljs-comment">// 如果目标已经是一个代理，直接返回</span>
  <span class="hljs-comment">// 除非对一个响应式对象执行 readonly</span>
  <span class="hljs-keyword">if</span> (
    target[ReactiveFlags.RAW] &&
    !(isReadonly && target[ReactiveFlags.IS_REACTIVE])
  ) &#123;
    <span class="hljs-keyword">return</span> target
  &#125;
  <span class="hljs-comment">// 目标已经存在对应的代理对象</span>
  <span class="hljs-keyword">const</span> existingProxy = proxyMap.get(target)
  <span class="hljs-keyword">if</span> (existingProxy) &#123;
    <span class="hljs-keyword">return</span> existingProxy
  &#125;
  <span class="hljs-comment">// 只有白名单里的类型才能被创建响应式对象</span>
  <span class="hljs-keyword">const</span> targetType = getTargetType(target)
  <span class="hljs-keyword">if</span> (targetType === TargetType.INVALID) &#123;
    <span class="hljs-keyword">return</span> target
  &#125;
  <span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(
    target,
    targetType === TargetType.COLLECTION ? collectionHandlers : baseHandlers
  )
  proxyMap.set(target, proxy)
  <span class="hljs-keyword">return</span> proxy
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在该函数的逻辑部分，可以看到基础数据类型并不会被转换成代理对象，而是直接返回原始值。</p>
<p>并且会将已经生成的代理对象缓存进传入的 proxyMap，当这个代理对象已存在时不会重复生成，会直接返回已有对象。</p>
<p>也会通过 TargetType 来判断 target 目标对象的类型，Vue3 仅会对 Array、Object、Map、Set、WeakMap、WeakSet 生成代理，其他对象会被标记为 INVALID，并返回原始值。</p>
<p>当目标对象通过类型校验后，会通过 new Proxy() 生成一个代理对象 proxy，handler 参数的传入也是与 targetType 相关，并最终返回已生成的 proxy 对象。</p>
<p>所以回顾 reactive api，我们可能会得到一个代理对象，也可能只是获得传入的 target 目标对象的原始值。</p>
<h3 data-id="heading-5">Handlers 的组成</h3>
<p>在 @vue/reactive 库中有 baseHandlers 和 collectionHandlers 两个模块，分别生成 Proxy 代理的 handlers 中的 trap 陷阱。</p>
<p>例如在上面生成 reactive 的 api 中 baseHandlers 的参数传入了一个 mutableHandlers 对象，这个对象是这样的：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> mutableHandlers: ProxyHandler<<span class="hljs-built_in">object</span>> = &#123;
  get,
  set,
  deleteProperty,
  has,
  ownKeys
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过变量名我们能知道 mutableHandlers 中存在 5 个 trap 陷阱。而在 baseHandlers 中，get 和 set 都是通过工厂函数生成的，以便于适配除 reactive 外的其他 api，例如 readonly、shallowReactive、shallowReadonly 等。</p>
<p>baseHandlers 是处理 Array、Object 的数据类型的，这也是我们绝大部分时间使用 Vue3 时使用的类型，所以笔者接下来着重的讲一下baseHandlers 中的 get 和 set 陷阱。</p>
<h3 data-id="heading-6">get 陷阱</h3>
<p>上一段提到 get 是由一个工厂函数生成的，先来看一下 get 陷阱的种类。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> get = <span class="hljs-comment">/*#__PURE__*/</span> createGetter()
<span class="hljs-keyword">const</span> shallowGet = <span class="hljs-comment">/*#__PURE__*/</span> createGetter(<span class="hljs-literal">false</span>, <span class="hljs-literal">true</span>)
<span class="hljs-keyword">const</span> readonlyGet = <span class="hljs-comment">/*#__PURE__*/</span> createGetter(<span class="hljs-literal">true</span>)
<span class="hljs-keyword">const</span> shallowReadonlyGet = <span class="hljs-comment">/*#__PURE__*/</span> createGetter(<span class="hljs-literal">true</span>, <span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>get 陷阱有 4 个类型，分别对应不同的响应式 API，从名称中就可以知道对应的 API 名称，非常一目了然。而所有的 get 都是由 createGetter 函数生成的。所以接下来我们着重看一下 createGetter 的逻辑。</p>
<p>还是老规矩，先从函数签名看起。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createGetter</span>(<span class="hljs-params">isReadonly = <span class="hljs-literal">false</span>, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params">target: Target, key: <span class="hljs-built_in">string</span> | symbol, receiver: <span class="hljs-built_in">object</span></span>) </span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>createGetter 有 isReadonly 和 shallow 两个参数，让使用 get 陷阱的 api 按需使用。而函数的内部返回了一个 get 函数，使用高阶函数的方式返回将会传入 handlers 中 get 参数的函数。</p>
<p>接着看 createGetter 的逻辑：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 如果 get 访问的 key 是 '__v_isReactive'，返回 createGetter 的 isReadonly 参数取反结果</span>
<span class="hljs-keyword">if</span> (key === ReactiveFlags.IS_REACTIVE) &#123;
  <span class="hljs-keyword">return</span> !isReadonly
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === ReactiveFlags.IS_READONLY) &#123;
  <span class="hljs-comment">// 如果 get 访问的 key 是 '__v_isReadonly'，返回 createGetter 的 isReadonly 参数</span>
  <span class="hljs-keyword">return</span> isReadonly
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
  <span class="hljs-comment">// 如果 get 访问的 key 是 '__v_raw'，并且 receiver 与原始标识相等，则返回原始值</span>
  key === ReactiveFlags.RAW &&
  receiver ===
    (isReadonly
      ? shallow
        ? shallowReadonlyMap
        : readonlyMap
      : shallow
        ? shallowReactiveMap
        : reactiveMap
    ).get(target)
) &#123;
  <span class="hljs-keyword">return</span> target
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这段 createGetter 逻辑中，笔者专门介绍过的 ReactiveFlags 枚举在这就取得了妙用。其实目标对象中并没有这些 key，但是在 get 中Vue3 就对这些 key 做了特殊处理，当我们在对象上访问这几个特殊的枚举值时，就会返回特定意义的结果。而可以关注一下 ReactiveFlags.IS_REACTIVE 这个 key 的判断方式，为什么是只读标识的取反呢？因为当一个对象的访问能触发这个 get 陷阱时，说明这个对象必然已经是一个 Proxy 对象了，所以只要不是只读的，那么就可以认为是响应式对象了。</p>
<p>接着看 get 的后续逻辑。</p>
<p>继续判断 target 是否是一个数组，如果代理对象不是只读的，并且 target 是一个数组，并且访问的 key 在数组需要特殊处理的方法里，就会直接调用特殊处理的数组函数执行结果，并返回。</p>
<p>arrayInstrumentations 是一个对象，对象内保存了若干个被特殊处理的数组方法，并以键值对的形式存储。</p>
<p>我们之前说过 Vue2 以原型链的方式劫持了数组，而在这里也有类似地作用，而数组的部分我们准备放在后续的文章中再介绍，下面是需要特殊处理的数组。</p>
<ul>
<li>对索引敏感的数组方法
<ul>
<li>includes、indexOf、lastIndexOf</li>
</ul>
</li>
<li>会改变自身长度的数组方法，需要避免 length 被依赖收集，因为这样可能会造成循环引用
<ul>
<li>push、pop、shift、unshift、splice</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 判断 taeget 是否是数组</span>
<span class="hljs-keyword">const</span> targetIsArray = isArray(target)
<span class="hljs-comment">// 如果不是只读对象，并且目标对象是个数组，访问的 key 又在数组需要劫持的方法里，直接调用修改后的数组方法执行</span>
<span class="hljs-keyword">if</span> (!isReadonly && targetIsArray && hasOwn(arrayInstrumentations, key)) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(arrayInstrumentations, key, receiver)
&#125;

<span class="hljs-comment">// 获取 Reflect 执行的 get 默认结果</span>
<span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver)

<span class="hljs-comment">// 如果是 key 是 Symbol，并且 key 是 Symbol 对象中的 Symbol 类型的 key</span>
<span class="hljs-comment">// 或者 key 是不需要追踪的 key: __proto__,__v_isRef,__isVue</span>
<span class="hljs-comment">// 直接返回 get 结果</span>
<span class="hljs-keyword">if</span> (isSymbol(key) ? builtInSymbols.has(key) : isNonTrackableKeys(key)) &#123;
  <span class="hljs-keyword">return</span> res
&#125;

<span class="hljs-comment">// 不是只读对象，执行 track 收集依赖</span>
<span class="hljs-keyword">if</span> (!isReadonly) &#123;
  track(target, TrackOpTypes.GET, key)
&#125;

<span class="hljs-comment">// 如果是 shallow 浅层响应式，直接返回 get 结果</span>
<span class="hljs-keyword">if</span> (shallow) &#123;
  <span class="hljs-keyword">return</span> res
&#125;

<span class="hljs-keyword">if</span> (isRef(res)) &#123;
  <span class="hljs-comment">// 如果是 ref ，则返回解包后的值 - 当 target 是数组，key 是 int 类型时，不需要解包</span>
  <span class="hljs-keyword">const</span> shouldUnwrap = !targetIsArray || !isIntegerKey(key)
  <span class="hljs-keyword">return</span> shouldUnwrap ? res.value : res
&#125;

<span class="hljs-keyword">if</span> (isObject(res)) &#123;
  <span class="hljs-comment">// 将返回的值也转换成代理，我们在这里做 isObject 的检查以避免无效值警告。</span>
  <span class="hljs-comment">// 也需要在这里惰性访问只读和星影视对象，以避免循环依赖。</span>
  <span class="hljs-keyword">return</span> isReadonly ? <span class="hljs-keyword">readonly</span>(res) : reactive(res)
&#125;

<span class="hljs-comment">// 不是 object 类型则直接返回 get 结果</span>
<span class="hljs-keyword">return</span> res
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在处理完数组后，我们对 target 执行 Reflect.get 方法，获得默认行为的 get 返回值。</p>
<p>之后判断 当前 key 是否是 Symbol，或者是否是不需要追踪的 key，如果是的话直接返回 get 的结果 res。</p>
<p>下面👇几个 key 是不需要被依赖收集或者返回响应式结果的。</p>
<ul>
<li><code>__proto__</code></li>
<li><code>_v_isRef</code></li>
<li><code>__isVue</code></li>
</ul>
<p>接着判断当前代理对象是否是只读对象，如果不是只读的话，则运行笔者上文提及的 tarck 处理器函数收集依赖。</p>
<p>如果是 shallow 的浅层响应式，则不需要将内部的属性转换成代理，直接返回 res。</p>
<p>如果 res 是一个 Ref 类型的对象，就会自动解包返回，这里就能解释官方文档中提及的 ref 在 reactive 中会自动解包的特性了。而需要注意的是，当 target 是一个数组类型，并且 key 是 int 类型时，即使用索引访问数组元素时，不会被自动解包。</p>
<p>如果 res 是一个对象，就会将该对象转成响应式的 Proxy 代理对象返回，再结合我们之前分析的缓存已生成的 proxy 对象，可以知道这里的逻辑并不会重复生成相同的 res，也可以理解文档中提及的当我们访问 reactive 对象中的 key 是一个对象时，它也会自动的转换成响应式对象，而且由于在此处生成 reactive 或者 readonly 对象是一个延迟行为，不需要在第一时间就遍历 reactive 传入的对象中的所有 key，也对性能的提升是一个帮助。</p>
<p>当 res 都不满足上述条件时，直接返回 res 结果。例如基础数据类型就会直接返回结果，而不做特殊处理。</p>
<p>至此，get 陷阱的逻辑全部结束了。</p>
<h3 data-id="heading-7">set 陷阱</h3>
<p>与 createGetter 对应，set 也有一个 createSetter 的工厂函数，也是通过柯里化的方式返回一个 set 函数。</p>
<p>函数签名都大同小异，那么接下来笔者直接带大家盘逻辑。</p>
<p>set 的函数比较简短，所以这次一次性把写好注释的代码放上来，先看代码再讲逻辑。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSetter</span>(<span class="hljs-params">shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">
    target: <span class="hljs-built_in">object</span>,
    key: <span class="hljs-built_in">string</span> | symbol,
    value: unknown,
    receiver: <span class="hljs-built_in">object</span>
  </span>): <span class="hljs-title">boolean</span> </span>&#123;
    <span class="hljs-keyword">let</span> oldValue = (target <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>)[key]
    <span class="hljs-keyword">if</span> (!shallow) &#123;
      value = toRaw(value)
      oldValue = toRaw(oldValue)
      <span class="hljs-comment">// 当不是 shallow 模式时，判断旧值是否是 Ref，如果是则直接更新旧值的 value</span>
      <span class="hljs-comment">// 因为 ref 有自己的 setter</span>
      <span class="hljs-keyword">if</span> (!isArray(target) && isRef(oldValue) && !isRef(value)) &#123;
        oldValue.value = value
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// shallow 模式不需要特殊处理，对象按原样 set</span>
    &#125;

    <span class="hljs-comment">// 判断 target 中是否存在 key</span>
    <span class="hljs-keyword">const</span> hadKey =
      isArray(target) && isIntegerKey(key)
        ? <span class="hljs-built_in">Number</span>(key) < target.length
        : hasOwn(target, key)
    <span class="hljs-comment">// Reflect.set 获取默认行为的返回值</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver)
    <span class="hljs-comment">// 如果目标是原始对象原型链上的属性，则不会触发 trigger 派发更新</span>
    <span class="hljs-keyword">if</span> (target === toRaw(receiver)) &#123;
      <span class="hljs-comment">// 使用 trigger 派发更新，根据 hadKey 区别调用事件</span>
      <span class="hljs-keyword">if</span> (!hadKey) &#123;
        trigger(target, TriggerOpTypes.ADD, key, value)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasChanged(value, oldValue)) &#123;
        trigger(target, TriggerOpTypes.SET, key, value, oldValue)
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> result
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 set 的过程中会首先获取新旧与旧值，当目前的代理对象不是浅层比较时，会判断旧值是否是一个 Ref，如果旧值不是数组且是一个 ref类型的对象，并且新值不是 ref 对象时，会直接修改旧值的 value。</p>
<p>看到这里可能会有疑问，为什么要更新旧值的 value？如果你使用过 ref 这个 api 就会知道，每个 ref 对象的值都是放在 value 里的，而 ref 与 reactive 的实现是有区别的，ref 其实是一个 class 实例，它的 value 有自己的 set ，所以就不会在这里继续进行 set 了。ref 的部分在后续的文章中会详细讲解。</p>
<p>在处理完 ref 类型的值后，会声明一个变量 hadKey，判断当前要 set 的 key 是否是对象中已有的属性。</p>
<p>接下来调用 Reflect.set 获取默认行为的 set 返回值 result。</p>
<p>然后会开始派发更新的过程，在派发更新前，需要保证 target 和原始的 receiver 相等，target 不能是一个原型链上的属性。</p>
<p>之后开始使用 trigger 处理器函数派发更新，如果 hadKey 不存在，则是一个新增属性，通过 TriggerOpTypes.ADD 枚举来标记。这里可以看到开篇分析 Proxy 强于 Object.defineProperty 的地方，会监测到任何一个新增的 key，让响应式系统更强大。</p>
<p>如果 key 是当前 target 上已经存在的属性，则比较一下新旧值，如果新旧值不一样，则代表属性被更新，通过 TriggerOpTypes.SET 来标记派发更新。</p>
<p>在更新派发完后，返回 set 的结果 result，至此 set 结束。</p>
<h2 data-id="heading-8">总结</h2>
<p>在今天的文章中，笔者先带大家回顾了 Vue2 的响应式原理，又开始介绍 Vue3 的响应式原理，通过比较 Vue2 和 Vue3 的响应式系统的区别引出 Vue3 响应式系统的提升之处，尤其是其中最主要的调整将 Object.defineProperty 替换为 Proxy 代理对象。</p>
<p>为了让大家属性 Proxy 对响应式系统的影响，笔者着重介绍了响应式基础 API：reactive。分析了 reactive 的实现，以及 reactive api 返回的 proxy 代理对象使用的 handlers 陷阱。并且对陷阱中我们最常用的 get 和 set 的源码进行分析，相信大家在看完本篇文章以后，对 proxy 这个 ES2015 的新特性的使用又有了新的理解。</p>
<p>本文只是介绍 Vue3 响应式系统的第一篇文章，所以 track 收集依赖，trigger 派发更新的过程没有详细展开，在后续的文章中计划详细讲解副作用函数 effect，以及 track 和 trigger 的过程，如果希望能详细了解响应式系统的源码，麻烦大家点个关注免得迷路。</p>
<p>最后，如果这篇文章能够帮助到你了解 Vue3 中的响应式原理和 reactive 的实现，希望能给本文点一个喜欢❤️。如果想继续追踪后续文章，也可以关注我的账号或 follow 我的 <a href="https://github.com/originalix" target="_blank" rel="nofollow noopener noreferrer">github</a>，再次谢谢各位可爱的看官老爷。</p></div>  
</div>
            