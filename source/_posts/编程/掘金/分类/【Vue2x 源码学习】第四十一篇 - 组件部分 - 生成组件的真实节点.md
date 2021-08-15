
---
title: '【Vue2.x 源码学习】第四十一篇 - 组件部分 - 生成组件的真实节点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/419543ab0e4e411ca9ec251e0e010341~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:55:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/419543ab0e4e411ca9ec251e0e010341~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<hr>
<h2 data-id="heading-0">一，前言</h2>
<p>上篇，介绍了组件部分-组件的生命周期，主要涉及以下几部分：</p>
<p>本篇，组件部分-生成组件的真实节点；</p>
<hr>
<h2 data-id="heading-1">二，生成组件的真实节点</h2>
<h3 data-id="heading-2">1，前文回顾</h3>
<p>前篇，在 createElement 方法中，扩展了对组件的处理 createComponent：生成组件的虚拟节点；</p>
<p>按照模板渲染流程，接下来会进入 patch 方法，其中的 createElm 方法：将虚拟节点转化成为真实节点；</p>
<p>// todo 后续需详细描述相关流程，对 patch 和 createElm 方法进行必要的介绍和说明；</p>
<h3 data-id="heading-3">2，createElm 方法</h3>
<p>在 patch 方法中，createElm 方法会将虚拟节点生成为真实节点：
通过<code>vnode.el = document.createElement(tag)</code>直接创建出真实节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-comment">// vnode.el:绑定真实节点与虚拟节点的映射关系，便于后续的节点更新操作</span>

  <span class="hljs-comment">// 虚拟节点必备的三个：标签，数据，孩子</span>
  <span class="hljs-keyword">let</span> &#123; tag, data, children, text, vm &#125; = vnode;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> tag === <span class="hljs-string">'string'</span>) &#123; <span class="hljs-comment">// 处理元素节点</span>
    <span class="hljs-comment">// 创建真实节点</span>
    vnode.el = <span class="hljs-built_in">document</span>.createElement(tag) 
    updateProperties(vnode, data)  <span class="hljs-comment">// 处理元素的 data 属性</span>
    <span class="hljs-comment">// 处理当前元素节点的儿子：递归创建儿子的真实节点，并添加到对应的父亲中</span>
    children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123; <span class="hljs-comment">// 若不存在儿子，children为空数组</span>
      vnode.el.appendChild(createElm(child))
    &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 文本：文本中 tag 是 undefined</span>
    vnode.el = <span class="hljs-built_in">document</span>.createTextNode(text)  <span class="hljs-comment">// 创建文本的真实节点</span>
  &#125;
  <span class="hljs-keyword">return</span> vnode.el;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在由于组件的加入，createElm 方法中可能会存在 componentOptions：</p>
<p>打印createElm 查看：
第一次：真实节点：id=app
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/419543ab0e4e411ca9ec251e0e010341~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
第二次：组件：my-button
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb9409fc7d8c44edb5d78d22d1ee1cdd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加对组件的处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 创造组件的真实节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(vnode) <span class="hljs-comment">// my-button</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">let</span> &#123; tag, data, children, text, vm &#125; = vnode;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> tag === <span class="hljs-string">'string'</span>) &#123;<span class="hljs-comment">// 元素 or 组件</span>
    <span class="hljs-comment">// 添加对组件的处理</span>
    <span class="hljs-keyword">if</span>(createComponent(vnode))&#123; <span class="hljs-comment">// 将组件的虚拟节点，创建成为组件的真实节点</span>

    &#125;
    <span class="hljs-comment">// 创建真实节点</span>
    vnode.el = <span class="hljs-built_in">document</span>.createElement(tag) 
    updateProperties(vnode, data)
    children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
      vnode.el.appendChild(createElm(child))
    &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 文本</span>
    vnode.el = <span class="hljs-built_in">document</span>.createTextNode(text)
  &#125;
  <span class="hljs-keyword">return</span> vnode.el;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3，组件的初始化 Hook</h3>
<p>之前在组件的 data 属性上，扩展出了生命周期 hook；</p>
<p>在 createComponent 中获取 hook，如果有 hook 说明就是组件；</p>
<p>拿到 hook中的 init 方法，并使用 init 方法处理 vnode：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 创造组件的真实节点
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(vnode);
  <span class="hljs-keyword">let</span> i = vnode.data;
  <span class="hljs-comment">// 先确定有 hook；再拿到 init 方法；</span>
  <span class="hljs-keyword">if</span>((i = i.hook)&&(i = i.init))&#123; <span class="hljs-comment">// 最后 i 为 init 方法</span>
    i(vnode); <span class="hljs-comment">// 使用 init 方法处理 vnode</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">备注：
先将 hook 赋值给 i：看是否有 hook，如果有 hook 就是组件；
再将 hook 中的 init 方法赋值给 i；
最终 i 就是 hook 上的init 方法；
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 hook 上的init 方法处理 vnode，在 hook 中进行中组件的初始化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 创造组件的虚拟节点 componentVnode
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vm, tag, data, children, key, Ctor</span>) </span>&#123;

  <span class="hljs-keyword">if</span>(isObject(Ctor))&#123;
    Ctor = vm.$options._base.extend(Ctor)
  &#125;

  data.hook = &#123;
    <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-comment">// 创建组件的实例并挂载</span>
      <span class="hljs-keyword">let</span> child = <span class="hljs-keyword">new</span> Ctor(&#123;&#125;);
      child.$mount();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">prepatch</span>(<span class="hljs-params"></span>)</span>&#123;&#125;,
    <span class="hljs-function"><span class="hljs-title">postpatch</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
  &#125;
  
  <span class="hljs-keyword">let</span> componentVnode = vnode(vm, tag, data, <span class="hljs-literal">undefined</span>, key, <span class="hljs-literal">undefined</span>, &#123;Ctor, children, tag&#125;);
  <span class="hljs-keyword">return</span> componentVnode;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 new Ctor 时，会执行 _init 进行组件的初始化：
// 调用子类的初始化 _init 方法</p>
<pre><code class="hljs language-js copyable" lang="js">  Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    vm.$options = mergeOptions(vm.constructor.options, options);
    initState(vm);
    <span class="hljs-comment">// 由于 el 不存在，所以不会执行 vm.$mount</span>
    <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
      vm.$mount(vm.$options.el)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>child.$mount();</code>进行挂在，但没有传参 el = null，所以不会挂载：</p>
<pre><code class="hljs language-js copyable" lang="js">  Vue.prototype.$mount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">const</span> opts = vm.$options;
    el = <span class="hljs-built_in">document</span>.querySelector(el); <span class="hljs-comment">// 获取真实的元素</span>
    vm.$el = el;<span class="hljs-comment">// $el：页面上的真实元素</span>

    <span class="hljs-keyword">if</span> (!opts.render) &#123;
      <span class="hljs-keyword">let</span> template = opts.template;
      <span class="hljs-keyword">if</span> (!template) &#123;
        template = el.outerHTML;
      &#125;

      <span class="hljs-keyword">let</span> render = compileToFunction(template);
      opts.render = render;
    &#125;

    mountComponent(vm);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果组件的 render 函数不存在，使用组件的 template 编译为 render函数，并保存起来，之后 mountComponent 进行组件的挂载：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span>(<span class="hljs-params">vm</span>) </span>&#123;

  <span class="hljs-keyword">let</span> updateComponent = <span class="hljs-function">()=></span>&#123;
    vm._update(vm._render());  
  &#125;

  callHook(vm, <span class="hljs-string">'beforeCreate'</span>);
  <span class="hljs-comment">// 生成渲染 watcher ：每个组件都具有独立的渲染 watcher</span>
  <span class="hljs-keyword">new</span> Watcher(vm, updateComponent, <span class="hljs-function">()=></span>&#123;
    callHook(vm, <span class="hljs-string">'created'</span>);
  &#125;,<span class="hljs-literal">true</span>)
   callHook(vm, <span class="hljs-string">'mounted'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>updateComponent 会调用 _render 方法根据子组件创造虚拟节点：</p>
<pre><code class="hljs language-js copyable" lang="js">  Vue.prototype._render = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> &#123; render &#125; = vm.$options;
    <span class="hljs-keyword">let</span> vnode = render.call(vm);
    <span class="hljs-keyword">return</span> vnode
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 render.call 产生虚拟节点，这个 vnode 就是模板的 button</p>
<hr>
<h2 data-id="heading-5">三，结尾</h2>
<p>本篇，介绍了组件部分-生成组件的真实节点;</p>
<p>下篇，待定</p></div>  
</div>
            