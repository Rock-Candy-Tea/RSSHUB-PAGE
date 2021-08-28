
---
title: '我们可以使用 Container 查询创造一个_缩放大小工具_吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://github.com/PassionPenguin/gold-miner-images/blob/master/can-we-create-a-resize-hack-with-container-queries-twiter-1.png'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 10:25:01 GMT
thumbnail: 'https://github.com/PassionPenguin/gold-miner-images/blob/master/can-we-create-a-resize-hack-with-container-queries-twiter-1.png'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fcan-we-create-a-resize-hack-with-container-queries%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/can-we-create-a-resize-hack-with-container-queries/" ref="nofollow noopener noreferrer">Can We Create a “Resize Hack” With Container Queries?</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fauthor%2Fjheytompkins%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/author/jheytompkins/" ref="nofollow noopener noreferrer">Jhey Tompkins</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fcan-we-create-a-resize-hack-with-container-queries.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/can-we-create-a-resize-hack-with-container-queries.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FPassionPenguin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/PassionPenguin" ref="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：</li>
</ul>
</blockquote>
<p>如果你对 CSS 的新发展有所关注，你可能听说过 <strong>Container 查询</strong>即将到来。我们将在这里查看基础知识，但如果您想再看一看，请查看 Una 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Fnext-gen-css-container%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/next-gen-css-container/" ref="nofollow noopener noreferrer">Next Gen CSS CSS：@container</a> 一文（或者本人翻译并发表在掘金社区的 <a href="https://juejin.cn/post/6981456441341132837" target="_blank" title="https://juejin.cn/post/6981456441341132837">下一代 CSS：@container</a>）。在我们自己摸索基础知识之后，我们将用它们构建一些非常有趣的东西：对经典 CSS 模因的全新演绎，「彼得格里芬和他那百叶窗 Peter Griffin fussing with window blinds」。 ;)</p>
<p>那么，什么<strong>是</strong>容器查询？就是……就是……就像我们有媒体查询来查询诸如视口大小之类的东西一样，容器查询允许我们查询容器的大小。基于此，我们可以将不同的样式应用于所述容器的子项。</p>
<p>它是什么样子的？嗯，确切的标准正在制定中。但目前，它是这样的：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span> &#123;
  contain: layout size;
  <span class="hljs-comment">/* Or... */</span>
  contain: layout inline-size;
&#125;

<span class="hljs-keyword">@container</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">768px</span>) &#123;
  <span class="hljs-selector-class">.child</span> &#123; <span class="hljs-attribute">background</span>: hotpink; &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>layout</code> 关键字为元素开启 <code>layout-containment</code> 功能。<code>inline-size</code> 允许用户更具体地了解容器。这目前意味着我们只能查询容器的宽度 <code>width</code>，而使用 <code>size</code> 后，我们就可以查询容器的 <code>height</code>。</p>
<p>同样，我们现在做的事情<strong>可能</strong>仍然会在未来有所改变。在撰写本文时，使用容器查询（没有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjsxtools%2Fcqfill" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jsxtools/cqfill" ref="nofollow noopener noreferrer">polyfill</a>）的唯一方法隐藏在了 Chrome Canary 中的 Flags（<code>chrome://flags</code>）之后。我绝对建议您在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdrafts.c%25E2%2580%258B%25E2%2580%258Bsswg.org%2Fcss-contain%2F%23valdef-contain-layout" target="_blank" rel="nofollow noopener noreferrer" title="https://drafts.c%E2%80%8B%E2%80%8Bsswg.org/css-contain/#valdef-contain-layout" ref="nofollow noopener noreferrer">csswg.org</a> 上快速阅读这份草案。</p>
<p>开始尝试 Container 查询的最简单方法是制作几个带有可调整大小的容器元素的快速演示。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2Fpoeyxba" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/poeyxba" ref="nofollow noopener noreferrer">CodePen jh3y/poeyxba</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FzYZKEyM" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/zYZKEyM" ref="nofollow noopener noreferrer">CodePen jh3y/zYZKEyM</a></p>
<p>尝试在 Chrome Canary 中更改 <code>contain</code> 值并查看演示如何响应。这些演示使用不限制轴的 <code>contain: layout size</code>。当容器的 <code>height</code> 和 <code>width</code> 都满足特定阈值时，衬衫尺寸会在第一个演示中进行调整。第二个演示展示了每一个轴如何独立工作，比如说调整水平轴数值时胡须会改变颜色。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@container</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">400px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">400px</span>) &#123;
  <span class="hljs-selector-class">.t-shirt__container</span> &#123;
    --size: <span class="hljs-string">"L"</span>;
    --scale: <span class="hljs-number">2</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是我们现在需要了解的有关容器查询的信息，这实际上只是一些新的 CSS 的样式……</p>
<p>唯一的问题是：到目前为止，我见过的大多数容器查询演示都使用了一个非常标准的“卡片”示例来演示这个概念。不要误会我的意思，因为卡片是容器查询的一个很好的用例，卡片组件实际上是容器查询的子代。考虑通用卡片设计以及它在不同布局中使用时如何受到影响，这是一个常见的问题。我们中的许多人都参与过我们最终制作各种卡片变化的项目，所有这些都迎合了使用它们的不同布局。</p>
<p>但是卡片并不能激发我们使用容器查询的想象力，我希望看到他们<strong>有动力去</strong>以更大的极限来做有趣的事情。我在那个 T 恤尺码演示中和他们尝试了一会儿，我将等到有更好的浏览器支持，直到我开始进一步深入研究（我目前是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbrave.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://brave.com/" ref="nofollow noopener noreferrer">Brave</a> 用户）。但是后来 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fbramus" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/bramus" ref="nofollow noopener noreferrer">Bramus</a> 分享了一个容器查询 polyfill！</p>
<p><img src="https://github.com/PassionPenguin/gold-miner-images/blob/master/can-we-create-a-resize-hack-with-container-queries-twiter-1.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这让我开始思考如何“破解”容器查询。</p>
<p>⚠️ <strong>剧透警告：</strong> 我的 Hack 没有用。很短时间内它确实起效了，或者至少我认为它奏效了。但是，这实际上是一件幸事，因为它引发了更多关于容器查询的对话。</p>
<p>我的想法是什么？ 我想创建类似于“Checkbox Hack”的东西，但用于容器查询。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container__resizer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container__fixed-content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个想法是我们可以有一个容器，里面有一个可调整大小的元素，然后另一个元素在容器外固定定位，而调整容器大小可能会触发容器查询并重新设置固定元素的样式。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span> &#123;
  contain: layout size;
&#125;

<span class="hljs-selector-class">.container__resize</span> &#123;
  <span class="hljs-attribute">resize</span>: vertical;
  <span class="hljs-attribute">overflow</span>: hidden;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">max-height</span>: <span class="hljs-number">500px</span>;
&#125;

<span class="hljs-selector-class">.container__fixed-content</span> &#123;
  <span class="hljs-attribute">position</span>: fixed;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">200%</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">background</span>: red;
&#125;

<span class="hljs-keyword">@container</span>(min-height: <span class="hljs-number">300px</span>) &#123;
  <span class="hljs-selector-class">.container__fixed-content</span> &#123;
    <span class="hljs-attribute">background</span>: blue;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尝试调整此演示中红色框的大小，它将改变紫色框的颜色。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FmdWyLBW" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/mdWyLBW" ref="nofollow noopener noreferrer">CodePen jh3y/mdWylBW</a></p>
<h2 data-id="heading-0">我们可以用容器查询来做到经典的 CSS 模因吗？</h2>
<p>看到上面那个作品奏效了，着实让我很兴奋。现在，我们终于有机会用 CSS 创建一个 Peter Griffin 的 CSS 模因版本并揭穿它！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/491dcfeda6974081bf08358da1976378~tplv-k3u1fbpfcp-watermark.image" alt="giphy-downsized.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可能已经看过这个表情包了。这是对 Cascade 的一击，管理它是多么困难。我使用 <code>cqfill@0.5.0</code> 创建了这个演示……当然，我自己做了一些小改动。 😅</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FLYxKjKX" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/LYxKjKX" ref="nofollow noopener noreferrer">CodePen jh3y/LYxKjKX</a></p>
<p>移动绳索手柄，调整元素的大小，进而影响容器的大小。不同的容器断点会更新 CSS 变量 <code>--open</code>，从 <code>0</code> 到 <code>1</code>，其中 <code>1</code> 等于“打开”状态，而 <code>0</code> 等于“关闭”状态。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@container</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">54px</span>) &#123;
  <span class="hljs-selector-class">.blinds__blinds</span> &#123;
    --open: <span class="hljs-number">0.1</span>;
  &#125;
&#125;
<span class="hljs-keyword">@media</span> --css-container <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">54px</span>) &#123;
  <span class="hljs-selector-class">.blinds__blinds</span> &#123;
    --open: <span class="hljs-number">0.1</span>;
  &#125;
&#125;
<span class="hljs-keyword">@container</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">58px</span>) &#123;
  <span class="hljs-selector-class">.blinds__blinds</span> &#123;
    --open: <span class="hljs-number">0.2</span>;
  &#125;
&#125;
<span class="hljs-keyword">@media</span> --css-container <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">58px</span>) &#123;
  <span class="hljs-selector-class">.blinds__blinds</span> &#123;
    --open: <span class="hljs-number">0.2</span>;
  &#125;
&#125;
<span class="hljs-keyword">@container</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">62px</span>) &#123;
  <span class="hljs-selector-class">.blinds__blinds</span> &#123;
    --open: <span class="hljs-number">0.3</span>;
  &#125;
&#125;
<span class="hljs-keyword">@media</span> --css-container <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-height</span>: <span class="hljs-number">62px</span>) &#123;
  <span class="hljs-selector-class">.blinds__blinds</span> &#123;
    --open: <span class="hljs-number">0.3</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但…。正如我所提到的，这种 Hack 是不可能的。</p>
<p><img src="https://github.com/PassionPenguin/gold-miner-images/blob/master/can-we-create-a-resize-hack-with-container-queries-twiter-2.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很棒的是，它引发了关于容器查询如何工作的对话。它还强调了容器查询 polyfill 的一个错误，该错误现已修复。不过，我很想看到这个 “Hack” 能正常运转。</p>
<p>Miriam Suzanne 一直在围绕容器查询创建一些精彩的内容。容器查询的能力已经发生了很大的变化，这就是生活在最前沿的风险。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.miriamsuzanne.com%2F2021%2F05%2F02%2Fcontainer-queries%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.miriamsuzanne.com/2021/05/02/container-queries/" ref="nofollow noopener noreferrer">她的最新文章</a>总结了当前的状态。</p>
<p><img src="https://github.com/PassionPenguin/gold-miner-images/blob/master/can-we-create-a-resize-hack-with-container-queries-twiter-3.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>尽管我最初的演示/Hack 不起作用，但我们仍然可以使用“调整大小” Hack 来创建这扇百叶窗。同样，如果我们使用 <code>contain: layout size</code>，我们可以查询 <code>height</code>。旁注：有趣的是，我们目前无法使用 <code>contain</code> 根据调整其子元素的大小来查询容器的高度。</p>
<p>反正不管怎么说，看看下面这个演示：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FjOBEKZO" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/jOBEKZO" ref="nofollow noopener noreferrer">CodePen jh3y/jOBEKZO</a></p>
<p>箭头随着容器的大小而旋转。这里的技巧是使用容器查询来更新作用域 CSS 自定义属性。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span> &#123;
  contain: layout size;
&#125;

<span class="hljs-selector-class">.arrow</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-built_in">var</span>(--rotate, <span class="hljs-number">0deg</span>));
&#125;

<span class="hljs-keyword">@container</span>(min-height: <span class="hljs-number">200px</span>) &#123;
  <span class="hljs-selector-class">.arrow</span> &#123;
    --rotate: <span class="hljs-number">90deg</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们在这里有一个容器查询技巧。我们无法使用第一个 Hack 概念的缺点是我们不能完全实现 3D 效果。overflow <code>hidden</code> 将解决这个问题它。我们还需要将绳索穿过窗户下方，这意味着窗台会阻止我们实现效果。</p>
<p>不过，我们还是可以非常接近地实现这个效果了。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fjh3y%2Fpen%2FqBrEMEe" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/jh3y/pen/qBrEMEe" ref="nofollow noopener noreferrer">CodePen jh3y/qBrEMEe</a></p>
<p>上述演示使用预处理器生成容器查询步骤。在每一步，范围内的自定义属性都会更新。这就展示了彼得并打开了百叶窗。</p>
<p>这里的技巧是放大容器以使调整大小的句柄更大，然后我缩小内容以适应它原本的样子。</p>
<hr>
<p>这个有趣的演示“揭穿模因”还无法 100% 实现，但是，我们已经越来越近了。容器查询是一个令人兴奋的前景。看看它们如何随着浏览器支持的发展而变化会很有趣。看到人们如何突破极限或以不同方式使用它们，也会令人兴奋。</p>
<p>谁知道？有一天，“Resize Hack”可能会与臭名昭著的“Checkbox Hack”并驾齐驱。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            