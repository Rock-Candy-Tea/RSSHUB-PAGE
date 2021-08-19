
---
title: '再聊 Vue.js 3.2 关于 vnode 部分的优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=576'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 19:20:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=576'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>上一篇文章，分析了 Vue.js 3.2 关于响应式部分的优化，此外，在这次<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.vuejs.org%2Fposts%2Fvue-3.2.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.vuejs.org/posts/vue-3.2.html" ref="nofollow noopener noreferrer">优化升级</a>中，还有一个运行时的优化：</p>
<blockquote>
<p>~200% faster creation of plain element VNodes</p>
</blockquote>
<p>即针对普通元素类型 <code>vnode</code> 的创建，提升了约 <code>200%</code> 的性能。这也是一个非常伟大的优化，是 Vue 的官方核心开发者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHcySunYang" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/HcySunYang" ref="nofollow noopener noreferrer">HcySunYang</a> 实现的，可以参考这个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fpull%2F3334" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/pull/3334" ref="nofollow noopener noreferrer">PR</a>。</p>
<p>那么具体是怎么做的呢，在分析实现前，我想先带你了解一些 <code>vnode</code> 的背景知识。</p>
<h2 data-id="heading-1">什么是 vnode</h2>
<p><code>vnode</code> 本质上是用来描述 DOM 的 JavaScript 对象，它在 Vue.js 中可以描述不同类型的节点，比如普通元素节点、组件节点等。</p>
<h3 data-id="heading-2">普通元素 vnode</h3>
<p>什么是普通元素节点呢？举个例子，在 HTML 中我们使用 <code><button></code> 标签来写一个按钮：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width:100px;height:50px"</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用 <code>vnode</code> 这样表示 <code><button></code> 标签：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vnode = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'button'</span>,
  <span class="hljs-attr">props</span>: &#123; 
    <span class="hljs-string">'class'</span>: <span class="hljs-string">'btn'</span>,
    <span class="hljs-attr">style</span>: &#123;
      <span class="hljs-attr">width</span>: <span class="hljs-string">'100px'</span>,
      <span class="hljs-attr">height</span>: <span class="hljs-string">'50px'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">children</span>: <span class="hljs-string">'click me'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，<code>type</code> 属性表示 DOM 的标签类型；<code>props</code> 属性表示 DOM 的一些附加信息，比如 <code>style</code> 、<code>class</code> 等；<code>children</code> 属性表示 DOM 的子节点，在该示例中它是一个简单的文本字符串，当然，<code>children</code> 也可以是一个 <code>vnode</code> 数组。</p>
<h3 data-id="heading-3">组件 vnode</h3>
<p><code>vnode</code> 除了可以像上面那样用于描述一个真实的 DOM，也可以用来描述组件。举个例子，我们在模板中引入一个组件标签 <code><custom-component></code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">custom-component</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"test"</span>></span><span class="hljs-tag"></<span class="hljs-name">custom-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用 <code>vnode</code> 这样表示 <code><custom-component></code> 组件标签：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CustomComponent = &#123;
  <span class="hljs-comment">// 在这里定义组件对象</span>
&#125;
<span class="hljs-keyword">const</span> vnode = &#123;
  <span class="hljs-attr">type</span>: CustomComponent,
  <span class="hljs-attr">props</span>: &#123; 
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'test'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件 <code>vnode</code> 其实是对抽象事物的描述，这是因为我们并不会在页面上真正渲染一个 <code><custom-component></code> 标签，而最终会渲染组件内部定义的 HTML 标签。</p>
<p>除了上述两种 <code>vnode</code> 类型外，还有纯文本 <code>vnode</code>、注释 <code>vnode</code> 等等。</p>
<p>另外，Vue.js 3.x 内部还针对 <code>vnode</code> 的 <code>type</code>，做了更详尽的分类，包括 <code>Suspense</code>、<code>Teleport</code> 等，并且把 <code>vnode</code> 的类型信息做了编码，以便在后面 <code>vnode </code>的挂载阶段，可以根据不同的类型执行相应的处理逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// runtime-core/src/vnode.ts</span>
<span class="hljs-keyword">const</span> shapeFlag = isString(type)
  ? <span class="hljs-number">1</span> <span class="hljs-comment">/* ELEMENT */</span>
  : isSuspense(type)
    ? <span class="hljs-number">128</span> <span class="hljs-comment">/* SUSPENSE */</span>
    : isTeleport(type)
      ? <span class="hljs-number">64</span> <span class="hljs-comment">/* TELEPORT */</span>
      : isObject(type)
        ? <span class="hljs-number">4</span> <span class="hljs-comment">/* STATEFUL_COMPONENT */</span>
        : isFunction(type)
          ? <span class="hljs-number">2</span> <span class="hljs-comment">/* FUNCTIONAL_COMPONENT */</span>
          : <span class="hljs-number">0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">vnode 的优势</h3>
<p>知道什么是 <code>vnode</code> 后，你可能会好奇，那么 <code>vnode</code> 有什么优势呢？为什么一定要设计 <code>vnode</code> 这样的数据结构呢？</p>
<p>首先是抽象，引入 <code>vnode</code>，可以把渲染过程抽象化，从而使得组件的抽象能力也得到提升。</p>
<p>其次是跨平台，因为 <code>patch vnode</code> 的过程不同平台可以有自己的实现，基于 <code>vnode</code> 再做服务端渲染、<code>weex</code> 平台、小程序平台的渲染都变得容易了很多。</p>
<p>不过这里要特别注意，在浏览器端使用 <code>vnode</code> 并不意味着不用操作 DOM 了，很多人会误以为 <code>vnode</code> 的性能一定比手动操作原生 DOM 好，这个其实是不一定的。</p>
<p>因为这种基于 <code>vnode</code> 实现的 MVVM 框架，在每次组件渲染生成 <code>vnode</code> 的过程中，会有一定的 JavaScript 耗时，尤其是是大组件。举个例子，一个 <code>1000 * 10</code> 的 Table 组件，组件渲染生成 <code>vnode</code> 的过程会遍历 <code>1000 * 10</code> 次去创建内部 <code>cell vnode</code>，整个耗时就会变得比较长，再加上挂载 <code>vnode</code> 生成 DOM 的过程也会有一定的耗时，当我们去更新组件的时候，用户会感觉到明显的卡顿。</p>
<p>虽然 diff 算法在减少 DOM 操作方面足够优秀，但最终还是免不了操作 DOM，所以说性能并不是 <code>vnode</code> 的优势。</p>
<h2 data-id="heading-5">如何创建 vnode</h2>
<p>通常我们开发组件都是编写组件的模板，并不会手写 <code>vnode</code>，那么 <code>vnode</code> 是如何创建的呢？</p>
<p>我们知道，组件模板经过编译，会生成对应的 <code>render</code> 函数，在 <code>render</code> 函数内部，会执行 <code>createVNode</code> 函数创建 <code>vnode</code> 对象，我们来看一下 Vue.js 3.2 之前它的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVNode</span>(<span class="hljs-params">type, props = <span class="hljs-literal">null</span>, children = <span class="hljs-literal">null</span>, patchFlag = <span class="hljs-number">0</span>, dynamicProps = <span class="hljs-literal">null</span>, isBlockNode = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!type || type === NULL_DYNAMIC_COMPONENT) &#123;
    <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && !type) &#123;
      warn(<span class="hljs-string">`Invalid vnode type when creating vnode: <span class="hljs-subst">$&#123;type&#125;</span>.`</span>)
    &#125;
    type = Comment
  &#125;
  <span class="hljs-keyword">if</span> (isVNode(type)) &#123;
    <span class="hljs-keyword">const</span> cloned = cloneVNode(type, props, <span class="hljs-literal">true</span> <span class="hljs-comment">/* mergeRef: true */</span>)
    <span class="hljs-keyword">if</span> (children) &#123;
      normalizeChildren(cloned, children)
    &#125;
    <span class="hljs-keyword">return</span> cloned
  &#125;
  <span class="hljs-comment">// 类组件的标准化</span>
  <span class="hljs-keyword">if</span> (isClassComponent(type)) &#123;
    type = type.__vccOpts
  &#125;
  <span class="hljs-comment">// class 和 style 标准化.</span>
  <span class="hljs-keyword">if</span> (props) &#123;
    <span class="hljs-keyword">if</span> (isProxy(props) || InternalObjectKey <span class="hljs-keyword">in</span> props) &#123;
      props = extend(&#123;&#125;, props)
    &#125;
    <span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">class</span>: klass, style &#125; = props
    <span class="hljs-keyword">if</span> (klass && !isString(klass)) &#123;
      props.class = normalizeClass(klass)
    &#125;
    <span class="hljs-keyword">if</span> (isObject(style)) &#123;
      <span class="hljs-keyword">if</span> (isProxy(style) && !isArray(style)) &#123;
        style = extend(&#123;&#125;, style)
      &#125;
      props.style = normalizeStyle(style)
    &#125;
  &#125;
  <span class="hljs-comment">// 根据 vnode 的类型编码</span>
  <span class="hljs-keyword">const</span> shapeFlag = isString(type)
    ? <span class="hljs-number">1</span> <span class="hljs-comment">/* ELEMENT */</span>
    : isSuspense(type)
      ? <span class="hljs-number">128</span> <span class="hljs-comment">/* SUSPENSE */</span>
      : isTeleport(type)
        ? <span class="hljs-number">64</span> <span class="hljs-comment">/* TELEPORT */</span>
        : isObject(type)
          ? <span class="hljs-number">4</span> <span class="hljs-comment">/* STATEFUL_COMPONENT */</span>
          : isFunction(type)
            ? <span class="hljs-number">2</span> <span class="hljs-comment">/* FUNCTIONAL_COMPONENT */</span>
            : <span class="hljs-number">0</span>
  <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && shapeFlag & <span class="hljs-number">4</span> <span class="hljs-comment">/* STATEFUL_COMPONENT */</span> && isProxy(type)) &#123;
    type = toRaw(type)
    warn(<span class="hljs-string">`Vue received a Component which was made a reactive object. This can `</span> +
      <span class="hljs-string">`lead to unnecessary performance overhead, and should be avoided by `</span> +
      <span class="hljs-string">`marking the component with `</span>markRaw<span class="hljs-string">` or using `</span>shallowRef<span class="hljs-string">` `</span> +
      <span class="hljs-string">`instead of `</span>ref<span class="hljs-string">`.`</span>, <span class="hljs-string">`\nComponent that was made reactive: `</span>, type)
  &#125;
  <span class="hljs-keyword">const</span> vnode = &#123;
    <span class="hljs-attr">__v_isVNode</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">__v_skip</span>: <span class="hljs-literal">true</span>,
    type,
    props,
    <span class="hljs-attr">key</span>: props && normalizeKey(props),
    <span class="hljs-attr">ref</span>: props && normalizeRef(props),
    <span class="hljs-attr">scopeId</span>: currentScopeId,
    <span class="hljs-attr">slotScopeIds</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">children</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">suspense</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ssContent</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ssFallback</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">dirs</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">transition</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">el</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">anchor</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">targetAnchor</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">staticCount</span>: <span class="hljs-number">0</span>,
    shapeFlag,
    patchFlag,
    dynamicProps,
    <span class="hljs-attr">dynamicChildren</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">appContext</span>: <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && vnode.key !== vnode.key) &#123;
    warn(<span class="hljs-string">`VNode created with invalid key (NaN). VNode type:`</span>, vnode.type)
  &#125;
  normalizeChildren(vnode, children)
  <span class="hljs-comment">// 标准化 suspense 子节点</span>
  <span class="hljs-keyword">if</span> (shapeFlag & <span class="hljs-number">128</span> <span class="hljs-comment">/* SUSPENSE */</span>) &#123;
    type.normalize(vnode)
  &#125;
  <span class="hljs-keyword">if</span> (isBlockTreeEnabled > <span class="hljs-number">0</span> &&
    !isBlockNode &&
    currentBlock &&
    (patchFlag > <span class="hljs-number">0</span> || shapeFlag & <span class="hljs-number">6</span> <span class="hljs-comment">/* COMPONENT */</span>) &&
    patchFlag !== <span class="hljs-number">32</span> <span class="hljs-comment">/* HYDRATE_EVENTS */</span>) &#123;
    currentBlock.push(vnode)
  &#125;
  <span class="hljs-keyword">return</span> vnode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，创建 <code>vnode</code> 的过程做了很多事情，其中有很多判断的逻辑，比如判断 <code>type</code> 是否为空：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!type || type === NULL_DYNAMIC_COMPONENT) &#123;
  <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && !type) &#123;
    warn(<span class="hljs-string">`Invalid vnode type when creating vnode: <span class="hljs-subst">$&#123;type&#125;</span>.`</span>)
  &#125;
  type = Comment
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断 <code>type</code> 是不是一个 <code>vnode</code> 节点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (isVNode(type)) &#123;
  <span class="hljs-keyword">const</span> cloned = cloneVNode(type, props, <span class="hljs-literal">true</span> <span class="hljs-comment">/* mergeRef: true */</span>)
  <span class="hljs-keyword">if</span> (children) &#123;
    normalizeChildren(cloned, children)
  &#125;
  <span class="hljs-keyword">return</span> cloned
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断 <code>type</code> 是不是一个 <code>class</code> 类型的组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (isClassComponent(type)) &#123;
    type = type.__vccOpts
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除此之外，还会对属性中的 <code>style</code> 和 <code>class</code> 执行标准化，其中也会有一些判断逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (props) &#123;
  <span class="hljs-keyword">if</span> (isProxy(props) || InternalObjectKey <span class="hljs-keyword">in</span> props) &#123;
    props = extend(&#123;&#125;, props)
  &#125;
  <span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">class</span>: klass, style &#125; = props
  <span class="hljs-keyword">if</span> (klass && !isString(klass)) &#123;
    props.class = normalizeClass(klass)
  &#125;
  <span class="hljs-keyword">if</span> (isObject(style)) &#123;
    <span class="hljs-keyword">if</span> (isProxy(style) && !isArray(style)) &#123;
      style = extend(&#123;&#125;, style)
    &#125;
    props.style = normalizeStyle(style)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来还会根据 <code>vnode</code> 的类型编码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> shapeFlag = isString(type)
  ? <span class="hljs-number">1</span> <span class="hljs-comment">/* ELEMENT */</span>
  : isSuspense(type)
    ? <span class="hljs-number">128</span> <span class="hljs-comment">/* SUSPENSE */</span>
    : isTeleport(type)
      ? <span class="hljs-number">64</span> <span class="hljs-comment">/* TELEPORT */</span>
      : isObject(type)
        ? <span class="hljs-number">4</span> <span class="hljs-comment">/* STATEFUL_COMPONENT */</span>
        : isFunction(type)
          ? <span class="hljs-number">2</span> <span class="hljs-comment">/* FUNCTIONAL_COMPONENT */</span>
          : <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就是创建 <code>vnode</code> 对象，创建完后还会执行 <code>normalizeChildren</code> 去标准化子节点，这个过程也会有一系列的判断逻辑。</p>
<h2 data-id="heading-6">创建 vnode 过程的优化</h2>
<p>仔细想想，<code>vnode</code> 本质上就是一个 JavaScript 对象，之所以在创建过程中做很多判断，是因为要处理各种各样的情况。<strong>然而对于普通元素 <code>vnode</code> 而言，完全不需要这么多的判断逻辑</strong>，因此对于普通元素 <code>vnode</code>，使用 <code>createVNode</code> 函数创建就是一种浪费。</p>
<p>顺着这个思路，就可以在模板编译阶段，针对普通元素节点，使用新的函数来创建 <code>vnode</code>，Vue.js 3.2 就是这么做的，举个例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"home"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"Vue logo"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../assets/logo.png"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Welcome to Your Vue.js App"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>借助于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue-next-template-explorer.netlify.app%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vue-next-template-explorer.netlify.app/" ref="nofollow noopener noreferrer">模板导出工具</a>，可以看到它编译后的 <code>render</code> 函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createElementVNode <span class="hljs-keyword">as</span> _createElementVNode, resolveComponent <span class="hljs-keyword">as</span> _resolveComponent, createVNode <span class="hljs-keyword">as</span> _createVNode, openBlock <span class="hljs-keyword">as</span> _openBlock, createElementBlock <span class="hljs-keyword">as</span> _createElementBlock &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>

<span class="hljs-keyword">const</span> _hoisted_1 = &#123; <span class="hljs-attr">class</span>: <span class="hljs-string">"home"</span> &#125;
<span class="hljs-keyword">const</span> _hoisted_2 = <span class="hljs-comment">/*#__PURE__*/</span>_createElementVNode(<span class="hljs-string">"img"</span>, &#123;
  <span class="hljs-attr">alt</span>: <span class="hljs-string">"Vue logo"</span>,
  <span class="hljs-attr">src</span>: <span class="hljs-string">"../assets/logo.png"</span>
&#125;, <span class="hljs-literal">null</span>, -<span class="hljs-number">1</span> <span class="hljs-comment">/* HOISTED */</span>)

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">_ctx, _cache, $props, $setup, $data, $options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> _component_HelloWorld = _resolveComponent(<span class="hljs-string">"HelloWorld"</span>)

  <span class="hljs-keyword">return</span> (_openBlock(), _createElementBlock(<span class="hljs-string">"template"</span>, <span class="hljs-literal">null</span>, [
    _createElementVNode(<span class="hljs-string">"div"</span>, _hoisted_1, [
      _hoisted_2,
      _createVNode(_component_HelloWorld, &#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"Welcome to Your Vue.js App"</span> &#125;)
    ])
  ]))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>针对于 <code>div</code> 节点，这里使用了 <code>createElementVNode</code> 方法而并非 <code>createVNode</code> 方法，而 <code>createElementVNode</code> 在内部是 <code>createBaseVNode</code> 的别名，来看它的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createBaseVNode</span>(<span class="hljs-params">type, props = <span class="hljs-literal">null</span>, children = <span class="hljs-literal">null</span>, patchFlag = <span class="hljs-number">0</span>, dynamicProps = <span class="hljs-literal">null</span>, shapeFlag = type === Fragment ? <span class="hljs-number">0</span> : <span class="hljs-number">1</span> <span class="hljs-comment">/* ELEMENT */</span>, isBlockNode = <span class="hljs-literal">false</span>, needFullChildrenNormalization = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode = &#123;
    <span class="hljs-attr">__v_isVNode</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">__v_skip</span>: <span class="hljs-literal">true</span>,
    type,
    props,
    <span class="hljs-attr">key</span>: props && normalizeKey(props),
    <span class="hljs-attr">ref</span>: props && normalizeRef(props),
    <span class="hljs-attr">scopeId</span>: currentScopeId,
    <span class="hljs-attr">slotScopeIds</span>: <span class="hljs-literal">null</span>,
    children,
    <span class="hljs-attr">component</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">suspense</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ssContent</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ssFallback</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">dirs</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">transition</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">el</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">anchor</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">targetAnchor</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">staticCount</span>: <span class="hljs-number">0</span>,
    shapeFlag,
    patchFlag,
    dynamicProps,
    <span class="hljs-attr">dynamicChildren</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">appContext</span>: <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> (needFullChildrenNormalization) &#123;
    normalizeChildren(vnode, children)
    <span class="hljs-keyword">if</span> (shapeFlag & <span class="hljs-number">128</span> <span class="hljs-comment">/* SUSPENSE */</span>) &#123;
      type.normalize(vnode)
    &#125;
  &#125;
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (children) &#123;
    vnode.shapeFlag |= isString(children)
      ? <span class="hljs-number">8</span> <span class="hljs-comment">/* TEXT_CHILDREN */</span>
      : <span class="hljs-number">16</span> <span class="hljs-comment">/* ARRAY_CHILDREN */</span>
  &#125;
  <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && vnode.key !== vnode.key) &#123;
    warn(<span class="hljs-string">`VNode created with invalid key (NaN). VNode type:`</span>, vnode.type)
  &#125;
  <span class="hljs-keyword">if</span> (isBlockTreeEnabled > <span class="hljs-number">0</span> &&
    !isBlockNode &&
    currentBlock &&
    (vnode.patchFlag > <span class="hljs-number">0</span> || shapeFlag & <span class="hljs-number">6</span> <span class="hljs-comment">/* COMPONENT */</span>) &&
    vnode.patchFlag !== <span class="hljs-number">32</span> <span class="hljs-comment">/* HYDRATE_EVENTS */</span>) &#123;
    currentBlock.push(vnode)
  &#125;
  <span class="hljs-keyword">return</span> vnode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>createBaseVNode</code> 内部仅仅是创建了 <code>vnode</code> 对象，然后做了一些 <code>block</code> 逻辑的处理。相比于之前的 <code>createVNode</code> 的实现，<code>createBaseVNode</code> 少执行了很多判断逻辑，自然性能就获得了提升。</p>
<p>而 <code>createVNode</code> 的实现，是基于 <code>createBaseVNode</code> 做的一层封装：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVNode</span>(<span class="hljs-params">type, props = <span class="hljs-literal">null</span>, children = <span class="hljs-literal">null</span>, patchFlag = <span class="hljs-number">0</span>, dynamicProps = <span class="hljs-literal">null</span>, isBlockNode = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!type || type === NULL_DYNAMIC_COMPONENT) &#123;
    <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && !type) &#123;
      warn(<span class="hljs-string">`Invalid vnode type when creating vnode: <span class="hljs-subst">$&#123;type&#125;</span>.`</span>)
    &#125;
    type = Comment$<span class="hljs-number">1</span>
  &#125;
  <span class="hljs-keyword">if</span> (isVNode(type)) &#123;
    <span class="hljs-keyword">const</span> cloned = cloneVNode(type, props, <span class="hljs-literal">true</span> <span class="hljs-comment">/* mergeRef: true */</span>)
    <span class="hljs-keyword">if</span> (children) &#123;
      normalizeChildren(cloned, children)
    &#125;
    <span class="hljs-keyword">return</span> cloned
  &#125;
  <span class="hljs-keyword">if</span> (isClassComponent(type)) &#123;
    type = type.__vccOpts
  &#125;
  <span class="hljs-keyword">if</span> (props) &#123;
    props = guardReactiveProps(props)
    <span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">class</span>: klass, style &#125; = props
    <span class="hljs-keyword">if</span> (klass && !isString(klass)) &#123;
      props.class = normalizeClass(klass)
    &#125;
    <span class="hljs-keyword">if</span> (isObject$<span class="hljs-number">1</span>(style)) &#123;
      <span class="hljs-keyword">if</span> (isProxy(style) && !isArray(style)) &#123;
        style = extend(&#123;&#125;, style)
      &#125;
      props.style = normalizeStyle(style)
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> shapeFlag = isString(type)
    ? <span class="hljs-number">1</span> <span class="hljs-comment">/* ELEMENT */</span>
    : isSuspense(type)
      ? <span class="hljs-number">128</span> <span class="hljs-comment">/* SUSPENSE */</span>
      : isTeleport(type)
        ? <span class="hljs-number">64</span> <span class="hljs-comment">/* TELEPORT */</span>
        : isObject$<span class="hljs-number">1</span>(type)
          ? <span class="hljs-number">4</span> <span class="hljs-comment">/* STATEFUL_COMPONENT */</span>
          : isFunction$<span class="hljs-number">1</span>(type)
            ? <span class="hljs-number">2</span> <span class="hljs-comment">/* FUNCTIONAL_COMPONENT */</span>
            : <span class="hljs-number">0</span>
  <span class="hljs-keyword">if</span> ((process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) && shapeFlag & <span class="hljs-number">4</span> <span class="hljs-comment">/* STATEFUL_COMPONENT */</span> && isProxy(type)) &#123;
    type = toRaw(type)
    warn(<span class="hljs-string">`Vue received a Component which was made a reactive object. This can `</span> +
      <span class="hljs-string">`lead to unnecessary performance overhead, and should be avoided by `</span> +
      <span class="hljs-string">`marking the component with `</span>markRaw<span class="hljs-string">` or using `</span>shallowRef<span class="hljs-string">` `</span> +
      <span class="hljs-string">`instead of `</span>ref<span class="hljs-string">`.`</span>, <span class="hljs-string">`\nComponent that was made reactive: `</span>, type)
  &#125;
  <span class="hljs-keyword">return</span> createBaseVNode(type, props, children, patchFlag, dynamicProps, shapeFlag, isBlockNode, <span class="hljs-literal">true</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>createVNode</code> 的实现还是和之前类似，需要执行一堆判断逻辑，最终执行 <code>createBaseVNode</code> 函数创建 <code>vnode</code>，注意这里 <code>createBaseVNode</code> 函数最后一个参数传 <code>true</code>，也就是 <code>needFullChildrenNormalization</code> 为 <code>true</code>，那么在 <code>createBaseVNode</code> 的内部，还需要多执行 <code>normalizeChildren</code> 的逻辑。</p>
<p>组件 <code>vnode</code> 还是通过 <code>createVNode</code> 函数来创建。</p>
<h2 data-id="heading-7">总结</h2>
<p>虽然看上去只是少执行了几行代码，但由于大部分页面都是由很多普通 DOM 元素构成，创建普通元素 <code>vnode</code> 过程的优化，对整体页面的渲染和更新都会有很大的性能提升。</p>
<p>由于存在模板编译的过程，Vue.js 可以利用编译 + 运行时优化，来实现整体的性能优化。比如 <code>Block Tree</code> 的设计，就优化了 diff 过程的性能。</p>
<p>其实对一个框架越了解，你就会越有敬畏之情，Vue.js 在编译、运行时的实现都下了非常大的功夫，处理的细节很多，因此代码的体积也难免变大。而且在框架已经足够成熟，有大量用户使用的背景下还能从内部做这么多的性能优化，并且保证没有 regression bug，实属不易。</p>
<p>开源作品的用户越多，受到的挑战也会越大，需要考虑的细节就会越多，如果一个开源作品都没啥人用，玩具级别，就真的别来碰瓷 Vue 了，根本不是一个段位的。</p></div>  
</div>
            