
---
title: '如何使用Lighthouse性能检测工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/134180f910bf46019ceb8e71e57c1c54~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 19:51:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/134180f910bf46019ceb8e71e57c1c54~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近做性能检测工具，很多知识点不清楚，打算查缺补漏，补一补。</p>
<p>接下来从官方提供的性能检测工具Lighthouse(灯塔)开始我们的学习，简单介绍了下Lighthouse的一些点。</p>
<p>阅读完本文，你可以了解到</p>
<ul>
<li>Lighthouse 是什么。</li>
<li>如何快速上手Lighthouse (使用入门)。</li>
<li>Lighthouse中的一些Metrics指标。</li>
</ul>
<p>性能相关的总结准备搞个思维导图，可以<a href="https://docs.qq.com/mind/DWnljWm52eEVjWWNE" target="_blank" rel="nofollow noopener noreferrer">点这里</a>:</p>
<blockquote>
<p><a href="https://docs.qq.com/mind/DWnljWm52eEVjWWNE" target="_blank" rel="nofollow noopener noreferrer">docs.qq.com/mind/DWnljW…</a></p>
</blockquote>
<h2 data-id="heading-1">Lighthouse 是什么</h2>
<p>官方对它的解读:</p>
<blockquote>
<p><a href="https://github.com/GoogleChrome/lighthouse" target="_blank" rel="nofollow noopener noreferrer">Lighthouse</a> 是一个开源的自动化工具，用于改进网络应用的质量。 您可以将其作为一个 Chrome 扩展程序运行，或从命令行运行。 您为 Lighthouse 提供一个您要审查的网址，它将针对此页面运行一连串的测试，然后生成一个有关页面性能的报告。</p>
</blockquote>
<p>它是如何工作的呢？</p>
<p>如果你跟我一样，翻过它的代码，看过它的介绍肯定很懵逼，它的代码依赖性如下:</p>
<p><img alt="lighthouse内部模块依赖.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/134180f910bf46019ceb8e71e57c1c54~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>感兴趣的可以看看它的仓库，参考链接已经给出。</p>
<blockquote>
<p><a href="https://github.com/GoogleChrome/lighthouse" target="_blank" rel="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p>
</blockquote>
<h2 data-id="heading-2">使用入门</h2>
<p>运行 Lighthouse 的方式有两种: 作为 Chrome 扩展程序运行，或作为命令行工具运行。 Chrome 扩展程序提供了一个对用户更友好的界面，方便读取报告。 命令行工具允许您将 Lighthouse 集成到持续集成系统。</p>
<h3 data-id="heading-3">Chrome 扩展程序</h3>
<p>下载 Google Chrome 52 或更高版本。</p>
<p>安装 <a href="https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk" target="_blank" rel="nofollow noopener noreferrer">Lighthouse Chrome 扩展程序</a>。</p>
<blockquote>
<p>地址:<a href="https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk" target="_blank" rel="nofollow noopener noreferrer">chrome.google.com/webstore/de…</a></p>
</blockquote>
<p>点击 <strong>Generate report</strong> 按钮以针对当前打开的页面运行 Lighthouse 测试。</p>
<h3 data-id="heading-4">命令行工具</h3>
<p>Node CLI在配置和报告Lighthouse运行情况方面提供了最大的灵活性。如果用户需要更多的高级功能，或者想自动运行Lighthouse，可以使用Node CLI。安装 Lighthouse 作为一个全局节点模块。</p>
<p>安装:</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g lighthouse
<span class="hljs-comment"># or use yarn:</span>
<span class="hljs-comment"># yarn global add lighthouse</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>针对一个页面运行 Lighthouse 审查。</p>
<pre><code class="hljs language-bash copyable" lang="bash">lighthouse https://www.example.com --view
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传递 <code>--help</code> 标志以查看可用的输入和输出选项。</p>
<pre><code class="hljs language-bash copyable" lang="bash">lighthouse --<span class="hljs-built_in">help</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于一些options不清楚的，可以点击这个链接:</p>
<blockquote>
<p><a href="https://github.com/GoogleChrome/lighthouse#cli-options" target="_blank" rel="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p>
</blockquote>
<p>假设我们审查后，就会有这么一个结果:</p>
<p><img alt="light-metrics.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb85726649d34805a36742eeeb88d8d8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到一共6个Metrics，Lighthouse 6.0在报告中引入了三个新指标。其中两个新的指标--最大内容画（LCP）和累积布局偏移（CLS）--是Core Web Vitals的实验室实现。</p>
<p>那么接下来，我们看看这些Metrics指标的含义。</p>
<h2 data-id="heading-5">几个Metrics指标</h2>
<h3 data-id="heading-6">First Contentful Paint (FCP)</h3>
<p>第一次内容丰富的绘画(FCP)指标衡量了从页面开始加载到页面内容的任何部分呈现在屏幕上的时间。对于该指标，"内容 "指的是文本、图像（包括背景图像）、元素或非白色元素。</p>
<p><img alt="lighthouse-fcp.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8401aa9ee484d7186f5de6ea3308f57~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在上面的负载时间线中，FCP发生在第二帧中，就像呈现给屏幕的第一文本和图像元素时一样。</p>
<p>你会注意到，虽然部分内容已经呈现，但并非所有内容都已呈现。这是First Contentful Paint (FCP)和Largest Contentful Paint (LCP)之间的一个重要区别--LCP的目的是衡量页面的主要内容何时完成加载。</p>
<p>知道了概念，如何衡量FCP呢，我们可以接触的有<strong>Field tools</strong>和<strong>Lab tools</strong></p>
<p>要在JavaScript中测量FCP，你可以使用Paint Timing API。下面的例子展示了如何创建一个PerformanceObserver，该PerformanceObserver监听名称为first-contentful-paint的油漆条目，并将其记录到控制台。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> PerformanceObserver(<span class="hljs-function">(<span class="hljs-params">entryList</span>) =></span> &#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> entry <span class="hljs-keyword">of</span> entryList.getEntriesByName(<span class="hljs-string">'first-contentful-paint'</span>)) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'FCP candidate:'</span>, entry.startTime, entry);
  &#125;
&#125;).observe(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'paint'</span>, <span class="hljs-attr">buffered</span>: <span class="hljs-literal">true</span>&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Speed Index</h3>
<p>速度指数是Lighthouse报告中性能部分跟踪的六个指标之一。每项指标都能反映出页面加载速度的某些方面。</p>
<p>那么它是如何检测的呢？</p>
<blockquote>
<p>速度指数衡量的是内容在页面加载过程中的视觉显示速度。Lighthouse首先会在浏览器中捕获一段页面加载的视频，并计算出各帧之间的视觉进度。然后，Lighthouse使用Speedline Node.js模块来生成速度指数得分。</p>
</blockquote>
<p>至于具体的计算，可以参考GitHub里面的代码，这里就不展开了。</p>
<p>那么我们有机会提升它的性能吗？</p>
<p>利用Lighthouse报告中的 "<strong>Opportunities</strong> "部分来确定哪些改进对你的页面最有价值。机会越重要，对性能评分的影响就越大。例如，下面的Lighthouse截图显示，消除渲染阻塞资源将带来最大的改善。</p>
<p><img alt="lighthouse-speedindex.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af5279e1bb4643f9aec3b9e13f6605bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">Largest Contentful Paint (LCP)</h3>
<p>最大内容画（LCP）指标报告了在视口中可见的最大图像或文本块的渲染时间，相对于页面首次开始加载的时间。</p>
<p><img alt="light-lcp.svg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fe34160f7344500b6527912c2d5723b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从图上也能看出来，为了提供良好的用户体验，网站应该努力使最大内容画幅达到2.5秒或更少。</p>
<p>更多信息，请观看Paul Irish对LCP的深度剖析。</p>
<blockquote>
<p><a href="https://www.youtube.com/watch?v=diAc65p15ag" target="_blank" rel="nofollow noopener noreferrer">www.youtube.com/watch?v=diA…</a></p>
</blockquote>
<h3 data-id="heading-9">Cumulative Layout Shift (CLS)</h3>
<p>官方对它的解释:</p>
<blockquote>
<p>Cumulative Layout Shift (CLS)是一种视觉稳定性的测量方法，它量化了页面内容在视觉上的移动程度。它量化了一个页面的内容在视觉上移动的程度。</p>
</blockquote>
<p>简单理解就是:</p>
<p>CLS测量的是整个页面生命周期内发生的每一次意外布局转变的所有单个布局转变得分的总和。</p>
<p>布局偏移发生在可见元素从一个渲染帧到下一个渲染帧改变其位置的任何时候。关于如何计算单个布局偏移分数，请参见下文）。</p>
<blockquote>
<p><a href="https://web.dev/cls/" target="_blank" rel="nofollow noopener noreferrer">web.dev/cls/</a></p>
</blockquote>
<p><img alt="lighthouse-cls.svg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f428f403b344e69baabcef5434adb18~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面的图来看，CLS得分低是给开发者的一个信号，表明他们的用户没有经历不必要的内容移动；CLS得分低于0.10被认为是 "好"。</p>
<h3 data-id="heading-10">Total Blocking Time (TBT)</h3>
<p>我们看看官方对它的解读：</p>
<blockquote>
<p>总阻塞时间（Total Blocking Time，TBT）量化了负载响应能力，测量了主线程被阻塞的时间长到足以阻止输入响应的总时间。TBT衡量的是第一次有内容的绘画（FCP）和交互时间（TTI）之间的总时间。它是TTI的配套指标，它为量化主线程活动带来了更多的细微差别，这些活动阻碍了用户与您的页面进行交互的能力。</p>
</blockquote>
<p>此外，TBT与核心网络生命力的现场指标First Input Delay（FID）有很好的相关性。</p>
<p>需要更多的了解，可以参考链接:</p>
<blockquote>
<p><a href="https://web.dev/tbt/" target="_blank" rel="nofollow noopener noreferrer">web.dev/tbt/</a></p>
</blockquote>
<h3 data-id="heading-11">最新评分标准</h3>
<p>Lighthouse中的性能得分是由多个指标加权混合计算出来的，总结出一个页面的速度。6.0的性能得分公式如下。</p>








































<table><thead><tr><th align="left"><strong>Phase</strong></th><th align="left"><strong>Metric Name</strong></th><th align="left"><strong>Metric Weight</strong></th></tr></thead><tbody><tr><td align="left">Early (15%)</td><td align="left">First Contentful Paint (FCP)</td><td align="left">15%</td></tr><tr><td align="left">Mid (40%)</td><td align="left">Speed Index (SI)</td><td align="left">15%</td></tr><tr><td align="left"></td><td align="left">Largest Contentful Paint (LCP)</td><td align="left">25%</td></tr><tr><td align="left">Late (15%)</td><td align="left">Time To Interactive (TTI)</td><td align="left">15%</td></tr><tr><td align="left">Main Thread (25%)</td><td align="left">Total Blocking Time (TBT)</td><td align="left">25%</td></tr><tr><td align="left">Predictability (5%)</td><td align="left">Cumulative Layout Shift (CLS)</td><td align="left">5%</td></tr></tbody></table>
<p>那么你是不是会跟我一样，有疑问，我们不能修改这个权重嘛，当然可以试一试:</p>
<blockquote>
<p><a href="https://googlechrome.github.io/lighthouse/scorecalc/" target="_blank" rel="nofollow noopener noreferrer">googlechrome.github.io/lighthouse/…</a></p>
</blockquote>
<p>点击上面的链接，会展示这个一个画面:</p>
<p><img alt="lighthouse-Scoring-calculator.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5272b1ec14c44293ba2537b660c23e0f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个网站发布了一个评分计算器，帮助你了解性能评分。同时，该计算器还能为你提供Lighthouse 5版和6版的评分比较。当你使用Lighthouse 6.0版本进行审计时，报告中会有一个链接，链接到计算工具，并将结果填入其中。</p>
<hr>
<h2 data-id="heading-12">最后</h2>
<p>到这里，其实Lighthouse如何使用，以及一些关键的指标也做了说明，你一定会有疑问:</p>
<ul>
<li>我如何通过计算他们具体的值呢，有对应的JavaScript API？</li>
<li>既然可以通过Lighthouse来衡量性能并找到加快页面加载的机会，那么我们如何优化呢？</li>
</ul>
<p>想必看到这里，你遇到的疑惑跟之前一样，那么如何解决呢。</p>
<p>嗯，上面说的部分并没有详细的展开，剩下的部分，尝试去翻一翻官方文档，查一查资料，收获一定很大。</p>
<p>使用入门，很简单，没有难度，后续会继续梳理，思维导图在<a href="https://docs.qq.com/mind/DWnljWm52eEVjWWNE" target="_blank" rel="nofollow noopener noreferrer">这里</a>:</p>
<blockquote>
<p><a href="https://docs.qq.com/mind/DWnljWm52eEVjWWNE" target="_blank" rel="nofollow noopener noreferrer">docs.qq.com/mind/DWnljW…</a></p>
</blockquote>
<p><strong>我是TianTianUp，我们下一期见！！！</strong></p>
<h2 data-id="heading-13">参考</h2>
<p>[1] <strong>Lighthouse performance scoring</strong>: <a href="https://web.dev/performance-scoring/" target="_blank" rel="nofollow noopener noreferrer">web.dev/performance…</a></p>
<p>[2] <strong>GoogleChrome-lighthouse</strong>: <a href="https://github.com/GoogleChrome/lighthouse" target="_blank" rel="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p>
<p>[3] <strong>What's New in Lighthouse 6.0</strong>: <a href="https://web.dev/lighthouse-whats-new-6.0/" target="_blank" rel="nofollow noopener noreferrer">web.dev/lighthouse-…</a></p>
<p>[4] <strong>Measure:</strong> <a href="https://web.dev/measure/" target="_blank" rel="nofollow noopener noreferrer">web.dev/measure/</a></p>
<p>[5] <strong>How does Lighthouse work?</strong>: <a href="https://github.com/GoogleChrome/lighthouse/blob/master/docs/architecture.md" target="_blank" rel="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p>
<p>[6] <strong>Largest Contentful Paint (LCP)</strong>: <a href="https://web.dev/lcp/" target="_blank" rel="nofollow noopener noreferrer">web.dev/lcp/</a></p>
<p>[7] <strong>Total Blocking Time (TBT):</strong> <a href="https://web.dev/tbt/" target="_blank" rel="nofollow noopener noreferrer">web.dev/tbt/</a></p>
<p>[8] <strong>Cumulative Layout Shift (CLS):</strong> <a href="https://web.dev/cls/" target="_blank" rel="nofollow noopener noreferrer">web.dev/cls/</a></p>
<p>[9] <strong>First Contentful Paint (FCP):</strong> <a href="https://web.dev/fcp/" target="_blank" rel="nofollow noopener noreferrer">web.dev/fcp/</a></p>
<p>[10] <strong>Speed Index:</strong> <a href="https://web.dev/speed-index/" target="_blank" rel="nofollow noopener noreferrer">web.dev/speed-index…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            