
---
title: 'iOS开发 -卡死崩溃监控原理及最佳实践'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a1a6f4f50a48d1ac195856f5dae68f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 23:39:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a1a6f4f50a48d1ac195856f5dae68f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>字节跳动技术团队</p>
<p>参考：/ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank">Github</a> /</p>
<p>不同于 Android 系统中的卡死（ANR）问题，目前业界对 iOS 系统中 App 发生的卡死崩溃问题并无成熟的解决方案，主要原因是：</p>
<ol>
<li>
<p>通常 App 卡死时间超过 20s 之后会触发操作系统的保护机制，发生崩溃，此时在用户的设备中能找到操作系统生成的卡死崩溃日志，但是因为 iOS 系统封闭生态的关系，App 层面没有权限拿到卡死崩溃的日志。</p>
</li>
<li>
<p>一般而言用户遇到卡死问题的时候并没有耐心等待那么久的时间，可能在卡住 5s 时就已经失去耐心，直接手动关闭应用或者直接将应用退到后台，因此这两种场景下系统也就不会生成卡死崩溃日志。</p>
</li>
</ol>
<p>由于上面提到的两个原因，目前业界 iOS 生产环境中的卡死监控方案其实主要是基于卡顿监控，即当用户在使用 App 的过程中页面响应时间超过一定的卡顿的阈值（一般是几百 ms）之后判定为一次卡顿，然后抓取到当时现场的调用栈并且上报到后台分析。这种方案的缺陷主要体现在：</p>
<ol>
<li>
<p>没有将比较轻微的卡顿问题和严重的卡死问题区分开，导致上报的问题数量太多，很难聚焦到重点。实际上这部分问题对用户体验的伤害其实是远远大于卡顿的。</p>
</li>
<li>
<p>因为一些使用低端机型的用户更容易在短时间内遇到频繁的卡顿，但是调用栈抓取，日志写入和上报等监控手段都是性能有损的，这也是卡顿监控方案在生产环境中一般只能小流量而不能全量的原因。</p>
</li>
<li>
<p>试想一次卡顿持续了 100ms，前 99ms 都卡在 A 方法的执行上，但是最后 1ms 刚好切换到了 B 方法在执行，这时候卡顿监控抓到的调用栈是 B 方法的调用栈，其实 B 方法并不是造成卡顿的主要原因，这样也就造成了误导。</p>
</li>
</ol>
<p>基于上述的痛点，字节跳动 APM 中台团队自研了一套专门用于定位生产环境中的卡死崩溃的解决方案，本文将详细的介绍该方案的思路和具体实现，以及通过本方案上线后总结出来的一些典型问题和最佳实践，期望对大家有所启发。</p>
<h1 data-id="heading-0">卡死崩溃背景介绍</h1>
<h2 data-id="heading-1">什么是 watchdog</h2>
<p>如果某一天我们的 App 在启动时卡住大概 20s 然后崩溃之后，从设备中导出的系统崩溃日志很可能是下面这种格式：</p>
<pre><code class="copyable">Exception Type:  EXC_CRASH (SIGKILL)Exception Codes: 0x0000000000000000, 0x0000000000000000Exception Note:  EXC_CORPSE_NOTIFYTermination Reason: Namespace ASSERTIOND, Code 0x8badf00dTriggered by Thread:  0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面就其中最重要的前 4 行信息逐一解释：</p>
<ol>
<li>Exception Type</li>
</ol>
<p><code>EXC_CRASH</code>：Mach 层的异常类型，表示进程异常退出。</p>
<p><code>SIGKILL</code>：BSD 层的信号，表示进程被系统终止，而且这个信号不能被阻塞、处理和忽略。这时可以查看 <code>Termination Reason</code> 字段了解终止的原因。</p>
<ol>
<li>Exception Codes</li>
</ol>
<p>这个字段一般用不上，当崩溃报告包含一个未命名的异常类型时，这个异常类型将用这个字段表示，形式是十六进制数字。</p>
<ol>
<li>Exception Note</li>
</ol>
<p><code>EXC_CORPSE_NOTIFY</code> 和 <code>EXC_CRASH</code> 定义在同一个文件中，意思是进程异常进入 CORPSE 状态。</p>
<ol>
<li>Termination Reason</li>
</ol>
<p>这里主要关注 <code>Code 0x8badf00d</code>，可以在苹果的官方文档中查看到 <code>0x8badf00d</code> 意味着 App <code>ate bad food</code>，表示进程因为 <code>watchdog</code> 超时而被操作系统结束进程。通过上述已经信息可以得出 <code>watchdog</code> 崩溃的定义：</p>
<blockquote>
<p>在iOS平台上，App如果在启动、退出或者响应系统事件时因为耗时过长触发系统保护机制，最终导致进程被强制结束的这种异常定义为watchdog类型的崩溃。</p>
</blockquote>
<p>所谓的 <code>watchdog</code> 崩溃也就是本文所说的卡死崩溃。</p>
<h2 data-id="heading-2">为什么要监控卡死崩溃</h2>
<p>大家都知道在客户端研发中，因为会阻断用户的正常使用，闪退已经是最严重的 bug，会直接影响留存，收入等各项最核心的业务指标。之前大家重点关注的都是诸如 <code>unrecognized selector</code>、<code>EXC_BAD_ACCESS</code> 等可以在 App 进程内被捕获的崩溃（下文中称之为普通崩溃），但是对于 <code>SIGKILL</code> 这类因为进程外的指令强制退出导致的异常，原有的监控原理是覆盖不到的，也导致此类崩溃在生产环境中被长期忽视。除此之外，还有如下理由：</p>
<ol>
<li>
<p>因为卡死崩溃最常见发生于 App 启动阶段，用户在开屏页面卡住 20s 后什么都做不了紧接着 App 就闪退了。这种体验对用户的伤害比普通的崩溃更加严重。</p>
</li>
<li>
<p>在卡死监控上线之初，今日头条 App 每天卡死崩溃发生的量级大概是普通崩溃的 3 倍，可见如果不做任何治理的话，这类问题的发生量级是非常大的。</p>
</li>
<li>
<p>OOM 崩溃也是由 <code>SIGKILL</code> 异常信号最终触发的，目前 OOM 崩溃主流的监控原理还是排除法。不过传统方案在做排除法的时候漏掉了一类量级非常大的其他类型的崩溃就是这里的卡死崩溃。如果能准确的监控到卡死崩溃，也同样能大大提高 OOM 崩溃监控的准确性。关于 OOM 崩溃的具体监控原理和优化思路可以参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI1MzYzMjE0MQ%3D%3D%26mid%3D2247486858%26idx%3D1%26sn%3Dec5964b0248b3526836712b26ef1b077%26chksm%3De9d0c668dea74f7e1e16cd5d65d1436c28c18e80e32bbf9703771bd4e0563f64723294ba1324%26token%3D1483621236%26lang%3Dzh_CN%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247486858&idx=1&sn=ec5964b0248b3526836712b26ef1b077&chksm=e9d0c668dea74f7e1e16cd5d65d1436c28c18e80e32bbf9703771bd4e0563f64723294ba1324&token=1483621236&lang=zh_CN&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">iOS 性能优化实践：头条抖音如何实现 OOM 崩溃率下降 50%+</a></p>
</li>
</ol>
<p>因此，基于以上信息我们可以得出结论：卡死崩溃的监控和治理是非常有必要的。经过近 2 年的监控和治理，目前今日头条 App 卡死崩溃每天发生的量级大致和普通崩溃持平。</p>
<h1 data-id="heading-3">卡死崩溃监控原理</h1>
<h2 data-id="heading-4">卡顿监控原理</h2>
<p>其实从用户体验出发的话，卡死的定义就是长时间卡住并且最终也没有恢复的那部分卡顿，那么下面我们就先回顾一下卡顿监控的原理。我们知道在 iOS 系统中，主线程绝大部分计算或者绘制任务都是以 <code>runloop</code> 为单位周期性被执行的。单次 <code>runloop</code> 循环如果时长超过 16ms，就会导致 UI 体验的卡顿。那如何检测单次 <code>runloop</code> 的耗时呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a1a6f4f50a48d1ac195856f5dae68f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上图可以看到，如果我们注册一个 <code>runloop</code> 生命周期事件的观察者，那么在 <code>afterWaiting=>beforeTimers，beforeTimers=>beforeSources</code> 以及<code>beforeSources=>beforeWaiting</code> 这三个阶段都有可能发生耗时操作。所以对于卡顿问题的监控原理大概分为下面几步：</p>
<ol>
<li>
<p>注册 <code>runloop</code> 生命周期事件的观察者。</p>
</li>
<li>
<p>在 <code>runloop</code> 生命周期回调之间检测耗时，一旦检测到除休眠阶段之外的其他任意一个阶段耗时超过我们预先设定的卡顿阈值，则触发卡顿判定并且记录当时的调用栈。</p>
</li>
<li>
<p>在合适的时机上报到后端平台分析。</p>
</li>
</ol>
<p>整体流程如下图所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f47599571dd474ab60b76e6d9d315cf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">如何判定一次卡顿为一次卡死</h2>
<p>其实通过上面的一些总结我们不难发现，长时间的卡顿最终无论是触发了系统的卡死崩溃，还是用户忍受不了主动结束进程或者退后台，他们的共同特征就是发生了长期时间卡顿且最终没有恢复，阻断了用户的正常使用流程。</p>
<p>基于这个理论的指导，我们就可以通过下面这个流程来判定某次卡顿到底是不是卡死：</p>
<ol>
<li>
<p>某次长时间的卡顿被检测到之后，记录当时所有线程的调用栈，存到数据库中作为卡死崩溃的怀疑对象。</p>
</li>
<li>
<p>假如在当前 <code>runloop</code> 的循环中进入到了下一个活跃状态，那么该卡顿不是一次卡死，就从数据库中删除该条日志。本次使用周期内，下次长时间的卡顿触发时再重新写入一条日志作为怀疑对象，依此类推。</p>
</li>
<li>
<p>在下次启动时检测上一次启动有没有卡死的日志（用户一次使用周期最多只会发生一次卡死），如果有，说明用户上一次使用期间最终遇到了一次长时间的卡顿，且最终 runloop 也没能进入下一个活跃状态，则标记为一次卡死崩溃上报。</p>
</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90211edbddd049e3a424ecc9090cfe38~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过这套流程分析下来，我们不仅可以检测到系统的卡死崩溃，也可以检测到用户忍受不了长时间卡顿最终杀掉应用或者退后台之后被系统杀死等行为，这些场景虽然并没有实际触发系统的卡死崩溃，但是严重程度其实是等同的。也就是说本文提到的卡死崩溃监控能力是系统卡死崩溃的超集。</p>
<h2 data-id="heading-6">卡死时间的阈值如何确定</h2>
<p>系统的卡死崩溃日志格式截取部分如下：</p>
<pre><code class="copyable">Exception Type:  EXC_CRASH (SIGKILL)Exception Codes: 0x0000000000000000, 0x0000000000000000Exception Note:  EXC_CORPSE_NOTIFYTerminationReason: Namespace ASSERTIOND, Code 0x8badf00dTriggered by Thread:  0Termination Description: SPRINGBOARD, scene-create watchdog transgression: application<com.ss.iphone.article.News>:2135 exhausted real (wall clock) time allowance of 19.83 seconds
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 iOS 系统的保护机制只有在 App 卡死时间超过一个异常阈值之后才会触发，那么这个卡死时间的阈值就是一个非常关键的参数。</p>
<p>遗憾的是，目前没有官方的文档或者 api，可以直接拿到系统判定卡死崩溃的阈值。这里 <code>exhausted real (wall clock) time allowance of 19.83 seconds</code> 其中的 19.83 并不是一个固定的数字，在不同的使用阶段，不同系统版本的实现里都可能有差异，在一些系统的崩溃日志中也遇到过 10s 的 case。</p>
<p>基于以上信息，为了覆盖到大部分用户可以感知到的场景，屏蔽不同系统版本实现的差异，我们认为系统触发卡死崩溃的时间阈值为 10s，实际上有相当一部分用户在遇到 App 长时间卡顿的时候会习惯性的手动结束进程重启而不是一直等待，因此这个阈值不宜过长。为了给触发卡死判定之后的抓栈，日志写入等操作预留足够的时间，所以最终本方案的卡死时间阈值确定为 8s。发生 8s 卡死的概率比发生几百 ms 卡顿的概率要低的多，因此该卡死监控方案并没有太大的性能损耗，也就可以在生产环境中对全量用户开放。</p>
<h2 data-id="heading-7">如何检测到用户一次卡死的时间</h2>
<p>在卡死发生之后，实际上我们也会关注一次卡死最终到底卡住了多久，卡死时间越长，对用户使用体验的伤害也就越大，更应该被高优解决。</p>
<p>在触发卡死阈值之后我们可以再以一个时间间隔比较短的定时器（目前策略默认 1s，线上可调整），每隔 1s 就检测当前 <code>runloop</code> 有没有进入到下一个活跃状态，如果没有，则当前的卡死时间就累加 1s，用这种方式即使最终发生了闪退也可以逼近实际的卡死时间，误差不超过 1s，最终的卡死时间也会写入到日志中一起上报。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b9158b4daa47379b082e97bc26e287~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是这种方案在上线后遇到了一些卡死时长特别长的 case，这种问题多发生在 App 切后台的场景。因为在后台情况下，App 的进程会被挂起(suspend)后，就可能被判定为持续很久的卡死状态。而我们在计算卡死时间的时候，采用的是现实世界的时间差，也就是说当前 App 在后台被挂起 10s 后又恢复时，我们会认为 App 卡死了 10s，轻易的超过了我们设定的卡死阈值，但其实 App 并没有真正卡死，而是操作系统的调度行为。这种误报常常是不符合我们的预期的。误报的场景如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e6199a830b54ba4bb9748c0ba2516e1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">如何解决主线程调用栈可能有误报的问题</h2>
<p>为了解决上面的问题，我们采用多段等待的方式来降低线程调度、挂起导致的程序运行时间与现实时间不匹配的问题，以下图为例。在 8s 的卡死阈值前，采用间隔等待的方式，每隔 1s 进行一次等待。等待超时后对当前卡死的时间进行累加 1s。如果在此过程中，App 被挂起，无论被挂起多久，再恢复时最多会造成 1s 的误差，这与之前的方案相比极大的增加了稳定性和准确性。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6da5b02ada0470f8d63643a1f4c4ced~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外，待卡死时间超过了设定的卡死阈值后，会对全线程进行抓栈。但是仅凭这一时刻的线程调用栈并不保证能够准确定位问题。因为此时主线程执行的可能是一个非耗时任务，真正耗时的任务已经结束；或者在后续会发生一个更加耗时的任务，这个任务才是造成卡死的关键。因此，为了增加卡死调用栈的置信度，在超过卡死阈值后，每隔 1s 进行一次间隔等待的同时，对当前主线程的堆栈进行抓取。为了避免卡死时间过长造成的线程调用栈数量膨胀，最多会保留距离 App 异常退出前的最近 10 次主线程调用栈。经过多次间隔等待，我们可以获取在 App 异常退出前主线程随着时间变化的一组函数调用栈。通过这组函数调用栈，我们可以定位到主线程真正卡死的原因，并结合卡死时间超过阈值时获取的全线程调用栈进一步定位卡死原因。</p>
<p>最终的监控效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98c3620ea779427495eba354cf4ea317~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为图片大小的限制，这里仅仅截了卡死崩溃之前最后一次的主线程调用栈，实际使用的时候可以查看崩溃之前一段时间内每一秒的调用栈，如果发现每一次主线程的调用栈都没有变化，那就能确认这个卡死问题不是误报，例如这里就是一次异常的跨进程通信导致的卡死。</p>
<h1 data-id="heading-9">卡死崩溃常见问题归类及最佳实践</h1>
<h2 data-id="heading-10">多线程死锁</h2>
<h3 data-id="heading-11">问题描述</h3>
<p>比较常见的就是在 <code>dispatch_once</code> 中子线程同步访问主线程，最终造成死锁的问题。如上图所示，这个死锁的复现步骤是：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/530cbfcb49894c85b035409d845220b8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>子线程先进入 <code>dispatch_once</code> 的 block 中并加锁。</p>
</li>
<li>
<p>然后主线程再进入 <code>dispatch_once</code> 并等待子线程解锁。</p>
</li>
<li>
<p>子线程初始化时触发了 <code>CTTelephonyNetworkInfo</code> 对象初始化抛出了一个通知却要求主线程同步响应，这就造成了主线程和子线程因为互相等待而死锁，最终触发了卡死崩溃。</p>
</li>
</ol>
<p>这里的其实是踩到了 <code>CTTelephonyNetworkInfo</code> 一个潜在的坑。如果这里替换成一段 <code>dispatch_sync</code> 到 <code>dispatch_get_main_queue()</code>的代码，效果还是等同的，同样有卡死崩溃的风险。</p>
<h3 data-id="heading-12">最佳实践</h3>
<ol>
<li>
<p><code>dispatch_once</code> 中不要有同步到主线程执行的方法。</p>
</li>
<li>
<p><code>CTTelephonyNetworkInfo</code> 最好在 <code>+load</code>方法或者 <code>main</code> 方法之前的其他时机提前初始化一个共享的实例，避免踩到子线程懒加载时候要求主线程同步响应的坑。</p>
</li>
</ol>
<h2 data-id="heading-13">主线程执行代码与子线程耗时操作存在锁竞争</h2>
<h3 data-id="heading-14">问题描述</h3>
<p>一个比较典型的问题是卡死在<code>-[YYDiskCache containsObjectForKey:]</code>，<code>YYDiskCache</code> 内部针对磁盘多线程读写操作，通过一个信号量锁保证互斥。通过分析卡死堆栈可以发现是子线程占用锁资源进行耗时的写操作或清理操作引发主线程卡死，问题发生时一般可以发现如下的子线程调用栈：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ea5711c02304891971ac4aacd236432~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">最佳实践</h3>
<ol>
<li>
<p>有可能存在锁竞争的代码尽量不在主线程同步执行。</p>
</li>
<li>
<p>如果主线程与子线程不可避免的存在竞争时，加锁的粒度要尽量小，操作要尽量轻。</p>
</li>
</ol>
<h2 data-id="heading-16">磁盘 IO 过于密集</h2>
<h3 data-id="heading-17">问题描述</h3>
<p>此类问题，表现形式可能多种多样，但是归根结底都是因为磁盘 IO 过于密集最终导致主线程磁盘 IO 耗时过长。典型 case:</p>
<ol>
<li>
<p>主线程压缩/解压缩。</p>
</li>
<li>
<p>主线程同步写入数据库，或者与子线程可能的耗时操作（例如 <code>sqlite</code> 的 <code>vaccum</code> 或者<code>checkpoint</code> 等）复用同一个串行队列同步写入。</p>
</li>
<li>
<p>主线程磁盘 IO 比较轻量，但是子线程 IO 过于密集，常发生于一些低端设备。</p>
</li>
</ol>
<h3 data-id="heading-18">最佳实践</h3>
<ol>
<li>
<p>数据库读写，文件压缩/解压缩等磁盘 IO 行为不放在主线程执行。</p>
</li>
<li>
<p>如果存在主线程将任务同步到串行队列中执行的场景，确保这些任务不与子线程可能存在的耗时操作复用同一个串行队列。</p>
</li>
<li>
<p>对于一些启动阶段非必要同步加载并且有比较密集磁盘 IO 行为的 SDK，如各种支付分享等第三方 SDK 都可以延迟，错开加载。</p>
</li>
</ol>
<h2 data-id="heading-19">系统 api 底层实现存在跨进程通信</h2>
<h3 data-id="heading-20">问题描述</h3>
<p>因为跨进程通信需要与其他进程同步，一旦其他进程发生异常或者挂起，很有可能造成当前 App 卡死。典型 case：</p>
<ol>
<li>
<p><code>UIPasteBoard</code>，特别是 <code>OpenUDID</code>。因为 <code>OpenUDID</code> 这个库为了跨 App 可以访问到相同的 UDID，通过创建剪切板和读取剪切板的方式来实现的跨 App 通信，外部每次调用 <code>OpenUDID</code> 来获取一次 UDID，OpenUDID 内部都会循环 100 次，从剪切板获取 UDID，并通过排序获得出现频率最高的那个 UDID，也就是这个流程可能最终会导致访问剪切板卡死。</p>
</li>
<li>
<p><code>NSUserDefaults</code> 底层实现中存在直接或者间接的跨进程通信，在主线程同步调用容易发生卡死。</p>
</li>
<li>
<p><code>[[UIApplication sharedApplication] openURL]</code>接口，内部实现也存在同步的跨进程通信。</p>
</li>
</ol>
<h3 data-id="heading-21">最佳实践</h3>
<ol>
<li>
<p>废弃 <code>OpenUDID</code> 这个第三方库，一些依赖了 <code>UIPaseteBoard</code> 的第三方 SDK 推动维护者下掉对 UIPasteBoard 的依赖并更新版本；或者将这些 SDK 的初始化统一放在非主线程，不过经验来看子线程初始化可能有 5%的卡死转化为闪退，因此最好加一个开关逐步放量观察。</p>
</li>
<li>
<p>对于 kv 类存储需求，如果重度的使用可以考虑 <code>MMKV</code>，如果轻度的使用可以参考 <code>firebase</code> 的实现自己重写一个更轻量的 UserDefaults 类。</p>
</li>
<li>
<p>iOS10 及以上的系统版本使用<code>[[UIApplication sharedApplication] openURL:options:completionHandler:]</code>这个接口替换，此接口可以异步调起，不会造成卡死。</p>
</li>
</ol>
<h2 data-id="heading-22">Objective-C Runtime Lock 死锁</h2>
<h3 data-id="heading-23">问题描述</h3>
<p>此类问题虽然出现概率不大，但是在一些复杂场景下也是时有发生。主线程的调用栈一般都会卡死在一个看似很普通的 OC 方法调用，非常隐晦，因此想要发现这类问题，卡死监控模块本身就不能用 OC 语言实现，而应该改为 C/C++。此问题一般多发于<code>_dyld_register_func_for_add_image</code> 回调方法中同步调用 OC 方法（先持有 dyld lock 后持有 OC runtime lock），以及 OC 方法同步调用 <code>objc_copyClassNamesForImage</code> 方法（先持有 OC runtime lock 后持有 dyld lock）。典型 case：</p>
<ol>
<li>dyld lock、 selector lock 和 OC runtime lock 三个锁互相等待造成死锁的问题。三个锁互相等待的场景如下图所示：</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f27d74ae82d4cd2a54d5fb5c2854fc1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>在某次迭代的过程中 APM SDK 内部判定设备是否越狱的实现改为依赖 <code>fork</code> 方法能否调用成功，但是 <code>fork</code> 方法会调用 <code>_objc_atfork_prepare</code>，这个函数会获取 objc 相关的 lock，之后会调用 <code>dyld_initializer</code>，内部又会获取 dyld lock，如果此时我们的某个线程已经持有了 dyld lock，在等待 OC runtime lock，就会引发死锁。</li>
</ol>
<h3 data-id="heading-24">最佳实践</h3>
<ol>
<li>
<p>慎用<code>_dyld_register_func_for_add_image</code> 和 <code>objc_copyClassNamesForImage</code> 这两个方法，特别是与 OC 方法同步调用的场景。</p>
</li>
<li>
<p>越狱检测，不依赖 <code>fork</code> 方法的调用。</p>
</li>
</ol></div>  
</div>
            