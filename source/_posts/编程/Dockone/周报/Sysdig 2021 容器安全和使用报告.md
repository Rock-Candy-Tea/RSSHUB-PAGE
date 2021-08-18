
---
title: 'Sysdig 2021 容器安全和使用报告'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/7f17e65103c46776349309f0c48844c5.png'
author: Dockone
comments: false
date: 2021-08-18 05:06:52
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/7f17e65103c46776349309f0c48844c5.png'
---

<div>   
<br>    在容器中运行的十大开源解决方案<br>
<br>开源改变了企业在云计算领域的面貌。它不仅推动了基础设施的创新，也推动了应用研发的创新。Sysdig能够自动发现容器内的进程，这让我们能够即时了解客户在生产中，运行<a href="https://www.alauda.cn/product/acpflag.html">云原生服务</a>的解决方案。以下是Sysdig客户部署的十大开源技术:<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210817/7f17e65103c46776349309f0c48844c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/7f17e65103c46776349309f0c48844c5.png" class="img-polaroid" title="1628841037815271.png" alt="1628841037815271.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>2021年的榜单包括了各种各样的服务——每一种服务都对应用程序的功能至关重要，包括:<br>
<br>• http服务器和反向代理解决方案- NGINX<br>
<br>• NoSQL, 关系和内存数据库解决方案-MongoDB, Postgres和Redis<br>
<br>• 日志和数据分析——Elasticsearch<br>
<br>• 编程语言和框架 — node. js, Go, and Java/JVMs<br>
<br>• 消息队列代理软件 — RabbitMQ<br>
<br>开源社区中可供选择的范围尽管很广，但在我们记录列表中的服务在过去三年中保持了惊人的一致。我们有意省略了<a href="https://www.alauda.cn/product/detail/id/240.html">Kubernetes</a>组件，如etcd、fluentd以及Falco。由于这些都是默认部署的，所以对于每个Kubernetes用户来说，它们都位于列表的顶部。去年，Node.js和Go(又名golang)的使用量都超过了Java。今年，Go的使用率从14%飙升至66%，增长了470%。由谷歌工程师创建的Go语言正在迅速成为开发云原生应用程序的首选语言。列表中前10的解决方案是用户普遍部署的可信服务。如果您正在市场上寻找类似的服务，那么您应该充分利用这些开源解决方案。<br>
<br>  自定义指标<br>
<br>自定义指标解决方案为开发人员和DevOps团队提供了一种方法来收集独一无二的数据。这种方法已经成为在生产环境中监控应用程序的主流方法。三个主要解决方案是JMX、StatsD和Prometheus，其中Prometheus连续第二年获得了胜利。<br>
<br>与去年同期相比，我们的客户使用Prometheus指标的比例上升到了62%，而去年为46%。随着新编程框架的广泛使用，JMX指标(用于Java应用程序)和StatsD等替代指标继续下降，同比分别下降了35%和15%。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210817/870d757c53462f657d5fa8a497ae0a60.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/870d757c53462f657d5fa8a497ae0a60.png" class="img-polaroid" title="640_(1).png" alt="640_(1).png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Prometheus exporters 排名<br>
<br>作为CNCF最成功的开源项目之一，Prometheus已经成为云原生服务监控的代名词。它现在被Kubernetes、OpenShift和Istio等项目作为监控指标广泛使用。此外，越来越多的“exporters”可以为大量的第三方解决方案提供详细的数据指标。在Sysdig为大规模环境提供完全兼容Prometheus的情况下，我们预计Prometheus的受欢迎程度将在我们的客户基础中持续增长。<br>
<br>对于当前的排名情况，我们查看了在prometheus.io上列出的每个github项目。并统计了每个项目的问题、星标数和forks的数量，并将结果与Dockerhub或其他仓库拉取数量相关联。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210817/7c5d3cacd65d078c8ebe149bcaa93ed1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/7c5d3cacd65d078c8ebe149bcaa93ed1.png" class="img-polaroid" title="640_(2).png" alt="640_(2).png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>容器<br>
<br>每年，我们都要详细统计一下容器的数量和活动，还包括容器的密度和寿命。通过对容器的采样和研究，也验证了企业正在实现的规模和效率。<br>
<br>    在每个团队中容器的运行数量<br>
（<a href="https://www.alauda.cn/news/blog_detail/id/518.html">容器的使用周期</a>）<br>
<br>为了解企业当前的规模，我们调研了每个客户在其基础设施上运行的容器数量。超过一半的客户使用250个或更少的容器。在高端市场，只有4%的客户管理着超过5000个容器。大多数客户是从小规模开始慢慢累积的，也有一些是开发人员为推动容器化加速软件交付主动增加了规模。据DevOps和云计算团队报告称，一旦容器的优势得到证明，越来越多的业务部门会关注新的平台，这些平台普及的速度将会加快。然而，企业应该应该考虑运行容器的原始数量，以及这些容器的大小(见下图)。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210817/731f33c2474603fe6844043ad399a8a3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/731f33c2474603fe6844043ad399a8a3.png" class="img-polaroid" title="640_(3).png" alt="640_(3).png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br> 镜像到底有多大?<br>
<br>尽管镜像的大小取决于应用程序，但根据我们的数据，镜像的平均值是376 MB。较大的10GB 镜像是一个极端值，除非有使用该镜像的场景，否则使用较大的镜像并不是最佳实践。大型镜像不仅需要更长的部署时间，还会降低发布速度，更可能会暴露更多的漏洞。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210817/9abdeac4a68bf397d4fb38eb7f98a46d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/9abdeac4a68bf397d4fb38eb7f98a46d.png" class="img-polaroid" title="640_(4).png" alt="640_(4).png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>  容器密度<br>
<br>每个主机的容器密度增加了33%!<br>
<br>在过去四年中，每一份报告中都显示容器数量中位数有所增加。然而，今年同比增幅仅为33%，而去年的增幅为100%。在将来这个数字可能会继续小幅增加，但这种密度的增加可能会以牺牲整体镜像大小为代价。尽管容器的主要目标是加速开发和部署，但在容器执行效率一定的前提下，许多团队正在提高硬件资源利用率以获取更好的效益。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210817/6067127fd27bbe8dbaea063548b5262e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210817/6067127fd27bbe8dbaea063548b5262e.png" class="img-polaroid" title="640_(5).png" alt="640_(5).png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>原文链接：<a href="https://www.alauda.cn/news/detail/id/514.html" rel="nofollow" target="_blank">https://www.alauda.cn/news/detail/id/514.html</a>     
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            