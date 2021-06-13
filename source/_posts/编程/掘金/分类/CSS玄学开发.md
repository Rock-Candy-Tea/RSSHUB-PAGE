
---
title: 'CSS玄学开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a21be10f7ad4632893caaf6e325b07c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 05:28:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a21be10f7ad4632893caaf6e325b07c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>css很简单，完全不懂的人大概看个一两天，就可以实现基本的页面效果；但是css也复杂，有些异常的效果，很多有经验的开发者也搞不明白该怎么解释。只能骂一句“又出bug了”。对于css来说，名字就是层叠样式表，关键是这个层叠，多个属性造就一个效果，一个异常也可能有多个属性引起的。还有些规范为定义的实现，这些学起来真的就是活脱脱的玄学开发。让我们从一些现象看起，通过现象看本质，希望玄学水平早日达到天人合一的境界。</p>

<h2 data-id="heading-0">背景区域非矩形</h2>
<p>问题出现在张大神的《css世界》4.2.2章节，大神的解释没看懂。</p>
<h3 data-id="heading-1">效果</h3>
<p>代码及效果图如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"son"</span>></span>我国我国我国我国我国我国我国我国我国我国我国<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式如下，因为内联元素的padding只影响视觉层不会影响布局层，所以最好在测试的元素上加点对上边界的margin，否则会看不到padding-top的内容。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> dashed <span class="hljs-number">#cd0000</span>;
&#125;
<span class="hljs-selector-class">.son</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">background-color</span>: gray;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a21be10f7ad4632893caaf6e325b07c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">疑问点</h3>
<p>疑问如下：</p>
<ul>
<li>第一行、第二行看起来有些字被覆盖了</li>
<li>第二行怎么没铺满就换行了</li>
<li>最后一行怎么就一个字</li>
<li>英文怎么不换行</li>
</ul>
<h3 data-id="heading-3">解释</h3>
<p>其实如下图所示，有些消失的字时被背景覆盖了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d44a0cb75b944a98791d13e61aef044~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于white-space ：normal，文本自动处理换行.假如抵达容器边界内容会转到下一行，</p>
<p>因为有padding，当padding达到边界时，会带着最后一个字（铺满倒数第二行后，多余的字）换行</p>
<p>然后倒数第二行已经不是边界了，所以没有padding-left和right了，所以假如有多余的字，这一行就肯定铺满</p>
<p>最后因为汉字（东亚文字）最小宽度为每个汉字的宽度，可以在任何需要的时候换行，而西方文字最小宽度由特定的连续的英文字符单元决定。所以全部是是字母，就不会换行，因为找不到能换行的点，中间补上空格（普通空格）、短横线、问号以及其他非英文字符等就看到换行了。</p>
<h2 data-id="heading-4">父子margin合并的玄学问题</h2>
<p>这个有个很神奇的现象，在实际开发的时候，给我们带来麻烦的多半就是这里的父子 margin 合并。</p>
<h3 data-id="heading-5">效果</h3>
<p>我们给值元素设置一个margin-top的值，结果发现父元素的北京掉下来了。
代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是标题<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.container</span> &#123;
    <span class="hljs-attribute">max-width</span>: <span class="hljs-number">356px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">289px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">../assets/3.jpg</span>) no-repeat;
&#125;
<span class="hljs-selector-class">.container</span> > <span class="hljs-selector-tag">h2</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">38px</span>;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/104ffa795b9043eb88e54f6a758e19e9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">问题解释</h3>
<p>问题产生的原因就是这里的父子 margin 合并。这里大家需要理清楚“合并”这个概念。如果我们按照中文释义理解，应该必须有多个对象才能进行合并，否则根本就没有“合”这一说，确实如此。但是，这样理解也有可能会带来这样一个误区，即你要出点儿力，我要出点儿力，才叫“合”，其实不然。放到我们这里，这个父子 margin 合并的案例上就是：父元素没有出一点力，子元素出了全部的力，然后最终的 margin 全部合到了父元素上。也就是虽然是在子元素上设置的 margin-top，但实际上就等同于在父元素上设置了 margin-top，我想这样大家就能理解为何头图会掉下来了吧。</p>
<p>但是有一点需要注意，“等同于”并不是“就是”的意思，我们使用 getComputedStyle 方法获取父元素的 margin-top 值还是 CSS 属性中设置值，并非 margin 合并的表现值。</p>
<h3 data-id="heading-7">如何解决问题</h3>
<p>那该如何阻止这里 margin 合并的发生呢？对于 margin-top 合并，可以进行如下操作（满足一个条件即可）：</p>
<ul>
<li>父元素设置为块状格式化上下文元素；</li>
<li>父元素设置 border-top 值；</li>
<li>父元素设置 padding-top 值；</li>
<li>父元素和第一个子元素之间添加内联元素进行分隔。</li>
</ul>
<p>对于 margin-bottom 合并，可以进行如下操作（满足一个条件即可）：</p>
<ul>
<li>父元素设置为块状格式化上下文元素；</li>
<li>父元素设置 border-bottom 值；</li>
<li>父元素设置 padding-bottom 值；</li>
<li>父元素和最后一个子元素之间添加内联元素进行分隔；</li>
<li>父元素设置 height、 min-height 或 max-height。</li>
</ul>
<p>所以，上面因为 margin 合并导致头图掉下来的问题可以添加下面的 CSS 代码进行
修复：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span> &#123;
<span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其原理就是通过设置 overflow 属性让父级元素块状格式化上下文。</p>
<h3 data-id="heading-8">扩展</h3>
<p>jQuery 中有个<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mo stretchy="false">)</mo><mi mathvariant="normal">.</mi><mi>s</mi><mi>l</mi><mi>i</mi><mi>d</mi><mi>e</mi><mi>U</mi><mi>p</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">().slideUp()/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mclose">)</span><span class="mord">.</span><span class="mord mathnormal">s</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">d</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10903em;">U</span><span class="mord mathnormal">p</span><span class="mopen">(</span><span class="mclose">)</span><span class="mord">/</span></span></span></span></span>().slideDown()方法，如果在使用这个动画效果的时候，发现这内容在动画开始或结束的时候会跳一下，那八九不离十就是布局存在 margin 合并。 跳动之所以产生，就是因为 jQuery 的 slideUp 和 slideDown方法在执行的时候会被对象元素添加 overflow:hidden 设置，而 overflow: hidden 会阻止 margin 合并，于是一瞬间间距变大，产生了跳动。</p>
<h2 data-id="heading-9">单行文本的高度</h2>
<h3 data-id="heading-10">现象</h3>
<p>很多人都有这样一个错误的认知，认为对于单行文本，只要行高设置多少，其占据高度就是多少。比方说，对于下面非常简单的 CSS 和 HTML 代码：</p>
<pre><code class="copyable">.box &#123; line-height: 32px; &#125;
.box > span &#123; font-size: 24px; &#125;
<div class="box">
<span>文字</span>
</div>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>.box 元素的高度是多少？
很多人一定认为是 32px：因为没有设置 height 等属性，高度就由 line-height 决定，与 font-size 无关，所以这里明摆着最终高度就是 32px。</p>
<p><strong>但是事实上，高度并不是 32px，而是要大那么几像素（受不同字体影响，增加高度也不一样）， 比方说 36px如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baf53363fcdb499589449c34465e5815~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">分析</h3>
<p>这里，之所以最终.box 元素的高度并不等于 line-height，就是因为行高的朋友属性 vertical-align 在背后默默地下了黑手。</p>
<p>其中有一个很关键的点，那就是 24px 的 font-size 大小是设置在<code><span></code>元素上的，这就导致了外部<code><div></code>元素的字体大小和<code><span></code>元素有较大出入。看不见的东西不利于理解，因此我们不妨使用一个看得见的字符 x占位，同时“文字”后面也添加一个 x，便于看出基线位置，于是就有如下 HTML：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
x<span class="hljs-tag"><<span class="hljs-name">span</span>></span>文字 x<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，我们可以明显看到两处大小完全不同的文字。一处是字母 x 构成了一个“匿名内联盒子”，另一处是“文字 x”所在的<code><span></code>元素，构成了一个“内联盒子”。由于都受 lineheight:32px影响，因此，这两个“内联盒子”的高度都是 32px。</p>
<p>对字符而言， font-size 越大字符的基线位置越往下，因为文字默认全部都是基线对齐，所以当字号大小不一样的两个文字在一起的时候，彼此就会发生上下位移，如果位移距离足够大，就会超过行高的限制，而导致出现意料之外的高度,如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc70675d0fcc4371a960277e92a2ecba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">解决</h3>
<p>知道了问题发生的原因，那问题就很好解决了。我们可以让“幽灵空白节点”和后面<code><span></code>元素字号一样大，也就是：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">32px</span>;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
&#125;
<span class="hljs-selector-class">.box</span> > <span class="hljs-selector-tag">span</span> &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者改变垂直对齐方式，如顶部对齐，这样就不会有参差位移了：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123; <span class="hljs-attribute">line-height</span>: <span class="hljs-number">32px</span>; &#125;
<span class="hljs-selector-class">.box</span> > <span class="hljs-selector-tag">span</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
<span class="hljs-attribute">vertical-align</span>: top;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">图片底部留有间隙(扩展上述问题)</h2>
<p>搞清楚了大小字号文字的高度问题，对更为常见的图片底部留有间隙的问题的理解就容易多了。现象是这样的：任意一个块级元素，里面若有图片，则块级元素高度基本上都要比图片的高度高。例如：</p>
<h3 data-id="heading-14">问题描述</h3>
<pre><code class="copyable"><div class="box">
<img src="1.jpg">
</div>

.box &#123;
width: 280px;
outline: 1px solid #aaa;
text-align: center;
&#125;
.box > img &#123;
height: 96px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果.box 元素底部平白无故多了 5 像素。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a2badc25e0f4a1384bdce43b487d7a5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">分析</h3>
<p>间隙产生的三大元凶就是“幽灵空白节点”、 line-height 和 vertical-align 属性。为了直观演示原理，我们可以在图片前面辅助一个字符 x 代替“幽灵空白节点”，并想办法通过背景色显示其行高范围，于是，大家就会看到如图所示的现象:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b17f223f49644ebbea2013d5ad35f06~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当前 line-height 计算值是 20px，而 font-size 只有 14px，因此，字母 x 往下一定有至少 3px 的半行间距（具体大小与字体有关），**而图片作为替换元素其基线是自身的下边缘。**根据定义，默认和基线（也就是这里字母 x 的下边缘）对齐，字母 x 往下的行高产生的多余的间隙就嫁祸到图片下面，让人以为是图片产生的间隙，实际上，是“幽灵空白节点”、line-height 和 vertical-align 属性共同作用的结果。</p>
<h3 data-id="heading-16">解决</h3>
<p>知道了原理，要清除该间隙，就知道如何对症下药了。方法很多，具体如下。</p>
<ul>
<li>图片块状化。可以一口气干掉“幽灵空白节点”、 line-height 和 verticalalign。</li>
<li>容器 line-height 足够小。只要半行间距小到字母 x 的下边缘位置或者再往上，自然就没有了撑开底部间隙高度空间了。比方说，容器设置 line-height:0。</li>
<li>容器 font-size 足够小。此方法要想生效，需要容器的 line-height 属性值和当前 font-size 相关，如 line-height:1.5 或者 line-height:150%之类；否则只会让下面的间隙变得更大，因为基线位置因字符 x 变小而往上升了。</li>
<li>图片设置其他 vertical-align 属性值。间隙的产生原因之一就是基线对齐，所以我们设置 vertical-align 的值为 top、 middle、bottom 中的任意一个都是可以的。</li>
</ul>
<h2 data-id="heading-17">内联特性导致的 margin 无效</h2>
<p>紧跟上述问题</p>
<pre><code class="copyable"><div class="box">
<img src="mm1.jpg">
</div>
.box > img &#123;
height: 96px;
margin-top: -200px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的例子也很有代表性。一个容器里面有一个图片，然后这张图片设置 margin-top负值，让图片上偏移。但是，随着我们的负值越来越负，结果达到某一个具体负值的时候，图片不再往上偏移了。比方说，本例 margin-top 设置的是-200px，如果此时把 margin-top设置成-300px，图片会再往上偏移 100px 吗？不会！它会微丝不动， margin-top 变得无效了。要解释这里为何会无效，需要对 vertical-align 和内联盒模型有深入的理解。</p>
<h3 data-id="heading-18">分析</h3>
<p>此时，按照理解， -200px 远远超过图片的高度，图片应该完全跑到容器的外面，但是，图片依然有部分在.box 元素中，而且就算 margin-top 设置成-99999px，图片也不会继续往上移动，完全失效。其原理和上面图片底部留有间隙实际上是一样的，图片的前面有个“幽灵空白节点”，**而在 CSS 世界中，非主动触发位移的内联元素是不可能跑到计算容器外面的，**导致图片的位置被“幽灵空白节点”的 vertical-align:baseline 给限死了。我们不妨把看不见的“幽灵空白节点”使用字符 x 代替,原因就一目了然了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5802c6a254b0476bbd16ae53f5bbe0a7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为字符 x 下边缘和图片下边缘对齐，字符 x 非主动定位，不可能跑到容器外面，所以图片就被限死在此问题， margin-top 失效。</p>
<h2 data-id="heading-19">空的 inline-block 元素的高度居然不是0</h2>
<p><a href="http://demo.cssworld.cn/5/3-6.php" target="_blank" rel="nofollow noopener noreferrer">紧跟上述，再看一个复杂点的问题：</a></p>
<h3 data-id="heading-20">问题描述</h3>
<p>text-align:jusitfy 声明可以帮助我们实现兼容的列表两端对齐效果，但是 text-align:jusitfy 两端对齐需要内容超过一行，同时为了让任意个数的列表最后一行也是左对齐排列，我们需要在列表最后辅助和列表宽度一样的空标签元素来占位，类似下面 HTML 代码的<code><i></code>标签：</p>
<pre><code class="copyable">.box &#123;
text-align: justify;
&#125;
.justify-fix &#123;
display: inline-block;
width: 96px;
&#125;
<div class="box">
<img src="1.jpg" width="96">
<img src="1.jpg" width="96">
<img src="1.jpg" width="96">
<img src="1.jpg" width="96">
<i class="justify-fix"></i>
<i class="justify-fix"></i>
<i class="justify-fix"></i>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>空的 inline-block 元素的高度是 0，按照通常的理解，下面应该是一马平川，结果却有非常大的空隙存在:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8b8d81b6314414b98fbf02db13bf4b3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了便于大家看个究竟，我把占位<code><i></code>元素的 outline 属性用虚外框标示一下:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eefa16652e84a4eac1311e4cd20cce6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照之前解决问题的方法，我们可以直接给.box 元素来个 line-height:0 解决垂直间隙问题，结果，这样设置之后的效果,图片和图片之间的间隙是没有了，但是图片和最后的占位元素之间依然有几像素的间距.</p>
<h3 data-id="heading-21">分析</h3>
<p>简单现象的背后往往有大的学问，要明白其原因 ， 就需 要说 到 inline-block 元 素 和 基 线baseline 之间的一些纠缠的关系。</p>
<p>vertical-align 属性的默认值 baseline 在文本之类的内联元素那里就是字符 x 的下边缘，对于替换元素则是替换元素的下边缘。但是，如果是 inline-block 元素，则规则要复杂了： <strong>一个 inline-block 元素，如果里面没有内联元素，或者 overflow 不是 visible，则该元素的基线就是其 margin 底边缘；否则其基线就是元素里面最后一行内联元素的基线。</strong></p>
<p>对于我们上面的问题，上面的规范已经说明了一切。第一个框里面没有内联元素，因此基线就是容器的margin 下边缘，也就是下边框下面的位置；而第二个框里面有字符，纯正的内联元素，因此第二个框就是这些字符的基线，也就是字母 x 的下边缘了。于是，我们就看到了左边框框下边缘和右边框框里面字符 x 底边对齐的好戏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01614b07258e4c339ffb75ea6600cacc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为字符实际占据的高度是由 line-height 决定的，当 line-height 变成 0 的时候，字符占据的高度也是 0，此时，高度的起始位置就变成了字符内容区域的垂直中心位置，于是文字就有一半落在框的外面了。</p>
<p>现在行高 line-height 是 0，则字符x-baseline 行间距就是-1em，也就是高度为 0，由于 CSS 世界中的行间距是上下等分的，因此，此时字符 x-baseline 的对齐点就是当前内容区域（可以看成文字选中背景区域）的垂直中心位置。 x-baseline 使用的是微软雅黑字体，字形下沉明显，因此，内容区域的垂直中心位置大约在字符 x 的上面 1/4 处。而这个位置就是字符 x-baseline 和最后一行图片下边缘交汇的地方。</p>
<p><strong>理解了 x-baseline 的垂直位置表现，间隙问题就很好理解了。由于前面的<code><i class="justify-fix"></i></code>是一个 inline-block 的空元素，因此基线就是自身的底部，于是下移了差不多 3/4 个 x 的高度，这个下移的高度就是上面产生的间隙高度。</strong></p>
<h3 data-id="heading-22">解决</h3>
<p>好了，一旦知道了现象的本质，我们就能轻松对症下药了！要么改变占位<code><i></code>元素的基线，
要么改造“幽灵空白节点”的基线位置，要么使用其他 vertical-align 对齐方式。</p>
<h4 data-id="heading-23">改变基线位置</h4>
<p>只要在空的<code><i></code>元素里面随便放几个字符就可以了。例如，塞一个空格&nbsp：</p>
<pre><code class="copyable">.box &#123;
text-align: justify;
line-height: 0;
&#125;
<div class="box">
<img src="1.jpg" width="96">
<img src="1.jpg" width="96">
<img src="1.jpg" width="96">
<img src="1.jpg" width="96">
<i class="justify-fix">&nbsp;</i>
<i class="justify-fix">&nbsp;</i>
<i class="justify-fix">&nbsp;</i>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了更分明一些，我们将空格改为字符“xxx”，如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a0b877ccc3a4c0e84a9948d671dbf9a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为这个时候前两个<code><i></code>的元素错位已经没有了，最后一个自然就向上没有间隙了，但是，假如最后一个没有字符，依然会有间隙，如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccf07a2369b43f09b50ee4c1ceb9ac9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候的解释其实就是，虽然已经换行了，但是对齐点还是要和上一行的元素进行对齐，也就是说要和倒数第二个<code><i></code>对齐，就变成相同的问题了，即错位对齐了，所以每个<code><i></code>内都要添加元素才可以。</p>
<p>为什么呢？因为此时<code><i></code>元素的基线是里面字符的基线，此基线也正好和外面的“幽灵空白节点”的基线位置一致，没有了错位，就没有间隙。</p>
<h3 data-id="heading-24">改造“幽灵空白节点”的基线位置</h3>
<p>可以使用 font-size，当字体足够小时，基线和中线会重合在一起。什么时候字体足够小呢？就是 0。于是，如下 CSS 代码（line-height 如果是相对 font-size 的属性值， line-height:0 也可以省掉）：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">text-align</span>: justify;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看上去好像效果类似，都是没有间隙，但是font-size:0 下的各类对齐效果都更彻底。<strong>这时的幽灵节点已经没有高度了，肯定没有间隙了。</strong></p>
<h3 data-id="heading-25">修改vertical-align 对齐方式</h3>
<p>使用其他 vertical-align 对齐方式就是让<code><i></code>占位元素vertical-align:top/bottom之类，当前，前提还是先让容器 line-height:0，例如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
<span class="hljs-attribute">text-align</span>: justify;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.justify-fix</span> &#123;
<span class="hljs-attribute">vertical-align</span>: top; <span class="hljs-comment">/* top、 middle 都可以 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下图是top对齐的情况，这个时候其实没有了对不齐的基线问题了肯定就不会显示异常了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c55107201344e26b13a855a8a11edcd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候还会有疑问，假如接着增加<code><i></code>的个数，就不会出现对不齐吗，当然不会，下一行都是相对于上一行进行的，也就是说其实换行，对齐依然对的是上一行的元素，<strong>只要对齐位置没问题，就不会出现间隙。</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dee7415409d4e7c93d210f8fce13966~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">总结</h3>
<p>归根结底，就是inline-block基线位置问题，基线位置不同，就出现了错位的现象，只要消除了错位，就不会出现间隙。<strong>时时刻刻谨记一个块级元素内出现内联元素的时候，这个时候一定要考虑匿名内联，考虑了匿名内联，就要考虑匿名内联的空白幽灵高度，然后还有考虑空白幽灵节点的对齐是基线对齐</strong></p>
<p>以上！
最后的惯例，贴上<a href="https://github.com/zhyjor/homepage-index" target="_blank" rel="nofollow noopener noreferrer">我的博客</a>，欢迎关注</p>
<p><strong>参考资料</strong></p>
<p><a href="https://www.cnblogs.com/rixinren2010/archive/2012/03/10/2389301.html" target="_blank" rel="nofollow noopener noreferrer">垂直对齐：vertical-align属性（转）</a></p>
<p><a href="https://www.zhangxinxu.com/wordpress/2015/03/css3-object-position-object-fit/" target="_blank" rel="nofollow noopener noreferrer">半深入理解CSS3 object-position/object-fit属性</a>
<a href="http://ideazhao.lofter.com/post/1d377a05_709cb7f" target="_blank" rel="nofollow noopener noreferrer">小谈inline-block的那点空隙</a></p>
<p>请关注公众号：<strong>全栈飞行中队</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f98a8233a0a6487487b8ff592ecb3c25~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            