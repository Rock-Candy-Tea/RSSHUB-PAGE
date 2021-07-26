
---
title: 'Kubernetes监控介绍（一）'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/534037e633574fc17d6c9a12acc417c8.png'
author: Dockone
comments: false
date: 2021-07-26 07:06:48
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/534037e633574fc17d6c9a12acc417c8.png'
---

<div>   
<br>Kubernetes的控制器和Worker节点都包含多个组件。如果你是构建了一个集群的Kubernetes管理员，并且用户告诉你他们已经可以在集群上成功部署和测试应用程序了。<br>
<br>然而，集群是否能一直保持健康状态不出现什么问题，这一点却没什么保证。任何时候都有可能出问题，服务可能停止运行，Kubernetes组建也可能工作不正常等等。因此，很有必要为Kubernetes集群构建可靠的监控方案。<br>
<br>本文尝试解决：<br>
<ul><li>为什么需要监控</li><li>怎么监控？</li><li>介绍一些好用的工具</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/534037e633574fc17d6c9a12acc417c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/534037e633574fc17d6c9a12acc417c8.png" class="img-polaroid" title="pic1.png" alt="pic1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>为什么需要监控</h3>Kubernetes集群包括多个组件和层次，都有不同的故障点。知道什么时候以及为什么发生故障至关重要。监控系统的目标就是辅助提供健康可靠的系统。<br>
<br>除了提供可靠性，监控系统也可以帮助大家理解系统，有助于分析各种问题，比如故障，资源使用情况等等。<br>
<br>另一个使用监控的好处是可以理解并发现系统的趋势来辅助资源规划。<br>
<br>一些用户场景包括（不限于）：<br>
<ul><li>监控Kubernetes集群和节点。集群资源的使用，集群/节点可用性，健康情况等。</li><li>监控Kubernetes部署，服务和Pod。失败的Pod/部署/服务期待一些运行着的副本，Pod运行有资源的请求和限制等。</li><li>监控Kubernetes应用程序。可用性，健康状况，性能等。</li></ul><br>
<br><h3>什么是监控层？</h3>监控可以在很多不同的层面展开。如下是架构图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/77bad01df6814f3197033fa584a57e2c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/77bad01df6814f3197033fa584a57e2c.png" class="img-polaroid" title="pic2.png" alt="pic2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>监控指标</h3>在不同的监控层面可以收集不同的监控指标。下图展示了在不同的层面可以收集哪些指标。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/9a117940d90f7244c9d07b122ae1d040.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/9a117940d90f7244c9d07b122ae1d040.png" class="img-polaroid" title="pic3.png" alt="pic3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>监控工具</h3>Kubernetes有什么内建的监控工具吗？<br>
<br>Kubernetes提供了内建的监控工具。只需很少的配置就可以开箱即用，不过，也有其他更多更强大的工具。<br>
<br>Kubernetes集群里的每个节点上都运行着kubelet组件。每个kubelet包含<code class="prettyprint">cAdvisor</code>，它收集所在节点的每个容器的CPU，内存这些指标。它也帮助收集节点上的其他指标。<br>
<br><code class="prettyprint">Metrics Server</code>从cAdvisor收集指标并归总给中央控制平台。Metrics Server是在Kubernetes集群的一些节点上运行着的Pod。当这些指标收集上来后，用户可以运行<code class="prettyprint">kubectl top</code>查看容器，Pod或节点的CPU，内存和网络使用情况。<br>
<br><code class="prettyprint">Kubernetes Dashboard</code>提供了Metrics Server的数据的可视化展示。<br>
<br><code class="prettyprint">Kubernetes State Metrics</code>帮助提供Metrics Server无法提供的额外的指标。它监听Kubernetes API，生成和Kubernetes逻辑对象相关的指标，比如，节点状态，节点容量，Pod状态等。它可以部署为单个副本的服务。<br>
<br><code class="prettyprint">Probe</code>帮助监控容器和服务的健康状态。<code class="prettyprint">Liveness</code>探针帮助检查服务/Pod是否还在运行，如果没有运行就采取措施。<code class="prettyprint">Readiness</code>探针帮助检测服务/Pod是否能够接受访问流量。<a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/">Kubernetes官方文档</a>详细介绍了如何配置这些探针。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/709aa85a9052c07661a3539ccd3a3c5e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/709aa85a9052c07661a3539ccd3a3c5e.png" class="img-polaroid" title="pic4.png" alt="pic4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
推荐在生产环境上使用更成熟的开源或商业化的监控解决方案。下一篇博文会介绍其他监控方案，监控流水线和监控架构。<br>
<br><strong>原文链接：<a href="https://sandeepbaldawa.medium.com/intro-to-k8s-monitoring-part1-ba3c9f103ee1">Intro to K8s Monitoring — Part1</a>（翻译：崔婧雯）</strong> <br>
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br>
译者介绍<br>
崔婧雯，现就职于IBM，高级软件工程师，负责IBM WebSphere业务流程管理软件的系统测试工作。曾就职于VMware从事桌面虚拟化产品的质量保证工作。对虚拟化，中间件技术，业务流程管理有浓厚的兴趣。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            