
---
title: 'KUR8：可视化Kubernetes集群'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f61cb965bd8b92f84d20d80f3788fd6b.png'
author: Dockone
comments: false
date: 2021-08-16 02:18:50
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f61cb965bd8b92f84d20d80f3788fd6b.png'
---

<div>   
<br>自微服务架构这个术语在2011年的某次软件架构师大会上被首次提出时，它就在各个组织中引起了轩然大波。<br>
<br>微服务指的是应用程序由多个独立的组件组成。微服务的优势在于，它更有利于敏捷开发，以及成本控制和资源分配。并且微服务逐渐成为主流。根据Nginx最近的一项调查，36%的受访企业目前正在使用微服务，另有26%的企业目前正处于调研阶段。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/f61cb965bd8b92f84d20d80f3788fd6b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f61cb965bd8b92f84d20d80f3788fd6b.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>微服务生态链相关技术</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/a00e51d9586058d6afa0abcb218f083d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/a00e51d9586058d6afa0abcb218f083d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>容器化工具</h4>微服务应用程序通常被封装在Docker容器中，这些容器可以独立维护、部署和弹性伸缩。容器化使您的应用程序能够独立于主机环境、可移植并易于在持续集成（CI）和持续交付（CD）管道中使用。<br>
<br>随着微服务的兴起，我们也看到了一些新技术的出现，如Docker和Kubernetes，这些工具负责创建和管理容器。<br>
<h4>容器化编排工具</h4>在Kubernetes中，容器被包裹在Pod中。且Pod是Kubernetes中最小可调度单位。Pod中的容器共享相同的本地网络和资源，使Pod内部通信变得更容易。Pod使用kubelet与Kubernetes API和集群的其他部分通信，kubelet存在于集群中的每个节点。当某个容器的流量很大时，Kubernetes使用负载均衡器将网络流量分配到不同的Pod，以确保集群的稳定性。<br>
<br>从本质上讲，Kubernetes集群由大到小，从集群，节点，Pod，容器构成，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/faae2520596d6473e5e943c6ce802ad1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/faae2520596d6473e5e943c6ce802ad1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图仅包含两个节点，每个节点包含两个Pod。然而，在实践中，节点和Pod的数量可以非常大，这意味着Kubernetes集群可能包含数千个节点，每个节点包含数百个Pod。开发人员通常很难定位Kubernetes集群中单个Pod的信息。此外，开发人员经常需要访问特定的指标来监视基础设施，以提高操作效率。针对以上场景，<a href="https://github.com/oslabs-beta/KUR8">KUR8</a>将成为一个非常有价值的工具。<br>
<h3>KUR8简介</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/5ca69fd8437177c1b81f7f7f4fc81863.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/5ca69fd8437177c1b81f7f7f4fc81863.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>KUR8是一个开源的基于Prothemeus和时间序列数据库的Web应用程序，集Kubernetes分析、监控和可视化于一体，可用于查询、警报和创建自定义图表。</li><li>KUR8帮助您绘制应用程序和基础设施的逻辑拓扑图，使您的团队能够更好的理解和控制Kubernetes集群。</li><li>Prometheus是一款基于微服务的免费开源的事件监控工具，使用时间序列数据库实时记录指标数据，并使用拉取数据的方式来查询信息。</li><li>基于RBAC授权机制，让您可以一目了然地监控Kubernetes集群。</li></ul><br>
<br><h3>KUR8的功能简介</h3>我们将用一个实例来演示KUR8的功能。<br>
<br>让我们从KUR8的structure页面开始：<br>
<br>根据您的集群信息，structure页面将呈现主节点和工作节点的配置信息，每个节点的Pod信息，以及每个节点的容器数量。structure页面还负责统计每个Pod内的容器数量，以及相关的部署状态、调度器、容器ID等信息。并提供Ingress信息，以显示集群内对应的服务名和端口信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/c99ffac853c78f729684e5ba49785a67.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/c99ffac853c78f729684e5ba49785a67.gif" class="img-polaroid" title="1-min.gif" alt="1-min.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
切换到metrics页面和custom页面：<br>
<br>metrics页面显示一些默认的PromQL查询，用于监视Kubernetes集群，例如每个Kubernetes命名空间的Pod数量，哪些Pod处于未就绪状态，以图表、柱状图、折线图的方式实时显示容器的CPU和内存使用情况。此外，KUR8允许开发人员创建自定义指标数据页面，开发人员可以使用PromQL创建查询，并将自定义图表保存在custom页面。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/58076b2b16b36f3bf48d813bdf6f0683.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/58076b2b16b36f3bf48d813bdf6f0683.gif" class="img-polaroid" title="2-min_(2)_(1)_(1).gif" alt="2-min_(2)_(1)_(1).gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/cdde309e80c0812d655c38bd8bbd60c6.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/cdde309e80c0812d655c38bd8bbd60c6.gif" class="img-polaroid" title="3-min.gif" alt="3-min.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
最后，让我们看看Alerts页面：<br>
<br>该页面显示所有Prometheus警报（包括自定义警报），显示正在触发的警报以及它们属于哪个规则组，并显示每个警报的名称、运行状况、状态、评估时间、严重性、标签和摘要等信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210815/37cba45c9d8d7617fc058f9275a4216d.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210815/37cba45c9d8d7617fc058f9275a4216d.gif" class="img-polaroid" title="4-min.gif" alt="4-min.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>KUR8是如何工作的</h3><h4>第一部：部署KUR8</h4>KUR8要求您的Kubernetes集群处于运行状态。<br>
<br>您可以从Docker Hub拉取到所有KUR8的镜像。<br>
<br>1、 我们建议使用<a href="https://github.com/oslabs-beta/Kur8/blob/dev/infra/k8s/kur8-depl.yaml">kur8-depl.yaml</a>来部署KUR8<br>
<br>2、运行以下命令：<br>
<pre class="prettyprint">kubectl apply -f kur8-depl.yaml<br>
</pre><br>
3、此外，为了允许读取API的资源，您必须配置一组权限。我们已经使用RBAC授权设置了一个YAML文件，您可以使用命令行运行<a href="https://github.com/oslabs-beta/Kur8/blob/dev/infra/k8s/fabric8-rbac.yaml">fabric8-rbac.yaml</a><br>
<pre class="prettyprint">kubectl apply -f fabric8-rbac.yaml<br>
</pre><br>
4、使用端口转发，在端口3068上打开KUR8。<br>
<pre class="prettyprint">kubectl port-forward deployment/kur8-depl 3068:3068<br>
</pre><br>
5、然后，打开浏览器<a href="http://localhost:3068/" rel="nofollow" target="_blank">http://localhost:3068</a>。<br>
<br>通过浏览器左侧的structures选项卡，您可查询到Kubernetes的集群架构。<br>
<h4>第二部：部署Prometheus</h4>如果你还没有安装Prometheus，请按以下步骤安装Prometheus：<br>
<br>1、在KUR8文件夹中运行以下命令：<br>
<pre class="prettyprint">kubectl create -f infra/manifests/setup<br>
</pre><br>
2、等上一步完成后，运行以下命令：<br>
<pre class="prettyprint">kubectl create -f infra/manifests/<br>
</pre><br>
3、如果你想连接KUR8和Prometheus，通过以下方式打开端口：<br>
<pre class="prettyprint">kubectl — namespace monitoring port-forward svc/prometheus-k8s 9090<br>
</pre><br>
您也可以在<a href="http://localhost:3068/" rel="nofollow" target="_blank">http://localhost:3068</a>上查看KUR8中的Prometheus选项卡，以查看和创建您的自定义仪表板。<br>
<h3>接下来？</h3>目前，KUR8正处于Alpha阶段，由OSLabs技术加速器项目创建。我们一直在努力让KUR8在未来变得更加流线型。如果您有任何对产品有益的改进策略或建议，请随时联系我们。我们感谢来自开发者社区的反馈！测试一下，让我们知道你的意见。<br>
<br><strong>原文链接：<a href="https://medium.com/@ivkookie9/kur8-start-visualizing-your-clusters-topology-and-metrics-b5ca89452584">KUR8: Start Visualizing Your Cluster’s Topology and Metrics</a>  （翻译：钟涛）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            