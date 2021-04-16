
---
title: 'Nacos 2.0 性能提升十倍，贡献者 80% 以上来自阿里之外'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/0a3ca5293e05f63adf8216109a8d6435.png'
author: Dockone
comments: false
date: 2021-04-16 12:10:17
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/0a3ca5293e05f63adf8216109a8d6435.png'
---

<div>   
<br>来源 | <a href="https://mp.weixin.qq.com/s/CEsJUZA0KepD1YqNWL9m-w">阿里巴巴云原生公众号</a><br>
<br>3 月 20 日，Nacos 2.0 正式发布。Nacos 是阿里巴巴在 2018 年开源的一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台，也可以理解为微服务的注册中心 + 配置中心。<br>
<br>Nacos 目前在获取用户和开源社区运维上都取得了不错的成绩。据 Nacos 联合创始人李艳林介绍，在一次 2245 人样本的开发者调研中显示，用户在注册中心的选择上，选择 Nacos 的开发者已经达到了 49%。Nacos 在同领域中已经是国内开发者的首选。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210415/0a3ca5293e05f63adf8216109a8d6435.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/0a3ca5293e05f63adf8216109a8d6435.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>此外 Nacos 开源社区的贡献者有 80% 以上来自阿里之外，贡献了 Nacos 的 20% 左右的代码，尤其 Nacos 多语言部分，全部由外部开发者贡献，并且保持着不错的迭代速度。<br>
<br>而此次大升级，相较 1.x 版本，Nacos 2.0 性能提升了 10 倍，内核进行了分层抽象，并且实现插件扩展机制。未来 Nacos 计划通过集成主流 Sidecar 技术完成对 Nacos 多语言生态和云原生生态的整合。<br>
<br>为进一步了解 Nacos 是如何完成 2.0 架构大升级，实现 10 倍性能提升的，以及 Nacos 社区运营经验和未来规划。OSCHINA 邀请 Nacos 联合创始人为我们做了深入解读。<br>
<br><h1>Nacos 之于微服务 = Etcd 之于 K8s</h1><strong>Q：首先介绍下自己吧，如个人背景、与 Nacos 项目是如何结缘的等等</strong>?<br>
<br><strong>A</strong>：大家好，我是李艳林，花名彦林，阿里云软负载团队负责人，Nacos 联合创始人。阿里云产品 MSE 创始人。<br>
<br>随着开源对云计算行业影响越来越大，2018 年阿里加大了对开源的投入，我有幸参与 Nacos 开源工作，围绕着 Dubbo/Spring-cloud-alibaba 阿里微服务生态，提供开发者完整的微服务解决方案。<br>
<br><strong>Q：介绍下 Nacos 诞生、发展的历史吧</strong>？<br>
<br><strong>A</strong>：Nacos 在阿里巴巴起源于 2008 年五彩石项目（完成微服务拆分和业务中台建设），成长于十年双十一的洪峰考验，沉淀了简单易用、稳定可靠、性能卓越的核心竞争力。随着云计算兴起，2018 年我们深刻感受到开源软件行业的影响，因此决定将 Nacos（阿里内部 Configserver/Diamond/Vipserver 内核） 开源，输出阿里十年的沉淀，推动微服务行业发展。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210415/753432409ec65689ad8deb7d20264871.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/753432409ec65689ad8deb7d20264871.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>2018 年我们将 Nacos 正式开源，并快速成为国内最受关注开源产品，虎牙也最早跟进参与了 Nacos 的开发，并且大规模生产落地，后续视频行业快速跟随采用。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210415/cbee05cf26cf20b53620d44633d30315.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/cbee05cf26cf20b53620d44633d30315.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（2018 年 Nacos 开源，meetup @ 深圳）<br>
<br>2019 年我们发布 Nacos 1.0版本，标志着 Nacos 功能稳定成熟，并且支持了几乎所有的微服务框架和编程语言，由此 Nacos 被广泛使用，Nacos 也进入了高速发展期。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210415/6380e2f25286d413a72b55dfaa3f56b5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/6380e2f25286d413a72b55dfaa3f56b5.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（2019 年 Nacos 1.0 发布，Nacos Meetup @ 杭州）<br>
<br>2020 年新年伊始 Nacos Star 数破万，并且我们陆续发 1.X 多个版本，完成了存储和一致性模型的抽象分层，架构跟清晰和稳健，Nacos 也进入大规模使用期。<br>
<br>2021 年我们发布 Nacos2.0 版本，性能提升十倍，Nacos 进入第二发展曲线，以性能、高可用、生态为核心竞争力，继续保持高速发展。<br>
<br><strong>Q：您认为 Nacos 在云原生中间件江湖中的地位如何</strong>？<br>
<br><strong>A</strong>：Nacos 首先在同领域中已经是国内开发者的首选，Nacos 2.0 发布后有开发者自发发起调研，看大家注册中心的选项，从调研结果来看，选择 Nacos 的开发者已经达到了 49%。随着 2.0 发布，Nacos 的竞争优势正在不断扩大。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210415/eb277ca099ed01a9bee1fb934ec46f00.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/eb277ca099ed01a9bee1fb934ec46f00.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Nacos 代表的注册中心和配置中心在云原生中间件中就是最核心的服务，因为分布式后首先要解决的就是寻址问题。<br>
<br>我也可以做一个类比，Nacos 相对于微服务的地位，就跟 Etcd 相对 K8s 地位是一样的。<br>
<br><h1>2.0 架构升级</h1><strong>Q：Nacos 2.0 服务发现、配置管理性能提升 10 倍具体是怎么做到的，具体是哪些场景，测试方式是什么？背后对应的是哪些技术架构的升级</strong>？<br>
<br><strong>A</strong>：18 年开源的时候考虑到简单易用，我们基于内部产品内核做了一些取舍，如通信协议改成了 http 模式，这样简单，多语言容易实现，但是短链接确实性能弱了一些。<br>
<br>服务模型上我们有持久化和非持久化两种模式，开源的时候我们考虑持久化模式可以做更多的服务治理能力，但是发展一段时间够发现外面主流场景都是非持久化服务，但是也为性能问题埋了一些坑，主要模型不太匹配，当然我们现在做了很好的抽象和统一才能比较好的解决这个问题。对于 Dubbo 和 Spring-cloud-alibaba 这种最常规的非持久化服务性能提升最明显。<br>
<br>测试方式主要是针对服务和配置的关键的使用场景构建了几个典型的压测模型进行压测。<br>
<br>核心升级了通信协议、一致性模型、架构分层和抽象。<br>
<br><strong>Q：这次升级到 2.0 过程中有没有遇到一些技术难题，是怎么解决的</strong>？<br>
<br><strong>A</strong>：<br>
<ul><li>长连接协议选型：我们内部有一个私有长链接协议，市场上有 gRPC/Rsocket 两个主流选择，我们为了兼容必须做好扩展抽象，为了多语言容易实现和集成我们也做了很多压测验证。最终选择了 gRPC。从模型上看 Rsocket 的推模型对于 Nacos 更合适，在生态和多语言支持上 gRPC 更合适，综合平衡我们选择了 gRPC，并且做好扩展，以便后续有更好的选择。</li><li>服务一致性模型：Nacos 底层服务分为持久化服务和非持久化服务，在一致性模式和存储方式上有比较大差别，经过漫长时间打磨，我们把模型做好了抽象和融合，把每个场景性能都发挥到极致。</li><li>无缝升级方案：一般开源产品协议的跨代升级基本都是不考虑兼容的，但是由于 Nacos 有广泛用户基础，因此我们还是消耗了巨大的精力做好兼容工作，以便让所有用户能够升级享受到这些红利。</li></ul><br>
<br><strong>Q：听说阿里内部已经有了百万实例的案例，具体是指什么，可以详细介绍下吗</strong>？<br>
<strong>A</strong>：2020 年面对云原生大的趋势和阿里内部实例规模突破百万的大背景下，我们发起了中间件 4.0 项目，核心解决扩展性和标准化问题。实例指的是微服务实例节点，微服务实例节点。对于 Nacos 模型来说，关键性能指标一个是实例规模（业务发布启动写频繁），一个是单实例注册的服务规模（需要维持心跳消耗内存和网络），后续我们可以找一个单独机会，我详细给大家分享一下阿里百万实例软负载的实践。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210415/44bbb47064fc2f2cac01316951b88c56.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210415/44bbb47064fc2f2cac01316951b88c56.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（2020 年内部 KO，中间件 4.0 开启云原生中间件时代）<br>
<br><strong>Q：Nacos 在阿里内外部的落地情况如何？可以对比介绍下吗</strong>？<br>
<br><strong>A</strong>：目前 Nacos 已经完成了自研、开源、商业化三位一体的建设，阿里内部的钉钉、考拉、饿了么、优酷等业务域已经全部采用云产品 MSE 中的 Nacos 服务，并且与阿里和云原生的技术栈无缝整合。<br>
<br><h1>发展规划及商业化</h1><strong>Q：Nacos 2.X 规划中，很多关于插件的方面的优化，这样设计的原因和目标是什么</strong>？<br>
<br><strong>A</strong>：随着 Nacos 代码库日益庞大，之前耦合比较紧密的代码不方便扩展，用户定制性有比较高，又提交不到社区，如安全功能，因此通过扩展机制提升用户根据自己场景定制能力，当然也能更好的跟各个生态集成。<br>
<br><strong>Q：官宣 2.0 版本时提到，Nacos 以后会向 Mesh 化方向深入探索。这里的 Mesh 是指 Service Mesh 吗，有什么技术难点，具体要做哪些事情</strong>？<br>
<br><strong>A</strong>：是的，由于 Service Mesh 通过 Sidecar 模式能比较好的解决多语言问题，因此我们期望通过集成主流 Sidecar 技术完成对 Nacos 多语言生态和云原生生态的整合。<br>
<br>目前核心是 Istio 目前的性能指标挑战还很大，Sidecar 目前自动灰度升级是一个挑战，对于中小公司目前落地风险可控。 <br>
<br><strong>Q：Nacos 作为一款产品来看，其发展目标是偏向为阿里业务做好支撑，还是希望能发展更多外部用户？如果是后者，有没有大致的商业计划</strong>？<br>
<br><strong>A</strong>：从 2020 年开始，阿里云就提出了“三位一体”理念，即将“自研技术”、“开源项目”、“商业产品”形成统一的技术体系，最大化技术的价值。通过开源扩大生态，通过阿里集团场景锻造高性能和高可用能力，通过云产品构建产品化能力。<br>
<br>2020 年 1 月，我们就发布了 Nacos 有对应的商业化产品-微服务引擎（Micro Service Engine）简称 MSE，并对外提供商业化服务。它是一个面向业界主流开源微服务生态的一站式微服务平台， 提供注册中心、配置中心全托管（兼容 Nacos/ZooKeeper/Eureka），网关（兼容 Zuul/Kong/Spring Cloud Gateway），和无侵入的开源增强服务治理能。<br>
<br>2020 年双 11 ，我们就全面使用 EDAS、Dubbo、RocketMQ、AHAS、ARMS、MSE、PTS 等阿里云云产品来支撑双 11，做到了和客户在同一架“飞机”上。可以说阿里巴巴集团是阿里云的最大的公有云用户，目前已经有大量业务已经跑在阿里云 MSE 托管的 Nacos 上面了。预计 2021 年双十一阿里集团将 100% 跑到我们公有云产品上面。目前阿里云上已有数万企业采用了我们商业化产品 MSE 中托管的 Nacos，而且我们会加大对此投入，以便更好的服务阿里云用户。<br>
<br>最后，我们希望广大的开发者可以通过 Nacos 的开源，享受到阿里微服务体系的技术红利；另外通过阿里云的规模效应，企业用户可以通过 Nacos 商业化产品 MSE，获得比开源自建更稳定、成本更经济的产品红利。<br>
<br><h1>Nacos 开源社区</h1><strong>Q：Nacos 2.0 发布之后开发者的热烈反响，为什么，怎么做开发者维护的</strong>？<br>
<br><strong>A</strong>：首先 Nacos 经过近三年发展已经成为国内首选，有着广泛的群众基础；其次 Nacos2.0 是一个跨代产品，性能提升十倍，诚意十足的贡献了阿里核心能力，最后感谢媒体朋友，在这开放的时代让好的产品、技术大规模推广。<br>
<br>我们在开发者关系上简单分为贡献者和使用者。对于几百名贡献者，我们是通过定期周会机制交流一些前沿技术的想法和贡献的思路，根据贡献程度授予不同的社区名誉，帮助我们贡献者扩大技术影响力。<br>
<br>对于使用者，我们通过定期的 Meetup 和要求用户分享最佳实践的方式进行互通。从而形成正向循环。另外我们非常重视降低新手使用者使用 Nacos 的门槛，所以我们在文档建设、教程建设上都投入了很多精力。今年，我们将在知行动手实验室上线完整的 Nacos 入门教程，帮助开发者们更好地上手。<br>
<br><strong>Q：Nacos 开源社区现况如何？是否调查过贡献者构成</strong>？<br>
<br><strong>A</strong>：目前应该也是二八定律，80% 以上是外面的贡献者，贡献了 Nacos 的 20% 左右的代码，其中 chuntaojun、KeRan213539、paderlol、horizonzy 等小伙伴一直保持贡献。这个对于中国开源是有非常重要的意义，尤其 Nacos 多语言部分，全部是外部开发者贡献，而且保持着不错的迭代速度。<br>
<br>在社区数字化运营上，我们联合 X-lab，通过数据化、自动化的方式，清晰地展示出 Nacos 和对标的项目的活跃度、关注度趋势，和社区协作网络图，能快速定位社区里的活跃开发者。<br>
<br>借此机会感谢我们 200 多名为 Nacos 贡献代码的小伙伴！也期望更多的小伙伴能够参与到 Nacos 开源工作中来，一起把 Nacos 做强。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            