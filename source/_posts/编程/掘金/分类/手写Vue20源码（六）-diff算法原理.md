
---
title: '手写Vue2.0源码（六）-diff算法原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a856bf3d3fa49698f70122bc0c09ab3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 18:33:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a856bf3d3fa49698f70122bc0c09ab3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>此篇主要手写 Vue2.0 源码-<strong>diff 算法原理</strong></p>
<p>上一篇咱们主要介绍了 Vue <a href="https://juejin.cn/post/6939704519668432910" target="_blank">异步更新原理</a> 是对视图更新的性能优化 此篇同样是对渲染更新的优化 当模板发生变化之后 我们可以利用 diff 算法 对比新老虚拟 dom 看是否能进行节点复用 diff 算法也是 vue 面试比较热门的考点哈</p>
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
        <span class="hljs-attr">a</span>: <span class="hljs-number">123</span>,
      &#125;;
    &#125;,
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div id="a">hello &#123;&#123;a&#125;&#125;</div>`</span>,
  &#125;);

  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    vm.a = <span class="hljs-number">1</span>;
  &#125;, <span class="hljs-number">1000</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家思考一下 如果我们当初始渲染完成 1 秒后改变了一下模板里面 a 的值 vue 会怎么处理来显示最新的值呢?</p>
<p>1.把上次渲染的真实 dom 删除 然后重新渲染一个新的 dom 节点来应用最新的 a 的值</p>
<p>2.把老的 dom 进行复用 改变一下内部文本节点的 textContent 的值</p>
<blockquote>
<p>这两种方案 很明显后者的性能开销更小 一起来看看 vue 怎么使用 diff 算法来进行渲染更新的吧</p>
</blockquote>
<h4 data-id="heading-2">1.patch 核心渲染方法改写</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/vdom/patch.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> isRealElement = oldVnode.nodeType;
  <span class="hljs-keyword">if</span> (isRealElement) &#123;
    <span class="hljs-comment">// oldVnode是真实dom元素 就代表初次渲染</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// oldVnode是虚拟dom 就是更新过程 使用diff算法</span>
    <span class="hljs-keyword">if</span> (oldVnode.tag !== vnode.tag) &#123;
      <span class="hljs-comment">// 如果新旧标签不一致 用新的替换旧的 oldVnode.el代表的是真实dom节点--同级比较</span>
      oldVnode.el.parentNode.replaceChild(createElm(vnode), oldVnode.el);
    &#125;
    <span class="hljs-comment">// 如果旧节点是一个文本节点</span>
    <span class="hljs-keyword">if</span> (!oldVnode.tag) &#123;
      <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
        oldVnode.el.textContent = vnode.text;
      &#125;
    &#125;
    <span class="hljs-comment">// 不符合上面两种 代表标签一致 并且不是文本节点</span>
    <span class="hljs-comment">// 为了节点复用 所以直接把旧的虚拟dom对应的真实dom赋值给新的虚拟dom的el属性</span>
    <span class="hljs-keyword">const</span> el = (vnode.el = oldVnode.el);
    updateProperties(vnode, oldVnode.data); <span class="hljs-comment">// 更新属性</span>
    <span class="hljs-keyword">const</span> oldCh = oldVnode.children || []; <span class="hljs-comment">// 老的儿子</span>
    <span class="hljs-keyword">const</span> newCh = vnode.children || []; <span class="hljs-comment">// 新的儿子</span>
    <span class="hljs-keyword">if</span> (oldCh.length > <span class="hljs-number">0</span> && newCh.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 新老都存在子节点</span>
      updateChildren(el, oldCh, newCh);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldCh.length) &#123;
      <span class="hljs-comment">// 老的有儿子新的没有</span>
      el.innerHTML = <span class="hljs-string">""</span>;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newCh.length) &#123;
      <span class="hljs-comment">// 新的有儿子</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < newCh.length; i++) &#123;
        <span class="hljs-keyword">const</span> child = newCh[i];
        el.appendChild(createElm(child));
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们直接看 else 分支 代表的是渲染更新过程 可以分为以下几步</p>
<p>1.diff 只进行同级比较
<img alt="diff同级对比.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a856bf3d3fa49698f70122bc0c09ab3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2.根据新老 vnode 子节点不同情况分别处理
<img alt="diff流程.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90304a24ceab464abe2eafcef9490091~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">2.updateProperties 更新属性</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//  src/vdom/patch.js</span>

<span class="hljs-comment">// 解析vnode的data属性 映射到真实dom上</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateProperties</span>(<span class="hljs-params">vnode, oldProps = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> newProps = vnode.data || &#123;&#125;; <span class="hljs-comment">//新的vnode的属性</span>
  <span class="hljs-keyword">const</span> el = vnode.el; <span class="hljs-comment">// 真实节点</span>
  <span class="hljs-comment">// 如果新的节点没有 需要把老的节点属性移除</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> k <span class="hljs-keyword">in</span> oldProps) &#123;
    <span class="hljs-keyword">if</span> (!newProps[k]) &#123;
      el.removeAttribute(k);
    &#125;
  &#125;
  <span class="hljs-comment">// 对style样式做特殊处理 如果新的没有 需要把老的style值置为空</span>
  <span class="hljs-keyword">const</span> newStyle = newProps.style || &#123;&#125;;
  <span class="hljs-keyword">const</span> oldStyle = oldProps.style || &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> oldStyle) &#123;
    <span class="hljs-keyword">if</span> (!newStyle[key]) &#123;
      el.style[key] = <span class="hljs-string">""</span>;
    &#125;
  &#125;
  <span class="hljs-comment">// 遍历新的属性 进行增加操作</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> newProps) &#123;
    <span class="hljs-keyword">if</span> (key === <span class="hljs-string">"style"</span>) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> styleName <span class="hljs-keyword">in</span> newProps.style) &#123;
        el.style[styleName] = newProps.style[styleName];
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key === <span class="hljs-string">"class"</span>) &#123;
      el.className = newProps.class;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 给这个元素添加属性 值就是对应的值</span>
      el.setAttribute(key, newProps[key]);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比新老 vnode 进行属性更新</p>
<h4 data-id="heading-4">3.updateChildren 更新子节点-diff 核心方法</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/vdom/patch.js</span>

<span class="hljs-comment">// 判断两个vnode的标签和key是否相同 如果相同 就可以认为是同一节点就地复用</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isSameVnode</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-keyword">return</span> oldVnode.tag === newVnode.tag && oldVnode.key === newVnode.key;
&#125;
<span class="hljs-comment">// diff算法核心 采用双指针的方式 对比新老vnode的儿子节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parent, oldCh, newCh</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldStartIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">//老儿子的起始下标</span>
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]; <span class="hljs-comment">//老儿子的第一个节点</span>
  <span class="hljs-keyword">let</span> oldEndIndex = oldCh.length - <span class="hljs-number">1</span>; <span class="hljs-comment">//老儿子的结束下标</span>
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIndex]; <span class="hljs-comment">//老儿子的起结束节点</span>

  <span class="hljs-keyword">let</span> newStartIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">//同上  新儿子的</span>
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">let</span> newEndIndex = newCh.length - <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIndex];

  <span class="hljs-comment">// 根据key来创建老的儿子的index映射表  类似 &#123;'a':0,'b':1&#125; 代表key为'a'的节点在第一个位置 key为'b'的节点在第二个位置</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeIndexByKey</span>(<span class="hljs-params">children</span>) </span>&#123;
    <span class="hljs-keyword">let</span> map = &#123;&#125;;
    children.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
      map[item.key] = index;
    &#125;);
    <span class="hljs-keyword">return</span> map;
  &#125;
  <span class="hljs-comment">// 生成的映射表</span>
  <span class="hljs-keyword">let</span> map = makeIndexByKey(oldCh);

  <span class="hljs-comment">// 只有当新老儿子的双指标的起始位置不大于结束位置的时候  才能循环 一方停止了就需要结束循环</span>
  <span class="hljs-keyword">while</span> (oldStartIndex <= oldEndIndex && newStartIndex <= newEndIndex) &#123;
    <span class="hljs-comment">// 因为暴力对比过程把移动的vnode置为 undefined 如果不存在vnode节点 直接跳过</span>
    <span class="hljs-keyword">if</span> (!oldStartVnode) &#123;
      oldStartVnode = oldCh[++oldStartIndex];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!oldEndVnode) &#123;
      oldEndVnode = oldCh[--oldEndIndex];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isSameVnode(oldStartVnode, newStartVnode)) &#123;
      <span class="hljs-comment">// 头和头对比 依次向后追加</span>
      patch(oldStartVnode, newStartVnode); <span class="hljs-comment">//递归比较儿子以及他们的子节点</span>
      oldStartVnode = oldCh[++oldStartIndex];
      newStartVnode = newCh[++newStartIndex];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isSameVnode(oldEndVnode, newEndVnode)) &#123;
      <span class="hljs-comment">//尾和尾对比 依次向前追加</span>
      patch(oldEndVnode, newEndVnode);
      oldEndVnode = oldCh[--oldEndIndex];
      newEndVnode = newCh[--newEndIndex];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isSameVnode(oldStartVnode, newEndVnode)) &#123;
      <span class="hljs-comment">// 老的头和新的尾相同 把老的头部移动到尾部</span>
      patch(oldStartVnode, newEndVnode);
      parent.insertBefore(oldStartVnode.el, oldEndVnode.el.nextSibling); <span class="hljs-comment">//insertBefore可以移动或者插入真实dom</span>
      oldStartVnode = oldCh[++oldStartIndex];
      newEndVnode = newCh[--newEndIndex];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isSameVnode(oldEndVnode, newStartVnode)) &#123;
      <span class="hljs-comment">// 老的尾和新的头相同 把老的尾部移动到头部</span>
      patch(oldEndVnode, newStartVnode);
      parent.insertBefore(oldEndVnode.el, oldStartVnode.el);
      oldEndVnode = oldCh[--oldEndIndex];
      newStartVnode = newCh[++newStartIndex];
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 上述四种情况都不满足 那么需要暴力对比</span>
      <span class="hljs-comment">// 根据老的子节点的key和index的映射表 从新的开始子节点进行查找 如果可以找到就进行移动操作 如果找不到则直接进行插入</span>
      <span class="hljs-keyword">let</span> moveIndex = map[newStartVnode.key];
      <span class="hljs-keyword">if</span> (!moveIndex) &#123;
        <span class="hljs-comment">// 老的节点找不到  直接插入</span>
        parent.insertBefore(createElm(newStartVnode), oldStartVnode.el);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">let</span> moveVnode = oldCh[moveIndex]; <span class="hljs-comment">//找得到就拿到老的节点</span>
        oldCh[moveIndex] = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">//这个是占位操作 避免数组塌陷  防止老节点移动走了之后破坏了初始的映射表位置</span>
        parent.insertBefore(moveVnode.el, oldStartVnode.el); <span class="hljs-comment">//把找到的节点移动到最前面</span>
        patch(moveVnode, newStartVnode);
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">// 如果老节点循环完毕了 但是新节点还有  证明  新节点需要被添加到头部或者尾部</span>
  <span class="hljs-keyword">if</span> (newStartIndex <= newEndIndex) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = newStartIndex; i <= newEndIndex; i++) &#123;
      <span class="hljs-comment">// 这是一个优化写法 insertBefore的第一个参数是null等同于appendChild作用</span>
      <span class="hljs-keyword">const</span> ele =
        newCh[newEndIndex + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIndex + <span class="hljs-number">1</span>].el;
      parent.insertBefore(createElm(newCh[i]), ele);
    &#125;
  &#125;
  <span class="hljs-comment">// 如果新节点循环完毕 老节点还有  证明老的节点需要直接被删除</span>
  <span class="hljs-keyword">if</span> (oldStartIndex <= oldEndIndex) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldStartIndex; i <= oldEndIndex; i++) &#123;
      <span class="hljs-keyword">let</span> child = oldCh[i];
      <span class="hljs-keyword">if</span> (child != <span class="hljs-literal">undefined</span>) &#123;
        parent.removeChild(child.el);
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码特别长 但是理解起来其实可以简单的分为以下几点</p>
<p>1.使用双指针移动来进行新老节点的对比
<img alt="diff双指针.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d3aa437b5724cbfbdb0cf4503e7aa12~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2.用 isSameVnode 来判断新老子节点的头头 尾尾 头尾 尾头 是否是同一节点 如果满足就进行相应的移动指针(头头 尾尾)或者移动 dom 节点(头尾 尾头)操作</p>
<p>3.如果全都不相等 进行暴力对比 如果找到了利用 key 和 index 的映射表来移动老的子节点到前面去 如果找不到就直接插入</p>
<p><img alt="diff暴力对比.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c790b59c7c6f4708912be3598c42811f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>4.对老的子节点进行递归 patch 处理</p>
<p>5.最后老的子节点有多的就删掉 新的子节点有多的就添加到相应的位置</p>
<h4 data-id="heading-5">4.改造原型渲染更新方法_update</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/lifecycle.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lifecycleMixin</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-comment">// 把_update挂载在Vue的原型</span>
  Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">const</span> prevVnode = vm._vnode; <span class="hljs-comment">// 保留上一次的vnode</span>
    vm._vnode = vnode;
    <span class="hljs-keyword">if</span> (!prevVnode) &#123;
      <span class="hljs-comment">// patch是渲染vnode为真实dom核心</span>
      vm.$el = patch(vm.$el, vnode); <span class="hljs-comment">// 初次渲染 vm._vnode肯定不存在 要通过虚拟节点 渲染出真实的dom 赋值给$el属性</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      vm.$el = patch(prevVnode, vnode); <span class="hljs-comment">// 更新时把上次的vnode和这次更新的vnode穿进去 进行diff算法</span>
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改造_update 方法 在 Vue 实例的_vnode 保留上次的 vnode 节点 以供 patch 进行新老虚拟 dom 的对比</p>
<h4 data-id="heading-6">5.diff 算法的思维导图</h4>
<p><img alt="Vue2.0源码-diff算法.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f964567d4dbc4228bf9bdbdb4ad70c06~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">小结</h2>
<p>至此 Vue 的 diff 算法源码已经完结 大家主要理解 diff 整个过程 此篇代码量和难度稍微偏大 建议大家反复看 因为 diff 算法是 vue 里面非常核心的知识点 也是面试的常考点 大家可以看着思维导图自己动手写一遍核心代码哈 遇到不懂或者有争议的地方欢迎评论留言</p>
<blockquote>
<p>最后如果觉得本文有帮助 记得<strong>点赞三连</strong>哦 十分感谢！</p>
</blockquote>
<h2 data-id="heading-8">系列链接（后续都会更新完毕）</h2>
<ul>
<li><a href="https://juejin.cn/post/6935344605424517128" target="_blank">手写 Vue2.0 源码（一）-响应式数据原理</a></li>
<li><a href="https://juejin.cn/post/6936024530016010276" target="_blank">手写 Vue2.0 源码（二）-模板编译原理</a></li>
<li><a href="https://juejin.cn/post/6937120983765483528" target="_blank">手写 Vue2.0 源码（三）-初始渲染原理</a></li>
<li><a href="https://juejin.cn/post/6938221715281575973" target="_blank">手写 Vue2.0 源码（四）-渲染更新原理</a></li>
<li><a href="https://juejin.cn/post/6939704519668432910" target="_blank">手写 Vue2.0 源码（五）-异步更新原理 </a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 Vue2.0 源码（六）-diff 算法原理</a></li>
<li><a href="https://juejin.cn/post/6951671158198501383" target="_blank">手写 Vue2.0 源码（七）-Mixin 混入原理</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 Vue2.0 源码（八）-组件原理</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 Vue2.0 源码（九）-计算属性和侦听属性原理</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 Vue2.0 源码（十）-全局 api 分析</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">vue 面试真题-深入源码解析</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 vue-router 源码</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 vuex 源码</a></li>
<li><a href="https://juejin.cn/post/6953433215218483236">手写 vue3.0 源码</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            