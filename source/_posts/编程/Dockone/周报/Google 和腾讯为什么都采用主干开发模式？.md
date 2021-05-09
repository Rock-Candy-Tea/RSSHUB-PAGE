
---
title: 'Google 和腾讯为什么都采用主干开发模式？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/9ab8f4a385b01ff1e6319f4ff40499dd.jpg'
author: Dockone
comments: false
date: 2021-05-09 04:03:16
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/9ab8f4a385b01ff1e6319f4ff40499dd.jpg'
---

<div>   
<br>【编者的话】本文介绍了两种常用的代码分支模式，描述了国内大多数 IT 团队采用特性分支开发的现状，也剖析了 Google 和腾讯与众不同地采用了主干开发模式的原因、优势及其相关因素。通过对巨头采用主干开发模式的实践进行分析，供国内 IT 同仁在研发模式选型中参考。<br>
<h3>背景</h3>按之前的写作思路，本文应该叫《Google 工程效能三板斧之三：主干开发》，但我改变了主意，希望能同时提供国内互联网公司的实践，供读者参考，因此文章标题也随之更改。<br>
<br>软件开发过程中，开发人员通过版本管理工具对源码进行存储，追踪目录和文件的修改历史。为了区隔不同状态的源代码，会采用分支进行管理。不同的软件开发模式，对应着不同的分支模式。<br>
<br>软件业界常用的软件分支模式有多种，但本质上可以分为两类：<br>
<ul><li>主干开发模式</li><li>特性分支模式</li></ul><br>
<br>特性分支开发是指为一个或多个特定的需求/缺陷/任务创建代码分支，在其上完成相应的开发（一般经过增量测试）后，把它合并到主干/集成分支的开发模式。<br>
<br>特性分支开发模式中常用的有 Git-Flow 模式、Github-Flow 模式和 Gitlab-Flow 模式等。这些模式只有细节上的差异，以 Git-Flow为例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/9ab8f4a385b01ff1e6319f4ff40499dd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/9ab8f4a385b01ff1e6319f4ff40499dd.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
特性分支开发由于大量采用代码分支，因此流程比较复杂的，随之而来的是更多的烦乱的合并操作，普通开发人员没有一年半载都不容易熟练掌握。  <br>
<br>而主干开发，则相对简单和高效得多，下来我们重点介绍。<br>
<h3>什么是主干开发？</h3><h4>主干开发的特点</h4>主干开发有以下特点：<br>
<ul><li>有且只有1个开发分支，即主干分支；</li><li>所有改动都发生在主干分支；</li><li>发布一般从主干拉出发布分支；</li><li>缺陷在主干上修复，并根据需要 cherry pick 到对应版本的发布分支。</li></ul><br>
<br><h4>主干开发的流程</h4>主干开发的流程如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210507/d4ad530acfa5473f116bc35958c5c2a9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210507/d4ad530acfa5473f116bc35958c5c2a9.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>主干开发的优点</h4><ul><li>有利于持续集成和持续交付</li><li>分支少，实践简单</li><li>小步快跑，合并冲突少</li><li>代码总是最新，避免需要维护多个版本</li></ul><br>
<br><h4>主干开发所需配套</h4>主干开发虽好，但需要以下配套：<br>
<ul><li>基础架构上，需要高效和有效的持续集成和自动化测试平台，能在代码推送到主干时及时完成主干的验证；</li><li>研发文化上，需要研发团队有编写完备单元测试的习惯，确保在代码提交或合入到主干时，CI（持续集成）工具能通过运行自动化测试迅速反馈；</li><li>研发流程上，一般需要配套代码评审（CR）机制，在代码提交或合入到主干时，触发代码评审（CR）机制，通过 Peer Review 后才能生效；</li><li>发布策略上，有时候还需要配套特性开关（Feature Toggle），因为主干开发要求每次变更提交都非常小，才能降低冲突机会，因此功能特性会拆分得很小，有时候甚至可以理解为“特性半成品”，为了隔离“特性半成品”对主干和生产上的影响，需要通过特性开关先隐藏相关特性，只有当特性都完成后才通过灰度发布等手段逐步打开。</li></ul><br>
<br><h3>为什么 Google 和腾讯采用主干开发模式</h3>收益：<br>
<ul><li>更快的迭代 —— 主干开发模式配合持续集成的实践，使最新特性随时都处于可发布状态，显著提升迭代速度；</li><li>更低的代码合入成本 —— 越频繁的合入，冲突发生概率越低，冲突解决的成本就越低；而主干开发只有本地工作副本（也可以理解为一种分支），生命周期更短，因此合入成本最低；</li><li>团队代码依赖一致性高 —— 因为团队总是依赖最新代码，所以不会出现多个版本分支的情况引起依赖旧版本代码的问题；</li><li>代码和系统的质量更高 —— 主干开发模式通过持续集成触发的自动化测试、代码评审等机制保证的代码质量不但不会降低，反而更高。</li></ul><br>
<br>成本：<br>
<ul><li>需要持续集成和自动化测试工具链支持 —— Google 基于 Bazel 的持续集成平台和 TAP 自动化测试平台，腾讯的蓝盾持续集成平台和多个自动化测试平台都已经相对成熟；</li><li>需要持续部署和反馈工具支持 —— 灰度发布/金丝雀发布等工具已经是标配，允许新特性在可控的范围内实验，并通过数据埋点等机制及时进行反馈；</li><li>需要充分的自动化测试 —— Google 的自动化测试覆盖率已经相当高（普通在70%-90%之间）；腾讯在 930 变革后，自动化测试覆盖率也受到空前重视，试点团队已接近 Google 的水平；这样的自动化测试，可以保障主干代码不会轻易被 break；</li><li>需要严格的CR机制确保代码质量 —— Google 极其严苛的可读性认证（Readability）在业界已经是标杆，腾讯是国内少有正在采用类似实践的互联网企业。严格的代码可读性认证和根据此标准执行的严格代码评审制度，能有效的保证合入主干的代码质量不会降低。</li></ul><br>
<br>综上所述，收益包括了：质量和效率。而这2者是软件和互联网企业的核心诉求。成本方面，虽然短期投入不小，但长期是可控和收敛的。<br>
<br>因此，从ROI（Ratio of Investment）的角度来看，Google 和腾讯采用主干开发实属必然。<br>
<h3>Google 在主干开发的实践</h3>我们在之前的文章提到，Google 的工程效能（也叫研发效能）核心理念只有简单的3条：<br>
<ol><li>使用单体代码仓库（参考：<a href="https://mp.weixin.qq.com/s?__biz=MzU3Njc1MDMxNA==&mid=2247483674&idx=1&sn=37df1548873b5e2888c514ed9f8108f7&scene=21#wechat_redirect">Google 工程效能三板斧之一：单体代码仓库</a>）</li><li>使用 Bazel 构建（参考：<a href="https://mp.weixin.qq.com/s?__biz=MzU3Njc1MDMxNA==&mid=2247483681&idx=1&sn=f414497ba40f70a07615be107627a9c8&scene=21#wechat_redirect">Google 工程效能三板斧之二：使用 Bazel 构建</a>）</li><li>主干开发。</li></ol><br>
<br>其中的第3条，就是本文所述内容。<br>
<br>为了保证主干代码的质量，避免出现工程师合入到主干的代码 break 掉主干的情况，Google 采取了以下实践：<br>
<ul><li>代码合入事件触发通过持续集成，确保合入到主干的代码经过充分且必要测试；</li><li>通过 Bazel 实现相关代码（指依赖变更代码的代码）的精准测试；</li><li>至少 2 个合资格的 reviewer （代码评审人）的 LGTM（Look Good To Me），才允许代码合入主干；</li><li>合资格的 reviewer 都是在 Google 内部通过 Readability （代码可读性）认证的员工。</li></ul><br>
<br><h3>腾讯在主干开发的实践</h3>腾讯某个 BG 在 2018 年开始的“930 变革”后，在各试点团队推动主干开发，具体的举措包括：<br>
<ol><li>以度量牵引：通过对特性分支）的生命期监控和预警，实现非主干分支的生命期缩短，倒逼开发团队采用主干开发；</li><li>投大力气统一 BG 内的持续集成工具、开发自动化测试平台；</li><li>制定了 7 大编程语言的编码规范，并自研代码静态扫描工具；</li><li>并参考 Google 推行代码可读性（Readability）、可测试性（Testability）认证制度；</li><li>强力推行 CR （代码评审）制度，确保代码的可读性（命名、代码风格、设计、复杂度）。</li></ol><br>
<br>效果：<br>
<ul><li>质量提升：代码质量从可测量的维度得到明显提升（代码规范率、单元测试覆盖率）；</li><li>迭代速度提升：试点团队的迭代周期从 4 周或 2 周提升至 1 周；</li><li>代码从“私有”变“公有”：通过代码评审制度，提高了代码可读性，使代码从个人拥有（只有写代码的人能看懂），变成团队拥有（整个团队都能看懂）；这一点对于企业非常重要，接手过别人代码的程序们都有感受；</li><li>代码的自动化测试覆盖率提升明显，为未来的重构构筑了一张安全网；</li></ul><br>
<br><h3>中小企业能参考什么？</h3>主干开发的优点很诱人，但小厂的同学们可能会郁闷了，没有 Googe 和腾讯那样财大气粗的资源，不可能专门整几十上百号程序员来开发维护这些工具（没错，这些大厂的研发效能部门，有数百开发人员负责工具开发），怎么实践主干开发呢？<br>
<br>其实也不必郁闷，因为一方面，主干开发更多在于研发文化，而工具配套虽然是必需品，但开源工具或商业工具对于中小开发团队已经够用。<br>
<br>对照前文提到的“主干开发所需配套”的：<br>
<ul><li>代码规范、可读性、CR（代码评审）、单元测试、频繁提交（合入主干）这些都是研发文化，团队小甚至推行成本更低；</li><li>持续集成工具：业界已有成熟的开源或商业工具 Jenkins、Gitlab CI、Travis CI等众多工具；</li><li>代码扫描工具：SonarQube、DeepSource、Codacy等；</li><li>单元测试工具：基本上现代编程语言都已经内置或有对应工具；</li><li>特性开关：如果要求不高，可以通过代码 hard code 一个常量作为特性开关；如果要求高，也有相当稳定的开源特性开关（比如：unleash、piranha、flipper）。</li></ul><br>
<br>因此，中小企业或开发团队，也完全可以进行主干开发的实践，并获得对应的好处。<br>
<h3>后记</h3>上一篇文章《[Google 和 Facebooke 为什么不用 Git 管理源码？](<a href="https://mp.weixin.qq.com/s?__biz=MzU3Njc1MDMxNA==&mid=2247483696&idx=1&sn=0a79d3f3f73edd8490b70741bb4b7b4d&scene=21#wechat_redirect" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s%3F_ ... irect</a> "Google 和 Facebooke 为什么不用 Git 管理源码？")》提到过，Git 的其中一大优势是代码分支创建成本低，合入速度快（但冲突处理本质上仍然非常麻烦）。但当你看完本文，就应该明白，Git 的这个优点对于 Google、Facebook 是没有多大意义的，因为主干开发本身不需要创建太多分支。<br>
<br>另外，本文提到 Google 和腾讯都极度重视代码可读性（Readability），这个词对于国内读者可能是陌生而且奇怪的，毕竟都是程序员，难道还有不可读（读不懂）的代码吗？由于篇幅问题，我们下一篇文章再跟大家细说。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/9MJ8werJsD6sIYKcU5az0w" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/9MJ8werJsD6sIYKcU5az0w</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            