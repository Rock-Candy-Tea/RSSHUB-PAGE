
---
title: 'CSS系列 -- 清除浮动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/644ebae7e2e649dc930bd69e6acb7f9f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 21:34:12 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/644ebae7e2e649dc930bd69e6acb7f9f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">场景</h2>
<p>一个大盒子 Box，里面包含两个小盒子 box1、box2，想让 box1、box2 的高度来撑开 Box ，使得 Box 能做到 <strong>高度自适应</strong>（因为大盒子 Box 里面可能还有其他盒子 box3、box4、... 只是它们还未因为用户交互而被添加上去）。代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.Box</span>&#123;
  <span class="hljs-attribute">background-color</span>: gray;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-class">.box1</span>&#123;
  <span class="hljs-attribute">background-color</span>: yellow;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">25px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
&#125;
<span class="hljs-selector-class">.box2</span>&#123;
  <span class="hljs-attribute">background-color</span>: blue;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">75px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看到：Box 没有设置高度，但其包含的 box1 有高度 40px、box2 有高度 60px，所以其撑开的大盒子 Box 的高度为 40 +60 = 100px</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/644ebae7e2e649dc930bd69e6acb7f9f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果大盒子 Box 里面有小盒子 box1 或 box2 或两者都因为需求被设为浮动，那么<strong>浮动元素内容的高是不可以撑起盒子的高</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.Box</span>&#123;
  <span class="hljs-attribute">background-color</span>: gray;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-class">.box1</span>&#123;
  <span class="hljs-attribute">background-color</span>: yellow;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">25px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">float</span>: left;
&#125;
<span class="hljs-selector-class">.box2</span>&#123;
  <span class="hljs-attribute">background-color</span>: blue;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">75px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
  <span class="hljs-attribute">float</span>: right;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1550f2fc00b14c2f8b5f5b01d294da80~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/644a10fe5e34438ca353b33fcc992bb2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccae38c50ad14ea4a7c70c91e80c06ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（ 只有 box1 浮动 ）（ 只有 box2 浮动 ）（ box1 、box2 都浮动 ）</p>
<p>因此我们得出结论：</p>
<blockquote>
<p>浮动产生原因：1. 大盒子<strong>没有设置</strong>高度；2. 内部元素<strong>设置浮动</strong></p>
</blockquote>
<blockquote>
<p>浮动带来的问题：<strong>大盒子内部浮动元素内容的高不可以撑起盒子的高</strong></p>
</blockquote>
<p>所以我们需要清除浮动，这里介绍两种方式：</p>
<h2 data-id="heading-1">清除浮动</h2>
<h3 data-id="heading-2">1. 父级元素设置 overflow: hidden</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.Box</span>&#123;
  <span class="hljs-attribute">background-color</span>: gray;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父级元素被里面的子级元素内容撑开，高度为 max ( box1 , box2 ) = 60 px</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e6b7d40efe47e7b2a6e96efa7f7f05~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>为什么加入overflow:hidden即可清除浮动呢？</strong></p>
<p>那是因为overflow:hidden属性相当于是让父级紧贴内容，这样即可紧贴其对象内内容（包括使用float的div盒子），从而实现了清除浮动。</p>
<h3 data-id="heading-3">2. 在父级元素里面添加带 clear 属性的标签</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"clear"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span> <span class="hljs-comment"><!-- 添加此元素 --></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.clear</span> &#123;
  <span class="hljs-attribute">clear</span>: both; <span class="hljs-comment">/* 为该元素添加属性 clear: both; */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e6b7d40efe47e7b2a6e96efa7f7f05~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">其他方式参考：</h2>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/94697222" target="_blank" rel="nofollow noopener noreferrer">CSS技巧：清除浮动</a></li>
<li><a href="http://www.divcss5.com/jiqiao/j406.shtml" target="_blank" rel="nofollow noopener noreferrer">CSS清除浮动_清除float浮动</a></li>
</ul></div>  
</div>
            