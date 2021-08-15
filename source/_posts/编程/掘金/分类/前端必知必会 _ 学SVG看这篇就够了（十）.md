
---
title: '前端必知必会 _ 学SVG看这篇就够了（十）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd906ecfb754d52b39302f099827d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:05:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd906ecfb754d52b39302f099827d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">这是SVG系列目录：</h3>
<ul>
<li><a href="https://juejin.cn/post/6993211337509699620" target="_blank" title="https://juejin.cn/post/6993211337509699620">前端必知必会 | 学SVG看这篇就够了（一）</a></li>
<li><a href="https://juejin.cn/post/6993607549576544270" target="_blank" title="https://juejin.cn/post/6993607549576544270">前端必知必会 | 学SVG看这篇就够了（二）</a></li>
<li><a href="https://juejin.cn/post/6994024417001111560" target="_blank" title="https://juejin.cn/post/6994024417001111560">前端必知必会 | 学SVG看这篇就够了（三）</a></li>
<li><a href="https://juejin.cn/post/6994432253484859406" target="_blank" title="https://juejin.cn/post/6994432253484859406">前端必知必会 | 学SVG看这篇就够了（四）</a></li>
<li><a href="https://juejin.cn/post/6994790295439327269" target="_blank" title="https://juejin.cn/post/6994790295439327269">前端必知必会 | 学SVG看这篇就够了（五）</a></li>
<li><a href="https://juejin.cn/post/6995081482851057671" target="_blank" title="https://juejin.cn/post/6995081482851057671">前端必知必会 | 学SVG看这篇就够了（六）</a></li>
<li><a href="https://juejin.cn/post/6995479935666094094" target="_blank" title="https://juejin.cn/post/6995479935666094094">前端必知必会 | 学SVG看这篇就够了（七）</a></li>
<li><a href="https://juejin.cn/post/6995581188463149070" target="_blank" title="https://juejin.cn/post/6995581188463149070">前端必知必会 | 学SVG看这篇就够了（八）</a></li>
</ul>
<h4 data-id="heading-1">前言</h4>
<p><code>SVG</code>支持多种遮罩效果，使用这些特性，你可以在你的项目中生产出很多很酷炫的效果。分为剪切路径和遮罩,让我们一起来看看吧 👇👇👇</p>
<ul>
<li>剪切路径<code>cliping path</code>
<ul>
<li>在剪切路径内图形是可见的，在剪切路径之外的图形是不可见的。</li>
</ul>
</li>
<li>遮罩<code>mask</code>
<ul>
<li>遮罩是一种容器，它一定了一组图形并将它们作为半透明的媒介，可以用来组合前景对象和背景。</li>
</ul>
</li>
<li>裁剪路径和其他的蒙板一个重要的区别就是：裁剪路径是1位蒙板，也就是说裁剪路径覆盖的对象要么就是全透明（可见的，位于裁剪路径内部），要么就是全不透明（不可见，位于裁剪路径外部）。而蒙板可以指定不同位置的透明度。</li>
</ul>
<h4 data-id="heading-2">剪切</h4>
<p>剪切路径使用<code>clipPath</code>标签定义，后使用<code>clip-path</code>属性引用，它用于限制一个图形的显示。当图形超出<code>clipPath</code>规定的范围，那么超出的范围将不会绘制出来。这个图形可以是使用简单的图形绘画、<code>path</code>、<code>text</code>等图形绘制标签</p>
<p>下面是一个<code>clipPath</code>标签使用的例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">clipPath</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cTest"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50"</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">clipPath</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">clip-path</span>=<span class="hljs-string">"url(#cT
</svg>
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd906ecfb754d52b39302f099827d92~tplv-k3u1fbpfcp-watermark.image" alt="51.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个例子，将一个<code>100*100</code>的正方形遮挡了一半，因为我们使用了<code>clipPath</code>限制了它的绘制范围。它甚至还可以用于<code>text</code>标签，我们把上面例子的代码改改。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">clipPath</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cTest"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">font-size</span>=<span class="hljs-string">"10"</span>></span>用文本定范围<span class="hljs-tag"></<span class="hljs-name">text</span>></span><span class="hljs-tag"></<span class="hljs-name">clipPath</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">clip-path</span>=<span class="hljs-string">"url(#cTest)"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"red"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"45"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"green"</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">g</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c16b981995b34aefbe84c9a93c67f4ea~tplv-k3u1fbpfcp-watermark.image" alt="52.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>clipPath</code>标签还有一个<code>clipPathUnits</code>属性，用于定义用于元素内容的坐标系。</p>
<ul>
<li><strong>userSpaceOnUse</strong>（默认值）：<code>x</code>、<code>y</code>、<code>width</code>和<code>height</code>表示的值都是当前用户坐标系统的值。也就是说，这些值没有缩放，都是绝对值。</li>
<li><strong>objectBoundingBox</strong>：<code>x</code>、<code>y</code>、<code>width</code>和<code>height</code>表示的值都是当前剪切路径的图形的用户坐标系和包围图形比例值。</li>
</ul>
<h4 data-id="heading-3">遮罩</h4>
<p>遮罩的效果最令人印象深刻的是表现为一个渐变。如果你想要让一个元素淡出，你可以利用遮罩效果实现这一点。</p>
<p>我们简单对比下剪切路径和遮罩的区别：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">linearGradient</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"Gradient"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">stop-color</span>=<span class="hljs-string">"white"</span> <span class="hljs-attr">stop-opacity</span>=<span class="hljs-string">"0"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">stop-color</span>=<span class="hljs-string">"white"</span> <span class="hljs-attr">stop-opacity</span>=<span class="hljs-string">"1"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">linearGradient</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">clipPath</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cp"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"35"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"35"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">clipPath</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">mask</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"Mask"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#Gradient)"</span>  /></span>
      <span class="hljs-tag"></<span class="hljs-name">mask</span>></span>
<span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
<span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"./img/1.jpg"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50px"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50px"</span> <span class="hljs-attr">mask</span>=<span class="hljs-string">"url(#Mask)"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"./img/1.jpg"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50px"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50px"</span> <span class="hljs-attr">clip-path</span>=<span class="hljs-string">"url(#cp)"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec7cfc2ffd304412804a4377e3e627ab~tplv-k3u1fbpfcp-watermark.image" alt="53.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上例子中，我们将定义了一个简单的渐变效果，并绘制了一个矩形引用了它。最后用<code>mask</code>标签包裹了这个矩形。所以实现了图片与白色之间的渐变效果。遮罩与剪切路径类似，只不过是半透明的。遮罩通常用于将两个不同的对象进行组合显示，而剪切路径用于剪切图形。</p>
<p><code>mask</code>还可以设置以下属性</p>
<ul>
<li><strong>maskUnits</strong>： 定义<code>mask</code>标签中的坐标系统，引用该遮罩的图形的坐标系</li>
<li>**maskContentUnits **： 定义<code>mask</code>标签中子元素的坐标系统</li>
<li><code>x</code> / <code>y</code> 该属性分别设置图形的 <code>x</code> / <code>y</code> 轴坐标，在<code>mask</code>元素中 <code>x</code> / <code>y</code> 默认值为<code>-10%</code></li>
<li><code>width</code> / <code>height</code> 该属性在用户坐标系统中标识了一个水平 / 垂直长度，在<code>mask</code>元素中<code>x</code>默认值为<code>120%</code></li>
</ul>
<h4 data-id="heading-4">最后</h4>
<p>本篇文章讲述了在<code>SVG</code>中剪切路径与遮罩相关知识，感谢你的阅读！</p>
<p>😀😀 <strong>关注我，不迷路！</strong> 😀😀</p></div>  
</div>
            