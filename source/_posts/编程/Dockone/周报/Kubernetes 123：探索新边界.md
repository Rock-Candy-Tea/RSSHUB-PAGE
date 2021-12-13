
---
title: 'Kubernetes 1.23：探索新边界'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211208/dfc1449b73aa7fcdb1480cfafaff36f2.png'
author: Dockone
comments: false
date: 2021-12-13 10:08:46
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211208/dfc1449b73aa7fcdb1480cfafaff36f2.png'
---

<div>   
<br>今天，我们高兴地宣布Kubernetes正式迎来1.23版本，也是2021年内的最后一次版本更新。<br>
<br>此版本包含47项增强功能：其中11项增强已经升级至稳定版，17项增强进入测试阶段，19项增强迎来Alpha版，另有1项功能被弃用。<br>
<h3>要点整理</h3><h4>弃用FlexVolume</h4>FlexVolume已被弃用。现在Kubernetes确定将树外CSI驱动程序作为默认存储卷驱动程序编写方式。关于更多详细信息，请参阅<a href="https://github.com/kubernetes/community/blob/master/sig-storage/volume-plugin-faq.md#kubernetes-volume-plugin-faq-for-storage-vendors">说明文档</a>。FlexVolume驱动程序的维护者们应转向CSI驱动程序，并帮助FlexVolume用户完成CSI迁移。这里也提醒各位FlexVolume将工作负载转移至CSI驱动程序。<br>
<h4>弃用klog特定标记</h4>为了简化代码库，Kubernetes 1.23版本将<a href="https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#klog">弃用多个日志标记</a>；相关实现代码将在后续版本中逐步剔除，请用户们结合实际需要选择可行的替代标记解决方案。<br>
<h4>Kubernetes发布流程中的软件供应链SLSA L1级合规性</h4>Kubernetes各发行版现可生成出处证明文件，用以描述发布流程中的各登台（staging）与实际发布阶段。现在，各工件在由一个阶段转至下一阶段时会得到确切验证。最终阶段则保证Kubernetes发行版切实遵循SLSA安全框架L1级（面向软件工件的供应链等级）的合规性要求。<br>
<h4>IPv4/IPv6双栈网络已毕业为通用版本</h4>IPv4/IPv6双栈网络现已毕业为通用版本。自1.21版本以来，Kubernetes集群就默认支持双栈组网。在1.23版本中，我们进一步删除了IPv6DualStack功能门。我们并不强制要求使用双栈网络——虽然集群中已经启用双栈网络支持，但Pod与服务仍然默认为单栈。要使用双栈网络，你的Kubernetes节点必须具有可路由的IPv4/IPv6网络接口、必须使用支持双栈的CNI网络插件、必须将Pod配置为双栈，而且必须将服务的<code class="prettyprint">.spec.ipFamilyPolicy</code>字段设置为<code class="prettyprint">PreferDualStack</code>或者<code class="prettyprint">RequireDualStack</code>。<br>
<h4>HorizontalPodAutoscaler v2毕业为通用版本</h4>HorizontalPodAutscaler <code class="prettyprint">autoscaling/v2</code>稳定API已经在1.23中毕业为通用版本。相应的，HorizontalPodAutoscaler <code class="prettyprint">autoscaling/v2beta2</code>API已被弃用。<br>
<h4>Generic Ephemeral Volume（通用临时存储卷）功能毕业为通用版本</h4>通用临时存储卷功能在1.23中毕业为通用版本。这项功能允许用户将支持动态配置的一切现有存储驱动器作为临时存储卷，并将存储卷的生命周期绑定至相应Pod。此功能还支持存储卷配置中的所有StorageClass参数以及PersistentVolumeClaims所支持的一切功能。<br>
<h4>Skip Volume Ownership（跳过卷所有权）更改现已毕业至通用版本</h4>这项用于配置存储卷权限及所有权变更策略的功能已经在1.23中毕业为通用版本，可帮助用户通过挂载时的递归权限变更并加快Pod启动时间。<br>
<h4>允许CSI驱动程序选择加入卷所有权及权限变更的功能，现已毕业至通用版本</h4>这项功能允许CSI驱动程序以声明方式支持基于fsGroup的权限，现已在1.23中毕业为通用版本。<br>
<h4>PodSecurity升级至Beta版</h4>PodSecurity迎来Beta版。PodSecurity替换掉了已被弃用的PodSecurityPolicy准入控制器；其自身即可作为准入控制器，根据所设置实施级别中的特定命名空间标签对命名空间内的Pod执行安全标准。在1.23版本中，Kubernetes已经默认启用PodSecurity功能门。<br>
<h4>Container Runtime Interface（容器运行时接口CRI）v1现为默认选项</h4>Kubelet现在支持CRI v1 API，并将后者作为项目范围内的默认选项。如果某容器运行时不支持v1 API，Kubernetes将回退至v1 alpha2实现。最终用户不需要执行任何中间操作，因为v1与v1 alpha2在具体实现上没有区别。v1alpha2有望在后续Kubernetes版本中被删除，确保所有开发精力都将集中在v1身上。<br>
<h4>结构化日志升级至Beta版</h4>结构化日志已经迎来Beta版。目前，kubelet与kube-scheduler中的大部分日志信息均已完成转换。我们鼓励用户尝试JSON输出或者使用结构化文本格式解析，并向我们提供关于潜在问题及可行解决方案的反馈意见，例如日志值中的多行字符串处理等。<br>
<h4>面向调度器的精简化多点插件配置机制</h4>Kube-scheduler将为插件添加一个新的、精简化的配置字段，允许用户在单一位置启用多个扩展点。这种新的multiPoint（多点）插件字段将帮助管理员简化大部分调度程序设置。通过multiPoint启用的插件将自动在其实现的各个独立扩展点上完成注册。例如，你可以同时在Score与Filter两个扩展点上启用同一插件。如此一来，大家不必手动编辑各个扩展点设置，即可轻松启用和禁用该扩展点上的所有插件。而且由于并不影响大多数用户的实际使用，所以我们决定抽象掉这些扩展点。<br>
<h4>CSI迁移更新</h4>CSI迁移（CSI Migration）使用相应的CSI驱动程序替换现有树中存储插件，例如<code class="prettyprint">kubernetes.io/gce-pd</code>或者<code class="prettyprint">kubernetes.io/aws-ebs</code>。如果CSI Migration正常工作，则Kubernetes最终用户不会感受到任何区别。迁移完成之后，Kubernetes用户也可继续使用现有接口上全部树中存储插件的一切功能。<br>
<ul><li>CSI Migration功能默认开启，但在1.23版本中其在GCE PD、AWS EBS以及Azure Disk上仍处于Beta版阶段。</li><li>在1.23版本中，CSI Migration在Ceph RBD及Portworx上仍处于Alpha版阶段。</li></ul><br>
<br><h4>CRD表达式语言验证升级为Alpha版</h4>从1.23版本开始，CRD表达式语言验证（Expression language validation for CRD）正式进入Alpha版阶段。只要大家启用<code class="prettyprint">CustomResourceValidationExpressions</code>功能门，即代表自定义资源将由通用表达式语言（CEL）规则进行验证。<br>
<h4>服务器端字段验证升级为Alpha版</h4>在1.23版本中启用<code class="prettyprint">ServerSideFieldValidation</code>功能门后，用户将在通过包含未知或重复字段的请求发送Kubernetes对象时，收到来自服务器端的警告。与此同时，服务器将直接丢弃此前未知的字段以及除最后一个重复字段外的所有前置重复字段。<br>
<br>在启用此功能门后，我们还将引入fieldValidation查询参数，以便用户以每条单独请求为基础指定服务器的相应行为。这里fieldValidation查询参数的有效值为：<br>
<ul><li>Ignore（禁用功能门时的默认值，效果与1.23之前各版本删除/忽略未知字段的行为相同）。</li><li>Warn（启用功能门时的默认值）。</li><li>Strict（将导致包含Invalid Request错误的请求直接失败）。</li></ul><br>
<br><h4>OpenAPI v3升级为Alpha版</h4>从1.23版本开始，如果启用OpenAPIV3功能门，用户将能够为所有Kubernetes类型请求OpenAPI v3.0规范。OpenAPI v3完全透明，并能够支持此前OpenAPI v2发布时丢弃的一组字段，具体包括：<code class="prettyprint">default</code>，<code class="prettyprint">nullable</code>，<code class="prettyprint">oneOf</code>，<code class="prettyprint">anyOf</code>。<code class="prettyprint">V3</code>还为各个Kubernetes group版本发布了特定规范（位于<code class="prettyprint">$cluster/openapi/v3/apis/&lt;group>/&lt;version></code>  端点）以提升性能与发现性，所有group版本均可在<code class="prettyprint">$cluster/openapi/v3</code>路径处找到。<br>
<h3>毕业至稳定版的功能</h3><ul><li>IPv4/IPv6双栈支持：<a href="https://github.com/kubernetes/enhancements/issues/563" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... s/563</a></li><li>跳过卷所有权变更：<a href="https://github.com/kubernetes/enhancements/issues/695" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... s/695</a></li><li>TTL完成后控制器：<a href="https://github.com/kubernetes/enhancements/issues/592" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... s/592</a></li><li>CSI 驱动程序对象中的FSGroup配置策略<a href="https://github.com/kubernetes/enhancements/issues/1682" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /1682</a></li><li>通用临时内联存储卷：<a href="https://github.com/kubernetes/enhancements/issues/1698" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /1698</a></li><li>通过静态分析保护秘密日志：<a href="https://github.com/kubernetes/enhancements/issues/1933" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /1933</a></li><li>命名空间范围的入口类参数：<a href="https://github.com/kubernetes/enhancements/issues/2365" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /2365</a></li><li>减少Kubernetes构建维护负担：<a href="https://github.com/kubernetes/enhancements/issues/2420" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /2420</a></li><li>HPA API毕业为通用版本：<a href="https://github.com/kubernetes/enhancements/issues/2702" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /2702</a></li></ul><br>
<br><h4>重要变更</h4><ul><li>API服务器请求的优先级与公平性：<a href="https://github.com/kubernetes/enhancements/issues/1040" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... /1040</a></li></ul><br>
<br><h4>发行说明</h4>关于完整的发行说明信息，请参阅<a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md">Kubernetes 1.23版本发行说明</a>。<br>
<h4>可用性</h4>Kubernetes 1.23现已通过<a href="https://github.com/kubernetes/kubernetes/releases/tag/v1.23.0">GitHub</a>开放下载。要开始使用Kubernets，建议你首先观看<a href="https://kubernetes.io/docs/tutorials/">交互式教程</a>或通过<a href="https://kind.sigs.k8s.io/">kind</a>使用Docker容器“节点”运行本地Kubernetes集群。你也可以使用<a href="https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/">kubeadm</a>轻松安装1.23最新版本。<br>
<h4>发行版主题与徽标</h4>Kubernetes 1.23：探索新边界<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211208/dfc1449b73aa7fcdb1480cfafaff36f2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211208/dfc1449b73aa7fcdb1480cfafaff36f2.png" class="img-polaroid" title="kubernetes-1.23_.png" alt="kubernetes-1.23_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
“探索新边界（The Next Frontier）”主题体现出1.23版本中各项全新与渐进式增强功能，也希望整个社区的成员们能够秉持《星际迷航》中进取号船员们不断探索与成长的精神。<br>
<br>Kubernetes一直有着向《星际迷航》致敬的传统。早在谷歌内部的酝酿时期，Kubernetes的最初代号就是Project 7，代表着《星际迷航：航海家号》中的Borg人角色7/9。“探索新边界”也明显延续着《星际迷航》院线电影与电视剧集一以贯之的冒险精神。<br>
<br>“探索新边界”也是对我们项目SIG发布章程的重申，即“确保通过统一的社区成员小组支持漫长时间表中的发布流程。”我们携手新加入的发布团队成员共同发展社区，也很荣幸能成为很多新朋友们在开源领域的第一个家。<br>
<br>参考链接：<a href="https://kubernetes.io/blog/2015/04/borg-predecessor-to-kubernetes/" rel="nofollow" target="_blank">https://kubernetes.io/blog/201 ... etes/</a><br>
<br>参考链接：<a href="https://github.com/kubernetes/community/blob/master/sig-release/charter.md" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... er.md</a><br>
<br>Kubernetes 1.23发行版的徽标继续向《星际迷航》致敬，其中的每颗星星都代表着Kubernetes项目的一位领导者。而熟悉的进取号形象则代表着整个发行团队的团结与力量。<br>
<br>新版本徽标由Rey Lejano设计完成。<br>
<br><strong>原文链接：<a href="https://kubernetes.io/blog/2021/12/07/kubernetes-1-23-release-announcement/">Kubernetes 1.23: The Next Frontier</a></strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            