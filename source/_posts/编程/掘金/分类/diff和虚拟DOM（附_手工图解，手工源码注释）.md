
---
title: 'diff和虚拟DOM（附_手工图解，手工源码注释）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5952c5ef8046778d68e0e13d7fb913~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 23:56:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5952c5ef8046778d68e0e13d7fb913~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">snabbdom 介绍</h1>
<p>Snabbdom 是一个虚拟 DOM 库，专注提供简单、模块性的体验，以及强大的功能和性能。由于vue2.x中的diff借鉴了snabbdom。所以我们在这篇文章以snabbdom的源码为研究对象。
<a href="https://github.com/snabbdom/snabbdom" target="_blank" rel="nofollow noopener noreferrer">snabbdom github链接</a></p>
<ul>
<li>优异的性能，在 Virtual DOM Benchmark 测试中，Snabbdom 是最快的虚拟 DOM 库之一</li>
<li>可通过模块进行扩展</li>
</ul>
<p>（我的废话）由于snabbdom在v0.6.0版本以上是用TypeScript写的，那么我们主要也是以TypeScript版本的去进行理解。TypeScript编写的库对于我们进行源码解读是有好处的，虽然看起来会多很多类型判断，但是同时也增加了代码可读性，例如在库中的v-node会有很多的参数，如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vnode</span> (<span class="hljs-params">sel: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
  data: <span class="hljs-built_in">any</span> | <span class="hljs-literal">undefined</span>,
  children: <span class="hljs-built_in">Array</span><VNode | <span class="hljs-built_in">string</span>> | <span class="hljs-literal">undefined</span>,
  text: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
  elm: Element | Text | <span class="hljs-literal">undefined</span></span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">const</span> key = data === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">undefined</span> : data.key
  <span class="hljs-keyword">return</span> &#123; sel, data, children, text, elm, key &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们就可以很轻易的得到Vnode中每个参数代表是什么，所以在下面的内容，我们也会以Vnode为切入点去理解snabbdom的主要功能</p>
<h1 data-id="heading-1">虚拟DOM 、虚拟节点(Vnode)</h1>
<blockquote>
<p>虚拟DOM:用JavaScript对象描述DOM的层次结构。DOM中的一切属性都在虚拟DOM中有对应的属性</p>
</blockquote>
<p>至于如何将DOM转换成虚拟DOM可以参考我上一次的分享，类似于这篇笔记中将DOM转化为tokens的过程，感兴趣可以自己看一下我就不再介绍了。  <a href="https://blog.csdn.net/XX4xi/article/details/114106685?spm=1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer"><strong>mustache模板引擎链接</strong></a></p>
<p>在snabbdom中，作者用了一个<strong>h函数</strong>对我们的虚拟DOM进行了简单的处理，将我们的不规则的虚拟DOM封装成了各种参数都有对应位置的Vnode虚拟节点。让我们再来看一看源码中的Vnode</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vnode</span> (<span class="hljs-params">sel: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
  data: <span class="hljs-built_in">any</span> | <span class="hljs-literal">undefined</span>,
  children: <span class="hljs-built_in">Array</span><VNode | <span class="hljs-built_in">string</span>> | <span class="hljs-literal">undefined</span>,
  text: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
  elm: Element | Text | <span class="hljs-literal">undefined</span></span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">const</span> key = data === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">undefined</span> : data.key
  <span class="hljs-keyword">return</span> &#123; sel, data, children, text, elm, key &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我来简单讲一下Vnode中每个参数的意思</p>
<ol>
<li>sel:DOM中的各个标签如"div","p","h1","a"等等</li>
<li>data:标签上的属性以及样式，如a标签中的链接，class之类的</li>
<li>children:这个DOM上的子节点</li>
<li>text:文本内容</li>
<li>elm:挂载的标签</li>
<li>key:服务于最小更新(diff)后面会讲</li>
</ol>
<h2 data-id="heading-2">h函数</h2>
<p>那么h函数做了什么事情呢,让我们来先看一下h函数中的核心部分</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: <span class="hljs-built_in">string</span>, data: VNodeData | <span class="hljs-literal">null</span></span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: <span class="hljs-built_in">string</span>, children: VNodeChildren</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: <span class="hljs-built_in">string</span>, data: VNodeData | <span class="hljs-literal">null</span>, children: VNodeChildren</span>): <span class="hljs-title">VNode</span>
<span class="hljs-title">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span> (<span class="hljs-params">sel: <span class="hljs-built_in">any</span>, b?: <span class="hljs-built_in">any</span>, c?: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">VNode</span> </span>&#123;
 <span class="hljs-title">var</span> <span class="hljs-title">data</span>: <span class="hljs-title">VNodeData</span> = </span>&#123;&#125;
 <span class="hljs-title">var</span> <span class="hljs-title">children</span>: <span class="hljs-title">any</span>
 <span class="hljs-title">var</span> <span class="hljs-title">text</span>: <span class="hljs-title">any</span>
 <span class="hljs-title">var</span> <span class="hljs-title">i</span>: <span class="hljs-title">number</span>
 <span class="hljs-title">if</span> (<span class="hljs-params">c !== <span class="hljs-literal">undefined</span></span>) </span>&#123;
   <span class="hljs-title">if</span> (<span class="hljs-params">b !== <span class="hljs-literal">null</span></span>) </span>&#123;
     <span class="hljs-title">data</span> = <span class="hljs-title">b</span>
   &#125;
   <span class="hljs-title">if</span> (<span class="hljs-params">is.array(c)</span>) </span>&#123;
     children = c
   &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(c)) &#123;
     text = c
   &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (c && c.sel) &#123;
     children = [c]
   &#125;
 &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (b !== <span class="hljs-literal">undefined</span> && b !== <span class="hljs-literal">null</span>) &#123;
   <span class="hljs-keyword">if</span> (is.array(b)) &#123;
     children = b
   &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(b)) &#123;
     text = b
   &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (b && b.sel) &#123;
     children = [b]
   &#125; <span class="hljs-keyword">else</span> &#123; data = b &#125;
 &#125;
 <span class="hljs-keyword">if</span> (children !== <span class="hljs-literal">undefined</span>) &#123;
   <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
     <span class="hljs-keyword">if</span> (is.primitive(children[i])) children[i] = vnode(<span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, children[i], <span class="hljs-literal">undefined</span>)
   &#125;
 &#125;
 <span class="hljs-keyword">if</span> (
   sel[<span class="hljs-number">0</span>] === <span class="hljs-string">'s'</span> && sel[<span class="hljs-number">1</span>] === <span class="hljs-string">'v'</span> && sel[<span class="hljs-number">2</span>] === <span class="hljs-string">'g'</span> &&
   (sel.length === <span class="hljs-number">3</span> || sel[<span class="hljs-number">3</span>] === <span class="hljs-string">'.'</span> || sel[<span class="hljs-number">3</span>] === <span class="hljs-string">'#'</span>)
 ) &#123;
   addNS(data, children, sel)
 &#125;
 <span class="hljs-keyword">return</span> vnode(sel, data, children, text, <span class="hljs-literal">undefined</span>)
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在h函数中，我们可以看到对a、b、c做了各种各样的if判断，实际上就是判断这个虚拟DOM中，少了哪些参数。让传入的参数能到对应的位置。</p>
</blockquote>
<p>在这里我从snabbdom中的引入了h函数，将下面的虚拟DOM转换成Vnode辅助理解
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5952c5ef8046778d68e0e13d7fb913~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415e69c13d784153afb9488618348721~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
当我们拿到了我们想要的Vnode，不考虑其他的边边角角的功能（识别style 、class之类的功能），接下来我们只需要做两件事了</p>
<ol>
<li>利用diff算法. 让我们知道oldVnode（旧的节点）和newVnode（新的节点）之间的不同。</li>
<li>知道不同之后然后将旧的节点<strong>最小量更新</strong>为新的节点，也就是把不同的虚拟DOM渲染到真实的DOM中去。</li>
</ol>
<h1 data-id="heading-3">diff算法</h1>
<h2 data-id="heading-4">diff简介</h2>
<p>这里我们介绍一下diff，新虚拟DOM和老虚拟DOM进行diff（精细化比较），算出应该如何最小量更新，最后反应到真正的DOM上。让我们来看一下下面这张diff的源码图（snabbdom的inis.ts中的updateChildren函数）。先不用关注里面的具体内容</p>
<blockquote>
<p>我们可以先通过简单的观察发现，在不停的if判断中穿插着patchVnode。patchVnode()简单的讲就是更新节点的办法。那么在这个过程中，我们通过不断比较，找到不同的地方，然后针对性的更新节点。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8be208fd4a014c81b4f8b2dbeffa1cdf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
好的，到这里我们就可以开始diff了。但是在下面的学习过程中同时我们要带着两个问题</p>
<ol>
<li><strong>diff到底是怎么找到新旧Vnode中不同的地方，并更新旧节点。</strong></li>
<li>找到了之后是如何上树</li>
</ol>
<h2 data-id="heading-5">diff算法的过程</h2>
<p>这里偷了<a href="https://calendar.perfplanet.com/2013/diff/" target="_blank" rel="nofollow noopener noreferrer">React’s diff algorithm</a>中的图来介绍
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/921b1a7a99344b0989d3f1cdcef76663~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
图中连线的都是同一层级的节点，我们在diff的原则就是。只进行同层比较，不会进行跨层比较。即使是同一片虚拟节点，但是跨层了，就不会diff了，会删除旧的，插入新的。</p>
<h3 data-id="heading-6">关于key</h3>
<p>在同一层级节点中，只有是同一个虚拟节点，才进行精细化，否则就是暴力删除旧的插入新的。那么如何确定我们的节点是同一个虚拟节点呢？答案是添加唯一标识key。当我们为每一个节点都添加了唯一的key，我们再去更新就会比较有效率了。</p>
<p><strong>当节点z想插入cd之间的节点时</strong></p>
<h4 data-id="heading-7">无key更新</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81d21f5daddf47cca9b53d1671527410~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d35091b3e2b494aa787d41e2ae85b3a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果节点没有添加key，那么z就会硬生生的挤入cd之间然后把d的位置占住。那么后面的更新就会把d变成z，e变成d,然后再重新创建一个e。如果后面还有fghizklmnopgrszuvwhyz的话，那么后面每一个节点都需要重新更新。也就是一个个vnode去进行比较，发现其文本节点不对，就会一个个进行替换例。那么我们怎么来进行优化呢</p>
</blockquote>
<h4 data-id="heading-8">有key更新</h4>
<p>再次偷图<a href="https://calendar.perfplanet.com/2013/diff/" target="_blank" rel="nofollow noopener noreferrer">React’s diff algorithm</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84aa8cb9881f4675859787ca42f193f7~tplv-k3u1fbpfcp-zoom-1.image" alt="有key与无key的对比" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当我们为每一个节点都添加上了key，再次在cd之间插入z，c后面的节点在更新的时候就不会，重新创建了。换个方式说，c后面的节点是复用了，并没有更新。那么这样的效率就会快很多了，只需要在c后面创建一个z就可以了</p>
</blockquote>
<p>对比了一下着这个案例的两种情况，我们可以发现携带key的时候，我们可以把没有变化的部分识别出来，再添加的时候就只做了一次添加的DOM操作。而没有key的时候，那么我们需要做的DOM操作次数就得看这个节点后面有多长了……</p>
<h3 data-id="heading-9">patch函数</h3>
<p>patch函数是我们做diff的一个入口，我们将从这个函数为起点，一步一步的得到我们想要的效果。在snabbdom中的init.ts的最后，返回了一个patch函数。我会在源码上添加注释，来解释一些关键的判断，帮助理解。如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;
   <span class="hljs-comment">//这里oldVnode的类型是VNode或者Element也就说明了我们的oldVnode可以传一个DOM元素。</span>
   <span class="hljs-keyword">let</span> i: <span class="hljs-built_in">number</span>, <span class="hljs-attr">elm</span>: Node, <span class="hljs-attr">parent</span>: Node
   <span class="hljs-keyword">const</span> insertedVnodeQueue: VNodeQueue = []
   <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.pre.length; ++i) cbs.pre[i]()
   <span class="hljs-comment">// 判断oldVnode是虚拟节点还是DOM节点</span>
   <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
     <span class="hljs-comment">//如果oldVnode不是虚拟节点，那么将oldVnode通过emptyNodeAt()包装成虚拟节点</span>
     oldVnode = emptyNodeAt(oldVnode)
   &#125;
   <span class="hljs-comment">//通过sameVnode()判断oldVnode和我们传入的新的Vnode是不是同一个节点</span>
   <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
     <span class="hljs-comment">//如果是，那就进行精细化比较</span>
     patchVnode(oldVnode, vnode, insertedVnodeQueue)
   &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-comment">//不是就之间删除旧的节点、插入新的节点</span>
     elm = oldVnode.elm!
     parent = api.parentNode(elm) <span class="hljs-keyword">as</span> Node
 <span class="hljs-comment">//创建新的节点</span>
     createElm(vnode, insertedVnodeQueue)

     <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">null</span>) &#123;
       api.insertBefore(parent, vnode.elm!, api.nextSibling(elm))
       <span class="hljs-comment">//删除旧的节点</span>
       removeVnodes(parent, [oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
     &#125;
   &#125;

   <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < insertedVnodeQueue.length; ++i) &#123;
     insertedVnodeQueue[i].data!.hook!.insert!(insertedVnodeQueue[i])
   &#125;
   <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.post.length; ++i) cbs.post[i]()
   <span class="hljs-keyword">return</span> vnode
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在这里有必要稍微的说一下，将vnode转换为DOM我们使用了createElm()函数。但由于我们传入的Vnode是有子节点Children的，那么我们在创建节点的时候就会遇到数组对象嵌套的问题。在这里我就不具体细节的将createElm进行解读。但比较主要的是，createElm()在前面写好了vnode的各个属性该去的地方，然后再通过在对子节点遍历的时候调用自己，也就是递归来解决这个问题的，这里我用查找功能标出了createElm这个函数，方便大家阅读，我也将图贴在下面。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5962f6240ac4f29b44330200b26f161~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时我也将sameVnode()函数的代码贴下来，贴出来的原因是让大家看到snabbdom对个两个Vnode是不是相同的判断依据</p>
<ol>
<li>vnode的key相同</li>
<li>vnode的选择器相同</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1: VNode, vnode2: VNode</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> vnode1.key === vnode2.key && vnode1.sel === vnode2.sel
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他的小函数也确实不难，感兴趣的就自己理解，我们主要先把大体逻辑理通，主要是我懒( ̀⌄ ́)</p>
<blockquote>
<p>回到正题，通过patch函数我们可以看到，当我们进行了两次判断后，进入了patchVnode函数，那么接下来我们顺藤摸瓜进入patchVnode函数看看</p>
</blockquote>
<h3 data-id="heading-10">patchVnode函数</h3>
<blockquote>
<p>patchVnodez主要就是告诉了我们虚拟 DOM 如何实现 DOM 的更新，做了哪些逻辑了判断。在学习这一部分的时候，需要思考为什么可以这样判断？为什么要这样做？</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode: VNode, vnode: VNode, insertedVnodeQueue: VNodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">const</span> hook = vnode.data?.hook
    hook?.prepatch?.(oldVnode, vnode)
    <span class="hljs-keyword">const</span> elm = vnode.elm = oldVnode.elm!
    <span class="hljs-comment">//定义旧节点的子节点</span>
    <span class="hljs-keyword">const</span> oldCh = oldVnode.children <span class="hljs-keyword">as</span> VNode[]
    <span class="hljs-comment">//定义新节点的子节点</span>
    <span class="hljs-keyword">const</span> ch = vnode.children <span class="hljs-keyword">as</span> VNode[]
    <span class="hljs-comment">//判断oldVnode和vnode是不是同一个对象</span>
    <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 是，就不做操作</span>

    <span class="hljs-keyword">if</span> (vnode.data !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.update.length; ++i) cbs.update[i](oldVnode, vnode)
      vnode.data.hook?.update?.(oldVnode, vnode)
    &#125;
    <span class="hljs-comment">//判断vnode中是否有text属性，isUndef是判断里面的内容是不是undefined</span>
    <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
      <span class="hljs-comment">//如果vnode.text是undefined</span>
      <span class="hljs-comment">//当vnode中没有text属性，就意味着vnode中存在children</span>

      <span class="hljs-comment">//如果oldCh和ch都不是undefined</span>
      <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
        <span class="hljs-comment">//并且oldCh不等于ch，进入updateChildren()</span>
        <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
        <span class="hljs-comment">//如果Vnode有Children</span>
        <span class="hljs-comment">//添加Vnode中的Children</span>
        <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) api.setTextContent(elm, <span class="hljs-string">''</span>)
        addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
        <span class="hljs-comment">//如果oldVnode有Children</span>
        <span class="hljs-comment">//删除oldVnode中的Children</span>
        removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
        api.setTextContent(elm, <span class="hljs-string">''</span>)
      &#125;
      <span class="hljs-comment">//判断oldVnode和vnode的text是否相同</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
      <span class="hljs-comment">//判断oldCh是否存在</span>
      <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
        <span class="hljs-comment">//如果存在，旧把oldCh删除，然后吧vnode.text替换进去</span>
        removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>)
      &#125;
      api.setTextContent(elm, vnode.text!)
    &#125;
    hook?.postpatch?.(oldVnode, vnode)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>到这里我们可以看到虽然我们是说提高性能，但是还是有些地方是直接删除旧的插入新的。原因可能是这种情况其实我们并不会经常遇到，所以在优化的过程中并不一定要全都去做对比。接下来我们要进入最核心的部分updateChildren函数，也就是做diff算法地方。</p>
</blockquote>
<h3 data-id="heading-11">updateChildren函数（diff算法）</h3>
<p>patchVnode于updateChildren直接有一个互相引用的过程，因为我们第一次从patchVnode进入到updateChildren时，并不知道oldVnodeChildren中还有没有子节点，所以我们需要在每一次对比的中间再次加入patchVnode，这样循环调用，就可以对每一层有子节点的子节点都进行相应的处理</p>
<p>insertBefore在参考节点之前插入一个拥有指定父节点的子节点
首先我先将updateChildren函数代码贴出，然后分段讲解</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm: Node,
    oldCh: VNode[],
    newCh: VNode[],
    insertedVnodeQueue: VNodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]
    <span class="hljs-keyword">let</span> oldKeyToIdx: KeyToIndexMap | <span class="hljs-literal">undefined</span>
    <span class="hljs-keyword">let</span> idxInOld: <span class="hljs-built_in">number</span>
    <span class="hljs-keyword">let</span> elmToMove: VNode
    <span class="hljs-keyword">let</span> before: <span class="hljs-built_in">any</span>

    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
        oldStartVnode = oldCh[++oldStartIdx] <span class="hljs-comment">// Vnode might have been moved left</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
        oldEndVnode = oldCh[--oldEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
        patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue)
        oldStartVnode = oldCh[++oldStartIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
        patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue)
        oldEndVnode = oldCh[--oldEndIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123; <span class="hljs-comment">// Vnode moved right</span>
        patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue)
        api.insertBefore(parentElm, oldStartVnode.elm!, api.nextSibling(oldEndVnode.elm!))
        oldStartVnode = oldCh[++oldStartIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; <span class="hljs-comment">// Vnode moved left</span>
        patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue)
        api.insertBefore(parentElm, oldEndVnode.elm!, oldStartVnode.elm!)
        oldEndVnode = oldCh[--oldEndIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
          oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
        &#125;
        idxInOld = oldKeyToIdx[newStartVnode.key <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>]
        <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// New element</span>
          api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm!)
        &#125; <span class="hljs-keyword">else</span> &#123;
          elmToMove = oldCh[idxInOld]
          <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123;
            api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm!)
          &#125; <span class="hljs-keyword">else</span> &#123;
            patchVnode(elmToMove, newStartVnode, insertedVnodeQueue)
            oldCh[idxInOld] = <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>
            api.insertBefore(parentElm, elmToMove.elm!, oldStartVnode.elm!)
          &#125;
        &#125;
        newStartVnode = newCh[++newStartIdx]
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx || newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
        before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
        addVnodes(parentElm, before, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
      &#125; <span class="hljs-keyword">else</span> &#123;
        removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>diff分别在新旧的子节点的两头设置了指针，也就是四个指针。我们分别记录了这四个指针以及四个指针指向的Vnode</p>
<pre><code class="hljs language-ts copyable" lang="ts">   <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span><span class="hljs-comment">//指向旧节点的第一个Vnode</span>
   <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span><span class="hljs-comment">//指向新节点的第一个Vnode</span>
   <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span><span class="hljs-comment">//指向旧节点的最后一个Vnode</span>
   <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]<span class="hljs-comment">//旧节点的第一个Vnode</span>
   <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]<span class="hljs-comment">//旧节点的最后一个Vnode</span>
   <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span><span class="hljs-comment">//指向新节点的最后一个Vnode</span>
   <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]<span class="hljs-comment">//新节点的第一个Vnode</span>
   <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]<span class="hljs-comment">//新节点的最后一个Vnode</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在遍历过程中这四个指针都会向中间靠拢。
当oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx时结束循环</p>
</blockquote>
<p>接下来要介绍着四个指针的具体移动规则</p>
<h4 data-id="heading-12">旧头(oldStartVnode)  ----对比 ---新头(newStartVnode)</h4>
<blockquote>
<p>这里简单说明一下，我们使用sameVnode()判断两个Vnode是否相同</p>
</blockquote>
<ol>
<li>当新节点和老节点的第一个Vnode相同,即sameVnode(oldStartVnode, newStartVnode)，那么将该Vnode节点进行patchVnode。然后将oldStartIdx和newStartIdx两个指针+1，再将oldStartVnode和newStartVnode更新
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
    patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue)
    oldStartVnode = oldCh[++oldStartIdx]
    newStartVnode = newCh[++newStartIdx]
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
过程如下图（自己画自己截的图，将就看叭QAQ）第一列是新节点newCh，第二列是老节点oldCh<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcc38daee58c43cc8c065e34c9c3f44d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef34fcadbca748a8a2c1074df86811b9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></li>
</ol>
<h4 data-id="heading-13">旧尾(oldStartVnode)  ---对比 --- 新尾(newStartVnode)</h4>
<ol start="2">
<li>当新节点和老节点的最后一个Vnode相同，即sameVnode(oldEndVnode, newEndVnode)，那么将该Vnode节点进行patchVnode。然后将oldEndIdx和newEndIdx两个指针-1，再将oldEndVnode和newEndVnode更新</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
       patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue)
       oldEndVnode = oldCh[--oldEndIdx]
       newEndVnode = newCh[--newEndIdx]
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ffa485466b046ba87d917d1bf003600~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a7779b48ea848f29ea3a3d5c81d1f9c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">旧头(oldStartVnode)  ---对比 ---- 新尾(newStartVnode)</h4>
<ol start="3">
<li>当新节点的最后一个Vnode和老节点的第一个Vnode相同，即即sameVnode(oldStartVnode, newEndVnode)，那么将该Vnode节点进行patchVnode。然后将newEndIdx指针-1和oldStartIdx指针+1，然后把oldStartVnode移到oldEndVnode后面。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
       patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue)
       api.insertBefore(parentElm, oldStartVnode.elm!, api.nextSibling(oldEndVnode.elm!))
       oldStartVnode = oldCh[++oldStartIdx]
       newEndVnode = newCh[--newEndIdx]
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a063de5ff4784f8f94400039165c1cac~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>什么意思呢？就是当上面的新节点的D与旧节点的D通过sameVnode(oldStartVnode, newEndVnode)匹配上以后。为了将左边的旧节点变成右边的新节点，那么我们就将旧节点中的D移动到oldEndIdx指向的oldEndVnode的后面，也就是图中的B(注意是oldEndVnode的后面)。然后再将oldStartIdx指针+1和newEndIdx指针-1
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eee810833ba6472f9d25d2bed0fdb525~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>在这里还要介绍一下insertBefore() 。在MDN中是这样介绍的：<strong>Node.insertBefore() 方法在参考节点之前插入一个拥有指定父节点的子节点</strong>。简单的说就是把一个节点添加到另一个节点的前面。而nextSibling()是一个节点的下一个节点。所以我们通过insertBefore() 配合nextSibling()，来把上面的D添加到B的下一个节点的前面。这样我们就把D加在B的后面了也就是这一行代码</p>
<pre><code class="hljs language-ts copyable" lang="ts">api.insertBefore(parentElm, oldStartVnode.elm!, api.nextSibling(oldEndVnode.elm!))
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<blockquote>
<p>为什么不能用appendChild，是因为我们现在需要把节点添加到oldEndVnode的后面，而不是oldCh的后面。</p>
</blockquote>
<h4 data-id="heading-15">旧尾(oldStartVnode)  ----对比 --- 新头(newStartVnode)</h4>
<ol start="4">
<li>当老节点的最后一个Vnode和老新节点的第一个Vnode相同，即sameVnode(oldEndVnode,newStartVnode)，那么将该Vnode节点进行patchVnode。然后将oldEndIdx指针-1和newStartIdx指针+1，然后把oldStartVnode移到oldEndVnode后面。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123;
    patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue)
    api.insertBefore(parentElm, oldEndVnode.elm!, oldStartVnode.elm!)
    oldEndVnode = oldCh[--oldEndIdx]
    newStartVnode = newCh[++newStartIdx]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae4c904e30414978aab6ae53a94c4ed0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>当oldEndVnode与newStartVnode匹配上之后呢，为了将左边的旧节点变成右边的新节点，那么我们就需要把D放到oldStartVnode也就是B的前面。然后再将oldEndIdx指针-1和newStartIdx指针+1。
将D放到B前面的方法也就是直接用刚刚介绍的insertBefore()方法
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c95c7eaa3642435e971cd50aaa8377c6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>那么到这里，我以及将diff中的四种节点对比的方式讲清楚了（反正我觉得自己是讲清楚了，尽力了。自己在学习这部分源码的时候也是用PPT画了这个图，要是看着蒙圈就自己画画）。现在让我们再回来看这一段代码~</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm: Node,
    oldCh: VNode[],
    newCh: VNode[],
    insertedVnodeQueue: VNodeQueue</span>) </span>&#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span><span class="hljs-comment">//旧节点的起点指针</span>
    <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span><span class="hljs-comment">//新节点的起点指针</span>
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span><span class="hljs-comment">//旧节点最后一位指针</span>
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]<span class="hljs-comment">//旧节点的起点指针指向的Vnode</span>
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]<span class="hljs-comment">//旧节点的最后一位指针指向的Vnode</span>
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span><span class="hljs-comment">//新节点最后一位指针</span>
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]<span class="hljs-comment">//新节点的起点指针指向的Vnode</span>
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]<span class="hljs-comment">//新节点的最后一位指针指向的Vnode</span>
    <span class="hljs-keyword">let</span> oldKeyToIdx: KeyToIndexMap | <span class="hljs-literal">undefined</span>
    <span class="hljs-keyword">let</span> idxInOld: <span class="hljs-built_in">number</span>
    <span class="hljs-keyword">let</span> elmToMove: VNode
    <span class="hljs-keyword">let</span> before: <span class="hljs-built_in">any</span>

    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
        oldStartVnode = oldCh[++oldStartIdx] <span class="hljs-comment">// Vnode might have been moved left</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
        oldEndVnode = oldCh[--oldEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
      <span class="hljs-comment">//旧头(oldStartVnode)  ----------对比 ---------- 新头(newStartVnode)</span>
        patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue)
        oldStartVnode = oldCh[++oldStartIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
      <span class="hljs-comment">//旧尾(oldStartVnode)  ----------对比 ---------- 新尾(newStartVnode)</span>
        patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue)
        oldEndVnode = oldCh[--oldEndIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123; 
      <span class="hljs-comment">//旧头(oldStartVnode)  ----------对比 ---------- 新尾(newStartVnode)</span>
        patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue)
        api.insertBefore(parentElm, oldStartVnode.elm!, api.nextSibling(oldEndVnode.elm!))
        oldStartVnode = oldCh[++oldStartIdx]
        newEndVnode = newCh[--newEndIdx]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123; 
      <span class="hljs-comment">//旧尾(oldStartVnode)  ----------对比 ---------- 新头(newStartVnode)</span>
        patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue)
        api.insertBefore(parentElm, oldEndVnode.elm!, oldStartVnode.elm!)
        oldEndVnode = oldCh[--oldEndIdx]
        newStartVnode = newCh[++newStartIdx]
      &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">前面四种都找不到</h4>
<p>当新建节点的头尾四种对比都匹配不上时候,说明newStartVnode在oldCh中不在头尾或者并不存在。所以我们就用createKeyToOldIdx()方法制作了一个oldCh的映射的表。表中的值为每一个节点的key对应下标的值</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-comment">//创建oldCh的映射oldKeyToIdx</span>
        oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
      &#125;
      idxInOld = oldKeyToIdx[newStartVnode.key <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>]
      <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123; <span class="hljs-comment">// New element</span>
        <span class="hljs-comment">//如果idxInOld是undefined，就创建一个newStartVnode放在oldStartVnode.elm前面</span>
        api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm!)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//如果idxInOld不是undefined，那么就找出oldCh中含有idxInOld这一项记录为elmToMove</span>
        elmToMove = oldCh[idxInOld]
        <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123;
          <span class="hljs-comment">//如果elmToMove和newStartVnode的标签(sel)不一样，那么我们还是要再创建一个newStartVnode放在oldStartVnode.elm前面</span>
          api.insertBefore(parentElm, createElm(newStartVnode, insertedVnodeQueue), oldStartVnode.elm!)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">//如果都一样就做一次patchVnode，效果在前文已经描述过，都差不多</span>
          patchVnode(elmToMove, newStartVnode, insertedVnodeQueue)
          oldCh[idxInOld] = <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>
          <span class="hljs-comment">//终于在oldCh中找到newStartVnode，然后更新到oldStartVnode的前面</span>
          api.insertBefore(parentElm, elmToMove.elm!, oldStartVnode.elm!)
        &#125;
      &#125;
      newStartVnode = newCh[++newStartIdx]
    &#125;
&#125;
<span class="hljs-comment">//创建oldKeyToIdx</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span>(<span class="hljs-params">children: VNode[], beginIdx: <span class="hljs-built_in">number</span>, endIdx: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">KeyToIndexMap</span> </span>&#123;
  <span class="hljs-keyword">const</span> map: KeyToIndexMap = &#123;&#125;
  <span class="hljs-comment">//以beginIdx为起点，endIdx为终点遍历每一项</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = beginIdx; i <= endIdx; ++i) &#123;
    <span class="hljs-keyword">const</span> key = children[i]?.key
    <span class="hljs-keyword">if</span> (key !== <span class="hljs-literal">undefined</span>) &#123;
      map[key] = i
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> map
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/061c4e5d2c47497e97d807fa4436f127~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fda0c80fb73646928db6e320ea0626f7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在前面四次if判断，跳过Vnode为null的节点(就这节点没有，看下一个节点)。进入四种sameVnode的判断以及一种例外情况。通过源码我们可以看到五种判断的顺序如下</p>
<ol>
<li>旧头(oldStartVnode)  ----------对比 ---------- 新头(newStartVnode)</li>
<li>旧尾(oldStartVnode)  ----------对比 ---------- 新尾(newStartVnode)</li>
<li>旧头(oldStartVnode)  ----------对比 ---------- 新尾(newStartVnode)</li>
<li>旧尾(oldStartVnode)  ----------对比 ---------- 新头(newStartVnode)</li>
<li>前面四种都找不到</li>
</ol>
<blockquote>
<p>至于为什么是这个顺序，可能是以各种情况出现的概率为考虑点吧~~</p>
</blockquote>
<h4 data-id="heading-17">处理剩下节点</h4>
<p>按照这个顺序循环完之后，我们会有三种情况</p>
<ol>
<li>oldStartIdx > oldEndIdx。这种情况下就是老的Vnode节点遍历完了，但是新的Vnode节点还没有遍历完。所以这个时候新的Vnod比老的VNode节点多，所以我们需要将剩下的Vnode节点插入到真实的DOM节点中去。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
  before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm
  addVnodes(parentElm, before, newCh, newStartIdx, newEndIdx, insertedVnodeQueue)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>遍历before相当于是一个标杆，标记了节点需要插入的地方
addNodes方法就是遍历newCh中多出来的部分，插入到before这个标杆前</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addVnodes</span>(<span class="hljs-params">
    parentElm: Node,
    before: Node | <span class="hljs-literal">null</span>,
    vnodes: VNode[],
    startIdx: <span class="hljs-built_in">number</span>,
    endIdx: <span class="hljs-built_in">number</span>,
    insertedVnodeQueue: VNodeQueue
  </span>) </span>&#123;
  <span class="hljs-comment">//遍历newCh中多出来的部分</span>
    <span class="hljs-keyword">for</span> (; startIdx <= endIdx; ++startIdx) &#123;
      <span class="hljs-keyword">const</span> ch = vnodes[startIdx]
      <span class="hljs-comment">//只要节点不是null</span>
      <span class="hljs-keyword">if</span> (ch != <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-comment">//插入到before这个标杆前</span>
        api.insertBefore(parentElm, createElm(ch, insertedVnodeQueue), before)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>放两张图把
before不为null：(ps:看了一下 github万星的vue源码讲解，那大佬把这个图画错了哈哈哈哈哈哈哈哈哈)但是人家画的好，这个看不懂就看他的叭<a href="https://github.com/answershuto/learnVue/blob/master/docs/VirtualDOM%E4%B8%8Ediff%28Vue%E5%AE%9E%E7%8E%B0%29.MarkDown" target="_blank" rel="nofollow noopener noreferrer">大佬链接</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eb1f1e75c9d4b3186ad4c5918a57764~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
before为null，当before为null时，在addVnode方法中的insertBefore会将后面的选中的节点自动排到队尾去
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84e27d47f9df4b2b83c6b1627d786143~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>oldStartIdx <= oldEndIdx。这种情况下就是新的Vnode节点遍历完了，但是老的Vnode节点还没有遍历完。所以这个时候新的Vnod比老的VNode节点少，所以我们需要将老节点中多出来的Vnode节点删除。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts">removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfcc8194109747e294b20426bdb2b55b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>newCh，oldCh刚好都遍历完，就那没事了，下班。</li>
</ol>
<h2 data-id="heading-18">总结</h2>
<p>到这里爷可算是给这玩意整完了,讲讲感受。</p>
<ol>
<li>(我的绕口令)snabbdom的作者真厉害，能够构思出这中通过四个指针，来卡出新旧节点不同的地方，不知道为啥，我脑子总想着游标卡尺。指针就像两个外测量爪，外测量爪收缩的时候就像两个指针收缩，收缩到跳出while循环。内测量爪（外测量爪收缩到最小，内测量爪是会交叉的）或者外测量爪都卡着有意义的数据，就像4个节点一样。还有patchVnode和updateChildren的互相调用，除了解决了两个函数的本职工作，还通过互相调用解决了数组嵌套问题。与其相似的，createElm函数也通过递归去解决了这种数组嵌套的问题。</li>
<li>(我的废话)写博客确实很有助于我知识的沉淀。但是2W多字了，一个个画这些图，难顶……虽然vue源码中的diff和这区别不太大，函数名都差不多，但是vue3的diff好像更新了......但是收获还是很多，希望这些思想能像进击的巨人中的巨人死后随机传给下一个艾尔迪亚人一样传给我</li>
<li>1点了，下班。有人看到问题就说一下，没人看就算了。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a4bbab5f247456da704b3aa2bcf3fd5~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            