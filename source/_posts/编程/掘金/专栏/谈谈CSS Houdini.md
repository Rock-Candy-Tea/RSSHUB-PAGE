
---
title: '谈谈CSS Houdini'
categories: 
 - 编程
 - 掘金
 - 专栏
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9920a2b2d0044dc7a129b418cedbdfd7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 18:27:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9920a2b2d0044dc7a129b418cedbdfd7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文来自 飞猪前端团队成员 - 影羽 的内部分享</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9920a2b2d0044dc7a129b418cedbdfd7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>demo by @andreban</p>
<h2 data-id="heading-0">什么是CSS Houdini</h2>
<blockquote>
<p>Houdini 是一组底层 API，它们公开了 CSS 引擎的各个部分，从而使开发人员能够通过加入浏览器渲染引擎的样式和布局过程来扩展 CSS。 Houdini 是一组 API，它们使开发人员可以直接访问CSS 对象模型 （CSSOM），使开发人员可以编写浏览器可以解析为 CSS 的代码，从而创建新的 CSS 功能，而无需等待它们在浏览器中本地实现。 - MDN</p>
</blockquote>
<h4 data-id="heading-1">设计初衷</h4>
<p>不同于JS新特性可以通过类似babel等transform或者polyfill的方式来较快的使用上。CSS的新特性会经历长期的规范推进和浏览器厂商实现最后到浏览器版本覆盖才能够很好的使用。CSS的polyfill受制于浏览器限制，能够影响到渲染部分的阶段及其有限（DOM操作和部分CSSOM操作），而且很容易触发浏览器渲染步骤导致性能问题。所以它设计之初是为了解决这种CSS的新特性需要长周期才能适用的情况。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e5257e0ec84d1ea31e369570d73adb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">Houdini API概览和应用</h4>
<p>W3C规范中将Houdini API包含了Painting API、Parser API、Properties and Values API、Typed OM、Font Metrics API 、Layout API、Animation Worklet、Box Tree API。</p>
<p>其中这些API穿插在整个浏览器渲染过程的方方面面，以此来达到高性能和定制性的目的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7cebb3b72594ed6b4acd4856563fa10~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这个图很好的诠释了Houdini 的API们是如何运作的，首先在计算阶段，CSS Typed OM 扩展了CSSOM的能力，使之不仅仅局限于字符串的操作，从而可以更好的通过JavaScript来以对象形式进行访问和操作。Properties and Values API则可以更加自由的去注册具有自定义继承，初始值和类型的CSS变量或者方法。其次在渲染阶段，通过在渲染过程中执行的独立于JavaScript主线程的Worklets脚本，分别通过Layout API，Painting API等去控制自定义的CSS在浏览器中的渲染。</p>
<h2 data-id="heading-3">Houdini API</h2>
<blockquote>
<p>由于Houdini API依旧在不断发展的阶段，大部分功能还在缓慢的在浏览器和规范化进程中推进，这里主要介绍几个推进的比较好的，更加具象的API。</p>
</blockquote>
<h4 data-id="heading-4">CSS Typed OM 1</h4>
<p>首先CSS Typed OM API提供了更好的CSSOM操作能力，简单来说就是把JavaScript的Object这种描述方式应用到了CSSOM上去，可以通过对CSS属性的对象化操作来替代之前的字符串操作。官方提供了一个例子：</p>
<pre><code class="hljs language-ini copyable" lang="ini">// 修改元素高度 - now
// 需要提取字符串数字部分，对数字部分进行运算，将运算好的拼接成字符串重新赋值
let <span class="hljs-attr">heightValue</span> = target.style.height.slice(<span class="hljs-number">0</span>,-<span class="hljs-number">2</span>)<span class="hljs-comment">;</span>
heightValue++<span class="hljs-comment">;</span>
<span class="hljs-attr">target.style.height</span> = heightValue + <span class="hljs-string">'px'</span><span class="hljs-comment">;</span>

// 修改元素高度 - Typed OM
// 获取高度，对高度进行运算，赋值
let <span class="hljs-attr">heightValue</span> = element.attributeStyleMap.get(<span class="hljs-string">'height'</span>)<span class="hljs-comment">;</span>
heightValue.value++<span class="hljs-comment">;</span>
target.attributeStyleMap.set('height', heightValue)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就使得CSSOM的操作更加的“程序化”和自然。</p>
<p>另一方面，Typed OM也描述了CSSOM里面很多的变量及单位的定义，对后面的进一步Houdini使用也打好了基础。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f6a929e89304192aae38a6335ab95e3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">CSS Properties and Values API 1</h4>
<p>Properties and Values API 提供了可以通过JavaScript或者@property自由组合重新设计一个自定义的CSS 属性的能力。在以前的CSS使用当中我们没办法控制一个CSS属性的一些固有属性，比如是否能够继承，默认初始值是多少等等。通过前面Typed OM定义出来的一些属性和值，我们就可以根据自身诉求来创造出最佳的CSS属性和相应值。比如官方示例中：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// 注册自定义属性--stop-color，不可以被继承，类型时color，初始值是rgba(0,0,0,0)</span>
<span class="hljs-variable constant_">CSS</span>.<span class="hljs-title function_">registerProperty</span>(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"--stop-color"</span>,
  <span class="hljs-attr">syntax</span>: <span class="hljs-string">"<color>"</span>,
  <span class="hljs-attr">inherits</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">initialValue</span>: <span class="hljs-string">"rgba(0,0,0,0)"</span>
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.button</span> &#123;
  <span class="hljs-attr">--stop-color</span>: red;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-built_in">var</span>(--stop-color), black);
  <span class="hljs-attribute">transition</span>: --stop-color <span class="hljs-number">1s</span>;
&#125;

<span class="hljs-selector-class">.button</span><span class="hljs-selector-pseudo">:hover</span> &#123;
  <span class="hljs-attr">--stop-color</span>: green;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单总结下它带来的一些好处有：</p>
<ul>
<li>
<p>可以制定具体变量类型</p>
</li>
<li>
<p>可以支持渐变动画</p>
</li>
<li>
<p>可以设置初始值以及继承，控制后代元素的样式表现</p>
</li>
</ul>
<h4 data-id="heading-6">CSS Painting API 1</h4>
<p>Paint API从使用上来说就像一个使用方便的绘制自由的Canvas2D画布。它提供了对元素的background, border, or content的绘制填充能力，可以将想要的内容画上去，并且支持参数定制和变化。官方对此API设定的原因有如下几点解释：</p>
<ul>
<li><strong>简化DOM渲染</strong> - 当前很多“特殊”的CSS实现是通过堆叠DOM等操作去实现绘制和渲染，那么直接使用canvas画布渲染可以减少CPU内存等占用，提升页面性能。</li>
<li><strong>渲染流程效率</strong> - 前面提到了 Worklets 的方式，可以介入到浏览器渲染流程当中，是其他方式效率比拟不了的。</li>
<li><strong>页面绘制效率</strong> - 这个比较清晰，这种会绘制方式可以保持浏览器局部渲染（局部repaint），减少页面整体渲染的可能。</li>
<li><strong>扩展性</strong> - 这个是Houdini设计初衷，可以不依赖浏览器的实现去自己扩展需要的绘制能力，比如要实现虚线边框则不用等浏览器自身去实现（ps.扩展这个本身需要浏览器支持）</li>
</ul>
<p>Paint API的使用也不复杂，熟悉canvas的同学应该更加容易上手。主要由2部分构成：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-meta"><!DOCTYPE <span class="hljs-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-id">#example</span> &#123;
    <span class="hljs-attr">--circle-color</span>: deepskyblue;

    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">paint</span>(circle);
    <span class="hljs-attribute">font-family</span>: sans-serif;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">36px</span>;
    <span class="hljs-attribute">transition</span>: --circle-color <span class="hljs-number">1s</span>;
  &#125;

  <span class="hljs-selector-id">#example</span><span class="hljs-selector-pseudo">:focus</span> &#123;
    <span class="hljs-attr">--circle-color</span>: purple;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"example"</span>></span>
  CSS is awesome.
<span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-variable constant_">CSS</span>.<span class="hljs-title function_">registerProperty</span>(&#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'--circle-color'</span>,
      <span class="hljs-attr">syntax</span>: <span class="hljs-string">'<color>'</span>,
      <span class="hljs-attr">initialValue</span>: <span class="hljs-string">'black'</span>,
      <span class="hljs-attr">inherits</span>: <span class="hljs-literal">false</span>
    &#125;);
    <span class="hljs-variable constant_">CSS</span>.<span class="hljs-property">paintWorklet</span>.<span class="hljs-title function_">addModule</span>(<span class="hljs-string">'circle.js'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

registerPaint('circle', class &#123;
  static get inputProperties() &#123; return ['--circle-color']; &#125;
  paint(ctx, geom, properties) &#123;
    // Change the fill color.
    const color = properties.get('--circle-color');
    ctx.fillStyle = color.cssText;

    // Determine the center point and radius.
    const x = geom.width / 2;
    const y = geom.height / 2;
    const radius = Math.min(x, y);

    // Draw the circle \o/
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI, false);
    ctx.fill();
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即可在background中绘制出想要绘制的图案。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e7e6334665941cb8df4d3feea85998a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhoudini.how%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://houdini.how/" ref="nofollow noopener noreferrer">houdini.how/</a>上有大量的炫酷的效果可以去观赏。</p>
<h4 data-id="heading-7">CSS Layout API 1 & CSS Animation Worklet 1</h4>
<p>最后介绍的是Layout 和 Animation API，这两个API由于推进进展比较缓慢，所以还属于非常不成熟的状态，各大浏览器的实现及其有限，只做下简单介绍。详细可以浏览具体规范。</p>
<p>Layout API放开了对布局的一些限制，可以将自己的布局算法/函数应用到实际场景中，构建出类似于Flexbox等布局方式，比如瀑布流布局之类。</p>
<p>Animation Worklet API则是将动画能力开放出来，能够通过Worklet中的脚本来控制动画的函数，运行时间，结束状态等等，预想中能够自然实现诸如视差滚动，自定义缓动动画等等。</p>
<h2 data-id="heading-8">现状和活跃度</h2>
<p>首先是浏览器支持现状，如图（截止到21年5月，后面没有更新了🐶）。可见对于基础的Typed OM，priperties以及Paint API各方面支持的还挺不错，Safari也都在逐步支持中。而Layout 和 Animation等则依旧比较遥远。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/207e424407d641a98298396136da4c70~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>活跃度方面W3C规范草案更新还是比较频繁，最近的更新时间是22年7月还是在活跃中。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b23eda01aff46a18b72e19cd9267b21~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">个人理解</h2>
<p>CSS Houdini 设计初衷十分有远见和强大，但是也有比较明显的局限性。一方面是老生常谈的规范推进和浏览器厂商的实现。另一方面如MDN上说的：</p>
<blockquote>
<p>能力越大，责任越大！在 Houdini 的帮助下你能够在 css 中实现你自己的布局、栅格、或者区域特性，但是这么做并不是最佳实践。CSS 工作组已经做了许多努力来确保 CSS 中的每一项特性都能正常运行，覆盖各种边界情况，同时考虑到了安全、隐私，以及可用性方面的表现。如果你要深入使用 Houdini，确保你也把以上这些事项考虑在内！并且先从小处开始，再把你的自定义 Houdini 推向一个富有雄心的项目。</p>
</blockquote>
<p>CSS Houdini 有很高的理解成本，需要有足够的能力和想象力，而简单的实现又有很大的可替代性（可以简单通过其他方式实现）。</p>
<p>但是从另一个方面，CSS Houdini 将浏览器的渲染流程进一步的“坦诚相待”，一定程度的白盒化了渲染过程，好像试图要教会我们怎么做渲染，那对前端技术而言则不可谓是个深入学习渲染原理的方式。</p>
<h2 data-id="heading-10">参考</h2>
<ul>
<li>
<p>W3C规范：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdrafts.css-houdini.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://drafts.css-houdini.org/" ref="nofollow noopener noreferrer">drafts.css-houdini.org/</a></p>
</li>
<li>
<p>MDN：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FGuide%2FHoudini%23worklets" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/Guide/Houdini#worklets" ref="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></p>
</li>
<li>
<p>浏览器进展：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fishoudinireadyyet.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ishoudinireadyyet.com/" ref="nofollow noopener noreferrer">ishoudinireadyyet.com/</a></p>
</li>
<li>
<p>其他介绍：</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fhoudini.glitch.me%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://houdini.glitch.me/" ref="nofollow noopener noreferrer">houdini.glitch.me/</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3cplus.com%2Fcss%2Fhoudini-how-and-css-paint-api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3cplus.com/css/houdini-how-and-css-paint-api.html" ref="nofollow noopener noreferrer">www.w3cplus.com/css/houdini…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.to%2Fadrianbdesigns%2Fcss-houdini-paint-api-explained-3il0" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.to/adrianbdesigns/css-houdini-paint-api-explained-3il0" ref="nofollow noopener noreferrer">dev.to/adrianbdesi…</a></p>
</li>
<li>
<p>Painting API DEMO：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FGoogleChromeLabs%2Fhoudini-samples" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/GoogleChromeLabs/houdini-samples" ref="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p>
</li>
</ul></div>  
</div>
            