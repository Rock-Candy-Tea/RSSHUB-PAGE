
---
title: '手写Vue2.0源码（九）-侦听属性原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61fa92688a1e4ed2b000d362939a1133~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 19:05:32 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61fa92688a1e4ed2b000d362939a1133~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>此篇主要手写 Vue2.0 源码-<strong>侦听属性</strong></p>
<p>上一篇咱们主要介绍了 Vue <a href="https://juejin.cn/post/6954173708344770591" target="_blank">组件原理</a> 深入了解了 Vue 组件化开发的特色 此篇将介绍我们日常业务开发使用非常多的侦听属性的原理</p>
<p><strong>适用人群：</strong></p>
<p>1.想要深入理解 vue 源码更好的进行日常业务开发</p>
<p>2.想要在简历写上精通 vue 框架源码（再也不怕面试官的连环夺命问 哈哈）</p>
<p>3.没时间去看官方源码或者初看源码觉得难以理解的同学</p>
<hr>
<h3 data-id="heading-1">正文</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Vue实例化</span>
  <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">aa</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">bb</span>: <span class="hljs-number">2</span>,
      &#125;;
    &#125;,
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div id="a">hello 这是我自己写的Vue&#123;&#123;name&#125;&#125;</div>`</span>,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">doSomething</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
    &#125;,
    <span class="hljs-attr">watch</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">aa</span>(<span class="hljs-params">newVal, oldVal</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(newVal);
      &#125;,
      <span class="hljs-comment">// aa: &#123;</span>
      <span class="hljs-comment">//   handle(newVal， oldVal) &#123;</span>
      <span class="hljs-comment">//     console.log(newVal);</span>
      <span class="hljs-comment">//   &#125;,</span>
      <span class="hljs-comment">//   deep: true</span>
      <span class="hljs-comment">// &#125;,</span>
      <span class="hljs-comment">// aa: 'doSomething',</span>
      <span class="hljs-comment">// aa: [&#123;</span>
      <span class="hljs-comment">//   handle(newVal， oldVal) &#123;</span>
      <span class="hljs-comment">//     console.log(newVal);</span>
      <span class="hljs-comment">//   &#125;,</span>
      <span class="hljs-comment">//   deep: true</span>
      <span class="hljs-comment">// &#125;]</span>
    &#125;,
  &#125;);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    vm.aa = <span class="hljs-number">1111</span>;
  &#125;, <span class="hljs-number">1000</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>侦听属性的写法很多 可以写成 字符串 函数 数组 以及对象 对于对象的写法自己可以增加一些 options 用来增强功能 侦听属性的特点是监听的值发生了变化之后可以执行用户传入的自定义方法</p>
<h4 data-id="heading-2">1.侦听属性的初始化</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/state.js</span>

<span class="hljs-comment">// 统一初始化数据的方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-comment">// 获取传入的数据对象</span>
  <span class="hljs-keyword">const</span> opts = vm.$options;
  <span class="hljs-keyword">if</span> (opts.watch) &#123;
    <span class="hljs-comment">//侦听属性初始化</span>
    initWatch(vm);
  &#125;
&#125;

<span class="hljs-comment">// 初始化watch</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initWatch</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-keyword">let</span> watch = vm.$options.watch;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">in</span> watch) &#123;
    <span class="hljs-keyword">const</span> handler = watch[k]; <span class="hljs-comment">//用户自定义watch的写法可能是数组 对象 函数 字符串</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(handler)) &#123;
      <span class="hljs-comment">// 如果是数组就遍历进行创建</span>
      handler.forEach(<span class="hljs-function">(<span class="hljs-params">handle</span>) =></span> &#123;
        createWatcher(vm, k, handle);
      &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
      createWatcher(vm, k, handler);
    &#125;
  &#125;
&#125;
<span class="hljs-comment">// 创建watcher的核心</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createWatcher</span>(<span class="hljs-params">vm, exprOrFn, handler, options = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> handler === <span class="hljs-string">"object"</span>) &#123;
    options = handler; <span class="hljs-comment">//保存用户传入的对象</span>
    handler = handler.handler; <span class="hljs-comment">//这个代表真正用户传入的函数</span>
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> handler === <span class="hljs-string">"string"</span>) &#123;
    <span class="hljs-comment">//   代表传入的是定义好的methods方法</span>
    handler = vm[handler];
  &#125;
  <span class="hljs-comment">//   调用vm.$watch创建用户watcher</span>
  <span class="hljs-keyword">return</span> vm.$watch(exprOrFn, handler, options);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>initWatch初始化Watch对数组进行处理  createWatcher处理Watch的兼容性写法 包含字符串 函数 数组 以及对象 最后调用$watch 传入处理好的参数进行创建用户Watcher</p>
<h4 data-id="heading-3">2.$watch</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//  src/state.js</span>
<span class="hljs-keyword">import</span> Watcher <span class="hljs-keyword">from</span> <span class="hljs-string">"./observer/watcher"</span>;
Vue.prototype.$watch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">exprOrFn, cb, options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
  <span class="hljs-comment">//  user: true 这里表示是一个用户watcher</span>
  <span class="hljs-keyword">let</span> watcher = <span class="hljs-keyword">new</span> Watcher(vm, exprOrFn, cb, &#123; ...options, <span class="hljs-attr">user</span>: <span class="hljs-literal">true</span> &#125;);
  <span class="hljs-comment">// 如果有immediate属性 代表需要立即执行回调</span>
  <span class="hljs-keyword">if</span> (options.immediate) &#123;
    cb(); <span class="hljs-comment">//如果立刻执行</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型方法$watch 就是创建自定义 watch 的核心方法 把用户定义的 options 和 user:true 传给构造函数 Watcher</p>
<h4 data-id="heading-4">3.Watcher 改造</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/observer/watcher.js</span>

<span class="hljs-keyword">import</span> &#123; isObject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../util/index"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, exprOrFn, cb, options</span>)</span> &#123;
    <span class="hljs-comment">// this.vm = vm;</span>
    <span class="hljs-comment">// this.exprOrFn = exprOrFn;</span>
    <span class="hljs-comment">// this.cb = cb; //回调函数 比如在watcher更新之前可以执行beforeUpdate方法</span>
    <span class="hljs-comment">// this.options = options; //额外的选项 true代表渲染watcher</span>
    <span class="hljs-comment">// this.id = id++; // watcher的唯一标识</span>
    <span class="hljs-comment">// this.deps = []; //存放dep的容器</span>
    <span class="hljs-comment">// this.depsId = new Set(); //用来去重dep</span>

    <span class="hljs-built_in">this</span>.user = options.user; <span class="hljs-comment">//标识用户watcher</span>

    <span class="hljs-comment">// 如果表达式是一个函数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> exprOrFn === <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-built_in">this</span>.getter = exprOrFn;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.getter = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//用户watcher传过来的可能是一个字符串   类似a.a.a.a.b</span>
        <span class="hljs-keyword">let</span> path = exprOrFn.split(<span class="hljs-string">"."</span>);
        <span class="hljs-keyword">let</span> obj = vm;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < path.length; i++) &#123;
          obj = obj[path[i]]; <span class="hljs-comment">//vm.a.a.a.a.b</span>
        &#125;
        <span class="hljs-keyword">return</span> obj;
      &#125;;
    &#125;
    <span class="hljs-comment">// 实例化就进行一次取值操作 进行依赖收集过程</span>
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.get();
  &#125;
  <span class="hljs-comment">//   get() &#123;</span>
  <span class="hljs-comment">//     pushTarget(this); // 在调用方法之前先把当前watcher实例推到全局Dep.target上</span>
  <span class="hljs-comment">//     const res = this.getter.call(this.vm); //如果watcher是渲染watcher 那么就相当于执行  vm._update(vm._render()) 这个方法在render函数执行的时候会取值 从而实现依赖收集</span>
  <span class="hljs-comment">//     popTarget(); // 在调用方法之后把当前watcher实例从全局Dep.target移除</span>
  <span class="hljs-comment">//     return res;</span>
  <span class="hljs-comment">//   &#125;</span>
  <span class="hljs-comment">//   把dep放到deps里面 同时保证同一个dep只被保存到watcher一次  同样的  同一个watcher也只会保存在dep一次</span>
  <span class="hljs-comment">//   addDep(dep) &#123;</span>
  <span class="hljs-comment">//     let id = dep.id;</span>
  <span class="hljs-comment">//     if (!this.depsId.has(id)) &#123;</span>
  <span class="hljs-comment">//       this.depsId.add(id);</span>
  <span class="hljs-comment">//       this.deps.push(dep);</span>
  <span class="hljs-comment">//       //   直接调用dep的addSub方法  把自己--watcher实例添加到dep的subs容器里面</span>
  <span class="hljs-comment">//       dep.addSub(this);</span>
  <span class="hljs-comment">//     &#125;</span>
  <span class="hljs-comment">//   &#125;</span>
  <span class="hljs-comment">//   这里简单的就执行以下get方法  之后涉及到计算属性就不一样了</span>
  <span class="hljs-comment">//   update() &#123;</span>
  <span class="hljs-comment">//     // 计算属性依赖的值发生变化 只需要把dirty置为true  下次访问到了重新计算</span>
  <span class="hljs-comment">//     if (this.lazy) &#123;</span>
  <span class="hljs-comment">//       this.dirty = true;</span>
  <span class="hljs-comment">//     &#125;else&#123;</span>
  <span class="hljs-comment">//       // 每次watcher进行更新的时候  可以让他们先缓存起来  之后再一起调用</span>
  <span class="hljs-comment">//       // 异步队列机制</span>
  <span class="hljs-comment">//       queueWatcher(this);</span>
  <span class="hljs-comment">//     &#125;</span>
  <span class="hljs-comment">//   &#125;</span>
  <span class="hljs-comment">//   depend()&#123;</span>
  <span class="hljs-comment">//     // 计算属性的watcher存储了依赖项的dep</span>
  <span class="hljs-comment">//     let i=this.deps.length</span>
  <span class="hljs-comment">//     while(i--)&#123;</span>
  <span class="hljs-comment">//       this.deps[i].depend() //调用依赖项的dep去收集渲染watcher</span>
  <span class="hljs-comment">//     &#125;</span>
  <span class="hljs-comment">//   &#125;</span>
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> newVal = <span class="hljs-built_in">this</span>.get(); <span class="hljs-comment">//新值</span>
    <span class="hljs-keyword">const</span> oldVal = <span class="hljs-built_in">this</span>.value; <span class="hljs-comment">//老值</span>
    <span class="hljs-built_in">this</span>.value = newVal; <span class="hljs-comment">//现在的新值将成为下一次变化的老值</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
      <span class="hljs-comment">// 如果两次的值不相同  或者值是引用类型 因为引用类型新老值是相等的 他们是指向同一引用地址</span>
      <span class="hljs-keyword">if</span> (newVal !== oldVal || isObject(newVal)) &#123;
        <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, newVal, oldVal);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 渲染watcher</span>
      <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要改造有两点</p>
<p>1.实例化的时候为了兼容用户 watch 的写法 会将传入的字符串写法转成 Vue 实例对应的值 并且调用 get 方法获取并保存一次旧值</p>
<p>2.run 方法判断如果是用户 watch 那么执行用户传入的回调函数 cb 并且把新值和旧值作为参数传入进去</p>
<h4 data-id="heading-5">4.侦听属性的思维导图</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61fa92688a1e4ed2b000d362939a1133~tplv-k3u1fbpfcp-watermark.image" alt="Vue2.0源码-侦听属性.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">小结</h2>
<p>至此 Vue 的 侦听属性原理已经完结 此篇相较之前的原理来说比较容易 其实计算属性和侦听属性全都是借助 Watcher 进行实现的 不清楚整个 Watcher 实现的可以看看小编这篇<a href="https://juejin.cn/post/6938221715281575973" target="_blank">手写 Vue2.0 源码（四）-渲染更新原理</a> 下一篇是计算属性原理 会和侦听属性进行对比 大家可以看着思维导图自己动手写一遍核心代码哈 遇到不懂或者有争议的地方欢迎评论留言</p>
<blockquote>
<p>最后如果觉得本文有帮助 记得<strong>点赞三连</strong>哦 十分感谢！</p>
</blockquote>
<h2 data-id="heading-7">系列链接（后续都会更新完毕）</h2>
<ul>
<li><a href="https://juejin.cn/post/6935344605424517128" target="_blank">手写 Vue2.0 源码（一）-响应式数据原理</a></li>
<li><a href="https://juejin.cn/post/6936024530016010276" target="_blank">手写 Vue2.0 源码（二）-模板编译原理</a></li>
<li><a href="https://juejin.cn/post/6937120983765483528" target="_blank">手写 Vue2.0 源码（三）-初始渲染原理</a></li>
<li><a href="https://juejin.cn/post/6938221715281575973" target="_blank">手写 Vue2.0 源码（四）-渲染更新原理</a></li>
<li><a href="https://juejin.cn/post/6939704519668432910" target="_blank">手写 Vue2.0 源码（五）-异步更新原理 </a></li>
<li><a href="https://juejin.cn/post/6953433215218483236" target="_blank">手写 Vue2.0 源码（六）-diff 算法原理</a></li>
<li><a href="https://juejin.cn/post/6951671158198501383" target="_blank">手写 Vue2.0 源码（七）-Mixin 混入原理</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591" target="_blank">手写 Vue2.0 源码（八）-组件原理</a></li>
<li><a href="https://juejin.cn/post/6954925963226382367">手写 Vue2.0 源码（九）-侦听属性原理</a></li>
<li><a href="https://juejin.cn/post/6954925963226382367">手写 Vue2.0 源码（十）-全局 api 分析</a></li>
<li><a href="https://juejin.cn/post/6954925963226382367">vue 面试真题-深入源码解析</a></li>
<li><a href="https://juejin.cn/post/6954925963226382367">手写 vue-router 源码</a></li>
<li><a href="https://juejin.cn/post/6954925963226382367">手写 vuex 源码</a></li>
<li><a href="https://juejin.cn/post/6954925963226382367">手写 vue3.0 源码</a></li>
</ul></div>  
</div>
            