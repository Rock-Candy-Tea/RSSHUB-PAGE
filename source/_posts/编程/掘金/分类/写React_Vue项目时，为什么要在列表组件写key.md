
---
title: '写React_Vue项目时，为什么要在列表组件写key'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a36443b972e45288959c51233e7a442~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 01:58:58 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a36443b972e45288959c51233e7a442~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">key的作用是什么</h2>
<blockquote>
<p>key是给每一个vnode的唯一id，可以依靠key，更准确，更快地拿到oldVnode中对应的vnode节点。</p>
</blockquote>
<h3 data-id="heading-1">更准确</h3>
<p>在<code>vue/patch.js</code>中，<a href="https://github.com/vuejs/vue/blob/dev/src/core/vdom/patch.js#L35" target="_blank" rel="nofollow noopener noreferrer">sameVnode</a>函数需要进行判断：<code>a.key === b.key</code>。在不带key的情况下，a.key和b.key都是undefined，对于<strong>列表渲染</strong>来说，已经可以判断为相同节点，然后调用patchVnode。在带key的情况下，<code>a.key === b.key</code>对比中可以避免<a href="https://juejin.cn/post/6963567075214884895#%E5%B0%B1%E5%9C%B0%E5%A4%8D%E7%94%A8">就地复用</a>的情况，所以会更加准确。</p>
<h3 data-id="heading-2">更快</h3>
<p>vue和react都是采用<a href="https://juejin.cn/post/6963567075214884895#diff%E7%AE%97%E6%B3%95">diff算法</a>来对比新旧虚拟节点，从而更新节点。</p>
<p>利用key的唯一性生成map对象来获取对应节点，比遍历方式更快。在<code>vue/patch.js</code>的<a href="https://github.com/vuejs/vue/blob/dev/src/core/vdom/patch.js#L404" target="_blank" rel="nofollow noopener noreferrer">updateChild</a>函数中，会对新旧节点进行交叉对比，当新节点跟旧节点头尾交叉对比没有结果时，会根据新节点的key去对比旧节点数组中的key，从而找到相应旧节点（这里对应的是一个key => index 的map映射）。如果没找到就认为是一个新增节点。而如果没有key，那么就会采用遍历查找的方式去找到对应的旧节点。一种一个map映射，另一种是遍历查找。相比而言。map映射的速度更快。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue项目  src/core/vdom/patch.js  -488行</span>
<span class="hljs-comment">// 以下是为了阅读性进行格式化后的代码</span>

<span class="hljs-comment">// oldCh 是一个旧虚拟节点数组</span>
<span class="hljs-keyword">if</span> (isUndef(oldKeyToIdx)) &#123;
  oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx)
&#125;
<span class="hljs-keyword">if</span>(isDef(newStartVnode.key)) &#123;
  <span class="hljs-comment">// map 方式获取</span>
  idxInOld = oldKeyToIdx[newStartVnode.key]
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 遍历方式获取</span>
  idxInOld = findIdxInOld(newStartVnode, oldCh, oldStartIdx, oldEndIdx)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建map函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createKeyToOldIdx</span> (<span class="hljs-params">children, beginIdx, endIdx</span>) </span>&#123;
  <span class="hljs-keyword">let</span> i, key
  <span class="hljs-keyword">const</span> map = &#123;&#125;
  <span class="hljs-keyword">for</span> (i = beginIdx; i <= endIdx; ++i) &#123;
    key = children[i].key
    <span class="hljs-keyword">if</span> (isDef(key)) map[key] = i
  &#125;
  <span class="hljs-keyword">return</span> map
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遍历查找</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// sameVnode 是对比新旧节点是否相同的函数</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findIdxInOld</span> (<span class="hljs-params">node, oldCh, start, end</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = start; i < end; i++) &#123;
      <span class="hljs-keyword">const</span> c = oldCh[i]
      
      <span class="hljs-keyword">if</span> (isDef(c) && sameVnode(node, c)) <span class="hljs-keyword">return</span> i
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">补充知识</h2>
<h3 data-id="heading-4">diff算法</h3>
<p><strong>diff流程图</strong>：
当数据发生改变时，set方法会让调用<code>Dep.notify</code>通知所有订阅者Watcher，订阅者就会调用<code>patch</code>给真实的DOM打补丁，更新相应的视图。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a36443b972e45288959c51233e7a442~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>patch</strong></p>
<p>patch的核心代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span> (<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
    <span class="hljs-comment">// some code</span>
    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
    patchVnode(oldVnode, vnode)
    &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> oEl = oldVnode.el <span class="hljs-comment">// 当前oldVnode对应的真实元素节点</span>
    <span class="hljs-keyword">let</span> parentEle = api.parentNode(oEl)  <span class="hljs-comment">// 父元素</span>
    createEle(vnode)  <span class="hljs-comment">// 根据Vnode生成新元素</span>
    <span class="hljs-keyword">if</span> (parentEle !== <span class="hljs-literal">null</span>) &#123;
            api.insertBefore(parentEle, vnode.el, api.nextSibling(oEl)) <span class="hljs-comment">// 将新元素添加进父元素</span>
            api.removeChild(parentEle, oldVnode.el)  <span class="hljs-comment">// 移除以前的旧元素节点</span>
            oldVnode = <span class="hljs-literal">null</span>
    &#125;
    &#125;
    <span class="hljs-comment">// some code </span>
    <span class="hljs-keyword">return</span> vnode
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>patch函数接收两个参数<code>oldVnode</code>和<code>Vnode</code>分别代表新的节点和之前的旧节点。</p>
<p>判断两节点是否值得比较，值得比较则执行<code>patchVnode</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    a.key === b.key &&  <span class="hljs-comment">// key值</span>
    a.tag === b.tag &&  <span class="hljs-comment">// 标签名</span>
    a.isComment === b.isComment &&  <span class="hljs-comment">// 是否为注释节点</span>
    <span class="hljs-comment">// 是否都定义了data，data包含一些具体信息，例如onclick , style</span>
    isDef(a.data) === isDef(b.data) &&  
    sameInputType(a, b) <span class="hljs-comment">// 当标签是<input>的时候，type必须相同</span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不值得比较则用<code>Vnode</code>替换<code>oldVnode</code></p>
<p>如果两个节点都是一样的，那么就深入检查他们的子节点。如果两个节点不一样那就说明<code>Vnode</code>完全被改变了，就可以直接替换oldVnode。</p>
<p>虽然这两个节点不一样但是他们的子节点一样怎么办？别忘了，diff可是逐层比较的，如果第一层不一样那么就不会继续深入比较第二层了。</p>
<p><strong>patchVnode</strong></p>
<p>当我们确定两个节点值得比较之后我们会对两个节点指定<code>patchVnode</code>方法。那么这个方法做了什么呢？</p>
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
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数做了以下事情：</p>
<ul>
<li>找到对应的真实dom，称为el</li>
<li>判断Vnode和oldVnode是否指向同一个对象，如果是，那么直接return</li>
<li>如果他们都有文本节点并且不相等，那么将el的文本节点设置为Vnode的文本节点。</li>
<li>如果oldVnode有子节点而Vnode没有，则删除el的子节点</li>
<li>如果oldVnode没有子节点而Vnode有，则将Vnode的子节点真实化之后添加到el</li>
<li>如果两者都有子节点，则执行updateChildren函数比较子节点，这一步很重要</li>
</ul>
<p>其他几个点都很好理解，我们详细来讲一下updateChildren</p>
<p><strong>updateChildren</strong></p>
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
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
            patchVnode(oldStartVnode, newStartVnode)
            oldStartVnode = oldCh[++oldStartIdx]
            newStartVnode = newCh[++newStartIdx]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
            patchVnode(oldEndVnode, newEndVnode)
            oldEndVnode = oldCh[--oldEndIdx]
            newEndVnode = newCh[--newEndIdx]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
            patchVnode(oldStartVnode, newEndVnode)
            api.insertBefore(parentElm, oldStartVnode.el, api.nextSibling(oldEndVnode.el))
            oldStartVnode = oldCh[++oldStartIdx]
            newEndVnode = newCh[--newEndIdx]
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
<p>先说一下这个函数做了什么</p>
<ul>
<li>将<code>Vnode</code>的子节点<code>Vch</code>和<code>oldVnode</code>的子节点<code>oldCh</code>提取出来</li>
<li><code>oldCh</code>和<code>vCh</code>各有两个头尾的变量<code>StartIdx</code>和<code>EndIdx</code>，它们的2个变量相互比较，一共有4种比较方式。如果4种比较都没匹配，在设置了key的情况下，就会用key进行比较，在比较的过程中，变量会往中间靠，一旦StartIdx>EndIdx表明oldCh和vCh至少有一个已经遍历完了，就会结束比较。</li>
</ul>
<p>现在分别对<code>oldS</code>、<code>oldE</code>、<code>S</code>、<code>E</code>两两做<code>sameVnode</code>比较，有四种比较方式，当其中两个能匹配上那么真实dom中的相应节点会移到Vnode相应的位置，这句话有点绕，打个比方</p>
<ul>
<li>如果是<code>oldS</code>和<code>E</code>匹配上了，那么真实dom中的第一个节点会移到最后</li>
<li>如果是<code>oldE</code>和<code>S</code>匹配上了，那么真实dom中的最后一个节点会移到最前，匹配上的两个指针向中间移动</li>
<li>如果四种匹配没有一对是成功的，分为两种情况
<ul>
<li>如果新旧子节点都<strong>存在key</strong>，那么会根据<code>oldChild</code>的key生成一张<strong>hash表</strong>，用<code>S</code>的key与hash表做匹配，匹配成功就判断S和匹配节点是否为<code>sameNode</code>，如果是，就在真实dom中将成功的节点移到最前面，否则，将S生成对应的节点插入到dom中对应的<code>oldS</code>位置，S指针向中间移动，被匹配old中的节点置为null。</li>
<li>如果<strong>没有key</strong>,则直接将S生成新的节点插入真实DOM（ps：这下可以解释为什么v-for的时候需要设置key了，如果没有key那么就只会做四种匹配，就算指针中间有可复用的节点都不能被复用了）</li>
</ul>
</li>
</ul>
<h3 data-id="heading-5">就地复用</h3>
<p>官方解释：</p>
<blockquote>
<p>如果数据项的顺序被改变，Vue将不会移动DOM元素来匹配数据项的顺序，而是简单复用此处的每个元素</p>
</blockquote>
<p>用代码解释这段话：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">'item in list'</span>></span>
  &#123;&#123;文本&#125;&#125;<span class="hljs-tag"><<span class="hljs-name">input</span>/></span><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"将item在list中的位置下移"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>演示地址：<a href="https://jsbin.com/numiwog/edit?html,output" target="_blank" rel="nofollow noopener noreferrer">JsBin</a></p>
<p>在“就地复用”中，点击按钮，输入框不会随着文本下移。这是因为输入框没有与数据绑定(data)，所以vue默认使用已经渲染的DOM。然而文本是和数据绑定的，所以文本会被重新渲染。因为高效，这种处理方式在vue或者angular中都是默认的列表渲染策略。</p>
<p>这种“就地复用”一般的<strong>列表展示</strong>中不会出现问题，既然如此，为什么还要建议带key呢？因为这种模式只适用于渲染简单的无状态组件。对于大多数场景来说，列表组件都有自己的状态。</p>
<p>官方解释：</p>
<blockquote>
<p>“就地复用”的模式是高效的，但是只适用于<strong>不依赖子组件状态或临时DOM状态</strong>（例如：表单输入值）的列表渲染输出。</p>
</blockquote>
<p>举个例子：一个新闻列表，可点击列表项来将其标记为“已访问”，可通过tab切换“娱乐新闻”或者“社会新闻”。</p>
<p>不带key属性的情况下，在“娱乐新闻”下选中第二项然后切换到“社会新闻”，"社会新闻"里的第二项也会是被选中的状态，因为这里复用了组件，保留了之前的状态。要解决这个问题，可以为列表项带上新闻id作为唯一key，那么每次渲染列表时都会完全替换所有组件，使其拥有正确状态。</p>
<p>这只是个简单的例子，实际应用会更复杂。带上唯一key虽然会增加开销，但是对于用户来说基本感受不到差距，而且能保证组件状态正确，这应该就是为什么推荐使用唯一id作为key的原因。至于具体怎么使用，就要根据实际情况来选择了。</p>
<p>所以，建议是：如果列表元素存在<strong>与用户交互</strong>的场景（比如form表单或者重新排序等），那么需要为v-for指令设置key参数，key只想列表中每个元素的唯一值。</p>
<h2 data-id="heading-6">参考文章</h2>
<p><a href="https://github.com/Advanced-Frontend/Daily-Interview-Question/issues/1" target="_blank" rel="nofollow noopener noreferrer">依扬——Daily-Interview-Question</a></p>
<p><a href="https://juejin.cn/post/6844903607913938951" target="_blank">windlany——详解vue的diff算法</a></p>
<p><a href="https://www.zhihu.com/question/61078310" target="_blank" rel="nofollow noopener noreferrer">霸都丶傲天——Vue2.0 中 v-for里面的 “就地复用” 策略 是什么？</a></p></div>  
</div>
            