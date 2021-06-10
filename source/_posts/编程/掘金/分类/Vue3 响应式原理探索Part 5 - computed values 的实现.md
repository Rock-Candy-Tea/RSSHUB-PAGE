
---
title: 'Vue3 响应式原理探索Part 5 - computed values 的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc7048c2be643d59af0ee13db2c5a3f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 22:53:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc7048c2be643d59af0ee13db2c5a3f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<h3 data-id="heading-0">前文摘要</h3>
<p>通过之前的学习，我们已经通过 Proxy + Reflect 搭建出了一个基础的响应式实现，并探索了 ref 的原理和实现。</p>
<ul>
<li><a href="https://juejin.cn/post/6969108748560236575" target="_blank">Vue3 响应式原理探索Part 1 - 20行代码实现响应式</a></li>
<li><a href="https://juejin.cn/post/6969774015544049677" target="_blank">Vue3 响应式原理探索Part 2 - 多重结构的响应式</a></li>
<li><a href="https://juejin.cn/post/6971245771538563102" target="_blank">Vue3 响应式原理探索Part 3 - Proxy + Reflect + activeEffect</a></li>
<li><a href="https://juejin.cn/post/6971609188825432101" target="_blank">Vue3 响应式原理探索Part 4 - ref 的原理和实现</a></li>
</ul>
<p>本文我们将学习 <code>Computed Values</code> 的实现。</p>
<h3 data-id="heading-1">computed 用法</h3>
<p>回到之前 ref 的示例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> param = reactive(&#123; <span class="hljs-attr">width</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">height</span>: <span class="hljs-number">2</span>  &#125;);
<span class="hljs-keyword">let</span> size = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> newWidth = ref(<span class="hljs-number">0</span>);

effect(<span class="hljs-function">() =></span> &#123;
    newWidth.value = param.width * <span class="hljs-number">2</span>;
&#125;);

effect(<span class="hljs-function">() =></span> &#123;
    size = newWidth.value * param.height;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你已经熟悉了 Vue3 的用法，你会更习惯以下简洁的用法。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> param = reactive(&#123; <span class="hljs-attr">width</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">height</span>: <span class="hljs-number">2</span>  &#125;);
        
<span class="hljs-keyword">let</span> newWidth = computed(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> param.width * <span class="hljs-number">2</span>
&#125;);

<span class="hljs-keyword">let</span> size = computed(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> newWidth.value * param.height
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>它相对来说简洁优雅很多，只用 <code>computed</code> 包裹并赋值一次，用到的时候只要取 <code>.value</code> 即可。</p>
<h3 data-id="heading-2">computed 实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span>(<span class="hljs-params">getter</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = ref()  <span class="hljs-comment">// 创建一个新的响应引用</span>

  effect(<span class="hljs-function">() =></span> (result.value = getter())) <span class="hljs-comment">// 在 effect 调用时， 将 getter 的返回值赋值给 result.value ，</span>

  <span class="hljs-keyword">return</span> result <span class="hljs-comment">// 返回引用</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非常简洁。整体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> targetMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">let</span> activeEffect = <span class="hljs-literal">null</span> <span class="hljs-comment">// The active effect running</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">track</span>(<span class="hljs-params">target, key</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!activeEffect) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">let</span> depsMap = targetMap.get(target);
    <span class="hljs-keyword">if</span> (!depsMap) &#123;
        targetMap.set(target, (depsMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()));
    &#125;
    <span class="hljs-keyword">let</span> dep = depsMap.get(key);
    <span class="hljs-keyword">if</span> (!dep) &#123;
        depsMap.set(key, (dep = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()));
    &#125;
    dep.add(activeEffect);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span>(<span class="hljs-params">target, key</span>) </span>&#123;
    <span class="hljs-keyword">const</span> depsMap = targetMap.get(target);
    <span class="hljs-keyword">if</span> (!depsMap) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">let</span> dep = depsMap.get(key);
    <span class="hljs-keyword">if</span> (dep) &#123;
        dep.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
            element();
        &#125;);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-keyword">const</span> handler = &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key, receiver</span>)</span> &#123;
            <span class="hljs-keyword">let</span> result = <span class="hljs-built_in">Reflect</span>.get(target, key, receiver);
            track(target, key);
            <span class="hljs-keyword">return</span> result;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value, receiver</span>)</span> &#123;
            <span class="hljs-keyword">let</span> oldValue = target[key];
            <span class="hljs-keyword">let</span> result = <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver);
            <span class="hljs-keyword">if</span> (result && oldValue != value) &#123;
                trigger(target, key);
            &#125;
            <span class="hljs-keyword">return</span> result;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">raw</span>) </span>&#123;
    <span class="hljs-keyword">const</span> r = &#123;
        <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
            track(r, <span class="hljs-string">'value'</span>)
            <span class="hljs-keyword">return</span> raw
        &#125;,
        <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">newVal</span>) &#123;
            raw = newVal
            trigger(r, <span class="hljs-string">'value'</span>)
        &#125;,
    &#125;
    <span class="hljs-keyword">return</span> r
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span>(<span class="hljs-params">eff</span>) </span>&#123;
    activeEffect = eff  <span class="hljs-comment">// Set this as the activeEffect</span>
    activeEffect()      <span class="hljs-comment">// Run it</span>
    activeEffect = <span class="hljs-literal">null</span> <span class="hljs-comment">// Unset it</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computed</span>(<span class="hljs-params">getter</span>) </span>&#123;
    <span class="hljs-keyword">let</span> result = ref()  <span class="hljs-comment">// Create a new reactive reference</span>

    effect(<span class="hljs-function">() =></span> (result.value = getter())) <span class="hljs-comment">// Set this value equal to the return value of the getter</span>

    <span class="hljs-keyword">return</span> result <span class="hljs-comment">// return the reactive reference</span>
&#125;

<span class="hljs-keyword">let</span> param = reactive(&#123; <span class="hljs-attr">width</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">height</span>: <span class="hljs-number">2</span>  &#125;);

<span class="hljs-keyword">let</span> newWidth = computed(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> param.width * <span class="hljs-number">2</span>
&#125;);

<span class="hljs-keyword">let</span> size = computed(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> newWidth.value * param.height
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再执行如下代码，将会 <code>console</code> 出预期的结果。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`newWidth is <span class="hljs-subst">$&#123;newWidth.value&#125;</span>, size is <span class="hljs-subst">$&#123;size&#125;</span>`</span>); <span class="hljs-comment">// newWidth is 10, size is 20</span>

param.width = <span class="hljs-number">6</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`newWidth is <span class="hljs-subst">$&#123;newWidth.value&#125;</span>, size is <span class="hljs-subst">$&#123;size&#125;</span>`</span>); <span class="hljs-comment">// newWidth is 12, size is 24</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">Vue3 源码小析</h3>
<p>我们已经建立了一个响应式的系统了（嗯，当然是非常弱鸡版本的……）。在 Vue 的真实版本中，是比这个复杂N倍的。我们可以简单列举一下Vue 源码中响应式实现相关的文件。</p>
<p>主要目录在 <a href="https://github.com/vuejs/vue-next/tree/master/packages/reactivity" target="_blank" rel="nofollow noopener noreferrer">github.com/vuejs/vue-n…</a>。</p>
<p>主要结构如下（截止2021年6月10日）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc7048c2be643d59af0ee13db2c5a3f~tplv-k3u1fbpfcp-watermark.image" alt="vue.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有兴趣的同学可以直接阅读源码。</p>
<h3 data-id="heading-4">小结</h3>
<ul>
<li><code>computed</code> 用法更简洁优雅</li>
<li><code>computed</code> 的封装实现基于 <code>ref</code> 及 <code>reactive</code> 函数</li>
</ul></div>  
</div>
            