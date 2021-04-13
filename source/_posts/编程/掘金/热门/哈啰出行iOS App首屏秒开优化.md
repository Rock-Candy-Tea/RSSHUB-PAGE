
---
title: '哈啰出行iOS App首屏秒开优化'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28dee41f51d24e9b9f8e499f66bc2a90~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 19:15:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28dee41f51d24e9b9f8e499f66bc2a90~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>哈啰出行目前已经覆盖了出行相关领域多数业务场景。App首页作为哈啰用户第一个被用户感知的页面，几乎承载了所有核心业务的流量入口。App首屏渲染的快慢，对App整体用户体验至关重要。</p>
<p>本文主要介绍哈啰出行App在首屏启动渲染所面临的挑战，如何进行问题定位分析，并如何进行针对解决。</p>
<h2 data-id="heading-1">APP首屏渲染时间定义</h2>
<p>启动的定义在不同产品中有不同的标准，对于哈啰出行来说，首页启动加载完成的定义为：</p>
<p><strong>从用户感知侧，我们希望优化用户真正点击APP icon到首页首屏渲染加载完成的时间。</strong></p>
<p><img alt="截屏2021-04-08 下午7.07.54.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28dee41f51d24e9b9f8e499f66bc2a90~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">优化阶段</h2>
<p>产品快速迭代在解决快速业务发展的同时也带来了大量的技术债堆积，如果没有良好的规范和监控流程会使项目在稳定和体验上存在较多的隐患和挑战。正如启动阶段的启动项和业务逻辑堆积。
目前影响用户感知到的首页加载速度主要分以下三个阶段分析定位：</p>
<ul>
<li>启动/前置任务项</li>
<li>首页框架/业务逻辑</li>
<li>业务模块加载性能</li>
</ul>
<h3 data-id="heading-3">优化路径</h3>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2954281525b4098b05d5ab4455ad576~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>数据收集：收集启动阶段、首页加载、各业务模块加载性能数据</li>
<li>问题分析：确认并定位分析目前各阶段加载存在或依赖的问题</li>
<li>优化解决：启动项问题、首页逻辑处理问题、业务模块问题解决</li>
<li>持续监控：持续优化&监控首页的加载渲染和模块性能问题&可视化数据</li>
</ol>
<h2 data-id="heading-4">一、数据收集</h2>
<p>数据收集目前主要关注启动加载全链路的各阶段耗时，包括首页的页面加载时间、模块加载时间。</p>
<h3 data-id="heading-5">1、 APP启动渲染全链路数据收集</h3>
<p>从用户感知侧，我们希望收集到用户真正点APP Icon到首页首屏渲染加载的时间，以此来优化首页用户真实场景的体验。计划收集以下节点阶段数据分析：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a019a72206504c6e8557d7a2a997bc61~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>初始化耗时：DidFinishLaunching - App Process Init</li>
<li>前置任务耗时：DidFinishLaunching - Homepage Init</li>
<li>首页加载耗时：Homepage Init - Homepage Did Appear</li>
</ul>
<p>*<em>目前该阶段收集的时间方案为“首页生命周期初始节点”到“加载首页所有缓存模块完成“并且首屏已对用户可见。</em></p>
<p>点击打开APP：获取应用进程开始时间</p>
<pre><code class="copyable">+ (BOOL)processInfoForPID:(int)pid procInfo:(struct kinfo_proc*)procInfo &#123;
    int cmd[4] = &#123;CTL_KERN, KERN_PROC, KERN_PROC_PID, pid&#125;;
    size_t size = sizeof(*procInfo);
    return sysctl(cmd, sizeof(cmd)/sizeof(*cmd), procInfo, &size, NULL, 0) == 0;
&#125;
+ (NSTimeInterval)processStartTime &#123;
    struct kinfo_proc kProcInfo;
    if ([self processInfoForPID:[[NSProcessInfo processInfo] processIdentifier] procInfo:&kProcInfo]) &#123;
        return kProcInfo.kp_proc.p_un.__p_starttime.tv_sec * 1000.0 + kProcInfo.kp_proc.p_un.__p_starttime.tv_usec / 1000.0;
    &#125;
    else &#123;
        return 0;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2、启动项任务耗时收集（CocoaService）</h3>
<blockquote>
<p>CocoaService是团队内用于快速高质量开发iOS App的一套开发环境，主要提供模块管理、App启动流程任务管理、Service容器等功能。以及日志、监控、注解等工具API。实现快速构建iOS模块化App。</p>
</blockquote>
<p>目前启动项任务的耗时收集主要依赖于CocoaService 框架对于启动项任务的注册依赖和加载调度的管理策略。</p>
<p>目前调度策略分四个阶段，每个阶段加载注册依赖的任务列表，并收集任务的耗时上报。</p>
<h4 data-id="heading-7">任务加载阶段定义</h4>
<ul>
<li>AppInitialize：App初始化前执行（初始化前、用来替代+load 方法）。</li>
<li>CoreModuleMountedAfter：核心模块加载完成后（即时模块还未加载）。</li>
<li>InstantModulesMountedAfter：即时模块加载完成（所有同步启动项加载完成）。</li>
<li>AppLaunchedAfter ：App启动之后（App启动完成，UI已展示）。</li>
</ul>
<h4 data-id="heading-8">任务加载时序图：</h4>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f7fdd8e8e684e4f8811e0a8054f0666~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">3、模块加载时间收集</h3>
<p>目前首页模块加载数据收集分为两个阶段：加载数据阶段和UI渲染阶段。</p>
<p>*<em>Adapter为首页模块化的抽象实体对象</em>
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1bd955922e9443f98dfdf85cb9b8ea5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">二、问题分析</h2>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f1ed2e4eb04e548c6cef4a77e0185f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">1、App整体性能分析：Instrument</h3>
<h5 data-id="heading-12">使用 Instrument Time Profiler 性能工具分析</h5>
<blockquote>
<p>Time Profiler 是iOSer日常性能分析中用的比较多的工具，通常会选择一个时间段，然后聚合分析调用栈的耗时。
但Time Profiler 其实只适合粗粒度的分析，我们来看下它的实现原理：
默认 Time Profiler 会 1ms 采样一次，只采集在运行线程的调用栈，最后以统计学的方式汇总。比如下图中的 5 次采样中，method3 都没有采样到，所以最后聚合到的栈里就看不到 method3。所以 Time Profiler 中的看到的时间，并不是代码实际执行的时间，而是栈在采样统计中出现的时间。对于我们分析头部耗时问题的任务会有一定的帮助。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f943a6d8a4be44dc858bde349f5445d0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
Time Profiler 支持一些额外的配置，如果统计出来的时间和实际的时间相差比较多，可以尝试开启：</p>
<ul>
<li>High Frequency，降低采样的时间间隔</li>
<li>Record Kernel Callstacks，记录内核的调用栈</li>
<li>Record Waiting Thread，记录被 block 的线程</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4974b2798e248a6bb229a7100a784d8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8049242e607c4271be2b4c5582495715~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
环境：Xcode11 ， iOS 13，iPhone双核测试机。</p>
<h5 data-id="heading-13">结论：</h5>
<p>仅从截取部分的图中可以看到启动到首页加载阶段CPU都处于满负荷的状态，特别是在启动项加载和首页加载的阶段有异常的波峰。不完全统计启动项高达69+个(三方SDK、二方SDK、业务线Task)，线程数30+，同时工具分析出来的业务前置耗时代码逻辑也大量存在。</p>
<ul>
<li>启动阶段启动项Task、业务Task堆积处理占用CPU资源，造成资源抢占，存在性能瓶颈。</li>
<li>首页阶段加载业务过多，包括依赖首页加载的异步启动项对CPU占用明显过高，需要重点优化。</li>
<li>启动项的合理化管理、线程管理需要重点关注。</li>
</ul>
<h3 data-id="heading-14">2、首页阶段性能分析：排除法-错峰加载首页分析启动依赖影响</h3>
<p>首页作为项目中第一个页面，在运行加载环境上强耦合启动阶段的SDK启动项、业务前置Task。所以明确各阶段本身的问题痛点更有助于我们解决问题。
以下是我们分场景采样多次，进行场景排除法来缩小问题范围，下图是各场景采样后分别求平局数和中位数：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8b47c81f41d4ff6b00e7d499f28e4db~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<em>错峰加载：指将首页初始化加载延后，避开APP启动任务加载CPU使用高峰。</em></p>
<p>样本设备信息：系统：iOS 12.4.1，型号：iPhone 6
结论：</p>
<ul>
<li>异步启动项任务对首页加载有明显的影响，应该着重处理。</li>
<li>从错峰加载可以看出启动阶段的各SDK和业务Task对首页有严重影响</li>
</ul>
<h3 data-id="heading-15">3、具体业务场景分析：首屏模块加载耗时分析</h3>
<p>主要通过以下三个方式进行分析：</p>
<ul>
<li>Instruments(Timeprofile/System Trace)性能工具分析</li>
<li>排除法：简单直接有效，适合场景独立，环境稳定的情况下进行初步确认/缩小问题范围。</li>
<li>数据分析：Debug时的分析可能因样本数据不够，那线上收集到足够的样本数据分析后就可以帮助我们精准的确定耗时模块。</li>
</ul>
<h6 data-id="heading-16">结论:</h6>
<p>通过收集数据中定义的模块加载的两个阶段。各模块加载和UI渲染的耗时数据，存在大量的主线程耗时逻辑和复杂UI绘制的情况。</p>
<h2 data-id="heading-17">三、解决方案</h2>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f3711c42cd04fe191d2f81b74d668bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">1、启动项优化</h3>
<p>目前项目存在的现状，优化点主在于业务侧。主要问题在于前置阶段启动项/业务逻辑堆积，无规范和流程管控。</p>
<ul>
<li><strong>性能分析</strong>：启动项性能排查分析，明确问题启动项。</li>
</ul>
<p>通过针对性启动项性能排查分析优化解决或直接下线问题启动项。</p>
<ul>
<li><strong>规范方案</strong>：建立整套合理启动任务管理方案，合理处理启动项场景和时机。</li>
</ul>
<p>通过团队内同学开发的以注解的方式CocoasService得以在APP启动生命周期各阶段规范注册分发启动项加载时机，统一收口可监控。</p>
<ul>
<li><strong>调度策略</strong>：处理任务集中问题，降低CPU峰值。</li>
</ul>
<p>通过调度策略对启动项分阶段处理，降级集中处理的任务数量、延迟低优先级任务处理时机等等策略降低CPU峰值。</p>
<ul>
<li><strong>数据监控</strong>：监控启动项增长和各启动项性能数据。</li>
</ul>
<p>依赖于整体的启动项管控方案，基础架构同学目前在APM上增加了关于各启动项的初步性能数据收集可视化，并持续丰富数据、优化方案和改进策略。</p>
<h4 data-id="heading-19">二方、三方SDK影响</h4>
<p>在实际的Timprofile和debug分析中，SDK本身大多为基础库或组件能力库，在实际的开发中问题主要集中在以下几个方面：</p>
<ul>
<li>作为基础组件库在单一Demo环境下性能相对可控，对性能感知不明显，在接入大型项目后复杂的运行环境和基础接口的设计不合理，在启动场景下存在较严重的性能影响。</li>
<li>滥用Runtime、重写系统类方法，导致影响到业务逻辑。</li>
<li>接入SDK缺少完整的性能报告分析支撑。</li>
<li>不严谨的多线程处理方式，导致偶现的卡顿、崩溃等问题。</li>
</ul>
<p>后相关启动项都按照场景进行下线、延迟加载、异步加载等其他策略进行优化，并加入CocaService任务调度方案进行统一管理。</p>
<h4 data-id="heading-20">CocoaService 启动项后置任务处理策略问题</h4>
<p>目前依赖CocoaService管理启动项策略流程，初步收集了各启动项的性能数据。但也在优化首页启动时从中排查发现并优化了一些问题：</p>
<ul>
<li>几十个启动项分为同步和异步，异步启动项在初始化阶段同步并非初始化，导致CPU峰值过高。后改为异步串行并进行部分延迟策略进行初始化加载。</li>
<li>后置任务启动项定义的初始化节点为首页ViewController的-ViewDidApper时机，进行同步加载部分启动项任务，造成首页首屏展示卡顿和延迟。后改为异步串行并进行部分延迟策略进行初始化加载。</li>
</ul>
<p><em>因篇幅问题，启动项问题不再此一一列举。</em></p>
<h3 data-id="heading-21">2、业务问题优化</h3>
<h4 data-id="heading-22">Lottie框架</h4>
<blockquote>
<p>Lottie是一个iOS，Android和React Native库，可实时渲染After Effects动画，从而使应用程序可以像使用静态图像一样轻松地使用动画。
Lottie的特点：</p>
<ul>
<li>设计即所见: 设计师用AE设计好动画后直接导出Json文件，Lottie 解析Json文件后调Core Animation的API绘制渲染。还原度更好，开发成本更低。</li>
<li>跨平台: 一份json描述文件多端使用。支持iOS、Android、React Native。</li>
<li>性能：Lottie对于从AE导出的Json文件，用Core Animation做矢量动画, 性能较佳。Lottie 对解析后的数据模型有内存缓存。但是对多关键帧图片帧、图层混合较多的动画性能比较差。</li>
<li>支持动画属性丰富：比起脸书的Keyframes，Lottie支持了更多AE动画属性，比如Mask, Trim Paths,Stroke (shape layer)等。</li>
<li>包大小：相比动辄上百K的帧动画，Json文件包大小较小。有图片资源的情况下，同一张图片也可以被多个图层复用，而且运行时内存中只有一个UIImage对象（iOS）。</li>
</ul>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38d99318a5b344cdaa969932adbced1c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在项目中我们多处使用了Lottie的动画解决方案。但同时因为Lottie官方已不再维护Object-C版本，在实际使用和维护中我们也遇到了一些问题：</p>
<ul>
<li><strong>设计师在AE上出图时多加了很多无用图层忘记删掉，导出后这些无用图层在解析时缺少了LayerId，在iOS框架层解析异常导致崩溃</strong>。</li>
<li><strong>Lottie仅支持Memory cache，缺少二级缓存。每次新的APP生命周期内都需要重新下载</strong>。</li>
</ul>
<p>内存缓存可以快速的支持渲染和多次的动画执行效率。但缺少磁盘缓存，当资源相对较大、网络环境较差/网络抖动错误时每次重新加载的等待是一个非常糟糕的体验。</p>
<p>所以支持磁盘缓存，减少资源下载、减少等待快速加载展示是我们要解决的问题。参考SDWebImage的设计方式，我们在Lottie上扩展了对应的二级缓存：
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36824d1d59c94cbaa85ee4965a428e65~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>Lottie框架在同步处理转码时会根据关键帧图片的大小有不同的性能问题</strong>。</p>
<p>通过AE的bodymoving插件导出的常用文件格式有：json + zip(图片资源) 或 纯json(图片转为base64)。纯json描述文件的输出中关键帧图片一般会被处理成base64格式，需要本地转码生成位图渲染。</p>
</li>
</ul>
<pre><code class="copyable">- (void)_setImageForAsset:(LOTAsset *)asset &#123;
  if (asset.imageName) &#123;
    UIImage *image;
    if ([asset.imageName hasPrefix:@"data:"]) &#123;
      // Contents look like a data: URL. Ignore asset.imageDirectory and simply load the image directly.
      NSURL *imageUrl = [NSURL URLWithString:asset.imageName];
      NSData *imageData = [NSData dataWithContentsOfURL:imageUrl];
      image = [UIImage imageWithData:imageData];
    &#125; else if (asset.rootDirectory.length > 0) &#123;
      NSString *rootDirectory  = asset.rootDirectory;
      if (asset.imageDirectory.length > 0) &#123;
        rootDirectory = [rootDirectory stringByAppendingPathComponent:asset.imageDirectory];
      &#125;
     ....
    &#125; else &#123;
        NSString *imagePath = [asset.assetBundle pathForResource:asset.imageName ofType:nil];
        image = [UIImage imageWithContentsOfFile:imagePath];
    &#125;
      ....
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到源码中对于data:类型资源和获取路径资源都是在主线程进行的，对于关键帧多张或者单张较大的图片会阻塞线程。对于这种情况目前会有两种场景处理方式：</p>
<ol>
<li>创建异步线程队列处理关键帧过大和关键帧较多的情况，并将处理进度回调到外部感知进行合适的加载渲染时机处理。</li>
<li>减少关键帧的大小和数量，在一些场景下Lottie Animation必须更快速的加载渲染到屏幕，在这种场景下关键帧的大小可以通过图层混合、矢量绘制或设计输出规范等方式减少关键帧资源达到能快速加载的目的。</li>
</ol>
<h4 data-id="heading-23">图片资源加载渲染</h4>
<p>首页加载渲染时会有较多的图片资源加载，目前的图片资源加载方案，为了快速读取资源解码位图并渲染到屏幕，都会有二级缓存策略如下时序图(SDWebImage框架对于图片资源加载流程)。
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7de0c08474342bf9f6d24247ad320f4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在通常图片资源有缓存的情况下。首页冷启动时，内存中都没有对应的图片资源，需要进行async读取磁盘中的缓存图片进行解码渲染。当启动阶段CPU处理任务过多近乎满载的状态下，图片资源读取到渲染出来会被延到下一个runloop中，通常会看到宫格会有灰色占位图加载再到图片完全渲染出来的情况(如图)，体验较差。
<img alt="宫格加载对比.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bbbc1c9912c4bfdb1ce1cf3ac206823~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在通过对宫格模块的图片预加载同步解码，将图片预先从磁盘中读取到内存中解码，渲染时同步加载内存中解码后的图片直接渲染，和刷新机制的优化使宫格框架和图片可以在同一个runloop中渲染出来(如图)。提升了加载体验效果。</p>
<h4 data-id="heading-24">Runtime Hook Method</h4>
<blockquote>
<p>+load 除了方法本身的耗时，还会引起大量 Page In，另外 +load 的存在对 App 稳定性也是冲击，因为 Crash 了捕获不到。</p>
</blockquote>
<p>众所周知Object - C是一门动态语言，依赖于runtime的消息转发机制使我们可以在运行时做一些特殊的处理(比如AOP)。同时也在不规范开发中带来了很多隐患，如：</p>
<ol>
<li>+load方法的滥用，在项目中有大量的逻辑代码存在于+load方法中，对启动加载有较大影响。</li>
<li>在交换首页的生命周期方法后在一些内部逻辑处理后没有交换回来或没能及时交换回来。</li>
<li>对系统基础类大量的方法交换，进行一些逻辑处理。性能不可控，链路难以追踪</li>
</ol>
<p>通过对以上场景的处理首屏启动加载有比较可观的耗时优化。</p>
<h4 data-id="heading-25">First Frame Render</h4>
<p>一般会用 Root Controller 的 viewDidApper 作为渲染的终点，我们目前收集数据的策略也是以首页的viewDidApper为首屏的渲染节点。</p>
<p>Apple 在 MetricsKit 里对启动终点定义是第一个CA::Transaction::commit()。什么是 CATransaction 呢？我们先来看一下渲染的大致流程：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1bc7dd1f374fac813c8ad2d3ba181e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
iOS 的渲染是在一个单独的进程 RenderServer 做的，App 会把 Render Tree 编码打包给 RenderServer，RenderServer 再调用渲染框架(Metal/OpenGL ES)来生成 bitmap，放到帧缓冲区里，硬件根据时钟信号读取帧缓冲区内容，完成屏幕刷新。CATransaction 就是把一组 UI 上的修改，合并成一个事务，通过 commit 提交。
渲染可以分为四个步骤：</p>
<ul>
<li>Layout：Root Layer 调用[CALayer layoutSubLayers]，这时候 UIViewController 的 viewDidLoad 和 LayoutSubViews 会调用，autolayout 也是在这一步生效。</li>
<li>Display：Root Layer 调用[CALayer display]，如果 View 实现了 drawRect 方法，会在这个阶段调用。</li>
<li>Prepare：这个过程中会完成图片的解码。</li>
<li>Commit：打包 Render Tree 通过 XPC 的方式发给 Render Server。</li>
</ul>
<blockquote>
<p>XPC — XPC 是 OS X 下的一种 IPC (进程间通信) 技术, 它实现了权限隔离, 使得 App Sandbox 更加完备。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fbb0baa99cb454d9d25155f0bba5ccc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
由于首页是粗粒度模块的容器化页面开发，各业务的特性功能由对应的业务团队同学实现，在处理各自数据和UI渲染逻辑时会存在一些问题，影响首屏的加载：</p>
<ul>
<li>Layout阶段：部分业务模块层级过于复杂，复杂的嵌套和不同状态的Layout更新对AutoLayout的性能有较大的影响。特别是在iOS 12以下Apple未对AutoLayout算法进行优化。可以评估 ROI 决定要不要改成 frame。</li>
<li>Display阶段：部分业务模块drawRect实现了一些UI状态逻辑处理，重复处理subViews。建议Lazy 初始化 View，不要先创建设置成 hidden，不要在drawRect中处理UI状态逻辑。</li>
</ul>
<h1 data-id="heading-26">优化成果</h1>
<h2 data-id="heading-27">优化前后效果对比</h2>
<p><img alt="首页优化前后对比.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97f2ed17571946adaa02d9decc51f6d7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-28">优化数据对比</h2>
<p>线上采集数据情况：</p>
<p>优化前：首屏渲染时间都大于1秒。</p>
<p>优化后：90%的用户首屏渲染时间在1秒内，其中大部分用户在0.5秒内。
整体对比，首屏渲染性能提升40%。极大的提升了用户打开使用App的体验，同时也支撑了用户快速触达业务的响应。</p>
<h1 data-id="heading-29">规划和展望</h1>
<p>不积跬步，无以至千里；不积小流，无以成江海，持续提升用户体验是我们孜孜不倦的追求，未来我们会针对首页架构建设全链路监控和云端一体化容器，提升监控能力和动态化能力。我们同样也在期待志同道合的小伙伴加入，欢迎投递我们：<a href="mailto:liuhuan05877@hellobike.com">liuhuan05877@hellobike.com</a>， 优秀且富有抱负的你，还在等什么呢？</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            