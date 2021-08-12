
---
title: '前端必知必会 _ 学SVG看这篇就够了（七）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aaf48c7e124485dbc8d9c0af88bf387~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 01:55:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aaf48c7e124485dbc8d9c0af88bf387~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">这是SVG系列目录：</h3>
<ul>
<li><a href="https://juejin.cn/post/6993211337509699620" target="_blank" title="https://juejin.cn/post/6993211337509699620">前端必知必会 | 学SVG看这篇就够了（一）</a></li>
<li><a href="https://juejin.cn/post/6993607549576544270" target="_blank" title="https://juejin.cn/post/6993607549576544270">前端必知必会 | 学SVG看这篇就够了（二）</a></li>
<li><a href="https://juejin.cn/post/6994024417001111560" target="_blank" title="https://juejin.cn/post/6994024417001111560">前端必知必会 | 学SVG看这篇就够了（三）</a></li>
<li><a href="https://juejin.cn/post/6994432253484859406" target="_blank" title="https://juejin.cn/post/6994432253484859406">前端必知必会 | 学SVG看这篇就够了（四）</a></li>
<li><a href="https://juejin.cn/post/6994790295439327269" target="_blank" title="https://juejin.cn/post/6994790295439327269">前端必知必会 | 学SVG看这篇就够了（五）</a></li>
<li><a href="https://juejin.cn/post/6995081482851057671" target="_blank" title="https://juejin.cn/post/6995081482851057671">前端必知必会 | 学SVG看这篇就够了（六）</a></li>
</ul>
<h4 data-id="heading-1">前言</h4>
<p>在<code>SVG</code>中，图形对象一般使用<code>fill</code> 、<code>stroke</code>进行填充。<code>SVG</code>可以自定义一个图形作为填充的背景，这个图形可以是一个<code>SVG</code>元素，也可以是位图图像，下面我们结合实例来讲解如何去使用。</p>
<h4 data-id="heading-2">图案</h4>
<p><code>pattern</code>标签用于定义一个填充对象，可以将定义的这个对象到指定图形中进行重复、平铺、覆盖填充。之后使用自身的属性<code>fill</code> / <code>stroke</code>来引用自定义的填充对象<code>pattern</code>。</p>
<p>它和渐变一样，需要被放置到<code>defs</code>标签中。</p>
<p>我们先看下这个简单例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">pattern</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg_red_circle"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100%"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"25"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"25"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"none"</span> <span class="hljs-attr">fill-opacity</span>=<span class="hljs-string">"0.5"</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">pattern</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"blue"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#bg_red_circle)"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aaf48c7e124485dbc8d9c0af88bf387~tplv-k3u1fbpfcp-watermark.image" alt="34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用<code>pattern</code>定义了一个自定义图案，在<code>pattern</code>标签中放置你想要的图形，这里我们放的是一个红色无填充的圆形。给<code>pattern</code>标签需要绑定一个<code>ID</code>值，用于我们在其他元素上引用这个自定义图案进行填充。</p>
<p>这里是<code>width</code>和<code>height</code>是定义这个<code>pattern</code>是否占满被应用的图形，<code>100%（ or 1 ）</code>即是占满整个元素。如果不是占满，则是重复平铺在被应用的图形上。如果你想要在绘制时偏移矩形的开始点，也可以使用<code>x</code>和<code>y</code>属性</p>
<p>在<code>pattern</code>中，它也有自己的定位系统以及它们的大小。和<code>SVG</code>类似。</p>
<p>上面的例子我们的背景，被填充的图形比例都是<code>1:1</code>，我们再看看另外一个例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">pattern</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg_red_circle"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">patternUnits</span>=<span class="hljs-string">"userSpaceOnUse"</span>
        </<span class="hljs-attr">pattern</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"blue"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#bg_red_circle)"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dffab48e07042389d090eda520e46b8~tplv-k3u1fbpfcp-watermark.image" alt="35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>与上个例子不同的是，这个例子设置了自定义图形的<code>width</code>和<code>height</code>（这与<code>patternUnits</code>有关系），被填充的图形大小则是<code>200*200</code>，当画布还有多余的位置则会平铺填充。</p>
<p>这个例子还多了一个<code>patternUnits</code>属性，  用来定义图案效果区域的单位。他有两个值分别是<code>userSpaceOnUse</code>和<code>objectBoundingBox</code>。他的默认值是<code>objectBoundingBox</code>。</p>
<ul>
<li><strong>objectBoundingBox</strong>：<code>x</code>、<code>y</code>、<code>width</code>和<code>height</code>表示的值都是外框的坐标系统（包裹<code>pattern</code>的元素）。也就是说，图案的单位进行了一个缩放，比如：pattern中为<code>1</code>的值，会变成和包裹元素的外框的<code>width</code>和<code>height</code>一样的大小。（使用这个值时，width和height需要小于<code>1.0</code>，否则图案只会出现一次）</li>
<li><strong>userSpaceOnUse</strong>：<code>x</code>、<code>y</code>、<code>width</code>和<code>height</code>表示的值都是当前用户坐标系统的值。也就是说，这些值没有缩放，都是绝对值。</li>
</ul>
<p>在上面例子中，圆是完美的铺满了整个矩形。我们可以设置<code>x</code>和<code>y</code>值，看看有什么变化？</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">pattern</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg_red_circle"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">patternUnits</span>=<span class="hljs-string">"userSpaceOnUse"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"none"</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">pattern</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"blue"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#bg_red_circle)"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9339d42813744078f7a43990d7a0a02~tplv-k3u1fbpfcp-watermark.image" alt="36.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从矩形的四边，我们可以发现整个图形背景进行了偏移，也就是说<code>x</code>和<code>y</code>属性是修改整个图形的位置。</p>
<p>同样，我们也可以将这个图案应用到描边中</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">pattern</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bg_red_circle"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">patternUnits</span>=<span class="hljs-string">"userSpaceOnUse"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"none"</span>/></span>
        <span class="hljs-tag"></<span class="hljs-name">pattern</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"none"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"url(#bg_red_circle)"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/315b9c5644ec4109b9e31f430548d117~tplv-k3u1fbpfcp-watermark.image" alt="37.png" loading="lazy" referrerpolicy="no-referrer"></p>









































<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>x</td><td>自定义图案<code>x</code>轴坐标</td></tr><tr><td>y</td><td>自定义图案<code>y</code>轴坐标</td></tr><tr><td>width</td><td>自定义图案的宽度</td></tr><tr><td>height</td><td>自定义图案的宽度</td></tr><tr><td>preserveAspectRatio</td><td>以保留原始内容的宽高比</td></tr><tr><td>xlink:href</td><td>用于指另一种模式</td></tr><tr><td>patternUnits</td><td>用来定义图案效果区域的单位</td></tr><tr><td>patternContentUnits</td><td>用来定义模式内容区域的单位</td></tr></tbody></table>
<h4 data-id="heading-3">最后</h4>
<p>本篇文章讲述了在<code>SVG</code>中的如何在创建图案，然后使用<code>fill</code> 、<code>stroke</code>属性引用到绘制的图形中。以及图案中的一些相关属性，感谢你的阅读！</p>
<p>😀😀 <strong>关注我，不迷路！</strong> 😀😀</p></div>  
</div>
            