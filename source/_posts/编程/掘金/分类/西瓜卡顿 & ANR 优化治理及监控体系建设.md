
---
title: '西瓜卡顿 & ANR 优化治理及监控体系建设'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75e6e275778d4833b1b904082ccd53b0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 18:58:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75e6e275778d4833b1b904082ccd53b0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>卡顿 & ANR 在各 APP 中都是非常影响用户体验的问题，关于其的分析和治理一直也是个老生常谈的话题。过去调查卡顿 & ANR 问题主要依赖上报的堆栈和 traceInfo 文件，通过这些信息还原问题的现场情况。但是在实践过程中发现，现有监控机制下堆栈的抓取时机是晚于问题发生的，大部分情况获取到的是问题发生后某一瞬间的堆栈，随机性强，是不置信的，无法反映问题的真实现场情况，同一个问题可能聚合到不同堆栈中，无法清晰的归类和定位问题，这就使得很多开发者清楚原理，但到了具体 case 时无从下手，调查起来缺乏方向甚至因堆栈聚合的不置信而陷入了错误的排查方向，效率低下。另一方面，大多能够准确衡量性能的工具本身会带来严重耗时问题，无法用于线上，而性能问题大多发生于复杂的线上用户场景。所以，如何对卡顿 & ANR 进行有效的防治就是我们需要考虑的问题。</p>
<h2 data-id="heading-1">卡顿 & ANR 治理现状和痛点</h2>
<p>过去几年，在业务发展的同时积累了大量的卡顿 & ANR 问题，对用户的使用体验带来了极大的负面影响。随着治理工作的进行，现有的监控机制暴露出一定的问题，堆栈不置信、聚合错误、缺乏正确信息、缺乏有效防治策略，这些成了制约治理工作进行的瓶颈。</p>
<h3 data-id="heading-2">卡顿 & ANR 现状</h3>
<p>长期以来，新老问题的不断叠加，同时没有系统的进行相关防治工作使得数据指标常态高水位，影响的用户以及发生次数都很不乐观。</p>
<p>在治理之初，卡顿周均影响用户比例达到 10‰ 左右，受影响的用户平均 5 次卡顿，ANR 影响用户则常态高水位保持在 6‰ 左右，受影响用户平均 ANR 2 次，这些数据在公司的各大 APP 中都排名很差。</p>
<p>对问题进行筛查发现，问题呈现头部集中，整体分散的现象，TOP 2 问题占总体的 30%，其余问题零零散散的分布在 60000 个不同的堆栈聚合上，观察这些不同的堆栈聚合，TOP 2 问题落在了系统的堆栈上，同时很多小量级聚合并非直观上的耗时点，这些现象给我们初期的治理工作带来了很大的困扰，占比极大的 TOP 问题优先级最高，但是如何导致，需要如何优化，分散在 60000 个堆栈聚合上的问题应该如何切入。</p>
<p>另外，长期以来缺乏有效的增量问题防治能力。在开发、测试阶段没有专项测试，问题很少暴露，也缺乏持续跟进计划和问题复现定位能力，在灰度、线上等用户场景下报警策略单一，只有新增堆栈聚合情况下才会触发报警，实际运行中发现报警策略很少触发，大多情况下也无法消费。</p>
<h3 data-id="heading-3">卡顿 & ANR 检测机制及问题</h3>
<p>首先，我们来看一下 TOP 2 问题的堆栈表现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75e6e275778d4833b1b904082ccd53b0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09849f8dadc24a02b0e32d90be26e0e9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>TOP 2 问题聚合到了 nativePollOnce 和 nSyncAndDrawFrame 系统堆栈上，占比分别达到了 20% 和 10%，nativePollOnce 是主线程消息机制下的消息分发函数，nSyncAndDrawFrame 是页面的基础绘制函数，直观上看没有问题，对此我们在初期进行了一系列的常规分析和尝试。以 TOP 1 的 nativePollOnce 为例。首先，常规怀疑该方法本身耗时，分析了方法在 Java 层和 native 层的执行逻辑。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5f0e149f4654966840e95914f5d468a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到在 native 层有 epoll_wait 调用，通过在 C++ 层 hook 相关方法验证，没有发现问题。接着我们在 Java 层构造一个一直存在的 idleTask，使得消息队列空闲时就执行 idle 任务而不休眠，验证发现问题仍然存在。再看 Java 层逻辑。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/921eaf400ef84b9c821ca56de138b98c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这部分是关于同步屏障的处理，异步更新 UI 可能会导致同步屏障出现多线程问题而无法移除，验证后排除该可能。调查至此，并没有找到该问题的明确原因，排名第二的 nSyncAndDrawFrame 的问题与此类似，经过埋点调查，很多 nSyncAndDrawFrame 问题下的调用链路并不耗时。</p>
<p>此时，我们回过头来看一下目前的监控机制。对于卡顿 & ANR 的检测和分析，长期以来我们依赖于 NPTH 工具提供的能力。对于卡顿的监控，采用拦截消息调度流程，在消息执行前埋点计时，当耗时超过阈值时，则认为是一次卡顿，会进行堆栈抓取和上报工作。ANR 的监控则是通过定时轮询，在线程中每 500ms 定时和 AMS 进行交互，通过 AMS 的 Error 信息来判断是否发生 ANR，当确定发生 ANR 时，进行堆栈的抓取和信息的上报。</p>
<p>在实际分析解决问题时，以上不论卡顿还是 ANR，在现有检测机制下获取到的堆栈及其他信息都存在一定的缺陷，无法有效解决问题。</p>
<p>对于卡顿，由于是以 Message 为维度进行检测，当检测到 Message 超时发生卡顿时，拿到的堆栈是从 Message 开始到当前执行 Method 的堆栈链路。实际上 Message 中可能执行了几千个 Method，耗时点很可能是 Message 中的另外 Method 或者多个 Method 耗时堆积导致 Message 超时，这一点我们无法确认。因此知道 Message 耗时对我们排查问题帮助很小，我们还是无法定位到具体的可消费的耗时点，这就导致当前的卡顿数据无法快速消费。</p>
<p>对于 ANR，抓栈时机是定时轮询有 ANR 发生才进行的。一方面从发生 ANR 到开始抓栈到抓栈完成都有一定的时间间隔，除了少部分循环等待、锁等待等卡住场景能够相对准确抓到，大部分问题抓到堆栈和问题现场不匹配，堆栈会落在耗时点之后的调用链路上。另一方面对于那种多次耗时累积导致 ANR 的情况，单点的堆栈也无法定位问题。</p>
<p>在此基础上，我们接入了调度时序图，调度时序图就是主线程 MessageQueue 中的 Message 执行情况，包括已执行 Message、当前 Message 和待执行 Message，可以在 ANR 发生时一起上报。我们借助调度时序图来看 nativePollOnce 聚合下的 case：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afc148e2d19c4895942f346162074998~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，前边有 Message 耗时 42s，而上报的堆栈当前 Message 耗时很少，ANR 和当前 Message 没有关系。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1902b5d9ee849edbde209f2e197084b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是一个多次耗时累积导致 ANR 的问题，同样当前 Message 耗时很少。借助调度时序图我们可以得出结论，nativePollOnce 这类问题很可能和当前堆栈没有关系，聚合在 nativePollOnce 是因为消息调度是执行频率最高的函数，抓栈时堆栈落到 nativePollOnce 的频率是最高的，这个堆栈信息对于我们解决问题是无用的，那么是否可以借助调度时序图解决问题呢？</p>
<p>很遗憾，也不可以。调度时序图展示的是 Message 级的耗时情况，类似卡顿，我们即使知道了哪一个 Message 耗时，但 Message 中执行的 Method 非常多，而且很多都是系统级 Message，我们无法定位具体是哪些 Method 耗时。另外，单点的堆栈也无法定位问题，这种情况无论当前 Message 是否耗时都无法定位问题，因为问题的原因和已执行的耗时 Message 是息息相关的。</p>
<p>经过以上从原理分析和初期的案例调研，我们确认了基于目前的卡顿和 ANR 机制及工具，无法获取正确的问题堆栈聚合，对于多次耗时导致的问题更是无从下手，无法有效定位问题和解决问题。</p>
<h2 data-id="heading-4">增量问题的防治</h2>
<p>在优化工作中，新增问题的防治和存量问题的治理同样重要，只有堵住新增问题，线上的情况才会随着存量问题解决越来越好。</p>
<p>关于增量问题，之前并无有效的防治手段，仅有的线下测试和灰度/线上新增问题线上报警也收效甚微。线下测试主要是开发测试阶段针对功能的测试以及一系列自动化测试，这些测试并非针对卡顿 & ANR 等性能问题设计，对相关问题敏感度和关注度不够，同时机型和触达的场景不足使得暴露出的问题很少，而且缺乏必要的分析能力和分析工具，现场可用信息很少。</p>
<p>而灰度/线上新增问题报警策略，准确率和可消费性都不高。只有出现新的堆栈聚合才会触发报警，而通过对现状的分析可知，除了个别死锁、循环等待等 case 外，大部分 case 的堆栈具有很大的随机性，要么落到 nativePollOnce/nSyncAndDrawFrame 等无法消费的系统堆栈，要么分散到各类其他业务堆栈，分析人员拿到的信息大都是不置信的，这样很可能发生这样的情况：</p>
<ul>
<li>触发报警的堆栈聚合真实原因不是新增</li>
<li>新增问题导致的问题不触发报警</li>
<li>问题无法消费</li>
</ul>
<p>总之，抓栈随机性决定了我们无法定位真实原因，也就无法确定新增问题的有效性，这就使得很多新增问题被带入线上，我们也在这种低效的恶性循环中不断重复。</p>
<h2 data-id="heading-5">我们的诉求</h2>
<p>经过以上的分析和调研，我们的痛点可以归结为以下三类：</p>
<ul>
<li>对于单点问题，无法定位到真实堆栈。</li>
<li>对于多点耗时问题，无法还原问题现场。</li>
<li>缺乏有效的增量问题防治手段。</li>
</ul>
<p>现有的问题现场堆栈对于由于抓栈的不准确，无论对单点问题排查还是多段耗时问题排查都意义不大，无法正确的还原现场信息，这使得我们的问题排查优化进展缓慢，甚至偏离正常的方向。现有的卡顿及调度时序图等工具都是以 Message 为统计粒度，无法提供真正可优化的耗时定位，而现有的以 Method 为统计粒度的工具由于性能和稳定性问题都只能运行在线下。为此，我们希望有一套能够高效运行在线上的 Method trace 工具，用于卡顿及 ANR 的检测，以 Method 耗时为统计粒度，获取卡顿/ANR 时用户当前和之前一段时间内的 Method 执行耗时情况，这样我们可以完整的呈现问题发生时刻以及之前一段时间的 Method 执行耗时情况，高效清晰的定位问题症结所在。</p>
<p>针对增量问题的防治，由于现有的能力无法识别问题是否新增，导致在错误的方向上耗费太多精力，而真正的问题无法被发现从而带入线上，为此我们需要搭建增量问题的防治体系，去体系化前置化的完成增量问题的监控、有效信息的提供、问题的分发，前置化预防才能避免问题被带入线上，体系化才能更高效更全面的最大限度发现问题，同时将增量问题的防治体系建设和问题监控解决能力建设结合起来，建立一个自动化、前置化、发现问题全面、易消费、分发及时的的全链路体系。</p>
<h2 data-id="heading-6">监控体系建设</h2>
<p>在目前的监控体系下，堆栈抓取不准确，堆栈聚合存在问题，大量聚合在了无意义的堆栈上，现有的工具体系下，分析成本极高，大多数问题无法得到有效消费，卡顿和 ANR 指标长期高位，这就要求我们尽快找到破解之法。</p>
<p>诚然，最终导致弹出 ANR 弹窗的诱因很多，但是归根结底，根本原因都是执行超时，而我们最需要关注的也是那些耗时较高的 Method，当 Method 耗时减少后，相应的触发 ANR 的几率也会随之减少，为此我们就需要找出那些真正耗时卡顿的地方并对其进行优化。</p>
<p>针对以上的痛点和诉求，我们重新梳理了思路，对比了现有方案的优缺点后，取长补短，开发了基于 Method 的高性能线上 trace 工具。在此基础上，我们针对 ANR、卡顿进行了方案升级和全方位的体系建设。</p>
<h3 data-id="heading-7">基于 Sliver 的 ANR 治理方案介绍</h3>
<p>针对 ANR，我们希望获取到发生 ANR 时前一段时间的堆栈记录，以快速的找出发生耗时的 Method 调用堆栈。</p>
<p>Sliver 采用采样的方式来定时获取堆栈，我们在 APP 启动时打开 Sliver 的监控能力，根据不同机型传入不同的采样值，通常在低端机采样值会大一些，在高端机采样值会小一些，这样最大限度降低获取 trace 本身对性能的影响，Sliver 定时抓取堆栈，并对获取到的堆栈做 diff 聚合、缓存以区分不同堆栈的关系。同时，通过 NPTH 的接口注册 ANR 的回调，当发生 ANR 时，回调函数中将缓存的堆栈 dump 到文件，同时将文件随 ANR 其他信息上报到 Sladar，这样我们就可以在对 case 的分析中使用精确的 trace 信息问题定位，下图说明了针对 ANR 的整体工作流程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3a91afd01be4932aaf9b022c866f5b3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将这一套流程运行起来，收集了相关 case，在同一个 case 拿到相关信息对比。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d71d2f5f6f654c699075bf80f53df2cf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6b5dc9f6fd3484d9505b2dbe47b07a0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d779ed1a4b56487485b30038d7325fe7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上三个图是同一个 case 中的不同信息，分别是堆栈、调度时序图、trace，通过 trace 能清晰看出问题的原因所在。</p>
<p>目前该方案已在线下、灰度、众测渠道常态开启，作用明显，如下：</p>
<ul>
<li>帮助新增问题的界定、归因，防止新增问题带入线上。</li>
<li>帮助存量问题的归因、定位，梳理清楚各错误堆栈聚合中的真正问题原因。</li>
<li>对于线下、众测等反馈较多渠道单点精准定位解决问题。</li>
</ul>
<p>整体上，该方案的上线，使得我们能够更清晰准确的定位问题原因，加快问题的流转解决，促进各类隐藏较深问题的快速解决。</p>
<h3 data-id="heading-8">卡顿问题的防治方案</h3>
<p>不同于 ANR 问题，卡顿问题的标准是我们自己定义的，卡顿以及多次卡顿的叠加是导致 ANR 以及影响性能的大项，现有的卡顿监控只能拿到单一的堆栈链路，无法完整还原当前卡顿产生现场全貌，基于此我们设计了基于 Sliver trace 的卡顿监控体系。</p>
<p>先看整体流程图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08c86e6bd0294fd9baea91d0caa3ea6d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要包含两个方面：</p>
<ul>
<li>检测方案</li>
</ul>
<p>在监控卡顿时，首先需要打开 Sliver 的 trace 记录能力，Sliver 采样记录 trace 执行信息，对抓取到的堆栈进行 diff 聚合和缓存。</p>
<p>同时基于我们的需要设置相应的卡顿阈值，以 Message 的执行耗时为衡量。对主线程消息调度流程进行拦截，在消息开始分发执行时埋点，在消息执行结束时计算消息执行耗时，当消息执行耗时超过阈值，则认为产生了一次卡顿。</p>
<ul>
<li>堆栈聚合策略</li>
</ul>
<p>当卡顿发生时，我们需要为此次卡顿准备数据，这部分工作是在端上子线程中完成的，主要是 dump trace 到文件以及过滤聚合要上报的堆栈。分为以下几步：</p>
<ul>
<li>拿到缓存的主线程 trace 信息并 dump 到文件中。</li>
<li>然后从文件中读取 trace 信息，按照数据格式，从最近的方法栈向上追溯，找到当前 Message 包含的全部 trace 信息，并将当前 Message 的完整 trace 写入到待上传的 trace 文件中，删除其余 trace 信息。</li>
<li>遍历当前 Message trace，按照（Method 执行耗时 > Method 耗时阈值 & Method 耗时为该层堆栈中最耗时）为条件过滤出每一层函数调用堆栈的最长耗时函数，构成最后要上报的堆栈链路，这样特征堆栈中的每一步都是最耗时的，且最底层 Method 为最后的耗时大于阈值的 Method。</li>
</ul>
<p>之后，将 trace 文件和堆栈一同上报，这样的特征堆栈提取策略保证了堆栈聚合的可靠性和准确性，保证了上报到平台后堆栈的正确合理聚合，同时提供了进一步分析问题的 trace 文件。</p>
<p>上线后，我们通过和原卡顿体系进行效果对比：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e661fc3daff84efbb6771e743bc3a11a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2f0ea95784a4e268a87b56bc82303a1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b2d7372e054405ba66e6a6329e6cc30~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上三图分别是，针对高斯模糊问题的原卡顿列表、现在卡顿列表、trace 。在原先的卡顿上报列表中，问题分散到了不同的堆栈中，这是由于发生卡顿时抓栈随机，而现在的卡顿列表聚合到了单一的堆栈链路中，这是由于我们取每一层堆栈中耗时最长的函数组合成特征堆栈，通过 trace 也可以验证特征堆栈的有效性，能够更准确的定位问题原因。同时，trace 详细的展示了函数调用链路，提供了深入分析问题的能力。</p>
<p>经过 trace 和堆栈验证，该方式输出的卡顿信息，堆栈聚合更加契合真正的卡顿点，当然一个 Message 中可能有多个大大小小的耗时函数存在，trace 文件的存在能够更全面的还原现场情况，二者的结合才能更好的解决问题。</p>
<p>目前卡顿检测体系已经在众测及线下自动化常态运行，产出数据来看均为线上存在问题。</p>
<h3 data-id="heading-9">前置发现能力建设</h3>
<p>基于 Sliver 能力的卡顿和 ANR 检测方案，能够极大提高解决问题的效率，接下来我们需要考虑如何将这两种能力常态的运行起来，服务于我们的日常存量问题、增量问题的防和治，尤其是将问题的暴露阶段提前，减少对用户的影响尤为重要。为此，我们进行了以下几个方向的建设。</p>
<ul>
<li>线下压力测试</li>
</ul>
<p>目前，测试平台提供了一些自动化测试 job，这些 job 大多以遍历方式自动的测试 APP 的功能，对所有功能优先级一样的触达，我们将我们的 ANR 检测能力和卡顿检测能力进行集成打包，触发自动化 job，产出相关的卡顿和 ANR case。</p>
<p>分析对比这些 case 后发现，线下上报的 TOP 问题和线上问题差异较大，不符合用户真实的使用场景。线下检测出的一些量级较大的 case 在线上场景出现的量级很小，影响的用户很少，而线上一些影响用户较多的 case，线下检测却上报很少。分析这是由于遍历式的测试方案不符合真实的用户行为，这会使我们在推动解决问题中优先级错误，无法及时正确辨别那些真正量级高、影响用户多、优先级高的问题，影响整体的优化节奏。</p>
<p>为此，我们接入了更智能的基于用户行为的测试策略，产出了更符合用户真实行为的智能测试 job，基于此 job 进行卡顿和 ANR 数据收集，采样分析相关数据符合线上数据分布，在量级和影响用户量级分布上更接近真实的用户场景，得到正确的问题优先级。</p>
<p>同时利用测试平台接口，我们构建了完全自动化的测试机制：基于最新 release 分支定时触发打包平台打包 -> 配置渠道为性能测试专用渠道 -> 成功后执行自动化测试生成数据。</p>
<ul>
<li>线上 (beta_version 和灰度)</li>
</ul>
<p>线下的自动化测试毕竟受机型、场景等条件限制，不易发现一些用户个性化问题。为此，在线上进行问题检测显得尤为重要。beta_version 和灰度渠道都是真实的用户渠道，能够覆盖各种场景，但二者又有所不同，beta_version 用户较少但活跃度更高。为此我们在 beta_version 渠道集成了卡顿和 ANR 数据的收集方案。同时，灰度渠道由于用户数多，可以提供更全面的场景和用户，我们也在灰度渠道集成了 ANR 方案，不过由于卡顿发生的频率相对较高，考虑到灰度用户多的特点，我们暂未开启灰度渠道的卡顿采集。</p>
<ul>
<li>动态能力建设</li>
</ul>
<p>很多时候需要对线上用户遇到的问题进行动态调查，相关调查能力虽然完备，但出于包大小的考虑很多时候并不会带到线上。针对此类问题，需要有一种类似于补丁但又相对轻量的方案，能够动态的下发能力到用户的手机上。</p>
<p>为了提高西瓜 Android 客户端的动态调查能力，将所有的通用能力封装成一个模块，通过统一的接口进行调度与事件分发，结合插件化下发加载能力，实现精准下发调查能力到任意手机上。</p>
<p>在实现上，整体流程如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d484374a2ec94e79a1c3e8f3bcb12b5e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以分为宿主、插件、组件三部分来看：</p>
<ul>
<li>宿主控制器，进行配置的拉取、插件初始化，预埋接口供宿主调用，根据调用及动态配置反射向插件分发器传递指令。</li>
<li>插件分发器，接收宿主的指令，并对应的加载不同的组件，执行不同的操作。</li>
<li>组件是一个个的独立模块，提供能力的具体实现，执行具体的功能。</li>
</ul>
<p>基于此框架，我们可以根据需求以动态下发插件的方式下发携带不同能力的插件包，同时利用 Setting 控制宿主执行相应的操作，完成动态的定向下发特定能力到特定手机或某类渠道的能力，这有以下优点：</p>
<ul>
<li>工具无需集成到 APK，不影响包大小</li>
<li>动态能力强，线上可以定向调查问题，线下可以快速验证问题。</li>
</ul>
<p>目前，我们已将多种问题调查能力进行了集成，为线上问题调查和修复提供了支撑。</p>
<h3 data-id="heading-10">卡顿数据的消费链路建设</h3>
<p>以上部分从线上、线下、动态能力角度结合卡顿 & ANR 方案进行了全方位的运行，产出了易消费可消费的数据，接下来我们需要完善消费流程，提高问题的解决效率。</p>
<p>针对产出的数据，我们通过轻服务进行数据处理，根据 apm_open 开放接口，我们可以拿到 job 对应的卡顿& ANR 数据列表，遍历列表，将每一个 case 的相关信息进行拼接，尤其是卡顿的 trace 文件链接，避免了文件下载链路较长的弊端，降低优化成本，之后将这些信息分发到对应的跟进群中。同时，在 Sladar 上根据对应的代码修改人或模块 owner 指定 owner 跟进。效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf3dfa6b05ea4150b8421a22c51401d3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，针对需要获取大量 trace 文件进行分析的场景，我们也开发了本地工具，便捷批量拉取 trace 文件。</p>
<p>总的来说，西瓜从基础工具的开发到在此之上卡顿 & ANR 方案的优化到线上线下动态前置发现能力建设再到最终的消费链路，完成整个卡顿 & ANR 监控体系的闭环，在存量问题解决、增量问题防治、单点问题跟进、整体性能治理上发挥了重要作用。</p>
<h2 data-id="heading-11">典型案例介绍</h2>
<h3 data-id="heading-12">堆栈聚合错误案例</h3>
<p>对 TOP 1 的 nativePollOnce 问题捞取多个 trace 样本进行分析，堆栈表现如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe7c8f82cc4c4d239718a6f932a34a36~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>数据库问题</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b63201b4418944659a24e587ac024a62~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过 trace 看出其实是主线程在执行数据库操作，快速推动解决。</p>
<ul>
<li>Dex2oat 问题</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d07c07716fd940818d13024ca89e33d5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过 trace 看出其实是 ClassLoader. 执行了 20+s，查看源码，发现是 PluginClassLoader.->....dex2oat....->Runtime.exec 这样一个调用链路。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8abb29124de44c2a87997e8645fbc81~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20f79500f8a94706a144501f62eed314~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于以上的堆栈，我们知道该问题是在加载插件时，验证 oat 文件不通过而触发主线程 dex2oat 操作导致。因此我们提前在插件 Plugin 实例初始化时，判断 oat 文件是否有效，无效的话中断插件状态机，置为不可用，同时异步重新生成 dex2oat 产物。</p>
<ul>
<li>直播问题</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5478dd488c734bcf97028788e104cd31~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过 trace 清晰看出是直播插件内部的初始化耗时严重导致问题，而非上报的堆栈分析发现，触发主要发生在插件加载成功的回调中，基于现在的插件框架，插件的加载主要有两条路径：</p>
<ul>
<li>主动 preload 插件</li>
<li>反射插件类从而被动触发插件加载</li>
</ul>
<p>为此，我们从两个方面进行了优化：</p>
<ul>
<li>从宿主层面梳理两类拉起插件时机，避免过早无意义拉起插件，按需加载</li>
<li>推动业务方，根本上优化初始化耗时。</li>
</ul>
<h3 data-id="heading-13">非常规案例</h3>
<ul>
<li>Json copy 问题</li>
</ul>
<p>有一类这样的问题，看堆栈发生在 JSONObject clone = new JSONObject(origin.toString),在其中的浮点类型转换时。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/324a7e58447d450bac60b7254354e01a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这个堆栈的第一印象是该方法并不耗时，堆栈偏移，然后拿到对应的 trace 可以看到，确实是当前方法非常耗时导致。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe495fb523d644e9b8abe5672cd81588~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看 trace 的最下层，都是重复的位计算，推测是一个超级长的 double 类型数字导致的运算过长，在灰度上收集对应的 json 发现其中无此类数据，推测是 toString 的时候，会把存放的 double 数据转成 string，然后 new 的时候又把 string 转成 double，这两次转换可能会出现精度问题，造成 double 的值变成了 1.9999999999999999999999 这种很长的数，然后计算耗时很长，导致 ANR。</p>
<p>为此，将上述 JSONObject clone = new JSONObject(origin.toString) 逻辑修改为遍历 origin 内容复制拷贝，验证后此问题消失。</p>
<ul>
<li>HashMap 问题</li>
</ul>
<p>一类问题看堆栈报在了 HashMap.remove 方法中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d052373144f4fdc8069a139ea4f4fac~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样，看到该堆栈，第一反应是当前方法并不耗时，堆栈偏移导致，然而拿到对应的 trace 后，我们发现确实是当前方法导致的耗时。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b4f249110bd41d19411bee1e96330f1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从 trace 可以明显看出，确实在 HashMap.remove 中卡了 40+s，结合 cpu 负载情况看，也并不是得不到调度导致。</p>
<p>深入分析，发现在多线程操作 HashMap 时，若发生扩容，可能会产生循环链表，进而触发死循环，最终采用 ConcurrentHashMap 后解决该问题。参见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fc72af03abba5%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/c72af03abba5%E3%80%82" ref="nofollow noopener noreferrer">www.jianshu.com/p/c72af03ab…</a></p>
<h3 data-id="heading-14">卡顿案例</h3>
<ul>
<li>动画问题</li>
</ul>
<p>有一类动画问题，动画本身是个简单的闪光动画，内部没有复杂逻辑，关于其耗时的可信程度存疑，但是借助 trace 图可以看到：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8c2b6ca127d44c5b4f183a63dfadfe4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>确实动画存在严重的耗时情况，清晰的展示耗时点。此时再看原先卡顿监控和现在卡顿监控的堆栈聚合效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9970a7a1d8c34dea95c299f7e0db1e67~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/928a07d450d64755bdedebab71a72035~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上边两图分别表示了原卡顿监控和现在卡顿监控的堆栈聚合效果，可以看到原卡顿监控的堆栈聚合到了多个不同的堆栈链路下，这也是因为其抓栈的随机性，这样会使我们分散精力，也无法确定问题真实原因，而在我们现有的卡顿体系下，堆栈高度精确聚合到唯一的堆栈链路上，借助 trace 信息，也可以验证堆栈的准确性。基于此，我们可以精确定位和分析问题。</p>
<ul>
<li>详情页问题</li>
</ul>
<p>有一种情况，如果一个 Message 中每一层调用中的函数都非常耗时，那么就会有多个聚合，此时的每一个聚合都是一个真实耗时链路，对应的 trace 如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a999e059fb6c4f02a627179372844419~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，所有函数的耗时一目了然，这样可以清晰明确问题之所在，找准优化方向。</p>
<p>以上案例介绍，展示了我们在卡顿和 ANR 方面调查能力的提升，大大提升了我们在问题解决及防治上的能力，解决了长期以来制约我们提升性能的瓶颈，为长期的发展提升提供了支撑。</p>
<h2 data-id="heading-15">卡顿 & ANR 后续规划</h2>
<p>过去一段时间的监控建设和治理工作取得了不错的成果，但是仍然存在许多问题，主要有以下几类：</p>
<ul>
<li>卡顿 & ANR 问题很多时候不是独立的，和手机本身的 IO、内存、负载等因素息息相关，目前我们还没有将手机本身状态加入到监控体系中。</li>
<li>卡顿 & ANR 问题很多时候是由于子线程的抢占、Binder 等待等原因，目前我们的监控能力无法有效覆盖到。</li>
<li>随着越来越多的 native 代码运行在工程中，带来的影响影响也越来越大，目前我们的监控机制只能追溯到 java 层面，对于 native 层的问题链路无法有效定位，这一类问题仍然手段不足且低效。</li>
<li>随着 APP 动态能力越来越强，各类动态无感知上线场景增多，相关问题也很难在线下或灰度阶段发现，这给我们带来了新的挑战，一是数据敏感度建设，及时发现问题出现，二是线上归因问题能力建设，归因到具体什么上线导致，归因到具体问题场景和原因。</li>
</ul>
<p>基于这些仍然存在的问题，接下来，我们考虑做以下几方面的工作：</p>
<ul>
<li>完善对手机 IO、内存、负载等重要状态信息的监控和治理工作，检测高频、耗时、异常的 IO、内存、负载操作，通过对这些基本状态的优化间接优化卡顿和 ANR。</li>
<li>将卡顿监控能力和手机 IO、内存、负载结合起来，对问题聚合做 IO、内存、负载维度的划分，理清手机系统状态和 Method 自身运行问题。</li>
<li>完善监控体系中对于多线程和 Binder 调用的检测，尝试获取部分线程的 trace 现场用于辅助定位问题，并对 Binder 调用进行检测，对高频同类型 Binder 操作进行提取优化。</li>
<li>尝试对 native 代码调用进行检测，补齐监控链路无法触达 native 层的短板，提高问题定位效率和能力。</li>
<li>建设线上数据波动检测能力，加强数据波动的敏感度和发现效率，建设针对动态上线功能的归因筛选能力，筛选出数据波动一定范围内的动态上线功能，缩小排查范围，提高效率。同时结合我们的动态框架和工具链进行进一步详细归因。</li>
</ul>
<h2 data-id="heading-16">总结</h2>
<p>在上面我们整体介绍了过去一段时间西瓜 APP 的体系建设和治理工作，全方位的展示了我们的思考和各项短板的建设，并使之成功用于优化实践和常态问题防治，80% 以上的卡顿和 ANR 问题能够准确还原现场信息，线上严重影响用户体验的问题得到了很大程度的缓解，同时有效遏制了新增问题被带入线上，为西瓜长期常态性能问题防治提供了参考。</p>
<h2 data-id="heading-17">加入我们</h2>
<p>欢迎加入字节跳动西瓜视频客户端团队，我们专注于西瓜视频 App 的开发和基础技术建设，在客户端架构、性能、稳定性、编译构建、研发工具等方向都有投入。如果你也想一起攻克技术难题，迎接更大的技术挑战，欢迎加入我们！</p>
<p>西瓜视频客户端团队正在热招 Android、iOS 架构师和研发工程师，最 Nice 的工作氛围和成长机会，各种福利各种机遇，在北京、杭州、上海、厦门四地均有职位，欢迎投递简历！联系邮箱：<a href="https://link.juejin.cn/?target=mailto%3Aliaojinxing%40bytedance.com" target="_blank" title="mailto:liaojinxing@bytedance.com" ref="nofollow noopener noreferrer">liaojinxing@bytedance.com</a> ；邮件标题：姓名-西瓜-工作年限-工作地点。</p></div>  
</div>
            