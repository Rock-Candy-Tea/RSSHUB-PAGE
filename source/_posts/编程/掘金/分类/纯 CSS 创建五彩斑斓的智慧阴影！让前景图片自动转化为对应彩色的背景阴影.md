
---
title: '纯 CSS 创建五彩斑斓的智慧阴影！让前景图片自动转化为对应彩色的背景阴影'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bf9d69283e343e58cb217a9b5fffeca~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 02:18:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bf9d69283e343e58cb217a9b5fffeca~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://www.kirupa.com/html5/creating_colorful_smart_shadows.htm" target="_blank" rel="nofollow noopener noreferrer">Creating Colorful, Smart Shadows</a></li>
<li>原文作者：<a href="https://www.kirupa.com/me/index.htm" target="_blank" rel="nofollow noopener noreferrer">kirupa</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/creating_colorful_smart_shadows.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：</li>
</ul>
</blockquote>
<p>几天前，我在 Home Depot（aka <a href="http://en.wikipedia.org/wiki/Toys_R_Us" target="_blank" rel="nofollow noopener noreferrer">Toys "R" Us</a> for big kids）处发现，他们有一个巨大的显示器来展示所有这些彩色的供销售的电灯泡！其中一项是y一组在电视后面的智能灯泡。它们会在电视的后面投影近似于电视在播出的内容的彩色阴影，与以下内容 <a href="https://www.philips-hue.com/en-us/p/hue-play-hdmi-sync-box-/046677555221" target="_blank" rel="nofollow noopener noreferrer">类似</a>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bf9d69283e343e58cb217a9b5fffeca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意电视后面发生的事情。屏幕前景中显示的颜色会被灯泡投影为电视机身后面的彩色阴影。随着屏幕上的颜色发生变化，投射在背景中的颜色也会发生变化。真的很酷，对吧？</p>
<p>自然，看到这个之后，我的第一个想法是，我们是否可以使用网络技术创建一个足够智能以模仿前景色的彩色阴影。事实证明，我们完全可以只使用 CSS 构建出这个案例。在本文中，我们将了解如何创建这种效果。</p>
<p>走起！</p>
<h1 data-id="heading-0">让它变成真的！</h1>
<p>正如您将在以下部分中看到的，使用 CSS 创建这种彩色阴影似乎是一项艰巨的任务（当然，只是就刚开始而言）。当我们开始进入它并将这个任务的核心分解成更小的部分时，我们其实能够发现这真的很容易实现。在接下来的几节中，我们将创建以下示例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64594b3e1b6947ac9b800d15e7434bd8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你应该看到的是一张寿司的图片，后面出现了一个五颜六色的阴影。（只是为了强调我们正在做这一切，阴影被添加了脉冲的效果）抛开示例，让我们深入了解实现，看看 HTML 和 CSS 如何让这一切变为现实！</p>
<h2 data-id="heading-1">展示我们的照片</h2>
<p>展示我们的寿司的图片对应的 HTML 起始没什么特别的：</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"colorfulShadow sushi"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们有一个父 div 元素，包含一个负责显示寿司的子 div 元素。我们显示寿司的方式是将其指定为背景图像，并由以下 <strong>.sushi</strong> 样式规则处理：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.sushi</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"https://www.kirupa.com/icon/1f363.svg"</span>);
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-attribute">background-size</span>: contain;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在此样式规则中，我们将 div 的大小指定为 150 x 150 像素，并在其上设置 <code>background-image</code> 和相关的其他属性。就目前而言，我们所看到的 HTML 和 CSS 会给我们提供如下所示的内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ed452111de24b10a161a2cdd6c548b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">现在是阴影时间</h2>
<p>现在我们的图像出现了，剩下的就是我们定义阴影这一有趣的部分。我们要定义阴影的方法是指定一个子伪元素（使用 <code>::after</code>），它将做三件事：</p>
<ol>
<li>直接定位在我们的形象后面；</li>
<li>继承与父元素相同的背景图片；</li>
<li>依靠滤镜应用多彩的阴影效果；</li>
</ol>
<p>这三件事是通过以下两条样式规则完成的：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.colorfulShadow</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
&#125;

<span class="hljs-selector-class">.colorfulShadow</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: inherit;
    <span class="hljs-attribute">background-position</span>: center center;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们花一点时间来看看这里发生了些什么：先注意每一个属性和对应的值，有一些值得注意的标记是 <code>background</code> 和 <code>filter</code>。<code>background</code> 属性使用了 <code>inherit</code> 继承父元素，意味着能够继承父元素的背景：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.colorfulShadow</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: inherit;
    <span class="hljs-attribute">background-position</span>: center center;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们为 <code>filter</code> 属性定义了两个过滤的属性，分别是 <strong>drop-shadow</strong> 和 <strong>blur</strong>：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.colorfulShadow</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: inherit;
    <span class="hljs-attribute">background-position</span>: center center;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的 <strong>drop-shadow</strong> 过滤器设置为显示不透明度为 50% 的黑色阴影，而我们的 <strong>blur</strong> 过滤器会将我们的伪元素模糊 20px。 这两个过滤器的组合最终创建了彩色的阴影，当应用这两个样式规则时，该阴影现在将出现在我们的寿司图像后面：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c50a4ed5121b4f408e513589d248ff18~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这一点上，我们已经完成了。为完整起见，如果我们想要彩色阴影缩放的动画，如下 CSS 代码的添加能够助力我们实现目标：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.colorfulShadow</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
&#125;

<span class="hljs-selector-class">.colorfulShadow</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: inherit;
    <span class="hljs-attribute">background-position</span>: center center;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;

    <span class="hljs-comment">/* animation time! */</span>
    <span class="hljs-attribute">animation</span>: oscillate <span class="hljs-number">1s</span> <span class="hljs-built_in">cubic-bezier</span>(.<span class="hljs-number">17</span>, .<span class="hljs-number">67</span>, .<span class="hljs-number">45</span>, <span class="hljs-number">1.32</span>) infinite alternate;
&#125;

<span class="hljs-keyword">@keyframes</span> oscillate &#123;
    <span class="hljs-selector-tag">from</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
    &#125;

    <span class="hljs-selector-tag">to</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.3</span>, <span class="hljs-number">1.3</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您想要一些交互性而没有不断循环的动画，您还可以使用 CSS 过渡来更改阴影在某些动作（如悬停）上的行为方式。困难的部分是像对待在 HTML 中明确定义或使用 JavaScript 动态创建的任何其他元素一样对待伪元素。唯一的区别是这个元素是完全使用 CSS 创建的！</p>
<h1 data-id="heading-3">结语</h1>
<h2 data-id="heading-4">小结</h2>
<p>伪元素允许我们使用 CSS 来完成一些历史上属于 HTML 和 JavaScript 领域的元素创建任务。对于我们多彩而智能的阴影，我们能够依靠父元素来设置背景图像。这使我们能够轻松定义一个既继承了父元素的背景图像细节，又允许我们为其设置一系列属性以实现模糊和阴影效果的子伪元素。虽然所有这些都很好，并且我们最大限度地减少了大量复制和粘贴，但这种方法不是很灵活。</p>
<p>如果我想将这样的阴影应用到一个不只是带有背景图像的空元素上怎么办？如果我有一个像 <strong>Button</strong> 或 <strong>ComboBox</strong> 这样的 HTML 元素想要应用这种阴影效果怎么办？一种解决方案是依靠 JavaScript 在 DOM 中复制适当的元素，将它们放置在前景元素下方，应用过滤器，然后就可以了。虽然这有效，但考虑到该过程的复杂程度，实在是有些不寒而栗。太糟糕了，JavaScript 没有等效的 <a href="https://docs.microsoft.com/en-us/dotnet/api/system.windows.media.imaging.rendertargetbitmap?view=net-5.0" target="_blank" rel="nofollow noopener noreferrer">renderTargetBitmap</a> 这种能够把我们的视觉效果渲染成位图，然后你可以做任何你想做的事的 API…… 🥶</p>
<p>以上内容为译文翻译，下面为一些拓展：</p>
<hr>
<h2 data-id="heading-5">拓展</h2>
<p>说实在的，我们其实并不需要那么多复杂的内容，图片可以是任意的，比如说 PNG、SVG，最终精简后，HTML 代码仅仅为任意一个元素，附上 <code>style</code> 规定图片地址与大小：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shadowedImage"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--data-width: 164px; --data-height: 48px; --data-image: url('https://sf3-scmcdn2-tos.pstatp.com/xitu_juejin_web/dcec27cc6ece0eb5bb217e62e6bec104.svg');"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS 代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.shadowedImage</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">var</span>(--data-width);
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">var</span>(--data-height);
    <span class="hljs-attribute">max-height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">var</span>(--data-image);
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-attribute">background-size</span>: contain;
&#125;

<span class="hljs-selector-class">.shadowedImage</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: inherit;
    <span class="hljs-attribute">background-position</span>: center center;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">示例代码</h3>
<p>一段示例代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span>
          <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"ie=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.shadowedImage</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
        &#125;

        <span class="hljs-selector-class">.shadowedImage</span><span class="hljs-selector-pseudo">::after</span> &#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">background</span>: inherit;
            <span class="hljs-attribute">background-position</span>: center center;
            <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">drop-shadow</span>(<span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.50</span>)) <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
            <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;

            <span class="hljs-comment">/* animation time! */</span>
            <span class="hljs-attribute">animation</span>: oscillate <span class="hljs-number">1s</span> <span class="hljs-built_in">cubic-bezier</span>(.<span class="hljs-number">17</span>, .<span class="hljs-number">67</span>, .<span class="hljs-number">45</span>, <span class="hljs-number">1.32</span>) infinite alternate;
        &#125;

        <span class="hljs-keyword">@keyframes</span> oscillate &#123;
            <span class="hljs-selector-tag">from</span> &#123;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>);
            &#125;

            <span class="hljs-selector-tag">to</span> &#123;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.1</span>, <span class="hljs-number">1.1</span>);
            &#125;
        &#125;

        <span class="hljs-selector-class">.shadowedImage</span> &#123;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-built_in">var</span>(--data-width);
            <span class="hljs-attribute">height</span>: <span class="hljs-built_in">var</span>(--data-height);
            <span class="hljs-attribute">max-height</span>: <span class="hljs-number">150px</span>;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">var</span>(--data-image);
            <span class="hljs-attribute">background-repeat</span>: no-repeat;
            <span class="hljs-attribute">background-size</span>: contain;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shadowedImage"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--data-width: 164px; --data-height: 48px; --data-image: url('https://sf3-scmcdn2-tos.pstatp.com/xitu_juejin_web/dcec27cc6ece0eb5bb217e62e6bec104.svg');"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shadowedImage"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--data-width: 164px; --data-height: 164px; --data-image: url('https://sf1-dycdn-tos.pstatp.com/img/bytedance-cn/4ac74bbefc4455d0b350fff1fcd530c7~noop.image');"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shadowedImage"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--data-width: 164px; --data-height: 164px; --data-image: url('https://sf1-ttcdn-tos.pstatp.com/img/bytedance-cn/4bcac7e2843bd01c3158dcaefda77ada~noop.image');"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">示例效果</h3>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4d3efc354c4c57a405ca95bbd399d6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            