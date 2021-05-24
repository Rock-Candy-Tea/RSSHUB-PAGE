
---
title: '虚拟 DOM 和 diff 算法 -02'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83b5bbc021014742a91ce005547350ae~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 19:27:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83b5bbc021014742a91ce005547350ae~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文是关于虚拟 DOM 和 diff 算法的学习笔记，目的在于更好的理解 Vue 的底层原理，篇幅较长，故而拆分为几篇，今后将陆续更新。</p>
</blockquote>
<p>上一篇<a href="https://juejin.cn/post/6960906343259570206" target="_blank">《虚拟 DOM 和 diff 算法 -01》</a>我们手写实现了 h 函数，本篇着重介绍 diff 算法。</p>
<h1 data-id="heading-0">diff 算法的特点</h1>
<ul>
<li><strong>如果是往数组的最后面添加节点，那么前面的节点不会改动</strong></li>
</ul>
<p>比如有如下新(vnode2)旧(vnode1)两个节点，那么执行 <code>patch(vnode1, vnode2)</code> 会发现仅仅浏览器只是追加了一个节点 <code><div>东风破</div></code>， 不会改变前两个。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">"div"</span>, &#123;&#125;, [
  h(<span class="hljs-string">"div"</span>, <span class="hljs-string">"七里香"</span>),
  h(<span class="hljs-string">"div"</span>, <span class="hljs-string">"东风破"</span>)
])
<span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">"div"</span>, &#123;&#125;, [
  h(<span class="hljs-string">"div"</span>, <span class="hljs-string">"七里香"</span>),
  h(<span class="hljs-string">"div"</span>, <span class="hljs-string">"东风破"</span>),
  h(<span class="hljs-string">"div"</span>, <span class="hljs-string">"兰亭序"</span>)
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过在浏览器调试工具里直接将“七里香”改成“七里不香”，然后通过点击按钮执行 patch(vnode1, vnode2) 会发现“七里不香”依旧没变。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83b5bbc021014742a91ce005547350ae~tplv-k3u1fbpfcp-watermark.image" alt="gif5新文件.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>key 很重要，key 作为节点的标识，告诉 diff 算法在更改前后节点是否为同一个</strong></li>
</ul>
<p>如果是往数组的开头添加节点，则所有的节点都会被改动，想要做到最小化更新，需要给每个节点添加 key 属性，这样 <code><div>七里香</div></code> 和 <code><div>东风破</div></code> 两个节点就不会被改动了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">"div"</span>, &#123;&#125;, [
  h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">1</span> &#125;, <span class="hljs-string">"七里香"</span>),
  h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">2</span> &#125;, <span class="hljs-string">"东风破"</span>)
])
<span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">"div"</span>, &#123;&#125;, [
  h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">3</span> &#125;, <span class="hljs-string">"兰亭序"</span>),
  h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">1</span> &#125;, <span class="hljs-string">"七里香"</span>),
  h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">2</span> &#125;, <span class="hljs-string">"东风破"</span>)
])
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>只有是同一个虚拟节点，才进行精细化比较，否则直接删除旧节点，插入新节点</strong></li>
</ul>
<p>判断两个节点是否为同一个，是根据比较选择器，也就是 sel 的值和 key 的值是否都相同，都相等则判断为同一个虚拟节点</p>
<ul>
<li><strong>只进行同层比较</strong></li>
</ul>
<p>新旧节点的层级要相同，比如下面的例子里新节点比旧节点多了层 div，则不会进行精细化比较，直接删除旧节点插入新节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">"div"</span>, &#123;&#125;, [
  h(<span class="hljs-string">'div'</span>, [
    h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">3</span> &#125;, <span class="hljs-string">"兰亭序"</span>),
    h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">1</span> &#125;, <span class="hljs-string">"七里香"</span>),
    h(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-number">2</span> &#125;, <span class="hljs-string">"东风破"</span>)
  ])
])
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">手写 patch 函数</h1>
<p>diff 算法是通过 patch 函数实现的，在开始手写之前，我们先来理清 patch 函数做了什么</p>
<h2 data-id="heading-2">函数功能分析</h2>
<p>可以通过之前下载到 node_modules 里的 snabbdom 查看源码，patch 函数被定义在了 snabbdom 下的 src 目录下的 init.ts 里</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// init.ts</span>
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;
    <span class="hljs-comment">// ...忽略部分代码</span>
    <span class="hljs-comment">// 通过 isVnode 函数判断旧节点是否为虚拟节点</span>
    <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
      oldVnode = emptyNodeAt(oldVnode); <span class="hljs-comment">// 不是则通过 emptyNodeAt 包装为虚拟节点</span>
    &#125;
    <span class="hljs-comment">// 通过 sameVnode 函数判断新旧节点是否为为同一个节点</span>
    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
      <span class="hljs-comment">// 相同...</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 不同...</span>
    &#125;
    <span class="hljs-comment">// ...忽略部分代码</span>
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据源码得到如下流程图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ce886778eb04372963d2147aed7c60a~tplv-k3u1fbpfcp-watermark.image" alt="yuque_diagram.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">手写第一次上树</h2>
<p>新建 patch.js 文件，引入 vnode 函数用于将非虚拟节点的 oldVnode  包装为虚拟节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// patch.js</span>
<span class="hljs-keyword">import</span> vnode <span class="hljs-keyword">from</span> <span class="hljs-string">'./vnode.js'</span>
<span class="hljs-keyword">import</span> creatElement <span class="hljs-keyword">from</span> <span class="hljs-string">'./creatElement.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (oldVnode, newVnode) => &#123;
  <span class="hljs-comment">// 判断 oldVnode 是否为虚拟节点</span>
  <span class="hljs-keyword">if</span> (oldVnode.sel === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-comment">// oldVnode 不是虚拟节点，则包装成虚拟节点</span>
    oldVnode = vnode(oldVnode.tagName.toLowerCase, &#123;&#125;, [], <span class="hljs-literal">undefined</span>, oldVnode)
  &#125; 
  <span class="hljs-comment">// 判断 oldVnode, newVnode 是否为同一节点</span>
  <span class="hljs-keyword">if</span> (oldVnode.sel === newVnode.sel && oldVnode.key === newVnode.key) &#123;
    <span class="hljs-comment">// 同一节点</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 不是同一节点</span>
    <span class="hljs-keyword">const</span> domNode = creatElement(newVnode)
    <span class="hljs-comment">// 将新节点上树</span>
    oldVnode.elm.parentNode?.insertBefore(domNode, oldVnode.elm)
    <span class="hljs-comment">// 删除旧节点</span>
    oldVnode.elm.parentNode?.removeChild(oldVnode.elm)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 creatElement.js 并在 patch.js 引入 creatElement 函数，用于创建新节点，并将对应的虚拟节点的 elm 属性赋值为创建出的新节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * creatElement.js 
 * 将 vnode 创建为真正的 DOM 节点(但是没上树的孤儿节点)
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span> (<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> domNode = <span class="hljs-built_in">document</span>.createElement(vnode.sel)
  vnode.elm = domNode
  <span class="hljs-comment">// 判断 vnode 有子节点(children)还是文本(text)</span>
  <span class="hljs-keyword">if</span> (vnode.children !== <span class="hljs-literal">undefined</span> && vnode.children.length && vnode.text === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-comment">// 有子节点</span>
    vnode.children.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
      <span class="hljs-comment">// 调用 createElement 意味着创建出了 DOM，并且将改虚拟节点的 elm 属性指向了这个 DOM，</span>
      <span class="hljs-comment">// 但这个 DOM 是个孤儿节点，还没上树</span>
      <span class="hljs-keyword">const</span> childNode = createElement(item)
      item.elm = childNode
      domNode.appendChild(childNode)
    &#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 内部为文本</span>
    domNode.innerText = vnode.text
    vnode.elm = domNode
  &#125;
  <span class="hljs-keyword">return</span> domNode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们已经完成了上面 patch 函数流程图中除了“精细化比较”之外的内容。接下来就开始着手当 oldVnode 和 newVnode 是同一节点的情况下的精细化比较的内容，这部分将有较多的图示，写在本篇难免会导致页面过长，我将在下篇继续分享~</p>
<h1 data-id="heading-4">One More Thing</h1>
<p>本文有用到一些插入节点的方法，现在就此做一个扩展总结</p>
<ul>
<li>innerHTML（属性）：获取标签内部的HTML内容</li>
<li>outerHTML（属性）：获取包括目标标签在内，以及内部HTML的内容</li>
<li>appendChild（函数）：向目标标签末尾添加子节点，返回参数节点</li>
<li>insertBefore（函数）：向目标节点的第二个参数位置添加第一个参数为子节点，返回第一个参数</li>
<li>insertAdjacentHTML（函数）：向目标节点的指定位置添加节点</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24aeee4d4cef440caa685e09312d29d7~tplv-k3u1fbpfcp-watermark.image" alt="感谢.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34a30a24696466296ac3a81ae7d4b68~tplv-k3u1fbpfcp-watermark.image" alt="点赞.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            