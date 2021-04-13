
---
title: 'Intersection Observer 完全解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc71a7a6a82e4cea871f325286cec5bc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 18:32:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc71a7a6a82e4cea871f325286cec5bc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>试想以下场景，你想让你的网站实现以下功能：</p>
<ol>
<li>当页面滚动的时候懒加载图片，异步加载图片能够提升页面响应速度，优化 UX</li>
<li>实现无限滚动（Infinite scrolling），在一个页面中不断加载新的资源，并添加到当前页面中，如此避免了页面跳转从而重复渲染，和 Vue、React 等 <code>VDOM</code> 的优化思路类似，优化 UX</li>
<li>在页面上加载广告，而服务商要求提供相应数据，只有广告进入用户视图区才算计数</li>
<li>根据用户是否要查看结果决定是否渲染一些元素或动画</li>
</ol>
<p>如果要自己实现这些功能，那么需要在 js 中轮询不断获取 target 元素的位置信息，计算是否符合相应条件，但是由于这个轮询函数是在 V8 主线程中运行的，因此资源消耗巨大，非常容易掉帧，带来非常差的用户体验。</p>
<p>与此同时，假如有一个无限滚动的网页，开发者使用了一个第三方库来管理整个页面的广告，又用了另外一个库来实现消息盒子和点赞，并且页面有很多动画（译注：动画往往意味着较高的性能消耗）。两个库都有自己的相交检测程序，都运行在主线程里，而网站的开发者对这些库的内部实现知之甚少，所以并未意识到有什么问题。但当用户滚动页面时，这些相交检测程序就会在页面滚动回调函数里不停触发调用，造成性能问题，体验效果让人失望。</p>
<p>而 Intersection Observer 正是为了解决这个问题而诞生的。</p>
<h1 data-id="heading-1">Intersection Observer 概念及用法</h1>
<p>Intersection Observer 是 W3C 提出的一种 Observer API，属于浏览器中全局可访问对象 GO，通过 Intersection Observer 能够更好地支持上诉场景，因为 Observer 并不在主线程中执行，降低了资源消耗，优化了网页性能。</p>
<p>Intersection Observer API 提供给 web 开发者，<strong>一种异步查询元素相对于其他元素或窗口位置的能力</strong>。它常用于追踪一个元素在窗口的可视问题，比如下图，滚动页面，顶部会提示绿色方块的可视性。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc71a7a6a82e4cea871f325286cec5bc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在 Intersection Observer 出来之前，<strong>传统位置计算的方式，依赖于对 DOM 状态的轮询计算，然而这种方式会在主线程里密集执行从而造成页面性能问题</strong></p>
<p>getBoundingClientRect() 的频繁调用也可能引发浏览器的样式重计算和布局。如果是在 iframe 里，因为同源策略，我们不能直接访问元素，也就很难用传统方式去处理 iframe 里的元素。</p>
<p>Intersection Observer 的设计，就是为了更方便的处理元素的可视问题。使用 Intersection Observer 我们可以很容易的监控元素进入和离开可视窗口，实现节点的预加载和延迟加载。Intersection Observer 并不是基于像素变化的实时计算，它的反馈会有一定的延时，这种异步的方式减少了对 DOM 和 style 查询的昂贵计算和持续轮询，相比传统方式降低了 CPU、GPU 的消耗。</p>
<p>Intersection Observer API 会注册一个回调函数，每当被监视的元素进入或者退出另外一个元素时(或者 viewport )，或者两个元素的相交部分大小发生变化时，该回调方法会被触发执行。这样，我们网站的主线程不需要再为了监听元素相交而辛苦劳作，浏览器会自行优化元素相交管理。</p>
<p>注意 Intersection Observer API 无法提供重叠的像素个数或者具体哪个像素重叠，他的更常见的使用方式是——当两个元素相交比例在 N% 左右时，触发回调，以执行某些逻辑。</p>
<p>Intersection Observer API 允许你配置一个回调函数，当以下情况发生时会被调用</p>
<p>每当目标(<code>target</code>)元素与设备视窗或者其他指定元素发生交集的时候执行。设备视窗或者其他元素我们称它为根元素或根(<code>root</code>)。
Observer 第一次监听目标元素的时候
通常，您需要关注文档最接近的可滚动祖先元素的交集更改，如果元素不是可滚动元素的后代，则默认为设备视窗。如果要观察相对于根(<code>root</code>)元素的交集，请指定根(<code>root</code>)元素为<code>null</code>。</p>
<p>无论您是使用视口还是其他元素作为根，API 都以相同的方式工作，只要目标元素的可见性发生变化，就会执行您提供的回调函数，以便它与所需的交叉点交叉。</p>
<p>目标(<code>target</code>)元素与根(<code>root</code>)元素之间的交叉度是交叉比(<code>intersection ratio</code>)。这是目标(<code>target</code>)元素相对于根(<code>root</code>)的交集百分比的表示，它的取值在 0.0 和 1.0 之间。</p>
<h2 data-id="heading-2">相关参数</h2>
<ol>
<li>IntersectionObserver Option</li>
</ol>
<p>创建一个 IntersectionObserver 对象，并传入相应参数和回调用函数，该回调函数将会在目标(<code>target</code>)元素和根(<code>root</code>)元素的交集大小超过阈值(<code>threshold</code>)规定的大小时候被执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> options = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#scrollArea"</span>),
  <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">"0px"</span>,
  <span class="hljs-attr">threshold</span>: <span class="hljs-number">1.0</span>,
&#125;

<span class="hljs-keyword">let</span> observer = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>阈值为 1.0 意味着目标元素完全出现在 root 选项指定的元素中可见时，回调函数将会被执行。</p>
<p>可选参数：</p>
<ul>
<li><code>root</code>: 指定根(<code>root</code>)元素，用于检查目标的可见性。必须是目标元素的父级元素。如果未指定或者为<code>null</code>，则默认为浏览器视窗。</li>
<li><code>rootMargin</code>: 根(<code>root</code>)元素的外边距。类似于 CSS 中的 margin 属性，比如 "10px 20px 30px 40px" (top, right, bottom, left)。如果有指定 root 参数，则 rootMargin 也可以使用百分比来取值。该属性值是用作 root 元素和 target 发生交集时候的计算交集的区域范围，使用该属性可以控制 root 元素每一边的收缩或者扩张。默认值为 0。</li>
<li><code>threshold</code>: 可以是单一的 number 也可以是 number 数组，target 元素和 root 元素相交程度达到该值的时候 IntersectionObserver 注册的回调函数将会被执行。如果你只是想要探测当 target 元素的在 root 元素中的可见性超过 50%的时候，你可以指定该属性值为 0.5。如果你想要 target 元素在 root 元素的可见程度每多 25%就执行一次回调，那么你可以指定一个数组[0, 0.25, 0.5, 0.75, 1]。默认值是 0(意味着只要有一个 target 像素出现在 root 元素中，回调函数将会被执行)。该值为 1.0 含义是当 target 完全出现在 root 元素中时候 回调才会被执行。</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23379b6b97574959b9a0ce301fae5525~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>IntersectionObserver Entry</li>
</ol>
<p>IntersectionObserverEntry 对象提供了目标元素与跟元素相交的详细信息。他有如下几个属性。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IntersectionObserverEntry &#123;
  <span class="hljs-keyword">readonly</span> attribute DOMHighResTimeStamp time;
  <span class="hljs-keyword">readonly</span> attribute DOMRectReadOnly? rootBounds;
  <span class="hljs-keyword">readonly</span> attribute DOMRectReadOnly boundingClientRect;
  <span class="hljs-keyword">readonly</span> attribute DOMRectReadOnly intersectionRect;
  <span class="hljs-keyword">readonly</span> attribute <span class="hljs-built_in">boolean</span> isIntersecting;
  <span class="hljs-keyword">readonly</span> attribute double intersectionRatio;
  <span class="hljs-keyword">readonly</span> attribute Element target;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f356bfc652f4b3eb6c72414a082bcea~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>time：发生相交到相应的时间，毫秒。</li>
<li>rootBounds：根元素矩形区域的信息，如果没有设置根元素则返回 null，图中蓝色部分区域。</li>
<li>boundingClientRect：目标元素的矩形区域的信息，图中黑色边框的区域。</li>
<li>intersectionRect：目标元素与视口（或根元素）的交叉区域的信息，图中蓝色方块和粉红色方块相交的区域。</li>
<li>isIntersecting：目标元素与根元素是否相交</li>
<li>intersectionRatio：目标元素与视口（或根元素）的相交比例。</li>
<li>target：目标元素，图中黑色边框的部分。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义相交监视器</span>
<span class="hljs-keyword">var</span> observer = <span class="hljs-keyword">new</span> IntersectionObserver(<span class="hljs-function">(<span class="hljs-params">changes</span>) =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> change <span class="hljs-keyword">of</span> changes) &#123;
    <span class="hljs-built_in">console</span>.log(change.time) <span class="hljs-comment">// 发生变化的时间</span>
    <span class="hljs-built_in">console</span>.log(change.rootBounds) <span class="hljs-comment">// 根元素的矩形区域的信息</span>
    <span class="hljs-built_in">console</span>.log(change.boundingClientRect) <span class="hljs-comment">// 目标元素的矩形区域的信息</span>
    <span class="hljs-built_in">console</span>.log(change.isIntersection) <span class="hljs-comment">// 目标元素与视口（或根元素）是否相交</span>
    <span class="hljs-built_in">console</span>.log(change.intersectionRect) <span class="hljs-comment">// 目标元素与视口（或根元素）的交叉区域的信息</span>
    <span class="hljs-built_in">console</span>.log(change.intersectionRatio) <span class="hljs-comment">// 目标元素与视口（或根元素）的相交比例</span>
    <span class="hljs-built_in">console</span>.log(change.target) <span class="hljs-comment">// 被观察的目标元素</span>
  &#125;
&#125;, &#123;&#125;)

<span class="hljs-comment">// 开始观察某个目标元素</span>
observer.observe(target)

<span class="hljs-comment">// 停止观察某个目标元素</span>
observer.unobserve(target)

<span class="hljs-comment">// 关闭监视器</span>
observer.disconnect()

<span class="hljs-comment">// 获取所有 IntersectionObserver 观察的 targets</span>
observer.takeRecords()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请留意，你注册的回调函数将会在主线程中被执行。所以该函数执行速度要尽可能的快。如果有一些耗时的操作需要执行，建议使用 <code>Window.requestIdleCallback()</code> 方法。</p>


<p>所有区域均被 Intersection Observer API 当做一个矩形看待。如果元素是不规则的图形也将会被看成一个包含元素所有区域的最小矩形，相似的，如果元素发生的交集部分不是一个矩形，那么也会被看作是一个包含他所有交集区域的最小矩形。</p>
<p>这个有助于理解 IntersectionObserverEntry 的属性，IntersectionObserverEntry 用于描述 <code>target</code> 和 <code>root</code> 的交集。</p>
<h2 data-id="heading-3">The intersection root and root margin</h2>
<p>在我们开始跟踪 <code>target</code> 元素和容器元素之前，我们要先知道什么是容器(<code>root</code>)元素。容器元素又称为 <strong>intersection root</strong>, 或 <strong>root element</strong>.这个既可以是 <code>target</code> 元素祖先元素也可以是指定 <code>null</code> 则使用浏览器视口做为容器(<code>root</code>)。</p>
<p>用作描述 intersection <code>root</code> 元素边界的矩形可以使用 <code>root</code> margin 来调整矩形大小，即 <code>root</code>Margin 属性，在我们创建 IntersectionObserver 对象的时候使用。<code>root</code>Margin 的属性值将会做为 margin 偏移值添加到 intersection <code>root</code> 元素的对应的 margin 位置，并最终形成 <code>root</code> 元素的矩形边界。</p>
<h2 data-id="heading-4">Thresholds</h2>
<p>IntersectionObserver API 并不会每次在元素的交集发生变化的时候都会执行回调。相反它使用了 thresholds 参数。当你创建一个 observer 的时候，你可以提供一个或者多个 number 类型的数值用来表示 <code>target</code> 元素在 <code>root</code> 元素的可见程序的百分比，然后，API 的回调函数只会在元素达到 thresholds 规定的阈值时才会执行。</p>
<p>例如，当你想要在 <code>target</code> 在 <code>root</code> 元素中中的可见性每超过 25% 或者减少 25% 的时候都通知一次。你可以在创建 observer 的时候指定 thresholds 属性值为[0, 0.25, 0.5, 0.75, 1]，你可以通过检测在每次交集发生变化的时候的都会传递回调函数的参数"IntersectionObserverEntry.isIntersecting"的属性值来判断 <code>target</code> 元素在 <code>root</code> 元素中的可见性是否发生变化。如果 isIntersecting 是 true，<code>target</code> 元素的至少已经达到 thresholds 属性值当中规定的其中一个阈值，如果是 false，<code>target</code> 元素不在给定的阈值范围内可见。</p>
<p>为了让我们感受下 thresholds 是如何工作的，尝试滚动以下的例子，每一个 colored box 的四个边角都会展示自身在 <code>root</code> 元素中的可见程度百分比，所以在你滚动 <code>root</code> 的时候你将会看到四个边角的数值一直在发生变化。每一个 box 都有不同的 thresholds：</p>

<ul>
<li>第一个 box 的 thresholds 属性值 [0.00, 0.01, 0.02, ..., 0.99, 1.00].</li>
<li>第二个 box 只有唯一的值 [0.5].</li>
<li>第三个 box thresholds 按 10%从 0 递增(0%, 10%, 20%, etc.).</li>
<li>最后一个 box [0, 0.25, 0.5, 0.75, 1.0]</li>
</ul>
<h1 data-id="heading-5">实现原理</h1>
<h2 data-id="heading-6">异步机制</h2>
<p>没有找到 Chrome 或 V8 对 Intersection Observer 的文档或 blog 说明，UP 就找到 W3C 的规范文档，算是了解了 Intersection Observer 的实现原理，为何相比与 js 中轮询能够有效降低开销。</p>
<p>规范文档中更多是详细的 IDL 以及开发流程定义（包括如何创建 Intersection Object，放入队列，Notify Observer 的过程等等），大部分没太多可说的，主要核心在 <a href="https://www.w3.org/TR/intersection-observer/#update-intersection-observations-algo" target="_blank" rel="nofollow noopener noreferrer">3.2.8. Run the Update Intersection Observations Steps</a> 以及 <a href="https://www.w3.org/TR/intersection-observer/#external-spec-integrations" target="_blank" rel="nofollow noopener noreferrer">3.4 External Spec Integrations</a>,</p>
<p>首先关于每次循环中 Processing Model 如何处理所有 Intersection Observer，主要分为以下几步：</p>
<ol>
<li>如果是刚初始化的 observer，赋予一些初始值：
<ul>
<li>thresholdIndex: 0</li>
<li>isIntersecting: false</li>
<li>targetRect: <code>DOMRectReadOnly</code>对象，并且 x,y,width,height 均为 0</li>
<li>intersectionRect: <code>DOMRectReadOnly</code>对象，并且 x,y,width,height 均为 0</li>
</ul>
</li>
<li>如果是触发条件的 observer，利用下文描述的 Rect Ratio 算法计算 intersectionRect</li>
<li>赋值 targetArea 和 intersectionArea 分别为 targetRect 和 intersectionRect 的范围，并根据 targetArea 和 intersectionArea 的关系得到 Entry 属性的值：
<ul>
<li>intersectionRatio</li>
<li>isIntersecting</li>
</ul>
</li>
<li>thresholdIndex 是第一个触发 observer.thresholds 比 intersectionRatio 的 entry 索引，同时还有一个<em>previousThresholdIndex</em>以及<em>previousIsIntersecting</em>记录之前 entry 的状态，如果<em>previousThresholdIndex</em> !== thresholdIndex，则更新<code>observer, time, rootBounds, targetRect, intersectionRect, isIntersecting, target</code>所有属性.</li>
</ol>
<p>以上是处理所有 Observer 的主体循环，接下来是这个循环在浏览器引擎的什么时候执行呢？</p>
<blockquote>
<p>An Intersection Observer processing step should take place during the "Update the rendering" steps, after step 12, run the animation frame callbacks, in the in the HTML Processing Model.</p>
</blockquote>
<blockquote>
<p>This step is:</p>
</blockquote>
<blockquote>
<p>13.For each fully active document in docs, Run the update intersection observations steps for that document, passing in now as the timestamp.</p>
</blockquote>
<p>所以就是在 V8 event-loop 的更新渲染阶段之前，在动画帧回调函数执行之后，被称为<a href="https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model" target="_blank" rel="nofollow noopener noreferrer">Update the rendering</a>，UP 的理解是这个阶段处理 window 中各个容器的渲染更新，因此更适合在此阶段计算相交矩形，同时该阶段触发在异步阶段，执行频率并不高（这也是为什么滚动快的话有些中间的 <code>threshold</code> 触发不到），从而实现不阻塞主线程的同时实现监控目标元素出现的事件。根据 SOF 上一篇<a href="https://stackoverflow.com/questions/61951380/intersection-observer-fails-sometimes-when-i-scroll-fast" target="_blank" rel="nofollow noopener noreferrer">优质回答</a>上提到，Intersection Observer 触发频率已经很高了（60fps for most devices, or once every 16.66 miliseconds），这样的频率虽然不如主线程轮询，但对用户来说大部分时候是感知不到的，适合绝大部分的场景需求，但是如果这样的频率还不能满足一些高速 (high-velocity) 的应用场景，那么可以考虑采用以下思路：</p>
<ol>
<li>利用 setTimeout 修改 intersection Observer 的 callback</li>
<li>利用节流和 CSS 中 scrollTop 处理 wheel 事件</li>
<li>实现自定义的 intersection 检测</li>
</ol>
<p>这里就不再展开了</p>
<h2 data-id="heading-7">Rect Ratio 计算</h2>
<p>首先了解 intersection rectangle 是如何计算的（MDN 原文）：</p>
<blockquote>
<ol>
<li>The target element's bounding rectangle (that is, the smallest rectangle that fully encloses the bounding boxes of every component that makes up the element) is obtained by calling <code>getBoundingClientRect()</code> on the target. This is the largest the intersection rectangle may be. The remaining steps will remove any portions that don't intersect.</li>
<li>Starting at the target's immediate parent block and moving outward, each containing block's clipping (if any) is applied to the intersection rectangle. A block's clipping is determined based on the intersection of the two blocks and the clipping mode (if any) specified by the <code>overflow</code> property. Setting overflow to anything but <code>visible</code> causes clipping to occur.</li>
<li>If one of the containing elements is the root of a nested browsing context (such as the document contained in an <code><iframe></code>, the intersection rectangle is clipped to the containing context's viewport, and recursion upward through the containers continues with the container's containing block. So if the top level of an <code><iframe></code> is reached, the intersection rectangle is clipped to the frame's viewport, then the frame's parent element is the next block recursed through toward the intersection root.</li>
<li>When recursion upward reaches the intersection root, the resulting rectangle is mapped to the intersection root's coordinate space.</li>
<li>The resulting rectangle is then updated by intersecting it with the root intersection rectangle.</li>
<li>This rectangle is, finally, mapped to the coordinate space of the target's document.</li>
</ol>
</blockquote>
<p>简要说就是通过 <code>getBoundingClientRect()</code> 获取 <code>target</code> 的最小覆盖矩形，然后通过 <code>overflow</code> 获取 <code>target</code> 与根容器同样的矩形区域的交线，从而来计算 ratio，要注意如果有内嵌上下文，例如<code><iframe></code>时，上下文可视区域的边界也会被视为交线。</p>
<h1 data-id="heading-8">Intersection Observer v2</h1>
<p>看到一名 Google 的员工 po 了一篇 <a href="https://web.dev/intersectionobserver-v2/" target="_blank" rel="nofollow noopener noreferrer">blog</a>，提到了 Intersection observer v2 的提案，因为目前的 v1 仅仅会告诉你目标元素滚动到窗口的视图中了，但是不会告诉你目标元素是否被页面上其他元素覆盖，或该元素是否有一些 CSS 属性例如 <code>transform, opacity, filter</code> 等可能导致元素不可见的属性，可以想到，这个问题应该是源于广告追踪。</p>
<p>对于根文档（Document）中的元素，可以通过 <code>DocumentOrShadowRoot.elementFromPoint()</code> 来确定上述信息，但是如果位于第三方的 <code>iframe</code> 中，则无法获取这些信息。</p>
<p>Intersection Observer v2 引入了跟踪目标元素的实际“可见性”的概念，就像人类定义的那样。通过在 IntersectionObserver 构造函数中设置一个选项，相交的 IntersectionObserverEntry 实例将包含一个名为的新布尔字段 isVisible。甲 true 对于值 isVisible 是从底层实现了有力的保证，所述目标元件是由其他内容完全未被遮挡和不具有视觉效果应用将改变或扭曲在屏幕上的显示。相反，false 值意味着实现无法做出保证。</p>
<p>在一个重要的细节规范是实施允许上报假阴性（即设置 isVisible 到 false 即使目标元素是完全可见的和未改性）。出于性能或其他原因，浏览器仅限于使用边界框和直线几何体。他们不会尝试针对进行修改，以达到像素完美的效果 border-radius。</p>
<p>也就是说，在任何情况下都不允许出现误报（即，设置为目标元素不完全可见且未修改的时间）。<code>isVisible</code> <code>true</code></p>
<p>**警告**：可见性比交集要昂贵得多。因此，Intersection Observer v2不能像Intersection
  Observer v1那样广泛使用。Intersection Observer
  v2专注于打击欺诈，仅在需要可见性信息且Intersection Observer
  v1功能不足时才应使用。</p>
<h2 data-id="heading-9">新代码在实际中是什么样的？</h2>
<p>该 IntersectionObserver 构造函数现在只需两个额外的配置属性：delay 和 trackVisibility。的 delay 是一个数字，指示以毫秒为单位通知之间从观察者对于给定的目标的最小延迟。该 trackVisibility 是表示观察者是否会跟踪目标的可见性更改一个布尔值。</p>
<p>重要的是在这里要注意，当 trackVisibilityis 时 true，delay 必须至少是 100（即每 100 毫秒通知不超过一个）。如前所述，可见性的计算成本很高，并且此要求是防止性能下降和电池消耗的预防措施。负责任的开发人员将使用最大可容忍的延迟值。</p>
<p>根据当前规范，可见性计算如下：</p>
<ul>
<li>
<p>如果观察者的 trackVisibility 属性为 false，则该目标被视为可见。这对应于当前的 v1 行为。</p>
</li>
<li>
<p>如果目标具有 2D 平移或成比例的 2D 缩放以外的有效转换矩阵，则该目标被视为不可见。</p>
</li>
<li>
<p>如果目标或其包含的区块链中的任何元素的有效不透明度为 1.0，则该目标被视为不可见。</p>
</li>
<li>
<p>如果目标或其包含的块链中的任何元素应用了任何过滤器，则该目标被视为不可见。</p>
</li>
<li>
<p>如果实现不能保证目标完全不被其他页面内容所遮挡，则该目标被认为是不可见的。</p>
</li>
</ul>
<p>这意味着当前的实现在保证可见性的前提下非常保守。例如，应用几乎不引人注意的灰度滤镜 filter: grayscale(0.01%)或将设置为几乎不可见的透明度 opacity: 0.99 都会使元素不可见。</p>
<p>下面是一个简短的代码示例，说明了新的 API 功能。您可以在演示的第二部分中看到其点击跟踪逻辑的运行情况（但现在，尝试“观看”小狗视频）。请确保再次激活“技巧模式”，以立即将自己转变为一个黑幕发布者，并查看 Intersection Observer v2 如何防止跟踪非合法广告点击。这次，Intersection Observer v2 支持了我们！🎉</p>
<h1 data-id="heading-10">React.lazy</h1>
<p>在 React 中实现无线滑动以及图片懒加载可以考虑使用 React.lazy，配合 useCallback, useReducer 和 Intersection Observer 实现相应的功能，具体可以查看<a href="https://www.smashingmagazine.com/2020/03/infinite-scroll-lazy-image-loading-react/#top" target="_blank" rel="nofollow noopener noreferrer">blog</a></p>
<h1 data-id="heading-11">兼容性</h1>
<p>IntersectionObserver 目前除了 IE 和 OperaMini，已经被主流的浏览器支持。我们可以使用渐进支持的方式使用它。对于目前浏览器的生态，我们也要做好向下降级的措施。
我们也可以使用 IntersectionObserver polyfill 增加浏览器的兼容，具体可以查看 polyfill.io。</p>
<p><a href="https://caniuse.com/?search=Intersection" target="_blank" rel="nofollow noopener noreferrer">兼容性详情</a></p>
<h1 data-id="heading-12">参考链接</h1>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API" target="_blank" rel="nofollow noopener noreferrer">MDN Intersection Observer</a></li>
<li><a href="https://www.w3.org/TR/intersection-observer/#event-loop" target="_blank" rel="nofollow noopener noreferrer">W3C Event-Loop</a></li>
<li><a href="https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model" target="_blank" rel="nofollow noopener noreferrer">html sepc event-loop-processing-model</a></li>
<li><a href="https://stackoverflow.com/questions/61951380/intersection-observer-fails-sometimes-when-i-scroll-fast" target="_blank" rel="nofollow noopener noreferrer">Intersection Observer fails sometimes when i scroll fast
</a></li>
<li><a href="https://juejin.cn/post/6844903927419256846" target="_blank">深入理解 Intersection Observer</a></li>
<li><a href="https://www.smashingmagazine.com/2020/03/infinite-scroll-lazy-image-loading-react/#top" target="_blank" rel="nofollow noopener noreferrer">React implement infinity scrolling and lazy load image</a></li>
</ul>
<p>分享我私藏的TS教程，从0到高阶全系列，点击链接，0元获取
<a href="https://www.yidengxuetang.com/pub-page/index.html" target="_blank" rel="nofollow noopener noreferrer">www.yidengxuetang.com/pub-page/in…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            