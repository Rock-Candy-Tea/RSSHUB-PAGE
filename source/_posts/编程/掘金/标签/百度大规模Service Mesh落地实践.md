
---
title: '百度大规模Service Mesh落地实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed956c6ac2d4f21be5989c7d7c14437~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 22:28:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed956c6ac2d4f21be5989c7d7c14437~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed956c6ac2d4f21be5989c7d7c14437~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>导读</strong>：百度过去基于rpc框架的服务治理存在各种框架能力层次不齐、业务自身服务治理效率低、全局可观测性不足等诸多问题。本文介绍了百度内部落地service mesh的实践过程，以基础稳定性能力治理和流量调度治理能力为业务落地点，详细阐述了内部落地的service mesh整体技术方案以及一系列关键技术，如性能的极致优化、扩展的高级策略、周边服务治理系统等。</p>
<p><em>全文6835字，预计阅读时间13分钟。</em></p>
<h1 data-id="heading-0"><strong>一、背景</strong></h1>
<p>========</p>
<p>百度大部分产品线已完成微服务的改造， 数万个微服务对架构服务治理能力提出了更高的要求。传统的服务治理一般通过rpc框架去解决，多年以来百度内部也衍生出多种语言的rpc框架，比如c++、go、php等等框架，基础服务治理能力和rpc框架耦合，rpc框架能力参差不齐，给公司整体服务治理能力和效率提升带来较多的痛点及挑战：</p>
<p><strong>1.高级架构能力无法多语言、多框架复用</strong></p>
<p>如某产品线近2年发生数次雪崩case，底层依赖的php、golang等框架需要重复建设来定制动态熔断、动态超时等高级能力，而这些能力在其他rpc框架已支持；</p>
<p>如常用架构降级、止损能力各个产品线重复建设，接口方案差异大，从运维层面，运维同学期望基础的架构止损能力在不同产品线之间能够通用化，接口标准化，降低运维成本；</p>
<p><strong>2.架构容错能力治理周期长，基础能力覆盖度低</strong></p>
<p>随着混沌工程全面落地，对架构能力有了更高要求。多数模块对单点异常，慢节点等异常缺乏基础容忍能力，推动每个模块独立修复，成本高，上线周期长。</p>
<p>如某产品线治理改造花了2个季度完成；推荐某类召回服务经常出现超时、重试配置等不合理的问题，集中管理调整成本比较高。</p>
<p><strong>3.可观测性不足，是否有通用机制提升产品线可观测性？</strong></p>
<p>比如某推荐业务缺少整体模块调用关系链和流量视图，线上故障靠人肉经验定位、新机房搭建周期长，效率低。</p>
<h1 data-id="heading-1"><strong>二、service mesh解决什么问题？</strong></h1>
<p>=========================</p>
<p>为彻底解决当前业务服务治理的痛点和问题，我们引入了service mesh，基本思路解耦治理能力和框架，治理能力下沉到sidecar。内部联合多个部门通过合作共建方式建设通用的service mesh架构， 提供通用的基础稳定性能力和统一的流量控制接口。</p>
<p>我们期望service mesh在厂内业务落地解决什么问题？总结为两点：</p>
<p><strong>1、基础稳定性能力的关键组件</strong> – 为微服务提供通用的基础故障容错能力、基础故障检测能力、统一的干预和控制接口；</p>
<p><strong>2、流量治理的核心系统</strong> – 实现各产品线整体的连接托管、全局流量的可观测、精细调度能力；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/510f519faead4749a74955b7a2b45daf~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>附service mesh定义：Linkerd CEO William Morgan于2016年9月29日公开提出，service mesh是用于处理服务间通信的基础设施层，用于在云原生应用复杂的服务拓扑中实现可靠的请求传递。在实践中，service mesh通常是一组与应用一起部署，但对应用透明的轻量级网络代理。</em></p>
<h1 data-id="heading-2"><strong>三、技术挑战</strong></h1>
<p>==========</p>
<p><strong>我们在落地service mesh实际过程中，面临以下几大挑战</strong>：</p>
<p><strong>· 低侵入</strong>：百度大大小小有上百个产品线，模块数量级达到万级别，实例数达到百万级别，如何让业务在不改代码前提下无缝迁移，低侵入接入是我们在设计方案考虑第一要素；</p>
<p><strong>· 高性能</strong>：百度核心产品线在线服务对延迟要求极高，比如推荐、搜索等核心产品线，延迟上涨几毫秒会直接影响用户的体验和公司收入，从业务角度不能接受接入mesh后带来的性能退化。因此我们在落地过程中，投入很大精力来优化mesh的延迟，降低接入mesh后的性能损耗；</p>
<p><strong>· 异构系统融合</strong>：首先我们需要解决厂内多语言框架互通问题，其次需要统一接口和协议，打通厂内多个服务治理系统，如服务发现、流量调度、故障止损等系统；</p>
<p><strong>· mesh可靠性</strong>：在线业务对可靠性要求极高，要求我们在落地过程中，充分考虑自身稳定性，避免出重大case。</p>
<p><strong>总结：<strong>我们的需求是实现一套</strong>低侵入、高性能、完备的治理能力</strong>，能够解决业务实际问题service mesh架构。</p>
<h1 data-id="heading-3"><strong>四、整体架构</strong></h1>
<p>==========</p>
<p><strong>· 技术选型</strong>：我们底层以开源istio+envoy组件为基础，基于厂内实际业务场景，适配厂内组件。选择基于开源定制的主要原因是兼容社区，跟开源保持标准协议，吸收社区的高级feature同时能够反哺到社区。</p>
<p><strong>我们内部落地的mesh整体架构如下 ，包括以下核心组件：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c77c55d93855400d8311fb6a2ef83117~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>· Mesh控制中心：</strong></p>
<p><strong>· 接入中心</strong>：sidecar的注入，管理sidecar版本，统一上线入口；</p>
<p><strong>· 配置中心</strong>：稳定性治理和流量治理入口，托管连接、路由配置、通信等策略；</p>
<p><strong>· 运维中心</strong>：mesh的日常运维，如干预去劫持操作；</p>
<p><strong>· 控制面板</strong>：istio-pilot组件，负责路由管理、通信策略等功能；</p>
<p><strong>· 数据面板</strong>：envoy组件，负责流量转发、负载均衡等功能；</p>
<p><strong>· 依赖组件</strong>：融合厂内服务发现组件naming service、内部各种rpc框架适配、监控系统、底层paas支持；</p>
<p><strong>· 周边治理生态</strong>：基于mesh统一治理接口衍生出的服务治理生态，如智能调参系统、 故障自动定位&止损系统、故障治愈、混沌工程（基于mesh的精细化故障注入）。</p>
<p>接下来我们从<strong>接入方式、性能优化、稳定性治理、流量治理、周边系统协同、稳定性保障等</strong>关键技术来解析：</p>
<h2 data-id="heading-4"><strong>4.1 接入方式</strong></h2>
<p>============</p>
<p>社区采用的iptables流量劫持方案， iptables规则过多会导致性能问题，尤其在厂内数万个实例转发下受限iptables线性匹配规则，转发延迟非常大，不能满足在线低延迟的场景。</p>
<p><strong>我们的解决思路</strong>：基于本地lookbackip地址方案，envoy打通内部服务发现组件，劫持服务发现请求，通过回传lookback地址透明劫持业务流量。同时本地naming agent定期探活envoy，一旦envoy出现异常，自动回退到直连模式，避免envoy故障导致流量丢失。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4667bab513453ca4d7e4237a805fdd~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时针对一些不走流量劫持的业务，我们设计了proxyless方案，即通过rpc框架适配istio标准的xds，接入pilot服务治理的通路，托管服务治理策略和参数分发生效。无论业务流量是否被劫持，都通过mesh标准化的干预入口实现服务治理的统一管控和治理。目前proxyless方案已在内部c++等rpc框架完成适配，在搜索、推荐等业务线落地。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cda67ad3a7b4a6a85de70be3cef708d~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>总结</strong>：我们通过基于服务发现流量劫持和proxyless两种透明迁移的的接入方案，实现业务模块无需修改代码即可接入mesh的低侵入方式，降低业务接入mesh的成本。</p>
<h2 data-id="heading-5"><strong>4.2 性能极致优化</strong></h2>
<p>==============</p>
<p>我们在落地过程发现社区版本envoy延迟、资源消耗较大，在一些大扇出复杂场景下，流量劫持带来的延迟上涨接近5ms，cpu消耗占比20%以上，无法满足厂内在线业务高吞吐、低延迟场景。我们分析evnoy底层模型，<strong>本质原因是envoy 是一个单进程多线程的libevent线程模型，一个event-loop只能使用一个核，一个回调卡住就会卡住整个线程，容易产生高延时，导致吞吐长尾控制能力比较差。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/753db01f997c49018cf361ed46ed8d40~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们基于envoy扩展接口扩展envoy的网络模型&线程模型，引入brpc底层高性能的bthread协程模型 。在我们内部简称高性能brpc-envoy版本。同时我们打通pilot，实现原始libevent和brpc-thread在线切换，用户可以非常方便自助选择开启高性能模型。<em>备注：brpc 百度内部c++ 高性能rpc开源框架，内部数几十个产品线再使用，实例数有数百万规模，已开源。</em></p>
<p>测试下来结果，相比开源社区版本和MOSN（蚂蚁自研已开源）等业界框架， CPU降低60%+，平均延迟降低70%+，长尾延迟平均降低75%+，性能大幅领先业界，彻底解决社区版envoy无法满足大规模工业高性能场景的问题，为大规模落地mesh扫清障碍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b43b2b4c63946b4aa51c69f15e334c9~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时我们正在调研ebpf、dpdk等新技术，进一步降低延迟和资源消耗。目前测试下来ebpf相比本地lookbackip转发性能有20%的提升，dpdk相比内核协议栈有30%的性能优化空间（在绑核条件下）。</p>
<h2 data-id="heading-6"><strong>4.3 稳定性治理</strong></h2>
<p>================</p>
<p>内部在线&离线服务大规模混部，线上混部环境复杂，对模块的架构稳定性能力要求比较高。我们基于mesh提供通用的<strong>故障容错能力、故障检测能力、统一的干预和降级能力</strong>来整体提升产品线稳定性能力的baseline：</p>
<h3 data-id="heading-7"><strong>4.3.1 局部故障容错能力：</strong></h3>
<p>为了提升架构对日常机器故障的容错能力，我们基于envoy扩展了高级稳定性容错策略，比如增加动态重试熔断策略，通过滑动窗口计算分位值耗时，动态控制重试比例，通过重试捞回请求同时也避免大量重试引发雪崩的风险。另外我们引入反馈式的高级负载均衡策略，根据下游返回定制的错误码，降权&屏蔽故障实例，通过熔断保护机制控制权值，避免正常实例被打挂。在我们内部核心产品线上线后，大幅提升模块在局部故障下的容错能力，架构韧性能力大大提升。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df988950a6784763ae67b397fefdd5bc~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（参考下图，某在线核心模块接入mesh后，可用性从之前2个9提升到4个9）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3361a97925b245d2a8d38c0763525ffc~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>针对雪崩治理场景（我们统计厂内核心产品线雪崩历史case，90%以上case都是雪崩治理能力缺失，比如重试风暴、超时倒挂、降级能力缺失导致），我们基于mesh定制熔断能力的高级重试能力来抑制重试风暴，提供动态超时机制来预防超时倒挂。在核心产品线的大范围铺开后，覆盖近2年内雪崩90%+故障场景， 2020年雪崩case对比2019年雪崩类case损失环比下降了44%</p>
<h3 data-id="heading-8"><strong>4.3.2</strong> 局部故障检测能力：</h3>
<p>过去故障检测依赖机器粒度的基础指标，粒度比较粗，针对容器故障实例缺乏精细指标检测，无法及时探测到故障实例，通常需要数小时才会检测到故障实例。我们打通了上层故障自愈系统，基于envoy扩展故障检测策略，提供通用、快速直接的故障发现检测能力，外部故障自愈系统通过prometheus接口采集故障实例，经过汇聚分析，触发paas迁移故障实例。对于已接入mesh的业务线，几乎零成本代价下即可具备局部异常的快速发现&定位能力，故障实例的检测时效性从原来数小时优化到分钟级。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31ef04fa661e48d7a1fc7e3778aafd31~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9"><strong>4.3.3 统一的干预和降级能力：</strong></h3>
<p>对于一些大规模故障，单靠架构自身容错解决不了，需要依赖稳定性预案去止损，比如典型的下游弱依赖摘除预案。过去依赖不同产品线和模块自身去建设降级能力，不同模块接口方案差异大，随着系统不断迭代，降级能力可能出现退化，运维成本和挑战比较大。我们结合mesh实现通用降级和干预能力，如支持多协议场景下流量丢弃能力，实现统一的流量降级策略；通过统一的超时和重试干预能力，实现秒级的干预时效性。</p>
<p>通过落地mesh为多产品线提供统一的干预和控制接口，为稳定性预案提供一致的操作接口，大大提升了服务治理效率，产品线服务治理迭代周期从过去季度级缩短到月级。</p>
<p>如20年某业务线接入mesh两周完成4个方向20+模块架构治理改造，而原来往往需要一个季度周期才能完成改造。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f1e517b63804c69aaf342fb4085e5e4~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>===</p>
<h2 data-id="heading-10"><strong>4.4 流量治理能力</strong></h2>
<p>==============</p>
<p><strong>· 流量可观测性：</strong></p>
<p>过去构建产品线模块上下游调用链和基础黄金指标一直缺乏通用的解决方案，大多数都是基于rpc框架或者业务框架定制，模块调用链和黄金指标覆盖率低。比如某重要产品线端到端涉及到2000多个模块，调用链关系十分复杂，具体流量的来源不够透明，严重影响运维效率。如机房搭建不知道上下游的连接关系，靠人肉梳理误差大，某产品线一次搭建周期将近2个月时间。另外故障定位、容量管理等由于全局的可观测性不足，往往只能依赖经验定位，效率十分低下。</p>
<p><strong>我们整体思路以mesh为中心，结合周边rpc框架，构建全局servicegraph调用链。</strong></p>
<p><strong>· 一方面</strong>通过istio内部crd抽象表达出模块链路关系和链路属性，在istio上层自建mesh配置中心，屏蔽底层crd细节。以配置中心作为连接托管的唯一入口，托管模块全链路的调用关系，新机房建设基于servicegraph快速构建出新机房的拓扑，很大程度提升机房搭建效率，缩短周期。</p>
<p><strong>· 另一方面</strong>同时结合brpc和mesh，制定标准的黄金指标格式，建设统一的黄金指标数据仓库，支持上游的服务治理建设，比如容量管理分析、故障定位、性能分析、故障注入等。比如我们正在落地的故障自感知、止损系统基于servicegraph可自动化、快速、准确实现线上故障的感知、止损。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27baf436213f4196a7024bf4dc70f93a~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>· 流量精细调度：</strong></p>
<p>厂内大部分产品线基于入口整体切流，一直缺乏对模块链路内部流量精细调度控制能力。我们结合mesh的流量调度能力，打通厂内服务发现组件，整合一系列切流平台，统一流量调度入口到mesh控制中心。结合前面servicegraph提供的全局调用链，实现模块精细连接关系的流量调度能力；另外我们基于mesh实现模块实例粒度精细流量调度和流量复制能力，典型应用于模块的精细流量评估、线下压测、导流场景下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41058ac81aae4e6196003d30fd9053f1~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>===</p>
<h2 data-id="heading-11"><strong>4.5 周边生态协同</strong></h2>
<p>==============</p>
<p>===</p>
<p>基于mesh提供统一的控制接口，衍生出周边服务治理系统，典型场景如治理参数自动调参、故障自动止损、故障自愈等系统。</p>
<p><strong>· 自动调参系统</strong></p>
<p>服务治理参数依赖用户手工配置参数(超时比例、权重比例等)，完全依赖人肉经验，频繁出现配置不合理影响治理能力效果，同时线上环境差异比较大，静态配置无法适应线上复杂环境变化。我们设计出一套动态调参系统，核心思路基于mesh的治理统一接口和结合线上指标实时反馈，实时调整治理参数。比如根据下游CPU利用率，动态调参访问下游重试分位值比例；根据下游机器负载差异化，动态调参访问下游权重。</p>
<p>在厂内核心产品线落地后，通过自动调参完全代替人肉调参，实现服务治理参数自适应调整。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d945334622b46c1869893520ac5047d~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>· 故障自动感知止损系统</strong></p>
<p>传统线上故障凭人工经验定位，产品线深度定制预案能力，强依赖有经验的工程师，新人上手成本高；并且预案止损操作散落在文档中，可维护性差，随着业务迭代可能失效或者逐步退化，不可持续。</p>
<p>我们基于mesh通用的干预能力和统一控制接口，研发一套故障预案自动止损系统，结合前面提到的service graph提供全局调用链和黄金指标，实现常见故障的自动感知、预案自动止损，降低故障止损的mttr时间。同时打通混沌工程，定期端到端注入故障触发预案演练，避免预案能力退化。这套系统目前典型应用在强弱依赖降级、精细化流量调度等预案场景，预计到年底，接入mesh的产品线大部分线上故障都能自动化处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e792655ee10f4a1390db1bc1121fb02a~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>· 统一协议，协同周边系统</strong></p>
<p>基于mesh配置中心提供标准的流量控制和服务治理接口（如流量降级接口），协同周边系统生态，如自动调参、故障感知止损、故障自愈、流量调度。</p>
<p>基于开源xds协议，统一数据面协议，对接周边rpc框架，实现不同rpc框架能够统一控制。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fd1035226cb4f6a954df5f4a65cf01b~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12"><strong>4.6 自身稳定性保障</strong></h2>
<p>厂内业务比如搜索、推荐等关键业务对稳定性要求极高，在线迁移mesh好比”高速公路上换车轮“，必须保证对业务无损。因此稳定性建设是我们在落地mesh过程重点关注点之一。</p>
<p><strong>首先我们通过多级兜底机制保障流量转发的可靠性</strong>。针对局部故障，如个别envoy实例配置、进程等异常，envoy自身具备fallback机制，异常可以自动回退直连模式，无需人工介入。但一些大规模故障，比如envoy出现大范围故障，靠envoy自身机制已经无法保证（可能出现劫持、非劫持模式来回波动），我们通过外部干预平台一键下发转发黑名单，强制干预envoy切到直连模式，全产品线止损时效性控制在5分钟以内；极端情况下，如envoy大范围hang死，可能导致对外干预接口失效，我们准备了兜底预案，联动paas批量强制杀掉envoy进程，回退到直连模式。</p>
<p><strong>其次在服务治理配置发布方面，我们核心思路控制故障隔离域</strong>，比如打通mesh配置中心，灰度控制配置发布的百分比；同时构建mesh接入一站式平台，梯度逐步发布，控制envoy升级对业务的影响面。我们引入monitor模块定期做端到端巡检，如配置一致性、envoy节点服务异常、版本一致性等校验。</p>
<p><strong>最后我们定期通过混沌工程主动注入故障</strong>，比如模拟envoy异常、pilot异常、配置中心异常等，进行极限异常case演练，避免自身稳定性架构能力退化。</p>
<h1 data-id="heading-13"><strong>五、总结</strong></h1>
<p>========</p>
<p>从19年年底开始立项，不到2年的时候，在内部数十个产品线已完成落地，其中一些核心产品线主干模块已覆盖到80%以上，天级托管流量超过千亿。新接入模块几乎零成本接入，即可具备基础稳定性治理和流量调度能力。我们结合周边生态系统，构建一站式mesh接入平台，为各业务线提供低侵入、低成本、标准化的服务治理解决方案，系统性解决各个产品线的基础可用性问题，大幅降低治理迭代成本&周期，促进体系整体稳定性能力的提升。</p>
<p><strong>招聘信息</strong></p>
<p>如果你对微服务感兴趣，请你联系我，我们当面聊聊未来的N种可能性。无论你是后端，前端 ，大数据还是算法，这里有若干职位在等你，欢迎投递简历，关注同名公众号百度Geek说，输入内推即可，我们期待你的加入！</p>
<p><strong>推荐阅读</strong></p>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494238&idx=1&sn=efaf3b393a8d14d3f1e6e7bbd2bce3cd&chksm=c03eda22f7495334c4038e6c932dbfbe617ff4dd21c14ff79c222cc575df710211d49d043810&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer"><strong>｜</strong>百度同学教你怎样成为复盘高手</a></p>
<p><strong>｜</strong><a href="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494205&idx=1&sn=8af04b9aab29a6a1759de837be2b6251&chksm=c03eda41f7495357cb5d9a9c75e27caf93283b192456de55acb1e008c81774d53e5a14f01a82&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">联邦计算在百度观星盘的实践</a></p>
<p><strong>｜</strong><a href="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247493554&idx=1&sn=9eaa6cb738547c38980c23798fd66e29&chksm=c03ed7cef7495ed8422338b880235d04c0ca2ccfd4abb96ca0bd9c9ef47a535729865f1f0cdb&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">百度爱番番与Servicemesh不得不说的故事</a></p>
<p><strong>｜</strong><a href="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247493116&idx=1&sn=90925b509f4d8bfedc7066f2317e3d9c&chksm=c03ed580f7495c9621068194b799dd7fcc9ebff535a6fa04aacf593eae549c8d500b06df57d1&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">一种基于实时分位数计算的系统及方法</a></p>
<p>---------- END ----------</p>
<p>百度Geek说</p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            