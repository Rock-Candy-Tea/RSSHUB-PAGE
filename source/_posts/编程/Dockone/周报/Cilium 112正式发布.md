
---
title: 'Cilium 1.12正式发布'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220721/fb900fb8baee7f5654205fcc46b5c0ec.png'
author: Dockone
comments: false
date: 2022-07-29 10:11:09
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220721/fb900fb8baee7f5654205fcc46b5c0ec.png'
---

<div>   
<br>Cilium 正式宣布发布 Cilium 1.12 版本。<br>
<br>Cilium 是云原生领域网络安全的事实标准，被 Adobe、Bell Canada、IKEA，以及许多 Kubernetes 托管平台（包括谷歌云和 AWS 的产品）所采用。Cilium 1.12 版本中的主要功能由 Datadog、F5、Form3、Isovalent、Microsoft、Seznam.cz、纽约时报等公司共同贡献。<br>
<br>随着该版本的发布，Cilium Service Mesh 成为服务网格的主要开源项目。作为第一款既可以为企业提供以 sidecar 的方式运行服务网格，也同时可以以无 sidecar 的方式运行服务网格的项目，大大提高了企业运行服务网格的灵活性，并提供了不同的控制平面选择。此外，该版本还直接将 Kubernetes Ingress controller 集成到 Cilium 中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220721/fb900fb8baee7f5654205fcc46b5c0ec.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220721/fb900fb8baee7f5654205fcc46b5c0ec.png" class="img-polaroid" title="01.png" alt="01.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>具有可选 Sidecars 的 Kubernetes 服务网格项目</h3>Cilium Service Mesh 的愿景是使用 Kubernetes 的原生资源构建服务网格，就像 Cilium 的 ClusterMesh 一样，使用 Kubernetes 的 Services 和 NetworkPolicy 来执行多集群连接。今天，我们正式宣布，以无 sidecar 的方式运行服务网格的第一个稳定版发布，同时支持各种不同的控制平面选项。它补充了现有的基于 sidecar 的服务网格，即 Istio，目前 Istio 也是 Cilium 的一部分。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220721/dd51742d6b1aaeded8028ddc3a59dacf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220721/dd51742d6b1aaeded8028ddc3a59dacf.png" class="img-polaroid" title="02.png" alt="02.png" referrerpolicy="no-referrer"></a>
</div>
<br>
因此，我们的目标是通过为用户提供各种选择，来降低企业适配服务网格的复杂性。用户可以根据其独特的需求，选择最能满足其平台需求的方案，决定采用带 sidecar 或者不带 sidecar 的服务网格。<br>
<br>Cilium 的创始人 Thomas Graf 说：“Cilium Service Mesh 的宗旨是把选择权交给客户”。“客户希望能够在 sidecar 模式和无 sidecar 模式之间灵活做选择，希望有一个由 eBPF 和 Envoy 支持的高性能数据平面，使他们能够为自己的用例选择最佳的控制平面。将 Envoy 与eBPF 相结合，Cilium Service Mesh 可以为客户提供尽可能最佳的服务网格性能。”<br>
<br>随着新版本的发布，Cilium Service Mesh 还引入了 CiliumEnvoyConfig（CEC），以使用 Kubernetes 自定义资源（CRD）的方式跟 Envoy 集成，满足 L7 的各种高级用例，并且使得 Envoy 的完整功能集都可供用户使用。在下一个版本中，Cilium Service Mesh 还将增加对其他 Service Mesh 控制平面的支持，首先是网关 API 及其针对 Service Mesh 用例的 GAMMA 倡议。这将使 Cilium 服务网格数据平面与已迁移到网关 API 的服务网格（如 Istio）兼容。<br>
<h3>Cilium 1.12 的其他主要功能</h3>除了 Cilium Service Mesh 之外，Cilium 1.12 还提供了许多其他新功能：<br>
<ul><li><strong>完全兼容 Ingress Controller</strong>：除了新的无 sidecar 服务网格选项外，Cilium 1.12 还将 Kubernetes Ingress Controller 直接嵌入到 Cilium 中。</li><li><strong>ClusterMesh增强功能，包括服务亲和性</strong>：在 Cilium 1.12 中，ClusterMesh 可以将运行在多个集群上的服务视为一个全局服务，并考虑亲和性。根据服务亲和性，服务可以将本地或远程集群中的端点作为首选端点。</li><li><strong>出口网关和对外部工作负载的额外支持</strong>：出口网关（Egress Gateway），以前作为测试版功能引入，现在已达到稳定版要求。Cilium 允许用户将连接通过特定的网关节点转发到外部工作负载，用可预测的IP地址伪装连接，允许连接可以通过防火墙。当与ClusterMesh 结合使用时，允许外部工作负载的请求进入网格中的集群。</li><li><strong>发布 Cilium Tetragon</strong>：新的 Cilium Tetragon 组件支持强大的基于 eBPF 的实时安全观察能力和运行时强制执行。Tetragon 检测并能够对重要的安全事件做出反应，例如进程执行事件、系统调用活动和 I/O 活动，包括网络和文件访问。</li><li><strong>其他增强</strong>：额外的网络可见性控制、将 Cilium 作为非特权容器运行的能力、pod CIDR 的动态分配、IPv4/IPv6 NAT、AWS ENI prefix delegation 等等。</li></ul><br>
<br><strong>原文链接：<a href="https://www.cncf.io/blog/2022/07/20/cilium-1-12-ga-cilium-service-mesh-and-other-major-new-features-for-enterprise-kubernetes/">Cilium 1.12 GA: Cilium Service Mesh and other major new features for enterprise Kubernetes</a>  （翻译：钟涛）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            