
---
title: 'Kubernetes 稳定性保障手册 -- 可观测性专题'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/b6bdd7d8105bc2e968d9c999c0a7de2a.png'
author: Dockone
comments: false
date: 2021-04-03 12:09:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/b6bdd7d8105bc2e968d9c999c0a7de2a.png'
---

<div>   
<br>作者 | 悟鹏<br>
来源 | <a href="https://mp.weixin.qq.com/s/G2UoyOFHOQbvq39hkrVFDg">阿里巴巴云原生公众号</a><br>
<br>《Kubernetes 稳定性保障手册》系列文章：<br>
<ul><li><a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247501775&idx=1&sn=8b3b27934e7bced10b2a7f81483e3256&chksm=fae6cc00cd9145168b57c579ed488a7f92b67f86daf039de6b9518995d9e1ad27df2a382290e&scene=21#wechat_redirect">Kubernetes 稳定性保障手册 -- 极简版</a></li><li>Kubernetes 稳定性保障手册 -- 日志专题</li><li>Kubernetes 稳定性保障手册 -- 可观测性专题（本文）</li></ul><br>
<br>伴随大家对稳定性重视程度的不断提升、社区可观测性项目的火热，可观测性成为了一个很热门的话题，站在不同的角度会产生不同的理解。<br>
<br>我们从软件开发的生命周期出发，尝试形成对可观测性的一个宏观理解，并从 SRE 和 Serverless 两个角度具化可观测性的理解以及实践。<br>
<br><h2>目的</h2><ul><li>增强认知，通过全局把握来提升竞争力</li><li>通过合理的设计和实践，为未来带来可能性</li></ul><br>
<br><h2>目标</h2><ul><li>针对可观测性的理解达成一致</li><li>针对可观测性的发展方向达成一致</li></ul><br>
<br><h2>什么是可观测性？</h2>从 <a href="https://en.wikipedia.org/wiki/Observability">wikipedia: Observability</a> 可理解到 <strong>可观测性</strong> 的定义：<br>
<br><blockquote><br>In control theory, observability is a measure of how well internal states of a system can be inferred from knowledge of its external outputs.</blockquote>Consider a physical system modeled in state-space representation. A system is said to be observable if, for any possible evolution of state and control vectors, the current state can be estimated using only the information from outputs (physically, this generally corresponds to information obtained by sensors). In other words, one can determine the behavior of the entire system from the system's outputs. On the other hand, if the system is not observable, there are state trajectories that are not distinguishable by only measuring the outputs.<br>
<br>简单表述为，可观测性是一种方法，通过系统的外部输出推导出系统内部的状态。<br>
<br>下图简化了系统的组成和系统间的交互：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/b6bdd7d8105bc2e968d9c999c0a7de2a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/b6bdd7d8105bc2e968d9c999c0a7de2a.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>从上述交互图可了解到，系统的交互行为有如下几种形态：<br>
<ul><li><br>系统内部<br>
<ul><li>组件功能闭环，不与其他组件或系统交互</li><li>组件之间交互</li></ul></li><li><br>系统之间<br>
<ul><li>系统和系统之间进行交互</li></ul></li></ul><br>
<br>这样，通过如下两种形态的信息，就可以通过系统的外部输出了解到系统的内部状态：<br>
<ul><li>组件闭环的信息</li><li>组件间或系统间流动的信息</li></ul><br>
<br><h2>可观测性的问题域是什么？</h2>可观测性的核心在于 <strong>通过观测数据、满足不同人群、对于系统状态的理解需求</strong>，这里先抽象观测数据的生命周期，有如下图示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/60947196cbcfc0aea58f9f55b058031f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/60947196cbcfc0aea58f9f55b058031f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>观测数据通过 App 生成，经过中间处理环节后进行存储，然后提供查询服务。<br>
<br>观测数据服务于不同类型的人群，如产品的用户、业务、研发、SRE，不同的人群通过不同的形态来使用这些数据，包括 SLA / SLO / SLI / Alert 等。<br>
<br>根据可观测数据的生命周期，可粗略总结可观测性的问题域：<br>
<ul><li><br>生成端<br>
<ul><li>观测数据的数据模型</li><li>观测数据的生成</li><li>观测数据的导出</li></ul></li><li><br>处理端<br>
<ul><li>观测数据的采集</li><li>观测数据的处理</li><li>观测数据的导出</li></ul></li><li><br>存储端<br>
<ul><li>观测数据的存储</li><li>观测数据的查询</li><li>观测数据的使用</li></ul></li><li><br>使用端<br>
<ul><li>观测数据的消费</li></ul></li></ul><br>
<br><h2>软件开发生命周期中，可观测性的服务目标是什么？</h2>从项目整体视角来看软件开发的生命周期，有如下的流程：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/80c5541a60fb1c71d0b95b2a4cdbe1e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/80c5541a60fb1c71d0b95b2a4cdbe1e7.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>细化下来：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/cad142b4a90ee70ffd5ddc78d379805c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/cad142b4a90ee70ffd5ddc78d379805c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>在软件开发生命周期中，有 4 类角色。面对 4 类角色，可观测性的服务目标会有差异：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/3c90dd6828ee0ad9826d40f6ce9151c1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/3c90dd6828ee0ad9826d40f6ce9151c1.jpg" class="img-polaroid" title="4-1.jpg" alt="4-1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Note:<br>
<ul><li><strong>可靠</strong> 与 <strong>稳定</strong> 不是等同的关系，<strong>可靠</strong> 包含了 <strong>稳定+及时满足功能需求</strong> 特征</li></ul><br>
<br><h2>SRE 可以投入的方向</h2>基础服务：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/5f128d18e8e5f1cdd613dfd2ddb815f0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/5f128d18e8e5f1cdd613dfd2ddb815f0.jpg" class="img-polaroid" title="4-2.jpg" alt="4-2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>可以将 <a href="https://opentelemetry.io/">OpenTelemetry</a> 作为基础落地上述事项，参见：<a href="https://mp.weixin.qq.com/s/n4eVf2KZRIp2yKACk88qJA">《OpenTelemetry 简析》</a>。<br>
<br>与此同时，可以探索可视化的稳定性保障服务，从全局视角加快问题发现、定位、解决，一张图把握集群中「组件自身」和「组件之间交互」的健康状态 ，形如下图：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/2df7516644eb86b1037d1d411c7e1cbf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/2df7516644eb86b1037d1d411c7e1cbf.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>以此为入口，从整体把握集群状态，关联异常信息，处理问题时有的放矢。<br>
<br><h2>Serverless 场景下可观测性</h2>Serverless 是目前很有前景的云上计算形态，阿里云提供了比较完整的 Serverless 计算产品，如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/68a0df732cee4e4153d03800a638e163.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/68a0df732cee4e4153d03800a638e163.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>不同 Serverless 计算环境的一个主要差异点在于运行环境的持续时间，以此为出发点，可以抽象出 Serverless 计算环境中可观测性的核心，然后分解出相应的解决方案：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/764e489e5ea0f460b22b1e8e9c6f4462.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/764e489e5ea0f460b22b1e8e9c6f4462.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>根据运行环境持续时长的不同，可粗略划分为 3 类：<br>
<ul><li>天级别</li><li>小时级别</li><li>分钟或秒级别</li></ul><br>
<br>这些运行环境均可以通过虚拟机、容器或 WebAssembly 等技术实现，区别点在于业务层面限定的运行环境持续时长。<br>
<br>根据运行环境持续时长的特征，平台和用户的关注核心会有相应的变化：<br>
<ul><li><br>天级别的运行环境，平台方的核心在于提供可靠的运行环境，由用户自由管理应用<br>
<ul><li>对于可观测性，平台方核心在于运行环境可靠性，用户核心在于应用环境稳定性和请求响应性能</li></ul></li><li><br>小时级别的运行环境，平台方的核心在于围绕应用提供管理服务，用户聚焦于业务自身<br>
<ul><li>对于可观测性，平台方核心在于应用运行稳定性和请求响应性能，用户核心在于业务特征</li></ul></li><li><br>分钟或秒级别的运行环境，平台方的核心在于细粒度的用户业务逻辑管理，用户更聚焦在业务的敏感特征<br>
<ul><li>对于可观测性，平台方核心在于请求响应可靠性和业务特征，用户核心在于核心业务特征</li></ul></li></ul><br>
<br>对于 FaaS 场景，<a href="https://www.thundra.io/">THUNDRA 公司</a> 的 <a href="https://demo.thundra.io/functions">demo</a> 提供了比较好的示例以供参考 (截取 3 个示例)：<br>
<ul><li>函数</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/883f50ab9efd53cdfd9ec6efe9b78619.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/883f50ab9efd53cdfd9ec6efe9b78619.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>应用</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/31eae6bfb6f8520cae5b3ee7094e329f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/31eae6bfb6f8520cae5b3ee7094e329f.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>架构</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/9ab7d0be5f23deb0b1f5b39a2d97eb1a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/9ab7d0be5f23deb0b1f5b39a2d97eb1a.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>小结</h2>通过对可观测性概念、问题域、不同层级需求等形成深入理解，可以形成对可观测性的理解大图，然后在此基础上与业务结合，增强业务在可观测性方面的竞争力，同时迭代理解，技术与业务相互促进。<br>
<br><h2>References</h2><ul><li><a href="https://en.wikipedia.org/wiki/Observability">wikipedia: Observability</a></li><li><a href="https://en.wikipedia.org/wiki/Service-level_objective">wikipedia: Service-level objective</a></li><li><a href="https://en.wikipedia.org/wiki/Service-level_agreement">wikipedia: Service-level agreement</a></li><li><a href="https://en.wikipedia.org/wiki/Service_level">wikipedia: Service level</a></li><li><a href="https://research.google/pubs/pub36575/">Google-Wide Profiling: A Continuous Profiling Infrastructure for Data Centers</a></li><li><a href="https://github.com/conprof/conprof">conprof - Continuous Profiling</a></li><li><a href="https://github.com/open-telemetry/oteps/issues/139">OpenTelemetry Proposal issues: Adding profiling as a support event type</a></li><li><a href="https://github.com/kubernetes/community/blob/master/sig-scalability/slos/slos.md">Kubernetes scalability and performance SLIs/SLOs</a></li><li><a href="https://developer.aliyun.com/article/754236">从 DevOps 到 NoOps，Serverless 技术的落地方式探讨</a></li></ul><br>
<br><strong>欢迎大家留言交流使用 Kubernetes 过程中的稳定性保障问题，以及对稳定性保障的期待工具或服务。大家也可通过邮箱联系作者，进一步深入交流：<a href="mailto:flyer.zyf@alibaba-inc.com">flyer.zyf@alibaba-inc.com</a></strong>。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            