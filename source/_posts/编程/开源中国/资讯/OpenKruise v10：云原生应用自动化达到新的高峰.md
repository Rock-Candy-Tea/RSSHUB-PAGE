
---
title: 'OpenKruise v1.0：云原生应用自动化达到新的高峰'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1217/165553_UpC6_5430600.png'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 09:01:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1217/165553_UpC6_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>云原生应用自动化管理套件、CNCF Sandbox 项目 -- <strong>OpenKruise</strong>，近期发布了 v1.0 大版本。</p> 
<p>OpenKruise 是针对 Kubernetes 的增强能力套件，聚焦于云原生应用的部署、升级、运维、稳定性防护等领域。所有的功能都通过 CRD 等标准方式扩展，可以适用于 1.16 以上版本的任意 Kubernetes 集群。单条 helm 命令即可完成 Kruise 的一键部署，无需更多配置。</p> 
<p><img alt height="509" src="https://static.oschina.net/uploads/space/2021/1217/165553_UpC6_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">总得来看，目前 OpenKruise 提供的能力分为几个领域：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p><strong style="color:black">应用工作负载</strong>：面向无状态、有状态、daemon 等多种类型应用的高级部署发布策略，例如原地升级、灰度流式发布等。</p> </li> 
 <li> <p><strong style="color:black">Sidecar 容器管理</strong>：支持独立定义 sidecar 容器，完成动态注入、独立原地升级、热升级等功能。</p> </li> 
 <li> <p><strong style="color:black">增强运维能力</strong>：包括容器原地重启、镜像预拉取、容器启动顺序保障等。</p> </li> 
 <li> <p><strong style="color:black">应用分区管理</strong>：管理应用在多个分区（可用区、不同机型等）上的部署比例、顺序、优先级等。</p> </li> 
 <li> <p><strong style="color:black">应用安全防护</strong>：帮助应用在 Kubernetes 之上获得更高的安全性保障与可用性防护。</p> </li> 
</ul> 
<h2>版本解析</h2> 
<p>在 v1.0 大版本中，OpenKruise 带来了多种新的特性，同时也对不少已有功能做了增强与优化。</p> 
<p>首先要说的是，从 v1.0 开始 OpenKruise 将 CRD/WehhookConfiguration 等资源配置的版本从 v1beta1 升级到 v1，因此可以支持 Kubernetes v1.22 及以上版本的集群，但同时也要求 Kubernetes 的版本不能低于 v1.16。</p> 
<p>以下对 v1.0 的部分功能做简要介绍，详细的 ChangeLog 列表请查看 OpenKruise Github 上的 release 说明以及官网文档。</p> 
<h3><strong>1. 支持环境变量原地升级</strong></h3> 
<p><em>Author:<span> </span><strong style="color:#0080ff">@FillZpp</strong></em></p> 
<p>OpenKruise 从早期版本开始就支持了 “原地升级” 功能，主要应用于 CloneSet 与 Advanced StatefulSet 两种工作负载上。简单来说，原地升级使得应用在升级的过程中，不需要删除、新建 Pod 对象，而是通过对 Pod 中容器配置的修改来达到升级的目的。<br> <img alt height="506" src="https://static.oschina.net/uploads/space/2021/1217/165752_hvhp_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">如上图所示，原地升级过程中只修改了 Pod 中的字段，因此：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p>可以避免如<span> </span><em>调度</em>、<em>分配 IP</em>、<em>分配、挂载盘</em><span> </span>等额外的操作和代价。</p> </li> 
 <li> <p>更快的镜像拉取，因为开源复用已有旧镜像的大部分 layer 层，只需要拉取新镜像变化的一些 layer。</p> </li> 
 <li> <p>当一个容器在原地升级时，Pod 的网络、挂载盘、以及 Pod 中的其他容器不会受到影响，仍然维持运行。</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">然而，OpenKruise 过去只能对 Pod 中 image 字段的更新做原地升级，对于其他字段仍然只能采用与 Deployment 相似的重建升级。一直以来，我们收到很多用户反馈，希望支持对 env 等更多字段的原地升级 -- 由于受到 kube-apiserver 的限制，这是很难做到的。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">经过我们的不懈努力，OpenKruise 终于在 v1.0 版本中，支持了通过 Downward API 的方式支持了 env 环境变量的原地升级。例如对以下 CloneSet YAML，用户将配置定义在 annotation 中并关联到对应 env 中。后续在修改配置时，只需要更新 annotation value 中的值，Kruise 就会对 Pod 中所有 env 里引用了这个 annotation 的容器触发原地重建，从而生效这个新的 value 配置。</p> 
<pre><code>apiVersion: apps.kruise.io/v1alpha1
kind: CloneSet
metadata:
  ...
spec:
  replicas: 1
  template:
    metadata:
      annotations:
        app-config: "... the real env value ..."
    spec:
      containers:
      - name: app
        env:
        - name: APP_CONFIG
          valueFrom:
            fieldRef:
              fieldPath: metadata.annotations['app-config']
  updateStrategy:
    type: InPlaceIfPossible</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><em>与此同时，我们在这个版本中也去除了过去对镜像原地升级的<code>imageID</code>限制，即支持相同 imageID 的两个镜像替换升级。</em></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">具体使用方式请参考<strong style="color:#0080ff">文档</strong>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2. 配置跨命名空间分发</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><em>Author:<span> </span><strong style="color:#0080ff">@veophi</strong></em></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">在对 Secret、ConfigMap 等 namespace-scoped 资源进行跨 namespace 分发及同步的场景中，原生 kubernetes 目前只支持用户 one-by-one 地进行手动分发与同步，十分地不方便。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">典型的案例有：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>当用户需要使用 SidecarSet 的 imagePullSecrets 能力时，要先重复地在相关 namespaces 中创建对应的 Secret，并且需要确保这些 Secret 配置的正确性和一致性。</p> </li> 
 <li> <p>当用户想要采用 ConfigMap 来配置一些<strong style="color:black">通用</strong>的环境变量时，往往需要在多个 namespaces 做 ConfigMap 的下发，并且后续的修改往往也要求多 namespaces 之间保持同步。</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">因此，面对这些需要跨 namespaces 进行资源分发和<strong>多次同步</strong>的场景，我们期望一种更便捷的分发和同步工具来自动化地去做这件事，为此我们设计并实现了一个新的 CRD ---<span> </span><strong>ResourceDistribution</strong>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">ResourceDistribution 目前支持<span> </span><strong>Secret</strong><span> </span>和<span> </span><strong>ConfigMap</strong><span> </span>两类资源的分发和同步。</p> 
<pre><code>apiVersion: apps.kruise.io/v1alpha1
kind: ResourceDistribution
metadata:
  name: sample
spec:
  resource:
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: game-demo
    data:
      ...
  targets:
   namespaceLabelSelector:
      ...
    # or includedNamespaces, excludedNamespaces</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">如上述 YAML 所示，ResourceDistribution 是一类<span> </span><strong>cluster-scoped</strong><span> </span>的 CRD，其主要由<span> </span><strong><code>resource</code></strong><span> </span>和<span> </span><strong><code>targets</code></strong><span> </span>两个字段构成，其中<span> </span><strong><code>resource</code></strong><span> </span>字段用于描述用户所要分发的资源，<strong><code>targets</code></strong><span> </span>字段用于描述用户所要分发的目标命名空间。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">具体使用方式请参考<strong style="color:#0080ff">文档</strong>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">3. 容器启动顺序控制</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><em>Author:<span> </span><strong style="color:#0080ff">@Concurrensee</strong></em></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">对于 Kubernetes 的一个 Pod，其中的多个容器可能存在依赖关系，比如 容器 B 中应用进程的运行依赖于 容器 A 中的应用。因此，多个容器之间存在顺序关系的需求：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>容器 A 先启动，启动成功后才可以启动 容器 B</p> </li> 
 <li> <p>容器 B 先退出，退出完成后才可以停止 容器 A</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">通常来说 Pod 容器的启动和退出顺序是由 Kubelet 管理的。Kubernetes 曾经有一个 KEP 计划在 container 中增加一个 type 字段来标识不同类型容器的启停优先级。但是由于 sig-node 考虑到对现有代码架构的改动太大，目前这个 KEP 已经被拒绝了。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">因此，OpenKruise 在 v1.0 中提供了名为<span> </span><strong>Container Launch Priority</strong><span> </span>的功能，用于控制一个 Pod 中多个容器的强制启动顺序：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p>对于任意一个 Pod 对象，只需要在 annotations 中定义<span> </span><code>apps.kruise.io/container-launch-priority: Ordered</code>，则 Kruise 会按照 Pod 中<span> </span><code>containers</code><span> </span>容器列表的顺序来保证其中容器的串行启动。</p> </li> 
 <li> <p>如果要自定义<span> </span><code>containers</code><span> </span>中多个容器的启动顺序，则在容器 env 中添加<span> </span><code>KRUISE_CONTAINER_PRIORITY</code><span> </span>环境变量，value 值是范围在<span> </span><code>[-2147483647, 2147483647]</code><span> </span>的整数。一个容器的 priority 值越大，会保证越先启动。</p> </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">具体使用方式请参考<strong style="color:#0080ff">文档</strong>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">4.<span> </span><code>kubectl-kruise</code><span> </span>命令行工具</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><em>Author:<span> </span><strong style="color:#0080ff">@hantmac</strong></em></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">过去 OpenKruise 是通过 kruise-api、client-java 等仓库提供了 Go、Java 等语言的 Kruise API 定义以及客户端封装，可供用户在自己的应用程序中引入使用。但仍然有不少用户在测试环境下需要灵活地用命令行操作 workload 资源。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">然而原生<span> </span><code>kubectl</code><span> </span>工具提供的<span> </span><code>rollout</code>、<code>set image</code><span> </span>等命令只能适用于原生的 workload 类型，如 Deployment、StatefulSet，并不能识别 OpenKruise 中扩展的 workload 类型。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">因此，OpenKruise 最新提供了<span> </span><code>kubectl-kruise</code><span> </span>命令行工具，它是<span> </span><code>kubectl</code><span> </span>的标准插件，提供了许多适用于 OpenKruise workload 的功能。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><em># rollout undo cloneset</em>
$ kubectl kruise rollout undo cloneset/nginx

<em>#  rollout status advanced statefulset</em>
$ kubectl kruise rollout status statefulsets.apps.kruise.io/sts-demo

<em># set image of a cloneset</em>
$ kubectl kruise <span style="color:#0086b3">set</span> image cloneset/nginx busybox=busybox nginx=nginx:1.9.1
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">具体使用方式请参考<strong style="color:#0080ff">文档</strong>[9]。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">5. 其余部分功能改进与优化</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>CloneSet:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>通过<span> </span><code>scaleStrategy.maxUnavailable</code><span> </span>策略支持流式扩容</p> </li> 
 <li> <p>Stable revision 判断逻辑变化，当所有 Pod 版本与 updateRevision 一致时则标记为 currentRevision</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>WorkloadSpread:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>支持接管存量 Pod 到匹配的 subset 分组中</p> </li> 
 <li> <p>优化 webhook 在 Pod 注入时的更新与重试逻辑</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>Advanced DaemonSet:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>支持对 Daemon Pod 做原地升级</p> </li> 
 <li> <p>引入 progressive annotation 来选择是否按 partition 限制 Pod 创建</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>SidecarSet:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>解决 SidecarSet 过滤屏蔽 inactive Pod</p> </li> 
 <li> <p>在<span> </span><code>transferenv</code><span> </span>中新增<span> </span><code>SourceContainerNameFrom</code><span> </span>和<span> </span><code>EnvNames</code><span> </span>字段，来解决 container name 不一致与大量 env 情况下的冗余问题</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>PodUnavailableBudget:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>新增 “跳过保护” 标识</p> </li> 
 <li> <p>PodUnavailableBudget controller 关注 workload 工作负载的 replicas 变化</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>NodeImage:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>加入<span> </span><code>--nodeimage-creation-delay</code><span> </span>参数，并默认等待新增 Node ready 一段时间后同步创建 NodeImage</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>UnitedDeployment:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>解决<span> </span><code>NodeSelectorTerms</code><span> </span>为 nil 情况下 Pod<span> </span><code>NodeSelectorTerms</code><span> </span>长度为 0 的问题</p> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><strong>Other optimization:</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>kruise-daemon 采用 protobuf 协议操作 Pod 资源</p> </li> 
 <li> <p>暴露 cache resync 为命令行参数，并在 chart 中设置默认值为 0</p> </li> 
 <li> <p>解决 certs 更新时的 http checker 刷新问题</p> </li> 
 <li> <p>去除对 forked controller-tools 的依赖，改为使用原生 controller-tools 配合 markers 注解</p> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenkruise.io%2Fzh%2Fblog%2Fopenkruise-1.0%2F" target="_blank">https://openkruise.io/zh/blog/openkruise-1.0/</a></p>
                                        </div>
                                      
</div>
            