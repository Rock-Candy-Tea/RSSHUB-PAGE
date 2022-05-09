
---
title: '刚刚，Kubernetes 1.24正式发布'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/bcb42fc0de21e4c30d9af19c2b12c016.png'
author: Dockone
comments: false
date: 2022-05-09 02:53:24
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/bcb42fc0de21e4c30d9af19c2b12c016.png'
---

<div>   
<br>今天，我们很高兴地向大家宣布，Kubernetes 1.24暨2022年的首个版本已经正式发布！<br>
<br>1.24版本涉及46项增强功能：其中14项已升级为稳定版，15项进入beta阶段，13项则刚刚进入alpha阶段。此外，另有2项功能被弃用、2项功能被删除。<br>
<h3>要点汇总</h3><h4>从kubelet中移除dockershim</h4>自1.20版本被弃用之后，dockershim组件终于在1.24的kubelet中被删除。从1.24开始，大家需要使用其他受到支持的运行时选项（例如containerd或CRI-O）；如果您选择Docker Engine作为运行时，则需要使用cri-dockerd。关于dockershim移除的更多详细信息，请参阅本<a href="https://kubernetes.io/blog/2022/03/31/ready-for-dockershim-removal/">指南</a>。<br>
<h4>各beta API默认关闭</h4>在默认情况下，新的各beta API不会在集群内得到<a href="https://github.com/kubernetes/enhancements/issues/3136">启用</a>。但全部原有beta API及其新版本将在1.24中继续默认启用。<br>
<h4>签名发布工件</h4>在1.24版本中，发布工件将使用cosign进行签名，同时提供实验性的镜像签名验证支持。发布工件的签名与验证属于Kubernetes软件发布供应链的安全性改进举措之一。<br>
<h4>OpenAPI v3</h4>Kubernetes 1.24开始为API的OpenAPI v3发布格式提供beta支持。<br>
<h4>存储容量与存储卷扩展双双迎来通用版本</h4>存储容量跟踪通过CSIStorageCapacity对象公开当前可用的存储容量，并对使用后续绑定的CSI存储卷的pod进行调度增强。<br>
<br>存储卷扩展则新增对现有持久卷的重新调整功能。<br>
<h4>NonPreemptingPriority迎来稳定版</h4>此功能为PriorityClasses添加了新的选项，可开启或关闭pod抢占机制。<br>
<h4>存储插件迁移</h4>目前Kubernetes开发团队正在迁移树内存储插件，希望在实现CSI插件的同时、保持原有API的正常起效。Azure Disk与OpenStack Cinder等插件已经完成了迁移。<br>
<h4>gRPC探针升级至beta版</h4>在1.24版本中，gRPC探针功能已经进入beta阶段且默认启用。现在，大家可以在Kubernetes中为自己的gRPC应用程序原生配置启动、活动与就绪探测，而且无需公开HTTP商战或者使用额外的可执行文件。<br>
<h4>Kubelet证书提供程序升级至beta版</h4>最初在Kubernetes 1.20版本中以alpha版亮相的kubelet镜像证书提供程序现已升级至beta版。现在，kubelet将使用exec插件动态检索容器镜像注册表的凭证，而不再将凭证存储在节点文件系统之上。<br>
<h4>上下文日志记录进入alpha阶段</h4>Kubernetes 1.24还引入了上下文日志记录功能，允许函数调用方能够控制日志记录的各项细则（包括输出格式、详尽程度、附加值和名称）。<br>
<h4>避免为服务分配IP时发生冲突</h4>Kubernetes 1.24引入了一项新的选择性功能，允许用户为服务的静态IP分配地址保留一个软范围。通过手动启用此项功能，集群将从您指定的服务IP池中自动获取地址，从而降低冲突风险。<br>
<br>也就是说，服务的ClusterIP能够以下列方式分配：<br>
<ul><li>动态分配，即集群将在配置的服务IP范围内自动选择一个空闲IP。</li><li>静态分配，意味着用户需要在已配置的服务IP范围内指定一个IP。</li></ul><br>
<br>服务ClusterIP是唯一的；因此若尝试使用已被分配的ClusterIP进行服务创建，则会返回错误结果。<br>
<h4>从kubelet中移除动态kubelet配置</h4>在Kubernetes 1.22版本中被弃用后，动态kubelet配置现已从kubelet中正式移除。在未来的1.26版本中，此功能还将从API服务器中删除。<br>
<h3>关于CNI版本的重要变更</h3>在升级至1.24之前，请确认并测试您所使用的容器运行时能够在新版本中正常工作。<br>
<br>例如，以下容器运行时已经或即将全面兼容Kubernetes 1.24：<br>
<ul><li>containerd v1.6.4及更高，v1.5.11及更高</li><li>CRI-O 1.24及更高</li></ul><br>
<br>若CNI插件尚未升级且/或CNI配置文件中未声明CNI配置版本时，则containerd v1.6.0-v1.6.3版本将导致pod CNI网络setup及tear down发生问题。Containerd团队报告称，“这些问题已经在containerd v1.6.4中得到解决。”<br>
<br>在containerd v1.6.0-v1.6.3时，如果你未升级CNI插件且/或声明CNI配置版本，则可能遇到“CNI版本不兼容”或“无法为沙箱删除网络”等错误。<br>
<h3>其他更新</h3><h3>毕业至稳定版</h3>在1.24版本中，共有14项增强功能迎来稳定版：<br>
<ul><li><a href="https://github.com/kubernetes/enhancements/issues/284">容器存储接口(CSI) 存储卷扩展</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/688">Pod Overhead</a>：统计绑定至pod沙箱、但未绑定至指定容器的资源。</li><li><a href="https://github.com/kubernetes/enhancements/issues/902">向PriorityClasses添加非抢占选项</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/1472">存储容量跟踪</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/1489">OpenStack Cinder In-Tree迁移至CSI Driver</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/1490">Azure Disk In-Tree迁移至CSI Driver</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/1904">高效watch恢复</a>:可在kube-apiserver重启后，对watch进行高效恢复</li><li><a href="https://github.com/kubernetes/enhancements/issues/1959">服务类型=负载均衡器类字段</a>：引入一种新的服务注释<code class="prettyprint">service.kubernetes.io/load-balancer-class</code>，允许在同一集群中实现多种<code class="prettyprint">type: LoadBalancer</code>服务。</li><li><a href="https://github.com/kubernetes/enhancements/issues/2214">索引作业</a>：为具有固定完成计数的作业Pod添加完成索引。</li><li><a href="https://github.com/kubernetes/enhancements/issues/2232">为Jobs API添加暂停字段</a>：为Jobs API添加暂停字段，这样编排程序即可创建作业、从而更好地控制pod创建时间。</li><li><a href="https://github.com/kubernetes/enhancements/issues/2249">Pod Affinity NamespaceSelector</a>：为Pod亲和性/反亲和性规范添加<code class="prettyprint">namespaceSelector</code>字段。</li><li><a href="https://github.com/kubernetes/enhancements/issues/2436">面向控制器管理器的leader迁移</a>：kube-controller-manager与cloud-controller-manager现可在HA控制平面中使用新的_控制器到控制器管理器分配_功能，全程无需停机。</li><li><a href="https://github.com/kubernetes/enhancements/issues/2784">CSR持续时间</a>：为CertificateSigningRequest API提供新的扩展机制，允许客户端为已颁发的证书请求特定持续时长。</li></ul><br>
<br><h4>重要变更</h4>1.24版本包含2项重要变更：<br>
<ul><li><a href="https://github.com/kubernetes/enhancements/issues/2221">移除Dockershim</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/3136">默认关闭各Beta APIs</a></li></ul><br>
<br><h4>发布说明</h4>关于Kubernetes 1.24版本的更多详细信息，请参阅我们的发布<a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md">说明</a>。<br>
<h4>发布情况</h4>Kubernetes 1.24现已在<a href="https://github.com/kubernetes/kubernetes/releases/tag/v1.24.0">GitHub</a>上开放下载。要开始使用Kubernetes，请参阅各交互式<a href="https://kubernetes.io/docs/tutorials/">教程</a>，或在<a href="https://kind.sigs.k8s.io/">kind</a>中使用容器作为“节点”运行你的本地Kubernetes集群。你也可以通过<a href="https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/">kubeadm</a>轻松安装Kubernetes 1.24。<br>
<h4>发布团队</h4>如果没有Kubernetes发布团队中各位成员的共同努力，1.24版本将无法与大家见面。开发团队团结一致、共同带来了Kubernetes各个版本中的所有代码、文档、发布说明等宝贵成果。<br>
<br>这里要特别感谢发布负责人James Laverack为了Kubernetes的稳定更新做出的指导，也感谢每位团队成员为1.24版本投入的时间和精力。<br>
<h4>发布主题与Logo</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220504/bcb42fc0de21e4c30d9af19c2b12c016.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/bcb42fc0de21e4c30d9af19c2b12c016.png" class="img-polaroid" title="kubernetes-1.24_.png" alt="kubernetes-1.24_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes 1.24的主题为Stargazer，即观星者。<br>
<br>从古代天文学家到如今建造詹姆斯-韦伯太空望远镜的科学家，人类世世代代怀着敬畏与好奇仰望着星空。繁星启发了我们、激发着我们的想象力，也在一个又一个漂泊的夜晚为船员们指示着前进的方向。<br>
<br>通过此版本，我们再次将目光投向星空，象征着整个社区齐聚一堂、遥望前路。Kubernetes社区聚集着全球数百名贡献者和成千上万的最终用户，并最终支撑起数以百万计的运行服务。每一位参与者都如同一颗星斗，在夜空中帮助我们规划航向。<br>
<br>1.24版本的发行logo由Britnee Laverack制作，图中一架望远镜遥指空中的昴宿星团，也就是神话中的七仙女星。数字“七”也是Kubernetes的幸运数，毕竟最早我们曾把项目定名为“Project Seven”。<br>
<br>所以我们决定在1.24版本中回归初心，找回探索寰宇的项目使命。今天，我们都是“观星者”。<br>
<h4>项目进度</h4><a href="https://k8s.devstats.cncf.io/d/12/dashboards?orgId=1&refresh=15m">CNCF K8s DevStats</a>项目汇总了Kubernetes及下辖各个子项目的进度数据点，包括做出贡献的个人及企业数量等等。感兴趣的朋友可以点击查看，了解Kubernetes生态系统是在怎样的支持下才发展到如今的深度和广度。<br>
<br>1.24版本的开发和发布周期为17周（1月10日至5月3日），期间我们共收到来自1029家企业和1179位个人的贡献。<br>
<br><strong>原文链接：<a href="https://kubernetes.io/blog/2022/05/03/kubernetes-1-24-release-announcement/">Kubernetes 1.24: Stargazer</a></strong>
                                
                                                              
</div>
            