
---
title: '开源 1 年半 star 破 1.2 万的 Dapr 是如何在阿里落地的？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/f75a73c26db1d917e649ff5439fd2b27.png'
author: Dockone
comments: false
date: 2021-04-25 08:08:09
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/f75a73c26db1d917e649ff5439fd2b27.png'
---

<div>   
<br>作者 | 敖小剑<br>
来源 | <a href="https://mp.weixin.qq.com/s/Dsb7rwu5tRAizJ7Wdr23Fw">阿里巴巴云原生公众号</a><br>
<br>Dapr 是 2019 年 10 月微软开源的可移植、事件驱动分布式运行时，它使开发人员能够轻松地构建运行在云平台和边缘的弹性而微服务化的无状态和有状态的应用程序，从而降低基于微服务架构构建现代云原生应用的准入门槛。<br>
<br>在今年 2 月份刚刚发布了 v1.0 正式版本。虽然推出至今不过一年半时间，但 Dapr 发展势头十分迅猛，目前已经在 GitHub 上收获了 1.2w 星。阿里是 Dapr 开源项目的深度参与者和早期采用者，率先进行了生产落地，集团内部有十几个应用在使用 Dapr；目前已有 2 位 Dapr成员，是 Dapr 项目中除微软之外代码贡献最多的公司。<br>
<br><strong>拉到文末可以了解 Dapr 入门教程体验方式</strong><br>
<br><h1>为什么阿里会选择Dapr？</h1>在阿里巴巴，Java 使用非常广泛，不仅仅业务应用大量使用 Java，大量中间件和基础能力的服务器端也是使用 Java 开发。在过去十几年间，我们围绕 Java 建立了非常完备的生态体系，经历过各种严酷的考验。<br>
<br>而随着业务形态的日渐丰富，<strong>多语言</strong>的需求在不断的增加，如 nodejs / golang / c / c++ / rust 等。特别是在微服务流行之后，根据实际情况而选择使用不同的编程语言开发微服务成为趋势。但效仿 Java ，为每一种编程语言都打造一套功能完备的生态体系在成本上是不现实的。因此，需要一个成本可控的方案来解决多语言问题，让微服务开发能真正的实现“语言自由”。<br>
<br>随着云的采用，业务应用的形态也开始朝云原生方向发展，越来越多的业务应用（尤其是前台业务）开始拥抱 FaaS 和 Serverless  作为应用托管和资源调度的解决方案。而在 FaaS 和 Serverless 场景下，需要更轻量化的解决方案以满足快速启动和伸缩的需求 —— 传统类库模式下由于需要集成大量的 SDK，业务应用变得非常的臃肿。而在 Function 形态下更加的不协调，以 nodejs 为例：几百行的 nodejs Function 代码依然需要依赖多达几十兆的 node module。同时 FaaS 和 Serverless 也对多语言的支持提供了更高的要求。因此，在 FaaS 和 Serverless 这种新型形态下有必要提供有别于传统类库方式的、更轻量化的、支持多语言的解决方案。<br>
<br>显然，Servicemesh 倡导的 Sidecar 模式是解决上述问题的绝佳方案。在过去几年间，随着 Servicemesh 的发展和采用， Sidecar 模式已经得到充分验证：Sidecar 模式非常符合云原生的理念，特别是在多语言支持和应用轻量化方面具备天然优势。<br>
<br>我们非常认可 Bilgin Ibryam 在<a href="https://www.infoq.com/articles/multi-runtime-microservice-architecture/">"Multi-Runtime Microservices Architecture"</a> 一文中提出的 Multiple Runtime / Mecha Runtime 的理念，尤其是他对分布式应用需求的分析，很符合我们的实际情况：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/f75a73c26db1d917e649ff5439fd2b27.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/f75a73c26db1d917e649ff5439fd2b27.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>而 Dapr 是第一个实践 Multiple Runtime 理念的开源项目，我们从这个项目发布开始就密切关注它，因为 Dapr 可以很好的解决我们面临的问题：Sidecar 模式天然提供了对多语言的支持，各种客户端 SDK 被 Dapr Runtime 替代之后应用也得以轻量化。<br>
<br>此外，从长期战略的角度考虑，我们在 2020 年提出了"三位一体"的理念，即将“自研技术”、“开源项目”、“商业产品”形成统一的技术体系，最大化技术的价值。而当前的实际情况是三者有完全不同的产品和技术方案，导致当我们需要将某个产品在阿里内部、公有云、客户私有云等不同的平台上进行迁移时，或者是跨多个平台部署时，就会遇到非常大的挑战。Dapr 面向能力编程的理念，强调可移植性和可扩展性的标准 API，平台中立、无供应商锁定的设计，深深的吸引了我们。<br>
<br><blockquote><br>“在阿里云，我们相信 Dapr 将引领微服务的发展。通过采用 Dapr，我们的客户现在可以以更快的速度来构建可移植和健壮的分布式系统。”</blockquote>—— 阿里云资深技术专家 李响<br>
<br>在 2020 年年中，我们开始基于 Dapr 项目进行了内部小规模的试点，在实际的落地过程中探索和验证 Dapr 的理念。我们也积极参与到 Dapr 开源项目的建设中，提交了大量的改进建议和代码。<br>
<br>下面我们将以 Dapr 在阿里的实际落地场景来具体说明 Dapr 是如何帮助我们解决上述问题的。<br>
<br><h1>Dapr 在阿里的实践</h1><h2>1. 概况</h2><strong>目前 Dapr 在阿里巴巴内部还处于实验阶段</strong>。<br>
<br>我们的首要工作是为内部的中间件开发 Dapr 组件，使业务应用程序可以与这些中间件和实现它们的 Java 语言/ Java Client SDK 解耦。然后通过小规模的业务应用落地，在各种场景下的对 Dapr 进行验证，在验证完成之后计划继续部署较大规模的业务应用。<br>
<br>截止到 2021 年 3 月，Dapr 在阿里内部落地的场景主要集中在 2 个方面：多语言支持和云间迁移。<br>
<br><h2>2. 多语言支持</h2><h3><strong>1）Faas / Serverless 场景</strong></h3>> 背景：在阿里的电商系统中，存在大量活动和导购需求。<br>
<br>这些需求的特点是"短平快"：需要快速开发、快速迭代、生命周期相对比较短。因此这类需求非常适合通过采用 FaaS 的方式来落地。<br>
<br>Faas 对多语言支持有强烈的诉求，肯定不会局限于 Java。而阿里内部大部分应用都是 Java 体系，对多语言的支持比较弱，尤其是新兴语言（如 Dart）或者小众语言（如 Rust）。<br>
<br>而从需求上说，采用 FaaS 的应用也同样需要和内部运行的服务以及各种中间件/基础设施进行通讯，因此 FaaS 平台迫切的需要解决多语言支持问题。<br>
<br>通过 Dapr ，我们很好的解决了 FaaS 的多语言问题，从而使得客户通过 FaaS 实现了开发效率的大幅提升。<br>
<br><h3><strong>2）多语言应用的接入</strong></h3>> 背景：阿里收购有大量的公司。<br>
<br>这些收购的公司有大量的应用，而这些应用中很多不是 Java 体系，在接入阿里的技术体系时，对多语言支持有明确的需求。<br>
<br>另外，由于业务创新的需要，有些应用对 nodejs 和 golang 有强烈诉求，还有一些应用则需要使用到 Dart 和 C++。<br>
<br>但目前这些语言的生态系统并没有像 Java 那么完善，尤其部分中间件和基础设施已经发展的非常成熟，进入维护状态，不太可能在现在重新开发所有语言的客户端：成本上代价很高，时间上也来不及。<br>
<br>通过 Dapr ，我们可以为这些应用提供多语言解决方案。<br>
<br><h3><strong>3）复杂的 Java 遗留系统</strong></h3>> 背景：基于 Java ClassLoader 机制而设计的复杂系统。<br>
<br>为了解决类冲突问题，隔绝不同的业务模块，阿里针对  Java 系统设计了基于 ClassLoader 机制的复杂系统，这些系统的设计往往非常复杂，应用也非常臃肿。<br>
<br>此外，部分业务团队为了能和现有的中间件进行互通，自行维护了一套多语言的中间件 SDK，而这些 SDK 本来应该由中间件团队维护并保持同步更新。这也带来了稳定性方面的隐患和风险。<br>
<br>我们期望将这些遗留的系统迁移到 Dapr 中，统一实现中间件 SDK 的维护和更新。比较特殊的是这里存在一个需求：最好能让业务开发团队尽量不做代码层面的调整，以减少迁移时对业务应用的冲击。<br>
<br>所以针对 Java 遗留系统，在迁往 Dapr 时，我们额外设计了一个 Java 适配层：将原来的 Java 调用适配到 Dapr 的客户端 API 上。<br>
<br>以上三种多语言的落地实践场景，如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/f585b597589390320b495768bf3ec8c0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/f585b597589390320b495768bf3ec8c0.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>3. 云间迁移</h2>> 背景：业务应用对外输出时有跨平台需求。<br>
<br>阿里的部分业务，如钉钉文档，原本是提供给阿里内部和外部用户直接使用的，此时钉钉文档只需要部署在阿里内部的业务集群里，直接访问阿里内部的生态体系。<br>
<br>但是随着 SaaS 业务的发展，以及部分信息安全敏感的用户对于数据安全的强烈诉求， 需要将钉钉文档部署到用户 VPC 下或者公有云下。<br>
<br>为此，我们需要将钉钉文档的系统从阿里内部迁移到公有云上进行部署，而钉钉文档使用的底层技术需要从阿里内部的技术体系迁移到使用开源技术或阿里云的商业化产品上。<br>
<br>借助 Dapr 的标准 API 和可扩展的组建模型，我们采取的策略是让用户不需要修改任何代码，直接通过 Dapr Runtime 屏蔽底层使用的中间件：部署在不同平台时，通过激活 Dapr 中的不同的 Component 来提供一致的能力。<br>
<br>以消息通讯威力，当应用需要访问消息系统时：<br>
<ul><li>在阿里内部：通过 Rocketmq.yaml 激活 Rocketmq 组件。</li><li>在公有云上：通过 Kafka.yaml 激活 kafka 组件。</li></ul><br>
<br>通过 Dapr 的可移植性，上层的钉钉文档应用现在可以和底层的基础设施（如消息系统）解耦，从而实现在不同的云平台之间平滑迁移：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210420/032d5ec9bb8b43369cdb7b2d4d7f7111.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210420/032d5ec9bb8b43369cdb7b2d4d7f7111.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>最终帮助我们的业务团队实现了他们的<strong>业务目标</strong>：使 Dingtalk 在任何地方部署成为可能。<br>
<br><h1>阿里的 Dapr 未来规划</h1>未来我们将继续通过应用试点的方式对 Dapr 进行验证，包括：<br>
<ul><li>适用场景</li><li>性能</li><li>稳定性</li><li>可移植性</li></ul><br>
<br>同时我们将继续开发 Dapr 的组件，以集成更多的中间件和基础设施，包括内部产品和阿里云上支持的商业产品。其中对阿里云商业产品的集成代码，我们将在验证通过之后贡献给 Dapr 项目，从而为 Dapr 提供阿里云支持。这些项目预计将包括：<br>
<ul><li>Apache Dubbo 的 RPC 支持</li><li>Apache RocketMQ 的消息传递支持</li><li>Nacos 的动态配置支持</li><li>阿里云 RDS 的 MySQL 支持</li><li>阿里云缓存服务的 Redis 支持</li></ul><br>
<br>作为 Multiple Runtime 架构的先驱者和 Dapr 项目的早期采用者，我们将继续和 Dapr 社区合作，在落地的过程中努力完善 Dapr 的功能、性能、稳定性等关键指标，和社区一起联手打造云原生时代的<strong>D</strong>istributed<strong>AP</strong>plication<strong>R</strong>untime！
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            