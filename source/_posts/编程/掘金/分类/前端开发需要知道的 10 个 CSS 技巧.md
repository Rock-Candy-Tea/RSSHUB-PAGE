
---
title: '前端开发需要知道的 10 个 CSS 技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcf2ede07da9472aaf92049965c03e16~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 21:36:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcf2ede07da9472aaf92049965c03e16~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>【这是我参与更文挑战的第 <strong>15</strong> 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”】</p>
<p>个人觉得 CSS 是每个前端开发人员都必须掌握的基础，以完成相应的交互和终端设备的响应。在项目开发中，有些容易被忽略的小问题带来项目后期的胶水代码。本文总结一些项目开发中CSS的10个小技巧。</p>
<h3 data-id="heading-0">1.使用相对单位</h3>
<p>通常我们在项目开发中，使用<code>px</code>作为尺寸的单位，而不是使用相对单位，如：<code>rem</code>、<code>em</code>等。在万物互联的时代，最好的方式是相对单位<code>rem</code>、<code>vh</code>、<code>vw</code>等现代 CSS 布局（如 flexbox 和 grid）方式，最大限度的支持各种终端设备。</p>
<h4 data-id="heading-1">绝对单位</h4>
<ul>
<li><code>px</code> ：是一个绝对单位，主要是因为它是固定的，不会根据任何其他元素的测量而改变。</li>
</ul>
<h4 data-id="heading-2">相对单位</h4>
<ul>
<li><code>vw（viewpoint width）</code>：相对于视口的宽度</li>
<li><code>vh（viewpoint height）</code>：相对于视口的高度</li>
<li><code>rem（font size of the root element）</code>：相对于根 ( ) 元素 (默认字体大小通常为 16px )</li>
<li><code>em（font size of the element）</code>：相对于父元素</li>
<li><code>%</code> ：相对于父元素</li>
</ul>
<pre><code class="copyable">/* 不提倡 */
.wrap &#123;
    font-size: 14px;
    margin: 10px;
    line-height: 24px;
&#125;
/* 建议 */
.wrap &#123;
    font-size: 1.2rem;
    margin: 0.5rem;
    line-height: 1.6em;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. 代码复用</h3>
<p>很多开发人员在谈到CSS时都觉得代码重复性很高，在项目开发中这不是一个好的做法。好在现在有CSS预处理器（sass/scss、less、stylus、Turbine），能够让我们可以更好的规划CSS代码，提高其复用性。</p>
<p>当然需要提高代码复用，还是需要一定的CSS的基础，来设计好代码结构，如下：</p>
<pre><code class="copyable">/* 不提倡 */
.container &#123;
    background-color: #efefef;
    border-radius: 0.5rem;
&#125;

.sidebar &#123;
    background-color: #efefef;
    border-radius: 0.5rem;
&#125;

/* 建议 */
.container,
.sidebar &#123;
    background-color: #efefef;
    border-radius: 0.5rem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.CSS重置</h3>
<p>每个浏览器都有自己的默认样式，因此，当网页不包含CSS时，浏览器会为文本添加一些基本的默认样式、填充、边距等。</p>
<p>可以通过使用通用选择器 <code>*</code>  重置 <code>padding</code>、<code>margin</code>、<code>box-sizing</code> 和 <code>font-family</code> 来实现这一点。</p>
<p>像这样：</p>
<pre><code class="copyable">* &#123;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
&#125;
ul,
li &#123;
    list-style: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>不过这些问题现在基本都被框架解决了，对于初学者建议可以模仿但不建议一开始就上框架。</p>
</blockquote>
<h3 data-id="heading-5">4.不使用颜色名称</h3>
<p>不要使用<code>red</code>、<code>blue</code>等颜色名称，相反，建议使用颜色的十六进制值。</p>
<p>为什么呢？因为当使用像 <code>red</code> 这样的颜色名称时，在不同的浏览器或者设备中显示会有所不同。</p>
<pre><code class="copyable">/* 不提倡 */
.container &#123;
    background-color: red;
&#125;

/* 建议 */
.container &#123;
    background-color: #ff0000;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.使用简写属性</h3>
<p>在CSS中，多用简写属性，少用单独属性，具体哪些是简写属性，哪些是单独属性，下面列举一下常见的一些属性，是以通常项目为原则。</p>
<h4 data-id="heading-7">简写属性</h4>
<p><code>background</code>、<code>font</code>、 <code>margin</code>、<code>padding</code>、 <code>border</code>、  <code>transition</code>、 <code>transform</code>、 <code>list-style</code>、 <code>border-radius</code></p>
<h4 data-id="heading-8">单独属性</h4>
<p><code>rotate</code>、<code>scale</code>、<code>background-color</code>、<code>background-image</code>、<code>background-position</code>、<code>padding-left</code>、<code>padding-right</code>、<code>padding-top</code>、<code>padding-bottom</code>、<code>margin-left</code>、<code>margin-top</code>、<code>margin-right</code>、<code>margin-bottom</code>、<code>border-top</code>、 <code>border-right</code>、 <code>border-bottom</code>、<code> border-left</code>、 <code>border-width</code>、 <code>border-color</code>、 <code>border-style</code>、</p>
<pre><code class="copyable">/* 不提倡 */
.container &#123;
    background-image: url(bg.png);
    background-repeat: no-repeat;
    background-position: center;
&#125;

/* 建议 */
.container &#123;
    background: url(bg.png) no-repeat center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">6.文本截取</h3>
<p>在项目开发中，有些列表只需要显示一行文字，有些列表需要显示固定函数的文字，过去通过字符截取的方式来实现，但存在截取不统一（文本内容不同英文、中文、标点符号等），再加上现在各种终端的适配，不足就被放大了。</p>
<p>现在最佳的方式是通过CSS来实现，在文本最后增加省略号（<code>…</code>）。</p>
<h4 data-id="heading-10">单行截取</h4>
<p>元素必须是 <code>block</code> 或 <code>inline-block</code>，如果溢出被隐藏，则文本溢出不起作用，并且元素必须具有定义的宽度或最大宽度集。</p>
<pre><code class="copyable">p &#123;
    display: inline-block;
    max-width: 300px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">多行截取</h4>
<pre><code class="copyable">p &#123;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3; /* 需要显示的行数 */
    overflow: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">7.垂直居中</h3>
<p>垂直居中是一个很常见的需求，有很多实现方式，在伸缩容器内的任何东西垂直居中：</p>
<pre><code class="copyable">.flex-vertically-center &#123;
    display: flex;
    align-items: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>inline</code>、<code>inline-block</code>、<code>table-cell</code> 块垂直对齐：</p>
<pre><code class="copyable">img &#123;
    /* 只对block有效 */
    display: inline-block;
    vertical-align: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相对容器中垂直居中的绝对元素，下面代码是<code>.sub-container</code>在<code>.container</code>垂直居中：</p>
<pre><code class="copyable">.container &#123;
    position: relative;
&#125;
.sub-container &#123;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">8.水平居中</h3>
<p>与垂直对齐类似，不过水平居中更容易一点。</p>
<p>块居中</p>
<pre><code class="copyable">.block-element &#123;
    display: block;
    margin: 0 auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内联或内联块文本居中</p>
<pre><code class="copyable">.container &#123;
    text-align: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在相对容器内水平居中绝对元素：</p>
<pre><code class="copyable">.container &#123;
    position: relative;
&#125;
.sub-container &#123;
    position: absolute;
    top: 50%;
    transform: translateX(-50%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flex 容器内的任何内容水平居中：</p>
<pre><code class="copyable">.flex-vertically-center &#123;
    display: flex;
    justify-content: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">9.设置下一个或上一个兄弟元素样式</h3>
<p>对元素前面和后面的元素进行样式设置，在项目开发中很有用。例如10个按钮，当前按钮下一个及下一个的兄弟元素设置不同的颜色。</p>
<p>html代码如下：</p>
<pre><code class="copyable"><div>
    <button>1</button>
    <button>2</button>
    <button>3</button>
    <button>4</button>
    <button class="current">current</button>
    <button>+ button</button>
    <button>~ button</button>
    <button>~ button</button>
    <button>~ button</button>
    <button>~ button</button>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css代码：</p>
<pre><code class="copyable">.current ~ button &#123;
    background-color: #000;
    color: #ffffff;
&#125;
.current &#123;
    background-color: #ff0000;
&#125;
.current + button &#123;
    background-color: #333;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcf2ede07da9472aaf92049965c03e16~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来设置当前按钮前面样式，css代码如下：</p>
<pre><code class="copyable">button &#123;
    padding: 10px 15px;
    border: 1px solid #444444;
    font-size: 12px;
    background-color: #ff0000;
    color: #000;
&#125;
.current &#123;
    background-color: #000;
    color: #fff;
&#125;
.current ~ button &#123;
    background: initial;
&#125;
.container &#123;
    width: 1000px;
    margin: 50px auto;
    text-align: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80aa5afeff4f4794a5865009e241f657~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">10.宽高比</h3>
<p>如果想让盒子容器有一定的宽高比，如视频播放器尺寸，可以用几种方法来实现，其中有一种方法最直观。可以使用 <code>calc</code> 函数设置顶部填充 <code> (height * width) / 100%</code>。</p>
<p>如下，创建一个 <code>720px</code> 宽的 <code>16 x 9</code> 矩形：</p>
<p>html代码：</p>
<pre><code class="copyable"><div class="container">
    <div class="box"></div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css代码：</p>
<pre><code class="copyable">.container &#123;
    width: 720px;
&#125;
.box &#123;
    padding-top: calc((9 / 16) * 100%);
    background: #efefef;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3d3d33cdd7649308c7df122afc1bfa3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还可以使用 <code>after</code> 伪元素来创建比例大小。</p>
<pre><code class="copyable">.box::after &#123;
    content: "";
    display: block;
    padding-top: calc((9 / 16) * 100%);
    background: #eee;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的方案会导致里面所有的元素都必须向上移动或需要使用绝对定位。不过好消息是，CSS增加了<code>aspect-ratio</code>属性。</p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/aspect-ratio" target="_blank" rel="nofollow noopener noreferrer">aspect-ratio</a> 为box容器规定了一个期待的纵横比，这个纵横比可以用来计算自动尺寸以及为其他布局函数服务。</p>
<h3 data-id="heading-16">总结</h3>
<p>CSS 既有趣又强大，而且还在不断地成长和改进。</p></div>  
</div>
            