
---
title: '服务网格的eBPF _ 是的，但 Envoy Proxy 将继续存在'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://www.solo.io/wp-content/uploads/2021/12/Img1-1.png'
author: Dockone
comments: false
date: 2022-08-14 07:09:28
thumbnail: 'https://www.solo.io/wp-content/uploads/2021/12/Img1-1.png'
---

<div>   
<br><a href="http://solo.io/">Solo.io</a> 的目标是为<a href="https://www.solo.io/customers/">我们的客户</a>提供有关<a href="https://www.solo.io/products/gloo-mesh/">应用程序网络和服务连接</a>相关的解决方案。<a href="https://servicemeshconna21.sched.com/event/mH1h">早在10月</a>，我们就宣布了使用 eBPF 增强我们的企业服务网格产品(Gloo Mesh Enterprise)的计划，以优化网络、可监测性和安全性方面的功能。eBPF在服务网格中能发挥多大的作用呢？服务代理的角色如何变化？在这篇博客中，我们将深入探讨eBPF在服务网格数据平面的作用以及各种数据层架构之间的权衡。<br>
<br><h3>告别服务代理？</h3>服务网格为服务提供复杂的应用网络行为，例如服务发现、流量路由、弹性（超时/重试/断路）、身份验证/授权、可监测性（日志记录/指标/跟踪）等。我们可以用 eBPF 将所有这些功能重写到内核中吗？<br>
<br>简单回答：这将非常困难，可能不是正确的方法。eBPF 是一个事件处理模型，对它的运行方式有一些限制。你可以将 eBPF 模式视为内核的“功能即服务”。例如，在内核中安全执行之前，必须完全了解和验证 eBPF 执行路径。eBPF 程序不能有任意循环，其中的验证者不知道程序何时停止执行。简而言之，eBPF 是图灵不完整的。<br>
<br>七层协议（如各种协议编码器、重试、数据头操作等）单独在 eBPF 中实现可能非常复杂，并且没有更好的内核原生支持。也许这种支持会有，但这可能需要数年时间，并且不会在旧版本上提供。在许多方面，eBPF 是 O(1) 复杂度的理想选择（例如检查数据包、操作一些数据位并在途中发送它）。实现像 HTTP/2 和 gRPC 这样的复杂协议可能是O(n)复杂度并且非常难以调试。那么这些7层功能可以驻留在哪里呢？<br>
<br><a href="https://www.solo.io/blog/getting-started-with-envoy-proxy-in-15-minutes/">Envoy 代理</a>已成为服务网格实现的标准，并且对我们大多数客户所需的第七层功能有很好的支持。尽管 eBPF 和内核可用于改进网络的执行（短路最佳路径、卸载 TLS/mTLS、可监测性收集等），但复杂的协议协商、解析和用户扩展仍可以保留在用户空间中。对于第七层的复杂性，Envoy 仍然是服务网格的数据平面。<br>
<br><h3>共享代理 对比 Sidecar 代理？</h3>尝试优化服务网格的数据路径时的另一个考虑因素，是为每个工作负载运行一个旁路代理，还是为每个节点使用单个共享代理。例如，当运行具有数百个pod和数千个节点的大型集群时，共享代理模型可以围绕内存和配置的开销进行优化。但这是适合每个人的正确方法吗？绝对不是。对于许多企业用户来说，一些内存开销值得通过旁路代理来获得更好的租赁和工作负载隔离。<br>
<br>两种架构都有其在内存和网络开销、租用、操作和简单性方面的优势和权衡，并且都可以受益于基于eBPF的优化。然而，并不是只有这两个架构。让我们从以下维度深入研究全部选项：<br>
<ul><li><strong>内存/CPU 开销</strong> — 为七层代理配置路由和集群信息，包含代理特定的配置组成，这些配置可能很冗长；特定工作负载需要通信的服务越多，它需要的配置就越多。</li><li><strong>功能隔离</strong> — 应用程序很挑剔，往往需要对连接池、套接字缓冲区、重试语义/预算、外部身份验证和速率限制进行每个工作负载的优化。我们看到自定义数据路径的需求很大，这就是我们引入 Wasm 扩展的原因。调试这些功能和行为也变得很苛刻。我们需要找到一种方法来隔离工作负载之间的这些特性。</li><li><strong>安全粒度</strong> — 零信任理念的很大一部分是在运行时根据当前上下文建立对等点的信任；通常希望将这些信任边界的范围尽可能小。</li><li><strong>升级影响</strong> — 服务网格是非常重要的基础设施，因为它位于请求路径上；我们需要对服务网格数据平面组件进行非常可控的升级，以最大限度地减少中断。</li></ul><br>
<br>让我们看看四种可能的架构，其中 eBPF 用于优化和缩短网络路径，并利用 Envoy 代理来实现七层功能。对于每种架构，我们都会根据开销、隔离、安全性和升级来评估在何处运行第七层代理的好处和权衡。<br>
<br><h3>Sidecar 代理（服务代理）</h3><img src="https://www.solo.io/wp-content/uploads/2021/12/Img1-1.png" alt referrerpolicy="no-referrer"><br>
<br>在这个模型中，我们为每个应用程序实例部署了一个 sidecar 代理。Sidecar 具有代表工作负载路由流量所需的所有配置，并且可以根据工作负载进行定制。<br>
<br><img src="https://www.solo.io/wp-content/uploads/2021/12/Img1a.png" alt referrerpolicy="no-referrer"><br>
<br>对于许多工作负载和代理，此配置会在工作负载实例之间重复，并且可能会产生“次优”的资源开销。<br>
<br>该模型确实提供了最佳的特征隔离，以减少任何嘈杂邻居在爆炸半径内的影响。配置错误或特定应用缓冲区/连接池/超时被隔离到特定的工作负载。使用Lua 或 Wasm 的扩展（可能会关闭代理）也受限于特定的工作负载。<br>
<br>从安全角度来看，我们直接发起和终止与应用程序的连接。我们可以使用服务网格的 mTLS 功能来证明连接两端服务的身份，范围缩小到应用程序进程级别。然后我们可以根据这个身份编写细粒度的授权策略。此模型的另一个好处是，如果单个代理最终成为被攻击的受害者，受攻击的代理会被隔离到特定的工作负载；爆炸半径是有限的。然后，不利的一面是，由于 sidecar 必须与工作负载一起部署，因此工作负载可能会选择不注入 sidecar， 或者更糟糕的是，找到一种绕过 sidecar 的方法。<br>
<br>最后，在此模型中，可以按工作负载进行升级，并遵循仅影响特定工作负载的金丝雀方法。例如，我们可以将 Pod A 的数据平面升级到新版本，而不会影响节点上的其他任何工作负载。这样做的缺点是注入 sidecar 仍然很棘手，如果版本之间有变化，它可能会影响应用程序实例。<br>
<br><h3>每个节点共享代理</h3><img src="https://www.solo.io/wp-content/uploads/2021/12/Img2-2.png" alt referrerpolicy="no-referrer"><br>
<br>每个节点的共享代理引入了对大型集群有意义的优化，在这些集群中，内存开销是首先要考虑的，并且需要分摊内存成本。在此模型中，不是为每个 sidecar 代理配置路由流量所需的路由和集群，而是在单个代理中的节点上的所有工作负载之间共享该配置。<br>
<br><img src="https://www.solo.io/wp-content/uploads/2021/12/Img2-1.png" alt referrerpolicy="no-referrer"><br>
<br>从功能隔离的角度来看，您最终会尝试在一个进程（一个 Envoy 代理）中解决全部工作负载实例的全部问题，这可能会有缺点。例如，跨多个应用程序的配置是否会相互冲突或在代理中具有偏移行为？您能否安全地加载出于监管原因必须分开的密文或私钥？您能否在不影响其他应用程序代理行为的情况下部署 Wasm 扩展？为一堆应用程序共享一个代理存在隔离问题，这可能会通过单独的进程/代理更好地解决。<br>
<br>在每个节点共享代理的模型中，安全边界也变成共享。例如，工作负载身份确认现在在节点级别处理，而不是实际工作负载级别。代理和工作负载之间的“最后一英里”会发生什么？或者更糟糕的是，如果一个代表多个（数百个？）工作负载身份的共享代理遭到破坏，会发生什么情况？<br>
<br>最后，如果升级存在版本冲突、配置冲突或扩展不兼容等问题，升级每个节点的共享代理可能会影响节点上的所有工作负载。每次升级处理应用程序请求的共享基础架构时，都必须小心。从好的方面来说，升级共享节点代理不必考虑注入sidecar的任何复杂性。<br>
<br><h3>每个服务账户的共享代理（每个节点）</h3><img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1097/https://www.solo.io/wp-content/uploads/2021/12/Img3-2.png" alt referrerpolicy="no-referrer"><br>
我们可以将代理细分到每个节点的特定服务账户，而不是为整个节点使用单个共享代理。在此模型中，我们为每个服务账户/身份部署一个“共享代理”，并且该服务账户/身份下的任何工作负载都使用该代理。使用该模型，我们可以避免一些注入sidecar的复杂性。<br>
<br> <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_682/https://www.solo.io/wp-content/uploads/2021/12/Img3-1.png" alt referrerpolicy="no-referrer"><br>
<br>该模型可以在单个节点上存在相同身份的多个实例的情况下节省内存，并保持一定程度的特征和嘈杂邻居的隔离。这种模型在工作负载身份方面具有与sidecar相同的优点，但它确实具有共享代理的缺点：最后一英里连接会发生什么？工作负载实例的身份验证是如何建立的？为了改进这个模型，我们可以使用一个较小的“微代理”，它与应用程序工作负载实例一起存在，可以存进端到端 mTLS 到实例级别。在下一个模式中我们可以看到这一点。<br>
<br><h3>使用微代理做共享远程代理</h3> <img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1097/https://www.solo.io/wp-content/uploads/2021/12/remote-proxy-with-micro-proxy.png" alt referrerpolicy="no-referrer"><br>
<br>在这个模型中，一个更小、更轻量级的“微代理”（uProxy）被部署为带有工作负载实例的sidecar，它只处理mTLS（没有第7层策略，更小的攻击面）。当需要使用第7层策略时，流量会从工作负责实例通过第7层（Envoy）代理定向。第7层代理可以作为共享节点代理、每个服务账户甚至远程代理来运行。此模型还允许在可能不需要这些策略时完全通过第7层代理（但会与应用程序实例保持mTLS发起/协商/终止）。<br>
<br><img src="https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_684/https://www.solo.io/wp-content/uploads/2021/12/Img4-1.png" alt referrerpolicy="no-referrer"><br>
<br>此模型减少了您在sidecar中看到的第7层策略的配置开销，但可能会引入更多跃点。这些跃点可能（或可能不会）导致更多的呼叫延迟。对于某些呼叫，L7代理可能甚至不在数据路径中，这会改善呼叫延迟。<br>
<br>由于uProxy仍与工作负载实例一起部署，因此该模型结合了隔离性和安全性的sidecar代理优势。<br>
<br>从升级的角度来看，我们可以将L7代理无感的更新到应用程序，但是我们现在有更多的移动组件。我们还需要协调uProxy的升级，它与我们在第一模式中讨论的sidecar架构有一些相同的缺点。<br>
<br><h3>其他的想法</h3>正如在 Service Mesh Con 2019 上的“<a href="https://www.youtube.com/watch?v=bmf0JQtDJL4">关于服务网格数据平面的真相</a>”中所讨论的，代表数据平面的架构可能会有所不同，并且有不同的权衡利弊。在Solo.io，我们将eBPF视为优化服务网格的强大方法，并将Envoy代理视为数据平面的基石。与我们的许多客户（不同规模，包括世界上一些最大的服务网格部署）合作，我们处于一个独特的位置，可以帮助平衡优化、功能、可扩展性、可调试性和用户体验之间的权衡利弊。<br>
<br><strong>原文链接：<a href="https://www.solo.io/blog/ebpf-for-service-mesh/">eBPF for Service Mesh? Yes, but Envoy Proxy is here to stay</a></strong>
                                
                                                              
</div>
            