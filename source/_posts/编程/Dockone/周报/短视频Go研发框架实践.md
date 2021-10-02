
---
title: '短视频Go研发框架实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/e342fdbc4c450abb8fd8d5d259407e14.jpg'
author: Dockone
comments: false
date: 2021-10-02 06:09:13
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/e342fdbc4c450abb8fd8d5d259407e14.jpg'
---

<div>   
<br>【编者的话】hulk是短视频研发部研发的基于GDP2（Go Develop Platform）的Go服务开发框架。它是⼀款⾯向业务的Web开发框架，提供了诸多开箱即⽤的组件和功能，可以⽤来快速开发Web服务。同时，依托于hulk框架并结合⼚内/业界优秀的开发实践，初步构建了⼀个符合业务应⽤场景的Go⽣态体系。<br><br>
<h3>产生背景</h3>hulk框架是在“好看视频”服务端的Go服务化架构升级背景下产生的。<br>
<h4>为什么要做架构升级？当前架构面临哪些问题？</h4>好看视频初期因业务需要快速、灵活的开发迭代，采⽤PHP作为开发语⾔实现后端服务，前期取得了⽐较好的开发迭代效果。但随着好看业务快速发展，服务端的项⽬（接⼝、代码等）急速膨胀，类单体的PHP架构在多个⽅⾯遇到了瓶颈和问题，主要体现在以下⼏个⽅⾯：<br>
<ul><li>开发效率：对于主代码库，所有服务端同学都会在这同一个代码空间开发，此外还有依赖的第三方团队也会修改，频繁的修改/合并降低了开发效率，同时也加大了代码的维护成本和难度；</li><li>上线效率：多用户开发同一代码库的另一个弊端就是上线等待，由于同一个时刻只能有一个分支上线（分级上线），导致相连的上线需求要排队等待。这也导致我们的同学摸索出“搭车上线”的模式，虽然加快了上线效率，但也加大了上线的风险，没有从根本上解决问题；</li><li>运行效率：PHP在开发效率和灵活度方面确实有一定优势，但当所支撑的业务达到几千万DAU及以上时，我们必须要考虑服务的运行效率和资源成本等问题。PHP语言在多线程/多协程的支持上，弱于Java、C/C++、Go等语言，基于物理机部署的类单体服务部署架构，在资源利用率和服务扩缩容等方面也很难满足需求；</li><li>SRE效率：在出现稳定性问题时，我们期望能够做到快速感知、快速定位、快速止损。目前基于sia的监控/报警，基于日志的问题定位方式距离理想目标还有一定的距离：一是同学要奔波于各个平台/系统获取问题线索，二是获取到的线索及信息维度很多时候也无法满足快速、精确定位问题的需求。</li></ul><br>
<br>这些问题需要通过“4化”，从总体业务架构、部署架构、基础设施等多方面去解决：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/e342fdbc4c450abb8fd8d5d259407e14.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/e342fdbc4c450abb8fd8d5d259407e14.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Hulk作为一个研发框架，用来承接相关的开发工作，并与其他基础设施共同支撑整个“4化”工作。<br>
<h4>为什么不直接基于GDP2？</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/e2b6d5417cd20442cf84cbcc26fcd132.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/e2b6d5417cd20442cf84cbcc26fcd132.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><blockquote><br>好看的Go服务化升级工作开展时，GDP2还未正式发布，这也是其中一个因素。</blockquote><h4>hulk与GDP2能⼒对照</h4>下⾯从三个⽅⾯与GDP2做⼀个简单的对照，初步了解hulk的整体能⼒及与GDP2的⼀些差异。<br>
<br><strong>Web Server能⼒</strong><br>
<br>hulk⽬前主要服务于Web应⽤，⾸先了解⼀下hulk的Web Server能⼒。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/2b71189fabc9c3635c92e11ed1b18ae4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/2b71189fabc9c3635c92e11ed1b18ae4.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>功能/组件</strong><br>
<br>功能/组件的丰富度及⾃身能⼒，很⼤程度上影响了框架对业务服务的⽀持能⼒。备注：ral资源访问层<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/17f2d5ebe7f48cc8bed87ae46f7f2859.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/17f2d5ebe7f48cc8bed87ae46f7f2859.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>框架周边及基础设施</strong><br>
<br>框架从来不是“单打独⽃的”，它需要有周边⼯具和基础设施来⽀持。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/a9760f27638918b4873e1a0b48b019d5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/a9760f27638918b4873e1a0b48b019d5.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><blockquote><br>NOTE：好看在做Go化时，也调研了开源社区⾥⽐较优秀的⼀些⼯具系统和⽅案并引⼊， hulk中默认添加了对这些基础设施的集成。</blockquote><strong>对照总结</strong><br>
<br>本节主要站在hulk能力角度与GDP2做了一些方面的参考对照。以上对照，可以概括为4点：<br>
<ol><li>很多基础能⼒，hulk是复⽤GDP的，如：bns、net、codec等；</li><li>⼀些通⽤/扩展组件，hulk按照业务需求场景，进⾏⼆次封装和增强，如：HTTP Server、RAL、Redis、MySQL等；</li><li>对于GDP⽬前没有⽀持的⼀些业务需求，进⾏开发集成，如：定时任务、配置中⼼、服务治理等；</li><li>参考业界开源实践，引入了一些新的基础设施：如Prometheus+Grafana集群、Sentry集群、故障定位系统等；</li></ol><br>
<br><blockquote><br>GDP2由几十个模块共同构成，由于时间有限，可能个别功能点的对照有偏差。</blockquote><h3>了解hulk</h3><h4>设计思路</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/b6f42c3cfabc8002cade75e71cfce710.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/b6f42c3cfabc8002cade75e71cfce710.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>框架结构</h4>从功能上来看，hulk的整体能力可以划分为四层：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/46a46b03839e0b0f799a01a775489976.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/46a46b03839e0b0f799a01a775489976.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>基础组件</strong><br>
<br>提供了绝大部分项目都应该需要的基础能力，也是其他上层功能组件很可能依赖的组件。hulk框架通过这些基础组件，使上层应用可以无感的与基础设施进行集成：<br>
<ul><li><strong>日志组件</strong>：默认支持与PHP兼容的打印格式（用于配置sia监控和报警），同时也兼容ftrace接入的格式（日志查询和问题定位）；</li><li><strong>云原生监控</strong>：默认支持Prometheus，对所有接口请求、Redis、RAL等远程调用进行多维度的Metrics采集，并通过Grafana展示；</li><li><strong>配置中心</strong>：通过配置中心，可以实时下发并生效配置。目前支持Apollo/iConf，支持功能包括-版本管理、热发布、灰度发布、权限管理、审核与审计等；</li><li><strong>事件追踪/定位</strong>：借助sentry，对于一些故障，我们可以秒级感知。hulk在异常信息中保存了比较完整的现场信息-如调用栈、request、集群和实例信息等，通过这些信息，可以直接定位问题的原因；</li></ul><br>
<br><strong>通用组件</strong><br>
<br>这一层的组件能力是通用的，提供了一些管理控制和切面能力：<br>
<ul><li><strong>RAL组件</strong>：hulk的RAL模块封装了GDP2的RAL主体功能，同时，对RAL进行了增强- a) 提供了通过字符串而非文件来进行RAL初始化和RAL懒加载功能；b) 提供了多个hook能力，如Prometheus的监控信息采集，熔断、降级等；</li><li><strong>服务治理</strong>：框架的服务治理能力是基于Sentinel （阿里开源的高可用流量防护组件）和配置中心来构建的，主要以流量为切入点，从限流、流量整形、熔断、降级等多个维度来协助保障微服务的稳定性，并提供动态控制能力；</li><li><strong>协程池</strong>：a) 可以自动调度海量协程，复用Goroutines，减少GC，b) 可以优雅处理panic，防止程序崩溃 c) 提供了：任务提交、获取运行中的Goroutine数量、封装了WaitGroup支持协程任务编排等功能；</li><li><strong>事件通知</strong>：框架与如流做了集成。用户将robot token配置在项目里，就可以直接使用ruliu组件向指定的如流群发送报警/通告。如流组件结合sentry，可以让我们第一时间知道程序出了问题并快速定位到问题。</li></ul><br>
<br><strong>扩展组件</strong><br>
<br>前两层功能对直接的业务处理逻辑参与较少，这一层的组件其能力多是为了处理某一类特定业务逻辑和场景，如Redis/MySQL/定时任务等：<br>
<ul><li><br>Redis组件：基于GDP2 Redis模块的封装并作了功能增，提供了：<br>
<ul><li>Metrics hook，对所有的Redis请求进行监控（Prometheus）打点（Latency/P99/QPS/错误码分布等）；</li><li>Sentry hook，支持将Redis错误在记错误日志同时发送到sentry；</li><li>降级hook，支持按集群/实例/百分比维度降级Redis访问；</li><li>熔断hook，支持按集群/实例/错误率/慢请求率对依赖的服务进行熔断设置。</li></ul></li><li><br>MySQL组件：MySQL组件是基于GDP2 MySQL和gorm_adapter的封装，在已有能力之上，进行了以下功能扩展：<br>
<ul><li>提供了Metrics hook，对所有的MySQL请求进行监控（Prometheus）打点（Latency/P99/QPS/错误码分布等）；</li><li>提供了sentry hook，支持将MySQL错误在记错误日志的同时发送到sentry。</li></ul></li><li><br>分布式锁：hulk提供了基于Redis的分布式锁实现。其中Redis连接是基于GDP2的Redis模块的改造，分布式锁功能是封装了开源项目Redsync；</li><li><br>定时任务：支持两种定时任务模式：<br>
<ul><li>带分布式锁的运行方式：对于多实例部署的定时任务，如果任务不是幂等的，则需要使用分布式锁对任务的调度运行进行控制；</li><li>不带分布式锁的运行方式：此模式下，如果部署了多实例，则所有实例上同一时刻的定时任务，会同时执行。</li></ul></li></ul><br>
<br><strong>HTTP Server</strong><br>
<br>hulk（目前只提供了HTTP Server能力）提供了很多通用且高效的HTTP Middleware，并对外暴露了一些管理控制接口，在一些特殊情况下，可以通过这些管理接口，在运行时干预服务的运行：<br>
<ul><li><strong>logger_middleware</strong>：用于记录HTTP的请求、响应、耗时等信息，同时支持实时修改日志打印策略-如按IDC/IP/百分比/UID/CUID等维度打印；</li><li><strong>timer_middleware</strong>：用于HTTP请求的监控埋点，可以输出可用性、TP99、流量、平响、错误码等Metrics，维度包括服务级/IDC/instance等；</li><li><strong>recover_middleware</strong>：用于捕获HTTP请求链路中的painc事件，并可自定义panic handler逻辑，如通过结合sentry和如流，可以实时感知并定位panic事件；</li><li><strong>flow_control_middleware</strong>：接口限流组件，可以通过配置中心或管理接口，对接口按IDC/instance维度进行限流；</li><li><strong>timeout_middleware</strong>：通过该Middleware或与配置中心结合使用，可以对接口按IDC维度进行超时控制；</li><li>其他Middleware可以查看hulk文档（如-internal_user_middleware、jager_opentracing_middleware、thirdparty_auth_middleware、b2logger_middleware等）</li><li><strong>管理控制接口</strong>：如健康检查接口，服务治理-熔断、限流、降级接口，metrics接口，线上实例性能调试接口等。</li></ul><br>
<br><h4>框架生态</h4>通过近一年的建设，我们初步构建了一个以hulk框架为中心的、符合好看业务场景的Go生态体系，包括：<br>
<ul><li><strong>标准目录规范</strong>：避免各个项目结构不统一，减少项目维护难度和工作量；</li><li><strong>代码生成器</strong>：基于hulk框架、标准目录规范、组件使用规范的代码生成器，目的是减少通用模块/组件使用不规范，解决通用流程编码、处理不一致的问题；</li><li><strong>hklib</strong>：好看的通用lib库，提供了一些的通用功能（也包含了很多PHP转Go过程中的一些orp通用/基础的函数/功能），也提供了50+对中台服务的调用client，减少重复代码，提升研发效率，提升可维护性；</li><li><strong>基础设施</strong>：Prometheus+Thanos集群、sentry服务、Apollo集群、Pyroscope性能分析平台等；</li><li><strong>iconf</strong>：好看自研配置中心，能力在对齐开源的Apollo之外，还增加/增强了一些功能，如-key维度的发布、更安全的配置获取、更简洁的操作页面、类分级发布等；</li><li><strong>artemis</strong>：服务可视化与故障智能定位系统，可以在该系统中看到服务的部署架构、服务内部调用链、多维度细粒度的近实时监控和关键日志。在发生可用性故障时，一些故障问题可以秒级的定位到原因和具体代码。</li></ul><br>
<br><h4>框架应用情况</h4>目前短视频所有Go服务都是基于hulk构建的，在资源、接口性能和可用性等方面都有一些阶段性产出和收益。<br>
<br>hulk框架应用现状：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/694ff80646fe671d0a37b800189e5abc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/694ff80646fe671d0a37b800189e5abc.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
资源和性能收益：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/ff32173cfc840c2e7f7948d4b938082a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/ff32173cfc840c2e7f7948d4b938082a.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><blockquote><br>资源和性能收益，很大一部分要归属于PHP->Go的技术栈切换；而框架为服务应用相应技术栈特性提供了便捷和高效的方式。</blockquote><h4>hulk服务架构</h4>下图描述了一个微服务（基于hulk）的架构全景图：<br>
<ul><li>框架中个各功能组件都是围绕业务各个场景和需求的，在业务逻辑中能够比较便捷的使用相关功能组件；</li><li>这些组件在启用后，也会与相应的基础设施进行交互融合，共同支撑服务的高效、可控和稳定的运行。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/e2d2ff80d36a6a5524cdcfbd1b6ae982.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/e2d2ff80d36a6a5524cdcfbd1b6ae982.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><blockquote><br>hulk组件初始化及与周边基础设施的集成，基本都可以通过环境变量/配置文件来完成。</blockquote><h3>框架能力与应用</h3>下面我们从日常开发遇到的一些痛点，来介绍框架的能力，并配以示例来说明这些能力是如何减少或解决痛点的。<br>
<h4>如何提升代码质量？</h4>代码质量会直接或间接的产生以下影响：<br>
<ul><li>代码质量会直接影响代码维护成本；</li><li>代码质量会影响程序出bug的概率；</li><li>代码质量会影响程序运行效率。</li></ul><br>
<br>hulk框架从以下三方面分别来提升代码质量。<br>
<br><strong>规范代码组织结构</strong><br>
<br><blockquote><br>降低项目维护成本，提升研发效率。<br>
  <ul><li><strong>通过标准目录规范</strong>，定义通用（HTTP服务）的项目layout，避免出现每人一种或多种layout，最终项目结构“百花齐放”的现象；</li><li><strong>通过代码生成器</strong>，帮助开发者生成项目模板，对初始化流程，各目录/文件的使用进行潜在约定。</li></ul></blockquote><strong>编码规范和静态检查</strong><br>
<br><blockquote><br>提升代码可读性，减少低级代码bug。<br>
  <ul><li>遵循百度Go编码规范+业务编码补充规范；</li><li>使用GDP的代码检查工具：go_fmt、goc。</li></ul></blockquote><strong>配套的压测和性能分析平台</strong><br>
<br><blockquote><br>确定服务的压力边界，发现潜在的性能问题。<br>
  <ul><li>压测和性能测试平台（测试环境）：nGrinder<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/25c820d082e901db01b648a6adde9415.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/25c820d082e901db01b648a6adde9415.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><strong>程序性能分析平台</strong>：Pyroscope。可以通过hulk自集成的管理接口，实时打开或关闭线上实例的“continuous-prof”功能，定位线上性能问题：<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/ccc44aacbc393dbe41a17f45b505fac3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/ccc44aacbc393dbe41a17f45b505fac3.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
</li></ul></blockquote><h4>如何提升开发迭代速度？</h4><ul><li>如何让开发者专注于业务逻辑与实现？</li><li>如何让开发者快速响应并完成产品需求？</li></ul><br>
<br>hulk框架为提升迭代速度，提供了以下支持。<br>
<br><strong>丰富的实用组件/功能</strong><br>
<br><blockquote><br>提升研发效率，避免试错，减少出错。<br>
  <ul><li><strong>程序增强组件</strong>：增强的Redis/MySQL功能，增强的RAL调用等。例-下图中的Redis监控，其监控指标是由hulk Redis组件自动采集计算的：<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/8f5841ae3ef990b4ae8d479c00395865.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/8f5841ae3ef990b4ae8d479c00395865.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><strong>优秀的开源组件</strong>：sentry、Prometheus+Grafana、Apollo、协程池等。例-Prometheus+Grafana：hulk框架默认支持Prometheus，可以对服务的可用性、QPS、耗时、错误码等Metrics自动计算收集：<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/f6ef666d309d11fd99efaf3df8051040.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/f6ef666d309d11fd99efaf3df8051040.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>丰富的HTTP Middleware。</li></ul></blockquote><strong>配置化、低代码支持</strong><br>
<br><blockquote><br>减少代码的修改和上线，提升需求的响应和完成速度。<br>
  <ul><li>hulk框架中大部分组件可以通过环境变量/配置文件来初始化；</li><li>业务逻辑中的可变数据与配置，可以通过Apollo/iconf实时下发和生效，无需代码修改和长流程上线。例-可以通过开箱即用的配置中心功能，实时下发并生效配置：<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/5d2ab81449ad25c73275fc2b5feeb7e4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/5d2ab81449ad25c73275fc2b5feeb7e4.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul></blockquote><h4>如何快速感知并定位问题？</h4><ul><li>开发者如何快速感知服务中的问题，严重问题如何实时感知？</li><li>开发者如何能从监控、日志、报警中获得详细的问题信息，以快速定位问题？</li></ul><br>
<br>hulk为提升SRE效率，从以下几个方面提供支持。<br>
<br><strong>完善的事件追踪定位与通告能力</strong><br>
<br><blockquote><br>能够实时追踪开发者自定义的错误并通告。<br>
  <ul><li><strong>实时事件追踪组件</strong>：sentry。hulk提供了开箱即用的sentry组件功能，可以像打印日志一样使用，sentry中的信息包含代码调用栈、上下文、自定义关键信息等：<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/2a3aee01b084b1e2ff984bd7ff30b8c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/2a3aee01b084b1e2ff984bd7ff30b8c9.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><strong>通告组件</strong>：ruliu。一行Token配置就可以开启如流功能，可以将一些需要立即关注的信息实时打到如流群里，同时还可以和sentry结合，实现异常问题实时感知和定位：<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/2c0af3d8ca7cbde0db3ea2a82a40429f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/2c0af3d8ca7cbde0db3ea2a82a40429f.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul></blockquote><strong>Prometheus+Sia监控支持</strong><br>
<br><blockquote><br>通过Prometheus与Noah的互补，支持多维度全方位监控，能够获得更多的服务稳定性相关信息。<br>
  <ul><li>Prometheus为开发者提供灵活的多维度的业务监控信息；</li><li>Sia可以为开发者提供基于日志的采集的服务稳定指标和容器、网络等资源维度监控信息。</li></ul></blockquote><strong>ftrace日志查询与分析功能</strong><br>
<br><blockquote><br>hulk默认支持ftrace平台的日志格式。<br>
  <ul><li>通过ftrace，可以便捷高效的查询用户维度的日志信息；<br>
  <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/7bee767d31088bb8da43fc0a5a132796.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/7bee767d31088bb8da43fc0a5a132796.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>通过pdo2命令，可以检索查询自定义规则的日志信息；</li></ul></blockquote><h4>基于hulk的服务可视化和故障智能定位系统</h4>artemis是我们基于hulk研发的一款服务可视化与故障智能定位追踪系统，它集服务部署架构可视化、近实时多维度监控、关键日志、服务调用链等多方面信息，可以快速、高效、精准的发现和定位稳定性问题。<br>
<br>该系统目前已接入好看/全民/度咔等多个后端服务，极大加速了故障定位效率。在一些故障场景，可以秒级定位问题，给出问题的代码行。<br>
<br><strong>服务部署架构</strong><br>
<br>通过实例列表，可以获取服务的IDC列表、instance列表和详情，并提供了便捷高效的调试入口和登录指令：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/0e4c5d644bc960beb88e549168c5040e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/0e4c5d644bc960beb88e549168c5040e.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>近实时多维度监控</strong><br>
<br>artemis提供的近实时监控，能够提供更多维度信息，这些维度是Sia和Prometheus无法提供的，如：<br>
<ul><li>某个URI下面的某个下游（或下游实例）RAL的QPS、耗时、可用性；</li><li>某个服务实例实例的URI或RAL的监控信息。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/941f25e99e4dea62b330031504b6f31c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/941f25e99e4dea62b330031504b6f31c.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>关键日志</strong><br>
<br>由于与hulk的深度集成，在业务代码中打印warning级别以上的日志时，artemis能拿到更多的日志信息，如-各维度信息、调用栈、上下文等：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/13b3533133c511c05fae67cdc3d0bf84.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/13b3533133c511c05fae67cdc3d0bf84.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/f0fd4588566e05bdaf483c91b7995ea9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/f0fd4588566e05bdaf483c91b7995ea9.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>服务调用链</strong><br>
<br>在hulk框架的协助下，artemis还可以获取到URI及URI所依赖的RAL调用信息，由此可以构建出请求调用链，并实时展示调用链上的相关Metrics信息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/151f3789a6a0105e023ae083522c763a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/151f3789a6a0105e023ae083522c763a.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
不同颜色的链路代表不同的可用性：红色-1个9及以下，黄色-2个9，蓝色-3个9，灰色-4个9。通过服务调用链，可以非常直观的看到服务里，哪个接口有问题，还可以看到哪些下游影响了这个接口的可用性。<br>
<br><strong>使用案例</strong><br>
<br>通过与报警系统的联动，可以在发生报警的第一时间，在artemis系统中找到受影响的服务及URI，确定是否是下游引起，错误是什么，哪一行代码报了错等，以下是一个artemis的实际应用示例。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/c5fb06ad968ef6f3ac7ee0409122f669.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/c5fb06ad968ef6f3ac7ee0409122f669.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>hulk虽然是⼀个新的Go语⾔Web框架，但不是重复造轮，⽽是站在⼚内和开源软件的基础上，结合业务实际开发、部 署、运⾏、运维环境，对这些开源框架和⼯具进⾏取⻓补短、⼆次开发，最终切合实际的业务使⽤场景。同时，围绕hulk初步构建起的Go生态，为服务在开发、部署、运行、运维等各个阶段都提供了有力支持。<br>
<br>最后，希望短视频研发部在Go服务化架构升级/研发框架上的⼀些实践、⽅案和经验，能够给有相同架构升级需求、 在Go项⽬实践中遇到问题的其他业务线同学⼀些帮助和参考。<br>
<br>附录：<br>
<ol><li><a href="http://hulk-go.baidu-int.com/" rel="nofollow" target="_blank">http://hulk-go.baidu-int.com/</a></li><li><a href="http://gdp.baidu-int.com/" rel="nofollow" target="_blank">http://gdp.baidu-int.com/</a></li></ol><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/JdBjyb95U_oijYoszJubEw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/JdBjyb95U_oijYoszJubEw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            