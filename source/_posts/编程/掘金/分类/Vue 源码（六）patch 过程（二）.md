
---
title: 'Vue 源码（六）patch 过程（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9011a5e886ef4a5387729c12d8d9d87f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 23:22:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9011a5e886ef4a5387729c12d8d9d87f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>接下来就是更新过程</p>
<p>修改响应式属性时，会通知订阅Watcher更新，从而触发组件重新渲染；首先还是执行组件<code>render</code>函数获取组件VNode，然后执行<code>_update</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode: VNode, hydrating?: boolean</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> prevEl = vm.$el <span class="hljs-comment">// dom 节点</span>
    <span class="hljs-comment">// 获取更新前的VNode</span>
    <span class="hljs-keyword">const</span> prevVnode = vm._vnode
    <span class="hljs-comment">// 设置 activeInstance 并返回一个匿名函数，匿名函数返回值是上一个 activeInstance 的值</span>
    <span class="hljs-keyword">const</span> restoreActiveInstance = setActiveInstance(vm)
    <span class="hljs-comment">// 当前 vue实例的 render 函数创建的 vnode</span>
    vm._vnode = vnode
    <span class="hljs-keyword">if</span> (!prevVnode) &#123;
      vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 更新</span>
      vm.$el = vm.__patch__(prevVnode, vnode)
    &#125;
    <span class="hljs-comment">// 将 activeInstance 的值设置成上一个 vm 实例</span>
    restoreActiveInstance()
    <span class="hljs-comment">// update __vue__ reference</span>
    <span class="hljs-keyword">if</span> (prevEl) &#123;
      prevEl.__vue__ = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">if</span> (vm.$el) &#123;
      vm.$el.__vue__ = vm
    &#125;
    <span class="hljs-keyword">if</span> (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) &#123;
      vm.$parent.$el = vm.$el
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比于初次渲染，更新过程中的<code>prevVnode</code>是有值的，值为更新前的VNode；所以会走<code>else</code>逻辑，<code>else</code>逻辑也是调用<code>vm.__patch__</code>函数，但是会传入<code>prevVnode</code>。注意这里会将<code>vm._vnode</code>设置成最新的VNode；</p>
<p>接着看<code>patch</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span> (<span class="hljs-params">oldVnode, vnode, hydrating, removeOnly</span>) </span>&#123;
    <span class="hljs-comment">// 新节点不存在，老节点存在，销毁老节点</span>
    <span class="hljs-keyword">if</span> (isUndef(vnode)) &#123;
      <span class="hljs-keyword">if</span> (isDef(oldVnode)) invokeDestroyHook(oldVnode)
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">let</span> isInitialPatch = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">const</span> insertedVnodeQueue = []
    <span class="hljs-keyword">if</span> (isUndef(oldVnode)) &#123;
      isInitialPatch = <span class="hljs-literal">true</span>
      createElm(vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">const</span> isRealElement = isDef(oldVnode.nodeType)
      <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
        patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (isRealElement) &#123;
          oldVnode = emptyNodeAt(oldVnode)
        &#125;

        <span class="hljs-keyword">const</span> oldElm = oldVnode.elm
        <span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)
        createElm(
          vnode,
          insertedVnodeQueue,
          oldElm._leaveCb ? <span class="hljs-literal">null</span> : parentElm,
          nodeOps.nextSibling(oldElm)
        )

        <span class="hljs-comment">// 更新 组件vnode 的 elm 并重新执行父组件的 cbs.create 和 insert hooks（不包含 mounted 钩子）</span>
        <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
          <span class="hljs-keyword">let</span> ancestor = vnode.parent
          <span class="hljs-keyword">const</span> patchable = isPatchable(vnode)
          <span class="hljs-keyword">while</span> (ancestor) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) &#123;
              cbs.destroy[i](ancestor)
            &#125;
            <span class="hljs-comment">// 更新 组件vnode 的 elm</span>
            ancestor.elm = vnode.elm
            <span class="hljs-keyword">if</span> (patchable) &#123;
              <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
                cbs.create[i](emptyNode, ancestor)
              &#125;
              <span class="hljs-keyword">const</span> insert = ancestor.data.hook.insert
              <span class="hljs-keyword">if</span> (insert.merged) &#123;
                <span class="hljs-comment">// 从 1 开始，因为第一个insert hook 是 mounted</span>
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
<p>更新过程中，<code>patch</code>函数会出现3种情况，分别是：</p>
<ul>
<li>当前组件第一次创建，比如父组件通过<code>v-if</code>控制子组件是否渲染</li>
<li>新老节点相同</li>
<li>新老节点不同</li>
</ul>
<p>至于第一种情况，和初次渲染流程相同，这里就不多赘述了。下面这种情况会走第一种逻辑</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cmp1</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"xxx"</span>></span>xxx<span class="hljs-tag"></<span class="hljs-name">cmp1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cmp2</span> <span class="hljs-attr">v-else</span>></span>yyy<span class="hljs-tag"></<span class="hljs-name">cmp2</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当修改<code>xxx</code>为<code>false</code>，会创建<code>cmp2</code>，此时 <code>cmp2</code> 的 <code>oldVNode</code> 为 <code>null</code>。也就是说如果组件在初次渲染挂载过，在更新阶段就有<code>oldVNode</code>，反之没有</p>
<p>而第二三种情况根据下面的逻辑判断</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// patch 函数内部</span>
<span class="hljs-comment">// oldVnode 不是真实节点，并且 sameVnode 返回 true</span>
<span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
  patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>sameVnode</code>函数</p>
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
<ul>
<li>对于同步组件，如果两个 <code>vnode</code> 的 <code>key</code> 不相等，则是不同的；如果<code>key</code>相同则继续判断 <code>isComment</code>、<code>data</code>、<code>input</code> 类型等是否相同</li>
<li>对于异步组件，如果两个 <code>vnode</code> 的 <code>key</code> 不相等，则是不同的；如果<code>key</code>相同则继续判断 <code>asyncFactory</code>是否相同</li>
</ul>
<h2 data-id="heading-0">新老节点相同</h2>
<p>当<code>!isRealElement && sameVnode(oldVnode, vnode)</code>成立，会执行<code>patchVnode</code>函数</p>
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
  <span class="hljs-comment">// 将 oldVnode.elm 赋值给 vnode.elm</span>
  <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm

  <span class="hljs-keyword">if</span> (isTrue(oldVnode.isAsyncPlaceholder)) &#123;
    <span class="hljs-keyword">if</span> (isDef(vnode.asyncFactory.resolved)) &#123;
      hydrate(oldVnode.elm, vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode.isAsyncPlaceholder = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;
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

  <span class="hljs-comment">// 全量更新节点的所有属性</span>
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
<p><code>patchVnode</code> 的作用就是 <strong>更新VNode的<code>elm</code>属性</strong>，也就是说接下来的过程其实就是修改DOM树的过程</p>
<p>他的逻辑是，如果两个节点相同则返回。反之，将 <code>oldVnode.elm</code> 赋值给 <code>vnode.elm</code>，给新VNode设置DOM树；如果VNode是组件占位符VNode，执行VNode的<code>prepatch</code>钩子函数去更新子组件；然后，获取新老节点的子节点；执行<code>cbs.update</code>里面的所有函数和VNode的<code>update</code>钩子函数，全量更新节点的所有属性；然后开始比对，如果新节点是文本节点且新旧文本不相同，则直接替换<code>elm</code>文本内容。如果新VNode不是文本节点，则判断它们的子节点，并分了几种情况处理：</p>
<ol>
<li>新老节点都有子节点，并且子节点不相同，使用<code>updateChildren</code>函数来更新子节点</li>
<li>如果只有新VNode有子节点，说明老节点要么是文本节点要么就是没有子节点；如果旧的节点是文本节点将节点的文本清除；然后通过 <code>addVnodes</code> 将新VNode的所有子节点批量插入到新节点 <code>elm</code> 下</li>
<li>如果只有老VNode有子节点，说明新VNode是空节点；则将老VNode的所有子节点通过<code>removeVnodes</code>全部清除</li>
<li>当只有旧节点是文本节点的时候，则清除其节点文本内容</li>
</ol>
<p>上述执行完之后，会执行<code>postpatch</code>钩子函数</p>
<h3 data-id="heading-1">updateChildren</h3>
<p>上面第一条中当新老节点都有子节点，并且子节点不相同时会调用<code>updateChildren</code>函数；看下<code>updateChildren</code>函数是怎么更新子节点的，其实这个就是一个递归过程，代码如下（可以直接看后面的解释部分就行）</p>
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
<p>首先会定义4个指针以及4个指针对应的VNode节点</p>
<ul>
<li><code>oldStartIdx</code>、<code>oldEndIdx</code>、<code>newStartIdx</code>、<code>newEndIdx</code>分别是新老两个VNode的两边索引</li>
<li><code>oldStartVnode</code>、<code>oldEndVnode</code>、<code>newStartVnode</code>、<code>newEndVnode</code>分别指向这几个索引对应的VNode节点</li>
</ul>
<p>然后是一个<code>while</code>循环，<code>oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx</code>；在这个过程中4个指针会逐渐向中间靠拢，直到老节点的开始索引大于老节点的结束索引或者新节点的开始索引大于新节点的结束索引时，<code>while</code>循环结束。</p>
<p><code>while</code>循环内的逻辑如下</p>
<ol>
<li><code>oldStartVnode</code> 没有的情况，<code>oldStartIdx</code>向中间靠拢，并更新<code>oldStartVnode</code>的值</li>
<li><code>oldEndVnode</code> 没有的情况，<code>oldEndIdx</code>向中间靠拢，并更新<code>oldEndVnode</code>的值</li>
<li><code>oldStartVnode</code> 和 <code>newStartVnode</code> 是相同节点，也就是两个节点的开头是相同的，调用<code>patchVnode</code>去更新子节点，子节点更新完成之后，将 <code>oldStartIdx</code> 与 <code>newStartIdx</code> 向后移动一位</li>
<li><code>oldEndVnode</code> 和 <code>newEndVnode</code> 是相同节点，也就是两个节点的结尾是相同的，同样进行 <code>patchVnode</code> 操作并将 <code>oldEndIdx</code> 与 <code>newEndVnode</code> 向前移动一位</li>
<li><code>oldStartVnode</code> 和 <code>newEndVnode</code> 是相同节点，也就是老节点的头部与新节点的尾部是同一节点时，调用<code>patchVnode</code>，更新子节点；子节点更新完成之后，将 <code>oldStartVnode.elm</code>移动到 <code>oldEndVnode.elm</code> 后面；然后 <code>oldStartIdx</code> 向后移动一位，<code>newEndIdx</code> 向前移动一位。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9011a5e886ef4a5387729c12d8d9d87f~tplv-k3u1fbpfcp-watermark.image" alt="diff1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li><code>oldEndVnode</code> 和 <code>newStartVnode</code> 是相同节点，也就是老节点的尾部与新节点的头部是同一节点的时候，调用<code>patchVnode</code>，更新子节点；子节点更新完成之后，将 <code>oldEndVnode.elm</code> 插入到 <code>oldStartVnode.elm</code> 前面；<code>oldEndIdx</code> 向前移动一位，<code>newStartIdx</code> 向后移动一位。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f60e29fb667446cabe39be144f164d62~tplv-k3u1fbpfcp-watermark.image" alt="diff2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>如果上述都没命中，进入下面的逻辑</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">else</span> &#123;
   <span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx)) oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
   idxInOld = isDef(newStartVnode.key)
     ? oldKeyToIdx[newStartVnode.key]
   : findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
   <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123;
     createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
   &#125; <span class="hljs-keyword">else</span> &#123;
     vnodeToMove = oldCh[idxInOld]
     <span class="hljs-keyword">if</span> (sameVnode(vnodeToMove, newStartVnode)) &#123;
       patchVnode(vnodeToMove, newStartVnode, insertedVnodeQueue, newCh, newStartIdx)
       oldCh[idxInOld] = <span class="hljs-literal">undefined</span>
       canMove && nodeOps.insertBefore(parentElm, vnodeToMove.elm, oldStartVnode.elm)
     &#125; <span class="hljs-keyword">else</span> &#123;
       createElm(newStartVnode, insertedVnodeQueue, parentElm, oldStartVnode.elm, <span class="hljs-literal">false</span>, newCh, newStartIdx)
     &#125;
   &#125;
   newStartVnode = newCh[++newStartIdx]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先通过<code>createKeyToOldIdx</code>获取<code>oldCh</code>中所有<code>key</code>，<code>&#123; [key的名字]: [在oldCh中的索引] &#125;</code>；如果<code>newStartVnode</code>有<code>key</code>，获取这个 <code>key</code> 在<code>oldCh</code>中的位置，并赋值给<code>idxInOld</code>；否则，遍历 <code>oldCh</code> ，查找和 <code>newStartVnode</code>相同的节点，如果找到了就返回对应的索引，并赋值给<code>idxInOld</code>。接下来逻辑如下：</p>
<ul>
<li>
<p>如果<code>idxInOld</code>为<code>undefined</code>，说明<code>newStartVnode</code>和<code>oldCh</code>中所有节点都不相同，调用<code>createElm</code>创建节点，并插入到<code>oldStartVnode.elm</code>前面。让<code>newStartIdx</code>往后一位，并更新<code>newStartVnode</code>的值</p>
</li>
<li>
<p>如果<code>idxInOld</code>有值，说明<code>newStartVnode</code>在<code>oldCh</code>中有一样的节点或者相同节点，获取这个节点，并再次通过<code>sameVnode</code>判断这个节点和<code>newStartVnode</code>是否相同</p>
<ul>
<li>如果相同调用<code>patchVnode</code>更新子节点，子节点更新完成后将这个节点从<code>oldCh</code>中删除，并将 <code>vnodeToMove.elm</code>（<code>oldCh[key].elm</code>）插到 <code>oldStartVnode.elm</code> 前面；让<code>newStartIdx</code>往后一位，并更新<code>newStartVnode</code>的值</li>
<li>如果不同，调用<code>createElm</code>创建节点，并插入到<code>oldStartVnode.elm</code>前面。让<code>newStartIdx</code>往后一位，并更新<code>newStartVnode</code>的值</li>
</ul>
</li>
</ul>
<p>当<code>while</code>循环结束会执行下面逻辑</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
  refElm = isUndef(newCh[newEndIdx + <span class="hljs-number">1</span>]) ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
  addVnodes(parentElm, refElm, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartIdx > newEndIdx) &#123;
  removeVnodes(oldCh, oldStartIdx, oldEndIdx)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果<code>oldStartIdx</code>大于<code>oldEndIdx</code>说明老节点先遍历完成。然后判断<code>newCh[newEndIdx + 1]</code>是否有值，如果有值说明剩余的新节点（<code>newStartIdx</code>到<code>newEndIdx</code>之间的节点）应该插入到<code>newCh[newEndIdx + 1].elm</code>前面；反之插入到最后</li>
<li>如果<code>newStartIdx</code>大于<code>newEndIdx</code>说明新节点先遍历完成。直接将<code>oldStartIdx</code>到<code>oldEndIdx</code>之间的所有节点全部删除</li>
</ul>
<h3 data-id="heading-2">prepatch钩子函数</h3>
<p>在<code>patchVnode</code>方法中，如果新VNode是组件占位符VNode，会调用VNode的<code>prepatch</code>钩子函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  prepatch (oldVnode: MountedComponentVNode, <span class="hljs-attr">vnode</span>: MountedComponentVNode) &#123;
    <span class="hljs-comment">// 获取组件占位符VNode的 options</span>
    <span class="hljs-keyword">const</span> options = vnode.componentOptions
    <span class="hljs-comment">// 获取组件实例</span>
    <span class="hljs-keyword">const</span> child = vnode.componentInstance = oldVnode.componentInstance
    updateChildComponent(
      child,
      options.propsData, <span class="hljs-comment">// updated props 传入子组件的最新的 props 值</span>
      options.listeners, <span class="hljs-comment">// updated listeners 自定义事件</span>
      vnode, <span class="hljs-comment">// new parent vnode</span>
      options.children <span class="hljs-comment">// new children</span>
    )
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>prepatch</code>钩子函数内调用<code>updateChildComponent</code>，并传入子组件实例、最新的<code>prop</code>数据、自定义事件、新VNode和子节点（通过<code>name</code>属性指定插槽内容的具名插槽）</p>
<p><code>updateChildComponent</code>函数如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildComponent</span> (<span class="hljs-params">
  vm: Component, <span class="hljs-comment">// 子组件实例</span>
  propsData: ?<span class="hljs-built_in">Object</span>,
  listeners: ?<span class="hljs-built_in">Object</span>,
  parentVnode: MountedComponentVNode, <span class="hljs-comment">// 组件 vnode</span>
  renderChildren: ?<span class="hljs-built_in">Array</span><VNode>
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    <span class="hljs-comment">// 设置成 true 的目的是，给 props[key] 赋值时，触发 set 方法，不会让 customSetter 函数报错</span>
    isUpdatingChildComponent = <span class="hljs-literal">true</span>
  &#125;

  <span class="hljs-keyword">const</span> newScopedSlots = parentVnode.data.scopedSlots
  <span class="hljs-keyword">const</span> oldScopedSlots = vm.$scopedSlots
  <span class="hljs-keyword">const</span> hasDynamicScopedSlot = !!(
    (newScopedSlots && !newScopedSlots.$stable) ||
    (oldScopedSlots !== emptyObject && !oldScopedSlots.$stable) ||
    (newScopedSlots && vm.$scopedSlots.$key !== newScopedSlots.$key)
  )


  <span class="hljs-keyword">const</span> needsForceUpdate = !!(
    renderChildren ||               <span class="hljs-comment">// has new static slots</span>
    vm.$options._renderChildren ||  <span class="hljs-comment">// has old static slots</span>
    hasDynamicScopedSlot
  )
  <span class="hljs-comment">// vm.$options._parentVnode 指向 新的 组件vnode</span>
  vm.$options._parentVnode = parentVnode
  <span class="hljs-comment">// vm.$vnode 指向 新的 组件vnode</span>
  vm.$vnode = parentVnode <span class="hljs-comment">// update vm's placeholder node without re-render</span>

  <span class="hljs-keyword">if</span> (vm._vnode) &#123; <span class="hljs-comment">// update child tree's parent</span>
    <span class="hljs-comment">// 更新 渲染vnode 的 parent</span>
    vm._vnode.parent = parentVnode
  &#125;
  vm.$options._renderChildren = renderChildren

  vm.$attrs = parentVnode.data.attrs || emptyObject
  vm.$listeners = listeners || emptyObject

  <span class="hljs-comment">// update props</span>
  <span class="hljs-comment">// 更新 props</span>
  <span class="hljs-keyword">if</span> (propsData && vm.$options.props) &#123;
    toggleObserving(<span class="hljs-literal">false</span>)
    <span class="hljs-comment">// 之前的 propsData</span>
    <span class="hljs-keyword">const</span> props = vm._props
    <span class="hljs-comment">// 子组件定义的 props 的属性集合</span>
    <span class="hljs-keyword">const</span> propKeys = vm.$options._propKeys || []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < propKeys.length; i++) &#123;
      <span class="hljs-keyword">const</span> key = propKeys[i]
      <span class="hljs-keyword">const</span> propOptions: any = vm.$options.props <span class="hljs-comment">// wtf flow?</span>
      <span class="hljs-comment">// 在这里修改props的值触发 组件更新</span>
      props[key] = validateProp(key, propOptions, propsData, vm)
    &#125;
    toggleObserving(<span class="hljs-literal">true</span>)
    vm.$options.propsData = propsData
  &#125;

  <span class="hljs-comment">// update listeners</span>
  listeners = listeners || emptyObject
  <span class="hljs-comment">// 获取上一次绑定的自定义事件</span>
  <span class="hljs-keyword">const</span> oldListeners = vm.$options._parentListeners
  <span class="hljs-comment">// 将此次的自定义事件赋值给 _parentListeners</span>
  vm.$options._parentListeners = listeners
  updateComponentListeners(vm, listeners, oldListeners)

  <span class="hljs-comment">// resolve slots + force update if has children</span>
  <span class="hljs-keyword">if</span> (needsForceUpdate) &#123;
    vm.$slots = resolveSlots(renderChildren, parentVnode.context)
    vm.$forceUpdate()
  &#125;

  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    <span class="hljs-comment">// 更新完成后，置为 false</span>
    isUpdatingChildComponent = <span class="hljs-literal">false</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于更新了VNode，那么VNode对应实例的一系列属性也会发生变化，包括<code>vm.$vnode</code>的更新、<code>slot</code>的更新，<code>listeners</code>的更新，<code>props</code>的更新等等。这些属性的更新会触发子组件更新，具体更新方式在对应文章中都会介绍，这里就不赘述了。</p>
<p>如果子组件需要更新，则将子组件的<code>Render Watcher</code>直接添加到正在执行的队列中等待执行，而不是调用<code>nextTick</code>，因为此时<code>queueWatcher</code>方法的<code>flushing</code>为<code>true</code>，会将子组件的<code>Render Watcher</code>添加到队列的正确位置上；<code>waiting</code>为<code>true</code>，不会调用<code>nextTick</code>方法。</p>
<p>添加到队列后，回到<code>patchVnode</code>函数，继续更新；当父组件更新完成后，根据队列中的顺序，更新子组件。</p>
<h2 data-id="heading-3">新老节点不同</h2>
<p>当<code>!isRealElement && sameVnode(oldVnode, vnode)</code>不成立时，会执行下面的逻辑</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
  <span class="hljs-comment">// patch existing root node</span>
  patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-keyword">if</span> (isRealElement) &#123;
    <span class="hljs-comment">// 根据 oldVnode（此时 oldVnode 是真实节点） 创建一个 vnode</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;
  <span class="hljs-comment">// 获取节点的 真实元素</span>
  <span class="hljs-keyword">const</span> oldElm = oldVnode.elm
  <span class="hljs-comment">// 获取 oldVnode 的 父节点</span>
  <span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)

  createElm(
    vnode,
    insertedVnodeQueue,
    oldElm._leaveCb ? <span class="hljs-literal">null</span> : parentElm,
    nodeOps.nextSibling(oldElm)
  )

  <span class="hljs-comment">// 更新 组件vnode 的 elm 并重新执行 cbs.create 和 父组件的 insert hooks（不包含 mounted 钩子）</span>
  <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
    <span class="hljs-keyword">let</span> ancestor = vnode.parent
    <span class="hljs-keyword">const</span> patchable = isPatchable(vnode)
    <span class="hljs-keyword">while</span> (ancestor) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) &#123;
        cbs.destroy[i](ancestor)
      &#125;
      <span class="hljs-comment">// 更新 组件vnode 的 elm</span>
      ancestor.elm = vnode.elm
      <span class="hljs-keyword">if</span> (patchable) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
          cbs.create[i](emptyNode, ancestor)
        &#125;
        <span class="hljs-keyword">const</span> insert = ancestor.data.hook.insert
        <span class="hljs-keyword">if</span> (insert.merged) &#123;
          <span class="hljs-comment">// 从 1 开始，因为第一个insert hook 是 mounted</span>
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

  <span class="hljs-keyword">if</span> (isDef(parentElm)) &#123;
    removeVnodes([oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.tag)) &#123;
    invokeDestroyHook(oldVnode)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和第一次创建相同，通过<code>createElm</code>创建节点，如果是组件占位符VNode，则调用<code>init</code>钩子函数创建组件实例，并执行组件的挂载过程。如果是普通VNode，创建节点，并调用<code>createChildren</code>创建子节点，将子节点插入到当前节点中。上述执行完成后，将当前节点插入父节点中。</p>
<p>回到<code>patch</code>函数，<strong>更新组件占位符VNode的<code>elm</code>属性</strong>，并重新执行<code>cbs.create</code>内的函数和组件占位符VNode的<code>insert</code>钩子函数（不包含<code>mounted</code>的钩子），最后 <strong>删除旧节点</strong>，返回最新的DOM树，并赋值给<code>vm.$el</code></p>
<p>执行<code>insert</code>钩子的目的是防止出现下面这种情况，如果在组件占位符VNode上有自定义指令，并且<code>insert</code>回调内绑定了DOM，如果不更新，一直绑定的是老DOM树，所以需要更新</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"xxx"</span>></span>xxx<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else</span>></span>yyy<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            