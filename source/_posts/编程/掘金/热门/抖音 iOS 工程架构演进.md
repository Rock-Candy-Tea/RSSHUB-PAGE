
---
title: '抖音 iOS 工程架构演进'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12787cca0a64d45a38c7fc1a4f5e591~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 17:53:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12787cca0a64d45a38c7fc1a4f5e591~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言介绍</h1>
<p>2016.09.26，抖音版本 1.0.0 上线，随后不断迭代优化和丰富产品，截止目前，抖音日活跃用户突破 6 亿，短短 4 年间，抖音从零爆发性增长。</p>
<p>快速的业务发展也对技术支撑提出了更高的要求，为了保障敏捷的业务开发，提升跨团队的协同合作效率，提高本地研发和 CI/CD 效率，抖音 iOS App 工程架构在不同的阶段进行了不同的技术方案的改进，满足合理的架构演化，同时又不影响正常的业务迭代速度。</p>
<h1 data-id="heading-1">抖音工程架构演进</h1>
<p>架构演进的本质是为了提高研发效率，提高代码稳定性和保证代码质量。架构要解决的问题是如何组织代码。</p>
<p>合理的架构设计可以解决大型项目跨团队协作分工和多业务线并行开发的效率问题。抖音工程代码从一开始就采用了组件化思路，依赖管理工具是定制版的 Cocoapods。</p>
<p>以下动画介绍了抖音工程架构经历的四个阶段的演进过程：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12787cca0a64d45a38c7fc1a4f5e591~tplv-k3u1fbpfcp-watermark.image" alt="623eb9ec-8827-44ff-a6a9-544edda4c2f9.gif" loading="lazy" referrerpolicy="no-referrer">
图1：抖音项目工程架构演进</p>
<h3 data-id="heading-2">组件化</h3>
<p>在大型项目快速发展的过程中，要保证敏捷开发迭代的最大障碍就是快速膨胀的代码体积导致的编译效率问题，依赖关系复杂化问题，以及业务线代码冲突问题。</p>
<p>移动端项目可以类比后端项目中采用的微服务架构，要解决多业务线并行开发、并行测试问题，采用流水线式迭代开发，提高发版、集成、交付、提审、发布效率，结合分治思想技术选型上可以采用组件化的方案。</p>
<p>大部分小型项目，组件化仅仅做到代码分仓，使用 Cocoapods 的来管理组件依赖，就像抖音项目最初的工程形态。</p>
<p>但是对于几百号人、几十个业务线规模的大型项目，需要设计一套合理的组件分层架构，理清组件间依赖关系，需要 CI/CD 工具链支撑组件发版与集成，需要本地研发工具支撑本地代码同步、工程配置、依赖管理和效率优化。</p>
<h3 data-id="heading-3">流水线式迭代开发</h3>
<p>流水线（pipeline）技术是指在程序执行时多条指令重叠进行操作的一种准并行实现技术，该技术可以充分提高资源的利用率，同时缩短产品的研发周期。
对于客户端项目，流水线技术能很大程度满足敏捷开发迭代的节奏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83827de797164c629eae98a3b46a0efd~tplv-k3u1fbpfcp-zoom-1.image" alt="图2：抖音流水线式迭代发版" loading="lazy" referrerpolicy="no-referrer">
图2：抖音流水线式迭代发版</p>
<h1 data-id="heading-4">抖音工程架构演进</h1>
<h2 data-id="heading-5">阶段一：抖音原始工程架构（Original architecture of project）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8754745a0f354003a4023f1b4edfe26d~tplv-k3u1fbpfcp-zoom-1.image" alt="图3：抖音项目原始工程架构图" loading="lazy" referrerpolicy="no-referrer">
图3：抖音项目原始工程架构图</p>
<p>抖音项目一开始是单体架构+Cocoapods，业务代码、工程配置、资源文件全部放在一个大业务仓库。由 Podfile 文件描述第三方仓库的依赖版本。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152506deb3c34ca58c7c6ef2aa631304~tplv-k3u1fbpfcp-zoom-1.image" alt="图4：抖音项目原始工程架目录结构" loading="lazy" referrerpolicy="no-referrer">
图4：抖音项目原始工程架目录结构</p>
<h2 data-id="heading-6">阶段二：分离壳工程后的工程架构（After splitting of host shell pod）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ea434183158412d81eeca7fa62ad3b8~tplv-k3u1fbpfcp-zoom-1.image" alt="图5：拆分壳工程后的工程架构" loading="lazy" referrerpolicy="no-referrer">
图5：拆分壳工程后的工程架构</p>
<p>分离壳工程后，工程配置、部分系统资源、工程主入口被拆分到主宿主壳工程。</p>
<p>Podfile 拆分出版本依赖管理文件 Podfile.seer，由依赖管理平台进行各个版本的容器化管理，业务仓跟随宿主集成发版，打平依赖，解决版本依赖决议耗时问题。</p>
<p>大业务仓中的代码和资源被拆分到各个业务线的仓库下，由 podspec 文件描述内外依赖。业务线仓库增加 ModuleInterface subspec，存放对外接口，采用依赖注入方式实现接口隔离，初步建立接口层。</p>
<p>业务仓库之间规定只能依赖其他业务仓库的 ModuleInterface subspec，通过 lint 进行编译检查。</p>
<p>部分基础能力代码被拆分成基础仓库，跟第三方仓库一样独立发版。本地研发工具支持单仓开发和多仓开发，不参与代码修改的仓库通过二进制的方式进行链接。同时 CI 流程上也支持通过二进制打测试包，提高打包效率。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2574724baada499691156a6c4f0b17be~tplv-k3u1fbpfcp-zoom-1.image" alt="图6：抖音项目拆分壳工程后目录结构
" loading="lazy" referrerpolicy="no-referrer">
图6：抖音项目拆分壳工程后目录结构</p>
<h3 data-id="heading-7">壳工程</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77e6acfdf6a647bab1e77af60ec63759~tplv-k3u1fbpfcp-zoom-1.image" alt="图7：壳工程抽象" loading="lazy" referrerpolicy="no-referrer">
图7：壳工程抽象</p>
<p>为了满足一个工程同时支持多个项目、部分业务线功能复用、部分业务线中台化发展的需求，我们把所有业务线抽象成独立的 Pod，所有业务 Pod 必须通过宿主的壳工程进行集成发版。</p>
<p>壳工程包含了项目依赖的 Pod 信息描述，同时还包括工程的配置、部分系统级别的资源文件、工程主入口代码。基于多份宿主壳工程，一份代码可以打包出抖音、抖音极速版等项目。</p>
<p>同时，基于宿主壳工程，一些业务线可以通过自动化同步生成自己的子壳工程，实现业务线自己的 Example 工程，进行独立开发，比如有语音通话的 Example 工程，有工具的 Example 工程，有直播的 Example 工程等等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c3df0aadea340c5b2f6815959a6515a~tplv-k3u1fbpfcp-zoom-1.image" alt="图8：子壳工程配置同步同步" loading="lazy" referrerpolicy="no-referrer">
图8：子壳工程配置同步同步</p>
<h3 data-id="heading-8">接口层</h3>
<p>接口层顾名思义，只提供依赖的抽象接口，所有接口都是 protocol 协议声明。</p>
<p>接口层限制了所有其他依赖，类、枚举、 外部协议都采用前向声明，podspec 上只允许声明对 DI（依赖注入）框架的依赖。接口层满足封装、隔离和组合的原则。</p>
<ul>
<li>业务层面对外封装了实现代码；</li>
<li>编译层面隔离了组件间依赖传递，减少头文件 import 嵌套提高编译缓存的命中率，对于 swift 业务组件，还能达到减少编译传递的问题；</li>
<li>架构层面声明抽象协议支持接口组合；</li>
<li>DI 容器框架同时支持 stateless DI 容器，也支持 stateful DI 容器。</li>
</ul>
<h3 data-id="heading-9">依赖打平</h3>
<ul>
<li>
<p>采用 Cocoapods 本身自带的版本依赖决议进行版本分析会消耗大量的时间；</p>
</li>
<li>
<p>Podfile.lock 过于繁琐，可读性很差，难以解决 Podfile.lock 的冲突；</p>
</li>
<li>
<p>隐式依赖被动/不符合预期地升级，难以确定性地声明所有依赖，防止隐式依赖被升级；</p>
</li>
<li>
<p>依赖版本在 Podfile/Podfile.lock 重复声明，增加了解决冲突的成本；</p>
</li>
<li>
<p>Podfile.lock 参与依赖版本决议流程比较复杂，会出现不符合预期的情况。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6941fc6cd2c74f0786e618f50d8ce38d~tplv-k3u1fbpfcp-zoom-1.image" alt="图9：把版本管理和仓库源信息迁移到 Podfile.seer 文件
" loading="lazy" referrerpolicy="no-referrer">
图9：把版本管理和仓库源信息迁移到 Podfile.seer 文件</p>
<ul>
<li>hook 掉 Cocoapods 采用 podfile.lock 进行版本决议的逻辑，采用 Podfile.seer 文件直接描述所有组件的版本信息，打平依赖。</li>
</ul>
<h2 data-id="heading-10">阶段三：单仓多组件工程架构（Multicomponents in single repo）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c833b585c24408caf173ec04557f3bc~tplv-k3u1fbpfcp-zoom-1.image" alt="图10：拆分单仓多组件后的工程架构" loading="lazy" referrerpolicy="no-referrer">
图10：拆分单仓多组件后的工程架构</p>
<p>采用单仓多组件后，每个业务线仓库支持添加 podspec 增加组件，实现更小粒度的二进制依赖。业务线仓库内划分业务实现层、业务接口层、服务层和基础层，都是通过集成方式发版。</p>
<p>新增的服务层主要存放公共的业务逻辑和通用服务，限制 UI，一是满足业务逻辑复用，二是满足子壳工程最小化二进制依赖。同时服务层的服务接口也达到隔离依赖传递的目的，在不同的宿主上，支持通过改变服务层实现替换后台能力或者底层能力。建立分层间的依赖准入规则，完善 lint 编译链接检查。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5a0e192c74490d9d293f0a23fbed66~tplv-k3u1fbpfcp-zoom-1.image" alt="图11：单仓多组件目录结构" loading="lazy" referrerpolicy="no-referrer">
图11：单仓多组件目录结构</p>
<h3 data-id="heading-11">编译链接完备性校验</h3>
<ul>
<li>编译校验：分开编译各个 subspec，确保每个 subspec 的依赖是正确的(由于 subspec 没有编译隔离)</li>
<li>接口符号校验：校验当前接口组件(ModuleInterface)中符号是否完备的，以保证其他组件单独引用是否能正常使用。如 extern 声明的全局变量。</li>
</ul>
<h3 data-id="heading-12">分层依赖准入规则：</h3>
<ul>
<li>高层依赖低层</li>
<li>实现依赖接口</li>
<li>接口层无依赖</li>
<li>前向声明优先</li>
<li>服务层去"UI"</li>
</ul>
<p>以下动画展示了业务实现层和服务实现允许依赖的分层：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f66324d91934b7ca1abd15fab47cd52~tplv-k3u1fbpfcp-watermark.image" alt="2021412-164953.gif" loading="lazy" referrerpolicy="no-referrer">
图12：组件依赖关系示意图动画</p>
<h2 data-id="heading-13">阶段四：Example 子壳工程架构（Subshell for bizcomponent in example project）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74aa9d8a59c4490789ded6b2845cd2d4~tplv-k3u1fbpfcp-zoom-1.image" alt="图13:子壳工程架构" loading="lazy" referrerpolicy="no-referrer">
图13:子壳工程架构</p>
<p>每个业务仓从宿主同步工程配置构建子壳工程。增加 AWELaunchKit 为子壳工程提供运行时的基础能力。通过服务层提供业务间运行时共享的服务能力，满足代码复用和更小二进制依赖。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cafab20cd834e72abda071578b1f936~tplv-k3u1fbpfcp-zoom-1.image" alt="图14：子壳工程目录结构" loading="lazy" referrerpolicy="no-referrer">
图14：子壳工程目录结构</p>
<h3 data-id="heading-14">AWELaunchKit</h3>
<p>AWELaunchKit 框架为宿主和其他子壳工程提供了基础服务的依赖和初始化配置。同时提供了一套启动加载的 BootTasks 管理框架，部分业务涉及启动相关的逻辑可以在业务仓对应的服务层中实现，并通过 BootTasks 管理框架注册到启动加载器里面。</p>
<p>同时框架还提供了一套宿主 UI 入口和自定义入口框架。为了方便测试和调试，也整合了整套测试调试框架。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b50d5dc3f22450b9818d7ababe1806c~tplv-k3u1fbpfcp-zoom-1.image" alt="图15：子壳工程依赖关系" loading="lazy" referrerpolicy="no-referrer">
图15：子壳工程依赖关系</p>
<h3 data-id="heading-15">组件化探索过程中遇到的一些问题：</h3>
<h4 data-id="heading-16">二进制污染</h4>
<p>组件之间的依赖除了显式的依赖，还存在很多隐式依赖，代码层面，除了普通的接口依赖，还有宏依赖、枚举依赖、全局变量依赖以及内联函数等的依赖。单仓 lint 进行编译链接完备性检查并不能解决依赖变动对其他二进制的影响。</p>
<p>因此需要借助源码层面的依赖分析，判断当前组件的变更对其他依赖当前组件的二进制是否有影响，在 CI 流程中及时发现并拦截。否则错误的二进制发版，会直接导致整个 CI 研发流程和本地研发都受到影响。</p>
<h4 data-id="heading-17">编译优化</h4>
<p>编译优化最高效的方式就是提高缓存的利用率。对于本地研发和 CI 流程，都涉及分布式编译缓存同步。同时通过编译参数优化、依赖优化、hmap 优化也能不同程度的提高编译效率</p>
<h4 data-id="heading-18">主干分支稳定性问题</h4>
<p>对于多业务线并行开发，几百号人的业务开发团队，如果主干分支一旦出现问题，那么解决问题的时间就需要乘上几百倍。因此，需要从编译层面和运行层面都要有足够的机制去保证一个稳定的主干分支，才能保证业务侧的长期稳定性。</p>
<h4 data-id="heading-19">业务层的依赖耦合问题</h4>
<p>大型项目动则千万行的代码，代码间的依赖关系是复杂的网状关系。需要基于代码的语法树模型，从语义中去分析不合理的依赖，并输出治理的方案。</p>
<p>我们内部自研了源码依赖关系分析平台用于依赖关系分析监控和代码治理，长期监控组件间的依赖度。同时，需要建立依赖健康度模型，从长期演进的角度去监控防止代码的劣化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ba45bac33214f4a93ee3f60ba129f80~tplv-k3u1fbpfcp-zoom-1.image" alt="图16：spider 组件依赖分析平台" loading="lazy" referrerpolicy="no-referrer">
图16：spider 组件依赖分析平台</p>
<h1 data-id="heading-20">总结</h1>
<p>大型项目的组件化工作是一个系统性工程。涉及工程架构的改造、CI/CD 研发工具链的支撑、本地研发工具链的支撑，业务架构的设计优化，需要从各个方面综合考虑成本和收益。</p>
<p>没有最好的架构，只有更好的架构，在架构演进的过程中，我们需要充分考虑架构的改动对业务的影响以及能给业务带来的收益。好的架构一定是能帮助业务节省时间，保证质量的。与此同时，我们在架构改进的过程中，要保证不能影响业务的正常迭代，所以向前兼容且避免大面积冲突也是很重要的事情。</p>
<p>组件化里面处处都有惊喜，比如一个小小的 hmap 优化，可以很大程度的减少编译耗时，比如一个二进制的压缩和解压的优化，可以很大程度减少 pod install 的整体耗时。</p>
<p>当然这里面也会有很多很棘手的问题，需要通过一些特殊的方案解决，比如针对分布式开发，由于阻塞式发版必然会导致一些不同分支存在冲突的代码发版后影响主干的稳定性。</p>
<p><strong>由于文章篇幅有限，只能点到即止地介绍当前一些工作成果和思考，各个 Topic 还有一些新的方向在探索，如果你对 iOS 底层原理、架构设计、构建系统、自动化测试有深入了解，快来加入我们吧！</strong></p>
<h1 data-id="heading-21">加入我们</h1>
<p>我们是负责抖音客户端基础能力研发和新技术探索的团队。我们在工程/业务架构，研发工具，编译系统等方向深耕，支撑业务快速迭代的同时，保证超大规模团队的研发效能和工程质量。在性能/稳定性等方面不断探索，努力为全球数亿用户提供最极致的基础体验。</p>
<p>如果你对技术充满热情，欢迎加入抖音基础技术团队，让我们共建亿级全球化 App。目前我们在深圳、上海、北京、杭州、均有招聘需求，内推可以联系邮箱：<strong><a href="mailto:tech@bytedance.com">tech@bytedance.com</a></strong>，邮件标题： <strong>姓名-工作年限-抖音-基础技术-iOS/Android</strong>。或直接点击<a href="https://jobs.bytedance.com/experienced/position?keywords=iOS%20%E6%9E%B6%E6%9E%84&category=&location=&project=&type=&job_hot_flag=&current=1&limit=10" target="_blank" rel="nofollow noopener noreferrer">链接</a>查看部门所需岗位！</p>
<hr>
<p>欢迎关注「字节跳动技术团队」</p>
<p>投递简历请联系邮箱：<a href="mailto:tech@bytedance.com">tech@bytedance.com</a></p></div>  
</div>
            