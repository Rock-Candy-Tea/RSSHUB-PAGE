
---
title: 'CSS 中的 3D：学习去以立方体而不是盒子的方式考虑问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=73'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 10:09:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=73'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fcss-in-3d-learning-to-think-in-cubes-instead-of-boxes%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/css-in-3d-learning-to-think-in-cubes-instead-of-boxes/" ref="nofollow noopener noreferrer">CSS in 3D: Learning to Think in Cubes Instead of Boxes</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fauthor%2Fjheytompkins%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/author/jheytompkins/" ref="nofollow noopener noreferrer">Jhey Tompkins</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fcss-in-3d-learning-to-think-in-cubes-instead-of-boxes.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/css-in-3d-learning-to-think-in-cubes-instead-of-boxes.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FPassionPenguin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/PassionPenguin" ref="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：</li>
</ul>
</blockquote>
<p>我学习 CSS 的道路有点不正统。我不是从前端开发人员开始的，而是一名 Java 开发人员。事实上，我最早对 CSS 的回忆是在 Visual Studio 中为挑选颜色。</p>
<p>直到后来我才开始解决并找到我对前端的热爱。探索 CSS 是后话了。当它完全出现在我世界中时，大概已经是 CSS3 蓬勃发展的时候了。3D 和动画是这个街区的酷孩子，他们几乎塑造了我对 CSS 的学习。他们吸引我并<em>塑造</em>了（双关语）我，让对 CSS 的理解比其他东西更重要，比如布局、颜色等。</p>
<p>我的意思是我每一分钟都在做关于 CSS 3D 事情。与你花费大量时间处理的任何事情一样，随着你在这一技能上的磨练，你最终会在多年内完善你的处理能力。这篇文章介绍了我目前是如何处理 CSS 3D 的，并介绍了一些可能对你有所帮助的提示和技巧！</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FmLaXRe" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/mLaXRe" ref="nofollow noopener noreferrer">Codepen jh3y/mLaXRe</a></p>
<h2 data-id="heading-0">一切都是长方体</h2>
<p>对于 3D 中大多数的情况，我们可以使用长方体。我们当然可以创建更复杂的形状，但它们通常需要更多考虑。圆滑弯曲的部分特别的难，有一些处理它们的技巧（我们稍后会做详细介绍）。</p>
<p>我们不会介绍如何在 CSS 中制作长方体。你可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fsimplifying-css-cubes-custom-properties%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/simplifying-css-cubes-custom-properties/" ref="nofollow noopener noreferrer">Ana Tudor 的帖子</a>，或者看一下我制作的这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fwp-content%2Fuploads%2F2020%2F10%2Fuse-css-transforms-to-create-configurable-3d-cuboids.mp4" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/wp-content/uploads/2020/10/use-css-transforms-to-create-configurable-3d-cuboids.mp4" ref="nofollow noopener noreferrer">制作长方体的截屏</a>。</p>
<p>这里的核心是我们需要使用一个元素来包裹我们的长方体，然后在其中转换六个元素，让每个元素都充当我们长方体的一面。其中，应用 <code>transform-style:preserve-3d</code> 是很重要的，而且将它应用于任何地方也不是一个坏主意。当形状变得更复杂时，我们很可能会处理嵌套的长方体。在浏览器之间切换去尝试去调试一个缺失的 <code>transform-style</code> 可能会很痛苦。</p>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
    <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FQWELPQg" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/QWELPQg" ref="nofollow noopener noreferrer">Codepen jh3y/QWELPQg</a></p>
<p>对于我们的 3D 创作而言，远不止是常见的那几样形状。请尝试想象由长方体构建的整个场景，比如说，让我作一个真实的例子，请考虑在页面上渲染一本 3D 的图书，其中包含四个长方体。正反封面各一个、书脊一个、个书页一张。使用 <code>background-image</code> 为我们完成剩下的工作。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FZEOzNbm" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/ZEOzNbm" ref="nofollow noopener noreferrer">Codepen jh3y/ZEOzNbm</a></p>
<h2 data-id="heading-1">设置场景</h2>
<p>我们将使用像乐高积木这样的长方体。但是，我们可以通过设置场景和创建平面来让我们的生活更轻松一些。那个平面是我们的创作所在的地方，让我们更容易旋转和移动整个创作。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FpobzmNx" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/pobzmNx" ref="nofollow noopener noreferrer">Codepen jh3y/pobzmNx</a></p>
<p>对我来说，当我创建一个场景时，我喜欢先在 X 和 Y 轴上旋转它。然后我会用 <code>rotateX(90deg)</code> 把它平放。这样，当我想在场景中添加一个新的长方体时，我可以直接将新元素添加到平面元素中。我将在这里做的另一件事是在所有长方体上设置 <code>position: absolute</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.plane</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(<span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--rotate-x, -<span class="hljs-number">24</span>) * <span class="hljs-number">1deg</span>)) <span class="hljs-built_in">rotateY</span>(<span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--rotate-y, -<span class="hljs-number">24</span>) * <span class="hljs-number">1deg</span>)) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">从样板开始</h2>
<p>在平面上创建各种大小的长方体会导致每次创建都需要大量重复的代码。出于这个原因，我使用 Pug 通过 mixin 创建我的长方体。如果您不熟悉 Pug，我写了一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.to%2Fjh3y%2Fpug-in-5-minutes-272k" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.to/jh3y/pug-in-5-minutes-272k" ref="nofollow noopener noreferrer">5 分钟的介绍</a>。</p>
<p>一个典型的场景是这样的：</p>
<pre><code class="hljs language-pug copyable" lang="pug">//- Front
//- Back
//- Right
//- Left
//- Top
//- Bottom
mixin cuboid(className)
  .cuboid(class=className)
    - let s = 0
    while s < 6
      .cuboid__side
      - s++
.scene
  //- Plane that all the 3D stuff sits on
  .plane
    +cuboid('first-cuboid')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于 CSS，我的长方体类的样式代码目前看起来像这样：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.cuboid</span> &#123;
    <span class="hljs-comment">/* 默认样式 */</span>
    --<span class="hljs-attribute">width</span>: <span class="hljs-number">15</span>;
    --<span class="hljs-attribute">height</span>: <span class="hljs-number">10</span>;
    --depth: <span class="hljs-number">4</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--depth) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--width) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1rem</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">5vmin</span>);
&#125;

<span class="hljs-selector-class">.cuboid</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--height) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">transform-origin</span>: <span class="hljs-number">50%</span> <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">calc</span>((<span class="hljs-built_in">var</span>(--depth) / <span class="hljs-number">2</span>) * <span class="hljs-number">1vmin</span>));
&#125;

<span class="hljs-selector-class">.cuboid</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--height) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">transform-origin</span>: <span class="hljs-number">50%</span> <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">calc</span>((<span class="hljs-built_in">var</span>(--depth) / <span class="hljs-number">2</span>) * <span class="hljs-number">1vmin</span>));
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
&#125;

<span class="hljs-selector-class">.cuboid</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--height) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--depth) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">calc</span>((<span class="hljs-built_in">var</span>(--width) / <span class="hljs-number">2</span>) * <span class="hljs-number">1vmin</span>));
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
&#125;

<span class="hljs-selector-class">.cuboid</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--height) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--depth) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>) <span class="hljs-built_in">rotateY</span>(-<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">calc</span>((<span class="hljs-built_in">var</span>(--width) / <span class="hljs-number">2</span>) * <span class="hljs-number">1vmin</span>));
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
&#125;

<span class="hljs-selector-class">.cuboid</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">5</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--depth) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--width) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">calc</span>((<span class="hljs-built_in">var</span>(--height) / <span class="hljs-number">2</span>) * <span class="hljs-number">1vmin</span>));
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
&#125;

<span class="hljs-selector-class">.cuboid</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">6</span>) &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--depth) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--width) * <span class="hljs-number">1vmin</span>);
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>) <span class="hljs-built_in">translate3d</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">calc</span>((<span class="hljs-built_in">var</span>(--height) / <span class="hljs-number">2</span>) * -<span class="hljs-number">1vmin</span>)) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">180deg</span>);
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，它给了我这样的东西：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FabZorVz" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/abZorVz" ref="nofollow noopener noreferrer">Codepen jh3y/abZorVz</a></p>
<h2 data-id="heading-3">由 CSS 变量提供支持</h2>
<p>你可能已经注意到我在 CSS 代码中使用了一些 CSS 变量（也称为自定义属性）。这很大程度上节省了我的时间。我用了不少 CSS 变量助力构建我的长方体。</p>
<ul>
<li><code>--width</code>：平面上长方体的宽度</li>
<li><code>--height</code>：平面上长方体的高度</li>
<li><code>--depth</code>：平面上长方体的深度</li>
<li><code>--x</code>: 平面上的 X 位置</li>
<li><code>--y</code>: 平面上的 Y 位置</li>
</ul>
<p>我主要使用 <code>vmin</code> 作为我的大小调整单位，以保持响应式布局。如果我正在创建需要缩放的东西，我可能会创建一个响应式单位。我们在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fadvice-for-complex-css-illustrations%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/advice-for-complex-css-illustrations/" ref="nofollow noopener noreferrer">上一篇文章</a>中提到了这种技术。我再次将形状放平，现在我可以将我的长方体称为具有高度、宽度和深度的形状了。下面的演示展示了我们如何在平面上移动一个长方体来改变它的尺寸。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FBaKqQLJ" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/BaKqQLJ" ref="nofollow noopener noreferrer">Codepen jh3y/BaKqQLJ</a></p>
<h2 data-id="heading-4">使用 dat.GUI 调试</h2>
<p>您可能已经注意到我们介绍的一些演示右上角的小面板。那是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdataarts%2Fdat.gui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dataarts/dat.gui" ref="nofollow noopener noreferrer">dat.GUI</a>。这是一个轻量级的 JavaScript 控制器库，对于调试 CSS 3D 来说非常有用。不用太多代码，我们就可以设置一个面板，允许我们在运行时更改 CSS 变量。我喜欢做的一件事是使用面板在 X 和 Y 轴上旋转平面。这样，就可以看到事情如何排列或在我们一开始可能看不到的部分上工作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">dat</span>: &#123;GUI&#125;,
&#125; = <span class="hljs-built_in">window</span>
<span class="hljs-keyword">const</span> CONTROLLER = <span class="hljs-keyword">new</span> GUI()
<span class="hljs-keyword">const</span> CONFIG = &#123;
    <span class="hljs-string">'cuboid-height'</span>: <span class="hljs-number">10</span>,
    <span class="hljs-string">'cuboid-width'</span>: <span class="hljs-number">10</span>,
    <span class="hljs-string">'cuboid-depth'</span>: <span class="hljs-number">10</span>,
    <span class="hljs-attr">x</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">z</span>: <span class="hljs-number">5</span>,
    <span class="hljs-string">'rotate-cuboid-x'</span>: <span class="hljs-number">0</span>,
    <span class="hljs-string">'rotate-cuboid-y'</span>: <span class="hljs-number">0</span>,
    <span class="hljs-string">'rotate-cuboid-z'</span>: <span class="hljs-number">0</span>,
&#125;
<span class="hljs-keyword">const</span> UPDATE = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">Object</span>.entries(CONFIG).forEach(<span class="hljs-function">(<span class="hljs-params">[key, value]</span>) =></span> &#123;
        <span class="hljs-built_in">document</span>.documentElement.style.setProperty(<span class="hljs-string">`--<span class="hljs-subst">$&#123;key&#125;</span>`</span>, value)
    &#125;)
&#125;
<span class="hljs-keyword">const</span> CUBOID_FOLDER = CONTROLLER.addFolder(<span class="hljs-string">'Cuboid'</span>)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'cuboid-height'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">20</span>, <span class="hljs-number">0.1</span>)
    .name(<span class="hljs-string">'Height (vmin)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'cuboid-width'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">20</span>, <span class="hljs-number">0.1</span>)
    .name(<span class="hljs-string">'Width (vmin)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'cuboid-depth'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">20</span>, <span class="hljs-number">0.1</span>)
    .name(<span class="hljs-string">'Depth (vmin)'</span>)
    .onChange(UPDATE)
<span class="hljs-comment">// 在这里你有一个选择，可以使用 x||y</span>
<span class="hljs-comment">// 或者使用标准的带有 vmin 的 transform</span>
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'x'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">40</span>, <span class="hljs-number">0.1</span>)
    .name(<span class="hljs-string">'X (vmin)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'y'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">40</span>, <span class="hljs-number">0.1</span>)
    .name(<span class="hljs-string">'Y (vmin)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'z'</span>, -<span class="hljs-number">25</span>, <span class="hljs-number">25</span>, <span class="hljs-number">0.1</span>)
    .name(<span class="hljs-string">'Z (vmin)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'rotate-cuboid-x'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">360</span>, <span class="hljs-number">1</span>)
    .name(<span class="hljs-string">'Rotate X (deg)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'rotate-cuboid-y'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">360</span>, <span class="hljs-number">1</span>)
    .name(<span class="hljs-string">'Rotate Y (deg)'</span>)
    .onChange(UPDATE)
CUBOID_FOLDER.add(CONFIG, <span class="hljs-string">'rotate-cuboid-z'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">360</span>, <span class="hljs-number">1</span>)
    .name(<span class="hljs-string">'Rotate Z (deg)'</span>)
    .onChange(UPDATE)
UPDATE()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您观看此推文中的延时摄影视频。您会注意到我在构建场景时经常旋转平面。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fjh3yy%2Fstatus%2F1312126353177673732%3Fs%3D20" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/jh3yy/status/1312126353177673732?s=20" ref="nofollow noopener noreferrer">@jh3yy 的一份推文</a></p>
<p>dat.GUI 代码有点重复。我们可以创建接受配置并生成控制器的函数，不过需要稍加修改才能满足你的需求。我开始在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FGRJoWyp" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/GRJoWyp" ref="nofollow noopener noreferrer">这个演示</a> 中使用了动态生成的控制器。</p>
<h2 data-id="heading-5">居中</h2>
<p>你可能已经注意到，默认情况下，每个长方体都位于平面下方和上方的一半。这是我故意设置的，也是我最近才开始做的事情。为什么？因为我们想使用长方体的包含元素作为长方体的中心，而这能够让动画变得更容易。特别是，如果我们考虑绕 Z 轴旋转。我在创建 <code>CSS is Cake</code> 时发现了这一点。制作蛋糕后，我决定让每一片蛋糕都是能够交互的，然后我不得不返工更改我的实现，以修复翻转的蛋糕片的旋转中心。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FKKVGoGJ" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/KKVGoGJ" ref="nofollow noopener noreferrer">Codepen jh3y/KKVGoGJ</a></p>
<p>在这里，我拆分了该演示的显示中心以及偏移中心，展示这些会如何影响效果。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FXWKrLwe" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/XWKrLwe" ref="nofollow noopener noreferrer">Codepen jh3y/XWKrLwe</a></p>
<h2 data-id="heading-6">定位</h2>
<p>如果我们正在处理一个更复杂的场景 —— 我们可能会将其拆分为不同的部分。这就是子平面的概念派上用场的地方。考虑这个演示，我在其中重新创建了我的个人工作区。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fjh3yy%2Fstatus%2F1310658720746045440%3Fs%3D20" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/jh3yy/status/1310658720746045440?s=20" ref="nofollow noopener noreferrer">@jh3yy 的一份推文</a>。</p>
<p>这里发生了很多事情，很难跟踪所有的长方体。为此，我们可以引入子平面。让我们分解那个演示。椅子有自己的子平面。这使得在场景中移动和旋转它变得更容易 —— 除其他外 —— 而不影响其他任何东西。事实上，我们甚至可以在不移动椅子脚的情况下旋转顶部！</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FQWELerg" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/QWELerg" ref="nofollow noopener noreferrer">Codepen jh3y/QWELerg</a></p>
<h2 data-id="heading-7">美学</h2>
<p>一旦我们有了一个结构，就该研究美学了。这一切都取决于你在做什么。但是您可以通过使用某些技术获得一些快速的胜利。我倾向于从让事情变得“丑陋”开始，然后回去为所有颜色创建 CSS 变量并应用它们。特定事物的三种阴影使我们能够在视觉上区分长方体的侧面。考虑这个烤面包机的例子，让我们使用三种色调覆盖烤面包机的侧面：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FKKVjLrx" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/KKVjLrx" ref="nofollow noopener noreferrer">Codepen jh3y/KKVjLrx</a></p>
<p>我们之前的 Pug mixin 允许我们为长方体定义类名。将颜色应用到一侧通常看起来像这样：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 正面使用线性渐变来应用微光效果 */</span>
<span class="hljs-selector-class">.toaster__body</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">120deg</span>, transparent <span class="hljs-number">10%</span>, <span class="hljs-built_in">var</span>(--shine) <span class="hljs-number">10%</span> <span class="hljs-number">20%</span>, transparent <span class="hljs-number">20%</span> <span class="hljs-number">25%</span>, <span class="hljs-built_in">var</span>(--shine) <span class="hljs-number">25%</span> <span class="hljs-number">30%</span>, transparent <span class="hljs-number">30%</span>), <span class="hljs-built_in">var</span>(--shade-one);
&#125;

<span class="hljs-selector-class">.toaster__body</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">var</span>(--shade-one);
&#125;

<span class="hljs-selector-class">.toaster__body</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">3</span>),
<span class="hljs-selector-class">.toaster__body</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">var</span>(--shade-three);
&#125;

<span class="hljs-selector-class">.toaster__body</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">5</span>),
<span class="hljs-selector-class">.toaster__body</span> > <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">6</span>) &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">var</span>(--shade-two);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在我们的 Pug mixin 中包含额外的元素有点棘手。但是我们不要忘记，我们长方体的每一面都提供了两个伪元素。我们可以将这些用于各种细节。例如，烤面包机插槽和侧面的手柄插槽是伪元素。</p>
<p>另一个技巧是使用 <code>background-image</code> 来添加细节。例如，考虑 3D 工作区。我们可以使用背景层来创建阴影。我们可以使用实际图像来创建纹理表面。地板和地毯是重复的 <code>background-image</code>。事实上，对纹理使用伪元素是很棒的，因为我们可以在需要时转换它们，比如旋转平铺图像。我还发现，在某些情况下，直接使用长方体侧面工作时会出现渲染上的闪烁。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FXWdQBRx" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/XWdQBRx" ref="nofollow noopener noreferrer">Codepen jh3y/XWdQBRx</a></p>
<p>将图像用于纹理的一个问题是我们如何创建不同的阴影。我们需要色调来区分不同的侧面，这就是 <code>filter</code> 属性可以提供帮助的地方。让我们将 <code>brightness()</code> 过滤器应用于长方体的不同侧面使它们变亮或变暗。考虑这个 CSS 翻转桌子，所有的表面都使用纹理图像。但是为了区分侧面，我们在上面应用了亮度过滤器。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FxJXvjP" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/xJXvjP" ref="nofollow noopener noreferrer">Codepen jh3y/xJXvjP</a></p>
<p>如何使用有限的元素集来创建形状——或者我们想要创建的看似不可能的特征？有时我们可以用一点烟雾和镜像效果来欺骗眼睛。我们可以提供一种伪造的 3D 感觉。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzzz.dog" target="_blank" rel="nofollow noopener noreferrer" title="https://zzz.dog" ref="nofollow noopener noreferrer">Z dog library</a> 做得很好，就是一个很好的例子。</p>
<p>考虑一下我们现在有一捆气球，固定它们的绳子使用了正确的视角，并且每个绳子都有自己的旋转、倾斜等的效果。但气球本身是平的。如果我们旋转平面，气球会保持反平面旋转。这给人一种“虚假”的 3D 感觉，试用演示并解决这一问题。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FNWNVgJw" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/NWNVgJw" ref="nofollow noopener noreferrer">Codepen jh3y/NWNVgJw</a></p>
<p>有时需要一点开箱即用的思考。我在构建 3D 工作空间时有人向我建议种一些室内植物。在我房间里的确重了一些植物，但我最初的想法是，“不，我可以做一个方形的锅，我怎么做所有的叶子？”实际上，我们也可以在这个上使用一些视觉上的技巧。我们可以获取一些叶子或植物的图片，使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.remove.bg" target="_blank" rel="nofollow noopener noreferrer" title="https://www.remove.bg" ref="nofollow noopener noreferrer">remove.bg</a> 之类的工具删除背景，然后将许多图像放置在同一位置，但将它们每个旋转一定量。现在，当它们旋转时，我们就能够得到 3D 植物的感觉。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FoNLNZMR" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/oNLNZMR" ref="nofollow noopener noreferrer">Codepen jh3y/oNLNZMR</a></p>
<h2 data-id="heading-8">处理尴尬的形状</h2>
<p>笨拙的形状很难以通用的方式覆盖，每个创作都有自己的障碍。但是，有几个示例可以帮助您提供解决问题的想法。我最近看了一篇关于【乐高界面面板的 UX】的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.designedbycave.co.uk%2F2020%2FLEGO-Interface-UX%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.designedbycave.co.uk/2020/LEGO-Interface-UX/" ref="nofollow noopener noreferrer">文章</a>。事实上，将 CSS 3D 像乐高玩具一样处理并不是一个坏主意。但是乐高界面面板是我们可以用 CSS 制作的形状（除去螺柱 —— 我最近才知道这是螺栓的名称）。这是一个长方体，然后我们可以裁剪顶面，使端面透明，并旋转一个伪元素将其连接起来。我们可以使用伪元素添加一些背景层的细节。快来尝试在下面的演示中打开和关闭线框。如果我们想要形状的确切高度和角度，我们可以使用一些数学来构建斜边等。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FPozojYe" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/PozojYe" ref="nofollow noopener noreferrer">Codepen jh3y/PozojYe</a></p>
<p>另一个尴尬的事情是曲线 —— 球形不被 CSS 支持。在这一点上，我们有多种选择，一种选择是接受这一事实并创建边数有限的多边形，而另一种是创建圆形并使用我们在植物中提到的旋转方法。这些选项中的每一个都可以工作。但同样，它是基于用例的，各有利弊。有了多边形，我们在使用了很多的元素的情况下，我们几乎可以得到一条曲线，而后者可能会导致性能问题。使用透视技巧，我们最终也可能会遇到性能问题。我们也放弃了设计形状“侧面”的能力，因为没有适宜的方法。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FwvWvqqM" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/wvWvqqM" ref="nofollow noopener noreferrer">Codepen jh3y/wvWvqqM</a></p>
<h2 data-id="heading-9">与 Z 轴作斗争</h2>
<p>最后但并非最不重要的是与 Z 轴作斗争。这是平面上的某些元素可能重叠或导致我们不希望看到的渲染闪烁的地方。很难给出很好的例子，也没有通用的解决方案。这是要根据具体情况来解决的问题。主要策略是根据需要对 DOM 中的事物进行排序，但有时这不是唯一的问题。</p>
<p>做得准确有时也会导致问题，让我们再次参考 3D 工作区的案例。想一想墙上的画布，其中的阴影是一个伪元素。如果我们将画布正好靠在墙上，我们就会遇到问题。如果我们这样做，阴影和墙壁将争夺渲染上的层次问题。为了解决这个问题，我们可以稍微应用 translate。这将解决问题，可以有效声明应该放在前面的内容。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FPozoYWK" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/PozoYWK" ref="nofollow noopener noreferrer">Codepen jh3y/PozoYWK</a></p>
<p>尝试在打开和关闭“画布偏移”的情况下调整此演示的大小。注意没有偏移时阴影是如何闪烁的？那是因为阴影和墙壁在争夺层次。偏移量将 <code>--x</code> 设置为我们命名为 <code>--cm</code> 的 <code>1vmin</code> 的一小段长度，即用于该创作的响应单位。</p>
<h2 data-id="heading-10">就是这样</h2>
<p>我们现在可以将我们的 CSS 带到另一个维度 —— 3D。使用我的一些技巧，找到属于你自己的技巧，分享这些技巧，并分享你的 3D 创作！是的，在 CSS 中制作 3D 东西可能很困难，但绝对是一个我们可以随着我们进行而改进的能力。不同的方法适用于不同的人，耐心是必需的成分。我很想知道你的方法是什么！</p>
<p>最重要的事情？其实还是玩得开心，哈哈哈！</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FMWeWvGO" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/MWeWvGO" ref="nofollow noopener noreferrer">Codepen jh3y/MWeWvGO</a></p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            