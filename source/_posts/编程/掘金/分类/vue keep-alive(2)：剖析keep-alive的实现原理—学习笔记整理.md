
---
title: 'vue keep-alive(2)：剖析keep-alive的实现原理—学习笔记整理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db60baeff13e43d3b71eef5f724bf36a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 06:25:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db60baeff13e43d3b71eef5f724bf36a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言：</h2>
<p>​本篇主要内容来自以下文章</p>
<ul>
<li>
<p>彻底揭秘keep-alive原理 <a href="https://github.com/qiudongwei/blog/issues/4" target="_blank" rel="nofollow noopener noreferrer">github.com/qiudongwei/…</a> <strong>（此文的主要来源）</strong></p>
</li>
<li>
<p>Vue源码解析，keep-alive是如何实现缓存的？ <a href="https://juejin.cn/post/6862206197877964807" target="_blank">juejin.cn/post/686220…</a> （<strong>此文的主要来源</strong>）</p>
</li>
<li>
<p>keep-alive实现原理 <a href="https://www.jianshu.com/p/9523bb439950" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/9523bb439…</a></p>
</li>
<li>
<p><a href="http://blog.myweb.kim/vue/keep-alive/?utm-source=origin" target="_blank" rel="nofollow noopener noreferrer">blog.myweb.kim/vue/keep-al…</a> blog.myweb.kim/vue/keep-alive/?utm-source=origin</p>
</li>
<li>
<p>Vue.js 中，7种定义组件模板的方法 <a href="https://zhuanlan.zhihu.com/p/28073723" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/28073723</a></p>
</li>
<li>
<p>对于Vue组件的理解 <a href="https://www.jianshu.com/p/ce97328a9085" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/ce97328a9…</a></p>
</li>
<li>
<p>得物技术浅谈Keep-alive 原理及业务解决方案 <a href="https://zhuanlan.zhihu.com/p/351499525" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/351499525</a></p>
</li>
</ul>
<p>下文是上面这些文章的个人整理与总结，然后加上自己 标注（加粗、加色），以方便记忆。</p>
<p>在搭建 vue 项目时，有某些组件没必要多次渲染，所以需要将组件在内存中进行‘持久化’，此时  便可以派上用场了。  可以使被包含的组件状态维持不变，即便是组件切换了，其内的状态依旧维持在内存之中。</p>
<p>前面整理过《<a href="https://www.zhoulujun.cn/html/webfront/ECMAScript/vue/8236.html" target="_blank" rel="nofollow noopener noreferrer">vue keep-alive(1)：vue router如何保证页面回退页面不刷新？</a>，具体具体用法这里不提，这里来把keep-live 又弯掰直，深入 理解</p>
<h2 data-id="heading-1">keep-alive是什么（基本概念宣讲）</h2>
<p>keep-alive是Vue的内置的一个抽象组件。</p>
<h3 data-id="heading-2">什么是组件</h3>
<p>组件系统是vue的另一个重要概念，它是一种抽象，允许我们使用小型、独立和通常可复用的组件构建大型应用，因此，几乎任意类型的应用界面都可以看成一个组件树：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db60baeff13e43d3b71eef5f724bf36a~tplv-k3u1fbpfcp-zoom-1.image" alt="vue界面与组件" title="vue界面与组件" loading="lazy" referrerpolicy="no-referrer"></p>
<p>组件的作用既可以从父作用域将数据传到子组件，也可以将把组件内部的数据发送到组件外部，可以实现互相传送数据</p>
<h4 data-id="heading-3">7种定义组件模板的方法</h4>
<ol>
<li>
<p>字符串（String）</p>
</li>
<li>
<p>模板字符串（Template literal）</p>
</li>
<li>
<p>X-Templates</p>
</li>
<li>
<p>内联（Inline）</p>
</li>
<li>
<p>Render函数（Render functions）</p>
</li>
<li>
<p>JSX</p>
</li>
<li>
<p>单文件组件（Single page components）</p>
</li>
</ol>
<p>这知识举例，一般都是用单文件组件</p>
<h3 data-id="heading-4">抽象组件</h3>
<p>不会在DOM树中渲染(真实或者虚拟都不会)，不会渲染为一个DOM元素，也不会出现在父组件链中——你永远在 this.$parent 中找不到</p>
<p>它有一个属性 abstract 为 true，表明是它一个抽象组件</p>
<pre><code class="copyable">export default &#123;    name: 'abstractCompDemo',    abstract: true, //标记为抽象组件&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个特性，我就把当react的HOC 高阶组件来用（不知道对不？）</p>
<h4 data-id="heading-5">抽象组件是如何忽略掉父子关系</h4>
<p>Vue组件在初始化阶段会调用 initLifecycle，里面判断父级是否为抽象组件，如果是抽象组件，就选取抽象组件的上一级作为父级，忽略与抽象组件和子组件之间的层级关系。</p>
<pre><code class="copyable">// 源码位置： src/core/instance/lifecycle.js 32行export function initLifecycle (vm: Component) &#123;  const options = vm.$options  // locate first non-abstract parent  let parent = options.parent  if (parent && !options.abstract) &#123;    while (parent.$options.abstract && parent.$parent) &#123;      parent = parent.$parent    &#125;    parent.$children.push(vm)  &#125;  vm.$parent = parent  // ...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 keep-alive 存在多个子元素，<strong>keep-alive 要求同时只有一个子元素被渲染</strong>。</p>
<h5 data-id="heading-6">keep-alive组件怎么跳过生成DOM环节？</h5>
<p>组件实例建立父子关系会根据abstract属性决定是否忽略某个组件。在keep-alive中，设置了abstract: true，那Vue就会跳过该组件实例。</p>
<p>最后构建的组件树中就不会包含keep-alive组件，那么由组件树渲染成的DOM树自然也不会有keep-alive相关的节点了。</p>
<h4 data-id="heading-7">抽象组件代表：</h4>
<p>、、等组件</p>
<p>只需把封装的功能 在组件外面包裹一层就够了，这个用起来还是非常舒服的。比如节流、防抖、拖拽、权限控制等，都可以以这种形式去封装。</p>
<h3 data-id="heading-8">keep-alive组件</h3>
<p>**keep-alive是一个抽象组件，**使用keep-alive包裹动态组件时，<strong>会缓存不活动的组件实例</strong>，而不是销毁它们。</p>
<p>keep-alive不仅仅是能够保存页面/组件的状态这么简单，它还可以避免组件反复创建和渲染，有效提升系统性能。总的来说，keep-alive用于保存组件的渲染状态。</p>
<h4 data-id="heading-9">keep-alive props</h4>
<ul>
<li>
<p><strong>include</strong>定义缓存白名单，keep-alive会缓存命中的组件；</p>
</li>
<li>
<p><strong>exclude</strong>定义缓存黑名单，被命中的组件将不会被缓存；</p>
</li>
<li>
<p><strong>max</strong>定义缓存组件上限，超出上限使用LRU的策略置换缓存数据。</p>
</li>
</ul>
<p>LRU是内存管理的一种页面置换算法。</p>
<h3 data-id="heading-10">LRU缓存策略</h3>
<p><strong>（Least recently used，最近最少使用）缓存策略</strong>：从内存中找出最久未使用的数据置换新的数据.算法根据数据的历史访问记录来进行淘汰数据，其核心思想是<strong>如果数据最近被访问过，那么将来被访问的几率也更高</strong>。</p>
<blockquote>
<p>如果一个数据在最近一段时间没有被访问到，那么在将来它被访问的可能性也很小。也就是说，当限定的空间已存满数据时，应当把最久没有被访问到的数据淘汰。</p>
</blockquote>
<p><strong>keep-alive 缓存机制便是根据LRU策略来设置缓存组件新鲜度，将很久未访问的组件从缓存中删除</strong>。</p>
<h2 data-id="heading-11">keep-alive源码浅析</h2>
<p>keep-alive.js内部还定义了一些工具函数，我们按住不动，先看它对外暴露的对象</p>
<pre><code class="copyable">// src/core/components/keep-alive.jsexport default &#123;  name: 'keep-alive',  abstract: true, // 判断当前组件虚拟dom是否渲染成真实dom的关键  props: &#123;      include: patternTypes, // 缓存白名单      exclude: patternTypes, // 缓存黑名单      max: [String, Number] // 缓存的组件  &#125;,  created() &#123;     this.cache = Object.create(null) // 缓存虚拟dom     this.keys = [] // 缓存的虚拟dom的键集合  &#125;,  destroyed() &#123;    for (const key in this.cache) &#123;       // 删除所有的缓存       pruneCacheEntry(this.cache, key, this.keys)    &#125;  &#125;, mounted() &#123;   // 实时监听黑白名单的变动   this.$watch('include', val => &#123;       pruneCache(this, name => matched(val, name))   &#125;)   this.$watch('exclude', val => &#123;       pruneCache(this, name => !matches(val, name))   &#125;) &#125;, render() &#123;    // 先省略... &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，与我们定义组件的过程一样，先是设置组件名为keep-alive，其次定义了一个abstract属性，值为true。这个属性在vue的官方教程并未提及，却至关重要，后面的渲染过程会用到。</p>
<blockquote>
<p>在组件开头就设置 abstract 为 true，代表该组件是一个抽象组件。抽象组件，只对包裹的子组件做处理，并不会和子组件建立父子关系，也不会作为节点渲染到页面上。</p>
</blockquote>
<p>props属性定义了keep-alive组件支持的全部参数。</p>
<h3 data-id="heading-12">keep-alive在它生命周期内定义了三个钩子函数：</h3>
<h4 data-id="heading-13">created</h4>
<p>初始化两个对象分别缓存VNode(虚拟DOM)和VNode对应的键集合</p>
<h4 data-id="heading-14">destroyed</h4>
<p>删除this.cache中缓存的VNode实例。我们留意到，这不是简单地将this.cache置为null，而是遍历调用pruneCacheEntry函数删除。</p>
<pre><code class="copyable">// src/core/components/keep-alive.js  43行function pruneCacheEntry (  cache: VNodeCache,  key: string,  keys: Array<string>,  current?: VNode) &#123; const cached = cache[key] if (cached && (!current || cached.tag !== current.tag)) &#123;    cached.componentInstance.$destroyed() // 执行组件的destroy钩子函数 &#125; cache[key] = null remove(keys, key)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除缓存的VNode还要对应组件实例的destory钩子函数</p>
<h4 data-id="heading-15">mounted</h4>
<p>在mounted这个钩子中对include和exclude参数进行监听，然后实时地更新（删除）this.cache对象数据。pruneCache函数的核心也是去调用pruneCacheEntry</p>
<h5 data-id="heading-16">pruneCache</h5>
<pre><code class="copyable">function pruneCache (keepAliveInstance: any, filter: Function) &#123;  const &#123; cache, keys, _vnode &#125; = keepAliveInstance  for (const key in cache) &#123;    const cachedNode: ?VNode = cache[key]    if (cachedNode) &#123;      const name: ?string = getComponentName(cachedNode.componentOptions)      if (name && !filter(name)) &#123;        pruneCacheEntry(cache, key, keys, _vnode)      &#125;    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">matches</h5>
<p>判断缓存规则，可以得知include与exclude，值类型可以是 字符串、正则表达式、数组</p>
<pre><code class="copyable">function matches (pattern: string | RegExp | Array<string>, name: string): boolean &#123;  if (Array.isArray(pattern)) &#123;    return pattern.indexOf(name) > -1  &#125; else if (typeof pattern === 'string') &#123;    return pattern.split(',').indexOf(name) > -1  &#125; else if (isRegExp(pattern)) &#123;    return pattern.test(name)  &#125;  return false&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">pruneCacheEntry</h5>
<p>pruneCacheEntry 负责将组件从缓存中删除，它会调用组件 $destroy 方法销毁组件实例，缓存组件置空，并移除对应的 key。</p>
<pre><code class="copyable">function pruneCache (keepAliveInstance: any, filter: Function) &#123;  const &#123; cache, keys, _vnode &#125; = keepAliveInstance  for (const key in cache) &#123;    const cachedNode: ?VNode = cache[key]    if (cachedNode) &#123;      const name: ?string = getComponentName(cachedNode.componentOptions)      if (name && !filter(name)) &#123;        pruneCacheEntry(cache, key, keys, _vnode)      &#125;    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>keep-alive 在 mounted 会监听 include 和 exclude 的变化，属性发生改变时调整缓存和 keys 的顺序，最终调用的也是 pruneCacheEntry。</p>
<h4 data-id="heading-19">render</h4>
<p>render是核心，所以放在最后讲。简要来说**，keep-alive 是由 render 函数决定渲染结果。**</p>
<p>在开头会<strong>获取插槽内的子元素</strong>，调用 getFirstComponentChild 获取到第一个子元素的 VNode——如果 keep-alive 存在多个子元素，keep-alive 要求同时只有一个子元素被渲染。所以在开头会获取插槽内的子元素，调用 getFirstComponentChild 获取到第一个子元素的 VNode。</p>
<p>接着<strong>判断当前组件是否符合缓存条件</strong>，组件名与 include 不匹配或与 exclude 匹配都会直接退出并返回 VNode，不走缓存机制。</p>
<p>匹配条件通过会进入缓存机制的逻辑，如果命中缓存，从 cache 中获取缓存的实例设置到当前的组件上，并调整 key 的位置将其放到最后(LRU 策略)。如果没命中缓存，将当前 VNode 缓存起来，并加入当前组件的 key。如果缓存组件的数量超出 max 的值，即缓存空间不足，则调用 pruneCacheEntry 将最旧的组件从缓存中删除，即 keys[0] 的组件。之后将组件的 keepAlive 标记为 true，表示它是被缓存的组件。</p>
<pre><code class="copyable">render () &#123;  const slot = this.$slots.defalut  const vnode: VNode = getFirstComponentChild(slot) // 找到第一个子组件对象  const componentOptions : ?VNodeComponentOptions = vnode && vnode.componentOptions  if (componentOptions) &#123; // 存在组件参数    // check pattern    const name: ?string = getComponentName(componentOptions) // 组件名    const &#123; include, exclude &#125; = this    if (// 条件匹配，不匹配直接退出      // not included      （include && (!name || !matches(include, name))）||      // excluded        (exclude && name && matches(exclude, name))    ) &#123;        return vnode    &#125;    const &#123; cache, keys &#125; = this    // 定义组件的缓存key    const key: ?string = vnode.key === null ? componentOptions.Ctor.cid + (componentOptions.tag ? `::$&#123;componentOptions.tag&#125;` : '') : vnode.key    if (cache[key]) &#123; // 已经缓存过该组件        vnode.componentInstance = cache[key].componentInstance        remove(keys, key)        keys.push(key) // 调整key排序     &#125; else &#123;        cache[key] = vnode //缓存组件对象        keys.push(key)        if (this.max && keys.length > parseInt(this.max)) &#123;          //超过缓存数限制，将第一个删除          pruneCacheEntry(cahce, keys[0], keys, this._vnode)        &#125;     &#125;     vnode.data.keepAlive = true //渲染和执行被包裹组件的钩子函数需要用到 &#125; return vnode || (slot && slot[0])&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ol>
<li>
<p>获取keep-alive包裹着的第一个子组件对象及其组件名；</p>
</li>
<li>
<p>如果 keep-alive 存在多个子元素，keep-alive 要求同时只有一个子元素被渲染。所以在开头会获取插槽内的子元素，调用 getFirstComponentChild 获取到第一个子元素的 VNode。</p>
</li>
<li>
<p>根据设定的黑白名单（如果有）进行条件匹配，决定是否缓存。不匹配，直接返回组件实例（VNode），否则执行第三步；</p>
</li>
<li>
<p>根据组件ID和tag生成缓存Key，并在缓存对象中查找是否已缓存过该组件实例。如果存在，直接取出缓存值并更新该key在this.keys中的位置（更新key的位置是实现LRU置换策略的关键），否则执行第四步；</p>
</li>
<li>
<p>在this.cache对象中存储该组件实例并保存key值，之后检查缓存的实例数量是否超过max设置值，超过则根据LRU置换策略删除最近最久未使用的实例（即是下标为0的那个key）</p>
</li>
<li>
<p>最后并且很重要，将该组件实例的keepAlive属性值设置为true。</p>
</li>
</ol>
<h2 data-id="heading-20">Vue的渲染过程中keep-live分析</h2>
<p>借助一张图看下Vue渲染的整个过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38a2f2ee5f7b4cdbb55eca17d4621c36~tplv-k3u1fbpfcp-zoom-1.image" alt="张图描述了 Vue 视图渲染的流程.png" title="张图描述了 Vue 视图渲染的流程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>概括来说</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/878c185388974b0585f54614f9dd4d17~tplv-k3u1fbpfcp-zoom-1.image" alt="vue渲染过程图" title="vue渲染过程图" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>VNode构建完成后，最终会被转换成真实dom，而 patch 是必经的过程</strong>。</p>
<p>Vue的渲染是从图中render阶段开始的，<strong>但keep-alive的渲染是在patch阶段，这是构建组件树（虚拟DOM树），并将VNode转换成真正DOM节点的过程</strong>。</p>
<h3 data-id="heading-21">简单描述从render到patch的过程</h3>
<p>我们从最简单的new Vue开始：</p>
<pre><code class="copyable">import App from './App.vue'new Vue(&#123;render: h => h(App)&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>Vue在渲染的时候先调用原型上的_render函数将组件对象转化成一个VNode实例；而_render是通过调用createElement和createEmptyVNode两个函数进行转化；</p>
</li>
<li>
<p>createElement的转化过程会根据不同的情形选择new VNode或者调用createComponent函数做VNode实例化；</p>
</li>
<li>
<p>完成VNode实例化后，这时候Vue调用原型上的_update函数把VNode渲染成真实DOM，这个过程又是通过调用patch函数完成的（这就是patch阶段了）</p>
</li>
</ul>
<p>用一张图表达：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bc21ff3557f4ee4b3dcdd9e6ce4cb51~tplv-k3u1fbpfcp-zoom-1.image" alt="vue渲染过程流程图" title="vue渲染过程流程图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">keep-alive包裹的组件是如何使用缓存的?</h3>
<p>在patch阶段，会执行createComponent函数：</p>
<pre><code class="copyable">// src/core/vdom/patch.js 210行
function createComponent (vnode, insertedVnodeQueue, parentElm, refElm) &#123;  let i = vnode.data  if (isDef(i)) &#123;    // isReactivated 标识组件是否重新激活 isDef =(v)=>v !== undefined && v !== null    const isReactivated = isDef(vnode.componentInstance) && i.keepAlive    if (isDef(i = i.hook) && isDef(i = i.init)) &#123;      i(vnode, false /* hydrating */)    &#125;    // after calling the init hook, if the vnode is a child component    // it should've created a child instance and mounted it. the child    // component also has set the placeholder vnode's elm.    // in that case we can just return the element and be done.    if (isDef(vnode.componentInstance)) &#123;      // initComponent 将 vnode.elm 赋值为真实dom      initComponent(vnode, insertedVnodeQueue)      // insert 将组件的真实dom插入到父元素中。      insert(parentElm, vnode.elm, refElm)      if (isTrue(isReactivated)) &#123;        reactivateComponent(vnode, insertedVnodeQueue, parentElm, refElm)      &#125;      return true    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>在首次加载被包裹组件时，组件还没有初始化构造完成，vnode.componentInstance的值是undefined，keepAlive的值是true。因此isReactivated值为false。因为keep-alive组件作为父组件，它的render函数会先于被包裹组件执行；那么就只执行到i(vnode, false /* hydrating */)，后面的逻辑不再执行；</p>
</li>
<li>
<p>再次访问被包裹组件时，vnode.componentInstance的值就是已经缓存的组件实例，那么会执行insert(parentElm, vnode.elm, refElm)逻辑，这样就直接把上一次的DOM插入到了父元素中。</p>
</li>
</ol>
<h5 data-id="heading-23">init 函数</h5>
<p>init 函数进行组件初始化，它是组件的一个钩子函数：</p>
<pre><code class="copyable">// 源码位置：src/core/vdom/create-component.jsconst componentVNodeHooks = &#123;  init (vnode: VNodeWithData, hydrating: boolean): ?boolean &#123;    if (      vnode.componentInstance &&      !vnode.componentInstance._isDestroyed &&      vnode.data.keepAlive    ) &#123;      // kept-alive components, treat as a patch      const mountedNode: any = vnode // work around flow      componentVNodeHooks.prepatch(mountedNode, mountedNode)    &#125; else &#123;      const child = vnode.componentInstance = createComponentInstanceForVnode(        vnode,        activeInstance      )      child.$mount(hydrating ? vnode.elm : undefined, hydrating)    &#125;  &#125;,  // ...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>createComponentInstanceForVnode 内会 new Vue 构造组件实例并赋值到 componentInstance，随后调用 $mount 挂载组件。</p>
<h5 data-id="heading-24">reactivateComponent</h5>
<pre><code class="copyable">  function reactivateComponent (vnode, insertedVnodeQueue, parentElm, refElm) &#123;    let i    // hack for #4339: a reactivated component with inner transition    // does not trigger because the inner node's created hooks are not called    // again. It's not ideal to involve module-specific logic in here but    // there doesn't seem to be a better way to do it.    let innerNode = vnode    while (innerNode.componentInstance) &#123;      innerNode = innerNode.componentInstance._vnode      if (isDef(i = innerNode.data) && isDef(i = i.transition)) &#123;        for (i = 0; i < cbs.activate.length; ++i) &#123;          cbs.activate[i](emptyNode, innerNode)        &#125;        insertedVnodeQueue.push(innerNode)        break      &#125;    &#125;    // unlike a newly created component,    // a reactivated keep-alive component doesn't insert itself    insert(parentElm, vnode.elm, refElm)  &#125;  function insert (parent, elm, ref) &#123;    if (isDef(parent)) &#123;      if (isDef(ref)) &#123;        if (nodeOps.parentNode(ref) === parent) &#123;          nodeOps.insertBefore(parent, elm, ref)        &#125;      &#125; else &#123;        nodeOps.appendChild(parent, elm)      &#125;    &#125;  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以在初始化渲染中，keep-alive 将A组件缓存起来，然后正常的渲染A组件。</p>
<h3 data-id="heading-25">缓存渲染</h3>
<p>当切换到B组件，再切换回A组件时，A组件命中缓存被重新激活。</p>
<p>再次经历 patch 过程，keep-alive 是根据插槽获取当前的组件，那么插槽的内容又是如何更新实现缓存?</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32754c9ff10f406a8fd9f7eb4b12646e~tplv-k3u1fbpfcp-zoom-1.image" alt="WX20210629-213119@2x.png" title="20210629213212878769093.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">// src/core/vdom/patch.js 714行const isRealElement = isDef(oldVnode.nodeType)if (!isRealElement && sameVnode(oldVnode, vnode)) &#123;  // patch existing root node  patchVnode(oldVnode, vnode, insertedVnodeQueue, null, null, removeOnly)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非初始化渲染时，patch 会调用 patchVnode 对比新旧节点。</p>
<pre><code class="copyable">// 源码位置：src/core/vdom/patch.jsfunction patchVnode (  oldVnode,  vnode,  insertedVnodeQueue,  ownerArray,  index,  removeOnly) &#123;  // ...  let i  const data = vnode.data  if (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) &#123;    i(oldVnode, vnode)  &#125;  // ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>patchVnode 内会调用钩子函数 prepatch。</p>
<pre><code class="copyable">// 源码位置： src/core/vdom/create-component.jsprepatch (oldVnode: MountedComponentVNode, vnode: MountedComponentVNode) &#123;  const options = vnode.componentOptions  const child = vnode.componentInstance = oldVnode.componentInstance  updateChildComponent(    child,    options.propsData, // updated props    options.listeners, // updated listeners    vnode, // new parent vnode    options.children // new children  )&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>updateChildComponent 就是更新的关键方法，它里面主要是更新实例的一些属性：</p>
<pre><code class="copyable">// 源码位置：src/core/instance/lifecycle.jsexport function updateChildComponent (  vm: Component,  propsData: ?Object,  listeners: ?Object,  parentVnode: MountedComponentVNode,  renderChildren: ?Array<VNode>) &#123;  // ...  // Any static slot children from the parent may have changed during parent's  // update. Dynamic scoped slots may also have changed. In such cases, a forced  // update is necessary to ensure correctness.  const needsForceUpdate = !!(    renderChildren ||               // has new static slots    vm.$options._renderChildren ||  // has old static slots    hasDynamicScopedSlot  )    // ...    // resolve slots + force update if has children  if (needsForceUpdate) &#123;    vm.$slots = resolveSlots(renderChildren, parentVnode.context)    vm.$forceUpdate()  &#125;&#125;Vue.prototype.$forceUpdate = function () &#123;  const vm: Component = this  if (vm._watcher) &#123;    // 这里最终会执行 vm._update(vm._render)    vm._watcher.update()  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从注释中可以看到 needsForceUpdate 是有插槽才会为 true，keep-alive 符合条件。首先调用 resolveSlots 更新 keep-alive 的插槽，然后调用 $forceUpdate 让 keep-alive 重新渲染，再走一遍 render。因为A组件在初始化已经缓存了，keep-alive 直接返回缓存好的A组件 VNode。VNode 准备好后，又来到了 patch 阶段。</p>
<pre><code class="copyable">function createComponent (vnode, insertedVnodeQueue, parentElm, refElm) &#123;  let i = vnode.data  if (isDef(i)) &#123;    const isReactivated = isDef(vnode.componentInstance) && i.keepAlive    if (isDef(i = i.hook) && isDef(i = i.init)) &#123;      i(vnode, false /* hydrating */)    &#125;    // after calling the init hook, if the vnode is a child component    // it should've created a child instance and mounted it. the child    // component also has set the placeholder vnode's elm.    // in that case we can just return the element and be done.    if (isDef(vnode.componentInstance)) &#123;      initComponent(vnode, insertedVnodeQueue)      insert(parentElm, vnode.elm, refElm)      if (isTrue(isReactivated)) &#123;        reactivateComponent(vnode, insertedVnodeQueue, parentElm, refElm)      &#125;      return true    &#125;  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>A组件再次经历 createComponent 的过程，调用 init。</p>
<pre><code class="copyable">const componentVNodeHooks = &#123;  init (vnode: VNodeWithData, hydrating: boolean): ?boolean &#123;    if (      vnode.componentInstance &&      !vnode.componentInstance._isDestroyed &&      vnode.data.keepAlive    ) &#123;      // kept-alive components, treat as a patch      const mountedNode: any = vnode // work around flow      componentVNodeHooks.prepatch(mountedNode, mountedNode)    &#125; else &#123;      const child = vnode.componentInstance = createComponentInstanceForVnode(        vnode,        activeInstance      )      child.$mount(hydrating ? vnode.elm : undefined, hydrating)    &#125;  &#125;,&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时将不再走 $mount 的逻辑，只调用 prepatch 更新实例属性。所以在缓存组件被激活时，不会执行 created 和 mounted 的生命周期函数。</p>
<p>回到 createComponent，此时的 isReactivated 为 true，调用 reactivateComponent:</p>
<pre><code class="copyable">function reactivateComponent (vnode, insertedVnodeQueue, parentElm, refElm) &#123;  let i  // hack for #4339: a reactivated component with inner transition  // does not trigger because the inner node's created hooks are not called  // again. It's not ideal to involve module-specific logic in here but  // there doesn't seem to be a better way to do it.  let innerNode = vnode  while (innerNode.componentInstance) &#123;    innerNode = innerNode.componentInstance._vnode    if (isDef(i = innerNode.data) && isDef(i = i.transition)) &#123;      for (i = 0; i < cbs.activate.length; ++i) &#123;        cbs.activate[i](emptyNode, innerNode)      &#125;      insertedVnodeQueue.push(innerNode)      break    &#125;  &#125;  // unlike a newly created component,  // a reactivated keep-alive component doesn't insert itself  insert(parentElm, vnode.elm, refElm)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后调用 insert 插入组件的dom节点，至此缓存渲染流程完成。</p>
<h3 data-id="heading-26">keep-live钩子函数</h3>
<p>一般的组件，每一次加载都会有完整的生命周期，即生命周期里面对应的钩子函数都会被触发，为什么被keep-alive包裹的组件却不是呢？</p>
<h4 data-id="heading-27">只执行一次钩子函数</h4>
<p>一般的组件，每一次加载都会有完整的生命周期，即生命周期里面对应的钩子函数都会被触发，为什么被keep-alive包裹的组件却不是呢？</p>
<p>因为被缓存的组件实例会为其设置keepAlive = true，而在初始化组件钩子函数中：</p>
<pre><code class="copyable">// src/core/vdom/create-component.jsconst componentVNodeHooks = &#123;  init (vnode: VNodeWithData, hydrating: boolean): ?boolean &#123;    if (      vnode.componentInstance &&      !vnode.componentInstance._isDestroyed &&      vnode.data.keepAlive    ) &#123;      // kept-alive components, treat as a patch      const mountedNode: any = vnode // work around flow      componentVNodeHooks.prepatch(mountedNode, mountedNode)    &#125; else &#123;      const child = vnode.componentInstance = createComponentInstanceForVnode(        vnode,        activeInstance      )      child.$mount(hydrating ? vnode.elm : undefined, hydrating)    &#125;  &#125;  // ...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，当vnode.componentInstance和keepAlive同时为truly值时，不再进入$mount过程，那mounted之前的所有钩子函数（beforeCreate、created、mounted）都不再执行。</p>
<h4 data-id="heading-28">可重复的activated</h4>
<p>在patch的阶段，最后会执行invokeInsertHook函数，而这个函数就是去调用组件实例（VNode）自身的insert钩子：</p>
<pre><code class="copyable">// src/core/vdom/patch.js  function invokeInsertHook (vnode, queue, initial) &#123;    if (isTrue(initial) && isDef(vnode.parent)) &#123;      vnode.parent.data.pendingInsert = queue    &#125; else &#123;      for (let i = 0; i < queue.length; ++i) &#123;        queue[i].data.hook.insert(queue[i])  // 调用VNode自身的insert钩子函数      &#125;    &#125;  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看insert钩子：</p>
<pre><code class="copyable">// src/core/vdom/create-component.jsconst componentVNodeHooks = &#123;  // init()  insert (vnode: MountedComponentVNode) &#123;    const &#123; context, componentInstance &#125; = vnode    if (!componentInstance._isMounted) &#123;      componentInstance._isMounted = true      callHook(componentInstance, 'mounted')    &#125;    if (vnode.data.keepAlive) &#123;      if (context._isMounted) &#123;        queueActivatedComponent(componentInstance)      &#125; else &#123;        activateChildComponent(componentInstance, true /* direct */)      &#125;    &#125;  // ...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个钩子里面，调用了activateChildComponent函数递归地去执行所有子组件的activated钩子函数：</p>
<pre><code class="copyable">// src/core/instance/lifecycle.jsexport function activateChildComponent (vm: Component, direct?: boolean) &#123;  if (direct) &#123;    vm._directInactive = false    if (isInInactiveTree(vm)) &#123;      return    &#125;  &#125; else if (vm._directInactive) &#123;    return  &#125;  if (vm._inactive || vm._inactive === null) &#123;    vm._inactive = false    for (let i = 0; i < vm.$children.length; i++) &#123;      activateChildComponent(vm.$children[i])    &#125;    callHook(vm, 'activated')  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相反地，deactivated钩子函数也是一样的原理，在组件实例（VNode）的destroy钩子函数中调用deactivateChildComponent函数。</p>
<p>​</p></div>  
</div>
            