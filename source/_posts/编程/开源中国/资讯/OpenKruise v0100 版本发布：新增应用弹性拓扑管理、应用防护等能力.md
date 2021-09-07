
---
title: 'OpenKruise v0.10.0 版本发布：新增应用弹性拓扑管理、应用防护等能力'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3971'
author: 开源中国
comments: false
date: Tue, 07 Sep 2021 08:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3971'
---

<div>   
<div class="content">
                                                                                            <h3><strong>1 背景</strong></h3> 
<p>阿里云开源的云原生应用自动化管理套件、CNCF Sandbox 项目 -- OpenKruise，今天发布 v0.10.0 新版本，这也会是 OpenKruise v1.0 之前的最后一个 minor 版本。</p> 
<p>本文将带你一览 v0.10.0 的新变化，其中新增的 WorkloadSpread、PodUnavailableBudget 等大颗粒特性后续还将有转文详细介绍其设计实现原理。</p> 
<h3><strong>2 新功能概览</strong></h3> 
<h4><strong>1.  WorkloadSpread：旁路的应用弹性拓扑管理能力</strong></h4> 
<p>在应用部署运维的场景下，有着多种多样的拓扑打散以及弹性的诉求。其中最常见、最基本的，就是按某种或几种拓扑水平打散，比如：</p> 
<ul> 
 <li> <p>应用部署需要按 node 维度打散，避免堆叠（提高容灾能力）</p> </li> 
 <li> <p>应用部署需要按 AZ（available zone）维度打散（提高容灾能力）</p> </li> 
</ul> 
<p>这些基本的诉求，通过 Kubernetes 原生提供的 pod affinity、topology spread constraints 等能力目前都能够满足了。但在实际的生产场景下，还有着太多更加复杂的分区与弹性需求，以下举一些实际的例子：</p> 
<ul> 
 <li> <p>按 zone 打散时，需要指定在不同 zone 中部署的比例数，比如某个应用在 zone a、b、c 中部署的 Pod 数量比例为 1 : 1 : 2 等（由于一些现实的原因比如该应用在多个 zone 中的流量不均衡等）</p> </li> 
 <li> <p>存在多个 zone 或不同机型的拓扑，应用扩容时，优先部署到某个 zone 或机型上，当资源不足时再部署到另一个 zone 或机型上（往后以此类推）；应用缩容时，要按反向顺序，优先缩容后面 zone 或机型上的 Pod（往前以此类推）</p> </li> 
 <li> <p>存在多个基础的节点池和弹性的节点池，应用部署时需要固定数量或比例的 Pod 部署在基础节点池，其余的都扩到弹性节点池</p> </li> 
</ul> 
<p>对于这些例子，过去一般只能将一个应用拆分为多个 Workload（比如 Deployment）来部署，才能解决应用在不同拓扑下采用不同比例数量、扩缩容优先级、资源感知、弹性选择等场景的基本问题，但还是需要 PaaS 层深度定制化，来支持对一个应用多个 Workload 的精细化管理。</p> 
<p>针对这些问题，在 Kruise v0.10.0 版本中新增了 WorkloadSpread 资源，目前它支持配合 Deployment、ReplicaSet、CloneSet 这些 Workload 类型，来管理它们下属 Pod 的分区与弹性拓扑。</p> 
<p>以下是一个简化的例子：</p> 
<pre><code>apiVersion: apps.kruise.io/v1alpha1</code><code>kind: WorkloadSpread</code><code>metadata:</code><code>  name: workloadspread-demo</code><code>spec:</code><code>  targetRef:</code><code>    apiVersion: apps/v1 | apps.kruise.io/v1alpha1</code><code>    kind: Deployment | CloneSet</code><code>    name: workload-xxx</code><code>  subsets:</code><code>  - name: subset-a</code><code>    requiredNodeSelectorTerm:</code><code>      matchExpressions:</code><code>      - key: topology.kubernetes.io/zone</code><code>        operator: In</code><code>        values:</code><code>        - zone-a</code><code>    maxReplicas: 10 | 30%</code><code>  - name: subset-b</code><code>    requiredNodeSelectorTerm:</code><code>      matchExpressions:</code><code>      - key: topology.kubernetes.io/zone</code><code>        operator: In</code><code>        values:</code><code>        - zone-b</code></pre> 
<p>创建这个 WorkloadSpread 可以通过 targetRef 关联到一个 Workload 对象上，然后这个 Workload 在扩容 pod 的过程中，Pod 会被 Kruise 按上述策略注入对应的拓扑规则。这是一种旁路的注入和管理方式，本身不会干涉 Workload 对 Pod 的扩缩容、发布管理。</p> 
<p>注意：WorkloadSpread 对 Pod 缩容的优先级控制是通过 Pod Deletion Cost 来实现的：</p> 
<ul> 
 <li> <p>如果 Workload 类型是 CloneSet，则已经支持了这个 feature，可以实现缩容优先级</p> </li> 
 <li> <p>如果 Workload 类型是 Deployment/ReplicaSet，则要求 Kubernetes version >= 1.21，且在 1.21 中要在 kube-controller-manager 上开启 PodDeletionCost 这个 feature-gate</p> </li> 
</ul> 
<p>使用 WorkloadSpread 功能，需要在 安装/升级 Kruise v0.10.0 的时候打开 WorkloadSpread 这个 feature-gate。</p> 
<p>上述例子仅为最简化配置，更多使用说明请参考 官网文档，具体的实现原理我们将会在后续的文章中与大家分享。</p> 
<h4><strong>2.  PodUnavailableBudget：应用可用性防护</strong></h4> 
<p>在诸多 Voluntary Disruption 场景中 Kubernetes 原生提供的 Pod Disruption Budget（PDB） 通过限制同时中断的 Pod 数量，来保证应用的高可用性。</p> 
<p>但还有很多场景中，即便有 PDB 防护依然将会导致业务中断、服务降级，比如：</p> 
<ul> 
 <li> <p>应用 owner 通过 Deployment 正在进行版本升级，与此同时集群管理员由于机器资源利用率过低正在进行 node 缩容</p> </li> 
</ul> 
<ul> 
 <li> <p>中间件团队利用 SidecarSet 正在原地升级集群中的sidecar版本（例如：ServiceMesh envoy），同时HPA正在对同一批应用进行缩容</p> </li> 
 <li> <p>应用 owner 和中间件团队利用 CloneSet、SidecarSet 原地升级的能力，正在对同一批 Pod 进行升级</p> </li> 
</ul> 
<p>这其实很好理解 -- PDB 只能防控通过 Eviction API 来触发的 Pod 驱逐（例如 kubectl drain驱逐node上面的所有Pod），但是对于 Pod 删除、原地升级 等很多操作是无法防护的。</p> 
<p>在 Kruise v0.10.0 版本中新增的 PodUnavailableBudget（PUB）功能，则是对原生 PDB 的强化扩展。它包含了 PDB 自身的能力，并在此基础上增加了对更多 Voluntary Disruption 操作的防护，包括但不限于 Pod 删除、原地升级等。​​​​​​​</p> 
<pre><code>apiVersion: apps.kruise.io/v1alpha1</code><code>kind: PodUnavailableBudget</code><code>metadata:</code><code>  name: web-server-pub</code><code>  namespace: web</code><code>spec:</code><code>  targetRef:</code><code>    apiVersion: apps/v1 | apps.kruise.io/v1alpha1</code><code>    kind: Deployment | CloneSet | StatefulSet | ...</code><code>    name: web-server</code><code>  # selector 与 targetRef 二选一配置</code><code># selector:</code><code>#   matchLabels:</code><code>#     app: web-server</code><code>  # 保证的最大不可用数量</code><code>  maxUnavailable: 60%</code><code>  # 保证的最小可用数量</code><code># minAvailable: 40%</code></pre> 
<p>使用 PodUnavailableBudget 功能，需要在 安装/升级 Kruise v0.10.0 的时候打开feature-gate（两个可以选择打开一个，也可以都打开）：</p> 
<ul> 
 <li> <p>PodUnavailableBudgetDeleteGate：拦截防护 Pod 删除、驱逐等操作</p> </li> 
 <li> <p>PodUnavailableBudgetUpdateGate：拦截防护 Pod 原地升级等更新操作</p> </li> 
</ul> 
<p>更多使用说明请参考 官网文档，具体的实现原理我们将会在后续的文章中与大家分享。</p> 
<h4><strong>3.  CloneSet 支持按拓扑规则缩容</strong></h4> 
<p>在 CloneSet 缩容（调小 replicas 数量）的时候，选择哪些 Pod 删除是有一套固定算法排序的：</p> 
<ol> 
 <li> <p>未调度 < 已调度</p> </li> 
 <li> <p>PodPending < PodUnknown < PodRunning</p> </li> 
</ol> 
<ol start="3"> 
 <li> <p>Not ready < ready</p> </li> 
 <li> <p><strong>较小 pod-deletion cost < 较大 pod-deletion cost</strong></p> </li> 
</ol> 
<ol start="5"> 
 <li> <p><strong>较大打散权重 < 较小</strong></p> </li> 
 <li> <p>处于 Ready 时间较短 < 较长</p> </li> 
</ol> 
<ol start="7"> 
 <li> <p>容器重启次数较多 < 较少</p> </li> 
 <li> <p>创建时间较短 < 较长</p> </li> 
</ol> 
<p>其中，“4” 是在 Kruise v0.9.0 中开始提供的特性，用于支持用户指定删除顺序（WorkloadSpread 就是利用这个功能实现缩容优先级）；<strong>而 “5” 则是当前 v0.10.0 提供的特性，即在缩容的时候会参考应用的拓扑打散来排序。</strong></p> 
<ul> 
 <li> <p>如果应用配置了 topology spread constraints ，则 CloneSet 缩容时会按照其中的 topology 维度打散来选择 Pod 删除（比如尽量打平多个 zone 上部署 Pod 的数量）</p> </li> 
 <li> <p>如果应用没有配置 topology spread constraints ，则默认情况下 CloneSet 缩容时会按照 node 节点维度打散来选择 Pod 删除（尽量减少同 node 上的堆叠数量）</p> </li> 
</ul> 
<h4><strong>4.  Advanced StatefulSet 支持流式扩容</strong></h4> 
<p>为了避免在一个新 Advanced StatefulSet 创建后有大量失败的 pod 被创建出来，从 Kruise v0.10.0 版本开始引入了在 scale strategy 中的 maxUnavailable 策略：​​​​​​​</p> 
<pre><code>apiVersion: apps.kruise.io/v1beta1</code><code>kind: StatefulSet</code><code>spec:</code><code>  # ...</code><code>  replicas: 100</code><code>  scaleStrategy:</code><code>    maxUnavailable: 10% # percentage or absolute number</code></pre> 
<p>当这个字段被设置之后，Advanced StatefulSet 会保证创建 pod 之后不可用 pod 数量不超过这个限制值。</p> 
<p>比如说，上面这个 StatefulSet 一开始只会一次性创建 10 个 pod。在此之后，每当一个 pod 变为 running、ready 状态后，才会再创建一个新 pod 出来。</p> 
<p>注意：这个功能只允许在 podManagementPolicy 是 `Parallel` 的 StatefulSet 中使用。</p> 
<h4><strong>5.  其他</strong></h4> 
<p>除了上述内容外，还有一些变动如：</p> 
<ul> 
 <li> <p>SidecarSet 新增 imagePullSecrets、injectionStrategy.paused 等字段支持配置 sidecar 镜像拉取 secret 以及暂停注入</p> </li> 
 <li> <p>Advanced StatefulSet 支持配合原地升级的镜像提前预热</p> </li> 
</ul> 
<p>详见 ChangeLog 文档。</p> 
<h3><strong>3 最后</strong></h3> 
<p>本次的 v0.10.0 会是 OpenKruise v1.0 之前的最后一个 minor 版本，在年底之前 Kruise 将会发布首个 v1.0 大版本，敬请期待！</p> 
<p>另外，OpenKruise 社区开始组织定期的双周会，从本周四（9月9日）晚上19:00（ GMT+8 Asia/Shanghai）首次开始，本次周会将会讲解 v0.10.0 新版本的特性以及 demo 演示。参与方式：</p> 
<ul> 
 <li> <p>Zoom 会议链接（见文末链接）</p> </li> 
 <li> <p>加入 OpenKruise 社区交流群（钉钉搜群号 23330762 ），将会有群直播</p> </li> 
</ul> 
<p><strong><em>更多内容</em></strong></p> 
<p>OpenKruise：https://github.com/openkruise/kruise</p> 
<p>topology spread constraints：https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/</p> 
<p>Pod Deletion Cost：https://kubernetes.io/docs/reference/labels-annotations-taints/#pod-deletion-cost</p> 
<p>官网文档：https://openkruise.io/zh-cn/docs/workloadspread.html</p> 
<p>ChangeLog 文档：https://github.com/openkruise/kruise/blob/v0.10.0/CHANGELOG.md</p> 
<p>Zoom 会议链接：https://us02web.zoom.us/j/87059136652?pwd=NlI4UThFWXVRZkxIU0dtR1NINncrQT09</p> 
<p>Zoom 记录文档：https://shimo.im/docs/gXqmeQOYBehZ4vqo</p>
                                        </div>
                                      
</div>
            