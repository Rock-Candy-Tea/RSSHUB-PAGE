
---
title: 'Kubernetes之前世今生'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/546e4dad6db76d9554b3b223ea0583cd.jpeg'
author: Dockone
comments: false
date: 2021-08-15 02:17:44
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/546e4dad6db76d9554b3b223ea0583cd.jpeg'
---

<div>   
<br>虽然 <code class="prettyprint">Docker</code> 已经很强大了，但是在实际使用上还是有诸多不便，比如集群管理、资源调度、文件管理等等。那么在这样一个百花齐放的容器时代涌现出了很多解决方案，比如 <code class="prettyprint">Mesos</code>、<code class="prettyprint">Swarm</code>、<code class="prettyprint">Kubernetes</code> 等等，其中谷歌开源的 <code class="prettyprint">Kubernetes</code> 是作为老大哥的存在。<br>
<ul><li>Kubernetes 官方文档：<a href="https://kubernetes.io/docs/reference/" rel="nofollow" target="_blank">https://kubernetes.io/docs/reference/</a></li><li>Kubernetes 官方 Github 地址：<a href="https://github.com/kubernetes/kubernetes" rel="nofollow" target="_blank">https://github.com/kubernetes/kubernetes</a></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/546e4dad6db76d9554b3b223ea0583cd.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/546e4dad6db76d9554b3b223ea0583cd.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>发展经历</h3>历史总是不尽的相同，好的总会取代坏的。<br>
<br><code class="prettyprint">Kubernetes</code> 是希腊语『舵手』的意思，它最开始由 <code class="prettyprint">Google</code> 的几位软件工程师创立，深受公司内部 <code class="prettyprint">Borg</code> 和 <code class="prettyprint">Omega</code> 项目的影响，很多设计都是从 <code class="prettyprint">Borg</code> 中借鉴的，同时也对 <code class="prettyprint">Borg</code> 的缺陷进行了改进，<code class="prettyprint">Kubernetes</code> 目前是 <code class="prettyprint">CNCF</code> 的项目并且是很多公司管理分布式系统的解决方案。其中比较有意思的一点是，<code class="prettyprint">Kubernetes</code> 的简写称为 <code class="prettyprint">K8s</code>。即该单词 <code class="prettyprint">k</code> 和 <code class="prettyprint">s</code> 中间刚好是 <code class="prettyprint">8</code> 个字母组成，所以是一种单词的简写形式。类似于，我们在项目中使用的国际化（<code class="prettyprint">internationalization</code>）叫做 <code class="prettyprint">i18n</code> 是一样效果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/39d60e62cf9d06507c75e97c1037f75f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/39d60e62cf9d06507c75e97c1037f75f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
建于 <code class="prettyprint">Docker</code> 之上的 <code class="prettyprint">Kubernetes</code> 可以构建一个<strong>容器的调度服务</strong>，其目的是让用户透过 <code class="prettyprint">Kubernetes</code> 集群来进行云端容器集群的管理，而无需用户进行复杂的设置工作，系统会自动选取合适的工作节点来执行具体的容器集群调度处理工作。<br>
<br>其核心概念是 <code class="prettyprint">Container Pod</code>。一个 <code class="prettyprint">Pod</code> 由一组工作于同一物理工作节点的容器构成。这些组容器拥有相同的网络命名空间、<code class="prettyprint">IP</code> 以及存储配额，也可以根据实际情况对每一个 <code class="prettyprint">Pod</code> 进行端口映射。此外，<code class="prettyprint">Kubernetes</code> 工作节点会由主系统进行管理，节点包含了能够运行 <code class="prettyprint">Docker</code> 容器所用到的服务。<br>
<br>我们可以看到多种服务方式：<br>
<ul><li><strong>阿里云 => Infrastructure as a service</strong></li><li><strong>新浪云 => Platform as a service</strong></li><li><strong>Office365 => Software as a service</strong></li></ul><br>
<br>作为编排工具，从社区的年龄来讲，<code class="prettyprint">Kubernetes</code> 不占优势。毕竟 <code class="prettyprint">Kubernetes</code> 才三岁而已，而 <code class="prettyprint">Apache</code> 推出的 <code class="prettyprint">Mesos</code> 已经有 <code class="prettyprint">7</code> 年之久。<code class="prettyprint">Docker Swarm</code> 虽然是比 <code class="prettyprint">Kubernetes</code> 更年轻，但是它的背后是来自于 <code class="prettyprint">Docker</code> 官方容器中心的全方位支持。但是，因为是谷歌开源出来的，并且拥有十多年的容器化的经验，所以还是有很多人在使用，并且会变成以后整个行业的主要支柱。<br>
<br>Kubernetes 解决的核心问题：<br>
<ul><li><strong>服务发现和负载均衡</strong>，Kubernetes 可以使用 DNS 名称或自己的 IP 地址公开容器，如果到容器的流量很大，Kubernetes 可以负载均衡并分配网络流量，从而使部署稳定。</li><li><strong>存储编排</strong>，Kubernetes 允许您自动挂载您选择的存储系统，例如本地存储、公共云提供商等。</li><li><strong>自动部署和回滚</strong>，您可以使用 Kubernetes 描述已部署容器的所需状态，它可以以受控的速率将实际状态更改为所需状态。例如，您可以自动化 Kubernetes 来为您的部署创建新容器，删除现有容器并将它们的所有资源用于新容器。</li><li><strong>自动二进制打包</strong>，Kubernetes 允许您指定每个容器所需 CPU 和内存（RAM）。当容器指定了资源请求时，Kubernetes 可以做出更好的决策来管理容器的资源。</li><li><strong>自我修复</strong>，Kubernetes 重新启动失败的容器、替换容器、杀死不响应用户定义的运行状况检查的容器，并且在准备好服务之前不将其通告给客户端。</li><li><strong>密钥与配置管理</strong>，Kubernetes 允许您存储和管理敏感信息，例如密码、OAuth 令牌和 SSH 密钥。您可以在不重建容器镜像的情况下部署和更新密钥和应用程序配置，也无需在堆栈配置中暴露密钥。</li></ul><br>
<br><code class="prettyprint">Kubernetes</code> 的出现不仅主宰了容器编排的市场，更改变了过去的运维方式，不仅将开发与运维之间边界变得更加模糊，而且让 <code class="prettyprint">DevOps</code> 这一角色变得更加清晰，每一个软件工程师都可以通过 <code class="prettyprint">Kubernetes</code> 来定义服务之间的拓扑关系、线上的节点个数、资源使用量并且能够快速实现水平扩容、蓝绿部署等在过去复杂的运维操作。<br>
<h3>性能对比</h3>当今三大主流调度系统的比较与分析。<br>
<br>对比总结：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/83cfeb0ff3dfb1a9071ddcc3d7799ac7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/83cfeb0ff3dfb1a9071ddcc3d7799ac7.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Apache Mesos：<br>
<br><code class="prettyprint">Apache Mesos</code> 是一个分布式系统内核的开源集群管理器，<code class="prettyprint">Apache Mesos</code> 的出现要远早于 <code class="prettyprint">Docker Swarm</code> 和 <code class="prettyprint">Kubernetes</code>。再加上 <code class="prettyprint">Marathon</code> 这个基于容器的应用程序的编排框架，它为 <code class="prettyprint">Docker Swarm</code> 和 <code class="prettyprint">Kubernetes</code> 提供了一个有效的替代方案。<code class="prettyprint">Mesos</code> 同时可以使用其他框架来同时支持容器化和非容器化的工作负载。<br>
<br><code class="prettyprint">Mesos</code> 能够在同样的集群机器上运行多种分布式系统类型，可以更加动态高效的共享资源。而且 <code class="prettyprint">Messos</code> 也提供服务失败检查，服务发布，服务跟踪，服务监控，资源管理和资源共享。<code class="prettyprint">Messos</code> 可以扩展伸缩到数千个节点。 如果你拥有很多的服务器而且想构建一个大的集群的时候，<code class="prettyprint">Mesos</code> 就派上用场了。很多的现代化可扩展性的数据处理应用都可以在 <code class="prettyprint">Mesos</code> 上运行，包括大数据框架 <code class="prettyprint">Hadoop</code>、<code class="prettyprint">Kafka</code>、<code class="prettyprint">Spark</code>。 但是大而全，往往就是对应的复杂和困难，这一点体现在 <code class="prettyprint">Messos</code> 上是完全正确，与 <code class="prettyprint">Docker</code> 和 <code class="prettyprint">Docker Swarm</code> 使用同一种 <code class="prettyprint">API</code> 不同的，<code class="prettyprint">Mesos</code> 和 <code class="prettyprint">Marathon</code> 都有自己的 <code class="prettyprint">API</code>，这使得它们比其他编排系统更加的复杂。<code class="prettyprint">Apache Mesos</code> 是混合环境的完美编配工具，由于它包含容器和非容器的应用，虽然 <code class="prettyprint">Messos</code> 很稳定，但是它的使用户快速学习应用变得更加困难，这也是在应用和部署场景下难于推广的原因之一。<br>
<br>Docker Swarm：<br>
<br><code class="prettyprint">Docker Swarm</code> 是 <code class="prettyprint">Docker</code> 公司的容器编排系统，使用的是标准 <code class="prettyprint">Docker API</code> 接口，容器使用命令和 <code class="prettyprint">docker</code> 命令是一套，简单方便。<code class="prettyprint">Docker Swarm</code> 基本架构是也是简单直接，每个主机运行一个 <code class="prettyprint">Docker Swarm</code> 代理，一个主机运行一个 <code class="prettyprint">Docker Swarm</code> 管理者，这个管理者负责指挥和调度这些主机上的容器，<code class="prettyprint">Docker Swarm</code> 以高可用性模式运行，<code class="prettyprint">Docker Swarm</code> 中的一个节点充当其他节点的管理器，包括调度程序和服务发现组件的容器。<code class="prettyprint">Docker Swarm</code> 的优点和缺点都是使用标准的 <code class="prettyprint">Docker</code> 接口，因为使用简单，容易集成到现有系统，所以在支持复杂的调度系统时候就会比较困难了，特别是在定制的接口中实现的调度。这也许就是成也在 <code class="prettyprint">Docker</code>，败也在 <code class="prettyprint">Docker</code> 的原因所在。<br>
<br>Kubernetes：<br>
<br><code class="prettyprint">Kubernetes</code> 作为一个容器集群管理系统，用于管理云平台中多个主机上的容器应用，<code class="prettyprint">Kubernetes</code> 的目标是让部署容器化的应用变得简单且高效，所以 <code class="prettyprint">Kubernetes</code> 提供了应用部署，规划，更新，维护的一整套完整的机制。<br>
<br><code class="prettyprint">Kubernetes</code> 没有固定要求容器的格式，但是 <code class="prettyprint">Kubernetes</code> 使用它自己的 <code class="prettyprint">API</code> 和命令行接口来进行容器编排。 除了 <code class="prettyprint">Docker</code> 容器之外，<code class="prettyprint">Kubernetes</code> 还支持其他多种容器，如 <code class="prettyprint">rkt</code>、<code class="prettyprint">CoreOS</code> 等。  <code class="prettyprint">Kubernetes</code> 是自成体系的管理工具，可以实现容器调度，资源管理，服务发现，健康检查，自动伸缩，更新升级等，也可以在应用模版配置中指定副本数量，服务要求（<code class="prettyprint">IO</code> 优先；性能优先等），资源使用区间，标签（<code class="prettyprint">Labels</code> 等）来匹配特定要求达到预期状态等，这些特征便足以征服开发者，再加上 <code class="prettyprint">Kubernetes</code> 有一个非常活跃的社区。它为用户提供了更多的选择以方便用户扩展编排容器来满足他们的需求。但是由于 <code class="prettyprint">Kubernetes</code> 使用了自己的 <code class="prettyprint">API</code> 接口，所以命令系统是另外一套系统，这也是 <code class="prettyprint">kubernetes</code> 门槛比较高的原因所在。<br>
<br>大部分的应用程序我们在部署的时候都会适当的添加监控，对于运行载体容器则更应该如此。<code class="prettyprint">kubernetes</code> 提供了 <code class="prettyprint">liveness probes</code> 来检查我们的应用程序，它是由节点上的 <code class="prettyprint">kubelet</code> 定期执行的。<br>
<h3>知识图谱</h3>主要介绍学习一些什么知识。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/10d3fd2728cc3d8bcbc62c7abb1596b5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/10d3fd2728cc3d8bcbc62c7abb1596b5.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>软件架构</h3>传统的客户端服务端架构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/0668bf8bebcd90e61077bdc72edb0414.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/0668bf8bebcd90e61077bdc72edb0414.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>架构说明</h4><code class="prettyprint">Kubernetes</code> 遵循非常传统的客户端/服务端的架构模式，客户端可以通过 <code class="prettyprint">RESTful</code> 接口或者直接使用 <code class="prettyprint">kubectl</code> 与 <code class="prettyprint">Kubernetes</code> 集群进行通信，这两者在实际上并没有太多的区别，后者也只是对 <code class="prettyprint">Kubernetes</code> 提供的 <code class="prettyprint">RESTful API</code> 进行封装并提供出来。每一个 <code class="prettyprint">Kubernetes</code> 集群都是由一组 <code class="prettyprint">Master</code> 节点和一系列的 <code class="prettyprint">Worker</code> 节点组成，其中 <code class="prettyprint">Master</code> 节点主要负责存储集群的状态并为 <code class="prettyprint">Kubernetes</code> 对象分配和调度资源。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/f46fe54b3f02b33ad3bcce65106fb89e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/f46fe54b3f02b33ad3bcce65106fb89e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/b434b6bc952d9084384cf17277dfca9d.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/b434b6bc952d9084384cf17277dfca9d.jpeg" class="img-polaroid" title="7.jpeg" alt="7.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>主节点服务 - Master 架构</h4>作为管理集群状态的 <code class="prettyprint">Master</code> 节点，它主要负责接收客户端的请求，安排容器的执行并且运行控制循环，将集群的状态向目标状态进行迁移。<code class="prettyprint">Master</code> 节点内部由下面四个组件构成：<br>
<ul><li><code class="prettyprint">API Server</code>：负责处理来自用户的请求，其主要作用就是对外提供 <code class="prettyprint">RESTful</code> 的接口，包括用于查看集群状态的读请求以及改变集群状态的写请求，也是唯一一个与 <code class="prettyprint">etcd</code> 集群通信的组件。</li><li><code class="prettyprint">etcd</code>：是兼具一致性和高可用性的键值数据库，可以作为保存 <code class="prettyprint">Kubernetes</code> 所有集群数据的后台数据库。</li><li><code class="prettyprint">Scheduler</code>：主节点上的组件，该组件监视那些新创建的未指定运行节点的 <code class="prettyprint">Pod</code>，并选择节点让 <code class="prettyprint">Pod</code> 在上面运行。调度决策考虑的因素包括单个 <code class="prettyprint">Pod</code> 和 <code class="prettyprint">Pod</code> 集合的资源需求、硬件/软件/策略约束、亲和性和反亲和性规范、数据位置、工作负载间的干扰和最后时限。</li><li><code class="prettyprint">controller-manager</code>：在主节点上运行控制器的组件，从逻辑上讲，每个控制器都是一个单独的进程，但是为了降低复杂性，它们都被编译到同一个可执行文件，并在一个进程中运行。这些控制器包括：<strong>节点控制器</strong>（负责在节点出现故障时进行通知和响应）、<strong>副本控制器</strong>（负责为系统中的每个副本控制器对象维护正确数量的 Pod）、<strong>端点控制器</strong>（填充端点 Endpoints 对象，即加入 Service 与 Pod）、<strong>服务帐户和令牌控制器</strong>（为新的命名空间创建默认帐户和 API 访问令牌）。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/730933de60a4b6fd7f4c6565abcc0119.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/730933de60a4b6fd7f4c6565abcc0119.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h4>工作节点 - Node 架构</h4>其他的 <code class="prettyprint">Worker</code> 节点实现就相对比较简单了，它主要由 <code class="prettyprint">kubelet</code> 和 <code class="prettyprint">kube-proxy</code> 两部分组成。<br>
<ul><li><code class="prettyprint">kubelet</code>：是工作节点执行操作的 <code class="prettyprint">agent</code>，负责具体的容器生命周期管理，根据从数据库中获取的信息来管理容器，并上报 <code class="prettyprint">Pod</code> 运行状态等。</li><li><code class="prettyprint">kube-proxy</code>：是一个简单的网络访问代理，同时也是一个 <code class="prettyprint">Load Balancer</code>。它负责将访问到某个服务的请求具体分配给工作节点上同一类标签的 <code class="prettyprint">Pod</code>。<code class="prettyprint">kube-proxy</code> 实质就是通过操作防火墙规则（<code class="prettyprint">iptables</code> 或者 <code class="prettyprint">ipvs</code>）来实现 <code class="prettyprint">Pod</code> 的映射。</li><li><code class="prettyprint">Container Runtime</code>：容器运行环境是负责运行容器的软件，<code class="prettyprint">Kubernetes</code> 支持多个容器运行环境：<code class="prettyprint">Docker</code>、<code class="prettyprint">containerd</code>、<code class="prettyprint">cri-o</code>、<code class="prettyprint">rktlet</code> 以及任何实现 <code class="prettyprint">Kubernetes CRI</code>（容器运行环境接口）。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/27a9bf757846d848012a170b7de8c36a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/27a9bf757846d848012a170b7de8c36a.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/fcf3b5561a14a89eda0888c2b15abd3c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/fcf3b5561a14a89eda0888c2b15abd3c.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>组件说明</h3>主要介绍关于 Kubernetes 的一些基本概念。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210812/94afc4d5c44c1a84dd481a743b12a46c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210812/94afc4d5c44c1a84dd481a743b12a46c.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
主要由以下几个核心组件组成：<br>
<ul><li><code class="prettyprint">apiserver</code>，所有服务访问的唯一入口，提供认证、授权、访问控制、API 注册和发现等机制</li><li><code class="prettyprint">controller manager</code>，负责维护集群的状态，比如副本期望数量、故障检测、自动扩展、滚动更新等</li><li><code class="prettyprint">scheduler</code>，负责资源的调度，按照预定的调度策略将 Pod 调度到相应的机器上</li><li><code class="prettyprint">etcd</code>，键值对数据库，保存了整个集群的状态</li><li><code class="prettyprint">kubelet</code>，负责维护容器的生命周期，同时也负责 Volume 和网络的管理</li><li><code class="prettyprint">kube-proxy</code>，负责为 Service 提供 cluster 内部的服务发现和负载均衡</li><li><code class="prettyprint">Container runtime</code>，负责镜像管理以及 Pod 和容器的真正运行</li></ul><br>
<br>除了核心组件，还有一些推荐的插件：<br>
<ul><li><code class="prettyprint">CoreDNS</code>，可以为集群中的 SVC 创建一个域名 IP 的对应关系解析的 DNS 服务</li><li><code class="prettyprint">Dashboard</code>，给 Kubernetes 集群提供了一个 B/S 架构的访问入口</li><li><code class="prettyprint">Ingress Controller</code>，官方只能够实现四层的网络代理，而 Ingress 可以实现七层的代理</li><li><code class="prettyprint">Prometheus</code>，给 Kubernetes 集群提供资源监控的能力</li><li><code class="prettyprint">Federation</code>，提供一个可以跨集群中心多 Kubernetes 的统一管理功能，提供跨可用区的集群</li></ul><br>
<br>原文链接：<a href="https://www.escapelife.site/posts/2c4214e7.html" rel="nofollow" target="_blank">https://www.escapelife.site/posts/2c4214e7.html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            