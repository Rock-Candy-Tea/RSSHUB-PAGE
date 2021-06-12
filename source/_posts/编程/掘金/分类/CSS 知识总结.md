
---
title: 'CSS 知识总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16469928491b402db96c2d606eff4125~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:19:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16469928491b402db96c2d606eff4125~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">0. 序言</h1>
<p>关于这一部分，Google（Chrome）与Mozilla（Firefox）的官方文档就说的很明确了。Google文档需要一些特别手段才能看到，这对于程序员不是啥大问题。不过Google官方文档的一个问题是它是以英文原文写成，虽然对于我这个英文专业出身的人来说问题不大，但对于英文不好的同学来说会比较痛苦。但更重要的是Google官方的中文翻译质量不高，基本上断绝了大部分人看Google官方文档的可能及必要性。不过在文末还是附上了Google团队的文章，供我自己以及英文好的同学阅读。</p>
<p>但有一件好事是，Mozilla团队的本地化工作一直做的非常出色，虽然它们的文档是由英文写成，但它们的翻译同样良心。</p>
<p>本次笔记的参考文献是两家的文章。</p>
<h1 data-id="heading-1">1. 浏览器渲染原理</h1>
<p>在经过导航（Navigation）之后，浏览器获得了后台返回的数据，接下来就是对这些数据进行渲染及展示的过程。而这一过程正是浏览器的渲染原理。至于导航，涉及到HTTP协议相关知识，另起一篇博客写作，此处暂按下不表。写完之后会将超链接更新到这里。</p>
<p>我们从后台获取到的数据并不是一下子就成为网页的。最一开始要处理的数据是一段HTML代码及CSS代码。</p>
<p>HTML代码示例（来源于MDN文档）：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><!doctype HTML>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>My simple page<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"styles.css"</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"myscript.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"heading"</span>></span>My Page<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>A paragraph with a <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://example.com/about"</span>></span>link<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"myimage.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"image description"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"anotherscript.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS代码示例（我自己写的）：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">.heading&#123;
    font-family : san-serif;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器实际上执行的是对上述代码进行<strong>解析</strong>的过程。</p>
<p>获得代码后，浏览器便开始解析。解析的实质是经历一个Bytes → characters → tokens → nodes → object model的过程<sup>[3]</sup>。</p>
<p>从bytes到characters的转变涉及到计算机内部原理知识，倒也不难--按照一定的编码标准（通常是utf-8）解析我们写下的html代码。</p>
<p>从characters到tokens的转变过程是tokenization。根据Google官方的解释，tokenization是“The browser converts strings of characters into distinct tokens—as specified by the W3C HTML5 standard; for example, <code><html></code>, <code><body></code>—and other strings within angle brackets. Each token has a special meaning and its own set of rules.”翻译一下，是浏览器将<code>html</code>标签按照诸如W3C标准等标准进行意义化的过程。在这个过程中<code><html></code>等标签不再是干巴巴的字符串，而是有意义的。可以理解为把彩票兑奖了。</p>
<p>接下来，浏览器便构造DOM树（HTML DOM）与CSSDOM树，也就是俗称的“<strong>两棵树</strong>”。那么，两棵树分别长什么样子呢？</p>
<p>这是DOM树（图片来自Google）：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16469928491b402db96c2d606eff4125~tplv-k3u1fbpfcp-watermark.image" alt="Google团队DOM树" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是CSSDOM树（图片来自Google）：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a35d0ca2aa74cefafb9fee8aa5bc9dc~tplv-k3u1fbpfcp-watermark.image" alt="Google团队CSSDOM树" loading="lazy" referrerpolicy="no-referrer"></p>
<p>构建DOM树恰好符合html自身的树形结构。DOM树刚好描述了文档的内容，也表示出了层级关系。在DOM树中，<code><html></code>是树根，在其下逐层展开内容。</p>
<p>关于CSSDOM树，虽然CSS的指定方式并不必须遵守HTML式的树形结构，但其由于和HTML深度绑定，所以也获得了树形结构。在CSS中，子节点(node)会继承父节点的CSS样式，但也可以指定自己的样式。</p>
<p>最后一步进行渲染。具体过程是：</p>
<p>将DOM树与CSSDOM树组合而成一棵渲染树（render tree），树上只有需要被渲染到页面上的节点。然后进行布局（layout）计算，将树上的各个元素进行布局，可以理解为从树上摘下果子然后整齐地放到安排好的位置上去。最后再绘制网页。</p>
<p>总结一下，除却计算机内部的必要过程（Bytes → characters → tokens）外，后两步的过程（nodes → object model）与做画、写文章有类似之处：先搭骨架（DOM树和CSSDOM树），再搞内容。</p>
<h1 data-id="heading-2">2. CSS 动画的两种做法</h1>
<p>什么是动画？即静止画面连续播放时由于视觉残象产生的错觉。在CSS中，做动画有两种办法：<code>transition</code>和<code>animation</code>。</p>
<ul>
<li><code>transition</code>：可用于指定一个或多个属性的过渡效果。可以为一个元素在不同状态之间切换的时候定义不同的过渡效果。</li>
<li><code>animation</code>：用来指定一组或多组动画，每组之间用逗号相隔</li>
</ul>
<p>事实上，<code>transition</code>和<code>animation</code>都是简写属性。</p>
<p><code>transition</code>包括以下分支属性：</p>
<ul>
<li><code>transition-property</code>：指定应用过渡属性的名称。</li>
<li><code>transition-duration</code>：以秒或毫秒为单位指定过渡动画所需的时间。默认值为<code>0s</code>，表示不出现过渡动画。</li>
<li><code>transition-timing-function</code>：CSS属性受到<code>transition effect</code>的影响，会产生不断变化的中间值。而该属性是用来描述这个中间值是怎样计算的。</li>
<li><code>transition-delay</code>：规定了在过渡效果开始作用之前需要等待的时间。</li>
</ul>
<p><code>transition</code>后用空格分隔的属性顺序为：
<code>property name | duration | timing function | delay </code></p>
<p>关于都有哪些<code>transition-timing-function</code>，可以参考<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function" target="_blank" rel="nofollow noopener noreferrer">MDN官方说明</a><sup>[6]</sup>，有详细的说明及动态演示。</p>
<p>而<code>animation</code>包括的分支属性则更多。依顺序包括如下：</p>
<ul>
<li><code>animation-name</code>：为动画取名</li>
<li><code>animation-duration</code>：指定一个动画周期的时长</li>
<li><code>animation-timing-function</code>：属性定义CSS动画在每一动画周期中执行的节奏。可能值为一或多个 <code><timing-function></code>。</li>
<li><code>animation-delay</code>：定义动画于何时开始，即从动画应用在元素上到动画开始的这段时间的长度。0s是该属性的默认值，代表动画在应用到元素上后立即开始执行。</li>
<li><code>animation-iteration-count</code>：定义动画在结束前运行的次数。</li>
<li><code>animation-direction</code>：指示动画是否反向播放。</li>
<li><code>animation-fill-mode</code>：设置CSS动画在执行之前和之后如何将样式应用于其目标。</li>
<li><code>animation-play-state</code>：属性定义一个动画是否运行或者暂停。</li>
</ul>
<p>以空格形式隔开亦遵循上面的顺序。</p>
<h1 data-id="heading-3">3. 其他想写的话</h1>
<p>都在这两篇文章中了：</p>
<ul>
<li><a href="https://juejin.cn/post/6966186736086941726" target="_blank">前端学习踩的坑</a></li>
<li><a href="https://juejin.cn/post/6967567795798147085" target="_blank">CSS层叠上下文</a></li>
</ul>
<h1 data-id="heading-4">Reference</h1>
<ul>
<li>[1] <a href="https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work" target="_blank" rel="nofollow noopener noreferrer">Populating the page: how browsers work - MDN</a></li>
<li>[2] <a href="https://developer.mozilla.org/zh-CN/docs/Web/Performance/How_browsers_work" target="_blank" rel="nofollow noopener noreferrer">渲染页面：浏览器的工作原理-MDN</a></li>
<li>[3] <a href="https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction" target="_blank" rel="nofollow noopener noreferrer">Google团队的相关文章</a></li>
<li>[4] <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation" target="_blank" rel="nofollow noopener noreferrer">animation - MDN</a></li>
<li>[5] <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition" target="_blank" rel="nofollow noopener noreferrer">transition - MDN</a></li>
<li>[6] <a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition-timing-function" target="_blank" rel="nofollow noopener noreferrer">Timing Function - MDN</a></li>
</ul></div>  
</div>
            