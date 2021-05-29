
---
title: '手写React Fiber渲染逻辑 二'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86fbfa62b20f477da3d932034f8509ac~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 00:45:16 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86fbfa62b20f477da3d932034f8509ac~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">接上一篇 <a href="https://juejin.cn/post/6964943378127519781" target="_blank">手写React Fiber渲染逻辑 一</a></h3>
<blockquote>
<p>本章内容介绍：用React fiber实现更新渲染逻辑，实现类组件、函数组件和Hooks <br>
对React Fiber不太了解的，可以翻看上两篇文章</p>
</blockquote>
<h2 data-id="heading-1">实现更新</h2>
<h3 data-id="heading-2">调试用例</h3>
<ul>
<li>在index.html中新增两个按钮</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <div id=<span class="hljs-string">"root"</span>></div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"reRender2"</span>></span>reRender2<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"reRender3"</span>></span>reRender3<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在index.js中为两个按钮添加事件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// -------------渲染更新----------</span>

<span class="hljs-keyword">let</span> reRender2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'reRender2'</span>);
reRender2.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> element2 = (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"A1-new"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
      A1-new
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"B1-new"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
        B1-new
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"C1-new"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
          C1-new
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"C2-new"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
          C2-new
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"B2"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
        B2
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"B3"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
        B3
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
  ReactDOM.render(element2, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
&#125;);

<span class="hljs-keyword">let</span> reRender3 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'reRender3'</span>);
reRender3.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> element3 = (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"A1-new2"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
      A1-new2
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"B1-new2"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
        B1-new2
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"C1-new2"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
          C1-new2
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"C2-new2"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
          C2-new2
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"B2"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;style&#125;</span>></span>
        B2
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
  ReactDOM.render(element3, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击两个按钮实现页面的第二和第三次更新渲染，效果如下：</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86fbfa62b20f477da3d932034f8509ac~tplv-k3u1fbpfcp-watermark.image" alt="Untitled.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">alternate指针</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1348b6a1ddb748acb72e1c719812b012~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>老的fiber指当前页面已经渲染的节点，新fiber指将要渲染的节点</p>
</blockquote>
<ul>
<li>初次渲染完毕后，会给每个节点创建一个fiber对象，页面发生更新时，会创建一个新的fiber树</li>
<li>如图所示，currentRoot是我们页面当前显示的节点，当页面更新时，会创建一个新的根fiber <code>workInProgressRoot</code></li>
<li>每个新fiber节点都会有一个<code>alternate</code>指针，指向对应的老的fiber节点</li>
<li>alternate指针的作用就是进行新老节点的对比，进行dom-diff</li>
</ul>
<h3 data-id="heading-4">代码实现</h3>
<ul>
<li>在scheduler.js中添加两个全局变量</li>
<li>提交完成后，让<code>currentRoot</code>指向<code>workInProgressRoot</code>，将<code>workInProgressRoot</code>置为null</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> currentRoot = <span class="hljs-literal">null</span>; <span class="hljs-comment">//当前的根Fiber</span>
<span class="hljs-keyword">let</span> deletions = []; <span class="hljs-comment">//要删除的fiber节点</span>

<span class="hljs-comment">// -----------commit阶段-----------</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>) </span>&#123;
  .......
  currentRoot = workInProgressRoot;
  workInProgressRoot = <span class="hljs-literal">null</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>更新时，<code>render</code>函数再次调用<code>scheduleRoot</code>方法，如果<code>currentRoot</code>有值就是更新，让<code>rootFiber</code>的<code>alternate</code>指针，指向<code>currentRoot</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scheduleRoot</span>(<span class="hljs-params">rootFiber</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (currentRoot) &#123;
    <span class="hljs-comment">// 更新</span>
    rootFiber.alternate = currentRoot;
    workInProgressRoot = rootFiber;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 第一次渲染</span>
    workInProgressRoot = rootFiber;
  &#125;

  nextUnitOfWork = workInProgressRoot;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">修改<code>reconcileChildren</code>方法</h3>
<blockquote>
<p>此处只做简单的diff，遍历一遍，如果新老节点类型相同就复用，不同就重新创建，没有实现react的diff算法</p>
</blockquote>
<ul>
<li>
<p>遍历新的虚拟dom，并找到对应的老的oldFiber，进行比较，然后生成新的fiber树，每个新fiber都有<code>alternate</code>指针，指向<code>oldFiber</code></p>
</li>
<li>
<p>老的fiber节点与新的虚拟dom进行对比，如果类型相同，就复用老的fiber节点的<code>stateNode</code>，并将<code>newFiber</code>的<code>alternate</code>指向<code>oldFiber</code>，将<code>effectTag</code>标记为<code>UPDATE</code>更新</p>
</li>
<li>
<p>如果类型不同，创建<code>newFiber</code>时将<code>effectTag</code>标记为<code>PLACEMENT</code>插入，不复用老节点的<code>stateNode</code>，并将老节点<code>oldFiber</code>加入<code>deletions</code>中，提交时进行删除</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 创建fiber 构建fiber树
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>currentFiber 当前fiber
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>newChildren 当前节点的子节点，虚拟dom数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>deletions 指向全局变量 deletions, 放置要删除的节点
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildren</span>(<span class="hljs-params">currentFiber, newChildren, deletions</span>) </span>&#123;
  <span class="hljs-keyword">let</span> newChildIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">//新虚拟DOM数组中的索引</span>
  <span class="hljs-comment">// 老的父fiber的第一个子fiber</span>
  <span class="hljs-keyword">let</span> oldFiber = currentFiber.alternate && currentFiber.alternate.child;
  <span class="hljs-keyword">let</span> prevSibling;
  <span class="hljs-keyword">while</span> (newChildIndex < newChildren.length || oldFiber) &#123;
    <span class="hljs-keyword">const</span> newChild = newChildren[newChildIndex];

    <span class="hljs-comment">// 两个节点是不是相同类型 span div...</span>
    <span class="hljs-keyword">const</span> sameType = oldFiber && newChild && newChild.type === oldFiber.type;
    <span class="hljs-keyword">let</span> newFiber;
    <span class="hljs-keyword">let</span> tag;
    <span class="hljs-keyword">if</span> (newChild && newChild.type === ELEMENT_TEXT) &#123;
      tag = TAG_TEXT; <span class="hljs-comment">//文本</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newChild && <span class="hljs-keyword">typeof</span> newChild.type === <span class="hljs-string">'string'</span>) &#123;
      tag = TAG_HOST; <span class="hljs-comment">//原生DOM组件</span>
    &#125;

    <span class="hljs-comment">// 类型相同就更新，不同就重新创建插入</span>
    <span class="hljs-keyword">if</span> (sameType) &#123;
      <span class="hljs-comment">// 更新</span>
      newFiber = &#123;
        <span class="hljs-attr">tag</span>: oldFiber.tag, <span class="hljs-comment">//原生DOM组件</span>
        <span class="hljs-attr">type</span>: oldFiber.type, <span class="hljs-comment">//具体的元素类型</span>
        <span class="hljs-attr">props</span>: newChild.props, <span class="hljs-comment">//新的属性对象</span>
        <span class="hljs-attr">stateNode</span>: oldFiber.stateNode, <span class="hljs-comment">//复用老fiber的dom</span>
        <span class="hljs-attr">return</span>: currentFiber, <span class="hljs-comment">//父Fiber</span>
        <span class="hljs-attr">alternate</span>: oldFiber, <span class="hljs-comment">//上一个Fiber 指向旧树中的节点</span>
        <span class="hljs-attr">effectTag</span>: UPDATE, <span class="hljs-comment">//更新节点</span>
        <span class="hljs-attr">nextEffect</span>: <span class="hljs-literal">null</span>,
      &#125;;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 新建</span>
      <span class="hljs-keyword">if</span> (newChild) &#123;
        <span class="hljs-comment">// 创建fiber</span>
        newFiber = &#123;
          tag, <span class="hljs-comment">//原生DOM组件</span>
          <span class="hljs-attr">type</span>: newChild.type, <span class="hljs-comment">//具体的元素类型</span>
          <span class="hljs-attr">props</span>: newChild.props, <span class="hljs-comment">//新的属性对象</span>
          <span class="hljs-attr">stateNode</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">//stateNode肯定是空的</span>
          <span class="hljs-attr">return</span>: currentFiber, <span class="hljs-comment">//父Fiber</span>
          <span class="hljs-attr">effectTag</span>: PLACEMENT, <span class="hljs-comment">//插入节点</span>
        &#125;;
      &#125;
      <span class="hljs-keyword">if</span> (oldFiber) &#123;
        oldFiber.effectTag = DELETION;
        deletions.push(oldFiber);
      &#125;
    &#125;

    <span class="hljs-comment">// 构建fiber链表</span>
    <span class="hljs-keyword">if</span> (newFiber) &#123;
      <span class="hljs-keyword">if</span> (newChildIndex === <span class="hljs-number">0</span>) &#123;
        currentFiber.child = newFiber; <span class="hljs-comment">//第一个子节点挂到父节点的child属性上</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        prevSibling.sibling = newFiber;
      &#125;
      prevSibling = newFiber; <span class="hljs-comment">//然后newFiber变成了上一个哥哥了</span>
    &#125;

    <span class="hljs-keyword">if</span> (oldFiber) &#123;
      oldFiber = oldFiber.sibling;
    &#125;

    newChildIndex++;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">提交阶段</h3>
<ul>
<li>提交时，先清空<code>deletions</code>，将要删除的节点删除</li>
<li>然后根据节点的<code>effectTag</code>来进行插入和更新操作</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>) </span>&#123;
  deletions.forEach(commitWork);
  <span class="hljs-keyword">let</span> currentFiber = workInProgressRoot.firstEffect;
  <span class="hljs-keyword">while</span> (currentFiber) &#123;
    commitWork(currentFiber);
    currentFiber = currentFiber.nextEffect;
  &#125;
  <span class="hljs-comment">// 提交完成</span>
  deletions.length = <span class="hljs-number">0</span>;
  currentRoot = workInProgressRoot;
  workInProgressRoot = <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitWork</span>(<span class="hljs-params">currentFiber</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!currentFiber) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">let</span> returnFiber = currentFiber.return;
  <span class="hljs-keyword">const</span> domReturn = returnFiber.stateNode;

  <span class="hljs-keyword">if</span> (currentFiber.effectTag === PLACEMENT && currentFiber.stateNode) &#123;
    <span class="hljs-comment">//如果是新增DOM节点</span>
    domReturn.appendChild(currentFiber.stateNode);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (currentFiber.effectTag === DELETION) &#123;
    <span class="hljs-comment">// 删除</span>
    domReturn.removeChild(currentFiber.stateNode);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (currentFiber.effectTag === UPDATE && currentFiber.stateNode) &#123;
    <span class="hljs-comment">// 更新</span>
    <span class="hljs-keyword">if</span> (currentFiber.type === ELEMENT_TEXT) &#123;
      <span class="hljs-keyword">if</span> (currentFiber.alternate.props.text !== currentFiber.props.text) 
        <span class="hljs-comment">// 更新文本节点 </span>
        currentFiber.stateNode.textContent = currentFiber.props.text;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 更新其他节点</span>
        updateDOM(currentFiber.stateNode, currentFiber.alternate.props, currentFiber.props);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
    &#125;
  &#125;

  currentFiber.effectTag = <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><a href="https://github.com/Miller-Wang/reactFiber/commit/67a1632b9978e8f2a1da96d2b468b3caf89d7b28" target="_blank" rel="nofollow noopener noreferrer">commit记录</a></h3>
<h2 data-id="heading-8">双缓冲机制</h2>
<ul>
<li>react中为了避免重复创建销毁fiber对象，造成不必要的内存开销，采用了双缓冲机制</li>
<li>页面更新一次之后，每个节点会有两个fiber对象，<code>newFiber</code>和<code>newFiber.alternate</code>指向的<code>oldFiber</code></li>
<li>当第三次渲染时，不会重新创建newFiber，而是会复用老的fiber对象，如图所示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b2e391cf07e4346b6b6f62b0a35da78~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">双缓冲机制代码实现</h3>
<ul>
<li>scheduleRoot方法修改</li>
<li>第一次更新之后的更新逻辑，不直接使用<code>rootFiber</code>，而是将<code>currentRoot.alternate</code>给<code>workInProgressRoot</code>使用，更新它的props</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scheduleRoot</span>(<span class="hljs-params">rootFiber</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (currentRoot && currentRoot.alternate) &#123;
    <span class="hljs-comment">// 第一次更新之后的更新</span>
    <span class="hljs-comment">// 双缓冲机制，复用之前的fiber对象</span>
    workInProgressRoot = currentRoot.alternate;
    workInProgressRoot.alternate = currentRoot;
    <span class="hljs-keyword">if</span> (rootFiber) &#123;
      <span class="hljs-comment">// 更新复用fiber节点的props</span>
      workInProgressRoot.props = rootFiber.props;
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (currentRoot) &#123;
    <span class="hljs-comment">// 第一次更新</span>
    rootFiber.alternate = currentRoot;
    workInProgressRoot = rootFiber;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 第一次渲染</span>
    workInProgressRoot = rootFiber;
  &#125;

  <span class="hljs-comment">// 清除effect list</span>
  workInProgressRoot.firstEffect = workInProgressRoot.lastEffect = <span class="hljs-literal">null</span>;
  nextUnitOfWork = workInProgressRoot;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>reconcileChildren方法修改</li>
<li>节点类型相同时，如果老节点有<code>alternate</code>，就把老节点的<code>alternate</code>，拿过来更新一下属性，作为<code>newFiber</code>使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">if</span> (sameType) &#123;
      <span class="hljs-comment">// 更新</span>
      <span class="hljs-keyword">if</span> (oldFiber.alternate) &#123;
        <span class="hljs-comment">// 双缓冲机制，复用老的fiber</span>
        newFiber = oldFiber.alternate;
        newFiber.props = newChild.props;
        newFiber.alternate = oldFiber;
        newFiber.effectTag = UPDATE;
      &#125; <span class="hljs-keyword">else</span> &#123;
        newFiber = &#123;
          <span class="hljs-attr">tag</span>: oldFiber.tag, <span class="hljs-comment">//原生DOM组件</span>
          <span class="hljs-attr">type</span>: oldFiber.type, <span class="hljs-comment">//具体的元素类型</span>
          <span class="hljs-attr">props</span>: newChild.props, <span class="hljs-comment">//新的属性对象</span>
          <span class="hljs-attr">stateNode</span>: oldFiber.stateNode, <span class="hljs-comment">//复用老fiber的dom</span>
          <span class="hljs-attr">return</span>: currentFiber, <span class="hljs-comment">//父Fiber</span>
          <span class="hljs-attr">alternate</span>: oldFiber, <span class="hljs-comment">//上一个Fiber 指向旧树中的节点</span>
          <span class="hljs-attr">effectTag</span>: UPDATE, <span class="hljs-comment">//更新节点</span>
          <span class="hljs-attr">nextEffect</span>: <span class="hljs-literal">null</span>,
        &#125;;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这样我们双缓冲机制的更新逻辑就实现了</li>
</ul>
<h3 data-id="heading-10"><a href="https://github.com/Miller-Wang/reactFiber/commit/e8c3fc0ebcaaea1ca139d0d3ba0b57d610a99c6f" target="_blank" rel="nofollow noopener noreferrer">commit记录</a></h3>
<h2 data-id="heading-11">类组件渲染</h2>
<h3 data-id="heading-12">测试类组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'./react/react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'./react/react-dom'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClassCounter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">number</span>: <span class="hljs-number">0</span> &#125;;
  &#125;
  onClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(<span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123; <span class="hljs-attr">number</span>: state.number + <span class="hljs-number">1</span> &#125;));
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"counter"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;this.state.number&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.onClick&#125;</span>></span>加1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ClassCounter</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">UpdateQueue</h3>
<ul>
<li>更新队列，是个单链表结构</li>
<li>每次<code>setState</code>都会将要更新的数据放在队列中，到一定时机进行批量更新</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/551d33a634aa48c1abab6be33d09324f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Update</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">payload</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.payload = payload;
    &#125;
&#125;
<span class="hljs-comment">//数据结构是一个单链表</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UpdateQueue</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.firstUpdate = <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.lastUpdate = <span class="hljs-literal">null</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-title">enqueueUpdate</span>(<span class="hljs-params">update</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.lastUpdate === <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-built_in">this</span>.firstUpdate = <span class="hljs-built_in">this</span>.lastUpdate = update;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.lastUpdate.nextUpdate = update;
            <span class="hljs-built_in">this</span>.lastUpdate = update;
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">forceUpdate</span>(<span class="hljs-params">state</span>)</span> &#123;
        <span class="hljs-keyword">let</span> currentUpdate = <span class="hljs-built_in">this</span>.firstUpdate;
        <span class="hljs-keyword">while</span> (currentUpdate) &#123;
            <span class="hljs-keyword">let</span> nextState = <span class="hljs-keyword">typeof</span> currentUpdate.payload === <span class="hljs-string">'function'</span> ? currentUpdate.payload(state) : currentUpdate.payload;
            state = &#123; ...state, ...nextState &#125;;
            currentUpdate = currentUpdate.nextUpdate;
        &#125;
        <span class="hljs-built_in">this</span>.firstUpdate = <span class="hljs-built_in">this</span>.lastUpdate = <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">return</span> state;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">类组件代码实现</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5f94aa2ca424a74bde0e912a6b0d001~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在react.js文件中声明一个Componet类</li>
<li>internalFiber指向Componet类对应的fiber节点，fiber节点有updateQueue</li>
<li>调用<code>setState</code>方法时，会先将要更新的payload放入更新队列，然后执行<code>scheduleRoot</code>方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.props = props;
  &#125;

  <span class="hljs-function"><span class="hljs-title">setState</span>(<span class="hljs-params">payload</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.internalFiber.updateQueue.enqueueUpdate(<span class="hljs-keyword">new</span> Update(payload));
    scheduleRoot();
  &#125;
&#125;
<span class="hljs-comment">// 函数组件标识</span>
Component.prototype.isReactComponent = <span class="hljs-literal">true</span>;

<span class="hljs-keyword">const</span> React = &#123;
  createElement,
  Component,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">scheduler.js逻辑修改</h3>
<ul>
<li>当类组件setState时 传入的rootFiber为空，需要处理rootFiber为空的情况</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 暴露给外部, 当类组件setState时 传入的rootFiber为空</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scheduleRoot</span>(<span class="hljs-params">rootFiber</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (currentRoot && currentRoot.alternate) &#123;
    <span class="hljs-comment">// 第一次之后的更新</span>
    <span class="hljs-comment">// 双缓冲机制，复用之前的fiber对象</span>
    workInProgressRoot = currentRoot.alternate;
    workInProgressRoot.alternate = currentRoot;
    <span class="hljs-keyword">if</span> (rootFiber) &#123;
      <span class="hljs-comment">// 更新复用fiber节点的props</span>
      workInProgressRoot.props = rootFiber.props;
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (currentRoot) &#123;
    <span class="hljs-comment">// 第一次更新</span>
+    <span class="hljs-keyword">if</span> (rootFiber) &#123;
+      rootFiber.alternate = currentRoot;
+      workInProgressRoot = rootFiber;
+    &#125; <span class="hljs-keyword">else</span> &#123;
+      workInProgressRoot = &#123;
+        ...currentRoot,
+        alternate: currentRoot,
+      &#125;;
+    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    workInProgressRoot = rootFiber;
  &#125;

  <span class="hljs-comment">// 清除effect list</span>
  workInProgressRoot.firstEffect = workInProgressRoot.lastEffect = <span class="hljs-literal">null</span>;
  nextUnitOfWork = workInProgressRoot;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">新增 <code>updateClassComponent</code>处理类组件的更新</h3>
<ul>
<li>类组件的stateNode不是真实dom元素，是类组件的实例</li>
<li>每个类组件实例都有一个<code>internalFiber</code>指向类组件对应的fiber节点</li>
<li>给类组件实例的fiber节点创建一个updateQueue，用来处理类组件的更新逻辑</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 类组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateClassComponent</span>(<span class="hljs-params">currentFiber</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!currentFiber.stateNode) &#123;
    currentFiber.stateNode = <span class="hljs-keyword">new</span> currentFiber.type(currentFiber.props);
    currentFiber.stateNode.internalFiber = currentFiber;
    currentFiber.updateQueue = <span class="hljs-keyword">new</span> UpdateQueue();
  &#125;

  <span class="hljs-comment">// 获取最新状态</span>
  currentFiber.stateNode.state = currentFiber.updateQueue.forceUpdate(currentFiber.stateNode.state);
  <span class="hljs-comment">// 重新渲染组件</span>
  <span class="hljs-keyword">const</span> newChildren = [currentFiber.stateNode.render()];
  reconcileChildren(currentFiber, newChildren, deletions);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17"><code>reconcileChildren</code>处理类组件的fiber创建</h3>
<ul>
<li>判断是否是类组件，给类组件添加对应tag</li>
<li>创建fiber时给每个fiber添加<code>updateQueue</code>属性，处理组件更新</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reconcileChildren</span>(<span class="hljs-params">currentFiber, newChildren, deletions</span>) </span>&#123;
  <span class="hljs-keyword">let</span> newChildIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">//新虚拟DOM数组中的索引</span>
  <span class="hljs-comment">// 老的父fiber的第一个子fiber</span>
  <span class="hljs-keyword">let</span> oldFiber = currentFiber.alternate && currentFiber.alternate.child;
  <span class="hljs-keyword">if</span> (oldFiber) oldFiber.firstEffect = oldFiber.lastEffect = oldFiber.nextEffect = <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">let</span> prevSibling;
  <span class="hljs-keyword">while</span> (newChildIndex < newChildren.length || oldFiber) &#123;
    <span class="hljs-keyword">const</span> newChild = newChildren[newChildIndex];

    <span class="hljs-comment">// 两个节点是不是相同类型 span div...</span>
    <span class="hljs-keyword">const</span> sameType = oldFiber && newChild && newChild.type === oldFiber.type;
    <span class="hljs-keyword">let</span> newFiber;
    <span class="hljs-keyword">let</span> tag;

+    <span class="hljs-comment">// class 会被编译成函数，所以用function判断， 用 isReactComponent来判断是否是类组件</span>
+    <span class="hljs-keyword">if</span> (
+      newChild &&
+      <span class="hljs-keyword">typeof</span> newChild.type === <span class="hljs-string">'function'</span> &&
+      newChild.type.prototype.isReactComponent
+    ) &#123;
+      tag = TAG_CLASS;
+    &#125;  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newChild && <span class="hljs-keyword">typeof</span> newChild.type === <span class="hljs-string">'function'</span>) &#123;
+      <span class="hljs-comment">// 函数组件</span>
+      tag = TAG_FUNCTION_COMPONENT;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newChild && newChild.type === ELEMENT_TEXT) &#123;
      tag = TAG_TEXT; <span class="hljs-comment">//文本</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newChild && <span class="hljs-keyword">typeof</span> newChild.type === <span class="hljs-string">'string'</span>) &#123;
      tag = TAG_HOST; <span class="hljs-comment">//原生DOM组件</span>
    &#125;

    <span class="hljs-comment">// 类型相同就更新，不同就重新创建插入</span>
    <span class="hljs-keyword">if</span> (sameType) &#123;
      <span class="hljs-comment">// 更新</span>
      <span class="hljs-keyword">if</span> (oldFiber.alternate) &#123;
        <span class="hljs-comment">// 双缓冲机制，复用老的fiber</span>
        newFiber = oldFiber.alternate;
        newFiber.props = newChild.props;
        newFiber.alternate = oldFiber;
        newFiber.effectTag = UPDATE;
+        newFiber.updateQueue = oldFiber.updateQueue || <span class="hljs-keyword">new</span> UpdateQueue();
      &#125; <span class="hljs-keyword">else</span> &#123;
        newFiber = &#123;
          <span class="hljs-attr">tag</span>: oldFiber.tag, <span class="hljs-comment">//原生DOM组件</span>
          <span class="hljs-attr">type</span>: oldFiber.type, <span class="hljs-comment">//具体的元素类型</span>
          <span class="hljs-attr">props</span>: newChild.props, <span class="hljs-comment">//新的属性对象</span>
          <span class="hljs-attr">stateNode</span>: oldFiber.stateNode, <span class="hljs-comment">//复用老fiber的dom</span>
          <span class="hljs-attr">return</span>: currentFiber, <span class="hljs-comment">//父Fiber</span>
          <span class="hljs-attr">alternate</span>: oldFiber, <span class="hljs-comment">//上一个Fiber 指向旧树中的节点</span>
          <span class="hljs-attr">effectTag</span>: UPDATE, <span class="hljs-comment">//更新节点</span>
+          updateQueue: oldFiber.updateQueue || <span class="hljs-keyword">new</span> UpdateQueue(),
        &#125;;
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 新建</span>
      <span class="hljs-keyword">if</span> (newChild) &#123;
        <span class="hljs-comment">// 创建fiber</span>
        newFiber = &#123;
          tag, <span class="hljs-comment">//原生DOM组件</span>
          <span class="hljs-attr">type</span>: newChild.type, <span class="hljs-comment">//具体的元素类型</span>
          <span class="hljs-attr">props</span>: newChild.props, <span class="hljs-comment">//新的属性对象</span>
          <span class="hljs-attr">stateNode</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">//stateNode肯定是空的</span>
          <span class="hljs-attr">return</span>: currentFiber, <span class="hljs-comment">//父Fiber</span>
          <span class="hljs-attr">effectTag</span>: PLACEMENT, <span class="hljs-comment">//插入节点</span>
+          updateQueue: <span class="hljs-keyword">new</span> UpdateQueue(),
        &#125;;
      &#125;
      <span class="hljs-keyword">if</span> (oldFiber) &#123;
        oldFiber.effectTag = DELETION;
        deletions.push(oldFiber);
      &#125;
    &#125;

    <span class="hljs-comment">// 构建fiber链表</span>
    <span class="hljs-keyword">if</span> (newFiber) &#123;
      <span class="hljs-keyword">if</span> (newChildIndex === <span class="hljs-number">0</span>) &#123;
        currentFiber.child = newFiber; <span class="hljs-comment">//第一个子节点挂到父节点的child属性上</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        prevSibling.sibling = newFiber;
      &#125;
      prevSibling = newFiber; <span class="hljs-comment">//然后newFiber变成了上一个哥哥了</span>
    &#125;

    <span class="hljs-keyword">if</span> (oldFiber) &#123;
      oldFiber = oldFiber.sibling;
    &#125;

    newChildIndex++;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">类组件的提交逻辑</h3>
<ul>
<li>由于类组件没有真实dom(stateNode对应的是类的实例，不是真实dom)，所以删除和更新时需要进行特殊处理</li>
<li>需要递归往下查找到有真实dom的子节点，然后进行删除或插入</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitWork</span>(<span class="hljs-params">currentFiber</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!currentFiber) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">let</span> returnFiber = currentFiber.return;

  <span class="hljs-comment">// 类组件fiber 中的stateNode是类的实例，不是真实dom，需要往上查找到真实dom的节点</span>
  <span class="hljs-keyword">while</span> (returnFiber.tag === TAG_CLASS) &#123;
    returnFiber = returnFiber.return;
  &#125;

  <span class="hljs-keyword">const</span> domReturn = returnFiber.stateNode;

  <span class="hljs-keyword">if</span> (currentFiber.effectTag === PLACEMENT && currentFiber.stateNode) &#123;
    <span class="hljs-comment">// 类组件没有真实dom，需要往下查找</span>
    <span class="hljs-keyword">let</span> nextFiber = currentFiber;
    <span class="hljs-keyword">while</span> (nextFiber.tag === TAG_CLASS) &#123;
      nextFiber = nextFiber.child;
    &#125;

    <span class="hljs-comment">//如果是新增DOM节点</span>
    domReturn.appendChild(nextFiber.stateNode);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (currentFiber.effectTag === DELETION) &#123;
    <span class="hljs-comment">// 删除</span>
    commitDeletion(currentFiber, domReturn);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (currentFiber.effectTag === UPDATE && currentFiber.stateNode) &#123;
    <span class="hljs-comment">// 更新</span>
    <span class="hljs-keyword">if</span> (currentFiber.type === ELEMENT_TEXT) &#123;
      <span class="hljs-keyword">if</span> (currentFiber.alternate.props.text !== currentFiber.props.text) &#123;
        currentFiber.stateNode.textContent = currentFiber.props.text;
      &#125; <span class="hljs-keyword">else</span> &#123;
        updateDOM(currentFiber.stateNode, currentFiber.alternate.props, currentFiber.props);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
    &#125;
  &#125;

  currentFiber.effectTag = <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-comment">// 删除类组件dom</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitDeletion</span>(<span class="hljs-params">currentFiber, domReturn</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (currentFiber.tag === TAG_CLASS) &#123;
    <span class="hljs-comment">// 往下找</span>
    commitDeletion(currentFiber.child, domReturn);
  &#125; <span class="hljs-keyword">else</span> &#123;
    domReturn.removeChild(currentFiber.stateNode);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最终效果如下</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc2c94b55fcb4f7a8f53d63181afd35d~tplv-k3u1fbpfcp-watermark.image" alt="Untitled.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19"><a href="https://github.com/Miller-Wang/reactFiber/commit/5d3c1ec2813ed8b310d77a4a0567547a0736ef07" target="_blank" rel="nofollow noopener noreferrer">commit记录</a></h3>
<h2 data-id="heading-20">实现函数组件与Hooks</h2>
<ul>
<li>声明全局变量 <code>workInProgressFiber</code>与<code>hookIndex</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> workInProgressFiber = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 正在工作中的fiber</span>
<span class="hljs-keyword">let</span> hookIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">// hook索引</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在scheduler.js中添加函数组件的update方法<code>updateFunctionComponent</code></li>
<li>currentFiber.type 对应函数组件的函数名，调用 <code>currentFiber.type(currentFiber.props)</code>相当于执行函数组件，返回一个虚拟节点</li>
<li>执行函数组件时，会调用函数中引用的react hooks方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 函数组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateFunctionComponent</span>(<span class="hljs-params">currentFiber</span>) </span>&#123;
  workInProgressFiber = currentFiber;
  hookIndex = <span class="hljs-number">0</span>;
  workInProgressFiber.hooks = [];

  <span class="hljs-keyword">const</span> newChildren = [currentFiber.type(currentFiber.props)];
  reconcileChildren(currentFiber, newChildren, deletions);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在scheduler.js中实现<code>useReducer</code>和<code>useState</code>两个hooks</li>
<li><code>useState</code>是通过<code>useReducer</code>来实现的</li>
<li>函数组件的<code>fiber</code>会有<code>hooks</code>属性来存放用到的hooks，hooks包含两个属性<code>state</code>状态和<code>updateQueue</code>更新队列</li>
<li>第一次执行<code>useReducer</code>时会将初始状态存到<code>fiber.hooks</code>中，函数组件更新时，会使用存储在<code>fiber.hooks</code>中的状态</li>
<li>dispatch方法可以修改 hooks中的state，并触发<code>scheduleRoot</code>进行重新渲染</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// -------------------------------hooks--------------------------------------</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useReducer</span>(<span class="hljs-params">reducer, initialValue</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldHook =
    workInProgressFiber.alternate &&
    workInProgressFiber.alternate.hooks &&
    workInProgressFiber.alternate.hooks[hookIndex];
  <span class="hljs-keyword">let</span> newHook = oldHook;
  <span class="hljs-keyword">if</span> (oldHook) &#123;
    newHook.state = oldHook.updateQueue.forceUpdate(oldHook.state);
  &#125; <span class="hljs-keyword">else</span> &#123;
    newHook = &#123;
      <span class="hljs-attr">state</span>: initialValue,
      <span class="hljs-attr">updateQueue</span>: <span class="hljs-keyword">new</span> UpdateQueue(),
    &#125;;
  &#125;
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-function"><span class="hljs-params">action</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'action'</span>, action);
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> action === <span class="hljs-string">'function'</span>) &#123;
      action = action(newHook.state);
    &#125;
    <span class="hljs-keyword">const</span> newState = reducer ? reducer(newHook.state, action) : action;
    newHook.updateQueue.enqueueUpdate(<span class="hljs-keyword">new</span> Update(newState));
    scheduleRoot();
  &#125;;

  <span class="hljs-comment">// 将hook的数据放在 fiber的hooks中，并让hookIndex指针后移</span>
  workInProgressFiber.hooks[hookIndex++] = newHook;
  <span class="hljs-keyword">return</span> [newHook.state, dispatch];
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useState</span>(<span class="hljs-params">initState</span>) </span>&#123;
  <span class="hljs-keyword">return</span> useReducer(<span class="hljs-literal">null</span>, initState);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在react中引用<code>useReducer</code> <code>useState</code>并导出</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; scheduleRoot, useReducer, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./scheduler'</span>;

........

<span class="hljs-keyword">const</span> React = &#123;
  createElement,
  Component,
  useReducer,
  useState,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在index.js中引用hooks，用hooks实现一个计数器案例</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'./react/react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'./react/react-dom'</span>;

<span class="hljs-comment">// Hooks</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reducer</span>(<span class="hljs-params">state, action</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'ADD'</span>:
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span> &#125;;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> state;
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FunctionCounter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [numberState, setNumberState] = React.useState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">0</span> &#125;);
  <span class="hljs-keyword">const</span> [countState, dispatch] = React.useReducer(reducer, &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setNumberState(state => (&#123; number: state.number + 1 &#125;))&#125;>
        useState Count: &#123;numberState.number&#125;
      <span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">hr</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123; type: 'ADD' &#125;)&#125;>useReducer Count: &#123;countState.count&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">FunctionCounter</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21"><a href="https://github.com/Miller-Wang/reactFiber/commit/2e7108553923caf43a72c0133237fefdbd4794cd" target="_blank" rel="nofollow noopener noreferrer">commit记录</a></h3>
<h2 data-id="heading-22"><a href="https://github.com/Miller-Wang/reactFiber" target="_blank" rel="nofollow noopener noreferrer">代码奉上</a></h2>
<blockquote>
<p>有漏洞和不足之处，还请大家指正</p>
</blockquote></div>  
</div>
            