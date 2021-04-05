
---
title: 'Vue源码解析-patch&diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f70b90691e469f9a86f50e9322868b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 19:44:02 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f70b90691e469f9a86f50e9322868b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在vue中，patch过程，是以新的虚拟dom为基准，改造旧的虚拟dom。</p>
<p>宏观上讲，patch过程就做了3件事：</p>
<ul>
<li>创建节点</li>
<li>更新节点</li>
<li>删除节点</li>
</ul>
<p>接下来，我们逐个击破。</p>
<h1 data-id="heading-0">一. update</h1>
<p>在执行render函数，返回虚拟dom之后，vue会执行update方法，去更新视图。其主干代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
 Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode: VNode, hydrating?: boolean</span>) </span>&#123;
   <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
   <span class="hljs-keyword">const</span> prevEl = vm.$el
   <span class="hljs-keyword">const</span> prevVnode = vm._vnode
   
   <span class="hljs-keyword">const</span> restoreActiveInstance = setActiveInstance(vm)
   vm._vnode = vnode
   
   <span class="hljs-keyword">if</span> (!prevVnode) &#123;
     vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
   &#125; <span class="hljs-keyword">else</span> &#123;
     vm.$el = vm.__patch__(prevVnode, vnode)
   &#125;
   restoreActiveInstance()
   
   <span class="hljs-comment">// ...</span>
 &#125;
 

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">setActiveInstance</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> activeInstance: any = <span class="hljs-literal">null</span>

 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setActiveInstance</span>(<span class="hljs-params">vm: Component</span>) </span>&#123;
   <span class="hljs-keyword">const</span> prevActiveInstance = activeInstance
   activeInstance = vm
   <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
     activeInstance = prevActiveInstance
   &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面章节，我们分析了组件化实践。setActiveInstance方法是 设置 当前是 哪个组件被激活。 因为 同一时间，只会有一个组件实例化。</p>
<p>activeInstance变量是 当前正在实例化的组件对象。 prevActiveInstance实际上是父的实例化对象。在每次子组件实例化并且patch之后，就会执行restoreActiveInstance方法，就会将当前的  activeInstance 重置为 当前的父组件，以此类推，直到最上层的Vue。</p>
<p>需要指出的是， 这里设置了 activeInstance， 会在 组件实例化的 时候 会使用到， 不清楚的小伙伴可以看我的上一篇 《Vue源码解析-组件化&虚拟DOM》</p>
<p>下面，我们继续看__patch__</p>
<h1 data-id="heading-2">二. patch</h1>
<p>__patch__方法的定义，实际就是执行的 createPatchFunction  方法。此方法比较庞大，我们先看主入口patch方法定义：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode, hydrating, removeOnly</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-keyword">const</span> isRealElement = isDef(oldVnode.nodeType)
  <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
    patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
  &#125;<span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">if</span>(isRealElement) &#123;
      <span class="hljs-comment">// ssr 属性... 暂时忽略</span>
      
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
    
    <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;
  
  invokeInsertHook(vnode, insertedVnodeQueue, isInitialPatch)
  <span class="hljs-keyword">return</span> vnode.elm
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">我们先来看个🌰：</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'root'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../vue/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

      <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#root'</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">a</span>: <span class="hljs-string">"这是根节点"</span>
          &#125;
        &#125;,
        <span class="hljs-attr">template</span>: <span class="hljs-string">`<div data-test='这是测试属性' @click="handleClick"> &#123;&#123; a &#125;&#125; </div>`</span>,

        <span class="hljs-attr">methods</span>: &#123;
          <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.a = <span class="hljs-string">'变了'</span>
          &#125;
        &#125;,

      &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面渲染时，会执行一次update patch。</p>
<h4 data-id="heading-4">oldVnode</h4>
<p>此时oldVnode是div#root，是实际的DOM节点。</p>
<p>vnode值是执行render函数得到，其结构大致如下：</p>
<h4 data-id="heading-5">vnode</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>,
  <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">children</span>: [
    <span class="hljs-comment">// vnode  纯文本节点</span>
    &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  ],
  <span class="hljs-attr">context</span>: Vue,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">attrs</span>: &#123;...&#125;,
    <span class="hljs-attr">on</span>: &#123;
      <span class="hljs-attr">click</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;...&#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">nodeType</h4>
<p>nodeType实际上是html的原生属性，这里第一次渲染时，nodeType为节点, 值为 1。</p>
<p>不清楚nodeType的小伙伴，可以移步： <a href="https://www.w3school.com.cn/jsref/prop_node_nodetype.asp" target="_blank" rel="nofollow noopener noreferrer">www.w3school.com.cn/jsref/prop_…</a></p>
<p>回归到我们的demo中，isRealElement = 1, 显示是true。这个时候会调用 emptyNodeAt</p>
<h4 data-id="heading-7">emptyNodeAt</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emptyNodeAt</span> (<span class="hljs-params">elm</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> VNode(nodeOps.tagName(elm).toLowerCase(), &#123;&#125;, [], <span class="hljs-literal">undefined</span>, elm)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题来了，第一次页面渲染时，oldVnode是id = "root"的真实dom节点。为什么需要调用emptyNodeAt方法，重新设置为虚拟dom节点？</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f70b90691e469f9a86f50e9322868b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其实有几点原因：</p>
<ul>
<li>
<ol>
<li>removeVnodes是基于虚拟dom操作</li>
</ol>
</li>
<li>
<ol start="2">
<li>invokeDestroyHook也是基于虚拟dom操作</li>
</ol>
</li>
<li>
<ol start="3">
<li>新旧节点diff对比，都是基于虚拟dom操作</li>
</ol>
</li>
</ul>
<p>此时，根节点root转化为虚拟dom之后(即oldVnode)，其数据结构如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>,
  <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">children</span>: [],
  <span class="hljs-attr">context</span>: Vue,
  <span class="hljs-attr">data</span>: &#123;&#125;,
  <span class="hljs-comment">// 注意此变化</span>
  <span class="hljs-attr">elm</span>: div#root
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，页面还没渲染时，只有一个空div，id = 'root', vue将其转化为vnode，其上面的oldVnode空节点 和 new Vue之后的vnode做对比。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5e311c6a24540a78b6db398c2f2d3ec~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>需要指出的是： parentElm 在第一次update时，指的是body</p>
<h1 data-id="heading-8">三. createElm</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span> (<span class="hljs-params">
  vnode,
  insertedVnodeQueue,
  parentElm,
  refElm,
  nested,
  ownerArray,
  index
</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-comment">// 嵌套组件处理</span>
  <span class="hljs-keyword">if</span>(createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-keyword">const</span> tag = vnode.tag
  <span class="hljs-keyword">if</span>(isDef(tag)) &#123;
      vnode.elm = vnode.ns
        ? nodeOps.createElementNS(vnode.ns, tag)
        : nodeOps.createElement(tag, vnode);
        
      setScope(vnode)
  
      <span class="hljs-keyword">if</span>(__WEEX__) &#123;
        <span class="hljs-comment">// ... weex相关处理</span>
      &#125;<span class="hljs-keyword">else</span> &#123;
        createChildren(vnode, children, insertedVnodeQueue)
        <span class="hljs-keyword">if</span> (isDef(data)) &#123;
          invokeCreateHooks(vnode, insertedVnodeQueue)
        &#125;
        insert(parentElm, vnode.elm, refElm)
      &#125;
  &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(isTrue(vnode.isComment))&#123;
     <span class="hljs-comment">// 注释节点</span>
     vnode.elm = nodeOps.createComment(vnode.text)
     insert(parentElm, vnode.elm, refElm)
  &#125;<span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 纯文本节点</span>
    vnode.elm = nodeOps.createTextNode(vnode.text)
    insert(parentElm, vnode.elm, refElm)
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>createComponent实现多层嵌套组件，这里不再赘述。不清楚的小伙伴，可以看我之前的《vue源码解析-组件化&虚拟DOM》。</p>
<p>第一次渲染时，触发createElm方法，传入的vnode即新的vnode。显然，在我们的demo中，tag = "div"，ns = undefined。 将会执行nodeOps.createElement方法。</p>
<p>nodeOps对象，实际上就是封装了对原生DOM的操作。 这里createElement方法，实际上就是调用：document.createElement方法，返回原生dom对象。</p>
<p>此时新的虚拟dom上elm属性，指向就是刚创建的div。此时 vnode数据结构如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>,
  <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">// elm属性值变更为 刚创建的 div dom对象</span>
  <span class="hljs-attr">elm</span>: div,
  <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">children</span>: [
    <span class="hljs-comment">// vnode  纯文本节点</span>
    &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  ],
  <span class="hljs-attr">context</span>: Vue,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">attrs</span>: &#123;...&#125;,
    <span class="hljs-attr">on</span>: &#123;
      <span class="hljs-attr">click</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;...&#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是：setScope(vnode)，实际上是对于elm真实dom的style对象，添加scopeId。</p>
<p>到这里，demo中的外层div已创建，但是这个时候还是没有文字显示。因为children中的文字，也是个虚拟dom，只不过他是普通纯文本节点而已。</p>
<p>下面流程，将调用 createChildren 方法。</p>
<h1 data-id="heading-9">四. createChildren</h1>
<p>其主干代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChildren</span> (<span class="hljs-params">vnode, children, insertedVnodeQueue</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
    createElm(children[i], insertedVnodeQueue, vnode.elm, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>, children, i)
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，我们可以看到，实际上是个递归循环操作。 无论我们的组件嵌套多少层，都将对每层vnode的childrens进行循环。然后一个个createElm，遇到childrens，继续调用createChildren。如此反复，递归一个个创建子组件。</p>
<p>在我们的demo中，子的childrens是一行文本，属于纯文本节点。那么createElm时，将进入最后一个else操作，创建文本节点。即原生的dom调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.createTextNode(text)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同理，子的vnode对象上的elm属性，指向了刚刚创建的文本节点的真实dom 对象。</p>
<p>最后调用update restoreActiveInstance方法，激活当前的父组件为 当前的activeInstance实例。</p>
<p>嗯，这只是个最简单的patch过程，还未涉及多层嵌套和对比。</p>
<p>因为这是第一次渲染过程，而diff是发生已渲染页面的情况下，再次发生页面需要变更。</p>
<p>下面，我们将进入数据变化，视图需要变化的patch过程</p>
<h1 data-id="heading-10">五. patchVnode</h1>
<h4 data-id="heading-11">reactiveSetter</h4>
<p>前面的章节介绍了依赖收集，我们知道，当数据改变时，会触发reactiveSetter。</p>
<p>首先reactiveSetter 会判断，前后的value是否相同，如果相同直接return。 否则进入下面的环节。</p>
<p>依赖收集时，Dep类的实例对象dep下有个subs数组，里面存放了依赖这些数据的watcher对象。</p>
<p>所以当触发reactiveSetter时，实际上是调用了每个watcher的update方法。</p>
<p>watcher的update方法，并不是直接去更新。而是将watcher放入一个更新队列里。</p>
<p><strong>注意： 这个更新队列的大小，最大是100个</strong></p>
<p>最后调用nextTick函数，设置promise更新队列，在callback中执行Scheduler job，即每个watcher的run方法。最终将进入第二轮patch。</p>
<p><strong>需要注意的是：为什么要有队列？这其实是两方面考虑：</strong></p>
<ul>
<li>性能考虑，因为同一个nextTick里，可能同一个组件，依赖了多个数据对象，而多个数据对象都变化了，没必要update多次，在队列中，vue会判断是否属于同一个watcher id。</li>
<li>多个组件，分别依赖了多个数据对象。每个组件，实际上都会有自己的nextTick。</li>
</ul>
<p>这里实际上远不止如此，后面我将单独开一个章节，分享更新队列和nextTick。</p>
<p>此时，oldVnode数据结构如下：</p>
<h4 data-id="heading-12">oldVnode</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>,
  <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">elm</span>: div,
  <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">children</span>: [
    &#123;
      <span class="hljs-attr">tag</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">text</span>: <span class="hljs-string">"这是根节点"</span>,
      <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">elm</span>: test,
      <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">children</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-comment">// ...</span>
    &#125;
  ],
  <span class="hljs-attr">context</span>: Vue,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">attrs</span>: &#123;...&#125;,
    <span class="hljs-attr">on</span>: &#123;
      <span class="hljs-attr">click</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;...&#125;
    &#125;
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">vnode (新的vnode)</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>,
  <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">elm</span>: div,
  <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">children</span>: [
    &#123;
      <span class="hljs-attr">tag</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-comment">// 注意，这里变了</span>
      <span class="hljs-attr">text</span>: <span class="hljs-string">"变了"</span>,
      <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">elm</span>: test,
      <span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">children</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-comment">// ...</span>
    &#125;
  ],
  <span class="hljs-attr">context</span>: Vue,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">attrs</span>: &#123;...&#125;,
    <span class="hljs-attr">on</span>: &#123;
      <span class="hljs-attr">click</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;...&#125;
    &#125;
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不难看出，此次isRealElement = false，将先执行sameVnode判断。</p>
<p>我们先看sameVnode做了些什么</p>
<h4 data-id="heading-14">sameVnode</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    a.key === b.key &&
    (
      (
        a.tag === b.tag &&
        a.isComment === b.isComment &&
        isDef(a.data) === isDef(b.data) &&
        sameInputType(a, b)
      )
      ||
      (
        isTrue(a.isAsyncPlaceholder) &&
        a.asyncFactory === b.asyncFactory &&
        isUndef(b.asyncFactory.error)
      )
    )
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里第一层判断就是key的判断，有没有很熟悉？ 这也就是我们写数组循环时，需要加key的原因。</p>
<p>sameInputType方法，其实很简单：</p>
<ul>
<li>
<ol>
<li>如果不是input节点，直接返回true</li>
</ol>
</li>
<li>
<ol start="2">
<li>如果是，那么判断虚拟dom上的data, attrs, type是否相等</li>
</ol>
</li>
</ul>
<p>下面终于进入了 patchVnode 方法：</p>
<p>主干代码如下：</p>
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
  
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-comment">// ... 省略异步占位组件</span>
  
  <span class="hljs-keyword">if</span> (isTrue(vnode.isStatic) &&
      isTrue(oldVnode.isStatic) &&
      vnode.key === oldVnode.key &&
      (isTrue(vnode.isCloned) || isTrue(vnode.isOnce))
  ) &#123;
      vnode.componentInstance = oldVnode.componentInstance
      <span class="hljs-keyword">return</span>
  &#125;
  
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 组件节点，需要先调用组件prepatch钩子，data,props,slot,listener等可能都需要更新</span>
  <span class="hljs-comment">// ...此处省略</span>
  
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
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，这里是虚拟dom前后对比更新的情况。大致分以下几种：</p>
<ul>
<li>
<ol>
<li>先判断oldVnode和vnode，是否相等，如果相等，return</li>
</ol>
</li>
<li>
<ol start="2">
<li>如果oldVnode是静态节点，并且vnode也是静态节点。并且，oldVnode.key 和 vnode.key相等。并且，vnode节点是克隆的或者是isOnce，那么直接返回，不需要对比了。</li>
</ol>
</li>
<li>
<ol start="3">
<li>如果新的vnode，不是文本节点，那么：</li>
</ol>
<ul>
<li>
<p>3.1 如果oldVnode和vnode都存在children，那么：</p>
<ul>
<li>3.1.1 如果2个children不相等，那么updateChildren （这里比较复杂，需要单独分析）</li>
</ul>
</li>
<li>
<p>3.2 如果新的vnode存在children， 而老的oldVnode不存在children，那么：</p>
<ul>
<li>
<p>3.2.1 如果老的oldVnode是文本节点，那么先清空真实dom中的内容，再把新的vnode的children添加到真实dom中。</p>
</li>
<li>
<p>3.2.2 如果老的oldVnode不是文本节点，那么直接添加到DOM中</p>
</li>
</ul>
</li>
<li>
<p>3.3 如果新的vnode不存在children，而老的oldVnode中存在children，那么：直接把dom中的子节点清空</p>
</li>
<li>
<p>3.4 如果新的vnode，老的oldVnode都不存在children，但是老的oldVnode是文本节点，那么直接清空DOM内容</p>
</li>
</ul>
</li>
<li>
<ol start="4">
<li>如果新的vnode是文本节点，老的oldVnode也是文本节点，那么：如果内容不相等，用新的内容覆盖老的内容</li>
</ol>
</li>
</ul>
<h4 data-id="heading-15">updateChildren</h4>
<p>上面，3.1.1情况，如果新老vnode，都存在children，但是他们不相等，那么将调用updateChildren方法。这里单独说明。</p>
<p>其实，都有children的情况下，也不外乎四种处理方式，分别是：</p>
<ul>
<li>
<ol>
<li>创建子节点</li>
</ol>
</li>
<li>
<ol start="2">
<li>删除子节点</li>
</ol>
</li>
<li>
<ol start="3">
<li>移动子节点</li>
</ol>
</li>
<li>
<ol start="4">
<li>更新子节点</li>
</ol>
</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21ffc3e1ff124ffd85eaf77fed1a962c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
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
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/128fb71df39c42f0a3e090b6b318a420~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到，updateChildren阶段，实际上是将新的vnode和老的oldVnode，进行双重循环。</p>
<p>如下：</p>
<h4 data-id="heading-16">开始</h4>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e433c5f52b014b3281a8a92b58a795d6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">第二步</h4>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d3940378f1440b9bf003901ee7cf25c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">第三步</h4>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/661f88ea286a4ef18da863728747f678~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">第四步</h4>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38254c90bec34fb8a9d8151ef4433ed8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">第五步</h4>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/add57b7bbd034899800d9bcb1e4d6aeb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">第六步</h4>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae4a80c23304476a38fd09513312e1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>diff的比较，实际上，都是以新的vnode为基准，不断的调整老的vnode位置。</p>
<p>可以看到diff的比较策略， 左左，右右，左右，右左</p>
<h1 data-id="heading-22">六. 总结</h1>
<h4 data-id="heading-23">patch第一阶段：activeInstance</h4>
<ul>
<li>
<ol>
<li>同一时刻，只会有一个组件正在实例化和patch</li>
</ol>
</li>
<li>
<ol start="2">
<li>设置当前被实例化的activeInstace对象，并且保留preActiveInstace。</li>
</ol>
</li>
<li>
<ol start="3">
<li>当前保留的activeInstace，在patch过程中，遇到嵌套组件，需要做为其parent，进行组件的实例化。</li>
</ol>
</li>
<li>
<ol start="4">
<li>当前子组件patch完成后，将切换当前的activeInstance为preActiveInstance，如果还有多层嵌套的话，再次重复上面的过程。</li>
</ol>
</li>
</ul>
<h4 data-id="heading-24">patch第二阶段：root dom patch</h4>
<ul>
<li>
<ol>
<li>dom根即 div#root容器，页面首页渲染时，oldVnode不是一个虚拟dom，而是一个真实dom。此时oldVnode.nodeType = 1，</li>
</ol>
</li>
<li>
<ol start="2">
<li>将div#root本身，转化为空的虚拟dom。将其作为oldVnode与新的vnode进行对比。</li>
</ol>
</li>
<li>
<ol start="3">
<li>进入createElm，那么：</li>
</ol>
<ul>
<li>3.1 如果存在组件，那么进行组件化patch （组件化不了解的小伙伴可以看我的上一篇）</li>
</ul>
</li>
<li>
<ol start="4">
<li>完成insert，注意此时并没有进入patchVnode diff。</li>
</ol>
</li>
<li>
<ol start="5">
<li>设置dom style scope id</li>
</ol>
</li>
</ul>
<h4 data-id="heading-25">patch第三阶段：reactiveSetter</h4>
<ul>
<li>
<ol>
<li>页面完成了首次渲染，如果页面上有数据变化了，将触发reactiveSetter。（依赖收集不清楚的小伙伴，可以看我之前的分享：《vue源码解析-响应式原理》）</li>
</ol>
</li>
<li>
<ol start="2">
<li>对比新老数据是否相等，如果相等，直接return</li>
</ol>
</li>
<li>
<ol start="3">
<li>数据不相等，将根dep下的subs，循环调用watcher的update方法。</li>
</ol>
</li>
<li>
<ol start="4">
<li>watcher的update，并不是直接去通知更新。 而是放在一个队列中。更新通知将进入queueWatcher</li>
</ol>
</li>
<li>
<ol start="5">
<li>queueWatcher中优化不必要的多次渲染，比如：多个值的变化，都指向同一个watcher，没必要触发多次patch</li>
</ol>
</li>
<li>
<ol start="6">
<li>Scheduler job中，将调用watcher的run方法</li>
</ol>
</li>
<li>
<ol start="7">
<li>执行render函数，获取新的vnode，执行update，重复前1个阶段。</li>
</ol>
</li>
<li>
<ol start="8">
<li>isRealElement 为undefined，进入 patchVnode阶段</li>
</ol>
</li>
</ul>
<h4 data-id="heading-26">patch第四阶段：patchVnode</h4>
<ul>
<li>
<ol>
<li>比较新老节点，是否相等。即oldVnode == vnode。如果相等，直接return</li>
</ol>
</li>
<li>
<ol start="2">
<li>是否是静态节点，是否前后key相等，或者 是否是克隆节点/isOnce。是直接return。（备注：静态标记是compiler第二阶段生成的）</li>
</ol>
</li>
<li>
<ol start="3">
<li>如果是比较的是组件节点，那么根据vnode更新oldVnode组件props, listener, slots, parent等属性</li>
</ol>
</li>
<li>
<ol start="4">
<li>新的vnode是文本节点，那么：</li>
</ol>
<ul>
<li>4.1 如果oldVnode和vnode 都存在childrens，
<ul>
<li>4.1.1 如果2个children相等，那么直接return</li>
<li>4.1.2 如果2个children不相等，那么只需第5阶段-updateChildren</li>
</ul>
</li>
<li>4.2 如果新的节点存在children, 而老的节点不存在children，那么：
<ul>
<li>4.2.1 如果老的节点是文本节点，那么先清空老的子节点内容</li>
<li>4.2.1 将新的vnode的多个children，插入到老的dom流中</li>
</ul>
</li>
<li>4.3 如果新的节点不存在children，而老的节点存在children，那么：
<ul>
<li>4.3.1 将老的childrens全部删除</li>
</ul>
</li>
<li>4.4 如果老节点，新节点都不存在children，并且老的节点是文本节点，那么清空老的节点内容</li>
</ul>
</li>
<li>
<ol start="5">
<li>新老节点都是文本节点，但是文件节点内容不同，那么直接用新的文本内容 更新 老的文本内容</li>
</ol>
</li>
</ul>
<h4 data-id="heading-27">patch第五阶段：updateChildren</h4>
<ul>
<li>
<ol>
<li>同层比较，不同层的节点是不能复用的</li>
</ol>
</li>
<li>
<ol start="2">
<li>oldStartVnode指的是未处理的开始节点，newStartVnode新的未处理的开始节点</li>
</ol>
</li>
<li>
<ol start="3">
<li>oldEndVnode指的是未处理的最后节点，newEndVnode新的未处理的最后节点</li>
</ol>
</li>
<li>
<ol start="4">
<li>比较策略：oldStartVnode 和 newStartVnode 先比较，那么：</li>
</ol>
<ul>
<li>4.1 如果相等，那么将 oldStartVnode，newStartVnode 都往后挪一个</li>
<li>4.2 如果不相等，那么进入 oldEndVnode， newEndVnode 比较</li>
</ul>
</li>
<li>
<ol start="5">
<li>oldEndVnode 和 newEndVnode 比较，那么：</li>
</ol>
<ul>
<li>5.1 如果相等，那么将 oldEndVnode 和 newEndVnode 都往前挪一个</li>
<li>5.2 如果不相等，那么进入 oldStartVnode 和 newEndVnode</li>
</ul>
</li>
<li>
<ol start="6">
<li>oldStartVnode 和 newEndVnode 比较，那么：</li>
</ol>
<ul>
<li>6.1 如果相等，那么将 oldStartVnode 向后挪一个，将 newEndVnode向前挪一个。</li>
<li>6.2 如果不相等，将进入 oldEndVnode 和 newStartVnode 比较</li>
</ul>
</li>
<li>
<ol start="7">
<li>oldEndVnode 和 newStartVnode 比较，那么：</li>
</ol>
<ul>
<li>7.1 如果相等，将 oldEndVnode 往前挪一个，newStartVnode 往后挪一个</li>
<li>7.2 如果不相等，那么将进入 查找节点</li>
</ul>
</li>
<li>
<ol start="8">
<li>根据新的vnode位置，去同层的老节点中查找。</li>
</ol>
<ul>
<li>8.1 如果存在，那么移动到对应的位置（注意，是未处理节做参照物，而不是已处理节点）</li>
<li>8.2 如果不存在，那么根据新的节点children，创建节点，放入老的节点之中</li>
<li>8.3 如果老的节点，在新的节点中不存在，那么将老的对应的节点删除</li>
</ul>
</li>
<li>
<ol start="9">
<li>这就是双指针算法，如此循环，就能将所有节点对比完成。总的概括，不外乎三点：</li>
</ol>
<ul>
<li>9.1 同层不存在，直接更新移动</li>
<li>9.2 同层不存在，那么创建</li>
<li>9.3 新的节点，同层 在 老节点中 不存在，那么删除</li>
</ul>
</li>
</ul>
<p>以上，就是patch阶段的总体流程。</p>
<p>码字不易，多多关注😽</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            