
---
title: 'flex布局总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a24c8833b804bb5baf942c42e47e196~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 18:12:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a24c8833b804bb5baf942c42e47e196~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<p>最近在写移动端项目，想着把flex布局，重新梳理一遍，总结下。</p>
<h3 data-id="heading-0">参考地址:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fflex-grammar.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/flex-grammar.html" ref="nofollow noopener noreferrer">www.runoob.com/w3cnote/fle…</a></h3>
<h1 data-id="heading-1">flex布局</h1>
<p>Flex是Flexible Box的缩写，意为”弹性布局”，用来为盒状模型提供最大的灵活性。
任何一个容器都可以指定为Flex布局。
Webkit内核的浏览器，必须加上-webkit前缀。</p>
<pre><code class="hljs language-js copyable" lang="js">.flex &#123;
   <span class="hljs-attr">display</span>: -webkit-flex; <span class="hljs-comment">/* Safari */</span>
   display: flex;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">注意：这时子元素的float，clear和vertical-align就失效了</h5>
<p>以下是实例代码
未加flex</p>
<pre><code class="hljs language-js copyable" lang="js"><style>
    .border_red &#123;
      <span class="hljs-attr">border</span>: 1px solid red;
    &#125;
    .border_blue &#123;
      <span class="hljs-attr">border</span>: 1px solid blue;
    &#125;
    .flex &#123;
      <span class="hljs-attr">display</span>: -webkit-flex; <span class="hljs-comment">/* Safari */</span>
      display: flex;
    &#125;
    .float &#123;
      <span class="hljs-attr">float</span>: right;
    &#125;
    .span1 &#123;
      <span class="hljs-attr">display</span>: inline-block;
      width: 100px;
      height: 100px;
      vertical-align: middle;
    &#125;
    .span2 &#123;
      <span class="hljs-attr">display</span>: inline-block;
      width: 50px;
      height: 50px;
      vertical-align: middle;
    &#125;
</style>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">" border_red"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue float"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span2 border_blue"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a24c8833b804bb5baf942c42e47e196~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在给最外层的div加上flex</p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex border_red"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue float"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span2 border_blue"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e33e69b23507467b92fc5ec9c4d61683~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">基本概念</h1>
<p>采用Flex布局的元素，称为Flex容器（flex container），简称”容器”。它的所有子元素自动成为容器成员，称为Flex项目（flex item），简称”项目”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/882bbcbc3a8344a5abfc0498a3a0d624~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>容器默认存在两根轴：</p>
<p>水平的主轴（main axis）和垂直的交叉轴（cross axis）。</p>
<p>主轴的开始位置（与边框的交叉点）叫做main start，结束位置叫做main end；交叉轴的开始位置叫做cross start，结束位置叫做cross end。</p>
<p>项目默认沿主轴排列。单个项目占据的主轴空间叫做main size，占据的交叉轴空间叫做cross size。</p>
<h1 data-id="heading-4">容器的属性</h1>
<p>以下6个属性设置在容器上。</p>
<ol>
<li>flex-direction 属性决定主轴的方向（即项目的排列方向）。</li>
<li>flex-wrap 默认情况下，项目都排在一条线（又称”轴线”）上。flex-wrap属性定义，如果一条轴线排不下，如何换行。</li>
<li>flex-flow 属性是flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap。</li>
<li>justify-content属性定义了项目在主轴上的对齐方式。</li>
<li>align-items属性定义项目在交叉轴上如何对齐。</li>
<li>align-content属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。</li>
</ol>
<h2 data-id="heading-5">flex-direction</h2>
<p>flex-direction属性决定主轴的方向（即项目的排列方向）。</p>
<ol>
<li>row（默认值）：主轴为水平方向，起点在左端。</li>
<li>row-reverse：主轴为水平方向，起点在右端。</li>
<li>column：主轴为垂直方向，起点在上沿。</li>
<li>column-reverse：主轴为垂直方向，起点在下沿。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">.flex-direction &#123;
   flex-direction: row | row-reverse | column | column-reverse; 
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-direction border_red"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue float"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span1 border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"span2 border_blue"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改下几个span的样式</p>
<pre><code class="hljs language-js copyable" lang="js">.span1 &#123;
      <span class="hljs-attr">display</span>: inline-block;
      width: 100px;
      height: 100px;
      line-height: 100px;
      text-align: center;
      vertical-align: middle;
&#125;
.span2 &#123;
      <span class="hljs-attr">display</span>: inline-block;
      width: 50px;
      height: 50px;
      line-height: 50px;
      text-align: center;
      vertical-align: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>row</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d234912ab7b3402c8d7ce22620783965~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>row-reverse</strong>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4106e1344f3140a18cd1df649f3369f1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>column</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c537c4f017244560b887f46bbc5f16aa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>column-reverse</strong>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5efb6babf53947f8b8880f9c27320392~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">flex-wrap</h2>
<ol>
<li>nowrap（默认）：不换行</li>
<li>wrap：换行，第一行在上方</li>
<li>换行，第一行在下方</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">.flex-wrap &#123;
   flex-wrap: nowrap | wrap | wrap-reverse;
&#125;
.div &#123;
   <span class="hljs-attr">width</span>: <span class="hljs-number">50</span>%;
   height: 50px;
   line-height: 50px;
   text-align: center;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-wrap border_red"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>nowrap</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8bc16662974467da1c12601ba297c9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>wrap</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30e18bd69158419b9e3fdcc8fd4600e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>wrap-reverse</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a5cec2de2d46c4a42b34988cbda41a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">flex-flow</h2>
<p>flex-flow属性是flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap。</p>
<pre><code class="hljs language-js copyable" lang="js">.flex-flow &#123;
    flex-flow: column nowrap;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-flow border_red"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1af35bba19a04f3ba39b12b5e5a31f2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">justify-content</h2>
<p>它可能取5个值，具体对齐方式与轴的方向有关。下面假设主轴为从左到右。</p>
<ol>
<li>flex-start（默认值）：左对齐</li>
<li>flex-end：右对齐</li>
<li>center： 居中</li>
<li>space-between：两端对齐，项目之间的间隔都相等。</li>
<li>space-around：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">.justify-content &#123;
  justify-content: flex-start | flex-end | center | space-between | space-around;
&#125;
.div &#123;
   <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;
   height: 50px;
   line-height: 50px;
   text-align: center;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex justify-content border_red"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">flex-start</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/869d021dc4a64bffb19e35e1484e6a9c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">flex-end</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/430150a3604a4df69250d68d569e196f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">center</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da5d3d3fd3c94d80abd9cc1f95c4b93b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">space-between</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7086241186954756b7df21aaff044482~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">space-around</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96b4c92768e549329dd552e33fbc12eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">align-items</h2>
<ol>
<li>flex-start：交叉轴的起点对齐。</li>
<li>flex-end：交叉轴的终点对齐。</li>
<li>center：交叉轴的中点对齐。</li>
<li>baseline: 项目的第一行文字的基线对齐。</li>
<li>stretch（默认值）：如果项目未设置高度或设为auto，将占满整个容器的高度。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">.align-items &#123;
   align-items: flex-start | flex-end | center | baseline | stretch;
 &#125;
 .div &#123;
   <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;
   text-align: center;
 &#125;
 .div1 &#123;
   <span class="hljs-attr">height</span>: 20px;
   line-height: 20px;
 &#125;
 .div2 &#123;
   <span class="hljs-attr">height</span>: 30px;
   line-height: 30px;
&#125;
.div3 &#123;
  <span class="hljs-attr">height</span>: 40px;
  line-height: 40px;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex align-items border_red"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div2 border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div3 border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">flex-start</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/025dc9250dc2431fa279db6c0bf8c044~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">flex-end</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536e058511e94e2690c3c9655ce39fff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">center</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e8b6b434713478b8cb124d94253a601~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">baseline</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4cf67ef6294229b3f07c5f6e60822c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">stretch</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1851d3ad97d4ddcb80eaa2e603adc6a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">align-content</h2>
<ol>
<li>align-content属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。</li>
<li>flex-start：与交叉轴的起点对齐。</li>
<li>flex-end：与交叉轴的终点对齐。</li>
<li>center：与交叉轴的中点对齐。</li>
<li>space-between：与交叉轴两端对齐，轴线之间的间隔平均分布。</li>
<li>space-around：每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。</li>
<li>stretch（默认值）：轴线占满整个交叉轴。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">.align-content &#123;
      align-content: flex-start | flex-end | center | space-between | space-around | stretch;
&#125;
.flex-wrap &#123;
  flex-wrap: wrap;
&#125;
.div &#123;
  text-align: center;
&#125;
.div1 &#123;
   <span class="hljs-attr">height</span>: 20px;
   width: <span class="hljs-number">30</span>%;
&#125;
.div2 &#123;
   <span class="hljs-attr">height</span>: 30px;
   width: <span class="hljs-number">30</span>%;
&#125;
.div3 &#123;
   <span class="hljs-attr">height</span>: 40px;
   width: <span class="hljs-number">40</span>%;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex align-content flex-wrap border_red"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div2 border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div3 border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div2 border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div3 border_blue"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div1 border_blue"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div div2 border_blue"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">flex-start</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2781e17dcd3438b807ec2636b3c42c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">flex-end</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0911f88be6ad4ec1ad5b103572e0552f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">center</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e25fcfcb74446d3af7745314e2a7729~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">space-between</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949c27437d724d379ffaaad22969ca65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">space-around</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/936faf335e8e499784befffa86aa6bb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">stretch</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43f9e5764ac04a908f8d7eb2ce37e0dc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-27">项目的属性</h1>
<ol>
<li>order</li>
<li>flex-grow</li>
<li>flex-shrink</li>
<li>flex-basis</li>
<li>flex</li>
<li>align-self</li>
</ol>
<h2 data-id="heading-28">order</h2>
<p>order属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。</p>
<pre><code class="hljs language-js copyable" lang="js">.div &#123;
  <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;
  height: 40px;
  text-align: center;
&#125;
.order1 &#123;
  <span class="hljs-attr">order</span>: -<span class="hljs-number">1</span>;
&#125;
.order2 &#123;
  <span class="hljs-attr">order</span>: <span class="hljs-number">0</span>;
&#125;
.order3 &#123;
   <span class="hljs-attr">order</span>: <span class="hljs-number">1</span>;
 &#125;
  <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-wrap border_red"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div order3 border_blue"</span>></span>1-order3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div order2 border_blue"</span>></span>2-order2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div order1 border_blue"</span>></span>3-order1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/919c19e3cc454ffc842d6b5dc88b0103~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">flex-grow</h2>
<p>flex-grow属性定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。</p>
<p>如果所有项目的flex-grow属性都为1，则它们将等分剩余空间（如果有的话）。如果一个项目的flex-grow属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。</p>
<h3 data-id="heading-30">flex-grow: 1;</h3>
<pre><code class="hljs language-js copyable" lang="js">.div &#123;
  <span class="hljs-attr">width</span>: <span class="hljs-number">25</span>%;
  height: 40px;
  text-align: center;
&#125;
.flex-grow1 &#123;
   flex-grow: <span class="hljs-number">1</span>;
&#125;
.flex-grow2 &#123;
   flex-grow: <span class="hljs-number">1</span>;
&#125;
.flex-grow3 &#123;
   flex-grow: <span class="hljs-number">1</span>;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-wrap border_red"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div flex-grow1 border_blue"</span>></span>1-flex-grow1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div flex-grow2 border_blue"</span>></span>2-flex-grow2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div flex-grow3 border_blue"</span>></span>3-flex-grow3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/445dac2da2b4414e9e9e262703f74318~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-31">flex-grow: 2;</h3>
<pre><code class="hljs language-js copyable" lang="js">.flex-grow1 &#123;
   flex-grow: <span class="hljs-number">1</span>;
&#125;
.flex-grow2 &#123;
   flex-grow: <span class="hljs-number">2</span>;
&#125;
.flex-grow3 &#123;
  flex-grow: <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7a8bc952d204d5598d7dc0d92eb27e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-32">flex-shrink</h2>
<p>flex-shrink属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。</p>
<p>如果所有项目的flex-shrink属性都为1，当空间不足时，都将等比例缩小。如果一个项目的flex-shrink属性为0，其他项目都为1，则空间不足时，前者不缩小。</p>
<p>负值对该属性无效。</p>
<h3 data-id="heading-33">flex-shrink: 0;</h3>
<pre><code class="hljs language-js copyable" lang="js"> .flex-wrap &#123;
    flex-wrap: nowrap;
 &#125;
.div &#123;
   <span class="hljs-attr">width</span>: <span class="hljs-number">50</span>%;
   height: 40px;
   text-align: center;
&#125;
.flex-shrink1 &#123;
   flex-shrink: <span class="hljs-number">0</span>;
&#125;
.flex-shrink2 &#123;
   flex-shrink: <span class="hljs-number">1</span>;
&#125;
.flex-shrink3 &#123;
   flex-shrink: <span class="hljs-number">1</span>;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-wrap border_red"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div flex-shrink1 border_blue"</span>></span>1-flex-shrink1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div flex-shrink2 border_blue"</span>></span>2-flex-shrink2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div flex-shrink3 border_blue"</span>></span>3-flex-shrink3<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22fb185e0c29425786d546a5ac864208~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-34">flex-shrink: 1;</h3>
<pre><code class="hljs language-js copyable" lang="js">.flex-shrink1 &#123;
   flex-shrink: <span class="hljs-number">1</span>;
&#125;
.flex-shrink2 &#123;
   flex-shrink: <span class="hljs-number">1</span>;
&#125;
.flex-shrink3 &#123;
   flex-shrink: <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e4b296300d74d85b1a6e2f3d6ed6d57~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-35">flex-basis</h2>
<p>flex-basis属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为auto，即项目的本来大小。</p>
<pre><code class="hljs language-js copyable" lang="js">.flex-basis &#123;
    flex-basis: <length> | auto; <span class="hljs-comment">/* default auto */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">auto</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25982efa2f6b4b9780cb08f5b92d2484~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-37">100px</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c6b610fb18b4f27be99df865603913d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-38">flex</h2>
<p>flex属性是flex-grow, flex-shrink 和 flex-basis的简写，默认值为0 1 auto。后两个属性可选。</p>
<pre><code class="hljs language-js copyable" lang="js">.flex &#123;
      <span class="hljs-attr">flex</span>: none | [ <<span class="hljs-string">'flex-grow'</span>> <<span class="hljs-string">'flex-shrink'</span>>? || <<span class="hljs-string">'flex-basis'</span>> ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">align-self</h2>
<p>align-self属性允许单个项目有与其他项目不一样的对齐方式，可覆盖align-items属性。默认值为auto，表示继承父元素的align-items属性，如果没有父元素，则等同于stretch。</p>
<pre><code class="hljs language-js copyable" lang="js">.align-self &#123;
      align-self: auto | flex-start | flex-end | center | baseline | stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"> .align-self_auto &#123;
    align-self: auto;
 &#125;
 .align-self_flex-start &#123;
   align-self: flex-start;
 &#125;
 .align-self_flex-end &#123;
   align-self: flex-end;
 &#125;
.align-self_center &#123;
  align-self: center;
&#125;
.align-self_baseline &#123;
  align-self: baseline;
&#125;
.align-self_stretch &#123;
   align-self: stretch;
&#125;
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"flex flex-wrap border_red"</span>>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div align-self_auto border_blue"</span>></span>auto<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div align-self_flex-start border_blue"</span>></span>flex-start<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div align-self_flex-end border_blue"</span>></span>flex-end<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div align-self_center border_blue"</span>></span>center<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div align-self_baseline border_blue"</span>></span>baseline<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div align-self_stretch border_blue"</span>></span>stretch<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50b55e6edd5a47bebe9ad947c5aad521~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-40">总结：</h1>
<h2 data-id="heading-41">容器的6个属性</h2>
<h3 data-id="heading-42">控制整列排版的flex-direction，</h3>
<h3 data-id="heading-43">控制整列是否超出换行的flex-wrap，</h3>
<h3 data-id="heading-44">控制列排版和换行的集合flex-flow，</h3>
<h3 data-id="heading-45">控制整列内容横向排版的justify-content</h3>
<h3 data-id="heading-46">控制整列内容纵向排版的align-items</h3>
<h3 data-id="heading-47">控制整列排版的起始点的align-content</h3>
<h2 data-id="heading-48">项目的6个属性</h2>
<h3 data-id="heading-49">控制items顺序的order</h3>
<h3 data-id="heading-50">控制items放大的flex-grow</h3>
<h3 data-id="heading-51">控制items缩小的flex-shrink</h3>
<h3 data-id="heading-52">控制itens初始占据空间的flex-basis</h3>
<h3 data-id="heading-53">flex-grow，flex-shrink，flex-basis的集合flex</h3>
<h3 data-id="heading-54">控制items的对其方式的align-self</h3>
<h4 data-id="heading-55">以上就是所有内容，希望能对大家有所帮助，喜欢的欢迎点赞收藏</h4>
<p>如果有错误的地方，欢迎留言！！！</p>
<p>上一篇：<a href="https://juejin.cn/post/6983647396441931789" target="_blank" title="https://juejin.cn/post/6983647396441931789">mongodb基础用法</a></p></div>  
</div>
            