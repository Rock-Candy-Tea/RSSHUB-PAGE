
---
title: 'Kubernetes 1.21发布：社区的力量'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=4689'
author: Dockone
comments: false
date: 2021-04-09 12:10:24
thumbnail: 'https://picsum.photos/400/300?random=4689'
---

<div>   
<br>我们高兴地公布Kubernetes 1.21版本，这也是我们在2021年发布的第一个版本！此版本涉及51项增强功能：其中13项增强功能迎来稳定版，16项增强功能迎来beta版，20项增强功能迎来alpha版，另有2项功能不再推荐使用。<br>
<br>在本轮发布周期中，我们发布团队中的流程所有权也发生了重大变化。我们决定由以往从社区处定期征询到意见的同步通信模式，转变为由社区决定是否纳入特定功能及/或博文的新模式。这些变化让整个社区乃至各团队间的协作有所增加，由此带来的积极结果也让Kubernetes 1.21成为囊括新功能数量最多的版本。<br>
<h3>核心议题</h3><h4>CronJobs迎来稳定版！</h4>自Kubernetes 1.8起，<a href="https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/">CronJobs</a> (原ScheduledJobs) 就一直以beta功能的形式存在。而在本次1.21版本发布后，CronJobs这一早已得到广泛应用的API终于进入稳定阶段。<br>
<br>CronJobs用于定期执行各类需要无限期重复（例如每月、每周或每天执行一次）的计划操作，例如备份、报告生成等。您可以在指定的时间间隔之内，定义作业的具体启动时间点。<br>
<h4>Immutable Secrets与ConfigMaps</h4><a href="https://kubernetes.io/docs/concepts/configuration/secret/#secret-immutable">Immutable Secrets</a>与<a href="https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-immutable">ConfigMaps</a>各自向资源类型中加入了新的字段，确保新资源拒绝对这两种对象的更改。在默认情况下，Secrets与ConfigMap具有可变属性以保证各pod能够正常实现变更。但这种可变性，也会令Pod在收到错误Secrets与ConfigMap配置时引发问题。<br>
<br>通过将Secrets与ConfigMaps标记为不可变形式，大家可以确保您的应用程序配置不再发生变更。如果需要后续更改，您需要创建具有唯一新名称的Secret或ConfigMap，并部署相应的新pod以使用该资源。不可变资源还拥有扩展优势，这是因为控制器不需要轮询API服务器来监控变更活动。<br>
<br>这项功能在Kubernetes 1.21版本中正式迎来稳定版。<br>
<h4>IPv4/IPv6双协议栈支持</h4>IP地址是一种消耗性资源，集群运营者与管理员必须随时保证拥有充足的IP地址储备。目前公共IPv4地址已经相当稀缺，因此在双协议栈支持之下，我们可以将原生IPv6路由至各pod与服务，同时保证集群可以在必要时继续使用IPv4。双协议栈集群网络还有助于改善工作负载的潜在扩展受限问题。<br>
<br>Kubernetes迎来双协议栈支持，意味着各Pod、服务与节点可以同时获取IPv4与IPv6地址。在Kubernetes 1.21中，双协议栈网络已经进入beta阶段，且默认处于启用状态。<br>
<h4>节点优雅关闭</h4><a href="https://kubernetes.io/docs/concepts/architecture/nodes/#graceful-node-shutdown">节点优雅关闭</a>此次同样进入beta阶段，现可供更多用户使用！这是一项非常实用的功能，能够告知kubelet当前节点已经关闭，进而优雅地终止调度至该节点内的各个Pod。<br>
<br>在此之前，当节点关闭时，Pod的生命周期终止方式与我们的预期不同，因此无法正常关闭。这会给各类工作负载带来不同的问题。在1.21版本之后，kubelet将通过systemd检测到即将发生的系统关闭，而后向正在运行的Pod发出通知，借此保证各Pod尽可能实现正常终止。<br>
<h4>PersistentVolume状态监控器</h4>Persistent Volumes（即持久卷，简称PV）在应用程序中大多用于获取基于文件的本地存储数据。持久卷能够以多种方式起效，并帮助用户在无需重写存储后端的情况下完成应用程序迁移。<br>
<br>Kubernetes 1.21提供一项新的alpha功能，用以监控各持久卷的健康状态，并及时标记出状态异常的存储卷。工作负载将就此作出反应，避免从异常存储卷中读取、或者向其中写入数据。<br>
<h4>减少Kubernetes构建维护工作量</h4>以往，Kubernetes维护有多套构建系统。但这往往给各位贡献老鸟及新手带来严重困扰。<br>
<br>在上个版本当中，我们投入了大量精力以简化构建流程，并在原生Golang构建工具上实现了标准化。这应该能增强社区的广泛维护能力，同时降低新手贡献者们的入门门槛。<br>
<h3>主要变更</h3><h4>弃用PodSecurityPolicy</h4>在Kubernetes 1.21当中，PodSecurityPolicy已被弃用。与其他被弃用的Kubernetes功能一样，PodSecurityPolicy的现有beta版将继续在未来几个版本内完整存在，直到在Kubernetes 1.25当中被彻底移除。<br>
<br>下一步，我们将开发一种新的内置机制以帮助限制pod权限，名为“PSP替换策略”。我们将使用这种新机制涵盖各主要PodSecurityPolicy用例，借此大大改善工程效率与可维护性。关于更多详细信息，请参阅<a href="https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future">弃用PodSecurityPolicy：过去、现在与未来</a>。<br>
<h4>弃用TopologyKeys</h4>从1.21版本起，我们不再建议大家使用Service字段<code class="prettyprint">topologyKeys</code>；之前版本中所有使用此字段的组件功能均为alpha版，此次也将一并弃用。我们决定使用另外一种拓扑感知型路由实现方法（即拓扑感知提示，topology-aware hints）替代<code class="prettyprint">topologyKeys</code>。拓扑感知提示为Kubernetes 1.21版本中的alpha功能，您可以在<a href="https://kubernetes.io/docs/concepts/services-networking/service-topology/">Topology Aware Hints</a>部分了解关于这项功能的更多细节信息；或者参阅<a href="https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/2433-topology-aware-hints/README.md">KEP</a>以了解我们决定替换的理由。<br>
<h3>其他更新</h3><h4>以下功能迎来稳定版</h4><ul><li><a href="https://github.com/kubernetes/enhancements/issues/752">EndpointSlice</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/34">新增sysctl支持</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/85">PodDisruptionBudgets</a></li></ul><br>
<br><h4>重要功能更新</h4><ul><li><a href="https://github.com/kubernetes/enhancements/issues/541">External client-go credential providers</a> - 在1.21中提供beta版</li><li><a href="https://github.com/kubernetes/enhancements/issues/1602">Structured logging</a> - 将在1.22中提供beta版</li><li><a href="https://github.com/kubernetes/enhancements/issues/592">TTL after finish cleanup for Jobs and Pods</a> - 在1.21中提供beta版</li></ul><br>
<br><h3>发布说明</h3>关于1.21发布版的完整细节信息，请参阅<a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md">发布说明</a>。<br>
<h3>发布信息</h3>Kubernetes 1.21现已<a href="https://github.com/kubernetes/kubernetes/releases/tag/v1.21.0">在GitHub上开放下载</a>。这里提供丰富的资源，可供您轻松迈上Kubernetes探索之旅。您可以在Kubernetes主站点上观看<a href="https://kubernetes.io/docs/tutorials/">交互式教程</a>，或者使用Docker容器配合<a href="https://kind.sigs.k8s.io/">kind</a>在计算机上运行本地集群。如果您想尝试从零开始构建集群，请参阅Kelsey Hightower撰写的<a href="https://github.com/kelseyhightower/kubernetes-the-hard-way">Kubernetes the Hard Way</a>教程。<br>
<br><strong>原文链接：<a href="https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/">Kubernetes 1.21: Power to the Community</a></strong>
                                
                                                              
</div>
            