
---
title: 'HTML界的_苏炳添_——详解Canvas优越性能和实际应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d279e3a75540455497ef1cce9da1efd5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 19:03:37 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d279e3a75540455497ef1cce9da1efd5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Google Docs宣布将会把HTML迁移到基于Canvas渲染，这一消息的出现再次把几年前随HTML5诞生的标签重新推到了人们视线之中。Canvas在刚推出时主打的优势就是更快的渲染速度，堪称HTML届的“苏炳添”，刷新了人们对Web页面元素绘制速度的印象。但Canvas的优势仅限于此吗？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d279e3a75540455497ef1cce9da1efd5~tplv-k3u1fbpfcp-watermark.image" alt="0.jpg" loading="lazy" referrerpolicy="no-referrer">
（苏炳添，亚洲百米第一人）</p>
<h1 data-id="heading-0">HTML绘图届的前辈：SVG</h1>
<p>Canvas是HTML5时代引入的“新”标签。与很多标签不同，Canvas不具有自己的行为，只将一组API 展现给客户端 JavaScript ，让开发者使用脚本把想绘制的东西画到一张画布上。</p>
<p> </p>
<p>在HTML5之前，人们通常使用SVG来在页面上绘制出图形。SVG使用XML来定义图形，就像使用HTML标签和样式定义DIV一样，我们也可以将一个空白的DIV想象为长方形的SVG，两者的设计思想是相通的，SVG的本质就是一个DOM元素。而Canvas则不同，Canvas提供的是 JavaScript 的绘图 API，而不是像 SVG那样使用XML 描述绘图，通过JavaScript API直接完成绘制，比起修改XML来说要更简便、更直接。</p>
<p> </p>
<p>除了定义的方式不同，Canvas和DOM（当然也包含SVG）的差异更多的体现在浏览器的渲染方式上。</p>
<p> </p>
<p>浏览器在做页面渲染时，Dom元素是作为矢量图进行渲染的。每一个元素的边距都需要单独处理，浏览器需要将它们全都处理成像素才能输出到屏幕上，计算量十分庞大。当页面上内容非常多，存在大量DOM元素的时候，这些内容的渲染速度就会变得很慢。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94611cd7a78d4fe69a79ca9b805d6d71~tplv-k3u1fbpfcp-watermark.image" alt="1.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（Canvas）</p>
<p>而Canvas与DOM的区别则是Canvas的本质就是一张位图，类似img标签，或者一个div加了一张背景图（background-image）。所以，DOM那种矢量图在渲染中存在的问题换到Canvas身上就完全不同了。在渲染Canvas时，浏览器只需要在JavaScript引擎中执行绘制逻辑，在内存中构建出画布，然后遍历整个画布里所有像素点的颜色，直接输出到屏幕就可以了。不管Canvas里面的元素有多少个，浏览器在渲染阶段也仅需要处理一张画布。</p>
<p> </p>
<p>然而这样更加强大的功能，不可避免的让使用canvas渲染有很高的门槛。Google Docs在构建Canvas的过程中重新定义了往常已经被人们所熟悉的内容，例如精确定位、文本选择、拼写检查、重画调优等。为什么更多开发者还是选择了接纳Canvas这个门槛更高的技术路线呢？这就得回到Canvas的最大优势：渲染性能。</p>
<h1 data-id="heading-1">Canvas的渲染模式</h1>
<p>这里的渲染是指浏览器将页面的代码呈现为屏幕上内容的过程。Canvas和Dom的渲染模式完全不同，搞清楚这个差异对理解Canvas的性能优势至关重要。</p>
<h2 data-id="heading-2">Dom：驻留模式</h2>
<p>驻留模式（Retained Mode）是Dom在浏览器中的渲染模式。下图粗略展示了这一过程的工作流程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c375b932f48841b4af51414df0994916~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>(驻留模式)</p>
<p>DOM的核心是标签，一种文本标记型语言，多样性很强且多个标签之间存在各种关联（如在同一个DIV下设置为float的子DIV）。浏览器为了更好的处理这些DOM元素，减少对绘制API的调用，就设计了一套将中间结果存放于内存的“驻留模式”。首先，浏览器会将解析DOM相关的全部内容（包含HTML标签、样式和JavaScript），将其转化为场景（scene）和模型（model）存储到内存中，然后再调用系统的绘制API（如Windows程序员熟悉的GDI/GDI+），把这些中间产物绘制到屏幕。</p>
<p> </p>
<p>驻留模式通过场景和模型缓存减少了对绘制API的调用频次，将性能压力转移到场景和模型生成阶段，即浏览器需要根据DOM上下文和BOM中的尺寸数据，“自行判断”每一个元素的绘制结果。</p>
<h2 data-id="heading-3">Canvas：快速模式</h2>
<p>Canvas采用了和DOM不同的快速模式（Immediate Mode），让我们先来看看快速模式是如工作的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f5db7b1f5cc4866a6aef120b5d16675~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（快速模式）</p>
<h1 data-id="heading-4">Canvas的应用优点</h1>
<p>上面介绍的两种不同的模式直接造成了Dom和Canvas的性能差异。对于使用快速模式渲染的Canvas而言，浏览器的每次重绘都是基于代码的，不存在能让处理流程变慢的多层解析，所以它真的很快。除了快之外，Canvas的灵活性也大大超出DOM。我们可以通过代码精确的控制如何、何时绘制出我们想要的效果。</p>
<p> </p>
<p>在资源消耗上，DOM的驻留模式意味着场景中每增加一点东西就需要额外消耗一些内存，而Canvas并没有这个问题。这个差异会随着页面元素的数量增多而愈加明显。以B端的企业应用场景为例，表单那种数据量比较小的场景，不同渲染模式带来的效果差异并不明显；但在工业制造、金融财会等类Excel电子表格操作的场景下，单元格数量动辄便是上百万（5万行x 20列）甚至上亿个，浏览器需要对表格所有单元格本身内容进行渲染，同时还涉及到丰富的数据处理，情况就完全不同了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5561ef198c004b6fae5e44df1a204874~tplv-k3u1fbpfcp-watermark.image" alt="111.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（Web页面上的电子表格，包含1百万个单元格）</p>
<p>在Canvas出现之前，在前端渲染表格时只能通过构建复杂的DOM来实现。这种方式下，浏览器的性能成为了Web应用瓶颈，让很多开发者放弃了在浏览器上实现电子表格的想法。</p>
<p> </p>
<p>在Canvas出现后，快速模式带来的性能优势无疑是一个巨大的亮点，大量、复杂的DOM渲染处理带来的性能问题终于有了解决途径。</p>
<p> </p>
<p>回到电子表格的应用场景，业内已经出现了使用Canvas绘制画布的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fspreadjs" target="_blank" rel="nofollow noopener noreferrer" title="https://www.grapecity.com.cn/developer/spreadjs" ref="nofollow noopener noreferrer">表格组件</a>，这类组件在渲染数据层时不仅无需重复创建和销毁DOM元素，在画布的绘制过程中，也比Dom元素渲染的限制更少。除了表格之外，Canvas也为数字孪生可视化大屏、页面游戏等场景带来了变革。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c097078be5c94657957ee5655d610713~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（数字孪生大屏，精确控制各种形状、样式）</p>
<h1 data-id="heading-5">总结</h1>
<p>总结一下，在渲染模式上，Canvas站在了DOM的对面，浏览器对其内容一无所知，一切渲染的权利回到了开发者的手上，这个改变带来了显著的性能优势。此外，我们可以使用Canvas绘制种类更为丰富的UI元素，如线形、特殊图形等，通过画法逻辑，还可以实现更加精准的UI界面渲染，解决了浏览器差异造成的样式误差，让更多应用场景可以顺利迁移到Web平台上来。</p>
<p> </p>
<p> </p>
<p>参考资料：</p>
<p> </p>
<p>·       <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCanvas_element" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Canvas_element" ref="nofollow noopener noreferrer">Canvas的Wiki介绍</a></p>
<p>·       <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcommunity.canvaslms.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://community.canvaslms.com/" ref="nofollow noopener noreferrer">Canvas社区</a></p>
<p>·       <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.grapecity.com.cn%2Fdeveloper%2Fspreadjs" target="_blank" rel="nofollow noopener noreferrer" title="https://www.grapecity.com.cn/developer/spreadjs" ref="nofollow noopener noreferrer">基于Canvas表格组件 SpreadJS</a></p>
<p>转载请注明出处：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.grapecity.com.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.grapecity.com.cn/" ref="nofollow noopener noreferrer">葡萄城官网</a>，葡萄城为开发者提供专业的开发工具、解决方案和服务，赋能开发者。</p></div>  
</div>
            