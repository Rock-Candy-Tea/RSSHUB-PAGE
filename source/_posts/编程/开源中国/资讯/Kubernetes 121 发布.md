
---
title: 'Kubernetes 1.21 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4ac51f6989728df94e24491b42df7e19663.png'
author: 开源中国
comments: false
date: Sat, 10 Apr 2021 07:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4ac51f6989728df94e24491b42df7e19663.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2021%2F04%2F08%2Fkubernetes-1-21-release-announcement%2F" target="_blank">Kubernetes 1.21</a> 现已发布，这是 2021 年发布的首个版本。此版本共包含 51 项增强功能：其中，13 项增强功能已升级到稳定阶段，16 项增强功能转换为 Beta 版，20 项增强功能进入 alpha 版，还有 2 个功能被弃用。Kubernetes v1.21 发布周期历时 12 周（1 月 11 日-4 月 8 日），贡献者包括了 999 家公司以及 1279 位个人。</p> 
<p><img alt height="260" src="https://oscimg.oschina.net/oscnet/up-4ac51f6989728df94e24491b42df7e19663.png" width="250" referrerpolicy="no-referrer"></p> 
<p>此版本主要更新内容有：</p> 
<h4>Major Themes</h4> 
<ul> 
 <li><strong>CronJobs 达到稳定阶段</strong></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fworkloads%2Fcontrollers%2Fcron-jobs%2F" target="_blank">CronJobs</a>（以前称为 ScheduledJobs）自 Kubernetes 1.8 开始就进入了 beta 阶段。现在从 Kubernetes v1.21 开始，这个广泛使用的 API 则将进入稳定阶段。</p> 
<p>CronJob 用于执行定期的计划操作，如备份、报告生成等。所有这些任务中都应配置为无限期重复（如：每天/每周/每月一次）；用户可在该时间间隔内定义 job 应开始的时间点。</p> 
<ul> 
 <li><strong>不可变的 Secret 和 ConfigMap</strong></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fconfiguration%2Fsecret%2F%23secret-immutable" target="_blank">不可变的</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fconfiguration%2Fsecret%2F%23secret-immutable" target="_blank">Secrets</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fconfiguration%2Fconfigmap%2F%23configmap-immutable" target="_blank">ConfigMap</a> 向各自的资源类型中添加了新字段，确保新资源拒绝对这两种对象的更改。默认情况下，Secrets 和 ConfigMap 是可变的，这对于能够使用更改的 Pod 很有用。如果为使用 Secrets 和 ConfigMap 的 Pod 推送错误的配置，也会导致问题。</p> 
<p>通过将 Secrets 和 ConfigMaps 标记为不可变，可以确保用户的应用程序配置不会更改。如果要进行更改，则需要创建一个唯一已命名的 Secret 或 ConfigMap，并部署一个新的 Pod 来使用该资源。不可变的资源还具有扩展优势，因为 controller 不需要轮询 API 服务器来监视更改。</p> 
<p>该功能已在 Kubernetes 1.21 中达到稳定阶段。</p> 
<ul> 
 <li><strong>IPv4/IPv6 双协议栈支持</strong></li> 
</ul> 
<p>IP 地址是集群运维和管理员需要确保不会耗尽的一种消耗性资源。尤其是，公共 IPv4 地址现在很稀缺。具有双栈支持，可以将原生 IPv6 路由到 Pod 和 services，同时仍允许集群在需要的地方使用 IPv4。双栈集群网络还改善了工作负载的可能扩展限制。</p> 
<p>Kubernetes 中的双协议栈意味着 Pod、services 和节点可以获取 IPv4 地址和 IPv6 地址。在 Kubernetes 1.21 中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fservices-networking%2Fdual-stack%2F" target="_blank">，双栈网络</a>已从 alpha 升级到 beta，并且默认启用。</p> 
<ul> 
 <li><strong>优雅的节点关闭 </strong></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Farchitecture%2Fnodes%2F%23graceful-node-shutdown" target="_blank">优雅的节点关闭功能</a>在此版本中也已升级到 Beta 版（现在可供更多用户使用）。这是一项非常有用的功能，它使 kubelet 可以知道节点已关闭，并可以优雅地终止计划到该节点的 Pod。</p> 
<p>当前，当节点关闭时，Pod 不会遵循预期的终止生命周期，因此无法正常关闭，导致会给很多工作负载带来问题。展望未来，kubelet 将能够通过 systemd 检测即将发生的系统关闭，然后通知正在运行的 Pod，以便它们可以尽可能正常地终止。</p> 
<ul> 
 <li><strong>持久卷健康监控</strong></li> 
</ul> 
<p>持久卷（Persistent Volumes，PV）通常在应用程序中用于获取基于文件的本地存储。它们能以多种不同的方式使用，并可以帮助用户迁移应用程序而无需重新编写存储后端。</p> 
<p>Kubernetes v1.21 具有一项新的 alpha 功能，该功能可以监视 PV 的健康状况，并在 volume 变得不健康时进行相应标记。工作负载将能够对健康状况做出反应，以保护数据不会被从不健康的 volume 中写入或读取。</p> 
<ul> 
 <li><strong>减少 Kubernetes 的构建维护</strong></li> 
</ul> 
<p>以前，Kubernetes 维护了多个构建系统。对于新的和现有的贡献者来说，这通常是造成摩擦和复杂性的根源。</p> 
<p>在上一个发行周期中，已投入大量工作来简化构建过程，并在原生 Golang 构建工具上实现标准化。这应能使社区得到更广泛的维护，并降低新贡献者的进入门槛。</p> 
<h4>Major Changes</h4> 
<ul> 
 <li><strong>PodSecurityPolicy 弃用</strong></li> 
</ul> 
<p>在 Kubernetes 1.21 中，弃用 PodSecurityPolicy。与所有 Kubernetes 已弃用的功能一样，PodSecurityPolicy 将继续在多个版本中完整可用。作为此前的 beta 功能，PodSecurityPolicy 将在Kubernetes v1.25 中被删除。</p> 
<p>官方表示，其正开发一种新的内置机制来帮助限制 Pod 特权，名为“PSP Replacement Policy”。计划用这种新机制覆盖主要的 PodSecurityPolicy 用例，并大大改善可维护性。了解更多信息，可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2021%2F04%2F06%2Fpodsecuritypolicy-deprecation-past-present-and-future" target="_blank">PodSecurityPolicy Deprecation: Past, Present, and Future</a>。</p> 
<ul> 
 <li><strong>TopologyKeys 弃用</strong></li> 
</ul> 
<p>Service 字段 topologyKeys 现在已经被弃用；所有使用该字段的组件功能之前都是 alpha，现在也已弃用。开发团队表示，其已经用一种实现拓扑感知路由的方法取代了 topologyKeys，该方法名为拓扑感知提示（topology-aware hints）。目前，拓扑感知提示是 Kubernetes v1.21 中的一个 alpha 功能。</p> 
<h4>其他更新</h4> 
<p>进入稳定阶段的功能：</p> 
<ul> 
 <li> <p>EndpointSlice</p> </li> 
 <li> <p>新增 sysctl 支持</p> </li> 
 <li> <p>PodDisruptionBudgets</p> </li> 
</ul> 
<p>重要功能更新：</p> 
<ul> 
 <li> <p>External client-go credential providers：在 Kubernetes v1.21 中达到 beta 阶段；</p> </li> 
 <li> <p>Structured logging：将在 Kubernetes v1.22 中达到 beta 阶段；</p> </li> 
 <li> <p>TTL after finish cleanup for Jobs and Pods：在 Kubernetes v1.21 中达到 beta 阶段。</p> </li> 
</ul> 
<p>发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2021%2F04%2F08%2Fkubernetes-1-21-release-announcement%2F" target="_blank">https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/</a></p>
                                        </div>
                                      
</div>
            