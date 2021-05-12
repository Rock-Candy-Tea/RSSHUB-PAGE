
---
title: '【Vue源码系列】：DOM-Diff'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d37a3b58f243d18c4f0cdf03ff2cba~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 11 May 2021 22:53:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d37a3b58f243d18c4f0cdf03ff2cba~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>为了降低直接操作真实DOM带来的性能消耗。Vue内部引入了Vdom（虚拟DOM）。Vdom概念也比较简单，可以看成一个普通的JS对象，用来描述用户界面。而DOM-Diff的过程，简单来说，就是当有数据更新时，首先需要通过JS计算出Vdom的变化，然后再将变化更新到真实的用户界面。接下来，我们从源码出发，逐步分析。</p>
<h2 data-id="heading-1">_update</h2>
<p>从<strong>响应式原理</strong>学习中，<strong>了解了数据更新时重新执行render函数再次生成新的VNode的原理</strong>。但是，真正完成视图界面的更新，还需要经过后续复杂的过程，而这个过程的入口从 <code>vm.update()</code> 开始。流程图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d37a3b58f243d18c4f0cdf03ff2cba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>观察上面流程图发现，<code>update()</code>会将由 <code>render()</code> 生成的新VNode与旧VNode交给一个函数 <code>patch</code>去处理。</p>
<p>另外，交给<code>patch</code>处理之前，<strong>update()</strong> 会完成一些预处理，步骤如下：</p>
<ol>
<li>缓存 <strong>oldVNode</strong> 到内存中 => <code>const prevVnode = vm._vnode</code></li>
<li>更新 <strong>vm._vnode</strong> => <code>vm._vnode = vnode</code></li>
<li>判断 <strong>oldVNode</strong> 是否在：
<ol>
<li>不存在：表明是组件第一次加载，通过<code>patch</code>函数，直接遍历 <strong>newVNode</strong>，为每个节点生成真实DOM，并挂载到每个节点的 <code>elm</code> 属性上。</li>
<li>存在：表明此时为组件的更新操作，之前已经渲染过该组件。通过<code>patch</code>函数，对 <strong>oldVNode</strong> 和<strong>newVNode</strong>进行对比，找出差异变化，最后完成真实DOM的最小化更新，并且保证 newVNode上每个节点对应着正确的真实DOM。</li>
</ol>
</li>
</ol>
<h2 data-id="heading-2">__patch__</h2>
<p><code>patch</code>的作用：通过比较新旧VNode，找出差异变化，最后完成真实DOM的最小化更新，这个过程也就是<code>Diff</code>过程。</p>
<p><strong>diff核心</strong></p>
<blockquote>
<p>Diff算法的核心： <strong>深度优先，同层比较。</strong></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f67b9148ce5944c8b037f284f35d8ace~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们带着上面的讲到的算法核心，一步步体会。下面重点学习下 具体的<strong>diff</strong>原理。</p>
<h3 data-id="heading-3">sameVnode（节点是否相同）</h3>
<p><strong>diff</strong>原理实际上就是<strong>VNode</strong>节点之间比较的过程。首先明确一个概念，两个<strong>VNode</strong>节点<strong>相等</strong>的条件：</p>
<ol>
<li><strong>key</strong>值相等</li>
<li><strong>tag</strong> （标签类型）相等</li>
<li><strong>input</strong>元素的<strong>type</strong>属性要相等</li>
</ol>
<p><strong>判断节点是否相等</strong>的详细逻辑如下。源码位置： <code>core/vdom/patch.js</code> 的  <strong>sameVnode</strong> 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    a.key === b.key && (
      (
        a.tag === b.tag &&
        a.isComment === b.isComment &&
        isDef(a.data) === isDef(b.data) &&
        sameInputType(a, b)
      ) || (
        isTrue(a.isAsyncPlaceholder) &&
        a.asyncFactory === b.asyncFactory &&
        isUndef(b.asyncFactory.error)
      )
    )
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">patch （更新、删除、创建节点）</h3>
<p>接下来，从 diff入口 - <code>patch</code>函数开始分析。源码位置：<code>/core/vdom/patch.js</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span> (<span class="hljs-params">oldVnode, vnode, hydrating, removeOnly</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isUndef(vnode)) &#123;
      <span class="hljs-keyword">if</span> (isDef(oldVnode)) invokeDestroyHook(oldVnode)
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">let</span> isInitialPatch = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">const</span> insertedVnodeQueue = []

    <span class="hljs-keyword">if</span> (isUndef(oldVnode)) &#123;
      <span class="hljs-comment">// empty mount (likely as component), create new root element</span>
      isInitialPatch = <span class="hljs-literal">true</span>
      createElm(vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">const</span> isRealElement = isDef(oldVnode.nodeType)
      <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
        <span class="hljs-comment">// patch existing root node</span>
        patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (isRealElement) &#123;
          <span class="hljs-comment">// mounting to a real element</span>
          <span class="hljs-comment">// check if this is server-rendered content and if we can perform</span>
          <span class="hljs-comment">// a successful hydration.</span>
          <span class="hljs-keyword">if</span> (oldVnode.nodeType === <span class="hljs-number">1</span> && oldVnode.hasAttribute(SSR_ATTR)) &#123;
            oldVnode.removeAttribute(SSR_ATTR)
            hydrating = <span class="hljs-literal">true</span>
          &#125;
          <span class="hljs-keyword">if</span> (isTrue(hydrating)) &#123;
            <span class="hljs-keyword">if</span> (hydrate(oldVnode, vnode, insertedVnodeQueue)) &#123;
              invokeInsertHook(vnode, insertedVnodeQueue, <span class="hljs-literal">true</span>)
              <span class="hljs-keyword">return</span> oldVnode
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
              warn(
                <span class="hljs-string">'The client-side rendered virtual DOM tree is not matching '</span> +
                <span class="hljs-string">'server-rendered content. This is likely caused by incorrect '</span> +
                <span class="hljs-string">'HTML markup, for example nesting block-level elements inside '</span> +
                <span class="hljs-string">'<p>, or missing <tbody>. Bailing hydration and performing '</span> +
                <span class="hljs-string">'full client-side render.'</span>
              )
            &#125;
          &#125;
          <span class="hljs-comment">// either not server-rendered, or hydration failed.</span>
          <span class="hljs-comment">// create an empty node and replace it</span>
          oldVnode = emptyNodeAt(oldVnode)
        &#125;

        <span class="hljs-comment">// replacing existing element</span>
        <span class="hljs-keyword">const</span> oldElm = oldVnode.elm
        <span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)

        <span class="hljs-comment">// create new node</span>
        createElm(
          vnode,
          insertedVnodeQueue,
          <span class="hljs-comment">// extremely rare edge case: do not insert if old element is in a</span>
          <span class="hljs-comment">// leaving transition. Only happens when combining transition +</span>
          <span class="hljs-comment">// keep-alive + HOCs. (#4590)</span>
          oldElm._leaveCb ? <span class="hljs-literal">null</span> : parentElm,
          nodeOps.nextSibling(oldElm)
        )

        <span class="hljs-comment">// update parent placeholder node element, recursively</span>
        <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
          <span class="hljs-keyword">let</span> ancestor = vnode.parent
          <span class="hljs-keyword">const</span> patchable = isPatchable(vnode)
          <span class="hljs-keyword">while</span> (ancestor) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) &#123;
              cbs.destroy[i](ancestor)
            &#125;
            ancestor.elm = vnode.elm
            <span class="hljs-keyword">if</span> (patchable) &#123;
              <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
                cbs.create[i](emptyNode, ancestor)
              &#125;
              <span class="hljs-comment">// #6513</span>
              <span class="hljs-comment">// invoke insert hooks that may have been merged by create hooks.</span>
              <span class="hljs-comment">// e.g. for directives that uses the "inserted" hook.</span>
              <span class="hljs-keyword">const</span> insert = ancestor.data.hook.insert
              <span class="hljs-keyword">if</span> (insert.merged) &#123;
                <span class="hljs-comment">// start at index 1 to avoid re-invoking component mounted hook</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < insert.fns.length; i++) &#123;
                  insert.fns[i]()
                &#125;
              &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
              registerRef(ancestor)
            &#125;
            ancestor = ancestor.parent
          &#125;
        &#125;

        <span class="hljs-comment">// destroy old node</span>
        <span class="hljs-keyword">if</span> (isDef(parentElm)) &#123;
          removeVnodes([oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.tag)) &#123;
          invokeDestroyHook(oldVnode)
        &#125;
      &#125;
    &#125;

    invokeInsertHook(vnode, insertedVnodeQueue, isInitialPatch)
    <span class="hljs-keyword">return</span> vnode.elm
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析主干逻辑，<code>patch</code>主要处理以下内容：</p>
<ol>
<li>
<p>若 oldVNode 存在， newVNode 不存在。 则<strong>销毁元素</strong>。</p>
</li>
<li>
<p>若 oldVNode 不存在，newVNode 存在。 则<strong>创建元素</strong>，按照当前虚拟节点创建真实DOM，并挂载到 <code>vnode.elm</code>。</p>
</li>
<li>
<p>若 oldVNode 和 newVNode 都存在，并且通过 sameVnode 函数 判断两者是否相等。相等，则执行后续进一步比较（自身和子节点），这部分内容是通过 <code>patchVnode</code> 函数处理。稍后我们详细了解。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//... </span>
patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
<span class="hljs-comment">//...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>最后，返回diff渲染后的真实  <code>vnode.elm</code> 。</p>
</li>
</ol>
<p>接下来，看下 <code>patchVnode</code> 函数的主干逻辑。</p>
<h3 data-id="heading-5">patchVnode （更新节点）</h3>
<p>源代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span> (<span class="hljs-params">
    oldVnode,
    vnode,
    insertedVnodeQueue,
    ownerArray,
    index,
    removeOnly
  </span>) </span>&#123;
    <span class="hljs-keyword">if</span> (oldVnode === vnode) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
      <span class="hljs-comment">// clone reused vnode</span>
      vnode = ownerArray[index] = cloneVNode(vnode)
    &#125;

    <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm

    <span class="hljs-keyword">if</span> (isTrue(oldVnode.isAsyncPlaceholder)) &#123;
      <span class="hljs-keyword">if</span> (isDef(vnode.asyncFactory.resolved)) &#123;
        hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> &#123;
        vnode.isAsyncPlaceholder = <span class="hljs-literal">true</span>
      &#125;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// reuse element for static trees.</span>
    <span class="hljs-comment">// note we only do this if the vnode is cloned -</span>
    <span class="hljs-comment">// if the new node is not cloned it means the render functions have been</span>
    <span class="hljs-comment">// reset by the hot-reload-api and we need to do a proper re-render.</span>
    <span class="hljs-keyword">if</span> (isTrue(vnode.isStatic) &&
      isTrue(oldVnode.isStatic) &&
      vnode.key === oldVnode.key &&
      (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
    ) &#123;
      vnode.componentInstance = oldVnode.componentInstance
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">let</span> i
    <span class="hljs-keyword">const</span> data = vnode.data
    <span class="hljs-keyword">if</span> (isDef(data) && isDef(i = data.hook) && isDef(i = i.prepatch)) &#123;
      i(oldVnode, vnode)
    &#125;

    <span class="hljs-keyword">const</span> oldCh = oldVnode.children
    <span class="hljs-keyword">const</span> ch = vnode.children
    <span class="hljs-keyword">if</span> (isDef(data) && isPatchable(vnode)) &#123;
      <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
      <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.update)) i(oldVnode, vnode)
    &#125;
    <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
      <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
        <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue, removeOnly)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
        <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
          checkDuplicateKeys(ch)
        &#125;
        <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) nodeOps.setTextContent(elm, <span class="hljs-string">''</span>)
        addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
        removeVnodes(oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
        nodeOps.setTextContent(elm, <span class="hljs-string">''</span>)
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
      nodeOps.setTextContent(elm, vnode.text)
    &#125;
    <span class="hljs-keyword">if</span> (isDef(data)) &#123;
      <span class="hljs-keyword">if</span> (isDef(i = data.hook) && isDef(i = i.postpatch)) i(oldVnode, vnode)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>patchVnode，主干逻辑：</p>
<ol>
<li>若 <strong>oldVNode</strong> 和 <strong>newVnode</strong> <strong>完全相等</strong>，则 直接 return，无需后续diff操作。</li>
<li>若 <strong>oldVNode</strong> 和 <strong>newVnode</strong>  <strong>不完全相等</strong>（仅满足 sameVnode函数的判等逻辑）:
<ol>
<li>将 <code>oldVNode.elm</code> 关联到 <code>newVNode.elm</code>上，使 <strong>newVnode</strong> 具有对应真实DOM的引用。</li>
<li>将<strong>oldVNode</strong> 和 <strong>newVNode</strong>的差异变化，更新到<strong>当前节点</strong>对应的真实DOM上。</li>
<li>深度diff<strong>当前节点</strong>的<strong>子节点</strong>。<strong>子节点的比较</strong>通过 <strong>updateChildren</strong> 函数来完成。稍后我们详细了解。</li>
</ol>
</li>
</ol>
<h3 data-id="heading-6">updateChildren （更新子节点）</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span> (<span class="hljs-params">parentElm, oldCh, newCh, insertedVnodeQueue, removeOnly</span>) </span>&#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]
    <span class="hljs-keyword">let</span> oldKeyToIdx, idxInOld, vnodeToMove, refElm

    <span class="hljs-comment">// removeOnly is a special flag used only by <transition-group></span>
    <span class="hljs-comment">// to ensure removed elements stay in correct relative positions</span>
    <span class="hljs-comment">// during leaving transitions</span>
    <span class="hljs-keyword">const</span> canMove = !removeOnly

    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      checkDuplicateKeys(newCh)
    &#125;

    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (isUndef(oldStartVnode)) &#123;
        oldStartVnode = oldCh[++oldStartIdx] <span class="hljs-comment">// Vnode has been moved left</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isUndef(oldEndVnode)) &#123;
        oldEndVnode = oldCh[--oldEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
        patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
        oldStartVnode = oldCh[++oldStartIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
        patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
        oldEndVnode = oldCh[--oldEndIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123; <span class="hljs-comment">// Vnode moved right</span>
        patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue, newCh, newEndIdx)
        canMove && nodeOps.insertBefore(parentElm, oldStartVnode.elm, nodeOps.nextSibling(oldEndVnode.elm))
        oldStartVnode = oldCh[++oldStartIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; <span class="hljs-comment">// Vnode moved left</span>
        patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
        canMove && nodeOps.insertBefore(parentElm, oldEndVnode.elm, oldStartVnode.elm)
        oldEndVnode = oldCh[--oldEndIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx)) oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
        idxInOld = isDef(newStartVnode.key)
          ? oldKeyToIdx[newStartVnode.key]
          : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
        <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// New element</span>
          createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
        &#125; <span class="hljs-keyword">else</span> &#123;
          vnodeToMove = oldCh[idxInOld]
          <span class="hljs-keyword">if</span> (sameVnode(vnodeToMove, newStartVnode)) &#123;
            patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
            oldCh[idxInOld] = <span class="hljs-literal">undefined</span>
            canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// same key but different element. treat as new element</span>
            createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
          &#125;
        &#125;
        newStartVnode = newCh[++newStartIdx]
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
      refElm = isUndef(newCh[newEndIdx + <span class="hljs-number">1</span>]) ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
      addVnodes(parentElm, refElm, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartIdx > newEndIdx) &#123;
      removeVnodes(oldCh, oldStartIdx, oldEndIdx)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对<strong>子节点的比较</strong>，是<strong>diff算法的关键</strong>。为了<strong>提升渲染效率</strong>。子元素集合<strong>diff</strong>的<strong>基本原则</strong>， 如下：</p>
<ol>
<li><strong>尽可能多的复用已经存在的DOM</strong>
<ol>
<li>改变位置</li>
<li>修改属性</li>
</ol>
</li>
<li><strong>尽可能少的创建或删除真实DOM</strong></li>
</ol>
<p>具体实现，通过源码可知：比较时，会分别为<strong>新旧子节点集合</strong>设置<strong>头尾两个指针</strong>，<strong>头尾指针</strong>根据「<strong>比较规则</strong>」，向中间移动，依次比较新旧各个子节点，并更新（修改、移动、创建、删除）对应的真实DOM。</p>
<h4 data-id="heading-7">diff原理图</h4>
<p>【<strong>子节点diff前</strong>】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab4c36521d4cd5ab4e0be7396237fd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>【<strong>子节点diff后</strong>】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d814ffe0dfc846e99c34783b8a170cbc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">diff比较规则</h4>
<p>结合上面<strong>原理图</strong>，整理<strong>diff比较规则</strong>如下：</p>
<ol>
<li>头（旧） 不存在， oldStart ++</li>
<li>尾（旧）不存在， oldEnd - -</li>
<li>头（旧）和 头（新）相等。
<ol>
<li>递归调用 <code>patchVnode</code>、</li>
<li>oldStart ++ 、newStart ++</li>
</ol>
</li>
<li>尾（旧）和 尾（新）相等。
<ol>
<li>递归调用 <code>patchVnode</code></li>
<li>oldEnd - -、 newEnd - -</li>
</ol>
</li>
<li>头（旧）和 尾 （新）相等。
<ol>
<li>递归调用 <code>patchVnode</code></li>
<li>「<strong>移动</strong>」<strong>当前节点对应DOM</strong> 到 <strong>oldEnd 指针对应DOM下一个Dom</strong>的 <strong>前边</strong> —— <strong>moved right</strong></li>
<li>oldStart ++ 、newEnd - -</li>
</ol>
</li>
<li>尾（旧）和 头（新）相等。
<ol>
<li>递归调用 <code>patchVnode</code></li>
<li>「<strong>移动</strong>」<strong>当前节点对应DOM</strong> 到 <strong>oldStart 指针 对应DOM</strong> 的 <strong>前边</strong> —— <strong>moved left</strong></li>
<li>oldEnd - - 、newStart ++</li>
</ol>
</li>
<li>遍历<strong>剩余oldVNodeChildren</strong>，将 <strong>key -> index</strong> 的映射关系，存储到一个 map中，通过 key值， 判断 <strong>头（新）<strong>是否在</strong>剩余oldVNodeChildren</strong>中。
【注意，没有key的节点，需要再次遍历<strong>剩余oldVNodeChildren</strong>通过 <code>sameVnode</code> 函数判断】
<ol>
<li>头（新）「不在」 <strong>剩余oldVNodeChildren</strong> 中，「<strong>创建元素</strong>」</li>
<li>头 （新）的 key「在」 <strong>剩余oldVNodeChildren</strong> 的某一个vnode中，需要进一步通过 <code>sameVnode</code>  函数判断<strong>匹配的旧节点</strong>和 **头（新）**是否「<strong>相同</strong>」
<ol>
<li>「<strong>相同</strong>」
<ol>
<li>递归调用 <code>patchVnode</code> 函数</li>
<li>从<strong>剩余oldVNodeChildren</strong>中删除<strong>匹配的旧节点</strong></li>
<li>「<strong>移动</strong>」**当前节点对应DOM **到 <strong>oldStart指针对应DOM</strong>  的前边 —— <strong>moved left</strong></li>
</ol>
</li>
<li>「<strong>不相同</strong>」，表明只是key相同，但不是同一个 element，需要 「<strong>创建元素</strong>」</li>
</ol>
</li>
</ol>
</li>
<li>头尾指针停止后，查看指针位置状态
<ol>
<li>若 oldStart > oldEnd， 表明 newVNodeChildren 存在未处理的节点，需要 <strong>遍历未处理节点</strong>，依次「<strong>创建元素</strong>」</li>
<li>若 newStart > newEnd，表明 oldVNodeChildren 存在未处理的节点，需要 <strong>遍历未处理节点</strong>，依次「<strong>销毁元素</strong>」</li>
</ol>
</li>
</ol>
<h2 data-id="heading-9">开发示例</h2>
<h3 data-id="heading-10">列表渲染 —— key值不可缺</h3>
<p><strong>示例代码</strong></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
    <div class="list-key">
        <h1>观察控制面板，列表渲染加不加 key 的区别？</h1>
        <ul>
            <!--eslint-disable-->
            <!-- 不加 key -->
            <!-- <li v-for="n in list">&#123;&#123; n &#125;&#125;</li> -->
            <!-- 加 key -->
            <li v-for="n in list" :key="n">&#123;&#123; n &#125;&#125;</li>
        </ul>
        <button @click="list.reverse()">反转数组</button> &nbsp;
        <button @click="list.unshift(10)">头部添加</button>
    </div>
</template>

<script>
export default &#123;
    data() &#123;
        return &#123;
            list: [1, 2, 3, 4, 5],
        &#125;;
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>图示</strong></p>
<p>列表反转 —— 不加 <strong>key</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e8a9b95474f4193a607c20dc8f1980f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>列表反转 —— 加 <strong>key</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03a3c01f38414d2ea93ad569b0c4af9f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>头部添加 —— 不加 <strong>key</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfb549cb1164d43aeabfcf1b1e2e84f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>头部添加 —— 加 <strong>key</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94519b20cc9845ebae2843f3d333a7d7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">总结</h2>
<p>通过分析源码，可以清晰了解Vue中 DOM-Diff的过程、DOM-Diff的核心：<strong>深度优先，同层比较</strong>。并结合开发示例，学习了在列表渲染中，添加 key 值可以有效的复用已存在的DOM，提升渲染效率。</p>
<h2 data-id="heading-12">交流</h2>
<p>如果这篇文章帮助到你，<strong>点赞</strong>和<strong>关注</strong>不失联，你的支持是对笔者最大的鼓励！</p>
<p>微信关注 「 乘风破浪大前端 」，发现更多有趣好玩的前端知识和实战。</p>
<p>干货系列文章汇总如下，欢迎 <strong>start</strong> 、<strong>follow</strong> 交流学习👏🏻。</p>
<blockquote>
<p><a href="https://github.com/szjxxy/fe-happy-interview" target="_blank" rel="nofollow noopener noreferrer">github.com/szjxxy/fe-h…</a></p>
</blockquote>
<p>关于本文如有任何意见或建议，欢迎评论区讨论和指正。</p>
<p>也许你还想看：</p>
<ol>
<li><a href="https://juejin.cn/post/6960965999021522952" target="_blank">【Vue2.0源码系列】：响应式原理</a></li>
<li><a href="https://github.com/szjxxy/fe-happy-interview/issues/9" target="_blank" rel="nofollow noopener noreferrer">【Vue2.0源码系列】：computed vs methods</a></li>
<li><a href="https://juejin.cn/post/6960560502971826206" target="_blank">【专题实战】：带你彻底搞懂BFC及其应用</a></li>
</ol>
<p>2a04e28b665ce3563aebf25~tplv-k3u1fbpfcp-zoom-1.image)</p></div>  
</div>
            