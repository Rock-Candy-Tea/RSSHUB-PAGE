
---
title: '【Vue2.x源码学习】第二篇 - Vue 的初始化流程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4bd61bb50554470a182453ad8637e01~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 07:55:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4bd61bb50554470a182453ad8637e01~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">一，前言</h2>
<p>上篇，使用 rollup 完成了 Vue2 源码环境的搭建</p>
<p>本篇，介绍 Vue 的初始化流程</p>
<hr>
<h2 data-id="heading-1">二，Vue 简介</h2>
<p>以两个概念性问题做简单介绍</p>
<h3 data-id="heading-2">1，问题：Vue 是 MVVM 框架吗？</h3>
<p>在 Vue 官网上是这样说的：</p>
<pre><code class="copyable">Vue 是一套用于构建用户界面的渐进式框架，

Vue 并没有完全支持 MVVM 模型，但 Vue 的设计受到了它的启发，

变量名 vm 是 vue model 的缩写，表示 vue 实例
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，严格说 Vue 并不是一个 MVVM 框架</p>
<p>MVVM 模式是仅能够通过视图更改数据，通过数据来更改视图的，</p>
<p>但 Vue 是可以通过 ref 获取 dom 进行操作的</p>
<h3 data-id="heading-3">2，问题：Vue 的双向绑定和单向数据流矛盾吗？</h3>
<pre><code class="copyable">当然不矛盾，这是一个理解问题

双向绑定是指数据变了视图会更新；视图变了会影响数据；

单向数据说的是响应式数据，即数据变化后会更新视图；
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-4">三，使用 Vue</h2>
<h3 data-id="heading-5">1，Vue Demo</h3>
<p>以一个简单的 Vue Demo 为例:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-comment"><!-- 模板 --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">app</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-comment"><!-- 引入 vue --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
    <span class="hljs-comment"><!-- 初始化 Vue，传入 options 对象 --></span>
    let vm = new Vue(&#123;
      el: '#app',
      // 1，data 是对象
      data: &#123;
        message: 'Hello Vue'
      &#125;
      // 2，data 是函数，返回一个对象
      // data() &#123;
      //   return &#123; message: 'Hello Vue' &#125;
      // &#125;
    &#125;);
  </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 初始化时，传入 el 挂载点，data 数据；</p>
<p>初始化完成后，message 成为响应式数据，数据变化更新视图，视图变化影响数据；</p>
<h3 data-id="heading-6">2，问题：响应式数据原理</h3>
<p>Object.defineProperty 数据劫持（这里也正是 vue2 的性能瓶颈）</p>
<h3 data-id="heading-7">3，问题：Vue 中的数据可以是对象吗？</h3>
<p>根组件不会被共享，可以是对象也可以是函数</p>
<p>非根组件必须为函数，否则 data 状态会多组件共享</p>
<hr>
<h2 data-id="heading-8">四，Vue 的初始化操作</h2>
<h3 data-id="heading-9">1，原型方法 _init</h3>
<p>在 Vue 原型上扩展一个 _init 方法（原型方法），用于 Vue 的初始化操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * vue中所有功能都是通过原型扩展方式添加的
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options new Vue时传入的 options 配置对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params">options</span>)</span>&#123;
    <span class="hljs-built_in">this</span>._init(options);<span class="hljs-comment">// 调用Vue原型上_init方法</span>
&#125;

<span class="hljs-comment">// 在Vue原型上扩展一个原型方法_init,进行vue初始化</span>
Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
  
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2，重构：原型方法 _init 模块化处理</h3>
<p>将用于初始化操作的原型方法 _init 单独抽离形成一个独立模块 initMixin</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/init.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(options)
  &#125;
&#125;

<span class="hljs-comment">//------------------------------------------------//</span>
<span class="hljs-comment">// src/index.js</span>
<span class="hljs-keyword">import</span> &#123; initMixin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./init"</span>;<span class="hljs-comment">// 引入initMixin模块</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params">options</span>)</span>&#123;
    <span class="hljs-built_in">this</span>._init(options);<span class="hljs-comment">// 这里调用的是Vue的原型方法</span>
&#125;

<span class="hljs-comment">// 调用 initMixin 进行 Vue 初始化操作</span>
initMixin(Vue)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3，重构后测试</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4bd61bb50554470a182453ad8637e01~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-12">4，原型方法 _init 的 this 指向</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    <span class="hljs-built_in">console</span>.log(vm)<span class="hljs-comment">// this == vm 实例</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印原型方法 _init 的 this，this 指向 vm 实例</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3bff27e2524539a30357ce6e809562~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-13">5，vm.$options</h3>
<p>为了后续让 vue 中的其他方法也能够轻松获取到外部 new Vue 实例化时传入的 options 对象</p>
<p>干脆将 options 选项挂到 vm 实例上，即 vm.$options</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;  <span class="hljs-comment">// this 指向当前 vue 实例</span>
    vm.$options = options; <span class="hljs-comment">// 将 Vue 实例化时用户传入的 options 暴露到 vm 实例上</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-14">6，initState 方法：状态的初始化</h3>
<p>在实际使用中，数据不仅来源于传入的 data，还可能来自 props、watch、computed...</p>
<p>所以，最好能够统一在一个地方，集中进行数据的初始化处理：initState 方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/state.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span>(<span class="hljs-params">vm</span>)</span>&#123;
    <span class="hljs-comment">// 获取options：_init 中已将 options 挂载到 vm.$options</span>
    <span class="hljs-keyword">const</span> opts = vm.$options;

    <span class="hljs-keyword">if</span>(opts.data)&#123;
        initData(vm);<span class="hljs-comment">// data数据的初始化</span>
    &#125;
  <span class="hljs-comment">// props 数据的初始化</span>
    <span class="hljs-comment">// watch 数据的初始化</span>
    <span class="hljs-comment">// computed 数据的初始化</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"进入 state.js - initData，数据初始化操作"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入并使用 initState</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; initState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./state"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    vm.$options = options;

    <span class="hljs-comment">// new Vue 时，传入 options 选项,包含 el 和 data</span>
    initState(vm);  <span class="hljs-comment">// 状态的初始化</span>

    <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"有el,需要挂载"</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c864f43994c642699d135b61fdf982f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-15">五，结尾</h2>
<p>本篇主要介绍了 Vue 数据的初始化流程，核心的几个点：</p>
<ul>
<li>initMixin</li>
<li>vm.$options</li>
<li>initState</li>
</ul>
<p>下一篇，数据劫持：Object.defineProperty</p>
<h2 data-id="heading-16">维护日志</h2>
<ul>
<li>20210605：调整文章的目录结构</li>
</ul></div>  
</div>
            