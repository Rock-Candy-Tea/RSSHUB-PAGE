
---
title: '【译】理解CSS关键字：_Initial_，_Inherit_和_Unset_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0589315cdbd042089e392ca1a2030283~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 17:58:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0589315cdbd042089e392ca1a2030283~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>译文已同步收录在 <a href="https://github.com/ddzy/translations" target="_blank" rel="nofollow noopener noreferrer">Github</a></p>
<h2 data-id="heading-0">概述</h2>
<p>CSS 中有各种各样的关键字。本文我将着重介绍以下几个关键字：<code>initial</code>、<code>inherit</code> 以及较新的 <code>unset</code>。</p>
<p>我确信绝大多数开发者都见过这几个关键字，但是对于它们的原理确知之甚少。</p>
<p><img alt="1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0589315cdbd042089e392ca1a2030283~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在此之前的一段时间，我只知道这些关键字是用来重置 CSS 样式的，但是如果它们都起到了重置的效果，又为什么会有这么多种呢？它们之间的区别又是什么？<strong>于是，我决定深入探索它们的原理</strong>。</p>
<h2 data-id="heading-1">浏览器的基础样式</h2>
<p>在开始讲解这些 CSS 关键字之前，我们首先要了解浏览器的基础样式是从哪儿来的。</p>
<h3 data-id="heading-2">CSS 属性的初始值</h3>
<p>每个 CSS 属性都有一个初始值，这个值和 HTML 元素没有任何关系。</p>
<p>如下图所示的是从 MDN 上摘取的关于 <code>initial</code> 的例子：</p>
<p><img alt="2.jpeg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46b04cb45f5541d78d617f2b4031374b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">浏览器默认（User-Agent）样式表</h3>
<p>在所有的 CSS 属性都设置完初始样式之后，紧接着浏览器会加载自身的样式表。该样式表与 CSS 属性的初始值没有任何关系。</p>
<p><strong>user-agent 样式示例如下：</strong></p>
<p><img alt="3.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed7de5091fb4396a8694c76085565a7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>HTML 元素是没有初始的样式值的！上图中 <code><h1></code> 标签的基础样式是从 user agent stylesheet 中获取的，而不是 CSS 属性的初始值 <code>initial</code>。</p>
<p><strong>下面，让我们开始讲解这些 CSS 关键字吧！</strong></p>
<h2 data-id="heading-4">Inherit 关键字</h2>
<p><code>inherit</code> 关键字告诉浏览器去寻找离当前 HTML 元素最近的父级元素，然后继承该父级元素对应的 CSS 属性值。如果父级元素的 CSS 属性值也是 <code>inherit</code> 的话，会继续一层层的向上查找，直到最后一个 DOM 元素，如果还是没有找到对应的 CSS 属性值的话，就会使用浏览器默认样式表（user-agent-stylesheet）中的属性值，如果没有 user-agent 样式表，最后会使用初始值 <code>initial</code>。</p>
<p class="codepen">
  <span>See the Pen <a href="https://codepen.io/elad2412/pen/hdypx" target="_blank" rel="nofollow noopener noreferrer">
  inherit css style</a> by Elad Shechter (<a href="https://codepen.io/elad2412" target="_blank" rel="nofollow noopener noreferrer">@elad2412</a>)
  on <a href="https://codepen.io/" target="_blank" rel="nofollow noopener noreferrer">CodePen</a>.</span>
</p>

<h2 data-id="heading-5">Initial 关键字</h2>
<p>在学习 <code>initial</code> 关键字之前，我们首先要搞清楚：每个 CSS 属性都有一个初始值，该初始值和 user-agent 样式没有任何关系。 User-agent 是浏览器针对 HTML 元素所定义的基本样式表。我们倾向于把 user-agent 样式表理解为是 HTML 自带的，但实际上不是的。</p>
<p><code>initial</code> 关键字告诉浏览器去使用 CSS 属性的初始值，<strong>举个例子：</strong></p>
<ul>
<li><code>color</code> 属性的 <code>initial</code> 值总是 <code>black</code></li>
</ul>
<p>上述行为可能会产生一个困惑：CSS 属性的初始值并不一定和浏览器默认样式表中相应的属性值相同。比如：所有 HTML 元素的 <code>display</code> 属性的 <code>initial</code> 值都为 <code>inline</code>，因此如果把 <code><div></code> 元素的 <code>display</code> 属性值设为 <code>initial</code>，那么实际上此时的 <code>initial</code> 就是 <code>inline</code> 而不是 user-agent 中的属性值 <code>block</code>。</p>
<p>举个例子：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span><span class="hljs-selector-class">.box</span>&#123;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">display</span>: initial; <span class="hljs-comment">/* initial 的值为 `inline` 而不是 `block` */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://codepen.io/elad2412/pen/KKKqMyZ" target="_blank" rel="nofollow noopener noreferrer">CodePen 在线示例：div 元素的 display 属性的 Initial 值</a></p>
<p><img alt="4.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f37ba64eca1a425cb196f9230bdf5eeb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">Unset 关键字</h2>
<p><code>unset</code> 关键字比较特别，它会根据不同类型的 CSS 属性来进行重置。<strong>CSS 属性有两种类型：</strong></p>
<ul>
<li><strong>可继承的属性</strong> —— 当前 HTML 元素的 CSS 属性会影响它的后代元素。<strong>所有文本类型的 CSS 属性都有这个继承行为</strong>。比如：如果你给某个 HTML 元素设置了 <code>font-size</code> 属性，那么该元素的所有后代元素都会继承这个 <code>font-size</code>，除非你给某个后代元素又重新设置了 <code>font-size</code>。
<img alt="5.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e568d2318a94feb987fd6177d071f82~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li><strong>不可继承的属性</strong> —— 当前 HTML 元素的 CSS 属性只对自身有效。<strong>除了文本类型之外的其它 CSS 属性都是不可继承的</strong>。比如：给某个 HTML 元素设置一个 <code>border</code> CSS 属性，该元素的后代元素不会同步的获得这个属性。
<img alt="6.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda97e8f8c89412f9615be3186b7de41~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<p>对于可继承的属性，<code>unset</code> 的效果和 <code>inherit</code> 一样。例如：对于文本类型的 CSS 属性 <code>color</code>，<code>unset</code> 会一层层的向上查找，直到最后一个 HTML 元素，如果没有 <code>color</code> 属性值，那么就会查找 user-agent 样式表，如果还是没有，最后就直接使用 <code>initial</code> 初始值了。</p>
<p>对于不可继承的属性，<code>unset</code> 的效果和 <code>initial</code> 一样，直接使用该 CSS 属性的初始值。例如：<code>border-color: unset</code> 就等同于 <code>border-color: initial</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.some-class</span>&#123;
  <span class="hljs-attribute">color</span>: unset; <span class="hljs-comment">/* = inherit */</span>
  <span class="hljs-attribute">display</span>: unset; <span class="hljs-comment">/* = initial = inline */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">为什么要使用 Unset？</h3>
<p>既然已经有了 <code>initial</code> 和 <code>inherit</code> 关键字，为啥还要用 <code>unset</code> 呢？</p>
<p>如果只是重置单个 CSS 属性的值，那么就没必要使用 <code>unset</code>，使用 <code>initial</code> 和 <code>inherit</code> 就可以了。</p>
<p>但是由于全新的 CSS 属性 <code>all</code> 的出现，让我们可以一次性重置所有属性的值，包括<strong>可继承属性</strong>和<strong>不可继承属性</strong>！</p>
<p>把 <code>all</code> 的值设为 <code>unset</code>，就可以实现：所有的可继承属性的值变为 <code>inherit</code>，所有的不可继承属性的值变为 <code>initial</code>。</p>
<p><strong>这是 <code>unset</code> 这个关键字存在的唯一原因！除此之外，你完全可以用 <code>inherit</code> 和 <code>initial</code> 关键字替代 <code>unset</code></strong>。</p>
<p>如果我们一个个的书写重置属性，<strong>代码会像下面这样：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* Bad */</span>
<span class="hljs-selector-class">.common-content</span> * &#123;
  <span class="hljs-attribute">font-size</span>: inherit;
  <span class="hljs-attribute">font-weight</span>: inherit;
  <span class="hljs-attribute">border-width</span>: initial;
  <span class="hljs-attribute">background-color</span>: initial;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们使用 <code>all</code> 属性搭配 <code>unset</code> 属性值，会影响当前所有的 CSS 属性，<strong>代码如下：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* Good */</span>
<span class="hljs-selector-class">.common-content</span> * &#123;
  all: unset;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我为此专门写了一个例子，详情可见：<a href="https://codepen.io/elad2412/pen/QWWgKbB" target="_blank" rel="nofollow noopener noreferrer"><code>all: unset</code> 在线示例</a>。</p>
<h2 data-id="heading-8">Revert 关键字</h2>
<p>如果我们想把某个 CSS 属性的值重置为 user-agent 样式表中对应的样式值而不是该属性的初始值，我们应该怎么做呢？举个例子：怎么把 <code><div></code> 元素的值重置为 <code>block</code>（user-agent 样式），而不是 <code>inline</code>（初始值）？</p>
<p><img alt="7.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1bb2462201443cbb37db518d42809aa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为了解决这个问题，又出现了新的 CSS 关键字：<code>revert</code>。<code>revert</code> 和 <code>unset</code> 非常像，唯一的区别在于 <code>revert</code> 会把 CSS 属性值重置为 user-agent 中对应的值，<strong>举个例子：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">display</span>: revert; <span class="hljs-comment">/* = block */</span>
&#125;
<span class="hljs-selector-tag">h1</span> &#123;
  <span class="hljs-attribute">font-weight</span>: revert; <span class="hljs-comment">/* = bold */</span>
  <span class="hljs-attribute">font-size</span>: revert; <span class="hljs-comment">/* = 2em */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以一次性重置当前 HTML 元素的所有 CSS 属性：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* Good */</span>
<span class="hljs-selector-class">.common-content</span> * &#123;
  all: revert;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>revert</code> 相较于 <code>unset</code> 更加实用，但是浏览器兼容性不太好，目前只能在 Firefox 和 Safari 上正常工作。</p>
<h2 data-id="heading-9">浏览器兼容性</h2>
<ul>
<li><code>inherit</code> —— 包括 IE11 在内的所有浏览器都支持</li>
<li><code>initial</code> & <code>unset</code> —— 除了 IE11 之外的所有浏览器都支持</li>
<li><code>revert</code> —— 目前只支持 Firefox & Safari</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            