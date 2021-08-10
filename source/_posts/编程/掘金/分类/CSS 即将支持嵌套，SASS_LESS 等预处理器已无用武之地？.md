
---
title: 'CSS 即将支持嵌套，SASS_LESS 等预处理器已无用武之地？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73f4c4c6a2124e6aade7fb782d58cb53~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 17:17:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73f4c4c6a2124e6aade7fb782d58cb53~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近，有一则非常振奋人心的消息，CSS 即将原生支持嵌套 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Flists.w3.org%2FArchives%2FPublic%2Fwww-style%2F2021Mar%2F0019.html" target="_blank" rel="nofollow noopener noreferrer" title="https://lists.w3.org/Archives/Public/www-style/2021Mar/0019.html" ref="nofollow noopener noreferrer">Agenda+ to publish FPWD of Nesting</a>，表示 CSS 嵌套规范即将进入规范的 FWPD 阶段。</p>
<p>目前对应的规范为 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdrafts.csswg.org%2Fcss-nesting%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://drafts.csswg.org/css-nesting/" ref="nofollow noopener noreferrer">CSS Nesting Module</a>。</p>
<p>随着 CSS 自定义属性（CSS Variable）的大规模兼容，到如今 CSS 即将支持嵌套，一些预处理器的核心功能已经被 CSS 原生支持，这是否表示 SASS/LESS 等预处理器已无用武之地？即将被淘汰了？</p>
<h2 data-id="heading-0">规范的几个阶段</h2>
<p>首先简单介绍一下，一个规范从提出到落地，会经历的一些阶段：</p>
<ol>
<li>编辑草案 Editor's Draft (ED)</li>
<li>工作草案 Working Draft (WD)</li>
<li>过渡－最后通告工作草案 Transition – Last Call Working Draft (LCWD)</li>
<li>候选推荐标准 Candidate Recommendation (CR)</li>
<li>过渡－建议推荐标准 Transition – Proposed Recommendations (PR)</li>
<li>推荐标准 Recommendation (REC)</li>
</ol>
<p>上文说的，即将进入 FPWD，只是处于规范的第 2 个阶段 WD 阶段，FPWD 表示第一次公开工作草案（ First Public Working Draft (FPWD)）。FPWD 后面还会有数个工作草案，会处理来自 CSSWG 内部和小组外部更广泛社会的反馈。完善规范的设计。</p>
<p>也就是说，目前来看，即便后面的流程顺利，要等到浏览器大范围实现该规范到能落地的那天还有非常长一段时间。</p>
<p>除此之外，我觉得 SASS\LESS 等预处理器还有一些比较有意思的功能（函数），是即便原生 CSS 支持了自定义属性和嵌套之后依旧欠缺的，我简单罗列罗列我的看法。</p>
<h2 data-id="heading-1">for() 循环函数</h2>
<p>目前，原生 CSS 依旧不支持循环函数。</p>
<p>但是其实在预处理器中，循环还算是比较常用的一个功能。考虑下面这种布局：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73f4c4c6a2124e6aade7fb782d58cb53~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>ul</code> 下面有多个 <code>li</code>，每个 li 的高度递增 <code>20px</code>，一个一个写当然也可以，但是有了循环其实能极大减少工作量：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有预处理器，我们的 CSS 可能是这样的：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">ul</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: baseline;
    <span class="hljs-attribute">justify-content</span>: space-between;
&#125;
<span class="hljs-selector-tag">li</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
&#125;
<span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
&#125;
// ... <span class="hljs-number">3</span>~<span class="hljs-number">9</span>
<span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">10</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果利用 SASS 预处理器，可以简化成：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">ul</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: baseline;
    <span class="hljs-attribute">justify-content</span>: space-between;
&#125;
<span class="hljs-selector-tag">li</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
&#125;
<span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">10</span> &#123;
    <span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$<span class="hljs-selector-tag">i</span>&#125;) &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(#&#123;$i&#125; * <span class="hljs-number">20px</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，除此之外，在非常多的复杂 CSS 动画效果中，循环是非常非常常用的功能。</p>
<p>譬如一些粒子动画，我们通常可能需要去操纵 50<del>100 个粒子，也就是 50</del>100 个 div 的样式，甚至更多，如果没有循环，一个一个去写效率会大打折扣。</p>
<h3 data-id="heading-2">利用预处理器循环功能实现的一些效果展示</h3>
<p>下面我简单罗列一些我实现过的，运用到了 CSS 预处理器循环功能的动画效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f8e429d713b454099cedaf9110d9d62~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>像上面这个使用纯 CSS 实现的火焰效果，其中的火焰的动态燃烧效果。其实是通过大量的细微粒子的运动，配合滤镜实现。</p>
<p>其中使用到了 SASS 的循环函数的片段：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> to <span class="hljs-number">200</span> &#123;
    <span class="hljs-selector-class">.g-ball</span><span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$<span class="hljs-selector-tag">i</span>&#125;) &#123;
        $<span class="hljs-attribute">width</span>: #&#123;<span class="hljs-built_in">random</span>(<span class="hljs-number">50</span>)&#125;px;
        
        <span class="hljs-attribute">width</span>: $width;
        <span class="hljs-attribute">height</span>: $width;
        <span class="hljs-attribute">left</span>: <span class="hljs-built_in">calc</span>(#&#123;(<span class="hljs-built_in">random</span>(<span class="hljs-number">70</span>))&#125;px - <span class="hljs-number">55px</span>);
    &#125;
    
    <span class="hljs-selector-class">.g-ball</span><span class="hljs-selector-pseudo">:nth-child</span>(#&#123;$<span class="hljs-selector-tag">i</span>&#125;) &#123;
        <span class="hljs-attribute">animation</span>: movetop <span class="hljs-number">1s</span> linear -#&#123;<span class="hljs-built_in">random</span>(<span class="hljs-number">3000</span>)/<span class="hljs-number">1000</span>&#125;s infinite;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯哼，上面的循环是循环了 200 次之多，如果真要一个一个写，工作量还是非常巨大的。上述效果的完整代码，你可以戳这里：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FChokcoco%2Fpen%2FjJJbmz" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/Chokcoco/pen/jJJbmz" ref="nofollow noopener noreferrer">CodePen Demo -- CSS Candles</a></p>
<h2 data-id="heading-3">if() 条件语句</h2>
<p>接下来一个就是 if() 条件语句。</p>
<p>其实，CSS 中有一类非常类似条件语句的写法，也就是媒体查询 <code>@media</code> 以及 特性检测 <code>@supports</code> 语句，目前 CSS 中支持的类似条件选择的一些写法如下：</p>
<h3 data-id="heading-4">@support 条件语句</h3>
<p>CSS @supports 通过 CSS 语法来实现特性检测，并在内部 CSS 区块中写入如果特性检测通过希望实现的 CSS 语句。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">position</span>:fixed;
&#125;
 
<span class="hljs-keyword">@supports</span> (<span class="hljs-attribute">position</span>:sticky) &#123;
    <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">position</span>:sticky;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述 CSS 语句的意思是如果客户端支持 <code>position:sticky</code>，则采用 <code>position:sticky</code>，否则，就是 <code>position:fixed</code>。</p>
<p>关于 CSS 特性检测的深入讲解，你可以看看我的这篇文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fcoco1s%2Fp%2F6478389.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/coco1s/p/6478389.html" ref="nofollow noopener noreferrer">深入探讨 CSS 特性检测 @supports 与 Modernizr</a></p>
<h3 data-id="heading-5">@media 条件语句</h3>
<p>另外一种常见的条件语句就是媒体查询，这个大家还是比较熟悉的。</p>
<p>如果当前设备满足一种什么条件，则怎么样怎么样。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">article</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">4rem</span>;
&#125;
<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">900px</span>) &#123;
  <span class="hljs-selector-tag">article</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">1rem</span> <span class="hljs-number">3rem</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯，并且，上述的两种条件语句可以互相嵌套使用：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@supports</span> (<span class="hljs-attribute">display</span>: flex) &#123;
  <span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">900px</span>) &#123;
    <span class="hljs-selector-tag">article</span> &#123;
      <span class="hljs-attribute">display</span>: flex;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过，上述两种毕竟不是严格意义上的我们期待的 <code>if()</code> 语句。</p>
<p>很久之前，社区就有声音(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fw3c%2Fcsswg-drafts%2Fissues%2F3455" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/w3c/csswg-drafts/issues/3455" ref="nofollow noopener noreferrer">css-values - if() function</a>)，提议 CSS 规范中实现 <code>if()</code> 条件语句，类似于这样：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.foo</span> &#123;
  --calc: <span class="hljs-built_in">calc</span>(<span class="hljs-number">10</span> * (<span class="hljs-number">1vw</span> + <span class="hljs-number">1vh</span>) / <span class="hljs-number">2</span>);
  <span class="hljs-attribute">font-size</span>: <span class="hljs-built_in">if</span>(<span class="hljs-built_in">var</span>(--calc) < <span class="hljs-number">12px</span>, <span class="hljs-number">12px</span>, <span class="hljs-built_in">var</span>(--calc));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这一语句 <code>if(var(--calc) < 12px, 12px, var(--calc))</code> 类似于一个三元语句，还是比较好理解的。</p>
<p>然而，上述的条件语句一直没得到支持的原因，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fw3c%2Fcsswg-drafts%2Fissues%2F3455" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/w3c/csswg-drafts/issues/3455" ref="nofollow noopener noreferrer">scss-values - if() function</a> 可以略窥一二。</p>
<p>原因是 CSS 一直在尽量避免在属性当中产生任意依赖。在 CSS 中，属性之间本身存在一些隐式依赖，譬如 <code>em</code> 单位长度受到父元素的 <code>font-size</code> 的影响，如果作者能够添加任意依赖关系（通过 if() 条件语句），那么将会导致一些问题。</p>
<blockquote>
<p>原文是：this, unfortunately, means we're adding arbitrary dependencies between properties, something we've avoided doing so far because it's, in general, unresolvable.
Custom properties can arbitrarily refer to each other, but they're limited in what they can do, and have a somewhat reasonable "just become invalid" behavior when we notice a cycle. Cycles are more difficult to determine for arbitrary CSS, and can happen much more easily, because there are a number of existing, implicit between-property dependencies. For example, anything that takes a length relies on font-size (due to em), and so you can't have a value in font-size that refers to a property that takes a length (so no adjusting font-size to scale with width!). We add new dependencies of this sort over time (such as adding the lh unit, which induces a dependency on line-height); if authors could add arbitrary dependencies, we'd be unable to add new implicit ones for fear of breaking existing content (by forming cycles that were previous valid and non-cyclic).</p>
</blockquote>
<p>所以，CSS 中的直接 <code>if()</code> 语句一直没有得到实现。</p>
<h3 data-id="heading-6">SASS 等预处理器中的 <code>if()</code> 语句</h3>
<p>最后，我们来看看预处理器中对 <code>if()</code> 的运用，由于 SASS 等预处理器最终还是要编译成 CSS 文件，所以 <code>if()</code> 其实并不太常用。因为 SASS 中的 <code>if()</code> 也无法实现类似上述说的 <code>font-size: if(var(--calc) < 12px, 12px, var(--calc))</code> 这种功能。</p>
<p>在 SASS 中，我认为最常用的 <code>if()</code> 可能也就是这种场景：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@mixin</span> triangle($size, $<span class="hljs-attribute">color</span>, $direction) &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;

  <span class="hljs-attribute">border-color</span>: transparent;
  <span class="hljs-attribute">border-style</span>: solid;
  <span class="hljs-attribute">border-width</span>: $size;

  <span class="hljs-keyword">@if</span> $direction == up &#123;
    <span class="hljs-attribute">border-bottom-color</span>: $color;
  &#125; <span class="hljs-keyword">@else</span> if $direction == right &#123;
    <span class="hljs-attribute">border-left-color</span>: $color;
  &#125; <span class="hljs-keyword">@else</span> if $direction == down &#123;
    <span class="hljs-attribute">border-top-color</span>: $color;
  &#125; <span class="hljs-keyword">@else</span> if $direction == left &#123;
    <span class="hljs-attribute">border-right-color</span>: $color;
  &#125; <span class="hljs-keyword">@else</span> &#123;
    <span class="hljs-keyword">@error</span> <span class="hljs-string">"Unknown direction #&#123;$direction&#125;."</span>;
  &#125;
&#125;

<span class="hljs-selector-class">.next</span> &#123;
  <span class="hljs-keyword">@include</span> triangle(<span class="hljs-number">5px</span>, black, right);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码是对 CSS 实现三角形的一个封装，通过传入的参数，实现不同方向、颜色、大小的三角形。也就是预处理器中 <code>if()</code> ，更多的完成一些函数功能的封装，方便复用。</p>
<p>实际上述的代码会被编译成：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.next</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">border-color</span>: transparent;
  <span class="hljs-attribute">border-style</span>: solid;
  <span class="hljs-attribute">border-width</span>: <span class="hljs-number">5px</span>;
  <span class="hljs-attribute">border-left-color</span>: black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">Random() 随机函数</h2>
<p>OK，接下来这个是随机函数，是我个人在 SASS 等预处理器中最常用的一个函数。目前原生 CSS 不支持任意形式的随机。</p>
<p>在 CSS 动画效果中，非常多的因素我们不希望是一成不变的，我们希望的是，一些属性的值的产生由我们设定一个基础规则，一个范围中得到，这样每次刷新都能产生不同的效果。</p>
<p>最常见的莫过于不同的颜色、不同的长度、不同的数量等等等等。</p>
<p>譬如下面这个使用 CSS 实现的效果：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcsscoco.com%2Finspiration%2F%23%2F.%2Fcssdoodle%2Fsunset" target="_blank" rel="nofollow noopener noreferrer" title="https://csscoco.com/inspiration/#/./cssdoodle/sunset" ref="nofollow noopener noreferrer">夏日夕阳图</a>。</p>
<p>我们通过随机，每次刷新都可以得到高度/宽度不一样，位置不一样的 div 块，利用随机的特性，绘制一幅幅不一样的效果图：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/128620145-68a5c56c-a4c1-4886-a5f1-e474adaf2f5f.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcsscoco.com%2Finspiration%2F%23%2F.%2Fcssdoodle%2Fsunset" target="_blank" rel="nofollow noopener noreferrer" title="https://csscoco.com/inspiration/#/./cssdoodle/sunset" ref="nofollow noopener noreferrer">DEMO -- 夏日夕阳图</a></p>
<p>目前原生 CSS 不支持任意形式的随机。使用预处理器，也只能是在编译前编写随机函数，SASS 中比较常用的随机函数的一些写法：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">$r: <span class="hljs-built_in">random</span>(<span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>random()</code> 是 SASS 支持的一种函数，上述 $r 就能得到一个 0 ~ 100 的随机整数。</p>
<p>利用 <code>random()</code>，就能封装出各种随机函数，譬如随机颜色：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@function</span> randomNum($max, $<span class="hljs-attribute">min</span>: <span class="hljs-number">0</span>, $<span class="hljs-attribute">u</span>: <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">@return</span> ($min + random($max)) * $u;
&#125;

<span class="hljs-keyword">@function</span> randomColor() &#123;
    <span class="hljs-keyword">@return</span> rgb(randomNum(<span class="hljs-number">255</span>), randomNum(<span class="hljs-number">255</span>), randomNum(<span class="hljs-number">255</span>));
&#125;

<span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">randomColor</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">关于原生 CSS 实现 random() 的一些思考</h3>
<p>下面这个是社区对原生 CSS 实现 random() 函数的一些思考，感兴趣的可以猛击：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fw3c%2Fcsswg-drafts%2Fissues%2F2826" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/w3c/csswg-drafts/issues/2826" ref="nofollow noopener noreferrer">[css-values] random() function</a></p>
<p>简单搬运其中一些比较有意思的观点。</p>
<p>假设 CSS 原生实现了 <code>random()</code> 函数，譬如下述这个写法：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"foo"</span>></span>123<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"foo"</span>></span>456<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"foo"</span>></span>789<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.foo</span><span class="hljs-selector-pseudo">:hover</span> &#123; 
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-built_in">random</span>(<span class="hljs-number">0</span>, <span class="hljs-number">255</span>), <span class="hljs-number">0</span>, <span class="hljs-number">0</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设其中 <code>ramdom()</code> 是原生 CSS 实现的随机函数，有一些事情是需要被解决或者得到大家的认可的：</p>
<ol>
<li><code>random(0, 255)</code> 的值在什么时候被确定，是在每一次 CSS 解析时，还是每一次被应用触发时？</li>
<li>对于上述 DEMO，3 个 <code>.foo</code> 的 <code>color</code> 值是否一样？</li>
<li>对于反复的 <code>hover</code>，取消 <code>hover</code> 状态，<code>random(0, 255)</code> 的值是否会发生变化？</li>
</ol>
<p>上述的问题可以归结于如果 CSS 原生支持随机，随机值的持久化和更新是必须要解决的问题。总之，目前看来，未来 CSS 原生支持随机的可能性还是很大的。</p>
<h2 data-id="heading-9">工具函数：颜色函数、数学函数</h2>
<p>最后，我们再来看看一些有意思的工具函数。目前原生 CSS 暂时不支持一些比较复杂的颜色函数和数学函数。但是预处理器都带有这些函数。</p>
<p>在我之前的一篇关于阴影的文章中 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS%2Fissues%2F39" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS/issues/39" ref="nofollow noopener noreferrer">你所不知道的 CSS 阴影技巧与细节</a>，介绍过一种利用多重阴影实现立体阴影的效果，譬如我们要实现下面这个效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d0736a4b41d4ddeb297a1780a9013ec~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的阴影的颜色变化就借助了 SASS 的<strong>颜色函数</strong>：</p>
<ul>
<li><code>fade-out</code> 改变颜色的透明度，让颜色更加透明</li>
<li><code>desaturate</code> 改变颜色的饱和度值，让颜色更少的饱和</li>
</ul>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@function</span> makelongrightshadow($<span class="hljs-attribute">color</span>) &#123;
    $val: <span class="hljs-number">0px</span> <span class="hljs-number">0px</span> $color;

    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">50</span> &#123;
        $<span class="hljs-attribute">color</span>: <span class="hljs-built_in">fade-out</span>(<span class="hljs-built_in">desaturate</span>($color, <span class="hljs-number">1%</span>), .<span class="hljs-number">02</span>);
        $val: #&#123;$val&#125;, #&#123;$<span class="hljs-selector-tag">i</span>&#125;px #&#123;$<span class="hljs-selector-tag">i</span>&#125;px #&#123;$<span class="hljs-attribute">color</span>&#125;;
    &#125;

    <span class="hljs-keyword">@return</span> $val;
&#125;

<span class="hljs-selector-tag">p</span>&#123;
   <span class="hljs-attribute">text-shadow</span>: <span class="hljs-built_in">makelongrightshadow</span>(<span class="hljs-built_in">hsla</span>(<span class="hljs-number">14</span>, <span class="hljs-number">100%</span>, <span class="hljs-number">30%</span>, <span class="hljs-number">1</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，除了上述的两个颜色函数，SASS 还提供了非常多类似的颜色相关的函数，可以看看这里：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sass.hk%2Fskill%2Fsass25.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sass.hk/skill/sass25.html" ref="nofollow noopener noreferrer">Sass基础—颜色函数</a>。</p>
<p>除了颜色，数学函数也是经常在 CSS 效果中会需要用到的。</p>
<p>我在这篇文章中 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS%2Fissues%2F72" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS/issues/72" ref="nofollow noopener noreferrer">在 CSS 中使用三角函数绘制曲线图形及展示动画</a>，专门讲了如何利用 SASS 等预处理器实现<strong>三角函数</strong>，以实现曲线线条，实现一些有意思的效果，像是这样：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/69351842-e5f76b80-0cb6-11ea-8c3c-b6eee35dff01.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，目前 SASS 也不支持三角函数，但是我们可以利用 SASS function，实现一套三角函数代码：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-keyword">@function</span> fact($number) &#123;
    $value: <span class="hljs-number">1</span>;
    <span class="hljs-keyword">@if</span> $number><span class="hljs-number">0</span> &#123;
        <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through $number &#123;
            $value: $value * $i;
        &#125;
    &#125;
    <span class="hljs-keyword">@return</span> $value;
&#125;

<span class="hljs-keyword">@function</span> pow($number, $exp) &#123;
    $value: <span class="hljs-number">1</span>;
    <span class="hljs-keyword">@if</span> $exp><span class="hljs-number">0</span> &#123;
        <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through $exp &#123;
            $value: $value * $number;
        &#125;
    &#125;
    <span class="hljs-keyword">@else</span> if $exp < <span class="hljs-number">0</span> &#123;
        <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through -$exp &#123;
            $value: $value / $number;
        &#125;
    &#125;
    <span class="hljs-keyword">@return</span> $value;
&#125;

<span class="hljs-keyword">@function</span> rad($angle) &#123;
    $unit: <span class="hljs-built_in">unit</span>($angle);
    $unitless: $angle / ($angle * <span class="hljs-number">0</span> + <span class="hljs-number">1</span>);
    <span class="hljs-keyword">@if</span> $unit==deg &#123;
        $unitless: $unitless / <span class="hljs-number">180</span> * <span class="hljs-built_in">pi</span>();
    &#125;
    <span class="hljs-keyword">@return</span> $unitless;
&#125;

<span class="hljs-keyword">@function</span> pi() &#123;
    <span class="hljs-keyword">@return</span> <span class="hljs-number">3.14159265359</span>;
&#125;

<span class="hljs-keyword">@function</span> sin($angle) &#123;
    $sin: <span class="hljs-number">0</span>;
    $angle: <span class="hljs-built_in">rad</span>($angle);
    // Iterate <span class="hljs-selector-tag">a</span> bunch of times.
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">0</span> through <span class="hljs-number">20</span> &#123;
        $sin: $sin + <span class="hljs-built_in">pow</span>(-<span class="hljs-number">1</span>, $i) * <span class="hljs-built_in">pow</span>($angle, (<span class="hljs-number">2</span> * $i + <span class="hljs-number">1</span>)) / <span class="hljs-built_in">fact</span>(<span class="hljs-number">2</span> * $i + <span class="hljs-number">1</span>);
    &#125;
    <span class="hljs-keyword">@return</span> $sin;
&#125;

<span class="hljs-keyword">@function</span> cos($angle) &#123;
    $cos: <span class="hljs-number">0</span>;
    $angle: <span class="hljs-built_in">rad</span>($angle);
    // Iterate <span class="hljs-selector-tag">a</span> bunch of times.
    <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">0</span> through <span class="hljs-number">20</span> &#123;
        $cos: $cos + <span class="hljs-built_in">pow</span>(-<span class="hljs-number">1</span>, $i) * <span class="hljs-built_in">pow</span>($angle, <span class="hljs-number">2</span> * $i) / <span class="hljs-built_in">fact</span>(<span class="hljs-number">2</span> * $i);
    &#125;
    <span class="hljs-keyword">@return</span> $cos;
&#125;

<span class="hljs-keyword">@function</span> tan($angle) &#123;
    <span class="hljs-keyword">@return</span> sin($angle) / cos($angle);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就目前原生 CSS 而言，在数学函数等方面其实已经做出了非常多的努力，譬如：</p>
<ul>
<li>基础运算函数 <code>calc()</code></li>
<li>比较函数 <code>max()</code>、<code>min()</code>、<code>clamp()</code></li>
</ul>
<p>等兼容性已经逐渐铺开，可以开始大规模使用，而类似于</p>
<ul>
<li>指数函数 <code>pow()</code>、<code>sqrt()</code>、<code>hypot()</code>、<code>log()</code>、<code>exp()</code></li>
<li>三角函数 <code>sin()</code>、<code>con()</code>、<code>tan()</code></li>
<li>阶梯函数 <code>round()</code>、<code>mod()</code>、<code>rem()</code> 等</li>
</ul>
<p>也在规范 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdrafts.csswg.org%2Fcss-values-4%2F%23exponent-funcs" target="_blank" rel="nofollow noopener noreferrer" title="https://drafts.csswg.org/css-values-4/#exponent-funcs" ref="nofollow noopener noreferrer">CSS Values and Units Module Level 4</a> 中被提及定义，相信不久的将来也会逐渐落地。</p>
<p>关于社区对数学函数的一些讨论，感兴趣的也可以看看这里：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdrafts.csswg.org%2Fcss-values%2F%23math" target="_blank" rel="nofollow noopener noreferrer" title="https://drafts.csswg.org/css-values/#math" ref="nofollow noopener noreferrer">Mathematical Expressions</a></p>
<h2 data-id="heading-10">总结一下</h2>
<p>好了，综上总结一下，就目前而言，我觉得 SASS/LESS 等预处理器在很多方面还是有有用武之地的，在上述的一些功能原生 CSS 没有完全落地之前，预处理器能一定程度上弥补 CSS 的不足。</p>
<p>并且，除去上述说的一些我个人认为比较重要有意思的功能、函数之外，预处理器其它一些核心功能，譬如 extend、mixins 等也能有效的提升开发时的效率。</p>
<p>所以，在未来的一段时间内，我认为预处理器还是能和 CSS 友好共存~</p>
<h2 data-id="heading-11">最后</h2>
<p>好了，本文到此结束，希望对你有帮助 :)</p>
<p>想 Get 到最有意思的 CSS 资讯，千万不要错过我的公众号 -- <strong>iCSS前端趣闻</strong> 😄</p>
<p>更多精彩 CSS 效果可以关注我的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcsscoco.com%2Finspiration%2F%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://csscoco.com/inspiration/#/" ref="nofollow noopener noreferrer">CSS 灵感</a></p>
<p>更多精彩 CSS 技术文章汇总在我的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS" ref="nofollow noopener noreferrer">Github -- iCSS</a> ，持续更新，欢迎点个 star 订阅收藏。</p>
<p>如果还有什么疑问或者建议，可以多多交流，原创文章，文笔有限，才疏学浅，文中若有不正之处，万望告知。</p></div>  
</div>
            