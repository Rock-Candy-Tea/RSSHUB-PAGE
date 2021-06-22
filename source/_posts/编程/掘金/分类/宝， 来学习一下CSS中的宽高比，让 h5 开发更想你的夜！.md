
---
title: '宝， 来学习一下CSS中的宽高比，让 h5 开发更想你的夜！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f689ea0d24ea4705a92d3a994599b5df~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 16:22:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f689ea0d24ea4705a92d3a994599b5df~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：Ahmad Shadeed
译者：前端小智
来源：shadeed</p>
</blockquote>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://github.com/qq449245884/xiaozhi" target="_blank" rel="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>在图像和其他响应式元素的宽度和高度之间有一个一致的比例是很重要的。在CSS中，我们使用padding hack已经很多年了，但现在我们在CSS中有了原生的长宽比支持。</p>
<p>在这篇文章中，我们将讨论什么是宽高比，我们过去是怎么做的，新的做法是什么。当然，也会有一些用例，对它们进行适当的回退。</p>
<h3 data-id="heading-0">什么是高宽比</h3>
<p>根据维基百科的说法：</p>
<blockquote>
<p>在数学上，比率表示一个数字包含另一个数字的多少倍。例如，如果一碗水果中有八个橙子和六个柠檬，那么橙子和柠檬的比例是八比六（即8∶6，相当于比值4∶3）。</p>
</blockquote>
<p>在网页设计中，高宽比的概念是用来描述图像的宽度和高度应按比例调整。</p>
<p>考虑下图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f689ea0d24ea4705a92d3a994599b5df~tplv-k3u1fbpfcp-watermark.image" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比率是4:3，这表明苹果和葡萄的比例是<code>4:3</code>。</p>
<p>换句话说，我们可以为宽高比为4：3的最小框是<code>4px * 3px</code>框。 当此盒式高度按比例调整为其宽度时，我们将有一个致宽尺寸的框。</p>
<p>考虑下图。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d65c304e149e49d08e518f046ff0cd3c~tplv-k3u1fbpfcp-watermark.image" alt="02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>盒子被按比例调整大小，其宽度和高度之间的比例是一致的。现在，让我们想象一下，这个盒子里有一张重要的图片，我们关心它的所有细节。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf2c77fdb73445fe9c5144d8ce7dfd00~tplv-k3u1fbpfcp-watermark.image" alt="03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>请注意，无论大小如何，图像细节都被保留。通过拥有一致的高宽比，我们可以获得以下好处</p>
<ul>
<li>整个网站的图像将在不同的视口大小上保持一致。</li>
<li>我们也可以有响应式的视频元素。</li>
<li>它有助于设计师创建一个图像大小的清晰指南，这样开发者就可以在开发过程中处理它们。</li>
</ul>
<h3 data-id="heading-1">计算宽高比</h3>
<p>为了测量宽高比，我们需要将宽度除以如下图所示的高度。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a61302a5b4784d1ba2d1723215b2b43f~tplv-k3u1fbpfcp-watermark.image" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>宽度和高度之间的比例是1.33。这意味着这个比例应该得到遵守。请考虑</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/630c4f10ca064afa8e7f74dfc4a6b0b8~tplv-k3u1fbpfcp-watermark.image" alt="05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意右边的图片，宽度÷高度的值是 <strong>1.02</strong>，这不是原来的长宽比（1.33或4：3）。</p>
<p>你可能在想，如何得出4:3这个数值？嗯，这被称为最接近的正常长宽比，有一些工具可以帮助我们找到它。在进行UI设计时，强烈建议你确切地知道你所使用的图像的宽高比是多少。使用这个<a href="http://lawlesscreation.github.io/nearest-aspect-ratio/" target="_blank" rel="nofollow noopener noreferrer">网址</a>可以帮我们快速计算。</p>
<blockquote>
<p>网址地址：<a href="http://lawlesscreation.github.io/nearest-aspect-ratio/" target="_blank" rel="nofollow noopener noreferrer">lawlesscreation.github.io/nearest-asp…</a></p>
</blockquote>
<h3 data-id="heading-2">在 CSS 中实现宽高比</h3>
<p>我们过去是通过在CSS中使用百分比<code>padding</code> 来实现宽高比的。好消息是，最近，我们在所有主要的浏览器中都得到了<code>aspect-ratio</code>的原生支持。在深入了解原生方式之前，我们先首先解释一下好的老方法。</p>
<p>当一个元素有一个垂直百分比的<code>padding</code>时，它将基于它的父级宽度。请看下图。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c54cb93f069485bb2fa3d2662a5a2d2~tplv-k3u1fbpfcp-watermark.image" alt="06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当标题有<code>padding-top: 50%</code>时，该值是根据其父元素的宽度来计算的。因为父元素的宽度是<code>200px</code>，所以<code>padding-top</code>会变成<code>100px</code>。</p>
<p>为了找出要使用的百分比值，我们需要将图像的高度除以宽度。得到的数字就是我们要使用的百分比。</p>
<p>假设图像宽度为<code>260px</code>，高度为<code>195px</code>。</p>
<pre><code class="copyable">Percentage padding = height / width
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>195/260</code>的结果为 <code>0.75</code>（或<code>75％</code>）。</p>
<p>我们假设有一个卡片的网格，每张卡片都有一个缩略图。这些缩略图的宽度和高度应该是相等的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de05f7121024428e82d3ce6e5bf603f7~tplv-k3u1fbpfcp-watermark.image" alt="07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于某些原因，运营上传了一张与其他图片大小不一致的图片。注意到中间那张卡的高度与其他卡的高度不一样。</p>
<p>你可能会想，这还不容易解决？我们可以给图片加个<code>object-fit: cover</code>。问题解决了，对吗？不是这么简单滴。这个解决方案在多种视口尺寸下都不会好看。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9159fa4d1d7463eac160b6d1d5465c7~tplv-k3u1fbpfcp-watermark.image" alt="08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意到在中等尺寸下，固定高度的图片从左边和右边被裁剪得太厉害，而在手机上，它们又太宽。所有这些都是由于使用了固定高度的原因。我们可以通过不同的媒体查询手动调整高度，但这不是一个实用的解决方案。</p>
<p>我们需要的是，无论视口大小如何，缩略图的尺寸都要一致。为了实现这一点，我们需要使用百分比<code>padding</code>来实现一个宽高比。</p>
<p><strong>HTML</strong></p>
<pre><code class="copyable"><article class="card">
  <div class="card__thumb">
    <img src="thumb.jpg" alt="" />
  </div>
  <div class="card__content">
    <h3>Muffins Recipe</h3>
    <p>Servings: 3</p>
  </div>
</article>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>CSS</strong></p>
<pre><code class="copyable">.card__thumb &#123;
  position: relative;
  padding-top: 75%;
&#125;

.card__thumb img &#123;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述，我们定义了卡片缩略图包装器（<code>.card__thumb</code>）的高度取决于其宽度。另外，图片是绝对定位的，它有它的父元素的全部宽度和高度，有<code>object-fit: cover</code>，用于上传不同大小的图片的情况。请看下面的动图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1beb08fc489e4233b7ae3c75ccbc096c~tplv-k3u1fbpfcp-watermark.image" alt="09.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>请注意，卡片大小的变化和缩略图的长宽比没有受到影响。</p>
<h3 data-id="heading-3">aspect-ratio 属性</h3>
<p>今年早些时候，Chrome、Safari TP和Firefox Nightly都支持<code>aspect-ratio </code>CSS 属性。最近，它在Safari 15的官方版本中得到支持。</p>
<p>我们回到前面的例子，我们可以这样改写它。</p>
<pre><code class="copyable">/* 上面的方式 */
.card__thumb &#123;
  position: relative;
  padding-top: 75%;
&#125;

/* 使用 aspect-ratio 属性 */
.card__thumb &#123;
  position: relative;
  aspect-ratio: 4/3;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请看下面的动图，了解宽高比是如何变化的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e1ced53cef4829945127607b4b2687~tplv-k3u1fbpfcp-watermark.image" alt="10.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Demo 地址：<a href="https://codepen.io/shadeed/pen/ZEeMjZe" target="_blank" rel="nofollow noopener noreferrer">codepen.io/shadeed/pen…</a></p>
</blockquote>
<p>有了这个，让我们探索原始纵横比可以有用的一些用例，以及如何以逐步增强的方法使用它。</p>
<h3 data-id="heading-4">渐进增强</h3>
<p>我们可以通过使用CSS <code>@supports</code>和CSS变量来使用CSS <code>aspect-ratio</code>。</p>
<pre><code class="copyable">.card &#123;
  --aspect-ratio: 16/9;
  padding-top: calc((1 / (var(--aspect-ratio))) * 100%);
&#125;

@supports (aspect-ratio: 1) &#123;
  .card &#123;
    aspect-ratio: var(--aspect-ratio);
    padding-top: initial;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Logo Images</h3>
<p>来看看下面的 logo</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73645984917a467d89e66feea8f48956~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你是否注意到它们的尺寸是一致的，而且它们是对齐的？来看看幕后的情况。</p>
<pre><code class="copyable">// html
<li class="brands__item">
  <a href="#">
    <img src="assets/batch-2/aanaab.png" alt="" />
  </a>
</li>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.brands__item a &#123;
  padding: 1rem;
&#125;

.brands__item img &#123;
  width: 130px;
  object-fit: contain;
  aspect-ratio: 2/1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我添加了一个<code>130px</code>的基本宽度，以便有一个最小的尺寸，而<code>aspect-ratio</code>会照顾到高度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0798a39a9832472986f025eb043f98ab~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>蓝色区域是图像的大小，<code>object-fit: contain</code>是重要的，避免扭曲图像。</p>
<h3 data-id="heading-6">Responsive Circles</h3>
<p>你是否曾经需要创建一个应该是响应式的圆形元素？CSS <code>aspect-ratio</code>是这种使用情况的最佳选择。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d36f81716c9141f98fa86923d7fad534~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.person &#123;
  width: 180px;
  aspect-ratio: 1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果宽高比的两个值相同，我们可以写成<code>aspect-ratio: 1</code>而不是<code>aspect-ratio: 1/1</code>。如果你使用<code>flexbox</code>或<code>grid </code>，宽度将是可选的，它可以被添加作为一个最小值。</p>
<p><del>完，我是小智，宝，你学会了吗</del></p>
<hr>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://www.fundebug.com/?utm_source=xiaozhi" target="_blank" rel="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<p>原文：<a href="https://ishadeed.com/article/css-aspect-ratio/" target="_blank" rel="nofollow noopener noreferrer">ishadeed.com/article/css…</a></p>
<h3 data-id="heading-7">交流</h3>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://github.com/qq449245884/xiaozhi" target="_blank" rel="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote></div>  
</div>
            