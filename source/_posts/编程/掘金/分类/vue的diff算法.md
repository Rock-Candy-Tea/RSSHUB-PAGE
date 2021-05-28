
---
title: 'vue的diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2f06aec5bd14050991f42d56b35a90f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 22:21:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2f06aec5bd14050991f42d56b35a90f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>当组件创建和更新时，vue均会执行内部的update函数，该函数使用render函数生成的虚拟dom树，将新旧两树进行对比，找到差异点，最终更新到真实dom</li>
<li>对比差异的过程叫diff，vue在内部通过一个叫patch的函数完成该过程</li>
<li>在对比时，vue采用深度优先、同层比较的方式进行比对。</li>
<li>在判断两个节点是否相同时，vue是通过虚拟节点的key和tag来进行判断的</li>
<li>具体来说，首先对根节点进行对比，如果相同则将旧节点关联的真实dom的引用挂到新节点上，然后根据需要更新属性到真实dom，然后再对比其子节点数组；如果不相同，则按照新节点的信息递归创建所有真实dom，同时挂到对应虚拟节点上，然后移除掉旧的dom。</li>
<li>在对比其子节点数组时，vue对每个子节点数组使用了两个指针，分别指向头尾，然后不断向中间靠拢来进行对比，这样做的目的是尽量复用真实dom，尽量少的销毁和创建真实dom。如果发现相同，则进入和根节点一样的对比流程，如果发现不同，则移动真实dom到合适的位置。</li>
<li>这样一直递归的遍历下去，直到整棵树完成对比。</li>
</ol>
<h2 data-id="heading-0">diff的时机</h2>
<p>当组件创建时，以及依赖的属性或数据变化时，会运行一个函数，该函数会做两件事：</p>
<p>运行_render生成一棵新的虚拟dom树（vnode tree）
运行_update，传入虚拟dom树的根节点，对新旧两棵树进行对比，最终完成对真实dom的更新
核心代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// ... 其他代码</span>
  <span class="hljs-keyword">var</span> updateComponent = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>._update(<span class="hljs-built_in">this</span>._render())
  &#125;
  <span class="hljs-keyword">new</span> Watcher(updateComponent);
  <span class="hljs-comment">// ... 其他代码</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">diff就发生在_update函数的运行过程中
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>_update函数在干什么</strong></p>
<p>_update函数接收到一个vnode参数，这就是新生成的虚拟dom树</p>
<p>同时，_update函数通过当前组件的_vnode属性，拿到旧的虚拟dom树</p>
<p>_update函数首先会给组件的_vnode属性重新赋值，让它指向新树</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2f06aec5bd14050991f42d56b35a90f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>然后会判断旧树是否存在：</strong></p>
<ul>
<li>不存在：说明这是第一次加载组件，于是通过内部的patch函数，直接遍历新树，为每个节点生成真实DOM，挂载到每个节点的elm属性上</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51d0a077adfc41c7b4eb28d5c99721f8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210301194237825" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>存在：说明之前已经渲染过该组件，于是通过内部的patch函数，对新旧两棵树进行对比，以达到下面两个目标：</p>
<pre><code class="copyable">完成对所有真实dom的最小化处理

让新树的节点对应合适的真实dom
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d26108134184f68a0eb33a5b6f9d12e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>patch函数的对比流程</p>
<p>术语解释：</p>
<ul>
<li>「相同」：是指两个虚拟节点的标签类型、key值均相同，但input元素还要看type属性</li>
<li>「新建元素」：是指根据一个虚拟节点提供的信息，创建一个真实dom元素，同时挂载到虚拟节点的elm属性上</li>
<li>「销毁元素」：是指：vnode.elm.remove()</li>
<li>「更新」：是指对两个虚拟节点进行对比更新，它仅发生在两个虚拟节点</li>
<li>「相同」的情况下。具体过程稍后描述。</li>
<li>「对比子节点」：是指对两个虚拟节点的子节点进行对比，具体过程稍后描述</li>
</ul>
<p>详细流程：</p>
<p>根节点比较</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a267993abce407d879172c8ef0482d8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210301203350246" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>patch函数首先对根节点进行比较</strong></p>
<p>如果两个节点：</p>
<p>「相同」，进入**「更新」流程**</p>
<ol>
<li>将旧节点的真实dom赋值到新节点：newVnode.elm = oldVnode.elm</li>
<li>对比新节点和旧节点的属性，有变化的更新到真实dom中</li>
<li>当前两个节点处理完毕，开始**「对比子节点」**</li>
</ol>
<p>不「相同」</p>
<ol>
<li>新节点递归「新建元素」</li>
<li>旧节点「销毁元素」</li>
<li>「对比子节点」</li>
</ol>
<p>在「对比子节点」时，vue一切的出发点，都是为了：</p>
<ul>
<li>尽量啥也别做</li>
<li>不行的话，尽量仅改动元素属性</li>
<li>还不行的话，尽量移动元素，而不是删除和创建元素</li>
<li>还不行的话，删除和创建元素</li>
</ul></div>  
</div>
            