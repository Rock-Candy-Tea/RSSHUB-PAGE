
---
title: 'Kubernetes 1.23 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9720'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9720'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Kubernetes 1.23 正式发布，这是 2021 年的最后一个版本。此版本包含 47 项改进：11 项增强功能已升级到稳定版，17 项增强功能正在进入测试版，19 项增强功能正在进入 Alpha 版。此外，1 个功能已被弃用。</p> 
<p>该版本值得关注的更新内容包括：</p> 
<h3>弃用 FlexVolume</h3> 
<p>FlexVolume 已被弃用。树外 CSI 驱动是在 Kubernetes 中编写卷驱动的推荐方式。FlexVolume 驱动的维护者应该实现 CSI 驱动，并将 FlexVolume 的用户转移到 CSI。FlexVolume 的用户应将他们的工作负载转移到 CSI 驱动。</p> 
<h3>弃用 klog 的特定标志（flags）</h3> 
<p>为了简化代码库，在 Kubernetes 1.23 中的一些日志标志被标记为弃用。实现这些标志的代码将在未来的版本中被删除，所以这些标志的用户需要开始用一些替代的解决方案来替换被弃用的标志。</p> 
<h3>Kubernetes 发布过程中的 SLSA Level 1 合规性</h3> 
<p>Kubernetes 版本现在生成描述发布过程中的暂存和发布阶段的出处证明文件，软件产品在从一个阶段移交给下一个阶段时被验证。这最后一项工作完成了符合 SLSA（软件产品的供应链级别） 安全框架 Level 1 的要求。</p> 
<h3>IPv4/IPv6 <strong>双协议栈</strong>网络升级为 GA</h3> 
<p>IPv4/IPv6 双协议栈网络技术升级为 GA。从 1.21 开始，Kubernetes 集群默认支持双协议栈网络。在 1.23版本中， <code>IPv6DualStack</code> 被移除。双协议栈网络的使用不是强制性的。尽管集群被启用以支持双协议栈网络，但 Pod 和 Services 仍然默认为单协议栈。</p> 
<h3>HorizontalPodAutoscaler v2 升级为 GA</h3> 
<p>在 1.23 版本中，HorizontalPodAutoscaler API v2 升级为稳定版。HorizontalPodAutoscaler <code>autoscaling/v2beta2</code> API 已被弃用，转而使用新的 <code>autoscaling/v2</code> API，Kubernetes 项目推荐该 API 用于所有用例。</p> 
<h3>通用临时卷功能升级为 GA</h3> 
<p>通用临时卷功能（Generic Ephemeral Volume feature）在 1.23 版本中升级到了 GA。该功能允许任何支持动态配置的现有存储驱动器被用作临时卷，卷的生命周期与 Pod 绑定。所有用于卷配置的 StorageClass 参数和 PersistentVolumeClaims 支持的所有功能都支持。</p> 
<h3>跳过卷所有权更改（Skip Volume Ownership Change）升级到 GA</h3> 
<p>为 Pod 配置卷权限和所有权更改策略的功能在 1.23 中升级到了 GA。这允许用户跳过挂载时的递归权限变更，并加快了 Pod 的启动时间。</p> 
<h3>允许 CSI 驱动选择加入卷所有权和权限更改升级到 GA</h3> 
<p>允许 CSI 驱动程序声明支持基于 fsGroup 的权限的功能在 1.23 版本中升为 GA。</p> 
<h3>PodSecurity 升为 Beta 版</h3> 
<p>PodSecurity 转为 Beta 版本。 <code>PodSecurity</code> 取代了被废弃的 <code>PodSecurityPolicy</code> 准入控制器。 <code>PodSecurity</code> 是一个准入控制器，根据设定执行级别的特定命名空间标签，对命名空间中的 Pod 执行 Pod 安全标准。在 1.23 中， <code>PodSecurity</code> 默认是启用的。</p> 
<h3>容器运行时接口（CRI）v1 是默认值</h3> 
<p>Kubelet 现在支持 CRI v1 API，它现在是整个项目的默认值。如果容器运行时不支持 <code>v1</code> API，Kubernetes 将退回到 <code>v1alpha2</code> 实现。终端用户不需要进行任何中间操作，因为 <code>v1</code> 和 <code>v1alpha2</code> 在执行上没有区别。在未来的某个 Kubernetes 版本中，很可能会删除 v1alpha2。</p> 
<h3>结构化日志升级到 Beta 版</h3> 
<p>结构化日志达到了 Beta 的里程碑。来自 kubelet 和 kube-scheduler 的大部分日志信息已经被转换。我们鼓励用户尝试 JSON 输出或结构化文本格式的解析，并就可能的解决方案提供反馈。</p> 
<h3>简化了调度器的 <span>Multi-point </span>插件配置</h3> 
<p>kube-scheduler 正在为插件增加一个新的、简化的配置字段，允许在一个地方启用多个扩展点。新的 <code>multiPoint</code> 插件字段旨在为管理员简化大多数调度器的设置。通过 <code>multiPoint</code> 启用的插件将自动为它们实现的每个单独的扩展点注册。</p> 
<h3><strong>CSI Migration</strong> 更新</h3> 
<p>CSI 迁移使现有的树内存储插件（如 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubernetes.io%2Fgce-pd" target="_blank">kubernetes.io/gce-pd</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubernetes.io%2Faws-ebs%25EF%25BC%2589%25E8%25A2%25AB%25E7%259B%25B8%25E5%25BA%2594%25E7%259A%2584" target="_blank">kubernetes.io/aws-ebs）被相应的</a> CSI 驱动所取代。如果 CSI Migration 工作正常，Kubernetes 终端用户应该不会注意到有什么不同。迁移后，Kubernetes 用户可以继续使用现有界面依赖树内存储插件的所有功能。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2021%2F12%2F07%2Fkubernetes-1-23-release-announcement%2F" target="_blank">https://kubernetes.io/blog/2021/12/07/kubernetes-1-23-release-announcement/</a></p>
                                        </div>
                                      
</div>
            