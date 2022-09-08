
---
title: '不改一行业务代码，飞书 iOS 低端机启动优化实践'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8131522f2284574b95a4a03c4380790~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Tue, 23 Aug 2022 23:38:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8131522f2284574b95a4a03c4380790~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">引言</h2>
<p>在启动优化时，我们常常通过增加并发的方式来减轻主线程的耗时。而在 iOS 中，GCD 是并发编程最常用的框架。增加并发是否是启动优化的良策？开发者适合选用哪个优先级的 GCD 队列？本文将结合飞书启动优化，给出选取 GCD 队列的最佳实践，也提供针对低端机的启动优化思路。</p>
<p>应用此思路，我们在未修改飞书业务逻辑的情况下，在飞书低端机上，取得了不错的用户体验收益：首屏展示时间优化 100ms，消息列表首刷时间优化 1500ms。</p>
<h2 data-id="heading-1">低端机的特性</h2>
<p>通过 Instruments 的 App Launch 功能，我们能看到 App 启动时的线程状态、Time Profiler 等信息。其中，我们发现不同设备在启动时的表现有很大差异。</p>
<p>以 iPhone 7p（低端）和 iPhone 12（高端）举例，它们的设备参数分别为：</p>























<table><thead><tr><th>设备</th><th>CPU 参数</th><th>实际核数ProcessInfo.processInfo.activeProcessorCount</th><th>跑满的 CPU 占比（Xcode 测试）</th></tr></thead><tbody><tr><td>iPhone 7p</td><td>A10 芯片[1]，2 高性能 + 2 低功耗，但是只有 2 核能同时工作</td><td>2</td><td>200%</td></tr><tr><td>iPhone 12</td><td>A14 芯片[2]，2 高性能 + 4 低功耗</td><td>6</td><td>600%</td></tr></tbody></table>
<p>启动飞书时，我们通过 Instruments 观察两个设备的线程状态，经过统计发现，iPhone 7p 上，主线程 Preempted 和 Runnable 状态的占比高达 21%。Instruments 的图中能看到主线程大片被抢占。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8131522f2284574b95a4a03c4380790~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个典型的局部，能看到主线程是 preempted 状态，CPU0 在执行其他进程，CPU1 在执行 GCD 线程。</p>
<p>而 iPhone 12，主线程 Preempted 和 Runnable 状态占比则只占 1%从这里我们能发现：对低端机来说，CPU 已经成为了启动的瓶颈，“增大并发”已不是一个万能的启动优化措施，而想办法减少其他线程对主线程的抢占，可能会是优化思路。</p>
<p>GCD queue 对主线程的抢占评测</p>
<p>为了评估“减少其他线程对主线程的抢占”是否是一个可行的优化思路，我们首先需要弄明白，主线程被抢占的程度会有多大？</p>
<p>我们可以使用 Demo 制造一些极端场景，了解极端场景下，主线程有多少比例会被其他线程抢占，因此有了如下 Demo 实验：</p>
<p>实验组1：</p>
<ul>
<li>异步线程 QoS：DispatchQoS.userInteractive</li>
<li>代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> _ <span class="hljs-keyword">in</span> <span class="hljs-number">1.</span>.<span class="hljs-number">.100</span> &#123;
    <span class="hljs-keyword">let</span> queue = <span class="hljs-title class_">DispatchQueue</span>.<span class="hljs-title function_">init</span>(<span class="hljs-attr">label</span>: <span class="hljs-string">"serialQueue"</span>, <span class="hljs-attr">qos</span>: .<span class="hljs-property">userInteractive</span>)
    queue.<span class="hljs-property">async</span> &#123;
        <span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>qos_class_self 数值：33</li>
<li>主线程 Preempted + Runnable 占比：74%</li>
</ul>
<p>实验组2：</p>
<ul>
<li>异步线程 QoS：不指定 QoS 或 DispatchQoS.userInitiated</li>
<li>代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> _ <span class="hljs-keyword">in</span> <span class="hljs-number">1.</span>.<span class="hljs-number">.100</span> &#123;
    <span class="hljs-keyword">let</span> queue = <span class="hljs-title class_">DispatchQueue</span>.<span class="hljs-title function_">init</span>(<span class="hljs-attr">label</span>: <span class="hljs-string">"serialQueue"</span>)
    queue.<span class="hljs-property">async</span> &#123;
        <span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>qos_class_self 数值：25</li>
<li>主线程 Preempted + Runnable 占比：73%</li>
</ul>
<p>实验组3：</p>
<ul>
<li>异步线程 QoS：DispatchQoS.utility</li>
<li>代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> _ <span class="hljs-keyword">in</span> <span class="hljs-number">1.</span>.<span class="hljs-number">.100</span> &#123;
    <span class="hljs-keyword">let</span> queue = <span class="hljs-title class_">DispatchQueue</span>.<span class="hljs-title function_">init</span>(<span class="hljs-attr">label</span>: <span class="hljs-string">"serialQueue"</span>, <span class="hljs-attr">qos</span>: .<span class="hljs-property">utility</span>)
    queue.<span class="hljs-property">async</span> &#123;
        <span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>qos_class_self 数值：17</li>
<li>主线程 Preempted + Runnable 占比：1.3%</li>
</ul>
<p>实验组4：</p>
<ul>
<li>异步线程 QoS：DispatchQoS.background</li>
<li>代码：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> _ <span class="hljs-keyword">in</span> <span class="hljs-number">1.</span>.<span class="hljs-number">.100</span> &#123;
    <span class="hljs-keyword">let</span> queue = <span class="hljs-title class_">DispatchQueue</span>.<span class="hljs-title function_">init</span>(<span class="hljs-attr">label</span>: <span class="hljs-string">"serialQueue"</span>, <span class="hljs-attr">qos</span>: .<span class="hljs-property">background</span>)
    queue.<span class="hljs-property">async</span> &#123;
        <span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>qos_class_self 数值：9</li>
<li>主线程 Preempted + Runnable 占比：1.3%</li>
</ul>
<p>⬇️ 不指定 QoS 下，一个极端 Demo，启动期间主线程长时间处于 preempted 状态，一直无法得到 running 的机会</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5feea2d615154941bce3b28c9402feba~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从中我们能看到几个结论：</p>
<ol>
<li>不指定 QoS 时，自行创建的 GCD queue 的 QoS 是 User-Initiated</li>
</ol>

<ol start="2">
<li>User-Initiated 及以上优先级，对主线程会有严重抢占现象；而 Utility 和 Background 则几乎不会抢占主线程。</li>
</ol>
<p>另外，我们也做测试验证了，pthread_create 创建的线程，也有类似的抢占现象。</p>
<h1 data-id="heading-2">QoS 和 Priority</h1>
<p>看到 iPhone 7p 上主线程被其他线程抢占，我们可能会有疑问：主线程不应该是优先级最高的么？怎么还会被其他线程抢占？</p>
<p>这里，我们需要理解一下 QoS 和线程 priority 两个概念。</p>
<p>QoS（quality of service）意指服务质量，它影响线程优先级（priority），也影响 I/O 吞吐、 CPU 吞吐等指标[3]。开发者可以用 qos_class_self() 接口获得当前线程 / 队列的 QoS。</p>
<p>苹果对于每个任务应该选用哪个 QoS，也有一些指导意见[4]：</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5cb62683004424fb046e50bd7302344~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>QoS 和 priority 确实有对应关系，参考 xnu 源码和实验结果，对应关系为：</p>

























<table><thead><tr><th><strong>QoS</strong></th><th><strong>Priority</strong></th></tr></thead><tbody><tr><td>User-Interactive</td><td>46，对于 UI 线程是 47</td></tr><tr><td>User-Initiated</td><td>37</td></tr><tr><td>Utility</td><td>20</td></tr><tr><td>Background</td><td>4</td></tr></tbody></table>
<p>同时，线程的 priority 会随着执行动态调整。测试中我们会发现，主线程的 priority 在运行开始时是 QoS User-Interactive 对应的 47，但随着运行会出现下降的情况。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f91eecb0f7c423ab2197e7d9b445872~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方文档[5]中解释了线程 priority 变化的原因，priority 由 Mach scheduler 控制，为了防止计算密集的线程垄断资源，各个线程的 priority 会实时调整。</p>
<blockquote>
<p>All of these mechanisms are operating continually in the Mach scheduler. This means that threads are frequently moving up or down in priority based upon their behavior and the behavior of other threads in the system.</p>
</blockquote>
<p>进一步阅读 xnu 内核的源码[6]，我们发现，线程 priority 的变化，是由各个 Mach scheduler 实现的 compute_timeshare_priority 接口控制的。在 iOS 使用的 Mach scheduler 中，compute_timeshare_priority 为同一个实现 sched_compute_timeshare_priority。线程调度时的 priority，会在线程固有 priority 的基础上，结合当前线程的 CPU 占用情况和当前设备的整体负载进行调整。</p>
<p>在这个实现中，我们能看到 Mach scheduler 对 priority 的调整会有一个极限：对于原先 priority = 47 的线程来说，向下调整的极限是 47 - ((BASEPRI_FOREGROUND - BASEPRI_DEFAULT) + 2) = 29。这和我们用多个设备测试到的结果吻合：主线程执行时，priority 的最低值是 29，依然高于 Utility 对应的 priority 20。</p>
<p>这也解释了，为什么 Demo 中当异步线程的 QoS 是 Utility 时，就几乎无法对主线程造成抢占。</p>
<h1 data-id="heading-3">优化落地</h1>
<p>通过 Demo 实验，一个启动优化思路产生了：在飞书中，大量异步队列的 QoS 是 User-Initiated，尽管这一 QoS 低于主线程的 User-Interactive，但依然可能对主线程造成抢占；那么，如果将异步队列的 QoS 调低到 Utility，是不是就可以优先保障主线程执行，让首屏更早展现出来？</p>
<p>经过一些粗暴的实验，我们证实了飞书在这个思路上存在优化空间。但另一个问题随之而来：如何兼顾首屏、消息列表首刷等多个指标？</p>
<p>考虑消息列表首刷的场景：获取到最新的消息，不仅仅需要主线程构建 UI，还需要依赖数据库读取、网络请求等异步操作。如果我们粗暴地将所有异步队列的 QoS 调低，首屏确实能更快展现，但消息列表的首刷则随着异步操作的变慢更劣化了。这对用户体验反而带来了负向影响。</p>
<p>梳理出哪些异步操作是首刷依赖的，确保这些队列的 QoS ，是优化中非常重要的一环。我们首先通过不断用 Instruments 测试、阅读代码梳理出了首版白名单队列，并在线下和线上验证了首屏、首刷等关键指标的优化收益。在后来的迭代中，我们又开发了线下工具，通过在线下 hook dispatch_async 等函数，记录下首刷等时机依赖的 GCD 队列，达成了白名单队列自动生成的能力。</p>
<h1 data-id="heading-4">效果分析</h1>
<p>这一优化在线上产生了不错的体验优化效果：</p>
<ol>
<li>
<h3 data-id="heading-5"><strong>启动首屏展现时间优化 100ms</strong></h3>
</li>
</ol>
<p>通过调整异步线程的 QoS，启动期间主线程 CPU 抢占现象有明显降低。更多计算资源集中到主线程，使得首屏展示速度明显加快。</p>
<ol start="2">
<li>
<h3 data-id="heading-6"><strong>消息列表首刷时间优化 1500ms</strong></h3>
</li>
</ol>
<p>通过对消息列表首刷依赖的任务的分析，我们调低了无关线程的 QoS，这也让首刷依赖的数据库读取、网络请求等任务得到了更多资源，加速了它们的执行。</p>
<h1 data-id="heading-7">总结</h1>
<p>“增加并发”在一定范围内可以作为启动优化的方案，但在低端机上，CPU 已经成为瓶颈，并发时异步线程对主线程的抢占也需要引起重视。</p>
<p>GCD 提供了四种 QoS 给开发者使用，官方也为这四种 QoS 提供了最佳实践建议。</p>
<p>经过评测和源码推理，User-Interactive 和 User-Initiated 对主线程有明显抢占，Utility 和 Background 对主线程的抢占极少。开发者创建的 GCD 队列，默认的 QoS 实际为 User-Initiated。因此在启动期间（或者任何耗时敏感期间），与启动无直接关系的 queue，应该主动设置为 Utility 或 Background，减少对主线程的抢占。</p>
<p>通过飞书上落地优化，我们能得出结论：对线程或 GCD queue 调整 QoS，能在不改变启动业务逻辑的情况下取得显著收益。</p>
<p>当然，比事后优化更好的操作，是在编码时就充分了解不同 QoS 的行为特性，选用最适合的 QoS。</p>
<p><strong>参考文献</strong></p>
<p>[1] Apple A10 </p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FApple_A10" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Apple_A10" ref="nofollow noopener noreferrer">en.wikipedia.org/wiki/Apple_…</a></p>
<p>[2] Apple A14</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FApple_A14" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Apple_A14" ref="nofollow noopener noreferrer">en.wikipedia.org/wiki/Apple_…</a></p>
<p>[3] 《*OS Internals》Chapter 6</p>
<p>[4] Prioritize Work with Quality of Service
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FPerformance%2FConceptual%2FEnergyGuide-iOS%2FPrioritizeWorkWithQoS.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html" ref="nofollow noopener noreferrer">developer.apple.com/library/arc…</a></p>
<p>[5]Why Did My Thread Priority Change?</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FDarwin%2FConceptual%2FKernelProgramming%2Fscheduler%2Fscheduler.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/scheduler/scheduler.html" ref="nofollow noopener noreferrer">developer.apple.com/library/arc…</a></p>
<p>[6] xnu 源码 sched_compute_timeshare_priority </p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fapple-oss-distributions%2Fxnu%2Fblob%2Fe7776783b89a353188416a9a346c6cdb4928faad%2Fosfmk%2Fkern%2Fpriority.c%23L558" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/apple-oss-distributions/xnu/blob/e7776783b89a353188416a9a346c6cdb4928faad/osfmk/kern/priority.c#L558" ref="nofollow noopener noreferrer">github.com/apple-oss-d…</a></p>
<h1 data-id="heading-8">加入我们</h1>
<p>字节跳动 APM 中台目前致力于提升整个集团内全系产品的性能和稳定性表现，技术栈覆盖 iOS/Android/Server/Web/Hybrid/PC/游戏/小程序等，工作内容包括但不限于性能稳定性监控，问题排查，深度优化，防劣化等。长期期望为业界输出更多更有建设性的问题发现和深度优化手段。欢迎对字节APM 团队职位感兴趣的同学投递简历到邮箱<a href="https://link.juejin.cn/?target=mailto%3Afengyadong%40bytedance.com" target="_blank" title="mailto:fengyadong@bytedance.com" ref="nofollow noopener noreferrer">fengyadong@bytedance.com</a>。</p></div>  
</div>
            