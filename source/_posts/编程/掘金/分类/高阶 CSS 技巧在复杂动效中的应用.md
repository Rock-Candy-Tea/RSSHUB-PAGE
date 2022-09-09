
---
title: '高阶 CSS 技巧在复杂动效中的应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f6c7748c8241ae91ed9ad47e8b212d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 22:42:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f6c7748c8241ae91ed9ad47e8b212d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
</blockquote>
<p>最近我在 CodePen 上看到了这样一个有意思的动画：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f6c7748c8241ae91ed9ad47e8b212d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bbb1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>整个动画效果是在一个标签内，借助了 SVG PATH 实现。其核心在于对<strong>渐变</strong>（Gradient）的究极利用。</p>
<p>完整的代码你可以看看这里 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fpropjockey%2Fpen%2FVwKQENg" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/propjockey/pen/VwKQENg" ref="nofollow noopener noreferrer">CodePen DEMO -- to the future 🍻 By Jane Ori</a>]</p>
<p>源代码还是非常非常复杂的，并且叠加了复杂的 SVG PATH 路径。</p>
<p>我尝试着将其稍微拆分成几小块，运用不同的 CSS 高阶技巧从另外一个方面方向重新实现了一遍。因为整个过程还是有非常多有意思的 CSS 技巧，本文就给大家分享一下。</p>
<h3 data-id="heading-0">实现上半部分背景加落日</h3>
<p>首先，我们来实现上半部分的背景加落日效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a70640ea67646c3bf0f9d456e416575~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以先停顿思考下，这里让你来实现，会如何去做？需要多少个标签？</p>
<p>好的，这里，我们利用一个 DOM 标签去完成这个图形：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-bg"</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>背景色好做，使用一个径向渐变或者线性渐变即可：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此，先实现一个背景：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d1ad2d140c3459884aff16f4d1b9760~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，接下来，我们使用其中一个<strong>伪元素实现落日</strong>的效果。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
    
    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">20%</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">10%</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">10%</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">10%</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color3), <span class="hljs-built_in">var</span>(--color4) <span class="hljs-number">55%</span>, transparent <span class="hljs-number">55.1%</span>, transparent);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a501bbd0e0ab49e99d951fce1318cfd0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里，我觉得算是出现了第一个技巧，也就是这一行代码 <code>background: radial-gradient(circle at 50% 100%, var(--color3), var(--color4) 55%, transparent 55.1%, transparent)</code>，它用于在一个矩形元素中，通过径向渐变从实色到透明色，实现一个半圆。</p>
<p><strong>技巧 1：可以利用径向渐变，在一个矩形 DIV 元素中，通过径向渐变从实色到透明色的变化，实现一个半圆</strong>。</p>
<p>我们继续，接下来，切割这个圆形，得到这样一种效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3409711598a84c9eb8201c8810ed8aa9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意，这里需要裁剪切割的地方不是白色，而是透明的，需要透出后面的背景色。</p>
<p>毫无疑问，这里需要使用  mask 来完成，我们给伪元素加上 mask：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
    
    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">20%</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">10%</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">10%</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">10%</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color3), <span class="hljs-built_in">var</span>(--color4) <span class="hljs-number">55%</span>, transparent <span class="hljs-number">55.1%</span>, transparent);
        <span class="hljs-attribute">mask</span>: <span class="hljs-built_in">linear-gradient</span>(to top,
            <span class="hljs-number">#000</span> <span class="hljs-number">0</span>, <span class="hljs-number">#000</span> <span class="hljs-number">10%</span>,
            transparent <span class="hljs-number">10%</span>, transparent <span class="hljs-number">13%</span>,
            <span class="hljs-number">#000</span> <span class="hljs-number">13%</span>, <span class="hljs-number">#000</span> <span class="hljs-number">20%</span>,
            transparent <span class="hljs-number">20%</span>, transparent <span class="hljs-number">22%</span>,
            <span class="hljs-number">#000</span> <span class="hljs-number">22%</span>, <span class="hljs-number">#000</span> <span class="hljs-number">35%</span>,
            transparent <span class="hljs-number">35%</span>, transparent <span class="hljs-number">36%</span>,
            <span class="hljs-number">#000</span> <span class="hljs-number">36%</span>, <span class="hljs-number">#000</span> <span class="hljs-number">100%</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就实现了这个效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2841d2c1dc2b434387cb1515b94596bd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，引出了第二个技巧：</p>
<p><strong>技巧 2：利用 mask 可以对图形进行裁剪，被裁剪区域将会变成透明。</strong></p>
<p>好，接下来，我们需要在整个图形上再叠加上竖形黑色条纹。这个其实也可以用 mask，如果整个图形后面还有一层黑色背景。</p>
<p>当然，这里我们也可以把另外一个伪元素利用起来，利用它，通过多重线性渐变（repeating-linear-gradient）实现这里的竖形黑色条纹。</p>
<p>看看代码：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
    
    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // <span class="hljs-selector-tag">code</span> of sun
    &#125;

    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">repeating-linear-gradient</span>(<span class="hljs-number">90deg</span>, transparent <span class="hljs-number">0</span>, transparent <span class="hljs-number">3px</span>, <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>) <span class="hljs-number">4px</span>, <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>) <span class="hljs-number">5px</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，我们利用 <code>repeating-linear-gradient</code> 快速创建批量的竖形黑色条纹效果，得到这样的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c6451d7fd0449b8a41c2b402480a291~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，得到技巧 3。</p>
<p><strong>技巧 3：当你碰到大量重复有规律的线条，或者方块图形，你第一时间就应该想到在一个 DOM 中利用渐变而不是多个 DOM 去实现</strong></p>
<p>好，至此，我们整个上半部分就实现了。</p>
<h2 data-id="heading-1">利用 -webkit-box-reflect 实现倒影</h2>
<p>有了上面的基础，接下来我们要得到完整的背景：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a457cee502c746b69753d5547414e0f1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>怎么做呢？换个配色重新实现一遍吗？当然不是，这里我们利用 CSS 提供的倒影功能，可以快速完成这个操作。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
    -webkit-box-reflect: below;

    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // ...
    &#125;
    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们给 <code>.g-bg</code> 加一个 <code>-webkit-box-reflect: below</code>，意为下方的倒影：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/484d7ffc7e03424fbe3815720ef8dbef~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然是复制了一个一模一样的 <code>.g-bg</code> 出来，但是和我们要的效果还相差很多啊，怎么办呢？</p>
<p>别急，<code>-webkit-box-reflect: below</code> 还提供，倒影偏移距离，倒影遮罩等属性。</p>
<p>我们需要给下方的倒影，添加一个遮罩，修改一下 <code>-webkit-box-reflect</code> 的代码：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
    -webkit-box-reflect: below -<span class="hljs-number">50px</span> <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, .<span class="hljs-number">2</span>), transparent);

    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // ...
    &#125;
    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就得到了这样一种效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4557733dc68b42c4ad7b028ef473554d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，整个图形其实是半透明的，我们在背后叠加上一层我们想要的色彩渐变，可以利用 body 的伪元素：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">body</span> &#123;
    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">var</span>(--c5), <span class="hljs-built_in">var</span>(--c6));
    &#125;
&#125;
<span class="hljs-selector-class">.g-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">50%</span> <span class="hljs-number">100%</span>, <span class="hljs-built_in">var</span>(--color1), <span class="hljs-built_in">var</span>(--color2));
    -webkit-box-reflect: below -<span class="hljs-number">50px</span> <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, .<span class="hljs-number">2</span>), transparent);

    &<span class="hljs-selector-pseudo">::before</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // ...
    &#125;
    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        // ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>倒影通过半透明和背后的渐变背景叠加，这样，我们就完美实现了我们想要的整体背景效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c64ab7d572f42b89249be50e0bf54de~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bg10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，我们可以引出技巧 4。</p>
<p><strong>技巧 4：当出现重复的对称图形时，<code>-webkit-box-reflect</code> 也许能派上用场。</strong></p>
<h2 data-id="heading-2">利用 CSS 3D 动画实现线条动画</h2>
<p>好，主体背景完成了，下面，我们来试着实现 3D 线条动画：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2bbcbf8259e4ab8b879bc2db3029246~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>利用 CSS 3D，我们是可以实现这样一种效果的。我们一步一步来拆解。</p>
<p>首先，我们需要实现这样一种网格效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/624ac00a12f04f3da949150571640d6b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还记得上面的技巧 3 吗？当你碰到大量重复有规律的线条，或者方块图形，你第一时间就应该想到在一个 DOM 中利用渐变而不是多个 DOM 去实现。</p>
<p>这种效果，其实利用渐变一个标签就组足够了：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.grid</span> &#123;
    <span class="hljs-attribute">background</span>:
        <span class="hljs-built_in">repeating-linear-gradient</span>(<span class="hljs-built_in">var</span>(--c1), <span class="hljs-built_in">var</span>(--c1) <span class="hljs-number">1px</span>, transparent <span class="hljs-number">1px</span>, transparent <span class="hljs-number">20px</span>),
        <span class="hljs-built_in">repeating-linear-gradient</span>(<span class="hljs-number">90deg</span>, <span class="hljs-built_in">var</span>(--c1), <span class="hljs-built_in">var</span>(--c1) <span class="hljs-number">1px</span>, transparent <span class="hljs-number">1px</span>, transparent <span class="hljs-number">20px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅此而已，我们就能得到一个网格图。</p>
<p>好的，接下来，需要利用 transform 让他呈现一种 3D 视觉：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">perspective</span>: <span class="hljs-number">300px</span>;
&#125;
<span class="hljs-selector-class">.grid</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300vw</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">100vw</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">55vh</span>;
    <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
    <span class="hljs-attribute">background</span>:
        <span class="hljs-built_in">repeating-linear-gradient</span>(<span class="hljs-built_in">var</span>(--c1), <span class="hljs-built_in">var</span>(--c1) <span class="hljs-number">1px</span>, transparent <span class="hljs-number">1px</span>, transparent <span class="hljs-number">20px</span>),
        <span class="hljs-built_in">repeating-linear-gradient</span>(<span class="hljs-number">90deg</span>, <span class="hljs-built_in">var</span>(--c1), <span class="hljs-built_in">var</span>(--c1) <span class="hljs-number">1px</span>, transparent <span class="hljs-number">1px</span>, transparent <span class="hljs-number">20px</span>);
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
    <span class="hljs-attribute">transform-origin</span>: <span class="hljs-number">50%</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc861535a2004c27b958a46f6ddf8110~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于，整体绕 X 轴旋转 90°，所以这里的 <code>top: 55vh</code> 很重要。</p>
<p>由于旋转圆心是 <code>50% 0</code>，如果是 <code>top: 50vh</code>， 相当于整个图形会垂直于屏幕，如果 <code>top</code> 值小于 50vh，则整个网格是一种向上的翻转效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc0bee50b8234411b02df150dd2fee9c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着，我们需要让其运动起来。</p>
<p>我们尝试添加一个 translateZ 的运动动画：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.grid</span> &#123;
    // ...
    <span class="hljs-attribute">animation</span>: move <span class="hljs-number">10s</span> infinite linear;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, -<span class="hljs-number">600px</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">600px</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b4bf0e7b3c4273b5ec32f3eca92d3a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bbb4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里有个很严重的问题，仅仅只是单个动画，很难做到无限循环衔接。</p>
<p>因此，我们需要再加一组 Grid，动画两组动画先后出发，来实现整个动画的衔接。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"grid"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.grid</span> &#123;
    // ...
    <span class="hljs-attribute">animation</span>: move <span class="hljs-number">10s</span> infinite linear;
&#125;
<span class="hljs-selector-class">.grid</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">animation</span>: move <span class="hljs-number">10s</span> infinite -<span class="hljs-number">5s</span> linear;
&#125;
<span class="hljs-keyword">@keyframes</span> move &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, -<span class="hljs-number">600px</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">600px</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过这么一种方式：</p>
<ol>
<li>两组一模一样的动画，整个位移长度是 1200px，整个动画持续 10s，缓动为线性动画</li>
<li>第一组出发 5s 后（刚好行进了 600px），第二组再出发，如此 infinite 反复</li>
<li>整个 3D 动画，在近屏幕端看上去就是无限循环的一种效果</li>
<li>这里运用的是 <code>-5s</code>，意思是提前 5s 出发，实际动画效果也就不会有等待感</li>
</ol>
<p>如下（这里，为了录制 GIF，我整体是加快了动画的速度）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2bbcbf8259e4ab8b879bc2db3029246~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，近屏幕端的动画是连续不断的，只是远端会出现一定的闪烁。这里，可以得到技巧 5。</p>
<p><strong>技巧 5：利用 2 组动画可以将一些有效在单组内的动画无法实现的连续效果实现</strong></p>
<p>这样，叠加上上面的效果，我们就得到了这样一种效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b73cce3b350045eb8c2de19cfa6025bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，很接近了。目前线条动画远处还有一些抖动。刚好，我们还差一个山峰的效果，可以把这块瑕疵挡住。</p>
<h2 data-id="heading-3">使用 box-shadow 及 SVG 滤镜实现山脉效果</h2>
<p>OK，最后，我们在屏幕中间再叠加上一个山峰的效果就好。</p>
<p>这里，原效果使用的是一长串导出的 SVG 路径。如果我们没有这种资源，只是想简单模拟一下效果。这里我给出一种可能可行的方案。</p>
<p>我首先利用一个圆角矩形进行旋转，再配合容器的 <code>overflow: hidden</code> 得到一个小山峰：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-mountain"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-mountain</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">15%</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">42%</span>;
    <span class="hljs-attribute">overflow</span>: hidden;
    
    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">78%</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#011d3f</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">15vw</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">15vw</span>;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">45deg</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大概是这样一种效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7637092a0af34b17ad0c5b9a5297d5c7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，如果我们想重复得到多个这样的图形，该怎么办呢？多个 DOM 吗？不是的，这里我们可以利用 <code>box-shadow</code> 复制自身。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-mountain</span> &#123;
    // ...
    &<span class="hljs-selector-pseudo">::after</span> &#123;
        <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">78%</span>;
        <span class="hljs-attribute">background</span>: <span class="hljs-number">#011d3f</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">15vw</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">15vw</span>;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">45deg</span>);
        <span class="hljs-attribute">box-shadow</span>: 
            -<span class="hljs-number">3vw</span> -<span class="hljs-number">3vw</span>, <span class="hljs-number">5vw</span> <span class="hljs-number">5vw</span>, 
            <span class="hljs-number">10vw</span> <span class="hljs-number">10vw</span> <span class="hljs-number">0</span> <span class="hljs-number">3vw</span>, <span class="hljs-number">15vw</span> <span class="hljs-number">20vw</span> <span class="hljs-number">0</span> <span class="hljs-number">4vw</span>, 
            <span class="hljs-number">22vw</span> <span class="hljs-number">22vw</span> <span class="hljs-number">0</span> <span class="hljs-number">6vw</span>, <span class="hljs-number">25vw</span> <span class="hljs-number">30vw</span> <span class="hljs-number">0</span> <span class="hljs-number">12vw</span>, 
            <span class="hljs-number">38vw</span> <span class="hljs-number">36vw</span> <span class="hljs-number">0</span> <span class="hljs-number">1vw</span>, <span class="hljs-number">41vw</span> <span class="hljs-number">39vw</span> <span class="hljs-number">0</span> <span class="hljs-number">3vw</span>, 
            <span class="hljs-number">45vw</span> <span class="hljs-number">45vw</span> <span class="hljs-number">0</span> <span class="hljs-number">2vw</span>, <span class="hljs-number">52vw</span> <span class="hljs-number">52vw</span> <span class="hljs-number">0</span> <span class="hljs-number">4vh</span>, 
            <span class="hljs-number">55vw</span> <span class="hljs-number">55vw</span> <span class="hljs-number">0</span> <span class="hljs-number">1.5vw</span>, <span class="hljs-number">61vw</span> <span class="hljs-number">61vw</span> <span class="hljs-number">0</span> <span class="hljs-number">0.5vw</span>, <span class="hljs-number">68vw</span> <span class="hljs-number">68vw</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就用一个标签，实现了一系列的“山”：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c82b2b2a9f774d1b984d74b72eff8381~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，我们得到了技巧 6。</p>
<p><strong>技巧 6：<code>box-shadow</code> 可以有效的复制自身，并且，可以利用第四个参数，扩散半径，来等比例放大自身。</strong></p>
<p>其实，到这里，一个比较粗糙的还原就完成了。当然，有一点小问题是，山峰明显不应该是一条条直线。能否营造出一种弯弯曲曲的外轮廓效果呢？</p>
<p>这个使用纯 CSS 是比较难实现的，当然，好在这里我们可以运用上之前给大家多次提及过的 SVG 滤镜。</p>
<p>利用 <code>feTurbulence</code> 可以有效实现一些波形纹理效果。并且可以通过 CSS filter 快速引入。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"g-mountain"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"filter"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">feTurbulence</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"turbulence"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"fractalNoise"</span> <span class="hljs-attr">baseFrequency</span>=<span class="hljs-string">".03"</span> <span class="hljs-attr">numOctaves</span>=<span class="hljs-string">"20"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">feDisplacementMap</span> <span class="hljs-attr">in</span>=<span class="hljs-string">"SourceGraphic"</span> <span class="hljs-attr">scale</span>=<span class="hljs-string">"30"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">filter</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.g-mountain</span> &#123;
    // ...
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'#filter'</span>);   

    &<span class="hljs-selector-pseudo">::after</span> &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，原本，整齐划一的直线，立马变得杂乱无章了起来，看起来更像是山脉的轮廓：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1fcba585bd144ec901e77534bda0f8f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，我们得出了技巧 7。</p>
<p><strong>技巧 7：SVG 滤镜可以通过 CSS 滤镜快速引入，SVG 滤镜可以实现一些 CSS 完成不了的事情，譬如一些特殊的纹理，波纹，烟雾颗粒感等等效果。</strong></p>
<p>好，至此，我们就大体上按照自己的理解，重新实现了一遍上述的动画，再做一些简单的修饰，最终的效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c52bd4a504c4cf3b8168568bfee5160~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>码上掘金示意：</p>
<p><span href="https://code.juejin.cn/pen/7140982487194271785" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140982487194271785" data-src="https://code.juejin.cn/pen/7140982487194271785" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-4">最后</h2>
<p>今天的内容有点多，技巧也很猛。文中所有技巧在我过往的文章中都有非常高频的出现次数，对其中细节不了解的可以在 iCSS 中通过关键字查找，好好补一补。</p>
<p>好了，本文到此结束，希望本文对你有所帮助 :)</p>
<p>更多精彩 CSS 技术文章汇总在我的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS" ref="nofollow noopener noreferrer">Github -- iCSS</a> ，持续更新，欢迎点个 star 订阅收藏。</p>
<p>如果还有什么疑问或者建议，可以多多交流，原创文章，文笔有限，才疏学浅，文中若有不正之处，万望告知。</p></div>  
</div>
            