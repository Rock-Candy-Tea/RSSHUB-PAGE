
---
title: '阿ken的HTML、CSS的学习笔记_浮动与定位（笔记六）2'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bf31ac487394f5b97a9cef0d85d26ad~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 20:55:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bf31ac487394f5b97a9cef0d85d26ad~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>6.1.2_清除浮动 clear</h2>
<p>在网页中，<strong>由于浮动元素不再占用原文档流的位置，使用浮动时会影响后面相邻的固定元素。</strong></p>
<p>例如上述刚才那个案例中定义完 box03 ，受到其周围元素浮动的影响，产生了位置上的变化。这时如果要避免浮动对其他元素的影响，就需要清除浮动。在 CSS 中，使用 clear 属性清除浮动，其基本语法格式如下。</p>
<pre><code class="hljs language-css copyable" lang="css">选择器 &#123; 
<span class="hljs-attribute">clear</span>: 属性值; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>clear 的常用属性值：</strong></p>





















<table><thead><tr><th>属性值</th><th>描述</th></tr></thead><tbody><tr><td>left</td><td>不允许左侧有浮动元素(清除左侧浮动的影响)</td></tr><tr><td>right</td><td>不允许右侧有浮动元素(清除右侧浮动的影响)</td></tr><tr><td>both</td><td>同时清除左右两侧浮动的影响</td></tr></tbody></table>
<p>案例：< p>标记应用 clear 属性来清除浮动元素对段落文本的影响，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>清除元素的左浮动<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.father</span> &#123;   <span class="hljs-comment">/*定义父元素的样式*/</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
&#125;

<span class="hljs-selector-class">.box01</span>, <span class="hljs-selector-class">.box02</span>, <span class="hljs-selector-class">.box03</span> &#123; 
<span class="hljs-comment">/*定义box01、box02、box03三个盒子的样式*/</span>
<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#FF9</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#F33</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">15px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">float</span>: left; <span class="hljs-comment">/*定义box01、box02、box03 左浮动*/</span>
&#125;

<span class="hljs-selector-tag">p</span> &#123;  <span class="hljs-comment">/*定义段落文本的样式*/</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#FCF</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#F33</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">15px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">clear</span>: left;  <span class="hljs-comment">/*清除左浮动*/</span>
<span class="hljs-comment">/*上一行代码用于清除段落文本左侧浮动元素的影响*/</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box01"</span>></span>box01<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box02"</span>></span>box02<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box03"</span>></span>box03<span class="hljs-tag"></<span class="hljs-name">d1v</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>111<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bf31ac487394f5b97a9cef0d85d26ad~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923445ae1af64dddadfd5ac629b81fbd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行后可以看出，清除段落文本左侧的浮动后，段落文本不再受到浮动元素的影响，而是按照元素自身的默认排列方式，独占一行，排列在浮动元素 box01、 box02、box03的下面。</p>
<p>**需要注意的是， clear 属性只能清除元素左右两侧浮动的影响。**然而在制作网页时，经常会遇到一些特殊的浮动影响。例如，对子元素设置浮动时，如果不对其父元素定义高度，则子元素的浮动会对父元素产生影响，</p>
<p>案例：演示上述例子，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>清除浮动<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.father</span> &#123;  <span class="hljs-comment">/*没有给父元素定义高度*/</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
&#125;

<span class="hljs-selector-class">.box01</span>, <span class="hljs-selector-class">.box02</span>, <span class="hljs-selector-class">.box03</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#f9c</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">15px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">float</span>: left;
<span class="hljs-comment">/*定义box01、box02、box03三个盒子左浮动*/</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box01"</span>></span>box01<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box02"</span>></span>box02<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box03"</span>></span>box03<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6373e497ca1c4865ab4d2f6560c89e93~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码为 box01、box02、box03 三个子盒子定义左浮动，同时，不给其父元素设置高度。</p>
<p>运行后，由于受到子元素浮动的影响，没有设置高度的父元素变成了一条直线，即父元素不能自适应子元素的高度了。</p>
<p><strong>我们知道子元素和父元素为嵌套关系，不存在左右位置，所以使用 clear 属性并不能清除子元素浮动对父元素的影响。对于这种情况该如何清除浮动呢?具体介绍如下。</strong></p>
<ul>
<li><strong>方法一: 使用空标记清除浮动</strong><br>
_<br>
在浮动元素之后添加空标记，并对该标记应用 " clear:both " 样式，可清除元素浮动所产生的影响，这个空标记可以为 < div>、< p>、 < hr /> 等任何标记。<br>
_<br>
案例：演示使用空标记清除浮动的方法，</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>空标记清除浮动<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.father</span> &#123;  <span class="hljs-comment">/*没有给父元素定义高度*/</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border</span>: lpx dashed <span class="hljs-number">#999</span>;
&#125;

<span class="hljs-selector-class">.box01</span>, <span class="hljs-selector-class">.box02</span>, <span class="hljs-selector-class">.box03</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#f9c</span>;
<span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> dashed <span class="hljs-number">999</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">15px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">float</span>: left;
<span class="hljs-comment">/*定义box01、box02、box03三个盒子左浮动*/</span>
&#125;

<span class="hljs-selector-class">.box04</span> &#123; 
<span class="hljs-attribute">clear</span>: both;
&#125;

<span class="hljs-comment">/*对空标记应用clear:both;*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box01"</span>></span>box01<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box02"</span>></span>box02<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box03"</span>></span>box03<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box04"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!--在浮动元素后添加空标记--></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5143d284a9c24fd7aa3cd21b9bb02881~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在浮动元素 box01、box02、box03 之后添加 class 为 box04 的空 div ，然后对 box04 应用 " clear: both; " 样式。</p>
<p>父元素被其子元素撑开了，即子元素的浮动对父元素的影响已经不存在。</p>
<p>需要注意的是，上述方法虽然可以清除浮动， 但是在无形中增加了毫无意义的结构元素(空标记)，因此在实际工作中不建议使用。</p>
<p>(空标记)因此在实际工作中不建议使用。</p>
<ul>
<li><strong>方法二:使用 overflow 属性清除浮动</strong><br>
_<br>
对元素应用 " overflow: hidden; " 也可以清除浮动对该元素的影响，该方法弥补了空标记清除浮动的不足。</li>
</ul>
<p>案例：演示使用 overflow 属性清除浮动的方法，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>overflow属性清除浮动<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-comment">/*没有给父元素定义高度*/</span>
<span class="hljs-selector-class">.father</span> &#123;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
<span class="hljs-attribute">overflow</span>: hidden;   <span class="hljs-comment">/*对父元素应用overflow:hidden;*/</span>
&#125;

<span class="hljs-selector-class">.box01</span>, <span class="hljs-selector-class">.box02</span>, <span class="hljs-selector-class">.box03</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#f9c</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">15px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">float</span>: left;
<span class="hljs-comment">/*定义box01、box02、box03三个盒子左浮动*/</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box01"</span>></span>box01<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box02"</span>></span>box02<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box03"</span>></span>box03<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对父元素应用 " overflow: hidden; " 样式来清除子元素浮动对父元素的影响。</strong></p>
<p>父元素又被其子元素撑开了，即子元素浮动对父元素的影响已经不存在。</p>
<ul>
<li>方法三: 使用 after 伪对象清除浮动</li>
</ul>
<p>使用 after 伪对象也可以清除浮动，但是该方法只适用于 IE8 及以上版本浏览器和其他非 IE 浏览器。</p>
<p>另外，使用 after 伪对象清除浮动时需要注意：</p>
<p>(1) 必须为需要清除浮动的元素伪对象设置 " height: (); " 样式，否则该元素会比其实际高度高出若干像素。</p>
<p>(2) 必须在伪对象中设置 content 属性，属性值可以为空，如 " content：" " ; 。</p>
<p>案例：演示使用 after 伪对象清楚浮动的方法。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">htm1</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>使用after伪对象清除浮动<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.father</span> &#123;      <span class="hljs-comment">/*没有给父元素定义高度*/</span>
<span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
&#125;

<span class="hljs-selector-class">.father</span>:after &#123;   /*对父元素应用after伪对象样式*/
display: block;
<span class="hljs-attribute">clear</span>: both;
<span class="hljs-attribute">content</span>:<span class="hljs-string">""</span>;
<span class="hljs-attribute">visibility</span>: hidden;
<span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.box01</span>, <span class="hljs-selector-class">.box02</span>, <span class="hljs-selector-class">.box03</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#f9c</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#999</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">15px</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">10px</span>;
<span class="hljs-attribute">float</span>: left;  <span class="hljs-comment">/*定义box01、box02、box03三个盒子左浮动*/</span>
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box01"</span>></span>box01<span class="hljs-tag"></<span class="hljs-name">d1v</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box02"</span>></span>box02<span class="hljs-tag"></<span class="hljs-name">d1v</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box03"</span>></span>box03<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第 11 ~ 17 行代码用于为父元素应用 after 伪对象样式来清除浮动。</p>
<p>父元素又被其子元素撑开了，即子元素浮动对父元素的影响已经不存在。</p></div>  
</div>
            