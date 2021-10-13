
---
title: 'Periscope——Kubernetes的监控和跟踪仪表盘系统'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/5a17daa5d83349ca2b3ed5614c1f3119.png'
author: Dockone
comments: false
date: 2021-10-13 02:28:15
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/5a17daa5d83349ca2b3ed5614c1f3119.png'
---

<div>   
<br>【编者的话】Kubernetes已经被大多数企业接受，并且正在成为基础架构的基石。我们在迁移容器和管理集群时，如何有效的管理和监控容器状态和编排呢？Periscope也许是一种不错的选择。下面是Periscope的一篇介绍文章，可以作为入门和尝试。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/5a17daa5d83349ca2b3ed5614c1f3119.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/5a17daa5d83349ca2b3ed5614c1f3119.png" class="img-polaroid" title="0_VLZa808S_mP6CfCd.png" alt="0_VLZa808S_mP6CfCd.png" referrerpolicy="no-referrer"></a>
</div>
<br>
越来越多的公司转向微服务和容器，容器编排也在管理其基础架构过程中变得越来越重要。众所周知，过去几年中Kubernetes已经成为最具影响力的容器编排技术之一。<br>
<br>但Kubernetes已经变的相当复杂，部署和维护Kubernetes集群都是困难的事情。因此，市场上明显需要一种可以轻松、快速可查看Kubernetes集群的状态和健康状况的解决方案。<br>
<br>我们很高兴地推出<a href="http://getperiscopedashboard.com/">Periscope</a>——它是一个仪表板应用程序，可跨Kubernetes集群监控和跟踪关键指标。<br>
<h3>什么是Kubernetes？</h3>你可能只是听说过使用Kubernetes很折腾，但不太清楚这具体意味着什么。其实它的概念始于一家使用微服务构建的公司。这意味着将单体应用程序被分解成更小的、独立的部分（微服务），然后每个部分/微服务都被放入一个容器（一个轻量级的基础设施来运行每个部分/微服务）。<br>
<br>一旦我们有多个容器，我们就需要一种方法来管理或编排它们。Kubernetes是一种容器编排工具，可以管理调度容器的运行方式、结合负载平衡、跟踪资源分配、基于利用率进行扩展等等。<br>
<h3>为什么是Periscope？</h3>我们的行业正面临DevOps工程师短缺的困扰。更重要的是，Kubernetes是一项相当复杂且难以掌握的技术。很多工程师和小型企业开发者没有足够时间浏览Kubernetes官方文档，也没有精力花大量时间学习如何跟踪集群的状态和健康状况。<br>
<br>Periscope正好为此而生，下面我们来简单介绍一下Periscope：<br>
<br>Periscope是用于监控和跟踪Kubernetes Pod和节点的仪表板解决方案。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/6ee64bd80e2ebbeae3fff7fb01acd81e.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/6ee64bd80e2ebbeae3fff7fb01acd81e.gif" class="img-polaroid" title="1_apnuu62be-TOp9m-SiLSSw.gif" alt="1_apnuu62be-TOp9m-SiLSSw.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
Periscope与Prometheus服务器集成，然后显示任何工程师需要了解其集群状态和健康状况的核心指标。<br>
<br>工程师可以跨节点和Pod ，查看CPU、磁盘使用情况和内存使用情况。仪表板可以轻松查看不同时间范围内的异常的趋势。同时也向开发人员提供了可以更改所需的信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211009/0dea1bbc606fb587f13e2cf31b52c6d6.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211009/0dea1bbc606fb587f13e2cf31b52c6d6.gif" class="img-polaroid" title="1_e_GJP-gAUrSPkcWDUznakQ.gif" alt="1_e_GJP-gAUrSPkcWDUznakQ.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
Periscope是一个优秀的解决方案，特别是对于DevOps资源有限的工程师和公司。按照我们在<a href="https://github.com/oslabs-beta/Periscope">GitHub</a> 上的简单“入门”说明进行操作，在短短几分钟内，你将看到有关集群的一些最重要的详细信息。<br>
<br>让我们立即就开始着手尝试一下Periscope吧。<br>
<br><strong>原文链接：<a href="https://medium.com/@periscopeoslabs/periscope-the-kubernetes-monitoring-and-tracking-dashboard-e4e883b35db3">Periscope — The Kubernetes Monitoring and Tracking Dashboard</a>（翻译：ylzhang）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            