
---
title: 'CSS实现动画真的性能更好么？由页面动画卡顿引发的思考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20a57cb3db3543b0bceae950caba6b9e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 23:08:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20a57cb3db3543b0bceae950caba6b9e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在优化页面动画效果时，和同事探讨到了页面动画卡顿的问题，即使大致了解CSS实现的动画会比JS性能更佳，卡顿更少，但是一直没有深究这样的问题原理是什么。这次在优化过程中，发现即使使用CSS动画，但是在使用height，width，margin，padding作为transition的值的时候，依然会卡顿，但是使用CSS transform就会有明显的改善。问题类似就不赘述了，在参考中附一个类似的问题。
这里主要讲一讲CSS到底哪些动画效果帧数高，性能好，背后的原理到底又是什么。</p>
<h3 data-id="heading-0">CSS 和 JS 怎样实现页面动画？</h3>
<p>CSS和JS都可以实现一些网页的动画效果，比如CSS transitions/animations 和 JavaScript-based animations (using requestAnimationFrame())</p>
<h4 data-id="heading-1">CSS transitions 和 animations</h4>
<p>CSS transitions 提供了一种简单的方式在现有样式和最终CSS状态之间实现动画效果。即使元素仍然在变化过程中，新的transition会从现在的样式开始变化而不是直接跳到结束时的CSS状态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20a57cb3db3543b0bceae950caba6b9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>CSS animations允许开发者在一系列开始值和终止值之间设定动画，它包含两个部分，一种描述CSS animation的样式，以及定义多个关键帧以及每个关键帧中元素的属性值</p>
<h4 data-id="heading-2">requestAnimationFrame</h4>
<p>requestAnimationFrame告诉浏览器——你希望执行一个动画，并且要求浏览器在下次重绘之前调用指定的回调函数更新动画。该方法需要传入一个回调函数作为参数，该回调函数会在浏览器下一次重绘之前执行。
和CSS transitions 和 animations一样，requestAnimationFrame()在当前Tab被push到后台时，也会暂停。</p>
<h3 data-id="heading-3">CSS真的比JS实现的动画快么？</h3>
<p>先说结论，不是的。
在大多数情况下，其实CSS和JS实现的动画性能其实都是差不太多的，甚至有些JS动画库宣称他们的性能是要强过CSS原生动画的。这种情况之所以会发生，是因为CSS transitions/animations会在repaint事件发生前，在UI主进程中重新采集元素的样式。这和requestAnimationFrame() callback采用的形式其实基本上一样。
所以如果animations是发生在主进程中，其实性能上并没什么卵差别的。</p>
<h3 data-id="heading-4">为啥CSS animations仍是更棒的选择？</h3>
<p>CSS animations更棒的关键在于，只要我们希望设置动效的属性并没有触发reflow/repaint操作，我们就可以将塑造元素的操作移除主进程。浏览器只需要一次生成这个元素的位图，并在动画开始的时候将它提交给GPU去处理，这就会显著提升处理性能，尤其是在移动设备上。之后，浏览器不需要再做任何布局、 绘制以及提交位图的操作。从而，浏览器可以充分利用 GPU 的特长去快速地将位图绘制在不同的位置、执行旋转或缩放处理。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a966b5a720f745299ba213b08429fb6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Platform/GFX/OffMainThreadCompositing <a href="https://wiki.mozilla.org/Platform/GFX/OffMainThreadCompositing" target="_blank" rel="nofollow noopener noreferrer">wiki.mozilla.org/Platform/GF…</a></p>
</blockquote>
<p><strong>这其中，最常见的用法就是 CSS transform</strong></p>
<p>在 CSS triggers（<a href="https://csstriggers.com/%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">csstriggers.com/）</a>
这张表里，我们可以看到transform是不会在Layout和Paint层面作trigger的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02d7ebef84a242769510856efa8ecc2d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/101bb85184ee49dd81437000ac291c56~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当然，也可以发现目前WebKit内核在CSS triggers上和Gecko内核仍然是有区别的，这也就不排除IOS和Android设备在移动端的动画性能上，同样的实现方式仍然会有体验上的差别。</p>
<p>参考：</p>
<ol>
<li>CSS and JavaScript animation performance <a href="https://developer.mozilla.org/en-US/docs/Web/Performance/CSS_JavaScript_animation_performance" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></li>
<li>CSS3动画卡顿性能优化解决方案 <a href="https://segmentfault.com/a/1190000013045035" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></li>
<li>Using CSS transitions <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></li>
<li>Using CSS animations <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></li>
</ol></div>  
</div>
            