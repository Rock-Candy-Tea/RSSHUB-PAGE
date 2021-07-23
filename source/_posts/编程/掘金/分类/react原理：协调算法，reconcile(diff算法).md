
---
title: 'react原理：协调算法，reconcile(diff算法)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806716c6adee407e82416af853cdeae2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 07:07:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806716c6adee407e82416af853cdeae2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>讲解完函数组件和类组件是如何计算状态更新之后，这篇文章讲一下<code>reconcile</code>的流程，也就是我们俗称的<code>diff</code>算法。</p>
<blockquote>
<p><code>reconcile</code>就是构建<code>workInProgress</code>树的流程</p>
</blockquote>
<p>类组件的<code>diff</code>入口在<code>finishClassComponent</code>中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">finishClassComponent</span>(<span class="hljs-params">current, workInProgress, Component, shouldUpdate, hasContext, renderLanes</span>) </span>&#123;
  markRef(current, workInProgress);
  <span class="hljs-keyword">var</span> didCaptureError = (workInProgress.flags & DidCapture) !== NoFlags;

  <span class="hljs-keyword">if</span> (!shouldUpdate && !didCaptureError) &#123;
    <span class="hljs-comment">// 根据shouldComponentUpdate生命周期决定是否需要更新组件</span>
    <span class="hljs-keyword">if</span> (hasContext) &#123;
      invalidateContextProvider(workInProgress, Component, <span class="hljs-literal">false</span>);
    &#125;

    <span class="hljs-keyword">return</span> bailoutOnAlreadyFinishedWork(current, workInProgress, renderLanes);
  &#125;

  <span class="hljs-keyword">var</span> instance = workInProgress.stateNode;

  ReactCurrentOwner$<span class="hljs-number">1.</span>current = workInProgress;
  <span class="hljs-keyword">var</span> nextChildren;

  <span class="hljs-keyword">if</span> (didCaptureError && <span class="hljs-keyword">typeof</span> Component.getDerivedStateFromError !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 出现错误</span>
    nextChildren = <span class="hljs-literal">null</span>;
    &#123;
      stopProfilerTimerIfRunning();
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    &#123;
      setIsRendering(<span class="hljs-literal">true</span>);
      <span class="hljs-comment">// 执行render方法</span>
      nextChildren = instance.render();
      <span class="hljs-keyword">if</span> ( workInProgress.mode & StrictMode) &#123;
        <span class="hljs-comment">// 严格模式</span>
        disableLogs();
        <span class="hljs-keyword">try</span> &#123;
          instance.render();
        &#125; <span class="hljs-keyword">finally</span> &#123;
          reenableLogs();
        &#125;
      &#125;
      setIsRendering(<span class="hljs-literal">false</span>);
    &#125;
  &#125;

  workInProgress.flags |= PerformedWork;

  <span class="hljs-keyword">if</span> (current !== <span class="hljs-literal">null</span> && didCaptureError) &#123;
    forceUnmountCurrentAndReconcile(current, workInProgress, nextChildren, renderLanes);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// diff的入口</span>
    reconcileChildren(current, workInProgress, nextChildren, renderLanes);
  &#125;

  workInProgress.memoizedState = instance.state;

  <span class="hljs-keyword">if</span> (hasContext) &#123;
    invalidateContextProvider(workInProgress, Component, <span class="hljs-literal">true</span>);
  &#125;

  <span class="hljs-keyword">return</span> workInProgress.child;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于函数组件，会在<code>updateFunctionComponent</code>中，<code>renderWithHooks</code>之后，调用<code>reconcileChildren</code>进入<code>diff</code></p>
<h2 data-id="heading-0">入口函数</h2>
<p><code>reconcileChildren</code>方法定义如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildren</span>(<span class="hljs-params">current, workInProgress, nextChildren, renderLanes</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (current === <span class="hljs-literal">null</span>) &#123;
    workInProgress.child = mountChildFibers(workInProgress, <span class="hljs-literal">null</span>, nextChildren, renderLanes);
  &#125; <span class="hljs-keyword">else</span> &#123;
    workInProgress.child = reconcileChildFibers(workInProgress, current.child, nextChildren, renderLanes);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当组件是初次加载时，会执行<code>mountChildFibers</code>方法，更新时执行<code>reconcileChildFibers</code>，这两个方法定义如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> reconcileChildFibers = ChildReconciler(<span class="hljs-literal">true</span>);
<span class="hljs-keyword">var</span> mountChildFibers = ChildReconciler(<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看<code>ChildReconciler</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ChildReconciler</span>(<span class="hljs-params">shouldTrackSideEffects</span>) </span>&#123;
    <span class="hljs-comment">// ... </span>
    <span class="hljs-keyword">return</span> reconcileChildFibers
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>shouldTrackSideEffects</code>表示是否有副作用。当组件初次挂载时，显然是没有副作用的，而组件更新可能会涉及到元素的删除，插入等操作，因此<code>shouldTrackSideEffects</code>为<code>true</code>。接下来看这个方法的返回值：<code>reconcileChildFibers</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildFibers</span>(<span class="hljs-params">returnFiber, currentFirstChild, newChild, lanes</span>) </span>&#123;
    <span class="hljs-keyword">var</span> isUnkeyedTopLevelFragment = <span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span> && newChild.type === REACT_FRAGMENT_TYPE && newChild.key === <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">if</span> (isUnkeyedTopLevelFragment) &#123;
      newChild = newChild.props.children;
    &#125;

    <span class="hljs-keyword">var</span> isObject = <span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">if</span> (isObject) &#123;
      <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
        <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE:
          <span class="hljs-keyword">return</span> placeSingleChild(reconcileSingleElement(returnFiber, currentFirstChild, newChild, lanes));
      &#125;
        <span class="hljs-comment">// ...</span>
    &#125;
    
    <span class="hljs-comment">// ...</span>

    <span class="hljs-keyword">if</span> (isArray$<span class="hljs-number">1</span>(newChild)) &#123;
      <span class="hljs-keyword">return</span> reconcileChildrenArray(returnFiber, currentFirstChild, newChild, lanes);
    &#125;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法会根据不同的节点类型来进行对应的<code>diff</code>操作：比如对于单个react元素，会执行<code>reconcileSingleElement</code>，对于多个元素，执行<code>reconcileChildrenArray</code>。这也就是单节点<code>diff</code>和多节点<code>diff</code>，下面就会分析这两种算法流程。再开始分析之前，先看一下<code>reconcileChildFibers</code>的参数：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806716c6adee407e82416af853cdeae2~tplv-k3u1fbpfcp-watermark.image" alt="reconcileChildFibers参数.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>diff算法的对象：老的fiber树和render方法返回的jsx</p>
</blockquote>
<blockquote>
<p>下文中老<code>fiber</code>指<code>current</code>树某一层的fiber链表，新<code>fiber</code>指<code>workInProgress</code>树要构建出的<code>fiber</code>链表，新<code>jsx</code>指<code>render</code>方法返回的<code>react</code>元素</p>
</blockquote>
<h2 data-id="heading-1">单节点diff</h2>
<p>单节点<code>diff</code>是指新的节点为单个节点时的<code>diff</code>流程。单节点<code>diff</code>由三种可能的情况：</p>
<ol>
<li>老<code>fiber</code>为空</li>
<li>老<code>fiber</code>有一个节点</li>
<li>老<code>fiber</code>有多个节点</li>
</ol>
<p>单节点<code>diff</code>比较简单，只需要在老<code>fiber</code>中找到<code>key</code>和<code>type</code>与新的<code>jsx</code>节点都相同节点，然后删除剩余老节点即可。如果找不到，删除所有老节点，创建新的节点。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileSingleElement</span>(<span class="hljs-params">returnFiber, currentFirstChild, element, lanes</span>) </span>&#123;
    <span class="hljs-keyword">var</span> key = element.key;
    <span class="hljs-keyword">var</span> child = currentFirstChild;
    <span class="hljs-comment">// 循环currentFirstChild这一层的所有老fiber节点</span>
    <span class="hljs-keyword">while</span> (child !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">if</span> (child.key === key) &#123;
        <span class="hljs-keyword">switch</span> (child.tag) &#123;
          <span class="hljs-comment">// ...</span>
          <span class="hljs-attr">default</span>:
            &#123;
              <span class="hljs-keyword">if</span> (child.elementType === element.type || (
               isCompatibleFamilyForHotReloading(child, element) )) &#123;
                <span class="hljs-comment">// 因为是单节点diff，所以找到key和type均相同的节点后，直接删除所有剩余节点即可</span>
                deleteRemainingChildren(returnFiber, child.sibling);
<span class="hljs-comment">// 根据老fiber创建新fiber</span>
                <span class="hljs-keyword">var</span> _existing3 = useFiber(child, element.props);
                _existing3.ref = coerceRef(returnFiber, child, element);
                _existing3.return = returnFiber;
<span class="hljs-comment">// 。。。</span>
                <span class="hljs-comment">// 当找到key和type均相同的节点时，直接return新fiber</span>
                <span class="hljs-keyword">return</span> _existing3;
              &#125;
              <span class="hljs-keyword">break</span>;
            &#125;
        &#125;
<span class="hljs-comment">// key相同，但是type不同</span>
        deleteRemainingChildren(returnFiber, child);
        <span class="hljs-keyword">break</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// key不同，直接删除遍历到的老fiber</span>
        deleteChild(returnFiber, child);
      &#125;
      child = child.sibling;
    &#125;
    <span class="hljs-comment">// 当没有找到key和type均相同的节点时，根据jsx创建新fiber</span>
    <span class="hljs-keyword">if</span> (element.type === REACT_FRAGMENT_TYPE) &#123;
      <span class="hljs-keyword">var</span> created = createFiberFromFragment(element.props.children, returnFiber.mode, lanes, element.key);
      created.return = returnFiber;
      <span class="hljs-keyword">return</span> created;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">var</span> _created4 = createFiberFromElement(element, returnFiber.mode, lanes);

      _created4.ref = coerceRef(returnFiber, currentFirstChild, element);
      _created4.return = returnFiber;
      <span class="hljs-keyword">return</span> _created4;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意几个点：</p>
<ol>
<li>
<p>在执行<code>deleteChild</code>（<code>deleteRemainingChildren</code>内也会调用<code>deleteChild</code>）时会为要删除的就<code>fiber</code>打上<code>Deletion</code>的<code>tag</code>，表示这个旧的节点要被删除(注意，并不是真的删除这个节点，而是打上<code>tag</code>)。</p>
</li>
<li>
<p>如果要被删除的节点还有子节点，只会在要被删除的节点上打上<code>tag</code>，不会在其子节点上打<code>tag</code></p>
</li>
<li>
<p>当找到可复用的<code>fiber</code>节点时(key和type相同)，会创建一个新的<code>fiber</code>节点，并建立新的<code>fiber</code>节点和旧的<code>fiber</code>节点之间的联系，即设置<code>alternate</code>属性。但是当不能复用时，新旧<code>fiber</code>之间的<code>alternate</code>连接是不存在的。</p>
</li>
<li>
<p>细心的同学可能发现了，既然旧<code>fiber</code>会被打上<code>Deletion</code>的tag，那么新<code>fiber</code>节点呢？注意<code>reconcileChildFibers</code>有这样的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> placeSingleChild(reconcileSingleElement(returnFiber, currentFirstChild, newChild, lanes));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>placeSingleChild</code>方法中才会对新增的节点打上<code>Placement</code>的tag</p>
</li>
</ol>
<blockquote>
<p>单节点<code>diff</code>的流程还是比较简单的，这里再强调一个概念：<code>fiber</code>复用：所谓复用<code>fiber</code>，并非直接使用老的<code>fiber</code>对象，而是要新建一个<code>workInProgress</code>树的<code>fiber</code>对象，新对象中的属性变为新<code>jsx</code>中的属性。而复用<code>fiber</code>的条件是<code>key</code>和<code>type</code>均相同。当发生<code>fiber</code>复用时，新老<code>fiber</code>节点之间会用<code>alternate</code>连接；而不发生<code>fiber</code>复用时，新老<code>fiber</code>之间是不存在相互引用的。这一点非常重要。</p>
</blockquote>
<h2 data-id="heading-2">多节点diff</h2>
<p>单节点diff看完后，来看一下多节点diff。回到<code>reconcileChildFibers</code>方法，这里会做一个特殊处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildFibers</span>(<span class="hljs-params">returnFiber, currentFirstChild, newChild, lanes</span>) </span>&#123;
    <span class="hljs-keyword">var</span> isUnkeyedTopLevelFragment = <span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span> && newChild.type === REACT_FRAGMENT_TYPE && newChild.key === <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 如果新的jsx节点是没有key的Fragment节点，则取出它的children</span>
    <span class="hljs-keyword">if</span> (isUnkeyedTopLevelFragment) &#123;
      newChild = newChild.props.children;
    &#125;
    <span class="hljs-comment">// 多节点diff</span>
    <span class="hljs-keyword">if</span> (isArray$<span class="hljs-number">1</span>(newChild)) &#123;
      <span class="hljs-keyword">return</span> reconcileChildrenArray(returnFiber, currentFirstChild, newChild, lanes);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，多节点diff就是新的<code>jsx</code>存在多个节点时的diff策略。</p>
<p>这里首先说明一下，<code>react</code>的<code>diff</code>策略并不是不惜代价地复用节点，而是在保证效率的基础上进行复用。比如一个组件发生了跨层级的移动，虽然只是位置上的变化，但是<code>react</code>则不会复用这个节点，这一点很多文章里也讲过，就不展开了。下面讲解一下<code>react</code>的多节点<code>diff</code>策略。</p>
<blockquote>
<p>下文中老<code>fiber</code>指<code>current</code>树某一层的fiber链表，新<code>fiber</code>指<code>workInProgress</code>树要构建出的<code>fiber</code>链表，新<code>jsx</code>指<code>render</code>方法返回的<code>react</code>元素</p>
</blockquote>
<p>首先是几个变量</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> resultingFirstChild = <span class="hljs-literal">null</span>;   <span class="hljs-comment">// 新fiber链表中的第一个fiber节点</span>

<span class="hljs-keyword">var</span> newIdx = <span class="hljs-number">0</span>;                   <span class="hljs-comment">// 用于循环新jsx数组中的指针</span>
<span class="hljs-keyword">var</span> previousNewFiber = <span class="hljs-literal">null</span>;      <span class="hljs-comment">// 新fiber链表中，当前fiber的前一个fiber</span>

<span class="hljs-keyword">var</span> oldFiber = currentFirstChild; <span class="hljs-comment">// 用于循环旧fiber节点的指针</span>
<span class="hljs-keyword">var</span> nextOldFiber = <span class="hljs-literal">null</span>;          <span class="hljs-comment">// 老fiber链表中，当前fiber的下一个fiber</span>

<span class="hljs-comment">// 老fiber树中最靠右的一个不需要移动的fiber节点，在老fiber树中的位置，下文会讲到</span>
<span class="hljs-keyword">var</span> lastPlacedIndex = <span class="hljs-number">0</span>;          
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">第一部分</h3>
<p>首先看多节点diff的第一部分：针对节点更新的循环</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 循环新fiber和老fiber</span>
<span class="hljs-keyword">for</span> (; oldFiber !== <span class="hljs-literal">null</span> && newIdx < newChildren.length; newIdx++) &#123;
  <span class="hljs-keyword">if</span> (oldFiber.index > newIdx) &#123;
    nextOldFiber = oldFiber;
    oldFiber = <span class="hljs-literal">null</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    nextOldFiber = oldFiber.sibling;
  &#125;
  <span class="hljs-comment">// 更新fiber节点</span>
  <span class="hljs-comment">// 如果新的jsx返回null，或者新老fiber的key不同，updateSlot返回null</span>
  <span class="hljs-comment">// 如果新老fiber的key相同，但是type不同，或者老fiber不存在，说明fiber不能复用(注意前文提到的fiber复用的含义)</span>
  <span class="hljs-comment">// 如果新老fiber都存在，并且能够复用，则复用fiber</span>
  <span class="hljs-keyword">var</span> newFiber = updateSlot(returnFiber, oldFiber, newChildren[newIdx], lanes);
  <span class="hljs-comment">// newFiber为null时，直接跳出循环</span>
  <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
      oldFiber = nextOldFiber;
    &#125;
    <span class="hljs-keyword">break</span>;
  &#125;
  <span class="hljs-comment">// 组件更新，shouldTrackSideEffects为true</span>
  <span class="hljs-comment">// 组件挂载，shouldTrackSideEffects为false，前文有提到</span>
  <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
    <span class="hljs-comment">// 如果没有发生fiber复用，说明老fiber被删除</span>
    <span class="hljs-keyword">if</span> (oldFiber && newFiber.alternate === <span class="hljs-literal">null</span>) &#123;
      deleteChild(returnFiber, oldFiber);
    &#125;
  &#125;
  <span class="hljs-comment">// 确定新fiber的位置，placeChild方法下文会单独讲</span>
  lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
  <span class="hljs-comment">// 记录新fiber中的第一个节点</span>
  <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
    resultingFirstChild = newFiber;
  &#125; <span class="hljs-keyword">else</span> &#123;
    previousNewFiber.sibling = newFiber;
  &#125;
  previousNewFiber = newFiber;
  oldFiber = nextOldFiber;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39ea3b259054a00ae02ad5e35d57536~tplv-k3u1fbpfcp-watermark.image" alt="多节点diff第一部分.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，只有在新的<code>jsx</code>返回<code>null</code>，或者新老<code>fiber</code>的<code>key</code>不同时，才会中途跳出循环。如果中途跳出了循环，会跳过下文的第二和第三部分，直接进入第四部分</p>
<h3 data-id="heading-4">第二部分</h3>
<p>如果循环正常结束，没有中途跳出，会进入第二部分：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 如果新fiber遍历完毕，直接删除旧fiber中的剩余节点即可，并返回resultingFirstChild</span>
<span class="hljs-keyword">if</span> (newIdx === newChildren.length) &#123;
  deleteRemainingChildren(returnFiber, oldFiber);
  <span class="hljs-keyword">return</span> resultingFirstChild;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">第三部分</h3>
<p>接下来是第三部分：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 如果老fiber遍历结束，则剩余的新fiber都是新增节点，直接新增即可</span>
<span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
  <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
    <span class="hljs-keyword">var</span> _newFiber = createChild(returnFiber, newChildren[newIdx], lanes);
    <span class="hljs-keyword">if</span> (_newFiber === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">continue</span>;
    &#125;
    <span class="hljs-comment">// 放置新增节点</span>
    lastPlacedIndex = placeChild(_newFiber, lastPlacedIndex, newIdx);
    <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
      resultingFirstChild = _newFiber;
    &#125; <span class="hljs-keyword">else</span> &#123;
      previousNewFiber.sibling = _newFiber;
    &#125;
    previousNewFiber = _newFiber;
  &#125;
  <span class="hljs-keyword">return</span> resultingFirstChild;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意，如果第一部分的循环中途退出，则新旧<code>fiber</code>都不会遍历完毕，因此是不会进入第二和第三部分的，而是会直接进入第四部分。</p>
<h3 data-id="heading-6">第四部分</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 首先将老fiber链表中没有遍历到的剩余节点放到一个map中，key是fiber的key或者在老fiber链表中的位置索引，value是fiber节点</span>
<span class="hljs-keyword">var</span> existingChildren = mapRemainingChildren(returnFiber, oldFiber);

<span class="hljs-comment">// 循环新的jsx数组中的剩余部分</span>
<span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
  <span class="hljs-comment">// 如果新的jsx返回null，updateFromMap返回null，跳过本轮循环</span>
  <span class="hljs-comment">// 新jsx不返回null，从existingChildren中找到与新jsx的key相同的老fiber，看是否能够复用fiber</span>
  <span class="hljs-keyword">var</span> _newFiber2 = updateFromMap(existingChildren, returnFiber, newIdx, newChildren[newIdx], lanes);

  <span class="hljs-keyword">if</span> (_newFiber2 !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
      <span class="hljs-keyword">if</span> (_newFiber2.alternate !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// 当新fiber非空，并且新fiber复用了老fiber，说明新老fiber存在对应关系，从existingChildren中删除老fiber</span>
        existingChildren.delete(_newFiber2.key === <span class="hljs-literal">null</span> ? newIdx : _newFiber2.key);
      &#125;
    &#125;
    <span class="hljs-comment">// 放置新fiber</span>
    lastPlacedIndex = placeChild(_newFiber2, lastPlacedIndex, newIdx);
    <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
      resultingFirstChild = _newFiber2;
    &#125; <span class="hljs-keyword">else</span> &#123;
      previousNewFiber.sibling = _newFiber2;
    &#125;
    previousNewFiber = _newFiber2;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cacd3a70f3142e5b1badca77a53ce08~tplv-k3u1fbpfcp-watermark.image" alt="多节点diff第四部分.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">第五部分</h3>
<p>最后还有一个收尾工作，遍历<code>existingChildren</code>，删除掉其中的旧<code>fiber</code>节点，并返回新<code>fiber</code>链表的第一个节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
  existingChildren.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">child</span>) </span>&#123;
    <span class="hljs-keyword">return</span> deleteChild(returnFiber, child);
  &#125;);
&#125;

<span class="hljs-keyword">return</span> resultingFirstChild;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，<code>beginWork</code>就会拿到这个函数的返回值，并返回到<code>performUnitOfWork</code>中，用来修改全局变量<code>workInProgress</code>，从而继续执行<code>workLoopSync</code>循环。</p>
<h2 data-id="heading-8">placeChild方法</h2>
<p><code>placeChild</code>是用来确定新<code>fiber</code>节点在新<code>fiber</code>链表中的位置，并返回前文中提到的<code>lastPlacedIndex</code>。接下来看一下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">placeChild</span>(<span class="hljs-params">newFiber, lastPlacedIndex, newIndex</span>) </span>&#123;
    <span class="hljs-comment">// 确定新fiber节点的位置索引</span>
    newFiber.index = newIndex;
    <span class="hljs-keyword">if</span> (!shouldTrackSideEffects) &#123;
      <span class="hljs-comment">// 不采取任何操作</span>
      <span class="hljs-keyword">return</span> lastPlacedIndex;
    &#125;
    <span class="hljs-keyword">var</span> current = newFiber.alternate;
    <span class="hljs-keyword">if</span> (current !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-comment">// current不为null，说明新老fiber有关联</span>
      <span class="hljs-keyword">var</span> oldIndex = current.index;
      <span class="hljs-keyword">if</span> (oldIndex < lastPlacedIndex) &#123;
        <span class="hljs-comment">// 老fiber在lastPlacedIndex左边，无需更新lastPlacedIndex</span>
        newFiber.flags = Placement;
        <span class="hljs-keyword">return</span> lastPlacedIndex;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 老fiber在lastPlacedIndex的右边，说明在新fiber链表中，对应节点发生了移动</span>
        <span class="hljs-keyword">return</span> oldIndex;
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// current为null，说明新老fiber没有关联，直接插入新fiber</span>
      newFiber.flags = Placement;
      <span class="hljs-keyword">return</span> lastPlacedIndex;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面举个例子：</p>
<pre><code class="hljs language-js copyable" lang="js">旧fiber链表
A -> B -> C -> D -> E
新fiber链表
A -> B -> D -> E -> C
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>当<code>newIndex</code>为0，进入第一部分的循环，执行到<code>placeChild</code>方法，由于新老<code>fiber</code>节点存在关联，因此<code>current</code>不为空，而<code>oldIndex</code>和<code>lastPlacedIndex</code>都是0，因此返回了<code>oldIndex</code></li>
<li>当<code>newIndex</code>为1，和第一步流程相同，也返回了<code>oldIndex(1)</code>，<code>lastPlacedIndex</code>变为1</li>
<li>当<code>newIndex</code>为2，跳出第一部分的循环，进入第四部分，执行到<code>placeChild</code>方法，<code>newFiber</code>为D节点，<code>current</code>为老<code>fiber</code>链表的D节点，因此<code>current</code>不为空，<code>oldIndex</code>为3，<code>lastPlacedIndex</code>为1，因此返回3，<code>lastPlacedIndex</code>变为3</li>
<li>当<code>newIndex</code>为3，和第3步流程相同，<code>lastPlacedIndex</code>变为4</li>
<li>当<code>newIndex</code>为4，执行到<code>placeChild</code>方法，<code>newFiber</code>为C节点，<code>current</code>为老<code>fiber</code>链表的C节点，<code>current</code>不为空，<code>oldIndex</code>为2，<code>lastPlacedIndex</code>为4，此时<code>oldIndex</code>小于<code>lastPlacedIndex</code>，因此<code>react</code>认为C节点发生了移动，为其打上Placement的tag</li>
</ol>
<p>因此，<code>lastPlacedIndex</code>的含义就是：在老<code>fiber</code>链表中，最靠右的一个不需要移动的<code>fiber</code>节点，在老<code>fiber</code>链表中的位置索引。</p>
<p>最后再来个整体的流程图吧</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91a14036cfd6454886dcc38246196d61~tplv-k3u1fbpfcp-watermark.image" alt="react-reconcile整体流程jpg.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            