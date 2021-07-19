
---
title: 'react+vue2+vue3 diff算法分析及比较'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e7f0737d30f4404901d03e6e93b0634~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:45:19 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e7f0737d30f4404901d03e6e93b0634~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>此文内容包括以下：</p>
<p><strong>介绍diff算法</strong></p>
<ol>
<li>react-diff: 递增法</li>
</ol>
<p>移动节点：移动的节点称为α，将α对应的真实的DOM节点移动到，α在<code>新列表中的前一个VNode对应的真实DOM的后面</code></p>
<p>添加节点：在<strong>新列表</strong>中有全新的<code>VNode</code>节点，在<strong>旧列表</strong>中找不到的节点需要添加（通过find这个布尔值来查找）</p>
<p>移除节点：当旧的节点不在<strong>新列表</strong>中时，我们就将其对应的DOM节点移除（通过key来查找确定是否删除）</p>
<p>不足：从头到尾单边比较，容易增加比较次数</p>
<ol start="2">
<li>vue2-diff: 双端比较</li>
</ol>
<p>DOM节点什么时候需要移动和如何移动，总结如下：</p>
<ul>
<li>头-头：不移动</li>
<li>尾-尾：不移动</li>
<li>头-尾: 插入到旧节点的尾节点的后面</li>
<li>尾-头：插入到旧列表的第一个节点之前</li>
<li>以上4种都不存在（特殊情况）：在旧节点中找，如果找到，移动找到的节点，移动到开头；没找到，直接创建一个新的节点放到最前面</li>
</ul>
<p>添加节点【<code>oldEndIndex</code>以及小于了<code>oldStartIndex</code>】：将剩余的节点依次插入到<code>oldStartNode</code>的<code>DOM</code>之前</p>
<p>移除节点【<code>newEndIndex</code>小于<code>newStartIndex</code>】：将<strong>旧列表</strong>剩余的节点删除即可</p>
<ol start="3">
<li>vue3-diff： 最长递增子序列</li>
</ol>
<p><strong>区别</strong></p>
<ol>
<li>react和vue2的比较：</li>
</ol>
<ul>
<li>vue2双端比较解决react单端比较导致移动次数变多的问题，react只能从头到尾遍历，增加了移动次数</li>
</ul>
<ol start="2">
<li>
<p>vue2和vue3的比较：都用了双端指针</p>
</li>
<li>
<p>vue3和react比较：vue3在判断是否需要移动，使用了react的递增法</p>
</li>
</ol>
<p>几个算法看下来，套路就是找到移动的节点，然后给他移动到正确的位置。把该加的新节点添加好，把该删的旧节点删了，整个算法就结束了。</p>
<h1 data-id="heading-0">一、react-diff —— 递增法</h1>
<h3 data-id="heading-1">实现原理</h3>
<p><code>从头到尾</code>遍历比较，新列表的节点在旧列表中的位置是否是递增
如果递增，不需要移动，否则需要移动。</p>
<p>通过key在旧节点中找到新节点的节点，所以key一定要代表唯一性。</p>
<h3 data-id="heading-2">移动节点：在旧节点中找到需要移动的VNode，我们称该VNode为α</h3>
<blockquote>
<p>生成的<code>DOM</code>节点插入到哪里？</p>
</blockquote>
<p>将α对应的真实的DOM节点移动到，α在<code>新列表中的前一个VNode对应的真实DOM的后面</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e7f0737d30f4404901d03e6e93b0634~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将DOM-B移到DOM-D的后面</p>
<p>为什么这么移动？</p>
<p>首先我们列表是<code>从头到尾</code>遍历的。这就意味着对于当前<code>VNode</code>节点来说，该节点之前的所有节点都是排好序的，如果该节点需要移动，那么只需要将DOM节点移动到前一个<code>vnode</code>节点之后就可以，因为在<strong>新列表</strong>中<code>vnode</code>的顺序就是这样的。</p>
<h3 data-id="heading-3">添加节点：在<strong>新列表</strong>中有全新的<code>VNode</code>节点，在<strong>旧列表</strong>中找不到的节点需要添加</h3>
<blockquote>
<p>如何发现全新的节点？</p>
</blockquote>
<p>定义一个<code>find</code>变量值为<code>false</code>。如果在<strong>旧列表</strong>找到了<code>key</code> 相同的<code>vnode</code>，就将<code>find</code>的值改为<code>true</code>。当遍历结束后判断<code>find</code>值，如果为<code>false</code>，说明当前节点为新节点</p>
<blockquote>
<p>生成的<code>DOM</code>节点插入到哪里？</p>
</blockquote>
<p>分两种情况：</p>
<ul>
<li>
<ol>
<li>新的节点位于<strong>新列表</strong>的第一个，这时候我们需要找到<strong>旧列表</strong>第一个节点，将新节点插入到原来第一个节点之前，这个很好理解，也就是最在最前面的新节点插入第一个节点之前。</li>
</ol>
</li>
<li>
<ol start="2">
<li>将新的真实的DOM节点移动到，<code>新列表中的前一个VNode对应的真实DOM的后面</code>。移动原理同移动节点，也就是因为该节点之前已经排好序。</li>
</ol>
</li>
</ul>
<h3 data-id="heading-4">删除节点：当旧的节点不在<strong>新列表</strong>中时，我们就将其对应的DOM节点移除</h3>
<h3 data-id="heading-5">实现代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactDiff</span>(<span class="hljs-params">prevChildren, nextChildren, parent</span>) </span>&#123;
    <span class="hljs-keyword">let</span> lastIndex = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nextChildren.length; i++) &#123;
        <span class="hljs-keyword">let</span> nextChild = nextChildren[i],
            find = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < prevChildren.length; j++) &#123;
            <span class="hljs-keyword">let</span> prevChild = prevChildren[j]
            <span class="hljs-keyword">if</span> (nextChild.key === prevChild.key) &#123;
                find = <span class="hljs-literal">true</span>
                patch(prevChild, nextChild, parent)
                <span class="hljs-keyword">if</span> (j < lastIndex) &#123;
                    <span class="hljs-comment">// 移动节点：移动到前一个节点的后面</span>
                    <span class="hljs-keyword">let</span> refNode = nextChildren[i - <span class="hljs-number">1</span>].el.nextSibling;
                    parent.insertBefore(nextChild.el, refNode)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-comment">// 不需要移动节点，记录当前位置，与之后的节点进行对比</span>
                    lastIndex = j
                &#125;
                <span class="hljs-keyword">break</span>
            &#125;
        &#125;
        <span class="hljs-keyword">if</span> (!find) &#123;
            <span class="hljs-comment">// 定义了find变量，插入新节点</span>
            <span class="hljs-keyword">let</span> refNode = i <= <span class="hljs-number">0</span>
                            ? prevChildren[<span class="hljs-number">0</span>].el
                            : nextChildren[i - <span class="hljs-number">1</span>].el.nextSibling
            mount(nextChild, parent, refNode);
        &#125;
    &#125;
    <span class="hljs-comment">//移除节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prevChildren.length; i++) &#123;
        <span class="hljs-keyword">let</span> prevChild = prevChildren[i],
            key = prevChild.key,
            has = nextChildren.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.key === key);
        <span class="hljs-keyword">if</span> (!has) parent.removeChild(prevChild.el)
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">算法优化及不足</h3>
<ol>
<li>时间复杂度是<code>O(m*n)</code>，有不足，可优化</li>
</ol>
<p>我们可以用空间换时间，把<code>key</code>与<code>index</code>的关系维护成一个<code>Map</code>，从而将时间复杂度降低为<code>O(n)</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactdiff</span>(<span class="hljs-params">prevChildren, nextChildren, parent</span>) </span>&#123;
  <span class="hljs-keyword">let</span> prevIndexMap = &#123;&#125;,
    nextIndexMap = &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prevChildren.length; i++) &#123;
    <span class="hljs-keyword">let</span> &#123; key &#125; = prevChildren[i]
    <span class="hljs-comment">//保存旧列表key和指引i的关系</span>
    prevIndexMap[key] = i
  &#125;
  <span class="hljs-keyword">let</span> lastIndex = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nextChildren.length; i++) &#123;
    <span class="hljs-keyword">let</span> nextChild = nextChildren[i],
      nextKey = nextChild.key,
      <span class="hljs-comment">// 通过新列表的key得到旧列表的指引</span>
      j = prevIndexMap[nextKey];

    <span class="hljs-comment">//保存新列表key和指引i的关系</span>
    nextIndexMap[nextKey] = i
    
    <span class="hljs-keyword">if</span> (j === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-comment">//添加节点</span>
      <span class="hljs-keyword">let</span> refNode = i === <span class="hljs-number">0</span>
                    ? prevChildren[<span class="hljs-number">0</span>].el
                    : nextChildren[i - <span class="hljs-number">1</span>].el.nextSibling;
      mount(nextChild, parent, refNode)
    &#125; <span class="hljs-keyword">else</span> &#123;
      patch(prevChildren[j], nextChild, parent)
      <span class="hljs-keyword">if</span> (j < lastIndex) &#123;
      <span class="hljs-comment">//移动节点：移动到前一个节点的后面</span>
        <span class="hljs-keyword">let</span> refNode = nextChildren[i - <span class="hljs-number">1</span>].el.nextSibling;
        parent.insertBefore(nextChild.el, refNode)
      &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-comment">// 不需要移动节点，记录当前位置，与之后的节点进行对比</span>
        lastIndex = j
      &#125;
    &#125;
  &#125;

<span class="hljs-comment">//删除节点</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prevChildren.length; i++) &#123;
    <span class="hljs-keyword">let</span> &#123; key &#125; = prevChildren[i]
    <span class="hljs-keyword">if</span> (!nextIndexMap.hasOwnProperty(key)) parent.removeChild(prevChildren[i].el)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>移动次数有不足</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b5f30b8b0594e1b904396fb73df6a64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据<code>reactDiff</code>的思路，我们需要先将<code>DOM-A</code>移动到<code>DOM-C</code>之后，然后再将<code>DOM-B</code>移动到<code>DOM-A</code>之后，完成<code>Diff</code>。但是我们通过观察可以发现，只要将<code>DOM-C</code>移动到<code>DOM-A</code>之前就可以完成<code>Diff</code>。</p>
<p>这是因为react只能从头到尾遍历，增加了移动次数。所以这里是有可优化的空间的，接下来我们介绍<code>vue2.x</code>中的<code>diff</code>算法——<code>双端比较</code>，该算法解决了上述的问题</p>
<h1 data-id="heading-7">vue2-diff —— 双端比较</h1>
<h3 data-id="heading-8">实现原理</h3>
<p><code>双端比较</code>就是<strong>新列表</strong>和<strong>旧列表</strong>两个列表的头与尾互相对比，，在对比的过程中指针会逐渐向内靠拢，直到某一个列表的节点全部遍历过，对比停止。</p>
<p>按照以下四个步骤进行对比</p>
<ol>
<li>使用<strong>旧列表</strong>的头一个节点<code>oldStartNode</code>与<strong>新列表</strong>的头一个节点<code>newStartNode</code>对比</li>
<li>使用<strong>旧列表</strong>的最后一个节点<code>oldEndNode</code>与<strong>新列表</strong>的最后一个节点<code>newEndNode</code>对比</li>
<li>使用<strong>旧列表</strong>的头一个节点<code>oldStartNode</code>与<strong>新列表</strong>的最后一个节点<code>newEndNode</code>对比</li>
<li>使用<strong>旧列表</strong>的最后一个节点<code>oldEndNode</code>与<strong>新列表</strong>的头一个节点<code>newStartNode</code>对比</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7ee668a462a4fcfaed0d3e11eaea211~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><code>通过图形记住1-4的比较顺序，先前后双竖再首尾两交叉，记住这张图就够了</code></strong></p>
<p><strong><code>具体规则和移动规则，这里是重中之重，一定要学习</code></strong></p>
<ol>
<li>当<strong>旧列表</strong>的头一个节点<code>oldStartNode</code>与<strong>新列表</strong>的头一个节点<code>newStartNode</code>对比时<code>key</code>相同。那么<strong>旧列表</strong>的头指针<code>oldStartIndex</code>与<strong>新列表</strong>的头指针<code>newStartIndex</code>同时向<strong>后</strong>移动一位。</li>
</ol>
<blockquote>
<p>原本在旧列表中就是头节点，在新列表中也是头节点，<code>该节点不需要移动</code>，所以什么都不需要做</p>
</blockquote>
<ol start="2">
<li>当<strong>旧列表</strong>的最后一个节点<code>oldEndNode</code>与<strong>新列表</strong>的最后一个节点<code>newEndNode</code>对比时<code>key</code>相同。那么<strong>旧列表</strong>的尾指针<code>oldEndIndex</code>与<strong>新列表</strong>的尾指针<code>newEndIndex</code>同时向<strong>前</strong>移动一位。</li>
</ol>
<blockquote>
<p>原本在旧列表中就是尾节点，在新列表中也是尾节点，说明<code>该节点不需要移动</code>，所以什么都不需要做</p>
</blockquote>
<ol start="3">
<li>当<strong>旧列表</strong>的头一个节点<code>oldStartNode</code>与<strong>新列表</strong>的最后一个节点<code>newEndNode</code>对比时<code>key</code>相同。那么<strong>旧列表</strong>的头指针<code>oldStartIndex</code>向<strong>后</strong>移动一位；<strong>新列表</strong>的尾指针<code>newEndIndex</code>向<strong>前</strong>移动一位。</li>
</ol>
<blockquote>
<p>原本旧列表中是头节点，然后在新列表中是尾节点。那么<code>只要在旧列表中把当前的节点移动到原本尾节点的后面</code>，就可以了</p>
</blockquote>
<ol start="4">
<li>当<strong>旧列表</strong>的最后一个节点<code>oldEndNode</code>与<strong>新列表</strong>的头一个节点<code>newStartNode</code>对比时<code>key</code>相同。那么<strong>旧列表</strong>的尾指针<code>oldEndIndex</code>向<strong>前</strong>移动一位；<strong>新列表</strong>的头指针<code>newStartIndex</code>向<strong>后</strong>移动一位。</li>
</ol>
<blockquote>
<p>本在旧列表末尾的节点，却是新列表中的开头节点，没有人比他更靠前，因为他是第一个，所以<code>只需要把当前的节点移动到原本旧列表中的第一个节点之前，让它成为第一个节点</code>即可。</p>
</blockquote>
<p>DOM节点什么时候需要移动和如何移动，总结如下：</p>
<ul>
<li>头-头：不移动</li>
<li>尾-尾：不移动</li>
<li>头-尾: 插入到旧节点的尾节点的后面</li>
<li>尾-头：插入到旧列表的第一个节点之前</li>
</ul>
<p>当然也有特殊情况，下面继续</p>
<h3 data-id="heading-9">当四次对比都<strong>没找到</strong>复用节点</h3>
<p>我们只能拿<strong>新列表</strong>的第一个节点去<strong>旧列表</strong>中找与其<code>key</code>相同的节点</p>
<p>找节点的时候有两种情况：</p>
<ol>
<li>一种在<strong>旧列表</strong>中找到了</li>
</ol>
<p><code>移动找到的节点，移动到开头</code></p>
<p>DOM移动后，由我们将<strong>旧列表</strong>中的节点改为<code>undefined</code>，这是<strong>至关重要</strong>的一步，因为我们已经做了节点的移动了所以我们不需要进行再次的对比了。最后我们将头指针<code>newStartIndex</code>向后移一位。</p>
<ol start="2">
<li>另一种情况是没找到</li>
</ol>
<p>直接创建一个新的节点放到最前面就可以了，然后后移头指针<code>newStartIndex</code>。</p>
<h3 data-id="heading-10">添加节点</h3>
<p><code>oldEndIndex</code>小于了<code>oldStartIndex</code>，但是<strong>新列表</strong>中还有剩余的节点，我们只需要将剩余的节点依次插入到<code>oldStartNode</code>的<code>DOM</code>之前就可以了。为什么是插入<code>oldStartNode</code>之前呢？原因是剩余的节点在<strong>新列表</strong>的位置是位于<code>oldStartNode</code>之前的，如果剩余节点是在<code>oldStartNode</code>之后，<code>oldStartNode</code>就会先行对比，这个需要思考一下，其实还是与<code>第四步</code>的思路一样。</p>
<h3 data-id="heading-11">移除节点</h3>
<p>当<strong>新列表</strong>的<code>newEndIndex</code>小于<code>newStartIndex</code>时，我们将<strong>旧列表</strong>剩余的节点删除即可。这里我们需要注意，<strong>旧列表</strong>的<code>undefind</code>。前面提到过，当头尾节点都不相同时，我们会去<strong>旧列表</strong>中找<strong>新列表</strong>的第一个节点，移动完DOM节点后，将<strong>旧列表</strong>的那个节点改为<code>undefind</code>。所以我们在最后的删除时，需要注意这些<code>undefind</code>，遇到的话跳过当前循环即可。</p>
<h3 data-id="heading-12">实现代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vue2diff</span>(<span class="hljs-params">prevChildren, nextChildren, parent</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldStartIndex = <span class="hljs-number">0</span>,
    newStartIndex = <span class="hljs-number">0</span>,
    oldStartIndex = prevChildren.length - <span class="hljs-number">1</span>,
    newStartIndex = nextChildren.length - <span class="hljs-number">1</span>,
    oldStartNode = prevChildren[oldStartIndex],
    oldEndNode = prevChildren[oldStartIndex],
    newStartNode = nextChildren[newStartIndex],
    newEndNode = nextChildren[newStartIndex];
    <span class="hljs-comment">//循环结束条件</span>
  <span class="hljs-keyword">while</span> (oldStartIndex <= oldStartIndex && newStartIndex <= newStartIndex) &#123;
    <span class="hljs-keyword">if</span> (oldStartNode === <span class="hljs-literal">undefined</span>) &#123;
      oldStartNode = prevChildren[++oldStartIndex]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndNode === <span class="hljs-literal">undefined</span>) &#123;
      oldEndNode = prevChildren[--oldStartIndex]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldStartNode.key === newStartNode.key) &#123;
    <span class="hljs-comment">// 头-头：不移动</span>
      patch(oldStartNode, newStartNode, parent)

      oldStartIndex++
      newStartIndex++
      oldStartNode = prevChildren[oldStartIndex]
      newStartNode = nextChildren[newStartIndex]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndNode.key === newEndNode.key) &#123;
      <span class="hljs-comment">// 尾-尾：不移动</span>
      patch(oldEndNode, newEndNode, parent)

      oldStartIndex--
      newStartIndex--
      oldEndNode = prevChildren[oldStartIndex]
      newEndNode = nextChildren[newStartIndex]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldStartNode.key === newEndNode.key) &#123;
    <span class="hljs-comment">// 头-尾: 插入到旧节点的尾节点的后面</span>
      patch(oldStartNode, newEndNode, parent)
      parent.insertBefore(oldStartNode.el, oldEndNode.el.nextSibling)
      oldStartIndex++
      newStartIndex--
      oldStartNode = prevChildren[oldStartIndex]
      newEndNode = nextChildren[newStartIndex]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndNode.key === newStartNode.key) &#123;
    <span class="hljs-comment">// 尾-头：插入到旧列表的第一个节点之前</span>
      patch(oldEndNode, newStartNode, parent)
      parent.insertBefore(oldEndNode.el, oldStartNode.el)
      oldStartIndex--
      newStartIndex++
      oldEndNode = prevChildren[oldStartIndex]
      newStartNode = nextChildren[newStartIndex]
    &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//特殊情况</span>
      <span class="hljs-keyword">let</span> newKey = newStartNode.key,
        oldIndex = prevChildren.findIndex(<span class="hljs-function"><span class="hljs-params">child</span> =></span> child && (child.key === newKey));
      <span class="hljs-keyword">if</span> (oldIndex === -<span class="hljs-number">1</span>) &#123;
        mount(newStartNode, parent, oldStartNode.el)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">let</span> prevNode = prevChildren[oldIndex]
        patch(prevNode, newStartNode, parent)
        parent.insertBefore(prevNode.el, oldStartNode.el)
        prevChildren[oldIndex] = <span class="hljs-literal">undefined</span>
      &#125;
      newStartIndex++
      newStartNode = nextChildren[newStartIndex]
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (newStartIndex > newStartIndex) &#123;
    <span class="hljs-keyword">while</span> (oldStartIndex <= oldStartIndex) &#123;
      <span class="hljs-keyword">if</span> (!prevChildren[oldStartIndex]) &#123;
        oldStartIndex++
        <span class="hljs-keyword">continue</span>
      &#125;
      parent.removeChild(prevChildren[oldStartIndex++].el)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldStartIndex > oldStartIndex) &#123;
    <span class="hljs-keyword">while</span> (newStartIndex <= newStartIndex) &#123;
      mount(nextChildren[newStartIndex++], parent, oldStartNode.el)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">vue3-diff —— 最长递增子序列</h1>
<p>双端比较，while循环，两端是向内靠拢的
头-头<br>
尾-尾</p>
<p>j是头向内靠拢指针；<br>
prevEnd是尾向内靠拢指针</p>
<h3 data-id="heading-14">添加节点：<code>j > prevEnd</code>且<code>j <= nextEnd</code>【证明新列表有多余的】</h3>
<h3 data-id="heading-15">移除节点：<code>j > nextEnd</code>【证明旧列表有多余的】</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca72d836e70a43d59a1067b49736370f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图，<code>j > prevEnd</code>且<code>j <= nextEnd</code>，只需要把<strong>新列表</strong>中<code>j</code>到<code>nextEnd</code>之间剩下的节点<strong>插入</strong>进去。</p>
<p>如果<code>j > nextEnd</code>【证明旧列表有多余的】时，把<strong>旧列表</strong>中<code>j</code>到<code>prevEnd</code>之间的节点<strong>删除</strong></p>
<h3 data-id="heading-16">移动节点</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deea7566ce0f4d6d9247084d09969502~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据<strong>新列表</strong>剩余的节点数量，创建一个<code>source</code>数组，并将数组填满<code>-1</code>。</p>
<p>创建数组和对象建立关系：</p>
<ul>
<li>数组source【来做新旧节点的对应关系的，根据<code>source</code>计算出它的<code>最长递增子序列</code>用于移动DOM节点】：<strong>新节点</strong>在<strong>旧列表</strong>的位置存储在该数组中，</li>
<li>对象nextIndexMap【通过新列表的key去找旧列表的key】：存储当前<strong>新列表</strong>中的<code>节点key</code>与<code>指引i</code>的关系，再通过key去<strong>旧列表</strong>中去找位置</li>
</ul>
<p><strong>如果旧节点在新列表中没有的话，直接删除就好</strong></p>
<pre><code class="hljs language-js copyable" lang="js">
    <span class="hljs-keyword">let</span> prevStart = j,
      nextStart = j,
      nextLeft = nextEnd - nextStart + <span class="hljs-number">1</span>,     <span class="hljs-comment">// 新列表中剩余的节点长度</span>
      source = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(nextLeft).fill(-<span class="hljs-number">1</span>),  <span class="hljs-comment">// 创建数组，填满-1</span>
      nextIndexMap = &#123;&#125;,                      <span class="hljs-comment">// 新列表节点与index的映射</span>
      patched = <span class="hljs-number">0</span>;                            <span class="hljs-comment">// 已更新过的节点的数量</span>
      
    <span class="hljs-comment">// 保存映射关系  </span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = nextStart; i <= nextEnd; i++) &#123;
      <span class="hljs-keyword">let</span> key = nextChildren[i].key
      nextIndexMap[key] = i
    &#125; 
    
    <span class="hljs-comment">// 去旧列表找位置</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = prevStart; i <= prevEnd; i++) &#123;
      <span class="hljs-keyword">let</span> prevNode = prevChildren[i],
      prevKey = prevNode.key,
        nextIndex = nextIndexMap[prevKey];
      <span class="hljs-comment">// 新列表中没有该节点 或者 已经更新了全部的新节点，直接删除旧节点</span>
      <span class="hljs-keyword">if</span> (nextIndex === undefind || patched >= nextLeft) &#123;
        parent.removeChild(prevNode.el)
        <span class="hljs-keyword">continue</span>
      &#125;
      <span class="hljs-comment">// 找到对应的节点</span>
      <span class="hljs-keyword">let</span> nextNode = nextChildren[nextIndex];
      patch(prevNode, nextNode, parent);
      <span class="hljs-comment">// 给source赋值</span>
      source[nextIndex - nextStart] = i
      patched++
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在找节点时要注意，<strong>如果旧节点在新列表中没有的话，直接删除就好</strong>。除此之外，我们还需要一个数量表示记录我们已经<code>patch</code>过的节点，如果数量已经与<strong>新列表</strong>剩余的节点数量一样，那么剩下的<code>旧节点</code>就直接删除</p>
<p><code>如果是全新的节点的话，其在source数组中对应的值就是初始的-1</code>，通过这一步可以区分出来哪个为全新的节点，哪个是可复用的。</p>
<blockquote>
<p>判断是否要移动？递增法，同react思路：如果找到的<code>index</code>是一直递增的，说明不需要移动任何节点。我们通过设置一个变量move来保存是否需要移动的状态。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vue3Diff</span>(<span class="hljs-params">prevChildren, nextChildren, parent</span>) </span>&#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-attr">outer</span>: &#123;
  <span class="hljs-comment">// ...</span>
  &#125;
  
  <span class="hljs-comment">// 边界情况的判断</span>
  <span class="hljs-keyword">if</span> (j > prevEnd && j <= nextEnd) &#123;
    <span class="hljs-comment">// ...</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (j > nextEnd && j <= prevEnd) &#123;
    <span class="hljs-comment">// ...</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">let</span> prevStart = j,
      nextStart = j,
      nextLeft = nextEnd - nextStart + <span class="hljs-number">1</span>,     <span class="hljs-comment">// 新列表中剩余的节点长度</span>
      source = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(nextLeft).fill(-<span class="hljs-number">1</span>),  <span class="hljs-comment">// 创建数组，填满-1</span>
      nextIndexMap = &#123;&#125;,                      <span class="hljs-comment">// 新列表节点与index的映射</span>
      patched = <span class="hljs-number">0</span>,
      move = <span class="hljs-literal">false</span>,                           <span class="hljs-comment">// 是否移动</span>
      lastIndex = <span class="hljs-number">0</span>;                          <span class="hljs-comment">// 记录上一次的位置</span>
      
    <span class="hljs-comment">// 保存映射关系  </span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = nextStart; i <= nextEnd; i++) &#123;
      <span class="hljs-keyword">let</span> key = nextChildren[i].key
      nextIndexMap[key] = i
    &#125; 
    
    <span class="hljs-comment">// 去旧列表找位置</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = prevStart; i <= prevEnd; i++) &#123;
      <span class="hljs-keyword">let</span> prevNode = prevChildren[i],
      prevKey = prevNode.key,
        nextIndex = nextIndexMap[prevKey];
      <span class="hljs-comment">// 新列表中没有该节点 或者 已经更新了全部的新节点，直接删除旧节点</span>
      <span class="hljs-keyword">if</span> (nextIndex === undefind || patched >= nextLeft) &#123;
        parent.removeChild(prevNode.el)
        <span class="hljs-keyword">continue</span>
      &#125;
      <span class="hljs-comment">// 找到对应的节点</span>
      <span class="hljs-keyword">let</span> nextNode = nextChildren[nextIndex];
      patch(prevNode, nextNode, parent);
      <span class="hljs-comment">// 给source赋值</span>
      source[nextIndex - nextStart] = i
      patched++
      
      <span class="hljs-comment">// 递增方法，判断是否需要移动</span>
      <span class="hljs-keyword">if</span> (nextIndex < lastIndex) &#123;
      move = <span class="hljs-literal">false</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
      lastIndex = nextIndex
      &#125;
    &#125;
    
    <span class="hljs-keyword">if</span> (move) &#123;
    
    <span class="hljs-comment">// 需要移动</span>
    &#125; <span class="hljs-keyword">else</span> &#123;

    <span class="hljs-comment">//不需要移动</span>
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>怎么移动?</p>
</blockquote>
<p>一旦需要进行DOM移动，我们首先要做的就是找到<code>source</code>的<strong>最长递增子序列</strong>。</p>
<p>从后向前进行遍历<code>source</code>每一项。此时会出现三种情况：</p>
<ol>
<li>当前的值为<code>-1</code>，这说明该节点是全新的节点，又由于我们是<strong>从后向前</strong>遍历，我们直接创建好DOM节点插入到队尾就可以了。</li>
<li>当前的索引为<code>最长递增子序列</code>中的值，也就是<code>i === seq[j]</code>，这说说明该节点不需要移动</li>
<li>当前的索引不是<code>最长递增子序列</code>中的值，那么说明该DOM节点需要移动，这里也很好理解，我们也是直接将DOM节点插入到队尾就可以了，因为队尾是排好序的。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0657d2691beb4fb1a9a494e7cb19a51a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vue3Diff</span>(<span class="hljs-params">prevChildren, nextChildren, parent</span>) </span>&#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-keyword">if</span> (move) &#123;
<span class="hljs-keyword">const</span> seq = lis(source); <span class="hljs-comment">// [0, 1]</span>
    <span class="hljs-keyword">let</span> j = seq.length - <span class="hljs-number">1</span>;  <span class="hljs-comment">// 最长子序列的指针</span>
    <span class="hljs-comment">// 从后向前遍历</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = nextLeft - <span class="hljs-number">1</span>； i >= <span class="hljs-number">0</span>; i--) &#123;
      <span class="hljs-keyword">let</span> pos = nextStart + i, <span class="hljs-comment">// 对应新列表的index</span>
        nextNode = nextChildren[pos],<span class="hljs-comment">// 找到vnode</span>
      nextPos = pos + <span class="hljs-number">1</span>，    <span class="hljs-comment">// 下一个节点的位置，用于移动DOM</span>
        refNode = nextPos >= nextChildren.length ? <span class="hljs-literal">null</span> : nextChildren[nextPos].el, <span class="hljs-comment">//DOM节点</span>
        cur = source[i];  <span class="hljs-comment">// 当前source的值，用来判断节点是否需要移动</span>
    
      <span class="hljs-keyword">if</span> (cur === -<span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// 情况1，该节点是全新节点</span>
      mount(nextNode, parent, refNode)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (cur === seq[j]) &#123;
        <span class="hljs-comment">// 情况2，是递增子序列，该节点不需要移动</span>
        <span class="hljs-comment">// 让j指向下一个</span>
        j--
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 情况3，不是递增子序列，该节点需要移动</span>
        parent.insetBefore(nextNode.el, refNode)
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//不需要移动: 我们只需要判断是否有全新的节点【其在source数组中对应的值就是初始的-1】，给他添加进去</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = nextLeft - <span class="hljs-number">1</span>； i >= <span class="hljs-number">0</span>; i--) &#123;
      <span class="hljs-keyword">let</span> cur = source[i];  <span class="hljs-comment">// 当前source的值，用来判断节点是否需要移动</span>
    
      <span class="hljs-keyword">if</span> (cur === -<span class="hljs-number">1</span>) &#123;
       <span class="hljs-keyword">let</span> pos = nextStart + i, <span class="hljs-comment">// 对应新列表的index</span>
          nextNode = nextChildren[pos],<span class="hljs-comment">// 找到vnode</span>
          nextPos = pos + <span class="hljs-number">1</span>，    <span class="hljs-comment">// 下一个节点的位置，用于移动DOM</span>
          refNode = nextPos >= nextChildren.length ? <span class="hljs-literal">null</span> : nextChildren[nextPos].el, <span class="hljs-comment">//DOM节点</span>
      mount(nextNode, parent, refNode)
      &#125;
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">小结</h3>
<ol>
<li>需要创建数组和对象建立关系：</li>
</ol>
<ul>
<li>数组source【来做新旧节点的对应关系的，根据<code>source</code>计算出它的<code>最长递增子序列</code>用于移动DOM节点】：<strong>新节点</strong>在<strong>旧列表</strong>的位置存储在该数组中，</li>
<li>对象nextIndexMap【通过新列表的key去找旧列表的key】：存储当前<strong>新列表</strong>中的<code>节点key</code>与<code>指引i</code>的关系，再通过key去<strong>旧列表</strong>中去找位置</li>
</ul>
<ol start="2">
<li>移除节点满足以下任何一个条件：</li>
</ol>
<ul>
<li><code>j > nextEnd</code></li>
<li>如果旧节点在新列表中没有的话，直接删除</li>
<li>已经更新了全部的新节点，剩下的<code>旧节点</code>就直接删除了【patch标记已更新过的节点的数量】</li>
</ul>
<ol start="3">
<li>新增节点满足以下任何一个条件：</li>
</ol>
<ul>
<li><code>j > prevEnd</code>且<code>j <= nextEnd</code></li>
<li><code>如果是全新的节点的话，其在source数组中对应的值就是初始的-1</code>，新增</li>
</ul>
<ol start="4">
<li>移动节点满足以下任何一个条件：</li>
</ol>
<ul>
<li>当前的索引不是<code>最长递增子序列</code>中的值，那么说明该DOM节点需要移动</li>
</ul>
<ol start="5">
<li>
<p><strong>最长递增子序列</strong>是为了操作移动DOM</p>
</li>
<li>
<p>对比规则：</p>
</li>
</ol>
<p>第一步：对比新老节点数组的头头和尾尾  在这一步将两头两尾相同的进行 patch
第二步：头尾 patch 结束之后，查看新老节点数组是不是有其中一方已经 patch 完了，假如是，那么就多删少补
第三步：遍历老节点，看老节点是否在新节点里面存在，假如不存在，就删除。
// 假如新的子节点都被遍历完了，那么就代表说老的数组之后的，都是需要被删除的
第四步：获取最长递增子序列</p>
<h1 data-id="heading-18">总结</h1>
<p><strong>介绍diff算法</strong></p>
<ol>
<li>react-diff: 递增法</li>
</ol>
<p>移动节点：移动的节点称为α，将α对应的真实的DOM节点移动到，α在<code>新列表中的前一个VNode对应的真实DOM的后面</code></p>
<p>添加节点：在<strong>新列表</strong>中有全新的<code>VNode</code>节点，在<strong>旧列表</strong>中找不到的节点需要添加（通过find这个布尔值来查找）</p>
<p>移除节点：当旧的节点不在<strong>新列表</strong>中时，我们就将其对应的DOM节点移除（通过key来查找确定是否删除）</p>
<p>不足：从头到尾单边比较，容易增加比较次数</p>
<ol start="2">
<li>vue2-diff: 双端比较</li>
</ol>
<p>DOM节点什么时候需要移动和如何移动，总结如下：</p>
<ul>
<li>头-头：不移动</li>
<li>尾-尾：不移动</li>
<li>头-尾: 插入到旧节点的尾节点的后面</li>
<li>尾-头：插入到旧列表的第一个节点之前</li>
<li>以上4种都不存在（特殊情况）：在旧节点中找，如果找到，移动找到的节点，移动到开头；没找到，直接创建一个新的节点放到最前面</li>
</ul>
<p>添加节点【<code>oldEndIndex</code>以及小于了<code>oldStartIndex</code>】：将剩余的节点依次插入到<code>oldStartNode</code>的<code>DOM</code>之前</p>
<p>移除节点【<code>newEndIndex</code>小于<code>newStartIndex</code>】：将<strong>旧列表</strong>剩余的节点删除即可</p>
<ol start="3">
<li>vue3-diff： 最长递增子序列</li>
</ol>
<p><strong>区别</strong></p>
<ol>
<li>react和vue2的比较：</li>
</ol>
<ul>
<li>vue2双端比较解决react单端比较导致移动次数变多的问题，react只能从头到尾遍历，增加了移动次数</li>
</ul>
<ol start="2">
<li>
<p>vue2和vue3的比较：都用了双端指针</p>
</li>
<li>
<p>vue3和react比较：vue3在判断是否需要移动，使用了react的递增法；react是单端比较，这样移动效率降低，vue3是使用双端比较</p>
</li>
</ol>
<p>几个算法看下来，套路就是找到移动的节点，然后给他移动到正确的位置。把该加的新节点添加好，把该删的旧节点删了，整个算法就结束了。</p>
<p>此文借鉴别人的文章，梳理成自己的笔记，分别分析了react、vue2、vue3的diff算法实现原理和具体实现，同时比较了这3种算法，应对面试肯定不会害怕。当然总结它不仅仅为了以后的面试，也为了提升算法思想。</p>
<p>最长递增子序列可以使用动态规划方法
<a href="https://juejin.cn/post/6962783046009356295" target="_blank" title="https://juejin.cn/post/6962783046009356295">juejin.cn/post/696278…</a></p>
<p><a href="https://juejin.cn/post/6919376064833667080#heading-7" target="_blank" title="https://juejin.cn/post/6919376064833667080#heading-7">React、Vue2、Vue3的三种Diff算法 (juejin.cn)</a></p></div>  
</div>
            