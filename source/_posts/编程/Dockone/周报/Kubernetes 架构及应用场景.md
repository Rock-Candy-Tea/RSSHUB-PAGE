
---
title: 'Kubernetes 架构及应用场景'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/c88a32249a94438791d138ff720b56ea.png'
author: Dockone
comments: false
date: 2021-08-20 10:08:06
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/c88a32249a94438791d138ff720b56ea.png'
---

<div>   
<br>Kubernetes，简称 K8s，是用 8 代替中间 8 个字符 “ubernete” 而成的缩写，是一个开源的，用于管理云平台中多个主机上的容器化的应用，Kubernetes 的目标是让部署容器化的应用简单并且高效（powerful），Kubernetes 提供了应用部署，规划，更新，维护的一种机制。<br>
<br>以下为本人学习 Kubernetes 的笔记，这篇博客是笔记的第一部分。<br>
<h3>Kubernetes 在企业中的应用场景</h3>首先我们了解一下 Kubernetes 的三个基本特点：<br>
<ul><li>可移植：支持公有云，私有云，混合云，多重云（multi-cloud）</li><li>可扩展：模块化，插件化，可挂载，可组合</li><li>自动化：自动部署，自动重启，自动复制，自动伸缩/扩展</li></ul><br>
<br><h4>自动化运维平台</h4>对于中小型企业，为了降本增效，使用 Kubernetes 来构建一套自动化运维平台，提供了应用部署，规划，更新，维护的一种机制。<br>
<br>对于大型互联网公司更要使用容器化部署。现在服务器越来越多，不可能都人工部署，需要使用自动化的运维平台来监控服务，来实现自动服务化的部署、运维。<br>
<h4>充分利用服务器资源</h4>举例说明：<br>
<br>假设现在有一个开发量为 200 个的请求，服务器配置为 2cpus 4G<br>
<br>静态请求：150（访问 CDN，Nginx，cache 等）<br>
<br>动态请求：50（访问数据库，需要把数据读入内存）<br>
<br>估算服务器资源（只考虑内存，不考虑程序响应时间RT，不考虑CPU切换时间）：<br>
<ul><li>假设一个静态请求进程占用 2M，一个动态请求进程占用 10M，则这 200 个请求并发占用：150×2M + 50×10M = 800M 内存</li><li>可以支持的 QPS（批发量，每秒查询率）为：200×4=800（因为 800M × 4 < 4G）</li><li>因此如果要充分利用服务器资源，需要达到 QPS=800，此时占用内存 3.2G（剩下 0.8G 给 OS 等）</li><li>实际上：800QPS 无法达到，还要考虑 RT、CPU 切换、内存等因素，那就保守把 QPS=300，但这时没能充分利用服务器的资源。更何况当下服务器配置可不止 2cpus 4G</li><li>容器化解决方案，在服务器部署多个容器，容器当中运行着我们部署的各种服务</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/c88a32249a94438791d138ff720b56ea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/c88a32249a94438791d138ff720b56ea.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>服务无缝迁移</h4>在开发环境开发，然后拿到测试环境去测试，但往往一上线就会有 bug，因为应用的运行、配置、管理、所有生存周期将与当前操作系统绑定，所以生产环境的不一致就可能导致错误。<br>
<br>使用容器化解决方案，每个应用可以被打包成一个容器镜像（红色圈起来表示把服务部署在容器中），使用容器可以在 开发 或 测试 的阶段，为应用创建容器镜像，这些镜像能够完全脱离环境，每个应用不需要与其余的应用堆栈组合，也不依赖于生产环境基础结构，这使得从研发到测试、生产能提供一致环境。使用 kubernetes 来管理这些容器，便能够实现服务的无缝迁移。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/c8520f036c79c5aaa398d71f1f44d6c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/c8520f036c79c5aaa398d71f1f44d6c4.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>服务部署模式变迁 & 服务部署变化问题的思考</h3><h4>服务部署模式是如何变迁的</h4><ul><li>物理机：传统的应用部署方式是通过插件或脚本来安装应用。这样做的缺点是应用的运行、配置、管理、所有生存周期将与当前操作系统绑定，这样做并不利于应用的升级更新/回滚等操作。</li><li>虚拟化（虚拟机）：当然上面的问题可以通过创建虚拟机的方式来实现某些功能，但是虚拟机本身就很占用资源，并不利于可移植性。（就是把服务部署在虚拟机中，达到分隔物理资源的作用——充分利用服务器资源）</li><li>容器部署：每个容器之间互相隔离，每个容器有自己的文件系统 ，容器之间进程不会相互影响，能区分计算资源。相对于虚拟机，容器能快速部署，由于容器与底层设施、机器文件系统解耦的，所以它能在不同云、不同版本操作系统间进行迁移。而且更轻量级、运行效率更快。</li></ul><br>
<br><h4>服务部署模式变化，带来了哪些问题</h4>前提条件：SOA 架构，微服务架构模式下，服务拆分越来越多，部署维护的服务越来越多，该如何管理？<br>
<ul><li>虚拟机服务部署方式（通过 OpenStack 软件提供可视化的方式来管理虚拟机）</li><li>容器化部署模式（通过 Kubernetes 软件管理容器，其实容器也可以看成一个虚拟机，只不过更轻量级）</li></ul><br>
<br>容器化部署问题：<br>
<ul><li>如何对服务横向扩展？</li><li>容器宕机怎么办？如何恢复？</li><li>重新发布版本如何更新且更新后不影响业务？</li><li>如何监控容器？</li><li>容器如何调度创建？</li><li>数据安全性如何保证？</li></ul><br>
<br>使用 Kubernetes 管理容器，以上问题都能够完美的解决 ✿✿ヽ(°▽°)ノ✿<br>
<h3>云架构 & 云原生</h3><h4>云和 Kubernetes 的关系</h4>云：使用容器构建的一套服务集群网络，云是由很多的容器构成。<br>
<br>Kubernetes：用来管理云中的容器<br>
<h4>云架构</h4><ul><li><br>IaaS：基础设施即服务<br>
<ul><li>用户角度：租用（购买或分配权限）云主机，用户不用考虑网络、DNS、存储和硬件环境等方面的问题。</li><li>运营商角度：提供网络、DNS、存储等这样的服务就叫做基础设置服务</li></ul></li><li><br>PaaS：平台即服务<br>
<ul><li>在平台上提供了很多服务，如 MySQL 服务、Redis 服务、MQ 服务、Elasticsearch 服务等等</li></ul></li><li><br>SaaS：软件即服务<br>
<ul><li>钉钉、财务管理等等，一些软件维护工作都是由运行商来做，用户只管体验软件提供的服务就行了。</li></ul></li><li><br>Serverless：server 服务，less 无 —— 无服务 不需要服务器<br>
<ul><li>站在用户角度考虑问题，用户只需要使用云服务器即可。</li><li>在云服务器上的所有的基础环境、软件环境都不需要考虑和维护，非常方便。</li></ul></li></ul><br>
<br>未来开发的趋势都是 Serverless，企业都构建了自己的私有云或者公有云环境。使用 Kubernetes 构建非常方便。<br>
<h4>云原生</h4>为了让应用程序（项目，服务软件）都运行在云上的解决方案，这样方案叫做云原生，有以下特点：<br>
<ul><li>容器化：所有的服务都必须部署在容器中。</li><li>微服务：Web 服务架构是微服务架构</li><li>CI/CD：可持续交互和可持续部署</li><li>DevOps：开发和运维密不可分</li></ul><br>
<br><h3>Kubernetes 架构原理</h3><h4>Kubernetes 的历史</h4>Kubernetes 是由 Google 公司用 Go 语言开发的。Google 在全球有相当多的服务器，当然需要一个管理软件。Google内部本身就有一个叫 Borg 的系统云平台管理工具，已经使用了十几年。后来参照 Borg 系统架构开发了 Kubernetes，主要用它来编排、管理容器，为容器化的应用提供部署运行、资源调度、服务发现和动态伸缩等一系列完整功能，提高了大规模容器集群管理的便捷性。<br>
<h4>Kubernetes 的架构</h4><strong>Kubernetes 集群（Cluster）</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/39c213565794f9d0a2673631a68625d6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/39c213565794f9d0a2673631a68625d6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
一个 Master 对应一群 Node 节点。<br>
<br><strong>Master 节点</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/96fd7ea590c83c4f547a4a6a29a24aa2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/96fd7ea590c83c4f547a4a6a29a24aa2.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>API Server：相当于 Kubernetes 的网关，所有的指令请求都必须经过 API Server</li><li>Scheduler：调度器，使用调度算法，把请求资源调度到某个 Node 节点</li><li>Controller：控制器，维护 Kubernetes 资源对象（CRUD：添加、删除、更新、修改）</li><li>etcd：存储资源对象（可以服务注册、发现等等）</li></ul><br>
<br><strong>Node 节点</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/a527e4b8ec3d211887cd99d1ae92f9f9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/a527e4b8ec3d211887cd99d1ae92f9f9.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Docker：运行容器的基础环境，容器引擎</li><li>kubelet：每个 Node 节点都有一份 kubelet，在 Node 节点上的资源操作指令由 kuberlet 来执行，Scheduler 把请求交给 API，然后 API Server 再把信息指令数据存储在 etcd 里，于是 kuberlet 会扫描 etcd 并获取指令请求，然后去执行</li><li>kube-proxy：代理服务，负载均衡</li><li>Fluentd：日志收集服务</li><li>Pod：Kubernetes 管理的基本单元（最小单元），Pod 内部是容器。Kubernetes 不直接管理容器，而是管理 Pod。</li></ul><br>
<br><h4>回顾架构特点</h4><ul><li>Kubernetes 是用来管理容器的，但是不直接操作容器，最小的操作单元是 Pod（间接管理容器）</li><li>一个 Master 对应一群 Node 节点。</li><li>Master 节点不存储容器，只负责调度，网关，控制器，资源对象存储等</li><li>容器存储在 Node 节点 的 Pod 内部</li><li>Pod 内部可以有一个或多个容器</li><li>kubelet 负责本地的 Pod 的维护，CRUD</li><li>kube-proxy 负责负载均衡，在多个 Pod 间负载均衡</li></ul><br>
<br>原文链接：<a href="https://blog.csdn.net/qq_43280818/article/details/106648372" rel="nofollow" target="_blank">https://blog.csdn.net/qq_43280 ... 48372</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            