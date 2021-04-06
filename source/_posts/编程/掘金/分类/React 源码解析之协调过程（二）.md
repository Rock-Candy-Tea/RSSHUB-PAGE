
---
title: 'React 源码解析之协调过程（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9dc07f4ce5e44948d109954623af890~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 23:21:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9dc07f4ce5e44948d109954623af890~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>说明：本文结论均基于 React 17.0.2 得出，若有出入请参考对应版本源码</p>
</blockquote>
<h1 data-id="heading-0">引言</h1>
<p><a href="https://juejin.cn/post/6929423413832335367" target="_blank">上篇文章</a>介绍了 React 协调过程中 <code>beginWork</code> 阶段的前半部分，这篇文章我们来介绍后半部分。</p>
<h1 data-id="heading-1">beginWork</h1>
<p>同样的，我们还是精简一下代码，只关注感兴趣的部分：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">
  current: Fiber | <span class="hljs-literal">null</span>,
  workInProgress: Fiber,
  renderLanes: Lanes,
</span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
  ...
  workInProgress.lanes = NoLanes;
  <span class="hljs-keyword">switch</span> (workInProgress.tag) &#123;
    <span class="hljs-keyword">case</span> IndeterminateComponent:
    ...
    <span class="hljs-keyword">case</span> LazyComponent:
    ...
    <span class="hljs-keyword">case</span> FunctionComponent:
    ...
    <span class="hljs-keyword">case</span> ClassComponent:
    ...
    <span class="hljs-keyword">case</span> HostRoot:
    ...
    <span class="hljs-keyword">case</span> HostComponent:
    ...
    <span class="hljs-keyword">case</span> HostText:
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先会通过 <code>workInProgress.tag</code> 来判断当前处理的 <code>FiberNode</code> 是哪种类型，并针对不同的类型调用不同的 update 方法。这些方法虽然名字差别很大，但是最后都逃不过这两句代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  reconcileChildren(current, workInProgress, nextChildren, renderLanes);
  <span class="hljs-keyword">return</span> workInProgress.child;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>workInProgress</code> 为当前正在处理的 <code>FiberNode</code>，<code>current</code> 即为上一次更新的与 <code>workInProgress</code> 配对的 <code>FiberNode</code>（有可能不存在），<code>nextChildren</code> 是这次更新的 <code>workInProgress</code> 下新的子节点（ <code>ReactElement</code> 数组），<code>renderLanes</code> 则是跟更新优先级相关。</p>
<p>接下来看看 <code>reconcileChildren</code> 做了什么：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildren</span>(<span class="hljs-params">
  current: Fiber | <span class="hljs-literal">null</span>,
  workInProgress: Fiber,
  nextChildren: any,
  renderLanes: Lanes,
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (current === <span class="hljs-literal">null</span>) &#123;
    workInProgress.child = mountChildFibers(
      workInProgress,
      <span class="hljs-literal">null</span>,
      nextChildren,
      renderLanes,
    );
  &#125; <span class="hljs-keyword">else</span> &#123;
    workInProgress.child = reconcileChildFibers(
      workInProgress,
      current.child,
      nextChildren,
      renderLanes,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>reconcileChildren</code> 中根据 <code>current</code> 是否存在来决定是应该 <code>mountChildFibers</code> 还是 <code>reconcileChildFibers</code>，这两个方法其实是类似的，只是 <code>reconcileChildFibers</code> 时 <code>shouldTrackSideEffects</code> 为 true，会多做一些事情：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ChildReconciler</span>(<span class="hljs-params">shouldTrackSideEffects</span>) </span>&#123;
  ...
  <span class="hljs-keyword">return</span> reconcileChildFibers;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> reconcileChildFibers = ChildReconciler(<span class="hljs-literal">true</span>);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> mountChildFibers = ChildReconciler(<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这里暂时只看 <code>reconcileChildFibers</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildFibers</span>(<span class="hljs-params">
  returnFiber: Fiber,
  currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
  newChild: any,
  lanes: Lanes,
</span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
  ...
  <span class="hljs-comment">// Handle object types</span>
  <span class="hljs-keyword">const</span> isObject = <span class="hljs-keyword">typeof</span> newChild === <span class="hljs-string">'object'</span> && newChild !== <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">if</span> (isObject) &#123;
    <span class="hljs-keyword">switch</span> (newChild.$$typeof) &#123;
      <span class="hljs-keyword">case</span> REACT_ELEMENT_TYPE:
        <span class="hljs-keyword">return</span> placeSingleChild(
          reconcileSingleElement(
            returnFiber,
            currentFirstChild,
            newChild,
            lanes,
          ),
        );
      ...
    &#125;
  &#125;

  ...
  <span class="hljs-keyword">if</span> (isArray(newChild)) &#123;
    <span class="hljs-keyword">return</span> reconcileChildrenArray(
      returnFiber,
      currentFirstChild,
      newChild,
      lanes,
    );
  &#125;

  ...
  <span class="hljs-comment">// Remaining cases are all treated as empty.</span>
  <span class="hljs-keyword">return</span> deleteRemainingChildren(returnFiber, currentFirstChild);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>reconcileChildFibers</code> 中根据 <code>newChild</code> 的类型来进行不同的处理，我们这里去掉了暂时不关心的部分，仅分析 <code>newChild</code> 为对象且是 <code>REACT_ELEMENT_TYPE</code> 或者 <code>newChild</code> 为数组的情形。事实上 <code>reconcileChildFibers</code> 就涉及到了 React 中面试常考的 Diff 算法，接下来我们深入研究一下。</p>
<h1 data-id="heading-2">Diff 算法</h1>
<h2 data-id="heading-3">Diff 的是什么？</h2>
<p>首先，需要知道的第一个问题是：Diff 算法到底 Diff 的是哪两个东西？是旧的 <code>FiberNode</code> 和 新的 <code>FiberNode</code>？答案是 No。</p>
<p>从上面的代码可知，传入 <code>reconcileChildFibers</code> 的是 <code>current.child</code> 和 <code>nextChildren</code>，所以 Diff 算法 其实是比较旧的 <code>FiberNode</code> 和新的 <code>ReactElement</code> 来生成新的 <code>FiberNode</code> 的一个过程：</p>
<p><img alt="diff-what.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9dc07f4ce5e44948d109954623af890~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Diff 分类</h2>
<p>根据 Diff 时 <code>ReactElement</code> 的类型，我们可以把 Diff 算法分为：</p>
<ul>
<li>单节点 Diff（reconcileSingleElement）：<code>ReactElement</code> 是对象。</li>
<li>多节点 Diff（reconcileChildrenArray）：<code>ReactElement</code> 是数组。</li>
</ul>
<p><img alt="diff-2-types.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/362180e6d01c443d88c00eac0b31e1a4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">单节点 Diff</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileSingleElement</span>(<span class="hljs-params">
    returnFiber: Fiber,
    currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
    element: ReactElement,
    lanes: Lanes,
  </span>): <span class="hljs-title">Fiber</span> </span>&#123;
    <span class="hljs-keyword">const</span> key = element.key;
    <span class="hljs-keyword">let</span> child = currentFirstChild;
    <span class="hljs-keyword">while</span> (child !== <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">if</span> (child.key === key) &#123;
        <span class="hljs-keyword">const</span> elementType = element.type;
        <span class="hljs-keyword">if</span> (elementType === REACT_FRAGMENT_TYPE) &#123;
          ...
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-keyword">if</span> (
            child.elementType === elementType ||
            <span class="hljs-comment">// Keep this check inline so it only runs on the false path:</span>
            (__DEV__
              ? isCompatibleFamilyForHotReloading(child, element)
              : <span class="hljs-literal">false</span>) ||
            (enableLazyElements &&
              <span class="hljs-keyword">typeof</span> elementType === <span class="hljs-string">'object'</span> &&
              elementType !== <span class="hljs-literal">null</span> &&
              elementType.$$typeof === REACT_LAZY_TYPE &&
              resolveLazy(elementType) === child.type)
          ) &#123;
            deleteRemainingChildren(returnFiber, child.sibling);
            <span class="hljs-keyword">const</span> existing = useFiber(child, element.props);
            existing.ref = coerceRef(returnFiber, child, element);
            existing.return = returnFiber;
            <span class="hljs-keyword">return</span> existing;
          &#125;
        &#125;
        <span class="hljs-comment">// Didn't match.</span>
        deleteRemainingChildren(returnFiber, child);
        <span class="hljs-keyword">break</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        deleteChild(returnFiber, child);
      &#125;
      child = child.sibling;
    &#125;

    <span class="hljs-keyword">if</span> (element.type === REACT_FRAGMENT_TYPE) &#123;
      ...
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">const</span> created = createFiberFromElement(element, returnFiber.mode, lanes);
      created.ref = coerceRef(returnFiber, currentFirstChild, element);
      created.return = returnFiber;
      <span class="hljs-keyword">return</span> created;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>去掉一些调试代码以及类型为 <code>Fragment</code> 的代码，分析剩下的代码，发现可以分为四种场景：</p>
<ol>
<li>原来的 <code>FiberNode</code> 不存在。只需要创建新的 <code>FiberNode</code> 并标记为 <code>Placement</code> 即可。</li>
<li>新的 <code>ReactElement</code> 和 旧的 <code>FiberNode</code> 的 <code>type</code> 和 <code>key</code> 都相同。可以复用旧的 <code>FiberNode</code>，并将旧的 <code>FiberNode</code> 的所有兄弟节点标记为。</li>
<li>新的 <code>ReactElement</code> 和 旧的 <code>FiberNode</code> 的 <code>key</code> 相同，<code>type</code> 不同。需要将旧的 <code>FiberNode</code> 及其兄弟节点都标记为删除，然后创建新的 <code>FiberNode</code> 并标记为 <code>Placement</code>。</li>
<li>新的 <code>ReactElement</code> 和 旧的 <code>FiberNode</code> 的 <code>key</code> 不同。将当前 <code>FiberNode</code> 标记为删除，继续按照 2，3，4 的策略对比其兄弟节点和 <code>ReactElement</code> 直到遍历完成。</li>
</ol>
<p><img alt="diff-single.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86a8c56a8dd7474cb3d5be1add6b61c5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">多节点 Diff</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildrenArray</span>(<span class="hljs-params">
    returnFiber: Fiber,
    currentFirstChild: Fiber | <span class="hljs-literal">null</span>,
    newChildren: <span class="hljs-built_in">Array</span><*>,
    lanes: Lanes,
  </span>): <span class="hljs-title">Fiber</span> | <span class="hljs-title">null</span> </span>&#123;
    <span class="hljs-keyword">let</span> resultingFirstChild: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> previousNewFiber: Fiber | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">let</span> oldFiber = currentFirstChild;
    <span class="hljs-keyword">let</span> lastPlacedIndex = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> newIdx = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> nextOldFiber = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 第一轮循环，依次对比新旧节点，当 key 不同时就会退出</span>
    <span class="hljs-keyword">for</span> (; oldFiber !== <span class="hljs-literal">null</span> && newIdx < newChildren.length; newIdx++) &#123;
      <span class="hljs-keyword">if</span> (oldFiber.index > newIdx) &#123;
        nextOldFiber = oldFiber;
        oldFiber = <span class="hljs-literal">null</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        nextOldFiber = oldFiber.sibling;
      &#125;
      <span class="hljs-keyword">const</span> newFiber = updateSlot(
        returnFiber,
        oldFiber,
        newChildren[newIdx],
        lanes,
      );
      <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
          oldFiber = nextOldFiber;
        &#125;
        <span class="hljs-keyword">break</span>;
      &#125;
      <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
        <span class="hljs-comment">// 新旧节点 key 相同，type 不同</span>
        <span class="hljs-keyword">if</span> (oldFiber && newFiber.alternate === <span class="hljs-literal">null</span>) &#123;
          deleteChild(returnFiber, oldFiber);
        &#125;
      &#125;
      lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
      <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
        resultingFirstChild = newFiber;
      &#125; <span class="hljs-keyword">else</span> &#123;
        previousNewFiber.sibling = newFiber;
      &#125;
      previousNewFiber = newFiber;
      oldFiber = nextOldFiber;
    &#125;

    <span class="hljs-comment">// 第二轮循环</span>

    <span class="hljs-comment">// ReactElement 数组遍历完了，需要把剩下的旧的节点都标记为删除</span>
    <span class="hljs-keyword">if</span> (newIdx === newChildren.length) &#123;
      deleteRemainingChildren(returnFiber, oldFiber);
      <span class="hljs-keyword">return</span> resultingFirstChild;
    &#125;

    <span class="hljs-comment">// 旧的 FiberNode 链表遍历完了，则通过 ReactElement 数组中剩下的节点创建 FiberNode，并标记为 Placement</span>
    <span class="hljs-keyword">if</span> (oldFiber === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
        <span class="hljs-keyword">const</span> newFiber = createChild(returnFiber, newChildren[newIdx], lanes);
        <span class="hljs-keyword">if</span> (newFiber === <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-keyword">continue</span>;
        &#125;
        lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
        <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> Move out of the loop. This only happens for the first run.</span>
          resultingFirstChild = newFiber;
        &#125; <span class="hljs-keyword">else</span> &#123;
          previousNewFiber.sibling = newFiber;
        &#125;
        previousNewFiber = newFiber;
      &#125;
      <span class="hljs-keyword">return</span> resultingFirstChild;
    &#125;


    <span class="hljs-comment">// 将旧的未处理完的 FiberNode 节点保存到 map 中</span>
    <span class="hljs-keyword">const</span> existingChildren = mapRemainingChildren(returnFiber, oldFiber);

    <span class="hljs-comment">// 遍历新的 ReactElement 数组中的元素，到 map 中找 key 相同的节点</span>
    <span class="hljs-keyword">for</span> (; newIdx < newChildren.length; newIdx++) &#123;
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
            existingChildren.delete(
              newFiber.key === <span class="hljs-literal">null</span> ? newIdx : newFiber.key,
            );
          &#125;
        &#125;
        lastPlacedIndex = placeChild(newFiber, lastPlacedIndex, newIdx);
        <span class="hljs-keyword">if</span> (previousNewFiber === <span class="hljs-literal">null</span>) &#123;
          resultingFirstChild = newFiber;
        &#125; <span class="hljs-keyword">else</span> &#123;
          previousNewFiber.sibling = newFiber;
        &#125;
        previousNewFiber = newFiber;
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (shouldTrackSideEffects) &#123;
      existingChildren.forEach(<span class="hljs-function">(<span class="hljs-params">child</span>) =></span> deleteChild(returnFiber, child));
    &#125;

    <span class="hljs-keyword">return</span> resultingFirstChild;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为实际应用场景中列表更新时大部分都是追加或者节点本身的更新，节点位置发生变化的情况相对少见，所以 React 在多节点 Diff 过程中分成了两轮：</p>
<p>第一轮从前往后一一比对，这里分为三种情况：</p>
<ol>
<li>如果新旧节点 <code>key</code> 和 <code>type</code> 相同则说明可以复用旧节点，继续往下遍历。</li>
<li><code>key</code> 相同 <code>type</code> 不同，将旧节点标记为删除，新节点标记为 <code>Placement</code>，继续往下遍历。</li>
<li><code>key</code> 不同，退出循环。</li>
</ol>
<p>第一轮结束后，开始第二轮遍历，这里又分为三种情况：</p>
<ol>
<li>
<p>新节点即 <code>ReactElement</code> 数组遍历完成了，此时只需要把旧的剩下的节点标记为删除，然后返回。</p>
</li>
<li>
<p>旧节点链表遍历完成了，此时只需要处理 <code>ReactElement</code> 数组中剩下的元素，即通过他们创建新的 <code>FiberNode</code> 并标记为 <code>Placement</code>，然后返回。</p>
</li>
<li>
<p>都没有遍历完成，说明第一轮遍历中提前终止了。接下来详细讨论该步骤：</p>
<p>3.1. 将未遍历完的旧节点以保存为 Map，用 <code>key</code> 作为索引。
3.2. 遍历新节点，通过新节点去 Map 中寻找是否有可以复用的节点。如果没有找到则通过 <code>ReactElement</code> 创建新的节点，找到了则复用旧节点来创建新的节点。最后得到的都是 <code>newFiber</code>。
3.3. 调用 <code>placeChild</code> 来处理 <code>newFiber</code>。这里分三种情形：a. 它是通过 <code>ReactElement</code> 创建来的，将其标记为 <code>Placement</code>；b. 它是通过复用旧节点而得到的且旧节点的位置小于 <code>lastPlacedIndex</code>，将其标记为 <code>Placement</code>；c. 它是通过复用旧节点而得到的且旧节点的位置 <code>oldIndex</code> 大于 <code>lastPlacedIndex</code>，无需标记，更新 <code>lastPlacedIndex</code> 为 <code>oldIndex</code>。</p>
</li>
</ol>
<p>上面的步骤肯定看了很懵逼，尤其是涉及到 <code>lastPlacedIndex</code> 的更新这一块。不妨看下面两个例子：</p>
<p>例一:</p>
<pre><code class="copyable">旧列表：abcde
新列表：abdec
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="diff-multi.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccc04ad0e95140369a2e3a1fdaff10e0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>该例子最后得到的结果是要把 c 移到最后面。</p>
<p>例二：</p>
<pre><code class="copyable">旧列表：abcde
新列表：abecd
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="diff-multi-2.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/322b03e1ac334bba8ff98f6259015d26~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>该例子最后得到的结果是要把 c 和 d 移到最后面。</p>
<p>同样都只是移动了一个元素，得到的结果却不大一样，例二的代价明显要大，原因就在于 React 的 Diff 算法。</p>
<h1 data-id="heading-7">总结</h1>
<p>本文介绍了 <code>beginWork</code> 函数的后半部分并引出了 Diff 算法，讨论了 Diff 算法的作用、分类以及详细步骤，并结合案例进行了对比。</p>
<p><em>欢迎关注公众号「前端游」，让我们一起在前端的海洋里遨游。</em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            