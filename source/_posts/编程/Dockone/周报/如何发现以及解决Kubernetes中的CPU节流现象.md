
---
title: '如何发现以及解决Kubernetes中的CPU节流现象'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210724/2edf9b5e254325cac16229623e47aba5.png'
author: Dockone
comments: false
date: 2021-07-25 06:08:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210724/2edf9b5e254325cac16229623e47aba5.png'
---

<div>   
<br>Kubernetes是我们基础设施的重要组成部分。我们不仅在生产环境中使用Kubernetes，同时在CI/CD和开发/测试环境中也大量使用Kubernetes。在开发CI/CD基础设施时，我们遇到了一个特殊的性能问题，我们花费了大量的时间来解决它。<br>
<br>在本文中，我们将尝试深入探讨导致应用程序性能下降的原因，以及最终如何解决该问题。<br>
<h3>背景</h3>在Grofers（Grofers是一家印度在线杂货配送服务公司），我们使用微服务架构，所有关键组件（如支付、购物车、库存等）都作为微服务进行组织。因此，开发人员不能在同一命名空间中同时处理多个服务。这使我们采用了这样一种设计：每个开发人员都有自己的命名空间，所有服务都部署在一个隔离的环境中进行测试和调试。这就是我们内部所说的<code class="prettyprint">Grofers-in-a-namespace</code>。为了实现这一点，我们开发了一个名为<code class="prettyprint">mft</code>的内部工具。Mft用于在Kubernetes中创建新的命名空间，并从Vault和Consul中注入必要的依赖关系。<br>
<br>并通过Jenkins部署Grofers副本，此副本中包含了Grofers所需的所有微服务程序。然后，这些微服务通过Ingress暴露服务，供开发人员与测试人员使用。<br>
<h3>问题</h3>我们的服务采用了<a href="https://orangematter.solarwinds.com/2017/10/05/monitoring-and-observability-with-use-and-red/">USE-RED</a>仪表盘，以帮助我们跟踪关键指标。这使我们能够进一步优化基础设施，以获得最大的性能。<br>
<br>当我们开始分析这些指标时，我们发现某些应用程序需要花费大量的时间来启动，这是开发人员在本地环境中没有观察到的。另外，通过Jenkins创建Grofers环境，也需要花费大量的时间，这是我们以前没有预料到的。这使得我们开始重新审视所有指标，以确定是什么导致了Kubernetes基础设施的启动缓慢。<br>
<br>此外，在生产环境中没有观察到启动缓慢的问题。生产环境与开发/测试环境有很大区别，生成环境有更充裕的CPU和内存。同时，我们的生产集群还留有很大的扩展空间，这使我们相信这是一个特定于基础设施的问题。<br>
<h3>根本原因</h3>在调试了将近一个月之后，我们决定重新审视我们的测试用例和Kubernetes设置来帮助隔离问题。在RAV（回归和验证）测试的优化过程中，我们开始绘制所有可能影响容器性能的Kubernetes指标。我们确定的一个有趣的指标是CPU节流（<code class="prettyprint">container_cpu_cfs_throttled_seconds_total</code>）。一旦我们绘制出这个指标，我们就发现了令人震惊和有趣的结果。我们的一些最关键的服务正在被限制使用CPU，而我们却不知道为什么。此外，我们观察到，在我们的CI和开发/测试环境中，在启动某些特定容器时，经常发生这种情况，而这些容器在启动时，会运行一些CPU密集型操作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210724/2edf9b5e254325cac16229623e47aba5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210724/2edf9b5e254325cac16229623e47aba5.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们立即开始分析原因，并得出以下可能的原因：<br>
<ol><li>容器的<code class="prettyprint">CPU limit</code>设置不正确，导致应用程序很快达到最高CPU限制，从而导致Kubernetes对其进行节流。</li><li>像GC这样的后台活动，在一段时间后触发，导致CPU使用率增加。这也可能是由于基于JVM的应用程序的堆大小设置不正确造成的。</li><li>节点上的一些周期性CPU密集型活动消耗了大量cgroups可用的CPU周期。</li></ol><br>
<br><h3>什么是CPU节流（CPU Throttling）</h3>几乎所有的容器编排器都依赖于内核控制组（cgroup）机制来管理资源约束。当在容器编排器中设置硬CPU限制时，内核使用完全公平调度程序（CFS）来强制执行这些限制。CFS机制使用两种设置来管理CPU分配：配额和周期。当应用程序在给定的时间段内使用分配到的CPU配额时，CPU最大值不能超过配额值。<br>
<br>cgroup的所有CPU度量都位于<code class="prettyprint">/sys/fs/cgroup/cpu</code>，<code class="prettyprint">cpuacct/&lt;container></code>中。配额和周期设置在<code class="prettyprint">cpu.cfs_quota</code>和<code class="prettyprint">cpu.cfs_period</code>中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210724/b3d32317e2d272d7a47dc995a04af068.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210724/b3d32317e2d272d7a47dc995a04af068.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
你还可以在cpu.stat中查看节流指标。在cpu.stat中，你将发现：<br>
<ol><li>nr_periods -- cgroup中任何线程可运行的周期数</li><li>nr_throttled -- 应用程序被节流的可运行周期数</li><li>throttled_time -- cgroup中单个线程被节流的总时间</li></ol><br>
<br><h4>监视内存溢出</h4>另一个有趣的度量是由于内存溢出（OOM）导致的容器重新启动的数量。这突出显示哪些容器经常达到内存限制。<br>
<pre class="prettyprint">kube_pod_container_status_terminated_reason&#123;reason=”OOMKilled”&#125;)<br>
</pre><br>
<h3>解决方案</h3>> 因此，解决这个问题的一个快速方法是增加<strong>10-25%</strong>的<code class="prettyprint">CPU limit</code>，以确保峰值被击中的频率降低，或者完全避免。<br>
<br>在确定了根本原因之后，我们想出了一些可能的解决办法。我们考虑了以下因素：<br>
<br>CPU被节流主要是因为<code class="prettyprint">CPU limit</code>较低。实际上是由Cgroup行为所致。因此，解决这个问题的一个快速方法是增加<strong>10-25%</strong>的<code class="prettyprint">CPU limit</code>，以确保峰值被击中的频率降低，或者完全避免。这也不会影响pod启动所需的资源，因为<code class="prettyprint">CPU request</code>保持不变。<br>
<br>同时，对于那些IO或者CPU密集型应用程序，特别是那些使用基于JVM的应用程序，我们决定再次分析应用程序以确定正确的CPU和内存需求，因为JVM以高资源消耗而臭名昭著。从长远来看，调整JVM参数将是此类应用程序的正确解决方案。<br>
<h3>我们学到的和下一步行动</h3>这对我们来说是一次深刻的经历。我们意识到，一些看起来不那么重要（或者在本例中被忽视）的指标会对应用程序性能产生深远的影响。对CFS和cgroup以及内核如何处理资源虚拟化，我们也获得了一些惊人的见解。<br>
<br>在此基础上，我们为我们的主要应用程序提出了一个应用程序配置计划，并将CPU节流添加到我们的核心指标上，即应用程序性能差。<br>
<br><strong>原文链接：<a href="https://lambda.grofers.com/cpu-throttling-in-kubernetes-a-postmortem-b9b433d24b03">CPU Throttling in Kubernetes: A Postmortem</a>（翻译：钟涛）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            