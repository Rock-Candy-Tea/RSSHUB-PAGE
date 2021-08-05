
---
title: 'Vue Diff 算法的执行过程探究'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0107b7701b00497d8ac26f003ed1a6be~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 01:59:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0107b7701b00497d8ac26f003ed1a6be~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">Diff 算法的执行过程</h4>
<p>描述diff算法的执行过程之前，首先需要了解的是虚拟DOM的diff算法的比较对象是什么？以及怎么描述虚拟DOM，是真的创建一个DOM树对比还是其他的方式？</p>
<ul>
<li>虚拟dom中的diff算法是需要对比两棵树每一个节点的差异</li>
<li>当数据发生变化后不直接操作dom,而是用js对象的方式描述真实dom</li>
<li>当数据发生变化后先比较js对象是否发生改变，找到所有改变的位置，然后最小化的更新变化的位置</li>
</ul>
<h5 data-id="heading-1">diff算法的执行流程：</h5>
<ol>
<li>
<p>执行patch函数传入新旧两个节点如：pacth(oldVnode,vnode)。</p>
</li>
<li>
<p>判断新旧两个节点即oldVnode、vnode是否相同。在这里需要注意的是snabbdom在回想出入的新旧节点oldVnode、vnode先转化成VNode对象。那么判断相同的依旧是节点(vnode.key && vnode.sel)相同。</p>
</li>
<li>
<p>如果两个节点不相同，在父节点插入新节点即（vnode）,然后在删除老节点（oldVnde）。（差异是最好处理的）</p>
</li>
<li>
<p>如果两个节点的key&&sel相同，就需要对比两个节点的文本、子节点（数组）是否相同，找出差异位置。</p>
</li>
<li>
<p>如果新老节点的文本不相同，只需要更新文本内容，同时判断老节点的子节点数组不为空的，删除老节点的所有子节点 。（差异是最好处理的）</p>
</li>
<li>
<p>如果只有新节点有子节点数组，重置老节点的文本为空，添加新节点数组。（差异是最好处理的）</p>
</li>
<li>
<p>如果只有老节点有子节点数组，删除所有子节点数组。（差异是最好处理的）</p>
</li>
<li>
<p>如果新老节点都有子节点数组，且子节点不相同(相同的key&&sel,但子节点数组不同，最复杂的处理逻辑)</p>
</li>
<li>
<p>在这一步会发现是新老子节点数组对比，那么必定是一个循环遍历。这个是后续可以参考snabbdom源码会发现有一下几个变量</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//新老节点数组开始、结束的位置</span>
<span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span>;
​
<span class="hljs-comment">//新老节点数组开始、结束的位置对应的数据</span>
<span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>];
<span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx];
<span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>];
<span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>基于第9步，会发现在遍历对比节点内容是，该步骤会返回到执行流程的第3步。</p>
</li>
</ol>
<h5 data-id="heading-2">简单的伪代码实现流程如下，代码注释可能会帮助理解流程：</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span> (<span class="hljs-params">oldCh,newCh</span>)</span>&#123;
    <span class="hljs-comment">// 以下参数有助于帮助理解遍历是下标的移动过程</span>
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
​
    <span class="hljs-comment">//同级别节点比较</span>
    <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
        oldStartVnode = oldCh[++oldStartIdx]; <span class="hljs-comment">// Vnode might have been moved left</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
        oldEndVnode = oldCh[--oldEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
        newStartVnode = newCh[++newStartIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
        newEndVnode = newCh[--newEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
        <span class="hljs-comment">// 同级节点且新、旧开始位置相同 比较好理解</span>
        patchVnode(oldStartVnode, newStartVnode);
        oldStartVnode = oldCh[++oldStartIdx];
        newStartVnode = newCh[++newStartIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newEndVnode)) &#123;
        <span class="hljs-comment">// 同级节点且新、旧开始位置相同 比较好理解</span>
        patchVnode(oldEndVnode, newEndVnode);
        oldEndVnode = oldCh[--oldEndIdx];
        newEndVnode = newCh[--newEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newEndVnode)) &#123;
        <span class="hljs-comment">// 同级节点且新、旧开始位置不同，如果相同交互位置</span>
        <span class="hljs-comment">// Vnode moved right</span>
        patchVnode(oldStartVnode, newEndVnode);
        api.insertBefore();
        oldStartVnode = oldCh[++oldStartIdx];
        newEndVnode = newCh[--newEndIdx];
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldEndVnode, newStartVnode)) &#123;
        / 同级节点且新、旧开始位置不同，如果相同交互位置
        <span class="hljs-comment">// Vnode moved left</span>
        patchVnode(oldEndVnode, newStartVnode);
        api.insertBefore();
        oldEndVnode = oldCh[--oldEndIdx];
        newStartVnode = newCh[++newStartIdx];
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// createKeyToOldIdx 获取所有老节点子节点数组的key  这可能是最麻烦的对比的位置</span>
        <span class="hljs-keyword">if</span> (oldKeyToIdx === <span class="hljs-literal">undefined</span>) &#123;
          oldKeyToIdx = createKeyToOldIdx(oldCh, oldStartIdx, oldEndIdx);
        &#125;
        <span class="hljs-comment">// 最后的理论场景还是将新节点插入到老节点的父元素</span>
        <span class="hljs-comment">// 找到老节点子节点数组key</span>
        <span class="hljs-comment">// 找到新开始节点位置的key 不为空 然后插入父元素</span>
        idxInOld = oldKeyToIdx[newStartVnode.key <span class="hljs-keyword">as</span> string];
        <span class="hljs-keyword">if</span> (isUndef(idxInOld)) &#123;
          <span class="hljs-comment">// New element</span>
          api.insertBefore();
        &#125; <span class="hljs-keyword">else</span> &#123;
          elmToMove = oldCh[idxInOld];
          <span class="hljs-keyword">if</span> (elmToMove.sel !== newStartVnode.sel) &#123;
            api.insertBefore();
          &#125; <span class="hljs-keyword">else</span> &#123;
            patchVnode(elmToMove, newStartVnode);
            oldCh[idxInOld] = <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> any;
            api.insertBefore();
          &#125;
        &#125;
        newStartVnode = newCh[++newStartIdx];
      &#125;
    &#125;
    <span class="hljs-comment">//循环结束的收尾工作</span>
    <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx || newStartIdx <= newEndIdx) &#123;
      <span class="hljs-keyword">if</span> (oldStartIdx > oldEndIdx) &#123;
        before = newCh[newEndIdx + <span class="hljs-number">1</span>] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : newCh[newEndIdx + <span class="hljs-number">1</span>].elm;
        addVnodes();
      &#125; <span class="hljs-keyword">else</span> &#123;
        removeVnodes(parentElm, oldCh, oldStartIdx, oldEndIdx);
      &#125;
    &#125;
  &#125;
​
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode,vnode</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (oldVnode === vnode) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">if</span> (isUndef(vnode.text)) &#123; 
      <span class="hljs-keyword">if</span> (isDef(oldCh) && isDef(ch)) &#123;
        <span class="hljs-comment">// 新旧节点的子节点存在且不相同是，逐个对比子节点，如要遍历</span>
        <span class="hljs-keyword">if</span> (oldCh !== ch) updateChildren(elm, oldCh, ch, insertedVnodeQueue);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(ch)) &#123;
        <span class="hljs-comment">// 只有新节点的子节点数组有值，添加所有子节点</span>
        <span class="hljs-comment">// 重置文本参数</span>
        <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) api.setTextContent(elm, <span class="hljs-string">""</span>);
        addVnodes();
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
        <span class="hljs-comment">// 只有老节点的子节点数组有值 删除所有子节点</span>
        removeVnodes();
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.text)) &#123;
        <span class="hljs-comment">// 只有老节点的文本有值 重置参数</span>
        api.setTextContent(elm, <span class="hljs-string">""</span>);
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldVnode.text !== vnode.text) &#123;
      <span class="hljs-keyword">if</span> (isDef(oldCh)) &#123;
        <span class="hljs-comment">// 若老节点的子节点数组不为空 删除</span>
        removeVnodes()
      &#125;
      api.setTextContent(elm, vnode.text!);
    &#125;
  &#125;
​
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode,vnode</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
      <span class="hljs-comment">// 初次将oldVnode转换成VNode节点</span>
      oldVnode = emptyNodeAt(oldVnode)
    &#125;
    <span class="hljs-comment">// 比较两个节点是否相同 key && sel (即两个节点的标识是否相同)</span>
    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123; 
      <span class="hljs-comment">// 详情对比新旧两个节点参数</span>
      patchVnode(oldVnode, vnode);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 找到父元素是否存在</span>
      <span class="hljs-comment">// 创建新节点</span>
      createElm(vnode);
      <span class="hljs-comment">// 插入新节点，移除老节点</span>
      <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">null</span>) &#123;
        api.insertBefore(parent, vnode.elm!, api.nextSibling(elm));
        removeVnodes(parent, [oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> vnode
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">同时了梳理一份流程图：</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0107b7701b00497d8ac26f003ed1a6be~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="Vue DIff (1).jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            