
---
title: 'Service Mesh 在中国工商银行的探索与实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/73e9bdc8f127def438f7d813a4216824.png'
author: Dockone
comments: false
date: 2021-12-31 03:09:26
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/73e9bdc8f127def438f7d813a4216824.png'
---

<div>   
<br>微服务架构是当今互联网和金融机构渐趋主流的系统架构模式，其核心是集成服务通信、服务治理功能的服务框架，微服务框架在持续演进同时，服务网格（Service Mesh）作为一种新型的微服务架构，因架构灵活、普适性强，被认为具有较好发展前景。中国工商银行（后简称工行）主动探索服务网格领域，从 2019 年开始服务网格技术预研工作，通过对服务网格技术深入研究和实践后，于 2021 年建设了服务网格平台。服务网格与现有微服务架构融合发展，助力工行应用架构向分布式、服务化转型，承载未来开放平台核心银行系统。<br>
<h3>业界服务网格发展现状</h3>自 2016 年服务网格技术诞生以来，业界涌现了诸多的开源产品，如 Istio（Google + IBM + Lyft）、Linkerd（Twitter）、Consul（Hashicorp）等。其中以 Istio 社区活跃度和认可度最高，被作为服务网格的标杆开源产品。<br>
<br>服务网格是一个专门处理服务通讯的基础设施层。它通过在业务 Pod 中注入 Sidecar 容器，接管业务容器的通信流量，同时 Sidecar 容器与网格平台的控制平面对接，基于控制平面下发的策略，对代理流量实施治理和管控，将原有服务框架的治理能力下层到 Sidecar 容器中，从而实现了基础框架能力的下沉，与业务系统解耦。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/73e9bdc8f127def438f7d813a4216824.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/73e9bdc8f127def438f7d813a4216824.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 1：服务网格示意图</em><br>
<br>Sidecar 容器接管后端服务通信的进出流量后，通过标准协议进行服务间通信，可实现跨语言、跨协议的服务互访。此外，Sidecar 容器可对代理的流量进行管控，如统一的服务路由、安全加密、监控采集等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/8b59848dca044927e6836284aa91be28.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/8b59848dca044927e6836284aa91be28.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 2：服务网格请求流转过程示意图</em><br>
<h3>服务网格技术在工行的探索与实践</h3>工行从 2015 年开启了 IT 架构转型工程，截止目前分布式体系已覆盖 240 余个关键应用，生产已有约超 48 万个提供方分布式服务节点，日均服务调用量超 127 亿，逐步实现了超越主机性能容量的集群处理能力。工行分布式服务平台在稳定支撑已有业务系统的平稳运行同时，也存在一些业界共性的挑战，诸如：<br>
<ul><li>跨语言技术栈的互联互通需研发多套基础框架，技术研发和维护成本高。</li><li>多产品线下，各应用使用了不同版本的基础框架，推动各应用升级框架周期较长，生产并行运行多版本的基础框架，兼容压力较大。</li></ul><br>
<br>为解决当前痛点，工行积极引入服务网格技术，探索解耦业务系统与基础设施，完善服务治理能力。<br>
<h4>与微服务框架融合发展，构建企业级服务网格平台</h4>服务网格（Service Mesh）平台在建设过程中，集成了原有分布式体系的注册中心、服务监控等基础设施，将原服务框架客户端中最基础的通讯协议编解码能力以轻量级客户端的形式保留在业务系统中，其余服务框架客户端的能力均下沉至 Sidecar 中，可与服务框架兼容发展，平滑过渡。目前工行已完成服务网格（Service Mesh）平台的建设，在与分布式服务平台融合发展过程中，打通了异构语言系统的服务治理与监控体系，解耦了业务与中间件系统，丰富了流量治理能力，并已在智能投顾、文字识别等应用完成业务试点。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/15ddbbb2f208771ac9b01f2096a13426.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/15ddbbb2f208771ac9b01f2096a13426.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 3：服务网格边车（Sidecar）与微服务 SDK 对比图</em><br>
<br>服务网格控制平面包含了配置中心、注册中心、安全中心、管控中心、监控中心、日志中心等模块。数据平面 Sidecar 与原服务框架使用相同的通讯协议（Dubbo/Spring Cloud），支持服务网格系统与原服务框架系统互联互通，平滑迁移。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/1110ac22c4946b18498203a84d81b60c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/1110ac22c4946b18498203a84d81b60c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 4：工行服务网格架构图</em><br>
<h4>探索企业级方案，支持规模化部署和平滑迁移</h4>工行服务网格在大数据、高频联机等服务场景下，对流量代理部署模式、平滑迁移、性能优化等方面开展了落地实践。<br>
<br><strong>大数据场景下的无侵入流量代理部署模式</strong><br>
<br>工行应用开发语言主要使用 Java，但在大数据领域 Python 语言也被广泛使用。针对异构语言场景，服务网格平台提供了无侵入透明劫持的流量代理方案，简化了异构语言应用接入难度。无侵入流量代理的核心是通过修改网络 Iptables 规则，强制拦截进出业务容器的流量，并将这部分流量重定向至 Sidecar 容器。其具体实现为：在启动业务 Pod 时，通过 Init Container（初始化容器）修改业务 Pod 的网络 Iptables 规则，该规则让进出业务容器的流量都强制重定向至 Sidecar 容器，实现 Sidecar 容器对业务容器的流量接管。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/e474396f36ffaece4c999be6bdcf0903.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/e474396f36ffaece4c999be6bdcf0903.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 5：透明劫持流量代理示意图</em><br>
<br>但是 Iptables 对性能和可维护性都存在较大的挑战，故在联机高频服务场景，我们提供了轻量级客户端与 Sidecar 协作的流量代理方案。<br>
<br><strong>高频联机场景下的低侵入流量代理部署模式</strong><br>
<br>在联机高频服务场景，我们通过对业务应用引入轻量级的客户端，该客户端在对业务透明的前提下，改变业务应用的服务注册发现行为，将原往注册中心发起的服务注册与订阅的行为转变为往本地 127.0.0.1 的 Sidecar 地址发起服务注册与订阅，并由 Sidecar 代理向注册中心发起服务注册与订阅。业务容器通过 Sidecar 代理订阅后，本地获取的服务目的地址则为 127.0.0.1 的 Sidecar 地址，后续所有请求将会直接发往 Sidecar，再由 Sidecar 转发至真实的服务目的地址，实现流量代理能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/747f64e2ee72ad8d8f996f443c4887bc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/747f64e2ee72ad8d8f996f443c4887bc.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 6：端口流量代理示意图</em><br>
<br><strong>传统部署向网格化部署的平滑迁移</strong><br>
<br>目前工行微服务主要有基于 Dubbo 和 Spring Cloud 两种服务实例组成，且已在生产环境大规模运行，在引入服务网格系统时需具备与原微服务系统的平滑过渡能力。工行通过服务网格系统同时支持 Dubbo 与 Spring Cloud 协议，服务网格实例可与原服务框架实例通过相同协议互相访问。使在同一注册中心下，服务网格系统与原分布式服务系统可融合发展，平滑过渡。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/544064cd68fd5a7e1da12ffdd157bbcb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/544064cd68fd5a7e1da12ffdd157bbcb.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 7：平滑迁移示意图</em><br>
<br><strong>规模化部署后的性能挑战与优化</strong><br>
<br>目前工行最大的注册中心集群上有超 48 万提供者的超大规模业务场景，而在开源 Isito 架构中，服务发现的目的地址、配置信息等会通过 Pilot 的 Xds API 进行全量下发。在大量服务实例的情况下，全量下发会影响 Pilot 和 Sidecar 的性能和稳定性。服务网格平台通过引入第三方注册中心与配置中心。由 Sidecar 直接对接注册中心与配置中心，支持按需订阅，配置精准下发，大幅降低 Pilot 和 Sidecar 压力。通过压测，控制平面具备支持百万级实例的性能容量能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/c91653e1c4b0e15859cddf52f4e6e7ba.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/c91653e1c4b0e15859cddf52f4e6e7ba.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 8：工行控制面组件演进图</em><br>
<h4>构建企业级服务治理能力，支持精准流量管控</h4>目前开源 Istio 的流量治理能力极其有限，只有基础的路由与可观察性，无法满足企业级的需求。SOFAMesh 基于 Istio 架构设计，自研数据面，并调优部分控制面组件，可满足企业落地需求，工行与 SOFAMesh 团队合作，建设了金融级的服务网格平台，并对流量管控能力进行了企业级增强。工行服务网格已具备完善的监控运维能力，能监控到各节点运行时状态，支持对各节点进行实时流量调拨，对于故障节点具备实时流量摘除能力，能对各节点进行统一安全管控。<br>
<br><strong>监控运维能力</strong><br>
<br>服务网格平台内置了完善的监控与报警能力，支持向第三方监控系统上报服务监控、链路监控等监控指标；并具备根据单位时间内的业务请求异常率阈值的报警，且能在触发限流、熔断、降级、故障自愈等服务治理功能时，同步触发对应的报警事件。<br>
<br><strong>流量治理能力</strong><br>
<br>服务网格平台已具备细粒度的流量精准匹配能力，从流量身份标识角度识别特定标识的流量合集，并对这部分流量进行精准管控。平台现已支持（标签级/方法级/服务级/应用级）限流、熔断、降级、路由、流量镜像、链路加密、鉴权、故障演练、故障隔离等企业级的流量管控能力。<br>
<br><strong>故障自愈能力</strong><br>
<br>传统故障反馈依赖监控报警后通过应急预案临时处置故障节点，业务和运维定制应急预案的能力，强依赖有经验的运维工程师，新人上手成本高；且预案操作散落在文档中，可维护性差，随着业务迭代可能会逐步退化，增加操作复杂度。服务网格平台提供了一套统一的基础故障自愈系统，以时间窗口内的业务请求失败率为黄金指标，辅助窗口期间最少调用次数、失败率倍数等，实现常见故障自动感知，自动从客户端或服务端侧网络隔离故障节点，并在故障节点恢复后能网络自恢复，达到业务自愈的能力，提升了分布式系的运维高可用能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/99e780823eb661ee3f56d5226ddafb9c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/99e780823eb661ee3f56d5226ddafb9c.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 9：故障隔离工作图</em><br>
<br><strong>安全管理能力</strong><br>
<br>服务网格平台已支持安全认证能力，支持国密及多种主流算法构建加密通道，实现更加安全的数据传输，以零信任网络的安全态度，实现全链路可信、加密；并能识别调用方身份标识，根据身份标识设置访问控制策略（黑/白名单）。在有多接入方的业务场景中，可预防个别客户系统故障或者恶意攻击，对异常客户实施黑名单管控，拒绝非法访问，保护本系统的可用性。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/f42126dec9dc5eb23e8c98d8dbe95263.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/f42126dec9dc5eb23e8c98d8dbe95263.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 10：安全管控工作示意图</em><br>
<h3>未来展望</h3>服务网格作为云原生领域下一代微服务技术，经过 5 年多地演进，仅在个别头部企业大规模生产实践，以银行为代表的金融同业中尚无成功案例。工行服务网格已完成多语言、异构技术、边缘场景的业务试点，基本论证服务网格在流量管控、系统扩展性的优势，具有下沉服务治理能力到基础设施层，高度解耦中间件与业务系统的可行性。后续，工行将在全面总结前期试点经验的基础上，扩大试点应用范围，充分论证服务网格技术在差异化的技术架构、银行多样化业务场景的适应性，同步打磨完善平台能力，全面提升性能容量和稳定性，为金融同业落地服务网格技术提供最佳实践与示范。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/1fSxNvdPRwEpUFlEPFxpgQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/1fSxNvdPRwEpUFlEPFxpgQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            