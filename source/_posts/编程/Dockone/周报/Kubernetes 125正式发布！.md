
---
title: 'Kubernetes 1.25正式发布！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220824/7239f736d82b130f65a389b50de463cc.jpg'
author: Dockone
comments: false
date: 2022-08-28 10:10:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220824/7239f736d82b130f65a389b50de463cc.jpg'
---

<div>   
<br>此版本共包含40项增强功能。其中15项增强功能进入Alpha阶段，10项正升级至Beta阶段，另有13项进入Stable稳定阶段。此外，有两项功能被弃用或移除。<br>
<br><h3>版本主题与徽标</h3>Kubernete 1.25徽标：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220824/7239f736d82b130f65a389b50de463cc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220824/7239f736d82b130f65a389b50de463cc.jpg" class="img-polaroid" title="1.25_.jpg" alt="1.25_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Kubernete 1.25主题是Combiner，即组合器。<br>
<br>Kubernetes项目本身是由众多独立组件所构成，这些组件集合起来，就形成了我们今天看到的项目形式。另外，Kubernetes也离不开众多贡献者的构建和维护，每位贡献成员都有着不同的技能、经验、历史和兴趣。他们有些加入了发布团队，有些则以特殊兴趣小组（SIG）的方式负责项目的持续支持和社区运营。<br>
<br>通过1.25版本，我们希望尊重这种协作和开放的精神。正是这种精神，让全球各地的开发者、作家和用户们凝聚成一股足以改变世界的力量。Kubernetes 1.25中包含多达40项增强功能，如果没有这些工作伙伴的鼎力协同，项目根本不可能取得今天的进展。<br>
<br>受到发行版负责人的儿子Albert Song的启发，Kubernetes 1.25的版本名称充分体现了每位参与者的重要意义，也期待各位在Kubernetes大家庭中继续贡献自己的一份特殊力量。<br>
<br><h3>重要变动</h3><h4>PodSecurityPolicy被移除；Pod Security Admission毕业为稳定版</h4>PodSecurityPolicy是在1.21版本中被决定弃用的，到1.25版本则将被正式删除。之所以删除此项功能，是因为想要进一步提升其可用性，就必须引入重大变更。为了保持项目整体稳定，只得加以弃用。取而代之的正是在1.25版本中毕业至稳定版的Pod Security Admission。如果你当前仍依赖PodSecurityPolicy，请按照<a href="https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/">Pod Security Admission迁移说明</a>进行操作。<br>
<br><h4>临时容器迎来稳定版</h4>临时容器是指在Pod中仅存在有限时长的容器。当我们需要检查另一容器，但又不能使用kubectl exec时（例如在执行故障排查时），往往可以用临时容器替代已经崩溃、或者镜像缺少调试工具的容器。临时容器在Kubernetes 1.23版本中已经升级至Beta版，这一次则进一步升级为稳定版。<br>
<br><h4>对cgroups v2的稳定支持</h4>自Linux内核cgroups v2 API公布稳定版至今，已经过去两年多时间。如今，已经有不少发行版默认使用此API，Kubernetes自然需要支持该内核才能顺利对接这些发行版。Cgroups v2对cgroups v1做出了多项改进，更多细节请参见<a href="https://kubernetes.io/docs/concepts/architecture/cgroups/">cgroups v2说明文档</a>。虽然cgroups v1将继续受到支持，但我们后续将逐步弃用v1并全面替换为v2。<br>
<br><h4>更好的Windows系统支持</h4><ul><li>性能仪表板添加了对Windows系统的支持</li><li>单元测试增加了对Windows系统的支持</li><li>一致性测试增加了对Windows系统的支持</li><li>为Windows Operational Readiness创建了新的GitHub仓库</li></ul><br>
<br><h4>将容器注册服务从k8s.gcr.io移动至registry.k8s.io</h4>1.25版本已经合并将容器注册服务从k8s.gcr.io移动至registry.k8s.io的变更。关于更多细节信息，请参阅相应<a href="https://github.com/kubernetes/k8s.io/wiki/New-Registry-url-for-Kubernetes-(registry.k8s.io)">wiki页面</a>，我们也通过Kubernetes开发邮件清单发出了全面通报。<br>
<br><h4>SeccompDefault升级为Beta版</h4>SeccompDefault现已升级为beta版。关于更多详细信息，请参阅<a href="https://kubernetes.io/docs/tutorials/security/seccomp/#enable-the-use-of-runtimedefault-as-the-default-seccomp-profile-for-all-workloads">使用seccomp限制容器的系统调用教程</a>。<br>
<br><h4>网络策略中的endPort已升级为稳定版</h4>网络策略中的endPort已经迎来GA通用版。支持endPort字段的网络策略提供程序，现可使用该字段来指定端口范围以应用网络策略。在之前的版本中，每个网络策略只能指向单一端口。<br>
<br>请注意，endPort的起效前提是必须得到网络策略提供程序的支持。如果提供程序不支持endPort，而您又在网络策略中指定了此字段，则会创建出仅覆盖端口字段（单端口）的网络策略。<br>
<br><h4>本地临时存储容量隔离迎来稳定版</h4>本地临时存储容量隔离功能已经迎来GA通用版。这项功能最早于1.8版本中公布了alpha版，在1.10中升级至beta，如今终于成为稳定功能。它通解为各Pod之间的本地临时存储提供容量隔离支持，例如EmptyDir。因此如果Pod对本地临时存储容量的消耗超过了该上限，则会驱逐该Pod以限制其对共享资源的占用。<br>
<br><h4>核心CSI迁移迎来稳定版</h4>CSI迁移是SIG Storage在之前多个版本中做出的持续努力，目标是将树内存储卷插件移动到树外CSI驱动程序，并最终移除树内存储卷插件。此次核心CSI迁移已迎来GA通用版，GCE PD和AWS EBS的CSI迁移功能也同步达到GA阶段。vSphere的CSI迁移仍处于beta阶段（但也已经默认启用），Portworx的CSI迁移功能同样处于beta阶段（默认关闭）。<br>
<br><h4>CSI临时存储卷提升至稳定版</h4>CSI临时存储卷功能，允许用户在临时用例的pod规范中直接指定CSI存储卷。如此一来，即可使用已安装的存储卷直接在pod内注入任意状态，例如配置、机密、身份、变量或其他类似信息。这项功能最初于1.15版本中推出alpha版，现已升级为GA通用版。某些CSI驱动程序会使用此功能，例如负责存储秘密信息的CSI驱动程序。<br>
<br><h4>CRD验证表达式语言升级至Beta版</h4>CRD验证表达式语言现已升级为beta版，因此声明能够使用通用表达式语言（CEL）验证自定义资源。关于更多细节信息，请参阅验证规则<a href="https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-rules">指南</a>。<br>
<br><h4>服务器端未知字段验证升级为Beta版</h4><code class="prettyprint">ServerSideFieldValidation</code>功能门现已升级为Beta版（默认启用），允许用户在检测到未知字段时，有选择地触发API服务器上的模式验证机制。如此一来，即可从kubectl中删除客户端验证，同时继续保持对包含未知/无效字段的请求报错。<br>
<br><h4>引入KMS v2 API</h4>引入KMS v2 alpha1 API以提升性能，实现轮替与可观察性改进。此API使用AES-GCM替代了AES-CBC，通过DEK实现静态数据（即Kubernetes Secrets）加密。过程中无需额外用户操作，而且仍然支持通过AES-GCM和AES-CBC进行读取。关于更多细节信息，请参阅<a href="https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/">使用KMS提供程序进行数据加密的说明指南</a>。<br>
<br><h3>其他更新</h3><h4>稳定版升级</h4>1.25版本共包含13项升级至稳定版的增强功能：<br>
<ul><li>临时容器</li><li>本地临时存储资源管理</li><li>CSI临时存储卷</li><li>CSI迁移——核心</li><li>将kube-scheduler ComponentConfig升级至GA通用版</li><li>CSI迁移——AWS</li><li>CSI迁移——GCE</li><li>DaemonSets支持MaxSurge</li><li>网络策略端口范围</li><li>cgroups v2支持</li><li>Pod Security Admission</li><li>将minReadySeconds添加至Statefulsets</li><li>在API准入层级权威识别Windows pod</li></ul><br>
<br><h4>弃用与移除</h4>1.25版本中弃用/移除了以下两项功能：<br>
<ul><li>PodSecurityPolicy</li><li>GlusterFS插件（从树内驱动程序移除）</li></ul><br>
<br><h4>发行版说明</h4>关于Kubernetes 1.25版本的完整信息，请参阅我们的<a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md">发行版说明</a>。<br>
<br><h4>发布时间</h4>Kubernetes 1.25现已在<a href="https://github.com/kubernetes/kubernetes/releases/tag/v1.25.0">GitHub</a>上开放下载。要开始使用Kubernetes，请参阅<a href="https://kubernetes.io/docs/tutorials/">交互式教程</a>，或使用容器为“节点”运行你的本地Kubernetes集群（<a href="https://kind.sigs.k8s.io/" rel="nofollow" target="_blank">https://kind.sigs.k8s.io/</a>）。你也可以通过<a href="https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/">kubeadm</a>轻松安装1.25新版本。<br>
<br><h4>发布团队</h4>Kubernetes的发展壮大，离不开社区的支持、承诺和协同努力。我们的发布团队由敬业的社区志愿者组成，他们共同构建了大量增强功能，共同成就了如今大家所熟悉并依赖的Kubernetes。<br>
<br>这里要感谢整个发布团队的辛勤工作，感谢你们带来的Kubernetes 1.25新版本。我们还要特别感谢发行版负责人Cici Huang，正是她的付出把整个发布团队紧紧凝聚在一起。<br>
<br><strong>原文链接：<a href="https://kubernetes.io/blog/2022/08/23/kubernetes-v1-25-release/">Kubernetes v1.25: Combiner</a></strong>
                                
                                                              
</div>
            