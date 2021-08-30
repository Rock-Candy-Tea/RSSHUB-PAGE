
---
title: 'CSS-流的破坏和保护'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/321c768070594e938c1d4d25e199a9ae~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 00:57:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/321c768070594e938c1d4d25e199a9ae~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在日常开发中，经常会遇到float浮动导致的父级塌陷问题，为此，我们可以通过clearfix来解决，但内部到底发生了什么？
本文将带你理解其中的原理，主要分为4个部分：</p>
<ul>
<li>流式布局</li>
<li>流的破坏-float浮动</li>
<li>流的保护-clear清除浮动</li>
<li>流的保护-BFC结界</li>
</ul>
<h2 data-id="heading-1">流式布局</h2>
<p>我们知道，HTML默认按照 <code>流</code> 在页面上进行排列布局，<code>流式布局</code>是指利用元素 <code>流</code> 的特性实现各种布局。
简单说，流式布局从上到下，从左到右，块状元素独占一行，内联元素非独占，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/321c768070594e938c1d4d25e199a9ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是块状元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我是内联元素<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我是内联元素1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我是内联元素2<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>流式布局可以满足早期像W3C那样的简单页面布局，但像文字环绕图片这样的需求却力不从心。
这时，float应运而生了。</p>
<h2 data-id="heading-2">流的破坏-float浮动</h2>
<p>最初，float的初衷是用来实现文字环绕图片，类似下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec936f01396b44e183f61a0004b274cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://www.imooc.com/static/img/index/logo.png"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-right: 10px;"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">""</span>></span>某一段文字……某一段文字……某一段文字……某一段文字……某一段文字……某一段文字……某一段文字……某一段文字……<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>float实现文字环绕的原理是：</p>
<ol>
<li>首先，图片脱离文档流，覆盖在父级元素上（父级元素和图片是重叠的）。这也导致父级元素在计算高度时排除了图片，可能出现父级元素高度小于图片高度的情况，造成<strong>父级塌陷</strong>的感觉；</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a86e4a869e0f4c6ba652ae94c4d1bc20~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>其次，每行文字和图片都要保证不重叠。</li>
</ol>
<p>上面提到，添加float属性的元素会有父级塌陷的问题，影响后面的元素，比如：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8173f634a1ab40528bb652680d320c2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://www.imooc.com/static/img/index/logo.png"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-right: 10px;"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">""</span>></span>某一段文字……某一段文字……<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!-- 父级塌陷导致下面的元素也受到影响 --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width:300px;"</span>></span>另一段文字...另一段文字...另一段文字...另一段文字...另一段文字...另一段文字......<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，上面的元素影响到底部的文字的显示。</p>
<p>由于float被用来做布局，其父级塌陷的特性导致了许多不便，因此clear属性应运而生，用来解决这个问题。</p>
<h2 data-id="heading-3">流的保护-clear清除浮动</h2>
<blockquote>
<p><code>clear</code> 属性的原理是：让自身不能和前面的(clear:left)或后面的(clear:right)浮动元素相邻（改变自身，而不是改变浮动元素）</p>
</blockquote>
<ul>
<li>clear:none</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7071538344b949f3b3400025b17c201e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>clear:left</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb1d40dab2c2487396f7e07274c82b95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>clear:right/clear:both</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23f2523a185a4c768bfbc936cfefeacf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体可参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Fclear" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/clear" ref="nofollow noopener noreferrer">mdn clear</a></p>
<h3 data-id="heading-4">clearfix</h3>
<blockquote>
<p>如果一个元素里只有浮动元素，那它的高度会是0。如果你想要它自适应即包含所有浮动元素，那你需要清除它的子元素。一种方法叫做 <code>clearfix</code> ，即clear一个不浮动的 ::after 伪元素。</p>
</blockquote>
<p><code>clear</code> 属性只有块级元素才有效，而::after等伪元素默认都是内联水平，这就是借助伪元素清除浮动时需要设置display属性的原因：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#container</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
  <span class="hljs-attribute">display</span>: block;
  <span class="hljs-attribute">clear</span>: both;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但 <code>clear</code> 属性消除浮动不是一个完美的解决方案，比如：</p>
<ol>
<li>如果clear:both元素前面的元素就是float元素，则 <code>margin-top</code> 负值即使设成-9999px，也无效</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbd28321f756488488c1adc5ce584956~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"float:left;"</span>></span>我是谁<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"clear:both;margin-top:-9999px"</span>></span>我在哪<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>clear:both 后面的元素依旧可能会发生文字环绕的现象（<code>margin-top:-xxpx</code>）:</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d795752a90fc415792adbad8d9eba3eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container clearfix"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://www.imooc.com/static/img/index/logo.png"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-right: 10px;"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">""</span>></span>某一段文字……某一段文字……某一段文字……某一段文字……<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width:300px;margin-top:-30px;"</span>></span>另一段文字...另一段文字...另一段文字...另一段文字...另一段文字...另一段文字...<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那有没有更好的办法来解决float布局造成的父级塌陷问题呢？
答案是 <code>BFC</code></p>
<h2 data-id="heading-5">流的保护-BFC结界</h2>
<p><code>BFC</code> 全称是 <code>Block Format Context</code>，中文是块级格式化上下文。BFC的特性可以简单理解为结界：通过一些特定的手段形成的封闭空间，里面的人出不去，外面的人进不来，具有极强的防御性。BFC的特性表现如出一辙。</p>
<h3 data-id="heading-6">BFC的触发条件</h3>
<ul>
<li><code><html></code>根元素</li>
<li>float 值不为none</li>
<li>overflow 值为auto/scroll/hidden</li>
<li>display 值为table-cell/table-caption/inline-block</li>
<li>position 值不为 static/relative</li>
</ul>
<h3 data-id="heading-7">BFC与流体布局</h3>
<blockquote>
<p>BFC的结界特性最重要的用途其实不是去margin重叠，或者是清除float影响，而是实现更健壮、更智能的自适应布局。</p>
</blockquote>
<p>既然BFC这么优秀，为什么它没有完全替代流体布局呢？</p>
<h3 data-id="heading-8">BFC的缺点</h3>
<p>触发BFC的属性都自带副作用,最后筛选出两个常用的：</p>
<ul>
<li>overflow:hidden;</li>
<li>display:table-cell;</li>
</ul>
<p>两种方案均有一点不足，前者如果子元素要定位到父元素外面可能会被隐藏，后者无法直接让连续英文字符换行。所以，大家可以根据实际的项目场景选择合适的技术方案。</p>
<h2 data-id="heading-9">总结</h2>
<p>本文主要讲解了float浮动的实现原理和父级塌陷的解决方案，希望能对你有所帮助。
文中的代码可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FRealAaron%2Fpen%2FLYLpXqj%3Feditors%3D1100" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/RealAaron/pen/LYLpXqj?editors=1100" ref="nofollow noopener noreferrer">codepen</a> 中查看。</p>
<p>谢谢您的阅读，欢迎点赞和评论交流~</p>
<h2 data-id="heading-10">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F27615777" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/27615777" ref="nofollow noopener noreferrer">《CSS世界》</a></li>
</ul></div>  
</div>
            