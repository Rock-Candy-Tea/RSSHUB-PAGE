
---
title: 'CSS 奇思妙想 _ 全兼容的毛玻璃效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00cd727243b46779a25275a265d3e8d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 17:23:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00cd727243b46779a25275a265d3e8d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>通过本文，你能了解到</p>
<ol>
<li>最基本的使用 CSS <code>backdrop-filter</code> 实现磨砂玻璃(毛玻璃)的效果</li>
<li>在至今不兼容 <code>backdrop-filter</code> 的 firefox 浏览器，如何利用一些技巧性的操作，巧妙的同样实现毛玻璃效果，让这个效果真正能运用在业务当中</li>
</ol>
<h2 data-id="heading-0">什么是 <code>backdrop-filter</code></h2>
<p><code>backdrop-filter</code> CSS 属性可以让你为一个元素后面区域添加图形效果（如模糊或颜色偏移）。 因为它适用于元素背后的所有元素，为了看到效果，必须使元素或其背景至少部分透明。</p>
<p><code>backdrop-filter</code> 与 <code>filter</code> 非常类似，可以取的值都是一样的，但是一个是作用于整个元素，一个是只作用于元素后面的区域。</p>
<h3 data-id="heading-1"><code>backdrop-filter</code> 与 <code>filter</code> 对比</h3>
<p>我们使用 <code>backdrop-filter</code> 与 <code>filter</code> 同时实现一个毛玻璃效果作为对比，伪代码如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Normal<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-filter"</span>></span>filter<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-backdrop-filter"</span>></span>backdrop-filter<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.bg</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">image.png</span>);
    
    & > <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, .<span class="hljs-number">7</span>);
    &#125;
    <span class="hljs-selector-class">.g-filter</span> &#123;
        <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">6px</span>);
    &#125;
    <span class="hljs-selector-class">.g-backdrop-filter</span> &#123;
        backdrop-<span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">6px</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00cd727243b46779a25275a265d3e8d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://codepen.io/Chokcoco/pen/WNjebrr" target="_blank" rel="nofollow noopener noreferrer">CodePen Demo -- filter 与 backdrop-filter 对比</a></p>
<p>在 <code>backdrop-filter</code> 之前，想实现上述的只给元素背景添加滤镜效果还是非常困难的，并且，对于静态画面还好，如果背景还是可以滚动的动态背景，通常 CSS 是无能为力的。</p>
<p><code>backdrop-filter</code> 正是为了给元素后的内容添加滤镜而不影响元素本身而诞生的。使用它可以非常方便的实现磨砂玻璃效果（毛玻璃）！</p>
<h2 data-id="heading-2"><code>backdrop-filter</code> 的兼容性</h2>
<p><code>backdrop-filter</code> 其实已经诞生挺久了，然而，firefox 至今都不兼容它！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3844c5f068fb498e84759db843394e64~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于部分已经放弃了 IE 的 PC 端业务而言，firefox 还是需要兼容的，想要让使用 <code>backdrop-filter</code> 实现毛玻璃效果应用落地，firefox 的兼容问题必须得解决。</p>
<h2 data-id="heading-3">在 firefox 中实现毛玻璃效果</h2>
<p>OK，本文的重点就是在于如何在 firefox 中，不使用 <code>backdrop-filter</code> 而尽可能的还原毛玻璃的效果。</p>
<p>首先看一下，如果是正常使用  <code>backdrop-filter</code>，还是上述的例子效果如下，是没有毛玻璃效果的：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/123533146-97893900-d745-11eb-9c38-a0e485cb71a8.png" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">使用 background-attachment: fixed 兼容静态背景图</h3>
<p>如果在 firefox 上想使用毛玻璃效果。应用毛玻璃元素的背景只是一张静态背景图，其实方法是有很多的。</p>
<p>我们只需在元素的背后，叠加一张同样的图片，利用 <code>background-attachment: fixed</code> 将叠加在元素下面的图片定位到与背景相同的坐标，再使用 <code>filter: blur()</code> 对其进行模糊处理即可。</p>
<p>伪代码如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-glossy"</span>></span>frosted glass effect <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS">$<span class="hljs-selector-tag">img</span>: <span class="hljs-string">'https://static.pexels.com/photos/373934/pexels-photo-373934.jpeg'</span>;

<span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">$img</span>);
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-attribute">background-attachment</span>: fixed;
    <span class="hljs-attribute">background-size</span>: cover;
&#125;

<span class="hljs-selector-class">.g-glossy</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.5</span>);
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;
    
    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">$img</span>);
        <span class="hljs-attribute">background-repeat</span>: no-repeat;
        <span class="hljs-attribute">background-attachment</span>: fixed;
        <span class="hljs-attribute">background-size</span>: cover;
        <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">10px</span>);
        <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/123533707-2f892180-d74a-11eb-8317-4ea44965a6ad.png" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此方法也是在没有 <code>backdrop-filter</code> 之前，在各个浏览器想实现简单毛玻璃效果最常用的方法之一。</p>
<p><a href="https://codepen.io/Chokcoco/pen/XWRrVma" target="_blank" rel="nofollow noopener noreferrer">CodePen Demo -- 使用 background-attachment: fixed | filter: bulr() 实现毛玻璃效果</a></p>
<h4 data-id="heading-5">使用 background-attachment: fixed 兼容静态背景图的缺点</h4>
<p>不过这种方法也有两个缺点：</p>
<ol>
<li>由于使用了伪元素叠加了一层背景，因为层级关系，父元素的 background 是在最下层的，所以元素本身的背景色其实并没有被充分体现，可以对比下两种方法的实际效果图：</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/8554143/123607540-9123bb80-d830-11eb-8a7e-d6d9f4c861af.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方案是再通过另外一个伪元素再叠加一层背景色，这个背景色应该是原本赋值给父元素本身的。</p>
<p>叠加之后的效果如下：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/123610266-03959b00-d833-11eb-990f-10ceb0230180.png" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://codepen.io/Chokcoco/pen/abWbzKG" target="_blank" rel="nofollow noopener noreferrer">CodePen Demo -- 使用 background-attachment: fixed | filter: bulr() 实现毛玻璃效果优化</a></p>
<ol start="2">
<li>上述效果已经非常接近了，硬要挑刺的话，就是应用了模糊滤镜的伪元素的边缘有白边瑕疵，这一点其实是滤镜本身的问题，也非常好解决，我们只需要将伪元素的范围扩大一点即可：</li>
</ol>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-glossy</span> &#123;
    <span class="hljs-attribute">overflow</span>: hidden;
    ....
    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: -<span class="hljs-number">100px</span>;
        <span class="hljs-attribute">left</span>: -<span class="hljs-number">100px</span>;
        <span class="hljs-attribute">right</span>: -<span class="hljs-number">100px</span>;
        <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">100px</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定位的代码由 <code>top: 0px;</code> 改为 <code>top: -100px</code>，四个方位都是如此即可。如此一来，就能做到基本上是百分百的模拟。</p>
<h3 data-id="heading-6">使用 <code>moz-element()</code> 配合 <code>filter: blur()</code> 实现复杂背景毛玻璃效果</h3>
<p>下面这种方法就非常巧妙了，正常而言，运用毛玻璃效果的背景元素，都不是一张图片那么简单！背后通常都是整个页面复杂的结构，多层 DOM 的嵌套。</p>
<p>那么通过叠加一张简单的图片，就无法奏效了，我们得想办法模拟整个 DOM 元素。</p>
<p>而恰好，在 Firefox 中，有这么一个属性 -- <code>-moz-element()</code>。</p>
<p>何为 <code>-moz-element()</code>？<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/element()" target="_blank" rel="nofollow noopener noreferrer">MDN-element</a> 的解释是，CSS 函数 <code>element()</code> 定义了一个从任意的 HTML 元素中生成的图像 <code><image></code> 值。该图像值是实时的，这意味着如果被指定的 HTML 元素被更改，应用了该属性的元素的背景也会相应更改。</p>
<p>它其实是个草案规范，但是一直以来，只有 Firefox 支持它 -- <a href="https://caniuse.com/css-element-function" target="_blank" rel="nofollow noopener noreferrer">CAN I USE -- CSS element()</a>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4204c0fee5c24d769c395ab449f24908~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它有什么作用呢？</p>
<h3 data-id="heading-7"><code>-moz-element()</code> 如何使用</h3>
<p>那么 <code>-moz-element()</code> 如何使用呢？简而言之，它能够复制一个元素内部渲染出来的 UI，并且能够实时同步变化。</p>
<p>假设我们有这样一个简单的结构，元素背景和内容都在运动：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-normal"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Content<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-normal</span> &#123;
    <span class="hljs-attribute">margin</span>: auto;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">animation</span>: change <span class="hljs-number">5s</span> infinite;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(deeppink, yellowgreen);
&#125;

<span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">animation</span>: move <span class="hljs-number">5s</span> infinite;
&#125;

<span class="hljs-keyword">@keyframes</span> change &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">0</span>);
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">hue-rotate</span>(<span class="hljs-number">360deg</span>);
    &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> move &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(<span class="hljs-number">150px</span>, <span class="hljs-number">150px</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的效果大概是这样：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/123617162-8d486700-d839-11eb-9b0c-f090cbc52abd.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们就假设这个结构就是我们页面某一块的内容，然后，我们就可以使用 <code>background: -moz-element(#id)</code> 这种方式，将这个元素内绘制的 UI 内容完全拷贝至另外一个元素，看看效果。</p>
<p>我们添加一个元素 <code><div class="g-element-copy"></div></code>，在这个元素内模拟 <code>#bg</code> 内的内容：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-normal"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Content<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-element-copy"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-element-copy</span> &#123;
    <span class="hljs-attribute">margin</span>: auto;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    // 核心代码
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">-moz-element</span>(#bg);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它可以完全复制另外一个元素内绘制出来的 UI，并且能追踪实时变化：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/123618303-a69de300-d83a-11eb-9ddd-4b6b929fcdac.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://codepen.io/Chokcoco/pen/jOmOPPL" target="_blank" rel="nofollow noopener noreferrer">CodePen Demo -- -moz-element Demo(Firefox Only)</a></p>
<h2 data-id="heading-8">在 firefox 中使用 element 复制 UI，用作毛玻璃元素背景</h2>
<p>这样，有了上面的铺垫，下面的内容就比较好理解了。</p>
<p>和上述的 <code>background-attachment: fixed</code> 方案对比，我们还是通过伪元素叠加一层背景，只不过背景内的内容由单纯一张图片，变成了由 <code>-moz-element()</code> 复制的整段 UI 内容。</p>
<p>其次，上面的方案我们使用 <code>background-attachment: fixed</code> 使背景图和伪元素内叠加的图片的位置对齐，在这里，我们需要借助 Javascript 进行简单的运算，确定背景内容元素的相关位置，计算对齐量。</p>
<p>来看这样一个 DEMO：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>模拟真实 DOM<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-glossy"</span>></span>frosted glass effect <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-glossy-firefox"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，<code>.g-glossy</code> 是在正常情况下 <code>backdrop-filter</code> 兼容时，我们的毛玻璃元素，而 <code>.g-glossy-firefox</code> 则是不兼容 <code>backdrop-filter</code> 时，我们需要模拟整个 DOM 背景 UI时候的元素，可以通过 CSS 特性检测 <code>CSS @support</code> 进行控制：</p>
<p>核心 CSS 代码：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.bg</span> &#123;
    // 整个页面的 DOM 结构
&#125;

<span class="hljs-selector-class">.g-glossy</span> &#123;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.5</span>);
    backdrop-<span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">10px</span>);
&#125;

<span class="hljs-selector-class">.g-glossy-firefox</span> &#123;
    <span class="hljs-attribute">display</span>: none;
&#125;

<span class="hljs-keyword">@supports</span> (<span class="hljs-attribute">background</span>: -moz-element(#bg)) &#123;
    <span class="hljs-selector-class">.g-glossy-firefox</span> &#123;
        <span class="hljs-attribute">display</span>: block;
        <span class="hljs-attribute">position</span>: fixed;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">-moz-element</span>(#bg) no-repeat;
        <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">10px</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单解读一下：</p>
<ol>
<li>对于兼容 <code>backdrop-filter</code> 的，<code>.g-glossy</code> 内的代码将直接生效，并且 <code>.g-glossy-firefox</code> 不会展示</li>
<li>对于 Firefox 浏览器，因为 <code>backdrop-filter</code> 必然不兼容，所以 <code>.g-glossy</code> 内的 <code>backdrop-filter: blur(10px)</code> 不会生效，而 <code>@supports (background: -moz-element(#bg))</code> 内的样式会生效，此时 <code>.g-glossy-firefox</code> 将会利用 <code>background: -moz-element(#bg) no-repeat;</code> 模拟 id 为 <code>bg</code> 的元素</li>
</ol>
<p>当然，这里我们需要借助一定的 JavaScript 代码，计算我们的模拟页面 UI 的元素 <code>.g-glossy-firefox</code> 相对它模拟的 <code>#bg</code> 元素，也就是页面布局的一个定位偏差：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">$(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> blur = $(<span class="hljs-string">'.g-glossy-firefox'</span>)[<span class="hljs-number">0</span>].style;
        <span class="hljs-keyword">let</span> offset = $(<span class="hljs-string">'.g-glossy'</span>).eq(<span class="hljs-number">0</span>).offset();

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateBlur</span>(<span class="hljs-params"></span>) </span>&#123;
            blur.backgroundPosition = 
                <span class="hljs-string">`<span class="hljs-subst">$&#123;-<span class="hljs-built_in">window</span>.scrollX - offset.left&#125;</span>px `</span> + 
                <span class="hljs-string">`<span class="hljs-subst">$&#123;-<span class="hljs-built_in">window</span>.scrollY - offset.top&#125;</span>px`</span>;
        &#125;
        <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'scroll'</span>, updateBlur, <span class="hljs-literal">false</span>), updateBlur();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK，至此，我们就能完美的在 Firefox 上也实现毛玻璃的效果了：</p>
<p><img src="https://user-images.githubusercontent.com/8554143/123645631-14f19e00-d859-11eb-9aaa-3b0032da89e0.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它相对于上面的第一种方案而言，最大的不同之处在于，它可以模拟各式各样的背景元素，背景元素可以不仅仅只是一张图片！它可以是各种复杂的结构！</p>
<p>这种方案是我的 CSS 群中，<code>风海流</code> 同学提供的一种思路，非常的巧妙，并且，他自己也对这种方案进行了完整的阐述，你可以戳这里看看：<a href="https://chaoli.club/index.php/5347" target="_blank" rel="nofollow noopener noreferrer">在网页中实现标题栏「毛玻璃」效果</a>，本文也是经过他的同意，重新整理发出。</p>
<p>上述效果的完整代码，你可以戳这里：</p>
<p><a href="https://github.com/chokcoco/iCSS/issues/124" target="_blank" rel="nofollow noopener noreferrer">CodePen Demo -- 兼容 Firefox 的复杂背景毛玻璃（磨砂玻璃）效果</a></p>
<h2 data-id="heading-9">总结一下</h2>
<p>简单对上述内容进行一个总结：</p>
<ul>
<li>你可以使用 <code>backdrop-filter</code> 对兼容它的浏览器非常简单的实现毛玻璃（磨砂玻璃）效果</li>
<li>对于不兼容 <code>backdrop-filter</code> 的浏览器，如果它只是简单背景，可以使用 <code>background-attachment: fixed</code> 配合 <code>filter: blur()</code> 进行模拟</li>
<li>对于 firefox 浏览器，你还可以使用 <code>moz-element()</code> 配合 <code>filter: blur()</code> 实现复杂背景毛玻璃效果</li>
<li>对于不兼容的上述 3 种效果的其他浏览器，设置了毛玻璃效果的元素，可以通过设置类似 <code>background: rgba(255, 255, 255, 0.5)</code> 的样式，使之回退到半透明效果，也算一种非常合理的降级效果，不会引起 Bug</li>
</ul>
<h2 data-id="heading-10">最后</h2>
<p>好了，本文到此结束，希望对你有帮助 :)</p>
<p>想 Get 到最有意思的 CSS 资讯，千万不要错过我的公众号 -- <strong>iCSS前端趣闻</strong> 😄</p>
<p>更多精彩 CSS 技术文章汇总在我的 <a href="https://github.com/chokcoco/iCSS" target="_blank" rel="nofollow noopener noreferrer">Github -- iCSS</a> ，持续更新，欢迎点个 star 订阅收藏。</p>
<p>如果还有什么疑问或者建议，可以多多交流，原创文章，文笔有限，才疏学浅，文中若有不正之处，万望告知。</p></div>  
</div>
            