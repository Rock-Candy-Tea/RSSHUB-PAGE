
---
title: '如何选择最佳的 Kubernetes 集群自动伸缩策略'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/4e2e55ab6044166d9b351d3efc27bfe7.jpg'
author: Dockone
comments: false
date: 2021-08-13 10:08:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/4e2e55ab6044166d9b351d3efc27bfe7.jpg'
---

<div>   
<br>这篇内容篇幅比较长，如果不想深入探讨或时间有限，这是全文简述：在默认设置下，扩展 Kubernetes 集群中的 Pod 和节点可能需要几分钟时间。了解如何调整集群节点的大小、配置水平和集群自动缩放器以及过度配置集群以加快扩展速度。<br>
<br>在 Kubernetes 中，自动伸缩功能包括：<br>
<ul><li>Pod 水平自动伸缩（Horizontal Pod Autoscaler，HPA）</li><li>Pod 垂直自动伸缩（Vertical Pod Autoscaler，VPA）</li><li>集群自动伸缩（Cluster Autoscaler，CA）</li></ul><br>
<br>这些自动伸缩组件属于不同的类别，关注点也不同。<br>
<br>Horizontal Pod Autoscaler 负责增加 Pod 的副本数量。随着你的应用接收到的流量越来越多，你可以让自动伸缩组件调整副本数量来处理更多的请求。<br>
<br>Vertical Pod Autoscaler 的使用场景是，当资源不足无法创建更多的 Pod 副本时，而又仍然需要处理更多的流量。一个简单的例子，你无法通过简单地添加更多的 Pod 副本来扩容数据库。数据库可能需要进行数据分片或者配置只读节点。但你可以通过增加内存和 CPU 资源来让数据库能够处理更多的连接数。这正是 VPA 的目的，增加 Pod 的资源大小。<br>
<br>最后，我们要说说集群自动伸缩组件了。当你的集群资源不足时，Cluster Autoscaler 会配置一个新的计算单元并将其添加到集群中。如果空节点过多，会移除它们以降低成本。<br>
<br>虽然这三个组件都 “自动伸缩” 了一些东西，但它们并不造成相互之间的干扰。它们各自都有自己使用场景，定义和工作机制。并且它们是在独立的项目中开发的，独立的使用。然而，更重要的是，为了最好的 scaling 你的集群，你必须花些心思去设置好这些 Autoscaler，让我们看个例子。<br>
<h3>当自动伸缩的 Pod 报错</h3>想象一下，有一个应用程序始终需要并使用 1.5GB 内存和 0.25 个 vCPU。你配置了一个具有 8GB 和 2 个 vCPU 的单个节点的集群 —— 它应该能够完美地容纳四个 Pod（并且还有一点额外的空间）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/4e2e55ab6044166d9b351d3efc27bfe7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/4e2e55ab6044166d9b351d3efc27bfe7.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
现在，你部署了一个 Pod 并且配置如下：<br>
<ol><li>HPA 配置每 10 个请求进来就添加一个 Pod 副本（例如：如果有 40 个并发请求涌入，会扩容到 4 个 Pod 副本）。</li><li>CA 配置在资源不足时，创建更多的 Node 节点。</li></ol><br>
<br><blockquote><br>HPA 可以通过在 deployment 文件中使用 Custom Metrics（例如在 Ingress Controller 中的 queries per second（QPS）） 来扩容 Pod 副本数量。</blockquote>现在，你开始为集群增加 30 个并发请求，并观察一下情况：<br>
<ol><li>HPA 开始扩容 Pod。</li><li>创建了两个 Pod 副本。</li><li>CA 没有触发 - 没有新增集群 Node 节点。</li></ol><br>
<br>这很好理解，因为现在有足够的内存和 CPU 资源来支持更多的 Pod。<br>
<br>你进一步将流量增加到 40 个并发请求，并再次观察：<br>
<ol><li>HPA 又创建了一个 Pod。</li><li>这个 Pod 是 pending 状态并且无法被部署。</li><li>CA 触发创建了一个新的 Node 节点。</li><li>新 Node 节点启动 4 分钟后开始工作。之后，pending Pod 也成功被部署了。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/cf592da59d184f9ee426d8d6e6634d64.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/cf592da59d184f9ee426d8d6e6634d64.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/803bb315621bd61ee8dd825e7365f89b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/803bb315621bd61ee8dd825e7365f89b.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
为什么第四个 Pod 没有部署在第一个 Node 节点上呢？<br>
<br>Pod 部署在集群上需要消耗内存，CPU，硬盘空间等资源，在同一个 Node 上，操作系统和 kubelet 组件也需要消耗内存和 CPU 资源。<br>
<br>Kubernetes 中一个 Worker Node 节点的内存和 CPU 等资源使用分布如下：<br>
<ol><li>需要运行操作系统和一些系统级的守护进程，例如 SSH，Systemd 等。</li><li>需要运行 Kubernetes Agent 组件，例如 Kubelet，Container Runtime，Node Problem Detector 等。</li><li>需要运行 Pod。</li><li>需要保留一些资源用来驱逐阀值之用。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/311933d44e843e0949b80b737a4c9606.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/311933d44e843e0949b80b737a4c9606.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
你猜的没错，所有这些配额都是可定制的，但你需要好好计算一下。<br>
<br>在一个 8GB 内存和 2vCPU 的单个节点的，可以按如下估算：<br>
<ul><li>操作系统运行大概需要 100MB 内存和 0.1vCPU。</li><li>kubelet 运行大概需要 1.8GB 内存和 0.07vCPU。</li><li>驱逐阀值大概需要 100MB 内存。</li></ul><br>
<br>剩余的大约 6GB 内存空间和 1.83vCPU 是提供给 Pod 使用的。<br>
<br>如果你的集群需要运行 DaemonSet 资源，像 kube-proxy，那么你应该进一步减少提供给 Pod 的资源。考虑到 kube-proxy 大概需要 128MB 内存和 0.1vCPU，那么剩余大约 5.9GB 内存空间和 1.73vCPU 是提供给 Pod 使用的。<br>
<br>另外，如果还需要运行 CNI 组件（例如：Flannel）和日志收集组件（Flentd），又会进一步减少提供给 Pod 的资源。<br>
<br>在统计完所有其他的资源占用情况后，集群的剩余空间就只够运行三个 Pod 了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/1eb75812338382b6475728be889492e6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/1eb75812338382b6475728be889492e6.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
所以第四个会一直保持 “pending” 状态，直到它被调度到其他的 Node 节点上。<br>
<br>既然 Cluster Autoscaler 知道没有空间容纳第四个 Pod，为什么不提前配置一个新节点？为什么它要在 Pod 处于 “pending” 状态之后再触发创建新 Node 节点的操作？<br>
<h3>Kubernetes 的 Cluster Autoscaler 是如何工作的</h3>Cluster Autoscaler 不是通过观察内存或 CPU 的使用情况来触发自动伸缩的。相反地，是通过对事件的响应和每 10s 对不可调度的 Pod 进行检查。<br>
<br>当 Scheduler 无法找到可以容纳它的 Node 节点时，Pod 就会变成不可调度状态。例如，当一个 Pod 需要 1vCPU 资源而集群只有 0.5vCPU 资源可用，Scheduler 就会把该 Pod 标记为不可调度状态。<br>
<br>这时，Cluster Autoscaler 会开始创建新 Node 节点。创建完成后，它会扫描集群中的不可调度状态的 Pod，检查是否可以将这些 Pod 调度到新节点上。<br>
<br>如果你的集群具有多种节点类型（通常也称为节点组或节点池），则 Cluster Autoscaler 将使用以下策略选择其中一种：<br>
<ul><li>Random - 随机选择一种节点类型（默认策略）。</li><li>Most Pods - 选择将调度最多 Pod 的节点组。</li><li>Least waste - 选择扩容后空闲 CPU 最少的节点组。</li><li>Price - 选择成本最低的节点组（目前仅适用于 GCP）。</li><li>Priority - 选择优先级最高的节点组（优先级可以手动设置）。</li></ul><br>
<br>一旦确定了节点类型，Cluster Autoscaler 将调用相关 API 来提供新的计算资源。<br>
<br>如果你使用的是 AWS，Cluster Autoscaler 将预置一个新的 EC2 实例。在 Azure 上，它将创建一个新的虚拟机，并在 GCP 上创建一个新的计算引擎。<br>
<br>创建的节点可能需要一些时间才能出现在 Kubernetes 中。计算资源准备就绪后，节点将被初始化并添加到可以部署未被调度 Pod 的集群中。<br>
<br>不幸的是，配置一个新节点通常会很慢。它可能会花费好几分钟来做这件事。<br>
<br>让我们来看看这几分钟到底干了什么。<br>
<h3>探索 Pod 自动伸缩前置期</h3>在新节点上创建新 Pod 所需的时间由四个主要因素决定：<br>
<ol><li>HPA 的反应时间。</li><li>CA 的反应时间。</li><li>Node 节点的反应时间。</li><li>Pod 创建的时间。</li></ol><br>
<br>默认地，kubelet 每 10 秒抓取一次 Pod 的 CPU 和内存使用情况。每分钟，Metrics Server 都会聚合这些指标并将它们发送给 Kubernetes API 的其他组件。<br>
<br>Horizontal Pod Autoscaler 控制器负责检查指标并决定扩大或缩小副本数量。<br>
<br>默认地，Horizontal Pod Autoscaler 每 15 秒检查一次 Pod 指标。<br>
<br>Cluster Autoscaler 每 10 秒检查一次集群中不可调度的 Pod。<br>
<br>一旦 CA 检测到不可调度的 Pod，它就会运行一个算法来做决策：<br>
<ol><li>需要多少个节点来将所有的不可调度 Pod 部署完成。</li><li>需要创建那种类型的节点组。</li></ol><br>
<br>整个过程的时间花费应该是：<br>
<ul><li>在少于 100 个节点且每个节点最多 30 个 Pod 的集群上不超过 30 秒。平均延迟应该是大约 5 秒。</li><li>在具有 100 到 1000 个节点的集群上不超过 60 秒。平均延迟应约为 15 秒。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/459e4eb35b247e2d267730c5f4499367.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/459e4eb35b247e2d267730c5f4499367.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后是节点配置时间，这主要取决于云提供商。在 3-5 分钟内供应新的计算资源是非常标准的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/952dbfd87efcfe4b20e0a177e1598dfc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/952dbfd87efcfe4b20e0a177e1598dfc.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
最后，Pod 必须由容器运行时创建。启动一个容器应该不会超过几毫秒，但下载容器镜像可能需要几秒钟。如果没有缓存容器映像，则从容器注册表下载映像可能需要几秒钟到一分钟的时间，具体取决于层的大小和数量。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/ab3efb5697df00544c0fe7f78bf65ee4.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/ab3efb5697df00544c0fe7f78bf65ee4.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
因此，当集群中没有空间而触发自动伸缩的时间消耗如下：<br>
<ol><li>Horizontal Pod Autoscaler 可能需要长达 1min30s 来增加副本数量。</li><li>对于少于 100 个节点的集群，Cluster Autoscaler 应该花费不到 30s 的时间，对于超过 100 个节点的集群，应该不到 1min。</li><li>云提供商可能需要 3-5min 来创建计算机资源。</li><li>容器运行时可能需要长达 30s 才能下载容器映像。</li></ol><br>
<br>如果你的集群规模不是很大，在最坏的情况下，时间消耗：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/6d04a3878033c757170ee513640b619a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/6d04a3878033c757170ee513640b619a.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
对于超过 100 个节点的集群，总延迟可能高达 7 分钟。在有更多 Pod 来处理突然激增的流量之前，您是否愿意等待这 7 分钟？<br>
<br>这里提供了几种减少 scaling 时间的方法：<br>
<ul><li>调整 Horizontal Pod Autoscaler 的刷新时间（由 –horizontal-pod-autoscaler-sync-period 参数控制，默认 15s）。•</li><li>整抓取 Pod 的 CPU 和内存使用情况的间隔频率（由 metric-resolution 变量控制，默认 60s）。</li><li>调整 Cluster Autoscaler 扫描未被调度 Pod 的间隔频率（由 scan-interval 变量控制，默认 10s）。</li><li>调整 Node 节点上缓存容器镜像的方式（通过诸如 kube-fledged 等工具）。</li></ul><br>
<br>但即使将这些设置调整为很小的值，你仍然会收到云提供商创建计算资源的时间限制。有什么方式优化这个部分吗？<br>
<br>这里可以做两件事：<br>
<ol><li>尽可能地避免创建新地 Node 节点。</li><li>主动提前创建节点，以便在需要时能直接使用。</li></ol><br>
<br><h3>为 Kubernetes 节点选择最佳实例大小</h3>选择正确的节点实例类型对集群的扩展策略有很大的影响。<br>
<br>考虑一个这样的场景。你有一个应用需要 1GB 的内存资源和 0.1 vCPU 资源。你提供的 Node 节点有 4GB 的内存资源和 1 vCPU 资源。在为操作系统、kubelet 和驱逐阀值保留内存和 CPU 后，将拥有约 2.5GB 的内存资源和 0.7 vCPU 可用于运行 Pod。所以你的 Node 节点只能承载 2 个 Pod 的运行。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/1304c77b9ade325f5dc21a68027b9743.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/1304c77b9ade325f5dc21a68027b9743.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
每次扩展 Pod 副本时，都可能会产生最多 7 分钟的延迟（触发 HPA，CA 和云提供商配置计算资源的前置时间）。<br>
<br>让我们来看看如果改成提供 64GB 的内存和 16 vCPU 的节点会发生什么。<br>
<br>在为操作系统、kubelet 和驱逐阀值保留内存和 CPU 后，将拥有约 58.32GB 的内存资源和 15.8 vCPU 可用于运行 Pod。<br>
<br>Node 节点可以承载 58 个 Pod 的运行，只有超过 58 个 Pod 副本时，才需要一个新的节点。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/70653a3bb377019ef47672bd40eedb17.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/70653a3bb377019ef47672bd40eedb17.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
此外，每次向集群中添加节点时，都可以部署多个 Pod。再次触发 Cluster Autoscaler 的机会更少。<br>
<br>选择大型节点实例类型还有另一个好处。为 kubelet 预留的资源、操作系统和驱逐阀值与运行 Pod 的可用资源之间的比率更大。看看这张图，它描绘了 Pod 可用的内存。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/d9ae0c22e445f7c1d23d5822bf025070.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/d9ae0c22e445f7c1d23d5822bf025070.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
随着 Node 实例大小的增加，你可以注意到（按比例）可用于 Pod 的资源增加。换句话说，与拥有两个大小一半的实例相比，可以更高效地利用资源。<br>
<br>那应该一直选择最大的实例吗？<br>
<br>节点上可以拥有的 Pod 数量决定了效率的峰值。<br>
<br>一些云提供商将 Pod 的数量限制为 110 个（比如 GKE）。其他一些限制是由底层网络基于每个实例（即 AWS）规定的。<br>
<br><blockquote><br>你可以在这里查看大多数云提供商的限制</blockquote>所以选择更大的实例类型并不总是一个好的选择。<br>
<br>我们还需要考虑：<br>
<ol><li>爆炸半径 - 如果你只有几个节点，那么一个失败节点的影响比你有很多节点的影响更大。</li><li>自动伸缩的成本更高，因为下一个增量是（非常）大的节点。</li></ol><br>
<br>假设你为集群选择了正确的实例类型，你在配置新计算单元时可能仍然会遇到延迟。<br>
<br>如果不是在需要扩展时创建新节点，而是提前创建相同的节点会怎么样？<br>
<h3>在 Kubernetes 集群中过度配置节点</h3>如果你可以负担得起随时可用的备用节点的话，你可以：<br>
<ol><li>提前创建一个空的 Node 节点。</li><li>一旦空的 Node 节点上有 Pod 了，就会创建另一个空的 Node 节点。</li></ol><br>
<br>换句话说，让 Cluster Autoscaler 总是保持有一个备用的空 Node 节点。<br>
<br>这是一种权衡：你会产生额外的成本，但扩展新节点的速度会提高。<br>
<br>但有坏消息和好消息。<br>
<br>坏消息是 Cluster Autoscaler 没有内置此功能。它不能被显式的配置，并且也没有提供相应的参数。<br>
<br>好消息是你仍然可以通过一些 trick 的方式来达到这个目的。<br>
<br>你可以运行具有足够请求的 Deployment 来保留一个完整的 Node 节点。你可以将这些 Pod 视为占位符 - 它旨在保留空间，而不是使用资源。<br>
<br>一旦创建了真正的 Pod，就可以驱逐占位符并部署真正的 Pod。<br>
<br>请注意，这一次你仍然需要等待 5 分钟才能将节点添加到集群中，但你可以继续使用当前节点。同时，在后台又提供了一个新的节点。<br>
<br>如何做到这一点呢？<br>
<br>可以使用运行永久休眠的 pod 的部署来配置过度配置。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/154b6e23890639a6856bd8557980105d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/154b6e23890639a6856bd8557980105d.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
上图中，你需要特别关注内存和 CPU 配置。Scheduler 会使用这些值来决定部署 Pod 的位置。在这种特殊情况下，它们用于保留空间。<br>
<br>你可以配置一个大型 Pod，该 Pod 的请求大致与可用节点资源相匹配。同时要确保你考虑了 kubelet、操作系统、kube-proxy 等消耗的资源。<br>
<br>如果你的节点实例是 2 vCPU 和 8GB 内存，并且 pod 的可用空间是 1.73 vCPU 和～5.9GB 内存，则该节点就无法承载这个 Pod，因为实际的 Pod 可用资源是要小于所需资源的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/943c5756958049466bffa5a6e238026a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/943c5756958049466bffa5a6e238026a.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
为了确保在创建真正的 Pod 时能快速的驱逐占位 Pod，可以使用优先级和抢占。<br>
<br>Pod Priority 表示一个 Pod 相对于其他 Pod 的重要性。<br>
<br>当一个 Pod 无法被调度时，Scheduler 会尝试抢占（驱逐）较低优先级的 Pod 以调度 “pending” 的 Pod。<br>
<br>可以使用 PodPriorityClass 在集群中配置 Pod 优先级：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/d56c24a3b5e595e19d5e9b6cf4d7bff1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/d56c24a3b5e595e19d5e9b6cf4d7bff1.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
由于 Pod 的默认优先级为 0，而过度配置的 PriorityClass 值为 -1，因此当集群空间不足时，这些 Pod 将首先被逐出。<br>
<br>PriorityClass 还有两个可选字段：globalDefault 和 description。<br>
<ul><li>description 字段是提供给人阅读的关于 PriorityClass 的描述信息。</li><li>globalDefault 字段表示这个 PriorityClass 的值应该用于没有 priorityClassName 的 Pod。系统中只能存在一个 global Default 设置为 true 的 PriorityClass。</li></ul><br>
<br>你可以使用下面的命令为你的 Pod 指定优先级：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/08ca31f263dc68757f3b1eaed8da3794.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/08ca31f263dc68757f3b1eaed8da3794.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
设置完成！<br>
<br>当集群中没有足够的资源时，Pause Pod 会被抢占，并由新的 Pod 取而代之。<br>
<br>由于 Pause pod 变得不可调度，它会强制 Cluster Autoscaler 向集群添加更多节点。<br>
<br>现在，你已准备好过度配置集群，该是时候考虑优化应用程序以进行扩展了。<br>
<h3>为 Pod 选择正确的内存和 CPU 资源</h3>Cluster Autoscaler 会根据 “pending” Pod 的出现来做出 scaling 决策。<br>
<br>Kubernetes Scheduler 根据 Node 节点的内存和 CPU 负载情况决定将 Pod 分配（或不分配）给节点。<br>
<br>因此，必须为你的工作负载设置正确的资源使用请求，否则您可能会过晚（或过早）触发自动伸缩机制。<br>
<br>让我们看一个例子。<br>
<br>您决定要测试一个应用程序，并发现：<br>
<ul><li>在平均负载下，应用程序消耗 512MB 内存和 0.25 vCPU。</li><li>在高峰期，应用程序应最多消耗 4GB 内存和 1 vCPU。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/fef6559aa777d699f808267ad4db69d0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/fef6559aa777d699f808267ad4db69d0.jpg" class="img-polaroid" title="17.jpg" alt="17.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
你的容器的限制应该是 4GB 内存和 1 个 vCPU。但是，请求呢？<br>
<br>Scheduler 在创建 Pod 之前使用 Pod 的内存和 CPU 请求来选择最佳节点。<br>
<br>所以你可以：<br>
<ol><li>将请求设置为低于实际平均使用量。</li><li>保守一点，分配更接近限制的请求。</li><li>设置请求以匹配实际的限制。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/3fdc9d261e07ebdb6d44ccbbd61d3af7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/3fdc9d261e07ebdb6d44ccbbd61d3af7.jpg" class="img-polaroid" title="18.jpg" alt="18.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/5789e96f6f5dda8308bf469a6819d2fc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/5789e96f6f5dda8308bf469a6819d2fc.jpg" class="img-polaroid" title="19.jpg" alt="19.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/01900af1a749b584fbaf07b3ccceae7b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/01900af1a749b584fbaf07b3ccceae7b.jpg" class="img-polaroid" title="20.jpg" alt="20.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
定义低于实际使用的请求是有问题的，因为你的节点经常会被过度使用。<br>
<br>例如，你可以分配 256MB 的内存作为内存请求。Scheduler 可以为每个节点安装两倍的 Pod。然而，Pod 在实践中使用两倍的内存并开始竞争资源 (CPU) 并被驱逐（节点上没有足够的内存）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/da297531b34a8b8f3334c72dee48db59.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/da297531b34a8b8f3334c72dee48db59.jpg" class="img-polaroid" title="21.jpg" alt="21.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
过度使用节点会导致过多的驱逐、更多的 kubelet 工作和大量的重新调度。<br>
<br>如果将请求设置为与限制相同的值会发生什么？<br>
<br>在 Kubernetes 中，这通常被称为 Guaranteed Quality of Service 类，指的是 pod 不太可能被终止和驱逐。Scheduler 将为分配的节点上的 Pod 保留整个 CPU 和内存。该类 Pod 运行稳定，但同时该节点的使用效率就会比较低。<br>
<br>如果你的应用平均使用 512MB 的内存，但为它预留了 4GB，那么大部分时间有 3.5GB 未使用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/e9a5c8b239e0f03167b75196f217ef37.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/e9a5c8b239e0f03167b75196f217ef37.jpg" class="img-polaroid" title="22.jpg" alt="22.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这值得么？<br>
<br>如果你想要更多的稳定性，是值得的。<br>
<br>如果你想要效率，你可能希望降低请求并在这些请求与限制之间找到平衡。<br>
<br>这通常被称为 Burstable Quality of Service 类，指的是 Pod 消耗稳定但偶尔会突然使用更多内存和 CPU。<br>
<br>当你的请求与应用的实际使用相匹配时，Scheduler 将高效地将你的 Pod 打包到你的节点中。<br>
<br>有时，应用程序可能需要更多内存或 CPU。<br>
<ol><li>如果 Node 中有资源，应用程序将会在达到最低消耗之前使用它们。2. 如果 Node 中资源不足，Pod 将竞争资源（CPU），kubelet 可能会尝试驱逐 Pod（内存）。</li></ol><br>
<br>此时，你应该使用 Guaranteed Quality of Service 还是 Burstable Quality of Service？<br>
<br>这取决于如下两点：<br>
<ol><li>当你希望最小化 Pod 的重新调度和驱逐时，请使用 Guaranteed Quality of Service（请求等于限制）。一个很好的例子是用于数据库的 Pod。</li><li>当你想要优化集群并明智地使用资源时，请使用 Burstable Quality of Service（请求匹配实际平均使用情况）。如果您有 Web 应用程序或 REST API，您可能希望使用 Burstable Quality of Service。</li></ol><br>
<br>那如何选择正确的请求和限制值？<br>
<br>你应该分析应用程序并测量空闲、负载和峰值时的内存和 CPU 消耗。更直接的策略包括部署 Vertical Pod Autoscaler 并等待它建议正确的值。<br>
<br>Vertical Pod Autoscaler 从 Pod 收集数据并应用回归模型来推断请求和限制。<br>
<br>您可以在本文中了解有关如何执行此操作的更多信息。<br>
<h3>关于集群的缩容</h3>每 10 秒，只有当请求利用率低于 50% 时，Cluster Autoscaler 才会决定删除节点。<br>
<br>换句话说，对于同一节点上的所有 Pod，它会汇总 CPU 和内存请求。<br>
<br>如果它们低于节点容量的一半，Cluster Autoscaler 将考虑当前节点进行缩减。<br>
<br><blockquote><br>值得注意的是，Cluster Autoscaler 不考虑实际的 CPU 和内存使用或限制，而只查看资源请求。</blockquote>在移除节点之前，Cluster Autoscaler 执行：<br>
<ul><li>Pod 检查以确保 Pod 可以移动到其他节点。</li><li>Node 节点检查以防止节点过早被破坏。</li></ul><br>
<br>如果检查通过，Cluster Autoscaler 将从集群中删除节点。<br>
<h3>为什么不基于内存或 CPU 进行自动伸缩</h3>在扩缩容时，基于 CPU 或内存的 Cluster Autoscaler 不关心 Pod。<br>
<br>想象一下，有一个只有一个节点的集群，并设置 Autoscaler 来添加一个新节点当 CPU 使用率达到总容量的 80%。<br>
<br>然后你决定创建一个具有 3 个副本的 Deployment。三个 Pod 的总资源使用率达到了 CPU 的 85%。<br>
<br>一个新的 Node 节点被提供。如果你不需要更多 Pod 怎么办？你有一个完整节点处于空闲的状态 —— 这不是很好。这种使用 Autoscaler 的方式是不鼓励的。<br>
<h3>总结</h3>在 Kubernetes 中定义和实施成功的扩缩容策略需要您掌握几个主题：<br>
<ul><li>熟悉 Kubernetes 节点中的可分配资源。</li><li>微调 Metrics Server、Horizontal Pod Autoscaler 和 Cluster Autoscalers 的刷新间隔。</li><li>规划集群和节点实例大小。</li><li>做好容器镜像的缓存。</li><li>做好应用程序基准测试和分析。</li></ul><br>
<br>但是上面这些还不够，你还需要使用适当的监控工具，反复测试您的扩缩容策略并调整集群的节点创建速度和成本。<br>
<br>译文链接：<a href="https://mp.weixin.qq.com/s/hgw_yjCsNKPo7hP01FfSJQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/hgw_yjCsNKPo7hP01FfSJQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            