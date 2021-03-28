
---
title: '如何在 Kubernetes 上扩展微服务'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/8b47a0663e8ef35fcf3c5ff535db9055.png'
author: Dockone
comments: false
date: 2021-03-28 12:10:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/8b47a0663e8ef35fcf3c5ff535db9055.png'
---

<div>   
<br>【编者的话】使用微服务可以对应用程序的性能进行更精细的控制。微服务有许多扩展选项，本文概述了一些使用 Kubernetes 扩展微服务的简单技术。<br>
<br>基于微服务的应用程序可以以多种方式扩展。我们可以通过扩展以支持更大的团队开发，或者来获得更好的性能。这样，应用程序可以具有更高的容量，并能处理更大的工作负载。<br>
<br>使用微服务可以对应用程序的性能进行更精细的控制。我们可以轻松把握微服务的性能，以发现在需求高峰时性能不佳、工作过度或过载的服务。图 1 展示了如何使用 Kubernetes 仪表盘来了解微服务的 CPU 和内存使用情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/8b47a0663e8ef35fcf3c5ff535db9055.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/8b47a0663e8ef35fcf3c5ff535db9055.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1：在 Kubernetes 仪表盘中查看微服务的 CPU 和内存使用情况</em><br>
<br>对于微服务，我们有许多扩展选项，本文中将概述一些使用 Kubernetes 扩展微服务的简单技术：<br>
<ul><li>垂直扩展整个集群</li><li>水平扩展整个集群</li><li>水平扩展单个微服务</li><li>弹性伸缩整个集群</li><li>弹性伸缩单个微服务</li></ul><br>
<br>扩展通常需要对集群进行冒险的配置更改。因此，我们不要直接对生产集群进行这些更改，最好是创建一个新集群，并使用蓝绿部署或类似的部署策略，以避免更改基础结构带来的风险。<br>
<h3>垂直扩展集群</h3>随着应用程序的增长，我们可能会遇到这样的情况：集群没有足够的计算资源、内存或存储来运行我们的应用程序。随着我们添加新的微服务，最终使集群中的节点达到最大化。<br>
<br>此时，我们必须增加集群的可用资源总量。在 Kubernetes 集群上扩展微服务时，我们可以使用垂直或水平扩展。图 2 展示了 Kubernetes 的垂直扩展效果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/fd4cf4cf01d3c1a238e204b3c85504a6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/fd4cf4cf01d3c1a238e204b3c85504a6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 2：通过增加虚拟机（VM）的大小垂直扩展集群</em><br>
<br>我们通过增加节点池中虚拟机（VM）的规模来扩展集群。在此示例中，我们增加了三个小型 VM 的大小，因此现在有了三个大型 VM。我们没有更改虚拟机的数量，我们只是增加了它们的大小，即垂直扩展了我们的 VM。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/54296bdb31f536ac14728ef43e92101b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/54296bdb31f536ac14728ef43e92101b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 3：使用 Terraform 垂直扩展集群</em><br>
<br>图 3 是从 Terraform 代码中摘录的，该代码在 Azure 上配置了一个集群，将 vm_size 字段从 Standard_B2ms 更改为 Standard_B4ms。这将升级 Kubernetes 节点池中每个 VM 的大小。现在，我们有四个 CPU，而不是两个 CPU（每个 VM 一个）。作为此更改的一部分，VM 的内存和硬盘驱动器也增加了。<br>
<br>集群中仍然只有一个 VM，但 VM 的大小增加了。在此示例中，扩展集群就像更改代码一样简单。这就是基础架构即代码的力量，这是将基础架构配置存储为代码，并通过提交触发连续交付（CD）流水线的代码更改来对基础架构进行更改。<br>
<h3>水平扩展集群</h3>除了垂直扩展集群外，我们还可以水平扩展集群。VM 可以保持相同的大小，只需添加更多 VM。<br>
<br>通过将更多的虚拟机添加到集群中，我们可以将应用程序的负载分散到更多的计算机上。图 4 展示了如何将集群从三个 VM 扩展到六个 VM。每个 VM 的大小保持不变，但是通过拥有更多的 VM，我们可以获得更多的计算能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/7847bdf885268ecc9cd97574dee1fd59.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/7847bdf885268ecc9cd97574dee1fd59.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 4：通过增加虚拟机数量来水平扩展集群</em><br>
<br>图 5 是 Terraform 代码的一部分，该代码将更多的 VM 添加到节点池中。回到图 3，我们将 node_count 设置为 1，但是在这里我们将其更改为 6。请注意，我们将 vm_size 字段还原为较小的 Standard_B2ms。在此示例中，我们增加了虚拟机的数量，但没有增加它们的大小。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/e062fe36c71f47af72e04a8f71c2e672.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/e062fe36c71f47af72e04a8f71c2e672.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 5：使用 Terraform对集群进行水平伸缩</em><br>
<br>通常，水平伸缩会更好，因为它比垂直伸缩便宜，使用许多较小的 VM 会比使用较少但较大且价格更高的 VM 便宜。<br>
<h3>水平扩展单个微服务</h3>假设我们的集群已扩展到足够大的规模，可以托管所有具有良好性能的微服务，那么当单个微服务过载时，我们该怎么办？<br>
<br>每当微服务成为性能瓶颈时，我们就可以水平扩展它以在多个实例上分配其负载。如图 6 所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/e3618a339309004a002cf836fdea9a3e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/e3618a339309004a002cf836fdea9a3e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 6：通过复制水平扩展微服务</em><br>
<br>这样可以有效地为这个特定的微服务提供更多的计算资源、内存和存储，以便它处理更大的工作负载。<br>
<br>同样，我们可以使用代码进行此更改。我们可以通过在 Kubernetes deployment 或 Pod 的规范中设置副本字段来实现此目的，如图 7 所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/a9717031188b2a0cff3f60f9032508a1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/a9717031188b2a0cff3f60f9032508a1.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 7：使用 Terraform 水平扩展微服务</em><br>
<br>我们不仅可以扩展单个微服务以提高性能，还可以水平扩展微服务以实现冗余，从而创建更具容错能力的应用程序。通过具有多个实例，每当一个实例发生故障时，就有其他实例来承担负载。这可以允许微服务的失败实例重新启动并重新开始工作。<br>
<h3>集群的弹性伸缩</h3>现在我们可以考虑弹性伸缩，这是一种可以自动动态地伸缩集群以满足不同级别需求的技术。<br>
<br>每当需求低时，Kubernetes 可以自动释放不需要的资源。在需求高峰时，将分配新资源来满足增加的工作负载。这样可以节省大量成本，因为在任何给定时刻，我们只为处理应用程序工作负载所需的资源付费。<br>
<br>我们可以在集群级别使用弹性伸缩来自动增长接近其资源极限的集群。图 8 显示了如何启用 Kubernetes 自动伸缩器并设置节点池的最小和最大大小。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/caeaf1725dc5c57faabf82d33d1d9c51.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/caeaf1725dc5c57faabf82d33d1d9c51.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 8：使用 Terraform 为集群启用弹性伸缩</em><br>
<h3>单个微服务的弹性伸缩</h3>我们还可以为单个微服务启用弹性伸缩。图 9 是 Terraform 代码的示例，该示例为微服务提供了“突发式”功能。微服务的副本数量会动态伸缩，以适应微服务的各种工作负载。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210325/14015a2024097bf20b99c176bfa35f3a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210325/14015a2024097bf20b99c176bfa35f3a.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 9：使用 Terraform 为微服务启用弹性伸缩</em><br>
<br>要了解有关 Kubernetes 中 Pod 自动伸缩的更多信息，请参阅 Kubernetes docs：<a href="https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/" rel="nofollow" target="_blank">https://kubernetes.io/docs/tas ... cale/</a><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/daMyOgEUzWm-zZHCRq_YMQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/daMyOgEUzWm-zZHCRq_YMQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            