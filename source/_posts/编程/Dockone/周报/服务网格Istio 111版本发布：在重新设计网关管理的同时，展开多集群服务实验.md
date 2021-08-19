
---
title: '服务网格Istio 1.11版本发布：在重新设计网关管理的同时，展开多集群服务实验'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=6756'
author: Dockone
comments: false
date: 2021-08-19 07:07:43
thumbnail: 'https://picsum.photos/400/300?random=6756'
---

<div>   
<br>服务网格Istio开发团队正式推出最新1.11版本。除了提供网关注入功能之外，新版本还在多集群Kubernetes服务的实现方面做出大胆实验。<br>
<br>在添加网关注入功能之后，管理员能够更轻松地管理并升级作为Istio与其他实例间接口的网关。更新之后，网关将获得与边车（sidecar）代理相同的管理方式，因此全局代理配置也将作用于网关，进而减少组件间的配置漂移。<br>
<br>多集群服务支持则源自Kubernetes项目中的同名API。只要通过ENABLE_MCS_SERVICE_DISCOVERY标记启用这项功能，则默认情况下将只能从同一集群之内发现服务端点。如果要求各端点通过网格接受访问，则需要首先导出端点（也可以使用automation自动化标记）。<br>
<br>除此之外，与上个版本相比，Istio开发团队还对CNI插件进行了大量测试并完善了文档资源。CNI的作用在于替代当前用于设置Pod网络流量重新定向，而且尚处于beta阶段的istio-init容器。去年推出的用于改善集群管理员与用户之间关注点分离问题的外部控制平面，在1.11版本中也升级至beta阶段。<br>
<br>Istio的命令行工具istioctl现在为istioctl命名空间、Kubernetes Pod及服务提供自动补全功能；同时也为uninstall命令新增了-dry-run标记，确保用户在实际卸载之前切实理解将要删除的内容。新的-workloadIP标记则可帮助设置Sidecar代理用于自动注册工作负载条目的工作负载IP。<br>
<br>经验丰富的Istio用户可能需要略微调整自己的工作流程，以便在新增外部控制平面的远程集群上安装网格。由于istiodRemote组件在新版本中配备了各集群所需要的全部charts，用户现在可以通过新的values.global.configCluster变量启用集群配置所需的各类资源。<br>
<br>部分团队会依靠主机标头回退对Prometheus中的入站流量指标进行destination_service标记，但在新版本中这项功能不再默认选定，因此你需要手动启用。另一项新优化允许多个域共享同一虚拟主机，这可能会改变与特定虚拟主机相匹配的过滤条件的输出结果。如果发生意外问题，请在Istiod部署上设置PILOT_ENABLE_ROUTE_COLLAPSE_OPTIMIZATION=false作为临时解决办法。<br>
<br>感兴趣的朋友请<a href="https://istio.io/latest/news/releases/1.11.x/announcing-1.11/change-notes/">点击此处</a>参阅Istio网站上的发行版说明信息。此项目由谷歌、IBM及Lyft团队合作开发，并于2017年首次公开发布。去年，谷歌将Istio商标授予Open Usage Commons，这也让Istio项目获得广泛关注。此举不仅让Istio迎来了加入云原生计算基金会（CNCF）的希望，这条开源发展路线也得到IBM的大力支持。Open Usage Commons是由谷歌创立的开源组织，目标是为“开源项目提供商标管理与指导意见”。<br>
<br><strong>原文链接：<a href="https://devclass.com/2021/08/16/service-mesh-istio-1-11-reworks-gateway-management-experiments-with-multi-cluster-services/">Service mesh Istio 1.11 reworks gateway management, experiments with multi-cluster services</a></strong>
                                
                                                              
</div>
            