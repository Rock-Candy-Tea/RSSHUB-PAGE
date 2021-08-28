
---
title: '使用 CSS 和 SVG 滤镜给 SVG 图标添加阴影'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/s_EE31147C7EC35BC4B7EE00D7050579562DC2DDDC7CFB621A7904E66DFA700FE7_1622485808504_drop-shadow-01.jpg?resize=1800%2C846'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 10:29:31 GMT
thumbnail: 'https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/s_EE31147C7EC35BC4B7EE00D7050579562DC2DDDC7CFB621A7904E66DFA700FE7_1622485808504_drop-shadow-01.jpg?resize=1800%2C846'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fadding-shadows-to-svg-icons-with-css-and-svg-filters%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/adding-shadows-to-svg-icons-with-css-and-svg-filters/" ref="nofollow noopener noreferrer">Adding Shadows to SVG Icons With CSS and SVG Filters</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fauthor%2Fjoelolawanlet%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/author/joelolawanlet/" ref="nofollow noopener noreferrer">Joel Olawanle </a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fadding-shadows-to-svg-icons-with-css-and-svg-filters.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/adding-shadows-to-svg-icons-with-css-and-svg-filters.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FPassionPenguin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/PassionPenguin" ref="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：</li>
</ul>
</blockquote>
<p>为什么我们需要给 SVG 添加阴影？</p>
<ol>
<li>阴影是一种常见的设计功能，可以帮助图标等元素脱颖而出。它们可以是持久的，也可以应用于不同的状态（例如专属于 <code>:hover</code>、<code>:focus</code> 或<code>:active</code> 的阴影）以指示与用户的交互。</li>
<li>阴影发生在现实生活中，因此在页面中应用阴影可以为我们的元素注入活力，并<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fgetting-deep-into-shadow%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/getting-deep-into-shadow/" ref="nofollow noopener noreferrer">为设计添加一丝真实感</a>。</li>
</ol>
<p>由于我们正在制作列表，因此我们可以通过两种主要方式将阴影应用于 SVG：</p>
<ol>
<li>使用 CSS <code>[filter()](https://css-tricks.com/almanac/properties/f/filter/)</code> 属性；</li>
<li>使用 SVG <code><filter></code>；</li>
</ol>
<p>是的，两者都涉及滤镜！而且，是的，CSS 和 SVG 都有自己的滤镜类型。但这些之间也有一些交叉。例如，一个 CSS <code>filter</code> 可以引用一个 SVG <code><filter></code>；也就是说，我们可以在 CSS 中使用内联 SVG 而不是别的，比如说，在 CSS 中用作背景图像的 SVG。</p>
<p>**不能使用的内容：**CSS <code>box-shadow</code> 属性。这通常用于阴影，但它只会遵循元素的矩形外边缘，而不是我们所希望它遵循的 SVG 元素的边缘。这是 Michelle Barker 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-irl.info%2Fdrop-shadow-the-underrated-css-filter%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-irl.info/drop-shadow-the-underrated-css-filter/" ref="nofollow noopener noreferrer">清晰解释</a>：</p>
<p><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/s_EE31147C7EC35BC4B7EE00D7050579562DC2DDDC7CFB621A7904E66DFA700FE7_1622485808504_drop-shadow-01.jpg?resize=1800%2C846" alt="两张亮粉色的扁平小猫脸，露出耳朵、眼睛和胡须。第一只小猫的盒子周围有阴影，第二只小猫的路径边缘有阴影。" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是，如果我们使用的是 SVG 图标字体，则 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Falmanac%2Fproperties%2Ft%2Ftext-shadow%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/almanac/properties/t/text-shadow/" ref="nofollow noopener noreferrer"><code>text-shadow</code></a> 始终都是可选择的添加阴影的方法。那确实会奏效。但是让我们关注前两个，因为它们符合大多数用例。</p>
<h2 data-id="heading-0">带有 CSS 滤镜的阴影</h2>
<p>通过 CSS 滤镜将阴影直接应用于 SVG 的技巧是 <code>drop-shadow()</code> 函数：</p>
<pre><code class="hljs language-css copyable" lang="css">SVG &#123;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">shadow</span>(<span class="hljs-number">3px</span> <span class="hljs-number">5px</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> / <span class="hljs-number">0.4</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将应用一个阴影，从水平方向 3px 开始并向下 5px，模糊半径是 2px，阴影颜色是 40% 的黑色。以下是一些示例：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fchriscoyier%2Fpen%2FrNypeeJ" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/chriscoyier/pen/rNypeeJ" ref="nofollow noopener noreferrer">Codepen chriscoyier/rNypeeJ</a>。</p>
<blockquote>
<p>此浏览器支持数据来自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%23feat%3D%25E2%2580%259Dcss-filters%25E2%2580%259D" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/#feat=%E2%80%9Dcss-filters%E2%80%9D" ref="nofollow noopener noreferrer">Caniuse</a>，其中有更多详细信息。数字表示浏览器支持该版本及更高版本的功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59bfdc0377e34923a2463e7c16adefb3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-1">在 CSS 滤镜中调用 SVG 滤镜</h3>
<p>假设我们在 HTML 中有一个 SVG 滤镜：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"0"</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'shadow'</span> <span class="hljs-attr">color-interpolation-filters</span>=<span class="hljs-string">"sRGB"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">feDropShadow</span> <span class="hljs-attr">dx</span>=<span class="hljs-string">"2"</span> <span class="hljs-attr">dy</span>=<span class="hljs-string">"2"</span> <span class="hljs-attr">stdDeviation</span>=<span class="hljs-string">"3"</span> <span class="hljs-attr">flood-opacity</span>=<span class="hljs-string">"0.5"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">filter</span>></span>

<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用 CSS 滤镜通过 ID 调用该 SVG 滤镜，而不是我们之前看到的值：</p>
<pre><code class="hljs language-css copyable" lang="css">SVG &#123;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">#shadow</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在该滤镜取自 HTML 并在应用它的 CSS 中引用：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fchriscoyier%2Fpen%2FyLMpOoP" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/chriscoyier/pen/yLMpOoP" ref="nofollow noopener noreferrer">Codepen chriscoyier/yLMpOoP</a>。</p>
<h3 data-id="heading-2">使用 SVG 滤镜原始类型</h3>
<p>你可能想知道我们是如何让 SVG <code><filter></code> 工作的。为了使用 SVG 滤镜制作阴影，我们使用<strong>filter 原始类型</strong>。SVG 中的滤镜原始类型是一种元素，它以某种图像或图形作为输入，然后在调用时输出该图像或图形。它们有点像图形编辑应用程序中的滤镜，但它们是代码中并且只能在 SVG <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FSVG%2FElement%2Ffilter" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter" ref="nofollow noopener noreferrer"><code><filter></code></a> 元素中定义。</p>
<p>SVG 中有<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FSVG%2FElement%23filter_primitive_elements" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/SVG/Element#filter_primitive_elements" ref="nofollow noopener noreferrer">许多不同的滤镜原始类型</a>。我们要接触的是 <code><feDropShadow></code>。我会让你只看名字就猜到要做什么。</p>
<p>因此，类似于我们使用 CSS 滤镜执行此操作的方式：</p>
<pre><code class="hljs language-css copyable" lang="css">svg &#123;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">3px</span> <span class="hljs-number">5px</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> / <span class="hljs-number">0.4</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>……我们可以使用 <code><feDropShadow></code> SVG 滤镜原始类型完成相同的操作。有三个关键属性值得一提，因为它们有助于定义阴影的外观：</p>
<ul>
<li><code>dx</code> —— 这会沿 x 轴移动阴影的位置。</li>
<li><code>dy</code> —— 这会沿着 y 轴移动阴影的位置。</li>
<li><code>stdDeviation</code> —— 这定义了阴影模糊操作的标准偏差。我们还可以使用其他属性，例如用于设置阴影颜色的 <code>flood-color</code> 和用于设置阴影不透明度的 <code>flood-opacity</code>。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Folawanlejoel%2Fpen%2FxxqdaqN" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/olawanlejoel/pen/xxqdaqN" ref="nofollow noopener noreferrer">Codepen olawanlejoel/xxqdaqN</a></p>
<p>该示例包括三个 <code><filter></code> 元素，每个元素都有自己的 <code><feDropShadow></code> 滤镜原始类型。</p>
<h2 data-id="heading-3">使用 SVG 滤镜</h2>
<p>SVG 滤镜非常强大。我们刚刚了解了 <code><feDropShadow></code>，这当然非常有用，但它们可以做的还有很多（包括类似 Photoshop 的效果），而且我们只为阴影获得的东西的子集非常广泛。让我们看一些，比如彩色阴影和插入阴影。</p>
<p>让我们以 Twitter 徽标的 SVG 标记为例：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"svg-icon"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 20 20"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#4691f6"</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M18.258,3.266c-0.693,0.405-1.46,0.698-2.277,0.857c-0.653-0.686-1.586-1.115-2.618-1.115c-1.98,0-3.586,1.581-3.586,3.53c0,0.276,0.031,0.545,0.092,0.805C6.888,7.195,4.245,5.79,2.476,3.654C2.167,4.176,1.99,4.781,1.99,5.429c0,1.224,0.633,2.305,1.596,2.938C2.999,8.349,2.445,8.19,1.961,7.925C1.96,7.94,1.96,7.954,1.96,7.97c0,1.71,1.237,3.138,2.877,3.462c-0.301,0.08-0.617,0.123-0.945,0.123c-0.23,0-0.456-0.021-0.674-0.062c0.456,1.402,1.781,2.422,3.35,2.451c-1.228,0.947-2.773,1.512-4.454,1.512c-0.291,0-0.575-0.016-0.855-0.049c1.588,1,3.473,1.586,5.498,1.586c6.598,0,10.205-5.379,10.205-10.045c0-0.153-0.003-0.305-0.01-0.456c0.7-0.499,1.308-1.12,1.789-1.827c-0.644,0.28-1.334,0.469-2.06,0.555C17.422,4.782,17.99,4.091,18.258,3.266"</span> ></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们需要一个 <code><filter></code> 元素来实现这些效果。这需要在 HTML 的 <code><svg></code> 元素中。 <code><filter></code> 元素永远不会直接在浏览器中呈现 — 它仅用作可以通过 SVG 中的 <code>filter</code> 属性或 CSS 中的 <code>url()</code> 函数引用的内容。</p>
<p>以下是显示 SVG 滤镜并将其应用于源图像的语法：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 300 300"</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myfilters"</span>></span>
    <span class="hljs-comment"><!-- 所有的滤镜效果/原始类型在此定义 --></span>
  <span class="hljs-tag"></<span class="hljs-name">filter</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">filter</span>=<span class="hljs-string">"url(#myfilters)"</span>></span>
    <span class="hljs-comment"><!-- 滤镜会应用于这一组下所有的东西 --></span>
    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"……"</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"……"</span> ></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">g</span>></span>

<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>filter</code> 元素旨在将 <strong>filter 原始类型</strong>作为子元素。它是一系列过滤操作的容器，这些操作组合起来以创建过滤效果。</p>
<p>这些滤镜原始类型对一个或多个输入执行单个基本图形操作（例如模糊、移动、填充、组合或扭曲）。它们就像构建块，每个 SVG 滤镜都可以用来与其他滤镜结合使用以创建效果。<code><feGaussianBlur></code> 是一种流行的滤镜原始类型，用于添加高斯模糊效果。</p>
<p>假设我们使用 <code><feGaussianBlur></code> 定义了以下 SVG 滤镜：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.1"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"gaussian-blur"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">feGaussianBlur</span> <span class="hljs-attr">stdDeviation</span>=<span class="hljs-string">"1 0"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">filter</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当应用于元素时，此滤镜会创建<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.adobe.com%2Fcreativecloud%2Fphotography%2Fdiscover%2Fgaussian-blur.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.adobe.com/creativecloud/photography/discover/gaussian-blur.html" ref="nofollow noopener noreferrer">高斯模糊</a>效果，在 x 上以 <code>1px</code> 的模糊半径模糊元素，但在 y 轴上没有模糊。这是有和没有效果的结果：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Folawanlejoel%2Fpen%2FrNyGbjw" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/olawanlejoel/pen/rNyGbjw" ref="nofollow noopener noreferrer">CodePen olawanlejoel/rNyGbjw</a></p>
<p>我们可以在单个滤镜中使用多个原始类型。这将创建有趣的效果，但是，我们需要让不同的原始类型相互了解。Bence Szabó 有一套<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fcreating-patterns-with-svg-filters%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/creating-patterns-with-svg-filters/" ref="nofollow noopener noreferrer">疯狂酷炫的模式</a>，他是用这种方式创建的：</p>
<p>当组合多个滤镜原始类型时，第一个原始类型使用原始图形（<code>SourceGraphic</code>）作为其图形输入。任何后续原始类型都使用它之前的过滤效果的结果作为其输入。等等。但是我们可以通过在原始元素上使用 <code>in</code>、<code>in2</code> 和 <code>result</code> 属性来获得一些灵活性。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvanseodesign.com%2Fweb-design%2Fsvg-filter-primitives-input-output%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vanseodesign.com/web-design/svg-filter-primitives-input-output/" ref="nofollow noopener noreferrer">Steven Bradley 有一篇关于滤镜原始类型的优秀文章</a>可以追溯到 2016 年，但今天仍然适用。</p>
<p>我们今天可以使用 17 个原始类型：</p>
<ul>
<li><code><feGaussianBlur></code></li>
<li><code><feDropShadow></code></li>
<li><code><feMorphology></code></li>
<li><code><feDisplacementMap></code></li>
<li><code><feBlend></code></li>
<li><code><feColorMatrix></code></li>
<li><code><feConvolveMatrix></code></li>
<li><code><feComponentTransfer></code></li>
<li><code><feSpecularLighting></code></li>
<li><code><feDiffuseLighting></code></li>
<li><code><feFlood></code></li>
<li><code><feTurbulence></code></li>
<li><code><feImage></code></li>
<li><code><feTile></code></li>
<li><code><feOffset></code></li>
<li><code><feComposite></code></li>
<li><code><feMerge></code></li>
</ul>
<p>注意所有这些的 <code>fe</code> 前缀。那代表 <code>过滤效果</code>（<code>filter effect</code>）。理解 SVG 滤镜具有挑战性。像插入阴影这样的效果需要冗长的语法，如果没有对数学和色彩理论的透彻理解，就很难掌握。（Rob O'Leary 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fgetting-deep-into-shadows%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/getting-deep-into-shadows/" ref="nofollow noopener noreferrer">“深入阴影”</a> 是一个很好的起点。）</p>
<p>我们将使用一些预制的滤镜，而把我们自己带入奇妙的超现实状态或情况的事物之中。幸运的是，我们身边有很多现成的 SVG 滤镜。</p>
<h3 data-id="heading-4">插入阴影</h3>
<p>要在 Twitter 徽标上使用过滤效果，我们需要在我们的“SVG 源文档”中声明它，并在我们的 <code><filter></code> 标签中使用唯一的 ID 进行引用。</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'inset-shadow'</span>></span>
  <span class="hljs-comment"><!-- Shadow offset --></span>
  <span class="hljs-tag"><<span class="hljs-name">feOffset</span>
    <span class="hljs-attr">dx</span>=<span class="hljs-string">'0'</span>
    <span class="hljs-attr">dy</span>=<span class="hljs-string">'0'</span>
  /></span>

  <span class="hljs-comment"><!-- 阴影半径 --></span>
  <span class="hljs-tag"><<span class="hljs-name">feGaussianBlur</span>
    <span class="hljs-attr">stdDeviation</span>=<span class="hljs-string">'1'</span>
    <span class="hljs-attr">result</span>=<span class="hljs-string">'offset-blur'</span>
  /></span>

  <span class="hljs-comment"><!-- 反转阴影以制作内嵌的阴影 --></span>
  <span class="hljs-tag"><<span class="hljs-name">feComposite</span>
    <span class="hljs-attr">operator</span>=<span class="hljs-string">'out'</span>
    <span class="hljs-attr">in</span>=<span class="hljs-string">'SourceGraphic'</span>
    <span class="hljs-attr">in2</span>=<span class="hljs-string">'offset-blur'</span>
    <span class="hljs-attr">result</span>=<span class="hljs-string">'inverse'</span>
  /></span>

  <span class="hljs-comment"><!-- 修改阴影内的颜色透明度 --></span>
  <span class="hljs-tag"><<span class="hljs-name">feFlood</span>
    <span class="hljs-attr">flood-color</span>=<span class="hljs-string">'black'</span>
    <span class="hljs-attr">flood-opacity</span>=<span class="hljs-string">'.95'</span>
    <span class="hljs-attr">result</span>=<span class="hljs-string">'color'</span>
  /></span>
  <span class="hljs-tag"><<span class="hljs-name">feComposite</span>
    <span class="hljs-attr">operator</span>=<span class="hljs-string">'in'</span>
    <span class="hljs-attr">in</span>=<span class="hljs-string">'color'</span>
    <span class="hljs-attr">in2</span>=<span class="hljs-string">'inverse'</span>
    <span class="hljs-attr">result</span>=<span class="hljs-string">'shadow'</span>
  /></span>

  <span class="hljs-comment"><!-- 在元素上放置阴影 --></span>
  <span class="hljs-tag"><<span class="hljs-name">feComposite</span>
    <span class="hljs-attr">operator</span>=<span class="hljs-string">'over'</span>
    <span class="hljs-attr">in</span>=<span class="hljs-string">'shadow'</span>
    <span class="hljs-attr">in2</span>=<span class="hljs-string">'SourceGraphic'</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">filter</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那里有四种不同的原始类型，每一种都执行不同的功能。 但是，综合起来，它们实现了插入阴影。</p>
<table>
    <tbody><tr>
        <td><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/twitter-shadow-1a.jpg?ssl=1&resize=500%2C500" alt="fig 1a" loading="lazy" referrerpolicy="no-referrer"></td>
        <td><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/twitter-shadow-2.jpg?ssl=1&resize=500%2C500" alt="fig 2" loading="lazy" referrerpolicy="no-referrer"></td>
        <td><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/twitter-shadow-3.jpg?ssl=1&resize=500%2C500" alt="fig 3" loading="lazy" referrerpolicy="no-referrer"></td>
    </tr>
    <tr>
        <td><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/twitter-shadow-4.jpg?ssl=1&resize=500%2C500" alt="fig 4" loading="lazy" referrerpolicy="no-referrer"></td>
        <td><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/twitter-shadow-5.jpg?ssl=1&resize=500%2C500" alt="fig 5" loading="lazy" referrerpolicy="no-referrer"></td>
        <td><img src="https://i2.wp.com/css-tricks.com/wp-content/uploads/2021/06/twitter-shadow-6.jpg?ssl=1&resize=500%2C500" alt="fig 6" loading="lazy" referrerpolicy="no-referrer"></td>
    </tr>
</tbody></table>
<p>现在我们已经创建了这个插入阴影滤镜，我们可以将它应用到我们的 SVG 中。我们已经看到了如何通过 CSS 应用它。 就像是：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.filtered</span> &#123;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">#myfilters</span>);
&#125;

<span class="hljs-comment">/* 或者只应用于特定的状态，比如说： */</span>
svg<span class="hljs-selector-pseudo">:hover</span>,
svg<span class="hljs-selector-pseudo">:focus</span> &#123;
  <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">#myfilters</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Folawanlejoel%2Fpen%2FjOBBRjd" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/olawanlejoel/pen/jOBBRjd" ref="nofollow noopener noreferrer">Codepen olawanlejoel/jOBBRjd</a></p>
<p>我们还可以使用 <code>filter</code> 属性直接在 SVG 语法中应用 SVG <code><filter></code>，就像：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span>></span>

  <span class="hljs-comment"><!-- 应用单一滤镜 --></span>
  <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"..."</span> <span class="hljs-attr">filter</span>=<span class="hljs-string">"url(#myfilters)"</span> /></span>

  <span class="hljs-comment"><!-- 或者应用于一组元素 --></span>
  <span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">filter</span>=<span class="hljs-string">"url(#myfilters)"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"……"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"……"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">g</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Folawanlejoel%2Fpen%2FvYxmXVg" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/olawanlejoel/pen/vYxmXVg" ref="nofollow noopener noreferrer">CodePen olawanlejoel/vYxmXVg</a></p>
<h2 data-id="heading-5">更多例子</h2>
<p>以下是来自 Oleg Solomka 的更多阴影示例：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fsol0mka%2Fpen%2F6eca814eda8ec7e758d0feab628bd390" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/sol0mka/pen/6eca814eda8ec7e758d0feab628bd390" ref="nofollow noopener noreferrer">CodePen sol0mka/6eca814eda8ec7e758d0feab628bd390</a></p>
<p>请注意，这里的基本阴影可能比它们需要的要复杂一些。例如，彩色阴影仍然可以使用 <code><feDropShadow></code> 来完成，例如：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">feDropShadow</span> <span class="hljs-attr">dx</span>=<span class="hljs-string">"-0.8"</span> <span class="hljs-attr">dy</span>=<span class="hljs-string">"-0.8"</span> <span class="hljs-attr">stdDeviation</span>=<span class="hljs-string">"0"</span>
  <span class="hljs-attr">flood-color</span>=<span class="hljs-string">"pink"</span> <span class="hljs-attr">flood-opacity</span>=<span class="hljs-string">"0.5"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这种浮雕效果作为滤镜非常棒！</p>
<p>另请注意，我们可能会在 SVG 语法中看到 SVG 滤镜，如下所示：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"position: absolute; margin-left: -100%;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-filters"</span>></span>
      <span class="hljs-comment"><!-- …… --></span>
    <span class="hljs-tag"></<span class="hljs-name">filter</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">symbol</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-icon"</span>></span>
      <span class="hljs-comment"><!-- …… --></span>
    <span class="hljs-tag"></<span class="hljs-name">symbol</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在第一行，意思是：这个 SVG 根本不应该渲染 —— 它只是我们打算稍后使用的东西。<code><defs></code> 标签说了类似的话：我们只是定义这些东西以备后用。这样，我们就不必一遍又一遍地写东西来重复自己。我们将通过 ID 和符号引用滤镜，也许像：</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">svg</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#my-icon"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SVG 滤镜得到广泛支持（甚至在 Internet Explorer 和 Edge 中！），而且性能非常之好。</p>
<blockquote>
<p>此浏览器支持数据来自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%23feat%3D%25E2%2580%259Dsvg-filters%25E2%2580%259D" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/#feat=%E2%80%9Dsvg-filters%E2%80%9D" ref="nofollow noopener noreferrer">Caniuse</a>，其中有更多详细信息。数字表示浏览器支持该版本及更高版本的功能。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/383949f020d7469ea809a65807ceefbb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-6">总结一下</h2>
<p>最后对比：</p>
<ul>
<li>CSS 滤镜更易于使用，但限制更多。例如，我认为不可能使用 <code>drop-shadow()</code> 函数添加插入阴影。</li>
<li>SVG 滤镜更加健壮，但也更加复杂，并且需要在 HTML 中的某处使用 <code><filter></code>。</li>
<li>它们都具有出色的浏览器支持并且在所有现代浏览器上都表现良好，尽管 SVG 滤镜（令人惊讶地）拥有最深入的浏览器支持。</li>
</ul>
<p>在本文中，我们通过示例了解了为什么以及如何将阴影应用于 SVG 图标。你有没有这样做过，但它的方式与我们所看到的不同吗？你是否尝试过制作无法实现的阴影效果？请分享！</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            