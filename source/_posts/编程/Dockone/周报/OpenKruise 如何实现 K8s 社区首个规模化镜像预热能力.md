
---
title: 'OpenKruise 如何实现 K8s 社区首个规模化镜像预热能力'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/9651f86fd1f008f6277426d93e4092be.png'
author: Dockone
comments: false
date: 2021-03-24 05:19:29
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/9651f86fd1f008f6277426d93e4092be.png'
---

<div>   
<br>作者 | 王思宇（酒祝）<br>
来源 | <a href="https://mp.weixin.qq.com/s/teL4k8_egS9fgFPH7a70Zg">阿里巴巴云原生公众号</a><br>
<br><h1>前言</h1><a href="https://github.com/openkruise/kruise">OpenKruise</a> 是阿里云开源的云原生应用自动化管理套件，也是当前托管在 Cloud Native Computing Foundation (CNCF) 下的 Sandbox 项目。它来自阿里巴巴多年来容器化、云原生的技术沉淀，是阿里内部生产环境大规模应用的基于 Kubernetes 之上的标准扩展组件，也是紧贴上游社区标准、适应互联网规模化场景的技术理念与最佳实践。<br>
<br>OpenKruise 在 2021.3.4 发布了最新的 v0.8.0 版本（<a href="https://github.com/openkruise/kruise/blob/master/CHANGELOG.md">ChangeLog</a>），其中一个主要变动是新增了 **镜像预热 **能力。本文由《通过 OpenKruise 实现大规模集群 镜像预热&部署发布加速实践》分享整理为文字，为大家介绍我们所提供的镜像预热能力的需求来源、实现方式以及使用场景。<br>
<br><h1>背景：为什么镜像预热能力是必要的</h1>“镜像” 也算是 Docker 为容器领域带来的一大创新。在 Docker 之前，虽然 Linux 已经提供了 cgroup 隔离，尽管阿里巴巴从 2011 年已经逐渐基于 LXC 开始容器化，但都缺乏镜像这种对运行环境的封装。不过呢，尽管镜像为我们带来了诸多好处，但不可否认在实际场景中我们也面临各种各样拉镜像带来的问题，其中最常见的一点就是拉镜像的耗时。<br>
<br>我们过去听到过很多用户对容器化的期待和认识，比如 “极致弹性”、“秒级扩容”、“高效发布” 等等，但结合 Kubernetes 中一个标准的 Pod 创建过程来看，和用户的期望还是有一定差距的（假设 Pod 中包含 sidecar、app 两个容器）：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/9651f86fd1f008f6277426d93e4092be.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/9651f86fd1f008f6277426d93e4092be.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>正常来说，对于小规模集群中调度、分配/挂载远程盘、分配网络等操作耗时较小，对于大规模集群需要做一定优化，但都还在可控的范围内。然而对于拉镜像的耗时，在大规模弹性的集群中则尤为棘手，即使采用了 P2P 等技术手段来优化，对于一个较大的业务镜像还是可能需要较长的时间来拉取，与用户所期望的扩容、发布速度不符。<br>
<br>而我们如果能做到将 sidecar 容器的镜像、以及业务容器的基础镜像提前在节点上拉取好，则 Pod 创建过程可以大幅缩短，其中拉镜像的耗时甚至能优化 70% 以上：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/51c3037e18841718076ac0a6224437bb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/51c3037e18841718076ac0a6224437bb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>而 Kubernetes 自身是没有提供任何面向镜像的操作能力的，围绕 Kubernetes 的生态来看，目前也没有比较成熟的规模化镜像预热产品。这是我们在 OpenKruise 中提供镜像预热的原因，并且这套镜像预热能力已经在阿里巴巴内部的云原生环境大面积落地，在后文的实践中也会简单介绍我们的基本用法。<br>
<br><h1>OpenKruise 是如何实现镜像预热的</h1>OpenKruise 实现镜像预热的原理，要先从它的运行架构看起：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/efd703fbd1cf7fec86fa364aab82b206.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/efd703fbd1cf7fec86fa364aab82b206.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>从 v0.8.0 开始，安装了 Kruise 之后，有两个在 kruise-system 命名空间下的组件：kruise-manager 与 kruise-daemon。前者是一个由 Deployment 部署的中心化组件，一个 kruise-manager 容器（进程）中包含了多个 controller 和 webhook；后者则由 DaemonSet 部署到集群中的节点上，通过与 CRI 交互来绕过 Kubelet 完成一些扩展能力（比如拉取镜像、重启容器等）。<br>
<br>因此，Kruise 会为每个节点（Node）创建一个同名对应的自定义资源：NodeImage，而每个节点的 NodeImage 里写明了在这个节点上需要预热哪些镜像，因此这个节点上的 kruise-daemon 只要按照 NodeImage 来执行镜像的拉取任务即可：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/8dbebf34b4753fe492baf8bc54d30ce7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/8dbebf34b4753fe492baf8bc54d30ce7.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，我们在 NodeImage 中能指定要拉取的镜像名、tag、拉取的策略，比如单次拉取的超时、失败重试次数、任务的 deadline、TTL 时间等等。<br>
<br>有了 NodeImage，我们也就拥有了最基本的镜像预热能力了，不过还不能完全满足大规模场景的预热需求。在一个有 5k 个节点的集群中，要用户去一个个更新 NodeImage 资源来做预热显然是不够友好的。因此，Kruise 还提供了一个更高抽象的自定义资源 ImagePullJob：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/a9afbfd0b1d5ac074ca763dfd9394731.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/a9afbfd0b1d5ac074ca763dfd9394731.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，在 ImagePullJob 中用户可以指定一个镜像要在哪些范围的节点上批量做预热，以及这个 job 的拉取策略、生命周期等。一个 ImagePullJob 创建后，会被 kruise-manager 中的 imagepulljob-controller 接收到并处理，将其分解并写入到所有匹配节点的 NodeImage 中，以此来完成规模化的预热。<br>
<br>整体的流程如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/5df3e34f05200a97936445bca9738845.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/5df3e34f05200a97936445bca9738845.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>而有了镜像预热能力后，我们怎么去使用它，或者说什么场景下需要来使用呢？接下来我们介绍下镜像预热在阿里巴巴中的几种常见使用方式。<br>
<br><h1>常见的镜像预热使用方式有哪些</h1><h3>1. 基础镜像 – 集群维度预热</h3>最常见的预热场景，是在整个集群维度持续预热一些基础镜像：<br>
<br><code class="prettyprint">yaml<br>
apiVersion: apps.kruise.io/v1alpha1<br>
kind: ImagePullJob<br>
metadata:<br>
  name: base-image-job<br>
spec:<br>
  image: xxx/base-image:latest<br>
  parallelism: 10<br>
  completionPolicy:<br>
    type: Never<br>
  pullPolicy:<br>
    backoffLimit: 3<br>
    timeoutSeconds: 300</code><br>
<br>如上述 ImagePullJob 有几个特征：<br>
<ol><li>不配置 selector 规则，即默认整个集群维度预热<br>
<ol><li>存量的节点上统一预热</li>1. 后续新增（导入）的节点上也会立即自动做预热</ol></li><li>采用 Never 的 completionPolicy 策略来长期运行<br>
<ol><li>Never 策略表明这个 job 持续做预热，不会结束（除非被删除）</li>1. Never 策略下，ImagePullJob 每隔 24h 左右会触发在所有匹配的节点上重试拉取一次，也就是每天都会确保一次镜像存在</ol></li></ol><br>
<br>根据我们的经验，一个集群中预热基础镜像的 ImagePullJob 在 10~30 个左右，具体视集群以及业务场景而定。<br>
<br><h3>2. sidecar 镜像 – 集群维度预热</h3>我们同样也可以对一些 sidecar 的镜像做预热，尤其是那些基本上每个业务 Pod 中都会带有的基础 sidecar：<br>
<br><code class="prettyprint">yaml<br>
apiVersion: apps.kruise.io/v1alpha1<br>
kind: ImagePullJob<br>
metadata:<br>
  name: sidecar-image-job<br>
spec:<br>
  image: xxx/sidecar-image:latest<br>
  parallelism: 20<br>
  completionPolicy:<br>
    type: Always<br>
    activeDeadlineSeconds: 1800<br>
    ttlSecondsAfterFinished: 300<br>
  pullPolicy:<br>
    backoffLimit: 3<br>
    timeoutSeconds: 300</code><br>
<br>如上述 ImagePullJob 有几个特征：<br>
<ol><li>不配置 selector，默认整个集群维度预热，这一点与基础镜像类似</li><li>采用 Always 策略一次性预热<br>
<ol><li>所有节点做一次预热</li><li>整个 job 预热超时时间 30min</li>1. job 完成后过 5min 自动删除</ol></li></ol><br>
<br>当然，这里的 sidecar 预热也可以配置为 Never 策略，视场景而定。以我们的经验来看，尤其在 sidecar 做版本迭代、镜像升级的时候，提前做一次规模化的镜像预热，可以大幅提升后续 Pod 扩容、发布的速度。<br>
<br><h3>3. 特殊业务镜像 – 资源池维度预热</h3>对于一些多租的 Kubernetes 集群中会存在多个不同的业务资源池，其中可能需要将一些特定的业务镜像按资源池维度来预热：<br>
<br><code class="prettyprint">yaml<br>
apiVersion: apps.kruise.io/v1alpha1<br>
kind: ImagePullJob<br>
metadata:<br>
  name: serverless-job<br>
spec:<br>
  image: xxx/serverless-image:latest<br>
  parallelism: 10<br>
  completionPolicy:<br>
    type: Never<br>
  pullPolicy:<br>
    backoffLimit: 3<br>
    timeoutSeconds: 300<br>
  selector:<br>
    matchLabels:<br>
      resource-pool: serverless</code><br>
<br>如上述 ImagePullJob 有几个特征：<br>
<ol><li>采用 Never 策略长期预热</li><li>指定 selector 预热范围，是匹配 resource-pool=serverless 标签的节点</li></ol><br>
<br>当然，这里只是以资源池为例，用户可以根据自身的场景来定义在哪些节点上预热某种镜像。<br>
<br><h1>版本前瞻：原地升级与预热的结合</h1>最后，再来介绍下 OpenKruise 的下个版本（v0.9.0）中，我们会基于当前的镜像预热实现怎样的增强能力呢？<br>
<br>之前对 OpenKruise 了解过的同学一定知道，我们提供的一大特性就是 “原地升级”，即打破了 Kubernetes 原生 workload 发布时必须将 Pod 删除、重建的模式，支持在原 Pod 上只更新其中某个容器的镜像。对原地升级原理感兴趣的同学可以读这篇文章：《<a href="https://mp.weixin.qq.com/s/CNLf8MHYGs_xeD4PxChR4A">揭秘：如何为 Kubernetes 实现原地升级？</a>》。<br>
<br>由于原地升级避免了 Pod 删除、重建的过程，它本身已经能为我们带来了如下的好处：<br>
<ul><li>节省了<strong>调度</strong>的耗时，Pod 的位置、资源都不发生变化</li><li>节省了<strong>分配网络</strong>的耗时，Pod 还使用原有的 IP</li><li>节省了<strong>分配、挂载远程盘</strong>的耗时，Pod 还使用原有的 PV（且都是已经在 Node 上挂载好的）</li><li>节省了<strong>大部分拉取镜像</strong>的耗时，因为节点上已经存在了应用的旧镜像，当拉取新版本镜像时只需要下载少数的几层 layer</li><li>原地升级 Pod 中某个容器时，其他容器<strong>保持正常运行</strong>，网络、存储均不受影响</li></ul><br>
<br>其中，“节省了大部分拉取镜像的耗时” 后，只需要下载新镜像上层的部分 layer 即可。而我们有没有可能把这个镜像拉取时间彻底优化掉呢？答案是肯定的。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210323/057136767a72a52fb42a5062b139e6f5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210323/057136767a72a52fb42a5062b139e6f5.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如上图所示，在下个版本中 OpenKruise 的 CloneSet 将支持发布过程自动镜像预热。当用户还在灰度升级第一批 Pod 的时候，Kruise 会提前在后续 Pod 所在节点上把新版本的镜像预热好。这样一来，在后续批次的 Pod 做原地升级时候，新镜像都已经在节点上准备好了，也就节省了真正发布过程中的拉镜像耗时。<br>
<br>当然，这种 “发布+预热” 的模式也只适用于 OpenKruise 的原地升级场景。对于原生 workload 如 Deployment 而言，由于发布时 Pod 是新建出来的，我们无法提前预知到它会被调度到的节点，自然也就没办法提前把镜像预热好了。<br>
<br>如果大家对 OpenKruise 项目感兴趣，有任何希望交流的话题，欢迎大家访问 <a href="https://openkruise.io/en-us/">OpenKruise 官网</a>、<a href="https://github.com/openkruise/kruise">GitHub</a>！
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            