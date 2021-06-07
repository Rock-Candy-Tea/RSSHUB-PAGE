
---
title: 'CSS 常用布局及解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6475'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 01:27:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=6475'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>CSS 常用布局包括元素的水平、垂直居中，单栏布局、三栏布局等，本文分析多种情况下的布局方案。</p>
<h2 data-id="heading-0">一、居中</h2>
<h3 data-id="heading-1">1. 水平居中</h3>
<p><strong>(1) 基于盒模型的实现</strong></p>
<ul>
<li>子元素为行内元素</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>子元素为行内元素<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-comment">/* 行内元素直接设置文本居中 */</span>
<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>子元素为定宽块状元素</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child child-box"</span>></span>定宽子元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-selector-class">.child-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-comment">/* 设置 margin 值，平分剩余空间 */</span>
<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">margin</span>: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>子元素为不定宽块状元素</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>子元素为不定宽块状元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-comment">/* 子元素设置为 inline，父元素设置文本居中 */</span>
<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">text-align</span>: center;
&#125;
<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">display</span>: inline;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>(2) 基于 flex 的实现</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>flex 布局<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-comment">/* 使用弹性盒子，水平轴设置为居中 */</span>
<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2. 垂直居中</h3>
<p><strong>(1) 基于盒模型的实现</strong></p>
<ul>
<li>父元素一定，子元素为单行内联文本</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>父元素一定，子元素为单行内联文本<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">260px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-comment">/* 设置一个任意行高 */</span>
<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>父元素一定，子元素为多行内联文本</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
    父元素一定，子元素为多行内联文本父元素一定，子元素为多行内联文本父元素一定，子元素为多行内联文本父元素一定，子元素为多行内联文本
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-comment">/* 父元素设置 line-height */</span>
<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">300px</span>;
&#125;
<span class="hljs-comment">/* 子元素设置为内联块级盒子，垂直居中，行高设置为任意一个值 */</span>
<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">1.5</span>;
  <span class="hljs-attribute">vertical-align</span>: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>父元素一定，子元素为块级元素</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child child-box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-selector-class">.child-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="hljs-comment">/* 原理就是 margin 平分剩余空间 */</span>
<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">margin</span>: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>(2) 基于 flex 的实现</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent parent-box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent-box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;

<span class="hljs-selector-class">.parent</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
&#125;

<span class="hljs-selector-class">.child</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid purple;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">二、单列布局</h2>
<h3 data-id="heading-4">1. header、content、footer 为浏览器宽度</h3>
<ul>
<li>方案 1：计算中间列高度</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>></span>头部<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>尾部<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-selector-class">.header</span>,
<span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#009cff</span>;
&#125;

<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100vh</span> - <span class="hljs-number">80px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方案 2：flex 布局</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-direction</span>: column;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-selector-class">.header</span>,
<span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#009cff</span>;
&#125;

<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. header、footer 宽度为浏览器宽度，content 宽度小于浏览器宽度居中</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>></span>头部<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>内容<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>尾部<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-selector-class">.header</span>,
<span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#009cff</span>;
&#125;

<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">80%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100vh</span> - <span class="hljs-number">80px</span>);
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#eee</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种方案参考上一个 demo</p>
<h2 data-id="heading-6">三、三列布局</h2>
<h3 data-id="heading-7">1. 基于盒模型的实现</h3>
<ul>
<li><strong>float + margin</strong></li>
</ul>
<p>左右两列先写，中间列最后写，左右列分别设置一个宽度左右浮动，中间列 margin 左右分别设置为左右列的宽度。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sub"</span>></span>sub<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"extra"</span>></span>extra<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>main<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.sub</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#009cff</span>;
&#125;

<span class="hljs-selector-class">.extra</span> &#123;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#009cff</span>;
&#125;

<span class="hljs-selector-class">.main</span> &#123;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">20%</span>;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">10%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#dff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>position + margin</strong></li>
</ul>
<p>左右元素绝对定位，中间元素的 margin-left、margin-right 对应左右元素的宽度。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sub"</span>></span>left<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>main<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"extra"</span>></span>right<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.sub</span>,
<span class="hljs-selector-class">.extra</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">56</span>, <span class="hljs-number">165</span>, <span class="hljs-number">238</span>);
&#125;
<span class="hljs-selector-class">.sub</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10%</span>;
&#125;

<span class="hljs-selector-class">.extra</span> &#123;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20%</span>;
&#125;

<span class="hljs-selector-class">.main</span> &#123;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10%</span>;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">20%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实现都是中间列要么写在中间，要么写在最后面，不利于主要内容的 seo 和优先渲染，那若是我们想优先渲染主要内容该怎么办呢？DOM Tree 是从上往下解析的，所以我们需要把 main 提到前面，于是就有了下面的布局方案。</p>
<h3 data-id="heading-8">2. 基于盒模型的三列布局增强版</h3>
<ul>
<li><strong>双飞翼布局</strong></li>
</ul>
<p>双飞翼布局也是用 float+margin 进行布局，不同的是 main 被提到了最前面，里面加了个子元素。该布局方案的精髓在于左列和中间列左浮动，右列右浮动，左列设置 margin: -100%，把该列拉回原本的位置，右列设置 margin 为负的自身宽度，回到上一行。main 的宽度设置为容器宽度，子元素 margin 的左右设置为左右列的宽度。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.left</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background-color</span>: antiquewhite;
&#125;
<span class="hljs-selector-class">.right</span> &#123;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background-color</span>: aquamarine;
&#125;
<span class="hljs-selector-class">.main</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">float</span>: left;
&#125;
<span class="hljs-selector-class">.content</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background-color</span>: bisque;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>圣杯布局</strong></li>
</ul>
<p>圣杯布局比双飞翼布局相比，元素嵌套没这么深，主要精髓在于，所有列设置左浮动，左右列设置 position: relative,分别设置对应方向的偏移值。父元素设置左右 margin 分别为左右列的宽度。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>content<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>left<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>right<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">200px</span>;
&#125;
<span class="hljs-selector-class">.left</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100%</span>;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">300px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">background-color</span>: antiquewhite;
&#125;
<span class="hljs-selector-class">.right</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">right</span>: -<span class="hljs-number">200px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background-color</span>: aquamarine;
&#125;
<span class="hljs-selector-class">.main</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">background-color</span>: bisque;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3. 基于 flex 实现三栏布局</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layout"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>主内容栏宽度自适应<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">aside</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>侧边栏宽度固定<span class="hljs-tag"></<span class="hljs-name">aside</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">aside</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right"</span>></span>侧边栏宽度固定<span class="hljs-tag"></<span class="hljs-name">aside</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.layout</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.main</span> &#123;
  <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#aaa</span>;
&#125;

<span class="hljs-selector-class">.left</span>,
<span class="hljs-selector-class">.right</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-class">.left</span> &#123;
  <span class="hljs-attribute">order</span>: -<span class="hljs-number">1</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">10%</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#009cff</span>;
&#125;

<span class="hljs-selector-class">.right</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20%</span>;
  <span class="hljs-attribute">background</span>: orange;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原创文章，首发于<a href="https://canace.site/css%E5%B8%83%E5%B1%80%E7%AF%87/" target="_blank" rel="nofollow noopener noreferrer">个人博客</a>，转载请注明出处</p></div>  
</div>
            