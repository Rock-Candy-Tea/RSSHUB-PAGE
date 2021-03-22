
---
title: 'Serverless 时代 DevOps 的最佳打开方式'
categories: 
    - 编程
    - Dockone - 周报
author: Dockone - 周报
comments: false
date: 2021-03-22 03:42:44
thumbnail: 'http://dockone.io/uploads/article/20210318/ba539ddbefef3cb1c0b32b47550ec3b1.jpg'
---

<div>   
<br>作者 | 许成铭（竞霄）<br>
来源 | <a href="https://mp.weixin.qq.com/s/v0iQDgDrIr9BZCv3MlijWA">阿里巴巴云原生公众号</a><br>
<br><h1>DevOps 简析</h1>传统软件开发过程中，开发和运维是极其分裂的两个环节，运维人员不关心代码是怎样运作的，开发人员也不知道代码是如何运行的。<br>
<br>而对于互联网公司而言，其业务发展迅速，需要快速更新以满足用户差异化的需求或者竞对的产品策略，需要进行产品的快速迭代，通过小步快跑的方式进行敏捷开发。<br>
<br>对于这种每周发布 n 次甚至每天发布 n 次的场景，高效的协作文化就显得尤为重要。DevOps 就在这种场景下应运而生，它打破了开发人员和运维人员之间的壁垒。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/ba539ddbefef3cb1c0b32b47550ec3b1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/ba539ddbefef3cb1c0b32b47550ec3b1.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>DevOps 是一种重视“软件开发人员（Dev）”和“IT 运维技术人员（Ops）”之间沟通合作的文化、运动或惯例。通过自动化“软件交付”和“架构变更”的流程，来使得构建、测试、发布软件能够更加地快捷、频繁和可靠。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/b7bc02b3231187c907e61667ebe8284c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/b7bc02b3231187c907e61667ebe8284c.jpg" class="img-polaroid" title="1-1.jpg" alt="1-1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>上图是一个完整的软件开发生命周期，DevOps 运动的主要特点是倡导对构建软件的整个生命周期进行全面的管理。<br>
<br><strong>DevOps 工程师的职责</strong>：<br>
<ul><li>管理应用的全生命周期，比如需求、设计、开发、QA、发布、运行；</li><li>关注全流程效率提升，挖掘瓶颈点并将其解决；</li><li>通过标准化、自动化、平台化的工具来解决问题。</li></ul><br>
<br><strong>DevOps 的关注点在于缩短开发周期，增加部署频率，更可靠地发布</strong>。通过将 DevOps 的理念引入到整个系统的开发过程中，能够显著提升软件的开发效率，缩短软件交付的周期，更加适应当今快速发展的互联网时代。<br>
<br><h1>Serverless 简析</h1><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/1fa87384ad48e85f11448fc1a78a1d84.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/1fa87384ad48e85f11448fc1a78a1d84.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>上图左侧是谷歌趋势，对比了 Serverless 和微服务的关键词趋势走向，可看出随着时间变化，<strong>Serverless 的热度已经逐渐超过微服务</strong>，这说明全世界的开发人员及公司对 Serverless 非常青睐。<br>
<br>那 Serverless 究竟是什么？上图右侧是软件逻辑架构图，有开发工程师写的应用，也有应用部署的 Server（服务器），还有 Server 的维护操作，比如资源申请、环境搭建、负载均衡、扩缩容、监控、日志、告警、容灾、安全、权限等。而 Serverless 实际上是把 Server 的维护工作屏蔽了，对于开发者是黑盒，这些工作都由平台方支持，对业务来说只需关注核心逻辑即可。<br>
<br>总得来说，Serverless 架构是“无服务器”架构，是云计算时代的一种架构模式，能够让开发者在构建应用的过程中无需关注计算资源的获取和运维，降低运营成本，缩短上线时间。<br>
<br><h1>Serverless 时代 DevOps 的变化</h1><h2>1. Serverless 的特性</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/323119058742ced1bbbfe59fe628f818.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/323119058742ced1bbbfe59fe628f818.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>上图左侧为 2020 年中国云原生用户调查报告中 Serverless 技术在国内的采用情况，图中显示近三成用户已经把 Serverless 应用在生产环境中，16% 的用户已经将 Serverless 应用在核心业务的生产环境，12% 的用户也已经在非核心业务的生产环境中用到 Serverless，可见国内对 Serverless 接受度较高。<br>
<br>上图右侧为咨询公司 O'Reilly 对全球不同地区不同行业的公司进行的调查报告结果，图中显示一马当先使用 Serverless 架构的就是 DevOps 人员。<br>
<br>那么当 Serverless 遇上 DevOps，会发生哪些变化呢？首先我们看一下云原生架构白皮书中对 Serverless 特性的归纳总结：<br>
<ul><li><strong>全托管的计算服务</strong>  </li></ul><br>
<br>用户只需要编写自己的代码来构建应用，无需关注同质化的复杂的基础设施的开发运维工作。<br>
<ul><li><strong>通用性</strong></li></ul><br>
<br>能够在云上构建普适的各种类型应用。<br>
<ul><li><strong>自动的弹性伸缩</strong></li></ul><br>
<br>用户无需对资源进行预先的容量规划，业务如果有明显的波峰波谷或临时容量需求，Serverless 平台都能够及时且稳定地提供对应资源。<br>
<ul><li><strong>按量计费</strong></li></ul><br>
<br>企业可以使成本管理更加有效，不用为闲置资源付费。<br>
<br>Serverless 让运维行为对开发透明，开发人员只需关注核心业务逻辑的开发，进而精益整个产品开发流程，快速适应市场变化。而上述 Serverless 的这些特性与 DevOps 的文化理念及目标是天然契合的。<br>
<br><h2>2. Serverless 开发运维体验</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/7bee0ba6488b8cfcd2f647ea29371dd7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/7bee0ba6488b8cfcd2f647ea29371dd7.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>传统应用构建的流程中，DevOps 人员管理整个生命周期的步骤非常多：<br>
<ul><li>在资源准备阶段，要购买 ECS 进行机器初始化等系列操作；</li><li>在研发部署阶段，需要把业务应用、监控系统、日志系统等旁路系统部署在 ECS 上；</li><li>在运维阶段，你不仅需要运维自己的应用，还需运维 Iaas 及其他旁路的监控、日志、告警组件。</li></ul><br>
<br>而如果迁到 Serverless，其开发体验是怎么样的呢？<br>
<ul><li>在资源准备阶段，不需要任何资源准备，因为 Serverless 是按需使用、按量付费的，不用关注底层 Server；</li><li>在研发部署阶段，只需要将自己的业务部署到对应的 Serverless 平台上；</li><li>在运维阶段，彻底做到了免运维。</li></ul><br>
<br>可以看到，传统应用构建流程中的 Iaas 及监控、日志、告警，在 Serverless 上完全没有，它以全托管、免运维的形式展现给用户。<br>
<br><h1>Serverless 时代 DevOps 的最佳实践</h1>上文介绍的体验其实就是基于阿里云的一款 Serverless 产品——SAE 来实现的。Serverless 应用引擎（SAE）是阿里云 Serverless 产品矩阵中提供的 DevOps 最佳实践。先简单介绍一下 SAE：<br>
<br><h2>1. Serverless 应用引擎（SAE）</h2>SAE 是一款面向应用 Serverless PaaS 平台，支持 Spring Cloud、Dubbo、HSF 等主流的应用开发框架。用户可以零代码改造，直接将应用部署到 SAE 上，并且按需使用、按量付费、秒级弹性，可以充分发挥 Serverless 的优势，为用户节省闲置的资源成本。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/a422384769ff84339072fa4265e30c28.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/a422384769ff84339072fa4265e30c28.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>在体验上，SAE 采用全托管、免运维的方式，用户可以聚焦于核心的业务逻辑开发，而应用的整个生命周期管理，如监控、日志、告警，这些都由 SAE 完成。可以说，SAE 提供了一个成本更优、效率更高的一站式应用托管方案，用户可以做到零门槛、零改造、零容器基础就可以享受到 Serverless 带来的技术红利。<br>
<br>Serverless 应用引擎（SAE）三大特点：<br>
<ul><li><strong>0 代码改造</strong>：微服务无缝迁移，开箱即用，支持 War/Jar 自动构建镜像；</li><li><strong>15s 弹性效率</strong>：应用端到端快速扩容，应对突发流量；</li><li><strong>57% 降本提效</strong>：多套环境按需启停，降本且提效。</li></ul><br>
<br><h2>2. 构建高效闭环的 DevOps 体系</h2>SAE 内构建了高效闭环 DevOps 体系，覆盖开发态、部署态和运维态的整个过程。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/6296588c85c16601ea6f31072d42e5ce.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/6296588c85c16601ea6f31072d42e5ce.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>中大型企业一般都使用企业级的 CICD 工具（如 Jenkins 或云效）部署到 SAE，从而完成从源码到构建再到部署的整个流程。<br>
<br>对于个人开发者或者中小企业，更倾向于使用 Maven 插件或 IDEA 插件一键部署到云端，方便本地调试，也提升了整个的用户体验。<br>
<br>当部署到 SAE 之后，可以进行可视化的智能运维操作，比如高可用运维（服务治理、性能压测、限流降级等）、应用诊断（线程诊断、日志诊断、数据库诊断等）以及数据化运营。以上操作都是部署到 SAE 之后，用户可以开箱即用的现成的功能。<br>
<br>用户通过 SAE 可以非常方便地实现整体的开发运维流程，感受 Serverless 带来的全方位体验和效率上的提升。下面介绍几个 SAE 的最佳实践：<br>
<br><h2>3. 部署态最佳实践：CI/CD</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/3bd855c864491a749ab4441b750244ff.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/3bd855c864491a749ab4441b750244ff.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>SAE 目前支持三种部署方式，分别是 War、Jar 和镜像</strong>。<br>
<br>如果用户使用 Spring Cloud、Dubbo 或 HSF 这类应用，可以直接打包或者填写对应的 URL 地址，就可以直接部署到 SAE 上。而对于非 Java 语言的场景，可以通过镜像方式进行部署。后续我们也会支持其他的语言包以自动化构建的方式进行部署。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/b17ef9c5273e4b751f88e54a773d9fe7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/b17ef9c5273e4b751f88e54a773d9fe7.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>除了直接部署之外，SAE 也支持本地部署、云效部署和自建部署这三种方式</strong>。<br>
<br>本地部署依赖 CloudToolkit 插件，对 IDEA/Eclipse 进行了支持，用户可以在 IDEA 里一键部署到 SAE 上，无需登录，方便地进行自动化操作。<br>
<br>云效部署是阿里云提供的企业级一体化 CICD 平台型产品，通过云效可以监听代码库的变动，如果进行 Push 操作，就会触发云效的整个发布流程。比如进行代码检查或者单元测试，在对这个代码进行编译、打包、构建，构建好后会生成对应的构建物，之后它会调用 SAE 的 API，然后执行整体的部署操作。这一整套流程也是开箱即用的，用户只需要在云效控制台上进行可视化配置就可以把整个流程串起来。<br>
<br>自建部署指用户的公司如果是直接通过 Jenkins 进行构建的话，也可以直接使用 SAE。Jenkins 作为开源的最大的 CICD 平台，我们也提供了有力支持，许多用户也通过 Jenkins 成功地部署到 SAE 上。<br>
<br><h2>4. 部署态最佳实践：应用发布三板斧</h2><strong>应用发布三板斧包括：可灰度、可监控、可回滚</strong>。在阿里内部所有的变更都需要严格做到上述的“三板斧”，而 SAE 作为一款云产品，也是把阿里巴巴的最佳实践对外输出进行产品化的集成。<br>
<ul><li><strong>可灰度</strong>：支持单批、分批、金丝雀等多种发布策略；支持按流量灰度，批次间自动/手动发布，分批间隔等多种发布选项；</li><li><strong>可监控</strong>：发布过程中清晰对比不同批次基础监控与应用监控指标异动，及时暴露问题，定位变更风险；</li><li><strong>可回滚</strong>：在发布过程中，允许人工介入控制发布流程，如异常中止、一键回滚。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/644ea28dee6e4115357ba2e700426bec.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/644ea28dee6e4115357ba2e700426bec.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/3c186f193cbf7247b6166df6a8ad9f14.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/3c186f193cbf7247b6166df6a8ad9f14.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>上图为控制台截图，可以看到在部署上我们支持单批、分批和灰度三种方式进行发布。<br>
<br>执行发布的过程都是通过发布端进行，每个发布端都有具体的步骤，首先进行构建镜像，然后初始化环境，接着创建和更新部署配置。用户可以清晰地看到发布端当前的运行进度与状态，方便排查。<br>
<br><h2>5. 运维态最佳实践：全方位可观测</h2>SAE 提供全方位可观测，可以对分布式系统中的任何变化进行观测。当系统出现问题时，可以便捷地定位问题、排查问题、分析问题；当系统平稳运行时，也可以提前暴露风险，预测可能出现的问题。通过 SAE 用户可以对自己的应用了如指掌。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/4c6172cdaedf56023ecfc458dc802574.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/4c6172cdaedf56023ecfc458dc802574.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>这里列举了可观测性的三个方面：Metrics、Logging 、Tracing。<br>
<ul><li><strong>Metrics</strong></li></ul><br>
<br>代表聚合的数据，SAE 提供如下基础监控指标：<br>
<br>1）基础监控：CPU、MEM、Load、Network、Disk、IO；<br>
2）应用监控：QPS、RT、异常数、HTTP 状态码、JVM 指标；<br>
3）监控告警：丰富的告警源上报、告警收敛处理、多种告警渠道触达（如邮箱、短信、电话等）。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/8407614763b77a9cc1ce626a03ff0217.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/8407614763b77a9cc1ce626a03ff0217.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>Logging</strong></li></ul><br>
<br>代表离散的数据，提供以下功能：<br>
<br>1）实时日志：Stdout、Stderr 实时查看；<br>
2）文件日志：自定义采集规则、持久化存储、高效查询；<br>
3）事件：发布单变更事件、应用生命周期事件、事件通知回调机制。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/9e0308253fa49d65caab66b93fcf894c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/9e0308253fa49d65caab66b93fcf894c.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>Tracing</strong></li></ul><br>
<br>意味着可以按请求维度进行排查，提供如下开箱即用的功能：<br>
<br>1）请求调用链堆栈查询；<br>
2）应用拓扑自动发现；<br>
3）常用诊断场景的指标下钻分析；<br>
4）事务快照查询；<br>
5）异常事务和慢事务捕捉。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/17d113332d67141f9ce253525f2732da.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/17d113332d67141f9ce253525f2732da.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>6. 运维态最佳实践：在线调试</h2><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/1a4af43697a20b2411b57c7d453e22f3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/1a4af43697a20b2411b57c7d453e22f3.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>通过 SAE 在线调试可以访问单实例的目标端口，相当于用户在本地可以直接访问云端某个应用的某个具体实例，原理是为实例提供了端口映射的 SLB，通过这个能力用户可以实现如下功能：<br>
<ul><li><strong>SSH / SFTP 访问实例</strong></li></ul><br>
<br>可以在本地通过 SSH 直接连到应用的具体的实例上，或者通过 SFTP 进行上传/下载文件。<br>
<ul><li><strong>Java retmote debug</strong></li></ul><br>
<br>相当于在 IDEA 里配置一个断点，再远程连接到对应的 SAE 的实例上，这样就可以通过断点来查看整个方法的调用站与上下文信息，对线上正在运行的应用进行诊断。<br>
<ul><li><strong>其他诊断工具连接实例</strong></li></ul><br>
<br>其他诊断工具也可以通过在线调试的手段连接到 SAE 的实例上，进而看到 Java 的一些信息，比如堆栈或者线程等。 <strong>适用场景</strong>：针对运行时在线应用的实时观测运维及问题排查求解。<br>
<br><h2>7. 开发态最佳实践：端云联调</h2>针对微服务场景，我们提供了一个非常好用的能力：端云联调。它基于 CloudToolkit 插件+ 跳板机，<strong>可以实现</strong>：<br>
<br>1）本地服务订阅并注册到云端 SAE 内置的注册中心；<br>
2）本地服务可以和云端 SAE 服务互相调用。 <br>
<br><strong>适用场景</strong>：<br>
<br>1）微服务应用迁移到云端 SAE，迁移过程中的开发联调；<br>
2）本地开发测试验证。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/dbb3fede09a9760c8ebda7cb768a9bc1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/dbb3fede09a9760c8ebda7cb768a9bc1.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>这个功能的原理是需要在用户的 VPC 内，然后通过 ECS 代理服务器作为跳板机，ECS 可以和同一个 VPC 内的 SAE 应用进行互调，然后这台 ECS 通过反应代理的方式，可以与本地进行连接。<br>
<br>CloudToolkit 插件会在应用启动时就注入对应 SAE 注册中心的地址，以及微服务的一些上下文参数，使得用户本地的应用通过跳板机连到 SAE 的应用上，从而进行整个端云联调的过程。<br>
<br><h2>作者简介</h2>许成铭，花名：竞霄，先后参与 aPaaS 领域 EDAS 和 SAE 后端研发工作，经历云原生与 Serverless 技术趋势变革。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            