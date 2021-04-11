
---
title: '经常问到的CSS BFC 和 IFC 是什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6a900211eb4223b766003f04a5effe~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 08:37:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6a900211eb4223b766003f04a5effe~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是BFC？什么作用？</h2>
<p><strong>Block Formatting Context</strong></p>
<p>==块盒子布局发生的区域，浮动元素和其他元素交互的区域==</p>
<p>浮动定位和清除浮动的时候只会应用于同一个BFC内的元素。浮动不会影响其他BFC中元素的布局，而<strong>清除浮动只能清除同一BFC中在它前面的元素的浮动</strong>。</p>
<p><strong>外边距的折叠也只会发生在同一BFC中的块级元素之间</strong>。可以创建新的BFC来消除外边距的折叠问题。</p>
<p>常见的定位布局方案有，普通流，浮动和绝对定位。</p>
<p>BFC 是一块渲染区域，有一套渲染定位规则。决定子元素定位其他元素的关系和相互作用，是属于普通流的。<strong>具有 BFC 特性的元素可以看作是隔离了的独立容器，容器里面的元素不会在布局上影响到外面的元素，并且 BFC 具有普通容器所没有的一些特性。</strong></p>
<p>其实也不是什么新鲜东西，可能都在用但不知道这个概念。</p>
<hr>
<h3 data-id="heading-1">案例1:使浮动元素和周围内容等高</h3>
<p>对于以下代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">224</span>, <span class="hljs-number">206</span>, <span class="hljs-number">247</span>);
    <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid rebeccapurple;
    <span class="hljs-comment">/* overflow: auto; */</span>
    <span class="hljs-comment">/* display: flow-root; */</span>
  &#125;
  <span class="hljs-selector-class">.float</span> &#123;
    <span class="hljs-attribute">float</span>: left;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">background-color</span>: white;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>I am a floated box!<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>I am content inside the container.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示的效果如下：</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6a900211eb4223b766003f04a5effe~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>因为浮动盒子脱离了文档流。浮动的div元素更大，就穿出了边框。</p>
<p>一般是需要将盒子和浮动元素做成等高的，即浮动元素应该包含在box内部，要达到这个效果，可以这样：</p>
<ol>
<li>
<p><strong>使用<code>display: flow-root</code></strong></p>
<p>一个新的<code>display</code>属性值，可以创建无副作用的BFC。在父级元素中使用<code>display: flow-root</code>就可以创建新的BFC。</p>
<blockquote>
<p>可以理解为和创建根元素一样，创建一个<strong>文档流的上下文</strong>。</p>
</blockquote>
</li>
<li>
<p><strong>使用overflow:auto</strong></p>
<p>只要设置overflow为一个非visible的值就可以。使用<code>overflow</code>创建一个新的BFC，<code>overflow</code>会告诉浏览器如何处理超出部分的内容。</p>
<p>但是如果只是用来创建BFC的话，可能引发其他情况。</p>
</li>
</ol>
<hr>
<h3 data-id="heading-2">案例2: 清除外部浮动</h3>
<p>对于以下代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-tag">section</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
  &#125;
  <span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">224</span>, <span class="hljs-number">206</span>, <span class="hljs-number">247</span>);
    <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid rebeccapurple;
  &#125;
  <span class="hljs-selector-class">.box</span><span class="hljs-selector-attr">[style]</span> &#123;
    <span class="hljs-attribute">background-color</span>: aliceblue;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid steelblue;
  &#125;
  <span class="hljs-selector-class">.float</span> &#123;
    <span class="hljs-attribute">float</span>: left;
    <span class="hljs-attribute">overflow</span>: hidden; <span class="hljs-comment">/* required by resize:both */</span>
    <span class="hljs-attribute">resize</span>: both;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.75</span>);
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>


<span class="hljs-tag"><<span class="hljs-name">section</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>Try to resize this outer float<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"><<span class="hljs-name">section</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>Try to resize this outer float<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"display:flow-root"</span>></span><span class="hljs-tag"><<span class="hljs-name">p</span>></span>     
    <span class="hljs-tag"><<span class="hljs-name">code</span>></span>display:flow-root<span class="hljs-tag"></<span class="hljs-name">code</span>></span><span class="hljs-tag"><<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要关注的是<code>float</code>元素上的<code>margin-right</code>这个属性。</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95bc01acf64f40b494dcb4e4211a5a11~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>上面的两个元素之间，margin-right 没有生效。但是对<code>box</code>添加<code>display:flow-root</code>属性之后，margin-right 属性就生效了，左边的元素缩放的时候始终都保持有<code>25px</code>的距离。也就是**<code>display:flow-root</code>对同级的外部元素的浮动也清除了**。</p>
<p>如果对HTML部分写成这样：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">section</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>Try to resize this outer float<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>Try to resize this outer float<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"><<span class="hljs-name">section</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>Try to resize this outer float<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"float"</span>></span>Try to resize this outer float<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"display: flow-root"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">code</span>></span>display:flow-root<span class="hljs-tag"></<span class="hljs-name">code</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>xx<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>消除同级元素的float, 显示出 margin-right 的效果就更明显了。</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a06a638d8a472c9ba44abb576a8197~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>需要注意的是：清除同一BFC中的浮动，只能清除在它前面元素的浮动。</p>
</blockquote>
<hr>
<h3 data-id="heading-3">案例3:  外边距塌陷问题</h3>
<p>对于如下代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.blue</span>,
  <span class="hljs-selector-class">.red-inner</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span> <span class="hljs-number">0</span>;
    <span class="hljs-attribute">background</span>: blue;
  &#125;

  <span class="hljs-selector-class">.red-outer</span> &#123;
    <span class="hljs-comment">/* display: flow-root; */</span>
    <span class="hljs-comment">/* overflow: hidden; */</span>
    <span class="hljs-attribute">background</span>: red;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"blue"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"red-outer"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"red-inner"</span>></span>red inner<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示的效果如下：</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de566865f41f4090b7afa121351afe75~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>可以看到，对red-inner的margin没法撑起盒子，两个蓝色盒子之间的距离是50px.</p>
<p>使用<code>display: flow-root;</code></p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ecc12891dd4f3a9a46f40ac2f32d54~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>两个蓝色盒子就距离100px了，而且<code>margin</code>也完全显示了出来。</p>
<hr>
<h2 data-id="heading-4">创建BFC的方法</h2>
<p>使用这些BFC的特性，需要创建出BFC：</p>
<ul>
<li><strong>根元素（<code><html>）</code></strong></li>
<li><strong>浮动元素（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/float" target="_blank" rel="nofollow noopener noreferrer"><code>float</code></a> 不是 <code>none</code>）</strong></li>
<li><strong>绝对定位元素（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/position" target="_blank" rel="nofollow noopener noreferrer"><code>position</code></a> 为 <code>absolute</code> 或 <code>fixed</code>）</strong></li>
<li><strong>行内块元素（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 为 <code>inline-block</code>）</strong></li>
<li>表格单元格（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 为 <code>table-cell</code>，HTML表格单元格默认为该值）</li>
<li>表格标题（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 为 <code>table-caption</code>，HTML表格标题默认为该值）</li>
<li>匿名表格单元格元素（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 为 <code>table、``table-row</code>、 <code>table-row-group、``table-header-group、``table-footer-group</code>（分别是HTML table、row、tbody、thead、tfoot 的默认属性）或 <code>inline-table</code>）</li>
<li><strong><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow" target="_blank" rel="nofollow noopener noreferrer"><code>overflow</code></a> 计算值(Computed)不为 <code>visible</code> 的块元素</strong></li>
<li><strong><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 值为 <code>flow-root</code> 的元素</strong></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/contain" target="_blank" rel="nofollow noopener noreferrer"><code>contain</code></a> 值为 <code>layout</code>、<code>content </code>或 paint 的元素</li>
<li><strong>弹性元素（<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 为 <code>flex</code> 或 <code>inline-flex </code>元素的直接子元素）</strong></li>
<li>网格元素（<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/display" target="_blank" rel="nofollow noopener noreferrer"><code>display</code></a> 为 <code>grid</code> 或 <code>inline-grid</code> 元素的直接子元素）</li>
<li>多列容器（元素的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-count" target="_blank" rel="nofollow noopener noreferrer"><code>column-count</code></a> 或 <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/column-width" target="_blank" rel="nofollow noopener noreferrer"><code>column-width</code> (en-US)</a> 不为 <code>auto，包括 ``column-count</code> 为 <code>1</code>）</li>
<li><code>column-span</code> 为 <code>all</code> 的元素始终会创建一个新的BFC，即使该元素没有包裹在一个多列容器中（<a href="https://github.com/w3c/csswg-drafts/commit/a8634b96900279916bd6c505fda88dda71d8ec51" target="_blank" rel="nofollow noopener noreferrer">标准变更</a>，<a href="https://bugs.chromium.org/p/chromium/issues/detail?id=709362" target="_blank" rel="nofollow noopener noreferrer">Chrome bug</a>）</li>
</ul>
<hr>
<h2 data-id="heading-5">什么又是 IFC？</h2>
<p>相对于块级格式化上下文，还有行内格式化上下文，<strong>Inline formatting context</strong>。</p>
<p>对于IFC，行内框一个接一个地排列，排列顺序和书写方向一致。</p>
<ul>
<li>水平书写模式，行内框从左边开始水平排列</li>
<li>垂直书写模式，行内框从顶部开始水平排列</li>
</ul>
<p>一个行内框在被分割到多行中的时候，margin，border以及padding的设定不会在断裂处生效**（边框跨行连续，不会产生两块border）**</p>
<p>Margin，border和padding的设置在行方向上生效。</p>
<h3 data-id="heading-6">垂直方向上对齐</h3>
<p>垂直方向上的位置主要是用<code>vertical-align</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.horizontal</span> &#123;
    writing-mode: horizontal-tb;
   &#125;

  <span class="hljs-selector-class">.vertical</span> &#123;
    writing-mode: vertical-rl;
   &#125;
<span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">200%</span>;
    <span class="hljs-comment">/* vertical-align: top; */</span>
    <span class="hljs-attribute">vertical-align</span>: bottom;
   &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>    

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example horizontal"</span>></span>
      Before that night—<span class="hljs-tag"><<span class="hljs-name">span</span>></span>a memorable night<span class="hljs-tag"></<span class="hljs-name">span</span>></span>, as it was to prove—hundreds of millions of
      people had watched the rising smoke-wreaths of their fires without drawing any special
      inspiration from the fact.”
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示效果：</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97386e260f0244e9b50a00ab9fb7d377~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>==而如果将<code>vertical-align: bottom</code>设置为<code>top</code>，效果则是顶部对齐==：</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7554ea4cf9c346908dd73509200c0f1e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<blockquote>
<p>需要注意的是，如果文字方向是垂直书写模式的话，对齐方式不变，但实际上应该是左右对齐，与vertical-align的字面意思稍有出入。在<code>vertical-align:top</code>再加上<code>writing-mode: vertical-rl</code>。</p>
<img width="80/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c1d6cd8df28412ab2deff49565652f7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</blockquote>
<h3 data-id="heading-7">水平方向上对齐</h3>
<p>行内元素在水平方向上的位置主要是用<code>text-align</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
   <span class="hljs-selector-class">.horizontal</span> &#123;
    writing-mode: horizontal-tb;
   &#125;

  <span class="hljs-selector-class">.vertical</span> &#123;
    writing-mode: vertical-rl;
   &#125;
<span class="hljs-selector-class">.example</span> &#123;
    <span class="hljs-attribute">text-align</span>: center;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example horizontal"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: 1px solid"</span>></span>One Two Three<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example vertical"</span>></span>One Two Three<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示效果：</p>
<img width="600/" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/344f67c3c66443cd82710d80ab3295ac~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<hr>
<p>参考：</p>
<ul>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Block_formatting_context#exclude_external_floats" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Inline_formatting_context" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
</li>
<li>
<p><a href="https://zhuanlan.zhihu.com/p/25321647" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/25321647</a></p>
</li>
<li>
<p><a href="https://www.runoob.com/" target="_blank" rel="nofollow noopener noreferrer">www.runoob.com/</a></p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            