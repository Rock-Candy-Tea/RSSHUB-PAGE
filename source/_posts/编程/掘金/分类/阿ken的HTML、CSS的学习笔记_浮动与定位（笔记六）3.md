
---
title: '阿ken的HTML、CSS的学习笔记_浮动与定位（笔记六）3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44b911cfcfa443dc94f6834c0787d462~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 20:55:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44b911cfcfa443dc94f6834c0787d462~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.2_overflow 属性</h1>
<p>overflow 属性是 CSS 中的重要属性。<strong>当盒子内的元素超出盒子自身的大小时，内容就会溢出，如果想要规范溢出内容的显示方式，就需要使用 overflow 属性</strong>，其基本语法格式如下。</p>
<pre><code class="hljs language-css copyable" lang="css">选择器 &#123;
<span class="hljs-attribute">overflow</span>: 属性值;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>overflow 的常用属性值：</strong></p>

























<table><thead><tr><th>属性值</th><th>描述</th></tr></thead><tbody><tr><td>visible</td><td>内容不会被修剪，会呈现在元素框之外(默认值)</td></tr><tr><td>hidden</td><td>溢出内容会被修剪，并且被修剪的内容是不可见的</td></tr><tr><td>auto</td><td>在需要时产生滚动条，即自适应所要显示的内容</td></tr><tr><td>scroll</td><td>溢出内容会被修剪，且浏览器会始终显示滚动条</td></tr></tbody></table>
<p>案例：演示 overflow 属性的用法和效果，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>overflow属性<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">sty1e</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span>

div &#123;
width: 100px;
height: 140px;
background: #F99;
overflow: visible;  /*溢出内容呈现在元素框之外*/
&#125;

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
当盒子内的元素超出盒子自身的大小时， 内容就会滥出，如果想要规范後出内容的显示方式，就需要使用overflow属性，它用于规范元素中溢出内容的显示方式。
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第11行代码通过 " overflow：visible; " 样式，定义溢出的内容不会被修剪，而呈现在元素框之外。一般而言，并没有必要设定 overflow 的属性为 visible , 除非你想覆盖它在其他地方设定的值。</p>
<p>运行后可知，溢出的内容不会被修剪，而呈现在元素框之外。</p>
<p>如果希望溢出的内容被修剪，且不可见，可将 overflow 的属性值定义为 hidden 接下来，将第 11 行代码更改如下即可，</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">overflow</span>: hidden;<span class="hljs-comment">/*溢出内容被修剪，且不可见*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后可以看出，使用 " overflow: hidden " 可以将溢出内容修剪，并且被修剪的内容不可见。</p>
<p>另外，如果希望元素框能够多自适应其内容的多少，在内容溢出时，产生滚动条，否则，则不产生滚动条，可以将 overflow 的属性值定义为 auto 。将第 11 行代码更改如下即可，</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">overflow</span>: auto;<span class="hljs-comment">/*根据需要产生活动条*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后可发现，元素框的右侧产生了滚动条，拖动滚动条即可查看溢出的内容。当盒子中的内容减少时，滚动条就会消失。<br>
值得一提的是，当定义 overflow 的属性值为 scroll 时，元素框中也会产生滚动条。将第 11 行代码更改如下即可，</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">overflow</span>: scroll; <span class="hljs-comment">/*始终显示滚动条*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后可发现，元素框中出现了水平和竖直方向的滚动条。与 " overflow: auto; " 不同，当定义 " overflow: scroll; "时，不论元素是否溢出，元素框中的水平和竖直方向的滚动条都始终存在。</p>
<h1 data-id="heading-1"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3_元素的定位</h1>
<p>浮动布局虽然灵活，但是却无法对元素的位置进行精确的控制。在 CSS 中，通过定位属性可以实现网页中元素的精确定位。下面，我们将对<strong>元素的定位属性及常用的几种定位方式</strong>进行详细讲解。</p>
<h2 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.1_元素的定位属性</h2>
<p>制作网页时，如果希望元素出现在某个特定的位置，就需要使用定位属性对元素进行精确定位。<strong>元素的定位就是将元素放置在页面的指定位置，主要包括定位模式和边偏移两部分。</strong></p>
<h3 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. 定位模式</h3>
<p>_<br>
在 CSS 中，<strong>position 属性用于定义元素的定位模式</strong>，其基本语法格式如下。</p>
<pre><code class="hljs language-css copyable" lang="css">选择器 &#123;
<span class="hljs-attribute">position</span>: 属性值;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>position 属性的常用值：</strong></p>

























<table><thead><tr><th>值</th><th>描述</th></tr></thead><tbody><tr><td>static</td><td>静态定位(默认定位方式)</td></tr><tr><td>relative</td><td>相对定位，相对于其原文档流的位置进行定位</td></tr><tr><td>absolute</td><td>绝对定位，相对于其上一个已经定位的父元素进行定位</td></tr><tr><td>fixed</td><td>固定定位，相对于浏览器窗口进行定位</td></tr></tbody></table>
<p>从上表可以看出，定位的方法有多种，分别为静态定位 (static)、相对定位 (relative)、绝对定位 (absolute) 及固定定位 (fixed)，后面我们将对它们进行详细讲解。</p>
<h3 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>2. 边偏移</h3>
<p>_<br>
<strong>定位模式 ( position ) 仅仅用于定义元素以哪种方式定位，并不能确定元素的具体位置</strong>。在 CSS 中，<strong>通过边偏移属性 top、bottom、left 或 right 来精确定义定位元素的位置。</strong></p>
<p><strong>边偏移设置方式：</strong></p>

























<table><thead><tr><th>边偏移属性</th><th>描述</th></tr></thead><tbody><tr><td>top</td><td>顶端偏移量，定义元素相对于其父元素上边线的距离</td></tr><tr><td>bottom</td><td>底部偏移量，定义元素相对于其父元素下边线的距离</td></tr><tr><td>left</td><td>左侧偏移量，定义元素相对于其父元素左边线的距离</td></tr><tr><td>right</td><td>右侧偏移量，定义元素相对于其父元素右边线的距离</td></tr></tbody></table>
<p>从上表可以看出，边偏移可以通过 top、bottom、left、 right 进行设置，其取值为不同单位的数值或百分比，示例如下。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">position</span>: relative; <span class="hljs-comment">/*相对定位*/</span>
<span class="hljs-attribute">left</span>: <span class="hljs-number">50px</span>; <span class="hljs-comment">/*距左边线50px*/</span>
<span class="hljs-attribute">top</span>: <span class="hljs-number">10px</span>;  <span class="hljs-comment">/*距顶部边线10px*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.2_静态定位 static</h2>
<p><strong>静态定位是元素的默认定位方式</strong>，当 position 属性的取值为 static 时，可以将元素定位于静态位置。<strong>所谓静态位置就是各个元素在 HTML 文档流中默认的位置。</strong></p>
<p>任何元素在默认状态下都会以静态定位来确定自己的位置，所以当没有定义 position 属性时， 并不说明该元素没有自己的位置， 它会遵循默认值显示为静态位置。<strong>在静态定位状态下，无法通过边偏移属性 ( top、bottom、left 或 right ) 来改变元素的位置。</strong></p>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.3.3_相对定位 relative</h2>
<p><strong>相对定位是将元素相对于它在标准文档流中的位置进行定位，当 position 属性的取值为 relative 时，可以将元素定位于相对位置。对元素设置相对定位后，可以通过边偏移属性改变元素的位置，但是它在文档流中的位置仍然保留。</strong></p>
<p>案例：演示对元素设置相对定位的方法和效果，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>元素的定位<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">body</span> &#123; 
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0px</span>; 
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span>; 
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>; 
<span class="hljs-attribute">font-weight</span>: bold; 
&#125;

<span class="hljs-selector-class">.father</span> &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> auto;
<span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;
&#125;

<span class="hljs-selector-class">.child01</span>, <span class="hljs-selector-class">.child02</span>, <span class="hljs-selector-class">.child03</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ff0</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0px</span>;
<span class="hljs-attribute">text-align</span>: center;
&#125;

<span class="hljs-selector-class">.child02</span> &#123;
<span class="hljs-attribute">position</span>: relative; <span class="hljs-comment">/*相对定位*/</span>
<span class="hljs-attribute">left</span>: <span class="hljs-number">150px</span>; <span class="hljs-comment">/*距左边线150px*/</span>
<span class="hljs-attribute">top</span>: <span class="hljs-number">100px</span>; <span class="hljs-comment">/*距顶部边线100px*/</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child01"</span>></span>child-01<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child02"</span>></span>child-02<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child03"</span>></span>child-03<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44b911cfcfa443dc94f6834c0787d462~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述第 25 ~ 29 代码对 child02 设置相对定位模式，并通过边偏移属性 left 和 top 改变它的位置。</p>
<p>运行后不难看出，对 child02 设置相对定位后，它会相对于其自身的默认位置进行偏移，但是它在文档流中的位置仍然保留。</p></div>  
</div>
            