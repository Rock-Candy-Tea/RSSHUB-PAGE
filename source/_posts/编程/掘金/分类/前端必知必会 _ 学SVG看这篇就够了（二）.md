
---
title: '前端必知必会 _ 学SVG看这篇就够了（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a78e60ab4a9b4ddeb04d7425f5ac8a27~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 00:54:32 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a78e60ab4a9b4ddeb04d7425f5ac8a27~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">这是SVG系列目录：</h3>
<ul>
<li><a href="https://juejin.cn/post/6993211337509699620" target="_blank" title="https://juejin.cn/post/6993211337509699620">前端必知必会 | 学SVG看这篇就够了（一）</a></li>
</ul>
<h4 data-id="heading-1">前言</h4>
<p>在上一篇文章中，我们已经学习了简单的SVG的绘画，如何去引入<code>SVG</code>文件。接下来我们继续看看<code>SVG</code>中的定位系统与<code>viewBox</code>的知识点。</p>
<h4 data-id="heading-2">SVG定位</h4>
<p>在<code>SVG</code>元素使用的是坐标系统（网络系统），和<code>Canvas</code>类似。以页面的左上角为起标点，以<code>px</code>为单位，x轴的正方形是向右边的，而y轴正方向是向下边。</p>
<p>看下面这个例子，绘画一个矩形，在<code>rect</code>标签中加入<code>x</code>和<code>y</code>属性，从左上角开始，向右边偏移<code>50px</code>的距离，再向下偏移<code>60px</code>的距离，开始绘画一个宽高各<code>100</code>的矩形。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#f06"</span> /></span>
    <span class="hljs-comment"><!--x表示横坐标，y表示纵坐标，width表示宽，height表示高--></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a78e60ab4a9b4ddeb04d7425f5ac8a27~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">viewBox属性</h4>
<p><code>viewBox</code>是<code>svg</code>标签中的一个属性，它允许指定一个给定的一组图形伸展以适应特定的容器元素。</p>
<p><code>viewBox</code>属性的值是一个包含<code>4</code>个参数的列表 <code>min-x</code>, <code>min-y</code>, <code>width</code> ,<code>height</code>， 以空格或者逗号分隔开， 在用户空间中指定一个矩形区域映射到给定的元素，不允许宽度和高度为负值,<code>0</code>则禁用元素的呈现。</p>
<p>例如，我用<code>SVG</code>画了一个半径<code>200px</code>圆形，在一个<code>400*400</code>的画布上的话这个圆形刚刚好占满了整个画布，这时候显示没有问题。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#f00"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但在实际开发中，页面的画布尺寸是根据实际业务来设定的，不一定是刚刚好。例如在宽高<code>200*200</code>的画布上那它将是这样子显示出来的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89856176357e4cbc9cbe29406b62de03~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/861bea2f7b1746cba18eb0bf29cdae0f~tplv-k3u1fbpfcp-watermark.image" alt="zb.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样子肯定不是我们想看到的效果，我们可以修改下圆的大小，但是实际开发中可能是个复杂的<code>SVG</code>呢？<code>viewBox</code>属性就是来解决这个问题的。</p>
<p>在<code>SVG</code>标签加入<code>viewBox</code>属性：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 400 400"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#f00"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb9fb53343e34e208935672adfcd3f39~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这里的<code>viewBox</code>是一个<code>400*400</code>的正方形，此时它的单位不是<code>px</code>，是一个虚拟的单位。我们在<code>viewBox</code>里边放入了一个圆，这个圆的半径是200，但放入<code>viewBox</code>后它的单位不是<code>px</code>，而是变成了和<code>viewBox</code>的虚拟单位。这个虚拟单位代表的长度是会变动的。</p>
<p>这个虚拟单位我们是可以计算出来的，即<code>200px/400=0.5px</code>。所以<code>viewBox</code>内部的所有数值去乘<code>0.5px</code>才是真正的长度大小。</p>
<p>前面两个参数指的是对内部SVG做一个整体的位移，通常设置<code>0 0</code>，这里我们用不到这个参数，不做任何设置。</p>
<h4 data-id="heading-4">preserveAspectRatio属性</h4>
<p>这个属性直接翻译过来是意思是：<strong>保留纵横比</strong>，它跟<code>viewBox</code>的关系特别密切，它表示是否强制进行统一缩放.，如果你设置了<code>viewBox</code>属性，不声明这个<code>preserveAspectRatio</code>属性，<code>viewBox</code>也会给这个属性声明一个默认值为<code>xMidYMid meet</code>。</p>
<p>我们上面的例子，画布的宽高和<code>viewBox</code>的宽高比是一样<code>1:1</code>的。但实际开发中我们不可能一直跟画布保持一样的比例。此时就需要声明<code>preserveAspectRatio</code>属性了，该属性也是应用在<code>svg</code>标签上的。</p>
<p>我们先看看它第一个参数都有哪些属性可以设定：</p>
<ul>
<li><strong>none</strong>
不会进行强制统一缩放，如果需要，会缩放指定元素的图形内容，使元素的边界完全匹配视图矩形。
(注意：如果第一个参数的值是 <code>none</code> ，则属性的第二个值将会被忽略。)</li>
<li><strong>xMinYMin</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的最小值与视图的X的最小值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的最小值与视图的Y的最小值对齐。</li>
<li><strong>xMidYMin</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的中点值与视图的X的中点值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的最小值与视图的Y的最小值对齐。</li>
<li><strong>xMaxYMin</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的最小值+元素的宽度与视图的X的最大值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的最小值与视图的Y的最小值对齐。</li>
<li><strong>xMinYMid</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的最小值与视图的X的最小值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的中点值与视图的Y的中点值对齐。</li>
<li><strong>xMidYMid</strong> (默认值) - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的中点值与视图的X的中点值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的中点值与视图的Y的中点值对齐。</li>
<li><strong>xMaxYMid</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的最小值+元素的宽度与视图的X的最大值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的中点值与视图的Y的中点值对齐。</li>
<li><strong>xMinYMax</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的最小值与视图的X的最小值对齐。
将SVG元素的<code>viewbox</code>属性的Y的最小值+元素的高度与视图的Y的最大值对齐。</li>
<li><strong>xMidYMax</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的中点值与视图的X的中点值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的最小值+元素的高度与视图的Y的最大值对齐。</li>
<li><strong>xMaxYMax</strong> - 强制统一缩放。
将<code>SVG</code>元素的<code>viewbox</code>属性的X的最小值+元素的宽度与视图的X的最大值对齐。
将<code>SVG</code>元素的<code>viewbox</code>属性的Y的最小值+元素的高度与视图的Y的最大值对齐。</li>
</ul>
<p>第二个参数是可选的，如果填写第二个参数的时候，你需要第一个参数后面使用空格符，将两个参数隔开。</p>
<ul>
<li>
<p><code>meet</code>(默认值) - 图形将缩放到:</p>
<ul>
<li>宽高比将会被保留</li>
<li>整个<code>SVG</code>的<code>viewbox</code>在视图范围内是可见的</li>
<li>尽可能的放大<code>SVG</code>的<code>viewbox</code>，同时仍然满足其他的条件。</li>
</ul>
<p>在这种情况下，如果图形的宽高比和视图窗口不匹配，则某些视图将会超出<code>viewbox</code>范围（即<code>SVG</code>的<code>viewbox</code>视图将会比可视窗口小）。</p>
</li>
<li>
<p><code>slice</code>图形将缩放到:</p>
<ul>
<li>宽高比将会被保留</li>
<li>整个视图窗口将覆盖<code>viewbox</code></li>
<li><code>SVG</code>的<code>viewbox</code>属性将会被尽可能的缩小，但是仍然符合其他标准。</li>
</ul>
<p>在这种情况下，如果<code>SVG</code>的<code>viewbox</code>宽高比与可视区域不匹配，则<code>viewbox</code>的某些区域将会延伸到视图窗口外部（即<code>SVG</code>的<code>viewbox</code>将会比可视窗口大）。</p>
</li>
</ul>
<p>在了解这个属性和他的参数之后，我们修改上面的例子，让画布的比例成<code>1:2</code>，现在画布的高度已经发生了改变，圆垂直居中了</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"400"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 400 400"</span>></span><span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#f00"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4796e7d36d2448a18cbe25abcb09ac3f~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们画布和<code>viewBox</code>的两者比例是不同的，可以看到我们的圆被居中了。此时我们要配置<code>preserveAspectRatio</code>属性，让元素左对齐。也就是<code>xMinxMin</code>值。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"400"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 400 400"</span> <span class="hljs-attr">preserveAspectRatio</span>=<span class="hljs-string">"xMinYMin"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#f00"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c20a51f6b2bd4299a20ee77040514135~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">最后</h4>
<p>本篇文章讲述了SVG的定位系统以及<code>SVG</code>标签中<code>viewBox</code>属性和<code>preserveAspectRatio</code>的基本使用，感谢你的阅读！</p>
<p>😀😀 <strong>关注我，不迷路！</strong>  😀😀</p></div>  
</div>
            