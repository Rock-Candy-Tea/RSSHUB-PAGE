
---
title: '短视频go研发框架实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ca78cd65414498bf7dd20ac05e4e6f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 19:22:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ca78cd65414498bf7dd20ac05e4e6f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>导读</strong>：hulk是短视频研发部研发的基于GDP2（Go Develop Platform ）的go服务开发框架。它是⼀款⾯向业务的Web开发框架，提供了诸多开箱即⽤的组件和功能，可以⽤来快速开发Web服务。同时，依托于hulk框架并结合⼚内/业界优秀的开发实践，初步构建了⼀个符合业务应⽤场景的go⽣态体系。</p>
<p><em>全文7330字，预计阅读时间 12分钟。</em></p>
<p>===</p>
<h1 data-id="heading-0"><strong>一、产生背景</strong></h1>
<p>hulk框架是在“好看视频”服务端的go服务化架构升级背景下产生的。</p>
<h2 data-id="heading-1"><strong>1.1 为什么要做架构升级？当前架构面临哪些问题？</strong></h2>
<p>好看视频初期因业务需要快速、灵活的开发迭代，采⽤PHP作为开发语⾔实现后端服务，前期取得了⽐较好的开发迭代效果。但随着好看业务快速发展，服务端的项⽬(接⼝、代码等)急速膨胀，类单体的PHP架构在多个⽅⾯遇到了瓶颈和问题，主要体现在以下⼏个⽅⾯：</p>
<p><strong>1.开发效率</strong>：对于主代码库，所有服务端同学都会在这同一个代码空间开发，此外还有依赖的第三方团队也会修改，频繁的修改/合并降低了开发效率，同时也加大了代码的维护成本和难度；</p>
<p><strong>2.上线效率</strong>：多用户开发同一代码库的另一个弊端就是上线等待，由于同一个时刻只能有一个分支上线（分级上线），导致相连的上线需求要排队等待。这也导致我们的同学摸索出“搭车上线”的模式，虽然加快了上线效率，但也加大了上线的风险，没有从根本上解决问题；</p>
<p><strong>3.运行效率</strong>：PHP在开发效率和灵活度方面确实有一定优势，但当所支撑的业务达到几千万DAU及以上时，我们必须要考虑服务的运行效率和资源成本等问题。PHP语言在多线程/多协程的支持上，弱于Java、C/C++、Go等语言，基于物理机部署的类单体服务部署架构，在资源利用率和服务扩缩容等方面也很难满足需求；</p>
<p><strong>4.SRE效率</strong>：在出现稳定性问题时，我们期望能够做到快速感知、快速定位、快速止损。目前基于sia的监控/报警，基于日志的问题定位方式距离理想目标还有一定的距离：一是同学要奔波于各个平台/系统获取问题线索，二是获取到的线索及信息维度很多时候也无法满足快速、精确定位问题的需求；</p>
<p>这些问题需要通过“4化”，从总体业务架构、部署架构、基础设施等多方面去解决：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ca78cd65414498bf7dd20ac05e4e6f~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-2"><strong>1.2 为什么不直接基于GDP2 ？</strong></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c85a1e21e0a4e9a82f2d3c02c48291d~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>好看的go服务化升级工作开展时，GDP2还未正式发布，这也是其中一个因素。</p>
</blockquote>
<hr>
<h2 data-id="heading-3"><strong>1.3 hulk与gdp2能⼒对照</strong></h2>
<p>下⾯从三个⽅⾯与gdp2做⼀个简单的对照，初步了解hulk的整体能⼒及与gdp2的⼀些差异。</p>
<h3 data-id="heading-4">1.3.1 web server能⼒</h3>
<p>hulk⽬前主要服务于web应⽤，⾸先了解⼀下hulk的web server能⼒。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c3192fe09e944e6902489ebdefeab64~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5"></h3>
<h3 data-id="heading-6">1.3.2 功能/组件</h3>
<p>功能/组件的丰富度及⾃身能⼒，很⼤程度上影响了框架对业务服务的⽀持能⼒。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c74cc94746744789138009ed14ae893~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7"></h3>
<h3 data-id="heading-8">1.3.3 框架周边及基础设施</h3>
<p>框架从来不是“单打独⽃的”，它需要有周边⼯具和基础设施来⽀持。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98eba0bf231e407a97d5511e261c404b~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>NOTE：</p>
<p>1. 好看在做go化时，也调研了开源社区⾥⽐较优秀的⼀些⼯具系统和⽅案并引⼊， hulk中默认添加了对这些基础设施的集成；</p>
</blockquote>
<h3 data-id="heading-9"></h3>
<h3 data-id="heading-10">1.3.4 对照总结</h3>
<p>本节主要站在hulk能力角度与GDP2做了一些方面的参考对照。以上对照，可以概括为4点：</p>
<p>1.很多基础能⼒，hulk是复⽤gdp的，如：bns、net、codec等；</p>
<p>2.⼀些通⽤/扩展组件，hulk按照业务需求场景，进⾏⼆次封装和增强，如：httpserver、ral、redis、mysql等；</p>
<p>3.对于gdp⽬前没有⽀持的⼀些业务需求，进⾏开发集成，如：定时任务、配置中⼼、服务治理等；</p>
<p>4.参考业界开源实践，引入了一些新的基础设施：如prometheus+grafana集群、sentry集群、故障定位系统等；</p>
<blockquote>
<p>GDP2由几十个模块共同构成，由于时间有限，可能个别功能点的对照有偏差。</p>
</blockquote>
<p>===</p>
<h1 data-id="heading-11"><strong>二、了解hulk</strong></h1>
<h2 data-id="heading-12"><strong>2.1 设计思路</strong></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/841e0dcf4a5b40be90b6b17ee59b2415~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-13"><strong>2.2 框架结构</strong></h2>
<p>从功能上来看，hulk的整体能力可以划分为四层：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d124799b8364df5861f665d2337fecd~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14"></h3>
<h3 data-id="heading-15">2.2.1 基础组件</h3>
<p>提供了绝大部分项目都应该需要的基础能力，也是其他上层功能组件很可能依赖的组件。hulk框架通过这些基础组件，使上层应用可以无感的与基础设施进行集成：</p>
<ul>
<li>
<p><strong>日志组件</strong>：默认支持与PHP兼容的打印格式（用于配置sia监控和报警），同时也兼容ftrace接入的格式（日志查询和问题定位）；</p>
</li>
<li>
<p><strong>云原生监控</strong>：默认支持prometheus，对所有接口请求、redis、ral等远程调用进行多维度的metrics采集，并通过grafana展示；</p>
</li>
<li>
<p><strong>配置中心</strong>：通过配置中心，可以实时下发并生效配置。目前支持Apollo/iConf，支持功能包括-版本管理、热发布、灰度发布、权限管理、审核与审计等；</p>
</li>
<li>
<p><strong>事件追踪/定位</strong>：借助sentry，对于一些故障，我们可以秒级感知。hulk在异常信息中保存了比较完整的现场信息-如调用栈、request、集群和实例信息等，通过这些信息，可以直接定位问题的原因；</p>
</li>
</ul>
<h3 data-id="heading-16">2.2.2 通用组件</h3>
<p>这一层的组件能力是通用的，提供了一些管理控制和切面能力：</p>
<ul>
<li>
<p><strong>ral组件</strong>：hulk的ral模块封装了GDP2的ral主体功能，同时，对ral进行了增强- a) 提供了通过字符串而非文件来进行ral初始化和ral懒加载功能；b) 提供了多个hook能力，如prometheus的监控信息采集，熔断、降级等；</p>
</li>
<li>
<p><strong>服务治理</strong>：框架的服务治理能力是基于Sentinel （阿里开源的高可用流量防护组件）和配置中心来构建的，主要以流量为切入点，从限流、流量整形、熔断、降级等多个维度来协助保障微服务的稳定性，并提供动态控制能力；</p>
</li>
<li>
<p><strong>协程池</strong>：a) 可以自动调度海量协程，复用goroutines，减少gc，b) 可以优雅处理 panic，防止程序崩溃 c) 提供了：任务提交、获取运行中的 goroutine 数量、封装了WaitGroup支持协程任务编排等功能；</p>
</li>
<li>
<p><strong>事件通知</strong>：框架与如流做了集成。用户将robot token配置在项目里，就可以直接使用ruliu组件向指定的如流群发送报警/通告。如流组件结合sentry，可以让我们第一时间知道程序出了问题并快速定位到问题；</p>
</li>
</ul>
<h3 data-id="heading-17">2.2.3 扩展组件</h3>
<p>前两层功能对直接的业务处理逻辑参与较少，这一层的组件其能力多是为了处理某一类特定业务逻辑和场景，如redis/mysql/定时任务等：</p>
<p><strong>1.redis组件</strong>：基于GDP2 redis模块的封装并作了功能增，提供了：</p>
<p><strong>a)</strong> <strong>metrics hook</strong>，对所有的redis请求进行监控(prometheus)打点（latency/p99/qps/错误码分布等）；</p>
<p><strong>b) sentry hook</strong>，支持将redis错误在记错误日志同时发送到sentry；</p>
<p><strong>c) 降级hook</strong>，支持按集群/实例/百分比维度降级redis访问；</p>
<p><strong>d) 熔断hook</strong>，支持按集群/实例/错误率/慢请求率对依赖的服务进行熔断设置；</p>
<p><strong>2.mysql组件</strong>：mysql组件是基于GDP2 mysql和 gorm_adapter的封装，在已有能力之上，进行了以下功能扩展：</p>
<p><strong>a) 提供了metrics hook</strong>，对所有的mysql请求进行监控(prometheus)打点（latency/p99/qps/错误码分布等）；</p>
<p><strong>b) 提供了sentry hook</strong>，支持将mysql错误在记错误日志的同时发送到sentry；</p>
<p><strong>3.分布式锁</strong>：hulk提供了基于redis的分布式锁实现。其中redis连接是基于GDP2的redis模块的改造，分布式锁功能是封装了开源项目redsync；</p>
<p><strong>4.定时任务</strong>：支持两种定时任务模式；</p>
<p><strong>a) 带分布式锁的运行方式</strong>：对于多实例部署的定时任务，如果任务不是幂等的，则需要使用分布式锁对任务的调度运行进行控制；</p>
<p><strong>b) 不带分布式锁的运行方式</strong>：此模式下，如果部署了多实例，则所有实例上同一时刻的定时任务，会同时执行；</p>
<h3 data-id="heading-18">2.2.4 http server</h3>
<p>hulk（目前只提供了http server能力）提供了很多通用且高效的http middleware，并对外暴露了一些管理控制接口，在一些特殊情况下，可以通过这些管理接口，在运行时干预服务的运行：</p>
<ul>
<li>
<p><strong>logger_middleware</strong>：用于记录http的请求、响应、耗时等信息，同时支持实时修改日志打印策略-如按idc/ip/百分比/uid/cuid等维度打印；</p>
</li>
<li>
<p><strong>timer_middleware</strong>：用于http请求的监控埋点，可以输出可用性、tp99、流量、平响、错误码等metrics，维度包括服务级/idc/instance等；</p>
</li>
<li>
<p><strong>recover_middleware</strong>：用于捕获http 请求链路中的painc事件，并可自定义panic handler逻辑，如通过结合sentry和如流，可以实时感知并定位panic事件；</p>
</li>
<li>
<p><strong>flow_control_middleware</strong>：接口限流组件，可以通过配置中心或管理接口，对接口按idc/instance维度进行限流；</p>
</li>
<li>
<p><strong>timeout_middleware</strong>：通过该middleware或与配置中心结合使用，可以对接口按idc维度进行超时控制；</p>
</li>
<li>
<p><strong>其他middleware可以查看hulk文档</strong></p>
<p>（如-internal_user_middleware、jager_opentracing_middleware、thirdparty_auth_middleware、b2logger_middleware等）</p>
</li>
<li>
<p><strong>管理控制接口</strong>：如健康检查接口，服务治理-熔断、限流、降级接口，metrics接口，线上实例性能调试接口等；</p>
</li>
</ul>
<h2 data-id="heading-19"><strong>2.3 框架生态</strong></h2>
<p>通过近一年的建设，我们初步构建了一个以hulk框架为中心的、符合好看业务场景的go生态体系，包括：</p>
<ul>
<li>
<p><strong>标准目录规范</strong>：避免各个项目结构不统一，减少项目维护难度和工作量；</p>
</li>
<li>
<p><strong>代码生成器</strong>：基于hulk框架、标准目录规范、组件使用规范的代码生成器，目的是减少通用模块/组件使用不规范，解决通用流程编码、处理不一致的问题；</p>
</li>
<li>
<p><strong>hklib</strong>：好看的通用lib库，提供了一些的通用功能（也包含了很多PHP转go过程中的一些orp通用/基础的函数/功能），也提供了50+对中台服务的调用client，减少重复代码，提升研发效率，提升可维护性；</p>
</li>
<li>
<p><strong>基础设施</strong>：prometheus+thanos集群、sentry服务、apollo集群、pyroscope性能分析平台等；</p>
</li>
<li>
<p><strong>iconf</strong>：好看自研配置中心，能力在对齐开源的Apollo之外，还增加/增强了一些功能，如-key维度的发布、更安全的配置获取、更简洁的操作页面、类分级发布等；</p>
</li>
<li>
<p><strong>artemis</strong>：服务可视化与故障智能定位系统，可以在该系统中看到服务的部署架构、服务内部调用链、多维度细粒度的近实时监控和关键日志。在发生可用性故障时，一些故障问题可以秒级的定位到原因和具体代码；</p>
</li>
</ul>
<h2 data-id="heading-20"><strong>2.4 框架应用情况</strong></h2>
<p>目前短视频所有go服务都是基于hulk构建的，在资源、接口性能和可用性等方面都有一些阶段性产出和收益。</p>
<p>hulk框架应用现状：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d90e82b690e4d06a05d96669e2267c7~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>资源和性能收益：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761815802be9425eb7f9dfbf7551bcbc~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>资源和性能收益，很大一部分要归属于PHP->Go的技术栈切换；而框架为服务应用相应技术栈特性提供了便捷和高效的方式。</p>
</blockquote>
<p><strong>2.4 hulk服务架构</strong></p>
<hr>
<p>下图描述了一个微服务（基于hulk）的架构全景图：</p>
<ul>
<li>
<p>框架中个各功能组件都是围绕业务各个场景和需求的，在业务逻辑中能够比较便捷的使用相关功能组件；</p>
</li>
<li>
<p>这些组件在启用后，也会与相应的基础设施进行交互融合，共同支撑服务的高效、可控和稳定的运行；</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c23fff2b6a1247e3bc7de687b77e0f85~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>hulk组件初始化及与周边基础设施的集成，基本都可以通过环境变量/配置文件来完成。</p>
</blockquote>
<p>===</p>
<h1 data-id="heading-21"><strong>三、框架能力与应用</strong></h1>
<p>下面我们从日常开发遇到的一些痛点，来介绍框架的能力，并配以示例来说明这些能力是如何减少或解决痛点的。</p>
<h2 data-id="heading-22"><strong>3.1 如何提升代码质量？</strong></h2>
<p>代码质量会直接或间接的产生以下影响：</p>
<ul>
<li>
<p>代码质量会直接影响代码维护成本；</p>
</li>
<li>
<p>代码质量会影响程序出bug的概率；</p>
</li>
<li>
<p>代码质量会影响程序运行效率；</p>
</li>
</ul>
<p>hulk框架从以下三方面分别来提升代码质量。</p>
<h3 data-id="heading-23">3.1.1 规范代码组织结构</h3>
<blockquote>
<p>降低项目维护成本，提升研发效率。</p>
</blockquote>
<ul>
<li>
<p><strong>通过标准目录规范</strong>，定义通用(http服务)的项目layout，避免出现每人一种或多种layout，最终项目结构“百花齐放”的现象；</p>
</li>
<li>
<p><strong>通过代码生成器</strong>，帮助开发者生成项目模板，对初始化流程，各目录/文件的使用进行潜在约定；</p>
</li>
</ul>
<h3 data-id="heading-24">3.1.2 编码规范和静态检查</h3>
<blockquote>
<p>提升代码可读性，减少低级代码bug</p>
</blockquote>
<ul>
<li>
<p>遵循百度Go编码规范+业务编码补充规范；</p>
</li>
<li>
<p>使用GDP的代码检查工具：go_fmt、goc；</p>
</li>
</ul>
<h3 data-id="heading-25">3.1.3 配套的压测和性能分析平台</h3>
<blockquote>
<p>确定服务的压力边界，发现潜在的性能问题。</p>
</blockquote>
<ul>
<li>压测和性能测试平台（测试环境）：nGrinder</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95335fa4eca8451f9c084a6fbf4a68af~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>程序性能分析平台</strong>：pyroscope。可以通过hulk自集成的管理接口，实时打开或关闭线上实例的“continuous-prof”功能，定位线上性能问题：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c5069d27f694060a8a2ce88ddf18ab4~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-26"><strong>3.2 如何提升开发迭代速度？</strong></h2>
<ul>
<li>
<p>如何让开发者专注于业务逻辑与实现？</p>
</li>
<li>
<p>如何让开发者快速响应并完成产品需求？</p>
</li>
</ul>
<p>hulk框架为提升迭代速度，提供了以下支持。</p>
<h3 data-id="heading-27"></h3>
<h3 data-id="heading-28">3.2.1 丰富的实用组件/功能</h3>
<blockquote>
<p>提升研发效率，避免试错，减少出错。</p>
</blockquote>
<ul>
<li><strong>程序增强组件</strong>：增强的redis/mysql功能，增强的ral调用等。例-下图中的redis监控，其监控指标是由hulk redis组件自动采集计算的：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f9a6d2d51ef49b3bb6b81f1634d9e93~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>优秀的开源组件</strong>：sentry、prometheus+grafana、apollo、协程池等。例-prometheus+grafana：hulk框架默认支持prometheus，可以对服务的可用性、QPS、耗时、错误码等metrics自动计算收集：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/579e2a4131254437bdf1f1fdcd7a10bb~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>丰富的http middleware。</p>
</li>
</ul>
<h3 data-id="heading-29">3.2.2 配置化、低代码支持</h3>
<blockquote>
<p>减少代码的修改和上线，提升需求的响应和完成速度。</p>
</blockquote>
<ul>
<li>
<p>hulk框架中大部分组件可以通过环境变量/配置文件来初始化；</p>
</li>
<li>
<p>业务逻辑中的可变数据与配置，可以通过apollo/iconf实时下发和生效，无需代码修改和长流程上线。例-可以通过开箱即用的配置中心功能，实时下发并生效配置：</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec5da27af6ed4c41a28adb1789846688~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-30"><strong>3.3 如何快速感知并定位问题？</strong></h2>
<ul>
<li>
<p>开发者如何快速感知服务中的问题，严重问题如何实时感知？</p>
</li>
<li>
<p>开发者如何能从监控、日志、报警中获得详细的问题信息，以快速定位问题？</p>
</li>
</ul>
<p>hulk为提升SRE效率，从以下几个方面提供支持。</p>
<h3 data-id="heading-31">3.3.1 完善的事件追踪定位与通告能力</h3>
<blockquote>
<p>能够实时追踪开发者自定义的错误并通告</p>
</blockquote>
<ul>
<li><strong>实时事件追踪组件</strong>：sentry。hulk提供了开箱即用的sentry组件功能，可以像打印日志一样使用，sentry中的信息包含代码调用栈、上下文、自定义关键信息等：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47604ac761b54734ae7c5cc8361fb71c~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>通告组件</strong>：ruliu。一行token配置就可以开启如流功能，可以将一些需要立即关注的信息实时打到如流群里，同时还可以和sentry结合，实现异常问题实时感知和定位：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d9a33e0dfa148efa84db4813a5149c0~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-32"></h3>
<h3 data-id="heading-33">3.3.2 prometheus+sia监控支持</h3>
<blockquote>
<p>通过prometheus与noah的互补，支持多维度全方位监控，能够获得更多的服务稳定性相关信息</p>
</blockquote>
<ul>
<li>
<p>prometheus为开发者提供灵活的多维度的业务监控信息；</p>
</li>
<li>
<p>sia可以为开发者提供基于日志的采集的服务稳定指标和容器、网络等资源维度监控信息；</p>
</li>
</ul>
<h3 data-id="heading-34">3.3.3 ftrace日志查询与分析功能</h3>
<blockquote>
<p>hulk默认支持ftrace平台的日志格式</p>
</blockquote>
<ul>
<li>通过ftrace，可以便捷高效的查询用户维度的日志信息；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/801a1bee713240209b406ae770630414~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>通过pdo2命令，可以检索查询自定义规则的日志信息；</p>
</li>
</ul>
<h2 data-id="heading-35"><strong>3.4 基于hulk的服务可视化和故障智能定位系统</strong></h2>
<p>artemis是我们基于hulk研发的一款服务可视化与故障智能定位追踪系统，它集服务部署架构可视化、近实时多维度监控、关键日志、服务调用链等多方面信息，可以快速、高效、精准的发现和定位稳定性问题。</p>
<p>该系统目前已接入好看/全民/度咔等多个后端服务，极大加速了故障定位效率。在一些故障场景，可以秒级定位问题，给出问题的代码行。</p>
<h3 data-id="heading-36">3.4.1 服务部署架构</h3>
<p>通过实例列表，可以获取服务的idc列表、instance列表和详情，并提供了便捷高效的调试入口和登录指令：</p>
<h3 data-id="heading-37"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b9cf51bd9cb4933806993688a418f22~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></h3>
<h3 data-id="heading-38"></h3>
<h3 data-id="heading-39">3.4.2 近实时多维度监控</h3>
<p>artemis提供的近实时监控，能够提供更多维度信息，这些维度是sia和prometheus无法提供的，如：</p>
<ul>
<li>
<p>某个URI下面的某个下游(或下游实例)RAL的QPS、耗时、可用性；</p>
</li>
<li>
<p>某个服务实例实例的URI或RAL的监控信息；</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f09688ad2a414dcb98b7b86a1d4cbe24~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-40"></h3>
<h3 data-id="heading-41">3.4.3 关键日志</h3>
<p>由于与hulk的深度集成，在业务代码中打印warning级别以上的日志时，artemis能拿到更多的日志信息，如-各维度信息、调用栈、上下文等：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29f45c8fb57c4e26a4e1ce78ea9d9571~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e0cb420bdf1499b8840e1a500659a13~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-42">3.4.4 服务调用链</h3>
<p>在hulk框架的协助下，artemis还可以获取到URI及URI所依赖的RAL调用信息，由此可以构建出请求调用链，并实时展示调用链上的相关metrics信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d64b71a7f7d54c4fb5436a50013d1190~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不同颜色的链路代表不同的可用性：红色-1个9及以下，黄色-2个9，蓝色-3个9，灰色-4个9。通过服务调用链，可以非常直观的看到服务里，哪个接口有问题，还可以看到哪些下游影响了这个接口的可用性。</p>
<h3 data-id="heading-43">3.4.5 使用案例</h3>
<p>通过与报警系统的联动，可以在发生报警的第一时间，在artemis系统中找到受影响的服务及URI，确定是否是下游引起，错误是什么，哪一行代码报了错等，以下是一个artemis的实际应用示例。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a6d4dfff0e444a9bf2c6aa23ed2f88a~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>===</p>
<p><strong>四、总结</strong></p>
<p>===========</p>
<p>hulk虽然是⼀个新的go语⾔web框架，但不是重复造轮，⽽是站在⼚内和开源软件的基础上，结合业务实际开发、部 署、运⾏、运维环境，对这些开源框架和⼯具进⾏取⻓补短、⼆次开发，最终切合实际的业务使⽤场景。同时，围绕hulk初步构建起的go生态，为服务在开发、部署、运行、运维等各个阶段都提供了有力支持。</p>
<p>最后，希望短视频研发部在go服务化架构升级/研发框架上的⼀些实践、⽅案和经验，能够给有相同架构升级需求、 在go项⽬实践中遇到问题的其他业务线同学⼀些帮助和参考。</p>
<p><strong>招聘信息</strong>：</p>
<p>短视频研发部，负责好看视频、全民小视频以及多款创新APP的孵化研发工作。是公司级战略产品，承担百度系产品矩阵短视频内容供给任务，重点支持百度搜索和信息流视频化，肩负百度内容生态视频化转型使命。仅用两年的时间就实现用户规模从零到亿级增长，日活数千万。拥有百亿级流量，亿级数据量，丰富新奇和全面的产品玩法，多类型的技术系统和领先的技术架构。</p>
<p>欢迎加入短视频研发部，社招，实习，校招都要哦</p>
<p>简历投递邮箱：<a href="https://link.juejin.cn/?target=mailto%3Ageektalk%40baidu.com" target="_blank" title="mailto:geektalk@baidu.com" ref="nofollow noopener noreferrer">geektalk@baidu.com</a> （投递备注【短视频】）</p>
<p><strong>推荐阅读：</strong></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498417%26idx%3D1%26sn%3Da3f0a0c312c58693b3623cab0f387df4%26chksm%3Dc03ecacdf74943db287e50e0249cb8ae14823bc84d6f22ddacd8ee3cf5bc8038c76faa4ed667%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498417&idx=1&sn=a3f0a0c312c58693b3623cab0f387df4&chksm=c03ecacdf74943db287e50e0249cb8ae14823bc84d6f22ddacd8ee3cf5bc8038c76faa4ed667&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">千亿级模型在离线一致性保障方案详解</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498185%26idx%3D1%26sn%3D6abfb6a1bb9c3c78ca6f7a974174905d%26chksm%3Dc03ec9b5f74940a3c51744c44b39ab5c74967421389a7eaa2f596c3a9ec66e733e5d3d551215%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498185&idx=1&sn=6abfb6a1bb9c3c78ca6f7a974174905d&chksm=c03ec9b5f74940a3c51744c44b39ab5c74967421389a7eaa2f596c3a9ec66e733e5d3d551215&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">如何快速定位程序Core？</a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498047%26idx%3D1%26sn%3D5feff879b7160b93523333d0b9891399%26chksm%3Dc03ec943f749405534fc60e82359c3f9db77caab4baf44c96d4275bff6539745c3793a96128b%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498047&idx=1&sn=5feff879b7160b93523333d0b9891399&chksm=c03ec943f749405534fc60e82359c3f9db77caab4baf44c96d4275bff6539745c3793a96128b&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">百度BaikalDB在同程艺龙的成功应用实践剖析</a></p>
<p>---------- END ----------</p>
<p><strong>百度Geek说</strong></p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            