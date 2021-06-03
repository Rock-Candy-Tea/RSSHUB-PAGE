
---
title: 'Vue - key_diff'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/525731de53d641ab903e3b324d5f5180~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 18:33:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/525731de53d641ab903e3b324d5f5180~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://juejin.im/post/6844903607913938951" target="_blank" rel="nofollow noopener noreferrer">参考原文-掘金-详解 vue 的 diff 算法</a></p>
<p><code>key</code> 的特殊属性，主要用于 <code>Vue</code> 的虚拟 <code>DOM</code> 算法。在新旧 <code>vnode</code> 的对比中，如果不使用 <code>key</code> ，<code>Vue</code> 会最大限度的减少动态元素并尽可能的就地复用。这会导致一些渲染错误。而且当我们想要触发一些 <code>transition</code> 过渡动画的时候，会出现不生效的情况。因为 <code>vue</code> 判断该元素并没有改变。</p>
<p>而使用 <code>key</code> 的时候，它会基于 <code>key</code> 的变化，重新计算排序元素序列。并且会移除 <code>key</code> 不存在的元素。</p>
<p>其原理在于 <code>Vue</code> 的 <code>diff</code> 算法。而我们的 <code>key</code> 起作用在其 <code>patch</code> 的过程。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
    <span class="hljs-comment">// some code</span>
    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
        patchVnode(oldVnode, vnode);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> oEl = oldVnode.el; <span class="hljs-comment">// 当前oldVnode对应的真实元素节点</span>
        <span class="hljs-keyword">let</span> parentEle = api.parentNode(oEl); <span class="hljs-comment">// 父元素</span>
        createEle(vnode); <span class="hljs-comment">// 根据Vnode生成新元素</span>
        <span class="hljs-keyword">if</span> (parentEle !== <span class="hljs-literal">null</span>) &#123;
            api.insertBefore(parentEle, vnode.el, api.nextSibling(oEl)); <span class="hljs-comment">// 将新元素添加进父元素</span>
            api.removeChild(parentEle, oldVnode.el); <span class="hljs-comment">// 移除以前的旧元素节点</span>
            oldVnode = <span class="hljs-literal">null</span>;
        &#125;
    &#125;
    <span class="hljs-comment">// some code</span>
    <span class="hljs-keyword">return</span> vnode;
&#125;

<span class="hljs-comment">// 作者：windlany</span>
<span class="hljs-comment">// 链接：https://juejin.im/post/6844903607913938951</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/525731de53d641ab903e3b324d5f5180~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">同层比较</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3639a0c26a6d4da681485f357b93c0f2~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果两个节点是一样的，就执行 <code>patchVnode()</code> 方法进一步比较。</p>
<p>如果两个节点不一样，直接用新的 <code>Vnode</code> 替换旧的。如果两个父节点不一样，但是其子节点都是一样的，也不会进行子节点比较。这就是同层比较。</p>
<h2 data-id="heading-1">patchNode()</h2>
<pre><code class="hljs language-js copyable" lang="js">patchVnode (oldVnode, vnode) &#123;
    <span class="hljs-keyword">const</span> el = vnode.el = oldVnode.el
    <span class="hljs-keyword">let</span> i, oldCh = oldVnode.children, ch = vnode.children
    <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">if</span> (oldVnode.text !== <span class="hljs-literal">null</span> && vnode.text !== <span class="hljs-literal">null</span> && oldVnode.text !== vnode.text) &#123;
        api.setTextContent(el, vnode.text)
    &#125;<span class="hljs-keyword">else</span> &#123;
        updateEle(el, vnode, oldVnode)
    <span class="hljs-keyword">if</span> (oldCh && ch && oldCh !== ch) &#123;
            updateChildren(el, oldCh, ch)
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ch)&#123;
            createEle(vnode) <span class="hljs-comment">//create el's children dom</span>
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldCh)&#123;
            api.removeChildren(el)
    &#125;
    &#125;
&#125;

<span class="hljs-comment">// 作者：windlany</span>
<span class="hljs-comment">// 链接：https://juejin.im/post/6844903607913938951</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是根据不同情况进行不同处理了。</p>
<ul>
<li>如果新旧节点指向同一个对象，直接 <code>return</code> 什么都不做。</li>
<li>如果都有文本节点，并且不一样，则用新的替换旧的。</li>
<li>如果 <code>oldVnode</code> 有子节点，而新的 <code>Vnode</code> 没有，则删除该子节点。</li>
<li>反过来，如果 <code>Vnode</code> 有子节点，而 <code>oldVnode</code> 没有，则将该子节点添加。</li>
<li>如果都有子节点，则进行 <code>updateChildren()</code> 比较。</li>
</ul>
<p><code>diff</code> 算法就在 <code>updateChildren()</code> 函数里。</p>
<h2 data-id="heading-2">updateChildren()</h2>
<pre><code class="hljs language-js copyable" lang="js">updateChildren (parentElm, oldCh, newCh) &#123;
    <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>, newStartIdx = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx]
    <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx]
    <span class="hljs-keyword">let</span> oldKeyToIdx
    <span class="hljs-keyword">let</span> idxInOld
    <span class="hljs-keyword">let</span> elmToMove
    <span class="hljs-keyword">let</span> before
    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
        <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;   <span class="hljs-comment">// 对于vnode.key的比较，会把oldVnode = null</span>
            oldStartVnode = oldCh[++oldStartIdx]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
            oldEndVnode = oldCh[--oldEndIdx]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
            newStartVnode = newCh[++newStartIdx]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
            newEndVnode = newCh[--newEndIdx]
            <span class="hljs-comment">// oldS 与 S 比较</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
            patchVnode(oldStartVnode, newStartVnode)
            oldStartVnode = oldCh[++oldStartIdx]
            newStartVnode = newCh[++newStartIdx]
            <span class="hljs-comment">// oldE 与 E 比较</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
            patchVnode(oldEndVnode, newEndVnode)
            oldEndVnode = oldCh[--oldEndIdx]
            newEndVnode = newCh[--newEndIdx]
            <span class="hljs-comment">// oldS 与 E 比较</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
            patchVnode(oldStartVnode, newEndVnode)
            api.insertBefore(parentElm, oldStartVnode.el, api.nextSibling(oldEndVnode.el))
            oldStartVnode = oldCh[++oldStartIdx]
            newEndVnode = newCh[--newEndIdx]
            <span class="hljs-comment">// oldE 与 S 比较</span>
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123;
            patchVnode(oldEndVnode, newStartVnode)
            api.insertBefore(parentElm, oldEndVnode.el, oldStartVnode.el)
            oldEndVnode = oldCh[--oldEndIdx]
            newStartVnode = newCh[++newStartIdx]
        &#125;<span class="hljs-keyword">else</span> &#123;
           <span class="hljs-comment">// 使用key时的比较</span>
            <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
                oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx) <span class="hljs-comment">// 有key生成index表</span>
            &#125;
            idxInOld = oldKeyToIdx[newStartVnode.key]
            <span class="hljs-keyword">if</span> (!idxInOld) &#123;
                api.insertBefore(parentElm, createEle(newStartVnode).el, oldStartVnode.el)
                newStartVnode = newCh[++newStartIdx]
            &#125;
            <span class="hljs-keyword">else</span> &#123;
                elmToMove = oldCh[idxInOld]
                <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123;
                    api.insertBefore(parentElm, createEle(newStartVnode).el, oldStartVnode.el)
                &#125;<span class="hljs-keyword">else</span> &#123;
                    patchVnode(elmToMove, newStartVnode)
                    oldCh[idxInOld] = <span class="hljs-literal">null</span>
                    api.insertBefore(parentElm, elmToMove.el, oldStartVnode.el)
                &#125;
                newStartVnode = newCh[++newStartIdx]
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
        before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].el
        addVnodes(parentElm, before, newCh, newStartIdx, newEndIdx)
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartIdx > newEndIdx) &#123;
        removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数主要做了以下事情：</p>
<ul>
<li>将 <code>Vnode</code> 的子节点 <code>VnodeChildren(下文称Vch)</code> 和 <code>oldNode</code> 的子节点 <code>oldNodeChildren(下文称oldCh)</code> 提取出来。</li>
<li><code>Vch</code> 和 <code>oldCh</code> 各有两个头尾的变量 <code>startIdx</code> 和 <code>endIdx</code> 。 他们的两个变量相互比较。一共有 4 种比较方式。如果 4 种都没有匹配，再看是否设置了 <code>key</code>。如果设置了，就会用 <code>key</code> 进行比较。在比较的过程中，变量会往中间靠，一旦 <code>startIdx > endIdx</code> 表明 <code>oldCh</code> 和 <code>Vch</code> 至少有一个已经遍历完了，就会结束比较。</li>
</ul>
<p>接下来上图：</p>
<p>以下是 <code>Vnode</code> 和 <code>oldVnode</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12902cbe73ab49c7b8cc591ab9defeb7~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将其取出来，并分别赋予头尾变量。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5a814b3420b4df7b59ad34b42aa8b0d~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>oldS</code> 将会与 <code>S</code> 和 <code>E</code> 做 <code>sameNode</code> 比较。<code>oldE</code> 将会与 <code>S</code> 和 <code>E</code> 做 <code>sameNode</code> 比较。</p>
<ul>
<li>一旦有一对匹配上了，那么真实的 <code>DOM</code> 会移动到与之对应的节点。这两个指针会像中间移动。</li>
<li>如果 4 组都没有匹配上，分两种情况。
<ul>
<li>如果新旧子节点都存在 <code>key</code> , 那么会根据 <code>oldCh</code> 的 <code>key</code> 生成一张 <code>hash表</code> 。用 <code>S</code> 的 <code>key</code> 与之做对比。匹配成功就去判断这 <code>S</code> 和 该节点是否 <code>sameNode</code> 。如果是，就在真实 <code>DOM</code> 中将成功的节点移到最前面。否则将 <code>S</code> 对应生成的节点插入到 <code>DOM</code> 中对应的 <code>oldS</code> 位置。 <code>S</code> 指针向中间移动，被匹配 <code>old</code> 中的节点置为 <code>null</code> 。</li>
<li>如果没有 <code>key</code>, 则直接将 <code>S</code> 生成新的节点插入真实 <code>DOM</code>。</li>
</ul>
</li>
</ul>
<p>也就是，没有 <code>key</code> 只会做 4 中匹配，就算指针中间有可复用的节点，也不能被复用。</p>
<p>接下来，看一下上图做匹配的过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c064ee4f8b00421b8b0ab87606742bb0~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>oldS</code> 与 <code>S</code> 匹配</p>
</blockquote>
<p>将 <code>DOM</code> 中的节点 <code>a</code> 放到第一个。已经是第一个了就不管了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecb89e0fcb6f43b8b24c32ddc28822a1~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>olds</code> 与 <code>E</code> 匹配</p>
</blockquote>
<p>将 <code>DOM</code> 中的节点 <code>b</code> 放到最后一个。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85ff7dee14494c42a344d08b88ddebf3~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>oldE</code> 与 <code>S</code> 匹配</p>
</blockquote>
<p>本来是要将 <code>c</code> 移动到 <code>S</code> 对应的位置。可是真实 <code>DOM</code> 中节点<code>c</code> 已经是在第二个位置了。所以什么都不做。</p>
<blockquote>
<p><code>oldS > oldE</code> 结束匹配。</p>
</blockquote>
<p>将剩余的节点 <code>d</code> 按照自己的 <code>index</code> 插入到 <code>DOM</code> 中去。</p>
<p>匹配结束有两种情况。</p>
<ul>
<li><code>oldS > oldE</code> 说明 <code>oldCh</code> 先遍历完，则需要将多余的 <code>Vch</code> 根据 <code>index</code> 添加到 <code>DOM</code> 中。</li>
<li><code>S > E</code> 说明 <code>Vch</code> 先遍历完。则需要删除 <code>oldCh</code> 中多余的节点。</li>
</ul></div>  
</div>
            