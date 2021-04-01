
---
title: 'OpenTelemetry 简析'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/bf3242aa315842a1ad0714607c116ecf.png'
author: Dockone
comments: false
date: 2021-04-01 12:10:45
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/bf3242aa315842a1ad0714607c116ecf.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/bf3242aa315842a1ad0714607c116ecf.png" alt="头图.png" referrerpolicy="no-referrer"><br>
<br>作者 | 悟鹏<br>
来源 | <a href="https://mp.weixin.qq.com/s/n4eVf2KZRIp2yKACk88qJA">阿里巴巴云原生公众号</a><br>
<br>OpenTelemetry 是 CNCF 的一个可观测性项目，旨在提供可观测性领域的标准化方案，解决观测数据的数据模型、采集、处理、导出等的标准化问题，提供与三方 vendor 无关的服务。<br>
<br>2021.02.10，OpenTelemetry 的 tracing spec 达到 1.0 版本 (<a href="https://medium.com/opentelemetry/opentelemetry-specification-v1-0-0-tracing-edition-72dd08936978">link</a>)，基于这个里程碑，笔者对 OpenTelemetry 进行了探索，判断在可观测性领域带来的价值和发展前景。<br>
<br>下面给出笔者对 OpenTelemetry 的理解，抛砖引玉。由于笔者能力有限，理解不当的地方请大家指正。<br>
<br><h2>OpenTelemetry 是什么？</h2>从官方 <a href="https://opentelemetry.io/docs/concepts/what-is-opentelemetry/">What is OpenTelemetry?</a> 可了解到：<br>
<br><blockquote><br>OpenTelemetry is a set of APIs, SDKs, tooling and integrations that are designed for the creation and management of telemetry data such as traces, metrics, and logs.</blockquote>The project provides a vendor-agnostic implementation that can be configured to sent telemetry data to the backend(s) of your choice. It supports a variety of popular open-source projects including Jaeger and Prometheus.<br>
<br>OpenTelemetry 是一组标准和工具的集合，旨在管理观测类数据，如 trace、metrics、logs 等 (未来可能有新的观测类数据类型出现)。<br>
<br>OpenTelemetry 提供与 vendor 无关的实现，根据用户的需要将观测类数据导出到不同的后端，如开源的 Prometheus、Jaeger 或云厂商的服务中。<br>
<br>那么 OpenTelemetry 不是什么？从官方描述可以看出：<br>
<br><blockquote><br>OpenTelemetry is not an observability back-end like Jaeger or Prometheus. Instead, it supports exporting data to a variety of open-source and commercial back-ends. It provides a pluggable architecture so additional technology protocols and formats can be easily added.</blockquote>即 OpenTelemetry 不提供与可观测性相关的后端服务，这类后端服务通常提供的是存储、查询、可视化等服务。<br>
<br>通过下述抽象图可以简单理解 OpenTelemetry 的工作范围：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/a2e384c3a2fac63d9421449d2e0a4d59.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/a2e384c3a2fac63d9421449d2e0a4d59.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>OpenTelemetry 面对的问题域是什么？</h2>从 <a href="https://en.wikipedia.org/wiki/Observability">wikipedia: Observability</a> 可理解到 <strong>可观测性</strong> 的定义：<br>
<br><blockquote><br>In control theory, observability is a measure of how well internal states of a system can be inferred from knowledge of its external outputs.</blockquote>Consider a physical system modeled in state-space representation. A system is said to be observable if, for any possible evolution of state and control vectors, the current state can be estimated using only the information from outputs (physically, this generally corresponds to information obtained by sensors). In other words, one can determine the behavior of the entire system from the system's outputs. On the other hand, if the system is not observable, there are state trajectories that are not distinguishable by only measuring the outputs.<br>
<br>简单表述为，可观测性是一种方法，通过系统的外部输出推导出系统内部的状态。<br>
<br>下图简化了系统的组成和系统间的交互：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/6f89be04812a37a5f3d3e026672954b1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/6f89be04812a37a5f3d3e026672954b1.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>从上述交互图可了解到，系统的交互行为有如下几种形态：<br>
<ul><li><br>系统内部<br>
<ul><li>组件功能闭环，不与其他组件或系统交互</li><li>组件之间交互</li></ul></li><li><br>系统之间<br>
<ul><li>系统和系统之间进行交互</li></ul></li></ul><br>
<br>这样，若想通过系统的外部输出了解系统的状态，就需要两种形态的信息：<br>
<ul><li>组件闭环的信息</li><li>组件间或系统间流动的信息</li></ul><br>
<br>第一种形态通常可通过 logs 或 metrics 表征，第二种形态就需要 trace 表征，在流动的信息中增加标记。<br>
<br>对于 logs 和 metrics 的区别，可通过它们的操作方法进行理解。<br>
<br>再进一步抽象，可观测性涉及到如下问题：<br>
<ul><li>观测数据的数据模型</li><li>观测数据的采集</li><li>观测数据的处理</li><li>观测数据的导出</li><li>观测数据的使用</li><li>etc.</li></ul><br>
<br>上述即是 OpenTelemetry 面对的问题域及具体的问题，且将具体的问题限定在：<br>
<ul><li>观测数据的数据模型</li><li>观测数据的采集</li><li>观测数据的处理</li><li>观测数据的导出</li></ul><br>
<br><h2>OpenTelemetry 的解决方案是什么？</h2>OpenTelemetry 通过 Spec 规范了观测数据的数据模型以及采集、处理、导出方法，包括 trace、metrics、logs (未来不排除会有新的类型)，参见 <a href="https://github.com/open-telemetry/opentelemetry-specification">opentelemetry-specification</a>。<br>
<br>同时为了方便使用，通过 protobuf 来描述，参见<a href="https://github.com/open-telemetry/opentelemetry-proto">opentelemetry-proto</a>。<br>
<br>基于 Spec，OpenTelemetry 面向观测数据的生成和处理，做了如下的努力：<br>
<ul><li>为了方便开发者使用，提供了语言相关的 SDK，如 <a href="https://github.com/open-telemetry/opentelemetry-go">opentelemetry-go</a>、<a href="https://github.com/open-telemetry/opentelemetry-java">opentelemetry-java</a>、<a href="https://github.com/open-telemetry/opentelemetry-js">opentelemetry-js</a> 等，所有支持的开发语言可参见 <a href="https://opentelemetry.io/docs/">官方文档</a></li><li>为了方便可观测数据的采集、处理、导出，提供了通过配置管理的 Collector 服务，如对接开源项目的 <a href="https://github.com/open-telemetry/opentelemetry-collector">opentelemetry-collector</a>、对接第三方 vendor 的 <a href="https://github.com/open-telemetry/opentelemetry-collector-contrib">opentelemetry-collector-contrib</a></li></ul><br>
<br>通过下图可直观理解 OpenTelemetry 的组件和工作流：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/1ecec18b5a76641ab907b85c3971916f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/1ecec18b5a76641ab907b85c3971916f.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>OpenTelemetry 的历史是什么？</h2>从 <a href="https://www.cncf.io/blog/2019/05/21/a-brief-history-of-opentelemetry-so-far/">A brief history of OpenTelemetry (So Far) </a> 可简单了解到，OpenTelemetry 是由两个开源项目合并组成的：<br>
<ul><li><br><a href="https://opencensus.io/">OpenCensus</a><br>
<ul><li>面向 trace 和 metrics 进行数据模型标准化，并提供采集、处理、导出的工具</li></ul></li><li><br><a href="https://opentracing.io/">OpenTracing</a><br>
<ul><li>面向 trace 进行数据模型标准化，并提供采集、处理、导出的工具</li></ul></li></ul><br>
<br>2019 年 5 月，两个开源项目合并，官方宣布开源 OpenTelemetry 项目。<br>
<br>2021.02，trace spec 达到 1.0 版本，根据官方的成熟度模型 (<a href="https://github.com/open-telemetry/opentelemetry-proto#maturity-level">link</a>)，目前 trace 的 spec 已经达到 stable 级别，metrics 达到了 beta 级别，logs 当前还处在 alpha 级别：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/4497ba774c4cd14b164453348d2adfd5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/4497ba774c4cd14b164453348d2adfd5.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>OpenTelemetry 的前景如何？</h2>自 OpenTelemetry 推出以来，有越来越多的厂商开始关注和贡献。<br>
<br>从 <a href="https://github.com/open-telemetry/opentelemetry-collector-contrib">opentelemetry-collector-contrib</a> 可看出来，厂商的关注重点在于 exporter 部分，将观测数据便利导入到自身的服务中，其中已经包含阿里云自身的 <a href="https://www.aliyun.com/product/sls">SLS 产品</a>：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/1e2ca6e23395d4911a212d2babd1adc5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/1e2ca6e23395d4911a212d2babd1adc5.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>对于 receiver 和 processor 环节，相信厂商也会逐步投入更多的精力，如：<br>
<ul><li>通过 receiver 和 exporter 的配合，形成观测数据的处理 workflow</li><li>通过 processor，在观测数据存储前进行规范化处理</li></ul><br>
<br>对于多云场景，OpenTelemetry 定义的观测数据模型、采集/处理/导出 标准，将有利于用户通过一套可观测性标准对接多种云厂商，避免 vendor 锁定。<br>
<br>即使是面向单一的云 (如云厂商内部的服务)，也不可避免会考虑未来进行开源、与外部共建等，使用社区的可观测性标准可以降低开源成本。同时，可观测性的理念、标准、技术在不断迭代，通过跟进社区，可以更好使用到社区带来的技术红利和影响力。<br>
<br>因此，无论是面对多云场景还是单一的云厂商，采用业界的可观测性标准都是很有必要。<br>
<br><h2>OpenTelemetry 如何使用？</h2><h3>核心概念</h3>OpenTelemetry 中的概念比较多，这里列举些常见的概念，方便进行理解：<br>
<ul><li><br>观测数据相关<br>
<ul><li>Signal<br>
<ul>- 观测数据类型，如 trace、metrics、logs</ul></li><li>Instrument<br>
<ul>- 可认为是某种 Signal 的实例</ul></li></ul></li><li><br>OpenTelemetry 自身项目相关<br>
<ul><li>API<br>
<ul>- OpenTelemetry Spec 的形式化描述，如 [opentelemetry-proto](https://github.com/open-telemetry/opentelemetry-proto)</ul></li><li>SDK<br>
<ul>- 面向不同开发语言的 API 实现</ul></li><li>Contrib Packages<br>
<ul>- 与具体的开源项目或 vendor 产品相关的实现</ul></li></ul></li><li><br>使用的组件相关<br>
<ul><li>Components<br>
<ul><li>Receivers<br>
<ul>- 接收观测数据的组件</ul></li><li>Processors<br>
<ul>- 处理接收到的观测数据的组件</ul></li><li>Exporters<br>
<ul>- 将观测数据导出的组件，如导出到开源项目 Prometheus 或云厂商服务中</ul></li><li>Extensions<br>
<ul>- 不参与观测数据的处理，辅助相关处理组件的运行，如健康检测、服务发现等</ul></li><li>Services<br>
<ul>- 表征配置的哪些组件需要运行，如 receivers / processors / exporters / extentions</ul></li><li>Collector<br>
<ul>- 可认为是 receivers / processors / exporters / extentions / services 组成的整体</ul></li>- Controller<br>
 - 用于开发者开发的应用中，作用可等同于 receivers / processors / exporters 组成的整体</ul></li></ul></li></ul><br>
<br><h3>golang demo</h3>笔者写了一个 golang demo，用来演示：<br>
<ul><li>APP 中如何生成 trace / metrics 数据</li><li>APP 中使用 stdout controller 来采集、处理、打印 trace / metrics 数据</li><li>APP 中通过 otlp controller 采集 trace / metrics 数据，并导出到外部运行的 collector 中</li><li>本地独立运行一个 collector 服务，接收 otlp controller 推送的 trace / metrics 数据，并将其导出到本地文件和阿里云 SLS 中</li></ul><br>
<br>demo 参见：<a href="https://github.com/flyer103/otel-demo"></a><a href="https://github.com/flyer103/otel-demo" rel="nofollow" target="_blank">https://github.com/flyer103/otel-demo</a><br>
<br>具体的使用方法参见 demo 的 README.md，下述简单描述下思路。<br>
<br>cmd/app/server.go 文件描述了 OpenTelemetry 的使用逻辑，分成两部分：<br>
<ol><li>初始化并运行全局的 controller，用来在 APP 内部 receive / process / export 观测数据，或将 APP 内的观测数据推送到外部</li><li>APP 内按照业务需求生成 metrics 和 trace</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/aed2256ef48d58c017e24f19dee1766e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/aed2256ef48d58c017e24f19dee1766e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>pkg/ 目录下分别封装了 controller 和 signal (trace / metrics)，具体的实现不再赘述：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/9940b0302ef54017ca24d898003a56b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/9940b0302ef54017ca24d898003a56b4.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>yaml/ 下提供了一个将观测数据导出到 SLS 的示例，包括了用于接收观测数据的 receiver (client 端可通过 grpc client 将数据推送到该 receiver)、用于观测数据转换处理的 processors、用于数据导出的 exporters、用于开启组件的 services：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/15536bf7b80b7d3bbe5d46b8eeda3a0c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210401/15536bf7b80b7d3bbe5d46b8eeda3a0c.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>畅想</h2>通过上述分析，大家对 OpenTelemetry 的概念、问题域、解决方案和使用方法会有一个直观的体会，通过上述 golang demo 可以快速上手。<br>
<br>对于开发者，基于 OpenTelemetry 可通过一套标准的方案进行 trace / metrics / logs 的生成和导出，降低开发过程中对不同类型观测数据的使用成本，也降低对接不同后端服务的成本，如开源项目 Prometheus 或第三方云厂商的服务。<br>
<br>对于 SRE，基于 OpenTelemetry 可为观测数据提供一套标准的采集、处理、导出流程，并在处理环节根据团队需求规范化观测数据，便于后续采用标准化的方案使用观测数据，如监控、告警服务。<br>
<br>同时，不论对于开发者还是 SRE，均可以通过社区的力量持续迭代对可观测性问题域的理解，吸收社区的技术红利，并将生产中产生的最佳实践回馈社区，更好推动可观测性领域的发展。<br>
<br><h2>References</h2><ul><li><a href="https://peter.bourgon.org/blog/2017/02/21/metrics-tracing-and-logging.html">Metrics, tracing, and logging</a></li><li><a href="https://medium.com/opentracing/a-roadmap-to-convergence-b074e5815289">Merging OpenTracing and OpenCensus: A Roadmap to Convergence</a></li><li><a href="https://epsagon.com/tools/introduction-to-opentelemetry-overview/">Introduction to OpenTelemetry (Overview Part 1/2)</a></li><li><a href="https://epsagon.com/observability/opentelemetry-best-practices-overview-part-2-2/">OpenTelemetry Best Practices (Overview Part 2/2)</a></li><li><a href="https://www.cncf.io/blog/2020/08/06/opentelemetry-future-proofing-your-instrumentation/">OpenTelemetry: Future-Proofing Your Instrumentation</a></li><li><a href="https://signoz.io/blog/opentelemetry-kubernetes/">Getting started with OpenTelemetry on Kubernetes</a></li><li><a href="https://opentelemetry.io/">OpenTelemetry 官网</a></li><li><a href="https://en.wikipedia.org/wiki/Observability">wikipedia: Observability</a></li></ul><br>
<br><strong>欢迎大家留言交流使用 Kubernetes 过程中的稳定性保障问题，以及对稳定性保障的期待工具或服务。大家也可通过邮箱联系作者，进一步深入交流：<a href="mailto:flyer.zyf@alibaba-inc.com">flyer.zyf@alibaba-inc.com</a></strong>。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            