
---
title: '有趣的 CSS 数学函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/474c196700694a609ca4c70781528c3f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 16:33:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/474c196700694a609ca4c70781528c3f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>大家好，这里是 CSS 兼 WebGL 魔法使——alphardex。</p>
<p>之前一直在玩 three.js ，接触了很多数学函数，用它们创造过很多特效。于是我思考：能否在 CSS 中也用上这些数学函数，但发现 CSS 目前还没有，据说以后的新规范会纳入，估计也要等很久。</p>
<p>然而，我们可以通过一些小技巧，来创作出一些属于自己的 CSS 数学函数，从而实现一些有趣的动画效果。</p>
<p>让我们开始吧！</p>

<h2 data-id="heading-1">CSS 数学函数</h2>
<p>注意：以下的函数用原生 CSS 也都能实现，这里用 SCSS 函数只是为了方便封装，封装起来的话更方便调用</p>
<h3 data-id="heading-2">绝对值</h3>
<p>绝对值就是正的还是正的，负的变为正的</p>
<p>可以创造 2 个数，其中一个数是另一个数的相反数，比较它们的最大值，即可获得这个数的绝对值</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@function</span> abs(<span class="hljs-variable">$v</span>) &#123;
  <span class="hljs-keyword">@return</span> max(#&#123;<span class="hljs-variable">$v</span>&#125;, calc(-<span class="hljs-number">1</span> * #&#123;$v&#125;));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">中位数</h3>
<p>原数减 1 并乘以一半即可</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@function</span> middle(<span class="hljs-variable">$v</span>) &#123;
  <span class="hljs-keyword">@return</span> calc(<span class="hljs-number">0.5</span> * (#&#123;<span class="hljs-variable">$v</span>&#125; - 1));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">数轴上两点距离</h3>
<p>数轴上两点距离就是两点所表示数字之差的绝对值，有了上面的绝对值公式就可以直接写出来</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@function</span> dist-<span class="hljs-number">1</span>d(<span class="hljs-variable">$v1</span>, <span class="hljs-variable">$v2</span>) &#123;
  <span class="hljs-variable">$v-delta</span>: calc(#&#123;<span class="hljs-variable">$v1</span>&#125; - #&#123;<span class="hljs-variable">$v2</span>&#125;);
  <span class="hljs-keyword">@return</span> #&#123;abs($v-delta)&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">三角函数</h3>
<p>其实这个笔者也不会实现~不过之前看到过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS%2Fissues%2F72" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS/issues/72" ref="nofollow noopener noreferrer">好友 chokcoco 的一篇文章</a>写到了如何在 CSS 中实现三角函数，在此表示感谢</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@function</span> fact(<span class="hljs-variable">$number</span>) &#123;
  <span class="hljs-variable">$value</span>: <span class="hljs-number">1</span>;
  <span class="hljs-keyword">@if</span> <span class="hljs-variable">$number</span>><span class="hljs-number">0</span> &#123;
    <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$number</span> &#123;
      <span class="hljs-variable">$value</span>: <span class="hljs-variable">$value</span> * <span class="hljs-variable">$i</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">@return</span> <span class="hljs-variable">$value</span>;
&#125;

<span class="hljs-keyword">@function</span> pow(<span class="hljs-variable">$number</span>, <span class="hljs-variable">$exp</span>) &#123;
  <span class="hljs-variable">$value</span>: <span class="hljs-number">1</span>;
  <span class="hljs-keyword">@if</span> <span class="hljs-variable">$exp</span>><span class="hljs-number">0</span> &#123;
    <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$exp</span> &#123;
      <span class="hljs-variable">$value</span>: <span class="hljs-variable">$value</span> * <span class="hljs-variable">$number</span>;
    &#125;
  &#125; <span class="hljs-keyword">@else</span> if <span class="hljs-variable">$exp</span> < <span class="hljs-number">0</span> &#123;
    <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through -<span class="hljs-variable">$exp</span> &#123;
      <span class="hljs-variable">$value</span>: <span class="hljs-variable">$value</span> / <span class="hljs-variable">$number</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">@return</span> <span class="hljs-variable">$value</span>;
&#125;

<span class="hljs-keyword">@function</span> rad(<span class="hljs-variable">$angle</span>) &#123;
  <span class="hljs-variable">$unit</span>: unit(<span class="hljs-variable">$angle</span>);
  <span class="hljs-variable">$unitless</span>: <span class="hljs-variable">$angle</span> / (<span class="hljs-variable">$angle</span> * <span class="hljs-number">0</span> + <span class="hljs-number">1</span>);
  <span class="hljs-keyword">@if</span> <span class="hljs-variable">$unit</span>==deg &#123;
    <span class="hljs-variable">$unitless</span>: <span class="hljs-variable">$unitless</span> / <span class="hljs-number">180</span> * pi();
  &#125;
  <span class="hljs-keyword">@return</span> <span class="hljs-variable">$unitless</span>;
&#125;

<span class="hljs-keyword">@function</span> pi() &#123;
  <span class="hljs-keyword">@return</span> <span class="hljs-number">3.14159265359</span>;
&#125;

<span class="hljs-keyword">@function</span> sin(<span class="hljs-variable">$angle</span>) &#123;
  <span class="hljs-variable">$sin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-variable">$angle</span>: rad(<span class="hljs-variable">$angle</span>);
  <span class="hljs-comment">// Iterate a bunch of times.</span>
  <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">0</span> through <span class="hljs-number">20</span> &#123;
    <span class="hljs-variable">$sin</span>: <span class="hljs-variable">$sin</span> + pow(-<span class="hljs-number">1</span>, <span class="hljs-variable">$i</span>) * pow(<span class="hljs-variable">$angle</span>, (<span class="hljs-number">2</span> * <span class="hljs-variable">$i</span> + <span class="hljs-number">1</span>)) / fact(<span class="hljs-number">2</span> * <span class="hljs-variable">$i</span> + <span class="hljs-number">1</span>);
  &#125;
  <span class="hljs-keyword">@return</span> <span class="hljs-variable">$sin</span>;
&#125;

<span class="hljs-keyword">@function</span> cos(<span class="hljs-variable">$angle</span>) &#123;
  <span class="hljs-variable">$cos</span>: <span class="hljs-number">0</span>;
  <span class="hljs-variable">$angle</span>: rad(<span class="hljs-variable">$angle</span>);
  <span class="hljs-comment">// Iterate a bunch of times.</span>
  <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">0</span> through <span class="hljs-number">20</span> &#123;
    <span class="hljs-variable">$cos</span>: <span class="hljs-variable">$cos</span> + pow(-<span class="hljs-number">1</span>, <span class="hljs-variable">$i</span>) * pow(<span class="hljs-variable">$angle</span>, <span class="hljs-number">2</span> * <span class="hljs-variable">$i</span>) / fact(<span class="hljs-number">2</span> * <span class="hljs-variable">$i</span>);
  &#125;
  <span class="hljs-keyword">@return</span> <span class="hljs-variable">$cos</span>;
&#125;

<span class="hljs-keyword">@function</span> tan(<span class="hljs-variable">$angle</span>) &#123;
  <span class="hljs-keyword">@return</span> sin(<span class="hljs-variable">$angle</span>) / cos(<span class="hljs-variable">$angle</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">例子</h2>
<p>以下的几个动画特效演示了上面数学函数的作用</p>
<h3 data-id="heading-7">一维交错动画</h3>
<h4 data-id="heading-8">初始状态</h4>
<p>创建一排元素，用内部阴影填充，准备好我们的数学函数</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略14个 list-item)
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#222</span>;
&#125;

<span class="hljs-selector-pseudo">:root</span> &#123;
  --blue-<span class="hljs-attribute">color</span>-1: <span class="hljs-number">#6ee1f5</span>;
&#125;

(这里复制粘贴上文所有的数学公式)

<span class="hljs-selector-class">.list</span> &#123;
  --n: <span class="hljs-number">16</span>;

  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-wrap</span>: wrap;
  <span class="hljs-attribute">justify-content</span>: space-evenly;

  &-item &#123;
    --<span class="hljs-selector-tag">p</span>: <span class="hljs-number">2vw</span>;
    --gap: <span class="hljs-number">1vw</span>;
    --bg: var(--blue-color-<span class="hljs-number">1</span>);

    <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through <span class="hljs-number">16</span> &#123;
      &<span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$i&#125;) &#123;
        --<span class="hljs-selector-tag">i</span>: #&#123;<span class="hljs-variable">$i</span>&#125;;
      &#125;
    &#125;

    <span class="hljs-attribute">padding</span>: var(--p);
    <span class="hljs-attribute">margin</span>: var(--gap);
    <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> var(--p) var(--bg);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2Ffb7wZV" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fb7wZV" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/474c196700694a609ca4c70781528c3f~tplv-k3u1fbpfcp-watermark.image" alt="fb7wZV.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-9">应用动画</h4>
<p>这里用了 2 个动画：grow 负责将元素缩放出来；melt 负责“融化”元素（即消除阴影的扩散半径）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list grow-melt"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略14个 list-item)
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.list</span> &#123;
  &<span class="hljs-selector-class">.grow-melt</span> &#123;
    <span class="hljs-selector-class">.list-item</span> &#123;
      --t: <span class="hljs-number">2s</span>;

      <span class="hljs-attribute">animation-name</span>: grow, melt;
      <span class="hljs-attribute">animation-duration</span>: var(--t);
      <span class="hljs-attribute">animation-iteration-count</span>: infinite;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> grow &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: scale(<span class="hljs-number">0</span>);
  &#125;

  50%,
  100% &#123;
    <span class="hljs-attribute">transform</span>: scale(<span class="hljs-number">1</span>);
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> melt &#123;
  0%,
  50% &#123;
    <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> var(--p) var(--bg);
  &#125;

  100% &#123;
    <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> var(--bg);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FfqkIkF" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fqkIkF" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145f32b3348141939cc15c7b6d348d46~tplv-k3u1fbpfcp-watermark.image" alt="fqkIkF.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-10">交错动画</h4>
<ol>
<li>计算出元素下标的中位数</li>
<li>计算每个元素 id 到这个中位数的距离</li>
<li>根据距离算出比例</li>
<li>根据比例算出 delay</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list grow-melt middle-stagger"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略14个 list-item)
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.list</span> &#123;
  &<span class="hljs-selector-class">.middle-stagger</span> &#123;
    <span class="hljs-selector-class">.list-item</span> &#123;
      --m: #&#123;middle(var(--n))&#125;; <span class="hljs-comment">// 中位数，这里是7.5</span>
      --<span class="hljs-selector-tag">i</span>-m-dist: #&#123;dist-<span class="hljs-number">1</span>d(var(--i), var(--m))&#125;; <span class="hljs-comment">// 计算每个id到中位数之间的距离</span>
      --ratio: calc(var(--i-m-dist) / var(--m)); <span class="hljs-comment">// 根据距离算出比例</span>
      --delay: calc(var(--ratio) * var(--t)); <span class="hljs-comment">// 根据比例算出delay</span>
      --n-delay: calc((var(--ratio) - <span class="hljs-number">2</span>) * var(--t)); <span class="hljs-comment">// 负delay表示动画提前开始</span>

      <span class="hljs-attribute">animation-delay</span>: var(--n-delay);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FfqkzkD" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fqkzkD" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/455e9865195549079ddb9bdd8cd9af68~tplv-k3u1fbpfcp-watermark.image" alt="fqkzkD.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Falphardex%2Fpen%2FvYmqvpe" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/alphardex/pen/vYmqvpe" ref="nofollow noopener noreferrer">Symmetric Line Animation</a></p>
<h3 data-id="heading-11">二维交错动画</h3>
<h4 data-id="heading-12">初始状态</h4>
<p>如何将一维的升成二维？应用网格系统即可</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略62个 grid-item)
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grid</span> &#123;
  <span class="hljs-variable">$row</span>: <span class="hljs-number">8</span>;
  <span class="hljs-variable">$col</span>: <span class="hljs-number">8</span>;
  --row: #&#123;<span class="hljs-variable">$row</span>&#125;;
  --col: #&#123;<span class="hljs-variable">$col</span>&#125;;
  --gap: <span class="hljs-number">0.25vw</span>;

  <span class="hljs-attribute">display</span>: grid;
  gap: var(--gap);
  grid-template-rows: repeat(var(--row), <span class="hljs-number">1</span>fr);
  grid-template-<span class="hljs-attribute">columns</span>: repeat(var(--col), <span class="hljs-number">1</span>fr);

  &-item &#123;
    --<span class="hljs-selector-tag">p</span>: <span class="hljs-number">2vw</span>;
    --bg: var(--blue-color-<span class="hljs-number">1</span>);

    <span class="hljs-keyword">@for</span> <span class="hljs-variable">$y</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$row</span> &#123;
      <span class="hljs-keyword">@for</span> <span class="hljs-variable">$x</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$col</span> &#123;
        <span class="hljs-variable">$k</span>: <span class="hljs-variable">$col</span> * (<span class="hljs-variable">$y</span> - <span class="hljs-number">1</span>) + <span class="hljs-variable">$x</span>;
        &<span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$k&#125;) &#123;
          --x: #&#123;<span class="hljs-variable">$x</span>&#125;;
          --y: #&#123;<span class="hljs-variable">$y</span>&#125;;
        &#125;
      &#125;
    &#125;

    <span class="hljs-attribute">padding</span>: var(--p);
    <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> var(--p) var(--bg);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FfLsvPx" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fLsvPx" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/308d898ff1eb4545bf7bab4e3aa62988~tplv-k3u1fbpfcp-watermark.image" alt="fLsvPx.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-13">应用动画</h4>
<p>跟上面的动画一模一样</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid grow-melt"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略62个 grid-item)
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grid</span> &#123;
  &<span class="hljs-selector-class">.grow-melt</span> &#123;
    <span class="hljs-selector-class">.grid-item</span> &#123;
      --t: <span class="hljs-number">2s</span>;

      <span class="hljs-attribute">animation-name</span>: grow, melt;
      <span class="hljs-attribute">animation-duration</span>: var(--t);
      <span class="hljs-attribute">animation-iteration-count</span>: infinite;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FfLsGvD" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fLsGvD" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/848b1417cf3d48d28d5b0cf604c79f30~tplv-k3u1fbpfcp-watermark.image" alt="fLsGvD.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-14">交错动画</h4>
<ol>
<li>计算出网格行列的中位数</li>
<li>计算网格 xy 坐标到中位数的距离并求和</li>
<li>根据距离算出比例</li>
<li>根据比例算出 delay</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid grow-melt middle-stagger"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略62个 grid-item)
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grid</span> &#123;
  &<span class="hljs-selector-class">.middle-stagger</span> &#123;
    <span class="hljs-selector-class">.grid-item</span> &#123;
      --m: #&#123;middle(var(--col))&#125;; <span class="hljs-comment">// 中位数，这里是7.5</span>
      --x-m-dist: #&#123;dist-<span class="hljs-number">1</span>d(var(--x), var(--m))&#125;; <span class="hljs-comment">// 计算x坐标到中位数之间的距离</span>
      --y-m-dist: #&#123;dist-<span class="hljs-number">1</span>d(var(--y), var(--m))&#125;; <span class="hljs-comment">// 计算y坐标到中位数之间的距离</span>
      --dist-sum: calc(var(--x-m-dist) + var(--y-m-dist)); <span class="hljs-comment">// 距离之和</span>
      --ratio: calc(var(--dist-sum) / var(--m)); <span class="hljs-comment">// 根据距离和计算比例</span>
      --delay: calc(var(--ratio) * var(--t) * <span class="hljs-number">0.5</span>); <span class="hljs-comment">// 根据比例算出delay</span>
      --n-delay: calc(
        (var(--ratio) - <span class="hljs-number">2</span>) * var(--t) * <span class="hljs-number">0.5</span>
      ); <span class="hljs-comment">// 负delay表示动画提前开始</span>

      <span class="hljs-attribute">animation-delay</span>: var(--n-delay);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FfL2Ppt" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fL2Ppt" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87253929c45d46bbaec2f3edd40aed81~tplv-k3u1fbpfcp-watermark.image" alt="fL2Ppt.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Falphardex%2Fpen%2FzYwgdZO" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/alphardex/pen/zYwgdZO" ref="nofollow noopener noreferrer">Symmetric Grid Animation</a></p>
<h4 data-id="heading-15">另一种动画</h4>
<p>可以换一种动画 shuffle（穿梭），会产生另一种奇特的效果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid shuffle middle-stagger"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略254个 grid-item )
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.grid</span> &#123;
  <span class="hljs-variable">$row</span>: <span class="hljs-number">16</span>;
  <span class="hljs-variable">$col</span>: <span class="hljs-number">16</span>;
  --row: #&#123;<span class="hljs-variable">$row</span>&#125;;
  --col: #&#123;<span class="hljs-variable">$col</span>&#125;;
  --gap: <span class="hljs-number">0.25vw</span>;

  &-item &#123;
    --<span class="hljs-selector-tag">p</span>: <span class="hljs-number">1vw</span>;

    <span class="hljs-attribute">transform-origin</span>: bottom;
    <span class="hljs-attribute">transform</span>: scaleY(<span class="hljs-number">0.1</span>);
  &#125;

  &<span class="hljs-selector-class">.shuffle</span> &#123;
    <span class="hljs-selector-class">.grid-item</span> &#123;
      --t: <span class="hljs-number">2s</span>;

      <span class="hljs-attribute">animation</span>: shuffle var(--t) infinite ease-in-out alternate;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> shuffle &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: scaleY(<span class="hljs-number">0.1</span>);
  &#125;

  50% &#123;
    <span class="hljs-attribute">transform</span>: scaleY(<span class="hljs-number">1</span>);
    <span class="hljs-attribute">transform-origin</span>: bottom;
  &#125;

  50<span class="hljs-selector-class">.01</span>% &#123;
    <span class="hljs-attribute">transform-origin</span>: top;
  &#125;

  100% &#123;
    <span class="hljs-attribute">transform-origin</span>: top;
    <span class="hljs-attribute">transform</span>: scaleY(<span class="hljs-number">0.1</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FfOJSZ8" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/fOJSZ8" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e89c00039dd4afcb571a86b47d9980a~tplv-k3u1fbpfcp-watermark.image" alt="fOJSZ8.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Falphardex%2Fpen%2FYzVmYaV" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/alphardex/pen/YzVmYaV" ref="nofollow noopener noreferrer">Shuffle Grid Animation</a></p>
<h3 data-id="heading-16">余弦波动动画</h3>
<h4 data-id="heading-17">初始状态</h4>
<p>创建 7 个不同颜色的（这里直接选了彩虹色）列表，每个列表有 40 个子元素，每个子元素是一个小圆点</p>
<p>让这 7 个列表排列在一条线上，且 z 轴上距离错开，设置好基本的 delay</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"lists"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    ...(此处省略39个 list-item)
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  ...(此处省略6个 list)
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.lists</span> &#123;
  <span class="hljs-variable">$list-count</span>: <span class="hljs-number">7</span>;
  <span class="hljs-variable">$colors</span>: red, orange, yellow, green, cyan, blue, purple;

  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">34vw</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">2vw</span>;
  <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
  <span class="hljs-attribute">perspective</span>: <span class="hljs-number">800px</span>;

  <span class="hljs-selector-class">.list</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">transform</span>: translateZ(var(--z));

    <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$list-count</span> &#123;
      &<span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$i&#125;) &#123;
        --bg: #&#123;nth(<span class="hljs-variable">$colors</span>, <span class="hljs-variable">$i</span>)&#125;;
        --z: #&#123;<span class="hljs-variable">$i</span> * -<span class="hljs-number">1vw</span>&#125;;
        --basic-delay-ratio: #&#123;<span class="hljs-variable">$i</span> / <span class="hljs-variable">$list-count</span>&#125;;
      &#125;
    &#125;

    &-item &#123;
      --w: <span class="hljs-number">0.6vw</span>;
      --gap: <span class="hljs-number">0.15vw</span>;

      <span class="hljs-attribute">width</span>: var(--w);
      <span class="hljs-attribute">height</span>: var(--w);
      <span class="hljs-attribute">margin</span>: var(--gap);
      <span class="hljs-attribute">background</span>: var(--bg);
      <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FhSdtfI" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/hSdtfI" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19b1cb956f4849ef9a23cce10fe50653~tplv-k3u1fbpfcp-watermark.image" alt="hSdtfI.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-18">余弦排列</h4>
<p>运用上文的三角函数公式，让这些小圆点以余弦的一部分形状进行排列</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.lists</span> &#123;
  <span class="hljs-selector-class">.list</span> &#123;
    &-item &#123;
      <span class="hljs-variable">$item-count</span>: <span class="hljs-number">40</span>;
      <span class="hljs-variable">$offset</span>: pi() * <span class="hljs-number">0.5</span>;
      --wave-length: <span class="hljs-number">21vw</span>;

      <span class="hljs-keyword">@for</span> <span class="hljs-variable">$i</span> from <span class="hljs-number">1</span> through <span class="hljs-variable">$item-count</span> &#123;
        &<span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$i&#125;) &#123;
          --<span class="hljs-selector-tag">i</span>: #&#123;<span class="hljs-variable">$i</span>&#125;;
          <span class="hljs-variable">$ratio</span>: (<span class="hljs-variable">$i</span> - <span class="hljs-number">1</span>) / (<span class="hljs-variable">$item-count</span> - <span class="hljs-number">1</span>);
          <span class="hljs-variable">$angle-unit</span>: pi() * <span class="hljs-variable">$ratio</span>;
          <span class="hljs-variable">$wave</span>: cos(<span class="hljs-variable">$angle-unit</span> + <span class="hljs-variable">$offset</span>);
          --single-wave-length: calc(#&#123;<span class="hljs-variable">$wave</span>&#125; * var(--wave-length));
          --n-single-wave-length: calc(var(--single-wave-length) * -<span class="hljs-number">1</span>);
        &#125;
      &#125;

      <span class="hljs-attribute">transform</span>: translateY(var(--n-single-wave-length));
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FhSwuNj" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/hSwuNj" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/251dd0ca8f274ba6b30eee1bb615cbff~tplv-k3u1fbpfcp-watermark.image" alt="hSwuNj.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-19">波动动画</h4>
<p>对每个小圆点应用上下平移动画，平移的距离就是余弦的波动距离</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.lists</span> &#123;
  <span class="hljs-selector-class">.list</span> &#123;
    &-item &#123;
      --t: <span class="hljs-number">2s</span>;

      <span class="hljs-attribute">animation</span>: wave var(--t) infinite ease-in-out alternate;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> wave &#123;
  from &#123;
    <span class="hljs-attribute">transform</span>: translateY(var(--n-single-wave-length));
  &#125;

  to &#123;
    <span class="hljs-attribute">transform</span>: translateY(var(--single-wave-length));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FhSwfPA" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/hSwfPA" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7bb9a09b894aaa8c650223d56c6964~tplv-k3u1fbpfcp-watermark.image" alt="hSwfPA.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h4 data-id="heading-20">交错动画</h4>
<p>跟上面一个套路，计算从中间开始的 delay，再应用到动画上即可</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.lists</span> &#123;
  <span class="hljs-selector-class">.list</span> &#123;
    &-item &#123;
      --n: #&#123;<span class="hljs-variable">$item-count</span> + <span class="hljs-number">1</span>&#125;;
      --m: #&#123;middle(var(--n))&#125;;
      --<span class="hljs-selector-tag">i</span>-m-dist: #&#123;dist-<span class="hljs-number">1</span>d(var(--i), var(--m))&#125;;
      --ratio: calc(var(--i-m-dist) / var(--m));
      --square: calc(var(--ratio) * var(--ratio));
      --delay: calc(
        calc(var(--square) + var(--basic-delay-ratio) + <span class="hljs-number">1</span>) * var(--t)
      );
      --n-delay: calc(var(--delay) * -<span class="hljs-number">1</span>);

      <span class="hljs-attribute">animation-delay</span>: var(--n-delay);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FhSwqaQ" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/hSwqaQ" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13d51dcb29224763965c15262577137d~tplv-k3u1fbpfcp-watermark.image" alt="hSwqaQ.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Falphardex%2Fpen%2FGREKJbL" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/alphardex/pen/GREKJbL" ref="nofollow noopener noreferrer">Rainbow Sine</a></p>
<h2 data-id="heading-21">最后</h2>
<p>CSS 数学函数能实现的特效远不止于此，希望通过本文能激起大家创作特效的灵感~</p></div>  
</div>
            