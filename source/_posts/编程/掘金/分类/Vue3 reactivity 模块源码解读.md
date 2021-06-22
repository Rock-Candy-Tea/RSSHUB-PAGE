
---
title: 'Vue3 reactivity 模块源码解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48a33976ede64718963a59b7e76f5949~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 03:39:52 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48a33976ede64718963a59b7e76f5949~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">阅读源码带来的收获。</h2>
<ul>
<li>（1）ES6 的 <code>Proxy、Reflect</code> 组合语义化语法；</li>
<li>（2）<code>TypeScript</code> 的深度用法；</li>
<li>（3）<code>Vue3</code> 响应式原理；</li>
<li>（4）依赖收集和触发过程；</li>
<li>（5）Vue3 的 <code>reactivity</code> 模块的常用 API 实现。</li>
</ul>
<h3 data-id="heading-1">阅读前所需要掌握的知识点。</h3>
<ul>
<li>
<p>了解 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy" target="_blank" rel="nofollow noopener noreferrer">ES6 Proxy API</a></p>
</li>
<li>
<p>了解 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect" target="_blank" rel="nofollow noopener noreferrer">ES6 Reflect API</a></p>
</li>
<li>
<p>了解 <code>TypeScript</code> 的使用 <a href="https://www.tslang.cn/docs/handbook/basic-types.html" target="_blank" rel="nofollow noopener noreferrer">Typescript tslang</a></p>
</li>
<li>
<p>对于Vue2.x时候的 <code>Object.defineProperty</code> 响应式处理来说，<code>Proxy</code> 具备了更加强大的能力，<code>新增、删除、迭代</code>操作也能够监听到，而无需多余API进行新增、删除。</p>
</li>
<li>
<p>而使用了 <code>TypeScript</code> 重构了整个项目，配合 <code>monorepo</code> 实现了模块的划分，其中响应式相关的原理都存放到了 <code>reactivity</code> 模块中。</p>
</li>
</ul>
<h2 data-id="heading-2">1. reactivity 入口</h2>
<ul>
<li><a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/index.ts" target="_blank" rel="nofollow noopener noreferrer">源码地址入口</a></li>
</ul>
<h3 data-id="heading-3">reactivity 入口部分可以说只是做出了相关的导出操作</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> &#123; ref, toRefs <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./ref"</span>;
<span class="hljs-keyword">export</span> &#123; reactive, readonly <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./reactive"</span>;
<span class="hljs-keyword">export</span> &#123; computed <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./computed"</span>;
<span class="hljs-keyword">export</span> &#123; effect, stop, trigger, track <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./effect"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>核心部分在上面导出的几个 API。</p>
</li>
<li>
<p>我们可以通过 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/reactive.ts" target="_blank" rel="nofollow noopener noreferrer">reactive</a> 去开始解读源码，从中展开到个个 API 实现。</p>
</li>
</ul>
<h3 data-id="heading-4">1.1 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/reactive.ts#L87" target="_blank" rel="nofollow noopener noreferrer">reactive.ts 解读</a></h3>
<ul>
<li>（1）首先使用了 <code>TypeScript</code> 的函数重载，对类型进行的声明；</li>
<li>（2）然后通过判断有没有 <code>ReactiveFlags.IS_READONLY</code> 来调用 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/reactive.ts#L173" target="_blank" rel="nofollow noopener noreferrer"><code>function createReactiveObject</code></a> 创建 reactive 对象；</li>
<li>（3）通过判断是否可以被代理、是否有缓存、是否可以被代理进行处理；</li>
<li>（4）是否被代理的核心是调用 <code>Object.prototype.toString.call</code> 验证类型；</li>
<li>（5）最后进行代理，缓存后返回被代理的对象。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; mutableHandlers <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./baseHandlers"</span>;
<span class="hljs-keyword">import</span> &#123; mutableCollectionHandlers <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./collectionHandlers"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> reactiveMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span><Target, <span class="hljs-built_in">any</span>>();

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>>(<span class="hljs-params">target: T</span>): <span class="hljs-title">UnwrapNestedRefs</span><<span class="hljs-title">T</span>></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">target: <span class="hljs-built_in">object</span></span>) </span>&#123;
  <span class="hljs-comment">// if trying to observe a readonly proxy, return the readonly version.</span>
  <span class="hljs-keyword">if</span> (target && (target <span class="hljs-keyword">as</span> Target)[ReactiveFlags.IS_READONLY]) &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
  <span class="hljs-keyword">return</span> createReactiveObject(
    target, <span class="hljs-comment">// 响应式的目标对象</span>
    <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否只读</span>
    mutableHandlers, <span class="hljs-comment">// reactive基本对象的代理处理</span>
    mutableCollectionHandlers, <span class="hljs-comment">// Map、Set等对象的代理</span>
    reactiveMap <span class="hljs-comment">// 缓存Map</span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; isObject, toRawType <span class="hljs-comment">/* ... */</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>;
<span class="hljs-comment">// 拿到对象（WeakMap、Map、WeakSet、Set、Object、Array）的Type</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTargetType</span>(<span class="hljs-params">value: Target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> value[ReactiveFlags.SKIP] || !<span class="hljs-built_in">Object</span>.isExtensible(value)
    ? TargetType.INVALID
    : targetTypeMap(toRawType(value));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveObject</span>(<span class="hljs-params">
  target: Target, <span class="hljs-comment">// 创建响应式的目标对象（可以是数组、对象、Map、Set...）</span>
  isReadonly: <span class="hljs-built_in">boolean</span>, <span class="hljs-comment">// 是否是只读模式</span>
  baseHandlers: ProxyHandler<<span class="hljs-built_in">any</span>>, <span class="hljs-comment">// 基本的Proxy代理函数</span>
  collectionHandlers: ProxyHandler<<span class="hljs-built_in">any</span>>, <span class="hljs-comment">// Map、Set等的Proxy代理函数</span>
  proxyMap: <span class="hljs-built_in">WeakMap</span><Target, <span class="hljs-built_in">any</span>> <span class="hljs-comment">// 代理的proxy缓存Map</span>
</span>) </span>&#123;
  <span class="hljs-comment">// 非object情况直接返回</span>
  <span class="hljs-keyword">if</span> (!isObject(target)) &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
  <span class="hljs-comment">// 目标对象上存在 ReactiveFlags.RAW （调用过reactive/readonly函数）</span>
  <span class="hljs-keyword">if</span> (
    target[ReactiveFlags.RAW] &&
    !(isReadonly && target[ReactiveFlags.IS_REACTIVE])
  ) &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
  <span class="hljs-comment">// 目标对象被代理过存在缓存中</span>
  <span class="hljs-keyword">const</span> existingProxy = proxyMap.get(target);
  <span class="hljs-keyword">if</span> (existingProxy) &#123;
    <span class="hljs-keyword">return</span> existingProxy;
  &#125;
  <span class="hljs-comment">// 获取类型，判断是否可以被代理</span>
  <span class="hljs-keyword">const</span> targetType = getTargetType(target);
  <span class="hljs-keyword">if</span> (targetType === TargetType.INVALID) &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
  <span class="hljs-comment">// 通过拿到的类型验证是否是COLLECTION（Map、Set...）还是基本的类型（Object、Array）</span>
  <span class="hljs-keyword">const</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(
    target,
    targetType === TargetType.COLLECTION ? collectionHandlers : baseHandlers
  );
  <span class="hljs-comment">// 设置缓存并导出代理后的对象</span>
  proxyMap.set(target, proxy);
  <span class="hljs-keyword">return</span> proxy;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>reactive.ts</code> 其他 <code>readonly、shallowReactive、shallowReadonly</code> 也是类型的调用方式，在<code>createReactiveObject</code>的时候传递对应的处理对象、缓存 Map。</p>
</li>
<li>
<p>而 <code>isReadonly、isReactive</code> 是巧妙的验证对象上面添加的 <code>ReactiveFlags</code> 里面枚举的类型。</p>
</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ReactiveFlags 是一个 TypeScript 的枚举类型</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-built_in">enum</span> ReactiveFlags &#123;
  SKIP = <span class="hljs-string">"__v_skip"</span>,
  IS_REACTIVE = <span class="hljs-string">"__v_isReactive"</span>,
  IS_READONLY = <span class="hljs-string">"__v_isReadonly"</span>,
  RAW = <span class="hljs-string">"__v_raw"</span>,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isReactive</span>(<span class="hljs-params">value: unknown</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">if</span> (isReadonly(value)) &#123;
    <span class="hljs-keyword">return</span> isReactive((value <span class="hljs-keyword">as</span> Target)[ReactiveFlags.RAW]);
  &#125;
  <span class="hljs-keyword">return</span> !!(value && (value <span class="hljs-keyword">as</span> Target)[ReactiveFlags.IS_REACTIVE]);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isReadonly</span>(<span class="hljs-params">value: unknown</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> !!(value && (value <span class="hljs-keyword">as</span> Target)[ReactiveFlags.IS_READONLY]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>reactive() 小总结：</p>
<ul>
<li>在 <code>reactive.ts</code> 中主要是进行了验证、缓存的操作，处理了<code>重复代理的问题、空间换时间</code>的方式进行优化。</li>
<li>Proxy 的代理核心在<code>baseHandlers.ts</code> 和 <code>collectionHandlers.ts</code>导出引用；</li>
<li>调用了 <code>@vue/shared</code> 模块导出的 <code>isObject、toRawType</code> 等共享方法，这个模块的<code>常用utils可以运用到我们实际项目开发</code>当中；</li>
</ul>
</li>
<li>
<p>接下来就是我们的 Proxy 代理核心 <code>baseHandlers.ts</code>。</p>
</li>
</ul>
<h3 data-id="heading-5">1.2 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/baseHandlers.ts" target="_blank" rel="nofollow noopener noreferrer">baseHandlers.ts 解读</a></h3>
<ul>
<li><code>reactive</code>调用 <code>createReactiveObject</code> 的时候传递了<a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/baseHandlers.ts#L197" target="_blank" rel="nofollow noopener noreferrer"><code>mutableHandlers</code></a></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> mutableHandlers: ProxyHandler<<span class="hljs-built_in">object</span>> = &#123;
  get,
  set,
  deleteProperty,
  has,
  ownKeys,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代理了以上五个操作、对增删改查、验证、枚举操作进行处理</li>
</ul>
<h4 data-id="heading-6">1.2.1 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/baseHandlers.ts#L77" target="_blank" rel="nofollow noopener noreferrer">get 函数</a></h4>
<ul>
<li>（1）<code>createGetter</code> 通过判断，对自身定义的属性进行处理返回、对<code>数组原型</code>函数<code>push、pop</code>等进行处理；</li>
<li>（2）处理以上操作之后，通过 key 调用<code>Reflect.get</code> 拿到结果；</li>
<li>（3）<code>ref</code> 情况进行自动解构，直接返回数据源；</li>
<li>（4）后面还验证是否需要进行依赖收集、是否要对返回的对象数据进行深层代理。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123;
  isObject,
  hasOwn,
  isSymbol,
  <span class="hljs-comment">/* ... */</span>
  isArray,
  isIntegerKey,
  <span class="hljs-comment">/* ... */</span>
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/shared"</span>;
<span class="hljs-comment">// 执行高阶函数 createGetter 拿到对应的get函数</span>
<span class="hljs-keyword">const</span> get = <span class="hljs-comment">/*#__PURE__*/</span> createGetter();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createGetter</span>(<span class="hljs-params">isReadonly = <span class="hljs-literal">false</span>, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-comment">// target（被代理的对象）、key、receiver（代理后的对象）</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params">target: Target, key: <span class="hljs-built_in">string</span> | symbol, receiver: <span class="hljs-built_in">object</span></span>) </span>&#123;
    <span class="hljs-comment">// key 为 vue内部注入的ReactiveFlags，返回相关的true/false</span>
    <span class="hljs-keyword">if</span> (key === ReactiveFlags.IS_REACTIVE) &#123;
      <span class="hljs-keyword">return</span> !isReadonly;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === ReactiveFlags.IS_READONLY) &#123;
      <span class="hljs-keyword">return</span> isReadonly;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
      <span class="hljs-comment">// 响应式情况， 通过ReactiveFlags.RAW获取数据，直接返回目标对象</span>
      <span class="hljs-comment">// 这个操作在toRaw函数、isReactive都有体现</span>
      key === ReactiveFlags.RAW &&
      receiver === <span class="hljs-comment">// 并且代理对象是否被缓存过</span>
        (isReadonly
          ? shallow
            ? shallowReadonlyMap
            : readonlyMap
          : shallow
          ? shallowReactiveMap
          : reactiveMap
        ).get(target)
    ) &#123;
      <span class="hljs-keyword">return</span> target;
    &#125;
    <span class="hljs-keyword">const</span> targetIsArray = isArray(target);
    <span class="hljs-comment">// 非只读 & 数组 & 属于重写的['push', 'pop', 'shift', 'unshift', 'splice'] | ['includes', 'indexOf', 'lastIndexOf']</span>
    <span class="hljs-keyword">if</span> (!isReadonly && targetIsArray && hasOwn(arrayInstrumentations, key)) &#123;
      <span class="hljs-comment">// 直接拿相关的函数</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(arrayInstrumentations, key, receiver);
    &#125;
    <span class="hljs-comment">// 获取数据</span>
    <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);
    <span class="hljs-comment">// 验证是否存在相关不需要 Track 依赖收集</span>
    <span class="hljs-keyword">if</span> (isSymbol(key) ? builtInSymbols.has(key) : isNonTrackableKeys(key)) &#123;
      <span class="hljs-keyword">return</span> res;
    &#125;

    <span class="hljs-keyword">if</span> (!isReadonly) &#123;
      <span class="hljs-comment">// 非只读状态下收集依赖</span>
      track(target, TrackOpTypes.GET, key);
    &#125;
    <span class="hljs-comment">// 浅代理情况直接返回</span>
    <span class="hljs-keyword">if</span> (shallow) &#123;
      <span class="hljs-keyword">return</span> res;
    &#125;
    <span class="hljs-comment">// 对属于ref情况，判断是否存在 __v_isRef & 非数组 或非数值key，直接解构拿到.value</span>
    <span class="hljs-keyword">if</span> (isRef(res)) &#123;
      <span class="hljs-comment">// ref unwrapping - does not apply for Array + integer key.</span>
      <span class="hljs-keyword">const</span> shouldUnwrap = !targetIsArray || !isIntegerKey(key);
      <span class="hljs-keyword">return</span> shouldUnwrap ? res.value : res;
    &#125;
    <span class="hljs-comment">// 如果获取的数据是对象，进行深层次只读/代理</span>
    <span class="hljs-keyword">if</span> (isObject(res)) &#123;
      <span class="hljs-comment">// Convert returned value into a proxy as well. we do the isObject check</span>
      <span class="hljs-comment">// here to avoid invalid value warning. Also need to lazy access readonly</span>
      <span class="hljs-comment">// and reactive here to avoid circular dependency.</span>
      <span class="hljs-keyword">return</span> isReadonly ? <span class="hljs-keyword">readonly</span>(res) : reactive(res);
    &#125;

    <span class="hljs-keyword">return</span> res;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">1.2.2 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/baseHandlers.ts#L138" target="_blank" rel="nofollow noopener noreferrer">set 函数</a></h4>
<ul>
<li>（1）<code>createSetter</code> 对 <code>oldValue是ref、newValue是非ref</code> 情况进行自动赋值处理，简化了 reactive 里面嵌套 ref 情况的赋值操作（前面在获取的时候进行了解构）；</li>
<li>（2）设置 newValue 之前，进行判断 <code>key</code> 是否存在，进行对应的触发<code>TriggerOpTypes</code>进行标明，在没有变化情况下不做处理。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 一样通过createSetter创建set函数</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-comment">/*#__PURE__*/</span> createSetter();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSetter</span>(<span class="hljs-params">shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-comment">// target（被代理的对象）、key、value、receiver（代理后的对象）</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">
    target: <span class="hljs-built_in">object</span>,
    key: <span class="hljs-built_in">string</span> | symbol,
    value: unknown,
    receiver: <span class="hljs-built_in">object</span>
  </span>): <span class="hljs-title">boolean</span> </span>&#123;
    <span class="hljs-comment">// 拿到修改/添加之前的值</span>
    <span class="hljs-keyword">let</span> oldValue = (target <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>)[key];
    <span class="hljs-keyword">if</span> (!shallow) &#123;
      <span class="hljs-comment">// 拿到源值（toRaw这样处理是为了防止获取的值是一个Proxy，进行解构拿到被代理前的对象）</span>
      value = toRaw(value);
      oldValue = toRaw(oldValue);
      <span class="hljs-comment">// 属于老值是ref、新值非ref，直接赋值（get情况进行解构，set的时候进行自动赋值到ref的value上）</span>
      <span class="hljs-keyword">if</span> (!isArray(target) && isRef(oldValue) && !isRef(value)) &#123;
        oldValue.value = value;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// in shallow mode, objects are set as-is regardless of reactive or not</span>
    &#125;
    <span class="hljs-keyword">const</span> hadKey =
      isArray(target) && isIntegerKey(key)
        ? <span class="hljs-built_in">Number</span>(key) < target.length
        : hasOwn(target, key);
    <span class="hljs-comment">// 进行设置新的value</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver);
    <span class="hljs-comment">// don't trigger if target is something up in the prototype chain of original</span>
    <span class="hljs-keyword">if</span> (target === toRaw(receiver)) &#123;
      <span class="hljs-comment">// 设置之前没有这个key，就是添加操作，否则是修改操作（触发对应的trigger，就是触发收集的依赖）</span>
      <span class="hljs-keyword">if</span> (!hadKey) &#123;
        trigger(target, TriggerOpTypes.ADD, key, value);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasChanged(value, oldValue)) &#123;
        <span class="hljs-comment">// 判断有无变化（相同情况不触发依赖）</span>
        trigger(target, TriggerOpTypes.SET, key, value, oldValue);
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> result;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">1.2.3 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/baseHandlers.ts#L174" target="_blank" rel="nofollow noopener noreferrer">deleteProperty 函数</a> 和 has、ownKey函数</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target: <span class="hljs-built_in">object</span>, key: <span class="hljs-built_in">string</span> | symbol</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">const</span> hadKey = hasOwn(target, key);
  <span class="hljs-keyword">const</span> oldValue = (target <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>)[key];
  <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Reflect</span>.deleteProperty(target, key);
  <span class="hljs-keyword">if</span> (result && hadKey) &#123;
    trigger(target, TriggerOpTypes.DELETE, key, <span class="hljs-literal">undefined</span>, oldValue);
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>deleteProperty函数</code> 就做了删除对应的 value、然后判断是否存在来触发依赖。</p>
</li>
<li>
<p><code>has、ownKeys</code> 函数调用较为简单、直接进行依赖收集，等到 set 情况进行触发依赖。</p>
</li>
<li>
<p><code>collectionHandlers.ts</code>里面的处理比较类似，对相关的操作做出类似的处理，调用<code>原型上面的function(get、set、has)进行原生处理</code>。</p>
</li>
</ul>
<h3 data-id="heading-9">1.3 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/effect.ts" target="_blank" rel="nofollow noopener noreferrer">effect.ts 解读</a></h3>
<ul>
<li><code>effect.ts</code> 里面有 track（依赖收集）函数、trigger（依赖触发函数）和 effect 副作用函数。</li>
<li>其中核心的是<code>track和trigger</code>，而<code>effect</code>作为为外部提供依赖监听触发的函数，可以运用在 vue 的更新流程中和日常使用。</li>
</ul>
<h4 data-id="heading-10">1.3.1 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/effect.ts#L70" target="_blank" rel="nofollow noopener noreferrer">effect function 实现</a></h4>
<ul>
<li>（1）处理多层<code>effect</code>包裹 callback；</li>
<li>（2）创建<code>reactiveEffect</code>，判断<code>options.lazy</code>是否默认执行一次 effect。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 定义了effect函数的类型</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> ReactiveEffect<T = any> &#123;
  (): T; <span class="hljs-comment">// 一个函数的申明</span>
  _isEffect: <span class="hljs-literal">true</span>;
  id: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 对应自身的id</span>
  active: <span class="hljs-built_in">boolean</span>; <span class="hljs-comment">// 是否被激活了</span>
  raw: <span class="hljs-function">() =></span> T; <span class="hljs-comment">// 被调用的目标对象源（effect(fn)调用的fn）</span>
  deps: <span class="hljs-built_in">Array</span><Dep>; <span class="hljs-comment">// 依赖项（也是一个effect Set集）</span>
  options: ReactiveEffectOptions; <span class="hljs-comment">// 调用effect的第二个参数选项</span>
  allowRecurse: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="hljs-comment">// 存储当前调用的effect函数，用于track进行收集</span>
<span class="hljs-keyword">const</span> effectStack: ReactiveEffect[] = [];
<span class="hljs-comment">// 如其名，激活中的effect函数</span>
<span class="hljs-keyword">let</span> activeEffect: ReactiveEffect | <span class="hljs-literal">undefined</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  fn: () => T,
  options: ReactiveEffectOptions = EMPTY_OBJ
</span>): <span class="hljs-title">ReactiveEffect</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-comment">// 传递进来的fn已经是effect过的function，则直接拿这个fn的raw（也就是上次被fn的回调函数）</span>
  <span class="hljs-keyword">if</span> (isEffect(fn)) &#123;
    fn = fn.raw;
  &#125;
  <span class="hljs-comment">// 调用创建ReactiveEffect</span>
  <span class="hljs-keyword">const</span> effect = createReactiveEffect(fn, options);
  <span class="hljs-comment">// 默认调用一次</span>
  <span class="hljs-keyword">if</span> (!options.lazy) &#123;
    effect();
  &#125;
  <span class="hljs-comment">// 返回被创建的ReactiveEffect</span>
  <span class="hljs-keyword">return</span> effect;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>（3）effect 处理的只有创建一个 effect 对象，除了执行，也可以用来暂停处理；</li>
<li>（4）同时设置下当前被<code>激活的 effect、用于 track 进行收集</code>，相对简单明了；</li>
<li>（5）stop 的作用就是<code>清空依赖、修改active为false</code>。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveEffect</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  fn: () => T,
  options: ReactiveEffectOptions
</span>): <span class="hljs-title">ReactiveEffect</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveEffect</span>(<span class="hljs-params"></span>): <span class="hljs-title">unknown</span> </span>&#123;
    <span class="hljs-comment">// 非激活状态，直接执行fn这个callback，不做后续操作</span>
    <span class="hljs-comment">// 这种情况下在stop函数被调用时候存在，这时候进行get、has操作则不会收集到对应的依赖</span>
    <span class="hljs-keyword">if</span> (!effect.active) &#123;
      <span class="hljs-keyword">return</span> fn()
    &#125;
    <span class="hljs-comment">// 不存在情况，需要保存effect到栈里面缓存</span>
    <span class="hljs-keyword">if</span> (!effectStack.includes(effect)) &#123;
      <span class="hljs-comment">// 清除正在运行的effect依赖</span>
      cleanup(effect)
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 禁止收集依赖，收集上次的track state</span>
        enableTracking()
        effectStack.push(effect)
        <span class="hljs-comment">// 设置当前激活</span>
        activeEffect = effect
        <span class="hljs-keyword">return</span> fn() <span class="hljs-comment">// 调用fn回调函数，默认收集一次依赖</span>
      &#125; <span class="hljs-keyword">finally</span> &#123;
        effectStack.pop() <span class="hljs-comment">// 只想完毕推出栈</span>
        <span class="hljs-comment">// 复原到上次的track state 和 active effect</span>
        resetTracking()
        activeEffect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">as</span> ReactiveEffect
  <span class="hljs-comment">// 配置一些变量到effect fn上做下次处理</span>
  effect.id = uid++
  effect.allowRecurse = !!options.allowRecurse
  effect._isEffect = <span class="hljs-literal">true</span>
  effect.active = <span class="hljs-literal">true</span>
  effect.raw = fn
  effect.deps = []
  effect.options = options
  <span class="hljs-keyword">return</span> effect
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">1.3.2 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/effect.ts#L70" target="_blank" rel="nofollow noopener noreferrer">track function 依赖收集实现</a></h4>
<ul>
<li>
<p>（1）<code>WeakMap</code> 和 <code>Map</code> 的区别在于，key 必须是对象，而且还是<code>对象的浅引用</code>（删除原对象 key 不受影响）；</p>
</li>
<li>
<p>（2）在 Vue3 中、是直接使用 WeakMap 的 key 为被代理前的对象；</p>
<ul>
<li>WeakMap 的 value 则是一个 key 的 Map。</li>
<li>key 的 Map 内部又存储了 Set 集合的 ReactiveEffect 函数。</li>
</ul>
</li>
<li>
<p>（3）<code>track</code>通过判断全局变量<code>shouldTrack 和 activeEffect</code>，进行依赖的 Map 和 Set 的验证，最终存储<code>activeEffect 到 depsMap中对应key: value(Set)，然后把 value（Set） 放入 activeEffect.deps 里面</code>。</p>
</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/*
    主要存储形式是 WeakMap<target, new Map<key, new Set<ReactiveEffect>>>
*/</span>
<span class="hljs-keyword">type</span> Dep = <span class="hljs-built_in">Set</span><ReactiveEffect>;
<span class="hljs-keyword">type</span> KeyToDepMap = <span class="hljs-built_in">Map</span><<span class="hljs-built_in">any</span>, Dep>;

<span class="hljs-keyword">const</span> targetMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span><<span class="hljs-built_in">any</span>, KeyToDepMap>();
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target: <span class="hljs-built_in">object</span>, <span class="hljs-keyword">type</span>: TrackOpTypes, key: unknown</span>) </span>&#123;
  <span class="hljs-comment">// 当前状态是禁止收集依赖 | 被激活的activeEffect没有（就是没有调用过effect、ref等API情况）</span>
  <span class="hljs-keyword">if</span> (!shouldTrack || activeEffect === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-comment">// 被代理的key map，也就是依赖收集的map</span>
  <span class="hljs-keyword">let</span> depsMap = targetMap.get(target);
  <span class="hljs-keyword">if</span> (!depsMap) &#123;
    targetMap.set(target, (depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()));
  &#125;
  <span class="hljs-comment">// depsMap中拿到Set集，没有也重新设置</span>
  <span class="hljs-keyword">let</span> dep = depsMap.get(key);
  <span class="hljs-keyword">if</span> (!dep) &#123;
    depsMap.set(key, (dep = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()));
  &#125;
  <span class="hljs-comment">// 当前key不存在这个依赖函数，则添加，并且在依赖函数上面添加这个dep集合，用于后续的清理操作</span>
  <span class="hljs-keyword">if</span> (!dep.has(activeEffect)) &#123;
    dep.add(activeEffect);
    activeEffect.deps.push(dep);
    <span class="hljs-comment">// 开发模式下调用effect(fn, option的onTrack函数，用于测试和调试)</span>
    <span class="hljs-keyword">if</span> (__DEV__ && activeEffect.options.onTrack) &#123;
      activeEffect.options.onTrack(<span class="hljs-comment">/* ... */</span>);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">1.3.3 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/effect.ts#L70" target="_blank" rel="nofollow noopener noreferrer">trigger function 依赖触发实现</a></h4>
<ul>
<li>（1）通过判断什么类型，拿到对应的 effect，放入 Set 集合中，处理一些特殊的 effect；</li>
<li>（2）最后 <code>run</code> 函数执行，判断是否有<code>scheduler函数</code>来执行 <code>scheduler</code> 还是 <code>effect</code> 自身。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">
  target: object,
  type: TriggerOpTypes,
  key?: unknown,
  newValue?: unknown,
  oldValue?: unknown,
  oldTarget?: <span class="hljs-built_in">Map</span><unknown, unknown> | <span class="hljs-built_in">Set</span><unknown>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> depsMap = targetMap.get(target)
  <span class="hljs-keyword">if</span> (!depsMap) &#123;
    <span class="hljs-comment">// never been tracked</span>
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 创建一个依赖函数集，用于收集相关的依赖，等到run时执行触发</span>
  <span class="hljs-keyword">const</span> effects = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><ReactiveEffect>()
  <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">effectsToAdd: <span class="hljs-built_in">Set</span><ReactiveEffect> | <span class="hljs-literal">undefined</span></span>) =></span> &#123;
    <span class="hljs-comment">// 收集非当前已经激活的effect</span>
    <span class="hljs-keyword">if</span> (effectsToAdd) &#123;
      effectsToAdd.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (effect !== activeEffect || effect.allowRecurse) &#123;
          effects.add(effect)
        &#125;
      &#125;)
    &#125;
  &#125;
  <span class="hljs-comment">// 对各自type、Array进行处理添加到effects集合中。</span>
  <span class="hljs-keyword">if</span> (type === TriggerOpTypes.CLEAR) &#123;
    <span class="hljs-comment">// collection being cleared</span>
    <span class="hljs-comment">// trigger all effects for target</span>
    depsMap.forEach(add)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'length'</span> && isArray(target)) &#123;
    depsMap.forEach(<span class="hljs-function">(<span class="hljs-params">dep, key</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'length'</span> || key >= (newValue <span class="hljs-keyword">as</span> number)) &#123;
        add(dep)
      &#125;
    &#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// schedule runs for SET | ADD | DELETE</span>
    <span class="hljs-keyword">if</span> (key !== <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>) &#123;
      add(depsMap.get(key))
    &#125;
    <span class="hljs-comment">// 迭代操作的key操作依赖</span>
    <span class="hljs-comment">// also run for iteration key on ADD | DELETE | Map.SET</span>
    <span class="hljs-keyword">switch</span> (type) &#123;
      <span class="hljs-keyword">case</span> TriggerOpTypes.ADD:
        <span class="hljs-keyword">if</span> (!isArray(target)) &#123;
          <span class="hljs-comment">// 对象在ownKeys情况设置的依赖、add、delete、set情况都有</span>
          add(depsMap.get(ITERATE_KEY))
          <span class="hljs-keyword">if</span> (isMap(target)) &#123;
            add(depsMap.get(MAP_KEY_ITERATE_KEY))
          &#125;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isIntegerKey(key)) &#123;
          <span class="hljs-comment">// 新增索引到数组之后触发的length改变依赖</span>
          <span class="hljs-comment">// new index added to array -> length changes</span>
          add(depsMap.get(<span class="hljs-string">'length'</span>))
        &#125;
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> TriggerOpTypes.DELETE:
        <span class="hljs-keyword">if</span> (!isArray(target)) &#123;
          add(depsMap.get(ITERATE_KEY))
          <span class="hljs-keyword">if</span> (isMap(target)) &#123;
            add(depsMap.get(MAP_KEY_ITERATE_KEY))
          &#125;
        &#125;
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> TriggerOpTypes.SET:
        <span class="hljs-keyword">if</span> (isMap(target)) &#123;
          add(depsMap.get(ITERATE_KEY))
        &#125;
        <span class="hljs-keyword">break</span>
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> run = <span class="hljs-function">(<span class="hljs-params">effect: ReactiveEffect</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (__DEV__ && effect.options.onTrigger) &#123;
      effect.options.onTrigger(<span class="hljs-comment">/* ... */</span>)
    &#125;
    <span class="hljs-comment">// 最终运行依赖，当依赖存在scheduler函数，则执行提供的scheduler函数，否则执行effect函数</span>
    <span class="hljs-keyword">if</span> (effect.options.scheduler) &#123;
      effect.options.scheduler(effect)
    &#125; <span class="hljs-keyword">else</span> &#123;
      effect()
    &#125;
  &#125;
  <span class="hljs-comment">// 运行需要执行的依赖项</span>
  effects.forEach(run)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">1.4 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/ref.ts" target="_blank" rel="nofollow noopener noreferrer">ref.ts 解读</a></h3>
<h4 data-id="heading-14">1.4.1 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/ref.ts#L38" target="_blank" rel="nofollow noopener noreferrer">ref function 实现</a></h4>
<ul>
<li>（1）首先定义 TypeScript 函数重载，调用<code>createRef</code>；</li>
<li>（2）在<code>createRef</code>中验证 rawValue 是不是 ref 来进行创建 ref 实例并返回；</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>>(<span class="hljs-params">value: T</span>): <span class="hljs-title">ToRef</span><<span class="hljs-title">T</span>></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span><<span class="hljs-title">T</span>>(<span class="hljs-params">value: T</span>): <span class="hljs-title">Ref</span><<span class="hljs-title">UnwrapRef</span><<span class="hljs-title">T</span>>></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params"></span>): <span class="hljs-title">Ref</span><<span class="hljs-title">T</span> | <span class="hljs-title">undefined</span>></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">value?: unknown</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createRef(value);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRef</span>(<span class="hljs-params">rawValue: unknown, shallow = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-comment">// ref情况直接返回</span>
  <span class="hljs-keyword">if</span> (isRef(rawValue)) &#123;
    <span class="hljs-keyword">return</span> rawValue;
  &#125;
  <span class="hljs-comment">// 创建一个Ref对象实例</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> RefImpl(rawValue, shallow);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>（3）先验证是否是 shallow，非 shallow 则进行<code>调用convert深度代理（对象情况）</code>；</li>
<li>（4）然后在<code>.value</code>获取的时候收集依赖，赋值时<code>调用convert</code>并<code>触发依赖</code>。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> convert = <T extends unknown>(val: T): T =>
  isObject(val) ? reactive(val) : val;

class RefImpl<T> &#123;
  private _value: T; // 存储我们定义的rawValue

  public readonly __v_isRef = true; // 标识是一个ref

  constructor(private _rawValue: T, public readonly _shallow: boolean) &#123;
    // 判断是不是浅层渲染还是深层次渲染（深层次渲染进行验证、对象情况通过reactive代理）
    this._value = _shallow ? _rawValue : convert(_rawValue);
  &#125;
  // .value时候，触发track操作收集依赖，key为value
  get value() &#123;
    track(toRaw(this), TrackOpTypes.GET, "value");
    return this._value;
  &#125;
  // .set时候验证是否值有变化，并且再次验证是否需要继续代理
  // 最后执行依赖触发操作
  set value(newVal) &#123;
    if (hasChanged(toRaw(newVal), this._rawValue)) &#123;
      this._rawValue = newVal;
      this._value = this._shallow ? newVal : convert(newVal);
      trigger(toRaw(this), TriggerOpTypes.SET, "value", newVal);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">1.4.2 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/ref.ts#L149" target="_blank" rel="nofollow noopener noreferrer">toRefs function 实现</a></h4>
<ul>
<li>（1）<code>toRefs</code>方法，把代理过后的对象/数组每一项都进行 toRef 并返回；</li>
<li>（2）<code>toRef</code>方法则判断 isRef()来进行 objectRef 转换，旨意在<code>被解构之后还能保留响应式</code>状态。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toRefs</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>>(<span class="hljs-params"><span class="hljs-built_in">object</span>: T</span>): <span class="hljs-title">ToRefs</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">if</span> (__DEV__ && !isProxy(<span class="hljs-built_in">object</span>)) &#123;
    <span class="hljs-built_in">console</span>.warn(
      <span class="hljs-string">`toRefs() expects a reactive object but received a plain one.`</span>
    );
  &#125;
  <span class="hljs-keyword">const</span> ret: <span class="hljs-built_in">any</span> = isArray(<span class="hljs-built_in">object</span>) ? <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">object</span>.length) : &#123;&#125;;
  <span class="hljs-comment">// 处理生成新的数值（一个ObjectRef实例）</span>
  <span class="hljs-comment">// `for in` 这种操作触发了Proxy的`ownKeys`迭代操作</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> <span class="hljs-built_in">object</span>) &#123;
    ret[key] = toRef(<span class="hljs-built_in">object</span>, key);
  &#125;
  <span class="hljs-keyword">return</span> ret;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ObjectRefImpl</span><<span class="hljs-title">T</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">object</span>, <span class="hljs-title">K</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">readonly</span> __v_isRef = <span class="hljs-literal">true</span>
  <span class="hljs-comment">// 保存这个object和对应的key到.value操作上，并且设置成ref情况</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> _object: T, <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> _key: K</span>)</span> &#123;&#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._object[<span class="hljs-built_in">this</span>._key]
  &#125;

  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
    <span class="hljs-built_in">this</span>._object[<span class="hljs-built_in">this</span>._key] = newVal
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toRef</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>, <span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params">
  <span class="hljs-built_in">object</span>: T,
  key: K
</span>): <span class="hljs-title">ToRef</span><<span class="hljs-title">T</span>[<span class="hljs-title">K</span>]> </span>&#123;
  <span class="hljs-comment">// ref情况直接返回，非ref情况则创建ObjectRefImpl</span>
  <span class="hljs-keyword">return</span> isRef(<span class="hljs-built_in">object</span>[key])
    ? <span class="hljs-built_in">object</span>[key]
    : (<span class="hljs-keyword">new</span> ObjectRefImpl(<span class="hljs-built_in">object</span>, key) <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">1.5 <a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/computed.ts" target="_blank" rel="nofollow noopener noreferrer">computed.ts 解读</a></h3>
<h4 data-id="heading-17"><a href="https://github.com/vuejs/vue-next/blob/master/packages/reactivity/src/computed.ts#L66" target="_blank" rel="nofollow noopener noreferrer">computed function 实现</a></h4>
<ul>
<li>
<p>（1）判断参数，先处理get、set函数、最后调用<code>new ComputedRefImpl</code>创建实例；</p>
<ul>
<li>当传递的是 <code>getter</code>，默认给 <code>setter</code> 一个空函数。</li>
<li>当传递的是 <code>options</code>，则直接提供赋值给 <code>getter、setter</code>。</li>
</ul>
</li>
<li>
<p>（2）在 <code>ComputedRefImpl的constructor</code> 时；</p>
<ul>
<li>创建一个effect、把 <code>getter 当成 callback</code> 传入。</li>
<li>传递 <code>scheduler</code> 函数，调用时通过 <code>trigger</code> 依赖触发。</li>
</ul>
</li>
<li>
<p>（3）在get时候调用 <code>this.effect</code> 拿到新的值（前提是数据更新了），最终<code>track收集computed</code>的依赖项；</p>
</li>
<li>
<p>（4）则set情况直接调用setter。</p>
</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ComputedGetter<T> = <span class="hljs-function">(<span class="hljs-params">ctx?: <span class="hljs-built_in">any</span></span>) =></span> T
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ComputedSetter<T> = <span class="hljs-function">(<span class="hljs-params">v: T</span>) =></span> <span class="hljs-built_in">void</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> WritableComputedOptions<T> &#123;
  <span class="hljs-attr">get</span>: ComputedGetter<T>
  set: ComputedSetter<T>
&#125;

<span class="hljs-comment">// 进行函数重载，因为computed的参数可能是一个getter函数，也可以是一个包含get、set的对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span><<span class="hljs-title">T</span>>(<span class="hljs-params">getter: ComputedGetter<T></span>): <span class="hljs-title">ComputedRef</span><<span class="hljs-title">T</span>>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span><<span class="hljs-title">T</span>>(<span class="hljs-params">
  options: WritableComputedOptions<T>
</span>): <span class="hljs-title">WritableComputedRef</span><<span class="hljs-title">T</span>>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span><<span class="hljs-title">T</span>>(<span class="hljs-params">
  getterOrOptions: ComputedGetter<T> | WritableComputedOptions<T>
</span>) </span>&#123;
  <span class="hljs-title">let</span> <span class="hljs-title">getter</span>: <span class="hljs-title">ComputedGetter</span><<span class="hljs-title">T</span>>
  <span class="hljs-title">let</span> <span class="hljs-title">setter</span>: <span class="hljs-title">ComputedSetter</span><<span class="hljs-title">T</span>>
  // 如果是<span class="hljs-function"><span class="hljs-keyword">function</span>则是一个<span class="hljs-title">get</span>函数
  <span class="hljs-title">if</span> (<span class="hljs-params">isFunction(getterOrOptions)</span>) </span>&#123;
    <span class="hljs-title">getter</span> = <span class="hljs-title">getterOrOptions</span>
    <span class="hljs-title">setter</span> = <span class="hljs-title">__DEV__</span>
      ? (<span class="hljs-params"></span>) => </span>&#123;
          <span class="hljs-title">console</span>.<span class="hljs-title">warn</span>(<span class="hljs-params"><span class="hljs-string">'Write operation failed: computed value is readonly'</span></span>)
        &#125;
      : <span class="hljs-title">NOOP</span>
  &#125; <span class="hljs-title">else</span> </span>&#123;
    getter = getterOrOptions.get
    setter = getterOrOptions.set
  &#125;
  <span class="hljs-comment">// 创建ComputedRefImpl实例</span>
  <span class="hljs-comment">// 通过判断是函数/没有options.set函数为只读模式</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ComputedRefImpl(
    getter,
    setter,
    isFunction(getterOrOptions) || !getterOrOptions.set
  ) <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ComputedRefImpl</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">private</span> _value!: T
  <span class="hljs-keyword">private</span> _dirty = <span class="hljs-literal">true</span>

  <span class="hljs-keyword">public</span> <span class="hljs-keyword">readonly</span> effect: ReactiveEffect<T>

  <span class="hljs-keyword">public</span> <span class="hljs-keyword">readonly</span> __v_isRef = <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">readonly</span> [ReactiveFlags.IS_READONLY]: <span class="hljs-built_in">boolean</span>

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">
    getter: ComputedGetter<T>,
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> _setter: ComputedSetter<T>,
    isReadonly: <span class="hljs-built_in">boolean</span>
  </span>)</span> &#123;
    <span class="hljs-comment">// 进入创建一个异步执行的effect</span>
    <span class="hljs-built_in">this</span>.effect = effect(getter, &#123;
      <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 异步、不立即执行</span>
      <span class="hljs-attr">scheduler</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 等到trigger时候，触发effect.options.scheduler</span>
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>._dirty) &#123;
          <span class="hljs-comment">// 设置_dirty，依赖被调用过了，这时候才能去获取新的value</span>
          <span class="hljs-built_in">this</span>._dirty = <span class="hljs-literal">true</span>
          trigger(toRaw(<span class="hljs-built_in">this</span>), TriggerOpTypes.SET, <span class="hljs-string">'value'</span>)
        &#125;
      &#125;
    &#125;)

    <span class="hljs-built_in">this</span>[ReactiveFlags.IS_READONLY] = isReadonly
  &#125;

  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-comment">// the computed ref may get wrapped by other proxies e.g. readonly() #3376</span>
    <span class="hljs-comment">// 等到.value调起的时候拿值</span>
    <span class="hljs-keyword">const</span> self = toRaw(<span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">if</span> (self._dirty) &#123;
      self._value = <span class="hljs-built_in">this</span>.effect() <span class="hljs-comment">// 调用effect拿到getter执行结果</span>
      self._dirty = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-comment">// 收集依赖项</span>
    track(self, TrackOpTypes.GET, <span class="hljs-string">'value'</span>)
    <span class="hljs-keyword">return</span> self._value
  &#125;

  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newValue: T</span>) &#123;
    <span class="hljs-comment">// 赋值的时，调用setter</span>
    <span class="hljs-built_in">this</span>._setter(newValue)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">总体流程如图所示</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48a33976ede64718963a59b7e76f5949~tplv-k3u1fbpfcp-watermark.image" alt="reactivity流程图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">总结：</h3>
<ul>
<li>reactivity模块核心在于 <code>reactive、track、trigger、effect</code> 四个API、各类操作都离不开。</li>
<li>通过设置对应的 __v_xxx 变量来确定是否是一个 <code>reactive、ref、readonly、raw</code> 等，从而进行各种的处理。
<ul>
<li><code>isRef、isReactive、isReadonly、toRaw...</code> 都围绕了这些变量。</li>
<li>通过这些变量中的 <code>__v_raw</code> 可以在Proxy代理的get函数里面直接返回对象源。</li>
</ul>
</li>
<li><code>reactive函数</code> 内部处理了ref的解构和赋值，简化使用者使用的难度</li>
<li>Vue3的响应式原理就在于对 <code>Proxy的运用和依赖收集触发</code> 操作。
<ul>
<li>在其他地方通过effect+响应式原理进行更新操作。</li>
<li>具备了<code>组件级的effect</code>可能、当响应式数据发生变化，则调用到<code>effect的callback</code>对内部vnode进行diff。</li>
</ul>
</li>
<li>effect原则上就是定义 <code>activeEffect</code> 提供给track进行收集，等到trigger时触发。</li>
<li>而ref的核心是一个class的实例，里面使用了计算属性 <code>get value()、set value(newValue)</code> ，调用了 <code>track、trigger</code> 做到响应 <code>副作用</code>。</li>
<li>computed函数也是返回一个class实例、在<code>constructor时创建一个effect</code>、设置<code>_dirty来防止重复计算触发getter</code>，当依赖被触发之后才<code>调用get获取新的value</code>。</li>
<li>平时项目中，我们可以<code>直接使用vue提供的share模块</code>，直接导出使用相关的工具方法。</li>
</ul>
<h3 data-id="heading-20">参考文献：</h3>
<ol>
<li><a href="https://github.com/vuejs/vue-next" target="_blank" rel="nofollow noopener noreferrer">vue-next</a></li>
<li><a href="https://vue3js.cn/start/" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn</a></li>
<li><a href="https://developer.mozilla.org/zh-CN" target="_blank" rel="nofollow noopener noreferrer">MDN Web Docs</a></li>
</ol></div>  
</div>
            