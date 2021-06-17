
---
title: 'APP终极性能生存指南'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb057deb0f144e20952b273cd7d9a3da~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 21:08:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb057deb0f144e20952b273cd7d9a3da~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>性能是客户端永远绕不开的话题，一起来康康今年的WWDC提供了哪些有关性能提升的建议吧~</p>
<blockquote>
<p>（温馨提示：本片内容来源自WWDC21：<a href="https://developer.apple.com/videos/play/wwdc2021/10181/" target="_blank" rel="nofollow noopener noreferrer">Ultimate application performance survival guide</a>）</p>
<p>想了解更多WWDC2021内容的小伙伴，可以阅读我以下文章，欢迎多多交流和指正</p>
<p><a href="https://gcsnnb.github.io/2021/06/12/WWDC21-%E6%A3%80%E6%B5%8B%E5%92%8C%E8%AF%8A%E6%96%AD%E5%86%85%E5%AD%98%E9%97%AE%E9%A2%98/" target="_blank" rel="nofollow noopener noreferrer">检测和诊断内存问题</a></p>
<p><a href="https://gcsnnb.github.io/2021/06/08/What-s-new-in-WWDC21/" target="_blank" rel="nofollow noopener noreferrer">一文带你读完WWDC21核心（新）技术点</a></p>
</blockquote>
<ul>
<li>
<p>使用的五种工具</p>
<ul>
<li>Xcode Organizer</li>
<li>MetricKit</li>
<li>Instruments</li>
<li>XCTest</li>
<li>App Store Connect API</li>
</ul>
</li>
<li>
<p>参考的八个性能指标</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb057deb0f144e20952b273cd7d9a3da~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>电量</p>
</li>
<li>
<p>启动时间</p>
</li>
<li>
<p>超时响应率（Hang rate）</p>
<blockquote>
<p>APP无法响应用户的输入或者行为超过250ms，即记作一个hang</p>
</blockquote>
</li>
<li>
<p>内存</p>
</li>
<li>
<p>磁盘写入</p>
</li>
<li>
<p>滚动卡顿</p>
</li>
<li>
<p>APP终止</p>
</li>
<li>
<p>MXSignposts</p>
</li>
</ul>
</li>
<li>
<p>电量（battery usage）</p>
<ul>
<li>
<p>优化电池使用需要关注的几点：</p>
<ul>
<li>CPU</li>
<li>网络</li>
<li>定位</li>
<li>音频</li>
<li>蓝牙</li>
<li>GPU</li>
</ul>
<blockquote>
<p>其中CPU、网络、定位是电量消耗大户</p>
</blockquote>
</li>
<li>
<p>使用Xcode工具查看Debug期间的电量损耗情况</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2cdc223f2e14f6c86f7cffadb3b9ab9~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看CPU超过20%的阶段（CPU High Utilization）</li>
<li>查看CPU从闲置被唤醒的阶段（CPU Wake Overhead）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69caebc3011548fc9ecda4cbb850ca2f~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>使用Instrument中的Time Profile工具查看该阶段更详细的信息</p>
<p>（比如使用Location Energy Model确保应用如预期中正确地使用定位功能）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/234a6739171e4e27977616d2804e93a6~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>使用MetricKit收集用户的性能数据</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64aa3abfe0494119a46b0fdc72ed37e8~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-swift copyable" lang="swift">  <span class="hljs-comment">// 创建遵守`MXMetricManagerSubscriber`的协议的类AppMetrics</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppMetrics</span>: <span class="hljs-title">MXMetricManagerSubscriber</span> </span>&#123;
<span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
<span class="hljs-comment">// 初始化时将AppMetrics加入到`MXMetricManager`单例中</span>
<span class="hljs-keyword">let</span> shared <span class="hljs-operator">=</span> <span class="hljs-type">MXMetricManager</span>.shared
shared.add(<span class="hljs-keyword">self</span>)
&#125;
<span class="hljs-keyword">deinit</span> &#123;
<span class="hljs-comment">// 销毁时进行移除</span>
<span class="hljs-keyword">let</span> shared <span class="hljs-operator">=</span> <span class="hljs-type">MXMetricManager</span>.shared
shared.remove(<span class="hljs-keyword">self</span>)
&#125;

  <span class="hljs-comment">// 处理每日的metrics</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">didReceive</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">payloads</span>: [<span class="hljs-type">MXMetricPayload</span>])</span> &#123;

&#125;

  <span class="hljs-comment">// 处理diagnostics</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">didReceive</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">payloads</span>: [<span class="hljs-type">MXDiagnositcPayload</span>])</span> &#123;

&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>使用Xcode Organizer查看线上性能数据</p>
<blockquote>
<p>Xcode Organizer对MetrixKit收集到的数据进行了聚合，忽略了单一用户的详细数据，展现的是整体的趋势；</p>
<p>而使用MetricKit可以更具针对性的对某一用户在一段时间内的性能表现进行分析。</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1560306e29aa40b182e12d173e346550~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看用户的电量使用情况</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f9343c35dcd401ba1c14fe5ec6d186e~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>Regressions</p>
<blockquote>
<p>Regressions是Xcode 13新增的模块，它将各个版本的性能指标中发生劣化的情况单独拎出来展示，让开发者更清晰的看到哪些性能指标亟待优化。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f48dd73bbbee40e2ba332552b093b7c9~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>查看问题发生时对应的代码</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54bcd467686c4177b3dd2afd8f681db0~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p>超时响应率和滚动卡顿（Hang rate & Scrolling）</p>
<ul>
<li>
<p>超时响应</p>
<p>长时间无法响应是导致用户强退应用的重要原因</p>
</li>
<li>
<p>滚动卡顿</p>
<p>当在下一次屏幕刷新时，新的内容还未ready就会出现卡顿</p>
</li>
</ul>
<blockquote>
<p>Hang rate & Scrollings是表明APP没有及时响应的两个指标,一旦发生会严重影响用户体验，甚至让用户在使用应用时产生挫败感，从而降低用户的使用APP的意愿。</p>
</blockquote>
<ul>
<li>
<p>使用Xcode Organizer查看线上的卡顿情况</p>
<ul>
<li>Hang rate</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcb77ca920ab4c81ae0a24d9cb4044a2~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Scrolling</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a2daf1918ea4ad1a816d06a3cf60eb0~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>使用Instrument进行分析</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df0a20d9b2c749bfbf70d4b2bf0345fe~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>Thread State Trace</p>
<p>可以查看线程被阻塞的详细情况</p>
</li>
<li>
<p>System Call Trace</p>
<p>可以查看系统函数调用的时机和时长</p>
</li>
</ul>
</li>
<li>
<p>使用XCTest进行性能测试</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">testScrollingAnimationPerformance</span>()</span> <span class="hljs-keyword">throws</span> &#123;
app.launch()
app.staticTexts[<span class="hljs-string">"Meal Planner"</span>].tap()
<span class="hljs-keyword">let</span> foodCollection <span class="hljs-operator">=</span> app.collectionViews.firstMatch
<span class="hljs-comment">// `measure`函数默认重复5次，可以通过option设置手动停止</span>
<span class="hljs-keyword">let</span> measureOptions <span class="hljs-operator">=</span> <span class="hljs-type">XCTMeasureOptions</span>()
measureOptions.invocationOptions <span class="hljs-operator">=</span> [.manuallyStop]
<span class="hljs-comment">// 开始measure</span>
measure(metrics: [<span class="hljs-type">XCTOSSignpostMetric</span>.scrollDecelerationMetric], 
option: measureOptions) &#123;
    <span class="hljs-comment">// 滑动</span>
foodCollection.swipeUP(velocity: .fast)
    <span class="hljs-comment">// 停止measure</span>
stopMeasuring()
    <span class="hljs-comment">// 重置状态</span>
foodCollection.swipeDown(velocity: .fast)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用MetricKit收集线上数据</p>
<blockquote>
<p>在iOS 14中，MetricKit会收集用户使用过程中发生的问题，然后每24小时集中上报一次。</p>
<p><del>在iOS 15和MacOS 12中，MetricKit会在用户发生问题后，并且立刻进行上报</del></p>
<p>在iOS 15和MacOS 12中，MetricKit仍是每天上报一次，但会在<code>addSubscriber</code>后，并且立刻进行回调</p>
</blockquote>
</li>
<li>
<p>iOS 15中MetricKit新增动画性能检测的API，能够记录动画期间详细的性能数据和卡顿情况</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">startAnimating</span>()</span> &#123;
 <span class="hljs-comment">// 标记动画开始执行</span>
 mxSignpostAnimaitionIntervalBegin(
 log: <span class="hljs-type">MXMetricManager</span>.makeLogHandle(category: <span class="hljs-string">"animation"</span>_telemetry),
 name: <span class="hljs-string">"custom_animation"</span>)
 )
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">animationDidComplete</span>()</span> &#123;
<span class="hljs-comment">// 标记动画结束</span>
mxSignpost(<span class="hljs-type">OSSignpostType</span>.end, log: <span class="hljs-type">MXMetricManager</span>.makeLogHandle(category: <span class="hljs-string">"animation_telemetry"</span>), name: <span class="hljs-string">"custom_animation"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="copyable">  
  > 注：MXSignpost是MetricKit中封装的API，可以用来监控关键代码的运行情况

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38fcd4eff5764b208e36dc466137b27c~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>磁盘写入</p>
<ul>
<li>
<p>使用Instrument中的File Activity查看磁盘写入情况</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a592e23dbaf46cd85463564c5a091d9~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>优化建议：</p>
<ul>
<li>
<p>对于频繁写入的case，推荐使用Core Data</p>
</li>
<li>
<p>避免快速创建和删除文件</p>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>使用XCTest进行性能测试</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">testSaveMeal</span>()</span> &#123;
<span class="hljs-keyword">let</span> app <span class="hljs-operator">=</span> <span class="hljs-type">XCUIApplication</span>()
<span class="hljs-keyword">let</span> options <span class="hljs-operator">=</span> <span class="hljs-type">XCTMeasureOptions</span>()
options.invocationOptions <span class="hljs-operator">=</span> [.manullyStart]
<span class="hljs-comment">// 检测下面代码运行时的磁盘写入情况</span>
measure(metrics: [<span class="hljs-type">XCTStorageMetric</span>(application: app)], options: options) &#123;
app.launch()
startMeasuring()

<span class="hljs-keyword">let</span> firstCell <span class="hljs-operator">=</span> app.cells.firstMatch
firstCell.buttons[<span class="hljs-string">"Save meal"</span>].firstMatch.tap()

<span class="hljs-keyword">let</span> savedButton <span class="hljs-operator">=</span> firstCell.buttons[<span class="hljs-string">"Saved"</span>].firshMatch
<span class="hljs-type">XCTAssertTure</span>(savedButton.waitForExistence(timeout: <span class="hljs-number">2</span>))
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用Xcode Organizer查看线上磁盘写入情况</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45dbbd1a91ee4fce9bfae748afaa1ee3~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看在Disk Writes报告中可以查看24小时内写入量超过1GB的case</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8edf1fecf8ac441294e84d8b558c8c51~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在Xcode 13中，还可以得到一些优化建议</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65a02cf233254774b99564e0afd43ac4~tplv-k3u1fbpfcp-watermark.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>使用MetricKit收集用户的磁盘写入情况</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 标记开始磁盘写入</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">syncAllContentsToDB</span>()</span> &#123;
mxSignpost(<span class="hljs-type">OSSignpostType</span>.begin, 
log:<span class="hljs-type">MXMetricManager</span>.makeLogHandle(categroy: <span class="hljs-string">"diskWrite_telemetry"</span>),
name: <span class="hljs-string">"custom_diskWrites"</span>)

<span class="hljs-comment">// sync contents to database</span>

  <span class="hljs-comment">// 标记磁盘写入结束</span>
mxSignpost(<span class="hljs-type">OSSignpostType</span>.end,
log:<span class="hljs-type">MXMetricManager</span>.makeLogHandle(category: <span class="hljs-string">"diskWrite_telemetry"</span>),
name: <span class="hljs-string">"custom_diskWrites"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>启动时间</p>
<ul>
<li>
<p>使用Xcode Organizer查看线上启动数据</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ecfccd49914260b9674c9c99ab9f87~tplv-k3u1fbpfcp-watermark.image" alt="20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看因启动超时导致的程序终止</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db2037be3690476c9fc7659b7e700b61~tplv-k3u1fbpfcp-watermark.image" alt="21.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>使用Instrument中的App Launch工具进一步分析</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/970b14a5f65a4438af08b2ccc8af66a4~tplv-k3u1fbpfcp-watermark.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p>Memory</p>
<ul>
<li>
<p>使用Xcode Organizer查看线上内存使用情况</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e139a512d8b54e018e5b89bcf25f80b7~tplv-k3u1fbpfcp-watermark.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>使用Instrument中的Leak、Allocations和VM Tracker三个模板</p>
<ul>
<li>Leak检测内存泄漏</li>
<li>Allocations分析内存的生命周期</li>
<li>VM Tracker展示虚拟内存空间的使用情况</li>
</ul>
</li>
<li>
<p>使用MetricKit收集线上数据</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">saveAppAssets</span>()</span> &#123;
mxSignpost(<span class="hljs-type">OSSignpostType</span>.begin, 
log: <span class="hljs-type">MXMetricManager</span>.makeLogHandle(category: <span class="hljs-string">"memory_telemetry"</span>),
name: <span class="hljs-string">"custom_memory"</span>)

<span class="hljs-comment">// save app metadata</span>

mxSignpost(<span class="hljs-type">OSSignpostType</span>.end,
log: <span class="hljs-type">MXMetricManger</span>.makeLogHandle(category: <span class="hljs-string">"memory_telemetry"</span>),
name: <span class="hljs-string">"custom_memory"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<p>更多有关电量优化的Session：</p>
<p><a href="https://developer.apple.com/videos/play/wwdc2019/417/" target="_blank" rel="nofollow noopener noreferrer">Improving battery life and performance WWDC19</a></p>
<p><a href="https://developer.apple.com/videos/play/wwdc2021/10212/" target="_blank" rel="nofollow noopener noreferrer">Analyze HTTP traffic in Instruments WWDC 21</a></p>
<p>更多Hang优化的Session：</p>
<p><a href="https://developer.apple.com/videos/play/wwdc2021/10258/" target="_blank" rel="nofollow noopener noreferrer">Understand and Eliminate Hangs from you app WWDC21</a></p>
<p>更多滚动优化的Session：</p>
<p><a href="https://developer.apple.com/videos/play/tech-talks/10855/" target="_blank" rel="nofollow noopener noreferrer">Explore UI animation hitches and the render loop WWDC20</a></p>
<p><a href="https://developer.apple.com/videos/play/wwdc2020/10077/" target="_blank" rel="nofollow noopener noreferrer">Eliminate animation hitches with XCTest WWDC20</a></p>
<p>更多磁盘写入优化的Session：</p>
<p><a href="https://developer.apple.com/videos/play/wwdc2021/10087/" target="_blank" rel="nofollow noopener noreferrer">Diagnose power and performance regressions in your app WWDC21</a></p>
<p>更多启动优化的Session：</p>
<p><a href="https://developer.apple.com/videos/play/wwdc2020/10078/" target="_blank" rel="nofollow noopener noreferrer">Why is my app getting killed WWDC20</a></p>
<p>更多内存优化的Session：</p>
<p><a href="https://developer.apple.com/videos/play/wwdc2021/10180/" target="_blank" rel="nofollow noopener noreferrer">Detect and diagnose memory issues</a></p>
<p>更多关于性能工具的Session：</p>
<p><a href="https://developer.apple.com/videos/play/wwdc2020/10076/" target="_blank" rel="nofollow noopener noreferrer">Diagnose performance issues with Xcode Organizer WWDC20</a></p>
<p><a href="https://developer.apple.com/videos/play/wwdc2020/10081/" target="_blank" rel="nofollow noopener noreferrer">What's new in MetricKit WWDC20</a></p>
<p><a href="https://developer.apple.com/videos/play/wwdc2020/10057/" target="_blank" rel="nofollow noopener noreferrer">Identify trends with Power and Performance API WWDC20</a></p>
<p><a href="https://developer.apple.com/videos/play/wwdc2019/411/" target="_blank" rel="nofollow noopener noreferrer">Getting started with Instruments WWDC19</a></p></div>  
</div>
            