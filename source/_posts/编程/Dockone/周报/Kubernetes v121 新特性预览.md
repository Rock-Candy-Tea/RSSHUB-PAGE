
---
title: 'Kubernetes v1.21 新特性预览'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210330/b2e4d031e8cd882ebddb3ac913b796a8.png'
author: Dockone
comments: false
date: 2021-04-03 00:25:24
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210330/b2e4d031e8cd882ebddb3ac913b796a8.png'
---

<div>   
<br>Kubernetes v1.21 下个月就要发布了（v1.21.0 将于 4 月 8 日发布），本文梳理该版本带来的新特性，以便你为下个月的升级做好准备。<br>
<h4>PodSecurityPolicy 弃用</h4>PodSecurityPolicy（PSP）是 Kubernetes 1.8 开始就支持的 Beta 特性，大量应用于容器的安全策略控制。但由于其 API 不够灵活、认证模型不够完善且配置更新繁琐等缺陷，PodSecurityPolicy 将<a href="http://weekly.dockone.io/_https://github.com/kubernetes/kubernetes/pull/97171_">在 v1.21 正式弃用</a>，并将在 v1.25 中从代码库中删除。已经使用 PodSecurityPolicy 的用户建议迁移到  <a href="http://weekly.dockone.io/_https://github.com/open-policy-agent/gatekeeper_">Gatekeeper</a>。<br>
<h4>不可变 ConfigMap/Secret 进入稳定版</h4>当集群包含大量 ConfigMap 和 Secret 时，大量的 watch 事件会急剧增加 kube-apiserver 的负载，并会导致错误配置过快传播到整个集群。在这种情况中，给不需要经常修改的 ConfigMap 和 Secret 设置  <code class="prettyprint">immutable: true</code>  就可以避免类似的问题。<br>
<br>注意，设置  <code class="prettyprint">immutable: true</code>  之后，ConfigMap 和 Secret 内容更新时需要删除并重新创建，且使用它们的 Pod 也需要删除重建。<br>
<h4>IPv4/IPv6 双栈支持 Beta</h4>IPv4/IPv6 双栈支持在 v1.20 的时候进行了重构，并将于 v1.21 中进入 Beta 版本（默认开启），kubeadm 也已经支持创建 IPv4/IPv6 双栈集群。该特性开启后，Kubernetes Service 和 Pod 会同时分配 IPv4 和 IPv6 两个地址。<br>
<br>注意，如果使用了 CNI 插件和云服务商扩展（Cloud Provider），CNI 插件和云服务商扩展也需要支持 IPv4/IPv6 双栈。<br>
<h4>CSIVolumeHealth Alpha 和 CSIStorageCapacity Beta</h4>从 v1.21 开始，Kubernetes 支持 CSI 存储插件的 Volume 健康检查（Alpha 版），CSI 插件需要实现外部健康监控控制器。当 Volume 或者 Node 出现异常时，该控制器会向 Volume 所属的 PVC 以及使用该 PVC 的 Pod 发送一个异常事件。<br>
<br>CSIStorageCapacity 用于跟踪 CSI 存储容量并确保 Pod 调度到足够存储容量的节点上。该特性从 v1.21 开始进入 Beta 阶段，并默认开启。注意，使用该特性需要 CSI 驱动程序实现对应的接口。<br>
<h4>TTL 控制器 Beta</h4>TTL 控制器用来自动清理已经结束的 Pod，如处于 Complete 或 Failed 状态的 Job。Pod 停止之后的 TTL 可以通过  <code class="prettyprint">.spec.ttlSecondsAfterFinished</code>  来设置。<br>
<br>注意，该特性要求集群中各节点（包括控制节点）的时间一致，比如在所有节点中运行 NTP 服务。<br>
<h4>GenericEphemeralVolume Beta</h4>通用临时卷（GenericEphemeralVolume）类似于 emptyDir 卷，但它更加灵活：<br>
<ul><li>存储可以是本地的，也可以是网络存储。    </li><li>卷可以有固定的大小，Pod 不能超量使用。    </li><li>卷可能有一些初始数据，这取决于驱动程序和参数。    </li><li>当驱动程序支持，卷上的典型操作（如快照、克隆、扩展等）也被支持。</li></ul><br>
<br><h4>Kubelet 内存控制策略 Alpha</h4>内存控制策略是 Kubelet 在 v1.21 中新增的一个 Alpha 特性，用于为 Pod 提供 NUMA 内存。Kubelet 新增了  <code class="prettyprint">--memory-manager-policy</code>  用于配置内存控制策略，它支持两个策略：<br>
<ul><li>默认策略是 none，等同于内存控制策略未开启；  </li><li>static 策略：为 Pod 分配 NUMA 内存并确保 Guaranteed Pod 预留足够的内存（Kubelet 状态保存在  <code class="prettyprint">/var/lib/kubelet/memory_manager_state</code>  文件中）。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210330/b2e4d031e8cd882ebddb3ac913b796a8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210330/b2e4d031e8cd882ebddb3ac913b796a8.png" class="img-polaroid" title="001.png" alt="001.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>ServiceLoadBalancerClass Alpha</h4>以前 LoadBalancer 类型的服务都需要云服务商扩展（Cloud Provider）去配置云上负载均衡器，并且整个集群中只能运行一个 Cloud Provider。Kubernetes v1.21 新增的 ServiceLoadBalancerClass 特性允许一个集群中运行多个负载均衡器的实现，而 Service 可以通过  <code class="prettyprint">spec.loadBalancerClass</code>  指定使用哪个具体实现（类似于 Ingress Controller）。<br>
<h4>PodDeletionCost Alpha</h4>以前从 ReplicaSet 删除 Pod 时只能设置副本数量而不能指定要删除的 Pod，而 Kubernetes v1.21 新增的 PodDeletionCost 特性允许用户设置哪些 Pod 优先删除。使用该特性时需要给 Pod 增加一个 annotation  <code class="prettyprint">controller.kubernetes.io/pod-deletion-cost</code>，其值表示删除一个 Pod 的成本，值越小代表越优先删除。当 annotation 不存在时，表示其删除成本为 0。<br>
<h4>Indexed Jobs Alpha</h4>通常，当使用 Job 来运行分布式任务时，用户需要一个单独的系统来在 Job 的不同 worker Pod 之间分配任务。比如，设置一个工作队列，逐一给每个 Pod 分配任务。Kubernetes v1.21 新增的 Indexed Job 会给每个任务分配一个数值索引，并通过 annotation  <code class="prettyprint">batch.kubernetes.io/job-completion-index</code>  暴露给每个 Pod。使用方法为在 Job spec 中设置  <code class="prettyprint">completionMode: Indexed</code>。<br>
<h4>TopologyAwareHints Alpha</h4>服务拓扑（Service Topology）在 Kubernetes v1.21 中已弃用，并将在 v1.22 中删除。Kubernetes v1.21 新增的拓扑感知提示提供了类似的功能。该特性开启后，EndpointSlice 控制器将填充 EndpointSlice 中每个 Endpoint 上的提示字段，以将其分配到一个区域。然后，诸如 kube-proxy 这样的组件在配置请求路由时就可以使用这些提示。<br>
<h4>其他需要留意的新特性</h4><ul><li>CronJob 进入稳定版本，已有用户注意切换 API 版本到  <code class="prettyprint">apiVersion: batch/v1</code>。    </li><li>Sysctls 进入稳定版本，用户终于有一个稳定的 API 来配置 Sysctl 了。</li><li>Pod disruption budgets（PDB）进入稳定版本，已有用户注意切换 API 版本到  <code class="prettyprint">apiVersion: policy/v1</code>。</li><li>RootCAConfigMap 进入稳定版本，kube-controller-manager 将会在每个 namespace 发布一个名为  <code class="prettyprint">kube-root-ca.crt</code>  的 ConfigMap，内容是 ca.crt，可用来验证 Kubernetes API 连接。</li><li>EndpointSlice 进入稳定版本，已有用户注意切换 API 版本到  <code class="prettyprint">apiVersion: discovery.k8s.io/v1</code>。</li><li>ServiceAccountIssuerDiscovery 进入稳定版本，该特性使得用户能够用联邦的方式结合使用 Kubernetes 集群（_Identity Provider_，标识提供者）与外部系统（_relying parties_， 依赖方）所分发的服务账号令牌。</li><li>CRIContainerLogRotation 进入稳定版本，kubelet 将会自动为 containerd 等 CRI 容器运行时轮换日志。</li><li>结构化日志（Structured Logging）进入 Beta，很多组件的日志都改成以 JSON 格式记录，这样第三方日志处理系统就可以方便地从日志中解析出日志所对应的资源对象和资源属性。</li><li>EfficientWatchResumption 进入 Beta，kube-apiserver 重启后 watch 缓存将更高效的恢复，更好的支持大规模集群。</li><li>CSIServiceAccountToken 进入 Beta，使得 CSI 驱动程序可以获取 Pod 的 service account token。</li><li>GracefulNodeShutdown 进入 Beta，Kubelet 将会检测 Node 的状态并在 Node 关闭前终止其上运行的 Pod（使用前需要配置 ShutdownGracePeriod 和 ShutdownGracePeriodCriticalPods）。</li><li>Network Policy 支持设置端口范围（port 和 endPort），大量端口时不再需要每个端口单独列出。</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/N1IRbNGZ2wTRuCeGz1I4HQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/N1IRbNGZ2wTRuCeGz1I4HQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            