
---
title: 'Kubernetes 1.22发布：迈向新巅峰'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/1c7cc43eaebd0ff028d201ab6a3337b6.png'
author: Dockone
comments: false
date: 2021-08-05 04:09:27
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/1c7cc43eaebd0ff028d201ab6a3337b6.png'
---

<div>   
<br>今天，我们兴奋地向大家宣布，Kubernetes在2021年内的第二个版本、即1.22版本已经正式来临！<br>
<br>新版本包含53项增强功能：其中13项功能已升级至稳定版，24项功能顺利步入beta阶段，16项功能刚刚开始alpha阶段。另有3项功能被彻底弃用。<br>
<br>今年4月，Kubernetes的发布周期已经正式由每年4次调整为每年3次。而1.22版本正是调整之后的首个长周期发布版本。随着Kubernetes的逐渐成熟，每个发布周期中包含的增强功能数量一直在持续增加。这意味着贡献者社区及发布工程团队需要在两个版本之间完成更多开发工作，而新版本中的大量全新功能也会给最终用户社区带来一定的学习压力。<br>
<br>有鉴于此，Kubernetes的发布节奏由一年四次调整为一年三次能够带来更好的均衡效果，包括贡献与版本管理、社区规划升级并为用户提供更舒适的更新上手体验。<br>
<h3>版本要点</h3><h4>Server-side Apply迎来GA通用版本</h4><a href="https://kubernetes.io/docs/reference/using-api/server-side-apply/">Server-side Apply</a>是一种面向Kubernetes API服务器的全新字段所有权及对象合并算法。Server-side Apply通过声明式配置帮助用户及控制器管理其资源，包括以声明方式创建及/或修改对象、发送明确指定的意图等等。经过数个版本的测试之后，Server-side Apply现已正式进入GA通用版阶段。<br>
<h4>外部凭证提供程序迎来稳定版</h4>自1.11版本以来，对Kubernetes客户端凭证插件的支持就一直处于测试阶段。而随着Kubernetes 1.22的推出，这项功能逐步趋于稳定。其中的GA功能集现在包括对交互式登录流程插件提供更好的支持，同时修复了多项bug。感兴趣的插件作者可以参考<a href="https://github.com/ankeesler/sample-exec-plugin">sample-exec-plugin</a>以了解更多详细信息。<br>
<h4>etcd更新至3.5.0</h4>Kubernetes的默认后端存储etcd获得了3.5.0新版本。新版本改进了安全性、性能、监控以及开发者体验，修复了多项bug，同时带来了迁移为结构化日志记录与内置日志轮替等重要新功能。3.5.0版本还提出详尽的后续发展路线图，探索如何更好地解决流量过载问题。感兴趣的朋友可以参考<a href="http://dockone.io/article/2434363">3.5.0发布公告</a>中的完整变更清单。<br>
<h4>用于内存资源的Quality of Service（QoS）</h4>最初，Kubernetes使用的是v1 cgroups API。通过这种设计，Pod的QoS类将仅可用于CPU资源（例如cpu_shares）。如今，Kubernetes 1.22版以alpha测试的形式使用cgroups v2 API控制内存分配与隔离，希望在内存资源发生争用时提高工作负载与节点的可用性、改善容器生命周期的可预测性。<br>
<h4>节点系统交换支持</h4>每一位系统管理员或Kubernetes用户在设置和使用Kubernetes时，都会不约而同地禁用掉交换空间。随着Kubernetes 1.22版本的发布，新的alpha功能已可支持运行具有交换内存的节点。这项变更使得管理员能够选择在Linux节点上配置交换，并将一部分块存储视为额外的虚拟内存。<br>
<h4>Windows增强与功能</h4>SIG Windows继续为不断发展壮大的开发者社区提供支持，并在1.22新版本中发布了自己的开发环境。这些新工具支持多种CNI提供程序并能够在多个平台上顺畅运行。通过编译Windows kubelet与kube-proxy，再配合日常构建的其他Kubernetes组件，新版本为用户带来一种从零开始使用全新Windows功能的新方法。<br>
<br>CSI对Windows节点的支持也在1.22版本中达到GA通用阶段。另外，Kubernetes 1.22迎来了新的alpha功能——Windows特权容器。为了在Windows节点上使用CSI存储，CSIProxy允许我们将CSI节点插件部署为非特权Pod，并使用代理在节点上执行特权存储操作。<br>
<h4>seccomp默认配置</h4>Kubelet以alpha功能的形式提供默认seccomp配置功能，同时附带新的命令行标志与配置。在使用时，这项新功能可提供集群范围内的seccomp默认值，并使用RuntimeDefault seccompt配置取代默认情况下的Unconfined，从而大大增强了Kubernetes部署的默认安全性。凭借更出色的默认工作负载安全效果，管理员们终于可以睡个好常见了。若需了解这项功能的更多详细信息，请参阅官方<a href="https://kubernetes.io/docs/tutorials/clusters/seccomp/#enable-the-use-of-runtimedefault-as-the-default-seccomp-profile-for-all-workloads">seccomp教程</a>。<br>
<h4>使用kubeadm提升控制平面安全</h4>这项新的alpha功能允许我们以非root用户身份运行kubeadm控制平面组件。长久以来，kubeadm一直要求采取这样一种安全措施。要实际体验，你需要在kubeadm中启用特定的RootlessControlPlane feature gate。在使用这项alpha功能部署集群时，你的控制平面将以较低权限运行。<br>
<br>对于kubeadm，Kubernetes 1.22还带来了新的v1beta3配置API。此次迭代带来了多项社区期待已久的功能，同时弃用了部分现有功能。v1beta3将成为目前的首选API版本；但v1beta2 API仍然正常可用，并未在1.22版中被淘汰。<br>
<h3>主要变化</h3><h4>删除了几个已弃用的beta API</h4>1.22版本中删除了许多已经弃用的beta API，并发布这些API的GA通用版本。全部现有对象均可通过稳定的API进行交互。此次删除涉及  <code class="prettyprint">Ingress</code>，<code class="prettyprint">IngressClass</code>，<code class="prettyprint">Lease</code>，<code class="prettyprint">APIService</code>，<code class="prettyprint">ValidatingWebhookConfiguration</code>，<code class="prettyprint">MutatingWebhookConfiguration</code>，<code class="prettyprint">CustomResourceDefinition</code>，<code class="prettyprint">TokenReview</code>，<code class="prettyprint">SubjectAccessReview</code>以及  <code class="prettyprint">CertificateSigningRequest</code> API的beta版本。<br>
<br>关于完整清单，请参阅<a href="https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22">已弃用API迁移指南</a>以及博文<a href="https://blog.k8s.io/2021/07/14/upcoming-changes-in-kubernetes-1-22/">《1.22版本中的Kubernetes API与功能删除：你需要了解的一切》</a>。<br>
<h4>临时容器的API变更与改进</h4>用于创建临时容器的API在1.22版本中也发生了变化。临时容器功能现为alpha版且默认禁用，新的API也不再响应客户端对旧有API的使用请求。<br>
<br>在稳定功能方面，kubectl工具遵循Kubernetes版本倾斜策略，但kubectl v1.21及更早版本无法支持临时容器的新API。如果你打算使用kubectl debug创建临时容器，且你的集群运行有Kubernetes 1.22，则无法使用kubectl v1.21或更早版本完成这项操作。如果你希望将kubectl debug与多个集群版本混合使用，请务必将kubectl更新至1.22。<br>
<h3>其他更新</h3><h4>更新至稳定版</h4><ul><li><a href="https://github.com/kubernetes/enhancements/issues/542">限定服务账户令牌数量</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/2047">CSI服务账户令牌</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/1122">Windows对CSI插件的支持</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/1693">对于在操作中使用已弃用API的警告机制</a></li><li><a href="https://github.com/kubernetes/enhancements/issues/85">清退PodDisruptionBudget</a></li></ul><br>
<br><h4>重要功能更新</h4><ul><li>引入新的PodSecurity准入alpha功能，用以替代原有PodSecurityPolicy</li><li>The Momory Manager进入beta阶段</li><li>推出新的alpha功能，用于实现API Server Tracing</li><li>kubeadm配置格式迎来新的v1beta3版本</li><li>用于PersistentVolumes的通用数据填充器已提供alpha版</li><li>Kubernetes控制平面现可始终使用CronJobs v2控制器</li><li>作为alpha功能，所有Kubernetes节点组件（包括kubelet、kube-proxy与容器运行时）都能够以非root用户身份运行</li></ul><br>
<br><h3>发布说明</h3>请<a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md">点击此处</a>查看1.22版本的完整发布说明信息。<br>
<h3>发布时间</h3>Kubernetes 1.22现已<a href="https://kubernetes.io/releases/download/">开放下载</a>并正式登陆<a href="https://github.com/kubernetes/kubernetes/releases/tag/v1.22.0">GitHub</a>。<br>
<h3>版本徽标</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210805/1c7cc43eaebd0ff028d201ab6a3337b6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210805/1c7cc43eaebd0ff028d201ab6a3337b6.png" class="img-polaroid" title="kubernetes-1.22_.png" alt="kubernetes-1.22_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
面对新冠疫情、自然灾害与倦怠情绪的重重挑战，Kubernetes 1.22仍然拿出了53项增强功能，这也使其成为迄今为止更新量最大的Kubernetes版本。这样辉煌的成就，离不开发布团队成员们的辛勤努力、热情奉献以及Kubernetes生态系统中杰出贡献者们的不懈支持。1.22版本发布徽标提醒我们要不断突破新的极限、创造新的纪录。谨以此标，献给每一位发布团队成员、攀登者与前瞻者！<br>
<br>徽标由Boris Zotkin设计。作为MathWorks的Mac/Linux管理员，Boris热爱生活中平淡简单的一切，喜欢与家人共度时光。这里再次感谢这位乐观技术人贡献的精美作品！<br>
<br><strong>原文链接：<a href="https://kubernetes.io/blog/2021/08/04/kubernetes-1-22-release-announcement/">Kubernetes 1.22: Reaching New Peaks</a></strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            