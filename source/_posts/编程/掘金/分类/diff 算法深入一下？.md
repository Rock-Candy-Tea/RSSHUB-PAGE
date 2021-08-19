
---
title: 'diff 算法深入一下？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a349dcbba1934ad59a1046be25684fef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 18:39:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a349dcbba1934ad59a1046be25684fef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>有同学问：能否详细说一下 diff 算法。</p>
<blockquote>
<p>简单说：diff 算法是一种优化手段，将前后两个模块进行差异化比较，修补(更新)差异的过程叫做 patch，也叫打补丁。</p>
</blockquote>
<p>详细的说，请阅读这篇文章，有疑问的地方欢迎联系「松宝写代码」一起讨论。</p>
<p>文章主要解决的问题：</p>
<ul>
<li>1、为什么要说这个 diff 算法？</li>
<li>2、虚拟 dom 的 diff 算法</li>
<li>3、为什么使用虚拟 dom？</li>
<li>4、diff 算法的复杂度和特点？</li>
<li>5、vue 的模板文件是如何被编译渲染的？</li>
<li>6、vue2.x 和 vue3.x 中的 diff 有区别吗</li>
<li>7、diff 算法的源头 snabbdom 算法</li>
<li>8、diff 算法与 snabbdom 算法的差异地方？</li>
</ul>
<h2 data-id="heading-1">二、为什么要说这个 diff 算法？</h2>
<p>因为 diff 算法是 vue2.x ， vue3.x 以及 react 中关键核心点，理解 diff 算法，更有助于理解各个框架本质。</p>
<p>说到「diff 算法」，不得不说「虚拟 Dom」，因为这两个息息相关。</p>
<p>比如：</p>
<ul>
<li>vue 的响应式原理？</li>
<li>vue 的 template 文件是如何被编译的？</li>
<li>介绍一下 Virtual Dom 算法？</li>
<li>为什么要用 virtual dom 呢？</li>
<li>diff 算法复杂度以及最大的特点？</li>
<li>vue2.x 的 diff 算法中节点比较情况？</li>
</ul>
<p>等等</p>
<h2 data-id="heading-2">三、虚拟 dom 的 diff 算法</h2>
<p>我们先来说说虚拟 Dom，就是通过 JS 模拟实现 DOM ，接下来难点就是如何判断旧对象和新对象之间的差异。</p>
<p>Dom 是多叉树结构，如果需要完整的对比两棵树的差异，那么算法的时间复杂度 O(n ^ 3)，这个复杂度很难让人接收，尤其在 n 很大的情况下，于是 React 团队优化了算法，实现了 O(n) 的复杂度来对比差异。</p>
<p>实现 O(n) 复杂度的关键就是只对比同层的节点，而不是跨层对比，这也是考虑到在实际业务中很少会去跨层的移动 DOM 元素。</p>
<p>虚拟 DOM 差异算法的步骤分为 2 步：</p>
<ul>
<li>首先从上至下，从左往右遍历对象，也就是树的深度遍历，这一步中会给每个节点添加索引，便于最后渲染差异</li>
<li>一旦节点有子元素，就去判断子元素是否有不同</li>
</ul>
<h3 data-id="heading-3">3.1 vue 中 diff 算法</h3>
<p>实际 diff 算法比较中，节点比较主要有 5 种规则的比较</p>
<ul>
<li>
<p>1、如果新旧 VNode 都是静态的，同时它们的 key 相同（代表同一节点），并且新的 VNode 是 clone 或者是标记了 once（标记 v-once 属性，只渲染一次），那么只需要替换 elm 以及 componentInstance 即可。</p>
</li>
<li>
<p>2、新老节点均有 children 子节点，则对子节点进行 diff 操作，调用 updateChildren，这个 updateChildren 也是 diff 的核心。</p>
</li>
<li>
<p>3、如果老节点没有子节点而新节点存在子节点，先清空老节点 DOM 的文本内容，然后为当前 DOM 节点加入子节点。</p>
</li>
<li>
<p>4、当新节点没有子节点而老节点有子节点的时候，则移除该 DOM 节点的所有子节点。</p>
</li>
<li>
<p>5、当新老节点都无子节点的时候，只是文本的替换</p>
</li>
</ul>
<p>部分源码
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js%23L501" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js#L501" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a> 如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode, vnode, insertedVnodeQueue, ownerArray, index, removeOnly</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (oldVnode === vnode) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
    <span class="hljs-comment">// clone reused vnode</span>
    vnode = ownerArray[index] = cloneVNode(vnode);
  &#125;

  <span class="hljs-keyword">const</span> elm = (vnode.elm = oldVnode.elm);

  <span class="hljs-keyword">if</span> (isTrue(oldVnode.isAsyncPlaceholder)) &#123;
    <span class="hljs-keyword">if</span> (isDef(vnode.asyncFactory.resolved)) &#123;
      hydrate(oldVnode.elm, vnode, insertedVnodeQueue);
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode.isAsyncPlaceholder = <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">if</span> (
    isTrue(vnode.isStatic) &&
    isTrue(oldVnode.isStatic) &&
    vnode.key === oldVnode.key &&
    (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
  ) &#123;
    vnode.componentInstance = oldVnode.componentInstance;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-keyword">let</span> i;
  <span class="hljs-keyword">const</span> data = vnode.data;
  <span class="hljs-keyword">if</span> (isDef(data) && isDef((i = data.hook)) && isDef((i = i.prepatch))) &#123;
    i(oldVnode, vnode);
  &#125;

  <span class="hljs-keyword">const</span> oldCh = oldVnode.children;
  <span class="hljs-keyword">const</span> ch = vnode.children;
  <span class="hljs-keyword">if</span> (isDef(data) && isPatchable(vnode)) &#123;
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode);
    <span class="hljs-keyword">if</span> (isDef((i = data.hook)) && isDef((i = i.update))) i(oldVnode, vnode);
  &#125;
  <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
    <span class="hljs-comment">// 定义了子节点，且不相同，用diff算法对比</span>
    <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
      <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly);
      <span class="hljs-comment">// 新节点有子元素。旧节点没有</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
        <span class="hljs-comment">// 检查key</span>
        checkDuplicateKeys(ch);
      &#125;
      <span class="hljs-comment">// 清空旧节点的text属性</span>
      <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) nodeOps.setTextContent(elm, <span class="hljs-string">''</span>);
      <span class="hljs-comment">// 添加新的Vnode</span>
      addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue);
      <span class="hljs-comment">// 如果旧节点的子节点有内容，新的没有。那么直接删除旧节点子元素的内容</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
      removeVnodes(oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>);
      <span class="hljs-comment">// 如上。只是判断是否为文本节点</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
      nodeOps.setTextContent(elm, <span class="hljs-string">''</span>);
    &#125;
    <span class="hljs-comment">// 如果文本节点不同，替换节点内容</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
    nodeOps.setTextContent(elm, vnode.text);
  &#125;
  <span class="hljs-keyword">if</span> (isDef(data)) &#123;
    <span class="hljs-keyword">if</span> (isDef((i = data.hook)) && isDef((i = i.postpatch))) i(oldVnode, vnode);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.2 React diff 算法</h3>
<p>在 reconcileChildren 函数的入参中</p>
<pre><code class="hljs language-js copyable" lang="js">workInProgress.child = reconcileChildFibers(
  workInProgress,
  current.child,
  nextChildren,
  renderLanes,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>workInProgress：作为父节点传入，新生成的第一个 fiber 的 return 会被指向它。</li>
<li>current.child：旧 fiber 节点，diff 生成新 fiber 节点时会用新生成的 ReactElement 和它作比较。</li>
<li>nextChildren：新生成的 ReactElement，会以它为标准生成新的 fiber 节点。</li>
<li>renderLanes：本次的渲染优先级，最终会被挂载到新 fiber 的 lanes 属性上。</li>
</ul>
<p>diff 的两个主体是：oldFiber（current.child）和 newChildren（nextChildren，新的 ReactElement），它们是两个不一样的数据结构。</p>
<p>部分源码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildrenArray</span>(<span class="hljs-params">
  returnFiber: Fiber,
  currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
  newChildren: <span class="hljs-built_in">Array</span><*>,
  lanes: Lanes,
</span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
  <span class="hljs-comment">/* * returnFiber：currentFirstChild的父级fiber节点
   * currentFirstChild：当前执行更新任务的WIP（fiber）节点
   * newChildren：组件的render方法渲染出的新的ReactElement节点
   * lanes：优先级相关
   * */</span>
  <span class="hljs-comment">// resultingFirstChild是diff之后的新fiber链表的第一个fiber。</span>
  <span class="hljs-keyword">let</span> resultingFirstChild: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// resultingFirstChild是新链表的第一个fiber。</span>
  <span class="hljs-comment">// previousNewFiber用来将后续的新fiber接到第一个fiber之后</span>
  <span class="hljs-keyword">let</span> previousNewFiber: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;

  <span class="hljs-comment">// oldFiber节点，新的child节点会和它进行比较</span>
  <span class="hljs-keyword">let</span> oldFiber = currentFirstChild;
  <span class="hljs-comment">// 存储固定节点的位置</span>
  <span class="hljs-keyword">let</span> lastPlacedIndex = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 存储遍历到的新节点的索引</span>
  <span class="hljs-keyword">let</span> newIdx = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 记录目前遍历到的oldFiber的下一个节点</span>
  <span class="hljs-keyword">let</span> nextOldFiber = <span class="hljs-literal">null</span>;

  <span class="hljs-comment">// 该轮遍历来处理节点更新，依据节点是否可复用来决定是否中断遍历</span>
  <span class="hljs-keyword">for</span> (; oldFiber !== <span class="hljs-literal">null</span> && newIdx < newChildren.length; newIdx++) &#123;
    <span class="hljs-comment">// newChildren遍历完了，oldFiber链没有遍历完，此时需要中断遍历</span>
    <span class="hljs-keyword">if</span> (oldFiber.index > newIdx) &#123;
      nextOldFiber = oldFiber;
      oldFiber = <span class="hljs-literal">null</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 用nextOldFiber存储当前遍历到的oldFiber的下一个节点</span>
      nextOldFiber = oldFiber.sibling;
    &#125;
    <span class="hljs-comment">// 生成新的节点，判断key与tag是否相同就在updateSlot中</span>
    <span class="hljs-comment">// 对DOM类型的元素来说，key 和 tag都相同才会复用oldFiber</span>
    <span class="hljs-comment">// 并返回出去，否则返回null</span>
    <span class="hljs-keyword">const</span> newFiber = updateSlot(returnFiber, oldFiber, newChildren[newIdx], lanes);

    <span class="hljs-comment">// newFiber为 null说明 key 或 tag 不同，节点不可复用，中断遍历</span>
    <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// oldFiber 为null说明oldFiber此时也遍历完了</span>
        <span class="hljs-comment">// 是以下场景，D为新增节点</span>
        <span class="hljs-comment">// 旧 A - B - C</span>
        <span class="hljs-comment">// 新 A - B - C - D oldFiber = nextOldFiber;</span>
      &#125;
      <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
      <span class="hljs-comment">// shouldTrackSideEffects 为true表示是更新过程</span>
      <span class="hljs-keyword">if</span> (oldFiber && newFiber.alternate === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// newFiber.alternate 等同于 oldFiber.alternate</span>
        <span class="hljs-comment">// oldFiber为WIP节点，它的alternate 就是 current节点</span>
        <span class="hljs-comment">// oldFiber存在，并且经过更新后的新fiber节点它还没有current节点,</span>
        <span class="hljs-comment">// 说明更新后展现在屏幕上不会有current节点，而更新后WIP</span>
        <span class="hljs-comment">// 节点会称为current节点，所以需要删除已有的WIP节点</span>
        deleteChild(returnFiber, oldFiber);
      &#125;
    &#125;
    <span class="hljs-comment">// 记录固定节点的位置</span>
    lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
    <span class="hljs-comment">// 将新fiber连接成以sibling为指针的单向链表</span>
    <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
      resultingFirstChild = newFiber;
    &#125; <span class="hljs-keyword">else</span> &#123;
      previousNewFiber.sibling = newFiber;
    &#125;
    previousNewFiber = newFiber;
    <span class="hljs-comment">// 将oldFiber节点指向下一个，与newChildren的遍历同步移动</span>
    oldFiber = nextOldFiber;
  &#125;

  <span class="hljs-comment">// 处理节点删除。新子节点遍历完，说明剩下的oldFiber都是没用的了，可以删除.</span>
  <span class="hljs-keyword">if</span> (newIdx === newChildren.length) &#123;
    <span class="hljs-comment">// newChildren遍历结束，删除掉oldFiber链中的剩下的节点</span>
    deleteRemainingChildren(returnFiber, oldFiber);
    <span class="hljs-keyword">return</span> resultingFirstChild;
  &#125;

  <span class="hljs-comment">// 处理新增节点。旧的遍历完了，能复用的都复用了，所以意味着新的都是新插入的了</span>
  <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
      <span class="hljs-comment">// 基于新生成的ReactElement创建新的Fiber节点</span>
      <span class="hljs-keyword">const</span> newFiber = createChild(returnFiber, newChildren[newIdx], lanes);
      <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">continue</span>;
      &#125;
      <span class="hljs-comment">// 记录固定节点的位置lastPlacedIndex</span>
      lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
      <span class="hljs-comment">// 将新生成的fiber节点连接成以sibling为指针的单向链表</span>
      <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
        resultingFirstChild = newFiber;
      &#125; <span class="hljs-keyword">else</span> &#123;
        previousNewFiber.sibling = newFiber;
      &#125;
      previousNewFiber = newFiber;
    &#125;
    <span class="hljs-keyword">return</span> resultingFirstChild;
  &#125;
  <span class="hljs-comment">// 执行到这是都没遍历完的情况，把剩余的旧子节点放入一个以key为键,值为oldFiber节点的map中</span>
  <span class="hljs-comment">// 这样在基于oldFiber节点新建新的fiber节点时，可以通过key快速地找出oldFiber</span>
  <span class="hljs-keyword">const</span> existingChildren = mapRemainingChildren(returnFiber, oldFiber);

  <span class="hljs-comment">// 节点移动</span>
  <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
    <span class="hljs-comment">// 基于map中的oldFiber节点来创建新fiber</span>
    <span class="hljs-keyword">const</span> newFiber = updateFromMap(
      existingChildren,
      returnFiber,
      newIdx,
      newChildren[newIdx],
      lanes,
    );
    <span class="hljs-keyword">if</span> (newFiber !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
        <span class="hljs-keyword">if</span> (newFiber.alternate !== <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-comment">// 因为newChildren中剩余的节点有可能和oldFiber节点一样,只是位置换了，</span>
          <span class="hljs-comment">// 但也有可能是是新增的.</span>

          <span class="hljs-comment">// 如果newFiber的alternate不为空，则说明newFiber不是新增的。</span>
          <span class="hljs-comment">// 也就说明着它是基于map中的oldFiber节点新建的,意味着oldFiber已经被使用了,所以需</span>
          <span class="hljs-comment">// 要从map中删去oldFiber</span>
          existingChildren.delete(newFiber.key === <span class="hljs-literal">null</span> ? newIdx : newFiber.key);
        &#125;
      &#125;

      <span class="hljs-comment">// 移动节点，多节点diff的核心，这里真正会实现节点的移动</span>
      lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
      <span class="hljs-comment">// 将新fiber连接成以sibling为指针的单向链表</span>
      <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
        resultingFirstChild = newFiber;
      &#125; <span class="hljs-keyword">else</span> &#123;
        previousNewFiber.sibling = newFiber;
      &#125;
      previousNewFiber = newFiber;
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
    <span class="hljs-comment">// 此时newChildren遍历完了，该移动的都移动了，那么删除剩下的oldFiber</span>
    existingChildren.forEach(<span class="hljs-function">(<span class="hljs-params">child</span>) =></span> deleteChild(returnFiber, child));
  &#125;
  <span class="hljs-keyword">return</span> resultingFirstChild;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">四、为什么使用虚拟 dom？</h2>
<p>很多时候手工优化 dom 确实会比 virtual dom 效率高，对于比较简单的 dom 结构用手工优化没有问题，但当页面结构很庞大，结构很复杂时，手工优化会花去大量时间，而且可维护性也不高，不能保证每个人都有手工优化的能力。至此，virtual dom 的解决方案应运而生。</p>
<p>virtual dom 是“解决过多的操作 dom 影响性能”的一种解决方案。</p>
<p>virtual dom 很多时候都不是最优的操作，但它具有普适性，在效率、可维护性之间达平衡。</p>
<p>** virutal dom 的意义：**</p>
<ul>
<li>1、提供一种简单对象去代替复杂的 dom 对象，从而优化 dom 操作</li>
<li>2、提供一个中间层，js 去写 ui，ios 安卓之类的负责渲染，就像 reactNative 一样。</li>
</ul>
<h2 data-id="heading-6">五、diff 算法的复杂度和特点？</h2>
<p>vue2.x 的 diff 位于 patch.js 文件中，该算法来源于 snabbdom，复杂度为 O(n)。了解 diff 过程可以让我们更高效的使用框架。react 的 diff 其实和 vue 的 diff 大同小异。</p>
<p>最大特点：比较只会在同层级进行, 不会跨层级比较。</p>
<pre><code class="hljs language-js copyable" lang="js"><!-- 之前 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>              <span class="hljs-comment"><!-- 层级1 --></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>              <span class="hljs-comment"><!-- 层级2 --></span>
    <span class="hljs-tag"><<span class="hljs-name">b</span>></span> aoy <span class="hljs-tag"></<span class="hljs-name">b</span>></span>   <span class="hljs-comment"><!-- 层级3 --></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>diff<span class="hljs-tag"></<span class="hljs-name">Span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<!-- 之后 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>             <span class="hljs-comment"><!-- 层级1 --></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>              <span class="hljs-comment"><!-- 层级2 --></span>
    <span class="hljs-tag"><<span class="hljs-name">b</span>></span> aoy <span class="hljs-tag"></<span class="hljs-name">b</span>></span>   <span class="hljs-comment"><!-- 层级3 --></span>
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>diff<span class="hljs-tag"></<span class="hljs-name">Span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比之前和之后：可能期望将<code><span></code>直接移动到<code><p></code>的后边，这是最优的操作。</p>
<p>但是实际的 diff 操作是：</p>
<ul>
<li>1、移除<code><p></code>里的<code><span></code>；</li>
<li>2、在创建一个新的<code><span></code>插到<code><p></code>的后边。 因为新加的<code><span></code>在层级 2，旧的在层级 3，属于不同层级的比较。</li>
</ul>
<h2 data-id="heading-7">六、vue 的模板文件是如何被编译渲染的？</h2>
<p>vue 中也使用 diff 算法，有必要了解一下 Vue 是如何工作的。通过这个问题，我们可以很好的掌握，diff 算法在整个编译过程中，哪个环节，做了哪些操作，然后使用 diff 算法后输出什么？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a349dcbba1934ad59a1046be25684fef~tplv-k3u1fbpfcp-watermark.image" alt="vue-template.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解释：</p>
<h3 data-id="heading-8">1、mount 函数</h3>
<p>mount 函数主要是获取 template，然后进入 compileToFunctions 函数。</p>
<h3 data-id="heading-9">2、compileToFunction 函数</h3>
<p>compileToFunction 函数主要是将 template 编译成 render 函数。首先读取缓存，没有缓存就调用 compile 方法拿到 render 函数的字符串形式，在通过 new Function 的方式生成 render 函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 有缓存的话就直接在缓存里面拿</span>
<span class="hljs-keyword">const</span> key = options && options.delimiters ? <span class="hljs-built_in">String</span>(options.delimiters) + template : template;
<span class="hljs-keyword">if</span> (cache[key]) &#123;
  <span class="hljs-keyword">return</span> cache[key];
&#125;
<span class="hljs-keyword">const</span> res = &#123;&#125;;
<span class="hljs-keyword">const</span> compiled = compile(template, options); <span class="hljs-comment">// compile 后面会详细讲</span>
res.render = makeFunction(compiled.render); <span class="hljs-comment">//通过 new Function 的方式生成 render 函数并缓存</span>
<span class="hljs-keyword">const</span> l = compiled.staticRenderFns.length;
res.staticRenderFns = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(l);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < l; i++) &#123;
  res.staticRenderFns[i] = makeFunction(compiled.staticRenderFns[i]);
&#125;

<span class="hljs-comment">// ......</span>

<span class="hljs-keyword">return</span> (cache[key] = res); <span class="hljs-comment">// 记录至缓存中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3、compile 函数</h3>
<p>compile 函数将 template 编译成 render 函数的字符串形式。后面我们主要讲解 render</p>
<p>完成 render 方法生成后，会进入到 mount 进行 DOM 更新。该方法核心逻辑如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 触发 beforeMount 生命周期钩子</span>
callHook(vm, <span class="hljs-string">'beforeMount'</span>);
<span class="hljs-comment">// 重点：新建一个 Watcher 并赋值给 vm._watcher</span>
vm._watcher = <span class="hljs-keyword">new</span> Watcher(
  vm,
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateComponent</span>(<span class="hljs-params"></span>) </span>&#123;
    vm._update(vm._render(), hydrating);
  &#125;,
  noop,
);
hydrating = <span class="hljs-literal">false</span>;
<span class="hljs-comment">// manually mounted instance, call mounted on self</span>
<span class="hljs-comment">// mounted is called for render-created child components in its inserted hook</span>
<span class="hljs-keyword">if</span> (vm.$vnode == <span class="hljs-literal">null</span>) &#123;
  vm._isMounted = <span class="hljs-literal">true</span>;
  callHook(vm, <span class="hljs-string">'mounted'</span>);
&#125;
<span class="hljs-keyword">return</span> vm;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>首先会 new 一个 watcher 对象（主要是将模板与数据建立联系），在 watcher 对象创建后，</p>
</li>
<li>
<p>会运行传入的方法 vm._update(vm._render(), hydrating) 。
其中的 vm._render()主要作用就是运行前面 compiler 生成的 render 方法，并返回一个 vNode 对象。</p>
</li>
<li>
<p>vm.update() 则会对比新的 vdom 和当前 vdom，并把差异的部分渲染到真正的 DOM 树上。（watcher 背后的实现原理：vue2.x 的响应式原理）</p>
</li>
</ul>
<p>上面提到的 compile 就是将 template 编译成 render 函数的字符串形式。核心代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compile</span>(<span class="hljs-params">template: string, options: CompilerOptions</span>): <span class="hljs-title">CompiledResult</span> </span>&#123;
  <span class="hljs-keyword">const</span> AST = parse(template.trim(), options); <span class="hljs-comment">//1. parse</span>
  optimize(AST, options); <span class="hljs-comment">//2.optimize</span>
  <span class="hljs-keyword">const</span> code = generate(AST, options); <span class="hljs-comment">//3.generate</span>
  <span class="hljs-keyword">return</span> &#123;
    AST,
    <span class="hljs-attr">render</span>: code.render,
    <span class="hljs-attr">staticRenderFns</span>: code.staticRenderFns,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>compile 这个函数主要有三个步骤组成：</p>
<ul>
<li>parse，</li>
<li>optimize</li>
<li>generate</li>
</ul>
<p>分别输出一个包含</p>
<ul>
<li>AST 字符串</li>
<li>staticRenderFns 的对象字符串</li>
<li>render 函数 的字符串。</li>
</ul>
<p>parse 函数：主要功能是<strong>将 template 字符串解析成 AST（抽象语法树）</strong>。前面定义的 ASTElement 的数据结构，parse 函数就是将 template 里的结构（指令，属性，标签）
转换为 AST 形式存进 ASTElement 中，最后解析生成 AST。</p>
<p>optimize 函数（src/compiler/optomizer.js）:主要功能是<strong>标记静态节点</strong>。后面 patch 过程中对比新旧 VNode 树形结构做优化。被标记为 static 的节点在后面的 diff 算法中会被直接忽略，不做详细比较。</p>
<p>generate 函数（src/compiler/codegen/index.js）:主要功能<strong>根据 AST 结构拼接生成 render 函数的字符串</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> code = AST ? genElement(AST) : <span class="hljs-string">'_c("div")'</span>;
staticRenderFns = prevStaticRenderFns;
onceCount = prevOnceCount;
<span class="hljs-keyword">return</span> &#123;
  <span class="hljs-attr">render</span>: <span class="hljs-string">`with(this)&#123;return <span class="hljs-subst">$&#123;code&#125;</span>&#125;`</span>, <span class="hljs-comment">//最外层包一个 with(this) 之后返回</span>
  <span class="hljs-attr">staticRenderFns</span>: currentStaticRenderFns,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 genElement 函数（src/compiler/codgen/index.js）是根据 AST 的属性调用不同的方法生成字符串返回。</p>
<p><strong>总之：</strong></p>
<p>就是 compile 函数中三个核心步骤介绍，</p>
<ul>
<li>
<p>compile 之后我们得到 render 函数的字符串形式，后面通过 new Function 得到真正的渲染函数。</p>
</li>
<li>
<p>数据发生变化后，会执行 watcher 中的_update 函数（src/core/instance/lifecycle.js），_update 函数会执行这个渲染函数，输出一个新的 VNode 树形结构的数据。</p>
</li>
<li>
<p>然后调用 patch 函数，拿到这个新的 VNode 与旧的 VNode 进行对比，只有反生了变化的节点才会被更新到新的真实 DOM 树上。</p>
</li>
</ul>
<h3 data-id="heading-11">4、patch 函数</h3>
<p>patch 函数 就是新旧 VNode 对比的 diff 函数，主要是为了优化 dom，通过算法使操作 dom 的行为降低到最低，
diff 算法来源于 snabbdom，是 VDOM 思想的核心。snabbdom 的算法是为了 DOM 操作跨级增删节点较少的这一目标进行优化，
它只会在同层级进行，不会跨层级比较。</p>
<h3 data-id="heading-12">总结一下</h3>
<ul>
<li>compile 函数主要是将 template 转换为 AST，优化 AST，再将 AST 转换为 render 函数的字符串形式。</li>
<li>再通过 new Function 得到真正的 render 函数，render 函数与数据通过 Watcher 产生关联。</li>
<li>在数据反生变化的时候调用 patch 函数，执行 render 函数，生成新的 VNode，与旧的 VNode 进行 diff，最终更新 DOM 树。</li>
</ul>
<h2 data-id="heading-13">七、vue2.x，vue3.x，React 中的 diff 有区别吗？</h2>
<p>总的来说：</p>
<ul>
<li>
<p>vue2.x 的核心 diff 算法采用双端比较的算法，同时从新旧 children 的两端开始进行比较，借助 key 可以复用的节点。</p>
</li>
<li>
<p>vue3.x 借鉴了一些别的算法 inferno(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Finfernojs%2Finferno" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/infernojs/inferno" ref="nofollow noopener noreferrer">github.com/infernojs/i…</a>) 解决：1、处理相同的前置和后置元素的预处理；2、一旦需要进行 DOM 移动，我们首先要做的就是找到 source 的最长递增子序列。</p>
</li>
</ul>
<p>在创建 VNode 就确定类型，以及在 mount/patch 的过程中采用位运算来判断一个 VNode 的类型，在这个优化的基础上再配合 Diff 算法，性能得到提升。</p>
<p>可以看一下 vue3.x 的源码：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></p>
<ul>
<li>react 通过 key 和 tag 来对节点进行取舍，可直接将复杂的比对拦截掉，然后降级成节点的移动和增删这样比较简单的操作。</li>
</ul>
<p>对 oldFiber 和新的 ReactElement 节点的比对，将会生成新的 fiber 节点，同时标记上 effectTag，这些 fiber 会被连到 workInProgress 树中，作为新的 WIP 节点。树的结构因此被一点点地确定，而新的 workInProgress 节点也基本定型。在 diff 过后，workInProgress 节点的 beginWork 节点就完成了，接下来会进入 completeWork 阶段。</p>
<h2 data-id="heading-14">八、diff 算法的源头 snabbdom 算法</h2>
<p>snabbdom 算法： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></p>
<p>定位：一个专注于简单性、模块化、强大功能和性能的虚拟 DOM 库。</p>
<h3 data-id="heading-15">1、snabbdom 中定义 Vnode 的类型</h3>
<p>snabbdom 中定义 Vnode 的类型(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Fvnode.ts%23L12" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/vnode.ts#L12" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a>)</p>
<pre><code class="copyable">export interface VNode &#123;
  sel: string | undefined; // selector的缩写
  data: VNodeData | undefined; // 下面VNodeData接口的内容
  children: Array<VNode | string> | undefined; // 子节点
  elm: Node | undefined; // element的缩写，存储了真实的HTMLElement
  text: string | undefined; // 如果是文本节点，则存储text
  key: Key | undefined; // 节点的key，在做列表时很有用
&#125;

export interface VNodeData &#123;
  props?: Props;
  attrs?: Attrs;
  class?: Classes;
  style?: VNodeStyle;
  dataset?: Dataset;
  on?: On;
  attachData?: AttachData;
  hook?: Hooks;
  key?: Key;
  ns?: string; // for SVGs
  fn?: () => VNode; // for thunks
  args?: any[]; // for thunks
  is?: string; // for custom elements v1
  [key: string]: any; // for any other 3rd party module
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">2、init 函数分析</h3>
<p>init 函数的地址：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Finit.ts%23L63" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/init.ts#L63" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></p>
<p>init() 函数接收一个模块数组 modules 和可选的 domApi 对象作为参数，返回一个函数，即 patch() 函数。</p>
<p>domApi 对象的接口包含了很多 DOM 操作的方法。</p>
<h3 data-id="heading-17">3、patch 函数分析</h3>
<p>源码：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Finit.ts%23L367" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/init.ts#L367" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></p>
<ul>
<li>init() 函数返回了一个 patch() 函数</li>
<li>patch() 函数接收两个 VNode 对象作为参数，并返回一个新 VNode。</li>
</ul>
<h3 data-id="heading-18">4、h 函数分析</h3>
<p>源码：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Fh.ts%23L33" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/h.ts#L33" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></p>
<p>h() 函数接收多种参数，其中必须有一个 sel 参数，作用是将节点内容挂载到该容器中，并返回一个新 VNode。</p>
<h2 data-id="heading-19">九、diff 算法与 snabbdom 算法的差异地方？</h2>
<p>在 vue2.x 不是完全 snabbdom 算法，而是基于 vue 的场景进行了一些修改和优化，主要体现在判断 key 和 diff 部分。</p>
<p>1、在 snabbdom 中 通过 key 和 sel 就判断是否为同一节点，那么在 vue 中，增加了一些判断 在满足 key 相等的同时会判断，tag 名称是否一致，是否为注释节点，是否为异步节点，或者为 input 时候类型是否相同等。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js%23L35" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js#L35" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param </span>a 被对比节点
 * <span class="hljs-doctag">@param </span>b  对比节点
 * 对比两个节点是否相同
 * 需要组成的条件：key相同，tag相同，是否都为注释节点，是否同事定义了data，如果是input标签，那么type必须相同
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    a.key === b.key &&
    ((a.tag === b.tag &&
      a.isComment === b.isComment &&
      isDef(a.data) === isDef(b.data) &&
      sameInputType(a, b)) ||
      (isTrue(a.isAsyncPlaceholder) &&
        a.asyncFactory === b.asyncFactory &&
        isUndef(b.asyncFactory.error)))
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、diff 差异，patchVnode 是对比模版变化的函数，可能会用到 diff 也可能直接更新。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js%23L404" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js#L404" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">
  parentElm,
  oldCh,
  newCh,
  insertedVnodeQueue,
  removeOnly
</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx];
  <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx];
  <span class="hljs-keyword">let</span> oldKeyToIdx, idxInOld, vnodeToMove, refElm;
  <span class="hljs-keyword">const</span> canMove = !removeOnly;

  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">"production"</span>) &#123;
    checkDuplicateKeys(newCh);
  &#125;

  <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    <span class="hljs-keyword">if</span> (isUndef(oldStartVnode)) &#123;
      oldStartVnode = oldCh[++oldStartIdx]; <span class="hljs-comment">// Vnode has been moved left</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isUndef(oldEndVnode)) &#123;
      oldEndVnode = oldCh[--oldEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
      patchVnode(
        oldStartVnode,
        newStartVnode,
        insertedVnodeQueue,
        newCh,
        newStartIdx
      );
      oldStartVnode = oldCh[++oldStartIdx];
      newStartVnode = newCh[++newStartIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
      patchVnode(
        oldEndVnode,
        newEndVnode,
        insertedVnodeQueue,
        newCh,
        newEndIdx
      );
      oldEndVnode = oldCh[--oldEndIdx];
      newEndVnode = newCh[--newEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
      <span class="hljs-comment">// Vnode moved right</span>
      patchVnode(
        oldStartVnode,
        newEndVnode,
        insertedVnodeQueue,
        newCh,
        newEndIdx
      );
      canMove &&
        nodeOps.insertBefore(
          parentElm,
          oldStartVnode.elm,
          nodeOps.nextSibling(oldEndVnode.elm)
        );
      oldStartVnode = oldCh[++oldStartIdx];
      newEndVnode = newCh[--newEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123;
      <span class="hljs-comment">// Vnode moved left</span>
      patchVnode(
        oldEndVnode,
        newStartVnode,
        insertedVnodeQueue,
        newCh,
        newStartIdx
      );
      canMove &&
        nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm);
      oldEndVnode = oldCh[--oldEndIdx];
      newStartVnode = newCh[++newStartIdx];
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx))
        oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx);
      idxInOld = isDef(newStartVnode.key)
        ? oldKeyToIdx[newStartVnode.key]
        : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx);
      <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123;
        <span class="hljs-comment">// New element</span>
        createElm(
          newStartVnode,
          insertedVnodeQueue,
          parentElm,
          oldStartVnode.elm,
          <span class="hljs-literal">false</span>,
          newCh,
          newStartIdx
        );
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// vnodeToMove将要移动的节点</span>
        vnodeToMove = oldCh[idxInOld];
        <span class="hljs-keyword">if</span> (sameVnode(vnodeToMove, newStartVnode)) &#123;
          patchVnode(
            vnodeToMove,
            newStartVnode,
            insertedVnodeQueue,
            newCh,
            newStartIdx
          );
          oldCh[idxInOld] = <span class="hljs-literal">undefined</span>;
          canMove &&
            nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// same key but different element. treat as new element</span>
          createElm(
            newStartVnode,
            insertedVnodeQueue,
            parentElm,
            oldStartVnode.elm,
            <span class="hljs-literal">false</span>,
            newCh,
            newStartIdx
          );
        &#125;
      &#125;
      <span class="hljs-comment">// vnodeToMove将要移动的节点</span>
      newStartVnode = newCh[++newStartIdx];
    &#125;
  &#125;
  <span class="hljs-comment">// 旧节点完成，新的没完成</span>
  <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
    refElm = isUndef(newCh[newEndIdx + <span class="hljs-number">1</span>]) ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm;
    addVnodes(
      parentElm,
      refElm,
      newCh,
      newStartIdx,
      newEndIdx,
      insertedVnodeQueue
    );
    <span class="hljs-comment">// 新的完成，老的没完成</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartIdx > newEndIdx) &#123;
    removeVnodes(oldCh, oldStartIdx, oldEndIdx);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">更多阅读</h4>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F7Sz0dSFkWOEo2iw5xrcCLA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/7Sz0dSFkWOEo2iw5xrcCLA" ref="nofollow noopener noreferrer">AB 实验：MAB 多臂老虎机智能调优的基本原理</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FTXzuf_98yMojVAFlDv0CCQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/TXzuf_98yMojVAFlDv0CCQ" ref="nofollow noopener noreferrer">AB 实验基础-专有名词</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FUcwpNqRQ3we10S9z5cO53g" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/UcwpNqRQ3we10S9z5cO53g" ref="nofollow noopener noreferrer">AB 实验基础-AB 是什么？AB 的价值？为什么使用 AB 实验？</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FsXIJ6bQj97bZTaYHQgJTIw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/sXIJ6bQj97bZTaYHQgJTIw" ref="nofollow noopener noreferrer">【每日一题】(57 题)数组扁平化的方法有哪些？</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FKkqdB4mWlMgZMcHVhZVZXQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/KkqdB4mWlMgZMcHVhZVZXQ" ref="nofollow noopener noreferrer">【每日一题】(56 题)介绍下深度优先遍历和广度优先遍历，如何实现？</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F0KKYgUXJpnJ2yIQ9DY8eJA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/0KKYgUXJpnJ2yIQ9DY8eJA" ref="nofollow noopener noreferrer">【每日一题】(55 题)算法题：实现数组的全排列</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F_ay6KfcC5DMoZu9XqS2NHA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/_ay6KfcC5DMoZu9XqS2NHA" ref="nofollow noopener noreferrer">2020「松宝写代码」个人年终总结：未来可期</a></p>
</li>
</ul>
<h4 data-id="heading-21">引用</h4>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js%23L501" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js#L501" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Finfernojs%2Finferno" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/infernojs/inferno" ref="nofollow noopener noreferrer">github.com/infernojs/i…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Fvnode.ts%23L12" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/vnode.ts#L12" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Finit.ts%23L63" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/init.ts#L63" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Finit.ts%23L367" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/init.ts#L367" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom%2Fblob%2F27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df%2Fsrc%2Fh.ts%23L33" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom/blob/27e9c4d5dca62b6dabf9ac23efb95f1b6045b2df/src/h.ts#L33" ref="nofollow noopener noreferrer">github.com/snabbdom/sn…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js%23L35" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js#L35" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2F8a219e3d4cfc580bbb3420344600801bd9473390%2Fsrc%2Fcore%2Fvdom%2Fpatch.js%23L404" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/8a219e3d4cfc580bbb3420344600801bd9473390/src/core/vdom/patch.js#L404" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></li>
</ul></div>  
</div>
            