
---
title: '如何基于K3s构建云原生边缘基础设施？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210517130621251.png'
author: Dockone
comments: false
date: 2021-05-18 08:03:18
thumbnail: 'https://img-blog.csdnimg.cn/20210517130621251.png'
---

<div>   
<br><blockquote><br>作者简介 <br>
  Janakiram MSV是Janakiram & Associates的首席分析师，也是国际信息技术学院的兼职教师。他也是Google Qualified  Developer、亚马逊认证解决方案架构师、亚马逊认证开发者、亚马逊认证SysOps管理员和微软认证Azure专业人员。<br>
  <br>
  <br>Janakiram是云原生计算基金会的大使，也是首批Kubernetes认证管理员和Kubernetes认证应用开发者之一。他曾在微软、AWS、Gigaom Research等知名公司工作。</blockquote>Kubernetes正在通过数据中心寻找一条从云端通向边缘的道路。早些时候，Kubernetes还被认为是运行在公有云上的超大规模工作负载。近几年，企业开始将Kubernetes应用于数据中心。它最终成为在混合云和多云环境中运行工作负载的一致和统一的基础设施层。<br>
<br>物联网和人工智能的兴起，促使业界在将计算能力向数据靠拢，这就成为边缘计算层。<br>
<br>边缘计算是边缘设备和云端/数据中心的中介。它基于业务逻辑提取设备的数据，同时提供实时分析。它作为数据源头和云之间的通道，极大地降低了由于往返云端可能出现的延迟。由于边缘可以对需要发送到云端的数据进行处理和过滤，因此也降低了带宽成本。最后，边缘计算将通过本地处理和存储帮助企业实现数据的本地化和对数据的管理主权。<br>
<br><img src="https://img-blog.csdnimg.cn/20210517130621251.png" alt="图片" referrerpolicy="no-referrer"><br>
<br>边缘计算充分利用了云平台的基础服务，如数据提取、数据处理、流分析、存储、设备管理和机器学习推理等。<br>
<br>Kubernetes正迅速成为边缘计算的首选基础设施。敏捷性、规模性和安全性的承诺正逐渐延伸到边缘基础设施。基于CI/CD和GitOps的现代软件交付机制使得管理运行在边缘的应用程序变得容易。部署在边缘位置的数万个Kubernetes集群由Anthos、Arc、Tanzu和Rancher等管理平台进行管理。<br>
<br><h2>边缘的构成</h2>其实，计划在边缘运行Kubernetes的用户没有太多选择，他们必须从云原生生态系统中最好的开源软件和商业软件中组装堆栈。<br>
<br><img src="https://img-blog.csdnimg.cn/20210517130631727.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br>商业化的Kubernetes发行版并没有针对在资源有限的环境中进行优化。部署在边缘的Kubernetes发行版应该占用较小的空间，并且不会影响API的一致性和兼容性。<br>
<br>边缘的存储是基础设施的关键构件之一。它必须支持处理非结构化数据集、NoSQL数据库和共享文件系统的有状态工作负载的各种需求。它应该具有定期拍摄数据快照并将其存储在云中的能力。而迁移和灾难恢复等高级能力可以使边缘计算层具有弹性。<br>
<br>网络层应该为运行在边缘的工作负载提供安全性和隔离性。在大多数情况下，边缘基础设施由多个组共享。例如，在智慧建筑的用例中，同一个边缘集群可能为每个楼层运行工作负载。集群管理员应该能够应用网络策略，防止在一个命名空间中运行的应用程序访问另一个命名空间的应用数据。并且网络层应通过入侵检测和声明式策略提供安全性。<br>
<br><img src="https://img-blog.csdnimg.cn/20210517130641545.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<br><h2>K3s：为边缘而生的Kubernetes发行版</h2>由Rancher Labs推出的K3s是一款轻量级Kubernetes发行版，它针对边缘场景进行了优化。虽然K3s是Kubernetes的简化版、迷你版，但它并没有影响API的一致性和功能。<br>
<br>从Kubectl到Helm再到Kustomize，几乎所有的云原生生态中的工具都能无缝地与K3s一起工作。事实上，K3s是一个经过CNCF认证的、符合要求的Kubernetes发行版，可以在生产环境中部署。最近，K3s捐献给CNCF，成为一个沙箱项目。几乎所有在基于上游Kubernetes发行版的集群中运行的工作负载都能保证在K3s集群上运行。<br>
<br>K3s通过协调运行在边缘的基础设施和工作负载，有效地解决了计算层的问题。<br>
<br><h2>Portworx：容器云原生存储层</h2>Portworx是一个为容器和微服务构建的软件定义存储平台。它将多个存储设备抽象化，为云原生应用暴露出一个统一的、覆盖式的存储层。<br>
<br>Portworx的关键差异化因素之一是容器颗粒式存储卷。与其他存储产品不同，Portworx暴露了一个统一的覆盖存储层，可以适应不同的用例。例如，存储管理员可以定义一个旨在以高可用模式运行NoSQL数据库的存储类，同时为共享卷创建另一个存储类。这两种方案都是基于同一个存储后端，而不需要管理两个不同的存储层。<br>
<br>边缘计算层处理各种工作负载，包括流媒体、数据存储、分析、复杂事件处理和AI推理。其中一些工作负载需要专用的存储卷，而其他工作负载则需要共享卷。例如，服务于AI推理的多个pod将共享同一个填入ML模型的存储卷。同时，message broker需要一个专用卷来持久化消息。<br>
<br>Portworx通过统一的方法消除了管理多个存储层的痛苦。其中的一些功能，如快照、调度备份、迁移、集成RBAC和预测性容量规划等，使得Portworx成为边缘的理想选择。<br>
<br>目前，最新版本Portworx 2.6已经正式支持K3s。<br>
<br><h2>Calico项目：边缘的安全网络</h2>Calico为Kubernetes带来了细粒度的网络策略。虽然Kubernetes对基于角色的访问控制（RBAC）有广泛的支持，但上游Kubernetes发行版中提供的默认网络栈并不支持细粒度的网络策略。Calico通过允许和拒绝Kubernetes工作负载的流量来提供细粒度的控制。<br>
<br>对于DevOps来说，将应用程序有逻辑地分组到Kubernetes命名空间中是一种常见的做法。在边缘计算场景中，一个K3s集群可能会运行多个由命名空间分隔的工作负载。Calico通过声明式策略实现了命名空间的强隔离。通过这些策略，传感器流式传输的数据将被授权的应用提取和处理。<br>
<br>Calico带有内置的入侵检测功能，可以识别可疑的活动。多云联邦的多集群管理，使其能够从统一的管理界面中轻松管理分布式边缘基础设施。并且只要对安装过程稍作修改，Calico就可以轻松地与K3s集成。<br>
<br>在接下来的教程中，我将带大家了解如何配置基于K3s、Portworx和Calico的边缘集群。在随后的部分中，我们还将探索利用该解决方案堆栈进行AIoT部署。保持关注哟！<br>
<blockquote><br>原文链接：<br>
  <a href="https://thenewstack.io/how-k3s-portworx-and-calico-can-serve-as-a-foundation-of-cloud-native-edge-infrastructure/" rel="nofollow" target="_blank">https://thenewstack.io/how-k3s ... ture/</a></blockquote>
                                
                                                              
</div>
            