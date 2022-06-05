
---
title: 'Kubernetes 1.24新特性解读'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220507/bc892d719898b11a5a911d56a4ddfab7.png'
author: Dockone
comments: false
date: 2022-06-05 14:09:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220507/bc892d719898b11a5a911d56a4ddfab7.png'
---

<div>   
<br>北京时间5月4日， Kubernetes 1.24版正式发布了，像之前的几个版本一样，给Kubernetes带来了大大小小多达几十项的变化。几十项涉及到基础设施、运维和应用开发的方方面面，可能很难有人能够全部搞懂，本文也不打算一一罗列，谨结合自己的体会，谈几个应用开发者可能比较关注的点。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220507/bc892d719898b11a5a911d56a4ddfab7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220507/bc892d719898b11a5a911d56a4ddfab7.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Kubernetes 1.24版Logo：观星者</em><br>
<br>首当其冲是对dockershim支持的正式移除。在一年多以前，Kubernetes 1.20版本宣布对Docker的支持置为“废弃（Deprecated）”状态，不再演进，并“将在未来的某个版本中移除（Will be removed）”。这次发布的1.24版即是所谓“正式移除Docker支持”的版本，然而，Docker公司却宣称，在Kubernetes环境中，可以继续使用Docker，其Docker Desktop产品的用户仍然能够无缝使用Kubernetes的最新发布版本。这是怎么回事？<br>
<br>事实上，仔细阅读Kubernetes官方的1.24版的Change Log，你会发现，其对于Docker支持的表述与一年前的1.20版有微妙的不同。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220507/1de0475e20dd8ca9a8aa561b78f638e9.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220507/1de0475e20dd8ca9a8aa561b78f638e9.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>1.20版Change Log 截图</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220507/3065e01404d1b32b3449fdfafc567f81.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220507/3065e01404d1b32b3449fdfafc567f81.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>1.24版Change Log截图</em><br>
<br>Kubernetes移除Docker主要是因为Docker长期以来不支持Kubernetes主推的CRI容器运行时接口标准，因此Kubernetes社区维护了一个dockershim组件专门用来对接Docker。<br>
<br>这在当年Docker具备垄断地位时非常有必要，随着containerd和kata等容器运行时发展成熟，尤其是containerd在生产环境中大量使用，Kubernetes社区决定不再维护dockershim。<br>
<br>然而，最近两年Mirantis（已于2019年11月收购Docker Enterprise部门）和Docker公司在对Kubernetes的支持上不断投入，目前社区里已经有一个独立于Kubernetes并且支持CRI的“shim”：cri-dockerd，继续实现Kubernetes与Docker的对接。<br>
<br>Docker Desktop以其优秀的用户体验深得很多开发者的青睐，自Kubernetes 1.20版本发布以来，笔者就在寻找Docker Desktop的替代品，也尝试了不少，但目前还没有找到能够与之媲美的产品。cri-dockerd让Kubernetes 1.24能够继续对接Docker容器运行时，这意味着用户可以像以前一样在Docker Desktop中一键安装并无缝使用最新版的Kubernetes，对于开发者来说无疑是个好消息。<br>
<br>同时由于Docker Image已经成为了各类容器运行时使用的标准镜像格式，开发使用Docker，生产或者发布到客户的环境中使用的是其他容器运行时可能会成为一种长期存在的普遍现象。<br>
<br>第二个想聊一聊的是Kubernetes的Job。对于批处理类的应用负载，Kubernetes提供了Job资源来支持。但是当我们要运行并行处理或者分布式计算的Job时，会遇到一个问题：Kubernetes中的Pod是动态创建和回收的，这也是基于Kubernetes Job来运行批处理负载的优势之一，因为资源能够在需要时才被占用，用完可以立即回收，然而这却会导致任务在往各个Pod分配时缺少依据（基于机器的并行计算系统中往往需要将主机名称等相对固定的标识作为任务调度的输入）。<br>
<br>在早些版本中，Kubernetes官方建议引入消息队列或者内存数据库来给Job的各个Pod分配编号以解决该<a href="https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/">问题</a>，这无疑提升了应用的复杂度且引入了第三方组件的运维问题。在Kubernetes 1.24版本中，有一项从Beta阶段提升为正式特性的功能叫做“Indexed Job”，该特性会给同一个Job的各个Pod在环境变量中注入一个编号索引，应用可以根据这个编号为各个Pod分配具体的task。<br>
<br>去年该特性还在beta阶段时，笔者尝试将一个基于Kubernetes Job的云原生分布式图计算应用从依赖外部消息队列分配task改为Indexed Job，应用的可维护性、稳定性和资源消耗都得到了明显的改善。<br>
<br>第三个推荐开发者关注的特性是gPRC健康状态探针已经是beta状态了，这是一个很值得期待的功能。gRPC协议在云原生应用中得到日益广泛的使用，然而Kubernetes过去一直缺少gRPC原生的健康状态探针支持，使得对gRPC服务的启动、存活和就绪状态检查都需要依赖其他手段，官网有一篇文章对这些技术手段进行了<a href="https://kubernetes.io/blog/2018/10/01/health-checking-grpc-servers-on-kubernetes/">介绍</a>，从文章中不难看出，这些方法对于应用迁移上Kubernetes的成本和云原生应用的可维护性、可用性都会有一定的影响。在Kubernetes原生支持gRPC探针后，这些问题得到了有效的解决，采用gRPC协议构建云原生应用的同仁们可以期待一下这个特性未来从beta状态变为正式可用。<br>
<br>最后想到一个非常有意思的更新，1.24版本以后，kubeadm安装Kubernetes集群时，不再给运行控制面组件的节点标记为“master”，因为这个词被认为是“具有攻击性的、无礼的（offensive）”。近几年，一些用master-slave来表示主-从节点的计算机系统纷纷改掉术语，slave前两年就已经销声匿迹了，现在看来master也不能用。
                                
                                                              
</div>
            