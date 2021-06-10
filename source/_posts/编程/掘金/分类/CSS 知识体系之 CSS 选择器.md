
---
title: 'CSS 知识体系之 CSS 选择器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cbb4dd5949c41f0a45b0d66d7d32776~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 01:14:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cbb4dd5949c41f0a45b0d66d7d32776~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与更文挑战的第五天，活动详情查看:<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>层叠样式表 (<code>Cascading</code> Style Sheets<code>，缩写为 </code>CSS<code>），是一种 样式表 语言，用来描述 </code>HTML<code>或</code>XML<code>（包括如 </code>SVG<code>、</code>MathML<code>、</code>XHTML<code>之类的</code>XML<code> 分支语言）文档的呈现。</code>CSS` 描述了在屏幕、纸质、音频等其它媒体上的元素应该如何被渲染的问题。</p>
<p>而<code>CSS</code> 选择器规定了 <code>CSS</code> 规则会被应用到哪些元素上。</p>
<h2 data-id="heading-0">1.1 简单/基本选择器</h2>
<h3 data-id="heading-1"><strong>标签/元素选择器</strong>:</h3>
<ul>
<li>
<p>按照给定的节点名称，选择所有匹配的元素。</p>
</li>
<li>
<p>语法：<code>elementname</code></p>
</li>
<li>
<p>例子：<code>input</code> 匹配任何 <code><input></code> 元素。<code>div</code>(标签选择器)   <code>svg</code>|<code>a</code>(命名空间选择器-html 部分的知识)</p>
</li>
</ul>
<h3 data-id="heading-2"><strong>类选择器</strong>:</h3>
<ul>
<li>
<p>按照给定的 <code>class</code> 属性的值，选择所有匹配的元素。</p>
</li>
<li>
<p>语法：<code>.classname</code>,<code>.class</code> (支持用空格分隔多个)</p>
</li>
<li>
<p>例子：<code>.index</code> 匹配任何 <code>class</code> 属性中含有 "index" 类的元素。</p>
</li>
</ul>
<h3 data-id="heading-3"><strong>ID 选择器</strong>:</h3>
<ul>
<li>
<p>按照 <code>id</code> 属性选择一个与之匹配的元素。需要注意的是，一个文档中，每个 <code>ID</code> 属性都应当是唯一的。</p>
</li>
<li>
<p>语法：<code>#idname</code>,<code>#id</code>(必须完全匹配)</p>
</li>
<li>
<p>例子：<code>#toc</code> 匹配 ID 为 "toc" 的元素。</p>
</li>
</ul>
<h3 data-id="heading-4"><strong>属性选择器</strong>:</h3>
<ul>
<li>
<p>按照给定的属性，选择所有匹配的元素。</p>
</li>
<li>
<p>语法：<code>[attr]</code> <code>[attr=value]</code> <code>[attr~=value]</code> <code>[attr|=value]``[attr^=value]</code> <code>[attr$=value]</code> <code>[attr*=value]</code>。</p>
</li>
<li>
<p>例子：<code>[autoplay]</code> 选择所有具有 <code>autoplay 属性</code>的元素（不论这个属性的值是什么）。</p>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 匹配存在title属性的a标签*/</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[title]</span> &#123;
  <span class="hljs-attribute">color</span>: purple;
&#125;

<span class="hljs-comment">/* 匹配href="https://example.org"的a标签 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[href=<span class="hljs-string">"https://example.org"</span>]</span>
&#123;
  <span class="hljs-attribute">color</span>: green;
&#125;

<span class="hljs-comment">/* 匹配href的内容包含"example"的 a 标签 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[href*=<span class="hljs-string">"example"</span>]</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">2em</span>;
&#125;

<span class="hljs-comment">/* 匹配href的内容以 ".org" 结尾的a标签 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[href$=<span class="hljs-string">".org"</span>]</span> &#123;
  <span class="hljs-attribute">font-style</span>: italic;
&#125;

<span class="hljs-comment">/* 匹配class属性的内容包含"logo"的 a标签 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[class~=<span class="hljs-string">"logo"</span>]</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">2px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><strong>伪类选择器</strong>:</h3>
<ul>
<li>
<p><code>:</code> 伪选择器支持按照未被包含在文档树中的状态信息来选择元素。</p>
</li>
<li>
<p>例子：<code>a:visited</code> 匹配所有曾被访问过的 <code><a></code> 元素。<code>:hover</code>  (伪类)</p>
</li>
</ul>
<h3 data-id="heading-6"><strong>伪元素选择器</strong>:</h3>
<ul>
<li>
<p><code>::</code> 伪选择器用于表示无法用 <code>HTML</code> 语义表达的实体。</p>
</li>
<li>
<p>例子：<code>p::first-line</code> 匹配所有 <code><p></code> 元素的第一行。<code>::before</code>  (伪元素)</p>
</li>
</ul>
<h2 data-id="heading-7">1.2 选择器语法</h2>
<h3 data-id="heading-8">1.2.1 复合选择器</h3>
<p>复合选择器即多个简单选择器的组合，此情况下必须匹配每一个选择器</p>
<ul>
<li><简单选择器><简单选择器><简单选择器></li>
<li><code>*</code> 或者 <code>div</code> 必须写在最前面， <code>伪类</code>，<code>伪元素</code>写在最后面</li>
</ul>
<h3 data-id="heading-9">1.2.2 选择器列表</h3>
<ul>
<li>
<p><code>,</code> 是将不同的选择器组合在一起的方法，它选择所有能被列表中的任意一个选择器选中的节点。</p>
</li>
<li>
<p>语法：<code>A, B</code></p>
</li>
<li>
<p>示例：<code>div , span</code> 会同时匹配 <code><span></code> 元素和 <code><div></code> 元素。</p>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*

*/</span>
<span class="hljs-selector-tag">div</span>,
<span class="hljs-selector-id">#id</span>,
<span class="hljs-selector-class">.class</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">1.2.3 复杂选择器</h3>
<p>复杂选择器也叫组合器, 是把复合选择器用一定的操作符链接</p>
<ul>
<li><复合选择器><code><sp></code><复合选择器></li>
<li><复合选择器><code>></code><复合选择器></li>
<li><复合选择器><code>~</code><复合选择器></li>
<li><复合选择器><code>+</code><复合选择器></li>
<li><复合选择器><code>||</code><复合选择器></li>
</ul>
<h4 data-id="heading-11">1.2.3.1 子孙选择器</h4>
<p>子孙选择器也叫后代组合器（Descendant combinator）</p>
<ul>
<li>
<p><code> </code>(空格)组合器选择前一个元素的后代节点。</p>
</li>
<li>
<p>语法：<code>A B</code></p>
</li>
<li>
<p>例子：<code>div span</code> 匹配所有位于任意 <code><div></code> 元素之内的 <code><span></code> 元素。</p>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*

选中 div 下面 含有  .class 的所有子元素
*/</span>
<span class="hljs-selector-tag">div</span> <span class="hljs-selector-class">.class</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">1.2.3.2 子选择器</h4>
<p>子选择器也叫直接子代组合器（Child combinator）</p>
<ul>
<li>
<p><code>></code> 组合器选择前一个元素的直接子代的节点。</p>
</li>
<li>
<p>语法：<code>A > B</code></p>
</li>
<li>
<p>例子：<code>ul > li</code> 匹配直接嵌套在 <code><ul></code> 元素内的所有 <code><li></code> 元素。</p>
</li>
<li>
<p>特点: 只能选择子一级，是一个严格的父子关系</p>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*
选中 div 下面 含有  .class 的一个子元素
*/</span>
<span class="hljs-selector-tag">div</span> > <span class="hljs-selector-class">.class</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">1.2.3.3 兄弟选择器</h4>
<p>兄弟选择器也叫一般兄弟组合器（General sibling combinator）</p>
<ul>
<li>
<p><code>~</code> 组合器选择兄弟元素，也就是说，后一个节点在前一个节点后面的任意位置，并且共享同一个父节点。</p>
</li>
<li>
<p>语法：<code>A ~ B</code></p>
</li>
<li>
<p>例子：<code>p ~ span</code> 匹配同一父元素下，<code><p></code> 元素后的所有 <code><span></code> 元素。</p>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*

*/</span>
<span class="hljs-selector-tag">div</span> ~ <span class="hljs-selector-class">.class</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">1.2.3.4 邻居选择器</h4>
<p>邻居选择器也叫紧邻兄弟组合器（Adjacent sibling combinator）</p>
<ul>
<li>
<p><code>+</code> 组合器选择相邻元素，即后一个元素紧跟在前一个之后，并且共享同一个父节点。</p>
</li>
<li>
<p>语法：<code>A + B</code></p>
</li>
<li>
<p>例子：<code>h2 + p</code> 会匹配所有紧邻在 <code><h2></code> (en-US) 元素后的 <code><p></code> 元素。</p>
</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*

*/</span>
<span class="hljs-selector-tag">div</span> + <span class="hljs-selector-class">.class</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">1.2.3.5 双竖线(level4 标准)</h4>
<ul>
<li>
<p><code>||</code> 组合器选择属于某个表格行的节点。</p>
</li>
<li>
<p>语法： <code>A || B</code></p>
</li>
<li>
<p>例子： <code>col || td</code> 会匹配所有 <code><col></code> 作用域内的 <code><td></code> 元素。</p>
</li>
</ul>
<p>table 里面去选中一列</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*

*/</span>
<span class="hljs-selector-tag">div</span>||<span class="hljs-selector-class">.class</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2. 选择器优先级</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cbb4dd5949c41f0a45b0d66d7d32776~tplv-k3u1fbpfcp-zoom-1.image" alt="20210607152853" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从高到低排列有</p>
<ol>
<li>行内样式</li>
</ol>
<p>给元素添加的内联样式 (例如，<code>style="font-weight:bold"</code>) 总会覆盖外部样式表的任何样式 ，因此可看作是具有最高的优先级。</p>
<ol start="2">
<li>
<p>关系选择符（combinators）</p>
<ul>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Adjacent_sibling_combinator" target="_blank" rel="nofollow noopener noreferrer"><code>+</code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Child_combinator" target="_blank" rel="nofollow noopener noreferrer"><code>></code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/General_sibling_combinator" target="_blank" rel="nofollow noopener noreferrer"><code>~</code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Descendant_combinator" target="_blank" rel="nofollow noopener noreferrer"><code> </code>(空格)</a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Column_combinator" target="_blank" rel="nofollow noopener noreferrer"><code>||</code></a>和 <strong>否定伪类</strong>（negation pseudo-class）（<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:not" target="_blank" rel="nofollow noopener noreferrer"><code>:not()</code></a>）对优先级没有影响。（但是，在<code>:not()</code> 内部声明的选择器会影响优先级）。</p>
</li>
</ul>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Universal_selectors" target="_blank" rel="nofollow noopener noreferrer">通配选择符（universal selector</a>,即<code>*</code></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/ID_selectors" target="_blank" rel="nofollow noopener noreferrer">ID 选择器</a>（例如，<code>#example</code>）。</p>
</li>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors" target="_blank" rel="nofollow noopener noreferrer">类选择器</a> (例如，<code>.example</code>)，属性选择器（例如，<code>[type="radio"]</code>）和伪类（例如，<code>:hover</code>）</p>
</li>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Type_selectors" target="_blank" rel="nofollow noopener noreferrer">类型选择器</a>（例如，<code>h1</code>）和伪元素（例如，<code>::before</code>）</p>
</li>
</ol>
<p>可以访问以下来了解更多关于优先级的详细信息。</p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#%E4%BC%98%E5%85%88%E7%BA%A7_2" target="_blank" rel="nofollow noopener noreferrer">CSS 优先级-MDN</a></li>
</ul>
<h2 data-id="heading-17">2.1 简单选择器优先级的如何计算</h2>
<p>当我们用一个非常复杂的规则去选择元素时，最终优先级可以用一个"四元组"来表示:</p>
<p><code>[inline(最高),id 个数,class 个数,tag 个数]</code></p>
<p>结果从后往前数(因为最后一位是 inline,优先级最高)</p>
<p>在 <code>CSS 标准</code>中我们需要使用一个足够大的 N 进制 来进行计算出优先级</p>
<hr>
<p>在简单选择器中， 除了 <code>#id</code>, <code>.class</code>， 其他简单选择器的优先级是一样的</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*1             2*/</span>
<span class="hljs-selector-id">#id</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-class">.a</span><span class="hljs-selector-id">#id</span> &#123;
  <span class="hljs-comment">/**/</span>
&#125;

<span class="hljs-comment">/* [0,2,1,1] */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>S = 0 _ N+ 2 _ N + 1 N+1</p>
<p>取 N = 1000000</p>
<p>S = 2000001000001</p>
<hr>
<p>请使用<code>[inline(最高),id 个数,class 个数,tag 个数]</code>的范式写出下面选择器的优先级:</p>
<ul>
<li><code>div#a.b .c[id=x]</code></li>
<li><code>#a:not(#b)</code></li>
<li><code>.a</code></li>
<li><code>div.a</code></li>
</ul>
<p>正确答案</p>
<ul>
<li>[0,1,3,1]</li>
<li>[0,2,0,0]</li>
<li>[0,0,1,0]</li>
<li>[0,0,1,1]</li>
</ul>
<h2 data-id="heading-18">解析  div#a.b .c[id=x]的优先级</h2>
<h3 data-id="heading-19">相同的规则的优先级--二者相等()</h3>
<p><strong>优先级相同，后面的规则会覆盖前面的规则</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-attr">[id=<span class="hljs-string">"x"</span>]</span> &#123;
    <span class="hljs-attribute">color</span>: red;
  &#125;

  <span class="hljs-comment">/*
优先级相同，后面的规则会覆盖前面的规则
*/</span>
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-attr">[id=<span class="hljs-string">"x"</span>]</span> &#123;
    <span class="hljs-attribute">color</span>: blue;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"c"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">id 选择器优先级 >  属性选择器优先级</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/*
    #x 与  [id=x] 相比，  #x优先级跟高
  */</span>
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-id">#x</span> &#123;
    <span class="hljs-attribute">color</span>: red;
  &#125;

  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-attr">[id=<span class="hljs-string">"x"</span>]</span> &#123;
    <span class="hljs-attribute">color</span>: blue;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"c"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">class 选择器优先级 ===  属性选择器优先级</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/*
    .d 与  [id=x] 相比，  二者优先级是一致的
  */</span>

  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-class">.d</span> &#123;
    <span class="hljs-attribute">color</span>: red;
  &#125;

  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-attr">[id=<span class="hljs-string">"x"</span>]</span> &#123;
    <span class="hljs-attribute">color</span>: blue;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"c d"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/*
    .d 与  [id=x] 相比，  二者优先级是一致的
  */</span>

  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-class">.d</span> &#123;
    <span class="hljs-attribute">color</span>: blue;
  &#125;

  <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#a</span><span class="hljs-selector-class">.b</span> <span class="hljs-selector-class">.c</span><span class="hljs-selector-attr">[id=<span class="hljs-string">"x"</span>]</span> &#123;
    <span class="hljs-attribute">color</span>: red;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"c d"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">解析  #a:not(#b)的优先级</h2>
<h3 data-id="heading-23">伪类是不参与优先级计算的</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/*
       伪类是不参与优先级计算的
       但是，在 :not() 内部声明的选择器会影响优先级

      MDN中说到(https://developer.mozilla.org/zh-CN/docs/Web/CSS/:not)
      可以利用这个伪类提高规则的优先级。例如， #foo:not(#bar) 和 #foo 会匹配相同的元素，
      但是前者的优先级更高。
    */</span>
  <span class="hljs-selector-id">#a</span><span class="hljs-selector-pseudo">:not</span>(<span class="hljs-selector-id">#b</span>) &#123;
    <span class="hljs-attribute">color</span>: green;
  &#125;

  <span class="hljs-selector-id">#a</span> &#123;
    <span class="hljs-attribute">color</span>: black;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"c d"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/*
       伪类是不参与优先级计算的

    */</span>
  <span class="hljs-selector-id">#a</span><span class="hljs-selector-pseudo">:not</span>(<span class="hljs-selector-id">#b</span>) &#123;
    <span class="hljs-attribute">color</span>: green;
  &#125;

  <span class="hljs-selector-id">#x</span> <span class="hljs-selector-id">#a</span> &#123;
    <span class="hljs-attribute">color</span>: black;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"c d"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">解析 .a 与  div.a 的优先级</h2>
<h3 data-id="heading-25"><code>*</code> 号不会影响优先级</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/*
       * 号不会影响优先级

    */</span>
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-class">.a</span> &#123;
    <span class="hljs-attribute">color</span>: brown;
  &#125;

  *<span class="hljs-selector-class">.a</span> &#123;
    <span class="hljs-attribute">color</span>: green;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"x"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"b"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"a"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a"</span>></span>666<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>复杂选择器的优先级就是把每个简单选择器的优先级加起来吗？  是的！</li>
<li>transform 不会改变别的元素， 只会改变自身元素位置，会改变重绘，</li>
<li>css 有继承吗？ 是指子元素属性与父元素属性的继承， 不是 面向对象说到的继承</li>
</ol>
<h2 data-id="heading-26">3 . 伪类</h2>
<h3 data-id="heading-27">表示链接/行为的伪类</h3>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:any-link" target="_blank" rel="nofollow noopener noreferrer"><code>:any-link</code></a></li>
</ul>
<p><code>CSS</code> 伪类 选择器代表一个有链接锚点的元素，而不管它是否被访问过，也就是说，它会匹配每一个有 <code>href</code> 属性的 <code><a></code>、<code><area></code> 或 <code><link></code> 元素。因此，它会匹配到所有的 <code>:link</code> 或 <code>:visited</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ff21777522043c5a3bab0edf4c9200a~tplv-k3u1fbpfcp-zoom-1.image" alt="any-link" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:link" target="_blank" rel="nofollow noopener noreferrer"><code>:link(未访问的超链接)</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:visited" target="_blank" rel="nofollow noopener noreferrer"><code>:visited(已访问的超链接)</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:hover" target="_blank" rel="nofollow noopener noreferrer"><code>:hover(鼠标悬停状态)</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:active" target="_blank" rel="nofollow noopener noreferrer"><code>:active(鼠标点击的状态--可以被键盘触发)</code></a></li>
</ul>
<p><code>active</code> 表示当所指元素处于激活状态（鼠标在元素上按下还没有松开）时所显示的颜色。</p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:focus" target="_blank" rel="nofollow noopener noreferrer"><code>:focus(--可以被键盘触发)</code></a></li>
</ul>
<p><code>focus</code> 表示元素获得光标焦点时使用的颜色，主要用于文本框输入文字时使用（鼠标松开时显示的颜色）。</p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Using_the_:target_selector" target="_blank" rel="nofollow noopener noreferrer"><code>:target</code></a></li>
</ul>
<p><strong>伪类的顺序</strong>应为:</p>
<ol>
<li><code>:link</code></li>
<li><code>:visited</code></li>
<li><code>:hover</code></li>
<li><code>:focus</code></li>
<li><code>:active</code></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:link</span> &#123;
  <span class="hljs-attribute">color</span>: blue;
&#125; <span class="hljs-comment">/* 未访问链接 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:visited</span> &#123;
  <span class="hljs-attribute">color</span>: purple;
&#125; <span class="hljs-comment">/* 已访问链接 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:hover</span> &#123;
  <span class="hljs-attribute">background</span>: yellow;
&#125; <span class="hljs-comment">/* 用户鼠标悬停 */</span>
<span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:active</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125; <span class="hljs-comment">/* 激活链接 */</span>

<span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:active</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#eee</span>;
&#125; <span class="hljs-comment">/* 激活段落 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">表示树形结构的伪类</h3>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:empty" target="_blank" rel="nofollow noopener noreferrer"><code>:empty</code></a></li>
</ul>
<p>代表没有子元素的元素。子元素只可以是元素节点或文本（包括空格）。注释或处理指令都不会产生影响。</p>
<ul>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-child" target="_blank" rel="nofollow noopener noreferrer"><code>:nth-child()</code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-last-child" target="_blank" rel="nofollow noopener noreferrer"><code>:nth-last-child()</code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:first-child" target="_blank" rel="nofollow noopener noreferrer"><code>:first-child</code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:last-child" target="_blank" rel="nofollow noopener noreferrer"><code>:last-child</code></a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:only-child" target="_blank" rel="nofollow noopener noreferrer"><code>:only-child</code></a></p>
</li>
</ul>
<p>在玩具浏览器中，在 startTag 的时候去做 computeCSS，</p>
<ul>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-last-child" target="_blank" rel="nofollow noopener noreferrer">:nth-last-child()</a></p>
</li>
<li>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:last-child" target="_blank" rel="nofollow noopener noreferrer">:last-child()</a></p>
</li>
</ul>
<p>至少要到 endtag 之后的下一个 token 是什么</p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:only-child" target="_blank" rel="nofollow noopener noreferrer">:only-child</a></li>
</ul>
<p>至少要到标签结束的时候，再往后扫一个 token，才能知道是不是 此伪类对应的元素</p>
<p>是无法实现的，<strong>在真实代码场景中不建议使用，</strong></p>
<h3 data-id="heading-29">CSS 回溯问题</h3>
<h4 data-id="heading-30">逻辑型</h4>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:not" target="_blank" rel="nofollow noopener noreferrer"><code>:not</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:where" target="_blank" rel="nofollow noopener noreferrer"><code>:where</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/:has" target="_blank" rel="nofollow noopener noreferrer"><code>:has</code></a></li>
</ul>
<p>not 中加复杂选择器， 可以这样使用</p>
<h2 data-id="heading-31">4.伪元素</h2>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/::before" target="_blank" rel="nofollow noopener noreferrer"><code>::before</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/::after" target="_blank" rel="nofollow noopener noreferrer"><code>::after</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/::first-line" target="_blank" rel="nofollow noopener noreferrer"><code>::firstline</code></a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/::first-letter" target="_blank" rel="nofollow noopener noreferrer"><code>::firstletter</code></a></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <::before/> content content content content content content content content
  content content content content content content content content <::after/>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> ></span>
<::first-letter/>c</::first-letter> ontent content content content
    content content content content
    content content content content
    content content content content
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
<::first-line/>content content content content </::first-line>
    content content content content
    content content content content
    content content content content
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">思考</h2>
<ul>
<li>编写一个 match 函数</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params">selector, element</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;

<span class="hljs-comment">// 第一个参数:任意选择器</span>
<span class="hljs-comment">// 第二个参数，定位html中一个已存在的元素</span>
<span class="hljs-comment">// 结果: 返回第一个参数与第二个参数是否相等</span>
match(<span class="hljs-string">"div #id.class"</span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"id"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"class"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"class"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params">selector, element</span>) </span>&#123;
    <span class="hljs-comment">// 返回与指定的选择器组匹配的文档中的元素列表 (使用深度优先的先序遍历文档的节点)。返回的对象是 NodeList 。</span>
    <span class="hljs-keyword">const</span> nodeList = <span class="hljs-built_in">document</span>.querySelectorAll(selector);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> e <span class="hljs-keyword">in</span> nodeList) &#123;
      <span class="hljs-comment">// 给定的元素与 NodeList的某一项是否匹配</span>
      <span class="hljs-keyword">return</span> nodeList[e] === element;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-keyword">const</span> mydiv = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"id"</span>);

  <span class="hljs-keyword">const</span> res = matchesSelector(<span class="hljs-string">"div #id.class"</span>, mydiv);

  <span class="hljs-built_in">console</span>.log(res);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">最后</h2>
<p>文章浅陋,欢迎各位看官评论区留下的你的见解！</p>
<p>觉得有收获的同学欢迎点赞，关注一波!</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/363190f494434fa7b82e323681717562~tplv-k3u1fbpfcp-zoom-1.image" alt="20210531095857" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-34">往期文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6968269593206849572" target="_blank">最全 ECMAScript 攻略</a></li>
<li><a href="https://juejin.cn/post/6968274790175997966" target="_blank">最全 ECMAScript 攻略之 ES2020-ES12</a></li>
<li><a href="https://juejin.cn/post/6968113844086374431" target="_blank">最全 ECMAScript 攻略之 ES2022-ES13</a></li>
</ul></div>  
</div>
            