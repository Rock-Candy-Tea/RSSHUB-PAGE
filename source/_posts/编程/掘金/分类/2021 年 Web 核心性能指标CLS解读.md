
---
title: '2021 年 Web 核心性能指标CLS解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a8203f423414595bb988899f7a1c2f7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 03:54:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a8203f423414595bb988899f7a1c2f7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>累计布局位移（CLS）是衡量用户视觉稳定性的一项重要的以用户为中心的度量标准，因为它有助于量化用户打开页面时，页面布局变化的频率。目前官方建议这个指标应该小于 0.1，这样的 CLS 有助于确保页面的用户体验。</p>
</blockquote>
<p>试想一下这样的场景，你想要点击一个链接或一个按钮，但是在手指落下的瞬间（BOOM），链接移动了，您最终点击了其他东西！这样的体验是不是糟糕透了？比如如下例子：</p>
<p>页面布局的变动通常是由于异步加载的资源或将DOM元素动态添加到现有内容上方的页面而发生的。罪魁祸首可能是尺寸未知的图像或视频，或者是动态调整自身大小的第三方广告或小部件等。</p>
<p>解决这个问题的难点在于，网站在开发中的功能通常与用户的体验有很大不同。个性化或第三方内容在开发环境中和在生产中的表现不尽相同，开发时的图片等资源通常已经存在于开发者的浏览器缓存中，并且在本地的API调用通常很快，所以延迟不明显。</p>
<p>而，累计布局位移（CLS）度量标准可通过测量实际用户发生变化的频率来帮助你发现这类问题。</p>
<h3 data-id="heading-0">什么是CLS？</h3>
<p>CLS是测量在页面整个生命周期中发生的每个元素布局变化的分数总和。</p>
<p>布局移动由<code>Layout Instability API</code>定义，该API定义在视口中可见的元素在两渲染帧之间更改其开始位置时，这些元素被认为是不稳定元素。</p>
<p>请注意，仅当现有元素更改其起始位置时，才会发生布局移动。如果将新元素添加到DOM或现有元素更改了大小，则只要更改不会导致其他可见元素更改其开始位置，该元素就不会算作布局偏移。</p>
<h3 data-id="heading-1">良好的CLS分数是多少？</h3>
<p>为了提供良好的用户体验，网站应努力使CLS得分不超过0.1。为确保大多数用户达到这一目标，可以用移动设备和台式机设备有75%的页面得分符合要求即为合格作为基本标准。</p>
<blockquote>
<p>要了解有关此建议背后的研究和方法的更多信息，请参阅：定义核心Web Vitals(<a href="https://web.dev/defining-core-web-vitals-thresholds/)%E6%8C%87%E6%A0%87%E9%98%88%E5%80%BC" target="_blank" rel="nofollow noopener noreferrer">web.dev/defining-co…</a></p>
</blockquote>
<h3 data-id="heading-2">影响分数</h3>
<p>要计算布局变化分数，浏览器将查看视口大小以及两个渲染帧之间视口中不稳定元素的移动。布局偏移分数是该运动的两个度量的乘积：<code>冲击分数</code>和<code>距离分数</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"> layout shift score = impact fraction * distance fraction
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>冲击分数</strong></p>
<p><code>冲击分数</code>衡量的是变动元素在两渲染帧之间对页面视口的影响。前一帧和当前帧的所有不稳定元素的可见区域的并集（作为视口总面积的一部分）是当前帧的影响分数。
// 图</p>
<p>在上图中，有一个元素在一帧中占据了视口的一半。然后，在下一帧中，元素下移视口高度的25％。红色的虚线矩形表示两个帧中元素的可见区域的并集，在这种情况下，其为总视口的75％，因此其影响分数为0.75。</p>
<p><strong>距离分数</strong>
<code>距离分数</code>是不稳定元素在视口中移动的最大距离(水平或垂直)除以视口的最大尺寸(宽度或高度，取较大的)。
// 图
在上面的例子中，最大的视口尺寸是高度，不稳定元素移动了视口高度的25%，这使得距离分数为0.25。</p>
<p>所以，在这个例子中，影响分数是0.75，距离分数是0.25，所以布局移位分数是0.75 * 0.25 = 0.1875。</p>
<h4 data-id="heading-3">向现有元素添加内容如何影响布局移位分数</h4>
<p>// 图
图中"Click Me!"按钮被添加到带有黑色文本的灰色框的底部，它将带有白色文本的绿色框向下推(并部分推出视口)。</p>
<p>在这个例子中，灰色框改变了大小，但是它的起始位置没有改变，所以它不是一个不稳定的元素。按钮以前并不在DOM中，因此它的起始位置也不会改变。</p>
<p>然而，绿色方块的起始位置确实会发生变化，但由于它已经部分移出了视口，所以在计算冲击分数时，不可见区域并不会被考虑在内。两个帧中绿色框的可视区域(用红色虚线矩形表示)的联合与第一个帧中50%视口的绿色框的区域相同。冲击分数为0.5。</p>
<p>距离分数用紫色箭头表示。绿框已经向下移动了大约14%的视口，所以距离分数是0.14。</p>
<p>布局位移得分为0.5 x 0.14 = 0.07。</p>
<h4 data-id="heading-4">多个不稳定元素</h4>
<p>// 图
在上面的第一帧中，有一个动物的API请求的四个结果，按字母顺序排序。在第二帧中，更多的结果被添加到排序列表中。</p>
<p>列表中的第一项("Cat")不会在帧之间改变它的起始位置，所以它是稳定的。类似地，添加到列表中的新项以前并不在DOM中，因此它们的起始位置也不会改变。但标有"狗"、"马"和"斑马"的物品都改变了它们的起始位置，使它们成为不稳定的元素。</p>
<p>红色的虚线矩形再次代表这三个不稳定元素的前后区域的结合，在这个例子中大约是视口区域的38%(撞击率为0.38)。</p>
<p>箭头表示不稳定元素从起始位置移动的距离。用蓝色箭头表示的"斑马"元素移动得最多，移动了视口高度的30%左右。这个例子中的距离分数是0.3。</p>
<p>布局位移分数是0.38 x 0.3 = 0.1172。</p>
<h3 data-id="heading-5">预期 VS 意外的布局变化</h3>
<p>并不是所有的布局变化都是不好的。事实上，许多动态web应用程序经常改变页面上元素的起始位置。</p>
<p>只有在用户非预期的情况下，布局的改变才是糟糕的。另外，在响应用户交互时(点击一个链接，按下一个按钮，输入一个搜索框等等)出现的布局变化通常是好的，只要这种变化发生在距离交互足够近的地方，用户能够清楚地看到这种关系。</p>
<p>动画和过渡是更新页面内容的好方法，不会让用户感到意外。页面上突然移动内容几乎总是会造成糟糕的用户体验。但是，从一个位置逐渐自然地移动到另一个位置的内容通常可以帮助用户更好地理解发生了什么。</p>
<p><code>CSS transform</code>属性允许你在不触发布局移位的情况下动画元素，比如使用<code>transform: scale()</code>代替改变高度和宽度属性。要移动元素，请避免更改顶部、右侧、底部或左侧属性，可以使用<code>transform: translate()</code>代替。</p>
<h3 data-id="heading-6">如何衡量CLS</h3>
<p>1、可以使用lighthouse和performce检测CLS。
// 图
2、手动测量
可以使用布局不稳定性API。创建一个PerformanceObserver，该observer侦听意外的布局移动元素，将它们累加，并将它们记录到控制台。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> cls = <span class="hljs-number">0</span>;

<span class="hljs-keyword">new</span> PerformanceObserver(<span class="hljs-function">(<span class="hljs-params">entryList</span>) =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> entry <span class="hljs-keyword">of</span> entryList.getEntries()) &#123;
    <span class="hljs-keyword">if</span> (!entry.hadRecentInput) &#123;
      cls += entry.value;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Current CLS value:'</span>, cls, entry);
    &#125;
  &#125;
&#125;).observe(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'layout-shift'</span>, <span class="hljs-attr">buffered</span>: <span class="hljs-literal">true</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">如何改善CLS</h3>
<p>首先，最常见的影响CLS的分数的有：</p>
<ul>
<li>未指定尺寸的图片</li>
<li>未指定尺寸的广告、嵌入元素、iframe</li>
<li>动态插入内容</li>
<li>自定义字体（引发FOIT/FOUT）</li>
<li>在更新DOM之前等待网络响应的操作</li>
</ul>
<p>因此，改善方法有：</p>
<ol>
<li>最开始就设定好图片的尺寸，或者预留足够空间。这样能确保浏览器可以在加载图像时在文档中分配正确的空间量。还可以使用<code>unsize -media</code>特性策略在支持特性策略的浏览器中强制执行此行为。</li>
<li>除非响应用户交互，否则切勿在现有内容上方插入内容。这样可以确保可以预期发生任何版式移位。</li>
<li>优先使用变换动画属性而不是触发布局更改的动画属性。对过渡进行动画处理，以提供状态与状态之间的上下文和连续性。</li>
<li>web字体尽可能早的加载，避免产生FOIT和FOUT</li>
<li>与UI同事配合在交互上避免布局偏移</li>
</ol>
<p>说明：本文大部分内容翻译自文章 <a href="https://web.dev/cls/" target="_blank" rel="nofollow noopener noreferrer">web.dev/cls/</a></p>
<h3 data-id="heading-8">参考资料</h3>
<ul>
<li><a href="https://web.dev/cls/" target="_blank" rel="nofollow noopener noreferrer">web.dev/cls/</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/207163394" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/207163394</a></li>
<li><a href="https://web.dev/optimize-cls/" target="_blank" rel="nofollow noopener noreferrer">web.dev/optimize-cl…</a></li>
<li><a href="https://developers.google.com/publisher-tag/guides/minimize-layout-shift" target="_blank" rel="nofollow noopener noreferrer">developers.google.com/publisher-t…</a></li>
</ul>
<h3 data-id="heading-9">最后</h3>
<ul>
<li>欢迎加我微信(winty230)，拉你进技术群，长期交流学习...</li>
<li>欢迎关注「前端Q」,认真学前端，做个有专业的技术人...</li>
</ul>
<p><img alt="GitHub" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a8203f423414595bb988899f7a1c2f7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            