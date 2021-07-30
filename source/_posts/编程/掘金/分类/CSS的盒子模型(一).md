
---
title: 'CSS的盒子模型(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73c4fd1c52684846a59e105f7b60daba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:07:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73c4fd1c52684846a59e105f7b60daba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">盒子的概念</h3>
<p>我们的网页是由一个一个的标签元素组成的，这些标签在CSS的体系中可以理解成一个一个的盒子，一个标签就是一个盒子，理解这些盒子的原理有助于我们更好的实现CSS的布局和排版。
CSS中广泛使用两种盒子:<strong>块级盒子</strong>和<strong>内联盒子</strong>，这两种盒子根据文档流和元素关系的不同会有不同的表现。</p>
<h3 data-id="heading-1">块级盒子和内联盒子</h3>
<h4 data-id="heading-2">块级盒子</h4>
<p>在CSS中通过<strong>display: block</strong>属性将元素定义成块级盒子，在HTML的标签元素中，像div标签、p段落标签、h标题标签等等这些标签在CSS中默认都是块级盒子块级盒子在浏览器中会有以下几个行为:</p>
<blockquote>
<p>1.如果不指定宽度，块级盒子会占满父容器的宽度<br>
2.每个盒子的内容都会自动换行<br>
3.width和height属性会有效果<br>
4.边距(margin/padding)和边框(border)会将其他元素从盒子周围推开</p>
</blockquote>
<p>用一个例子来验证以下块级盒子的这个行为， 我们先来创建一个只有宽高和背景的盒子，然后再添加一些其他的内容来逐个验证。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73c4fd1c52684846a59e105f7b60daba~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个盒子对应的CSS</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.div01</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">display</span>: block;
    <span class="hljs-attribute">background-color</span>: aquamarine;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们给这个盒子指定了宽和高，这也说明我们为块级盒子设置宽高属性是有作用的，现在我们把宽度属性去掉，其他属性不变，来验证以下上面讲到的第一个行为。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18eb042401984f618c284b1818f8e1a6~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，盒子的宽度已经铺满了浏览器。接下来为了显示方便我们依然为盒子指定宽度，并在盒子内部添加一些文字来观察一下盒子的行为。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7110f877cdba4da6bf2c7a1ad5feab02~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们会发现，盒子内部的文字自动换行了，为了进一步验证这个特性，我们继续把盒子由块级改为内联(inline)，其他属性保持不变，然后再观察盒子的内容是否还会换行。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.div01</span>&#123;
    ...
    <span class="hljs-attribute">display</span>: inline;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4ec95ccafc848a0afa5494c01084db6~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们会发现，盒子的内容不仅没有换行，而且原来设置的宽高属性都失效了。</p>
<p>通过上面的例子验证了块级盒子几个特性中的前三个，接下来继续用示例来验证最后一个。我们在刚刚创建的盒子下面再添加一个盒子，让这两个盒子上下紧挨着，为了便于区分两个盒子采用不同的背景色。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a280277e96d1433a88847ff87ac73fd3~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"><br>
我们给盒子1添加边框和margin属性，来观察盒子2的位置变化。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-attribute">border</span>: <span class="hljs-number">3px</span> lightcoral solid;
<span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">10px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1af1d622344496d8dc6543156f4b899~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很明显看到，盒子02的位置发生了位移(注意盒子01的位置是没有发生变化的)，因为border和margin-bottom的存在，使得盒子02向下移动了13px。</p>
<h4 data-id="heading-3">内联盒子</h4>
<p>内联盒子是通过将元素的display属性定义成inline来实现的，在html标签体系中，<code><a></code>标签、 <code><span></code>、 <code><em></code> 以及 <code><strong></code> 都是处于内联状态的。
内联状态的标签元素在浏览器中一般会有以下几种行为:</p>
<blockquote>
<p>1.盒子不会换行<br>
2.width和height属性将不会起作用<br>
3.垂直方向的内外边距以及边框会被应用但是不会把其他处于 <code>inline</code> 状态的盒子推开<br>
4.水平方向的内外边距以及边框会被应用且会把其他处于 <code>inline</code> 状态的盒子推开</p>
</blockquote>
<p>用一个例子来验证以下第三点和第四点，我们定义两个span元素，然后使这两个元素上下排列，为了便于区分需要给两个span设置不同的背景色。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inline"</span>></span>内联盒子01内联盒子01<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inline02"</span>></span>内联盒子02内联盒子02<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d6c753ebc24a8391e125c9ed961142~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后为其中一个span添加边框，最后观察以下效果:</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-selector-class">.inline</span>&#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
    <span class="hljs-attribute">background-color</span>: aquamarine;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">8px</span> solid skyblue;
&#125;
<span class="hljs-selector-class">.inline02</span>&#123;
    <span class="hljs-attribute">background-color</span>: lightblue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/435ee150187d45b184347b62151275a6~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"><br>
可以看到，即便我们给盒子01添加了边框，在内联状态下盒子02相对01的位置和距离依然没有发生变化，并且第一个盒子的边框和下边第二个盒子发生了区域重叠。</p>
<p>接下来我们稍微修改以下示例，再验证一下第四点。我们把上面两个盒子排列方向改为水平排列，再观察一下边框对盒子02的影响。<br>
先看一下没有添加边框的时候两个盒子水平排列时的情况。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48b61c97e9d04288b9f8955aba51df7f~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后继续对盒子01添加边框</p>
<pre><code class="hljs language-CSS copyable" lang="CSS"><span class="hljs-attribute">border</span>: <span class="hljs-number">8px</span> solid lightcoral;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d06e99084bc744748309827ba628c78a~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到水平状态下在给盒子01添加了边框之后，盒子02的位置向右发生了偏移并且两个盒子也没有发生重叠现象。</p>
<p>以上就是关于CSS盒子的简单总结，接下来会继续总结盒子模型的其他主要知识点，然后会形成一个短系列汇总。</p></div>  
</div>
            