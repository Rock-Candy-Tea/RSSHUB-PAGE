
---
title: 'Chrome Tools花式玩法（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/549389de8006493cbe153d1fbb7de379~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 04:37:45 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/549389de8006493cbe153d1fbb7de379~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>上一期Chrome Tools 传送门<a href="https://juejin.cn/post/6981710347140857870" target="_blank" title="https://juejin.cn/post/6981710347140857870">Chrome Tools花式玩法（二）</a><br>
<a href="https://juejin.cn/post/6903050346143318023" target="_blank" title="https://juejin.cn/post/6903050346143318023">字节内推</a>，加入我们，做有挑战的事</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/549389de8006493cbe153d1fbb7de379~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">Performance monitor</h1>
<p>从Chrome 64版本开始，新增了一个用于实时监控页面性能的监控器。平时我们分析页面性能的时候通常会用Performance，但它提供的是回顾性数据，而不是实时更新的数据。如果想要看实时的性能数据表现，我们就可以使用Performance monitor，像在日常工作中遇到类似内存泄漏等问题，它会是一个很不错的辅助排查问题工具</p>
<h2 data-id="heading-1"><strong>面板有哪些功能</strong></h2>
<p>左侧列表栏可以点击选择想要查看的信息，并且会在列表末尾标记出相关数据，例如CPU的使用率
右侧波形图区域为一个时间轴，实时绘制出页面加载或运行时性能的各个方面的实时视图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91646f9aa0f1482196865d47d678a143~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><strong>目前可以提供的能力</strong></h2>
<ul>
<li>CPU usage</li>
</ul>
<p>用于观察cpu的使用率</p>
<ul>
<li>JS heap size</li>
</ul>
<p>当前站点所占的内存空间大小</p>
<ul>
<li>
<p>DOM nodes</p>
</li>
<li>
<p>JavaScript event listeners</p>
</li>
</ul>
<p>可以查看有多少JavaScript事件监听被注册</p>
<ul>
<li>Documents</li>
</ul>
<p>对应memory里的Document</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/901760bbdb67494fb7287928ff113012~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Document Frames</li>
</ul>
<p>对应memory里的HTMLFrameElement (iframes、 workers)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6daface97d1c4f3395f6e53c23db54a8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Layouts / sec</li>
</ul>
<p>页面重新布局时每秒绘制的帧率</p>
<ul>
<li>Style recalcs / sec</li>
</ul>
<p>页面重新计算样式时每秒绘制的帧率</p>
<h2 data-id="heading-3">通过例子来看看实用价值</h2>
<p>代码可以看这里 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fmalyw%2Fpen%2FQOQvyz" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/malyw/pen/QOQvyz" ref="nofollow noopener noreferrer">codepen.io/malyw/pen/Q…</a>
我们直接来看对比 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcdpn.io%2Fmalyw%2Ffullpage%2FQOQvyz" target="_blank" rel="nofollow noopener noreferrer" title="https://cdpn.io/malyw/fullpage/QOQvyz" ref="nofollow noopener noreferrer">cdpn.io/malyw/fullp…</a></p>
<h1 data-id="heading-4">Javascript Profiler & Performance</h1>
<p>JavaScript Profiler 面板抓取的数据是 Performance 面板数据的一部分，官方长期目标是要移除它，所以我们这里简单略过。从Chrome 58开始，Timeline 面板被更名为 Performance。</p>
<blockquote>
<p>Kayce Basques：The long-term goal is to remove the old JavaScript CPU Profiler, and get everyone working with the new workflow.</p>
</blockquote>
<p><strong>顶部功能操作区域</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd07f908f4b04fa7a795b93cb794dc14~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">5个常用的按钮</h2>
<ul>
<li>
<p>Record 直接开始记录，不会自动停止</p>
</li>
<li>
<p>Reload 在页面刷新后重新加载时开始记录性能指标，并且会在加载完成后自动停止录制</p>
</li>
<li>
<p>Clear 清空记录</p>
</li>
<li>
<p>Load Profile 导入profile文件，Save Profile 保存profile文件</p>
</li>
</ul>
<h3 data-id="heading-6">可视化利器 Chrome Trace Viewer</h3>
<p>接着上面来看，如果选择Save Profile，这时候可以看到保存下来的Json文件，是不是很好奇它的结构呢，看看它的格式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
    &#123;
        <span class="hljs-comment">// name: 事件的名称，例如在面板中显示的</span>
        <span class="hljs-string">"name"</span>:<span class="hljs-string">"thread_name"</span>, 
        <span class="hljs-comment">// 事件分类categories，可以为一个list，用逗号进行分割</span>
        <span class="hljs-string">"cat"</span>:<span class="hljs-string">"__metadata"</span>,
        <span class="hljs-comment">// 事件类型phases，它是单个字符，根据输出事件的类型而变化，重要参数</span>
        <span class="hljs-string">"ph"</span>:<span class="hljs-string">"M"</span>,
        <span class="hljs-comment">// 事件的跟踪时间戳timestamp，粒度为微秒</span>
        <span class="hljs-string">"ts"</span>:<span class="hljs-number">0</span>,
        <span class="hljs-comment">// 事件的线程时间戳thread timestamp，粒度为微秒，可选参数</span>
        <span class="hljs-string">"tts"</span>:<span class="hljs-number">0</span>,
        <span class="hljs-comment">// 这个事件进程的编号process ID</span>
        <span class="hljs-string">"pid"</span>:<span class="hljs-number">1084</span>,
        <span class="hljs-comment">// 线程编号thread ID</span>
        <span class="hljs-string">"tid"</span>:<span class="hljs-number">0</span>,
        <span class="hljs-comment">// 一些事件类型的必要参数可以在这里配置</span>
        <span class="hljs-string">"args"</span>: &#123;
            <span class="hljs-string">"name"</span>:<span class="hljs-string">"xx"</span>
        &#125;,
   &#125;,
   ......
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然有特定的格式，那么它的能力肯定不止于此，所以有趣的东西来了～
Google官方做了一款强大的可视化展示和分析工具，之前有一个专门的 trace-viewer 项目，现在该项目合并到了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcatapult-project%2Fcatapult%2Fblob%2Fmaster%2Ftracing%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/catapult-project/catapult/blob/master/tracing/README.md" ref="nofollow noopener noreferrer">catapult</a> 中, catapult 是 Chromium 工程师开发的一系列性能工具的合集，可以用来收集、展示、分析 Chrome、Website 甚至 Android 的性能
废话不多说，我们在浏览器打开它 chrome://tracing</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd4a9932dd1f4e929b5b267f7b7b15c3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整体UI风格简洁朴素，使用起来也比较容易上手</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21191885131d47aeb025527a8845d3ea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里导入一段测试的例子，大家可以试试</p>
<pre><code class="hljs language-json copyable" lang="json">[ 
  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"lark日历"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"b"</span>, <span class="hljs-attr">"cat"</span>: <span class="hljs-string">"daily"</span>, <span class="hljs-attr">"id"</span>: <span class="hljs-string">"my-day"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"lark日历"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">0</span>&#125;,
  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"lark日历"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"e"</span>, <span class="hljs-attr">"cat"</span>: <span class="hljs-string">"daily"</span>, <span class="hljs-attr">"id"</span>: <span class="hljs-string">"my-day"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"lark日历"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">37800000000</span>&#125;, 

  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"写代码"</span>, <span class="hljs-attr">"cname"</span>: <span class="hljs-string">"good"</span>,<span class="hljs-attr">"ph"</span>: <span class="hljs-string">"X"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"工作"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">"dur"</span>: <span class="hljs-number">3600000000</span>&#125;, 
  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"写代码"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"X"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"工作"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">12400000000</span>, <span class="hljs-attr">"dur"</span>: <span class="hljs-number">20000000000</span>, <span class="hljs-attr">"args"</span>: &#123;<span class="hljs-attr">"mark"</span>:<span class="hljs-string">"用x和dur表示开始和结束"</span>&#125;&#125;,

  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"吃饭"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"B"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"休闲"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">3600000000</span>, <span class="hljs-attr">"args"</span>: &#123;<span class="hljs-attr">"mark"</span>:<span class="hljs-string">"用b - e也可以表示开始和结束"</span>&#125;&#125;,
  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"吃饭"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"E"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"休闲"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">12400000000</span>&#125;,

  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"游泳"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"X"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"tid"</span>: <span class="hljs-string">"休闲"</span>, <span class="hljs-attr">"ts"</span>: <span class="hljs-number">32400000000</span>, <span class="hljs-attr">"dur"</span>: <span class="hljs-number">5400000000</span>&#125;,

  &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"process_name"</span>, <span class="hljs-attr">"ph"</span>: <span class="hljs-string">"M"</span>, <span class="hljs-attr">"pid"</span>: <span class="hljs-string">"Main"</span>, <span class="hljs-attr">"args"</span>: &#123;<span class="hljs-attr">"name"</span>: <span class="hljs-string">"时间线"</span>&#125;&#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56d85d3fe16b44c69cf72c6709d1baf9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有事件类型（ph）及其相关阶段可以看这里 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU%2Fedit%23heading%3Dh.puwqg050lyuy" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/edit#heading=h.puwqg050lyuy" ref="nofollow noopener noreferrer">docs.google.com/document/d/…</a></p>
<h2 data-id="heading-7">多次记录的时间轴历史</h2>
<p>在顶部bar中有个不起眼的下拉框，它显示最近的时间轴会话，点击它可以看到历史记录，经过测试，最多可以保留最近5个历史时间轴。每个选项可以看到它的标题，录制时长，距离录制已过去的时间，概览的迷你图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e328960950ec4b48894423ac79061fe4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">3个可扩展的能力</h2>
<h3 data-id="heading-9">屏幕关键帧快照</h3>
<p>启用Screenshots屏幕截图可以针对每一帧进行截图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dc2c50ae83245ed9768f6e948343ddb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">Memory走势图</h3>
<p>开启Memory选项会以图表的形式记录一些数据信息，和 <del>(股票均线类似)</del> Performance monitor记录的东西类似，鼠标移上去可以看到各个时刻的性能指标，结合关键截图使用也是很不错滴</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ae4b6067c9648df8e052cb7a84b3185~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">Web Vitals规范性能指标</h3>
<p>Web Vitals是谷歌发起的一项倡议，旨在为页面性能和质量提供统一的质量标准，即使站点的维护者在性能方面没有很深的研究，也能有一个优化方向。关键指标随着时间的推移而演变，目前主要集中在用户体验加载、交互性和视觉稳定性这三个方面，三个指标的建议目标是75分位，分析这些指标可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbytedance.feishu.cn%2Fdocs%2FdoccnE9KJHYnl0QAPx58qhbeVLh%23iitBOE" target="_blank" rel="nofollow noopener noreferrer" title="https://bytedance.feishu.cn/docs/doccnE9KJHYnl0QAPx58qhbeVLh#iitBOE" ref="nofollow noopener noreferrer">Lighthouse</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43a0886dccca45d5895c75f115eb7550~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fweb.dev%2Flcp%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://web.dev/lcp/" ref="nofollow noopener noreferrer">Largest Contentful Paint (LCP)</a> : measures <em>loading performance</em> . To provide a good user experience, LCP should occur <strong>within 2.5 seconds</strong> of when the page first starts loading.
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fweb.dev%2Ffid%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://web.dev/fid/" ref="nofollow noopener noreferrer">First Input Delay (FID)</a> : measures <em>interactivity</em> . To provide a good user experience, pages should have a FID of <strong>less than 100 milliseconds</strong> .
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fweb.dev%2Fcls%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://web.dev/cls/" ref="nofollow noopener noreferrer">Cumulative Layout Shift (CLS)</a> : measures <em>visual stability</em> . To provide a good user experience, pages should maintain a CLS of <strong>less than 0.1</strong> .</p>
</blockquote>
<p>上面总结一下就是最大块的内容渲染、首次可交互时间尽量要早，页面无意义的抖动幅度要小且次数少
勾上Web Vitals选项，面板中会出现如下图的数据</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da65a6815ada46ccb056fc7be6798118~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12"><strong>强制内存垃圾回收</strong></h2>
<p>在最末尾有个不起眼的小垃圾箱collect garbage，它的作用就是让浏览器人工干预的进行一次GC，这里想看到这个按钮的效果，可以打开Performance monitor进行观察，在点击垃圾回收的时候内存空会有一定的减少，原因就是进行了手动GC</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8055e6e721ed4b929890f5b0db423299~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">其他设置</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a772130fe4de417daa194bbc6ca62256~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击小齿轮会展开一个区域，里面有4个可操作项</p>
<h3 data-id="heading-14">Disable JavaScript samples</h3>
<p>默认情况在记录指标数据的时候，浏览器会记下JavaScript详细的调用堆栈，通过勾起这个开关，可以取消记录，对比如下两张图片</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/672281ac3fe24e3ca77eb223dcad5a19~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">Enable advanced paint instrumentation</h3>
<p>打开可以查看绘制事件的高级信息，选中Paint事件在下方会多一个paint profile的tab，选中Frames会增加Layers的tab，开启这项功能会使分析变慢，页面也会变卡</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c3fd36cf7b4b19b325366715c5f0ee~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">Network / CPU</h3>
<p>Network可以设置当前网络的情况，用来模拟一些弱网的场景
CPU的设置则为限制计算机的CPU计算能力，例如：4倍减速（4 <strong>x slowdown</strong> ）选项会让CPU运行速度比平时慢4倍。（因为设备的架构的不同浏览器无法真正模拟移动设备的CPU）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52352793f3904854adb65e30758120e4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">分析结果面板</h2>
<p>这部分内容已经有很多总结了，所以快速过一下，着重讲一下有意思的地方
<strong>概览面板</strong>
这条轨迹从左到右按时间顺序显示了记录数据，从上往下依次为FPS、CPU和NET，这个图表让你大致了解帧数波动、CPU活动（黄色峰值）和网络活动</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9909290d2a994f799033de67d2d0c178~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>红色的小横线意味着帧率下降得很多，可能会损害用户体验</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8ed4af725aa4c73bf77d9ed5e286215~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不同颜色的竖直线表示当前不同的状态，它与 <strong>Timings</strong> 中的tag相对应</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99c98e9bb10a463e83b23faec4c985b8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Network视图</strong>
展开network可以看到时间轴对应各个阶段网络请求数据以及持续时间，同时根据从上往下的顺序来表示不同的优先级，HTML 文件为蓝色、脚本为黄色、样式表为紫色、媒体文件为绿色、其他资源为灰色</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe20ca0ff56e4e738064bfa51a93789a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>鼠标悬停可以看到相对详细的数据</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb0e58e4a4224014927d762b91e95206~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Frames</strong>
逐帧视图，将鼠标悬停在其中一个绿色方块上，每个方块显示特定帧的时间和帧率</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/346298608ae742e9b4a2ced232799a52~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Interactions</strong>
Interactions 用来记录用户交互操作，比如点击鼠标、输入文字等</p>
<p><strong>Timings</strong>
用来记录一些关键性能指标的时间节点，如FCP、LCP等等</p>
<p><strong>Main</strong>
主线程视图部分，从左到右显示了主线程按照时间先后的执行顺序日志，从顶部到底部显示了事件发生的原因
完整的信息可以查看这里 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FGoogleChrome%2Fdeveloper.chrome.com%2F%2Fblob%2Fmain%2Fsite%2Fen%2Fdocs%2Fdevtools%2Fevaluate-performance%2Fperformance-reference%2Findex.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/GoogleChrome/developer.chrome.com//blob/main/site/en/docs/devtools/evaluate-performance/performance-reference/index.md" ref="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p>
<p><strong>Raster</strong>
光栅化线程，光栅化的本质是坐标变换、几何离散化，该视图主要是记录执行光栅化任务的时间轴，光栅化的任务主要是决定每个渲染图元中的哪些像素应该被绘制在屏幕上</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43633d1623304731a713f16d11a81903~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Compositor</strong>
合成线程的执行时间线记录，主要工作是从html绘制阶段(Paint)结束后，将位图（GraphicsLayer 层）以纹理（texture）的形式上传给 GPU；计算页面的可见部分和即将可见部分（滚动）；CSS动画处理等</p>
<p><strong>GPU</strong>
可以直观看到是否启用了GPU渲染加速以及各时间节点的占用情况</p>
<p><strong>ServiceWorker thread</strong>
Service Worker线程有着独立的js环境，这个视图主要是用于查看该线程的活动情况</p>
<p><strong>Chrome_childIOThread</strong>
属于Child Processes(renderer, GPU, utility)核心进程，主要是用于观察子进程的IO线程的调用情况</p></div>  
</div>
            