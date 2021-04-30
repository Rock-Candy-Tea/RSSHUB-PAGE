
---
title: 'KubeSphere 3.1.0 GA：混合多云走向边缘，让应用无处不在'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f837d6bcd1f971b441576fbb27a1be07f1c.png'
author: 开源中国
comments: false
date: Fri, 30 Apr 2021 07:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f837d6bcd1f971b441576fbb27a1be07f1c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-f837d6bcd1f971b441576fbb27a1be07f1c.png" referrerpolicy="no-referrer"></p> 
<p>2021 年 4 月 29 日，KubeSphere 开源社区激动地向大家宣布，KubeSphere 3.1.0 正式发布！为了帮助企业最大化资源利用效率，KubeSphere 打造了一个以 Kubernetes 为内核的云原生分布式操作系统，提供可插拔的开放式架构，无缝对接第三方应用，极大地降低了企业用户的使用门槛。</p> 
<p>KubeSphere v3.1.0 主打 <strong>“延伸至边缘侧的容器混合云”</strong>，新增了对 <strong>“边缘计算”</strong> 场景的支持。同时在 v3.0.0 的基础上新增了 <strong>计量计费</strong>，让基础设施的运营成本更清晰，并进一步优化了在 <strong>“多云、多集群、多团队、多租户”</strong> 等应用场景下的使用体验，增强了 <strong>“多集群管理、多租户管理、可观测性、DevOps、应用商店、微服务治理”</strong> 等特性，更进一步完善交互设计提升了用户体验。</p> 
<p>云原生产业联盟撰写的《云原生发展白皮书》提到，万物互联时代加速了云-边协同的需求演进，传统云计算中心集中存储、计算的模式已经无法满足终端设备对于时效、容量、算力的需求，向边缘下沉并通过中心进行统一交付、运维、管控，已经成为云计算的重要发展趋势。</p> 
<p>面对这一发展趋势，KubeSphere 与 KubeEdge 社区紧密合作，将 Kubernetes 从云端扩展至边缘，以统一的标准实现了对边缘基础设施的纳管。通过与 KubeEdge 集成，解决了边缘节点纳管、边缘工作负载调度和边缘可观测性等难题，结合 KubeSphere 已有的多集群管理将混合多云管理延伸至边缘侧。</p> 
<p>并且，v3.1.0 得到了来自青云 QingCloud 之外的更多企业与用户的贡献和参与，无论是功能开发、功能测试、缺陷报告、需求建议、企业最佳实践，还是提供 Bug 修复、国际化翻译、文档贡献，这些来自开源社区的贡献都为 v3.1.0 的发布和推广提供了极大的帮助，我们将在文末予以特别致谢！</p> 
<h2>解读 v3.1.0 重大更新</h2> 
<p>KubeSphere 3.1.0 增加了计量计费功能，支持集群、企业空间的多层级与多租户在应用资源消耗的计量与统计。通过集成 KubeEdge，实现应用快速分发至边缘节点。同时还提供了更强大的可观测性能力，如兼容 PromQL、内置主流告警规则、可视化对接钉钉、企业微信、Slack 和 Webhook 等通知渠道。DevOps 的易用性在 3.1.0 也上了一个台阶，例如内置多套常用流水线模板，支持多分支流水线和流水线复制等，关于重大更新详情请查看文末海报。</p> 
<h2>多维度计量计费，让 K8s 运营成本更透明</h2> 
<p>在企业运营和管理 Kubernetes 容器平台时，通常需要分析资源消耗，查看集群及其中租户的消费账单，洞察资源使用情况，分析基础设施运营成本。</p> 
<p>在 KubeSphere 3.1.0 中，可从多个维度来分析平台资源消耗：</p> 
<ul> 
 <li> <p>从集群维度，可查看每个集群资源消耗，深入到节点中分析运行的工作负载，精准规划每个节点中工作负载的资源使用状况。</p> </li> 
 <li> <p>从企业空间维度，可查看每个企业空间资源消耗，获取企业空间中项目、应用、工作负载的消费账单，分析多租户环境中各个租户的资源使用是否合理。</p> </li> 
</ul> 
<p>另外，除了可以通过界面查看和导出数据，KubeSphere 计量计费平台也提供了所有操作的 API。接下来在后续的版本里，会持续加强并构筑端到端完整的计量计费可运营系统。</p> 
<h2>边缘节点管理</h2> 
<p>KubeEdge 是一个开源的边缘计算平台，它在 Kubernetes 原生的容器编排和调度能力之上，实现了 <strong>云边协同</strong>、<strong>计算下沉</strong>、<strong>海量边缘设备管理</strong>、<strong>边缘自治</strong> 等能力。但 KubeEdge 缺少云端控制层面的支持，如果将 KubeSphere 与 KubeEdge 相结合，可以很好解决这一问题，实现应用与工作负载在云端与边缘节点进行统一分发与管理。</p> 
<p>这一设想在 v3.1.0 中得以实现，KubeSphere 现已支持 KubeEdge 边缘节点纳管、KubeEdge 云端组件的安装部署、以及边缘节点的日志和监控数据采集与展示。结合 KubeEdge 的边缘自治功能和 KubeSphere 的多云与多集群管理功能，可以实现云-边-端一体化管控，解决在海量边、端设备上统一完成应用交付、运维、管控的需求。</p> 
<h2>强化微服务治理能力</h2> 
<p>KubeSphere 基于 Istio 提供了金丝雀发布、蓝绿部署、熔断等流量治理功能，同时还支持可视化呈现微服务之间的拓扑关系，并提供细粒度的监控数据。在分布式链路追踪方面，KubeSphere 基于 Jaeger 让用户快速追踪微服务之间的通讯情况，从而更易于了解微服务的请求延迟、性能瓶颈、序列化和并行调用等。</p> 
<p>KubeSphere 3.1.0 对微服务治理功能进行了强化，将 Istio 升级到了 1.6.10，支持图形化流量方向检测，图像化方式显示应用流量的流入/流出。同时还支持对 Nginx Ingress Gateway 进行监控，新增 Nginx Ingress Controller 的监控指标。</p> 
<h2>多云与多集群管理</h2> 
<p>虽然 KubeSphere 3.0.0 带来的多云与多集群管理提供了面向多个 Kubernetes 集群的中央控制面板，实现了应用跨云和跨集群的部署与运维，但 member 集群管理服务依赖 Redis、OpenLDAP、Prometheus 等组件，不适合轻量化部署。KubeSphere 3.1.0 移除了这些依赖组件，使 member 集群管理服务更加轻量化，并重构了集群控制器，支持以高可用方式运行 Tower 代理服务。</p> 
<h2>更强大的可观测性</h2> 
<p>可观测性是容器云平台非常关键的一环，狭义上主要包含监控、日志和追踪等，广义上还包括告警、事件、审计等。3.1.0 除了对已有的监控、日志、告警等功能进行优化升级，还新增了更多新特性。</p> 
<ul> 
 <li> <p>监控：支持图形化方式配置 <code>ServiceMonitor</code>，添加集群层级的自定义监控，同时还实现了类似于 Grafana 的 PromQL 语法高亮。</p> </li> 
 <li> <p>告警：在 v3.1.0 进行了架构调整，不再使用 MySQL、Redis 和 etcd 等组件以及旧版告警规则格式，改为使用 Thanos Ruler 配合 Prometheus 内置告警规则进行告警管理，兼容 Prometheus 告警规则。</p> </li> 
 <li> <p>通知管理：完成架构调整，与自研 Notification Manager v1.0.0 的全面集成，实现了以图形化界面的方式对接邮件、钉钉、企业微信、Slack、Webhook 等通知渠道。</p> </li> 
 <li> <p>日志：新增了对 Loki 的支持，可以将日志输出到 Loki。还新增了对 kubelet/docker/containerd 的日志收集。</p> </li> 
</ul> 
<h2>更易用的 DevOps</h2> 
<p>KubeSphere 3.1.0 新增了 GitLab 多分支流水线和流水线克隆等功能，并内置了常用的流水线模板，帮助 DevOps 工程师提升 CI/CD 流水线的创建与运维效率。大部分场景下可基于流水线模板进行修改，不再需要从头开始创建，实现了真正的开箱即用。</p> 
<h2>灵活可插拔的集群安装工具</h2> 
<p>KubeKey 不仅支持 Kubernetes 1.17 ~ 1.20 在 AMD 64 与 ARM 64 的安装，还支持了 K3s。并且，Kubekey 还新增支持 Cilium、Kube-OVN 等网络插件。鉴于 Dockershim 在 K8s 1.20 中被废弃，Kubekey 可用于部署 containerd、CRI-O、iSula 等容器运行时，让用户按需快速创建集群。</p> 
<h2>运维友好的网络管理</h2> 
<p>KubeSphere 将 IaaS 云平台强大的网络能力继承到容器云平台，让用户在 Kubernetes 之上获得与 IaaS 一样稳定、安全和易用的网络使用体验。v3.1.0 新增了网络可视化拓扑图，你可以通过拓扑图洞悉各个服务之间的网络调用关系。</p> 
<p>鉴于 Calico 是目前最常用的 Kubernetes CNI 插件之一，v3.1.0 现已支持 Calico IP 池管理，也可以为 Deployment 指定静态 IP。此外，v3.1.0 还新增了对 Kube-OVN 插件的支持。</p> 
<h2>完全开源：社区化与国际化</h2> 
<p>借助于开源社区的力量，KubeSphere 迅速走向全球，目前 KubeSphere 在全球的 90 多个国家和地区有超过 10w 下载量。v3.1.0 Console 支持中、英、繁中和西班牙语，KubeSphere 未来将进一步拓展海外市场。</p> 
<p>KubeSphere 3.1.0 将继续秉承 100% 开源的承诺，3.0.0 版本带来的诸多新功能也早已在 GitHub 开源，例如 Porter、OpenPitrix、Fluentbit Operator、 KubeKey、KubeEye、Notification Manager、Kube-Events，还开源了一套前端组件库 Kube Design，这些新特性的代码与设计文档在 GitHub 相关仓库都可以找到，欢迎大家在 GitHub 给我们 Star + Fork + PR 三连。</p> 
<h2>3.1.0 重要更新一览</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5f18855029a8b968758c683728616d3defa.png" referrerpolicy="no-referrer"></p> 
<h2>安装升级</h2> 
<p>KubeSphere 已将 v3.1.0 所有镜像在国内镜像仓库进行了同步与备份，国内用户下载镜像的安装体验会更加友好。关于最新的 v3.1.0 安装与升级指南，可参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubesphere.io%2Fdocs" target="_blank"> KubeSphere 官方文档</a>。</p> 
<h2>致谢</h2> 
<p>以下为 KubeSphere 3.1.0 主要仓库贡献者的 GitHub ID，排名不分先后：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a0ba747200f9d1405c6648387122b5f10ed.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            