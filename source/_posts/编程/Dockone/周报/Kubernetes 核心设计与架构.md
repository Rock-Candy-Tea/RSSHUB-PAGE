
---
title: 'Kubernetes 核心设计与架构'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/fa8a7e0097d43363a205a48391644ffc.png'
author: Dockone
comments: false
date: 2021-04-30 12:04:21
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/fa8a7e0097d43363a205a48391644ffc.png'
---

<div>   
<br>容器实际上是由 Linux Namespace、Linux Cgroups 和 rootfs 这 3 种技术构建出来的进程的隔离环境。<br>
<br>不难看出，一个正在运行的 Linux 容器，其实可以被“一分为二”地看待：<br>
<ul><li>一组联合挂载在 /var/lib/docker/aufs/mnt 上的 rootfs，这一部分称为容器镜像（container image），是容器的静态视图；</li><li>一个由 Namespace + Cgroups 构成的隔离环境，这一部分称为容器运行时（container runtime），是容器的动态视图。</li></ul><br>
<br>作为开发者，我并不关心容器运行时的差异。因为在整个“开发——测试——发布”的流程中，真正承载容器信息进行传递的，是容器镜像，而非容器运行时。<br>
<br>这个重要假设，正是容器技术圈在 Docker 项目成功后不久，就迅速走向容器编排这个“上层建筑”的主要原因：作为一家云服务提供商或者基础设施提供商，我只要能够将用户提交的 Docker 镜像以容器的方式运行起来，就能成为这张非常热闹的容器生态图上的一个承载点，从而将整个容器技术栈上的价值沉淀在我的节点上。<br>
<br>更重要的是，只要从我这个承载点向 Docker 镜像制作者和使用者方向回溯，整条路径上的各个服务节点，比如 CI/CD、监控、安全、网络、存储等，都有可以发挥和盈利的空间。这正是所有云计算提供商如此热衷于容器技术的重要原因：通过容器镜像，他们可以和潜在用户（开发者）直接关联起来。<br>
<br>从一位开发者和单一的容器镜像，到无数开发者和庞大的容器集群，容器技术实现了从“容器”到“容器云”的飞跃，标志着它真正得到了市场和生态的认可。<br>
<br>容器从开发者手里的一个小工具，一跃成为了云计算领域的绝对主角；而能够定义容器组织和管理规范的容器编排技术，则当仁不让地坐上了容器技术领域的“头把交椅”。其中最具代表性的容器编排工具，当属 Docker 公司的 Compose + Swarm 组合，以及谷歌公司共同主导的 Kubernetes 项目。<br>
<br>跟很多基础设施领域先有工程实践、后有方法论的发展路线不同，Kubernetes 项目的理论基础要比工程实践走得靠前得多，这当然要归功于谷歌公司在 2015 年 4 月发布的 Borg 论文。<br>
<br>Borg 系统一直以来都被誉为谷歌公司内部最强大的“秘密武器”。虽然略显夸张，但这个说法倒不算是吹牛。这是因为相比于 Spanner、BigTable 等相对上层的项目，Borg 的责任是承载谷歌公司整个基础设施的核心依赖。在谷歌公司已经公开发表的基础设施体系论文中，Borg 项目当仁不让地位居整个基础设施技术栈的最底层（见图 1）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210429/fa8a7e0097d43363a205a48391644ffc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/fa8a7e0097d43363a205a48391644ffc.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 1 谷歌的基础设施栈</em><br>
<br>图 1 来自谷歌 Omega 论文第一作者的博士毕业论文。它描绘了当时谷歌已经公开发表的整个基础设施栈。在这张图中，你既能看到 MapReduce、BigTable 等知名项目，也能看到 Borg 和它的继任者 Omega 位于整个技术栈的最底层。<br>
<br>正是由于这样的定位，Borg 可以说是谷歌最不可能开源的一个项目。而得益于 Docker 项目和容器技术的风靡，它最终以另一种方式与开源社区见面，这种方式就是 Kubernetes 项目。<br>
<br>所以，相比于“小打小闹”的 Docker 公司和“旧瓶装新酒”的 Mesos 社区，Kubernetes 项目从一开始就比较幸运地站在了他人难以企及的高度：在它的成长阶段，这个项目每一个核心特性的提出，几乎都脱胎于 Borg/Omega 系统的设计与经验。更重要的是，这些特性在开源社区落地的过程中，又在整个社区的合力之下得到了极大的改进，修复了遗留在 Borg 体系中的很多缺陷和问题。<br>
<br>所以，尽管在发布之初被批评是“曲高和寡”，但 Kubernetes 项目在 Borg 体系的指导下，逐步展现出了其独有的先进性与完备性，而这些特质才是一个基础设施领域开源项目赖以生存的核心价值。<br>
<br>为了更好地理解这两种特质，不妨从 Kubernetes 项目的设计与架构说起。首先，请思考这样一个问题：Kubernetes 项目主要解决的问题是什么？编排？调度？容器云？还是集群管理？<br>
<br>实际上，这个问题可能你很难立即给出答案。但至少作为用户来说，我们希望 Kubernetes 项目带来的体验是确定的：现在我有了应用的容器镜像，请帮我在一个给定的集群上运行这个应用。我还希望 Kubernetes 能给我提供路由网关、水平扩展、监控、备份、灾难恢复等一系列运维能力。<br>
<br>等等，这些功能听起来好像有些耳熟，这不正是经典 PaaS（比如 Cloud  Foundry）项目的能力吗？而且，有了 Docker 之后，我根本不需要什么 Kubernetes、PaaS，只要使用 Docker 公司的 Compose + Swarm 项目，就完全可以很方便地自己做出这些功能！所以，如果 Kubernetes 项目只  是停留在拉取用户镜像、运行容器，以及提供应用运维功能的话，那么别说跟“原生”的 Docker Swarm 项目竞争了，哪怕跟经典的 PaaS 项目相比，也难有优势可言。<br>
<br>实际上，在定义核心功能的过程中，Kubernetes 项目正是依托 Borg 项目的理论优势，才在短短几个月内迅速站稳脚跟，进而确定了一个如图 2 所示的全局架构。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210429/9e874273e23e90d44c84b513d25087d2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210429/9e874273e23e90d44c84b513d25087d2.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 2  Kubernetes 项目的全局架构</em><br>
<br>从这个架构中我们可以看到，Kubernetes 项目的架构跟它的原型项目 Borg 非常类似，都由 Master 和 Node 两种节点组成，而这两种角色分别对应控制节点和计算节点。其中，控制节点，即 Master 节点，由 3 个紧密协作的独立组件组合而成，分别是负责 API 服务的 kube-apiserver、  负责调度的 kube-scheduler，以及负责容器编排的 kube-controller-manager。整个集群的持久化数据，则由 kube-apiserver 处理后保存在 etcd 中。<br>
<br>计算节点上最核心的部分，是一个名为 kubelet 的组件。在 Kubernetes 项目中，kubelet 主要负责同容器运行时（比如 Docker 项目）交互。而这种交互所依赖的是一个称作 CRI（container  runtime  interface）的远程调用接口，该接口定义了容器运行时的各项核心操作，比如启动一个容器需要的所有参数。<br>
<br>这也是为何 Kubernetes 项目并不关心你部署的是什么容器运行时、使用了什么技术实现，只要你的容器运行时能够运行标准的容器镜像，它就可以通过实现 CRI 接入 Kubernetes 项目。而具体的容器运行时，比如 Docker 项目，则一般通过 OCI 这个容器运行时规范同底层的 Linux 操作系统进行交互，即把 CRI 请求翻译成对 Linux 操作系统的调用（操作 Linux  Namespace 和 Cgroups 等）。<br>
<br>此外，kubelet 还通过 gRPC 协议同一个叫作 Device Plugin 的插件进行交互。这个插件，是 Kubernetes 项目用来管理 GPU 等宿主机物理设备的主要组件，也是基于 Kubernetes 项目进行机器学习训练、高性能作业支持等工作必须关注的功能。<br>
<br>kubelet 的另一个重要功能，则是调用网络插件和存储插件为容器配置网络和持久化存储。这两个插件与 kubelet 进行交互的接口，分别是 CNI（container networking interface）和 CSI（container storage interface）。<br>
<br>实际上，kubelet 这个奇怪的名字来自 Borg 项目中的同源组件 Borglet。不过，如果你浏览过 Borg 论文，就会发现这个命名方式可能是 kubelet 组件与 Borglet 组件的唯一相似之处。这是因为 Borg 项目并不支持这里所讲的容器技术，而只是简单地使用了 Linux Cgroups 对进程进行限制。这就意味着，像 Docker 这样的“容器镜像”在 Borg 中是不存在的，Borglet 组件自然不需要像 kubelet 这样考虑如何同 Docker 进行交互、如何管理容器镜像的问题，也不需要支持 CRI、CNI、CSI 等诸多容器技术接口。<br>
<br>可以说，kubelet 完全就是为了实现 Kubernetes 项目对容器的管理能力而重新实现的一个组件，与 Borg 之间并没有直接的传承关系。<br>
<br>本文节选自《深入剖析Kubernetes》，经出版社授权转载。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            