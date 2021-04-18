
---
title: 'snabbdom源码解析：利用分治思想理解diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28d40712e5464615b0202987152b54d3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 19:26:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28d40712e5464615b0202987152b54d3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文同步在个人博客<a href="https://www.shymean.com/article/snabbdom%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90" target="_blank" rel="nofollow noopener noreferrer">shymean.com</a>上，欢迎关注</p>
</blockquote>
<p>最新在梳理一些前端框架的核心实现，关于diff算法这一块，发现目前大部分文章都是将源码翻译一遍，而关于诸如“为啥要定义多个游标”、”首尾对比”等细节，并没有给出比较好的解释。因此打算整理<code>snabbdom</code>源码，同时回答前面提到的一些问题。</p>

<p>如果只关心diff算法的核心实现，可以直接跳转到 <code>patchVnode diff新旧节点</code>这一章节</p>
<h2 data-id="heading-0">使用流程</h2>
<h3 data-id="heading-1">parcel搭建开发环境</h3>
<p>由于仓库并没有提供类似于<code>dev</code>之类的开发环境，可以使用Pracel快速搭建一个</p>
<p>首先克隆仓库，执行<code>npm install && npm run build</code>进行打包</p>
<p>然后在项目<code>examples</code>目录下创建一个demo目录，新建<code>index.js</code>和<code>index.html</code></p>
<pre><code class="hljs language-html copyable" lang="html">// index.html
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"change"</span>></span>change<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; init, classModule, propsModule, styleModule, eventListenersModule, h &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../build/index"</span>;

<span class="hljs-keyword">const</span> patch = init([
  classModule, <span class="hljs-comment">// makes it easy to toggle classes</span>
  propsModule, <span class="hljs-comment">// for setting properties on DOM elements</span>
  styleModule, <span class="hljs-comment">// handles styling on elements with support for animations</span>
  eventListenersModule <span class="hljs-comment">// attaches event listeners</span>
]);

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);

<span class="hljs-keyword">const</span> renderItem = <span class="hljs-function">(<span class="hljs-params">item</span>)=></span>&#123;
  <span class="hljs-keyword">return</span> h(<span class="hljs-string">"div"</span>, &#123;<span class="hljs-attr">key</span>:item&#125;, item);
&#125;
<span class="hljs-keyword">const</span> oldList = [<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>].map(renderItem);
<span class="hljs-keyword">const</span> newList = [<span class="hljs-string">"B"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"G"</span>, <span class="hljs-string">"D"</span>].map(renderItem);
<span class="hljs-keyword">const</span> vnode = h(<span class="hljs-string">"div"</span>, &#123;&#125;, oldList);
patch(container, vnode);

<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"change"</span>).onclick = <span class="hljs-function">()=></span>&#123;
  <span class="hljs-keyword">const</span> newVnode = h(<span class="hljs-string">"div"</span>, &#123;&#125;, newList);
  patch(vnode, newVnode);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<code>examples/demo</code>目录下启动<code>parcel index.html</code>即可。</p>
<h3 data-id="heading-2">相关概念</h3>
<p>snabbdom只提供了几个基础接口，使用起来大概是下面的流程，</p>
<ul>
<li>使用<code>init</code>和内置模块初始<code>patch</code>方法</li>
<li>使用<code>h</code>方法创建vnode</li>
<li>初始化<code>patch(container, vnode)</code>，container为应用根节点</li>
<li>更新<code>path(vnode, newVnode)</code></li>
</ul>
<p>vnode就是一个JS对象，用来描述真实的DOM，包含一些主要的信息</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> VNode &#123;
  <span class="hljs-attr">sel</span>: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 用来区分不同类型的节点</span>
  data: VNodeData | <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 配置数据，可以携带一些钩子或其他信息</span>
  children: <span class="hljs-built_in">Array</span><VNode | <span class="hljs-built_in">string</span>> | <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 子节点</span>
  elm: Node | <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 对应的DOM实例</span>
  text: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 文本</span>
  key: Key | <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// key，在兄弟节点中的唯一标识</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>h</code>方法的作用就是根据<code>sel</code>、<code>data</code>和<code>children</code>返回一个vnode</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">
  sel: <span class="hljs-built_in">string</span>,
  data: VNodeData | <span class="hljs-literal">null</span>,
  children: VNodeChildren
</span>): <span class="hljs-title">VNode</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>patch方法通过init方法构建，是整个框架的核心，也是本文关注的重点</p>
<h2 data-id="heading-3">patch 入口收敛</h2>
<p>先说流程</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28d40712e5464615b0202987152b54d3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>首先判断<code>oldVnode</code>是否是vnode，
<ul>
<li>如果不是，则说明是初始化，传入的一个container DOM节点，使用该dom节点创建一个empty vnode，作为<code>oldVnode</code></li>
</ul>
</li>
<li>通过<code>sameVnode</code>新旧vnode是否相同
<ul>
<li>如果不是，则通过<code>createElm(newVnode)</code>前序遍历虚拟dom树构建真实DOM树，然后将传入的container DOM替换成新的DOM</li>
<li>如果是，则说明newVnode可以复用oldVnode的DOM实例，<code>vnode.elm = oldVnode.elm</code>，然后走<code>patchVnode</code>流程</li>
</ul>
</li>
</ul>
<p>再看代码，由于insert的钩子需要等到节点被插入到dom中才会被调用，因此使用了一个<code>insertedVnodeQueue</code>列表，在遍历树的时候收集所有被插入的vnode</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;
    <span class="hljs-keyword">let</span> i: <span class="hljs-built_in">number</span>, <span class="hljs-attr">elm</span>: Node, <span class="hljs-attr">parent</span>: Node;
    <span class="hljs-keyword">const</span> insertedVnodeQueue: VNodeQueue = [];
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.pre.length; ++i) cbs.pre[i]();

    <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
      oldVnode = emptyNodeAt(oldVnode);
    &#125;

    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
      patchVnode(oldVnode, vnode, insertedVnodeQueue);
    &#125; <span class="hljs-keyword">else</span> &#123;
      elm = oldVnode.elm!;
      parent = api.parentNode(elm) <span class="hljs-keyword">as</span> Node;

      <span class="hljs-comment">// 根据vnode初始化DOM树</span>
      createElm(vnode, insertedVnodeQueue);

      <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">null</span>) &#123;
        api.insertBefore(parent, vnode.elm!, api.nextSibling(elm));
        <span class="hljs-comment">// 里面会完成对oldVnode dom实例的移除</span>
        removeVnodes(parent, [oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      &#125;
    &#125;

    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < insertedVnodeQueue.length; ++i) &#123;
      insertedVnodeQueue[i].data!.hook!.insert!(insertedVnodeQueue[i]);
    &#125;
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.post.length; ++i) cbs.post[i]();
    <span class="hljs-keyword">return</span> vnode;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以从两条路<code>createElm</code>和<code>patchVnode</code>分别出发，看看初始化和更新时的差异</p>
<blockquote>
<p>snabbdom使用了与C语言类似的编程习惯，会在函数头部声明变量，在后续的代码中只进行赋值</p>
</blockquote>
<h2 data-id="heading-4">createElm 递归创建DOM树</h2>
<p>主要功能是根据vnode的sel创建DOM节点，如果有子节点，则进行前序遍历，递归调用<code>createElm</code>获取子节点对应的DOM节点，然后将其插入到父DOM节点</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5ba0b0a98cf4bdaab253808bbeea79c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看出，这里是在递归的同时就执行创建DOM的操作，为了方便阅读，下面的源码进行了删减</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">vnode: VNode, insertedVnodeQueue: VNodeQueue</span>): <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-keyword">let</span> i: any;
    <span class="hljs-keyword">let</span> data = vnode.data;
    <span class="hljs-keyword">const</span> children = vnode.children;
    <span class="hljs-keyword">const</span> sel = vnode.sel;
    <span class="hljs-keyword">if</span> (sel === <span class="hljs-string">"!"</span>) &#123;
      <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
        vnode.text = <span class="hljs-string">""</span>;
      &#125;
      vnode.elm = api.createComment(vnode.text!);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sel !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-comment">// 根据sel解析tag</span>
      <span class="hljs-keyword">const</span> elm = (vnode.elm =
        isDef(data) && isDef((i = data.ns))
          ? api.createElementNS(i, tag, data)
          : api.createElement(tag, data));
<span class="hljs-comment">// 递归创建子节点</span>
      <span class="hljs-keyword">if</span> (is.array(children)) &#123;
        <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
          <span class="hljs-keyword">const</span> ch = children[i];
          <span class="hljs-keyword">if</span> (ch != <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">// 同时将子节点对应的DOM添加到父DOM</span>
            api.appendChild(elm, createElm(ch <span class="hljs-keyword">as</span> VNode, insertedVnodeQueue));
          &#125;
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(vnode.text)) &#123;
        api.appendChild(elm, api.createTextNode(vnode.text));
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode.elm = api.createTextNode(vnode.text!);
    &#125;
    <span class="hljs-keyword">return</span> vnode.elm;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，就根据一个vnode得到了它对应的完整DOM树。</p>
<h2 data-id="heading-5">patchVnode diff新旧节点</h2>
<p>前面提到，当新旧节点类型相同时，就会进入<code>patchVnode</code>流程，主要进行新旧节点对应子节点列表的判断</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">
  oldVnode: VNode,
  vnode: VNode,
  insertedVnodeQueue: VNodeQueue
</span>) </span>&#123;

  <span class="hljs-keyword">const</span> elm = (vnode.elm = oldVnode.elm)!;
  <span class="hljs-keyword">const</span> oldCh = oldVnode.children <span class="hljs-keyword">as</span> VNode[];
  <span class="hljs-keyword">const</span> ch = vnode.children <span class="hljs-keyword">as</span> VNode[];
  <span class="hljs-comment">// 节点在内存相同，则不进行比较</span>
  <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span>;

  <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123;
    <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
      <span class="hljs-comment">// 同时存在新旧子节点，如果子节点在内存相同，则不进行比较</span>
      <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
      <span class="hljs-comment">// 如果只存在新节点，则说明全部为新增节点，判断一下之前是否为文本节点</span>
      <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) api.setTextContent(elm, <span class="hljs-string">""</span>);
      <span class="hljs-comment">// 然后插入新节点</span>
      addVnodes(elm, <span class="hljs-literal">null</span>, ch, <span class="hljs-number">0</span>, ch.length - <span class="hljs-number">1</span>, insertedVnodeQueue);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
      <span class="hljs-comment">// 如果只存在旧节点，则需要全部移除</span>
      removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
      api.setTextContent(elm, <span class="hljs-string">""</span>);
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
    <span class="hljs-comment">// 新节点为文本节点时，移除旧节点，插入新的文本节点</span>
    <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
      removeVnodes(elm, oldCh, <span class="hljs-number">0</span>, oldCh.length - <span class="hljs-number">1</span>);
    &#125;
    api.setTextContent(elm, vnode.text!);
  &#125;
  hook?.postpatch?.(oldVnode, vnode);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文本节点、只有新节点或者只有旧节点的情况都比较容易理解，而新旧节点都存在的情况，在<code>updateChildren</code>里面包含了整个diff的核心。</p>
<p>在看源代码之前，需要先明白，比较新旧节点主要目的是什么？</p>
<p>整个diff算法的核心就是比较新旧节点，尽可能减少DOM操作带来的开销，为了达到这个目的，需要尽可能地复用已有的旧节点。换言之</p>
<ul>
<li>每个旧的子节点列表中都包含已经创建的DOM实例</li>
<li>每个新的子节点等着从已经创建的DOM实例中<strong>找到</strong>属于自己的那一个
<ul>
<li>如果能找到的话，直接复用</li>
<li>不能找到的话，才重新创建新的DOM实例</li>
</ul>
</li>
<li>最后如果旧的子节点中还有未被使用的DOM实例，需要从页面移除</li>
</ul>
<p>可见，关键思想就在于为新节点查找合适的旧节点，按照<code>patchVnode</code>的做法，两个vnode节点的类型相同，就可以复用他们的DOM节点。</p>
<h3 data-id="heading-6">BF版本</h3>
<p>按照最简单的思路，遍历新节点列表，获取每个新节点的type，然后从依次从旧节点列表中找到一个符合条件的就行了呗</p>
<p>把问题简化，假设需要根据下面的旧列表重新构建新列表</p>
<ul>
<li>旧的列表为<code>['A','B','C','D','E']</code></li>
<li>新的列表为<code>['B','A','C','F','G','D']</code></li>
</ul>
<p>从上帝视角来看，先确定节点，A、B、C、D节点都存在，可以复用旧DOM；新F、新G节点需要创建；旧E节点需要移除</p>
<p>在只考虑实现上述需求的情况下，写一个暴力版本</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> oldChildren = [<span class="hljs-string">'A'</span>,<span class="hljs-string">'B'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'D'</span>,<span class="hljs-string">'E'</span>]
<span class="hljs-keyword">var</span> newChildren = [<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'D'</span>]

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">var</span> map = arr.reduce(<span class="hljs-function">(<span class="hljs-params">acc, oldChild,index</span>)=></span>&#123;
        acc[oldChild] = index
        <span class="hljs-keyword">return</span> acc
    &#125;,&#123;&#125;)
    <span class="hljs-keyword">return</span> map
&#125;

<span class="hljs-keyword">var</span> parentElm = oldChildren.slice()
newChildren.forEach(<span class="hljs-function">(<span class="hljs-params">newChild, idx</span>)=></span>&#123;
    <span class="hljs-keyword">var</span> map = createKeyToOldIdx(parentElm)
    <span class="hljs-keyword">var</span> oldIdx = map[newChild]
    <span class="hljs-keyword">if</span>(oldIdx===<span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-comment">// 添加新节点</span>
        parentElm.splice(idx, <span class="hljs-number">0</span>, newChild)
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(oldIdx !== idx) &#123;
      <span class="hljs-comment">// 移动位置</span>
        parentElm.splice(oldIdx,<span class="hljs-number">1</span>) 
        parentElm.splice(idx, <span class="hljs-number">0</span>, newChild)
    &#125;
    <span class="hljs-built_in">console</span>.log(idx, parentElm) 
&#125;)

<span class="hljs-comment">// 移除不存在的节点</span>
parentElm =  parentElm.filter(<span class="hljs-function"><span class="hljs-params">child</span>=></span>&#123;
    <span class="hljs-keyword">return</span> newChildren.includes(child)
&#125;)
<span class="hljs-built_in">console</span>.log(parentElm)

<span class="hljs-comment">// 旧列表 ['A','B','C','D','E']</span>
<span class="hljs-comment">// 新列表 ['B','A','C','F','G','D']</span>

<span class="hljs-comment">// 初始parentElm与旧列表保持一致 ['A','B','C','D','E']</span>

<span class="hljs-comment">// 第1次循环 移动B 新的parentElm: B A C D E </span>
<span class="hljs-comment">// 第2次循环 不进行操作 parentElm: B A C D E</span>
<span class="hljs-comment">// 第3次循环 不进行操作 parentElm: B A C D E</span>
<span class="hljs-comment">// 第4次循环 插入F parentElm: B A C F D E </span>
<span class="hljs-comment">// 第5次循环 插入G parentElm: B A C F G D E</span>
<span class="hljs-comment">// 第6次循环 不进行操作 parentElm: B A C F G D E</span>
<span class="hljs-comment">// 第7次循环 移除旧节点 parentElm: B A C F G D </span>

<span class="hljs-comment">// 最终parentElm与新列表保持一致</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种实现方式下，</p>
<ul>
<li>
<p>遍历新节点列表，查找是否存在对应的旧节点，</p>
<ul>
<li>如果存在，则调整其顺序，满足其在新节点列表中的位置；</li>
<li>如果不存在，则创建，并插入到新节点列表的位置</li>
</ul>
</li>
<li>
<p>然后移除不在新节点列表中的节点</p>
</li>
</ul>
<p>由于<code>parentElm</code>会保存最新的节点顺序，因此在每轮遍历中都要通过<code>createKeyToOldIdx</code>查到新节点在旧列表中的位置，导致复杂度为O(mn)。</p>
<h3 data-id="heading-7">拆分子问题</h3>
<p>因此需要对上面的算法进行改良，尽可能减少操作步骤，肉眼看起来，一种较优的做法是</p>
<ul>
<li>将旧B节点移动到A节点前面，前三个节点顺序就跟新节点一致了</li>
<li>创建新F的DOM，插入到旧D前面</li>
<li>创建新G的DOM，插入到旧D前面</li>
<li>删除旧E的DOM</li>
</ul>
<p>只需要上面4步，就可以从旧的DOM树更新成新的DOM树。了解了这个背景之后，再继续阅读源码<code>updateChildren</code>。将一个列表修改成另外一个列表所需要的最少操作，实际上可以参考：<a href="https://zh.wikipedia.org/wiki/%E7%B7%A8%E8%BC%AF%E8%B7%9D%E9%9B%A2" target="_blank" rel="nofollow noopener noreferrer">编辑距离</a>，[letcode]上面也有相关的题解(<a href="https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/)%EF%BC%8C%E5%85%B6%E6%A0%B8%E5%BF%83%E6%80%9D%E8%B7%AF%E6%98%AF%E4%BD%BF%E7%94%A8%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%8C%E4%BB%8E%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E9%97%AE%E9%A2%98%E8%A7%A6%E5%8F%91%E9%80%90%E6%AD%A5%E8%8E%B7%E5%8F%96%E6%9C%80%E4%BC%98%E8%A7%A3%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">leetcode-cn.com/problems/ed…</a></p>
<p>参考这个思路，我们先来看看最简单的情况</p>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-string">"A"</span>]
[<span class="hljs-string">"A"</span>]
两个列表完全相同，不需要做任何操作

[<span class="hljs-string">"A"</span>]
[]
删除A即可

[]
[<span class="hljs-string">"A"</span>]
添加B即可

[<span class="hljs-string">"A"</span>]
[<span class="hljs-string">"B"</span>]
删除A 添加B
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再看看下面几种特殊情况</p>
<p><strong>首节点或尾节点不变</strong>，这种情况下，都可以忽略相同的节点，将问题简化为<strong>连续子数组</strong>的情况，解决这种问题需要的步骤 = 解决子问题需要的步骤</p>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-string">"A"</span>]
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]
有两种拆分方式
第一种 [<span class="hljs-string">"A"</span>]->[<span class="hljs-string">"A"</span>]子问题<span class="hljs-number">1</span>和[]->[<span class="hljs-string">"B"</span>]的子问题<span class="hljs-number">2</span>，需要操作<span class="hljs-number">1</span>次
第二种 []->[<span class="hljs-string">"A"</span>]子问题<span class="hljs-number">1</span>和[<span class="hljs-string">"A"</span>]->[<span class="hljs-string">"B"</span>]的子问题<span class="hljs-number">2</span>，需要操作<span class="hljs-number">3</span>次

可以看见第一种拆分方式所需要的步骤更少，则说明他可以作为最优解法
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考这种思路，拆分一下下面的问题，对于首或尾节点相同的情况</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 新增</span>
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>];
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>];
子问题 [<span class="hljs-string">"B"</span>] -> [<span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>]
继续拆一下子问题 [] -> [<span class="hljs-string">"C"</span>]

<span class="hljs-comment">// 删除</span>
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]
子问题 [<span class="hljs-string">"C"</span>] -> []

<span class="hljs-comment">// 修改</span>
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"A"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"B"</span>]
子问题 [<span class="hljs-string">"C"</span>] -> [<span class="hljs-string">"D"</span>]

[<span class="hljs-string">"A"</span>,<span class="hljs-string">"B"</span>]
[<span class="hljs-string">"A"</span>,<span class="hljs-string">"C"</span>]
子问题 [<span class="hljs-string">"B"</span>] -> [<span class="hljs-string">"C"</span>]

[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>]
子问题 [<span class="hljs-string">"A"</span>] -> [<span class="hljs-string">"C"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>旧首节点等于新尾节点，或者旧尾节点等于新首节点</strong>，这种情况下，只需要将新旧数组的首尾节点调整一下，就可以处理成<strong>首节点或尾节点不变</strong>的情况，解决这种问题需要的步骤 = 移动节点（1次） + 解决子问题需要的步骤</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>];
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"A"</span>];
先把旧节点转换成 [<span class="hljs-string">"B"</span>,<span class="hljs-string">"A"</span>]，然后再处理子问题 [<span class="hljs-string">""</span>] -> [<span class="hljs-string">"C"</span>]

[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"A"</span>];
先把旧节点转换成 [<span class="hljs-string">"B"</span>,<span class="hljs-string">"A"</span>]，然后再处理子问题 [<span class="hljs-string">"B"</span>] -> [<span class="hljs-string">"C"</span>,<span class="hljs-string">"D"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>不满足上面情况的子问题</strong>，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[<span class="hljs-string">"A"</span>,<span class="hljs-string">"B"</span>]
[<span class="hljs-string">"C"</span>,<span class="hljs-string">"A"</span>,<span class="hljs-string">"B"</span>,<span class="hljs-string">"D"</span>]
先添加C，变成[<span class="hljs-string">"C"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]，然后处理子问题[]->[<span class="hljs-string">"D"</span>]

[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"D"</span>]
先添加C，变成[<span class="hljs-string">"C"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]，然后处理子问题[<span class="hljs-string">"B"</span>]->[<span class="hljs-string">"D"</span>]

[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>]
先添加C，变成[<span class="hljs-string">"C"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]，然后处理子问题[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]->[<span class="hljs-string">"D"</span>]
对于子问题，先添加D，变成[<span class="hljs-string">"D"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]，然后处理子问题[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>]->[]

[<span class="hljs-string">"A"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"B"</span>]
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>]
原本先添加C，在添加C之前需要先查找旧节点中是否有，如果有就执行移动操作，变成[<span class="hljs-string">"C"</span>,<span class="hljs-string">"A"</span>,<span class="hljs-string">"B"</span>]->[<span class="hljs-string">"C"</span>,<span class="hljs-string">"D"</span>]
处理子问题[<span class="hljs-string">"A"</span>,<span class="hljs-string">"B"</span>]->[<span class="hljs-string">"D"</span>]，重复执行上面的过程
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照这种<strong>分治</strong>的思路，每一步我们都能将问题拆成更小的问题，那么我们可以很方便地计算出最少的操作步骤，回到上面的问题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">B存在旧节点，则直接移动，前三个节点就变成一样的了，使用一步移动操作
[<span class="hljs-string">'A'</span>,<span class="hljs-string">'B'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'D'</span>,<span class="hljs-string">'E'</span>]
[<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'D'</span>]
操作完的DOM节点[<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'D'</span>,<span class="hljs-string">'E'</span>]

子问题,首==尾，移动一下，使用一步移动操作
[<span class="hljs-string">'D'</span>,<span class="hljs-string">'E'</span>]
[<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'D'</span>]
操作完的DOM节点[<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'E'</span>,<span class="hljs-string">'D'</span>]

子问题，满足尾==尾，使用<span class="hljs-number">0</span>步
[<span class="hljs-string">'E'</span>,<span class="hljs-string">'D'</span>]
[<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'D'</span>]

子问题，完全不满足，则需要添加两步，移除一步
[<span class="hljs-string">'E'</span>]
[<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>]
操作完的DOM节点
添加F [<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'F'</span>,<span class="hljs-string">'E'</span>,<span class="hljs-string">'D'</span>]
添加G [<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'E'</span>,<span class="hljs-string">'D'</span>]
删除E [<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'D'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是比较接近我们上面提到的较优做法了？由于E节点后面会被移除，因此移动D这一步是多余的，除此之外，所需的操作与前面上帝视角观察到的基本一致。</p>
<p>这是很关键的一步，我们将DOM更新的问题拆分成了最小的子问题，而已经处理好的节点，他们的顺序不会再发生改变。</p>
<p>再来看一个比较复杂的例子，来源<a href="https://www.jianshu.com/p/f45463e7be20" target="_blank" rel="nofollow noopener noreferrer">Snabbdom 底层Diff算法详解</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">首==首 || 尾==尾 ，使用<span class="hljs-number">0</span>步
旧 [<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"G"</span>]
新 [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]
完整DOM节点[<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"G"</span>]

子问题,首==尾 || 尾==首，需要移动位置，使用<span class="hljs-number">2</span>次移动，转换成首==首 尾==尾
[<span class="hljs-string">"B"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"F"</span>]
[<span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>]
完整DOM节点[<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]

子问题，满足尾==尾，使用<span class="hljs-number">0</span>步
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>]
[<span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>, <span class="hljs-string">"E"</span>]
完整DOM节点[<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]

子问题，完全不符合，需要<span class="hljs-number">4</span>次新增和<span class="hljs-number">2</span>次移除，
[<span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>]
[<span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>]
完整DOM节点
添加E [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>] 
添加M [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]
添加O [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]
添加I [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]
移除C [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]
移除D [<span class="hljs-string">"A"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"M"</span>, <span class="hljs-string">"O"</span>, <span class="hljs-string">"I"</span>, <span class="hljs-string">"E"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"G"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>操作步骤都是类似的，接下来实现一个优化后的版本，由于没有实现<code>insertBefore</code>和<code>removeChild</code>等接口，在测试的时候需要保证每个元素唯一。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">var</span> a = [<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>];
<span class="hljs-keyword">var</span> b = [<span class="hljs-string">"B"</span>, <span class="hljs-string">"A"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"F"</span>, <span class="hljs-string">"G"</span>, <span class="hljs-string">"D"</span>];

<span class="hljs-keyword">var</span> oldStartIdx = <span class="hljs-number">0</span>
<span class="hljs-keyword">var</span> newStartIdx = <span class="hljs-number">0</span>
<span class="hljs-keyword">var</span> oldEndIdx = a.length - <span class="hljs-number">1</span>
<span class="hljs-keyword">var</span> newEndIdx= b.length - <span class="hljs-number">1</span>

<span class="hljs-keyword">var</span> oldStart = a[<span class="hljs-number">0</span>]
<span class="hljs-keyword">var</span> oldEnd = a[oldEndIdx]
<span class="hljs-keyword">var</span> newStart = b[<span class="hljs-number">0</span>]
<span class="hljs-keyword">var</span> newEnd = b[newEndIdx]

<span class="hljs-keyword">var</span> parentElm = a.slice()

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-keyword">var</span> map = a.reduce(<span class="hljs-function">(<span class="hljs-params">acc, oldChild, index</span>) =></span> &#123;
        acc[oldChild] = index;
        <span class="hljs-keyword">return</span> acc;
    &#125;, &#123;&#125;);
    <span class="hljs-keyword">return</span> map;
&#125;

<span class="hljs-keyword">var</span> oldKeyToIdx = createKeyToOldIdx(a)

<span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    <span class="hljs-keyword">if</span>(oldStart===<span class="hljs-literal">undefined</span>) &#123;
        oldStart = a[++oldStartIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(oldEnd === <span class="hljs-literal">undefined</span>)&#123;
        oldEnd = a[--oldEndIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(newStart === <span class="hljs-literal">undefined</span>)&#123;
        newStart = b[++newStartIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(newEnd === <span class="hljs-literal">undefined</span>)&#123;
        newEnd === b[--newEndIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(oldStart === newStart) &#123;
        oldStart = a[++oldStartIdx]
        newStart = b[++newStartIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(oldEnd === newEnd)&#123;
        oldEnd = a[--oldEndIdx]
        newEnd = b[--newEndIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(oldStart === newEnd)&#123;
      <span class="hljs-comment">// 移动到后面</span>
        parentElm.splice(oldStartIdx, <span class="hljs-number">1</span>)
        parentElm.splice(oldEndIdx, <span class="hljs-number">0</span>, oldStart)
        oldStart = a[++oldStartIdx]
        newEnd = b[--newEndIdx]
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(oldEnd === newStart)&#123;
      <span class="hljs-comment">// 移动到前面</span>
        parentElm.splice(oldEndIdx, <span class="hljs-number">1</span>)
        parentElm.splice(oldStartIdx, <span class="hljs-number">0</span>, oldEnd)
        oldEnd = a[--oldEndIdx]
        newStart = b[++newStartIdx]
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 首尾都不满足，则查找是否有旧节点，然后从newStart开始查找</span>
        <span class="hljs-keyword">var</span> idxInOld = oldKeyToIdx[newStart]
        <span class="hljs-keyword">if</span>(idxInOld===<span class="hljs-literal">undefined</span>)&#123;
            <span class="hljs-built_in">console</span>.log(oldStartIdx, newStart)
            <span class="hljs-comment">// 由于没有实现insertBefore，只能暂时获取对应的idx然后通过splice插入，</span>
            <span class="hljs-comment">// 否则可以直接使用在insertBefore(newStart, oldStart)直接插入节点</span>
            <span class="hljs-keyword">let</span> idx = parentElm.indexOf(oldStart)
            parentElm.splice(idx,<span class="hljs-number">0</span>,newStart)
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">var</span> elmToMove = a[idxInOld]
            a[idxInOld] = <span class="hljs-literal">undefined</span>
            parentElm.splice(idxInOld, <span class="hljs-number">1</span>)
            parentElm.splice(oldStartIdx, <span class="hljs-number">0</span>,elmToMove)
        &#125;
        newStart = b[++newStartIdx]
    &#125;
    <span class="hljs-built_in">console</span>.log(parentElm)
&#125;

<span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx || newStartIdx <= newEndIdx) &#123;
    <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
        <span class="hljs-comment">// 批量插入新节点</span>
        <span class="hljs-keyword">var</span> sub = b.slice(newStartIdx, newEndIdx+<span class="hljs-number">1</span>)
        <span class="hljs-keyword">var</span> before = b[newEndIdx+<span class="hljs-number">1</span>]
        <span class="hljs-comment">// 同上，这里直接insertBefore(node, before)可以快速插入节点</span>
        <span class="hljs-keyword">var</span> idx = parentElm.indexOf(before)
        parentElm = [...parentElm.slice(<span class="hljs-number">0</span>,idx),...sub,parentElm.slice(idx)]
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 批量删除无用的旧节点</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = oldStartIdx; i <= oldEndIdx;++i)&#123;
            <span class="hljs-keyword">var</span> child= a[i]
            <span class="hljs-comment">// 同上，这里使用node.parentNode.removeChild可以直接删除节点，而无需通过idx</span>
            <span class="hljs-keyword">var</span> idx = parentElm.indexOf(child)
            parentElm.splice(idx,<span class="hljs-number">1</span>)
        &#125;
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(parentElm)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个实现中有很多个判断</p>
<ul>
<li>使用新起始索引、新结束索引、新起始节点、新尾节点来结束新节点列表的子问题范围</li>
<li>使用旧起始索引、旧结束索引、旧起始节点、旧尾节点来结束旧节点列表的子问题范围</li>
<li>前四个判断是为了保证新旧节点存在，跳过<code>undefined</code>的节点</li>
<li>接下来的两个判断<code>oldStart === newStart</code>和<code>(oldEnd === newEnd</code>用来确定是否是旧首==新首或旧尾==新尾的情况，如果是，更新游标，直接缩小子问题范围</li>
<li>接下来的两个判断<code>oldStart === newEnd</code>和<code>oldEnd === newStart</code>用来确定是否是旧首==新尾或旧尾==新首的情况，如果是，则执行移动操作，同时更新游标，缩小子问题范围</li>
<li>最后的一个判断，用来处理常规子问题，首先检查新起始节点是否存在可以复用的旧节点
<ul>
<li>如果不存在，则创建节点插入</li>
<li>如果存在，则执行移动操作</li>
</ul>
</li>
</ul>
<p>这段代码看起来是不是很眼熟，没错，这就是<code>updateChildren</code>的简化版</p>
<h3 data-id="heading-8">updateChildren源码及存在的问题</h3>
<p>现在来看<code>updateChildren</code>的源码，就容易理解开头的这一堆变量了。主要就是为了在每一步操作之后，所以需要操作的DOM节点范围，范围小了，需要执行的DOM操作就少，也就达到了性能优化的目的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">
    parentElm: Node,
    oldCh: VNode[],
    newCh: VNode[],
    insertedVnodeQueue: VNodeQueue
  </span>) </span>&#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx];
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>;
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx];
    <span class="hljs-keyword">let</span> oldKeyToIdx: KeyToIndexMap | <span class="hljs-literal">undefined</span>;
    <span class="hljs-keyword">let</span> idxInOld: number;
    <span class="hljs-keyword">let</span> elmToMove: VNode;
    <span class="hljs-keyword">let</span> before: any;

    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      <span class="hljs-comment">// 第一类判断，保证新旧节点存在</span>
      <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
        oldStartVnode = oldCh[++oldStartIdx]; <span class="hljs-comment">// Vnode might have been moved left</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
        oldEndVnode = oldCh[--oldEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
        newStartVnode = newCh[++newStartIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
        newEndVnode = newCh[--newEndIdx];
       <span class="hljs-comment">// 第二类判断，起始或末尾节点是否相同</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
        patchVnode(oldStartVnode, newStartVnode, insertedVnodeQueue);
        oldStartVnode = oldCh[++oldStartIdx];
        newStartVnode = newCh[++newStartIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
        patchVnode(oldEndVnode, newEndVnode, insertedVnodeQueue);
        oldEndVnode = oldCh[--oldEndIdx];
        newEndVnode = newCh[--newEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
        <span class="hljs-comment">// 第三类判断，首尾节点是否相同，执行移动操作</span>
        <span class="hljs-comment">// Vnode moved right</span>
        patchVnode(oldStartVnode, newEndVnode, insertedVnodeQueue);
        api.insertBefore(
          parentElm,
          oldStartVnode.elm!,
          api.nextSibling(oldEndVnode.elm!)
        );
        oldStartVnode = oldCh[++oldStartIdx];
        newEndVnode = newCh[--newEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123;
        <span class="hljs-comment">// Vnode moved left</span>
        patchVnode(oldEndVnode, newStartVnode, insertedVnodeQueue);
        api.insertBefore(parentElm, oldEndVnode.elm!, oldStartVnode.elm!);
        oldEndVnode = oldCh[--oldEndIdx];
        newStartVnode = newCh[++newStartIdx];
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 第四类判断，根据key找到可以复用的DOM节点</span>
        <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
          oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx);
        &#125;
        idxInOld = oldKeyToIdx[newStartVnode.key <span class="hljs-keyword">as</span> string];
        <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123;
          <span class="hljs-comment">// 如果没有可复用的节点，就重新创建新节点</span>
          api.insertBefore(
            parentElm,
            createElm(newStartVnode, insertedVnodeQueue),
            oldStartVnode.elm!
          );
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 如果有可复用的节点，则执行移动操作</span>
          elmToMove = oldCh[idxInOld];
          <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123;
            api.insertBefore(
              parentElm,
              createElm(newStartVnode, insertedVnodeQueue),
              oldStartVnode.elm!
            );
          &#125; <span class="hljs-keyword">else</span> &#123;
            patchVnode(elmToMove, newStartVnode, insertedVnodeQueue);
            oldCh[idxInOld] = <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> any;
            api.insertBefore(parentElm, elmToMove.elm!, oldStartVnode.elm!);
          &#125;
        &#125;
        newStartVnode = newCh[++newStartIdx];
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx || newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
        <span class="hljs-comment">// 旧节点被消耗完毕，新节点还有剩余，则都执行插入操作</span>
        before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm;
        addVnodes(
          parentElm,
          before,
          newCh,
          newStartIdx,
          newEndIdx,
          insertedVnodeQueue
        );
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 反之，新节点被消耗完毕，旧节点还有剩余，都执行移除操作</span>
        removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx);
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照上面的分析，在移动节点这一步，其实并不是最优的，由于删除无用节点的操作都是在最后执行的，在上面</p>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-string">'A'</span>,<span class="hljs-string">'B'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'D'</span>,<span class="hljs-string">'E'</span>]
[<span class="hljs-string">'B'</span>,<span class="hljs-string">'A'</span>,<span class="hljs-string">'C'</span>,<span class="hljs-string">'F'</span>,<span class="hljs-string">'G'</span>,<span class="hljs-string">'D'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>的例子中，会先移动D到E后面，然后再把E删除，这一步无疑是无用的。由于被删除的节点并不影响整个diff，一种可行的方式是调整代码顺序，提前删除</p>
<ul>
<li>先遍历新旧节点，提前移除不会用到的节点，这里会多执行一轮循环，之后的问题可以简化为['A','B','C','D'] -> ['B','A','C','F','G','D']</li>
<li>再进行上述的diff操作</li>
<li>最后在<code>newStartIdx <= newEndIdx</code>时插入未被处理的vnode</li>
</ul>
<p>是否采用这种方案主要取决于<strong>多执行一轮循环用于删除无用节点</strong>得到的性能提升是否比<strong>减少一轮循环，使用可能带来的额外的移动操作</strong>得到的性能提升更大，但很显然，<code>Snabbdom</code>和<code>Vue</code>都没有采用这种<strong>提前删除无用节点</strong>的方案。</p>
<p>了解了内部的实现之后，我们再回答上面刻意避免的一个问题：vnode.key的作用是什么?</p>
<p>在<code>sameVnode</code>可以看见</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1: VNode, vnode2: VNode</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">const</span> isSameKey = vnode1.key === vnode2.key; <span class="hljs-comment">// 都为undefined或者字符串相等</span>
  <span class="hljs-keyword">const</span> isSameIs = vnode1.data?.is === vnode2.data?.is;
  <span class="hljs-keyword">const</span> isSameSel = vnode1.sel === vnode2.sel;

  <span class="hljs-keyword">return</span> isSameSel && isSameKey && isSameIs;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>key的一个作用是用来判断两个vnode是否相同，参与到上面diff过程的一些判断中，在都不定义key的情况下，两个相同sel的vnode会返回true，也就是常说的<strong>就地复用</strong>，只会更新DOM相关的信息，而不参与移动操作</p>
<p>在<code>createKeyToOldIdx</code>中可以查看定义了key的情况</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span>(<span class="hljs-params">
  children: VNode[],
  beginIdx: <span class="hljs-built_in">number</span>,
  endIdx: <span class="hljs-built_in">number</span>
</span>): <span class="hljs-title">KeyToIndexMap</span> </span>&#123;
  <span class="hljs-keyword">const</span> map: KeyToIndexMap = &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = beginIdx; i <= endIdx; ++i) &#123;
    <span class="hljs-keyword">const</span> key = children[i]?.key;
    <span class="hljs-comment">// 不处理undefined</span>
    <span class="hljs-keyword">if</span> (key !== <span class="hljs-literal">undefined</span>) &#123;
      map[key <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>] = i;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> map;
&#125;
<span class="hljs-comment">// 根据key返回旧节点的索引值</span>
idxInOld = oldKeyToIdx[newStartVnode.key <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>];
<span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123;
  <span class="hljs-comment">// ...创建新节点</span>
&#125;<span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// ... 移动操作</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果定义了key，则会在旧列表中找到对应的DOM节点，然后执行移动操作；换句话说，key用来在一个兄弟节点列表中进行唯一标记，这样在构建新节点的时候，会根据key去查找已经存在的节点，而不是就地复用，同时移除key不存在的节点。</p>
<p>举个例子</p>
<p>在不使用key的时候，将<code>[h('div', &#123;&#125;, '1'),h('div', &#123;&#125;, '2')]</code>修改为<code>[h('div', &#123;&#125;, '2'),h('div', &#123;&#125;, '1')]</code>，会将第一个DOM的文本节点修改为'2'，而不是移动两个DOM节点的顺序，这在DOM节点比较简单的时候貌似更加高效</p>
<p>在使用key的时候，<code>[h('div', &#123;key:'1'&#125;, '1'),h('div', &#123;key:'2'&#125;, '2')]</code>修改为<code>[h('div', &#123;key:'2'&#125;, '2'),h('div', &#123;key:'1'&#125;, '1')]</code>，会根据第一个新节点的key(这里是<code>'2'</code>)去旧节点列表中查找，找到对应的DOM节点（第2个DOM节点），然后执行位置移动操作，对于简单文本的改动，貌似是不划算的；但如果这两个节点的子节点是比较复杂的内容，交换顺序就比较划算了。</p>
<p>总结一下</p>
<ul>
<li>不使用key，尽可能就地复用已存在的同类型DOM</li>
<li>使用key，基于key的变化查找旧的节点，修改顺序进行移动操作，同时剔除key不存在的元素</li>
</ul>
<h2 data-id="heading-9">通过Module处理不同的DOM属性</h2>
<p>内置模块<code>Module</code>包含一些钩子方法，在vnode节点执行<code>create</code>、<code>update</code>、<code>remove</code>等操作时，会传入新旧的vnode然后执行，然后在新旧vnode的DOM实例上进行一些操作</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> Module = Partial<&#123;
  <span class="hljs-attr">pre</span>: PreHook;
  create: CreateHook;
  update: UpdateHook;
  destroy: DestroyHook;
  remove: RemoveHook;
  post: PostHook;
&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以<code>classModule</code>为例</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateClass</span>(<span class="hljs-params">oldVnode: VNode, vnode: VNode</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">let</span> cur: <span class="hljs-built_in">any</span>;
  <span class="hljs-keyword">let</span> name: <span class="hljs-built_in">string</span>;
  <span class="hljs-keyword">const</span> elm: Element = vnode.elm <span class="hljs-keyword">as</span> Element;
  <span class="hljs-comment">// `VNodeData`上支持传入`class`字段，类似于`&#123; class: &#123; active: true, selected: false &#125; &#125;`，为`true`表示添加样式类，为`false`表示移除样式类</span>
  <span class="hljs-keyword">let</span> oldClass = (oldVnode.data <span class="hljs-keyword">as</span> VNodeData).class;
  <span class="hljs-keyword">let</span> klass = (vnode.data <span class="hljs-keyword">as</span> VNodeData).class;

  <span class="hljs-keyword">if</span> (!oldClass && !klass) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">if</span> (oldClass === klass) <span class="hljs-keyword">return</span>;
  oldClass = oldClass || &#123;&#125;;
  klass = klass || &#123;&#125;;
  <span class="hljs-comment">// 从新的DOM实例上移除旧的样式类</span>
  <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> oldClass) &#123;
    <span class="hljs-keyword">if</span> (oldClass[name] && !<span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(klass, name)) &#123;
      <span class="hljs-comment">// was `true` and now not provided</span>
      elm.classList.remove(name);
    &#125;
  &#125;
  <span class="hljs-comment">// 添加或移除新的样式类</span>
  <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> klass) &#123;
    cur = klass[name];
    <span class="hljs-keyword">if</span> (cur !== oldClass[name]) &#123;
      (elm.classList <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>)[cur ? <span class="hljs-string">"add"</span> : <span class="hljs-string">"remove"</span>](name);
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> classModule: Module = &#123; <span class="hljs-attr">create</span>: updateClass, <span class="hljs-attr">update</span>: updateClass &#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在init时，会解析传入的内置模块，并将其通过闭包放在<code>cbs</code>变量中，在patch时的对应时机，就可以调用相关方法，传入新旧vnode，处理真实的DOM属性</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> cbs: ModuleHooks = &#123;
    <span class="hljs-attr">create</span>: [],
    <span class="hljs-attr">update</span>: [],
    <span class="hljs-attr">remove</span>: [],
    <span class="hljs-attr">destroy</span>: [],
    <span class="hljs-attr">pre</span>: [],
    <span class="hljs-attr">post</span>: [],
  &#125;;

  <span class="hljs-keyword">const</span> api: DOMAPI = domApi !== <span class="hljs-literal">undefined</span> ? domApi : htmlDomApi;

  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < hooks.length; ++i) &#123;
    cbs[hooks[i]] = [];
    <span class="hljs-keyword">for</span> (j = <span class="hljs-number">0</span>; j < modules.length; ++j) &#123;
      <span class="hljs-keyword">const</span> hook = modules[j][hooks[i]];
      <span class="hljs-keyword">if</span> (hook !== <span class="hljs-literal">undefined</span>) &#123;
        (cbs[hooks[i]] <span class="hljs-keyword">as</span> any[]).push(hook);
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种设计可以避免在diff的时候关注相关的DOM操作细节，还有很有意思的。</p>
<h2 data-id="heading-10">小结</h2>
<p>本文虽然命名为Snabbdom源码分析，但实际上主要只关注了<code>patch</code>相关的流程</p>
<ul>
<li>初始化时，使用newVnode，在<code>createElm</code>时通过前序遍历构建DOM树</li>
<li>更新时，对于不同类型的oldVnode和newVnode，先根据newVnode创建新DOM树，然后移除旧的oldVnode</li>
<li>更新时，对于相同类型的oldVnode和newVnode进行<code>patchVnode</code>操作
<ul>
<li>只存在旧子节点列表，执行移除操作</li>
<li>只存在新子节点列表，执行添加操作</li>
<li>同时存在且两者不相同，则执行updateChildren操作，其中包含了diff算法的实现</li>
</ul>
</li>
<li>diff算法的核心思路是通过分治的思想，在每一步操作之后缩小需要检测的范围</li>
</ul>
<p>Snabbdom的实现十分精简，是一份非常值得阅读的源码。现在在回头去看Vue的源码，就轻松得多了。</p>
<p>React在使用Fiber之后，摒弃了递归diff的做法，将整个diff流程分成了patch和commit两个阶段，但其使用diff减少DOM操作的核心思路是类似的，接下来会重新去整理React的fiber和diff实现。</p>
<p>相关参考</p>
<ul>
<li><a href="https://www.jianshu.com/p/f45463e7be20" target="_blank" rel="nofollow noopener noreferrer">Snabbdom 底层Diff算法详解</a></li>
<li><a href="https://lq782655835.github.io/blogs/vue/vue-code-2.snabbdom.html" target="_blank" rel="nofollow noopener noreferrer">虚拟DOM算法库-Snabbdom</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            