
---
title: '使用 Performance API 获取页面性能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4532'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 00:43:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=4532'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一 概述</h1>
<h2 data-id="heading-1">1. 什么是 Performance</h2>
<p>首先 <code>Performance</code> 是一个标准，用于解决开发者在浏览器中获取性能数据的问题。其次， <code>Performance</code> 是一个浏览器全局对象，提供了一组 API 用于编程式地获取程序在某些节点的性能数据。它包含一组高精度时间定义，以及配套的相关方法。</p>
<h2 data-id="heading-2">2. 新的 Performance 标准</h2>
<p>新的 <code>Performance</code> 标准包含了许多 API，它们各自针对性能监控的某个方面。但是目前 <code>Performance</code> 部分标准处于实验阶段，并未稳定发布，且已发布的标准，各浏览器支持度差异较大。</p>



























































<table><thead><tr><th>API</th><th>描述</th><th>状态</th><th>兼容性</th></tr></thead><tbody><tr><td><code>Navigation Timing</code></td><td>导航计时。用于记录并检测用户的设备，网络等环境，以及页面初始资源加载和解析耗时。</td><td>稳定</td><td><code>>= IE 9</code></td></tr><tr><td><code>High Resolution Timing</code></td><td>精确计时。用于精确到微秒级别的计时，实际使用时精度受浏览器实现限制，通常精确到毫秒</td><td>稳定</td><td><code>>= IE 10</code></td></tr><tr><td><code>Resource Timing</code></td><td>资源计时。对单个网络资源的计时，包含页面从打开到获取时的所有网络资源。</td><td>稳定</td><td><code>>= IE 10, Safari 不支持</code></td></tr><tr><td><code>Page Visiblity</code></td><td>页面可见性。获取页面是否可见（例如用户切换了标签页，当前页面隐藏，此时为不可见）</td><td>稳定</td><td><code>>= IE 10</code></td></tr><tr><td><code>Battery Status</code></td><td>电池状态。获取当前设备是否充电，电量等级等。对移动设备来说非常实用。</td><td>稳定</td><td><code>IE, Safari不支持, Android WebView >=40</code></td></tr><tr><td><code>User Timing</code></td><td>用户计时。手动对某段代码或函数计时。</td><td>稳定</td><td><code>>= IE 10, Firfox 40, safari 11</code></td></tr><tr><td><code>Beacon</code></td><td>灯塔。用于将分析结果和诊断数据采用非阻塞异步的方式发送到服务器，<code>Beacon</code> 方法保证在页面关闭前执行。</td><td>实验</td><td><code>IE, Safari, IOS, Android 不支持</code></td></tr><tr><td><code>Frame Timing</code></td><td>帧计时。获取与帧相关的性能数据，例如每秒帧数</td><td>实验</td><td><code>不支持</code></td></tr></tbody></table>
<h2 data-id="heading-3">3. 旧的 Performance 标准</h2>
<p><code>PerformanceTiming</code> 接口是为了向下兼容而存在的接口。它包含了全部的 <code>Navigation Timing</code> 以及部分 <code>Resource Timing</code> 的数据。<code>PerformanceTiming</code> 对象的兼容性是最好的，通过这个接口可以获取到页面从点击链接到页面渲染完毕的各个关键时间节点。</p>
<h2 data-id="heading-4">4. 如何获取 Performance</h2>
<p>通过 <code>window.performance</code> 来获取 <code>Performance</code> 对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.performance
<span class="hljs-comment">// Performance &#123;</span>
<span class="hljs-comment">//   timeOrigin: 1611749316627.347, </span>
<span class="hljs-comment">//   onresourcetimingbufferfull: null, </span>
<span class="hljs-comment">//   eventCounts: EventCounts, </span>
<span class="hljs-comment">//   timing: PerformanceTiming, </span>
<span class="hljs-comment">//   navigation: PerformanceNavigation, </span>
<span class="hljs-comment">//   ...</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>PerformanceEntry</code> 接口可以分类获取 performance 运行时的实例数据，例如手动创建的 <code>mark</code> 标记产生的性能数据，或者是在异步资源加载时（css，script，ajax，等）被动创建的资源标记</p>
<h1 data-id="heading-5">二 PerformanceTiming</h1>
<h2 data-id="heading-6">1. 概述</h2>
<p><code>PerformanceTiming</code> 接口提供了在页面加载和使用时的各种性能计时信息。通过 <code>window.performance.timing</code> 获得一个实例对象。</p>
<h2 data-id="heading-7">2. 属性</h2>
<blockquote>
<p>PerformanceTiming 接口的所有属性都是只读的，且没有任何继承属性，由于所有属性均是某个时间点，因此值类型都是 无符号 long long 类型（double）</p>
</blockquote>
<h3 data-id="heading-8">(1) PerformanceTiming.navigationStart</h3>
<p><code>PerformanceTiming.navigationStart</code> 表示同一个浏览器上下文中，上一个文档卸载结束的 UNIX 时间戳。如果没有上一个文档，这个值与 <code>PerformanceTiming.fetchStart</code> 相同。</p>
<h3 data-id="heading-9">(2) PerformanceTiming.unloadEventStart</h3>
<p><code>PerformanceTiming.unloadEventStart</code> 表示 <code>unload</code> 事件抛出时的 UNIX 时间戳。如果没有上一个文档，或者重定向中的一个与当前文档不同源，该值为 <code>0</code>。</p>
<h3 data-id="heading-10">(3) PerformanceTiming.unloadEventEnd</h3>
<p><code>PerformanceTiming.unloadEventEnd</code> 表示 <code>unload</code> 事件处理完成时的 UNIX 时间戳。如果没有上一个文档，或者重定向中的一个与当前文档不同源，该值为 <code>0</code>。</p>
<h3 data-id="heading-11">(4) PerformanceTiming.redirectStart</h3>
<p><code>PerformanceTiming.redirectStart</code> 表示第一个 HTTP 重定向开始时的 UNIX 时间戳。如果没有重定向，或者重定向中的一个不同源，该值为 <code>0</code>。</p>
<h3 data-id="heading-12">(5) PerformanceTiming.redirectEnd</h3>
<p><code>PerformanceTiming.redirectEnd</code> 表示最后一个 HTTP 重定向完成时（即最后一个 HTTP 响应的最后一个比特被接收到的时间）的 UNIT 时间戳。如果额米有重定向，或者重定向中的一个不同源，该值为 <code>0</code>。</p>
<h3 data-id="heading-13">(6) PerformanceTiming.fetchStart</h3>
<p><code>PerformanceTiming.fetchStart</code> 表示浏览器准备好用 HTTP 请求来获取文档的 UNIX 时间戳。这个时间早于检查应用缓存。</p>
<h3 data-id="heading-14">(7) PerformanceTiming.domainLookupStart</h3>
<p><code>PerformanceTiming.domainLookupStart</code> 表示域名查询开始的 UNIX 时间戳。如果使用了持续连接，或者这个信息被存储到了缓存或本地资源，那么该值与 <code>PerformanceTiming.fetchStart</code> 相同。</p>
<h3 data-id="heading-15">(8) PerformanceTiming.domainLookupEnd</h3>
<p><code>PerformanceTiming.domainLookupEnd</code> 表示域名查询结束的 UNIX 时间戳。如果使用了持续连接，或者这个信息被存储到了缓存或本地资源，那么该值与 <code>PerformanceTiming.fetchStart</code> 相同。</p>
<h3 data-id="heading-16">(9) PerformanceTiming.connectStart</h3>
<p><code>PerformanceTiming.connectStart</code> 表示 HTTP 请求开始向服务器发送时的 UNIX 时间戳。如果使用持久连接，则该值与 <code>PerformanceTiming.fetchStart</code> 相同。</p>
<h3 data-id="heading-17">(10) PerformanceTiming.connectEnd</h3>
<p><code>PerformanceTiming.connectEnd</code> 表示浏览器与服务器之间的连接建立（即握手与认证等过程全部结束）的 UNIX 时间戳。如果使用持久连接，则该值与 <code>PerformanceTiming.fetchStart</code> 相同。</p>
<h3 data-id="heading-18">(11) PerformanceTiming.secureConnectionStart</h3>
<p><code>PerformanceTiming.secureConnectionStart</code> 表示浏览器与服务器开始安全链接的握手时的 UNIX 时间戳。如果当前网页不要求安全链接，该值为 <code>0</code>。</p>
<h3 data-id="heading-19">(12) PerformanceTiming.requestStart</h3>
<p><code>PerformanceTiming.requestStart</code> 表示浏览器向服务器发送 HTTP 请求时的 UNIX 时间戳。</p>
<h3 data-id="heading-20">(13) PerformanceTiming.responseStart</h3>
<p><code>PerformanceTiming.responseStart</code> 表示浏览器从服务器收到（或从本地缓存读取）第一个字节时的 UNIX 时间戳。如果传输层从开始请求后失败并连接被重开，该值会被重置为新的请求的相应的时间。</p>
<h3 data-id="heading-21">(14) PerformanceTiming.responseEnd</h3>
<p><code>PerformanceTiming.responseEnd</code> 表示浏览器从服务器收到（或从本地缓存读取，或从本地资源读取）最后一个字节时（如果在此之前HTTP连接已经关闭，则返回关闭的时间）的 UNIX 时间戳。</p>
<h3 data-id="heading-22">(15) PerformanceTiming.domLoading</h3>
<p><code>Performance.domLoading</code> 表示当前网页 <code>DOM</code> 结构开始解析时（即 <code>Document.readyState</code> 属性变为 <code>loading</code>，相应的 <code>readystatechange</code> 事件触发时）的 UNIX 时间戳。</p>
<h3 data-id="heading-23">(16) PerformanceTiming.domInteractive</h3>
<p><code>Performance.domInteractive</code> 表示当前网页 <code>DOM</code> 结构解析结束，开始加载内嵌资源时（即 <code>Document.readyState</code> 的属性为 <code>interactive</code>，相应的 <code>readystatechange</code> 事件触发时）的 UNIX 时间戳。</p>
<h3 data-id="heading-24">(17) PerformanceTiming.domContentLoadedEventStart</h3>
<p><code>PerformanceTiming.domContentLoadedEventStart</code> 表示解析器触发 <code>DomContentLoaded</code> 事件，即所有需要被执行的脚本已经被解析时的 UNIX 时间戳。</p>
<h3 data-id="heading-25">(18) PerformanceTiming.domContentLoadedEventEnd</h3>
<p><code>PerformanceTiming.domContentLoadedEventEnd</code> 表示所有需要被执行的脚本均已被执行完成时的 UNIX 时间戳。</p>
<h3 data-id="heading-26">(19) PerformanceTiming.domComplete</h3>
<p><code>PerformanceTiming.domComplete</code> 表示文档解析完成，即 Document.readyState 变为 <code>complete</code> 且相应的 <code>readystatechange</code> 事件被触发时的 UNIX 时间戳。</p>
<h3 data-id="heading-27">(20) PerformanceTiming.loadEventStart</h3>
<p><code>PerformanceTiming.loadEventStart</code> 表示该文档下，<code>load</code> 事件被触发的 UNIX 时间戳。如果还未发送，值为 <code>0</code>。</p>
<h3 data-id="heading-28">(21) PerformanceTiming.loadEventEnd</h3>
<p><code>PerformanceTiming.loadEventEnd</code> 表示该文档下，<code>load</code> 事件结束，即加载事件完成时的 UNIX 时间戳，如果事件未触发或未完成，值为 <code>0</code>。</p>
<h2 data-id="heading-29">3. 各个性能时间节点</h2>
<p>先看一张社区流传甚广的图片：</p>
<p>这张图描述了从用户开始路由到这个页面，到这个页面完全加载完成，总过经历的所有过程，根据图片，我们可以划分出各个有意义的考察性能的时间节点：</p>





























































<table><thead><tr><th>时间段</th><th>描述</th></tr></thead><tbody><tr><td><code>navigationStart</code> ~ <code>unloadEventEnd</code></td><td>上一页面的卸载耗时</td></tr><tr><td><code>fetchStart</code> ~ <code>domainLookupStart</code></td><td>查询 app DNS 缓存耗时</td></tr><tr><td><code>domainLookupStart</code> ~ <code>domainLookupEnd</code></td><td>dns 查询耗时</td></tr><tr><td><code>connectStart</code> ~ <code>connectEnd</code></td><td>TCP 连接耗时</td></tr><tr><td><code>connectEnd</code> ~ <code>secureConnectionStart</code></td><td>针对 https 协议，在 tcp 握手后，传输真正的内容前，建立安全连接的耗时</td></tr><tr><td><code>fetchStart</code> ~ <code>responseStart</code></td><td><code>TTFB</code>（time to first byte）, 即首包时长（从用户代理发出第一个请求开始，到页面读取到第一个字节的耗时）。在一个 web 程序中，用户代理发送的第一个 get 请求一般是 index.html，即接收到这个 html 文件的第一个字节的耗费时间</td></tr><tr><td><code>responseStart</code> ~ <code>responseEnd</code></td><td>内容响应时长</td></tr><tr><td><code>domLoading</code> ~ <code>domInteractive</code></td><td>dom 解析完成，即 <code>DOM</code> 树构建完成的时长</td></tr><tr><td><code>domContentLoadedEventEnd</code> ~ <code>loadEventStart</code></td><td>渲染时长，<code>domContentLoaded</code> 表示 <code>DOM</code>，<code>CSSOM</code> 均准备就绪（<code>CSSOM</code> 就绪意味着没有样式表阻止 js 脚本执行），开始构建渲染树</td></tr><tr><td><code>navigationStart</code> ~ <code>domLoading</code></td><td><code>FPT</code>（first paint time）, 即首次渲染时间，或白屏时间，从用户打开页面开始，到第一次渲染出可见元素为止</td></tr><tr><td><code>navigationStart</code> ~ <code>domInteractive</code></td><td><code>TTI</code>（time to interact），首次可交互时间</td></tr><tr><td><code>fetchStart</code> ~ <code>domContentLoadedEventEnd</code></td><td><code>html</code> 加载完成时间，此时 <code>DOM</code> 已经解析完成</td></tr><tr><td><code>navigationStart</code> ~ <code>loadEventStart</code></td><td>页面完全加载完成的时间</td></tr></tbody></table>
<h1 data-id="heading-30">三 PerformanceEntry</h1>
<p><code>PerformanceTiming</code> 是向下兼容的旧接口，且只能保存页面打开过程（从路由到该地址，到当前页面load事件触发完成）中的性能数据，如果需要在页面运行过程中持续获取性能数据，需要使用 <code>PerformanceEntry</code> 实例。</p>
<h2 data-id="heading-31">1. Performance.getEntries</h2>
<p><code>Performance.getEntries([filterOption])</code> 方法用于获取 <code>PerformanceEntry</code> 实例数组，它接受一个可选的参数，如果不传则获取全部的 <code>entry</code> 数据。该参数对象可以包含以下，属性：</p>
<ul>
<li><code>name</code> : performance entry 的名字</li>
<li><code>entryType</code> : entry 类型，合法的 entry 值可以从 PerformanceEntry.entryType</li>
<li><code>initiatorType</code> :  初始化资源的类型，取值由 <code>PerformanceResourceTiming.initiatorType</code> 接口定义</li>
</ul>
<p>该方法返回 <code>entries</code> 数组，包含了所有符合筛选条件的 <code>entry</code> 。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.performance.getEntries(&#123; <span class="hljs-attr">entryType</span>: <span class="hljs-string">'resource'</span> &#125;)
<span class="hljs-comment">/*
0: PerformanceNavigationTiming &#123;unloadEventStart: 0, unloadEventEnd: 0, domInteractive: 1988.2200000574812, domContentLoadedEventStart: 2038.9849999919534, domContentLoadedEventEnd: 2049.5600000722334, …&#125;
1: PerformanceResourceTiming &#123;initiatorType: "link", nextHopProtocol: "h2", workerStart: 0, redirectStart: 0, redirectEnd: 0, …&#125;
...
13: PerformancePaintTiming &#123;name: "first-paint", entryType: "paint", startTime: 1987.154999980703, duration: 0&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">2. Performance.getEntriesByName</h2>
<p><code>Performance.getEntriesByName(name [, type])</code> 方法接受两个参数：</p>
<ol>
<li><code>name</code> : 必选，这个 entry 的名称</li>
<li><code>type</code>: 可选，想要过滤的 entry 类型</li>
</ol>
<p>返回符合条件的 <code>entries</code> 数组。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.performance.mark(<span class="hljs-string">'_my_mark_1'</span>)
<span class="hljs-built_in">window</span>.performance.getEntriesByName(<span class="hljs-string">'_my_mark_1'</span>)
<span class="hljs-comment">// [PerformanceMark]</span>
<span class="hljs-comment">// 0: PerformanceMark &#123;detail: null, name: "_my_mark_1", entryType: "mark", startTime: 5614367.25000001, duration: 0&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">3. Performance.getEntriesByType</h2>
<p><code>Performance.getEntriesByType(type)</code> 方法接受一个 <code>entryType</code> ，返回符合类型的 <code>PerformanceEntry</code> 列表。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.performance.getEntriesByType(<span class="hljs-string">'paint'</span>)
<span class="hljs-comment">/*
[PerformancePaintTiming, PerformancePaintTiming]
0: PerformancePaintTiming &#123;name: "first-paint", entryType: "paint", startTime: 2775.984999956563, duration: 0&#125;
1: PerformancePaintTiming &#123;name: "first-contentful-paint", entryType: "paint", startTime: 2775.984999956563, duration: 0&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">4. PerformanceEntry 属性</h2>
<blockquote>
<p>PerformanceEntry 的所有属性都是只读的</p>
</blockquote>
<h3 data-id="heading-35">(1) PerformanceEntry.entryType，PerformanceEntry.name</h3>
<p><code>PerformanceEntry.entryType</code> 是一个 performance entry 的类型，值为 <code>DOMString</code> 。用于区分不同类型的 performance 数据。<code>PerformanceEntry.name</code> 标识当前性能数据块的名称，它允许的值和类型随着 <code>entryType</code> 不同而不同</p>









































<table><thead><tr><th>值</th><th>标识的性能时间类型</th><th>name 属性类型</th><th>name 属性含义</th></tr></thead><tbody><tr><td><code>frame</code>, <code>navigation</code></td><td><code>PerformanceFrameTiming</code>, <code>PerformanceNavigationTiming</code></td><td><code>URL</code></td><td>产生这两个performance数据的文档地址</td></tr><tr><td><code>resource</code></td><td><code>PerformanceResourceTiming</code></td><td><code>URL</code></td><td>请求的资源的地址，即便请求被重定向了，这个值也不会改变</td></tr><tr><td><code>mark</code></td><td><code>PerformanceMark</code></td><td><code>DOMString</code></td><td>创建该 <code>mark</code> 时指定的 <code>name</code> 属性</td></tr><tr><td><code>measure</code></td><td><code>PerformanceMeasure</code></td><td><code>DOMString</code></td><td>使用 <code>performance.measure()</code> 创建 <code>measure</code> 时提供的 <code>name</code> 属性</td></tr><tr><td><code>paint</code></td><td><code>PerformancePaintTiming</code></td><td><code>DOMString</code></td><td><code>first-paint</code> 或者 <code>first-contentful-paint</code></td></tr></tbody></table>
<h3 data-id="heading-36">(2) PeformanceEntry.startTime</h3>
<p><code>performanceEntry.startTime</code> 表示这个 performance 数据被创建时的时间戳。根据不同的 <code>entryType</code> 值，<code>startTime</code> 取值的含义有些不同：</p>
<ul>
<li><code>frame</code> :  指定的帧（<code>frame</code>）开始渲染时的时间</li>
<li><code>mark</code> : 该 <code>mark</code> 标记被创建时的时间戳（<code>performance.mark()</code> 调用时的时间）</li>
<li><code>measure</code> : 该 measure 被创建时的时间戳（<code>performance.measure()</code> 方法调用时的时间）</li>
<li><code>navigation</code> : 值为 0</li>
<li><code>resource</code> : 浏览器发起该资源请求时的时间戳</li>
</ul>
<h3 data-id="heading-37">(3) PerformanceEntry.duration</h3>
<p><code>performanceEntry.duration</code> 表示这个 performance 数据标识的持续时间。根据不同的 <code>entryType</code> 值，<code>duration</code> 取值的含义有些不同：</p>
<ul>
<li><code>frame</code> : 两个连续的帧开始渲染的时间之差</li>
<li><code>mark</code> : 值为 0，<code>mark</code> 标记没有持续时间</li>
<li><code>measure</code> : 要测量的 measure 的持续时间</li>
<li><code>navigation</code> : <code>performanceEntry.startTime</code> 和 <code>performanceNavigationTiming.loadEventEnd</code> 的差值</li>
<li><code>resource</code> : 该资源加载的耗时，即 <code>performanceEntry.startTime</code> 和 <code>performanceResourseTiming.responseEnd</code> 的差值</li>
</ul>
<h1 data-id="heading-38">四 手动测量性能</h1>
<p><code>Performance</code> 接口除了测量资源加载性能（PerformanceResourceTiming），渲染帧性能（PerformanceFrameTiming），页面初始化性能（PerformanceNavigationTiming）等等以外，还允许手动创建标记，让开发者在代码中测量程序执行的性能。</p>
<h2 data-id="heading-39">1. Performance.mark</h2>
<p><code>performance.mark(name)</code> 方法接受一个字符串，用于创建一个标记（mark），字符串即为这个标记的名称，这个标记会固定下创建时的时间戳。后续开发者可以通过不同标记的 startTime 值相减来获取一段代码的执行耗时，也可以通过 performance.measure 来计算耗时。该方法返回一个 <code>mark</code> 类型的 <code>PerformanceEntry</code> 实例。</p>
<p>一个标记（mark）具有以下属性值：</p>
<ul>
<li><code>entryType</code> : 固定为 <code>mark</code></li>
<li><code>name</code> : 创建标记时通过参数指定的标记名</li>
<li><code>startTime</code> : 创建 <code>mark</code> 时的时间戳</li>
<li><code>duration</code> : 0，<code>mark</code> 没有持续时间</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.performance.mark(<span class="hljs-string">'_test_mark_1'</span>)
<span class="hljs-comment">// PerformanceMark &#123;detail: null, name: "_test_mark_1", entryType: "mark", startTime: 1978026.354999999, duration: 0&#125;</span>

<span class="hljs-built_in">window</span>.performance.mark(<span class="hljs-string">'_test_mark_2'</span>)
<span class="hljs-comment">// PerformanceMark &#123;detail: null, name: "_test_mark_2", entryType: "mark", startTime: 1991866.0800000008, duration: 0&#125;</span>

<span class="hljs-built_in">window</span>.performance.mark(<span class="hljs-string">'_test_mark_1'</span>)
<span class="hljs-comment">// PerformanceMark &#123;detail: null, name: "_test_mark_1", entryType: "mark", startTime: 1994302.8449999993, duration: 0&#125;</span>

performance.getEntriesByName(<span class="hljs-string">'_test_mark_1'</span>)
<span class="hljs-comment">// [PerformanceMark, PerformanceMark]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>mark 的 name 不要求唯一</p>
</blockquote>
<h2 data-id="heading-40">2. Performance.measure</h2>
<p><code>performance.measure(name [, startMarkName [, endMarkName]])</code> 方法创建一个 entryType 类型为 measure 的 PerformanceEntry 对象，用于计算两个标志位之间的间隔时间。它接受三个参数：</p>
<ol>
<li><code>name</code> : 创建 measure 时指定的名称</li>
<li><code>startMarkName</code> : 可选，指定作为开始时间点的 mark 的名称</li>
<li><code>endMarkName</code> : 可选，指定作为结束时间点的 mark 的名称</li>
</ol>
<p>该方法返回一个 <code>measure</code> 类型的 <code>PerformanceEntry</code> ，它具有以下属性</p>
<ul>
<li><code>entryType</code> : 值为 <code>measure</code></li>
<li><code>name</code> : 创建 <code>measure</code> 时的名称</li>
<li><code>startTime</code> : 这一段测量的开始时间，如果传了第二个参数，那就是该 mark 的标记时间</li>
<li><code>duration</code> : 这一段测量持续的时间</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.performance.measure(<span class="hljs-string">'__measure_test_mark_1'</span>, <span class="hljs-string">'_test_mark_1'</span>)
<span class="hljs-comment">// PerformanceMeasure &#123;detail: null, name: "__measure_test_mark_1", entryType: "measure", startTime: 1994302.8449999993, duration: 476087.44500000123&#125;</span>

<span class="hljs-built_in">window</span>.performance.measure(<span class="hljs-string">'__measure_test_mark'</span>, <span class="hljs-string">'_test_mark_1'</span>, <span class="hljs-string">'_test_mark_2'</span>)
PerformanceMeasure &#123;<span class="hljs-attr">detail</span>: <span class="hljs-literal">null</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"__measure_test_mark"</span>, <span class="hljs-attr">entryType</span>: <span class="hljs-string">"measure"</span>, <span class="hljs-attr">startTime</span>: <span class="hljs-number">1994302.8449999993</span>, <span class="hljs-attr">duration</span>: -<span class="hljs-number">2436.7649999985006</span>&#125;

<span class="hljs-built_in">window</span>.performance.measure(<span class="hljs-string">'__measure_test_mark'</span>)
PerformanceMeasure &#123;<span class="hljs-attr">detail</span>: <span class="hljs-literal">null</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"__measure_test_mark"</span>, <span class="hljs-attr">entryType</span>: <span class="hljs-string">"measure"</span>, <span class="hljs-attr">startTime</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">duration</span>: <span class="hljs-number">3290800.8249999993</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上， <code>duration</code> 取值有三种情况</p>
<ol>
<li>调用 performance.measure 创建 measure 时，三个参数都传递了，即 name, startMark, endMark 同时存在，那么 duration = startMark.startTime - endMark.startTime （注意，并不是 endMark - startMark），duration 此时可能是负值</li>
<li>创建 measure 只传了两个参数，即 endMark 不存在，那么该 measure 计算的是从 startMark.startTime 到创建 measure 时的时间间隔</li>
<li>创建 measure 只提供了一个参数，即 startMark, endMark 都不存在，那么该 measure 计算的是从页面打开到创建 measure 时的时间间隔</li>
</ol>
<h2 data-id="heading-41">3. 清理 mark，measure</h2>
<ol>
<li><code>Performance.clearMark([name])</code> 方法用于清理指定的 <code>mark</code>，如果不提供参数，则所有 entryType 为 <code>mark</code> 的 <code>PerformanceEntry</code> 全部被清理。</li>
<li><code>Performance.clearMeasure([name])</code> 方法用于清理指定的 <code>measure</code>，如果不提供参数，则所有 entryType 为 <code>measure</code> 的 <code>PerformanceEntry</code> 全部被清理。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">performance.clearMarks(<span class="hljs-string">'_test_mark_1'</span>)
<span class="hljs-literal">undefined</span>
performance.getEntriesByType(<span class="hljs-string">'mark'</span>)
<span class="hljs-comment">// [PerformanceMark, PerformanceMark]</span>
<span class="hljs-comment">// PerformanceMark &#123;detail: null, name: "LUX_end", entryType: "mark", startTime: 2039.1650000001391, duration: 0&#125;</span>
<span class="hljs-comment">// PerformanceMark &#123;detail: null, name: "_test_mark_2", entryType: "mark", startTime: 1991866.0800000008, duration: 0&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            