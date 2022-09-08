
---
title: 'Istio vs. Linkerd vs. Consul'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220818/5c82101f8512d7f52e826ddf1a9e9e0c.jpeg'
author: Dockone
comments: false
date: 2022-09-08 05:14:39
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220818/5c82101f8512d7f52e826ddf1a9e9e0c.jpeg'
---

<div>   
<br><h3>服务网格简介</h3>服务网格是应用程序组件和网络之间通过代理连接的基础设施层。这些应用程序组件通常是微服务，但从无服务器容器到虚拟机或裸机上的传统应用程序的任何工作负载都可以参与服务网格。每个组件之间不是通过网络直接通信，而是通过代理来通信。这些代理构成了数据平面，提供了许多功能，用于实现安全和流量策略，并对代理部署的服务进行遥测。更多关于服务网格功能的介绍请阅读<a href="https://www.tetrate.io/blog/what-is-a-service-mesh/">本篇文章</a>。<br>
<br>服务网格的功能包括：<br>
<ul><li>服务发现</li><li>弹性：重试、异常检测、断路、超时等</li><li>客户端负载平衡</li><li>L7 细粒度流量控制：按标题、目的地或源以及其他运行时信息进行路由</li><li>为每个请求设置安全策略，而不是每个连接</li><li>基于 L7 元数据的身份验证、速率限制、任意策略</li><li>强（L7）工作负载标识</li><li>服务到服务授权</li><li>指标、日志和跟踪</li></ul><br>
<br>我们相信，这项调查表明，Istio 是最有能力、最灵活、应用最广泛的服务网格，也是最受社区支持的服务网格。因此，Istio 在各个领域都在稳步改进。Consul 和Linkerd 属于轻量级设计，社区并不广泛支持。因此，它们在最初可能更容易实现，并且在过去具有性能优势，但它们可能不太适合要求苛刻的用例和长期使用。<br>
<br><h3>服务网格的工作模型</h3>服务网格遵循“中心辐射”模式，即使用代理或工作节点实现特定规则，并使用中央服务器管理代理。Istio 和 Consul 使用 Envoy 代理，而 Linkerd 使用其定制的代理。这些代理在应用程序级别的数据平面中工作。他们负责繁重的任务，如处理传入流量、连接服务和细粒度安全策略。网络通信和安全管理在集中控制平面完成。<br>
<br><h3>服务网格比较</h3>IT 部门通常会根据特定的标准，以找到合适的服务网格软件。本文将提供一个比较图表，以帮助 IT 架构师快速选择和采用正确的服务网格软件。<br>
<br>实现服务网格最著名的开源工具有：<a href="https://istio.io/">Istio</a>、<a href="https://linkerd.io/">Linkerd</a> 和 <a href="https://www.consul.io/">Consul</a>。Istio 和 Consul 都使用 Envoy 作为数据代理。Linkerd 有自己的开源代理。我们将在本文中比较这三个著名的服务网格项目。<br>
<br>我们基于以下六个标准比较服务网格软件：流量管理、安全管理、可伸缩性、可见性和可观察性、安装和实现、可扩展性。并分享了我们的观点。<br>
<br><h4>流量管理</h4>Istio、Consul 和 Linkerd 都提供基本的流量管理功能，如负载平衡、路由和服务发现。并且支持 HTTP、gRPC 代理、TCP 代理和协议检测。<br>
<br>Istio 和 Consul 使用的 Envoy 代理实现了比 Linkerd 更多的 HTTP 特定功能。Envoy 的 <a href="https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management">HTTP connection manager</a> 提供了对 HTTP/1.1、WebSocket、HTTP/2 和 HTTP/3 的支持，而 Linkerd 暂不支持HTTP/3。<br>
<br>相较于 Linkerd，因为 Istio 和 Consul 都使用了 Envoy，它们还具有更细粒度的流量管理功能，如断路、重试、超时、故障注入、延迟注入等功能。<br>
<br>Istio 是唯一一款支持 Kubernetes 的软件，无论是部署在公有云（例如 AWS，GCP，Azure）的 Kubernetes 还是私有云的 Kubernetes。这使得 Istio 成为许多大型企业的首选软件，因为大型企业既有支持云原生的应用程序，也有许多单体应用程序。<br>
<br>架构师和工程师喜欢 Istio 的理由：<br>
<ul><li>前端/边缘代理：Istio 可以根据运行时的值重定向请求，使金丝雀和蓝/绿等部署策略的实现变得容易。</li><li>支持入口网关：Istio 提供 Istio 入口网关，并支持第三方 ingress controllers 管理 Kubernetes 集群中的外部服务访问。</li><li>多集群通信：易于使用 Istio 服务网格连接跨集群或区域的 Kubernetes 服务。</li><li>多站点故障切换：由于支持所有公共云，Istio 可用于自动故障切换，以支持基于云的应用程序的高可用性和更大的弹性。</li></ul><br>
<br><h4>安全管理</h4>Istio、Consul 和 Linkerd 都支持身份验证和授权功能，例如：<br>
<ul><li>基于 mTLS 的身份验证，确保网络通信的安全性</li><li>基于 JWT 的身份验证可保护来自外部和内部用户的应用程序</li><li>定义细粒度的安全策略，例如工作负载到工作负载，最终用户到工作负载的授权和访问控制</li></ul><br>
<br>然而，由于 Istio 提供了与云平台和虚拟机的集成，可以使用 Istio 的 mTLS的身份验证，构建应用与外部客户机或其他 Kubernetes 集群或虚拟机之间的通信。以下是为什么安全经理更喜欢 Istio 以确保零信任安全模型的原因：<br>
<ul><li>FIPS 兼容：Istio 的许多实现都是 FIPS 兼容的，属于 FIPS 遵守的中等水平，而 Tetrate 的实现也是 FIPS 认证的，且属于 FIPS 的最高水平。这使得 Istio 成为遵守 2014年《联邦信息安全现代化法案》的组织的最佳选择。请参阅 <a href="https://www.tetrate.io/blog/tetrate-first-to-provide-hardened-istio-to-dods-iron-bank/">Refer to how Istio helps the Federal Government and the Department of Defense secure their internal applications</a>.</li><li>CVEs 的透明度：Istio 与国家 CVE 数据库共享漏洞，网络安全管理人员可以直接参考国家 CVE 数据库中的最新安全缺陷和问题，已知晓 Istio 存在的安全问题。此外，Istio 会及时实施安全补丁，并及时通知 Istio 用户。</li><li>灵活性：Istio 可以和任何的身份验证提供商集成，如 OpenID 连接提供商，例如 KeyClope、OAuth 2.0、Google Auth、Firebase Auth等。</li></ul><br>
<br>美国国家标准与技术研究所（NIST）使用 Istio 作为参考架构，为联邦机构实施安全标准，实现零信任。请参阅 <a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf">Security Strategies for Microservices</a>，<a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204A.pdf">Building Secure Microservice using Service Mesh Architecture</a>，<a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204B-draft.pdf">Attributed-based access control for microservices using Service mesh</a>，<a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204C-draft.pdf">Implementation of DevSecOps for a Microservice using Service Mesh</a>。<br>
<br><h4>安装和使用</h4>无需更改应用程序代码，就可以安装和使用服务网格。但一般来说，服务网格的设置和维护是一个难题。并且运维团队特别关注软件的安装、使用和性能问题。<br>
<br>Istio、Consul 和 Linkerd 都可以使用 Helm charts 或 Operators 在 Kubernetes 环境中轻松完成安装。由于 Linkerd 是轻量级的，具有较少的功能和简单的架构，因此它比 Istio 和 Consul 更易于维护和执行。Istio 通常被认为是“重量级”的，主要是因为它支持更多的工作负载、公共云和虚拟机。<br>
<br>但随着时间的推移，Istio 已经提高了性能，并努力以最小的资源开销提供更多的网络管理和安全优势。该项目还旨在支持具有高请求率的大型服务网格，同时增加最小延迟。<br>
<br><h4>可伸缩性</h4>在按需扩展方面，每种服务网格都具有独特的优势。<br>
<br>关于数据平面的可扩展性，Linkerd 的扩展速度比 Istio 和 Consul 快。主要原因是 Linkerd 的轻量级架构，它不支持高级流量管理和细粒度安全管理功能。<br>
<br>从数据平面的角度来看，在资源受限的环境中，Envoy 可能会比 Linkerd 消耗更多的 CPU。然而，Envoy 遵循一种实用的设计，适合在真实的 IT 环境中实现更快的性能。Envoy 的维护人员在关键路径的代理性能调优方面做了出色的工作。性能将因所使用的功能、Envoy 运行的环境和可用的计算机资源而大不相同。<br>
<br>此外，请注意，性能仅做了横向对比。如果此软件不能满足你的所有需求，也不能达到与竞争对手相同的性能标准，那么它就不会以一种有用的方式更快或更轻。如果你的用例（现在和将来）完全由其功能集满足，那么你只能考虑重量更轻、功能更少的替代方案。在企业实施或技术要求苛刻的环境中，这种情况不太可能发生。<br>
<br>同时，请注意，需在类似产品的基础上做性能比较。一款软件不可能既轻量级、性能高且功能全。<br>
<br>我们将遵循 <a href="https://www.envoyproxy.io/docs/envoy/latest/faq/performance/how_to_benchmark_envoy">best practices for benchmarking Envoy</a> ，以科学的流程进行性能测试。<br>
<br>Istio 负载测试，考虑了由 1000 个微服务和 2000 个 sidecars 组成的服务网格。每秒向网格发送 70000 个请求，并测量响应时间。使用 Istio 1.14.1 运行测试后，数据平面和控制平面的观察结果如下：<br>
<ul><li>数据平面性能：Envoy 代理每秒处理 1000 个请求，使用了 0.35 个 vCPU 和 40 MB 内存。还观察到 Envoy 代理，后 10% 的请求延迟增加了 2.65毫秒。</li><li>控制平面性能：Istiod 使用 1 个 vCPU 和 1.5 GB 内存。</li></ul><br>
<br>你可以在<a href="https://istio.io/latest/docs/ops/deployment/performance-and-scalability/">这里</a>找到 Istio 的详细性能测试结果。<br>
<br><h4>可见性和可观测性</h4>分布式服务的端到端可见性和可观察性对于运维团队来说至关重要。SRE 和 Ops 团队需要服务网格中的服务级别可见性、跟踪和监控能力。Istio、Consul 和 Linkerd 都提供了对应用程序性能健康状况的可见性，测量网络行为并向利益相关者出具报告。<br>
<br>Istio、Consul 和 Linkerd 生成监控所需的关键指标，如 HTTP、HTTP/2 和 gRPC 流量的延迟、错误和饱和度。服务网格软件提供的指标可以直接从命令行界面（CLI）或 Grafana 仪表板查看，也可以使用 Prometheus 来查看。<br>
<br>与 Linkerd 相比，Istio 和 Consul 都提供了更详细的网络指标。Envoy 代理在 Istio 和 Consul 中形成数据平面，为 Ops 团队提供足够的服务级别指标、代理级别指标和分布式跟踪，更快地诊断流量管理配置问题。由于 Envoy 也是一个广泛使用的数据平面，Ops 团队更容易从社区中找到配置或性能异常的解决方案。<br>
<br>与 Linkerd 不同，Istio 提供了对日志工具的支持，如 <a href="https://istio.io/latest/docs/tasks/observability/distributed-tracing/zipkin/">Zipkin</a>、<a href="https://istio.io/latest/docs/tasks/observability/distributed-tracing/jaeger/">Jaeger</a>、<a href="https://istio.io/latest/docs/tasks/observability/distributed-tracing/lightstep/">Lightstep</a> 和 <a href="https://www.datadoghq.com/blog/monitor-istio-with-datadog/">Datadog</a>。<br>
<br>如果你感兴趣，更多 Istio 命令，请参考 <a href="https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/">detailed overview</a>。<br>
<br><h4>人气</h4>Istio 是社区内外最流行的服务网格软件。这意味着更多的创新和更积极的功能开发。有证据表明，与任何其他服务网格相比，Istio 是全球架构师、DevOps 团队和安全专业人员最广泛使用的。虽然使用情况可能因行业有所不同，但 Istio 目前已在金融服务行业和美国政府使用，并在关键领域取得成功。因此，Istio 可能会全面保持或增加其领导地位。<br>
<br><strong>谷歌趋势（Google Trending）</strong><br>
<br>为了评估这些项目的受欢迎程度，我们在 Google Trends 上搜索了关键词 “Istio Service Mesh”、“Consul Service Mesh” 和 “Linkerd Service Mesh”。（我们之所以使用较长的短语，是因为“Consul”一词本身被广泛使用，并具有多种含义。）在过去五年左右的时间里，Istio 服务网格的受欢迎程度直线上升，Consul 和 Linkerd 远远落后，尤其是 Linkerd。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220818/5c82101f8512d7f52e826ddf1a9e9e0c.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220818/5c82101f8512d7f52e826ddf1a9e9e0c.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>谷歌搜索显示，Istio 的活动远远领先于 Consul 和 Linkerd。<br>
<br><a href="https://trends.google.com/trends/explore?date=2016-06-25%202022-07-25&q=istio%20" rel="nofollow" target="_blank">https://trends.google.com/tren ... %2520</a><br>
<br><strong>贡献者的多样性</strong><br>
<br>除了更多的参与和贡献外，Istio 还有各种各样的贡献者。虽然 Buoyant 和 Hashicorp 分别是 Linkerd 和 Consul 项目的主要贡献者，但对 Istio 的贡献来自于不同的大型企业，如谷歌、IBM、埃森哲、VMware 等，以及许多小型企业。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220818/a30e1c92d76f096a00941a53eba262c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220818/a30e1c92d76f096a00941a53eba262c7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>Git 订阅</strong><br>
<br>与同行相比，Istio 拥有最多的 Git 观星者。观星者越多，开源社区的参与度就越高。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220818/da5cb518d6dc47b7a77f7228ae8ab307.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220818/da5cb518d6dc47b7a77f7228ae8ab307.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>捐款管理</strong><br>
<br>Istio 项目的指导委员会实行良好治理，使 Istio 仅由贡献者和社区成员驱动。指导委员会至少代表七个不同的组织。这避免了任何供应商对 Istio 项目拥有多数投票控制权，而不管贡献大小。<br>
<br>没有其他服务网格软件委员会采用如此多样化的治理来满足社区的利益。Envoy 项目还具有不同的治理，最近添加了一个新项目，<a href="https://www.businesswire.com/news/home/20220515005047/en/Envoy-Gateway-Makes-Using-Envoy-Proxy-Easier-for-Developers-and-Reverses-Fragmentation">Envoy Gateway</a>，其中包括 Tetrate 作为指导委员会的一部分。<br>
<br>欲了解更多信息，请阅读 <a href="https://github.com/istio/community/blob/master/steering/README.md">the Istio governance structure</a>。<br>
<br><h4>Istio、Linkeder、Consul对比表格</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220818/26e77098cf8b538135dd56ea52c6e0c1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220818/26e77098cf8b538135dd56ea52c6e0c1.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>可扩展性</h4>所有服务网格软件都是模块化和可扩展的。但由于 Istio 比其他服务网格更受欢迎，许多开源项目都是通过 Istio 实现的。一些值得注意的项目包括：<br>
<ul><li>Slime，使用 Istio 和 Envoy 的智能服务管理器</li><li>MOSN，提供云本地边缘网关和代理</li><li>Aeraki，为除 HTTPs 和 gRPC 之外的所有 L7 协议提供支持</li><li>WASM，开发 WebAssembly 插件并增强服务网格功能</li></ul><br>
<br>在<a href="https://www.tetrate.io/blog/introducing-slime-and-aeraki-in-the-evolution-of-istio-open-source-ecosystem/">这里</a>你可以找到所有基于Istio生态系统的开源项目。<br>
<br><h3>总结</h3>随着越来越多的组织使用微服务并采用多云技术，服务网格在应对新的网络复杂性和安全挑战方面变得越来越重要。在选择服务网格软件时，组织必须仔细评估这些选项，以避免 IT 项目的失败。<br>
<br>在仔细评估了三种流行的服务网格的各种功能后，我们认为 Istio 提供了比其同类产品更丰富的功能集。如果你是一个小型的 IT 初创公司，只有一个小型的 DevOps 和安全团队，并且没有在一个特别具有挑战性的安全环境中运行，而且在可预见的未来你能够以这种方式运行，那么轻量级的 Linkerd 或 Consul 可能是更优选择。但如果你有一个大规模的 IT 系统和一个庞大的团队，或者你认为安全是首要任务，那么 Istio 是更安全的选择。<br>
<br>通过这些比较得出 Istio 是最受欢迎和广泛实施的服务网格，整体体验更佳。在可扩展性和性能方面，我们认为 Istio 和 Envoy 最适合大规模的产品系统。<br>
<br><strong>原文链接：<a href="https://www.tetrate.io/blog/istio-vs-linkerd-vs-consul/">Istio vs. Linkerd vs. Consul</a>  （翻译：钟涛）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            