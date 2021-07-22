
---
title: 'vertical-align的一些理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f24fae7665a47b498e66c918d445553~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:23:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f24fae7665a47b498e66c918d445553~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">例子</h1>
<p>首先看个具体的例子：</p>
<pre><code class="hljs language-html copyable" lang="html">
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.parent</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">250px</span>;
            <span class="hljs-attribute">background</span>: lightgray;
        &#125;
        <span class="hljs-selector-class">.child</span> &#123;
            <span class="hljs-attribute">display</span>: inline-block;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">background</span>: cornflowerblue;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"parent"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中定义了一个父元素，里面包含了两个 inline-block 的子元素，效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f24fae7665a47b498e66c918d445553~tplv-k3u1fbpfcp-zoom-1.image" alt="没有文字" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有没有发现，我们<strong>没有定义父元素的高度，子元素也没有设置 margin-bottom，为什么父元素底部还有段间距</strong>呢？</p>
<p>还是上面的样式和 DOM 结构，我们在其中一个子元素上添加一段文字，效果又成了下面这个样子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9356731957794ced8d983a18f4d2b258~tplv-k3u1fbpfcp-zoom-1.image" alt="添加了文字" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么<strong>添加了文字之后，两个子元素的对齐情况完全变了</strong>呢？</p>
<p>其实上面的现象都是与 CSS 的 vertical-align 属性有关系，希望你看完本文之后能了解为什么会产生上面的现象并处理这些对齐问题。</p>
<h1 data-id="heading-1">vertical-align 起作用的前提</h1>
<p>我们有时会遇到设置了 vertical-align 的属性但是没有任何效果的情况，这是因为 vertical-align 的作用对象是有限制的。MDN 上关于 vertical-align 定义如下：</p>
<blockquote>
<p>CSS 的属性 vertical-align 用来指定行内元素（inline）或表格单元格（table-cell）元素的垂直对齐方式。</p>
</blockquote>
<p>也就是说，vertical-align 作用于 inline 或 table-cell 元素（当然也作用于将 display 属性设置为 inline/inline-block/table-cell 的元素）。虽然 inline 和 table-cell 元素是很基础的 CSS 知识了，我这里还是罗列了一下：</p>
<ol>
<li>inline 元素</li>
</ol>
<ul>
<li>inline： img/span/em/b/匿名元素/...</li>
<li>inline-block: input/button</li>
</ul>
<ol start="2">
<li>table-cell 元素</li>
</ol>
<ul>
<li>table-cell: td</li>
</ul>
<p>因为 table-cell 元素的对齐比较简单，使用 table 时大多也会内嵌一层 dom，单独对模块进行排版，本文的讨论范围只限于 inline 元素。</p>
<h1 data-id="heading-2">vertical-align 的属性值</h1>
<h2 data-id="heading-3">继承类（inherit）</h2>
<p>我们对 inherit 再熟悉不过了，vertical-align 是支持继承的，子元素可以从父元素继承 vertical-align 属性的值。</p>
<h2 data-id="heading-4">文本类（text-top/text-bottom）</h2>
<p>文本类的属性值定义如下：</p>
<ul>
<li>text-top: 使元素的顶部与父元素的字体顶部对齐</li>
<li>text-bottom: 使元素的底部与父元素的字体底部对齐</li>
</ul>
<p>从定义看出，这类属性值与父元素的字体有关。我们定义父元素的字体大小为24px，3个包含了文字的子元素的字体大小分别为12px、24px和48px，对齐效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ebc085019394f00b13c736b6f86809a~tplv-k3u1fbpfcp-zoom-1.image" alt="text-top" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了更清楚看到对齐的边界，在设置了 vertical-align: text-top 的元素的上边缘和字体的背景进行了标注，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/607f8eda08a748ada4cb3c234d3fc1f2~tplv-k3u1fbpfcp-zoom-1.image" alt="text-top标注" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图可以看出，左侧 div 确实是与 24px 的文字的顶部对齐的。</p>
<p>再复杂一点，我们增加一个 inline-block 的 div 作为子元素，效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fb871a7098484d866bb3b24fc5053a~tplv-k3u1fbpfcp-zoom-1.image" alt="text-top-div" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的例子我们可以知道，text-top/text-bottom 只与父级字体大小有关系，与左右元素是没有关系的。如果我们要确定两个元素的对齐关系，不管中间是否插入元素，可以考虑使用这种对齐方式。</p>
<h2 data-id="heading-5">线类（baseline/top/middle/bottom）</h2>
<p>vertical-align 中我们用的最多，遇到问题也最多的应该就是线类属性了。线类属性值的定义如下：</p>
<ul>
<li>baseline（默认值）: 使元素的基线与父元素的基线对齐</li>
<li>middle: 使元素的中部与父元素的基线加上父元素x-height（译注：x高度）的一半对齐</li>
<li>top: 使元素及其后代元素的顶部与整行的顶部对齐</li>
<li>bottom: 使元素及其后代元素的底部与整行的底部对齐</li>
</ul>
<h3 data-id="heading-6">top 和 bottom</h3>
<ul>
<li>top: 使元素及其后代元素的顶部与整行的顶部对齐</li>
<li>bottom: 使元素及其后代元素的底部与整行的底部对齐</li>
</ul>
<p>我们先来看下相对简单的 top 和 bottom，这里以 top 为例，定义中包含了两个概念，一个是元素的顶部，一个是整行的顶部。</p>
<blockquote>
<p>Align the top of the aligned subtree with the top of the line box.</p>
</blockquote>
<ul>
<li>元素的顶部：元素盒模型的顶部，包含margin</li>
<li>整行的顶部：行框盒子的顶部。如果对行框盒子不了解，请看这里：[css行高line-height的一些理解](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyolkpie.net%2F2020%2F09%2F29%2Fcss%25E8%25A1%258C%25E9%25AB%2598line-height%25E7%259A%2584%25E4%25B8%2580%25E4%25BA%259B%25E7%2590%2586%25E8%25A7%25A3%2F%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://yolkpie.net/2020/09/29/css%E8%A1%8C%E9%AB%98line-height%E7%9A%84%E4%B8%80%E4%BA%9B%E7%90%86%E8%A7%A3/%EF%BC%89" ref="nofollow noopener noreferrer">yolkpie.net/2020/09/29/…</a></li>
</ul>
<p>下面的例子中，div 为 inline-block，右侧的字体设置了 margin-top: 20px。内联盒子和幽灵节点的标注为黄色，行框盒子的标注为绿色，可以看到，盒子的顶部是对齐的。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22f5273ffaa940609070d5ca10df1b0c~tplv-k3u1fbpfcp-zoom-1.image" alt="top的box拆分" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果把中间的文字设置margin-bottom: 100px，其他子元素的对齐方式由 top 变为 bottom，效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71886ee309654662a67ee671ec512d6f~tplv-k3u1fbpfcp-zoom-1.image" alt="bottom" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面的例子我们可以看到，使用 top 和 bottom 属性值时，对齐的是行框盒子的顶部或底部。遇到问题时，把行框盒子拆分下就比较容易理解了。</p>
<h3 data-id="heading-7">baseline</h3>
<ul>
<li>baseline（默认值）: 使元素的基线与父元素的基线对齐</li>
</ul>
<p>baseline 是无处不在的，因为 vertical-align 的默认值就是 baseline。从 baseline 的定义来看，我们需要弄清楚元素的基线是什么（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FCSS2%2Fvisudet.html%23leading" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/CSS2/visudet.html#leading" ref="nofollow noopener noreferrer">baseline定义</a>）：</p>
<blockquote>
<p>The baseline of an 'inline-block' is the baseline of its last line box in the normal flow, unless it has either no in-flow line boxes or if its 'overflow' property has a computed value other than 'visible', in which case the baseline is the bottom margin edge.</p>
</blockquote>
<p>inline-block 的基线是正常流中（非float/absolute/fixed/html根节点）最后一个内联盒子的基线，除非这个元素里既没有内联盒子或者本身的 overflow 的计算值不是 visile，这种情况下 baseline 是元素的 margin 底边缘。也就是说，如果 inline-block 中没有元素或者 overflow 属性不是 visible，这个元素的基线是 margin 底边缘，其他的情况都是最后一个内联盒子的基线。</p>
<p>我们知道，文字的基线是 x 字母的下边缘。我们可以通过这个原理来模拟父元素的基线，可以通过在父元素上添加一个 after 伪元素选择器，内容为字母 x，那么父元素的基线就是字母 x 的下边缘线。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.line-box</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">'x'</span>;
    <span class="hljs-attribute">background</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们来看下开头的第一个问题：为什么父元素底部还有段间距？</p>
<p>首先，我们先来确定每个子元素的基线：按照 baseline 的定义，因为两个 inline-block 的 div 中没有元素，所以这两个 div 的基线为div的下边缘。另外，每个行框盒子的最前面都有一个幽灵节点，继承了父级的行高和字体，我们可以用一个 x 来模拟这个幽灵节点，所以幽灵节点的基线就是字母 x 的下边缘。子元素的基线确定好了之后，我们来看下父元素的基线，父元素的基线是最后一个元素，也就是第二个 div 的基线，即第二个div的下边缘。让子元素的基线和父元素的基线挨个对齐（如下图），因为幽灵节点（最左侧 x）占有高度，所以父元素底部还是有段间距的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ca884ee8e924340ba08b260f5a51aeb~tplv-k3u1fbpfcp-zoom-1.image" alt="baseline" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个底部间距的问题我们也会经常遇到，最常见的就是图片（对应例子中的 inline-block 的 div 元素）的底部会有间距。要去掉这个间距，有下面几种方式：</p>
<ol>
<li>设置 line-height 为 0</li>
</ol>
<p>既然产生间距的原因是幽灵空白节点产生了高度，我们设置 line-height 为 0 就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df5ad70198844b7686fa8ddb49cb4152~tplv-k3u1fbpfcp-zoom-1.image" alt="设置 line-height 为 0" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>设置 font-size 为 0</li>
</ol>
<p>设置 font-size 为 0 的原理和设置 line-height 为 0 是一样的，都是要消灭幽灵空白节点的高度：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8c88eef7e3943f9acee7a11849c4794~tplv-k3u1fbpfcp-zoom-1.image" alt="设置 font-size 为 0" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>设置图片为 block 元素，可以消灭空白节点</li>
</ol>
<p>无话可说，但是这种情况下图片只能一行一个。</p>
<ol start="4">
<li>设置 vertical-align 为 top/bottom/middle</li>
</ol>
<p>使用这种方式的目的是使幽灵节点上移，这样底部的边距就不见了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7616ac92735049e28eab7df0664d5b69~tplv-k3u1fbpfcp-zoom-1.image" alt="设置 vertical-align 为 bottom" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再来看第二个问题：为什么加了字母之后对齐方式变了？</p>
<p>还是先来分析下每个子元素的基线（幽灵空白节点依然用字母 x代替），第一个 div 的基线是底边缘，第二个 div 里因为有文字，这个 div 的基线是文字的基线。父元素的基线是第二个 div 的基线，即第二个 div 中 x 的底边缘。挨个对齐后，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d686bcc842174db99441bbd210520df2~tplv-k3u1fbpfcp-zoom-1.image" alt="baseline+文字" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">middle</h3>
<ul>
<li>middle: 使元素的中部与父元素的基线加上父元素x-height（译注：x高度）的一半对齐</li>
</ul>
<p>直观一点，就是使元素的中部和我们在父元素上添加的 x 字母的中心对齐。通常我们使用 vertical-align 来实现垂直居中的效果。</p>
<p>我们设置子元素（可以是图片，也可以是任意长度的文字）为 inline-block, vertical-align 为middle，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd6ca8042552420c82d7b9626c4c4320~tplv-k3u1fbpfcp-zoom-1.image" alt="middle 近似垂直居中" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中，黄色虚线为父元素的中线，红色为各个子元素的中线，可以看到，父元素和子元素的中线是重合的。但是，上面的居中只是“近似”垂直居中，为什么呢，上面的例子中，父元素的基线应该是幽灵空白节点的基线，我们知道，因为视觉上的需要，字体的基线普遍是偏下的，所以字母 x 的中心也是在中点偏下的位置。我们把父元素的字体增大，就会看到这种差异了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d263bd6ef614cc6b3f89a79ea1a9ec9~tplv-k3u1fbpfcp-zoom-1.image" alt="middle 近似垂直居中细节" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那如何实现“真正”的垂直居中呢？我们首先想到的是把父元素的 font-size 或者 line-height 设置为 0，但是这种方法有局限性，比如后面要加一段文本，如果 font-size 为 0 的话文本就会被隐藏掉，line-height 为 0 的话就会失去高度。这时我们可以给父元素的最后添加一个空白的内联元素，效果如下：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"display:inline-block;height: 100%;vertical-align: middle;"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/987ae06516174a9f94be573ebf167522~tplv-k3u1fbpfcp-zoom-1.image" alt="middle 垂直居中" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">数值类百分比类（20px/2rem/20%...）</h2>
<p>数值类百分比类的定义如下：</p>
<ul>
<li>length: 使元素的基线对齐到父元素的基线之上的给定长度。可以是负数</li>
<li>percentage: 使元素的基线对齐到父元素的基线之上的给定百分比，该百分比是line-height属性的百分比。可以是负数。</li>
</ul>
<p>理解了 baseline 之后，这部分已经很简单了，就是在 baseline 的基础上加上偏移。有时候我们要把文字或图片上下调几个像素的时候会使用 relative + top 来处理，这种情况下可以考虑用 vertical-align 来代替。</p>
<h2 data-id="heading-10">上标下标类（sub/super）</h2>
<p>上标下标类的属性值定义如下：</p>
<ul>
<li>sub: 使元素的基线与父元素的下标基线对齐</li>
<li>super: 使元素的基线与父元素的上标基线对齐</li>
</ul>
<p>这种对齐方式在实际中并没有用到。不过联想到 html 中 的 sup 和 sub 标签实现的是相同的功能，我们来比较下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef84475fcd474e4caed99d1423cbf540~tplv-k3u1fbpfcp-zoom-1.image" alt="sup标签" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图上可以看出，使用 sup 标签和设置 vertical-align 为 super，这两种对齐效果是一样的，不同的是 sup 标签里的文字要比正常的小一些（原字体的75%）。通常上标和下标都会要求字体要比正文小一些，因此我认为使用标签要比设置vertical-align更合适。</p>
<h1 data-id="heading-11">总结</h1>
<p>CSS 的知识点很碎，而且因为兼容性的问题表现出来的总是莫名奇妙，但还是建议大家从 CSS 的各种概念入手，遇到不清楚的情况回到盒模型、行高、字体这些最基础的含义上，才能一步步梳理清楚。</p></div>  
</div>
            