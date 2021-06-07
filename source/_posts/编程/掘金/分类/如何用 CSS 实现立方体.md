
---
title: '如何用 CSS 实现立方体'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb796af8c8142eb980c45b4423442c2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 01:16:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb796af8c8142eb980c45b4423442c2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在 <a href="http://algoexpert.io/" target="_blank" rel="nofollow noopener noreferrer">algoexpert.io/</a> 上看到一个非常好玩的东西。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb796af8c8142eb980c45b4423442c2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>刚开始的时候，我还要以为要用到什么 JS 库来实现的，打开控制台研究了一下，原来用 CSS 就可以实现了，好吧，算我孤陋寡闻了，哈哈。于是，写篇博客记录一下吧。</p>
<h2 data-id="heading-0">6 个面</h2>
<p>首先，在 HTML 弄 6 个面。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-faces"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-face cube-face-front"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://yanhaixiang.com/cube/images/js.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"js"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-face cube-face-back"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://yanhaixiang.com/cube/images/python.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"python"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-face cube-face-top"</span>></span>
      <span class="hljs-symbol">&nbsp;</span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-face cube-face-bottom"</span>></span>
      <span class="hljs-symbol">&nbsp;</span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-face cube-face-left"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://yanhaixiang.com/cube/images/golang.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"golang"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cube-face cube-face-right"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://yanhaixiang.com/cube/images/cpp.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"cpp"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非常简单，container 作为正方体容器，cube-faces 作为 6 个面的容器，剩下的 div 就是 6 个面，里面放一个 img。</p>
<p>效果就是一列排下来：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b40bd7cd2884a698069fa2bf2587260~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">集合 6 个面</h2>
<p>第二步，就是将这 6 个面堆叠在一起。很简单，只要 .cube-faces 设置 position: relative，然后 .cube-face 设置 position: absolute 就可以使得 6 个面都脱离文档流叠在一起了。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.cube-faces</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
&#125;

<span class="hljs-selector-class">.cube-face</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">outline</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#02203c</span>;
  <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">100px</span> <span class="hljs-number">#02203c</span>;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3e526a</span>;
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.75</span>;
&#125;

<span class="hljs-selector-class">.cube-face</span> <span class="hljs-selector-tag">img</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd7e2e3b10c14e47a93100598a4b9ce5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">旋转平面</h2>
<p>现在还是一个平面结构，下面将这 6 个面通过 transform: rotate 来做旋转使得其像个正方体。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-front</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">150px</span>);
&#125;

<span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-back</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(-<span class="hljs-number">150px</span>) <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>);
&#125;

<span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-top</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">150px</span>);
  <span class="hljs-attribute">transform-origin</span>: top center;
&#125;

<span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-bottom</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translateY</span>(<span class="hljs-number">150px</span>);
  <span class="hljs-attribute">transform-origin</span>: bottom center;
&#125;

<span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-left</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">270deg</span>) <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">150px</span>);
  <span class="hljs-attribute">transform-origin</span>: left center;
&#125;

<span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-right</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(-<span class="hljs-number">270deg</span>) <span class="hljs-built_in">translateX</span>(<span class="hljs-number">150px</span>);
  <span class="hljs-attribute">transform-origin</span>: top right;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很遗憾，出来的效果还是一个“平面”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b0083bd45ac4192943d186bc69164fa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，这 6 个面其实已经转成了正方体了，但是因为我们目光只朝着一个面看，所以看起来还是二维的。但是也不对呀，如果已经变成立方体，那我们看到的应该是 JS 这一面而不是 Python 这面呀，Python 不是旋转到后面了么？</p>
<p>虽然 Python 是作为后背面，但是在 HTML 里，python 的 div 在 JS 的 div 之后，所以优先显示 Python。</p>
<p>为了去掉 HTML 的顺序影响，可以在 .cube-faces 添加：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.cube-faces</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d; <span class="hljs-comment">/* 3D */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在立方体的 JS 面就朝着我们来了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69ffa64a5f5048d3b3a7b883550447f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">立起来</h2>
<p>下面隆重介绍 CSS 的 perspective 属性，可以把它理解为我们的目光放在哪里。刚刚说到，我们看到二维面是因为我们目光死死盯着一个面，所以我们只需要将目光往上抬一下，从上往下看整个立方体，立方体就“立体”起来了。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*将立方体放中间*/</span>
<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
&#125;

<span class="hljs-selector-class">.cube-container</span> &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">perspective</span>: <span class="hljs-number">800px</span>; <span class="hljs-comment">/* 目光延长线 */</span>
  <span class="hljs-attribute">perspective-origin</span>: <span class="hljs-number">50%</span> <span class="hljs-number">100px</span>; <span class="hljs-comment">/* 目光位置水平居中，往上抬 100px */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb4a8c88d5364b158500572aa9cd9d20~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开始有那味了。</p>
<h2 data-id="heading-4">转起来</h2>
<p>下一步，为了让立方体有动感一点，定义一个 @keyframes 动画：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> spin &#123; <span class="hljs-comment">/* Y轴旋转 */</span>
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">360deg</span>);
  &#125;
&#125;

<span class="hljs-selector-class">.cube-faces</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
  <span class="hljs-attribute">animation</span>: spin <span class="hljs-number">10s</span> infinite linear; <span class="hljs-comment">/*动画*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82413225f75749d28397bd44be2d9cd3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">加点阴影</h2>
<p>现在的立方体已经很立体了，但是总感觉很假的样子，这是因为缺少阴影的原因。我们要以在底部那个 div 加点小阴影：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.cube-face</span><span class="hljs-selector-class">.cube-face-bottom</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>) <span class="hljs-built_in">translateY</span>(<span class="hljs-number">150px</span>);
  <span class="hljs-attribute">transform-origin</span>: bottom center;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">100px</span> <span class="hljs-number">#000</span>; <span class="hljs-comment">/*阴影*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a092fa519d924c08ab6a35edfabcea74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>大功告成！</p></div>  
</div>
            