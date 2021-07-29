
---
title: 'Vue3 源码解毒 & PK React17'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ff2d18d93049d4abf24abb14f6060c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 09:33:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ff2d18d93049d4abf24abb14f6060c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>因为最近开始写Vue了，对于我一个react骨灰级玩家来说其实是一个挑战。其实我现在更偏向于写原生JS，因为市场上绝大部分做得好的框架库几乎都脱离不了<code>Vitrual DOM</code>体系。</p>
<p>而我们知道的是，通过<code>Vitrual DOM</code>来更新真实DOM，性能肯定是比不过直接对原生DOM进行操作的性能。<strong>如果我能明确知道哪个DOM要发生变化，那直接 <code>document.getElementById(id).xx</code> 多好？</strong></p>
<p><code>Vitrual DOM</code>的价值从来都不在性能方面。emmm... 今天主题是对Vue的源码进行一个解毒，目的是能够清晰知道Vue到底做了哪些事情，优劣势又分别在哪。</p>
<h3 data-id="heading-1">1. 先从Vue 的 diff 算法开始解剖</h3>
<p>走<code>Vitrual DOM</code> 路线的都逃不过<code>diff</code>算法。 <code>diff</code>算法家家有，那 <strong><code>Vue3</code></strong> 的<code>diff</code>算法又是长什么样的。</p>
<p>先来看个栗子。</p>
<pre><code class="hljs language-js copyable" lang="js">    <ul key=<span class="hljs-string">"ul1"</span>> 
        <li>渣男<li>
        <li>胖子<li>
        <li>就知道吃<li>
    <ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要转化成：</p>
<pre><code class="hljs language-js copyable" lang="js">    <ol key=<span class="hljs-string">"ul1"</span>> 
        <li>渣男<li>
        <li>胖子<li>
        <li>就知道吃吗？<div>你个渣男！</div><li>
    <ol>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>Q： 就把</code>ul<code>变成</code>ol<code> ，key都没变，甚至其子结点都不变。请问 Vue 重新如何渲染？</code></strong></p>
<p>答： 全部重新渲染一遍。</p>
<p>所以，合理吗？ 如果存在即合理，那为什么要这样设计呢？ 这里有人要diss我了，这种场景实际开发中太少见了。（被怼得很难过，这个后续再说吧。真的是可以解决这种问题的……😂）</p>
<h4 data-id="heading-2">diff的执行策略</h4>
<ul>
<li><code>同一个虚拟节点，才进行精细化diff比较。</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 先看源码中的一个方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isSameVNodeType</span>(<span class="hljs-params">n1, n2</span>) </span>&#123; 
<span class="hljs-comment">// ... </span>
<span class="hljs-keyword">return</span> n1.type === n2.type && n1.key === n2.key 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看方法名你其实就明白了，这是个判断两个VNode 是否是同一个。 看函数返回值你就更加明白，两个VNode要一致就得结点类型一样、key也得一样。</p>
<ul>
<li><code>只进行同层比较，不会进行跨层比较</code></li>
</ul>
<p>那回到上面的问题，继续看个栗子：</p>
<pre><code class="hljs language-js copyable" lang="js">    <ul key=<span class="hljs-string">"ul1"</span>> 
        <li>渣男<li>
        <li>胖子<li>
        <li>就知道吃吗？<div>你个渣男！</div><li>
    <ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>Q： 如果 ul 不再变，只是其中一个 li 元素的内容发生了变化。那请问又是咋渲染的？</code></strong></p>
<p>答：如果<code>li</code>发送变动，只会进行<code>li</code>同层的diff比较，不会进行<code>li</code>子元素<code>div</code> diff 。 我相信使用过Vue的人都知道答案。</p>
<h4 data-id="heading-3">patchChildren - 更新子结点</h4>
<p>上源码。</p>
<pre><code class="hljs language-js copyable" lang="js">
      <span class="hljs-keyword">const</span> patchChildren = <span class="hljs-function">(<span class="hljs-params">n1, n2, container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized = <span class="hljs-literal">false</span></span>) =></span> &#123;
          <span class="hljs-keyword">const</span> c1 = n1 && n1.children;
          <span class="hljs-keyword">const</span> prevShapeFlag = n1 ? n1.shapeFlag : <span class="hljs-number">0</span>;
          <span class="hljs-keyword">const</span> c2 = n2.children;
          <span class="hljs-keyword">const</span> &#123; patchFlag, shapeFlag &#125; = n2;
          <span class="hljs-comment">// fast path</span>
          <span class="hljs-keyword">if</span> (patchFlag > <span class="hljs-number">0</span>) &#123;
              <span class="hljs-keyword">if</span> (patchFlag & <span class="hljs-number">128</span> <span class="hljs-comment">/* KEYED_FRAGMENT */</span>) &#123;
                  <span class="hljs-comment">// this could be either fully-keyed or mixed (some keyed some not)</span>
                  <span class="hljs-comment">// presence of patchFlag means children are guaranteed to be arrays</span>
                  <span class="hljs-comment">/*
                  *1 - patchKeyedChildren
                  */</span> 
                  patchKeyedChildren(c1, c2, container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
                  <span class="hljs-keyword">return</span>;
              &#125;
              <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (patchFlag & <span class="hljs-number">256</span> <span class="hljs-comment">/* UNKEYED_FRAGMENT */</span>) &#123;
                  <span class="hljs-comment">// unkeyed</span>
                  <span class="hljs-comment">/*
                   * 2 - patchUnkeyedChildren
                   */</span> 
                  patchUnkeyedChildren(c1, c2, container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
                  <span class="hljs-keyword">return</span>;
              &#125;
          &#125;
          <span class="hljs-comment">// children has 3 possibilities: text, array or no children.</span>
          <span class="hljs-keyword">if</span> (shapeFlag & <span class="hljs-number">8</span> <span class="hljs-comment">/* TEXT_CHILDREN */</span>) &#123;
              <span class="hljs-comment">// text children fast path</span>
              <span class="hljs-keyword">if</span> (prevShapeFlag & <span class="hljs-number">16</span> <span class="hljs-comment">/* ARRAY_CHILDREN */</span>) &#123;
                  unmountChildren(c1, parentComponent, parentSuspense);
              &#125;
              <span class="hljs-keyword">if</span> (c2 !== c1) &#123;
                  hostSetElementText(container, c2);
              &#125;
          &#125;
          <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-keyword">if</span> (prevShapeFlag & <span class="hljs-number">16</span> <span class="hljs-comment">/* ARRAY_CHILDREN */</span>) &#123;
                  <span class="hljs-comment">// prev children was array</span>
                  <span class="hljs-keyword">if</span> (shapeFlag & <span class="hljs-number">16</span> <span class="hljs-comment">/* ARRAY_CHILDREN */</span>) &#123;
                      <span class="hljs-comment">// two arrays, cannot assume anything, do full diff</span>
                      
                      patchKeyedChildren(c1, c2, container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
                  &#125;
                  <span class="hljs-keyword">else</span> &#123;
                      <span class="hljs-comment">// no new children, just unmount old</span>
                      unmountChildren(c1, parentComponent, parentSuspense, <span class="hljs-literal">true</span>);
                  &#125;
              &#125;
              <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-comment">// prev children was text OR null</span>
                  <span class="hljs-comment">// new children is array OR null</span>
                  <span class="hljs-keyword">if</span> (prevShapeFlag & <span class="hljs-number">8</span> <span class="hljs-comment">/* TEXT_CHILDREN */</span>) &#123;
                      hostSetElementText(container, <span class="hljs-string">''</span>);
                  &#125;
                  <span class="hljs-comment">// mount new if array</span>
                  <span class="hljs-keyword">if</span> (shapeFlag & <span class="hljs-number">16</span> <span class="hljs-comment">/* ARRAY_CHILDREN */</span>) &#123;
                      mountChildren(c2, container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
                  &#125;
              &#125;
          &#125;
      &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看这段源码你就知道：</p>
<ol>
<li>结点有 <code>patchFlag</code>, <code>shapeFlag</code> 两个属性。</li>
<li><code>patchChildren</code> 入参中 n1 为旧结点，并且<code>prevShapeFlag = n1.shapeFlag</code>。</li>
<li>n2 为新结点（旧结点更新后）</li>
<li><code>patchFlag</code>  为快速通道标志，一旦结点上有这个标志且值 > 0 则直接进行 有key的diff处理。</li>
<li>非快速通道 则要进行三种判断：文本结点、子结点、没有子结点。 其中遇见array结点则进行递归处理。</li>
</ol>
<p><strong>我在其中标注了两个地方（源码太多，只展示关键部分）</strong></p>
<ul>
<li>1 - patchKeyedChildren: 处理有key的节点</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
  <span class="hljs-keyword">const</span> patchKeyedChildren = <span class="hljs-function">(<span class="hljs-params">c1<span class="hljs-comment">/*旧的vnode*/</span>, c2<span class="hljs-comment">/*新的vnode*/</span>, container, parentAnchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized</span>) =></span> &#123;
          <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;<span class="hljs-comment">/* 记录索引 */</span>
          <span class="hljs-keyword">const</span> l2 = c2.length; <span class="hljs-comment">/* 新vnode的数量 */</span>
          <span class="hljs-keyword">let</span> e1 = c1.length - <span class="hljs-number">1</span>; <span class="hljs-comment">// prev ending index : 老vnode 最后一个节点的索引 </span>
          <span class="hljs-keyword">let</span> e2 = l2 - <span class="hljs-number">1</span>; <span class="hljs-comment">// next ending index : 新节点最后一个节点的索引</span>
          <span class="hljs-comment">// 1. sync from start</span>
         
          <span class="hljs-keyword">while</span> (i <= e1 && i <= e2) &#123; <span class="hljs-comment">// ### 1. 头头比较，发现不同就跳出</span>
              <span class="hljs-keyword">const</span> n1 = c1[i];
              <span class="hljs-keyword">const</span> n2 = (c2[i] = optimized
                  ? cloneIfMounted(c2[i])
                  : normalizeVNode(c2[i]));
              <span class="hljs-keyword">if</span> (isSameVNodeType(n1, n2)) &#123;
                  patch(n1, n2, container, <span class="hljs-literal">null</span>, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
              &#125;
              <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-keyword">break</span>;
              &#125;
              i++;
          &#125;
          <span class="hljs-comment">// 2. sync from end</span>
         
          <span class="hljs-keyword">while</span> (i <= e1 && i <= e2) &#123; <span class="hljs-comment">// ### 2. 尾尾比较，发现不同就跳出</span>
              <span class="hljs-keyword">const</span> n1 = c1[e1];
              <span class="hljs-keyword">const</span> n2 = (c2[e2] = optimized
                  ? cloneIfMounted(c2[e2])
                  : normalizeVNode(c2[e2]));
              <span class="hljs-keyword">if</span> (isSameVNodeType(n1, n2)) &#123;
                  patch(n1, n2, container, <span class="hljs-literal">null</span>, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
              &#125;
              <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-keyword">break</span>;
              &#125;
              e1--;
              e2--;
          &#125;
          <span class="hljs-comment">// 3. common sequence + mount</span>
        
          <span class="hljs-comment">// 老节点全部patch，还有新节点</span>
          <span class="hljs-keyword">if</span> (i > e1) &#123;  <span class="hljs-comment">// / 新节点大于老节点</span>
              <span class="hljs-keyword">if</span> (i <= e2) &#123; <span class="hljs-comment">// // 并且新节点e2指针还没有走完，表示需要新增节点</span>
                  <span class="hljs-keyword">const</span> nextPos = e2 + <span class="hljs-number">1</span>;
                  <span class="hljs-keyword">const</span> anchor = nextPos < l2 ? c2[nextPos].el : parentAnchor;
                  <span class="hljs-keyword">while</span> (i <= e2) &#123;
                      patch(<span class="hljs-literal">null</span>, (c2[i] = optimized
                          ? cloneIfMounted(c2[i])
                          : normalizeVNode(c2[i])), container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
                      i++;
                  &#125;
              &#125;
          &#125;
          <span class="hljs-comment">// 4. common sequence + unmount</span>
         <span class="hljs-comment">// 新节点全部patch，还有老节点</span>
          <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (i > e2) &#123; <span class="hljs-comment">// 新节点e2指针全部patch完 </span>
              <span class="hljs-keyword">while</span> (i <= e1) &#123; <span class="hljs-comment">// 新节点数小于老节点数，需要卸载节点</span>
                  unmount(c1[i], parentComponent, parentSuspense, <span class="hljs-literal">true</span>);
                  i++;
              &#125;
          &#125;
          
          <span class="hljs-comment">// 5. unknown sequence : 剩余不确定元素</span>
          <span class="hljs-comment">// [i ... e1 + 1]: a b [c d e] f g</span>
          <span class="hljs-comment">// [i ... e2 + 1]: a b [e d c h] f g</span>
          <span class="hljs-comment">// i = 2, e1 = 4, e2 = 5</span>
          <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-keyword">const</span> s1 = i; <span class="hljs-comment">// prev starting index</span>
              <span class="hljs-keyword">const</span> s2 = i; <span class="hljs-comment">// next starting index</span>
              <span class="hljs-comment">// 5.1 build key:index map for newChildren</span>
              <span class="hljs-keyword">const</span> keyToNewIndexMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
              <span class="hljs-keyword">for</span> (i = s2; i <= e2; i++) &#123;
                  <span class="hljs-keyword">const</span> nextChild = (c2[i] = optimized
                      ? cloneIfMounted(c2[i])
                      : normalizeVNode(c2[i]));
                  <span class="hljs-keyword">if</span> (nextChild.key != <span class="hljs-literal">null</span>) &#123;
                      <span class="hljs-keyword">if</span> (keyToNewIndexMap.has(nextChild.key)) &#123;
                          warn(<span class="hljs-string">`Duplicate keys found during update:`</span>, <span class="hljs-built_in">JSON</span>.stringify(nextChild.key), <span class="hljs-string">`Make sure keys are unique.`</span>);
                      &#125;
                      keyToNewIndexMap.set(nextChild.key, i);
                  &#125;
              &#125;
              <span class="hljs-comment">// 5.2 loop through old children left to be patched and try to patch</span>
              <span class="hljs-comment">// matching nodes & remove nodes that are no longer present</span>
              <span class="hljs-comment">// code ....</span>
              
              <span class="hljs-comment">// 5.3 move and mount</span>
              <span class="hljs-comment">// generate longest stable subsequence only when nodes have moved</span>
              <span class="hljs-comment">// code ...</span>
             
          &#125;
      &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>亲，先看看源码当中那些带数字标号的引文注释，都是源码自带的。 看不懂就再看看中文注释，那是我加的。</p>
<p>好吧，如果看到源码就头疼，<strong><code>那我来总结一下这个方法中的数字 5 </code>。</strong></p>
<h5 data-id="heading-4">5.1 build key，记录新的节点</h5>
<p>先看看代码中声明的变量：</p>
<pre><code class="copyable">const s1 = i  // 第一步遍历到的index
const s2 = i 
const keyToNewIndexMap = new Map()   // 把没有比较过的新的vnode节点,通过map保存
for (i = s2; i <= e2; i++) &#123;
  if (nextChild.key != null) &#123;
    keyToNewIndexMap.set(nextChild.key, i)
  &#125;
&#125;

let j // 新指针j
let patched = 0 
const toBePatched = e2 - s2 + 1 // 没有经过 path 的 新的节点的数量
let moved = false               // 是否需要移动
let maxNewIndexSoFar = 0 

const newIndexToOldIndexMap = new Array(toBePatched)
// 建立一个数组，每个子元素都是0 [ 0, 0, 0, 0, 0, 0 ]
for (i = 0; i < toBePatched; i++) newIndexToOldIndexMap[i] = 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>keyToNewIndexMap</code>变量中，我们得到的结果是：（假设节点 e 的key是 e）。</p>
<pre><code class="copyable">keyToNewIndexMap = &#123;"e" => 2, "d" => 3, "c" => 4, "h" => 5&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用新指针 <code>j</code> 来记录剩下的新的节点的索引。</p>
<p><code>newIndexToOldIndexMap</code> 用来存放新节点索引，和旧节点索引。</p>
<h4 data-id="heading-5">5.2 匹配节点，删除不存在的节点</h4>
<pre><code class="copyable">for (i = s1; i <= e1; i++) &#123;   /* 开始遍历老节点 */
  const prevChild = c1[i]      // c1是老节点
  if (patched >= toBePatched) &#123;  
    /* 已经patch数量大于等于剩余节点数量，卸载老的节点 */
    unmount(prevChild, parentComponent, parentSuspense, true)
    continue
  &#125;
  let newIndex   // 目标新节点的索引

  /* 如果,老节点的key存在 ，通过key找到对应的新节点的index */
  if (prevChild.key != null) &#123;
    newIndex = keyToNewIndexMap.get(prevChild.key)
  &#125; else &#123;
    /* 
    如果,老节点的key不存在，遍历剩下的所有新节点
      按我们上面的节点来讲，就是遍历 [e d c h]，代码中s2=2  e2=5，
    */
    for (j = s2; j <= e2; j++) &#123;
      if (
        newIndexToOldIndexMap[j - s2] === 0 &&
        isSameVNodeType(prevChild, c2[j])
      ) &#123;
        /* 如果找到与当前老节点对应的新节点那么 ，将新节点的索引，赋值给newIndex  */
        newIndex = j
        break
      &#125;
    &#125;
  &#125;

  if (newIndex === undefined) &#123;
    /* 没有找到与老节点对应的新节点，删除当前节点 */
    unmount(prevChild, parentComponent, parentSuspense, true)
  &#125; else &#123;
    /* 把老节点的索引，记录在存放新节点的数组中， */
    newIndexToOldIndexMap[newIndex - s2] = i + 1
    if (newIndex >= maxNewIndexSoFar) &#123;
      maxNewIndexSoFar = newIndex
    &#125; else &#123;
      /* 证明有节点已经移动了   */
      moved = true
    &#125;
    /* 找到新的节点进行patch */
    patch(
      prevChild,
      c2[newIndex],
      container,
      null,
      parentComponent,
      parentSuspense,
      isSVG,
      optimized
    )
    patched++   // 记录已经在新节点中找到了了多少个老节点了
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>所以你可以理解为主要执行了2步操作：</strong></p>
<p><strong>Step 1：</strong></p>
<p>通过老节点的key，找到新节点的 index，这里有两种情况：</p>
<ol>
<li>老节点没有key，遍历剩下的所有新节点，尝试找到索引</li>
<li>老节点有key，在<code>keyToNewIndexMap</code>中找到索引</li>
</ol>
<p><strong>Step 2：</strong></p>
<ol>
<li>如果第一步依旧没有找到 Index，则表示没有和新节点对应的老节点，删除当前旧节点。</li>
<li>如果找到了Index，则表示老节点中有对应的节点，赋值新节点索引到<code>newIndex</code>。再把老节点索引，记录到新节点的数组<code>newIndexToOldIndexMap</code>中，这里索引+1，是因为初始值就0，如果直接存放索引，从第一个开始就发生变化那么存入的索引会是0，则会直接被当作没有老节点匹配。</li>
</ol>
<p>解释判断： <code>newIndex >= maxNewIndexSoFar</code></p>
<p>因为遍历老数组是从前往后遍历，那么假如说在遍历的时候，就记录该节点在新节点数组中的位置，假如发生倒转，那么就是 <code>maxNewIndexSoFar > newIndex</code> ， 就代表说新老节点的某节点已经发生了调换，在 <code>diff</code> 过程中肯定会涉及元素的移动。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 举个栗子</span>
<span class="hljs-keyword">if</span> 旧节点 = [a, b, c, f];
<span class="hljs-keyword">if</span> 新节点 = [a, f, b, c];

so

循环遍历旧结点：
when Pointer -> b ，newIndex = <span class="hljs-number">2</span> and maxNewIndexSoFar = <span class="hljs-number">0</span>

when Pointer -> c ，newIndex = <span class="hljs-number">3</span> and maxNewIndexSoFar = <span class="hljs-number">2</span>

when Pointer -> f ，newIndex = <span class="hljs-number">1</span> and maxNewIndexSoFar = <span class="hljs-number">3</span> 

result ->  moved = <span class="hljs-literal">true</span>

<span class="hljs-comment">// 把流程串起来</span>

旧节点： a b [c d e] f g ， c key 存在，d、e 的 key === <span class="hljs-literal">undefined</span>

新节点： a b [e d c h] f g

得到待处理的节点： [e d c h]

按以上逻辑，先遍历 [c d e]。 

when when Pointer -> c, newIndex = <span class="hljs-number">4</span> s2 = <span class="hljs-number">2</span> newIndexToOldIndexMap = [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>,<span class="hljs-number">0</span>].执行 patch

when when Pointer -> d, newIndex = <span class="hljs-literal">undefined</span> ,删除 d
when when Pointer -> e, newIndex = <span class="hljs-literal">undefined</span> ,删除 e
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>多么可怕的事实，如果key不存在，直接删除旧结点。 所以得出结论：写Vue代码，一定要注意要有key ？我自己都差点信了😂</strong></p>
<p><code>提出一个很重要的概念： 最长递增子序列</code></p>
<p>我会给大家写上中文注释的。😊</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 5.3 move and mount</span>
<span class="hljs-comment">// generate longest stable subsequence only when nodes have moved</span>

<span class="hljs-comment">// 移动老节点、创建新节点</span>
<span class="hljs-keyword">const</span> increasingNewIndexSequence = moved
    ? getSequence(newIndexToOldIndexMap)
    : EMPTY_ARR;
<span class="hljs-comment">// // 用于节点移动判断</span>
j = increasingNewIndexSequence.length - <span class="hljs-number">1</span>;
<span class="hljs-comment">// looping backwards so that we can use last patched node as anchor</span>
<span class="hljs-comment">// 向后循环，也就是倒序遍历。 因为插入节点时使用 insertBefore， 即向前插以便我们可以使用最后一个更新的节点作为锚点 </span>
<span class="hljs-keyword">for</span> (i = toBePatched - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
    <span class="hljs-keyword">const</span> nextIndex = s2 + i;
    <span class="hljs-keyword">const</span> nextChild = c2[nextIndex];
    <span class="hljs-keyword">const</span> anchor = nextIndex + <span class="hljs-number">1</span> < l2 ? c2[nextIndex + <span class="hljs-number">1</span>].el : parentAnchor;
    <span class="hljs-keyword">if</span> (newIndexToOldIndexMap[i] === <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 如果仍然是默认值 0， 证明是一个全新的节点</span>
        <span class="hljs-comment">// mount new</span>
        patch(<span class="hljs-literal">null</span>, nextChild, container, anchor, parentComponent, parentSuspense, isSVG, slotScopeIds, optimized);
    &#125;
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (moved) &#123;
        <span class="hljs-comment">// move if:</span>
        <span class="hljs-comment">// There is no stable subsequence (e.g. a reverse)</span>
        <span class="hljs-comment">// OR current node is not among the stable sequence: 当前索引不是最长递增子序列里的值，需要移动</span>
        <span class="hljs-keyword">if</span> (j < <span class="hljs-number">0</span> || i !== increasingNewIndexSequence[j]) &#123;
            move(nextChild, container, anchor, <span class="hljs-number">2</span> <span class="hljs-comment">/* REORDER */</span>);
        &#125;
        <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 是最长递增子序列里的值，则指向下一个</span>
            j--;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2 - patchUnkeyedChildren: 处理有没有key的节点</li>
</ul>
<p>至于没有key的结点咋处理……</p>
<p>辣鸡，非常粗暴，简直无法直视。 自己去看源码。（就是对比新旧结点的length，新的长就直接mount new。 旧的长就先umount old）</p>
<h4 data-id="heading-6">小结一下：</h4>
<ol>
<li>没有key的结点发生变化，直接火葬场吧。</li>
<li>有key的结点发生变化
<ul>
<li>头和头比较一下</li>
<li>尾和尾比较一下</li>
<li>头和尾比较一下</li>
<li>找出最长递增子序列，随时移动，随时创建新结点。</li>
</ul>
</li>
</ol>
<h3 data-id="heading-7">2. 时间切片（Time Slicing）</h3>
<p>Vue3 抛弃了时间切片，这简直令我……。emmmm, 我还能说什么呢，你不卡谁卡。</p>
<p>关于为什么Vue3不使用时间切片（Time Slicing）， 尤雨溪在 <code>Vuejs issue</code> 里面有很详细的回答。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Frfcs%2Fissues%2F89%23issuecomment-546988615" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/rfcs/issues/89#issuecomment-546988615" ref="nofollow noopener noreferrer"> 尤雨溪回答的原文地址</a></p>
<p>好吧。我来翻译一下（我就在想，我不翻译让老铁们直接去看原文会被打吗？）。</p>
<hr>
<p>在web应用程序中，更新内容<code>丢帧（janky）</code>通常是由大量<code>CPU时间</code>+<code>原始DOM更新</code>的同步操作引起的。<strong><code>时间切片</code>是在CPU工作期间保持应用程序响应的一种尝试</strong>，但它只影响CPU工作。但DOM更新的刷新必须仍然是同步的，目的是确保最终DOM状态的一致性。</p>
<p>所以，想象两种丢帧更新的场景：</p>
<p>1.CPU工作时间在16ms以内，但原生DOM的更新操作量很大（例如，mount 大量新的 DOM内容）。无论有没有使用时间切片，该应用程序仍会感觉“僵硬（丢帧）”。</p>
<ol start="2">
<li>CPU任务非常繁重，需要超过16ms的时间。从理论上讲，时间切片开始发挥作用了。然而，HCI的研究表明，除非它在进行动画，否则对于正常的用户交互，大多数人不会感觉到差异，除非更新时间超过100毫秒。</li>
</ol>
<p>也就是说，只有当频繁的更新需要超过100毫秒的纯CPU时间时，时间切片才变得实际有用。</p>
<p>也就是说，只有在频繁进行超过100ms的纯CPU任务更新时，时间切片才实际有用。</p>
<p>有趣的地方在于，这样的场景更经常地发生在React中，因为：</p>
<ul>
<li>
<p>i.  React的虚拟DOM操作（ <code>reconciliation 调度算法</code>  ）天生就比较慢，因为它使用了大量的<code>Fiber架构</code>；</p>
</li>
<li>
<p>ii.  React使用JSX来渲染函数相对较于用模板来渲染更加难以优化，模板更易于静态分析。</p>
</li>
<li>
<p>iii.  React Hooks将大部分组件树级优化（即防止不必要的子组件的重新渲染）留给了开发人员，开发人员在大多数情况下需要显式地使用<code>useMemo</code>。而且，不管什么时候React接收到了<code>children</code>属性，它几乎总要重新渲染，因为每次的子组件都是一棵新的vdom树。这意味着，一个使用Hook的React应用在默认配置下会过度渲染。更糟糕的是，像<code>useMomo</code>这类优化不能轻易地自动应用，因为：</p>
<ol>
<li>它需要正确的deps数组；</li>
<li>盲目地任意使用它可能会阻塞本该进行的更新，类似与<code>PureComponent</code>。</li>
</ol>
<p><strong>不幸的是，大多数开发人员都很懒，不会积极地优化他们的应用。所以大多数使用Hook的React应用会做很多不必要的CPU工作。</strong></p>
</li>
</ul>
<p>相比之下，Vue就上面的问题做一下比较：</p>
<ol>
<li>
<p>本质上更简单，因此虚拟DOM操作更快（ <code>no时间切片-> no</code>fiber<code>-> 更低开销</code>）；</p>
</li>
<li>
<p>通过分析模板进行了大量的AOT优化，减少了虚拟DOM操作的基本开销。Benchmark显示，<strong>对于一个典型的DOM代码块来说，动态与静态内容的比例大约是1:4，Vue3的原生执行速度甚至比Svelte更快，在CPU上花费的时间不到React的1/10。</strong></p>
</li>
<li>
<p>智能组件树级优化通过响应式跟踪，将插槽编译成函数（避免子元素重复渲染）和自动缓存内联句柄（避免内联函数重复渲染）。除非必要，否则子组件永远不需要重新渲染。这一切不需要开发人员进行任何手动优化。</p>
<p>这意味着对于同一个更新，React应用可能造成多个组件重新渲染，但在Vue中大部分情况下只会导致一个组件重新渲染。</p>
</li>
</ol>
<p><strong><code>默认情况下</code>，</strong> Vue3应用比React应用花费更少的CPU工作时间， 并且CPU工作时间超过100ms的机会大幅度减少了，除非在一些极端的情况下，DOM可能成为更主要的瓶颈。</p>
<p>现在，时间切片或并发模式带来了另一个问题：因为框架现在安排和协调了所有更新，它在优先级、失效、重新实例化等方面产生了大量额外的复杂性。所有这些逻辑处理都不可能被<code>tree-shaken</code>，这将导致运行时所占CPU内存的大小膨胀。即使包含了<code>Suspense</code>和所有的<code>tree-shaken</code>，Vue 3的运行时仍然只有当前React + React DOM的1/4大小。</p>
<p>注意，这并不是说并发模式作为一个整体是一个坏主意。它确实提供了处理某类问题的有趣的新方法（特别是与协调异步状态转换相关的），但时间切片（作为并发的一个子功能）专门解决了React中比其他框架中更突出的问题，同时也产生了自己的成本。对于Vue 3来说，这种权衡似乎并不值得。</p>
<hr>
<p>如果你也是个老react玩家，想必你会不服气。 尤雨溪的回复当中看上去好像指出了 react 的一些弊端和短板。恰有一种踩低别人抬高自己的节奏。</p>
<p>尤雨溪指出：</p>
<ol>
<li>React + React DOM 在运行中所占CPU内存要高于Vue运行时所占内存，比例已经高达 <code>4:1</code></li>
<li>React Hooks 不好用，即使用好了<code>useMemo 、 memo</code> 也还得保证 deps 的正确性。</li>
<li>React的操作虚拟DOM，其实就是指 <code>React</code> 的调度算法比较慢。而 <code>Vue</code> 通过分析模板进行了大量的 <code>AOT优化</code>，减少了虚拟DOM操作的基本开销。<strong><code>所以Vue的操作虚拟 DOM 要比 React 快。</code></strong></li>
<li>并发模式不是坏死，但时间切片就不一定了，至少React 的时间切片作法就不咋地。</li>
</ol>
<p>作为一个过来人，深知React的一些缺点。 我们换个角度来看待1-4点。</p>
<ol>
<li>
<p>老实讲，谁跑得快得分时间。 如果React 需要4个小时，Vue需要1个小时，请问你觉得谁快？ 但React 跑400ms，Vue跑100ms，请问你觉得谁快？换句话说，针对此问题，真的很有必要吗？前端性能瓶颈如何优化？React好做还是Vue好做？</p>
</li>
<li>
<p>React Hooks 用起来很好用，但能用好确实不容易。但如果我用好了，这个问题还存在吗？</p>
</li>
<li>
<p>React 调度算法慢，Vue就相比较下快，那就得分两个方面来</p>
<ul>
<li>React 可以通过 实操写代码来控制快慢，例如每次操作尽可能少的VDOM。 Vue的AOT优化可以让开发人员去做吗？很明显，Vue 不可以。</li>
<li>React 真的慢吗？ 或者说在操作大量DOM的场景下，Vue 真的优于 React 吗？</li>
</ul>
</li>
<li>
<p>稍微解释一下所谓的 <code>React 时间切片做法</code>。 React 会将Fiber 字任务交给浏览器的空闲时间去完成，这个过程可以随时被中断，中断以后下次还能接着上一次的位置继续执行任务。</p>
<ul>
<li>“时间切片” 在react中的应用远不是为快不快的问题而存在的，而是为了可恢复性。例如用户在做负责的交互行为，或者页面要做复杂动画的时候，如果React加强了自身消耗却保证了交互、动画的流畅性，你觉得值吗？</li>
</ul>
</li>
</ol>
<h4 data-id="heading-8">小结一下</h4>
<p>其实，现在市场上关于React 和 Vue 有很多激烈的讨论，都是由于自身的优缺点而产生的。</p>
<p>例如网络上很多人在互相攻击：</p>
<p>“ Vue 只适合小项目，大项目扛不起来”</p>
<p>”React 无数个回调，无数个选择表达式，this绑定…乱！“</p>
<p>“Vue好上手，岗位多”</p>
<p>“大厂基本都用 React，不用 Vue ”</p>
<p>那如果从使用层面上来考虑的话，emmm，列个框吧。</p>













































<table><thead><tr><th>问题</th><th>Vue</th><th>React</th></tr></thead><tbody><tr><td>this混乱</td><td>源码实现已经处理好了this，不需要你额外处理</td><td>React Hooks 已经不存在this这个东西了。</td></tr><tr><td>上手</td><td>easy</td><td>normal</td></tr><tr><td>用好</td><td>normal</td><td>hard</td></tr><tr><td>新手友好</td><td>极度友好</td><td>不友好</td></tr><tr><td>可扩展性</td><td>一般</td><td>强</td></tr><tr><td>底层实现</td><td>硬核，能做的都做得挺好</td><td>硬核，但内容更多</td></tr><tr><td>hook</td><td>细讲</td><td>细讲</td></tr></tbody></table>
<h3 data-id="heading-9">3. Vue3 & React17 比较</h3>
<p>Vue 3.0 Beta 版本刚发布的时候，大家吵得很凶。印象深刻的有两点吐槽。</p>
<ul>
<li>吐槽意大利面代码结构
<ul>
<li>杂七杂八一堆丢在 <code>setup</code> 里，我还不如直接用 react</li>
<li>代码结构不清晰，语义不明确，这操作无异于把 vue 自身优点都扔了</li>
<li>结构不清晰，担心代码量一上去不好维护</li>
</ul>
</li>
<li>抄袭 React
<ul>
<li><code>Vue-Composition-Api</code>的主要灵感来源是 <code>React Hooks</code> 的创造力（这也是吐槽最狠的地方）</li>
</ul>
</li>
</ul>
<p><strong>其实真的用过并且懂 React hooks 的人看到这个都会意识到 <code>Vue Composition API （VCA）</code>跟 <code>hooks</code> 本质上的区别。<code>VCA</code> 在实现上也其实只是把 Vue 本身就有的响应式系统更显式地暴露出来而已。真要说像的话，<code>VCA</code> 跟 <code>MobX</code> 还更像一点。</strong></p>
<p>（这里我为Vue洗冤屈了，这说明我还是很可观的。毕竟是研究过Vue源码后的发言）</p>
<p>举一个 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-cli%2Fblob%2Fa09407dd5b9f18ace7501ddb603b95e31d6d93c0%2Fpackages%2F%40vue%2Fcli-ui%2Fsrc%2Fcomponents%2Ffolder%2FFolderExplorer.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-cli/blob/a09407dd5b9f18ace7501ddb603b95e31d6d93c0/packages/@vue/cli-ui/src/components/folder/FolderExplorer.vue" ref="nofollow noopener noreferrer">Vue CLI UI file explorer</a></strong> 官方吐槽的例子，这个组件是 Vue-CLI 的 gui 中（也就是平常我们命令行里输入 <code>vue ui</code> 出来的那个图形化控制台）的一个复杂的文件浏览器组件，这是 Vue 官方团队的大佬写的，相信是比较有说服力的一个案例了。</p>
<p>自看去github上看，我这就不贴代码了，深夜凌晨1点了都。</p>
<p>然后，看官方给的图你也明白了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ff2d18d93049d4abf24abb14f6060c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>图左边是原始风格，右边是 <code>hook</code> 风格。</strong></p>
<p>其中一个 hook 风格的方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCreateFolder</span>(<span class="hljs-params">openFolder</span>) </span>&#123;
  <span class="hljs-comment">// originally data properties</span>
  <span class="hljs-keyword">const</span> showNewFolder = ref(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">const</span> newFolderName = ref(<span class="hljs-string">""</span>);

  <span class="hljs-comment">// originally computed property</span>
  <span class="hljs-keyword">const</span> newFolderValid = computed(<span class="hljs-function">() =></span> isValidMultiName(newFolderName.value));

  <span class="hljs-comment">// originally a method</span>
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createFolder</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!newFolderValid.value) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> mutate(&#123;
      <span class="hljs-attr">mutation</span>: FOLDER_CREATE,
      <span class="hljs-attr">variables</span>: &#123;
        <span class="hljs-attr">name</span>: newFolderName.value,
      &#125;,
    &#125;);
    openFolder(result.data.folderCreate.path);
    newFolderName.value = <span class="hljs-string">""</span>;
    showNewFolder.value = <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    showNewFolder,
    newFolderName,
    newFolderValid,
    createFolder,
  &#125;;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看一下Vue Hook风格下的一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;,
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCreateFolder</span>(<span class="hljs-params">openFolder</span>)</span>&#123;
<span class="hljs-comment">// ...</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCurrentFolderData</span>(<span class="hljs-params">networkState</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useFolderNavigation</span>(<span class="hljs-params">&#123; networkState, currentFolderData &#125;</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useFavoriteFolder</span>(<span class="hljs-params">currentFolderData</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useHiddenFolders</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCreateFolder</span>(<span class="hljs-params">openFolder</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看看现在的 <code>setup</code> 函数。</p>
<pre><code class="copyable">export default &#123;
  setup() &#123;
    // Network
    const &#123; networkState &#125; = useNetworkState();

    // Folder
    const &#123; folders, currentFolderData &#125; = useCurrentFolderData(networkState);
    const folderNavigation = useFolderNavigation(&#123; networkState, currentFolderData &#125;);
    const &#123; favoriteFolders, toggleFavorite &#125; = useFavoriteFolders(currentFolderData);
    const &#123; showHiddenFolders &#125; = useHiddenFolders();
    const createFolder = useCreateFolder(folderNavigation.openFolder);

    // Current working directory
    resetCwdOnLeave();
    const &#123; updateOnCwdChanged &#125; = useCwdUtils();

    // Utils
    const &#123; slicePath &#125; = usePathUtils();

    return &#123;
      networkState,
      folders,
      currentFolderData,
      folderNavigation,
      favoriteFolders,
      toggleFavorite,
      showHiddenFolders,
      createFolder,
      updateOnCwdChanged,
      slicePath,
    &#125;;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>🐂🍺了，干净不？</code></p>
<h4 data-id="heading-10">对比一下hook原理吧。</h4>
<p>还是举个栗子。</p>
<pre><code class="hljs language-js copyable" lang="js">
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span> Add By 1 <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)

        <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> count.value++

        effect(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">active</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count changed!'</span>, count.value)
        &#125;)

        <span class="hljs-keyword">return</span> &#123; count, add &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非常简单的一个栗子。</p>
<ol>
<li>setup只执行一次，</li>
<li>如果需要在 <code>count</code> 发生变化的时候做某件事，我们只需要引入 <code>effect</code> 函数。</li>
<li>这个 <code>active</code> 函数只会产生一次，这个函数在读取 <code>count.value</code> 的时候会收集它作为依赖，那么下次 <code>count.value</code> 更新后，自然而然的就能触发 <code>active</code> 函数重新执行了。</li>
</ol>
<p>总结一下： hook 初始化一次，后用无穷。</p>
<p>再来看个栗子。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [name, setName] = useState(<span class="hljs-string">'渣男'</span>);
  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> setCount(<span class="hljs-function">(<span class="hljs-params">prev</span>) =></span> prev + <span class="hljs-number">1</span>);

  useEffect(<span class="hljs-function">()=></span>&#123;
      setName(<span class="hljs-string">`渣男渣了<span class="hljs-subst">$&#123;count&#125;</span>次`</span>)
  &#125;,[count])

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;add&#125;</span>></span> +1 <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看得出，功能一样，但这是个React 组件。通过引用 <code><Counter /></code> 这种方式引入的，我们知道JSX就是js，Babel 实际上会把它编译成 <code>React.createElement(Counter)</code> 这样的函数执行。</p>
<p><strong>也就是说每次渲染，这个函数都会被完整的执行一次。</strong></p>
<p><code>useState</code> 返回的 <code>count</code> 和 <code>setCount</code> 则会被保存在组件对应的 <code>Fiber</code> 节点上，并且每个 React 函数每次执行 Hook 的顺序必须是相同的。</p>
<p>React Hooks里的钩子函数都是可以被多次调用的，这也是目前我觉得React 对开发者最为友好的一个个创意。我可以充分利用这些钩子函数去最大程度颗粒化我的逻辑，达到高度复用且互不影响。</p>
<p>上述有说到 deps 依赖的弊端。 React Hooks 很多钩子都是需要依赖于状态变量的。 简单点说就是所依赖的状态变量发生了改变，那就可以执行相应的操作。听起来很美好对伐？ 但一个搞不好就是闭包陷进…… 你用的好，就牛。用不好你就是辣鸡。</p>
<p>所以如果你是函数式编程风格的死忠粉，React Hooks绝对是你的最爱。</p>
<p>另外，忽然想到网络上一句话：<strong><code> Vue 给你持久，React给你自由。</code></strong></p>
<p>所以，技术调研的时候，考虑清楚你的场景。其它真没啥，代码总是人写的，Vue再好用也能写成si，React 再难用，写好了也能上天。</p>
<p>凌晨1:26分了，技术文章是写起来就没边了，因为能讲的真的很多很多……  关于React源码解毒，可以看看过往文章。关于Vue 剩下源码，其实真的不多，相比之下Vue的源码真的少太多了，注释还丰富（比较国人写英文更容易看懂些）。所以，有机会再补上吧。</p>
<h3 data-id="heading-11">end</h3></div>  
</div>
            