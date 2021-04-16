
---
title: '手写Vue2.0源码-Mixin混入原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d80ad9361be64258b70c578cb3b14b74~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 00:34:32 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d80ad9361be64258b70c578cb3b14b74~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>此篇主要手写 Vue2.0 源码-<strong>Mixin 混入原理</strong></p>
<p>上一篇咱们主要介绍了 Vue <a href="https://juejin.cn/post/6939704519668432910" target="_blank">异步更新原理 </a> 核心是运用 nextTick 实现异步队列 此篇主要包含 Mixin 混入 这是 Vue 里面非常关键的一个 api 在 Vue 初始化的时候起到了合并选项的重要作用</p>
<p><strong>适用人群：</strong> 没时间去看官方源码或者看源码看的比较懵而不想去看的同学</p>
<hr>
<h3 data-id="heading-1">正文</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.mixin(&#123;
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是全局混入"</span>);
  &#125;,
&#125;);

<span class="hljs-comment">// Vue实例化</span>
<span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">a</span>: &#123; <span class="hljs-attr">a</span>: &#123; <span class="hljs-attr">a</span>: &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">456</span> &#125; &#125; &#125;,
      <span class="hljs-attr">aa</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">bb</span>: <span class="hljs-number">2</span>,
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是自己的"</span>);
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div id="a">hello 这是我自己写的Vue&#123;&#123;name&#125;&#125;
          </div>`</span>,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们在 Vue 里面想要复用一段业务代码逻辑时经常用到的就是混入的方法 但是对于混入的原理 混入的先后顺序以及不同选项的合并策略大家是否都清楚呢 让我们一起来手写一遍就都清楚了</p>
<h4 data-id="heading-2">1.定义全局 Mixin 函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/global-api/mixin.js</span>

<span class="hljs-keyword">import</span> &#123;mergeOptions&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util/index'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  Vue.mixin = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">mixin</span>) </span>&#123;
    <span class="hljs-comment">//   合并对象</span>
      <span class="hljs-built_in">this</span>.options=mergeOptions(<span class="hljs-built_in">this</span>.options,mixin)
  &#125;;
&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 global-api 文件夹 把 mixin 定义为 Vue 的全局方法 核心方法就是利用 mergeOptions 把传入的选项混入到自己的 options 上面</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/index.js</span>
<span class="hljs-keyword">import</span> &#123; initMixin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./init.js"</span>;
<span class="hljs-comment">// Vue就是一个构造函数 通过new关键字进行实例化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-comment">// 这里开始进行Vue初始化工作</span>
  <span class="hljs-built_in">this</span>._init(options);
&#125;
<span class="hljs-comment">// 此做法有利于代码分割</span>
initMixin(Vue);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 Vue 的入口文件里面引入 initMixin 方法</p>
<h4 data-id="heading-3">2.mergeOptions 方法</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/util/index.js</span>
<span class="hljs-comment">// 定义生命周期</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> LIFECYCLE_HOOKS = [
  <span class="hljs-string">"beforeCreate"</span>,
  <span class="hljs-string">"created"</span>,
  <span class="hljs-string">"beforeMount"</span>,
  <span class="hljs-string">"mounted"</span>,
  <span class="hljs-string">"beforeUpdate"</span>,
  <span class="hljs-string">"updated"</span>,
  <span class="hljs-string">"beforeDestroy"</span>,
  <span class="hljs-string">"destroyed"</span>,
];

<span class="hljs-comment">// 合并策略</span>
<span class="hljs-keyword">const</span> strats = &#123;&#125;;

<span class="hljs-comment">//生命周期合并策略</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeHook</span>(<span class="hljs-params">parentVal, childVal</span>) </span>&#123;
  <span class="hljs-comment">// 如果有儿子</span>
  <span class="hljs-keyword">if</span> (childVal) &#123;
    <span class="hljs-keyword">if</span> (parentVal) &#123;
      <span class="hljs-comment">// 合并成一个数组</span>
      <span class="hljs-keyword">return</span> parentVal.concat(childVal);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 包装成一个数组</span>
      <span class="hljs-keyword">return</span> [childVal];
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> parentVal;
  &#125;
&#125;

<span class="hljs-comment">// 为生命周期添加合并策略</span>
LIFECYCLE_HOOKS.forEach(<span class="hljs-function">(<span class="hljs-params">hook</span>) =></span> &#123;
  strats[hook] = mergeHook;
&#125;);

<span class="hljs-comment">// mixin核心方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeOptions</span>(<span class="hljs-params">parent, child</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = &#123;&#125;;
  <span class="hljs-comment">// 遍历父亲</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">in</span> parent) &#123;
    mergeFiled(k);
  &#125;
  <span class="hljs-comment">// 父亲没有 儿子有</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">in</span> child) &#123;
    <span class="hljs-keyword">if</span> (!parent.hasOwnProperty(k)) &#123;
      mergeFiled(k);
    &#125;
  &#125;

  <span class="hljs-comment">//真正合并字段方法</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeFiled</span>(<span class="hljs-params">k</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (strats[k]) &#123;
      options[k] = strats[k](parent[k], child[k]);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 默认策略</span>
      options[k] = child[k] ? child[k] : parent[k];
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> options;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先着重看下 mergeOptions 方法 主要是遍历父亲和儿子的属性 进行合并 如果合并的选项有自己的合并策略 那么就是用相应的合并策略</p>
<p>再来看看 我们这里的生命周期的合并策略 mergeHook 很明显是把全部的生命周期都各自混入成了数组的形式依次调用</p>
<h4 data-id="heading-4">3.生命周期的调用</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/lifecycle.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHook</span>(<span class="hljs-params">vm, hook</span>) </span>&#123;
  <span class="hljs-comment">// 依次执行生命周期对应的方法</span>
  <span class="hljs-keyword">const</span> handlers = vm.$options[hook];
  <span class="hljs-keyword">if</span> (handlers) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < handlers.length; i++) &#123;
      handlers[i].call(vm); <span class="hljs-comment">//生命周期里面的this指向当前实例</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把$options 上面的生命周期依次遍历进行调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/init.js</span>

Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
  <span class="hljs-comment">// 这里的this代表调用_init方法的对象(实例对象)</span>
  <span class="hljs-comment">//  this.$options就是用户new Vue的时候传入的属性和全局的Vue.options合并之后的结果</span>

  vm.$options = mergeOptions(vm.constructor.options, options);
  callHook(vm, <span class="hljs-string">"beforeCreate"</span>); <span class="hljs-comment">//初始化数据之前</span>
  <span class="hljs-comment">// 初始化状态</span>
  initState(vm);
  callHook(vm, <span class="hljs-string">"created"</span>); <span class="hljs-comment">//初始化数据之后</span>
  <span class="hljs-comment">// 如果有el属性 进行模板渲染</span>
  <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
    vm.$mount(vm.$options.el);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 init 初始化的时候调用 mergeOptions 来进行选项合并 之后在需要调用生命周期的地方运用 callHook 来执行用户传入的相关方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/lifecycle.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span>(<span class="hljs-params">vm, el</span>) </span>&#123;
  vm.$el = el;
  <span class="hljs-comment">// 引入watcher的概念 这里注册一个渲染watcher 执行vm._update(vm._render())方法渲染视图</span>
  callHook(vm, <span class="hljs-string">"beforeMount"</span>); <span class="hljs-comment">//初始渲染之前</span>
  <span class="hljs-keyword">let</span> updateComponent = <span class="hljs-function">() =></span> &#123;
    vm._update(vm._render());
  &#125;;
  <span class="hljs-keyword">new</span> Watcher(
    vm,
    updateComponent,
    <span class="hljs-function">() =></span> &#123;
      callHook(vm, <span class="hljs-string">"beforeUpdate"</span>); <span class="hljs-comment">//更新之前</span>
    &#125;,
    <span class="hljs-literal">true</span>
  );
  callHook(vm, <span class="hljs-string">"mounted"</span>); <span class="hljs-comment">//渲染完成之后</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 mountComponent 方法里面调用相关的生命周期 callHook</p>
<h4 data-id="heading-5">4.混入的思维导图</h4>
<p><img alt="Vue2.0源码-mixin原理.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d80ad9361be64258b70c578cb3b14b74~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">小结</h2>
<p>至此 Vue 的混入原型已经手写完毕 其实最核心的就是对象合并以及不同选项的合并策略 目前只是演示了生命周期的合并策略 后续到组件的时候会讲到组件相关的合并策略 大家可以看着思维导图自己动手写一遍核心代码哈 遇到不懂或者有争议的地方欢迎评论留言</p>
<blockquote>
<p>最后如果觉得本文有帮助 记得<strong>点赞三连</strong>哦 十分感谢！</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            